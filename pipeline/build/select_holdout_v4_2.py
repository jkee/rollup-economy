#!/usr/bin/env python3
"""Materialize the outcome-independent v4.2 holdout from methodology §13.

Selection uses the original frozen Phase-4 labor-share field solely for
stratification. Every legacy selection input must be bound byte-for-byte by
its normalized v4.1 snapshot provenance; the normalized snapshot is the
required dataset boundary for all later v4.2 work.
"""

import argparse
import hashlib
import json
import os
import re
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
METHODOLOGY_PATH = "V4_2_METHODOLOGY.md"
FLEET_PATH = "pipeline/blocks/targets_phase3.json"
GOLDEN_PATH = "pipeline/golden/golden_set.json"
LEGACY_DATASET_DIRECTORY = "pipeline/datasets/derived"
NORMALIZED_DATASET_DIRECTORY = "pipeline/datasets/v4_1"
OUTPUT_PATH = "pipeline/v4_2/holdout_membership.json"
SALT = "rollup-v4.2-holdout-2026-07-21|"
DEVELOPMENT_CODES = ("541512", "541511", "541214", "238220", "541930")
EXPECTED_SELECTED_CODES = ("541890", "541340", "541370", "541199", "541420")
PRIOR_ECONOMIC_ROOTS = {
    "v4_0": ("pipeline/v4/packets", "pipeline/v4/runs", "pipeline/v4/memos", "pipeline/v4/reviews"),
    "v4_1": ("pipeline/v4_1/packets", "pipeline/v4_1/runs", "pipeline/v4_1/memos", "pipeline/v4_1/reviews"),
}
V4_2_ECONOMIC_ROOTS = (
    "pipeline/v4_2/packets", "pipeline/v4_2/runs",
    "pipeline/v4_2/memos", "pipeline/v4_2/reviews",
)
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


def _code_from_path(relative_path):
    matches = NAICS_RE.findall(relative_path)
    return matches[-1] if matches else None


def economic_result_codes(repo_root, relative_roots):
    """Return code-addressable outputs without opening economic contents."""
    result = set()
    for relative_root in relative_roots:
        root = _absolute(repo_root, relative_root)
        if not os.path.isdir(root):
            continue
        for directory, _, filenames in os.walk(root):
            for filename in filenames:
                relative_path = os.path.relpath(
                    os.path.join(directory, filename), repo_root
                ).replace(os.sep, "/")
                code = _code_from_path(relative_path)
                if code:
                    result.add(code)
    return sorted(result)


def _selection_input(repo_root, code):
    """Return labor stratifier plus its normalized provenance boundary."""
    legacy_relative = "%s/%s.json" % (LEGACY_DATASET_DIRECTORY, code)
    normalized_relative = "%s/%s.json" % (NORMALIZED_DATASET_DIRECTORY, code)
    legacy_path = _absolute(repo_root, legacy_relative)
    normalized_path = _absolute(repo_root, normalized_relative)
    if not os.path.isfile(legacy_path) or not os.path.isfile(normalized_path):
        raise ValueError("missing legacy or normalized dataset for %s" % code)
    legacy = _load_json(legacy_path)
    normalized = _load_json(normalized_path)
    if legacy.get("naics") != code or normalized.get("naics") != code:
        raise ValueError("dataset identity mismatch for %s" % code)
    if normalized.get("dataset_version") != "4.1":
        raise ValueError("normalized dataset version mismatch for %s" % code)
    if not isinstance(normalized.get("snapshot_id"), str) or not normalized["snapshot_id"].strip():
        raise ValueError("normalized snapshot identity missing for %s" % code)
    provenance = normalized.get("provenance")
    if not isinstance(provenance, dict):
        raise ValueError("normalized provenance missing for %s" % code)
    legacy_digest = source_digest(repo_root, legacy_relative)
    if provenance.get("source_manifest_sha256") != legacy_digest["sha256"]:
        raise ValueError("normalized provenance does not bind legacy dataset for %s" % code)
    value = legacy.get("labor_share", {}).get("value")
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0:
        raise ValueError("legacy labor_share.value must be numeric for %s" % code)
    normalized_value = normalized.get("labor_share", {}).get("value")
    expected_normalized_value = value if value <= 1 else None
    if normalized_value != expected_normalized_value:
        raise ValueError("normalized labor_share translation mismatch for %s" % code)
    normalized_digest = source_digest(repo_root, normalized_relative)
    return float(value), legacy_digest, normalized_digest, {
        "dataset_version": normalized["dataset_version"],
        "snapshot_id": normalized["snapshot_id"],
        "derivation_version": provenance.get("derivation_version"),
        "normalized_labor_share": normalized_value,
        "source_manifest_sha256": provenance["source_manifest_sha256"],
    }


