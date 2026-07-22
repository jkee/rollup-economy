#!/usr/bin/env python3
"""Render isolated v5.1 researcher and validator assignments, and compute
block validation samples (code-owned; no session ever picks records).

This is campaign plumbing only. It does not alter the frozen methodology,
packet/review contracts, scoring, or publication gate.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
V5 = Path(__file__).resolve().parent
TARGETS = V5 / "targets.json"
DATASETS = ROOT / "pipeline" / "datasets" / "derived"
RUNS = V5 / "runs"

sys.path.insert(0, str(V5))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def compact(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def target(naics: str) -> dict:
    for row in load_json(TARGETS)["codes"]:
        if row["naics"] == naics:
            return row
    raise SystemExit(f"NAICS {naics} is not in {TARGETS.relative_to(ROOT)}")


def dataset_notes(naics: str) -> tuple[str, str]:
    data = load_json(DATASETS / f"{naics}.json")
    labor = data["labor_share"]
    n_band = data["n_band"]
    labor_note = compact(labor.get("method") or labor.get("derivation"))
    if n_band.get("value") is None:
        n_note = (
            "Declared dataset gap: no defensible n_band value. The finalizer will "
            "inject MISSING. Do not research, replace, or estimate n."
        )
    else:
        source = compact(n_band.get("margin_source"))
        n_note = (
            "Margin-bridged from SUSB size-class firm counts and average receipts "
            "into the $1-10M EBITDA band"
            + (f" using {source}" if source else "")
            + "; dataset quality ESTIMATE."
        )
    return (
        f"l = {json.dumps(labor.get('value'))}; quality {labor.get('quality')}; {labor_note}",
        f"n = {json.dumps(n_band.get('value'))}; quality {n_band.get('quality')}; {n_note}",
    )


def research_prompt(
    naics: str,
    run_date: str,
    model_id: str,
    attempt: int,
    findings_path: Path | None,
) -> str:
    row = target(naics)
    if attempt == 2 and findings_path is None:
        raise SystemExit("attempt 2 requires --findings-review")
    if attempt == 1 and findings_path is not None:
        raise SystemExit("--findings-review is only valid for attempt 2")
    run_id = f"{naics}-a{attempt}-{run_date.replace('-', '')}"
    run_dir = RUNS / naics / run_id
    l_note, n_note = dataset_notes(naics)
    remediation = ""
    if findings_path is not None:
        review = load_json(findings_path)
        remediation = "\nRemediation findings supplied by the isolated attempt-1 review:\n" + json.dumps(
            {
                "material_findings": review.get("material_findings", []),
                "summary": review.get("summary"),
            },
            indent=2,
            ensure_ascii=False,
        )
    return f"""You are the sole researcher for one v5.1 industry record.

Identity:
- NAICS: {naics}
- Title: {row['title']}
- run_id: {run_id}
- model_id: {model_id}
- run_date: {run_date}
- methodology_version: 5.1
- attempt: {attempt}

Read exactly these repository inputs, and no other repository files:
- pipeline/v5_1/research_brief.md
- pipeline/v5_1/research_packet.schema.json

Do not read methodology.md, scores, memos, reviews, prior runs, replication
runs, prior-version artifacts, fleet results, or any other industry record.
Do not spawn, delegate, consult, or fan out to any sub-agent. Work alone.

Frozen dataset inputs (provided here; do not research or re-estimate them):
- {l_note}
- {n_note}

Before registering a source, confirm the specific figure appears in the fetched
page content; never cite a number that only appears in a search-result summary.
BLS pages often return 403 to direct fetches; browser or reader-proxy fallbacks
are legitimate when they expose the actual page content.

Research the seven primitives under research_brief.md. Write one and only one
deliverable to:
  {run_dir.relative_to(ROOT)}/packet.json

Create that run directory if needed. The packet identity must match the values
above exactly. After writing it, self-check only with:
  python3 pipeline/v5_1/build.py validate {run_dir.relative_to(ROOT)}/packet.json

