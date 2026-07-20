#!/usr/bin/env python3
"""Generate and validate the deterministic v3 pilot review campaign.

The manifest freezes the exact 63 current fleet runs plus the 20 golden runs
that Stage 5 must review.  Validation is deliberately separate from build.py:
it covers run-scoped review identity, citation/flag coverage, and semantic
invariants that JSON Schema cannot conveniently express.

Usage:
  python3 pipeline/build/review_campaign.py generate
  python3 pipeline/build/review_campaign.py validate
"""

import argparse
import importlib.util
import json
import os
import re
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
DEFAULT_MANIFEST = os.path.join(HERE, "review_manifest.json")
EXPECTED_FLEET = 63
EXPECTED_GOLDEN = 20
EXPECTED_TOTAL = EXPECTED_FLEET + EXPECTED_GOLDEN
CHECK_NAMES = (
    "sources_exist",
    "figures_match_sources",
    "judgment_inputs_plausible",
    "rubric_consistent",
    "cross_checks_honest",
)
_spec = importlib.util.spec_from_file_location(
    "v3_build_for_review_campaign", os.path.join(HERE, "build.py")
)
build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build)


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path, value):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(value, f, indent=2, sort_keys=False)
        f.write("\n")


def source_audit_pairs(record):
    """Use build.py's canonical full-record citation inventory."""
    return build.source_audit_pairs(record)


def _declared_codes(path, label):
    data = load_json(path)
    raw_codes = data.get("codes")
    if not isinstance(raw_codes, list):
        raise ValueError("%s must contain a codes array: %s" % (label, path))
    codes = []
    for index, item in enumerate(raw_codes):
        code = item.get("naics") if isinstance(item, dict) else item
        if not isinstance(code, str) or not re.fullmatch(r"[0-9]{6}", code):
            raise ValueError("%s codes[%d] has invalid NAICS %r"
                             % (label, index, code))
        codes.append(code)
    duplicates = sorted(code for code in set(codes) if codes.count(code) > 1)
    if duplicates:
        raise ValueError("%s contains duplicate NAICS codes: %s"
                         % (label, duplicates))
    return set(codes)


def assert_exact_membership(actual, expected, label):
    """Raise with a deterministic diff when campaign membership drifts."""
    actual = set(actual)
    expected = set(expected)
    if actual != expected:
        raise ValueError(
            "%s membership mismatch: missing=%s unexpected=%s"
            % (label, sorted(expected - actual), sorted(actual - expected))
        )


def _campaign_entry(repo_root, kind, path, record, thresholds):
    computed, arithmetic_errors, deltas = build.recompute(record)
    if arithmetic_errors:
        raise ValueError("%s has arithmetic errors: %s"
                         % (path, "; ".join(arithmetic_errors)))
    factors = {name: computed[name] for name in ["V", "C", "A", "B", "M"]}
    decision = build.decide(
        computed["S"],
        factors,
        record["cross_checks"]["terminal_value"]["class"],
        record["confidence_overall"],
        thresholds,
    )
    flags = build.record_flags(record, computed, decision, deltas)
    run_id = record["run_meta"]["run_id"]
    naics = record["naics"]
    relpath = os.path.relpath(path, repo_root)
    prompt_path = os.path.join("pipeline", "prompts", naics + ".md")
    dataset_path = os.path.join(
        "pipeline", "datasets", "derived", naics + ".json"
    )
    for dependency_name, dependency_path in (
        ("prompt", prompt_path),
        ("dataset", dataset_path),
    ):
        if not os.path.isfile(os.path.join(repo_root, dependency_path)):
            raise ValueError(
                "%s %s dependency does not exist: %s"
                % (kind, dependency_name, dependency_path)
            )
    return {
        "kind": kind,
        "naics": naics,
        "run_id": run_id,
        "record_path": relpath,
        "prompt_path": prompt_path,
        "dataset_path": dataset_path,
        "review_path": os.path.join(
            "pipeline", "review", naics, run_id + ".json"
        ),
        "stage4_flags": flags,
        "expected_source_audits": source_audit_pairs(record),
    }


