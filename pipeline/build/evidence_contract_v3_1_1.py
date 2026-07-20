#!/usr/bin/env python3
"""Deterministic v3.1.1 evidence-contract checks.

The model may choose an input method, but it cannot author final provenance.
This module makes each method mechanically distinct:

- OBSERVED: selected value equals an explicitly repeated source value.
- CALCULATED: selected value equals a safe arithmetic expression over
  fact-backed numeric operands.
- ESTIMATE: the judgment is explicit and carries a basis/range.

It also enforces atomic fact IDs, contiguous quotes, structured scope and the
applicable structured-disclosure invariants. It performs no web or model calls.
"""

import ast
from datetime import date
import math
import re


METHOD_TO_PROVENANCE = {
    "OBSERVED": "DIRECT",
    "CALCULATED": "DERIVED",
    "ESTIMATE": "ESTIMATE",
}
CALC_TOL = 1e-9
RESIDUAL_TOL = 0.0005
ELLIPSIS_RE = re.compile(r"\.\s*\.\s*\.|…")


class CalculationError(ValueError):
    pass


def _eval_node(node, variables):
    if isinstance(node, ast.Expression):
        return _eval_node(node.body, variables)
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return float(node.value)
        raise CalculationError("only numeric constants are allowed")
    if isinstance(node, ast.Name):
        if node.id not in variables:
            raise CalculationError("unknown operand %r" % node.id)
        return variables[node.id]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _eval_node(node.operand, variables)
        return value if isinstance(node.op, ast.UAdd) else -value
    if isinstance(node, ast.BinOp) and isinstance(
        node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)
    ):
        left = _eval_node(node.left, variables)
        right = _eval_node(node.right, variables)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if right == 0:
            raise CalculationError("division by zero")
        return left / right
    raise CalculationError(
        "only operand names, numeric constants, parentheses and + - * / are allowed"
    )


def evaluate_calculation(calculation):
    """Return a finite numeric result or raise CalculationError."""
    operands = calculation.get("operands", [])
    names = [item.get("name") for item in operands]
    if len(names) != len(set(names)):
        raise CalculationError("operand names must be unique")
    variables = {item["name"]: float(item["value"]) for item in operands}
    try:
        tree = ast.parse(calculation.get("expression", ""), mode="eval")
    except (SyntaxError, ValueError) as exc:
        raise CalculationError("invalid arithmetic expression: %s" % exc)
    referenced_names = {
        node.id for node in ast.walk(tree) if isinstance(node, ast.Name)
    }
    unused = sorted(set(names) - referenced_names)
    if not referenced_names:
        raise CalculationError("calculation must reference at least one operand")
    if unused:
        raise CalculationError("calculation has unused operands: %s" % unused)
    result = _eval_node(tree, variables)
    if not math.isfinite(result):
        raise CalculationError("calculation result must be finite")
    return result


def selection_items(draft):
    """Yield (path, selection) for every v3.1.1 selected-value packet."""
    for name, value in draft.get("dataset_fallbacks", {}).items():
        yield "dataset_fallbacks.%s" % name, value
    for name, value in draft.get("inputs", {}).items():
        if name == "ai_replaceable_share":
            continue
        if name == "owners_60plus_pct":
            yield "inputs.owners_60plus_pct.selection", value.get("selection", {})
        else:
            yield "inputs.%s" % name, value


def final_selection_items(record):
    """Yield selected-value packets from a finalized v3.1.1 record."""
    for name in ("labor_share", "n_band"):
        value = record.get("dataset_inputs", {}).get(name, {})
        # Deterministic dataset packets may have a free-text `method`; only a
        # null-dataset fallback carries the final provenance contract.
        if isinstance(value, dict) and "provenance_type" in value:
            yield "dataset_inputs.%s" % name, value
    for name, value in record.get("inputs", {}).items():
        if name != "ai_replaceable_share":
            yield "inputs.%s" % name, value


def _fact_reference_errors(path, packet, fact_ids):
    errors = []
    refs = packet.get("fact_ids", [])
    if len(refs) != len(set(refs)):
        errors.append("%s.fact_ids contains duplicates" % path)
    unknown = sorted(set(refs) - fact_ids)
    if unknown:
        errors.append("%s.fact_ids references unknown facts: %s" % (path, unknown))
    quality = packet.get("evidence_quality")
    if refs and quality == "NONE":
        errors.append("%s: fact_ids is non-empty but evidence_quality is NONE" % path)
    if not refs and quality != "NONE":
        errors.append("%s: empty fact_ids requires evidence_quality NONE" % path)
    return errors