If validation fails, repair packet.json and rerun validate. Do not run finalize,
check, site, tests, git commands, or any command that reads another record.
Finish only when validate prints OK. In your final response report the packet
path, source count, primitive evidence states, and validation result.{remediation}
"""


def check_output(run_dir: Path) -> dict:
    result = subprocess.run(
        [sys.executable, str(V5 / "build.py"), "check", str(run_dir)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        mechanics = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"could not parse check output: {result.stdout}\n{result.stderr}") from exc
    if result.returncode or mechanics.get("errors"):
        raise SystemExit("run does not pass build.py check:\n" + json.dumps(mechanics, indent=2))
    return mechanics


def review_prompt(run_dir: Path, review_date: str, model_id: str) -> str:
    run_dir = run_dir.resolve()
    try:
        relative = run_dir.relative_to(ROOT)
    except ValueError as exc:
        raise SystemExit("run directory must be inside the repository") from exc
    packet = load_json(run_dir / "packet.json")
    identity = packet["identity"]
    mechanics = check_output(run_dir)
    cited = sorted(
        {
            source_id
            for primitive in packet["primitives"].values()
            for source_id in primitive.get("source_ids", [])
        },
        key=lambda value: int(value[1:]),
    )
    return f"""You are the fresh, isolated validator for one finalized v5.1 record.
You were not its researcher. Do not spawn, delegate, consult, or fan out to any
sub-agent. Perform the entire review yourself.

Read exactly these repository inputs, and no other repository files:
- {relative}/packet.json
- {relative}/score.json
- {relative}/memo.md
- pipeline/v5_1/methodology.md
- pipeline/v5_1/validator_brief.md
- pipeline/v5_1/review.schema.json

Do not read any other run, review, prior-version artifact, fleet result, plan,
report, dataset, source file, or build.py. Web access is for reopening the
packet's cited sources only.

Review identity:
- run_id: {identity['run_id']}
- naics: {identity['naics']}
- reviewer_model_id: {model_id}
- review_date: {review_date}
- methodology_version: 5.1

The orchestrator ran `python3 pipeline/v5_1/build.py check {relative}`. Copy this
mechanics block verbatim; do not recompute or reinterpret it:
{json.dumps({key: mechanics[key] for key in ('identity_ok', 'score_reproduces', 'memo_reproduces', 'artifacts_sha256')}, indent=2)}

Primitive-cited source IDs are exactly:
{json.dumps(cited)}

Reopen every one. `sources_audited` must contain exactly one entry for each ID
above, with no duplicates or extras. Apply validator_brief.md's materiality
test literally; unsupported decorative statistics are caveats unless their
correction or honest downgrade changes the base tier or action mechanism.

Write one and only one deliverable to:
  {relative}/review.json

Do not edit packet.json, score.json, or memo.md. Do not run git or site. In your
final response report the review path, outcome, audited-source count, material-
finding count, and caveat count.
"""


def write_sample(block_id: str, state_path: Path | None = None,
                 runs: Path | None = None, targets: dict | None = None) -> dict:
    """Compute and record one block's validation sample (frozen contract,
    code-owned). Idempotent; refuses to replace a different recorded sample."""
    from build import RUNS as BUILD_RUNS
    from build import STATE_PATH, compute_sample  # noqa: E402

    state_path = state_path or STATE_PATH
    state = load_json(state_path)
    entry = state.get("blocks", {}).get(block_id)
    if entry is None:
        raise SystemExit(f"unknown block {block_id!r}")
    try:
        sample = compute_sample(block_id, targets, runs or BUILD_RUNS)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    recorded = entry.get("sample")
    if recorded is not None and recorded != sample:
        raise SystemExit(
            f"block {block_id}: a different sample is already recorded — samples are "
            "never replaced; investigate with build.py audit-state")
    entry["sample"] = sample
    state_path.write_text(json.dumps(state, indent=1, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    return sample


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    research = sub.add_parser("research")
    research.add_argument("naics")
    research.add_argument("--date", required=True)
    research.add_argument("--model-id", default="claude-sonnet-5")
    research.add_argument("--attempt", type=int, choices=(1, 2), default=1)
    research.add_argument("--findings-review", type=Path)
    review = sub.add_parser("review")
    review.add_argument("run_dir", type=Path)
    review.add_argument("--date", required=True)
    review.add_argument("--model-id", default="claude-fable-5")
    sample = sub.add_parser("sample")
    sample.add_argument("block")
    args = parser.parse_args()
    if args.command == "research":
        print(research_prompt(
            args.naics, args.date, args.model_id, args.attempt, args.findings_review
        ))
    elif args.command == "review":
        print(review_prompt(args.run_dir, args.date, args.model_id))
    else:
        print(json.dumps(write_sample(args.block), indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
