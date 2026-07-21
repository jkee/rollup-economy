#!/usr/bin/env python3
"""Diagnostic golden separation for the closed v3.1.2 campaign.

Mechanics failures are fatal. Separation is reported, not used as a retry gate.
"""

import json
import os
import sys

import review_campaign_v3_1_2 as campaign


HERE = os.path.dirname(os.path.abspath(__file__))
OUT_JSON = os.path.join(HERE, "golden_analysis_v3_1_2.json")
OUT_MD = os.path.join(HERE, "golden_analysis_v3_1_2.md")


def analyze(repo_root=campaign.REPO, manifest_path=campaign.MANIFEST):
    manifest = campaign.load_json(manifest_path)
    classes = {
        item["naics"]: item["class"]
        for item in campaign.load_json(
            os.path.join(repo_root, "pipeline", "golden", "golden_set.json")
        )["codes"]
    }
    entries = [item for item in manifest["records"] if item["kind"] == "golden"]
    errors, rows = [], []
    if len(entries) != 20 or {item["naics"] for item in entries} != set(classes):
        errors.append("golden manifest membership must exactly match all 20 frozen codes")
    for entry in entries:
        errors.extend(campaign.validate_artifact(entry, repo_root))
        record = campaign.load_json(os.path.join(repo_root, entry["record_path"]))
        review_path = os.path.join(repo_root, entry["review_path"])
        outcome = campaign.load_json(review_path)["outcome"] if os.path.isfile(review_path) else "missing"
        rows.append({
            "naics": entry["naics"], "class": classes[entry["naics"]],
            "title": record["title"], "S": record["S"],
            "terminal": record["cross_checks"]["terminal_value"]["class"],
            "confidence": record["confidence_overall"],
            "verdict": record["decision"]["verdict"], "review_outcome": outcome,
        })
    rows.sort(key=lambda item: (-item["S"], item["naics"]))
    tier = {"kill": 0, "pass": 1, "conditional": 2, "strong": 3, "hell_yes": 4}
    melters = [item for item in rows if item["class"] == "melter"]
    uncaught = [item["naics"] for item in melters if not (
        item["terminal"] == "MELTING" or item["confidence"] == "LOW"
        or item["verdict"] in ("pass", "kill")
    )]
    winners = [item for item in rows if item["class"] == "winner"]
    top_winner = max((tier[item["verdict"]] for item in winners), default=-1)
    melters_at_or_above = [item["naics"] for item in melters if tier[item["verdict"]] >= top_winner]
    separation_pass = not uncaught and not melters_at_or_above
    return {
        "analysis_version": "golden-analysis-3.1.2",
        "diagnostic_only": True,
        "mechanics_errors": errors,
        "separation_pass": separation_pass,
        "uncaught_melters": uncaught,
        "melters_at_or_above_top_winner_tier": melters_at_or_above,
        "verdict_counts": {name: sum(item["verdict"] == name for item in rows) for name in tier},
        "review_outcome_counts": {name: sum(item["review_outcome"] == name for item in rows) for name in ("publishable", "publishable_with_caveats", "reject", "invalid", "missing")},
        "records": rows,
    }


def render(result):
    lines = ["# v3.1.2 golden analysis", "", "Diagnostic only: separation does not trigger retries.", "", "**Mechanics:** %s  " % ("PASS" if not result["mechanics_errors"] else "FAIL"), "**Separation:** %s" % ("PASS" if result["separation_pass"] else "FAIL"), "", "| NAICS | Class | S | Terminal | Confidence | Verdict | Publication tier |", "|---|---|---:|---|---|---|---|"]
    for item in result["records"]:
        lines.append("| %s | %s | %.3f | %s | %s | %s | %s |" % (item["naics"], item["class"], item["S"], item["terminal"], item["confidence"], item["verdict"], item["review_outcome"]))
    lines.extend(["", "Uncaught melters: %s" % (", ".join(result["uncaught_melters"]) or "none"), "", "Melters at/above top winner tier: %s" % (", ".join(result["melters_at_or_above_top_winner_tier"]) or "none"), ""])
    return "\n".join(lines)


def main():
    result = analyze()
    campaign.write_json(OUT_JSON, result)
    with open(OUT_MD, "w", encoding="utf-8") as handle:
        handle.write(render(result))
    print("golden mechanics=%s separation=%s (diagnostic only)" % ("PASS" if not result["mechanics_errors"] else "FAIL", "PASS" if result["separation_pass"] else "FAIL"))
    if result["mechanics_errors"]:
        for error in result["mechanics_errors"]:
            print("  " + error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
