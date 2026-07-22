#!/usr/bin/env python3
"""Validate, finalize, score, and render one isolated v4.2 research packet."""

import argparse
import ast
import copy
from datetime import date
from decimal import Decimal, DivisionByZero, InvalidOperation, Overflow, localcontext
import hashlib
import importlib.util
import json
import math
import os
import re
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMAS = os.path.join(HERE, "schemas")
FINALIZER_VERSION = "finalizer-4.2"
MEMO_RENDERER_VERSION = "memo-renderer-4.2"
BRIDGE_FIELDS = ("population", "geography", "period", "unit", "business_model")
MAX_EXPRESSION_LENGTH = 512
MAX_AST_NODES = 64
MAX_AST_DEPTH = 16
MAX_OPERANDS = 16
MAX_DECIMAL_ABS = Decimal("1e100")
DECIMAL_PRECISION = 28
VALUE_TOL = Decimal("1e-12")
SHARE_TOL = 1e-9
ROLE_WEIGHT_TOL = 1e-12
COVERAGE_TOL = 5e-4
HASH_KEYS = (
    "prompt_sha256", "dataset_sha256", "spec_sha256", "methodology_sha256",
    "thresholds_sha256", "research_packet_schema_sha256", "dataset_schema_sha256",
    "industry_spec_schema_sha256", "run_record_schema_sha256", "scoring_sha256",
    "finalizer_sha256",
)


def _load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


legacy_build = _load_module("legacy_schema_v4_2", "build.py")
scoring = _load_module("scoring_v4_2_finalizer", "v4_2_scoring.py")


class ContractError(ValueError):
    pass


def _reject_constant(value):
    raise ContractError("non-standard JSON constant %r is forbidden" % value)


def _closed_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ContractError("duplicate JSON key %r" % key)
        result[key] = value
    return result


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle, parse_constant=_reject_constant, object_pairs_hook=_closed_pairs)


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_sha256(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                         allow_nan=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def _complete_bridge(value):
    return (isinstance(value, dict) and set(value) == set(BRIDGE_FIELDS)
            and all(isinstance(value[field], str) and value[field].strip() for field in BRIDGE_FIELDS))


def _schema_errors(value, schema):
    try:
        return legacy_build.schema_errors(value, schema, schema)
    except (OverflowError, ValueError, TypeError, RecursionError, MemoryError) as exc:
        return ["schema validation failed safely: %s" % exc]


def _decimal(value):
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError, OverflowError) as exc:
        raise ContractError("invalid decimal value: %s" % exc)
    if not result.is_finite() or abs(result) > MAX_DECIMAL_ABS:
        raise ContractError("decimal value is non-finite or exceeds safe magnitude")
    return result


def _ast_depth(node):
    children = list(ast.iter_child_nodes(node))
    return 1 if not children else 1 + max(_ast_depth(child) for child in children)


