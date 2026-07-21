#!/usr/bin/env python3
"""Build reviewed v4 records into dashboard data and a campaign summary."""

import argparse
import importlib.util
import json
import os
import sys
from collections import Counter, defaultdict


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
PUBLISHABLE = {"publishable", "publishable_with_caveats"}


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


campaign = load_module("v4_build_campaign", "campaign_v4.py")


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path, value):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def _selected_entries(manifest):
    grouped = defaultdict(list)
    for entry in manifest["entries"]:
        grouped[(entry["kind"], entry["naics"])].append(entry)
    selected = []
    for key, entries in sorted(grouped.items()):
        attempts = sorted(entries, key=lambda item: (item["attempt"], item["run_id"]))
        selected.append(attempts[-1])
    return selected


def _publication_caveats(record, review):
    authored = campaign.finalizer.declared_caveats(record)
    return authored + [item for item in review.get("publication_caveats", []) if item not in authored]


def build(manifest_path, require_complete=True):
    validation_errors = campaign.validate(manifest_path, require_review=True)
    if validation_errors:
        return None, validation_errors
    manifest = load_json(manifest_path)
    selected = _selected_entries(manifest)
    fleet, golden, excluded = [], [], []
    all_attempts = []
    source_support = Counter()

    for entry in manifest["entries"]:
        review = load_json(os.path.join(REPO, entry["review_path"]))
        all_attempts.append({
            "kind": entry["kind"], "naics": entry["naics"], "run_id": entry["run_id"],
            "attempt": entry["attempt"], "outcome": review["outcome"],
        })
        source_support.update(item["support"] for item in review["source_reviews"])

    for entry in selected:
        record = load_json(os.path.join(REPO, entry["record_path"]))
        review = load_json(os.path.join(REPO, entry["review_path"]))
        if review["outcome"] not in PUBLISHABLE:
            excluded.append({
                "kind": entry["kind"], "naics": entry["naics"], "title": record["title"],
                "run_id": entry["run_id"], "outcome": review["outcome"],
                "summary": review["summary"], "findings": review["findings"],
            })
            continue
        output = {
            **record,
            "acceptance": {
                "outcome": review["outcome"],
                "review_meta": review["review_meta"],
                "summary": review["summary"],
            },
            "publication_caveats": _publication_caveats(record, review),
            "artifacts": {
                "packet": entry["packet_path"], "record": entry["record_path"],
                "memo": entry["memo_path"], "review": entry["review_path"],
            },
        }
        (fleet if entry["kind"] == "fleet" else golden).append(output)

    fleet.sort(key=lambda item: (-item["S"]["base"], item["naics"]))
    count = len(fleet)
    for index, record in enumerate(fleet):
        record["rank"] = index + 1
        record["percentile"] = 100.0 if count <= 1 else 100.0 * (count - 1 - index) / (count - 1)
    golden.sort(key=lambda item: (-item["S"]["base"], item["naics"]))

    expected_fleet, expected_golden = campaign.expected_codes(manifest["scope"])
    selected_codes = {
        "fleet": {entry["naics"] for entry in selected if entry["kind"] == "fleet"},
        "golden": {entry["naics"] for entry in selected if entry["kind"] == "golden"},
    }
    completeness = {
        "fleet_expected": len(expected_fleet), "fleet_attempted": len(selected_codes["fleet"]),
        "golden_expected": len(expected_golden), "golden_attempted": len(selected_codes["golden"]),
    }
    if require_complete and (selected_codes["fleet"] != expected_fleet or selected_codes["golden"] != expected_golden):
        return None, ["campaign membership incomplete: %s" % completeness]

    verdicts = Counter(record["decision"]["economic_verdict"] for record in fleet)
    readiness = Counter(record["decision"]["evidence_readiness"]["status"] for record in fleet)
    actions = Counter(record["decision"]["action"] for record in fleet)
    outcomes = Counter(item["outcome"] for item in all_attempts)
    result = {
        "_generated": "pipeline/build/build_v4.py — GENERATED, never hand-edited",
        "methodology_version": "4.0",
        "thresholds_version": "4.0",
        "manifest_scope": manifest["scope"],
        "complete": selected_codes["fleet"] == expected_fleet and selected_codes["golden"] == expected_golden,
        "records": fleet,
        "golden": golden,
        "excluded": excluded,
        "stats": {
            "completeness": completeness,
            "attempts": len(all_attempts),
            "selected_records": len(selected),
            "published_fleet": len(fleet),
            "published_golden": len(golden),
            "excluded": len(excluded),
            "verdicts": dict(sorted(verdicts.items())),
            "readiness": dict(sorted(readiness.items())),
            "actions": dict(sorted(actions.items())),
            "review_outcomes": dict(sorted(outcomes.items())),
            "source_support": dict(sorted(source_support.items())),
            "cross_tier": sum(record["decision"]["sensitivity"]["cross_tier"] for record in fleet),
        },
        "attempts": all_attempts,
    }
    return result, []


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--allow-partial", action="store_true")
    args = parser.parse_args(argv)
    result, errors = build(args.manifest, require_complete=not args.allow_partial)
    if errors:
        for item in errors:
            print(item, file=sys.stderr)
        return 1
    write_json(args.output, result)
    print("built v4 %s: fleet=%d golden=%d excluded=%d" % (
        result["manifest_scope"], len(result["records"]), len(result["golden"]), len(result["excluded"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
