#!/usr/bin/env python3

import importlib.util
from contextlib import nullcontext
from pathlib import Path
import tempfile
import unittest
from unittest import mock


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "full_issuance_authority_v4_2_tests", HERE / "issue_campaign_v4_2.py")
issuer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(issuer)


class FullIssuanceAuthorityV42Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.codes = ["%06d" % value for value in range(100001, 100054)]
        files = []
        for code in self.codes:
            for relative, content in (
                    ("pipeline/prompts_v4_2/%s.md" % code, b"prompt\n"),
                    ("pipeline/specs_v4_2/%s.json" % code, b"{}")):
                path = self.root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
                files.append({"path": relative, "sha256": issuer.sha256_bytes(content),
                              "byte_length": len(content)})
        self.extension = {
            "extension_version": "v4.2-full-scope-extension-1",
            "purpose": "authorize-post-gate-full-scope-inputs",
            "base_freeze_root_sha256": "b" * 64,
            "codes": self.codes, "files": files,
            "root_sha256": issuer._root_sha256(files),
        }
        self.extension_path = self.root / issuer.SCOPE_EXTENSION_MANIFEST_PATH
        self.extension_path.parent.mkdir(parents=True, exist_ok=True)
        self.extension_path.write_bytes(issuer.canonical_bytes(self.extension))
        self.ci_relative = "authorization/full-scope-extension-ci.json"
        ci = {"root_sha256": self.extension["root_sha256"],
              "manifest_sha256": issuer.sha256_file(self.extension_path),
              "commit_sha": "c" * 40, "tag_name": "v4.2-full-scope-test"}
        ci_path = self.root / self.ci_relative
        ci_path.parent.mkdir(parents=True, exist_ok=True)
        ci_path.write_bytes(issuer.canonical_bytes(ci))
        self.receipt = {
            "receipt_version": "v4.2-full-scope-extension-receipt-1",
            "kind": "full_scope_extension",
            "manifest_sha256": issuer.sha256_file(self.extension_path),
            "root_sha256": self.extension["root_sha256"], "commit_sha": "c" * 40,
            "tag_name": "v4.2-full-scope-test", "tag_object_sha": "d" * 40,
            "signed": True, "signature_verified": True, "signer_identity": "fixture",
            "ci_receipt": {"path": self.ci_relative, "sha256": issuer.sha256_file(ci_path),
                           "byte_length": ci_path.stat().st_size},
        }
        self.receipt_relative = "authorization/full-scope-extension-receipt.json"
        receipt_path = self.root / self.receipt_relative
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_bytes(issuer.canonical_bytes(self.receipt))

    def tearDown(self):
        self.temp.cleanup()

    def git_patches(self):
        tag = (b"object " + self.receipt["commit_sha"].encode() + b"\n"
               b"type commit\ntag " + self.receipt["tag_name"].encode() + b"\n\n"
               b"extension-root " + self.extension["root_sha256"].encode())
        def git(_root, *args):
            if args[:2] == ("cat-file", "-t"):
                return "commit" if args[2] == self.receipt["commit_sha"] else "tag"
            if args[:2] == ("rev-parse", self.receipt["tag_object_sha"] + "^{commit}"):
                return self.receipt["commit_sha"]
            return "verified"
        def git_bytes(_root, *args):
            if args[:2] == ("cat-file", "-p"):
                return tag
            relative = args[1].split(":", 1)[1]
            return (self.root / relative).read_bytes()
        return mock.patch.object(issuer, "_git", side_effect=git), \
            mock.patch.object(issuer, "_git_bytes", side_effect=git_bytes)

    def contract_result(self, *_args):
        return {"codes": self.codes, "root_sha256": self.extension["root_sha256"]}

    def test_signed_exact_extension_is_reachable_and_wrong_membership_fails(self):
        first, second = self.git_patches()
        with first, second, mock.patch.object(
                issuer, "_isolated_git_tree", return_value=nullcontext(self.root)):
            files, binding = issuer._validate_scope_extension(
                self.root, issuer.SCOPE_EXTENSION_MANIFEST_PATH,
                self.receipt_relative, self.codes, verify_live_ci=False,
                contract_validator=self.contract_result)
        self.assertEqual(set(files), {item["path"] for item in self.extension["files"]})
        self.assertEqual(binding["root_sha256"], self.extension["root_sha256"])
        first, second = self.git_patches()
        with first, second, mock.patch.object(
                issuer, "_isolated_git_tree", return_value=nullcontext(self.root)), \
                self.assertRaisesRegex(issuer.IssueError, "53-code"):
            issuer._validate_scope_extension(
                self.root, issuer.SCOPE_EXTENSION_MANIFEST_PATH,
                self.receipt_relative, self.codes[:-1], verify_live_ci=False,
                contract_validator=self.contract_result)

    def test_missing_invalid_and_accepted_gate_certificate_pairs(self):
        with self.assertRaisesRegex(issuer.IssueError, "required file"):
            issuer._validate_full_gate_certificates(
                self.root, issuer.REGRESSION_GATE_CERTIFICATE_PATH,
                issuer.HOLDOUT_GATE_CERTIFICATE_PATH, gate_validator=lambda _m, _r: [])
        for relative in (issuer.REGRESSION_GATE_CERTIFICATE_PATH,
                         issuer.HOLDOUT_GATE_CERTIFICATE_PATH):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"certificate")
        with self.assertRaisesRegex(issuer.IssueError, "not exactly valid"):
            issuer._validate_full_gate_certificates(
                self.root, issuer.REGRESSION_GATE_CERTIFICATE_PATH,
                issuer.HOLDOUT_GATE_CERTIFICATE_PATH,
                gate_validator=lambda _m, _r: ["rejected gate"])
        refs = issuer._validate_full_gate_certificates(
            self.root, issuer.REGRESSION_GATE_CERTIFICATE_PATH,
            issuer.HOLDOUT_GATE_CERTIFICATE_PATH, gate_validator=lambda _m, _r: [])
        self.assertEqual(set(refs), {"regression_canary", "holdout"})

    def test_extension_chain_rejects_divergence_base_change_and_extra_inventory(self):
        base = b"base freeze\n"
        (self.root / "base.txt").write_bytes(base)
        base_frozen = {"base.txt": {"path": "base.txt", "sha256": issuer.sha256_bytes(base),
                                    "byte_length": len(base)}}
        base_sha = "a" * 40
        first, second = self.git_patches()
        with first as git, second:
            git.side_effect = issuer.IssueError("not ancestor")
            with self.assertRaisesRegex(issuer.IssueError, "not ancestor"):
                issuer._validate_scope_extension(
                    self.root, issuer.SCOPE_EXTENSION_MANIFEST_PATH, self.receipt_relative,
                    self.codes, base_frozen, base_sha, verify_live_ci=False,
                    contract_validator=self.contract_result)

        tag = (b"object " + self.receipt["commit_sha"].encode() + b"\n"
               b"type commit\ntag " + self.receipt["tag_name"].encode() + b"\n\n"
               b"extension-root " + self.extension["root_sha256"].encode() + b"\n"
               b"base-commit " + base_sha.encode())
        expected_diff = "\n".join(
            sorted({item["path"] for item in self.extension["files"]}
                   | {issuer.SCOPE_EXTENSION_MANIFEST_PATH}))
        def good_git(_root, *args):
            if args[:2] == ("cat-file", "-t"):
                return "commit" if args[2] == self.receipt["commit_sha"] else "tag"
            if args[0] == "rev-parse":
                return self.receipt["commit_sha"]
            if args[0] == "diff":
                return expected_diff
            return ""
        def bytes_with_bad_base(_root, *args):
            if args[:2] == ("cat-file", "-p"):
                return tag
            relative = args[1].split(":", 1)[1]
            return b"changed" if relative == "base.txt" else (self.root / relative).read_bytes()
        with mock.patch.object(issuer, "_git", side_effect=good_git), \
                mock.patch.object(issuer, "_git_bytes", side_effect=bytes_with_bad_base), \
                self.assertRaisesRegex(issuer.IssueError, "changes base-freeze"):
            issuer._validate_scope_extension(
                self.root, issuer.SCOPE_EXTENSION_MANIFEST_PATH, self.receipt_relative,
                self.codes, base_frozen, base_sha, verify_live_ci=False,
                contract_validator=self.contract_result)

        def good_bytes(_root, *args):
            if args[:2] == ("cat-file", "-p"):
                return tag
            return (self.root / args[1].split(":", 1)[1]).read_bytes()
        def extra_git(_root, *args):
            value = good_git(_root, *args)
            return value + "\nextra.txt" if args[0] == "diff" else value
        with mock.patch.object(issuer, "_git", side_effect=extra_git), \
                mock.patch.object(issuer, "_git_bytes", side_effect=good_bytes), \
                self.assertRaisesRegex(issuer.IssueError, "inventory differs"):
            issuer._validate_scope_extension(
                self.root, issuer.SCOPE_EXTENSION_MANIFEST_PATH, self.receipt_relative,
                self.codes, base_frozen, base_sha, verify_live_ci=False,
                contract_validator=self.contract_result)


if __name__ == "__main__":
    unittest.main()
