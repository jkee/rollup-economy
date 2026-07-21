#!/usr/bin/env python3
"""Generate, validate and close the bounded v3.1.2 Phase-4 campaign."""

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
from collections import Counter


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SCHEMAS = os.path.join(HERE, "schemas")
MANIFEST = os.path.join(HERE, "review_manifest_v3_1_2.json")
REPORT_JSON = os.path.join(HERE, "campaign_report_v3_1_2.json")
REPORT_MD = os.path.join(HERE, "campaign_report_v3_1_2.md")


def _load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


build = _load_module("build_v312_campaign", "build.py")
finalizer = _load_module("finalizer_v312_campaign", "finalize_run_v3_1_2.py")


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path, value):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def target_codes(path):
    data = load_json(path)
    codes = []
    for item in data["codes"]:
        code = item.get("naics") if isinstance(item, dict) else item
        if not isinstance(code, str) or not re.fullmatch(r"[0-9]{6}", code):
            raise ValueError("invalid target code %r in %s" % (code, path))
        codes.append(code)
    if len(codes) != len(set(codes)):
        raise ValueError("duplicate target codes in %s" % path)
    return set(codes)


def discover_versioned(root):
    latest, histories = {}, {}
    if not os.path.isdir(root):
        return latest, histories
    for code in sorted(os.listdir(root)):
        directory = os.path.join(root, code)
        if not (re.fullmatch(r"[0-9]{6}", code) and os.path.isdir(directory)):
            continue
        rows = []
        for name in sorted(os.listdir(directory)):
            if not name.endswith(".json"):
                continue
            path = os.path.join(directory, name)
            record = load_json(path)
            meta = record.get("run_meta", {})
            if meta.get("template_version") != "3.1.2":
                continue
            rows.append((str(meta.get("run_date", "")), str(meta.get("run_id", "")), path, record))
        if rows:
            rows.sort(key=lambda row: (row[3].get("run_meta", {}).get("attempt", 0), row[0], row[1]))
            latest[code] = rows[-1][2:]
            histories[code] = rows
    return latest, histories


def validate_history(kind, code, history, repo_root):
    errors = []
    if len(history) > 2:
        errors.append("%s/%s has %d v3.1.2 attempts; maximum is 2" % (kind, code, len(history)))
    attempts = [row[3].get("run_meta", {}).get("attempt") for row in history]
    if attempts and attempts[0] != 1:
        errors.append("%s/%s first artifact must be attempt 1" % (kind, code))
    if len(attempts) == 2 and attempts != [1, 2]:
        errors.append("%s/%s attempt sequence must be [1, 2]" % (kind, code))
    if len(history) == 2:
        first_id = history[0][3]["run_meta"]["run_id"]
        second = history[1][3]
        if second["run_meta"].get("remediates_run_id") != first_id:
            errors.append("%s/%s attempt 2 does not bind attempt 1" % (kind, code))
        prior_review_path = os.path.join(repo_root, "pipeline", "review", code, first_id + ".json")
        if not os.path.isfile(prior_review_path):
            errors.append("%s/%s attempt 2 lacks prior exact-run review" % (kind, code))
        else:
            prior = load_json(prior_review_path)
            prior_entry = artifact_entry(kind, code, history[0][2], history[0][3], repo_root)
            review_schema = load_json(os.path.join(SCHEMAS, "review_record_v3_1_2.schema.json"))
            prior_errors = review_errors(prior, prior_entry, review_schema)
            errors.extend(
                "%s/%s prior review invalid: %s" % (kind, code, item)
                for item in prior_errors
            )
            if not prior_errors and prior.get("outcome") not in ("reject", "invalid"):
                errors.append("%s/%s attempt 2 is forbidden after %r" % (kind, code, prior.get("outcome")))
    return errors


