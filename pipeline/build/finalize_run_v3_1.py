#!/usr/bin/env python3
"""Finalize one v3.1 research draft into a deterministic run record.

This is a plain-Python boundary: the model authors evidence and judgment inputs
in pipeline/drafts/, while this script injects the immutable dataset objects,
locks role identities/shares to the dataset, calculates every contribution and
score, and writes the schema-valid record in pipeline/runs/.

No model calls, web calls, threshold decisions or review decisions occur here.
"""

import argparse
import copy
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMAS = os.path.join(HERE, "schemas")
FINALIZER_VERSION = "finalizer-3.1"
RESIDUAL_TOL = 0.0005

_spec = importlib.util.spec_from_file_location("build", os.path.join(HERE, "build.py"))
build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build)


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def evidence_objects(draft):
    """Yield (path, evidence-bearing object) for v3.1 semantic checks."""
    for name, value in draft.get("dataset_fallbacks", {}).items():
        yield "dataset_fallbacks.%s" % name, value
    for name, value in draft.get("inputs", {}).items():
        if isinstance(value, dict):
            yield "inputs.%s" % name, value


def semantic_errors(draft, dataset):
    errors = []
    naics = draft.get("naics")
    if dataset.get("naics") != naics:
        errors.append("dataset naics %r does not match draft naics %r"
                      % (dataset.get("naics"), naics))
    if dataset.get("title") != draft.get("title"):
        errors.append("dataset title %r does not match draft title %r"
                      % (dataset.get("title"), draft.get("title")))

    citations = 0
    for path, value in evidence_objects(draft):
        cited = value.get("citations", [])
        citations += len(cited) if isinstance(cited, list) else 0
        quality = value.get("evidence_quality")
        if cited and quality == "NONE":
            errors.append("%s: evidence_quality NONE conflicts with non-empty citations"
                          % path)
        if not cited and quality != "NONE":
            errors.append("%s: empty citations requires evidence_quality NONE" % path)
    if citations == 0:
        errors.append("draft must contain at least one fetched citation")

    for pair in build.source_audit_pairs(draft):
        if not re.search(r"\.citations\[[0-9]+\]\.url$", pair["input_path"]):
            errors.append(
                "%s: URLs are permitted only in citations[].url, found %s"
                % (pair["input_path"], pair["url"])
            )

    inputs = draft.get("inputs", {})
    numeric_bounds = {
        "current_adoption_pct": (0, 1),
        "t50_years": (0, None),
        "active_consolidators": (0, None),
        "buy_mult": (0, None),
        "exit_mult": (0, None),
    }
    for name, (lower, upper) in numeric_bounds.items():
        value = inputs.get(name, {}).get("value")
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            errors.append("inputs.%s.value must be numeric" % name)
            continue
        if name in ("buy_mult", "exit_mult") and value <= 0:
            errors.append("inputs.%s.value must be > 0" % name)
        elif value < lower:
            errors.append("inputs.%s.value must be >= %s" % (name, lower))
        if upper is not None and value > upper:
            errors.append("inputs.%s.value must be <= %s" % (name, upper))
    consolidators = inputs.get("active_consolidators", {}).get("value")
    if isinstance(consolidators, (int, float)) and int(consolidators) != consolidators:
        errors.append("inputs.active_consolidators.value must be an integer count")

    fallbacks = draft.get("dataset_fallbacks", {})
    for name in ("labor_share", "n_band"):
        dataset_value = dataset.get(name, {}).get("value")
        has_fallback = name in fallbacks
        if dataset_value is None and not has_fallback:
            errors.append("dataset %s.value is null; dataset_fallbacks.%s is required"
                          % (name, name))
        if dataset_value is not None and has_fallback:
            errors.append("dataset %s.value is non-null; fallback is forbidden"
                          % name)

    effective_labor_share = (
        fallbacks.get("labor_share", {}).get("value")
        if dataset.get("labor_share", {}).get("value") is None
        else dataset.get("labor_share", {}).get("value")
    )
    if (not isinstance(effective_labor_share, (int, float))
            or isinstance(effective_labor_share, bool)
            or effective_labor_share < 0):
        errors.append("effective labor_share.value must be a nonnegative number")

    for name in ("n_total", "n_band"):
        dataset_value = dataset.get(name, {}).get("value")
        effective_value = (
            fallbacks.get(name, {}).get("value")
            if dataset_value is None
            else dataset_value
        )
        if (not isinstance(effective_value, (int, float))
                or isinstance(effective_value, bool)
                or not float(effective_value).is_integer()
                or effective_value < 0):
            errors.append("effective %s.value must be a nonnegative integer" % name)

    role_mix = dataset.get("role_mix")
    occupations = role_mix.get("occupations") if isinstance(role_mix, dict) else None
    if not isinstance(occupations, list) or not occupations:
        errors.append("dataset role_mix.occupations must be a non-empty array for v3.1")
        return errors
    supplied_socs = [item.get("soc") for item in occupations]
    if len(supplied_socs) != len(set(supplied_socs)):
        errors.append("dataset role_mix contains duplicate SOC codes")
    if any(not isinstance(item.get("wage_share"), (int, float)) for item in occupations):
        errors.append("every dataset occupation requires numeric wage_share")
        return errors

    judgments = inputs.get("ai_replaceable_share", {}).get("role_judgments", [])
    judgment_socs = [item.get("soc") for item in judgments]
    if len(judgment_socs) != len(set(judgment_socs)):
        errors.append("inputs.ai_replaceable_share.role_judgments contains duplicate SOC codes")
    missing = sorted(set(supplied_socs) - set(judgment_socs))
    unexpected = sorted(set(judgment_socs) - set(supplied_socs) - {"RESIDUAL"})
    if missing:
        errors.append("role judgments missing supplied SOC codes: %s" % missing)
    if unexpected:
        errors.append("role judgments contain unapproved SOC codes: %s" % unexpected)

    residual = 1.0 - sum(item["wage_share"] for item in occupations)
    if residual < -RESIDUAL_TOL:
        errors.append("dataset role wage shares exceed 1.0 by %.6f" % -residual)
    requires_residual = residual > RESIDUAL_TOL
    has_residual = "RESIDUAL" in judgment_socs
    if requires_residual and not has_residual:
        errors.append("role judgments require RESIDUAL for unlisted wage share %.6f"
                      % residual)
    if not requires_residual and has_residual:
        errors.append("RESIDUAL role judgment supplied but residual share is only %.6f"
                      % max(0.0, residual))
    return errors