def _split_bins(rows, count=5):
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
    fleet = _codes(_load_json(_absolute(repo_root, FLEET_PATH)), FLEET_PATH)
    golden = _codes(_load_json(_absolute(repo_root, GOLDEN_PATH)), GOLDEN_PATH)
    development = sorted(DEVELOPMENT_CODES)
    prior_outputs = {
        version: economic_result_codes(repo_root, roots)
        for version, roots in sorted(PRIOR_ECONOMIC_ROOTS.items())
    }
    prefreeze_v4_2 = economic_result_codes(repo_root, V4_2_ECONOMIC_ROOTS)
    excluded = set(golden) | set(development) | set(prefreeze_v4_2)
    for codes in prior_outputs.values():
        excluded.update(codes)
    eligible_codes = [code for code in fleet if code not in excluded]

    rows = []
    source_digests = [
        source_digest(repo_root, METHODOLOGY_PATH),
        source_digest(repo_root, FLEET_PATH),
        source_digest(repo_root, GOLDEN_PATH),
    ]
    for code in eligible_codes:
        labor_share, legacy_digest, normalized_digest, boundary = _selection_input(repo_root, code)
        source_digests.extend((legacy_digest, normalized_digest))
        rows.append({
            "naics": code,
            "labor_share": labor_share,
            "legacy_selection_input": legacy_digest,
            "normalized_dataset": normalized_digest,
            "normalization_boundary": boundary,
        })
    rows.sort(key=lambda item: (item["labor_share"], item["naics"]))

    bins = []
    for index, members in enumerate(_split_bins(rows), start=1):
        candidates = [{
            "naics": member["naics"],
            "labor_share": member["labor_share"],
            "selection_hash": hash_candidate(member["naics"]),
        } for member in members]
        selected = min(candidates, key=lambda item: item["selection_hash"])
        bins.append({
            "bin": index,
            "candidates": candidates,
            "selected_naics": selected["naics"],
            "selected_hash": selected["selection_hash"],
        })

    source_digests.sort(key=lambda item: item["path"])
    selected_codes = [item["selected_naics"] for item in bins]
    if (os.path.realpath(repo_root) == os.path.realpath(REPO)
            and selected_codes != list(EXPECTED_SELECTED_CODES)):
        raise ValueError("current frozen inputs select unexpected v4.2 holdout codes")
    return {
        "version": "v4.2-holdout-2026-07-21",
        "methodology": {"path": METHODOLOGY_PATH, "section": "13"},
        "selection": {
            "labor_share_order": "ascending frozen legacy labor_share, then lexicographic NAICS",
            "normalization_boundary": NORMALIZED_DATASET_DIRECTORY,
            "bin_count": 5,
            "binning": "five contiguous balanced bins; leading bins receive the remainder",
            "salt": SALT,
            "hash": "lowercase SHA-256 UTF-8(salt + naics)",
            "winner": "lexicographically smallest lowercase hash in each bin",
        },
        "exclusions": {
            "golden_codes": golden,
            "disclosed_development_codes": development,
            "generated_prior_economic_output_codes": prior_outputs,
            "prefreeze_v4_2_result_codes": prefreeze_v4_2,
            "excluded_unique_codes": sorted(excluded),
        },
        "eligible_inputs": rows,
        "bins": bins,
        "selected_codes": selected_codes,
        "source_digests": source_digests,
    }


def _write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(content)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=REPO)
    parser.add_argument("--output", default=OUTPUT_PATH)
    parser.add_argument("--check", action="store_true")
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
            print("OK: v4.2 holdout membership reproduces byte-identically")
        else:
            _write(output_path, content)
            print("OK: wrote v4.2 holdout membership: %s" % args.output)
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print("V4.2 HOLDOUT FAILED: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
