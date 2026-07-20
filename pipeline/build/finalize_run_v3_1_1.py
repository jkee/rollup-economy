#!/usr/bin/env python3
"""Finalize one v3.1.1 evidence draft into a deterministic run record.

The model authors atomic facts and selected-value methods. Python validates the
method shape, recomputes CALCULATED values, assigns final provenance, injects
immutable datasets/role weights and calculates every score.
"""

import argparse
import copy
import importlib.util
import json
import math
import os
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMAS = os.path.join(HERE, "schemas")
FINALIZER_VERSION = "finalizer-3.1.1"
RESIDUAL_TOL = 0.0005


def _load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


build = _load_module("build_v311", "build.py")
contract = _load_module("evidence_contract_v311", "evidence_contract_v3_1_1.py")
legacy_finalizer = _load_module("finalizer_v31_helpers", "finalize_run_v3_1.py")


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _is_number(value):
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def dataset_and_role_errors(draft, dataset):
    errors = []
    naics = draft.get("naics")
    if dataset.get("naics") != naics:
        errors.append(
            "dataset naics %r does not match draft naics %r"
            % (dataset.get("naics"), naics)
        )
    if dataset.get("title") != draft.get("title"):
        errors.append(
            "dataset title %r does not match draft title %r"
            % (dataset.get("title"), draft.get("title"))
        )

    fallbacks = draft.get("dataset_fallbacks", {})
    for name in ("labor_share", "n_band"):
        dataset_value = dataset.get(name, {}).get("value")
        has_fallback = name in fallbacks
        if dataset_value is None and not has_fallback:
            errors.append(
                "dataset %s.value is null; dataset_fallbacks.%s is required"
                % (name, name)
            )
        if dataset_value is not None and has_fallback:
            errors.append("dataset %s.value is non-null; fallback is forbidden" % name)

    effective_labor_share = (
        fallbacks.get("labor_share", {}).get("value")
        if dataset.get("labor_share", {}).get("value") is None
        else dataset.get("labor_share", {}).get("value")
    )
    if not _is_number(effective_labor_share) or effective_labor_share < 0:
        errors.append("effective labor_share.value must be a nonnegative number")

    for name in ("n_total", "n_band"):
        dataset_value = dataset.get(name, {}).get("value")
        effective_value = (
            fallbacks.get(name, {}).get("value")
            if dataset_value is None
            else dataset_value
        )
        if (
            not _is_number(effective_value)
            or not float(effective_value).is_integer()
            or effective_value < 0
        ):
            errors.append("effective %s.value must be a nonnegative integer" % name)

    inputs = draft.get("inputs", {})
    adoption = inputs.get("current_adoption_pct", {}).get("value")
    t50 = inputs.get("t50_years", {}).get("value")
    if _is_number(adoption) and _is_number(t50):
        if adoption >= 0.5 and t50 != 0:
            errors.append("t50_years must be 0 when current_adoption_pct >= 0.5")
        if adoption < 0.5 and t50 <= 0:
            errors.append("t50_years must be > 0 when current_adoption_pct < 0.5")

    role_mix = dataset.get("role_mix")
    occupations = role_mix.get("occupations") if isinstance(role_mix, dict) else None
    if not isinstance(occupations, list) or not occupations:
        errors.append("dataset role_mix.occupations must be a non-empty array for v3.1.1")
        return errors
    supplied_socs = [item.get("soc") for item in occupations]
    if len(supplied_socs) != len(set(supplied_socs)):
        errors.append("dataset role_mix contains duplicate SOC codes")
    if any(not _is_number(item.get("wage_share")) for item in occupations):
        errors.append("every dataset occupation requires numeric wage_share")
        return errors

    role_packet = inputs.get("ai_replaceable_share", {})
    judgments = role_packet.get("role_judgments", [])
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
        errors.append(
            "role judgments require RESIDUAL for unlisted wage share %.6f" % residual
        )
    if not requires_residual and has_residual:
        errors.append(
            "RESIDUAL role judgment supplied but residual share is only %.6f"
            % max(0.0, residual)
        )
    return errors


def semantic_errors(draft, dataset):
    return contract.semantic_errors(draft) + dataset_and_role_errors(draft, dataset)


def finalize_selection(selection):
    finalized = copy.deepcopy(selection)
    method = finalized["method"]
    if method == "CALCULATED":
        finalized["value"] = contract.evaluate_calculation(finalized["calculation"])
    finalized["provenance_type"] = contract.provenance_for(finalized)
    return finalized


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
            injected[name] = finalize_selection(fallbacks[name])
        else:
            injected[name] = copy.deepcopy(value)
    return injected