def artifact_entry(kind, code, path, record, repo_root):
    run_id = record["run_meta"]["run_id"]
    packet_path = os.path.join(repo_root, "pipeline", "packets", code, run_id + ".json")
    memo_path = os.path.join(repo_root, "pipeline", "memos", code, run_id + ".md")
    for dependency in (path, packet_path, memo_path):
        if not os.path.isfile(dependency):
            raise ValueError("missing v3.1.2 artifact: %s" % dependency)
    return {
        "kind": kind,
        "naics": code,
        "run_id": run_id,
        "attempt": record["run_meta"]["attempt"],
        "packet_path": os.path.join("pipeline", "packets", code, run_id + ".json"),
        "record_path": os.path.relpath(path, repo_root),
        "dataset_path": os.path.join("pipeline", "datasets", "derived", code + ".json"),
        "memo_path": os.path.join("pipeline", "memos", code, run_id + ".md"),
        "review_path": os.path.join("pipeline", "review", code, run_id + ".json"),
        "source_registry": [
            {
                "source_id": item["id"],
                "url": item["url"],
                "score_driving": item["id"] in build.v312_score_driving_source_ids(record),
            }
            for item in record["sources"]
        ],
        "declared_caveats": build.v312_declared_caveats(record),
        "required_research_model_id": "gpt-5.6-terra" if kind == "fleet" else "gpt-5.6-sol",
        "required_validator_model_id": "gpt-5.6-sol",
        "required_validator_prompt_version": "validator-3.1.2",
        "artifact_digests": {
            "packet_sha256": build.sha256_file(packet_path),
            "run_sha256": build.sha256_file(path),
            "memo_sha256": build.sha256_file(memo_path),
        },
    }


def build_manifest(repo_root=REPO, allow_partial=False):
    fleet, fleet_histories = discover_versioned(os.path.join(repo_root, "pipeline", "runs"))
    golden, golden_histories = discover_versioned(os.path.join(repo_root, "pipeline", "golden_v3_1_2"))
    fleet_targets = target_codes(os.path.join(repo_root, "pipeline", "blocks", "targets_phase3.json"))
    golden_targets = target_codes(os.path.join(repo_root, "pipeline", "golden", "golden_set.json"))
    errors = []
    for kind, records, histories, targets in (
        ("fleet", fleet, fleet_histories, fleet_targets),
        ("golden", golden, golden_histories, golden_targets),
    ):
        unexpected = sorted(set(records) - targets)
        if unexpected:
            errors.append("%s has unexpected codes %s" % (kind, unexpected))
        if not allow_partial:
            missing = sorted(targets - set(records))
            if missing:
                errors.append("%s missing codes %s" % (kind, missing))
        for code, history in histories.items():
            errors.extend(validate_history(kind, code, history, repo_root))
    if errors:
        raise ValueError("; ".join(errors))
    entries = []
    attempt_entries = []
    for kind, records, histories in (
        ("fleet", fleet, fleet_histories), ("golden", golden, golden_histories)
    ):
        for code in sorted(records):
            path, record = records[code]
            entries.append(artifact_entry(kind, code, path, record, repo_root))
        for code in sorted(histories):
            for _date, _run_id, path, record in histories[code]:
                attempt_entries.append(artifact_entry(kind, code, path, record, repo_root))
    identities = [(item["naics"], item["run_id"]) for item in attempt_entries]
    if len(identities) != len(set(identities)):
        raise ValueError("fleet/golden packet, memo and review paths collide")
    counts = {"fleet": sum(item["kind"] == "fleet" for item in entries), "golden": sum(item["kind"] == "golden" for item in entries), "total": len(entries)}
    if not allow_partial and counts != {"fleet": 63, "golden": 20, "total": 83}:
        raise ValueError("campaign requires 63 fleet + 20 golden; got %s" % counts)
    attempt_counts = {
        "initial": sum(item["attempt"] == 1 for item in attempt_entries),
        "remediation": sum(item["attempt"] == 2 for item in attempt_entries),
        "total": len(attempt_entries),
    }
    return {
        "manifest_version": "review-campaign-3.1.2",
        "bounded_attempts_per_record": 2,
        "counts": counts,
        "attempt_counts": attempt_counts,
        "attempts": attempt_entries,
        "records": entries,
    }


