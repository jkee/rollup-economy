#!/usr/bin/env python3
"""Regenerate the v5 dashboard statistics block in README.md."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
DATA = ROOT / "6digit" / "six_data_v5.json"
RUNS = ROOT / "pipeline" / "v5" / "runs"
START = "<!-- DASHBOARD_STATS_START -->"
END = "<!-- DASHBOARD_STATS_END -->"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def render_block() -> str:
    data = load_json(DATA)
    summary = data["summary"]
    review_paths = sorted(RUNS.glob("*/*/review.json"))
    reviews = [load_json(path) for path in review_paths]
    outcomes = Counter(review["outcome"] for review in reviews)
    material_findings = sum(len(review["material_findings"]) for review in reviews)
    paths_by_code: dict[str, list[Path]] = {}
    for path in review_paths:
        paths_by_code.setdefault(path.parents[1].name, []).append(path)
    remediated_codes = [code for code, paths in paths_by_code.items() if len(paths) > 1]
    remediated = len(remediated_codes)
    accepted_outcomes = {"publishable", "publishable_with_caveats"}
    accepted_remediations = sum(
        load_json(sorted(paths_by_code[code])[-1])["outcome"] in accepted_outcomes
        for code in remediated_codes
    )
    tiers = summary["tiers"]
    readiness = summary["readiness"]
    actions = summary["actions"]
    source_audits = Counter(
        audit["support"]
        for record in data["records"]
        for audit in record["review"]["sources_audited"]
    )
    tick = chr(96)
    outcome_text = ", ".join(
        f"{outcomes.get(outcome, 0)} {tick}{outcome}{tick}"
        for outcome in ("publishable", "publishable_with_caveats", "reject", "invalid")
    )

    lines = [
        START,
        "This block is generated from " + tick + "six_data_v5.json" + tick
        + " and the validated review artifacts by "
        + tick + "pipeline/v5/update_docs.py" + tick + ".",
        "",
        f"- Publication: {summary['published']} records published; {summary['excluded']} excluded",
        f"- Reviewed attempts: {len(reviews)} total — {outcome_text}",
        f"- Remediation: {remediated} bounded attempt-2 records; "
        f"{accepted_remediations} accepted",
        f"- Material findings: {material_findings} across all review attempts",
        "- Published source audits: "
        f"{source_audits.get('supported', 0)} supported, "
        f"{source_audits.get('partially_supported', 0)} partially supported, "
        f"{source_audits.get('unsupported', 0)} unsupported, "
        f"{source_audits.get('not_score_driving', 0)} not score-driving",
        "- Tiers: "
        f"{tiers.get('HIGHEST_PRIORITY', 0)} highest priority, "
        f"{tiers.get('PRIORITY', 0)} priority, "
        f"{tiers.get('CONDITIONAL', 0)} conditional, "
        f"{tiers.get('LOW_PRIORITY', 0)} low priority, "
        f"{tiers.get('STRUCTURAL_OUT', 0)} structural out, "
        f"{tiers.get('None', 0)} unscored dataset gaps",
        "- Readiness: "
        f"{readiness.get('MODEL_CONDITIONED', 0)} model-conditioned, "
        f"{readiness.get('STRESS_TEST_ONLY', 0)} stress-test-only",
        "- Actions: "
        f"{actions.get('VALIDATE_ASSUMPTIONS', 0)} validate assumptions, "
        f"{actions.get('EVIDENCE_FIRST', 0)} evidence first",
        f"- Robust tiers: {summary['robust_tiers']}; methodology "
        f"{data['methodology_version']}; unreviewed publication disabled",
        END,
    ]
    return "\n".join(lines)


def expected_readme() -> str:
    current = README.read_text()
    if START not in current or END not in current:
        raise SystemExit("README.md is missing dashboard stats markers")
    start = current.index(START)
    end = current.index(END) + len(END)
    return current[:start] + render_block() + current[end:]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = expected_readme()
    current = README.read_text()
    if args.check:
        if current != expected:
            raise SystemExit("README.md v5 statistics are stale")
        print("README.md v5 statistics are current")
        return
    README.write_text(expected)
    print("updated README.md")


if __name__ == "__main__":
    main()
