#!/usr/bin/env python3
"""Keep the README Phase-4 snapshot coupled to generated campaign outputs."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
START = "<!-- DASHBOARD_STATS_START -->"
END = "<!-- DASHBOARD_STATS_END -->"


def load(name):
    return json.loads((ROOT / "pipeline" / "build" / name).read_text())


def snapshot():
    stats = load("stats.json")
    campaign = load("campaign_report_v3_1_2.json")
    golden = load("golden_analysis_v3_1_2.json")
    verdicts = stats["verdict_counts"]
    confidence = stats["confidence_distribution"]
    support = campaign["source_support"]
    return "\n".join([
        START,
        "This block is derived from `pipeline/build/stats.json`, `campaign_report_v3_1_2.json`, and `golden_analysis_v3_1_2.json` by `pipeline/build/update_dashboard_docs.py`.",
        "",
        "- Campaign: closed and complete; %d planned records independently reviewed" % campaign["planned"]["total"],
        "- Attempts: %d total, including %d bounded remediations" % (campaign["attempt_counts"]["total"], campaign["attempt_counts"]["remediation"]),
        "- Publication: %d records published with caveats; %d fleet record excluded" % (campaign["published"], campaign["excluded"]),
        "- Fleet dashboard: %d published records — %d conditional, %d pass, %d kill" % (stats["published"], verdicts.get("conditional", 0), verdicts.get("pass", 0), verdicts.get("kill", 0)),
        "- Fleet confidence: %d MED, %d LOW; %d borderline records" % (confidence.get("MED", 0), confidence.get("LOW", 0), stats["borderline_count"]),
        "- Source review: %d supported, %d partially supported, %d not score-driving" % (support["supported"], support["partially_supported"], support["not_score_driving"]),
        "- Golden diagnostic: separation %s; %d/%d mechanics-clean and published with caveats" % ("PASS" if golden["separation_pass"] else "FAIL", golden["review_outcome_counts"]["publishable_with_caveats"], len(golden["records"])),
        "- Frozen scoring model: thresholds version %s" % stats["thresholds_version"],
        END,
    ])


def updated_readme():
    text = README.read_text()
    before, remainder = text.split(START, 1)
    _current, after = remainder.split(END, 1)
    return before + snapshot() + after


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail when the generated snapshot is stale")
    args = parser.parse_args()
    current = README.read_text()
    expected = updated_readme()
    if args.check:
        if current != expected:
            raise SystemExit("README dashboard snapshot is stale; run update_dashboard_docs.py")
        print("README dashboard snapshot matches generated Phase-4 outputs")
        return
    README.write_text(expected)
    print("updated %s" % README.relative_to(ROOT))


if __name__ == "__main__":
    main()
