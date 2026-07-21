#!/usr/bin/env python3
"""Finalize one v4 packet into an immutable score record and Markdown memo."""

import argparse
import ast
import copy
import importlib.util
import json
import math
import os
import sys
from datetime import date


HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMAS = os.path.join(HERE, "schemas")
FINALIZER_VERSION = "finalizer-4.0"
MEMO_RENDERER_VERSION = "memo-renderer-4.0"
PROMPT_VERSION = "v4.0-target-archetype-1"
RESIDUAL_TOL = 0.0005
VALUE_TOL = 1e-9
PROVENANCE = {"OBSERVED": "DIRECT", "CALCULATED": "DERIVED", "ESTIMATE": "ESTIMATE"}


def _load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


legacy_build = _load_module("legacy_schema_v4", "build.py")
scoring = _load_module("scoring_v4_finalizer", "v4_scoring.py")


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def _safe_eval(calculation):
    operands = calculation.get("operands", [])
    names = [item.get("name") for item in operands]
    if len(names) != len(set(names)):
        raise ValueError("calculation operand names must be unique")
    values = {item["name"]: float(item["value"]) for item in operands}
    tree = ast.parse(calculation.get("expression", ""), mode="eval")

    def visit(node):
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant):
            if not _is_number(node.value):
                raise ValueError("calculation constants must be finite numbers")
            return float(node.value)
        if isinstance(node, ast.Name):
            if node.id not in values:
                raise ValueError("unknown calculation operand %r" % node.id)
            return values[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            result = visit(node.operand)
            return result if isinstance(node.op, ast.UAdd) else -result
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Add):
                result = left + right
            elif isinstance(node.op, ast.Sub):
                result = left - right
            elif isinstance(node.op, ast.Mult):
                result = left * right
            else:
                if right == 0:
                    raise ValueError("division by zero")
                result = left / right
            if not math.isfinite(result):
                raise ValueError("calculation result is non-finite")
            return result
        raise ValueError("unsafe calculation syntax: %s" % type(node).__name__)

    return visit(tree)


def _iter_selections(packet):
    scorecard = packet.get("scorecard", {})
    yield "scorecard.ai_replaceable_share", scorecard.get("ai_replaceable_share", {})
    yield "scorecard.target_archetype.coverage", scorecard.get("target_archetype", {}).get("coverage", {})
    for name in (
        "retained_savings_share_24m", "t50_years", "current_adoption_pct",
        "historical_analogs", "seller_supply_signal", "active_consolidators",
        "buy_mult", "exit_mult", "pricing_structure", "operator_survival",
    ):
        yield "scorecard.%s" % name, scorecard.get(name, {})
    for name, selection in packet.get("dataset_fallbacks", {}).items():
        yield "dataset_fallbacks.%s" % name, selection


def _numeric_errors(path, selection, low_bound=None, high_bound=None, positive=False, integer=False):
    errors = []
    state = selection.get("evidence_state")
    value = selection.get("value")
    numeric_range = selection.get("range", {})
    low, high = numeric_range.get("low"), numeric_range.get("high")
    if state == "MISSING":
        if value is not None or low is not None or high is not None:
            errors.append("%s MISSING requires null value/range" % path)
        return errors
    if not all(_is_number(item) for item in (value, low, high)):
        return ["%s requires finite numeric value/low/high" % path]
    if low > value or value > high:
        errors.append("%s range must satisfy low <= value <= high" % path)
    if low_bound is not None and low < low_bound:
        errors.append("%s range.low below %s" % (path, low_bound))
    if high_bound is not None and high > high_bound:
        errors.append("%s range.high above %s" % (path, high_bound))
    if positive and low <= 0:
        errors.append("%s range must be strictly positive" % path)
    if integer and not float(value).is_integer():
        errors.append("%s base value must be an integer" % path)
    return errors


