#!/usr/bin/env python3

import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "validate_full_scope_extension_v4_2_tests",
    HERE / "validate_full_scope_extension_v4_2.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
assembler_spec = importlib.util.spec_from_file_location(
    "assemble_prompts_for_full_scope_extension_tests",
    HERE / "assemble_prompts.py")
assembler = importlib.util.module_from_spec(assembler_spec)
assembler_spec.loader.exec_module(assembler)

prompt_test_spec = importlib.util.spec_from_file_location(
    "prompt_fixtures_for_full_scope_extension_tests",
    HERE / "test_prompt_v4_2.py")
prompt_fixtures = importlib.util.module_from_spec(prompt_test_spec)
prompt_test_spec.loader.exec_module(prompt_fixtures)


class FullScopeExtensionValidatorV42Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.email", "c2@test"], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.name", "C2 Test"], check=True)
        regression = ["100%02d" % index for index in range(1, 6)]
        holdout = ["200%02d" % index for index in range(1, 6)]
        self.codes = ["300%02d" % index for index in range(1, 54)]
        targets = regression + holdout + self.codes
        self.write_json(validator.TARGETS_PATH, {
            "codes": [{"naics": code, "title": "Target %s" % code} for code in targets]})
        self.write_json(validator.REGRESSION_PATH, {"selected_codes": regression})
        self.write_json(validator.HOLDOUT_PATH, {"selected_codes": holdout})
        base_files = []
        for relative in (validator.TARGETS_PATH, validator.REGRESSION_PATH, validator.HOLDOUT_PATH):
            path = self.root / relative
            base_files.append({"path": relative, "sha256": validator.sha256_bytes(path.read_bytes()),
                               "byte_length": path.stat().st_size})
        for code in regression + holdout:
            for relative, content in (
                    ("pipeline/specs_v4_2/%s.json" % code, b"{}"),
                    ("pipeline/prompts_v4_2/%s.md" % code, b"prompt\n")):
                path = self.root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
                base_files.append({"path": relative,
                                   "sha256": validator.sha256_bytes(content),
                                   "byte_length": len(content)})
        self.write_json(validator.BASE_MANIFEST_PATH, {
            "files": base_files, "manifest_version": "v4.2-freeze-1",
            "root_sha256": validator.root_sha256(base_files)})
        self.git("add", ".")
        self.git("commit", "-qm", "C1")
        self.base_commit = self.git("rev-parse", "HEAD")
        extension_files = []
        for code in self.codes:
            for relative, content in (
                    ("pipeline/specs_v4_2/%s.json" % code, b"{}"),
                    ("pipeline/prompts_v4_2/%s.md" % code, b"prompt\n")):
                path = self.root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
                extension_files.append({"path": relative,
                                        "sha256": validator.sha256_bytes(content),
                                        "byte_length": len(content)})
        base = json.loads((self.root / validator.BASE_MANIFEST_PATH).read_text())
        self.extension = {
            "extension_version": validator.EXTENSION_VERSION,
            "purpose": "authorize-post-gate-full-scope-inputs",
            "base_freeze_root_sha256": base["root_sha256"], "codes": self.codes,
            "files": extension_files, "root_sha256": validator.root_sha256(extension_files),
        }
        self.write_json(validator.EXTENSION_PATH, self.extension)
        self.git("add", ".")
        self.git("commit", "-qm", "C2")

    def tearDown(self):
        self.temp.cleanup()

    def write_json(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(validator.canonical_bytes(value))

    def git(self, *args):
        result = subprocess.run(["git", "-C", str(self.root), *args], check=True,
                                stdout=subprocess.PIPE, text=True)
        return result.stdout.strip()

    @staticmethod
    def passing_runner(command, **kwargs):
        if command[-6:] != ["--template-version", "4.2", "--scope", "full", "--check", "--lint"]:
            return SimpleNamespace(returncode=1, stderr="wrong assembler invocation", stdout="")
        return SimpleNamespace(returncode=0, stderr="", stdout="")

    def replace_extension_file(self, relative, content):
        path = self.root / relative
        path.write_bytes(content)
        for item in self.extension["files"]:
            if item["path"] == relative:
                item["sha256"] = validator.sha256_bytes(content)
                item["byte_length"] = len(content)
                break
        self.extension["root_sha256"] = validator.root_sha256(self.extension["files"])
        self.write_json(validator.EXTENSION_PATH, self.extension)
        self.git("add", relative, validator.EXTENSION_PATH)
        self.git("commit", "-qm", "mutate C2 fixture")

    def assembler_runner_for(self, relative):
        def runner(command, **kwargs):
            if command[-6:] != [
                    "--template-version", "4.2", "--scope", "full",
                    "--check", "--lint"]:
                return SimpleNamespace(
                    returncode=1, stderr="wrong assembler invocation", stdout="")
            path = Path(kwargs["cwd"]) / relative
            try:
                value = assembler._read_json(
                    "30001", path, "C2 industry spec", strict_v4_2=True)
                assembler.validate_industry_spec_v4_2(
                    value.get("naics", "300001"),
                    value.get("title", "Target 300001"), value)
            except assembler.AssembleError as exc:
                return SimpleNamespace(returncode=1, stderr=str(exc), stdout="")
            return SimpleNamespace(returncode=0, stderr="", stdout="")
        return runner

    def test_exact_c2_inventory_runs_full_semantic_lint(self):
        result = validator.validate(self.root, self.base_commit, runner=self.passing_runner)
        self.assertEqual(result["codes"], self.codes)

    def test_stale_base_arbitrary_inventory_and_semantic_leak_fail(self):
        target = self.root / validator.REGRESSION_PATH
        target.write_bytes(target.read_bytes() + b"\n")
        with self.assertRaisesRegex(validator.ExtensionError, "changes C1"):
            validator.validate(self.root, self.base_commit, runner=self.passing_runner)
        target.write_bytes(target.read_bytes()[:-1])

        broken = dict(self.extension)
        broken["files"] = list(broken["files"]) + [{
            "path": "arbitrary.txt", "sha256": "0" * 64, "byte_length": 0}]
        self.write_json(validator.EXTENSION_PATH, broken)
        with self.assertRaisesRegex(validator.ExtensionError, "106"):
            validator.validate(self.root, self.base_commit, runner=self.passing_runner)
        self.write_json(validator.EXTENSION_PATH, self.extension)

        failing = lambda *_args, **_kwargs: SimpleNamespace(
            returncode=1, stderr="scope leak", stdout="")
        with self.assertRaisesRegex(validator.ExtensionError, "semantic validation failed"):
            validator.validate(self.root, self.base_commit, runner=failing)

    def test_c2_full_check_lint_rejects_duplicate_spec_key(self):
        relative = "pipeline/specs_v4_2/30001.json"
        self.replace_extension_file(relative, b'{"naics":"30001","naics":"30001"}')
        with self.assertRaisesRegex(
                validator.ExtensionError, "duplicate JSON key 'naics'"):
            validator.validate(
                self.root, self.base_commit,
                runner=self.assembler_runner_for(relative))

    def test_c2_full_check_lint_rejects_duplicate_role_title(self):
        relative = "pipeline/specs_v4_2/30001.json"
        value = prompt_fixtures.fixture_spec(
            code="300001", title="Target 300001")
        value["value_basis"]["roles"][0]["role_cash_cost_weight"] = 0.5
        second = dict(value["value_basis"]["roles"][0])
        second["role_id"] = "delivery-two"
        second["source_ids"] = list(second["source_ids"])
        value["value_basis"]["roles"].append(second)
        self.replace_extension_file(relative, validator.canonical_bytes(value))
        with self.assertRaisesRegex(
                validator.ExtensionError, "unique role titles"):
            validator.validate(
                self.root, self.base_commit,
                runner=self.assembler_runner_for(relative))

    def test_c2_parser_rejects_duplicate_keys(self):
        path = self.root / "duplicate.json"
        path.write_text('{"value":1,"value":2}')
        with self.assertRaisesRegex(validator.ExtensionError, "duplicate JSON key 'value'"):
            validator.load_json(path)


if __name__ == "__main__":
    unittest.main()
