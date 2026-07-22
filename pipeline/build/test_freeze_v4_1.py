#!/usr/bin/env python3
"""Tests for the v4.1 §14 deterministic freeze-manifest utility."""

import hashlib
import importlib.util
import json
import tempfile
from pathlib import Path
import unittest


HERE = Path(__file__).resolve().parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


freeze = load_module("freeze_v4_1_tests", HERE / "freeze_v4_1.py")


class FreezeV41Tests(unittest.TestCase):
    def write(self, root, relative, content):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def test_manifest_is_sorted_compact_and_uses_section_14_root_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "z.txt", b"z")
            self.write(root, "a/alpha.txt", b"alpha\n")
            manifest = freeze.build_manifest(["z.txt", "a/alpha.txt"], root=root)

        files = manifest["files"]
        self.assertEqual([item["path"] for item in files], ["a/alpha.txt", "z.txt"])
        expected_stream = b"".join(
            item["path"].encode("utf-8") + b"\0" + str(item["byte_length"]).encode("ascii")
            + b"\0" + item["sha256"].encode("ascii") + b"\n"
            for item in files
        )
        self.assertEqual(manifest["root_sha256"], hashlib.sha256(expected_stream).hexdigest())
        self.assertEqual(
            freeze.canonical_bytes(manifest),
            json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"),
        )

    def test_plan_accepts_list_or_files_object(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "one.txt", b"one")
            from_list = freeze.build_manifest(["one.txt"], root=root)
            from_object = freeze.build_manifest({"files": ["one.txt"]}, root=root)
        self.assertEqual(from_list, from_object)

    def test_rejects_duplicates_missing_and_escape_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "safe.txt", b"safe")
            cases = (
                (["safe.txt", "safe.txt"], "duplicate"),
                (["missing.txt"], "does not exist"),
                (["../outside.txt"], "must not contain"),
                (["/tmp/outside.txt"], "repository-relative"),
                (["safe\\path.txt"], "POSIX"),
                ({"files": ["safe.txt"], "extra": True}, "exactly 'files'"),
            )
            for plan, message in cases:
                with self.subTest(plan=plan), self.assertRaisesRegex(freeze.FreezeError, message):
                    freeze.build_manifest(plan, root=root)

    def test_rejects_symlink_that_resolves_outside_repository(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside_directory:
            root = Path(directory)
            outside = Path(outside_directory) / "outside.txt"
            outside.write_bytes(b"outside")
            (root / "link.txt").symlink_to(outside)
            with self.assertRaisesRegex(freeze.FreezeError, "escapes repository"):
                freeze.build_manifest(["link.txt"], root=root)

    def test_check_requires_exact_canonical_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "data.txt", b"data")
            plan = root / "plan.json"
            output = root / "manifest.json"
            plan.write_text(json.dumps(["data.txt"]), encoding="utf-8")
            original_repo = freeze.REPO
            try:
                freeze.REPO = root
                self.assertEqual(freeze.main(["--plan", str(plan), "--output", str(output)]), 0)
                self.assertEqual(freeze.main(["--plan", str(plan), "--output", str(output), "--check"]), 0)
                output.write_bytes(output.read_bytes() + b"\n")
                self.assertEqual(freeze.main(["--plan", str(plan), "--output", str(output), "--check"]), 1)
            finally:
                freeze.REPO = original_repo


if __name__ == "__main__":
    unittest.main()