def semantic_errors(packet, dataset, kind):
    errors = []
    if kind not in ("fleet", "golden"):
        return ["kind must be fleet or golden"]
    required_model = {"fleet": "gpt-5.6-terra", "golden": "gpt-5.6-sol"}[kind]
    meta = packet.get("run_meta", {})
    if meta.get("model_id") != required_model:
        errors.append("%s packet model_id must be %s" % (kind, required_model))
    if meta.get("prompt_version") != PROMPT_VERSION:
        errors.append("prompt_version must be exactly %s" % PROMPT_VERSION)
    try:
        parsed_date = date.fromisoformat(meta.get("run_date", ""))
        if parsed_date > date.today():
            errors.append("run_date cannot be in the future")
    except (TypeError, ValueError):
        errors.append("run_date must be a real ISO date")
    attempt, remediates = meta.get("attempt"), meta.get("remediates_run_id")
    if attempt == 1 and remediates not in (None, ""):
        errors.append("attempt 1 may not set remediates_run_id")
    if attempt == 2 and not isinstance(remediates, str):
        errors.append("attempt 2 requires remediates_run_id")

    if dataset.get("naics") != packet.get("naics"):
        errors.append("dataset NAICS does not match packet")
    if dataset.get("title") != packet.get("title"):
        errors.append("dataset title does not match packet")

    source_ids = [item.get("id") for item in packet.get("sources", [])]
    source_set = set(source_ids)
    if len(source_ids) != len(source_set):
        errors.append("source IDs must be unique")
    source_urls = [item.get("url") for item in packet.get("sources", [])]
    if len(source_urls) != len(set(source_urls)):
        errors.append("source URLs must be unique; combine support descriptions")

    for path, selection in _iter_selections(packet):
        refs = selection.get("source_ids", [])
        unknown = sorted(set(refs) - source_set)
        if unknown:
            errors.append("%s references unknown source IDs %s" % (path, unknown))
        state, quality, method = selection.get("evidence_state"), selection.get("evidence_quality"), selection.get("method")
        if state in ("MISSING", "ASSUMPTION"):
            if refs or quality != "NONE" or method != "ESTIMATE":
                errors.append("%s %s requires ESTIMATE, NONE quality, and empty source_ids" % (path, state))
        else:
            if not refs or quality == "NONE":
                errors.append("%s %s requires sources and non-NONE quality" % (path, state))
        if state == "DIRECT" and method not in ("OBSERVED", "CALCULATED"):
            errors.append("%s DIRECT requires OBSERVED or CALCULATED" % path)
        if method == "CALCULATED":
            calculation = selection.get("calculation")
            if not isinstance(calculation, dict):
                errors.append("%s CALCULATED requires calculation" % path)
            else:
                operand_refs = [item.get("source_id") for item in calculation.get("operands", [])]
                if sorted(set(operand_refs) - set(refs)):
                    errors.append("%s calculation operand sources must be selected" % path)
                try:
                    computed = _safe_eval(calculation)
                    if not _is_number(selection.get("value")) or abs(float(selection["value"]) - computed) > VALUE_TOL:
                        errors.append("%s authored value does not equal safe calculation" % path)
                except (SyntaxError, ValueError) as exc:
                    errors.append("%s unsafe calculation: %s" % (path, exc))

    for name in ("seller_supply_signal", "operator_survival"):
        selection = packet.get("scorecard", {}).get(name, {})
        plausible = selection.get("plausible_values", [])
        if len(plausible) != len(set(plausible)):
            errors.append("scorecard.%s plausible_values must be unique" % name)
        if selection.get("value") not in plausible:
            errors.append("scorecard.%s base value must appear in plausible_values" % name)

    scorecard = packet.get("scorecard", {})
    numeric_specs = {
        "target_archetype.coverage": (0, 1, False, False),
        "retained_savings_share_24m": (0, 1, False, False),
        "t50_years": (0, None, False, False),
        "current_adoption_pct": (0, 1, False, False),
        "active_consolidators": (0, None, False, True),
        "buy_mult": (None, None, True, False),
        "exit_mult": (None, None, True, False),
    }
    for path, spec in numeric_specs.items():
        selection = scorecard
        for part in path.split("."):
            selection = selection[part]
        errors.extend(_numeric_errors("scorecard.%s" % path, selection, *spec))

    for role in scorecard.get("ai_replaceable_share", {}).get("role_judgments", []):
        role_sel = {
            "value": role.get("within_role_automatable_fraction"),
            "range": role.get("range", {}),
            "evidence_state": "ASSUMPTION",
        }
        errors.extend(_numeric_errors("role_judgments.%s" % role.get("soc"), role_sel, 0, 1))

    adoption, t50 = scorecard.get("current_adoption_pct", {}), scorecard.get("t50_years", {})
    if adoption.get("evidence_state") != "MISSING" and t50.get("evidence_state") != "MISSING":
        if adoption["value"] >= 0.5 and t50["value"] != 0:
            errors.append("t50_years must be zero when current adoption is at least 50%")
        if adoption["value"] < 0.5 and t50["value"] <= 0:
            errors.append("t50_years must be positive when current adoption is below 50%")

    for name in ("labor_share", "n_band"):
        dataset_value = dataset.get(name, {}).get("value")
        fallback = packet.get("dataset_fallbacks", {}).get(name)
        if dataset_value is None and fallback is None:
            errors.append("dataset %s.value is null; fallback required" % name)
        if dataset_value is not None and fallback is not None:
            errors.append("dataset %s.value is non-null; fallback forbidden" % name)

    occupations = dataset.get("role_mix", {}).get("occupations")
    if not isinstance(occupations, list) or not occupations:
        errors.append("dataset role_mix.occupations must be non-empty")
    else:
        supplied = [item.get("soc") for item in occupations]
        judgments = scorecard.get("ai_replaceable_share", {}).get("role_judgments", [])
        authored = [item.get("soc") for item in judgments]
        if len(authored) != len(set(authored)):
            errors.append("role judgments contain duplicate SOCs")
        missing = sorted(set(supplied) - set(authored))
        unexpected = sorted(set(authored) - set(supplied) - {"RESIDUAL"})
        if missing:
            errors.append("role judgments missing supplied SOCs: %s" % missing)
        if unexpected:
            errors.append("role judgments contain unapproved SOCs: %s" % unexpected)
        residual = 1.0 - sum(float(item["wage_share"]) for item in occupations)
        has_residual = "RESIDUAL" in authored
        if residual > RESIDUAL_TOL and not has_residual:
            errors.append("role judgments require RESIDUAL for %.6f wage share" % residual)
        if residual <= RESIDUAL_TOL and has_residual:
            errors.append("RESIDUAL forbidden without material residual")
    return errors


