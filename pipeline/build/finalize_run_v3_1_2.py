#!/usr/bin/env python3
"""Finalize one v3.1.2 text-first packet and render its Markdown memo.

The packet is the only model-authored artifact. This plain-Python boundary
validates source references and safe calculations, injects immutable dataset
inputs and role weights, computes every contribution/factor/S/verdict, and
renders the memo. Existing outputs are never overwritten.
"""

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
FINALIZER_VERSION = "finalizer-3.1.2"
MEMO_RENDERER_VERSION = "memo-renderer-3.1.2"
PROMPT_VERSION = "v3.1.2-text-first-1"
RESIDUAL_TOL = 0.0005
VALUE_TOL = 1e-9
PROVENANCE = {"OBSERVED": "DIRECT", "CALCULATED": "DERIVED", "ESTIMATE": "ESTIMATE"}


def _load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


build = _load_module("build_v312", "build.py")


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
            value = visit(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
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
    for name, selection in scorecard.items():
        if name == "ai_replaceable_share":
            yield "scorecard.ai_replaceable_share", selection
        elif name == "owners_60plus_pct":
            yield "scorecard.owners_60plus_pct.selection", selection.get("selection", {})
            yield ("scorecard.owners_60plus_pct.succession_shortage_documented",
                   selection.get("succession_shortage_documented", {}))
        else:
            yield "scorecard.%s" % name, selection
    for name, selection in packet.get("dataset_fallbacks", {}).items():
        yield "dataset_fallbacks.%s" % name, selection


def semantic_errors(packet, dataset, kind):
    errors = []
    if kind not in ("fleet", "golden"):
        errors.append("kind must be fleet or golden")
        return errors
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
    attempt = meta.get("attempt")
    remediates = meta.get("remediates_run_id")
    if attempt == 1 and remediates not in (None, ""):
        errors.append("attempt 1 may not set remediates_run_id")
    if attempt == 2 and not isinstance(remediates, str):
        errors.append("attempt 2 requires remediates_run_id")

    if dataset.get("naics") != packet.get("naics"):
        errors.append("dataset NAICS does not match packet")
    if dataset.get("title") != packet.get("title"):
        errors.append("dataset title does not match packet")

    source_ids = [source.get("id") for source in packet.get("sources", [])]
    if len(source_ids) != len(set(source_ids)):
        errors.append("source IDs must be unique")
    source_set = set(source_ids)
    source_urls = [source.get("url") for source in packet.get("sources", [])]
    if len(source_urls) != len(set(source_urls)):
        errors.append("source URLs must be unique; combine support descriptions")

    for path, selection in _iter_selections(packet):
        if not isinstance(selection, dict):
            continue
        refs = selection.get("source_ids", [])
        unknown = sorted(set(refs) - source_set)
        if unknown:
            errors.append("%s references unknown source IDs %s" % (path, unknown))
        method = selection.get("method")
        evidence_quality = selection.get("evidence_quality")
        if evidence_quality == "NONE" and refs:
            errors.append("%s evidence_quality NONE requires empty source_ids" % path)
        if evidence_quality != "NONE" and not refs:
            errors.append("%s non-NONE evidence_quality requires source_ids" % path)
        if method in ("OBSERVED", "CALCULATED") and not refs:
            errors.append("%s %s requires at least one source ID" % (path, method))
        if method == "CALCULATED":
            calculation = selection.get("calculation")
            if not isinstance(calculation, dict):
                errors.append("%s CALCULATED requires calculation" % path)
            else:
                operand_refs = [item.get("source_id") for item in calculation.get("operands", [])]
                missing_refs = sorted(set(operand_refs) - set(refs))
                if missing_refs:
                    errors.append("%s calculation operand source IDs not in selection: %s" % (path, missing_refs))
                if sorted(set(operand_refs) - source_set):
                    errors.append("%s calculation references unknown sources" % path)
                try:
                    computed = _safe_eval(calculation)
                    if not _is_number(selection.get("value")) or abs(float(selection["value"]) - computed) > VALUE_TOL:
                        errors.append("%s authored value does not equal safe calculation" % path)
                except (SyntaxError, ValueError) as exc:
                    errors.append("%s unsafe calculation: %s" % (path, exc))

    fallbacks = packet.get("dataset_fallbacks", {})
    for name in ("labor_share", "n_band"):
        dataset_value = dataset.get(name, {}).get("value")
        if dataset_value is None and name not in fallbacks:
            errors.append("dataset %s.value is null; fallback is required" % name)
        if dataset_value is not None and name in fallbacks:
            errors.append("dataset %s.value is non-null; fallback is forbidden" % name)

    role_mix = dataset.get("role_mix", {})
    occupations = role_mix.get("occupations") if isinstance(role_mix, dict) else None
    if not isinstance(occupations, list) or not occupations:
        errors.append("dataset role_mix.occupations must be non-empty")
    else:
        supplied_socs = [item.get("soc") for item in occupations]
        judgments = packet.get("scorecard", {}).get("ai_replaceable_share", {}).get("role_judgments", [])
        judgment_socs = [item.get("soc") for item in judgments]
        if len(supplied_socs) != len(set(supplied_socs)):
            errors.append("dataset role mix contains duplicate SOCs")
        if len(judgment_socs) != len(set(judgment_socs)):
            errors.append("role judgments contain duplicate SOCs")
        missing = sorted(set(supplied_socs) - set(judgment_socs))
        unexpected = sorted(set(judgment_socs) - set(supplied_socs) - {"RESIDUAL"})
        if missing:
            errors.append("role judgments missing supplied SOCs: %s" % missing)
        if unexpected:
            errors.append("role judgments contain unapproved SOCs: %s" % unexpected)
        if all(_is_number(item.get("wage_share")) for item in occupations):
            residual = 1.0 - sum(item["wage_share"] for item in occupations)
            if residual < -RESIDUAL_TOL:
                errors.append("dataset role wage shares exceed 1.0")
            has_residual = "RESIDUAL" in judgment_socs
            if residual > RESIDUAL_TOL and not has_residual:
                errors.append("role judgments require RESIDUAL for %.6f wage share" % residual)
            if residual <= RESIDUAL_TOL and has_residual:
                errors.append("RESIDUAL role is forbidden when no material residual exists")

    scorecard = packet.get("scorecard", {})
    adoption = scorecard.get("current_adoption_pct", {}).get("value")
    t50 = scorecard.get("t50_years", {}).get("value")
    if _is_number(adoption) and _is_number(t50):
        if adoption >= 0.5 and t50 != 0:
            errors.append("t50_years must be 0 when adoption is at least 50%")
        if adoption < 0.5 and t50 <= 0:
            errors.append("t50_years must be positive when adoption is below 50%")
    return errors


def _finalize_selection(selection):
    result = copy.deepcopy(selection)
    if result["method"] == "CALCULATED":
        result["value"] = _safe_eval(result["calculation"])
    result["provenance_type"] = PROVENANCE[result["method"]]
    return result


def _inject_dataset(packet, dataset):
    injected = {}
    fallbacks = packet["dataset_fallbacks"]
    for name in ("labor_share", "role_mix", "n_total", "n_band"):
        item = dataset[name]
        if name in ("labor_share", "n_band") and isinstance(item, dict) and item.get("value") is None:
            injected[name] = _finalize_selection(fallbacks[name])
        else:
            injected[name] = copy.deepcopy(item)
    return injected


def _finalize_roles(role_packet, role_mix):
    by_soc = {item["soc"]: item for item in role_packet["role_judgments"]}
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
            "soc": "RESIDUAL", "role": "Unlisted occupations / residual wage share",
            "labor_share_of_total": residual,
            "within_role_automatable_fraction": fraction,
            "contribution": residual * fraction,
            "rationale": judgment["rationale"],
            "plausible_range": judgment["plausible_range"],
        })
    result = {key: copy.deepcopy(value) for key, value in role_packet.items() if key != "role_judgments"}
    result["value"] = sum(item["contribution"] for item in breakdown)
    result["provenance_type"] = "ESTIMATE"
    result["breakdown_by_role"] = breakdown
    return result


