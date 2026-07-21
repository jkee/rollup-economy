#!/usr/bin/env python3
"""Tests for the fail-closed v4.1 Section 14 completeness contract."""

import copy
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest


HERE = Path(__file__).resolve().parent


def load_module():
    spec = importlib.util.spec_from_file_location(
        "freeze_contract_v4_1_tests", HERE / "freeze_contract_v4_1.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


contract_module = load_module()


def write_json(path, value, *, canonical=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    if canonical:
        path.write_bytes(contract_module.canonical_bytes(value))
    else:
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


class Fixture:
    HOLDOUT = list(contract_module.HOLDOUT_CODES)

    def __init__(self, root):
        self.root = Path(root)
        self.contract = {
            "contract_version": contract_module.CONTRACT_VERSION,
            "methodology_version": "4.1",
            "freeze_manifest_version": contract_module.FREEZE_MANIFEST_VERSION,
            "canary_codes": list(contract_module.CANARY_CODES),
            "holdout_membership_path": contract_module.HOLDOUT_MEMBERSHIP_PATH,
            "required_exact_paths": sorted(contract_module.BASE_REQUIRED_PATHS),
            "issuance_tooling_paths": ["pipeline/build/issue_campaign_v4_1.py"],
            "sentinel_test_paths": [contract_module.REQUIRED_SENTINEL_TEST],
            "change_control_path": contract_module.CHANGE_CONTROL_PATH,
            "model_routes": copy.deepcopy(contract_module.MODEL_ROUTES),
        }
        self.contract_path = self.root / contract_module.DEFAULT_CONTRACT
        self.membership = {
            "regression_codes": sorted(contract_module.CANARY_CODES),
            "selected_codes": list(self.HOLDOUT),
            "bins": [
                {"bin": index, "selected_naics": code, "candidates": []}
                for index, code in enumerate(self.HOLDOUT, 1)
            ],
        }
        self._write_required_files()
        self.refresh_manifest()
        self.refresh_receipts()

    def _write_required_files(self):
        write_json(self.contract_path, self.contract)
        write_json(self.root / contract_module.HOLDOUT_MEMBERSHIP_PATH, self.membership)
        write_json(self.root / contract_module.CHANGE_CONTROL_PATH, contract_module.CHANGE_CONTROL)
        write_json(
            self.root / contract_module.REGRESSION_MEMBERSHIP_PATH,
            contract_module.REGRESSION_MEMBERSHIP,
        )
        write_json(self.root / contract_module.MODEL_ROUTES_PATH, contract_module.MODEL_ROUTES)
        allowed_signers = self.root / contract_module.ALLOWED_SIGNERS_PATH
        allowed_signers.parent.mkdir(parents=True, exist_ok=True)
        allowed_signers.write_text(
            "jkee ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFixtureFixtureFixtureFixture\n",
            encoding="utf-8",
        )
        write_json(
            self.root / contract_module.TARGET_MEMBERSHIP_PATH,
            {
                "version": "phase3-2026-07-20",
                "description": "fixture",
                "codes": [
                    {"naics": code, "title": "Fixture %s" % code, "golden": False}
                    for code in contract_module.TARGET_CODES
                ],
            },
        )
        paths = set(self.contract["required_exact_paths"])
        paths.update(self.contract["issuance_tooling_paths"])
        paths.update(self.contract["sentinel_test_paths"])
        paths.update(contract_module.BASE_SCHEMA_PATHS)
        for code in (*contract_module.CANARY_CODES, *self.HOLDOUT):
            paths.update({
                "pipeline/specs_v4_1/%s.json" % code,
                "pipeline/prompts_v4_1/%s.md" % code,
            })
        for code in contract_module.TARGET_CODES:
            paths.add("pipeline/datasets/v4_1/%s.json" % code)
        for relative in paths:
            path = self.root / relative
            if path.exists():
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("fixture for %s\n" % relative, encoding="utf-8")

    def refresh_manifest(self, omit=()):
        required = contract_module.required_paths(self.contract, self.membership, self.root)
        files = []
        for relative in required:
            if relative in omit:
                continue
            path = self.root / relative
            files.append({
                "path": relative,
                "byte_length": path.stat().st_size,
                "sha256": contract_module.sha256_file(path),
            })
        files.sort(key=lambda item: item["path"].encode("utf-8"))
        self.manifest = {
            "files": files,
            "manifest_version": contract_module.FREEZE_MANIFEST_VERSION,
            "root_sha256": contract_module.root_sha256(files),
        }
        self.manifest_path = self.root / contract_module.FREEZE_MANIFEST_PATH
        write_json(self.manifest_path, self.manifest, canonical=True)

    def refresh_receipts(self):
        manifest_digest = contract_module.sha256_file(self.manifest_path)
        common = {
            "receipt_version": contract_module.RECEIPT_VERSION,
            "root_sha256": self.manifest["root_sha256"],
            "manifest_sha256": manifest_digest,
            "commit_sha": "a" * 40,
        }
        self.commit = {
            **common, "kind": "commit", "committed_at": "2026-01-01T00:00:00Z",
        }
        self.tag = {
            **common, "kind": "tag", "tag_name": "v4.1-freeze-test",
            "tag_object_sha": "b" * 40, "annotated": True, "signed": True,
            "signature_verified": True,
            "signer_identity": contract_module.ALLOWED_SIGNER_PRINCIPAL,
            "tagged_at": "2026-01-01T00:01:00Z",
        }
        self.ci = {
            **common, "kind": "ci", "tag_name": "v4.1-freeze-test",
            "workflow_path": contract_module.FREEZE_CI_WORKFLOW_PATH,
            "provider": "github-actions",
            "github_owner": contract_module.GITHUB_OWNER,
            "github_repository": contract_module.GITHUB_REPOSITORY,
            "workflow_id": 789, "run_id": 123, "run_attempt": 1,
            "run_api_url": "https://api.github.com/repos/jkee/rollup-economy/actions/runs/123",
            "run_html_url": "https://github.com/jkee/rollup-economy/actions/runs/123",
            "artifacts_api_url": "https://api.github.com/repos/jkee/rollup-economy/actions/runs/123/artifacts",
            "event": "push", "conclusion": "success",
            "run_started_at": "2026-01-01T00:02:00Z",
            "run_updated_at": "2026-01-01T00:03:00Z",
            "artifact_id": 456,
            "artifact_name": "v4.1-freeze-" + common["commit_sha"],
            "artifact_api_url": "https://api.github.com/repos/jkee/rollup-economy/actions/artifacts/456",
            "artifact_archive_download_url": "https://api.github.com/repos/jkee/rollup-economy/actions/artifacts/456/zip",
            "artifact_digest": "sha256:" + "c" * 64,
            "artifact_created_at": "2026-01-01T00:02:30Z",
            "artifact_updated_at": "2026-01-01T00:03:00Z",
            "issued_at": "2026-01-01T00:04:00Z",
        }
        self.commit_path = self.root / "commit-receipt.json"
        self.tag_path = self.root / "tag-receipt.json"
        self.ci_path = self.root / "ci-receipt.json"
        write_json(self.commit_path, self.commit)
        write_json(self.tag_path, self.tag)
        write_json(self.ci_path, self.ci)

    def git_runner(self, root, args):
        stdout = b""
        tag_ref = "refs/tags/" + self.tag["tag_name"]
        commit_prefix = self.commit["commit_sha"] + ":"
        if args and args[0] == "show" and args[1].startswith(commit_prefix):
            relative = args[1][len(commit_prefix):]
            stdout = (self.root / relative).read_bytes()
        elif (args[:2] == ["cat-file", "-t"] and len(args) == 3
              and args[2].startswith(commit_prefix)):
            stdout = b"blob\n"
        elif args[:3] == ["cat-file", "-t", tag_ref]:
            stdout = b"tag\n"
        elif args[:2] == ["rev-parse", tag_ref]:
            stdout = (self.tag["tag_object_sha"] + "\n").encode()
        elif args[:2] == ["rev-parse", tag_ref + "^{commit}"]:
            stdout = (self.commit["commit_sha"] + "\n").encode()
        elif args[:3] == ["cat-file", "-p", tag_ref]:
            stdout = (
                "object %s\ntype commit\ntag %s\ntagger Fixture <fixture@example.com> 0 +0000\n\n"
                "freeze root %s\n-----BEGIN SSH SIGNATURE-----\nfixture\n"
                % (self.commit["commit_sha"], self.tag["tag_name"],
                   self.manifest["root_sha256"])
            ).encode()
        return SimpleNamespace(returncode=0, stdout=stdout, stderr=b"")

    def validate(self):
        return contract_module.validate(
            self.contract_path, self.manifest_path, self.commit_path,
            self.tag_path, self.ci_path, self.root, git_runner=self.git_runner,
        )


class FreezeContractV41Tests(unittest.TestCase):
    def test_complete_manifest_and_root_bound_receipts_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            self.assertEqual([], fixture.validate())

    def test_arbitrary_incomplete_file_list_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            fixture.refresh_manifest(omit={"V4_1_METHODOLOGY.md"})
            fixture.refresh_receipts()
            errors = fixture.validate()
            self.assertTrue(any("omits required paths" in item and "V4_1_METHODOLOGY.md" in item
                                for item in errors))

    def test_manifest_rejects_paths_outside_the_closed_plan(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            extra = fixture.root / "post-treatment-result.json"
            extra.write_text("{}\n", encoding="utf-8")
            fixture.manifest["files"].append({
                "path": "post-treatment-result.json",
                "byte_length": extra.stat().st_size,
                "sha256": contract_module.sha256_file(extra),
            })
            fixture.manifest["files"].sort(key=lambda item: item["path"].encode("utf-8"))
            fixture.manifest["root_sha256"] = contract_module.root_sha256(
                fixture.manifest["files"]
            )
            write_json(fixture.manifest_path, fixture.manifest, canonical=True)
            fixture.refresh_receipts()
            errors = fixture.validate()
            self.assertTrue(any("outside the closed freeze plan" in item for item in errors))

    def test_every_selected_canary_and_holdout_artifact_is_required(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            missing = "pipeline/prompts_v4_1/541922.md"
            fixture.refresh_manifest(omit={missing})
            fixture.refresh_receipts()
            errors = fixture.validate()
            self.assertTrue(any(missing in item for item in errors))

    def test_new_v41_schema_is_automatically_required(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            extra = fixture.root / "pipeline/build/schemas/new_v4_1.schema.json"
            extra.write_text("{}\n", encoding="utf-8")
            # Do not refresh the manifest: discovery must make the new schema mandatory.
            errors = fixture.validate()
            self.assertTrue(any("new_v4_1.schema.json" in item for item in errors))

    def test_contract_cannot_weaken_routes_cohorts_or_issuance(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            broken = copy.deepcopy(fixture.contract)
            broken["model_routes"]["reviewer_model_id"] = "another-model"
            broken["canary_codes"] = broken["canary_codes"][:-1]
            broken["issuance_tooling_paths"] = []
            errors = contract_module.contract_errors(broken)
            self.assertTrue(any("model_routes" in item for item in errors))
            self.assertTrue(any("canary_codes" in item for item in errors))
            self.assertTrue(any("issuance_tooling_paths" in item for item in errors))

    def test_change_control_is_exact_and_outcome_independent(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            changed = copy.deepcopy(contract_module.CHANGE_CONTROL)
            changed["allowed_new_version_triggers"].append("named_industry_verdict")
            write_json(fixture.root / contract_module.CHANGE_CONTROL_PATH, changed)
            fixture.refresh_manifest()
            fixture.refresh_receipts()
            errors = fixture.validate()
            self.assertTrue(any("change-control artifact differs" in item for item in errors))

    def test_each_authorization_receipt_must_bind_root_manifest_commit_and_tag(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            fixture.tag["root_sha256"] = "0" * 64
            write_json(fixture.tag_path, fixture.tag)
            self.assertTrue(any("tag receipt does not bind" in item for item in fixture.validate()))

            fixture.refresh_receipts()
            fixture.ci["tag_name"] = "other-tag"
            write_json(fixture.ci_path, fixture.ci)
            self.assertTrue(any("does not bind the commit and tag" in item for item in fixture.validate()))

    def test_unsigned_tag_and_unsuccessful_ci_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            fixture.tag["signature_verified"] = False
            write_json(fixture.tag_path, fixture.tag)
            self.assertTrue(any("signed, verified tag" in item for item in fixture.validate()))

            fixture.refresh_receipts()
            fixture.ci["conclusion"] = "failure"
            write_json(fixture.ci_path, fixture.ci)
            self.assertTrue(any("conclusion must be success" in item for item in fixture.validate()))

    def test_manifest_members_are_byte_and_digest_verified(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            path = fixture.root / "V4_1_METHODOLOGY.md"
            path.write_text("tampered\n", encoding="utf-8")
            errors = fixture.validate()
            self.assertTrue(any("byte length is stale" in item or "digest is stale" in item
                                for item in errors))

    def test_malformed_manifest_fails_closed_without_raising(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            fixture.manifest["files"][0]["path"] = ["not", "a", "path"]
            write_json(fixture.manifest_path, fixture.manifest, canonical=True)
            fixture.refresh_receipts()
            errors = fixture.validate()
            self.assertTrue(any("malformed file entries" in item for item in errors))

    def test_freeze_plan_derivation_is_complete_and_byte_deterministic(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            output = contract_module.write_or_check_freeze_plan(
                contract_module.DEFAULT_CONTRACT, fixture.root,
            )
            first = output.read_bytes()
            contract_module.write_or_check_freeze_plan(
                contract_module.DEFAULT_CONTRACT, fixture.root,
            )
            self.assertEqual(first, output.read_bytes())
            contract_module.write_or_check_freeze_plan(
                contract_module.DEFAULT_CONTRACT, fixture.root, check=True,
            )
            plan = json.loads(first)
            self.assertEqual(plan["files"], sorted(set(plan["files"])))
            dataset_paths = [
                path for path in plan["files"] if path.startswith("pipeline/datasets/v4_1/")
            ]
            selected_specs = [
                path for path in plan["files"] if path.startswith("pipeline/specs_v4_1/")
            ]
            selected_prompts = [
                path for path in plan["files"] if path.startswith("pipeline/prompts_v4_1/")
            ]
            self.assertEqual(63, len(dataset_paths))
            self.assertEqual(10, len(selected_specs))
            self.assertEqual(10, len(selected_prompts))

    def test_plan_derivation_rejects_missing_and_ambiguous_versioned_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            required = fixture.root / "pipeline/build/finalize_run_v4_1.py"
            required.unlink()
            with self.assertRaisesRegex(contract_module.ContractError, "ambiguous v4.1 build"):
                contract_module.derive_freeze_plan(contract_module.DEFAULT_CONTRACT, fixture.root)

        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            extra = fixture.root / "pipeline/build/unregistered_v4_1.py"
            extra.write_text("# ambiguous\n", encoding="utf-8")
            with self.assertRaisesRegex(contract_module.ContractError, "ambiguous v4.1 build"):
                contract_module.derive_freeze_plan(contract_module.DEFAULT_CONTRACT, fixture.root)

    def test_git_authorization_checks_committed_manifest_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)

            def mismatched_git(root, args):
                result = fixture.git_runner(root, args)
                if args and args[0] == "show":
                    return SimpleNamespace(returncode=0, stdout=b"other manifest", stderr=b"")
                return result

            errors = contract_module.authorization_errors(
                fixture.manifest, fixture.manifest_path, fixture.commit, fixture.tag,
                fixture.ci, root=fixture.root, git_runner=mismatched_git,
            )
            self.assertTrue(any("exact freeze manifest bytes" in item for item in errors))

    def test_git_authorization_uses_exact_frozen_signer_principal(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            (fixture.root / contract_module.ALLOWED_SIGNERS_PATH).write_text(
                "other ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFixture\n",
                encoding="utf-8",
            )
            fixture.refresh_manifest()
            fixture.refresh_receipts()
            errors = fixture.validate()
            self.assertTrue(any("principal must be exactly" in item for item in errors))

    def test_descendant_repair_cannot_replace_member_missing_from_authorized_commit(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            target = "V4_1_METHODOLOGY.md"
            object_spec = fixture.commit["commit_sha"] + ":" + target

            def ancestor_git(root, args):
                result = fixture.git_runner(root, args)
                if args == ["show", object_spec]:
                    return SimpleNamespace(
                        returncode=0, stdout=b"unfrozen ancestor bytes\n", stderr=b""
                    )
                return result

            errors = contract_module.authorization_errors(
                fixture.manifest, fixture.manifest_path, fixture.commit, fixture.tag,
                fixture.ci, root=fixture.root, git_runner=ancestor_git,
            )
            self.assertTrue(any(
                "authorized commit bytes differ" in item and target in item for item in errors
            ))


if __name__ == "__main__":
    unittest.main(verbosity=2)