def _finalize_selection(selection):
    result = copy.deepcopy(selection)
    if result["method"] == "CALCULATED":
        result["value"] = _safe_eval(result["calculation"])
    result["provenance_type"] = PROVENANCE[result["method"]]
    return result


def _inject_dataset(packet, dataset):
    injected = {}
    for name in ("labor_share", "role_mix", "n_total", "n_band"):
        item = dataset[name]
        if name in ("labor_share", "n_band") and item.get("value") is None:
            injected[name] = _finalize_selection(packet["dataset_fallbacks"][name])
        else:
            injected[name] = copy.deepcopy(item)
    return injected


def _finalize_roles(role_packet, role_mix):
    by_soc = {item["soc"]: item for item in role_packet["role_judgments"]}
    breakdown, supplied_share = [], 0.0
    for occupation in role_mix["occupations"]:
        judgment = by_soc[occupation["soc"]]
        share = float(occupation["wage_share"])
        supplied_share += share
        breakdown.append({
            "soc": occupation["soc"],
            "role": occupation["title"],
            "labor_share_of_total": share,
            "within_role_automatable_fraction": judgment["within_role_automatable_fraction"],
            "range": copy.deepcopy(judgment["range"]),
            "contribution": share * judgment["within_role_automatable_fraction"],
            "rationale": judgment["rationale"],
        })
    residual = max(0.0, 1.0 - supplied_share)
    if residual > RESIDUAL_TOL:
        judgment = by_soc["RESIDUAL"]
        breakdown.append({
            "soc": "RESIDUAL",
            "role": "Unlisted occupations / residual wage share",
            "labor_share_of_total": residual,
            "within_role_automatable_fraction": judgment["within_role_automatable_fraction"],
            "range": copy.deepcopy(judgment["range"]),
            "contribution": residual * judgment["within_role_automatable_fraction"],
            "rationale": judgment["rationale"],
        })
    result = {key: copy.deepcopy(value) for key, value in role_packet.items() if key != "role_judgments"}
    result["value"] = sum(item["contribution"] for item in breakdown)
    result["provenance_type"] = "ESTIMATE"
    result["breakdown_by_role"] = breakdown
    return result