def validate_artifact(entry, repo_root):
    label = "%s/%s/%s" % (entry["kind"], entry["naics"], entry["run_id"])
    errors = []
    paths = {name: os.path.join(repo_root, entry[name]) for name in ("packet_path", "record_path", "dataset_path", "memo_path")}
    for name, path in paths.items():
        if not os.path.isfile(path):
            errors.append("%s missing %s: %s" % (label, name, path))
    if errors:
        return errors
    packet, record, dataset = load_json(paths["packet_path"]), load_json(paths["record_path"]), load_json(paths["dataset_path"])
    actual_digests = {
        "packet_sha256": build.sha256_file(paths["packet_path"]),
        "run_sha256": build.sha256_file(paths["record_path"]),
        "memo_sha256": build.sha256_file(paths["memo_path"]),
    }
    if actual_digests != entry.get("artifact_digests"):
        errors.append("%s artifact bytes differ from frozen manifest digests" % label)
    packet_schema = load_json(os.path.join(SCHEMAS, "research_packet_v3_1_2.schema.json"))
    run_schema = load_json(os.path.join(SCHEMAS, "run_record_v3_1_2.schema.json"))
    errors.extend("%s packet: %s" % (label, item) for item in build.schema_errors(packet, packet_schema, packet_schema))
    errors.extend("%s run: %s" % (label, item) for item in build.schema_errors(record, run_schema, run_schema))
    if packet.get("naics") != entry["naics"] or record.get("naics") != entry["naics"]:
        errors.append("%s NAICS identity mismatch" % label)
    if packet.get("run_meta", {}).get("run_id") != entry["run_id"] or record.get("run_meta", {}).get("run_id") != entry["run_id"]:
        errors.append("%s run identity mismatch" % label)
    if packet.get("run_meta", {}).get("model_id") != entry["required_research_model_id"]:
        errors.append("%s research model route mismatch" % label)
    fresh, final_errors = finalizer.finalize(packet, dataset, entry["kind"])
    errors.extend("%s fresh finalization: %s" % (label, item) for item in final_errors)
    with open(paths["record_path"], "rb") as handle:
        record_bytes = handle.read()
    if fresh is not None and finalizer.serialize_record(fresh) != record_bytes:
        errors.append("%s finalized record bytes differ from fresh finalization" % label)
    with open(paths["memo_path"], "r", encoding="utf-8") as handle:
        memo = handle.read()
    if fresh is not None and finalizer.render_memo(fresh) != memo:
        errors.append("%s memo differs from fresh deterministic rendering" % label)
    _computed, arithmetic_errors, _deltas = build.recompute(record) if not build.schema_errors(record, run_schema, run_schema) else ({}, [], {})
    errors.extend("%s arithmetic: %s" % (label, item) for item in arithmetic_errors)
    driving = build.v312_score_driving_source_ids(record)
    actual_registry = [
        {"source_id": item["id"], "url": item["url"], "score_driving": item["id"] in driving}
        for item in record.get("sources", [])
    ]
    if actual_registry != entry["source_registry"]:
        errors.append("%s source registry differs from manifest" % label)
    return errors