def inject_dataset(draft, dataset):
    injected = {}
    fallbacks = draft["dataset_fallbacks"]
    for name in ("labor_share", "role_mix", "n_total", "n_band"):
        value = dataset[name]
        if (
            name in ("labor_share", "n_band")
            and isinstance(value, dict)
            and value.get("value") is None
        ):
            injected[name] = copy.deepcopy(fallbacks[name])
        else:
            injected[name] = copy.deepcopy(value)
    return injected


def finalize_roles(role_input, role_mix):
    by_soc = {item["soc"]: item for item in role_input["role_judgments"]}
    breakdown = []
    supplied_share = 0.0
    for occupation in role_mix["occupations"]:
        judgment = by_soc[occupation["soc"]]
        share = occupation["wage_share"]
        fraction = judgment["within_role_automatable_fraction"]
        supplied_share += share
        breakdown.append({
            "soc": occupation["soc"],
            "role": occupation["title"],
            "labor_share_of_total": share,
            "within_role_automatable_fraction": fraction,
            "contribution": share * fraction,
            "rationale": judgment["rationale"],
            "plausible_range": judgment["plausible_range"],
        })
    residual = max(0.0, 1.0 - supplied_share)
    if residual > RESIDUAL_TOL:
        judgment = by_soc["RESIDUAL"]
        fraction = judgment["within_role_automatable_fraction"]
        breakdown.append({
            "soc": "RESIDUAL",
            "role": "Unlisted occupations / residual wage share",
            "labor_share_of_total": residual,
            "within_role_automatable_fraction": fraction,
            "contribution": residual * fraction,
            "rationale": judgment["rationale"],
            "plausible_range": judgment["plausible_range"],
        })
    finalized = {
        key: copy.deepcopy(value)
        for key, value in role_input.items()
        if key != "role_judgments"
    }
    finalized["breakdown_by_role"] = breakdown
    finalized["value"] = sum(item["contribution"] for item in breakdown)
    return finalized


