#!/usr/bin/env python3
"""Build and verify the file-digest manifest required by v4.1 §14.

The caller supplies membership explicitly as either a JSON array of
repository-relative paths or an object containing exactly ``{"files": [...]}``.
This utility deliberately has no opinion about which files belong in a freeze.
"""

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path, PureWindowsPath


REPO = Path(__file__).resolve().parent.parent.parent
MANIFEST_VERSION = "v4.1-freeze-1"


class FreezeError(ValueError):
    """Raised when a freeze plan cannot produce a safe deterministic manifest."""


def _reject_duplicate_key(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise FreezeError("duplicate JSON key: %r" % key)
        value[key] = item
    return value


def canonical_bytes(value):
    """Return the compact, sorted-key JSON encoding used for manifests."""
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_plan(path):
    try:
        with Path(path).open("r", encoding="utf-8") as handle:
            value = json.load(handle, object_pairs_hook=_reject_duplicate_key)
    except FileNotFoundError as exc:
        raise FreezeError("plan not found: %s" % path) from exc
    except json.JSONDecodeError as exc:
        raise FreezeError("plan is not valid JSON: %s" % exc) from exc
    return plan_paths(value)


def plan_paths(value):
    """Validate and return the caller-declared path list without sorting it."""
    if isinstance(value, list):
        paths = value
    elif isinstance(value, dict) and set(value) == {"files"}:
        paths = value["files"]
    else:
        raise FreezeError("plan must be a JSON array or an object containing exactly 'files'")
    if not isinstance(paths, list) or not paths:
        raise FreezeError("plan files must be a non-empty JSON array")
    if not all(isinstance(path, str) for path in paths):
        raise FreezeError("plan files must be strings")
    return paths


def _repository_file(root, relative):
    """Return a resolved file only for a canonical path contained in ``root``."""
    if not relative or "\x00" in relative:
        raise FreezeError("file path must be a non-empty path without NUL bytes")
    windows_path = PureWindowsPath(relative)
    if "\\" in relative or os.path.isabs(relative) or windows_path.is_absolute() or windows_path.drive:
        raise FreezeError("file path must be a canonical repository-relative POSIX path: %s" % relative)
    parts = relative.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise FreezeError("file path must not contain empty, '.' or '..' components: %s" % relative)

    root = Path(root).resolve()
    candidate = (root.joinpath(*parts)).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise FreezeError("file path escapes repository: %s" % relative) from exc
    if not candidate.is_file():
        raise FreezeError("file does not exist: %s" % relative)
    return candidate


def root_sha256(files):
    """Hash §14's sorted ``path NUL length NUL sha LF`` byte stream exactly."""
    digest = hashlib.sha256()
    for item in sorted(files, key=lambda entry: entry["path"].encode("utf-8")):
        digest.update(item["path"].encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(item["byte_length"]).encode("ascii"))
        digest.update(b"\0")
        digest.update(item["sha256"].encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def build_manifest(paths, root=None):
    """Build a canonical manifest from an explicit plan of repository files."""
    paths = plan_paths(paths)
    root = REPO if root is None else root
    seen = set()
    files = []
    for relative in paths:
        if relative in seen:
            raise FreezeError("duplicate file path: %s" % relative)
        seen.add(relative)
        absolute = _repository_file(root, relative)
        files.append({
            "path": relative,
            "byte_length": absolute.stat().st_size,
            "sha256": sha256_file(absolute),
        })
    files.sort(key=lambda item: item["path"].encode("utf-8"))
    return {
        "files": files,
        "manifest_version": MANIFEST_VERSION,
        "root_sha256": root_sha256(files),
    }


def _write(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_bytes(canonical_bytes(value))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, help="JSON array or {\"files\": [...]} freeze plan")
    parser.add_argument("--output", required=True, help="canonical freeze-manifest JSON path")
    parser.add_argument("--check", action="store_true", help="verify output is byte-identical to fresh generation")
    args = parser.parse_args(argv)
    try:
        manifest = build_manifest(_load_plan(args.plan))
        expected = canonical_bytes(manifest)
        output = Path(args.output)
        if args.check:
            try:
                actual = output.read_bytes()
            except FileNotFoundError as exc:
                raise FreezeError("freeze manifest not found for --check: %s" % output) from exc
            if actual != expected:
                raise FreezeError("freeze manifest differs from fresh canonical generation: %s" % output)
            print("OK: freeze manifest is byte-identical: %s" % output)
        else:
            _write(output, manifest)
            print("OK: wrote canonical freeze manifest: %s" % output)
    except (FreezeError, OSError, UnicodeError) as exc:
        print("FREEZE FAILED: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