def build_manifest(repo_root=DEFAULT_REPO, enforce_pilot_counts=True):
    """Build the in-memory campaign manifest from current repository records."""
    thresholds = load_json(
        os.path.join(repo_root, "pipeline", "build", "thresholds.json")
    )
    runs_dir = os.path.join(repo_root, "pipeline", "runs")
    fleet, _legacy = build.discover_runs(runs_dir)
    fleet_targets = _declared_codes(
        os.path.join(repo_root, "pipeline", "blocks", "targets_phase3.json"),
        "fleet target list",
    )
    assert_exact_membership(fleet, fleet_targets, "fleet records")
    entries = []
    for naics in sorted(fleet):
        path, record = fleet[naics]
        if record.get("naics") != naics:
            raise ValueError("%s record NAICS does not match directory %s"
                             % (path, naics))
        entries.append(_campaign_entry(
            repo_root, "fleet", path, record, thresholds
        ))

    golden_dir = os.path.join(repo_root, "pipeline", "golden")
    golden_paths = [
        os.path.join(golden_dir, name)
        for name in sorted(os.listdir(golden_dir))
        if re.fullmatch(r"[0-9]{6}\.json", name)
    ]
    golden_targets = _declared_codes(
        os.path.join(golden_dir, "golden_set.json"), "golden set"
    )
    assert_exact_membership(
        (os.path.basename(path)[:-5] for path in golden_paths),
        golden_targets,
        "golden records",
    )
    for path in golden_paths:
        record = load_json(path)
        entries.append(_campaign_entry(
            repo_root, "golden", path, record, thresholds
        ))

    counts = {
        "fleet": sum(e["kind"] == "fleet" for e in entries),
        "golden": sum(e["kind"] == "golden" for e in entries),
        "total": len(entries),
    }
    if enforce_pilot_counts and counts != {
        "fleet": EXPECTED_FLEET,
        "golden": EXPECTED_GOLDEN,
        "total": EXPECTED_TOTAL,
    }:
        raise ValueError(
            "pilot must contain exactly %d fleet + %d golden = %d records; got %s"
            % (EXPECTED_FLEET, EXPECTED_GOLDEN, EXPECTED_TOTAL, counts)
        )

    identities = [(e["kind"], e["naics"], e["run_id"]) for e in entries]
    if len(identities) != len(set(identities)):
        raise ValueError("duplicate campaign identity detected")

    return {
        "manifest_version": "review-campaign-1",
        "counts": counts,
        "records": entries,
    }


def generate_manifest(repo_root=DEFAULT_REPO, manifest_path=DEFAULT_MANIFEST):
    manifest = build_manifest(repo_root)
    write_json(manifest_path, manifest)
    return manifest


def _audit_identity(audit):
    if not isinstance(audit, dict):
        return None
    path = audit.get("input_path")
    url = audit.get("url")
    if isinstance(path, str) and isinstance(url, str):
        return path, url
    return None


def _reviewed_flag_identity(item):
    """Support the original string list and strengthened object form."""
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        for key in ("flag", "stage4_flag", "value"):
            if isinstance(item.get(key), str):
                return item[key]
    return None


def review_semantic_errors(review, entry):
    errors = []
    if review.get("naics") != entry["naics"]:
        errors.append("naics %r != manifest %r"
                      % (review.get("naics"), entry["naics"]))
    if review.get("run_id") != entry["run_id"]:
        errors.append("run_id %r != manifest %r"
                      % (review.get("run_id"), entry["run_id"]))

    expected_audits = {
        (item["input_path"], item["url"])
        for item in entry["expected_source_audits"]
    }
    raw_audits = review.get("source_audits")
    if not isinstance(raw_audits, list):
        errors.append("source_audits must be an array")
        raw_audits = []
    actual_audits = [_audit_identity(item) for item in raw_audits]
    if any(item is None for item in actual_audits):
        errors.append("every source_audit needs string input_path and url")
    actual_valid = [item for item in actual_audits if item is not None]
    if len(actual_valid) != len(set(actual_valid)):
        errors.append("source_audits contains duplicate input_path/url pairs")
    actual_set = set(actual_valid)
    missing_audits = sorted(expected_audits - actual_set)
    extra_audits = sorted(actual_set - expected_audits)
    if missing_audits:
        errors.append("missing source audits: %s" % missing_audits)
    if extra_audits:
        errors.append("unexpected source audits: %s" % extra_audits)

    expected_flags = set(entry["stage4_flags"])
    raw_flags = review.get("flags_reviewed")
    if not isinstance(raw_flags, list):
        errors.append("flags_reviewed must be an array")
        raw_flags = []
    actual_flags = [_reviewed_flag_identity(item) for item in raw_flags]
    if any(item is None for item in actual_flags):
        errors.append("every flags_reviewed item must identify its exact flag")
    actual_flag_set = {item for item in actual_flags if item is not None}
    if len([item for item in actual_flags if item is not None]) != len(actual_flag_set):
        errors.append("flags_reviewed contains duplicate flags")
    if actual_flag_set != expected_flags:
        errors.append("flags_reviewed mismatch: missing=%s unexpected=%s"
                      % (sorted(expected_flags - actual_flag_set),
                         sorted(actual_flag_set - expected_flags)))

    checks = review.get("checks")
    check_passes = {}
    if isinstance(checks, dict):
        for name in CHECK_NAMES:
            item = checks.get(name)
            if isinstance(item, dict) and isinstance(item.get("pass"), bool):
                check_passes[name] = item["pass"]
    verdict = review.get("verdict")
    reasons = review.get("reasons")
    actionable_reasons = (
        isinstance(reasons, list)
        and bool(reasons)
        and all(isinstance(reason, str) and reason.strip() for reason in reasons)
    )
    audit_failures = [
        audit for audit in raw_audits
        if isinstance(audit, dict)
        and (audit.get("resolves") is not True
             or audit.get("claim_supported") is not True)
    ]

    if verdict == "accepted":
        if set(check_passes) != set(CHECK_NAMES) or not all(check_passes.values()):
            errors.append("accepted requires all five checks to pass")
        if audit_failures:
            errors.append("accepted requires every source audit to resolve and support its claim")
        if reasons != []:
            errors.append("accepted requires an empty reasons array")
    elif verdict == "wrong":
        if not actionable_reasons:
            errors.append("wrong requires non-empty actionable reasons")
        if not (any(value is False for value in check_passes.values())
                or audit_failures):
            errors.append("wrong requires at least one failed check or source audit")
    return errors


