#!/usr/bin/env python3
"""Build or byte-check the canonical v4.2 §15 freeze manifest."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys


REPO = Path(__file__).resolve().parent.parent.parent
MANIFEST_VERSION = "v4.2-freeze-1"


class FreezeError(ValueError):
    """Raised when an unsafe or malformed freeze plan is supplied."""


def _closed_pairs(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise FreezeError("duplicate JSON key: %r" % key)
        value[key] = item
    return value


def _reject_constant(value):
    raise FreezeError("non-standard JSON constant is forbidden: %r" % value)


def load_json(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(
            handle, object_pairs_hook=_closed_pairs, parse_constant=_reject_constant,
        )


def canonical_bytes(value):
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")


def plan_paths(value):
    if isinstance(value, list):
        paths = value
    elif isinstance(value, dict) and set(value) == {"files"}:
        paths = value["files"]
    else:
        raise FreezeError("plan must be an array or a closed object containing files")
    if (not isinstance(paths, list) or not paths
            or not all(isinstance(path, str) for path in paths)):
        raise FreezeError("plan files must be a non-empty string array")
    if paths != sorted(set(paths), key=lambda path: path.encode("utf-8")):
        raise FreezeError("plan files must be bytewise sorted and unique")
    return paths


def repository_file(root, relative):
    if not relative or "\\" in relative or "\0" in relative:
        raise FreezeError("path must be a canonical repository-relative POSIX path")
    pure = PurePosixPath(relative)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
        raise FreezeError("unsafe repository path: %s" % relative)
    root = Path(root).resolve()
    candidate = root.joinpath(*pure.parts).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise FreezeError("path escapes repository: %s" % relative) from exc
    if not candidate.is_file():
        raise FreezeError("freeze member does not exist: %s" % relative)
    return candidate


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def root_sha256(files):
    digest = hashlib.sha256()
    for item in files:
        digest.update(item["path"].encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(item["byte_length"]).encode("ascii"))
        digest.update(b"\0")
        digest.update(item["sha256"].encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def build_manifest(plan, root=REPO):
    files = []
    for relative in plan_paths(plan):
        path = repository_file(root, relative)
        files.append({
            "path": relative,
            "byte_length": path.stat().st_size,
            "sha256": sha256_file(path),
        })
    return {
        "files": files,
        "manifest_version": MANIFEST_VERSION,
        "root_sha256": root_sha256(files),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--repo-root", default=str(REPO))
    args = parser.parse_args(argv)
    try:
        manifest = build_manifest(load_json(args.plan), Path(args.repo_root))
        expected = canonical_bytes(manifest)
        output = Path(args.output)
        if args.check:
            if output.read_bytes() != expected:
                raise FreezeError("freeze manifest is not byte-identical to fresh generation")
            print("OK: v4.2 freeze manifest is byte-identical: %s" % output)
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(expected)
            print("OK: wrote canonical v4.2 freeze manifest: %s" % output)
    except (OSError, UnicodeError, json.JSONDecodeError, FreezeError) as exc:
        print("V4.2 FREEZE FAILED: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
