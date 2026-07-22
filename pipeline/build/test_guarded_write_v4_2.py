#!/usr/bin/env python3

from datetime import date
import importlib.util
from pathlib import Path
import json
import os
import threading
from types import SimpleNamespace
import unittest
from unittest import mock


HERE = Path(__file__).resolve().parent


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


writer = _load("guarded_writer_v4_2_tests", "guarded_write_v4_2.py")
fixtures = _load("guarded_writer_v4_2_fixtures", "test_issue_campaign_v4_2.py")


class GuardedWriteV42Tests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.RepositoryFixture()
        self.run_date = date.today().isoformat()
        self.patches = []
        for module in (fixtures.issuer, writer.issuer):
            self.patches.extend([
                mock.patch.object(module, "_load_freeze_contract", return_value=SimpleNamespace(
                    validate=mock.Mock(return_value=[]))),
                mock.patch.object(module, "_verify_git_authority", return_value=None),
                mock.patch.object(module, "_verify_live_ci", return_value=None),
            ])
        for patch in self.patches:
            patch.start()
        self.plan, self.credentials = fixtures.issuer.issue_with_credentials(
            self.fixture.root, "regression", "claim-tests", self.run_date,
            self.fixture.freeze_path, self.fixture.plan_path, *self.fixture.issuance_args())
        self.entry = self.plan["entries"][0]
        public_bytes = (self.fixture.root / self.fixture.plan_path).read_bytes()
        for token in self.credentials[self.entry["entry_id"]].values():
            self.assertNotIn(token.encode("utf-8"), public_bytes)
            self.assertEqual(len(token) >= 32, True)
            for path in self.fixture.root.rglob("*"):
                if path.is_file():
                    self.assertNotIn(token.encode("utf-8"), path.read_bytes(), str(path))

    def tearDown(self):
        for patch in reversed(self.patches):
            patch.stop()
        self.fixture.close()

    def source(self, name, value):
        relative = "scratch/%s" % name
        content = value if isinstance(value, bytes) else fixtures.issuer.canonical_bytes(value)
        self.fixture.write_bytes(relative, content)
        return relative

    def write(self, kind, source, owner=None, **kwargs):
        execution = fixtures.issuer._claim_execution(self.entry, kind)
        return writer.guarded_write(
            self.fixture.root, self.fixture.plan_path, self.entry["entry_id"], kind,
            owner or execution["codex_task_path"],
            self.credentials[self.entry["entry_id"]][kind], source, **kwargs)

    def test_all_four_owners_consume_to_hash_bound_receipts(self):
        sources = {
            "packet": self.source("packet.json", {"naics": self.entry["naics"],
                                                    "title": self.entry["title"]}),
            "record": self.source("record.json", {"naics": self.entry["naics"],
                                                    "title": self.entry["title"],
                                                    "run_meta": {"run_id": self.entry["run_id"]}}),
            "memo": self.source("memo.md", b"bounded memo\n"),
            "review": self.source("review.json", {"entry_id": self.entry["entry_id"]}),
        }
        for kind, source in sources.items():
            receipt = self.write(kind, source)
            ref = self.entry["output_reservations"][kind]
            output = self.fixture.root / self.entry["planned_outputs"][kind]
            self.assertFalse((self.fixture.root / ref["path"]).exists())
            self.assertFalse((self.fixture.root / ref["lock_path"]).exists())
            self.assertTrue((self.fixture.root / ref["claim_receipt_path"]).is_file())
            self.assertEqual(receipt["artifact"]["sha256"], fixtures.issuer.sha256_file(output))
            self.assertEqual(receipt["authorized_task_path"],
                             fixtures.issuer._claim_execution(self.entry, kind)["codex_task_path"])
        _plan, errors = writer.issuer.validate_issued_plan(
            self.fixture.root, self.fixture.plan_path)
        self.assertEqual(errors, [])

    def test_wrong_owner_wrong_kind_and_replay_fail_without_stealing_claim(self):
        packet = self.source("packet.json", {"naics": self.entry["naics"],
                                              "title": self.entry["title"]})
        with self.assertRaisesRegex(writer.issuer.IssueError, "not authorized"):
            self.write("packet", packet, owner=self.entry["review_execution"]["codex_task_path"])
        self.assertTrue((self.fixture.root /
                         self.entry["output_reservations"]["packet"]["path"]).exists())
        with self.assertRaisesRegex(writer.issuer.IssueError, "claim token"):
            writer.guarded_write(
                self.fixture.root, self.fixture.plan_path, self.entry["entry_id"], "packet",
                self.entry["research_execution"]["codex_task_path"], "spoofed-token", packet)
        with self.assertRaisesRegex(writer.issuer.IssueError, "review artifact identity"):
            self.write("review", packet)
        self.write("packet", packet)
        with self.assertRaisesRegex(writer.issuer.IssueError, "not valid|consumed"):
            self.write("packet", packet)

    def test_race_has_exactly_one_winner(self):
        packet = self.source("packet.json", {"naics": self.entry["naics"],
                                              "title": self.entry["title"]})
        claimed = threading.Event()
        release = threading.Event()
        results = []

        def first():
            try:
                self.write("packet", packet, after_claim=lambda: (claimed.set(), release.wait(5)))
                results.append("won")
            except Exception as exc:  # pragma: no cover - diagnostic payload
                results.append(exc)

        thread = threading.Thread(target=first)
        thread.start()
        self.assertTrue(claimed.wait(5))
        with self.assertRaisesRegex(writer.issuer.IssueError, "not valid|in progress|consumed"):
            self.write("packet", packet)
        release.set()
        thread.join(5)
        self.assertEqual(results, ["won"])

    def test_artifact_or_receipt_tamper_invalidates_plan(self):
        packet = self.source("packet.json", {"naics": self.entry["naics"],
                                              "title": self.entry["title"]})
        self.write("packet", packet)
        output = self.fixture.root / self.entry["planned_outputs"]["packet"]
        output.write_bytes(b"tampered")
        _plan, errors = writer.issuer.validate_issued_plan(self.fixture.root, self.fixture.plan_path)
        self.assertTrue(any("claim receipt differs" in item for item in errors), errors)

    def test_formatted_json_is_accepted_and_exact_bytes_are_bound(self):
        values = {
            "packet": {"naics": self.entry["naics"], "title": self.entry["title"]},
            "record": {"naics": self.entry["naics"], "title": self.entry["title"],
                       "run_meta": {"run_id": self.entry["run_id"]}},
            "review": {"entry_id": self.entry["entry_id"]},
        }
        for kind, value in values.items():
            content = (json.dumps(value, indent=2) + "\n").encode("utf-8")
            source = self.source("formatted-%s.json" % kind, content)
            receipt = self.write(kind, source)
            self.assertEqual(receipt["artifact"]["sha256"],
                             fixtures.issuer.sha256_bytes(content))

    def test_malformed_and_semantically_wrong_json_are_rejected(self):
        malformed = self.source("malformed.json", b'{"naics":')
        with self.assertRaisesRegex(writer.issuer.IssueError, "strict JSON"):
            self.write("packet", malformed)
        mismatch = self.source("mismatch.json", {"naics": "000000",
                                                  "title": self.entry["title"]})
        with self.assertRaisesRegex(writer.issuer.IssueError, "identity"):
            self.write("packet", mismatch)

    def test_claim_token_cli_accepts_pipe_and_rejects_regular_file_or_directory(self):
        packet = self.source("pipe-packet.json", {"naics": self.entry["naics"],
                                                   "title": self.entry["title"]})
        token = self.credentials[self.entry["entry_id"]]["packet"]
        read_fd, write_fd = os.pipe()
        os.write(write_fd, token.encode("utf-8"))
        os.close(write_fd)
        try:
            result = writer.main([
                "--repo-root", str(self.fixture.root), "--plan", self.fixture.plan_path,
                "--entry-id", self.entry["entry_id"], "--artifact-kind", "packet",
                "--authorized-task-path", self.entry["research_execution"]["codex_task_path"],
                "--claim-token-fd", str(read_fd), "--source", packet])
        finally:
            os.close(read_fd)
        self.assertEqual(result, 0)

        regular = os.open(self.fixture.root / "scratch/token.txt",
                          os.O_CREAT | os.O_RDWR, 0o600)
        try:
            with self.assertRaisesRegex(writer.issuer.IssueError, "FIFO or socket"):
                writer._require_private_pipe_fd(regular)
        finally:
            os.close(regular)
        directory = os.open(self.fixture.root / "scratch", os.O_RDONLY)
        try:
            with self.assertRaisesRegex(writer.issuer.IssueError, "FIFO or socket"):
                writer._require_private_pipe_fd(directory)
        finally:
            os.close(directory)

    def test_recovery_restores_lock_only_or_completes_exact_output(self):
        kind = "packet"
        token = self.credentials[self.entry["entry_id"]][kind]
        execution = fixtures.issuer._claim_execution(self.entry, kind)
        ref = self.entry["output_reservations"][kind]
        reservation = self.fixture.root / ref["path"]
        lock = self.fixture.root / ref["lock_path"]
        output_relative = self.entry["planned_outputs"][kind]
        output = self.fixture.root / output_relative

        # Deterministic sentinel for a process killed after reservation.unlink().
        os.link(reservation, lock)
        reservation.unlink()
        result = writer.recover_claim(
            self.fixture.root, self.fixture.plan_path, self.entry["entry_id"], kind,
            execution["codex_task_path"], token)
        self.assertEqual(result["recovery"], "reservation_restored")
        self.assertTrue(reservation.is_file())
        self.assertFalse(lock.exists())

        # Deterministic sentinel for a kill after output create, before receipt.
        os.link(reservation, lock)
        reservation.unlink()
        content = fixtures.issuer.canonical_bytes({
            "naics": self.entry["naics"], "title": self.entry["title"]})
        fixtures.issuer._atomic_create(self.fixture.root, output_relative, content)
        receipt = writer.recover_claim(
            self.fixture.root, self.fixture.plan_path, self.entry["entry_id"], kind,
            execution["codex_task_path"], token)
        self.assertEqual(receipt["artifact"]["sha256"], fixtures.issuer.sha256_bytes(content))
        self.assertFalse(lock.exists())
        self.assertTrue((self.fixture.root / ref["claim_receipt_path"]).is_file())

    def test_recovery_rejects_tampered_or_conflicting_state_without_mutation(self):
        kind = "packet"
        token = self.credentials[self.entry["entry_id"]][kind]
        execution = fixtures.issuer._claim_execution(self.entry, kind)
        ref = self.entry["output_reservations"][kind]
        reservation = self.fixture.root / ref["path"]
        lock = self.fixture.root / ref["lock_path"]
        os.link(reservation, lock)
        reservation.unlink()
        lock.write_bytes(b"tampered-lock")
        before = lock.read_bytes()
        with self.assertRaisesRegex(writer.issuer.IssueError, "lock bytes"):
            writer.recover_claim(
                self.fixture.root, self.fixture.plan_path, self.entry["entry_id"], kind,
                execution["codex_task_path"], token)
        self.assertEqual(lock.read_bytes(), before)
        self.assertFalse(reservation.exists())


if __name__ == "__main__":
    unittest.main()