def finalize_roles(role_packet, role_mix):
    by_soc = {item["soc"]: item for item in role_packet["role_judgments"]}
    breakdown = []
    supplied_share = 0.0
    for occupation in role_mix["occupations"]:
        judgment = by_soc[occupation["soc"]]
        share = occupation["wage_share"]
        fraction = judgment["within_role_automatable_fraction"]
        supplied_share += share
        breakdown.append(
            {
                "soc": occupation["soc"],
                "role": occupation["title"],
                "labor_share_of_total": share,
                "within_role_automatable_fraction": fraction,
                "contribution": share * fraction,
                "rationale": judgment["rationale"],
                "plausible_range": judgment["plausible_range"],
            }
        )
    residual = max(0.0, 1.0 - supplied_share)
    if residual > RESIDUAL_TOL:
        judgment = by_soc["RESIDUAL"]
        fraction = judgment["within_role_automatable_fraction"]
        breakdown.append(
            {
                "soc": "RESIDUAL",
                "role": "Unlisted occupations / residual wage share",
                "labor_share_of_total": residual,
                "within_role_automatable_fraction": fraction,
                "contribution": residual * fraction,
                "rationale": judgment["rationale"],
                "plausible_range": judgment["plausible_range"],
            }
        )
    return {
        "value": sum(item["contribution"] for item in breakdown),
        "method": "ESTIMATE",
        "provenance_type": "ESTIMATE",
        "evidence_quality": role_packet["evidence_quality"],
        "fact_ids": copy.deepcopy(role_packet["fact_ids"]),
        "estimate_basis": role_packet["estimate_basis"],
        "breakdown_by_role": breakdown,
    }


def finalize_inputs(draft_inputs, role_mix):
    finalized = {}
    for name, value in draft_inputs.items():
        if name == "ai_replaceable_share":
            finalized[name] = finalize_roles(value, role_mix)
        elif name == "owners_60plus_pct":
            finalized[name] = finalize_selection(value["selection"])
            finalized[name]["succession_shortage_documented"] = copy.deepcopy(
                value["succession_shortage_documented"]
            )
        else:
            finalized[name] = finalize_selection(value)
    return finalized


def finalize(draft, dataset):
    draft_schema = load_json(
        os.path.join(SCHEMAS, "research_draft_v3_1_1.schema.json")
    )
    errors = build.schema_errors(draft, draft_schema, draft_schema)
    if errors:
        return None, errors
    errors = semantic_errors(draft, dataset)
    if errors:
        return None, errors

    rec = {
        "naics": draft["naics"],
        "title": draft["title"],
        "run_meta": copy.deepcopy(draft["run_meta"]),
        "evidence_facts": copy.deepcopy(draft["evidence_facts"]),
        "dataset_inputs": inject_dataset(draft, dataset),
        "inputs": {},
        "cross_checks": copy.deepcopy(draft["cross_checks"]),
        "disclosures": copy.deepcopy(draft["disclosures"]),
        "confidence_overall": draft["confidence_overall"],
        "heterogeneous": draft["heterogeneous"],
        "top_uncertain_inputs": copy.deepcopy(draft["top_uncertain_inputs"]),
        "reviewer_note": draft["reviewer_note"],
    }
    rec["run_meta"]["finalizer_version"] = FINALIZER_VERSION
    rec["inputs"] = finalize_inputs(draft["inputs"], rec["dataset_inputs"]["role_mix"])

    computed, calc_errors = build.calculate(rec)
    if calc_errors:
        return None, calc_errors
    rec["scores"] = {
        name: {"arithmetic": "", "score": computed[name]}
        for name in ("V", "C", "A", "B", "M")
    }
    for name, arithmetic in legacy_finalizer.arithmetic_strings(computed, rec).items():
        rec["scores"][name]["arithmetic"] = arithmetic.replace(
            "Python finalizer:", "Python finalizer v3.1.1:"
        )
    rec["S"] = computed["S"]
    rec["cross_checks"]["uplift_pp"] = computed["V_raw"] * 100.0

    schema = load_json(os.path.join(SCHEMAS, "run_record_v3_1_1.schema.json"))
    errors = build.schema_errors(rec, schema, schema)
    errors.extend(contract.final_record_semantic_errors(rec))
    if errors:
        return None, errors
    _computed, arithmetic_errors, _deltas = build.recompute(rec)
    if arithmetic_errors:
        return None, arithmetic_errors
    return rec, []


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Finalize one v3.1.1 evidence draft with deterministic provenance and scores."
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
    schema = load_json(os.path.join(SCHEMAS, "research_draft_v3_1_1.schema.json"))
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