def validate_campaign(repo_root=DEFAULT_REPO, manifest_path=DEFAULT_MANIFEST,
                      review_dir=None, schema_path=None, check_freshness=True):
    """Validate every run-scoped review and return counts plus named errors."""
    review_dir = review_dir or os.path.join(repo_root, "pipeline", "review")
    schema_path = schema_path or os.path.join(
        repo_root, "pipeline", "build", "schemas", "review_record.schema.json"
    )
    manifest = load_json(manifest_path)
    errors = []
    if check_freshness:
        expected = build_manifest(repo_root)
        if manifest != expected:
            errors.append(
                "manifest is stale; run review_campaign.py generate before validating"
            )

    schema = load_json(schema_path)
    counts = {"missing": 0, "accepted": 0, "wrong": 0, "invalid": 0}
    seen_review_paths = set()
    for entry in manifest.get("records", []):
        review_path = os.path.join(repo_root, entry["review_path"])
        if review_dir != os.path.join(repo_root, "pipeline", "review"):
            review_path = os.path.join(
                review_dir, entry["naics"], entry["run_id"] + ".json"
            )
        seen_review_paths.add(os.path.abspath(review_path))
        label = "%s/%s/%s" % (
            entry.get("kind"), entry.get("naics"), entry.get("run_id")
        )
        if not os.path.isfile(review_path):
            counts["missing"] += 1
            continue
        try:
            review = load_json(review_path)
        except (OSError, ValueError) as exc:
            counts["invalid"] += 1
            errors.append("%s: unreadable review: %s" % (label, exc))
            continue
        record_errors = build.schema_errors(review, schema, schema)
        record_errors.extend(review_semantic_errors(review, entry))
        if record_errors:
            counts["invalid"] += 1
            errors.extend("%s: %s" % (label, error)
                          for error in record_errors)
            continue
        counts[review["verdict"]] += 1

    if os.path.isdir(review_dir):
        for root, _dirs, files in os.walk(review_dir):
            for name in files:
                if not name.endswith(".json"):
                    continue
                path = os.path.abspath(os.path.join(root, name))
                # The legacy bootstrap is intentionally outside this campaign.
                if path not in seen_review_paths and root != review_dir:
                    errors.append("unmanifested run-scoped review: %s"
                                  % os.path.relpath(path, repo_root))

    return {"counts": counts, "errors": errors}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=DEFAULT_REPO)
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("generate")
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--review-dir")
    validate_parser.add_argument("--schema")
    validate_parser.add_argument(
        "--allow-missing",
        action="store_true",
        help="return success for a valid but incomplete progress sweep",
    )
    args = parser.parse_args(argv)

    if args.command == "generate":
        manifest = generate_manifest(args.repo_root, args.manifest)
        print("generated %s: fleet=%d golden=%d total=%d"
              % (os.path.relpath(args.manifest, args.repo_root),
                 manifest["counts"]["fleet"],
                 manifest["counts"]["golden"],
                 manifest["counts"]["total"]))
        return 0

    result = validate_campaign(
        repo_root=args.repo_root,
        manifest_path=args.manifest,
        review_dir=args.review_dir,
        schema_path=args.schema,
    )
    counts = result["counts"]
    print("reviews: missing=%d accepted=%d wrong=%d invalid=%d"
          % (counts["missing"], counts["accepted"],
             counts["wrong"], counts["invalid"]))
    for error in result["errors"]:
        print("ERROR: %s" % error)
    incomplete = counts["missing"] and not args.allow_missing
    return 1 if result["errors"] or counts["invalid"] or incomplete else 0


if __name__ == "__main__":
    sys.exit(main())
