#!/usr/bin/env python3
"""Generate validated statistics for the frozen 20-industry review checkpoint."""

import argparse
import importlib.util
import json
import os
import random
import sys
from collections import Counter


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
CHECKPOINT = os.path.join(HERE, "review_checkpoint_v3_1_2.json")
MANIFEST = os.path.join(HERE, "review_manifest_v3_1_2.json")
OUT_JSON = os.path.join(HERE, "review_statistics_v3_1_2.json")
OUT_MD = os.path.join(HERE, "review_statistics_v3_1_2.md")


def _load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


campaign = _load_module("campaign_v312_review_statistics", "review_campaign_v3_1_2.py")


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path, value):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(serialize_json(value))


def serialize_json(value):
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def collect(repo_root=REPO, checkpoint_path=CHECKPOINT, manifest_path=MANIFEST):
    checkpoint, manifest = load_json(checkpoint_path), load_json(manifest_path)
    checkpoint_entries = checkpoint.get("entries", [])
    codes = [entry.get("naics") for entry in checkpoint_entries]
    errors = []
    if checkpoint.get("target_count") != 20 or len(codes) != 20 or len(set(codes)) != 20:
        errors.append("checkpoint must contain exactly 20 unique codes")
    preselected = checkpoint.get("preselected_codes", [])
    sampling_frame = checkpoint.get("sampling_frame_codes", [])
    sample_size = checkpoint.get("sample_size")
    sampled = checkpoint.get("sampled_codes_in_draw_order", [])
    if (len(preselected) != 5 or len(set(preselected)) != 5 or
            len(sampling_frame) != 31 or len(set(sampling_frame)) != 31 or
            set(preselected) & set(sampling_frame)):
        errors.append("checkpoint selection populations must be 5 disjoint preselected and 31 unique sampling-frame codes")
    if sample_size != 15:
        errors.append("checkpoint sample_size must be 15")
    try:
        expected_sample = random.Random(checkpoint.get("selection_seed")).sample(sorted(sampling_frame), sample_size)
    except (TypeError, ValueError):
        expected_sample = []
        errors.append("checkpoint selection parameters are not reproducible")
    if sampled != expected_sample:
        errors.append("checkpoint sampled codes do not reproduce from the frozen seed and frame")
    if codes != sorted(preselected + expected_sample):
        errors.append("checkpoint entries do not equal the sorted preselected-plus-sampled codes")

    attempts = manifest.get("attempts", [])
    by_identity = {(entry["kind"], entry["naics"], entry["run_id"]): entry for entry in attempts}
    if len(by_identity) != len(attempts):
        errors.append("manifest contains duplicate attempt identities")
    selected_entries = {}
    for frozen in checkpoint_entries:
        identity = (frozen.get("kind"), frozen.get("naics"), frozen.get("run_id"))
        entry = by_identity.get(identity)
        if entry is None:
            errors.append("checkpoint artifact missing from manifest: %s" % (identity,))
            continue
        if frozen.get("artifact_digests") != entry.get("artifact_digests"):
            errors.append("checkpoint artifact digests changed: %s" % (identity,))
        selected_entries[frozen["naics"]] = entry

    review_schema = load_json(os.path.join(HERE, "schemas", "review_record_v3_1_2.schema.json"))
    outcomes, mechanics = Counter(), Counter()
    source_support, source_accessibility, source_role = Counter(), Counter(), Counter()
    finding_severity, finding_category = Counter(), Counter()
    confidence, verdicts = Counter(), Counter()
    rows, missing_reviews, invalid_reviews = [], [], []
    publication_caveats = authored_caveats = validator_caveats = 0

    for code in codes:
        entry = selected_entries.get(code)
        if not entry:
            continue
        artifact_errors = campaign.validate_artifact(entry, repo_root)
        errors.extend(artifact_errors)
        record = load_json(os.path.join(repo_root, entry["record_path"]))
        confidence[record["confidence_overall"]] += 1
        verdicts[record["decision"]["verdict"]] += 1
        review_path = os.path.join(repo_root, entry["review_path"])
        row = {
            "naics": code,
            "run_id": entry["run_id"],
            "S": record["S"],
            "verdict": record["decision"]["verdict"],
            "confidence": record["confidence_overall"],
            "review_status": "missing",
        }
        if not os.path.isfile(review_path):
            missing_reviews.append(code)
            rows.append(row)
            continue
        review = load_json(review_path)
        review_errors = campaign.review_errors(review, entry, review_schema)
        if review_errors:
            invalid_reviews.append(code)
            errors.extend("%s: %s" % (code, item) for item in review_errors)
            row["review_status"] = "invalid_review"
            rows.append(row)
            continue
        row["review_status"] = "valid"
        row["outcome"] = review["outcome"]
        row["source_count"] = len(review["source_reviews"])
        row["publication_caveat_count"] = len(review["publication_caveats"])
        row["finding_count"] = len(review["findings"])
        rows.append(row)
        outcomes[review["outcome"]] += 1
        for name, value in review["mechanics"].items():
            mechanics["%s:%s" % (name, "pass" if value else "fail")] += 1
        for source in review["source_reviews"]:
            source_support[source["support"]] += 1
            source_accessibility["accessible" if source["accessible"] else "inaccessible"] += 1
            source_role["score_driving" if source["score_driving"] else "not_score_driving"] += 1
        for finding in review["findings"]:
            finding_severity[finding["severity"]] += 1
            finding_category[finding["category"]] += 1
        declared = Counter(entry.get("declared_caveats", []))
        published = Counter(review["publication_caveats"])
        publication_caveats += len(review["publication_caveats"])
        authored_caveats += sum((declared & published).values())
        validator_caveats += sum((published - declared).values())

    valid = sum(outcomes.values())
    publishable = outcomes["publishable"] + outcomes["publishable_with_caveats"]
    result = {
        "statistics_version": "review-statistics-3.1.2-v1",
        "checkpoint_version": checkpoint.get("checkpoint_version"),
        "selection_seed": checkpoint.get("selection_seed"),
        "selection_method": checkpoint.get("selection_method"),
        "target_count": 20,
        "reviewed_valid": valid,
        "checkpoint_complete": valid == 20 and not errors,
        "missing_reviews": missing_reviews,
        "invalid_reviews": invalid_reviews,
        "review_outcomes": dict(sorted(outcomes.items())),
        "publishable_count": publishable,
        "publishable_rate": (publishable / valid) if valid else None,
        "remediation_eligible": outcomes["reject"] + outcomes["invalid"],
        "confidence_distribution": dict(sorted(confidence.items())),
        "verdict_distribution": dict(sorted(verdicts.items())),
        "mechanics": dict(sorted(mechanics.items())),
        "source_statistics": {
            "support": dict(sorted(source_support.items())),
            "accessibility": dict(sorted(source_accessibility.items())),
            "score_role": dict(sorted(source_role.items())),
        },
        "finding_severity": dict(sorted(finding_severity.items())),
        "finding_category": dict(sorted(finding_category.items())),
        "publication_caveats": publication_caveats,
        "authored_caveats": authored_caveats,
        "validator_added_caveats": validator_caveats,
        "errors": errors,
        "records": rows,
    }
    return result


