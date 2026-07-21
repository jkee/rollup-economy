#!/usr/bin/env python3
"""Materialize the outcome-independent v4.1 holdout from methodology §12."""

import argparse
import hashlib
import json
import os
import re
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
METHODOLOGY_PATH = "V4_1_METHODOLOGY.md"
FLEET_PATH = "pipeline/blocks/targets_phase3.json"
GOLDEN_PATH = "pipeline/golden/golden_set.json"
DATASET_DIRECTORY = "pipeline/datasets/derived"
OUTPUT_PATH = "pipeline/v4_1/holdout_membership.json"
SALT = "rollup-v4.1-holdout-2026-07-21|"
REGRESSION_CODES = ("541512", "541511", "541214", "238220", "541930")
NAICS_RE = re.compile(r"(?<![0-9])([0-9]{6})(?![0-9])")


def _absolute(repo_root, relative_path):
    if not isinstance(relative_path, str) or not relative_path or os.path.isabs(relative_path):
        raise ValueError("path must be a non-empty repository-relative path")
    root = os.path.realpath(repo_root)
    path = os.path.realpath(os.path.join(root, relative_path))
    if os.path.commonpath((root, path)) != root:
        raise ValueError("path escapes repository: %s" % relative_path)
    return path


def _load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_digest(repo_root, relative_path):
    """Return the audited byte identity for one frozen selector input."""
    path = _absolute(repo_root, relative_path)
    return {
        "path": relative_path,
        "byte_length": os.path.getsize(path),
        "sha256": _sha256(path),
    }


def _codes(value, source_path):
    rows = value.get("codes", value) if isinstance(value, dict) else value
    if not isinstance(rows, list):
        raise ValueError("%s must contain a codes list" % source_path)
    result = []
    for row in rows:
        code = row.get("naics") if isinstance(row, dict) else row
        if not isinstance(code, str) or not NAICS_RE.fullmatch(code):
            raise ValueError("%s contains an invalid NAICS code: %r" % (source_path, code))
        result.append(code)
    if len(result) != len(set(result)):
        raise ValueError("%s contains duplicate NAICS codes" % source_path)
    return sorted(result)


def _code_from_result_path(relative_path):
    """Find a code without parsing an economic artifact's contents."""
    matches = NAICS_RE.findall(relative_path)
    return matches[-1] if matches else None


def preexisting_v4_1_result_codes(repo_root):
    """Find code-addressable v4.1 output artifacts without examining economics.

    The v4.1 runner path is deliberately versioned.  Every artifact under its
    output roots is a burned result, including manually placed output, while
    the membership manifest itself is explicitly excluded.
    """
    result_root = _absolute(repo_root, "pipeline/v4_1")
    if not os.path.isdir(result_root):
        return []
    result = set()
    for directory, _, filenames in os.walk(result_root):
        for filename in filenames:
            path = os.path.join(directory, filename)
            relative_path = os.path.relpath(path, repo_root).replace(os.sep, "/")
            if relative_path == OUTPUT_PATH:
                continue
            code = _code_from_result_path(relative_path)
            if code:
                result.add(code)
    return sorted(result)


def _labor_share(repo_root, code):
    relative_path = "%s/%s.json" % (DATASET_DIRECTORY, code)
    path = _absolute(repo_root, relative_path)
    if not os.path.isfile(path):
        raise ValueError("missing frozen dataset for %s: %s" % (code, relative_path))
    dataset = _load_json(path)
    if dataset.get("naics") != code:
        raise ValueError("dataset identity mismatch for %s" % code)
    value = dataset.get("labor_share", {}).get("value")
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("dataset labor_share.value must be numeric for %s" % code)
    return float(value), relative_path


