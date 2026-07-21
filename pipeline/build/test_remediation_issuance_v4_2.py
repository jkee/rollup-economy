#!/usr/bin/env python3

from datetime import date
import importlib.util
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest import mock


HERE = Path(__file__).resolve().parent


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


issuer = _load("remediation_issuer_v4_2_tests", "issue_campaign_v4_2.py")
writer = _load("remediation_writer_v4_2_tests", "guarded_write_v4_2.py")
fixtures = _load("remediation_v4_2_fixtures", "test_issue_campaign_v4_2.py")


class RemediationIssuanceV42Tests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.RepositoryFixture()
        self.patches = []
        for module in (issuer, writer.issuer):
            self.patches.extend([
                mock.patch.object(module, "_load_freeze_contract", return_value=SimpleNamespace(
                    validate=mock.Mock(return_value=[]))),
                mock.patch.object(module, "_verify_git_authority", return_value=None),
                mock.patch.object(module, "_verify_live_ci", return_value=None),
            ])
        for patch in self.patches:
            patch.start()
        self.review_authority_patch = mock.patch.object(
            issuer, "_validate_predecessor_review", return_value=({}, {}))
        self.review_authority_patch.start()
        self.plan, self.credentials = issuer.issue_with_credentials(
            self.fixture.root, "regression", "remediation-tests", date.today().isoformat(),
            self.fixture.freeze_path, self.fixture.plan_path, *self.fixture.issuance_args())
        self.entry = self.plan["entries"][0]
        self.campaign_path = "pipeline/v4_2/campaigns/predecessor.json"
        self.fixture.write_json(self.campaign_path, {"fixture": True})

    def tearDown(self):
        self.review_authority_patch.stop()
        for patch in reversed(self.patches):
            patch.stop()
        self.fixture.close()

    def _source(self, relative, value):
        content = value if isinstance(value, bytes) else issuer.canonical_bytes(value)
        self.fixture.write_bytes(relative, content)
        return relative

    def _write(self, kind, source):
        return writer.guarded_write(
            self.fixture.root, self.fixture.plan_path, self.entry["entry_id"], kind,
            issuer._claim_execution(self.entry, kind)["codex_task_path"],
            self.credentials[self.entry["entry_id"]][kind], source)

    def _materialize_predecessor(self, outcome="reject", paths=None):
        record_source = self._source("scratch/predecessor-record.json", {
            "naics": self.entry["naics"], "title": self.entry["title"],
            "run_meta": {"run_id": self.entry["run_id"]}})
        self._write("record", record_source)
        findings = [] if paths is None else [{
            "finding_id": "F1", "severity": "material", "input_paths": paths,
            "source_ids": [], "fingerprint": "a" * 64,
        }]
        review_source = self._source("scratch/predecessor-review.json", {
            "entry_id": self.entry["entry_id"], "outcome": outcome, "findings": findings})
        self._write("review", review_source)
        return (
            issuer.sha256_file(self.fixture.root / self.entry["planned_outputs"]["record"]),
            issuer.sha256_file(self.fixture.root / self.entry["planned_outputs"]["review"]),
        )

    def test_rejected_remediable_attempt_1_issues_one_attempt_2_and_replay_fails(self):
        run_sha, review_sha = self._materialize_predecessor(
            paths=["inputs.implementation_realization.r2",
                   "inputs.commercial_retention.c4"])
        output = "pipeline/v4_2/plans/remediation.json"
        plan = issuer.issue_remediation(
            self.fixture.root, self.fixture.plan_path, self.campaign_path,
            self.entry["entry_id"],
            run_sha, review_sha, output)
        second = plan["entries"][-1]
        self.assertEqual(second["attempt"], 2)
        self.assertEqual(second["remediates_run_id"], self.entry["run_id"])
        self.assertEqual(second["remediable_paths"], [
            "inputs.commercial_retention.c4", "inputs.implementation_realization.r2"])
        _loaded, errors = issuer.validate_issued_plan(self.fixture.root, output)
        self.assertEqual(errors, [])
        with self.assertRaisesRegex(issuer.IssueError, "overwrite"):
            issuer.issue_remediation(
                self.fixture.root, self.fixture.plan_path, self.campaign_path,
                self.entry["entry_id"],
                run_sha, review_sha, output)
        with self.assertRaisesRegex(issuer.IssueError, "original attempt-1"):
            issuer.build_remediation_issuance(
                self.fixture.root, output, self.campaign_path,
                second["entry_id"], run_sha, review_sha)

    def test_unreviewed_wrong_digest_publishable_and_nonremediable_fail(self):
        with self.assertRaisesRegex(issuer.IssueError, "reserved|predecessor|required file"):
            issuer.build_remediation_issuance(
                self.fixture.root, self.fixture.plan_path, self.campaign_path,
                self.entry["entry_id"],
                "0" * 64, "0" * 64)
        run_sha, review_sha = self._materialize_predecessor(
            paths=["inputs.implementation_investment.k1"])
        with self.assertRaisesRegex(issuer.IssueError, "run digest"):
            issuer.build_remediation_issuance(
                self.fixture.root, self.fixture.plan_path, self.campaign_path,
                self.entry["entry_id"],
                "0" * 64, review_sha)
        review = issuer.load_json(self.fixture.root / self.entry["planned_outputs"]["review"])
        review["outcome"] = "publishable"
        with self.assertRaisesRegex(issuer.IssueError, "rejected"):
            issuer._remediable_paths(review) if review["outcome"] == "reject" else (_ for _ in ()).throw(
                issuer.IssueError("attempt 2 requires rejected review"))
        review["outcome"] = "reject"
        review["findings"][0]["input_paths"] = ["inputs.unlinked_v4_1_field"]
        with self.assertRaisesRegex(issuer.IssueError, "not a remediable"):
            issuer._remediable_paths(review)

        review["findings"][0]["input_paths"] = ["inputs.recognized_revenue"]
        review["findings"][0]["severity"] = "fatal_mechanics"
        with self.assertRaisesRegex(issuer.IssueError, "terminal"):
            issuer._remediable_paths(review)

    def test_exact_review_authority_rejects_schema_or_computed_outcome_mismatch(self):
        self.review_authority_patch.stop()
        plan_file = self.fixture.root / self.fixture.plan_path
        campaign_entry = {"entry_id": self.entry["entry_id"]}
        manifest = {
            "issuance_plan": {"path": self.fixture.plan_path,
                              "sha256": issuer.sha256_file(plan_file),
                              "byte_length": plan_file.stat().st_size},
            "entries": [campaign_entry],
        }
        self.fixture.write_json(self.campaign_path, manifest)
        review = {"outcome": "reject"}
        valid = SimpleNamespace(
            validate_manifest=lambda _manifest, _root: [],
            review_errors=lambda _review, _entry, _manifest, _root: [],
            computed_outcome=lambda _entry, _review: "reject",
        )
        loaded, selected = issuer._validate_predecessor_review(
            self.fixture.root, self.campaign_path, self.fixture.plan_path,
            self.entry, review, campaign_module=valid)
        self.assertEqual(loaded, manifest)
        self.assertEqual(selected, campaign_entry)
        invalid_schema = SimpleNamespace(
            validate_manifest=lambda _manifest, _root: [],
            review_errors=lambda *_args: ["schema/artifact/execution mismatch"],
            computed_outcome=lambda _entry, _review: "reject",
        )
        with self.assertRaisesRegex(issuer.IssueError, "schema/artifact/execution"):
            issuer._validate_predecessor_review(
                self.fixture.root, self.campaign_path, self.fixture.plan_path,
                self.entry, review, campaign_module=invalid_schema)
        wrong_outcome = SimpleNamespace(
            validate_manifest=lambda _manifest, _root: [],
            review_errors=lambda *_args: [],
            computed_outcome=lambda _entry, _review: "publishable",
        )
        with self.assertRaisesRegex(issuer.IssueError, "computed reject"):
            issuer._validate_predecessor_review(
                self.fixture.root, self.campaign_path, self.fixture.plan_path,
                self.entry, review, campaign_module=wrong_outcome)


if __name__ == "__main__":
    unittest.main()
