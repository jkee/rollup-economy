#!/usr/bin/env python3
"""Phase 3.2 prompt assembler — deterministic, stdlib-only, no model calls.

Reads pipeline/blocks/targets_phase3.json; for each code merges
pipeline/blocks/<naics>.json + pipeline/datasets/derived/<naics>.json into the
frozen template pipeline/template/prompt_template_v3.md and writes
pipeline/prompts/<naics>.md.

Generation-time placeholders filled here:
  {{NAICS}} {{TITLE}} {{ROLE_HINTS}} {{SOURCE_HINTS}} {{CAPTURE_QUESTIONS}}
  {{TERMINAL_VALUE_QUESTION}} {{SPECIAL_NOTES}} {{DATASET_INPUTS_JSON}}
Runtime placeholders left verbatim for the Phase-4 runner:
  {{MODEL_ID}} {{RUN_DATE}} {{RUN_ID}} {{PROMPT_VERSION}}

Missing block file  -> skip with warning (block generation fills in behind us).
Missing block key / malformed block / leftover placeholder -> hard fail.
--check: validate only (re-render in memory, compare against files on disk).

Two runs over the same inputs are byte-identical by construction: pure string
assembly, no timestamps, no randomness, no dict-order dependence beyond the
input files themselves.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
TARGETS_PATH = REPO / "pipeline" / "blocks" / "targets_phase3.json"
BLOCKS_DIR = REPO / "pipeline" / "blocks"
DERIVED_DIR = REPO / "pipeline" / "datasets" / "derived"

VERSION_PATHS = {
    "3.0": {
        "template": REPO / "pipeline" / "template" / "prompt_template_v3.md",
        "prompts": REPO / "pipeline" / "prompts",
    },
    "3.1": {
        "template": REPO / "pipeline" / "template" / "prompt_template_v3_1.md",
        "prompts": REPO / "pipeline" / "prompts_v3_1",
    },
    "3.1.1": {
        "template": REPO / "pipeline" / "template" / "prompt_template_v3_1_1.md",
        "prompts": REPO / "pipeline" / "prompts_v3_1_1",
    },
    "3.1.2": {
        "template": REPO / "pipeline" / "template" / "prompt_template_v3_1_2.md",
        "prompts": REPO / "pipeline" / "prompts_v3_1_2",
    },
}

RUNTIME_PLACEHOLDERS = {"{{MODEL_ID}}", "{{RUN_DATE}}", "{{RUN_ID}}", "{{PROMPT_VERSION}}"}
PLACEHOLDER_RE = re.compile(r"\{\{[^{}]*\}\}")

BLOCK_KEYS = [
    "role_hints",
    "source_hints",
    "capture_questions",
    "terminal_value_question",
    "special_notes",
    "research_gaps",
]
DATASET_FIELDS = ["labor_share", "role_mix", "n_total", "n_band"]

ROLE_HINT_KEYS = ["role", "oews_basis", "approx_share_of_wage_bill", "automatable", "note"]
SOURCE_HINT_KEYS = ["area", "source", "why", "uncertain_exists"]
GAP_KEYS = ["input", "instruction"]


class AssembleError(Exception):
    pass


def fail(naics, msg):
    raise AssembleError(f"[{naics}] {msg}")


def validate_block(naics, block):
    if not isinstance(block, dict):
        fail(naics, "block is not a JSON object")
    missing = [k for k in BLOCK_KEYS if k not in block]
    if missing:
        fail(naics, f"block missing key(s): {', '.join(missing)}")
    extra = [k for k in block if k not in BLOCK_KEYS]
    if extra:
        fail(naics, f"block has unexpected key(s): {', '.join(extra)}")

    rh = block["role_hints"]
    if not isinstance(rh, list) or not rh:
        fail(naics, "role_hints must be a non-empty array")
    for i, item in enumerate(rh):
        if not isinstance(item, dict):
            fail(naics, f"role_hints[{i}] is not an object")
        for k in ROLE_HINT_KEYS:
            if k not in item:
                fail(naics, f"role_hints[{i}] missing '{k}'")

    sh = block["source_hints"]
    if not isinstance(sh, list) or not sh:
        fail(naics, "source_hints must be a non-empty array")
    for i, item in enumerate(sh):
        if not isinstance(item, dict):
            fail(naics, f"source_hints[{i}] is not an object")
        for k in SOURCE_HINT_KEYS:
            if k not in item:
                fail(naics, f"source_hints[{i}] missing '{k}'")

    cq = block["capture_questions"]
    if not isinstance(cq, list) or not (3 <= len(cq) <= 5):
        n = len(cq) if isinstance(cq, list) else "non-array"
        fail(naics, f"capture_questions must be an array of 3-5 strings (got {n})")
    if not all(isinstance(q, str) and q.strip() for q in cq):
        fail(naics, "capture_questions entries must be non-empty strings")

    tv = block["terminal_value_question"]
    if not isinstance(tv, str) or not tv.strip():
        fail(naics, "terminal_value_question must be a non-empty string")

    sn = block["special_notes"]
    if not isinstance(sn, list) or not sn or not all(isinstance(s, str) and s.strip() for s in sn):
        fail(naics, "special_notes must be a non-empty array of non-empty strings")

    gaps = block["research_gaps"]
    if not isinstance(gaps, list):
        fail(naics, "research_gaps must be an array (empty when no gaps)")
    for i, item in enumerate(gaps):
        if not isinstance(item, dict):
            fail(naics, f"research_gaps[{i}] is not an object")
        for k in GAP_KEYS:
            if k not in item or not item[k]:
                fail(naics, f"research_gaps[{i}] missing '{k}'")
        if item["input"] not in ("labor_share", "n_band"):
            fail(naics, f"research_gaps[{i}].input must be 'labor_share' or 'n_band' (got {item['input']!r})")


def render_role_hints(block):
    lines = []
    for item in block["role_hints"]:
        auto = item["automatable"]
        auto_txt = {True: "yes", False: "no"}.get(auto, str(auto))
        lines.append(
            f"- **{item['role']}** — {item['approx_share_of_wage_bill']} of wage bill "
            f"(OEWS basis: {item['oews_basis']}); automatable: {auto_txt}. {item['note']}"
        )
    return "\n".join(lines)


def render_source_hints(block):
    lines = []
    for item in block["source_hints"]:
        suffix = " *(existence unverified — confirm this source still exists/publishes before relying on it)*" if item["uncertain_exists"] else ""
        lines.append(f"- ({item['area']}) {item['source']} — {item['why']}{suffix}")
    return "\n".join(lines)


def render_capture_questions(block):
    return "\n".join(f"- {q}" for q in block["capture_questions"])


def render_special_notes(block):
    return "\n".join(f"- {s}" for s in block["special_notes"])


def render_dataset_inputs(naics, block, dataset, template_version):
    missing = [f for f in DATASET_FIELDS if f not in dataset]
    if missing:
        fail(naics, f"dataset record missing field(s): {', '.join(missing)}")
    subset = {f: dataset[f] for f in DATASET_FIELDS}
    body = "```json\n" + json.dumps(subset, indent=2, ensure_ascii=False) + "\n```"
    gaps = block["research_gaps"]
    if gaps:
        gap_lines = "\n".join(f"- `{g['input']}`: {g['instruction']}" for g in gaps)
        if template_version == "3.1.2":
            fallback_rule = (
                "provide the value in `dataset_fallbacks` using the compact v3.1.2 "
                "selection shape; use `OBSERVED` only for an exact sourced value, "
                "`CALCULATED` only for safe source-backed arithmetic, and `ESTIMATE` "
                "for any judgmental bridge, with range, confidence and candid caveats"
            )
        elif template_version == "3.1.1":
            fallback_rule = (
                "provide the value in `dataset_fallbacks` using the v3.1.1 "
                "selection contract; use `OBSERVED` only for an exact sourced value, "
                "`CALCULATED` only for fully reproducible fact-backed arithmetic, and "
                "`ESTIMATE` for any judgmental bridge"
            )
        elif template_version == "3.1":
            fallback_rule = (
                "provide the value in `dataset_fallbacks`, show the full v3.1 evidence "
                "chain, and use `provenance_type: ESTIMATE` when no source directly "
                "establishes it"
            )
        else:
            fallback_rule = (
                "research the value yourself, show the full derivation chain, and mark "
                "it quality `ESTIMATE`"
            )
        body += (
            "\n\n**Research gaps — documented exception to core rule 6 (V3_PLAN.md 3.1).** "
            "The dataset input(s) below are null in the provided record. For these inputs ONLY, "
            + fallback_rule
            + ". Every other dataset input remains provided — do not re-research it.\n\n"
            + gap_lines
        )
    return body


def assemble_one(naics, title, template, template_version):
    block_path = BLOCKS_DIR / f"{naics}.json"
    dataset_path = DERIVED_DIR / f"{naics}.json"
    if not dataset_path.exists():
        fail(naics, f"derived dataset record not found: {dataset_path}")
    try:
        block = json.loads(block_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(naics, f"block file is not valid JSON: {e}")
    dataset = json.loads(dataset_path.read_text(encoding="utf-8"))

    validate_block(naics, block)

    replacements = {
        "{{NAICS}}": naics,
        "{{TITLE}}": title,
        "{{ROLE_HINTS}}": render_role_hints(block),
        "{{SOURCE_HINTS}}": render_source_hints(block),
        "{{CAPTURE_QUESTIONS}}": render_capture_questions(block),
        "{{TERMINAL_VALUE_QUESTION}}": block["terminal_value_question"].strip(),
        "{{SPECIAL_NOTES}}": render_special_notes(block),
        "{{DATASET_INPUTS_JSON}}": render_dataset_inputs(
            naics, block, dataset, template_version
        ),
    }
    text = template
    for ph, value in replacements.items():
        text = text.replace(ph, value)
    return text


def validate_prompt_text(naics, text):
    leftovers = sorted(set(PLACEHOLDER_RE.findall(text)) - RUNTIME_PLACEHOLDERS)
    if leftovers:
        fail(naics, f"unfilled placeholder(s) in assembled prompt: {', '.join(leftovers)}")
    missing_runtime = sorted(ph for ph in RUNTIME_PLACEHOLDERS if ph not in text)
    if missing_runtime:
        fail(naics, f"runtime placeholder(s) missing from assembled prompt: {', '.join(missing_runtime)}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Assemble v3 per-code prompts from blocks + datasets + frozen template.")
    parser.add_argument("--check", action="store_true", help="Validate only: re-render in memory and compare against prompts on disk; write nothing.")
    parser.add_argument(
        "--template-version",
        choices=sorted(VERSION_PATHS),
        default="3.0",
        help="Contract to assemble. Defaults to 3.0 so existing prompts remain untouched.",
    )
    args = parser.parse_args(argv)

    targets = json.loads(TARGETS_PATH.read_text(encoding="utf-8"))
    version_paths = VERSION_PATHS[args.template_version]
    template = version_paths["template"].read_text(encoding="utf-8")
    prompts_dir = version_paths["prompts"]
    if not args.check:
        prompts_dir.mkdir(parents=True, exist_ok=True)

    skipped, written, checked, errors = [], [], [], []

    for entry in targets["codes"]:
        naics, title = entry["naics"], entry["title"]
        block_path = BLOCKS_DIR / f"{naics}.json"
        if not block_path.exists():
            skipped.append(naics)
            continue
        try:
            text = assemble_one(naics, title, template, args.template_version)
            validate_prompt_text(naics, text)
            out_path = prompts_dir / f"{naics}.md"
            if args.check:
                if not out_path.exists():
                    fail(naics, f"--check: prompt file missing on disk: {out_path}")
                on_disk = out_path.read_text(encoding="utf-8")
                if on_disk != text:
                    fail(naics, f"--check: {out_path} differs from freshly assembled text (stale — re-run assemble_prompts.py)")
                checked.append(naics)
            else:
                out_path.write_text(text, encoding="utf-8")
                written.append(naics)
        except AssembleError as e:
            errors.append(str(e))

    if skipped:
        print(f"WARNING: {len(skipped)} code(s) skipped — no block file yet in {BLOCKS_DIR}/:")
        print("  " + " ".join(skipped))
    if written:
        print(f"OK: wrote {len(written)} prompt(s) to {prompts_dir}/: " + " ".join(written))
    if checked:
        print(f"OK: {len(checked)} prompt(s) validated against disk: " + " ".join(checked))
    if errors:
        print(f"FAIL: {len(errors)} error(s):", file=sys.stderr)
        for e in errors:
            print("  " + e, file=sys.stderr)
        sys.exit(1)
    if not (written or checked or skipped):
        print("Nothing to do: targets list is empty.")


if __name__ == "__main__":
    main()