def safe_calculation(calculation):
    expression, operands = calculation.get("expression"), calculation.get("operands")
    if not isinstance(expression, str) or not expression or len(expression) > MAX_EXPRESSION_LENGTH:
        raise ContractError("calculation expression length must be 1..%d" % MAX_EXPRESSION_LENGTH)
    if not isinstance(operands, list) or not (1 <= len(operands) <= MAX_OPERANDS):
        raise ContractError("calculation requires 1..%d operands" % MAX_OPERANDS)
    names = [item.get("name") for item in operands if isinstance(item, dict)]
    if len(names) != len(operands) or len(names) != len(set(names)):
        raise ContractError("calculation operand names must be present and unique")
    values = {item["name"]: _decimal(item.get("value")) for item in operands}
    try:
        tree = ast.parse(expression, mode="eval")
    except (SyntaxError, ValueError, TypeError, MemoryError, RecursionError) as exc:
        raise ContractError("calculation parse failed: %s" % exc)
    nodes = list(ast.walk(tree))
    if len(nodes) > MAX_AST_NODES:
        raise ContractError("calculation exceeds %d AST nodes" % MAX_AST_NODES)
    if _ast_depth(tree) > MAX_AST_DEPTH:
        raise ContractError("calculation exceeds AST depth %d" % MAX_AST_DEPTH)
    used = set()

    def visit(node):
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
                raise ContractError("calculation constants must be finite numbers")
            return _decimal(node.value)
        if isinstance(node, ast.Name):
            if node.id not in values:
                raise ContractError("unknown calculation operand %r" % node.id)
            used.add(node.id)
            return values[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = visit(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Add): result = left + right
            elif isinstance(node.op, ast.Sub): result = left - right
            elif isinstance(node.op, ast.Mult): result = left * right
            else:
                if right == 0: raise ContractError("division by zero")
                result = left / right
            if not result.is_finite() or abs(result) > MAX_DECIMAL_ABS:
                raise ContractError("calculation result is non-finite or exceeds safe magnitude")
            return result
        raise ContractError("unsafe calculation syntax: %s" % type(node).__name__)

    try:
        with localcontext() as context:
            context.prec = DECIMAL_PRECISION
            result = visit(tree)
    except (DivisionByZero, InvalidOperation, Overflow, OverflowError, RecursionError) as exc:
        raise ContractError("calculation failed safely: %s" % exc)
    unused = sorted(set(values) - used)
    if unused:
        raise ContractError("calculation operands are unused: %s" % unused)
    return result


def _support_flags(item, source_set):
    refs = set(item.get("source_ids", []))
    endpoint = item.get("endpoint_support")
    endpoints_supported = False
    endpoint_source_ids = set()
    if isinstance(endpoint, dict) and set(endpoint) == {"low_source_ids", "base_source_ids", "high_source_ids"}:
        endpoint_refs = [endpoint[name] for name in ("low_source_ids", "base_source_ids", "high_source_ids")]
        endpoints_supported = all(isinstance(group, list) and group and set(group) <= refs <= source_set
                                  for group in endpoint_refs)
        if endpoints_supported:
            endpoint_source_ids = set().union(*(set(group) for group in endpoint_refs))
    validation = item.get("validation_support")
    validation_kind = None
    validation_well_formed = False
    if isinstance(validation, dict) and set(validation) == {
            "kind", "source_ids", "independence_basis", "rationale"}:
        validation_refs = validation.get("source_ids")
        if (validation.get("kind") in ("independent_corroboration", "longitudinal_validation")
                and isinstance(validation_refs, list) and validation_refs
                and set(validation_refs) <= refs <= source_set
                and validation.get("independence_basis") ==
                    "validation_source_ids_disjoint_from_primary_support"
                and isinstance(validation.get("rationale"), str) and validation["rationale"].strip()):
            validation_well_formed = True
            validation_ids = set(validation_refs)
            primary_ids = endpoint_source_ids if endpoint_source_ids else refs - validation_ids
            if primary_ids and primary_ids.isdisjoint(validation_ids):
                validation_kind = validation["kind"]
    return endpoints_supported, validation_kind, validation_well_formed


def _evidence_errors(path, item, source_set, *, numeric=True):
    errors = []
    method, state, quality = item.get("method"), item.get("evidence_state"), item.get("evidence_quality")
    refs = item.get("source_ids", [])
    if len(refs) != len(set(refs)):
        errors.append("%s source_ids must be unique" % path)
    if set(refs) - source_set:
        errors.append("%s references unknown source IDs" % path)
    endpoints_supported, validation_kind, validation_well_formed = _support_flags(item, source_set)
    has_bridge, has_endpoints, has_validation = (name in item for name in
                                                 ("bridge", "endpoint_support", "validation_support"))
    if state == "DIRECT":
        if method not in ("OBSERVED", "CALCULATED") or quality not in ("HIGH", "MED") or not refs:
            errors.append("%s DIRECT requires OBSERVED/CALCULATED, HIGH/MED, and sources" % path)
        if has_bridge or has_validation:
            errors.append("%s DIRECT forbids proxy bridge/validation support" % path)
        if numeric and (not has_endpoints or not endpoints_supported):
            errors.append("%s DIRECT requires source-backed low/base/high endpoints" % path)
    elif state == "PROXY":
        if method not in ("OBSERVED", "CALCULATED", "ESTIMATE") or quality not in ("HIGH", "MED", "LOW") or not refs:
            errors.append("%s PROXY requires an allowed method, evidence quality, and sources" % path)
        if not _complete_bridge(item.get("bridge")):
            errors.append("%s PROXY requires a complete closed bridge" % path)
        if numeric and (not has_endpoints or not endpoints_supported):
            errors.append("%s PROXY requires source-backed low/base/high endpoints" % path)
        if has_validation and not validation_well_formed:
            errors.append("%s proxy validation support is malformed or references unknown sources" % path)
    elif state in ("ASSUMPTION", "MISSING"):
        if method != "ESTIMATE" or quality != "NONE" or refs:
            errors.append("%s %s requires ESTIMATE, NONE, and no sources" % (path, state))
        if has_bridge or has_endpoints or has_validation:
            errors.append("%s %s forbids empirical support attestations" % (path, state))
    else:
        errors.append("%s evidence_state is invalid" % path)
    has_calc = "calculation" in item
    if method == "CALCULATED" and not has_calc:
        errors.append("%s CALCULATED requires calculation" % path)
    if method != "CALCULATED" and has_calc:
        errors.append("%s calculation is forbidden unless CALCULATED" % path)
    return errors


def _numeric_errors(path, item, source_set, low_bound, high_bound=None, *, strict=False, integer=False):
    errors = _evidence_errors(path, item, source_set)
    value, rng = item.get("value"), item.get("range", {})
    low, high = rng.get("low"), rng.get("high")
    if item.get("evidence_state") == "MISSING":
        if value is not None or low is not None or high is not None:
            errors.append("%s MISSING requires null value/range" % path)
        return errors
    if not all(_is_number(x) for x in (value, low, high)):
        errors.append("%s requires finite numeric value/low/high" % path)
        return errors
    if not low <= value <= high:
        errors.append("%s range must satisfy low <= value <= high" % path)
    if (strict and low <= low_bound) or (not strict and low < low_bound):
        errors.append("%s range.low violates its domain" % path)
    if high_bound is not None and high > high_bound:
        errors.append("%s range.high violates its domain" % path)
    if integer and not all(float(x).is_integer() for x in (value, low, high)):
        errors.append("%s value/range must be integers" % path)
    if item.get("method") == "CALCULATED" and "calculation" in item:
        calculation = item["calculation"]
        operand_refs = [operand.get("source_id") for operand in calculation.get("operands", [])]
        if set(operand_refs) - set(item.get("source_ids", [])):
            errors.append("%s calculation operand sources must be selected" % path)
        try:
            computed = safe_calculation(calculation)
            authored = _decimal(value)
            tolerance = max(VALUE_TOL, abs(computed) * VALUE_TOL)
            if abs(authored - computed) > tolerance:
                errors.append("%s authored value does not equal safe calculation" % path)
            if not (_decimal(low) <= computed <= _decimal(high)):
                errors.append("%s calculated value lies outside its range" % path)
        except ContractError as exc:
            errors.append("%s unsafe calculation: %s" % (path, exc))
    return errors


def _construct_evidence_errors(path, item, source_set):
    errors = []
    method, state, quality = item.get("method"), item.get("evidence_state"), item.get("evidence_quality")
    refs = item.get("source_ids", [])
    if len(refs) != len(set(refs)) or set(refs) - source_set:
        errors.append("%s source references are invalid" % path)
    has_bridge, has_validation = "bridge" in item, "validation_support" in item
    _endpoints, validation_kind, validation_well_formed = _support_flags(item, source_set)
    if state == "DIRECT":
        if method not in ("OBSERVED", "CALCULATED") or quality not in ("HIGH", "MED") or not refs:
            errors.append("%s DIRECT evidence contract failed" % path)
        if has_bridge or has_validation: errors.append("%s DIRECT forbids proxy support" % path)
    elif state == "PROXY":
        if method not in ("OBSERVED", "CALCULATED", "ESTIMATE") or quality not in ("HIGH", "MED", "LOW") or not refs:
            errors.append("%s PROXY evidence contract failed" % path)
        if not _complete_bridge(item.get("bridge")): errors.append("%s PROXY requires a complete bridge" % path)
        if not has_validation or not validation_well_formed:
            errors.append("%s PROXY requires closed validation support" % path)
    elif state in ("ASSUMPTION", "MISSING"):
        if method != "ESTIMATE" or quality != "NONE" or refs or has_bridge or has_validation:
            errors.append("%s %s must be source-free ESTIMATE/NONE" % (path, state))
    else:
        errors.append("%s evidence_state is invalid" % path)
    return errors


def _construct_supported(item, source_set):
    if item.get("evidence_state") == "DIRECT":
        return (item.get("evidence_quality") in ("HIGH", "MED") and bool(item.get("source_ids")))
    if item.get("evidence_state") == "PROXY":
        _endpoints, validation_kind, valid = _support_flags(item, source_set)
        return (item.get("evidence_quality") in ("HIGH", "MED") and _complete_bridge(item.get("bridge"))
                and valid and validation_kind is not None)
    return False


def _state_digest_payload(state):
    return {key: state.get(key) for key in (
        "state_id", "accounting", "size", "service_mix", "customer_concentration",
        "management_depth", "platform_quality", "entry_equivalence")}


def normalized_state_digest(state):
    return canonical_sha256(_state_digest_payload(state))


def dataset_errors(dataset):
    errors = _schema_errors(dataset, load_json(os.path.join(SCHEMAS, "dataset_v4_2.schema.json")))
    if errors: return errors
    occupations = dataset.get("role_mix", {}).get("occupations", [])
    socs = [item.get("soc") for item in occupations]
    if len(socs) != len(set(socs)): errors.append("dataset role_mix SOCs must be unique")
    for field in ("employment_share", "wage_share"):
        if sum(float(item.get(field, 0)) for item in occupations) > 1 + SHARE_TOL:
            errors.append("dataset role_mix %s sum exceeds 1" % field)
    n_band, n_total = dataset.get("n_band", {}).get("value"), dataset.get("n_total", {}).get("value")
    if n_band is not None and n_total is not None and n_band > n_total:
        errors.append("dataset n_band may not exceed n_total")
    for field in ("labor_share", "n_band"):
        item = dataset.get(field, {})
        if item.get("value") is None and item.get("quality") != "NONE":
            errors.append("missing dataset %s requires NONE quality" % field)
    return errors


def spec_errors(spec, dataset, methodology_sha256=None):
    errors = _schema_errors(spec, load_json(os.path.join(SCHEMAS, "industry_spec_v4_2.schema.json")))
    if errors: return errors
    if spec.get("naics") != dataset.get("naics") or spec.get("title") != dataset.get("title"):
        errors.append("industry spec identity must equal dataset identity")
    if spec.get("dataset_snapshot", {}).get("sha256") is None:
        errors.append("industry spec must bind a dataset snapshot")
    if methodology_sha256 is not None and spec.get("methodology_snapshot", {}).get("sha256") != methodology_sha256:
        errors.append("industry spec methodology snapshot digest mismatch")
    target = spec.get("target_archetype", {})
    alternatives = target.get("alternatives", [])
    ids = [item.get("id") for item in alternatives]
    if len(ids) != len(set(ids)): errors.append("archetype alternative IDs must be unique")
    source_ids = [item.get("id") for item in target.get("sources", [])]
    if len(source_ids) != len(set(source_ids)): errors.append("archetype source IDs must be unique")
    for option in alternatives:
        count = option.get("band_count", {})
        if not count.get("low", 0) <= count.get("base", -1) <= count.get("high", -1):
            errors.append("archetype %s count range is unordered" % option.get("id"))
        if len(option.get("source_ids", [])) != len(set(option.get("source_ids", []))) or set(option.get("source_ids", [])) - set(source_ids):
            errors.append("archetype %s source references are invalid" % option.get("id"))
    if alternatives:
        ordered = sorted(alternatives, key=lambda x: (-float(x["band_count"]["base"]), x["id"]))
        if target.get("selected_id") != ordered[0]["id"]:
            errors.append("selected archetype violates largest-base lexicographic rule")
        uncertain = False
        if len(ordered) > 1:
            first, second = ordered[0]["band_count"], ordered[1]["band_count"]
            uncertain = (first["base"] == 0 or (first["base"] - second["base"]) / first["base"] < .10
                         or second["high"] >= first["low"])
        if target.get("selection_uncertainty") != uncertain:
            errors.append("selection_uncertainty does not match the frozen top-two rule")
    residual = target.get("residual", {}).get("band_count", {})
    if residual and not residual.get("low", 0) <= residual.get("base", -1) <= residual.get("high", -1):
        errors.append("archetype residual range is unordered")
    coverage = target.get("enumeration_coverage", {})
    if coverage and not coverage.get("low", 0) <= coverage.get("base", -1) <= coverage.get("high", -1):
        errors.append("enumeration coverage range is unordered")
    n_band = dataset.get("n_band", {}).get("value")
    if n_band is not None and alternatives and residual:
        enumerated = sum(float(item["band_count"]["base"]) for item in alternatives)
        if abs(enumerated + float(residual["base"]) - float(n_band)) > SHARE_TOL:
            errors.append("alternative base counts plus residual must equal n_band")
        expected = 0 if n_band == 0 else enumerated / float(n_band)
        if abs(float(coverage.get("base", -1)) - expected) > COVERAGE_TOL:
            errors.append("enumeration_coverage.base does not reconcile to n_band")
    basis = spec.get("value_basis", {})
    mode, roles, sources = basis.get("mode"), basis.get("roles", []), basis.get("sources", [])
    approved = basis.get("approved_pass_through_categories", [])
    if len(approved) != len(set(approved)): errors.append("approved pass-through categories must be unique")
    if mode in ("target_specific", "assumption"):
        cash_ids = [basis.get("employee_cash_cost_id"), basis.get("controllable_contractor_cash_cost_id")]
        if any(not isinstance(x, str) or not x for x in cash_ids) or len(set(cash_ids)) != 2:
            errors.append("nonmissing cash cost IDs must be nonempty and distinct")
        role_ids = [item.get("role_id") for item in roles]
        if len(role_ids) != len(set(role_ids)): errors.append("target role IDs must be unique")
        if abs(sum(float(item.get("role_cash_cost_weight", 0)) for item in roles) - 1) > ROLE_WEIGHT_TOL:
            errors.append("target role cash-cost weights must sum to 1")
        basis_sources = [item.get("id") for item in sources]
        if len(basis_sources) != len(set(basis_sources)): errors.append("value-basis source IDs must be unique")
        if mode == "target_specific":
            for role in roles:
                if set(role.get("source_ids", [])) - set(basis_sources):
                    errors.append("role %s references unknown value-basis sources" % role.get("role_id"))
        elif sources or any(role.get("method") != "ESTIMATE"
                            or role.get("evidence_quality") != "NONE"
                            or role.get("source_ids") for role in roles):
            errors.append("assumption value basis must remain source-free ESTIMATE/NONE")
    elif mode == "missing":
        if basis.get("employee_cash_cost_id") is not None or basis.get("controllable_contractor_cash_cost_id") is not None or roles or sources:
            errors.append("missing value basis requires null cost IDs and empty roles/sources")
    else:
        errors.append("value_basis.mode must be target_specific, assumption, or missing")
    return errors


def packet_errors(packet, dataset, spec):
    errors = _schema_errors(packet, load_json(os.path.join(SCHEMAS, "research_packet_v4_2.schema.json")))
    if errors: return errors
    if packet["naics"] != dataset["naics"] or packet["title"] != dataset["title"]:
        errors.append("packet identity must equal dataset identity")
    source_ids = [item["id"] for item in packet["sources"]]
    source_urls = [item["url"] for item in packet["sources"]]
    if len(source_ids) != len(set(source_ids)): errors.append("packet source IDs must be unique")
    if len(source_urls) != len(set(source_urls)): errors.append("packet source URLs must be unique")
    source_set, inputs = set(source_ids), packet["inputs"]
    accounting_basis = inputs["recognized_revenue"]["accounting_basis"]
    money = [
        ("recognized_revenue", inputs["recognized_revenue"]),
        ("employee_cash_cost", inputs["employee_cash_cost"]["amount"]),
        ("controllable_contractor_cash_cost", inputs["controllable_contractor_cash_cost"]["amount"]),
    ]
    pass_ids, pass_categories = [], []
    for item in inputs["third_party_pass_through"]:
        pass_ids.append(item["cost_id"]); pass_categories.append(item["category"])
        money.append(("third_party_pass_through.%s" % item["cost_id"], item["amount"]))
    if len(pass_ids) != len(set(pass_ids)): errors.append("pass-through cost IDs must be unique")
    if len(pass_categories) != len(set(pass_categories)): errors.append("pass-through categories must be unique")
    approved = set(spec["value_basis"]["approved_pass_through_categories"])
    if set(pass_categories) - approved: errors.append("packet deducts an unapproved pass-through category")
    reconciliation = inputs["recognized_revenue"]["pass_through_reconciliation"]
    included, netted = reconciliation["included_cost_ids"], reconciliation["already_netted_cost_ids"]
    if set(included) & set(netted): errors.append("pass-through reconciliation partitions must be disjoint")
    if set(included) | set(netted) != set(pass_ids):
        errors.append("pass-through reconciliation must exactly partition every pass-through cost ID")
    basis = reconciliation["revenue_basis"]
    if accounting_basis["pass_through_presentation"] != basis:
        errors.append("recognized_revenue accounting basis must equal the pass-through revenue basis")
    if basis == "GROSS_OF_ALL" and (set(included) != set(pass_ids) or netted):
        errors.append("GROSS_OF_ALL requires every pass-through ID in included_cost_ids")
    if basis == "NET_OF_ALL" and (included or set(netted) != set(pass_ids)):
        errors.append("NET_OF_ALL requires every pass-through ID in already_netted_cost_ids")
    if basis == "MIXED" and (not included or not netted):
        errors.append("MIXED requires nonempty included and already-netted partitions")
    if not pass_ids and (basis != "GROSS_OF_ALL" or included or netted):
        errors.append("empty pass-through uses canonical GROSS_OF_ALL with empty partitions")
    errors.extend(_construct_evidence_errors("inputs.recognized_revenue.pass_through_reconciliation.evidence",
                                             reconciliation["evidence"], source_set))
    for path, item in money:
        errors.extend(_numeric_errors("inputs." + path, item, source_set, 0))
    mode = spec["value_basis"]["mode"]
    employee_id = inputs["employee_cash_cost"]["cost_id"]
    contractor_id = inputs["controllable_contractor_cash_cost"]["cost_id"]
    if mode in ("target_specific", "assumption"):
        expected_ids = (spec["value_basis"]["employee_cash_cost_id"], spec["value_basis"]["controllable_contractor_cash_cost_id"])
        if (employee_id, contractor_id) != expected_ids:
            errors.append("packet G cost IDs must exactly equal the frozen value basis")
        if set(pass_ids) & set(expected_ids):
            errors.append("a pass-through cost ID may not also enter G")
        if mode == "assumption":
            for path, item in (("employee_cash_cost", inputs["employee_cash_cost"]["amount"]),
                               ("controllable_contractor_cash_cost", inputs["controllable_contractor_cash_cost"]["amount"])):
                if item["evidence_state"] != "ASSUMPTION":
                    errors.append("assumption basis requires %s to remain ASSUMPTION" % path)
    else:
        if employee_id is not None or contractor_id is not None:
            errors.append("missing value basis requires null packet cost IDs")
        for path, item in (("employee_cash_cost", inputs["employee_cash_cost"]["amount"]),
                           ("controllable_contractor_cash_cost", inputs["controllable_contractor_cash_cost"]["amount"])):
            if item["evidence_state"] != "MISSING": errors.append("%s must remain MISSING" % path)
    authored_roles = inputs["target_role_judgments"]["roles"]
    expected_roles = spec["value_basis"]["roles"]
    if [item["role_id"] for item in authored_roles] != [item["role_id"] for item in expected_roles]:
        errors.append("packet role IDs/order must exactly equal the frozen value basis")
    for index, role in enumerate(authored_roles):
        errors.extend(_numeric_errors("inputs.target_role_judgments.roles[%d].removable_fraction" % index,
                                      role["removable_fraction"], source_set, 0, 1))
        if mode == "assumption" and role["removable_fraction"]["evidence_state"] != "ASSUMPTION":
            errors.append("assumption basis requires role removable fractions to remain ASSUMPTION")
    schedules = (("implementation_realization", "r", 1, 5, 0, 1),
                 ("implementation_investment", "k", 0, 5, 0, None),
                 ("commercial_retention", "c", 1, 5, 0, 1))
    for group, prefix, start, end, low, high in schedules:
        for number in range(start, end + 1):
            errors.extend(_numeric_errors("inputs.%s.%s%d" % (group, prefix, number),
                                          inputs[group]["%s%d" % (prefix, number)], source_set, low, high))
    numeric_specs = (
        ("target_archetype_coverage", 0, 1, False), ("five_year_sale_availability", 0, 1, False),
        ("buyer_access_win_share", 0, 1, False), ("deal_execution_capacity_5y", 0, None, False),
        ("integration_onboarding_capacity_5y", 0, None, False), ("buy_multiple", 0, None, True),
    )
    for name, low, high, strict in numeric_specs:
        errors.extend(_numeric_errors("inputs." + name, inputs[name], source_set, low, high, strict=strict))
    state = inputs["normalized_y5_operating_state"]
    errors.extend(_evidence_errors("inputs.normalized_y5_operating_state", state, source_set, numeric=True))
    if state["evidence_state"] == "PROXY" and "validation_support" not in state:
        errors.append("PROXY normalized_y5_operating_state requires validation support")
    descriptors = ("state_id", "state_digest", "accounting", "size", "service_mix", "customer_concentration",
                   "management_depth", "platform_quality")
    if state["evidence_state"] == "MISSING":
        if any(state[name] is not None for name in descriptors): errors.append("MISSING y5 state requires null descriptors")
    else:
        if any(state[name] != "HOLD_ENTRY_REFERENCE" for name in descriptors[2:]):
            errors.append("nonmissing y5 state must hold all six entry-reference dimensions")
        if state["state_digest"] != normalized_state_digest(state):
            errors.append("normalized y5 state digest is not canonical")
    downside = inputs["downside_exit_multiple"]
    if downside["normalized_y5_state_digest"] != state["state_digest"]:
        errors.append("downside multiple must bind the exact normalized y5 state digest")
    errors.extend(_numeric_errors("inputs.downside_exit_multiple.anchor", downside["anchor"], source_set, 0))
    if downside["anchor"]["anchor_basis"]["normalized_y5_state_digest"] != state["state_digest"]:
        errors.append("downside anchor must bind the exact normalized y5 state digest")
    channels = [item["channel"] for item in downside["adjustments"]]
    if len(channels) != len(set(channels)): errors.append("downside adjustment channels must be unique")
    for index, adjustment in enumerate(downside["adjustments"]):
        amount = adjustment["amount"]
        errors.extend(_numeric_errors("inputs.downside_exit_multiple.adjustments[%d].amount" % index,
                                      amount, source_set, -1e100, 0))
        if amount["evidence_state"] != "MISSING" and amount["range"]["high"] > 0:
            errors.append("downside adjustments may not encode favorable multiple expansion")
    basket = inputs["operator_controlled_value_added_demand_share_y5"]
    service_ids = [item["service_id"] for item in basket["services"]]
    if len(service_ids) != len(set(service_ids)): errors.append("survival service IDs must be unique")
    for index, service in enumerate(basket["services"]):
        for name in ("baseline_quantity", "baseline_revenue", "baseline_pass_through",
                     "y5_operator_controlled_quantity"):
            errors.extend(_numeric_errors("inputs.operator_survival.services[%d].%s" % (index, name),
                                          service[name], source_set, 0))
        for name in ("baseline_quantity", "baseline_revenue", "baseline_pass_through"):
            item = service[name]
            if (item["evidence_state"] != "MISSING"
                    and not (item["range"]["low"] == item["value"] == item["range"]["high"])):
                errors.append("inputs.operator_survival.services[%d].%s must be point-identified "
                              "for a fixed baseline" % (index, name))
    n_band = dataset["n_band"]["value"]
    coverage_item = inputs["target_archetype_coverage"]
    if n_band is not None and coverage_item["evidence_state"] != "MISSING":
        selected = next(item for item in spec["target_archetype"]["alternatives"]
                        if item["id"] == spec["target_archetype"]["selected_id"])
        counts = selected["band_count"]
        implied = ({name: 0 for name in ("low", "base", "high")} if n_band == 0 else
                   {name: min(1, float(counts[name]) / float(n_band)) for name in ("low", "base", "high")})
        if abs(float(coverage_item["value"]) - implied["base"]) > COVERAGE_TOL:
            errors.append("target coverage value must equal selected base count / n_band")
        if (coverage_item["range"]["low"] > implied["low"] + COVERAGE_TOL
                or coverage_item["range"]["high"] < implied["high"] - COVERAGE_TOL):
            errors.append("target coverage range must contain the count-implied range")
    return errors


def envelope_errors(envelope, packet, dataset, spec, paths):
    required = {"envelope_version", "kind", "naics", "title", "run_id", "run_date", "attempt",
                "remediates_run_id", "issued_by_task_path", "codex_task_path", "fork_policy", "role",
                "model_id", *HASH_KEYS}
    if not isinstance(envelope, dict): return ["execution envelope must be an object"]
    errors = []
    if set(envelope) - required: errors.append("execution envelope has unknown keys %s" % sorted(set(envelope) - required))
    if required - set(envelope): errors.append("execution envelope missing keys %s" % sorted(required - set(envelope)))
    if errors: return errors
    if envelope["envelope_version"] != "4.2": errors.append("execution envelope version must be 4.2")
    if envelope["kind"] != "target" or envelope["model_id"] not in ("gpt-5.6-terra", "gpt-5.6-sol"):
        errors.append("execution envelope must expose neutral target kind and an allowed model")
    if envelope["issued_by_task_path"] != "/root": errors.append("execution envelope must be root-issued")
    if not isinstance(envelope["codex_task_path"], str) or not envelope["codex_task_path"].startswith("/root/"):
        errors.append("execution envelope requires an isolated Codex task path")
    if envelope["fork_policy"] != "none" or envelope["role"] != "research":
        errors.append("execution envelope research isolation is invalid")
    if any(envelope[field] != packet.get(field) or envelope[field] != dataset.get(field) or envelope[field] != spec.get(field)
           for field in ("naics", "title")):
        errors.append("execution envelope identity mismatch")
    try:
        run_date = date.fromisoformat(envelope["run_date"])
        if run_date > date.today(): errors.append("execution run_date cannot be in the future")
    except (TypeError, ValueError):
        errors.append("execution run_date must be a real ISO date"); run_date = None
    attempt, parent = envelope["attempt"], envelope["remediates_run_id"]
    if attempt == 1 and parent is not None: errors.append("attempt 1 requires null remediation parent")
    elif attempt == 2 and (not isinstance(parent, str) or not parent): errors.append("attempt 2 requires remediation parent")
    elif attempt not in (1, 2): errors.append("attempt must be 1 or 2")
    actual = {
        "prompt_sha256": sha256_file(paths["prompt"]), "dataset_sha256": sha256_file(paths["dataset"]),
        "spec_sha256": sha256_file(paths["spec"]), "methodology_sha256": sha256_file(paths["methodology"]),
        "thresholds_sha256": sha256_file(os.path.join(HERE, "thresholds_v4_2.json")),
        "research_packet_schema_sha256": sha256_file(os.path.join(SCHEMAS, "research_packet_v4_2.schema.json")),
        "dataset_schema_sha256": sha256_file(os.path.join(SCHEMAS, "dataset_v4_2.schema.json")),
        "industry_spec_schema_sha256": sha256_file(os.path.join(SCHEMAS, "industry_spec_v4_2.schema.json")),
        "run_record_schema_sha256": sha256_file(os.path.join(SCHEMAS, "run_record_v4_2.schema.json")),
        "scoring_sha256": sha256_file(os.path.join(HERE, "v4_2_scoring.py")),
        "finalizer_sha256": sha256_file(__file__),
    }
    for key in HASH_KEYS:
        value = envelope[key]
        if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
            errors.append("%s must be lowercase SHA-256" % key)
        elif value != actual[key]: errors.append("execution envelope %s does not match exact artifact" % key)
    if spec["dataset_snapshot"]["sha256"] != actual["dataset_sha256"]:
        errors.append("industry spec dataset snapshot digest mismatch")
    if spec["methodology_snapshot"]["sha256"] != actual["methodology_sha256"]:
        errors.append("industry spec methodology snapshot digest mismatch")
    if run_date is not None:
        for source in packet.get("sources", []):
            try:
                if date.fromisoformat(source["access_date"]) > run_date:
                    errors.append("source %s access_date exceeds run_date" % source["id"])
            except (TypeError, ValueError): errors.append("source access_date is invalid")
    return errors


def _missing_selection(rationale):
    return {"value": None, "range": {"low": None, "high": None}, "authored_value": None,
            "authored_range": {"low": None, "high": None}, "method": "ESTIMATE",
            "evidence_state": "MISSING", "evidence_quality": "NONE", "confidence": "LOW",
            "source_ids": [], "rationale": rationale, "caveats": [], "bridge_supported": False,
            "endpoints_supported": False, "independent_validation": False,
            "longitudinal_validation": False, "resolution_type": "UNRESOLVED_MISSING",
            "provenance": {"derivation_method": "ESTIMATE", "evidence_state": "MISSING",
                           "resolution_type": "UNRESOLVED_MISSING"}}


def _dataset_selection(item, kind):
    if item["value"] is None: return _missing_selection("Normalized dataset has no defensible %s." % kind)
    value = item["value"]
    if item["quality"] not in ("HIGH", "MED"):
        return {"value": value, "range": {"low": value, "high": value}, "authored_value": value,
                "authored_range": {"low": value, "high": value}, "method": "ESTIMATE",
                "evidence_state": "ASSUMPTION", "evidence_quality": "NONE", "confidence": "LOW",
                "source_ids": [], "rationale": item["basis"], "caveats": [
                    "Normalized dataset value lacks MED/HIGH support and is not promoted to DIRECT."],
                "bridge_supported": False, "endpoints_supported": False,
                "independent_validation": False, "longitudinal_validation": False,
                "resolution_type": "DATASET", "provenance": {
                    "derivation_method": "ESTIMATE", "evidence_state": "ASSUMPTION",
                    "resolution_type": "DATASET"}}
    return {"value": value, "range": {"low": value, "high": value}, "authored_value": value,
            "authored_range": {"low": value, "high": value}, "method": "OBSERVED",
            "evidence_state": "DIRECT", "evidence_quality": item["quality"],
            "confidence": item["quality"] if item["quality"] in ("HIGH", "MED", "LOW") else "LOW",
            "source_ids": ["DATASET"], "rationale": item["basis"], "caveats": [], "bridge_supported": False,
            "endpoints_supported": True, "independent_validation": False,
            "longitudinal_validation": False, "resolution_type": "DATASET",
            "provenance": {"derivation_method": "OBSERVED", "evidence_state": "DIRECT",
                           "resolution_type": "DATASET"}}


def _finalize_selection(item, source_set, *, rationale_separation=None):
    result = copy.deepcopy(item)
    result["authored_value"] = copy.deepcopy(item["value"])
    result["authored_range"] = copy.deepcopy(item["range"])
    endpoints, validation_kind, _validation_well_formed = _support_flags(item, source_set)
    result["bridge_supported"] = item["evidence_state"] == "PROXY" and _complete_bridge(item.get("bridge"))
    result["endpoints_supported"] = endpoints if item["evidence_state"] in ("DIRECT", "PROXY") else False
    result["independent_validation"] = validation_kind == "independent_corroboration"
    result["longitudinal_validation"] = validation_kind == "longitudinal_validation"
    result.pop("endpoint_support", None); result.pop("validation_support", None)
    if item["evidence_state"] == "MISSING": resolution = "UNRESOLVED_MISSING"
    elif item["method"] == "CALCULATED":
        result["value"] = float(safe_calculation(item["calculation"])); resolution = "SAFE_CALCULATION"
    else: resolution = "AUTHORED"
    result["resolution_type"] = resolution
    result["provenance"] = {"derivation_method": item["method"], "evidence_state": item["evidence_state"],
                            "resolution_type": resolution}
    if rationale_separation is not None: result["rationale_separation_passed"] = rationale_separation
    return result


def _finalize_state(item, source_set):
    result = copy.deepcopy(item)
    endpoints, validation_kind, _validation_well_formed = _support_flags(item, source_set)
    result["bridge_supported"] = item["evidence_state"] == "PROXY" and _complete_bridge(item.get("bridge"))
    result["endpoints_supported"] = endpoints if item["evidence_state"] in ("DIRECT", "PROXY") else False
    result["independent_validation"] = validation_kind == "independent_corroboration"
    result["longitudinal_validation"] = validation_kind == "longitudinal_validation"
    result["rationale_separation_passed"] = True
    result.pop("endpoint_support", None); result.pop("validation_support", None)
    return result


def _composite_selection(value, low, high, components, source_set, rationale, *, state_id_digest=None):
    states = [item["evidence_state"] for item in components]
    if any(state == "MISSING" for state in states):
        return _missing_selection(rationale)
    if any(state == "ASSUMPTION" for state in states):
        state, quality, sources, method = "ASSUMPTION", "NONE", [], "ESTIMATE"
        bridge_supported = endpoints_supported = independent = longitudinal = False
    else:
        sources = sorted(set(ref for item in components for ref in item.get("source_ids", [])))
        qualities = [item["evidence_quality"] for item in components]
        quality = "LOW" if "LOW" in qualities else "MED" if "MED" in qualities else "HIGH"
        proxies = [item for item in components if item["evidence_state"] == "PROXY"]
        if proxies:
            state, method = "PROXY", "ESTIMATE"
            flags = [_support_flags(item, source_set) for item in proxies]
            bridge_supported = all(_complete_bridge(item.get("bridge")) for item in proxies)
            endpoints_supported = all(flag[0] for flag in flags)
            independent = all(flag[1] in ("independent_corroboration", "longitudinal_validation")
                              and flag[2] for flag in flags)
            longitudinal = all(flag[1] == "longitudinal_validation" for flag in flags)
        else:
            state, method = "DIRECT", "CALCULATED"
            bridge_supported, endpoints_supported = False, True
            independent = longitudinal = False
    result = {
        "value": value, "range": {"low": low, "high": high}, "authored_value": value,
        "authored_range": {"low": low, "high": high}, "method": method,
        "evidence_state": state, "evidence_quality": quality,
        "confidence": "LOW" if quality in ("LOW", "NONE") else quality,
        "source_ids": sources, "rationale": rationale, "caveats": [],
        "bridge_supported": bridge_supported, "endpoints_supported": endpoints_supported,
        "independent_validation": independent, "longitudinal_validation": longitudinal,
        "resolution_type": "SAFE_CALCULATION", "provenance": {
            "derivation_method": method, "evidence_state": state, "resolution_type": "SAFE_CALCULATION"}}
    if state_id_digest is not None: result["normalized_y5_state_digest"] = state_id_digest
    return result


def _finalize_reconciliation(authored, pass_items, source_set):
    evidence = authored["evidence"]
    supported = not pass_items or _construct_supported(evidence, source_set)
    _endpoints, validation_kind, _well_formed = _support_flags(evidence, source_set)
    return {"revenue_basis": authored["revenue_basis"],
            "included_cost_ids": copy.deepcopy(authored["included_cost_ids"]),
            "already_netted_cost_ids": copy.deepcopy(authored["already_netted_cost_ids"]),
            "supported": supported, "method": evidence["method"],
            "evidence_state": evidence["evidence_state"],
            "evidence_quality": evidence["evidence_quality"],
            "source_ids": copy.deepcopy(evidence["source_ids"]),
            "bridge_supported": evidence["evidence_state"] == "PROXY" and _complete_bridge(evidence.get("bridge")),
            "independent_validation": validation_kind == "independent_corroboration",
            "longitudinal_validation": validation_kind == "longitudinal_validation",
            "rationale": evidence["rationale"], "caveats": copy.deepcopy(evidence["caveats"])}


def _selection_triplet(item):
    return item["value"], item["range"]["low"], item["range"]["high"]


def _finalize_survival(basket, revenue, pass_items, reconciliation, source_set):
    provenance = {"status": basket["status"], "basket_id": basket["basket_id"],
                  "fixed_base_assertions": copy.deepcopy(basket["fixed_base_assertions"]),
                  "services": [], "calculation_status": "MISSING", "failure_reasons": []}
    if basket["status"] == "MISSING":
        return _missing_selection("Fixed-base survival basket is missing."), provenance
    pass_by_id = {item["cost_id"]: item["amount"] for item in pass_items}
    if revenue["evidence_state"] == "MISSING" or (pass_items and not reconciliation["supported"]):
        provenance["failure_reasons"].append("R_cva_unavailable")
        return _missing_selection("Survival basket cannot reconcile without R_cva."), provenance
    included = reconciliation["included_cost_ids"]
    if any(pass_by_id[cost_id]["evidence_state"] == "MISSING" for cost_id in included):
        provenance["failure_reasons"].append("included_pass_through_missing")
        return _missing_selection("Survival basket cannot reconcile without included pass-through."), provenance
    r_cva = revenue["value"] - sum(pass_by_id[cost_id]["value"] for cost_id in included)
    if not _is_number(r_cva) or r_cva <= 0:
        provenance["failure_reasons"].append("nonpositive_R_cva")
        return _missing_selection("Survival basket requires positive reconciled baseline R_cva."), provenance
    components, computed = [], []
    for service in basket["services"]:
        q, rev, passed, y5 = (service[name] for name in (
            "baseline_quantity", "baseline_revenue", "baseline_pass_through", "y5_operator_controlled_quantity"))
        components.extend((q, rev, passed, y5))
        if any(item["evidence_state"] == "MISSING" for item in (q, rev, passed, y5)):
            provenance["failure_reasons"].append("missing_positive_weight_endpoint")
            continue
        baseline = {"baseline_quantity": q, "baseline_revenue": rev, "baseline_pass_through": passed}
        nonpoint = [name for name, item in baseline.items()
                    if not (item["range"]["low"] == item["value"] == item["range"]["high"])]
        if nonpoint:
            provenance["failure_reasons"].extend(
                "baseline_not_point_identified:%s:%s" % (service["service_id"], name)
                for name in nonpoint)
            continue
        q0, revenue0, pass0 = q["value"], rev["value"], passed["value"]
        cva, unit_price = revenue0 - pass0, (revenue0 - pass0) / q0 if q0 > 0 else None
        weight = cva / r_cva
        ybase, ylow, yhigh = _selection_triplet(y5)
        valid = (q0 > 0 and 0 <= pass0 <= revenue0 and cva >= 0 and unit_price is not None
                 and 0 <= ylow <= ybase <= yhigh <= q0
                 and abs(service["baseline_cva"] - cva) <= SHARE_TOL
                 and abs(service["baseline_cva_unit_price"] - unit_price) <= SHARE_TOL
                 and abs(service["base_weight"] - weight) <= SHARE_TOL)
        if not valid: provenance["failure_reasons"].append("invalid_service_reconciliation:" + service["service_id"])
        qrel = {"low": ylow / q0 if q0 > 0 else None, "base": ybase / q0 if q0 > 0 else None,
                "high": yhigh / q0 if q0 > 0 else None}
        computed.append((weight, qrel, cva))
        provenance["services"].append({"service_id": service["service_id"], "unit": service["unit"],
            "constant_quality_spec": service["constant_quality_spec"], "baseline_quantity": q0,
            "baseline_revenue": revenue0, "baseline_pass_through": pass0, "baseline_cva": cva,
            "baseline_cva_unit_price": unit_price, "base_weight": weight,
            "y5_quantity": {"low": ylow, "base": ybase, "high": yhigh}, "qrel": qrel,
            "source_ids": sorted(set(ref for item in (q, rev, passed, y5) for ref in item["source_ids"]))})
    if (provenance["failure_reasons"] or len(computed) != len(basket["services"])
            or abs(sum(item[2] for item in computed) - r_cva) > SHARE_TOL
            or abs(sum(item[0] for item in computed) - 1) > ROLE_WEIGHT_TOL):
        if not provenance["failure_reasons"]: provenance["failure_reasons"].append("basket_not_exhaustive")
        return _missing_selection("Fixed-base survival basket failed deterministic reconciliation."), provenance
    values = {bound: sum(weight * qrel[bound] for weight, qrel, _cva in computed)
              for bound in ("low", "base", "high")}
    provenance["calculation_status"] = "RECOMPUTED"
    provenance["R_cva_base"] = r_cva
    selection = _composite_selection(values["base"], values["low"], values["high"], components,
                                     source_set, "Recomputed fixed-base Laspeyres CVA survival basket.")
    return selection, provenance


def _finalize_downside(downside, state, source_set):
    state_supported = (state["evidence_state"] == "ASSUMPTION" or
                       (state["evidence_state"] == "DIRECT" and state["endpoints_supported"]) or
                       (state["evidence_state"] == "PROXY" and state["endpoints_supported"] and
                        (state["independent_validation"] or state["longitudinal_validation"])))
    components = [downside["anchor"]] + [item["amount"] for item in downside["adjustments"]]
    provenance = {"normalized_y5_state_digest": downside["normalized_y5_state_digest"],
                  "anchor": {"value": downside["anchor"]["value"],
                             "range": copy.deepcopy(downside["anchor"]["range"]),
                             "source_ids": copy.deepcopy(downside["anchor"]["source_ids"]),
                             "anchor_basis": copy.deepcopy(downside["anchor"]["anchor_basis"])},
                  "adjustments": [{"channel": item["channel"], "value": item["amount"]["value"],
                                   "range": copy.deepcopy(item["amount"]["range"]),
                                   "source_ids": copy.deepcopy(item["amount"]["source_ids"])}
                                  for item in downside["adjustments"]],
                  "excluded_channel_map": copy.deepcopy(downside["excluded_channel_map"]),
                  "calculation_status": "MISSING"}
    if not state_supported or any(item["evidence_state"] == "MISSING" for item in components):
        result = _missing_selection("Downside multiple state or allowed-channel evidence is unsupported.")
        result["normalized_y5_state_digest"] = state.get("state_digest")
        return result, provenance
    base = downside["anchor"]["value"] + sum(item["amount"]["value"] for item in downside["adjustments"])
    low = downside["anchor"]["range"]["low"] + sum(item["amount"]["range"]["low"] for item in downside["adjustments"])
    high = downside["anchor"]["range"]["high"] + sum(item["amount"]["range"]["high"] for item in downside["adjustments"])
    if low < 0 or not low <= base <= high:
        result = _missing_selection("Downside multiple recomputation produced invalid support.")
        result["normalized_y5_state_digest"] = state.get("state_digest")
        return result, provenance
    provenance.update(calculation_status="RECOMPUTED", value=base, range={"low": low, "high": high})
    return _composite_selection(base, low, high, components, source_set,
                                "Recomputed entry-equivalent downside multiple from closed channels.",
                                state_id_digest=state["state_digest"]), provenance


def _selected_archetype(spec):
    target = spec["target_archetype"]
    selected = next(item for item in target["alternatives"] if item["id"] == target["selected_id"])
    return {"selected_id": selected["id"], "selected_name": selected["name"],
            "inclusion_criteria": copy.deepcopy(selected["inclusion_criteria"]),
            "exclusion_criteria": copy.deepcopy(selected["exclusion_criteria"]),
            "selection_basis": target["selection_basis"],
            "selection_uncertainty": target["selection_uncertainty"],
            "enumeration_coverage": copy.deepcopy(target["enumeration_coverage"])}


def _target_role_mix(packet, spec, source_set):
    basis = spec["value_basis"]
    if basis["mode"] == "missing":
        return {"spec_mode": "missing", "basis_method": "ESTIMATE", "basis_evidence_state": "MISSING",
                "basis_evidence_quality": "NONE", "basis_source_ids": [], "basis_bridge_supported": False,
                "basis_endpoints_supported": False, "basis_independent_validation": False,
                "basis_longitudinal_validation": False, "roles": []}
    if basis["mode"] == "assumption":
        authored = packet["inputs"]["target_role_judgments"]["roles"]
        roles = [{"role": frozen["title"], "cost_weight": frozen["role_cash_cost_weight"],
                  "removable_fraction": _finalize_selection(judgment["removable_fraction"], source_set)}
                 for frozen, judgment in zip(basis["roles"], authored)]
        return {"spec_mode": "assumption", "basis_method": "ESTIMATE",
                "basis_evidence_state": "ASSUMPTION", "basis_evidence_quality": "NONE",
                "basis_source_ids": [], "basis_bridge_supported": False,
                "basis_endpoints_supported": False, "basis_independent_validation": False,
                "basis_longitudinal_validation": False, "roles": roles}
    methods = [role["method"] for role in basis["roles"]]
    qualities = [role["evidence_quality"] for role in basis["roles"]]
    source_ids = sorted(set(ref for role in basis["roles"] for ref in role["source_ids"]))
    authored = packet["inputs"]["target_role_judgments"]["roles"]
    roles = []
    for frozen, judgment in zip(basis["roles"], authored):
        roles.append({"role": frozen["title"], "cost_weight": frozen["role_cash_cost_weight"],
                      "removable_fraction": _finalize_selection(judgment["removable_fraction"], source_set)})
    return {"spec_mode": "frozen", "basis_method": "CALCULATED" if "CALCULATED" in methods else "OBSERVED",
            "basis_evidence_state": "DIRECT", "basis_evidence_quality": "MED" if "MED" in qualities else "HIGH",
            "basis_source_ids": source_ids, "basis_bridge_supported": False,
            "basis_endpoints_supported": True, "basis_independent_validation": False,
            "basis_longitudinal_validation": False, "roles": roles}


def _sanitize(value):
    if isinstance(value, float) and math.isinf(value): return "UNBOUNDED" if value > 0 else "NEGATIVE_UNBOUNDED"
    if isinstance(value, float) and math.isnan(value): raise ContractError("scoring returned NaN")
    if isinstance(value, dict): return {key: _sanitize(item) for key, item in value.items()}
    if isinstance(value, list): return [_sanitize(item) for item in value]
    return value


def finalize(packet, dataset, spec, envelope, paths):
    errors = ["dataset: " + item for item in dataset_errors(dataset)]
    methodology_sha = sha256_file(paths["methodology"])
    errors.extend("spec: " + item for item in spec_errors(spec, dataset, methodology_sha))
    if not errors:
        errors.extend("packet: " + item for item in packet_errors(packet, dataset, spec))
        errors.extend("envelope: " + item for item in envelope_errors(envelope, packet, dataset, spec, paths))
    if errors: return None, errors
    source_set = {item["id"] for item in packet["sources"]}
    authored = packet["inputs"]
    basis = spec["value_basis"]
    passthrough = [{"category": item["category"], "cost_id": item["cost_id"],
                    "amount": _finalize_selection(item["amount"], source_set)}
                   for item in authored["third_party_pass_through"]]
    employee = _finalize_selection(authored["employee_cash_cost"]["amount"], source_set)
    contractor = _finalize_selection(authored["controllable_contractor_cash_cost"]["amount"], source_set)
    employee["accounting_basis"] = authored["employee_cash_cost"]["accounting_basis"]
    contractor["accounting_basis"] = authored["controllable_contractor_cash_cost"]["accounting_basis"]
    numerator_ids = [] if basis["mode"] == "missing" else [basis["employee_cash_cost_id"],
                                                            basis["controllable_contractor_cash_cost_id"]]
    reconciliation = _finalize_reconciliation(
        authored["recognized_revenue"]["pass_through_reconciliation"],
        authored["third_party_pass_through"], source_set)
    revenue_authored = copy.deepcopy(authored["recognized_revenue"])
    revenue_authored.pop("pass_through_reconciliation")
    finalized_revenue = _finalize_selection(revenue_authored, source_set)
    finalized_state = _finalize_state(authored["normalized_y5_operating_state"], source_set)
    finalized_downside, downside_provenance = _finalize_downside(
        authored["downside_exit_multiple"], finalized_state, source_set)
    finalized_survival, survival_provenance = _finalize_survival(
        authored["operator_controlled_value_added_demand_share_y5"], authored["recognized_revenue"],
        authored["third_party_pass_through"], reconciliation, source_set)
    final_inputs = {
        "target_archetype": _selected_archetype(spec),
        "recognized_revenue": finalized_revenue,
        "pass_through_reconciliation": reconciliation,
        "third_party_pass_through": passthrough,
        "employee_cash_cost": employee, "controllable_contractor_cash_cost": contractor,
        "numerator_cost_ids": numerator_ids,
        "target_role_mix": _target_role_mix(packet, spec, source_set),
        "implementation_realization": {"r%d" % year: _finalize_selection(
            authored["implementation_realization"]["r%d" % year], source_set) for year in range(1, 6)},
        "implementation_investment": {"k%d" % year: _finalize_selection(
            authored["implementation_investment"]["k%d" % year], source_set) for year in range(6)},
        "commercial_retention": {"c%d" % year: _finalize_selection(
            authored["commercial_retention"]["c%d" % year], source_set) for year in range(1, 6)},
        "target_archetype_coverage": _finalize_selection(authored["target_archetype_coverage"], source_set),
        "five_year_sale_availability": _finalize_selection(authored["five_year_sale_availability"], source_set),
        "buyer_access_win_share": _finalize_selection(authored["buyer_access_win_share"], source_set),
        "deal_execution_capacity_5y": _finalize_selection(authored["deal_execution_capacity_5y"], source_set),
        "integration_onboarding_capacity_5y": _finalize_selection(
            authored["integration_onboarding_capacity_5y"], source_set),
        "buy_mult": _finalize_selection(authored["buy_multiple"], source_set),
        "normalized_y5_operating_state": finalized_state,
        "downside_exit_mult": finalized_downside,
        "operator_controlled_value_added_demand_share_y5": finalized_survival,
    }
    construct_provenance = {
        "cva_reconciliation": {
            "controllable_value_added_boundary": basis["controllable_value_added_boundary"],
            "recognized_revenue_accounting_basis": authored["recognized_revenue"]["accounting_basis"],
            "pass_through": [{"category": item["category"], "cost_id": item["cost_id"],
                              "accounting_basis": item["accounting_basis"]}
                             for item in authored["third_party_pass_through"]],
            "numerator_costs": [{"cost_id": authored["employee_cash_cost"]["cost_id"],
                                 "accounting_basis": authored["employee_cash_cost"]["accounting_basis"]},
                                {"cost_id": authored["controllable_contractor_cash_cost"]["cost_id"],
                                 "accounting_basis": authored["controllable_contractor_cash_cost"]["accounting_basis"]}],
        },
        "pass_through_reconciliation": copy.deepcopy(reconciliation),
        "p_attribution": downside_provenance,
        "constant_price_survival": survival_provenance,
        "h": {"formula": "sum_y(r_y*c_y/(1+0.10)^y)-k0-sum_y(k_y/(1+0.10)^y)",
              "discount_rate": 0.10,
              "realization_paths": ["implementation_realization.r%d" % year for year in range(1, 6)],
              "investment_paths": ["implementation_investment.k%d" % year for year in range(6)],
              "retention_paths": ["commercial_retention.c%d" % year for year in range(1, 6)],
              "investment_unit": "fraction_of_one_full_year_of_G"},
    }
    record = {
        "naics": packet["naics"], "title": packet["title"],
        "run_meta": {"run_id": envelope["run_id"], "run_date": envelope["run_date"], "kind": envelope["kind"],
                     "attempt": envelope["attempt"], "remediates_run_id": envelope["remediates_run_id"],
                     "model_id": envelope["model_id"], "issued_by_task_path": envelope["issued_by_task_path"],
                     "codex_task_path": envelope["codex_task_path"], "fork_policy": envelope["fork_policy"],
                     "finalizer_version": FINALIZER_VERSION, "memo_renderer_version": MEMO_RENDERER_VERSION},
        "artifact_provenance": {"execution_envelope": copy.deepcopy(envelope),
                                "execution_envelope_sha256": sha256_file(paths["envelope"]),
                                "packet_sha256": sha256_file(paths["packet"])},
        "narrative": copy.deepcopy(packet["narrative"]),
        "scenario_narratives": copy.deepcopy(packet["scenario_narratives"]),
        "sources": copy.deepcopy(packet["sources"]),
        "dataset_inputs": {"snapshot_id": dataset["snapshot_id"], "dataset_sha256": envelope["dataset_sha256"],
                           "n_total": dataset["n_total"]["value"],
                           "n_band": _dataset_selection(dataset["n_band"], "target-band count")},
        "inputs": final_inputs, "construct_provenance": construct_provenance,
        "cross_checks": copy.deepcopy(packet["cross_checks"]),
        "confidence_overall": packet["confidence_overall"],
        "top_uncertain_inputs": copy.deepcopy(packet["top_uncertain_inputs"]),
        "reviewer_note": packet["reviewer_note"],
    }
    try:
        computed = _sanitize(scoring.calculate(record))
    except (KeyError, TypeError, ValueError, ZeroDivisionError, OverflowError, ContractError) as exc:
        return None, ["v4.2 scoring failed: %s" % exc]
    record["scenarios"] = {bound: computed[bound] for bound in ("low", "base", "high")}
    record["decision"] = computed["decision"]
    schema_errors = _schema_errors(record, load_json(os.path.join(SCHEMAS, "run_record_v4_2.schema.json")))
    if schema_errors: return None, schema_errors
    return record, []


def render_memo(record):
    lines = ["# %s — %s" % (record["naics"], record["title"]), "",
             "*v4.2 memo · `%s` · %s*" % (record["run_meta"]["run_id"], record["run_meta"]["run_date"]), ""]
    for key, title in (("executive_view", "Executive view"),
                       ("revenue_and_pass_through", "Revenue and pass-through"),
                       ("technical_value", "Technical value"), ("implementation", "Implementation"),
                       ("commercial_capture", "Commercial capture"), ("buyability", "Buyability"),
                       ("entry_and_exit", "Entry and exit"), ("operator_survival", "Operator survival"),
                       ("risks_and_uncertainty", "Risks and uncertainty")):
        lines.extend(["## " + title, "", record["narrative"][key], ""])
    lines.extend(["## Deterministic result", "", "| Factor | Low | Base | High |", "|---|---:|---:|---:|"])
    for factor in scoring.FACTOR_NAMES:
        values = [record["scenarios"][bound]["scores"][factor] for bound in ("low", "base", "high")]
        rendered = ["—" if value is None else "%.2f" % value for value in values]
        lines.append("| %s | %s | %s | %s |" % (factor, *rendered))
    h_values = [record["scenarios"][bound]["subfactors"]["h"]["h"] for bound in ("low", "base", "high")]
    lines.append("")
    lines.append("**h (low/base/high):** %s" % " / ".join("—" if value is None else "%.4f" % value for value in h_values))
    decision = record["decision"]
    lines.extend(["", "**Economic verdict:** `%s`" % decision["economic_verdict"],
                  "", "**Evidence readiness:** `%s`" % decision["evidence_readiness"]["status"],
                  "", "**Action:** `%s`" % decision["action"], "", "## Sources", ""])
    for source in record["sources"]:
        lines.append("- **%s. [%s](%s)** — %s (accessed %s)" %
                     (source["id"], source["title"], source["url"], source["what_it_supports"], source["access_date"]))
    lines.extend(["", "---", "", "Generated by `%s`; do not hand-edit." % MEMO_RENDERER_VERSION, ""])
    return "\n".join(lines)


def serialize_record(record):
    return (json.dumps(record, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("packet", "dataset", "spec", "prompt", "methodology", "execution-envelope", "output", "memo"):
        parser.add_argument("--" + name, required=True)
    args = parser.parse_args(argv)
    for path in (args.output, args.memo):
        if os.path.exists(path):
            print("FINALIZE FAILED: output already exists: %s" % path, file=sys.stderr); return 1
    try:
        packet, dataset, spec, envelope = map(load_json, (args.packet, args.dataset, args.spec,
                                                          args.execution_envelope))
        paths = {"packet": args.packet, "dataset": args.dataset, "spec": args.spec,
                 "prompt": args.prompt, "methodology": args.methodology, "envelope": args.execution_envelope}
        record, errors = finalize(packet, dataset, spec, envelope, paths)
    except (OSError, json.JSONDecodeError, ContractError, KeyError, TypeError, ValueError,
            OverflowError, RecursionError, MemoryError) as exc:
        record, errors = None, ["v4.2 input failed safely: %s" % exc]
    if errors:
        print("FINALIZE FAILED — v4.2:", file=sys.stderr)
        for error in errors: print("  " + error, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(args.memo)), exist_ok=True)
    with open(args.output, "xb") as handle: handle.write(serialize_record(record))
    with open(args.memo, "x", encoding="utf-8") as handle: handle.write(render_memo(record))
    print("OK: finalized and rendered v4.2 %s (%s)" % (record["naics"], record["run_meta"]["run_id"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