def _selection_method_errors(path, selection):
    errors = []
    method = selection.get("method")
    value = selection.get("value")
    refs = selection.get("fact_ids", [])
    observed_present = "observed_value" in selection
    calculation_present = "calculation" in selection
    estimate_present = "estimate_basis" in selection

    if method == "OBSERVED":
        if not refs:
            errors.append("%s: OBSERVED requires at least one fact_id" % path)
        if not observed_present:
            errors.append("%s: OBSERVED requires observed_value" % path)
        elif selection.get("observed_value") != value:
            errors.append("%s: OBSERVED value must equal observed_value exactly" % path)
        if calculation_present or estimate_present:
            errors.append(
                "%s: OBSERVED forbids calculation and estimate_basis" % path
            )
    elif method == "CALCULATED":
        if not refs:
            errors.append("%s: CALCULATED requires at least one fact_id" % path)
        if observed_present or estimate_present:
            errors.append(
                "%s: CALCULATED forbids observed_value and estimate_basis" % path
            )
        calculation = selection.get("calculation")
        if not isinstance(calculation, dict):
            errors.append("%s: CALCULATED requires calculation" % path)
        else:
            operand_fact_ids = [item.get("fact_id") for item in calculation.get("operands", [])]
            missing_refs = sorted(set(operand_fact_ids) - set(refs))
            if missing_refs:
                errors.append(
                    "%s.calculation operands use fact IDs absent from fact_ids: %s"
                    % (path, missing_refs)
                )
            try:
                computed = evaluate_calculation(calculation)
            except (CalculationError, KeyError, TypeError, ValueError) as exc:
                errors.append("%s.calculation: %s" % (path, exc))
            else:
                if not isinstance(value, (int, float)) or isinstance(value, bool):
                    errors.append("%s: CALCULATED value must be numeric" % path)
                elif not math.isclose(float(value), computed, rel_tol=0, abs_tol=CALC_TOL):
                    errors.append(
                        "%s: CALCULATED value %r does not equal formula result %.12g"
                        % (path, value, computed)
                    )
    elif method == "ESTIMATE":
        if observed_present or calculation_present:
            errors.append("%s: ESTIMATE forbids observed_value and calculation" % path)
        if not estimate_present:
            errors.append("%s: ESTIMATE requires estimate_basis" % path)
    else:
        errors.append("%s: unsupported method %r" % (path, method))
    return errors


def _evidence_fact_errors(record):
    errors = []
    facts = record.get("evidence_facts", [])
    fact_ids_list = [fact.get("id") for fact in facts if isinstance(fact, dict)]
    fact_ids = set(fact_ids_list)
    if len(fact_ids_list) != len(fact_ids):
        duplicates = sorted(
            fact_id for fact_id in fact_ids if fact_ids_list.count(fact_id) > 1
        )
        errors.append("evidence_facts contains duplicate IDs: %s" % duplicates)

    for index, fact in enumerate(facts):
        quote = fact.get("quote", "") if isinstance(fact, dict) else ""
        if ELLIPSIS_RE.search(quote):
            errors.append(
                "evidence_facts[%d].quote must be one contiguous excerpt; ellipses are forbidden"
                % index
            )
        access_date = fact.get("access_date") if isinstance(fact, dict) else None
        try:
            date.fromisoformat(access_date)
        except (TypeError, ValueError):
            errors.append(
                "evidence_facts[%d].access_date must be a real ISO date" % index
            )

    run_date = record.get("run_meta", {}).get("run_date")
    try:
        date.fromisoformat(run_date)
    except (TypeError, ValueError):
        errors.append("run_meta.run_date must be a real ISO date")

    for pair in _source_audit_pairs(record):
        if not re.fullmatch(r"evidence_facts\[[0-9]+\]\.url", pair["input_path"]):
            errors.append(
                "%s: URLs are permitted only in evidence_facts[].url, found %s"
                % (pair["input_path"], pair["url"])
            )
    return errors, fact_ids


def _market_boundary_errors(record):
    errors = []
    disclosures = record.get("disclosures", {})
    boundary = disclosures.get("market_boundary", {})
    if record.get("heterogeneous") is True and boundary.get("applies") is not True:
        errors.append("heterogeneous=true requires disclosures.market_boundary.applies=true")
    if boundary.get("applies") is True:
        subsegments = boundary.get("subsegments", [])
        names = [item.get("name") for item in subsegments if isinstance(item, dict)]
        ranks = [item.get("revenue_rank") for item in subsegments if isinstance(item, dict)]
        if len(names) != len(set(names)):
            errors.append("disclosures.market_boundary subsegment names must be unique")
        if len(ranks) != len(set(ranks)):
            errors.append("disclosures.market_boundary revenue ranks must be unique")
        if not {1, 2, 3}.issubset(set(ranks)):
            errors.append("disclosures.market_boundary must include revenue ranks 1, 2 and 3")
        if boundary.get("dominant_subsegment") not in names:
            errors.append(
                "disclosures.market_boundary dominant_subsegment must name a listed subsegment"
            )
    return errors


def semantic_errors(draft):
    """Return named v3.1.1 evidence/method errors after schema validation."""
    errors, fact_ids = _evidence_fact_errors(draft)

    for path, selection in selection_items(draft):
        errors.extend(_fact_reference_errors(path, selection, fact_ids))
        errors.extend(_selection_method_errors(path, selection))

    role_packet = draft.get("inputs", {}).get("ai_replaceable_share", {})
    errors.extend(
        _fact_reference_errors(
            "inputs.ai_replaceable_share", role_packet, fact_ids
        )
    )
    errors.extend(_market_boundary_errors(draft))
    return errors