def review_errors(review, entry, schema):
    errors = build.schema_errors(review, schema, schema)
    if review.get("naics") != entry["naics"]:
        errors.append("review NAICS mismatch")
    if review.get("run_id") != entry["run_id"]:
        errors.append("review run ID mismatch")
    if review.get("artifact_digests") != entry.get("artifact_digests"):
        errors.append("review artifact digests do not match frozen exact bytes")
    meta = review.get("review_meta", {})
    if meta.get("model_id") != entry["required_validator_model_id"]:
        errors.append("validator model mismatch")
    if meta.get("prompt_version") != entry["required_validator_prompt_version"]:
        errors.append("validator prompt mismatch")
    actual = [(item.get("source_id"), item.get("url")) for item in review.get("source_reviews", []) if isinstance(item, dict)]
    expected = [(item["source_id"], item["url"]) for item in entry["source_registry"]]
    if len(actual) != len(set(actual)) or set(actual) != set(expected):
        errors.append("source review coverage mismatch")
    mechanics = review.get("mechanics", {})
    mechanics_ok = bool(mechanics) and all(value is True for value in mechanics.values())
    findings = review.get("findings", [])
    severities = [item.get("severity") for item in findings if isinstance(item, dict)]
    outcome = review.get("outcome")
    expected_driving = {item["source_id"]: item["score_driving"] for item in entry["source_registry"]}
    source_review_by_id = {item.get("source_id"): item for item in review.get("source_reviews", []) if isinstance(item, dict)}
    for source_id, value in expected_driving.items():
        if source_review_by_id.get(source_id, {}).get("score_driving") is not value:
            errors.append("source %s score_driving mismatch" % source_id)
    declared_caveats = entry.get("declared_caveats", [])
    publication_caveats = review.get("publication_caveats", [])
    if set(declared_caveats) - set(publication_caveats):
        errors.append("publication_caveats omit authored score-input caveats")
    driving_failures = [
        item for source_id, item in source_review_by_id.items()
        if expected_driving.get(source_id)
        and (item.get("accessible") is not True
             or item.get("support") in ("unsupported", "not_score_driving"))
    ]
    caveat_finding_text = [item.get("publication_caveat") for item in findings if isinstance(item, dict) and item.get("severity") == "caveat"]
    if any(not value or value not in publication_caveats for value in caveat_finding_text):
        errors.append("every caveat finding must be copied to publication_caveats")
    if driving_failures and mechanics_ok and outcome != "reject":
        errors.append("inaccessible/unsupported score-driving evidence requires reject")
    if (not mechanics_ok or "fatal_mechanics" in severities) and outcome != "invalid":
        errors.append("failed mechanics requires invalid")
    if outcome == "publishable" and (not mechanics_ok or findings or publication_caveats or declared_caveats):
        errors.append("publishable requires mechanics pass and no findings/caveats")
    if outcome == "publishable_with_caveats" and (not mechanics_ok or any(item != "caveat" for item in severities) or not publication_caveats):
        errors.append("publishable_with_caveats requires mechanics pass and caveat-only findings")
    if outcome == "reject" and (not mechanics_ok or "material" not in severities):
        errors.append("reject requires mechanics pass and a material finding")
    if outcome == "reject" and "fatal_mechanics" in severities:
        errors.append("fatal_mechanics requires invalid, never reject")
    if outcome == "invalid" and mechanics_ok and "fatal_mechanics" not in severities:
        errors.append("invalid requires failed mechanics or fatal finding")
    if outcome in ("publishable", "publishable_with_caveats") and any(item in ("material", "fatal_mechanics") for item in severities):
        errors.append("publishable outcome contains material/fatal finding")
    return errors


def validate_campaign(repo_root=REPO, manifest_path=MANIFEST, allow_missing=False, check_freshness=True):
    manifest = load_json(manifest_path)
    errors = []
    partial = manifest.get("counts", {}).get("total", 0) != 83
    if check_freshness:
        expected = build_manifest(repo_root, allow_partial=partial)
        if manifest != expected:
            errors.append("manifest is stale")
    review_schema = load_json(os.path.join(SCHEMAS, "review_record_v3_1_2.schema.json"))
    attempt_outcomes = Counter()
    valid_reviews = {}
    for entry in manifest.get("attempts", []):
        errors.extend(validate_artifact(entry, repo_root))
        path = os.path.join(repo_root, entry["review_path"])
        if not os.path.isfile(path):
            attempt_outcomes["missing"] += 1
            if not allow_missing:
                errors.append("missing review: %s" % entry["review_path"])
            continue
        review = load_json(path)
        item_errors = review_errors(review, entry, review_schema)
        if item_errors:
            attempt_outcomes["invalid_review"] += 1
            errors.extend("%s/%s: %s" % (entry["naics"], entry["run_id"], item) for item in item_errors)
        else:
            attempt_outcomes[review["outcome"]] += 1
            valid_reviews[(entry["kind"], entry["naics"], entry["run_id"])] = review
    final_outcomes = Counter()
    for entry in manifest.get("records", []):
        review = valid_reviews.get((entry["kind"], entry["naics"], entry["run_id"]))
        final_outcomes[review["outcome"] if review else "missing_or_invalid"] += 1
    for key in ("publishable", "publishable_with_caveats", "reject", "invalid", "missing", "invalid_review"):
        attempt_outcomes.setdefault(key, 0)
    for key in ("publishable", "publishable_with_caveats", "reject", "invalid", "missing_or_invalid"):
        final_outcomes.setdefault(key, 0)
    return {
        "counts": dict(final_outcomes),
        "attempt_outcomes": dict(attempt_outcomes),
        "errors": errors,
    }