def _arithmetic_strings(computed, rec):
    inputs, dataset = rec["inputs"], rec["dataset_inputs"]
    return {
        "V": "Python v3.1.2: V_raw = %.12g × %.12g = %.12g; V = 10 × min(1, V_raw / 0.25) = %.12g" % (dataset["labor_share"]["value"], inputs["ai_replaceable_share"]["value"], computed["V_raw"], computed["V"]),
        "C": "Python v3.1.2: C = 10 × %.12g × %.12g = %.12g" % (inputs["pi_dist"]["value"], inputs["pi_moat"]["value"], computed["C"]),
        "A": "Python v3.1.2: A = 10 when t50=0 else min(10,10/t50); t50=%.12g, A=%.12g" % (inputs["t50_years"]["value"], computed["A"]),
        "B": "Python v3.1.2: TD=%.12g, OW=%.12g, CFD=%.12g; B=10×sqrt(TD×OW)/(1+0.3×CFD)=%.12g" % (computed["TD"], computed["OW"], computed["CFD"], computed["B"]),
        "M": "Python v3.1.2: M=clamp(4×(exit−buy)/buy,0,10)=%.12g" % computed["M"],
    }


def finalize(packet, dataset, kind):
    errors = semantic_errors(packet, dataset, kind)
    if errors:
        return None, errors
    rec = {
        "naics": packet["naics"], "title": packet["title"],
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
    rec["run_meta"]["finalizer_version"] = FINALIZER_VERSION
    rec["run_meta"]["memo_renderer_version"] = MEMO_RENDERER_VERSION
    for name, selection in packet["scorecard"].items():
        if name == "ai_replaceable_share":
            rec["inputs"][name] = _finalize_roles(selection, rec["dataset_inputs"]["role_mix"])
        elif name == "owners_60plus_pct":
            owner = _finalize_selection(selection["selection"])
            owner["succession_shortage_documented"] = _finalize_selection(selection["succession_shortage_documented"])
            rec["inputs"][name] = owner
        else:
            rec["inputs"][name] = _finalize_selection(selection)
    computed, calculation_errors = build.calculate(rec)
    if calculation_errors:
        return None, calculation_errors
    arithmetic = _arithmetic_strings(computed, rec)
    rec["scores"] = {name: {"arithmetic": arithmetic[name], "score": computed[name]} for name in ("V", "C", "A", "B", "M")}
    rec["S"] = computed["S"]
    rec["cross_checks"]["uplift_pp"] = computed["V_raw"] * 100.0
    thresholds = load_json(os.path.join(HERE, "thresholds.json"))
    rec["decision"] = build.decide(rec["S"], {name: computed[name] for name in ("V", "C", "A", "B", "M")}, rec["cross_checks"]["terminal_value"]["class"], rec["confidence_overall"], thresholds)
    schema = load_json(os.path.join(SCHEMAS, "run_record_v3_1_2.schema.json"))
    errors = build.schema_errors(rec, schema, schema)
    if errors:
        return None, errors
    _computed, arithmetic_errors, _deltas = build.recompute(rec)
    if arithmetic_errors:
        return None, arithmetic_errors
    return rec, []


def render_memo(rec):
    narrative_titles = [
        ("executive_view", "Executive view"), ("how_ai_changes_work", "How AI changes the work"),
        ("value_capture", "Value capture"), ("adoption_timing", "Adoption timing"),
        ("consolidation_economics", "Consolidation and economics"), ("terminal_demand", "Terminal demand"),
        ("risks_and_uncertainty", "Risks and uncertainty"),
    ]
    lines = ["# %s — %s" % (rec["naics"], rec["title"]), "", "*v3.1.2 research memo · run `%s` · %s · %s*" % (rec["run_meta"]["run_id"], rec["run_meta"]["model_id"], rec["run_meta"]["run_date"]), ""]
    for key, title in narrative_titles:
        lines.extend(["## " + title, "", rec["narrative"][key], ""])
    lines.extend(["## Deterministic scorecard", "", "| Factor | Score |", "|---|---:|"])
    for name in ("V", "C", "A", "B", "M"):
        lines.append("| %s | %.2f |" % (name, rec["scores"][name]["score"]))
    lines.extend(["| **S** | **%.2f** |" % rec["S"], "", "**Verdict:** `%s`  " % rec["decision"]["verdict"], "**Overall confidence:** `%s`  " % rec["confidence_overall"], "**Terminal demand:** `%s`" % rec["cross_checks"]["terminal_value"]["class"], "", "## Selected inputs", "", "| Input | Value | Method | Confidence | Range |", "|---|---:|---|---|---|"])
    for name, value in rec["inputs"].items():
        shown = value["value"]
        if isinstance(shown, float):
            shown = "%.4g" % shown
        lines.append("| `%s` | %s | %s | %s | %s |" % (name, str(shown).replace("|", "\\|"), value["method"], value["confidence"], value["plausible_range"].replace("|", "\\|")))
    caveats = build.v312_declared_caveats(rec)
    lines.extend(["", "## Declared caveats", ""])
    lines.extend(["- " + item for item in caveats] or ["- No score-input caveats were declared."])
    lines.extend(["", "## Sources", ""])
    for source in rec["sources"]:
        lines.append("- **%s. [%s](%s)** — %s (accessed %s)" % (source["id"], source["title"], source["url"], source["what_it_supports"], source["access_date"]))
    lines.extend(["", "---", "", "Scores, verdict, deterministic inputs and this memo were rendered by `%s`; do not hand-edit." % MEMO_RENDERER_VERSION, ""])
    return "\n".join(lines)


def serialize_record(rec):
    """Canonical bytes written by the finalizer and checked by the campaign."""
    return (json.dumps(rec, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


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
    packet_schema = load_json(os.path.join(SCHEMAS, "research_packet_v3_1_2.schema.json"))
    errors = build.schema_errors(packet, packet_schema, packet_schema)
    if errors:
        print("FINALIZE FAILED — packet schema:", file=sys.stderr)
        for error in errors:
            print("  " + error, file=sys.stderr)
        return 1
    rec, errors = finalize(packet, dataset, args.kind)
    if errors:
        print("FINALIZE FAILED — semantic/injection checks:", file=sys.stderr)
        for error in errors:
            print("  " + error, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(args.memo)), exist_ok=True)
    with open(args.output, "wb") as handle:
        handle.write(serialize_record(rec))
    with open(args.memo, "w", encoding="utf-8") as handle:
        handle.write(render_memo(rec))
    print("OK: finalized and rendered %s (%s)" % (rec["naics"], rec["run_meta"]["run_id"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