def final_record_semantic_errors(record):
    """Independently validate the evidence contract on a finalized record.

    This is intentionally called by build.py. A record must not become trusted
    merely because it claims to have passed the finalizer.
    """
    errors, fact_ids = _evidence_fact_errors(record)

    for path, selection in final_selection_items(record):
        errors.extend(_fact_reference_errors(path, selection, fact_ids))
        errors.extend(_selection_method_errors(path, selection))
        expected = METHOD_TO_PROVENANCE.get(selection.get("method"))
        if selection.get("provenance_type") != expected:
            errors.append(
                "%s.provenance_type %r does not match Python mapping %r"
                % (path, selection.get("provenance_type"), expected)
            )

    role_packet = record.get("inputs", {}).get("ai_replaceable_share", {})
    errors.extend(
        _fact_reference_errors("inputs.ai_replaceable_share", role_packet, fact_ids)
    )
    if role_packet.get("method") != "ESTIMATE":
        errors.append("inputs.ai_replaceable_share.method must be ESTIMATE")
    if role_packet.get("provenance_type") != "ESTIMATE":
        errors.append("inputs.ai_replaceable_share.provenance_type must be ESTIMATE")
    errors.extend(_final_role_injection_errors(record))
    errors.extend(_market_boundary_errors(record))
    return errors


def _final_role_injection_errors(record):
    """Check that the finalized role rows still match the injected dataset."""
    errors = []
    role_packet = record.get("inputs", {}).get("ai_replaceable_share", {})
    role_mix = record.get("dataset_inputs", {}).get("role_mix", {})
    occupations = role_mix.get("occupations") if isinstance(role_mix, dict) else None
    if not isinstance(occupations, list) or not occupations:
        return ["dataset_inputs.role_mix.occupations must be a non-empty array"]

    supplied_socs = [item.get("soc") for item in occupations if isinstance(item, dict)]
    if len(supplied_socs) != len(occupations):
        return ["dataset_inputs.role_mix.occupations must contain objects"]
    if len(supplied_socs) != len(set(supplied_socs)):
        errors.append("dataset_inputs.role_mix contains duplicate SOC codes")

    wage_shares = [item.get("wage_share") for item in occupations]
    if any(
        not isinstance(value, (int, float)) or isinstance(value, bool)
        for value in wage_shares
    ):
        return errors + ["every dataset occupation requires numeric wage_share"]
    residual = 1.0 - sum(wage_shares)
    if residual < -RESIDUAL_TOL:
        errors.append("dataset role wage shares exceed 1.0 by %.6f" % -residual)

    expected = [
        (item["soc"], item.get("title"), item["wage_share"])
        for item in occupations
    ]
    if residual > RESIDUAL_TOL:
        expected.append(
            ("RESIDUAL", "Unlisted occupations / residual wage share", residual)
        )
    actual = role_packet.get("breakdown_by_role", [])
    if not isinstance(actual, list):
        return errors + ["inputs.ai_replaceable_share.breakdown_by_role must be an array"]
    if len(actual) != len(expected):
        errors.append(
            "inputs.ai_replaceable_share role count %d does not match injected dataset %d"
            % (len(actual), len(expected))
        )
        return errors
    for index, ((soc, title, share), role) in enumerate(zip(expected, actual)):
        path = "inputs.ai_replaceable_share.breakdown_by_role[%d]" % index
        if role.get("soc") != soc:
            errors.append("%s.soc %r does not match injected %r" % (path, role.get("soc"), soc))
        if role.get("role") != title:
            errors.append("%s.role %r does not match injected %r" % (path, role.get("role"), title))
        actual_share = role.get("labor_share_of_total")
        if (
            not isinstance(actual_share, (int, float))
            or isinstance(actual_share, bool)
            or not math.isclose(float(actual_share), float(share), rel_tol=0, abs_tol=CALC_TOL)
        ):
            errors.append(
                "%s.labor_share_of_total %r does not match injected %.12g"
                % (path, actual_share, share)
            )
    return errors


def provenance_for(selection):
    """Return Python-assigned final provenance for a schema-valid selection."""
    return METHOD_TO_PROVENANCE[selection["method"]]


def _source_audit_pairs(record):
    """Local URL inventory to keep this module import-cycle free."""
    url_re = re.compile(r"https?://[^\s<>\"']+")
    found = set()

    def trim(url):
        url = url.rstrip(".,;:]}")
        while url.endswith(")") and url.count(")") > url.count("("):
            url = url[:-1]
        return url

    def walk(value, path):
        if isinstance(value, dict):
            for key in sorted(value):
                child = "%s.%s" % (path, key) if path else key
                walk(value[key], child)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                walk(item, "%s[%d]" % (path, index))
        elif isinstance(value, str):
            for match in url_re.finditer(value):
                found.add((path, trim(match.group(0))))

    walk(record, "")
    return [
        {"input_path": path, "url": url}
        for path, url in sorted(found, key=lambda pair: (pair[0], pair[1]))
    ]
