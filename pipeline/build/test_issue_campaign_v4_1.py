#!/usr/bin/env python3

from datetime import date
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock


HERE = Path(__file__).resolve().parent


def load_module():
    spec = importlib.util.spec_from_file_location(
        "issue_campaign_v4_1_tests", HERE / "issue_campaign_v4_1.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


issuer = load_module()
freeze_test_spec = importlib.util.spec_from_file_location(
    "freeze_contract_shared_fixture", HERE / "test_freeze_contract_v4_1.py")
freeze_test_module = importlib.util.module_from_spec(freeze_test_spec)
freeze_test_spec.loader.exec_module(freeze_test_module)
REAL_VERIFY_GIT_AUTHORITY = issuer._verify_git_authority
REAL_VERIFY_LIVE_CI = issuer._verify_live_ci
REAL_GIT = issuer._git
REAL_GIT_BYTES = issuer._git_bytes


class RepositoryFixture:
    def __init__(self, omit_frozen=()):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.omit_frozen = set(omit_frozen)
        self.freeze_path = issuer.FREEZE_MANIFEST_PATH
        self.plan_path = "pipeline/v4_1/plans/test-plan.json"
        self._build()

    def close(self):
        self.temp.cleanup()

    def write_bytes(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def write_json(self, relative, value):
        return self.write_bytes(relative, issuer.canonical_bytes(value))

    def git(self, *args):
        result = subprocess.run(
            ["git", "-C", str(self.root), *args], check=False,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        )
        if result.returncode:
            raise AssertionError("git %s failed: %s" % (args, result.stderr))
        return result.stdout.strip()

    def _build(self):
        self.git("init", "-q")
        self.git("config", "user.email", "issuer-tests@example.com")
        self.git("config", "user.name", "Issuer Tests")
        codes = list(issuer.CANARY_CODES) + list(issuer.HOLDOUT_CODES)
        rows = []
        for code in codes:
            title = "Synthetic Industry %s" % code
            rows.append({"naics": code, "title": title})
            dataset_path = "pipeline/datasets/v4_1/%s.json" % code
            dataset = {
                "dataset_version": "4.1", "snapshot_id": "fixture-%s" % code,
                "naics": code, "title": title,
            }
            self.write_json(dataset_path, dataset)
            dataset_sha = issuer.sha256_file(self.root / dataset_path)
            self.write_json("pipeline/specs_v4_1/%s.json" % code, {
                "spec_version": "4.1", "naics": code, "title": title,
                "dataset_snapshot": {"path": dataset_path, "sha256": dataset_sha},
            })
            self.write_bytes(
                "pipeline/prompts_v4_1/%s.md" % code,
                ("frozen prompt for %s\n" % code).encode("utf-8"),
            )
        self.write_json(issuer.TARGETS_PATH, {"codes": rows})
        self.write_json(issuer.HOLDOUT_PATH, {"selected_codes": list(issuer.HOLDOUT_CODES)})
        self.write_json(issuer.REGRESSION_PATH, {
            "membership_version": "v4.1-regression-1",
            "purpose": "Disclosed development regression set; not holdout evidence",
            "selected_codes": list(issuer.CANARY_CODES),
            "selection_rule": "The five viewed v4.0 canary codes",
        })
        for key, relative in issuer.TOOLCHAIN_PATHS.items():
            if relative == "pipeline/build/issue_campaign_v4_1.py":
                content = (HERE / "issue_campaign_v4_1.py").read_bytes()
            elif relative == issuer.MODEL_ROUTES_PATH:
                self.write_json(relative, {
                    "route_version": "v4.1-model-routes-1",
                    "research": {"fleet": "fixture-terra", "golden": "fixture-sol"},
                    "review": {"all": "fixture-sol"},
                    "execution": {
                        "fork_policy": "none", "issued_by_task_path": "/root",
                        "research_role": "research", "review_role": "reviewer",
                    },
                })
                continue
            else:
                content = ("frozen %s\n" % key).encode("utf-8")
            self.write_bytes(relative, content)
        self.git("add", ".")
        self.git("commit", "-qm", "frozen inputs")

        required = set(issuer.TOOLCHAIN_PATHS.values()) | {
            issuer.TARGETS_PATH, issuer.HOLDOUT_PATH, issuer.REGRESSION_PATH,
        }
        for code in codes:
            required.update({
                "pipeline/prompts_v4_1/%s.md" % code,
                "pipeline/specs_v4_1/%s.json" % code,
                "pipeline/datasets/v4_1/%s.json" % code,
            })
        required -= self.omit_frozen
        files = []
        for relative in sorted(required, key=lambda value: value.encode("utf-8")):
            path = self.root / relative
            files.append({
                "path": relative,
                "byte_length": path.stat().st_size,
                "sha256": issuer.sha256_file(path),
            })
        manifest = {
            "files": files,
            "manifest_version": issuer.FREEZE_VERSION,
            "root_sha256": issuer._root_sha256(files),
        }
        self.write_json(self.freeze_path, manifest)
        self.git("add", self.freeze_path)
        self.git("commit", "-qm", "freeze manifest")
        commit_sha = self.git("rev-parse", "HEAD")
        self.git("tag", "-a", "v4.1-freeze-test", "-m", "v4.1 root %s" % manifest["root_sha256"])
        tag_sha = self.git("rev-parse", "refs/tags/v4.1-freeze-test^{tag}")
        common = {
            "receipt_version": "v4.1-authorization-receipt-1",
            "root_sha256": manifest["root_sha256"],
            "manifest_sha256": issuer.sha256_file(self.root / self.freeze_path),
            "commit_sha": commit_sha,
        }
        self.commit_receipt = "authorization/commit.json"
        self.tag_receipt = "authorization/tag.json"
        self.ci_receipt = "authorization/ci.json"
        self.write_json(self.commit_receipt, {
            **common, "kind": "commit", "committed_at": "2026-01-01T00:00:00Z",
        })
        self.write_json(self.tag_receipt, {
            **common, "kind": "tag", "tag_name": "v4.1-freeze-test",
            "tag_object_sha": tag_sha, "annotated": True, "signed": True,
            "signature_verified": True, "signer_identity": "jkee",
            "tagged_at": "2026-01-01T00:01:00Z",
        })
        self.write_json(self.ci_receipt, {
            **common, "kind": "ci", "tag_name": "v4.1-freeze-test",
            "workflow_path": ".github/workflows/v4-1-freeze.yml",
            "provider": "github-actions", "github_owner": "jkee",
            "github_repository": "rollup-economy", "workflow_id": 789,
            "run_id": 123, "run_attempt": 1,
            "run_api_url": "https://api.github.com/repos/jkee/rollup-economy/actions/runs/123",
            "run_html_url": "https://github.com/jkee/rollup-economy/actions/runs/123",
            "artifacts_api_url": "https://api.github.com/repos/jkee/rollup-economy/actions/runs/123/artifacts",
            "event": "push", "conclusion": "success",
            "run_started_at": "2026-01-01T00:02:00Z",
            "run_updated_at": "2026-01-01T00:03:00Z",
            "artifact_id": 456, "artifact_name": "v4.1-freeze-" + commit_sha,
            "artifact_api_url": "https://api.github.com/repos/jkee/rollup-economy/actions/artifacts/456",
            "artifact_archive_download_url": "https://api.github.com/repos/jkee/rollup-economy/actions/artifacts/456/zip",
            "artifact_digest": "sha256:" + "c" * 64,
            "artifact_created_at": "2026-01-01T00:02:30Z",
            "artifact_updated_at": "2026-01-01T00:03:00Z",
            "issued_at": "2026-01-01T00:04:00Z",
        })

    def issuance_args(self):
        return (self.commit_receipt, self.tag_receipt, self.ci_receipt)


class IssueCampaignV41Tests(unittest.TestCase):
    def setUp(self):
        self.fixture = RepositoryFixture()
        self.run_date = date.today().isoformat()
        self.contract_module = SimpleNamespace(validate=mock.Mock(return_value=[]))
        self.contract_patch = mock.patch.object(
            issuer, "_load_freeze_contract", return_value=self.contract_module)
        self.git_authority_patch = mock.patch.object(
            issuer, "_verify_git_authority", return_value=None)
        self.live_ci_patch = mock.patch.object(issuer, "_verify_live_ci", return_value=None)
        self.contract_patch.start()
        self.git_authority_patch.start()
        self.live_ci_patch.start()

    def tearDown(self):
        self.live_ci_patch.stop()
        self.git_authority_patch.stop()
        self.contract_patch.stop()
        self.fixture.close()

    def issue(self, scope="canary"):
        return issuer.issue(
            self.fixture.root, scope, "test-campaign", self.run_date,
            self.fixture.freeze_path, self.fixture.plan_path,
            *self.fixture.issuance_args(),
        )

    def test_canary_plan_and_envelopes_are_exact_and_create_no_research(self):
        plan = self.issue("canary")
        self.assertEqual(plan["plan_version"], issuer.PLAN_VERSION)
        self.assertEqual(plan["scope"], "canary")
        self.assertEqual(plan["membership"]["codes"], list(issuer.CANARY_CODES))
        self.assertEqual(
            plan["membership"]["regression_manifest"]["path"], issuer.REGRESSION_PATH)
        self.assertIsNone(plan["membership"]["holdout_manifest"])
        self.assertEqual(plan["plan_sha256"], issuer._plan_digest(plan))
        self.assertEqual(plan["freeze"]["root_sha256"], load_freeze(self.fixture)["root_sha256"])
        self.assertEqual(plan["freeze"]["git_commit"], self.fixture.git("rev-parse", "HEAD"))
        self.assertEqual(
            plan["authorization"]["ci_run_html_url"],
            "https://github.com/jkee/rollup-economy/actions/runs/123")
        self.assertEqual(
            plan["authorization"]["ci_artifact_api_url"],
            "https://api.github.com/repos/jkee/rollup-economy/actions/artifacts/456")
        self.assertEqual(plan["authorization"]["ci_artifact_digest"], "sha256:" + "c" * 64)
        for name in ("commit_receipt", "tag_receipt", "ci_receipt"):
            receipt = plan["authorization"][name]
            self.assertEqual(
                issuer.sha256_file(self.fixture.root / receipt["path"]), receipt["sha256"])
        self.assertEqual(len(plan["entries"]), 5)
        tasks = [
            entry[role]["codex_task_path"]
            for entry in plan["entries"]
            for role in ("research_execution", "review_execution")
        ]
        self.assertEqual(len(tasks), len(set(tasks)))
        for entry in plan["entries"]:
            self.assertEqual(entry["research_execution"], {
                "issued_by_task_path": "/root",
                "codex_task_path": entry["research_execution"]["codex_task_path"],
                "fork_policy": "none", "role": "research",
                "model_id": "fixture-terra",
            })
            self.assertEqual(entry["attempt"], 1)
            self.assertIsNone(entry["remediates_run_id"])
            envelope_ref = entry["execution_envelope"]
            envelope_path = self.fixture.root / envelope_ref["path"]
            self.assertTrue(envelope_path.is_file())
            self.assertEqual(issuer.sha256_file(envelope_path), envelope_ref["sha256"])
            envelope = issuer.load_json(envelope_path)
            self.assertEqual(envelope["prompt_sha256"], entry["frozen_inputs"]["assembled_prompt"]["sha256"])
            self.assertEqual(envelope["spec_sha256"], entry["frozen_inputs"]["industry_spec"]["sha256"])
            self.assertEqual(envelope["dataset_sha256"], entry["frozen_inputs"]["dataset"]["sha256"])
            for key in ("packet", "record", "memo", "review"):
                self.assertFalse((self.fixture.root / entry["planned_outputs"][key]).exists())
        self.assertEqual(
            (self.fixture.root / self.fixture.plan_path).read_bytes(),
            issuer.canonical_bytes(plan),
        )

    def test_holdout_uses_exact_frozen_membership_and_routes(self):
        plan = self.issue("holdout")
        self.assertEqual(plan["membership"]["codes"], list(issuer.HOLDOUT_CODES))
        self.assertIsNone(plan["membership"]["regression_manifest"])
        self.assertEqual(
            plan["membership"]["holdout_manifest"]["path"], issuer.HOLDOUT_PATH)
        for entry in plan["entries"]:
            self.assertEqual(entry["kind"], "fleet")
            self.assertEqual(entry["research_execution"]["model_id"], "fixture-terra")
            self.assertEqual(entry["review_execution"]["model_id"], "fixture-sol")
            self.assertEqual(entry["review_execution"]["fork_policy"], "none")
            self.assertRegex(entry["review_execution"]["codex_task_path"], r"^/root/review_")

    def test_validate_issued_plan_reconstructs_every_binding_and_envelope(self):
        issued = self.issue("canary")
        plan, errors = issuer.validate_issued_plan(
            self.fixture.root, self.fixture.plan_path, expected_scope="canary")
        self.assertEqual(errors, [])
        self.assertEqual(plan, issued)

        envelope = self.fixture.root / plan["entries"][0]["execution_envelope"]["path"]
        envelope.write_bytes(envelope.read_bytes() + b"\n")
        _plan, errors = issuer.validate_issued_plan(
            self.fixture.root, self.fixture.plan_path, expected_scope="canary")
        self.assertTrue(any("envelope bytes differ" in item for item in errors))

        self.fixture.close()
        self.fixture = RepositoryFixture()
        plan = self.issue("canary")
        plan["entries"][0]["review_execution"]["codex_task_path"] = "/root/review_tampered"
        plan["plan_sha256"] = issuer._plan_digest(plan)
        (self.fixture.root / self.fixture.plan_path).write_bytes(issuer.canonical_bytes(plan))
        _plan, errors = issuer.validate_issued_plan(
            self.fixture.root, self.fixture.plan_path, expected_scope="canary")
        self.assertTrue(any("differs from its exact reconstructed" in item for item in errors))

    def test_global_task_namespace_rejects_cross_role_and_cross_entry_collisions(self):
        plan, _envelopes = issuer.build_issuance(
            self.fixture.root, "canary", "test-campaign", self.run_date,
            self.fixture.freeze_path, *self.fixture.issuance_args(),
        )
        entries = json.loads(json.dumps(plan["entries"]))
        entries[0]["review_execution"]["codex_task_path"] = \
            entries[1]["research_execution"]["codex_task_path"]
        with self.assertRaisesRegex(issuer.IssueError, "globally unique"):
            issuer._validate_global_task_paths(entries)

        entries = json.loads(json.dumps(plan["entries"]))
        entries[2]["review_execution"]["codex_task_path"] = \
            entries[3]["review_execution"]["codex_task_path"]
        with self.assertRaisesRegex(issuer.IssueError, "globally unique"):
            issuer._validate_global_task_paths(entries)

    def test_model_routes_and_regression_membership_are_frozen_authorities(self):
        routes = issuer.load_json(self.fixture.root / issuer.MODEL_ROUTES_PATH)
        routes["execution"]["fork_policy"] = "all"
        (self.fixture.root / issuer.MODEL_ROUTES_PATH).write_bytes(issuer.canonical_bytes(routes))
        with self.assertRaisesRegex(issuer.IssueError, "stale|uncommitted"):
            issuer.build_issuance(
                self.fixture.root, "canary", "test-campaign", self.run_date,
                self.fixture.freeze_path, *self.fixture.issuance_args(),
            )

        self.fixture.close()
        self.fixture = RepositoryFixture()
        membership = issuer.load_json(self.fixture.root / issuer.REGRESSION_PATH)
        membership["selected_codes"] = list(reversed(issuer.CANARY_CODES))
        path = self.fixture.root / issuer.REGRESSION_PATH
        path.write_bytes(issuer.canonical_bytes(membership))
        with self.assertRaisesRegex(issuer.IssueError, "stale|uncommitted"):
            issuer.build_issuance(
                self.fixture.root, "canary", "test-campaign", self.run_date,
                self.fixture.freeze_path, *self.fixture.issuance_args(),
            )

    def test_authorization_validator_is_mandatory_and_receipts_are_exactly_bound(self):
        self.contract_module.validate.return_value = ["CI receipt is not externally verified"]
        with self.assertRaisesRegex(issuer.IssueError, "CI receipt is not externally verified"):
            self.issue()
        self.assertFalse((self.fixture.root / self.fixture.plan_path).exists())

        self.contract_module.validate.return_value = []
        plan = self.issue()
        call = self.contract_module.validate.call_args
        self.assertEqual(call.args[0], (self.fixture.root / issuer.FREEZE_CONTRACT_PATH).resolve())
        self.assertEqual(call.args[1], (self.fixture.root / self.fixture.freeze_path).resolve())
        self.assertEqual(call.args[2], (self.fixture.root / self.fixture.commit_receipt).resolve())
        self.assertEqual(call.args[3], (self.fixture.root / self.fixture.tag_receipt).resolve())
        self.assertEqual(call.args[4], (self.fixture.root / self.fixture.ci_receipt).resolve())
        self.assertEqual(call.args[5], self.fixture.root.resolve())
        for field, relative in (
                ("commit_receipt", self.fixture.commit_receipt),
                ("tag_receipt", self.fixture.tag_receipt),
                ("ci_receipt", self.fixture.ci_receipt)):
            ref = plan["authorization"][field]
            path = self.fixture.root / relative
            self.assertEqual(ref["sha256"], issuer.sha256_file(path))
            self.assertEqual(ref["byte_length"], path.stat().st_size)

    def test_real_freeze_contract_shared_fixture_integrates_with_issuer(self):
        # This test deliberately stops the broad validator mocks used by the
        # small issuer fixture.  Only the public GitHub API response is injected.
        self.live_ci_patch.stop()
        self.git_authority_patch.stop()
        self.contract_patch.stop()
        try:
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                fixture = freeze_test_module.Fixture(root)
                targets = issuer.load_json(root / issuer.TARGETS_PATH)
                titles = {row["naics"]: row["title"] for row in targets["codes"]}
                for code in (*issuer.CANARY_CODES, *issuer.HOLDOUT_CODES):
                    dataset_path = "pipeline/datasets/v4_1/%s.json" % code
                    issuer_path = root / dataset_path
                    issuer_path.write_bytes(issuer.canonical_bytes({
                        "dataset_version": "4.1", "snapshot_id": "shared-" + code,
                        "naics": code, "title": titles[code],
                    }))
                    (root / "pipeline/specs_v4_1" / (code + ".json")).write_bytes(
                        issuer.canonical_bytes({
                            "spec_version": "4.1", "naics": code, "title": titles[code],
                            "dataset_snapshot": {
                                "path": dataset_path, "sha256": issuer.sha256_file(issuer_path),
                            },
                        }))
                    (root / "pipeline/prompts_v4_1" / (code + ".md")).write_text(
                        "shared frozen prompt %s\n" % code, encoding="utf-8")
                for relative in (issuer.TOOLCHAIN_PATHS["issuer"], issuer.FREEZE_VALIDATOR_PATH):
                    (root / relative).write_bytes((HERE / Path(relative).name).read_bytes())

                key = root / "signing-key"
                subprocess.run(
                    ["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-f", str(key)],
                    check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                )
                public_key = (root / "signing-key.pub").read_text(encoding="utf-8").strip()
                (root / "pipeline/v4_1/allowed_signers").write_text(
                    "jkee %s\n" % public_key, encoding="utf-8")
                fixture.refresh_manifest()

                def git(*args):
                    result = subprocess.run(
                        ["git", "-C", str(root), *args], check=True,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    return result.stdout.strip()

                git("init", "-q")
                git("config", "user.email", "issuer-integration@example.com")
                git("config", "user.name", "Issuer Integration")
                git("config", "gpg.format", "ssh")
                git("config", "user.signingkey", str(key))
                git("config", "gpg.ssh.allowedSignersFile", "pipeline/v4_1/allowed_signers")
                git("add", ".")
                git("commit", "-qm", "exact frozen commit")
                commit_sha = git("rev-parse", "HEAD")
                tag_name = "v4.1-freeze-test"
                git("tag", "-s", tag_name, "-m", "freeze root %s" % fixture.manifest["root_sha256"])
                tag_sha = git("rev-parse", "refs/tags/%s^{tag}" % tag_name)
                manifest_sha = issuer.sha256_file(fixture.manifest_path)
                common = {
                    "receipt_version": "v4.1-authorization-receipt-1",
                    "root_sha256": fixture.manifest["root_sha256"],
                    "manifest_sha256": manifest_sha, "commit_sha": commit_sha,
                }
                commit = {**common, "kind": "commit", "committed_at": "2026-01-01T00:00:00Z"}
                tag = {
                    **common, "kind": "tag", "tag_name": tag_name,
                    "tag_object_sha": tag_sha, "annotated": True, "signed": True,
                    "signature_verified": True, "signer_identity": "jkee",
                    "tagged_at": "2026-01-01T00:01:00Z",
                }
                ci = {
                    **common, "kind": "ci", "tag_name": tag_name,
                    "provider": "github-actions", "github_owner": "jkee",
                    "github_repository": "rollup-economy",
                    "workflow_path": issuer.FREEZE_WORKFLOW_PATH, "workflow_id": 789,
                    "run_id": 123, "run_attempt": 1,
                    "run_api_url": issuer.GITHUB_API_ROOT + "/actions/runs/123",
                    "run_html_url": issuer.GITHUB_WEB_ROOT + "/actions/runs/123",
                    "artifacts_api_url": issuer.GITHUB_API_ROOT + "/actions/runs/123/artifacts",
                    "event": "push", "conclusion": "success",
                    "run_started_at": "2026-01-01T00:02:00Z",
                    "run_updated_at": "2026-01-01T00:03:00Z",
                    "artifact_id": 456, "artifact_name": "v4.1-freeze-" + commit_sha,
                    "artifact_api_url": issuer.GITHUB_API_ROOT + "/actions/artifacts/456",
                    "artifact_archive_download_url": issuer.GITHUB_API_ROOT + "/actions/artifacts/456/zip",
                    "artifact_digest": "sha256:" + "c" * 64,
                    "artifact_created_at": "2026-01-01T00:02:30Z",
                    "artifact_updated_at": "2026-01-01T00:03:00Z",
                    "issued_at": "2026-01-01T00:04:00Z",
                }
                commit_path, tag_path, ci_path = (
                    root / "commit-receipt.json", root / "tag-receipt.json", root / "ci-receipt.json")
                for path, value in ((commit_path, commit), (tag_path, tag), (ci_path, ci)):
                    path.write_bytes(issuer.canonical_bytes(value))

                run = {
                    "id": 123, "workflow_id": 789, "run_attempt": 1,
                    "html_url": ci["run_html_url"], "artifacts_url": ci["artifacts_api_url"],
                    "status": "completed", "conclusion": "success", "event": "push",
                    "head_sha": commit_sha, "head_branch": tag_name,
                    "name": issuer.FREEZE_WORKFLOW_NAME,
                    "path": issuer.FREEZE_WORKFLOW_PATH + "@refs/tags/" + tag_name,
                    "created_at": "2026-01-01T00:01:30Z",
                    "run_started_at": ci["run_started_at"], "updated_at": ci["run_updated_at"],
                }
                artifact = {
                    "id": 456, "name": ci["artifact_name"], "expired": False,
                    "expires_at": "2099-01-01T00:00:00Z", "digest": ci["artifact_digest"],
                    "url": ci["artifact_api_url"],
                    "archive_download_url": ci["artifact_archive_download_url"],
                    "created_at": ci["artifact_created_at"],
                    "updated_at": ci["artifact_updated_at"],
                    "workflow_run": {"id": 123, "head_sha": commit_sha},
                }
                responses = {
                    ci["run_api_url"]: run,
                    ci["artifacts_api_url"]: {"total_count": 1, "artifacts": [artifact]},
                }
                plan = issuer.issue(
                    root, "canary", "shared-integration", self.run_date,
                    issuer.FREEZE_MANIFEST_PATH, "pipeline/v4_1/plans/integration.json",
                    str(commit_path), str(tag_path), str(ci_path),
                    ci_fetcher=lambda url: responses[url],
                )
                self.assertEqual(plan["authorization"]["ci_artifact_digest"], ci["artifact_digest"])
                validated, errors = issuer.validate_issued_plan(
                    root, "pipeline/v4_1/plans/integration.json",
                    expected_scope="canary", ci_fetcher=lambda url: responses[url],
                )
                self.assertEqual(errors, [])
                self.assertEqual(validated, plan)
        finally:
            self.contract_patch.start()
            self.git_authority_patch.start()
            self.live_ci_patch.start()

    def test_actual_git_objects_not_receipt_booleans_authorize_issuance(self):
        manifest = load_freeze(self.fixture)
        commit = issuer.load_json(self.fixture.root / self.fixture.commit_receipt)
        tag = issuer.load_json(self.fixture.root / self.fixture.tag_receipt)

        def allow_fixture_signature(root, *args):
            if args == ("verify-tag", "v4.1-freeze-test"):
                return ""
            return REAL_GIT(root, *args)

        with mock.patch.object(issuer, "_git", side_effect=allow_fixture_signature):
            REAL_VERIFY_GIT_AUTHORITY(
                self.fixture.root, self.fixture.freeze_path, manifest, commit, tag)

        wrong_commit = dict(commit)
        wrong_commit["commit_sha"] = self.fixture.git("rev-parse", "HEAD^")
        with self.assertRaisesRegex(issuer.IssueError, "current HEAD"):
            REAL_VERIFY_GIT_AUTHORITY(
                self.fixture.root, self.fixture.freeze_path, manifest, wrong_commit, tag)

        def hide_root(root, *args):
            if args == ("cat-file", "-p", tag["tag_object_sha"]):
                return b"object " + commit["commit_sha"].encode("ascii") + b"\n\nnot the root\n"
            return REAL_GIT_BYTES(root, *args)

        with mock.patch.object(issuer, "_git_bytes", side_effect=hide_root), \
                self.assertRaisesRegex(issuer.IssueError, "tag message"):
            REAL_VERIFY_GIT_AUTHORITY(
                self.fixture.root, self.fixture.freeze_path, manifest, commit, tag)

        member = self.fixture.root / issuer.TOOLCHAIN_PATHS["methodology"]
        frozen_member = member.read_bytes()
        member.write_text("bad descendant bytes\n", encoding="utf-8")
        self.fixture.git("add", issuer.TOOLCHAIN_PATHS["methodology"])
        self.fixture.git("commit", "-qm", "bad descendant")
        member.write_bytes(frozen_member)
        self.fixture.git("add", issuer.TOOLCHAIN_PATHS["methodology"])
        self.fixture.git("commit", "-qm", "repair descendant")
        with self.assertRaisesRegex(issuer.IssueError, "current HEAD"):
            REAL_VERIFY_GIT_AUTHORITY(
                self.fixture.root, self.fixture.freeze_path, manifest, commit, tag)

    def test_external_receipts_are_supported_and_validation_is_toctou_closed(self):
        with tempfile.TemporaryDirectory() as receipt_directory:
            external = []
            for relative in self.fixture.issuance_args():
                target = Path(receipt_directory) / Path(relative).name
                target.write_bytes((self.fixture.root / relative).read_bytes())
                external.append(str(target))
            plan = issuer.issue(
                self.fixture.root, "canary", "external-receipts", self.run_date,
                self.fixture.freeze_path, self.fixture.plan_path, *external,
            )
            self.assertEqual(
                plan["authorization"]["ci_receipt"]["path"], external[2])

        self.fixture.close()
        self.fixture = RepositoryFixture()

        def mutate_ci(*args):
            args[4].write_bytes(args[4].read_bytes() + b"\n")
            return []

        self.contract_module.validate.side_effect = mutate_ci
        with self.assertRaisesRegex(issuer.IssueError, "changed during validation"):
            self.issue()
        self.assertFalse((self.fixture.root / self.fixture.plan_path).exists())

    def test_live_github_ci_proof_is_exact_and_fails_closed(self):
        commit = issuer.load_json(self.fixture.root / self.fixture.commit_receipt)
        tag = issuer.load_json(self.fixture.root / self.fixture.tag_receipt)
        ci = issuer.load_json(self.fixture.root / self.fixture.ci_receipt)
        api_run = issuer.GITHUB_API_ROOT + "/actions/runs/123"
        api_artifacts = api_run + "/artifacts"
        run = {
            "id": 123, "workflow_id": 789, "run_attempt": 1,
            "html_url": "https://github.com/jkee/rollup-economy/actions/runs/123",
            "artifacts_url": api_artifacts, "status": "completed",
            "conclusion": "success", "event": "push",
            "head_sha": commit["commit_sha"], "head_branch": tag["tag_name"],
            "name": issuer.FREEZE_WORKFLOW_NAME,
            "path": issuer.FREEZE_WORKFLOW_PATH + "@refs/tags/" + tag["tag_name"],
            "created_at": "2026-01-01T00:00:00Z",
            "run_started_at": ci["run_started_at"],
            "updated_at": ci["run_updated_at"],
        }
        artifact = {
            "id": 456, "name": "v4.1-freeze-" + commit["commit_sha"],
            "expired": False, "expires_at": "2099-01-01T00:00:00Z",
            "digest": ci["artifact_digest"],
            "url": ci["artifact_api_url"],
            "archive_download_url": ci["artifact_archive_download_url"],
            "created_at": ci["artifact_created_at"],
            "updated_at": ci["artifact_updated_at"],
            "workflow_run": {"id": 123, "head_sha": commit["commit_sha"]},
        }
        listing = {"total_count": 1, "artifacts": [artifact]}

        def fetch(url):
            return {api_run: run, api_artifacts: listing}[url]

        REAL_VERIFY_LIVE_CI(ci, commit, tag, fetch_json=fetch)

        for field, bad_value in (
                ("status", "in_progress"), ("event", "workflow_dispatch"),
                ("head_sha", "0" * 40), ("head_branch", "other-tag"),
                ("path", ".github/workflows/other.yml"), ("name", "other workflow"),
                ("updated_at", "2026-01-01T00:01:30Z")):
            bad_run = dict(run)
            bad_run[field] = bad_value
            with self.assertRaises(issuer.IssueError):
                REAL_VERIFY_LIVE_CI(
                    ci, commit, tag,
                    fetch_json=lambda url, value=bad_run: value if url == api_run else listing,
                )

        for field, bad_value in (
                ("expired", True), ("digest", "sha256:" + "0" * 64),
                ("name", "other-artifact"), ("expires_at", "2020-01-01T00:00:00Z")):
            bad_artifact = dict(artifact)
            bad_artifact[field] = bad_value
            bad_listing = {"total_count": 1, "artifacts": [bad_artifact]}
            with self.assertRaises(issuer.IssueError):
                REAL_VERIFY_LIVE_CI(
                    ci, commit, tag,
                    fetch_json=lambda url, value=bad_listing: run if url == api_run else value,
                )

        with self.assertRaisesRegex(issuer.IssueError, "outside the exact GitHub API"):
            issuer._github_get_json("https://example.com/redirect")
        with self.assertRaisesRegex(issuer.IssueError, "redirect"):
            issuer._RejectRedirects().redirect_request(None, None, 302, "moved", {}, "https://evil")
        with self.assertRaisesRegex(issuer.IssueError, "live GitHub CI verification failed"):
            REAL_VERIFY_LIVE_CI(
                ci, commit, tag,
                fetch_json=lambda _url: (_ for _ in ()).throw(OSError("offline")),
            )

    def test_refuses_plan_envelope_or_research_output_overwrite(self):
        self.issue()
        with self.assertRaisesRegex(issuer.IssueError, "refusing to overwrite"):
            self.issue()

        other = RepositoryFixture()
        try:
            run_id = "%s_canary_v4_1_238220_a1" % self.run_date
            packet = other.root / "pipeline/v4_1/packets/238220" / (run_id + ".json")
            packet.parent.mkdir(parents=True, exist_ok=True)
            packet.write_text("already exists", encoding="utf-8")
            with self.assertRaisesRegex(issuer.IssueError, "already exists before issuance"):
                issuer.issue(
                    other.root, "canary", "test-campaign", self.run_date,
                    other.freeze_path, other.plan_path,
                    *other.issuance_args(),
                )
        finally:
            other.close()

    def test_rejects_unlisted_and_uncommitted_frozen_inputs(self):
        omitted = "pipeline/prompts_v4_1/238220.md"
        fixture = RepositoryFixture(omit_frozen={omitted})
        try:
            with self.assertRaisesRegex(issuer.IssueError, "not listed in freeze manifest"):
                issuer.build_issuance(
                    fixture.root, "canary", "test-campaign", self.run_date,
                    fixture.freeze_path, *fixture.issuance_args(),
                )
        finally:
            fixture.close()

        prompt = self.fixture.root / omitted
        prompt.write_text("unstaged change", encoding="utf-8")
        with self.assertRaisesRegex(issuer.IssueError, "stale|uncommitted"):
            issuer.build_issuance(
                self.fixture.root, "canary", "test-campaign", self.run_date,
                self.fixture.freeze_path, *self.fixture.issuance_args(),
            )

    def test_rejects_bad_freeze_root_and_spec_dataset_binding(self):
        freeze = load_freeze(self.fixture)
        freeze["root_sha256"] = "0" * 64
        (self.fixture.root / self.fixture.freeze_path).write_bytes(issuer.canonical_bytes(freeze))
        with self.assertRaisesRegex(issuer.IssueError, "root_sha256|uncommitted"):
            issuer.build_issuance(
                self.fixture.root, "canary", "test-campaign", self.run_date,
                self.fixture.freeze_path, *self.fixture.issuance_args(),
            )

        self.fixture.close()
        self.fixture = RepositoryFixture()
        spec_path = self.fixture.root / "pipeline/specs_v4_1/238220.json"
        spec = issuer.load_json(spec_path)
        spec["dataset_snapshot"]["sha256"] = "0" * 64
        spec_path.write_bytes(issuer.canonical_bytes(spec))
        self.fixture.git("add", "pipeline/specs_v4_1/238220.json")
        self.fixture.git("commit", "-qm", "bad spec binding")
        # A newly committed file still differs from the older frozen digest.
        with self.assertRaisesRegex(issuer.IssueError, "stale"):
            issuer.build_issuance(
                self.fixture.root, "canary", "test-campaign", self.run_date,
                self.fixture.freeze_path, *self.fixture.issuance_args(),
            )

    def test_atomic_failure_rolls_back_new_envelopes_and_plan(self):
        real_create = issuer._atomic_create
        calls = {"count": 0}

        def fail_second(root, relative, content):
            calls["count"] += 1
            if calls["count"] == 2:
                raise OSError("synthetic atomic failure")
            return real_create(root, relative, content)

        with mock.patch.object(issuer, "_atomic_create", side_effect=fail_second):
            with self.assertRaisesRegex(OSError, "synthetic atomic failure"):
                self.issue()
        self.assertFalse((self.fixture.root / self.fixture.plan_path).exists())
        envelopes = list((self.fixture.root / "pipeline/v4_1/envelopes").rglob("*.json"))
        self.assertEqual(envelopes, [])

    def test_output_race_before_plan_commit_rolls_back_all_envelopes(self):
        real_create = issuer._atomic_create
        raced = {"path": None}

        def inject_packet(root, relative, content):
            real_create(root, relative, content)
            if raced["path"] is None and "/envelopes/" in relative:
                run_id = "%s_canary_v4_1_238220_a1" % self.run_date
                packet_relative = "pipeline/v4_1/packets/238220/%s.json" % run_id
                packet = root / packet_relative
                packet.parent.mkdir(parents=True, exist_ok=True)
                packet.write_text("appeared during issuance", encoding="utf-8")
                raced["path"] = packet

        with mock.patch.object(issuer, "_atomic_create", side_effect=inject_packet):
            with self.assertRaisesRegex(issuer.IssueError, "already exists before issuance"):
                self.issue()
        self.assertIsNotNone(raced["path"])
        self.assertTrue(raced["path"].exists())
        self.assertFalse((self.fixture.root / self.fixture.plan_path).exists())
        self.assertEqual(
            list((self.fixture.root / "pipeline/v4_1/envelopes").rglob("*.json")), [])


def load_freeze(fixture):
    return issuer.load_json(fixture.root / fixture.freeze_path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