def render(result):
    rate = "n/a" if result["publishable_rate"] is None else "%.1f%%" % (100 * result["publishable_rate"])
    lines = [
        "# v3.1.2 20-industry review checkpoint",
        "",
        "Generated by plain Python; do not hand-edit.",
        "",
        "- Reviewed and valid: %d / %d" % (result["reviewed_valid"], result["target_count"]),
        "- Checkpoint complete: %s" % ("yes" if result["checkpoint_complete"] else "no"),
        "- Publishable tiers: %d (%s)" % (result["publishable_count"], rate),
        "- Remediation eligible: %d" % result["remediation_eligible"],
        "- Publication caveats: %d authored + %d validator-added = %d" % (
            result["authored_caveats"], result["validator_added_caveats"], result["publication_caveats"]
        ),
        "",
        "## Review outcomes",
        "",
    ]
    lines.extend("- `%s`: %d" % item for item in sorted(result["review_outcomes"].items()))
    lines.extend(["", "## Source statistics", ""])
    for dimension in ("support", "accessibility", "score_role"):
        lines.append("### %s" % dimension.replace("_", " ").title())
        lines.append("")
        lines.extend("- `%s`: %d" % item for item in sorted(result["source_statistics"][dimension].items()))
        lines.append("")
    lines.extend(["", "## Findings", ""])
    lines.extend("- Severity `%s`: %d" % item for item in sorted(result["finding_severity"].items()))
    lines.extend("- Category `%s`: %d" % item for item in sorted(result["finding_category"].items()))
    lines.extend(["", "## Records", "", "| NAICS | S | Verdict | Confidence | Review |", "|---|---:|---|---|---|"])
    for row in result["records"]:
        lines.append("| %s | %.4f | %s | %s | %s |" % (
            row["naics"], row["S"], row["verdict"], row["confidence"], row.get("outcome", row["review_status"])
        ))
    if result["errors"]:
        lines.extend(["", "## Validation errors", ""])
        lines.extend("- %s" % item for item in result["errors"])
    lines.append("")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=REPO)
    parser.add_argument("--checkpoint", default=CHECKPOINT)
    parser.add_argument("--manifest", default=MANIFEST)
    parser.add_argument("--output-json", default=OUT_JSON)
    parser.add_argument("--output-md", default=OUT_MD)
    parser.add_argument("--check", action="store_true", help="fail if generated outputs are stale")
    args = parser.parse_args(argv)
    result = collect(args.repo_root, args.checkpoint, args.manifest)
    if args.check:
        expected = {args.output_json: serialize_json(result), args.output_md: render(result)}
        stale = []
        for path, value in expected.items():
            if not os.path.isfile(path) or open(path, "r", encoding="utf-8").read() != value:
                stale.append(path)
        if stale:
            print("stale review-statistics output: %s" % ", ".join(stale), file=sys.stderr)
            return 1
    else:
        write_json(args.output_json, result)
        with open(args.output_md, "w", encoding="utf-8") as handle:
            handle.write(render(result))
    print("review checkpoint: %d/%d valid; publishable=%d; errors=%d" % (
        result["reviewed_valid"], result["target_count"], result["publishable_count"], len(result["errors"])
    ))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