def arithmetic_strings(computed, rec):
    inputs = rec["inputs"]
    dataset = rec["dataset_inputs"]
    return {
        "V": (
            "Python finalizer: V_raw = labor_share × ai_replaceable_share = "
            "%.12g × %.12g = %.12g; V = 10 × min(1, V_raw / 0.25) = %.12g"
            % (
                dataset["labor_share"]["value"],
                inputs["ai_replaceable_share"]["value"],
                computed["V_raw"],
                computed["V"],
            )
        ),
        "C": (
            "Python finalizer: C = 10 × pi_dist × pi_moat = "
            "10 × %.12g × %.12g = %.12g"
            % (inputs["pi_dist"]["value"], inputs["pi_moat"]["value"], computed["C"])
        ),
        "A": (
            "Python finalizer: A = 10 when t50_years = 0, otherwise "
            "min(10, 10 / t50_years); t50_years = %.12g, A = %.12g"
            % (inputs["t50_years"]["value"], computed["A"])
        ),
        "B": (
            "Python finalizer: TD=%.12g, OW=%.12g, CFD=%.12g; "
            "B = 10 × sqrt(TD × OW) / (1 + 0.3 × CFD) = %.12g"
            % (computed["TD"], computed["OW"], computed["CFD"], computed["B"])
        ),
        "M": (
            "Python finalizer: M = clamp(4 × (exit_mult − buy_mult) / buy_mult, "
            "0, 10) = %.12g" % computed["M"]
        ),
    }


def finalize(draft, dataset):
    errors = semantic_errors(draft, dataset)
    if errors:
        return None, errors

    rec = {
        "naics": draft["naics"],
        "title": draft["title"],
        "run_meta": copy.deepcopy(draft["run_meta"]),
        "dataset_inputs": inject_dataset(draft, dataset),
        "inputs": copy.deepcopy(draft["inputs"]),
        "cross_checks": copy.deepcopy(draft["cross_checks"]),
        "confidence_overall": draft["confidence_overall"],
        "heterogeneous": draft["heterogeneous"],
        "top_uncertain_inputs": copy.deepcopy(draft["top_uncertain_inputs"]),
        "reviewer_note": draft["reviewer_note"],
    }
    rec["run_meta"]["finalizer_version"] = FINALIZER_VERSION
    rec["inputs"]["ai_replaceable_share"] = finalize_roles(
        draft["inputs"]["ai_replaceable_share"],
        rec["dataset_inputs"]["role_mix"],
    )

    computed, calc_errors = build.calculate(rec)
    if calc_errors:
        return None, calc_errors
    rec["scores"] = {
        name: {"arithmetic": "", "score": computed[name]}
        for name in ("V", "C", "A", "B", "M")
    }
    for name, arithmetic in arithmetic_strings(computed, rec).items():
        rec["scores"][name]["arithmetic"] = arithmetic
    rec["S"] = computed["S"]
    rec["cross_checks"]["uplift_pp"] = computed["V_raw"] * 100.0

    schema = load_json(os.path.join(SCHEMAS, "run_record_v3_1.schema.json"))
    errors = build.schema_errors(rec, schema, schema)
    if errors:
        return None, errors
    _computed, arithmetic_errors, _deltas = build.recompute(rec)
    if arithmetic_errors:
        return None, arithmetic_errors
    return rec, []


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Inject deterministic data and compute one finalized v3.1 run."
    )
    parser.add_argument("--draft", required=True)
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing output. Orchestrators should normally use a new run_id.",
    )
    args = parser.parse_args(argv)

    if os.path.exists(args.output) and not args.force:
        print("FINALIZE FAILED: output already exists: %s" % args.output, file=sys.stderr)
        return 1
    draft = load_json(args.draft)
    dataset = load_json(args.dataset)
    schema = load_json(os.path.join(SCHEMAS, "research_draft_v3_1.schema.json"))
    errors = build.schema_errors(draft, schema, schema)
    if errors:
        print("FINALIZE FAILED — draft schema:", file=sys.stderr)
        for error in errors:
            print("  " + error, file=sys.stderr)
        return 1
    rec, errors = finalize(draft, dataset)
    if errors:
        print("FINALIZE FAILED — semantic/injection checks:", file=sys.stderr)
        for error in errors:
            print("  " + error, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(rec, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    print(
        "OK: finalized %s (%s) -> %s"
        % (rec["naics"], rec["run_meta"]["run_id"], args.output)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
