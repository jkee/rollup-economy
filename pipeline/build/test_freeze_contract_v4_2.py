#!/usr/bin/env python3
"""Tests for the fail-closed v4.2 §15 freeze completeness contract."""

import copy
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest


HERE = Path(__file__).resolve().parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


contract_module = load_module("freeze_contract_v4_2_tests", HERE / "freeze_contract_v4_2.py")
freeze_module = load_module("freeze_v4_2_tests", HERE / "freeze_v4_2.py")


def write_json(path, value, canonical=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    data = contract_module.canonical_bytes(value) if canonical else (
        json.dumps(value, indent=2) + "\n"
    ).encode()
    path.write_bytes(data)


class Fixture:
    def __init__(self, root):
        self.root = Path(root)
        self.git_calls = []
        self._write_tree()
        self.refresh_manifest()
        self.refresh_receipts()

    def _write_tree(self):
        paths = set(contract_module.BASE_PATHS)
        paths.update(contract_module.CRITICAL_BUILD_PATHS)
        paths.update(contract_module.REQUIRED_SCHEMAS)
        paths.update(contract_module.TEMPLATES)
        for relative in paths:
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            if not path.exists():
                path.write_text("fixture for %s\n" % relative, encoding="utf-8")
        builder_path = self.root / "pipeline/build/build_runtime_methodology_v4_2.py"
        builder_path.write_bytes((HERE / "build_runtime_methodology_v4_2.py").read_bytes())
        methodology = ["# AI Roll-Up Map — v4.2 Methodology", ""]
        for number in range(1, 16):
            methodology.extend(("## %d. Fixture section %d" % (number, number), "", "Fixture.", ""))
        (self.root / "V4_2_METHODOLOGY.md").write_text(
            "\n".join(methodology).rstrip() + "\n", encoding="utf-8",
        )
        runtime_builder = load_module("freeze_fixture_runtime_builder", builder_path)
        runtime_builder.write_or_check(
            self.root / "V4_2_METHODOLOGY.md",
            self.root / "V4_2_RUNTIME_METHODOLOGY.md",
        )
        targets = {
            "version": "phase3-2026-07-20", "description": "fixture",
            "codes": [
                {"naics": code, "title": "Fixture %s" % code, "golden": False}
                for code in contract_module.TARGET_CODES
            ],
        }
        write_json(self.root / contract_module.TARGETS_PATH, targets)
        write_json(
            self.root / contract_module.REGRESSION_PATH,
            contract_module.REGRESSION_MEMBERSHIP,
        )
        write_json(self.root / contract_module.ROUTES_PATH, contract_module.MODEL_ROUTES)
        write_json(
            self.root / contract_module.CHANGE_CONTROL_PATH, contract_module.CHANGE_CONTROL,
        )
        (self.root / contract_module.ALLOWED_SIGNERS_PATH).write_text(
            "jkee ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFixtureFixtureFixture\n",
            encoding="utf-8",
        )
        for code in contract_module.TARGET_CODES:
            source = self.root / "pipeline/datasets/derived" / (code + ".json")
            source.parent.mkdir(parents=True, exist_ok=True)
            write_json(source, {"naics": code, "source": True})
            old = self.root / "pipeline/datasets/v4_1" / (code + ".json")
            write_json(old, {"naics": code, "dataset_version": "4.1"})
            new = self.root / "pipeline/datasets/v4_2" / (code + ".json")
            write_json(new, {
                "dataset_version": "4.2", "naics": code,
                "provenance": {
                    "derivation_version": "normalize-v4.2-1",
                    "source_manifest_sha256": contract_module.sha256_file(source),
                },
            })
        digest_paths = [
            contract_module.TARGETS_PATH, contract_module.GOLDEN_PATH,
            "V4_2_METHODOLOGY.md",
        ]
        for code in contract_module.TARGET_CODES[:41]:
            digest_paths.extend((
                "pipeline/datasets/derived/%s.json" % code,
                "pipeline/datasets/v4_1/%s.json" % code,
            ))
        write_json(
            self.root / contract_module.HOLDOUT_PATH,
            {
                "selected_codes": list(contract_module.HOLDOUT_CODES),
                "bins": [
                    {"selected_naics": code} for code in contract_module.HOLDOUT_CODES
                ],
                "source_digests": [
                    {
                        "path": relative,
                        "byte_length": (self.root / relative).stat().st_size,
                        "sha256": contract_module.sha256_file(self.root / relative),
                    }
                    for relative in digest_paths
                ],
            },
        )
        for code in (*contract_module.REGRESSION_CODES, *contract_module.HOLDOUT_CODES):
            dataset_path = "pipeline/datasets/v4_2/%s.json" % code
            write_json(self.root / "pipeline/specs_v4_2" / (code + ".json"), {
                "spec_version": "4.2", "naics": code, "title": "Fixture %s" % code,
                "dataset_snapshot": {
                    "path": dataset_path,
                    "sha256": contract_module.sha256_file(self.root / dataset_path),
                },
                "methodology_snapshot": {
                    "path": "V4_2_RUNTIME_METHODOLOGY.md",
                    "sha256": contract_module.sha256_file(
                        self.root / "V4_2_RUNTIME_METHODOLOGY.md"
                    ),
                },
            })
            prompt = self.root / "pipeline/prompts_v4_2" / (code + ".md")
            prompt.parent.mkdir(parents=True, exist_ok=True)
            prompt.write_text("prompt %s\n" % code, encoding="utf-8")
        build, schemas, templates = contract_module._discover(self.root)
        self.contract = {
            "contract_version": contract_module.CONTRACT_VERSION,
            "methodology_version": "4.2",
            "freeze_manifest_version": contract_module.MANIFEST_VERSION,
            "regression_codes": list(contract_module.REGRESSION_CODES),
            "holdout_codes": list(contract_module.HOLDOUT_CODES),
            "base_paths": sorted(contract_module.BASE_PATHS),
            "versioned_build_paths": build,
            "versioned_schema_paths": schemas,
            "versioned_template_paths": templates,
            "model_routes": copy.deepcopy(contract_module.MODEL_ROUTES),
            "dataset_contract": {
                "count": 63, "directory": "pipeline/datasets/v4_2",
                "dataset_version": "4.2", "derivation_version": "normalize-v4.2-1",
                "legacy_source_directory": "pipeline/datasets/derived",
                "holdout_snapshot_directory": "pipeline/datasets/v4_1",
            },
            "selected_artifact_contract": {
                "count": 10, "spec_directory": "pipeline/specs_v4_2",
                "prompt_directory": "pipeline/prompts_v4_2",
                "codes": sorted((*contract_module.REGRESSION_CODES,
                                 *contract_module.HOLDOUT_CODES)),
            },
        }
        self.contract_path = self.root / contract_module.CONTRACT_PATH
        write_json(self.contract_path, self.contract)

    def refresh_manifest(self, omit=(), extra=()):
        required = contract_module.required_paths(self.contract, self.root)
        files = []
        for relative in (*required, *extra):
            if relative in omit:
                continue
            path = self.root / relative
            files.append({
                "path": relative, "byte_length": path.stat().st_size,
                "sha256": contract_module.sha256_file(path),
            })
        files.sort(key=lambda item: item["path"].encode("utf-8"))
        self.manifest = {
            "files": files, "manifest_version": contract_module.MANIFEST_VERSION,
            "root_sha256": contract_module.root_sha256(files),
        }
        self.manifest_path = self.root / contract_module.MANIFEST_PATH
        write_json(self.manifest_path, self.manifest, canonical=True)

    def refresh_receipts(self):
        common = {
            "receipt_version": contract_module.RECEIPT_VERSION,
            "root_sha256": self.manifest["root_sha256"],
            "manifest_sha256": contract_module.sha256_file(self.manifest_path),
            "commit_sha": "a" * 40,
        }
        self.commit = {
            **common, "kind": "commit", "committed_at": "2026-01-01T00:00:00Z",
        }
        self.tag = {
            **common, "kind": "tag", "tag_name": "v4.2-freeze-test",
            "tag_object_sha": "b" * 40, "annotated": True, "signed": True,
            "signature_verified": True, "signer_identity": "jkee",
            "tagged_at": "2026-01-01T00:01:00Z",
        }
        api = "https://api.github.com/repos/jkee/rollup-economy"
        self.ci = {
            **common, "kind": "ci", "tag_name": self.tag["tag_name"],
            "provider": "github-actions", "github_owner": "jkee",
            "github_repository": "rollup-economy",
            "workflow_path": contract_module.WORKFLOW_PATH, "workflow_id": 789,
            "run_id": 123, "run_attempt": 1,
            "run_api_url": api + "/actions/runs/123",
            "run_html_url": "https://github.com/jkee/rollup-economy/actions/runs/123",
            "artifacts_api_url": api + "/actions/runs/123/artifacts",
            "event": "push", "conclusion": "success",
            "run_started_at": "2026-01-01T00:02:00Z",
            "run_updated_at": "2026-01-01T00:03:00Z", "artifact_id": 456,
            "artifact_name": "v4.2-freeze-" + common["commit_sha"],
            "artifact_api_url": api + "/actions/artifacts/456",
            "artifact_archive_download_url": api + "/actions/artifacts/456/zip",
            "artifact_digest": "sha256:" + "c" * 64,
            "artifact_created_at": "2026-01-01T00:02:30Z",
            "artifact_updated_at": "2026-01-01T00:03:00Z",
            "issued_at": "2026-01-01T00:04:00Z",
        }
        self.commit_path = self.root / "commit.json"
        self.tag_path = self.root / "tag.json"
        self.ci_path = self.root / "ci.json"
        write_json(self.commit_path, self.commit); write_json(self.tag_path, self.tag)
        write_json(self.ci_path, self.ci)

    def git_runner(self, root, args):
        self.git_calls.append(tuple(args))
        prefix = self.commit["commit_sha"] + ":"
        stdout = b""
        if args and args[0] == "show" and args[1].startswith(prefix):
            stdout = (self.root / args[1][len(prefix):]).read_bytes()
        elif args[:2] == ["cat-file", "-t"] and len(args) == 3 and args[2].startswith(prefix):
            stdout = b"blob\n"
        elif args == ["cat-file", "-t", self.tag["tag_object_sha"]]:
            stdout = b"tag\n"
        elif args == ["cat-file", "-p", self.tag["tag_object_sha"]]:
            stdout = (
                "object %s\ntype commit\ntag %s\ntagger Fixture <f@example.com> 0 +0000\n\n"
                "root %s\n-----BEGIN SSH SIGNATURE-----\nfixture\n"
                % (self.commit["commit_sha"], self.tag["tag_name"],
                   self.manifest["root_sha256"])
            ).encode()
        return SimpleNamespace(returncode=0, stdout=stdout, stderr=b"")

    def validate(self):
        return contract_module.validate(
            self.contract_path, self.manifest_path, self.commit_path, self.tag_path,
            self.ci_path, self.root, git_runner=self.git_runner,
        )


class FreezeContractV42Tests(unittest.TestCase):
    def test_hosted_workflows_resolve_tag_objects_and_absolute_signer_files(self):
        repo = HERE.parent.parent
        cases = (
            (".github/workflows/v4-2-freeze.yml", "FREEZE_TAG"),
            (".github/workflows/v4-2-full-scope-extension.yml", "EXTENSION_TAG"),
        )
        for relative, variable in cases:
            workflow = (repo / relative).read_text(encoding="utf-8")
            self.assertIn('git rev-parse "refs/tags/$%s"' % variable, workflow)
            self.assertNotIn('refs/tags/$%s^{tag}' % variable, workflow)
            self.assertIn(
                'gpg.ssh.allowedSignersFile "$GITHUB_WORKSPACE/'
                'pipeline/v4_2/allowed_signers"',
                workflow,
            )

    def test_complete_contract_and_authorization_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual([], Fixture(directory).validate())

    def test_incomplete_and_extra_manifest_members_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            fixture.refresh_manifest(omit={"V4_2_METHODOLOGY.md"})
            fixture.refresh_receipts()
            self.assertTrue(any("omits required" in error for error in fixture.validate()))
            extra = fixture.root / "economic-result.json"
            write_json(extra, {})
            fixture.refresh_manifest(extra={"economic-result.json"})
            fixture.refresh_receipts()
            self.assertTrue(any("outside the closed plan" in error for error in fixture.validate()))

    def test_plan_is_deterministic_and_covers_all_dataset_chains(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            output = contract_module.write_or_check_plan(
                contract_module.CONTRACT_PATH, fixture.root,
            )
            first = output.read_bytes()
            contract_module.write_or_check_plan(contract_module.CONTRACT_PATH, fixture.root)
            self.assertEqual(first, output.read_bytes())
            contract_module.write_or_check_plan(
                contract_module.CONTRACT_PATH, fixture.root, check=True,
            )
            files = json.loads(first)["files"]
            for relative in (
                "V4_2_METHODOLOGY.md", "V4_2_RUNTIME_METHODOLOGY.md",
                "pipeline/build/build_runtime_methodology_v4_2.py",
                "pipeline/build/test_runtime_methodology_v4_2.py",
            ):
                self.assertIn(relative, files)
            self.assertEqual(63, sum(path.startswith("pipeline/datasets/v4_2/") for path in files))
            self.assertEqual(63, sum(path.startswith("pipeline/datasets/v4_1/") for path in files))
            self.assertEqual(63, sum(path.startswith("pipeline/datasets/derived/") for path in files))

    def test_runtime_methodology_must_equal_fresh_derivation(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            runtime_path = fixture.root / "V4_2_RUNTIME_METHODOLOGY.md"
            runtime_path.write_bytes(runtime_path.read_bytes() + b"tamper\n")
            with self.assertRaisesRegex(contract_module.ContractError, "fresh deterministic"):
                contract_module.required_paths(fixture.contract, fixture.root)

    def test_invalid_runtime_builder_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            builder_path = fixture.root / "pipeline/build/build_runtime_methodology_v4_2.py"
            builder_path.write_text("not valid python !!!\n", encoding="utf-8")
            with self.assertRaisesRegex(contract_module.ContractError, "validation failed"):
                contract_module.required_paths(fixture.contract, fixture.root)

    def test_dataset_reuse_requires_exact_source_digest(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            source = fixture.root / "pipeline/datasets/derived/541890.json"
            write_json(source, {"naics": "541890", "changed": True})
            with self.assertRaisesRegex(contract_module.ContractError, "provenance/digest"):
                contract_module.required_paths(fixture.contract, fixture.root)

    def test_exact_ten_specs_and_prompts_are_required(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            (fixture.root / "pipeline/prompts_v4_2/541890.md").unlink()
            with self.assertRaisesRegex(contract_module.ContractError, "exact ten"):
                contract_module.required_paths(fixture.contract, fixture.root)

    def test_contract_cannot_weaken_routes_or_cohorts(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            broken = copy.deepcopy(fixture.contract)
            broken["holdout_codes"] = broken["holdout_codes"][:-1]
            broken["model_routes"]["review"]["all"] = "other"
            errors = contract_module.contract_errors(broken, fixture.root)
            self.assertTrue(any("holdout_codes" in error for error in errors))
            self.assertTrue(any("model_routes" in error for error in errors))

    def test_immutable_tag_oid_not_mutable_ref_is_verified(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            self.assertEqual([], fixture.validate())
            verify_calls = [call for call in fixture.git_calls if "verify-tag" in call]
            self.assertEqual(1, len(verify_calls))
            self.assertEqual(fixture.tag["tag_object_sha"], verify_calls[0][-1])
            self.assertNotIn("refs/tags/" + fixture.tag["tag_name"], verify_calls[0])

    def test_descendant_repair_does_not_replace_authorized_member(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            spec = fixture.commit["commit_sha"] + ":V4_2_METHODOLOGY.md"

            def stale_commit(root, args):
                result = fixture.git_runner(root, args)
                if args == ["show", spec]:
                    return SimpleNamespace(returncode=0, stdout=b"ancestor\n", stderr=b"")
                return result

            errors = contract_module.authorization_errors(
                fixture.manifest, fixture.manifest_path, fixture.commit, fixture.tag,
                fixture.ci, fixture.root, git_runner=stale_commit,
            )
            self.assertTrue(any("member digest mismatch" in error for error in errors))

    def test_arbitrary_ci_proof_urls_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Fixture(directory)
            fixture.ci["run_api_url"] = "https://example.com/run"
            write_json(fixture.ci_path, fixture.ci)
            self.assertTrue(any("noncanonical proof URL" in error for error in fixture.validate()))

    def test_freeze_builder_is_canonical_and_v42_versioned(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a").write_bytes(b"alpha")
            manifest = freeze_module.build_manifest({"files": ["a"]}, root)
            self.assertEqual("v4.2-freeze-1", manifest["manifest_version"])
            self.assertEqual(
                freeze_module.canonical_bytes(manifest),
                freeze_module.canonical_bytes(freeze_module.build_manifest(["a"], root)),
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