def finalize(packet, dataset, kind):
    errors = semantic_errors(packet, dataset, kind)
    if errors:
        return None, errors
    record = {
        "naics": packet["naics"],
        "title": packet["title"],
        "run_meta": copy.deepcopy(packet["run_meta"]),
        "narrative": copy.deepcopy(packet["narrative"]),
        "sources": copy.deepcopy(packet["sources"]),
        "dataset_inputs": _inject_dataset(packet, dataset),
        "inputs": {},
        "cross_checks": copy.deepcopy(packet["cross_checks"]),
        "disclosures": copy.deepcopy(packet["disclosures"]),
        "confidence_overall": packet["confidence_overall"],
        "heterogeneous": packet["heterogeneous"],
        "top_uncertain_inputs": copy.deepcopy(packet["top_uncertain_inputs"]),
        "reviewer_note": packet["reviewer_note"],
    }
    record["run_meta"]["finalizer_version"] = FINALIZER_VERSION
    record["run_meta"]["memo_renderer_version"] = MEMO_RENDERER_VERSION
    for name, selection in packet["scorecard"].items():
        if name == "ai_replaceable_share":
            record["inputs"][name] = _finalize_roles(selection, record["dataset_inputs"]["role_mix"])
        elif name == "target_archetype":
            target = copy.deepcopy(selection)
            target["coverage"] = _finalize_selection(selection["coverage"])
            record["inputs"][name] = target
        else:
            record["inputs"][name] = _finalize_selection(selection)

    try:
        computed = scoring.calculate(record)
    except (KeyError, TypeError, ValueError, ZeroDivisionError) as exc:
        return None, ["v4 scoring failed: %s" % exc]
    record["scores"] = {
        name: {
            "low": computed["low"]["scores"][name],
            "base": computed["base"]["scores"][name],
            "high": computed["high"]["scores"][name],
        }
        for name in scoring.FACTOR_NAMES
    }
    record["S"] = {bound: computed[bound]["S"] for bound in ("low", "base", "high")}
    record["subfactors"] = {bound: computed[bound]["subfactors"] for bound in ("low", "base", "high")}
    record["decision"] = computed["decision"]
    record["cross_checks"]["uplift_pp"] = computed["base"]["subfactors"]["V_raw"] * 100.0

    schema = load_json(os.path.join(SCHEMAS, "run_record_v4.schema.json"))
    schema_errs = legacy_build.schema_errors(record, schema, schema)
    if schema_errs:
        return None, schema_errs
    return record, []


def declared_caveats(record):
    caveats = []
    for path, selection in (
        ("inputs.ai_replaceable_share", record["inputs"]["ai_replaceable_share"]),
        ("inputs.target_archetype.coverage", record["inputs"]["target_archetype"]["coverage"]),
    ):
        caveats.extend("%s: %s" % (path, item) for item in selection.get("caveats", []))
    for name, selection in record["inputs"].items():
        if name in ("ai_replaceable_share", "target_archetype"):
            continue
        caveats.extend("inputs.%s: %s" % (name, item) for item in selection.get("caveats", []))
    return caveats