def completion_report(repo_root, manifest):
    rows, outcome_counts, confidence_counts, source_support = [], Counter(), Counter(), Counter()
    caveats, exclusions = [], []
    for entry in manifest["records"]:
        record = load_json(os.path.join(repo_root, entry["record_path"]))
        review = load_json(os.path.join(repo_root, entry["review_path"]))
        outcome = review["outcome"]
        outcome_counts[outcome] += 1
        confidence_counts[record["confidence_overall"]] += 1
        for source in review["source_reviews"]:
            source_support[source["support"]] += 1
        item = {"kind": entry["kind"], "naics": entry["naics"], "run_id": entry["run_id"], "attempt": entry["attempt"], "outcome": outcome, "confidence": record["confidence_overall"], "S": record["S"], "verdict": record["decision"]["verdict"], "publication_caveats": review["publication_caveats"]}
        rows.append(item)
        if outcome == "publishable_with_caveats":
            caveats.append({"naics": entry["naics"], "run_id": entry["run_id"], "caveats": review["publication_caveats"]})
        if outcome in ("reject", "invalid"):
            exclusions.append({"kind": entry["kind"], "naics": entry["naics"], "run_id": entry["run_id"], "attempt": entry["attempt"], "outcome": outcome, "summary": review["summary"], "findings": review["findings"]})
    attempts = []
    attempt_outcomes = Counter()
    for entry in manifest["attempts"]:
        review = load_json(os.path.join(repo_root, entry["review_path"]))
        attempt_outcomes[review["outcome"]] += 1
        attempts.append({
            "kind": entry["kind"], "naics": entry["naics"],
            "run_id": entry["run_id"], "attempt": entry["attempt"],
            "outcome": review["outcome"], "summary": review["summary"],
            "findings": review["findings"],
        })
    report = {
        "report_version": "campaign-report-3.1.2",
        "campaign_closed": True,
        "phase4_complete": False,
        "phase4_remaining_actions": [
            "record final build/golden/test/frozen verification in this generated report",
            "update documentation and push validated checkpoint commits to origin",
        ],
        "planned": manifest["counts"],
        "attempt_counts": manifest["attempt_counts"],
        "attempt_outcomes": dict(sorted(attempt_outcomes.items())),
        "review_outcomes": dict(sorted(outcome_counts.items())),
        "confidence_distribution": dict(sorted(confidence_counts.items())),
        "source_support": dict(sorted(source_support.items())),
        "published": sum(outcome_counts[key] for key in ("publishable", "publishable_with_caveats")),
        "excluded": len(exclusions), "caveats": caveats,
        "exclusions": exclusions, "attempts": attempts, "records": rows,
    }
    return report


def render_report(report):
    lines = ["# v3.1.2 Phase-4 campaign completion report", "", "Generated by plain Python; do not hand-edit.", "", "## Exact counts", "", "- Planned: %d fleet + %d golden = %d" % (report["planned"]["fleet"], report["planned"]["golden"], report["planned"]["total"]), "- Attempts: %d initial + %d remediation = %d" % (report["attempt_counts"]["initial"], report["attempt_counts"]["remediation"], report["attempt_counts"]["total"]), "- Published: %d" % report["published"], "- Excluded: %d" % report["excluded"]]
    for name, count in sorted(report["review_outcomes"].items()):
        lines.append("- `%s`: %d" % (name, count))
    lines.extend(["", "## Confidence", ""])
    lines.extend("- `%s`: %d" % item for item in sorted(report["confidence_distribution"].items()))
    lines.extend(["", "## Source support", ""])
    lines.extend("- `%s`: %d" % item for item in sorted(report["source_support"].items()))
    if "golden_analysis" in report:
        lines.extend(["", "## Golden diagnostic", "", "- Mechanics: %s" % ("PASS" if not report["golden_analysis"]["mechanics_errors"] else "FAIL"), "- Separation: %s (diagnostic only)" % ("PASS" if report["golden_analysis"]["separation_pass"] else "FAIL")])
    if "verification" in report:
        lines.extend(["", "## Deterministic verification", ""])
        for item in report["verification"]:
            lines.append("- `%s`: %s" % (item["command"], "PASS" if item["returncode"] == 0 else "FAIL"))
    lines.extend(["", "## Included caveats", ""])
    if report["caveats"]:
        for item in report["caveats"]:
            lines.append("- **%s** (`%s`): %s" % (item["naics"], item["run_id"], "; ".join(item["caveats"])))
    else:
        lines.append("- None.")
    lines.extend(["", "## Exclusions after the bounded remediation wave", ""])
    if report["exclusions"]:
        for item in report["exclusions"]:
            lines.append("- **%s** %s attempt %d (`%s`): %s" % (item["naics"], item["outcome"], item["attempt"], item["run_id"], item["summary"]))
    else:
        lines.append("- None.")
    lines.append("")
    return "\n".join(lines)