def _split_bins(rows, count=5):
    """Return contiguous balanced bins, giving each leading bin one remainder row."""
    if len(rows) < count:
        raise ValueError("need at least %d eligible codes to form holdout bins" % count)
    base, remainder = divmod(len(rows), count)
    bins, start = [], 0
    for index in range(count):
        size = base + (1 if index < remainder else 0)
        bins.append(rows[start:start + size])
        start += size
    return bins


def hash_candidate(code):
    return hashlib.sha256((SALT + code).encode("utf-8")).hexdigest()


def canonical_bytes(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def build_membership(repo_root=REPO):
    """Build the complete deterministic §12 selection manifest in memory."""
    fleet = _codes(_load_json(_absolute(repo_root, FLEET_PATH)), FLEET_PATH)
    golden = _codes(_load_json(_absolute(repo_root, GOLDEN_PATH)), GOLDEN_PATH)
    regression = sorted(REGRESSION_CODES)
    preexisting = preexisting_v4_1_result_codes(repo_root)
    excluded = set(regression) | set(golden) | set(preexisting)
    eligible_codes = [code for code in fleet if code not in excluded]

    rows = []
    source_digests = [
        source_digest(repo_root, METHODOLOGY_PATH),
        source_digest(repo_root, FLEET_PATH),
        source_digest(repo_root, GOLDEN_PATH),
    ]
    for code in eligible_codes:
        labor_share, dataset_path = _labor_share(repo_root, code)
        dataset_digest = source_digest(repo_root, dataset_path)
        source_digests.append(dataset_digest)
        rows.append({
            "naics": code,
            "labor_share": labor_share,
            "dataset": dataset_digest,
        })
    rows.sort(key=lambda item: (item["labor_share"], item["naics"]))

    bins = []
    for index, members in enumerate(_split_bins(rows), start=1):
        candidates = []
        for member in members:
            candidates.append({
                "naics": member["naics"],
                "labor_share": member["labor_share"],
                "selection_hash": hash_candidate(member["naics"]),
            })
        selected = min(candidates, key=lambda item: item["selection_hash"])
        bins.append({
            "bin": index,
            "candidates": candidates,
            "selected_naics": selected["naics"],
            "selected_hash": selected["selection_hash"],
        })

    source_digests.sort(key=lambda item: item["path"])
    return {
        "version": "v4.1-holdout-2026-07-21",
        "methodology": {
            "path": METHODOLOGY_PATH,
            "section": "12",
        },
        "selection": {
            "labor_share_order": "ascending numeric labor_share, then lexicographic NAICS",
            "bin_count": 5,
            "binning": "five contiguous balanced bins; leading bins receive the remainder",
            "salt": SALT,
            "hash": "lowercase SHA-256 UTF-8(salt + naics)",
            "winner": "lexicographically smallest lowercase hash in each bin",
        },
        "regression_codes": regression,
        "golden_codes": golden,
        "preexisting_v4_1_result_codes": preexisting,
        "eligible_inputs": rows,
        "bins": bins,
        "selected_codes": [item["selected_naics"] for item in bins],
        "source_digests": source_digests,
    }


def _write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(content)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=REPO,
                        help="repository root containing frozen membership and datasets")
    parser.add_argument("--output", default=OUTPUT_PATH,
                        help="repository-relative canonical membership output")
    parser.add_argument("--check", action="store_true",
                        help="fail unless the existing output reproduces byte-identically")
    args = parser.parse_args(argv)
    try:
        output_path = _absolute(args.repo_root, args.output)
        content = canonical_bytes(build_membership(args.repo_root))
        if args.check:
            if not os.path.isfile(output_path):
                raise ValueError("holdout membership is missing: %s" % args.output)
            with open(output_path, "rb") as handle:
                existing = handle.read()
            if existing != content:
                raise ValueError("holdout membership is not byte-identical: %s" % args.output)
            print("OK: holdout membership reproduces byte-identically")
        else:
            _write(output_path, content)
            print("OK: wrote holdout membership: %s" % args.output)
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print("HOLDOUT FAILED: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