def render_memo(record):
    titles = (
        ("executive_view", "Executive view"),
        ("target_archetype", "Target archetype"),
        ("how_ai_changes_work", "How AI changes the work"),
        ("value_capture", "Value capture"),
        ("adoption_timing", "Adoption timing"),
        ("buyability", "Buyability"),
        ("valuation", "Valuation"),
        ("operator_survival", "Operator survival"),
        ("risks_and_uncertainty", "Risks and uncertainty"),
    )
    lines = [
        "# %s — %s" % (record["naics"], record["title"]), "",
        "*v4.0 research memo · run `%s` · %s · %s*" % (
            record["run_meta"]["run_id"], record["run_meta"]["model_id"], record["run_meta"]["run_date"]), "",
    ]
    for key, title in titles:
        lines.extend(["## " + title, "", record["narrative"][key], ""])
    lines.extend(["## Deterministic economic result", "", "| Factor | Low | Base | High |", "|---|---:|---:|---:|"])
    for name in scoring.FACTOR_NAMES:
        item = record["scores"][name]
        lines.append("| %s | %.2f | %.2f | %.2f |" % (name, item["low"], item["base"], item["high"]))
    lines.append("| **S** | **%.2f** | **%.2f** | **%.2f** |" % (
        record["S"]["low"], record["S"]["base"], record["S"]["high"]))
    decision = record["decision"]
    lines.extend([
        "", "**Economic verdict:** `%s`" % decision["economic_verdict"],
        "", "**Evidence readiness:** `%s`" % decision["evidence_readiness"]["status"],
        "", "**Action:** `%s`" % decision["action"],
        "", "**Operator survival:** `%s`" % decision["operator_survival"],
        "", "**Sensitivity:** `%s` → `%s`%s" % (
            decision["sensitivity"]["low_verdict"], decision["sensitivity"]["high_verdict"],
            " (`CROSS_TIER`)" if decision["sensitivity"]["cross_tier"] else ""),
        "", "## Evidence gaps", "",
    ])
    readiness = decision["evidence_readiness"]
    for label, key in (("Missing", "missing_critical_inputs"), ("Assumptions", "assumption_critical_inputs"), ("Low quality", "low_quality_critical_inputs")):
        values = readiness[key]
        lines.append("- **%s:** %s" % (label, ", ".join(values) if values else "none"))
    lines.extend(["", "## Declared caveats", ""])
    lines.extend(["- " + item for item in declared_caveats(record)] or ["- None declared."])
    lines.extend(["", "## Sources", ""])
    for source in record["sources"]:
        lines.append("- **%s. [%s](%s)** — %s (accessed %s)" % (
            source["id"], source["title"], source["url"], source["what_it_supports"], source["access_date"]))
    lines.extend(["", "---", "", "Scores, ranges, readiness, gates, and this memo were rendered by `%s`; do not hand-edit." % MEMO_RENDERER_VERSION, ""])
    return "\n".join(lines)


def serialize_record(record):
    return (json.dumps(record, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", required=True)
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--kind", choices=("fleet", "golden"), required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--memo", required=True)
    args = parser.parse_args(argv)
    for path in (args.output, args.memo):
        if os.path.exists(path):
            print("FINALIZE FAILED: output already exists: %s" % path, file=sys.stderr)
            return 1
    packet, dataset = load_json(args.packet), load_json(args.dataset)
    packet_schema = load_json(os.path.join(SCHEMAS, "research_packet_v4.schema.json"))
    errors = legacy_build.schema_errors(packet, packet_schema, packet_schema)
    if errors:
        print("FINALIZE FAILED — packet schema:", file=sys.stderr)
    else:
        record, errors = finalize(packet, dataset, args.kind)
    if errors:
        for error in errors:
            print("  " + error, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(args.memo)), exist_ok=True)
    with open(args.output, "wb") as handle:
        handle.write(serialize_record(record))
    with open(args.memo, "w", encoding="utf-8") as handle:
        handle.write(render_memo(record))
    print("OK: finalized and rendered v4 %s (%s)" % (record["naics"], record["run_meta"]["run_id"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
