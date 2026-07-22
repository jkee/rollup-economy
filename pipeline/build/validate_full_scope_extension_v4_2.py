#!/usr/bin/env python3
"""Validate the exact post-gate C2 v4.2 full-scope extension before research."""

import argparse
import hashlib
import json
import os
from pathlib import Path, PureWindowsPath
import re
import subprocess
import sys


REPO = Path(__file__).resolve().parent.parent.parent
EXTENSION_VERSION = "v4.2-full-scope-extension-1"
EXTENSION_PATH = "pipeline/v4_2/full_scope_extension_manifest.json"
BASE_MANIFEST_PATH = "pipeline/v4_2/freeze_manifest.json"
TARGETS_PATH = "pipeline/blocks/targets_phase3.json"
REGRESSION_PATH = "pipeline/v4_2/regression_membership.json"
HOLDOUT_PATH = "pipeline/v4_2/holdout_membership.json"


class ExtensionError(ValueError):
    pass


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def repository_path(root, relative, must_exist=True):
    if (not isinstance(relative, str) or not relative or "\\" in relative
            or os.path.isabs(relative) or PureWindowsPath(relative).drive
            or any(part in ("", ".", "..") for part in relative.split("/"))):
        raise ExtensionError("unsafe repository path: %r" % relative)
    root = Path(root).resolve()
    path = root.joinpath(*relative.split("/")).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise ExtensionError("path escapes repository: %s" % relative) from exc
    if must_exist and not path.is_file():
        raise ExtensionError("required extension file missing: %s" % relative)
    return path


def _reject_constant(value):
    raise ExtensionError("non-standard JSON constant %r is forbidden" % value)


def _closed_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ExtensionError("duplicate JSON key %r" % key)
        result[key] = value
    return result


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"),
                          parse_constant=_reject_constant,
                          object_pairs_hook=_closed_pairs)
    except json.JSONDecodeError as exc:
        raise ExtensionError("invalid JSON: %s" % exc) from exc


def root_sha256(files):
    digest = hashlib.sha256()
    for item in sorted(files, key=lambda row: row["path"].encode("utf-8")):
        digest.update(item["path"].encode("utf-8") + b"\0")
        digest.update(str(item["byte_length"]).encode("ascii") + b"\0")
        digest.update(item["sha256"].encode("ascii") + b"\n")
    return digest.hexdigest()


def _git(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True, check=False)
    if result.returncode:
        raise ExtensionError("git %s failed: %s" % (" ".join(args), result.stderr.strip()))
    return result.stdout.strip()


def validate(root, base_commit, extension_path=EXTENSION_PATH,
             base_manifest_path=BASE_MANIFEST_PATH, runner=subprocess.run):
    root = Path(root).resolve()
    if not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", base_commit or ""):
        raise ExtensionError("base commit must be an exact lowercase git object ID")
    base_file = repository_path(root, base_manifest_path)
    extension_file = repository_path(root, extension_path)
    base, extension = load_json(base_file), load_json(extension_file)
    if base_file.read_bytes() != canonical_bytes(base) or extension_file.read_bytes() != canonical_bytes(extension):
        raise ExtensionError("base and extension manifests must be canonical JSON")
    if (not isinstance(base, dict) or set(base) != {"files", "manifest_version", "root_sha256"}
            or root_sha256(base["files"]) != base["root_sha256"]):
        raise ExtensionError("base freeze manifest is invalid")
    for ref in base["files"]:
        path = repository_path(root, ref["path"])
        content = path.read_bytes()
        if len(content) != ref["byte_length"] or sha256_bytes(content) != ref["sha256"]:
            raise ExtensionError("C2 changes C1 frozen member: %s" % ref["path"])
    targets = load_json(repository_path(root, TARGETS_PATH))["codes"]
    target_codes = {row["naics"] for row in targets}
    excluded = set(load_json(repository_path(root, REGRESSION_PATH))["selected_codes"])
    excluded.update(load_json(repository_path(root, HOLDOUT_PATH))["selected_codes"])
    codes = sorted(target_codes - excluded)
    if len(target_codes) != 63 or len(codes) != 53:
        raise ExtensionError("C2 membership must be exactly the 53 non-gate targets")
    expected_paths = {"pipeline/specs_v4_2/%s.json" % code for code in codes} | {
        "pipeline/prompts_v4_2/%s.md" % code for code in codes}
    for directory, suffix in (("pipeline/specs_v4_2", ".json"),
                              ("pipeline/prompts_v4_2", ".md")):
        actual = {
            path.relative_to(root).as_posix()
            for path in (root / directory).iterdir()
            if path.is_file()
        }
        expected_inventory = {"%s/%s%s" % (directory, code, suffix)
                              for code in target_codes}
        if actual != expected_inventory:
            raise ExtensionError(
                "C2 %s inventory must equal the exact 63 target files" % directory)
    if (not isinstance(extension, dict) or set(extension) != {
            "extension_version", "purpose", "base_freeze_root_sha256", "codes",
            "files", "root_sha256"}
            or extension["extension_version"] != EXTENSION_VERSION
            or extension["purpose"] != "authorize-post-gate-full-scope-inputs"
            or extension["base_freeze_root_sha256"] != base["root_sha256"]
            or extension["codes"] != codes):
        raise ExtensionError("C2 extension header/membership/base binding is invalid")
    files = extension["files"]
    paths = [item.get("path") for item in files if isinstance(item, dict)]
    if set(paths) != expected_paths or len(paths) != len(expected_paths):
        raise ExtensionError("C2 extension inventory must equal exact 106 prompt/spec paths")
    for ref in files:
        if set(ref) != {"path", "sha256", "byte_length"}:
            raise ExtensionError("C2 file reference is not closed")
        content = repository_path(root, ref["path"]).read_bytes()
        if len(content) != ref["byte_length"] or sha256_bytes(content) != ref["sha256"]:
            raise ExtensionError("C2 extension file is stale: %s" % ref["path"])
    if root_sha256(files) != extension["root_sha256"]:
        raise ExtensionError("C2 extension root digest is stale")
    _git(root, "merge-base", "--is-ancestor", base_commit, "HEAD")
    changed = set(filter(None, _git(root, "diff", "--name-only", base_commit, "HEAD").splitlines()))
    if changed != expected_paths | {extension_path}:
        raise ExtensionError("C2 git diff is not exact manifest + 106 inputs")
    command = [sys.executable, "pipeline/build/assemble_prompts.py",
               "--template-version", "4.2", "--scope", "full", "--check", "--lint"]
    result = runner(command, cwd=str(root), stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE, text=True, check=False)
    if result.returncode:
        raise ExtensionError("full prompt/spec semantic validation failed: %s" %
                             (result.stderr.strip() or result.stdout.strip()))
    return {"codes": codes, "root_sha256": extension["root_sha256"],
            "base_root_sha256": base["root_sha256"]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(REPO))
    parser.add_argument("--base-commit", required=True)
    parser.add_argument("--extension-manifest", default=EXTENSION_PATH)
    parser.add_argument("--base-manifest", default=BASE_MANIFEST_PATH)
    args = parser.parse_args(argv)
    try:
        result = validate(args.repo_root, args.base_commit, args.extension_manifest,
                          args.base_manifest)
    except (ExtensionError, OSError, TypeError, KeyError, ValueError) as exc:
        print("C2 EXTENSION FAILED: %s" % exc, file=sys.stderr)
        return 1
    print("OK: validated 53-code C2 extension %s" % result["root_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