def deterministic_verification(repo_root):
    commands = [
        [sys.executable, "pipeline/build/test_v3_1.py"],
        [sys.executable, "pipeline/build/test_v3_1_1.py"],
        [sys.executable, "pipeline/build/test_prompt_v3_1_1.py"],
        [sys.executable, "pipeline/build/test_build.py"],
        [sys.executable, "pipeline/build/test_review_campaign.py"],
        [sys.executable, "pipeline/build/test_v3_1_2.py"],
        [sys.executable, "pipeline/build/assemble_prompts.py", "--check"],
        [sys.executable, "pipeline/build/assemble_prompts.py", "--template-version", "3.1", "--check"],
        [sys.executable, "pipeline/build/assemble_prompts.py", "--template-version", "3.1.1", "--check"],
        [sys.executable, "pipeline/build/assemble_prompts.py", "--template-version", "3.1.2", "--check"],
        ["git", "diff", "--check"],
    ]
    results = []
    for command in commands:
        completed = subprocess.run(command, cwd=repo_root, text=True, capture_output=True)
        results.append({
            "command": " ".join(command), "returncode": completed.returncode,
            "stdout_tail": completed.stdout[-2000:], "stderr_tail": completed.stderr[-2000:],
        })
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=REPO)
    parser.add_argument("--manifest", default=MANIFEST)
    sub = parser.add_subparsers(dest="command", required=True)
    generate = sub.add_parser("generate")
    generate.add_argument("--allow-partial", action="store_true")
    validate = sub.add_parser("validate")
    validate.add_argument("--allow-missing", action="store_true")
    close = sub.add_parser("close")
    args = parser.parse_args(argv)
    if args.command == "generate":
        manifest = build_manifest(args.repo_root, allow_partial=args.allow_partial)
        write_json(args.manifest, manifest)
        print("generated v3.1.2 manifest: %s" % manifest["counts"])
        return 0
    result = validate_campaign(args.repo_root, args.manifest, allow_missing=getattr(args, "allow_missing", False))
    print("v3.1.2 campaign validation: %s" % result["counts"])
    if result["errors"]:
        for error in result["errors"]:
            print("  " + error, file=sys.stderr)
        return 1
    if args.command == "close":
        manifest = load_json(args.manifest)
        if manifest.get("counts") != {"fleet": 63, "golden": 20, "total": 83}:
            print("cannot close a partial campaign", file=sys.stderr)
            return 1
        build_result = build.run_build(args.repo_root)
        if not build_result.get("ok"):
            for error in build_result.get("errors", []):
                print("  " + error, file=sys.stderr)
            return 1
        golden = _load_module("golden_analysis_v312_close", "golden_analysis_v3_1_2.py")
        golden_result = golden.analyze(args.repo_root, args.manifest)
        if golden_result["mechanics_errors"]:
            for error in golden_result["mechanics_errors"]:
                print("  " + error, file=sys.stderr)
            return 1
        write_json(golden.OUT_JSON, golden_result)
        with open(golden.OUT_MD, "w", encoding="utf-8") as handle:
            handle.write(golden.render(golden_result))
        verification = deterministic_verification(args.repo_root)
        if any(item["returncode"] != 0 for item in verification):
            for item in verification:
                if item["returncode"] != 0:
                    print("verification failed: %s\n%s\n%s" % (item["command"], item["stdout_tail"], item["stderr_tail"]), file=sys.stderr)
            return 1
        report = completion_report(args.repo_root, manifest)
        report["build_stats"] = build_result["stats"]
        report["golden_analysis"] = golden_result
        report["verification"] = verification
        report["phase4_remaining_actions"] = [
            "update final documentation and push validated checkpoint commits to origin"
        ]
        write_json(REPORT_JSON, report)
        with open(REPORT_MD, "w", encoding="utf-8") as handle:
            handle.write(render_report(report))
        print("closed campaign: published=%d excluded=%d" % (report["published"], report["excluded"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
