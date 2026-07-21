#!/usr/bin/env python3
"""Finalize one v4.1 packet against frozen dataset/spec/envelope artifacts."""

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
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMAS = os.path.join(HERE, "schemas")
FINALIZER_VERSION = "finalizer-4.1"
MEMO_RENDERER_VERSION = "memo-renderer-4.1"
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
BRIDGE_FIELDS = ("population", "geography", "period", "unit", "business_model")


def _load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


legacy_build = _load_module("legacy_schema_v4_1", "build.py")
scoring = _load_module("scoring_v4_1_finalizer", "v4_1_scoring.py")


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
    expression = calculation.get("expression")
    operands = calculation.get("operands")
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
    try:
        depth = _ast_depth(tree)
    except RecursionError as exc:
        raise ContractError("calculation AST is too deep") from exc
    if depth > MAX_AST_DEPTH:
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
            if isinstance(node.op, ast.Add):
                result = left + right
            elif isinstance(node.op, ast.Sub):
                result = left - right
            elif isinstance(node.op, ast.Mult):
                result = left * right
            else:
                if right == 0:
                    raise ContractError("division by zero")
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


def _evidence_errors(path, selection, source_set):
    errors = []
    method = selection.get("method")
    state = selection.get("evidence_state")
    quality = selection.get("evidence_quality")
    refs = selection.get("source_ids", [])
    has_bridge = "bridge" in selection
    bridge = selection.get("bridge")
    if len(refs) != len(set(refs)):
        errors.append("%s source_ids must be unique" % path)
    unknown = sorted(set(refs) - source_set)
    if unknown:
        errors.append("%s references unknown source IDs %s" % (path, unknown))
    if state in ("ASSUMPTION", "MISSING"):
        if method != "ESTIMATE" or quality != "NONE" or refs:
            errors.append("%s %s requires ESTIMATE, NONE quality, and no sources" % (path, state))
    else:
        if not refs or quality == "NONE":
            errors.append("%s %s requires sources and non-NONE quality" % (path, state))
    if state == "DIRECT" and method not in ("OBSERVED", "CALCULATED"):
        errors.append("%s DIRECT requires OBSERVED or CALCULATED" % path)
    if state == "PROXY":
        if not _complete_bridge(bridge):
            errors.append("%s PROXY requires a complete population/geography/period/unit/business_model bridge" % path)
    elif has_bridge:
        errors.append("%s bridge is forbidden unless evidence_state is PROXY" % path)
    has_calc = "calculation" in selection
    if method == "CALCULATED" and not has_calc:
        errors.append("%s CALCULATED requires calculation" % path)
    if method != "CALCULATED" and has_calc:
        errors.append("%s calculation is forbidden unless method is CALCULATED" % path)
    return errors


def _numeric_errors(path, selection, source_set, low_bound, high_bound=None, *, strict=False, integer=False):
    errors = _evidence_errors(path, selection, source_set)
    value = selection.get("value")
    numeric_range = selection.get("range", {})
    low, high = numeric_range.get("low"), numeric_range.get("high")
    if selection.get("evidence_state") == "MISSING":
        if value is not None or low is not None or high is not None:
            errors.append("%s MISSING requires null value/range" % path)
        return errors
    if not all(_is_number(item) for item in (value, low, high)):
        errors.append("%s requires finite numeric value/low/high" % path)
        return errors
    if not low <= value <= high:
        errors.append("%s range must satisfy low <= value <= high" % path)
    if strict:
        if low <= low_bound:
            errors.append("%s range.low must be greater than %s" % (path, low_bound))
    elif low < low_bound:
        errors.append("%s range.low below %s" % (path, low_bound))
    if high_bound is not None and high > high_bound:
        errors.append("%s range.high above %s" % (path, high_bound))
    if integer and not all(float(item).is_integer() for item in (value, low, high)):
        errors.append("%s value/range must be integers" % path)
    if selection.get("method") == "CALCULATED" and "calculation" in selection:
        calculation = selection["calculation"]
        operand_refs = [item.get("source_id") for item in calculation.get("operands", [])]
        if sorted(set(operand_refs) - set(selection.get("source_ids", []))):
            errors.append("%s calculation operand sources must be selected" % path)
        try:
            computed = safe_calculation(calculation)
            authored = _decimal(value)
            tolerance = max(VALUE_TOL, abs(computed) * VALUE_TOL)
            if abs(authored - computed) > tolerance:
                errors.append("%s authored value does not equal safe calculation" % path)
            if not (_decimal(low) <= computed <= _decimal(high)):
                errors.append("%s calculated value must lie inside range" % path)
        except ContractError as exc:
            errors.append("%s unsafe calculation: %s" % (path, exc))
    return errors


def dataset_errors(dataset):
    schema = load_json(os.path.join(SCHEMAS, "dataset_v4_1.schema.json"))
    errors = _schema_errors(dataset, schema)
    if errors:
        return errors
    occupations = dataset["role_mix"]["occupations"]
    socs = [item["soc"] for item in occupations]
    if len(socs) != len(set(socs)):
        errors.append("dataset role_mix SOCs must be unique")
    for field in ("employment_share", "wage_share"):
        total = sum(float(item[field]) for item in occupations)
        if total > 1.0 + SHARE_TOL:
            errors.append("dataset role_mix %s sum exceeds 1" % field)
    n_band = dataset["n_band"]["value"]
    if n_band is not None and n_band > dataset["n_total"]["value"]:
        errors.append("dataset n_band may not exceed n_total")
    labor = dataset["labor_share"]
    if labor["value"] is None and labor["quality"] != "NONE":
        errors.append("missing dataset labor_share requires NONE quality")
    if n_band is None and dataset["n_band"]["quality"] != "NONE":
        errors.append("missing dataset n_band requires NONE quality")
    return errors


def spec_errors(spec, dataset):
    schema = load_json(os.path.join(SCHEMAS, "industry_spec_v4_1.schema.json"))
    errors = _schema_errors(spec, schema)
    if spec.get("naics") != dataset.get("naics") or spec.get("title") != dataset.get("title"):
        errors.append("industry spec identity must equal dataset identity")
    basis = spec.get("value_basis", {})
    mode = basis.get("mode")
    labor = basis.get("labor_contractor_cash_cost_share")
    roles, sources = basis.get("roles", []), basis.get("sources", [])
    bridge = basis.get("bridge")
    if mode == "target_specific":
        if not isinstance(labor, dict) or not roles or not sources:
            errors.append("target_specific value basis requires labor_share, roles, and sources")
        else:
            low, value, high = labor["range"]["low"], labor["value"], labor["range"]["high"]
            if not 0 <= low <= value <= high <= 1:
                errors.append("spec labor/contractor cash-cost range must satisfy 0 <= low <= value <= high <= 1")
            role_ids = [item["role_id"] for item in roles]
            if len(role_ids) != len(set(role_ids)):
                errors.append("spec target role IDs must be unique")
            weight = sum(float(item["role_cash_cost_weight"]) for item in roles)
            if abs(weight - 1.0) > ROLE_WEIGHT_TOL:
                errors.append("spec target role weights must sum to 1")
            source_ids = [item["id"] for item in sources]
            if len(source_ids) != len(set(source_ids)):
                errors.append("spec value-basis source IDs must be unique")
            source_set = set(source_ids)
            for path, refs in [("labor_share", labor["source_ids"])] + [
                    ("role %s" % item["role_id"], item["source_ids"]) for item in roles]:
                if len(refs) != len(set(refs)) or set(refs) - source_set:
                    errors.append("spec %s has duplicate or unknown source IDs" % path)
    elif mode == "assumption":
        if not isinstance(labor, dict) or not roles or sources:
            errors.append("assumption value basis requires bounded labor/roles and no sources")
        else:
            low, value, high = labor["range"]["low"], labor["base"], labor["range"]["high"]
            if not 0 <= low <= value <= high <= 1:
                errors.append("assumption cash-cost range must satisfy 0 <= low <= base <= high <= 1")
            if (labor.get("evidence_state") != "ASSUMPTION" or labor.get("evidence_quality") != "NONE"
                    or labor.get("source_ids")):
                errors.append("assumption cash-cost share requires ASSUMPTION/NONE/no sources")
            role_ids = [item["role_id"] for item in roles]
            if len(role_ids) != len(set(role_ids)):
                errors.append("assumption target role IDs must be unique")
            if abs(sum(float(item["role_cash_cost_weight"]) for item in roles) - 1.0) > ROLE_WEIGHT_TOL:
                errors.append("assumption target role weights must sum to 1")
            if any(item.get("source_ids") for item in roles):
                errors.append("assumption target roles may not claim sources")
    elif mode in ("dataset", "missing"):
        if labor is not None or roles or sources:
            errors.append("%s value basis requires null labor_share and empty roles/sources" % mode)
    else:
        errors.append("spec value_basis.mode is invalid")
    if mode == "dataset":
        if bridge is not None and not _complete_bridge(bridge):
            errors.append("dataset value basis bridge must be null or complete and closed")
    elif bridge is not None:
        errors.append("value basis bridge is forbidden outside dataset mode")
    archetype = spec.get("target_archetype", {})
    alternatives = archetype.get("alternatives", [])
    option_ids = [item.get("id") for item in alternatives]
    if len(option_ids) != len(set(option_ids)):
        errors.append("spec archetype alternative IDs must be unique")
    if archetype.get("selected_id") not in option_ids:
        errors.append("spec selected archetype must identify exactly one alternative")
    archetype_sources = [item.get("id") for item in archetype.get("sources", [])]
    if len(archetype_sources) != len(set(archetype_sources)):
        errors.append("spec archetype source IDs must be unique")
    archetype_source_set = set(archetype_sources)
    for option in alternatives:
        count = option.get("band_count", {})
        if not count.get("low", 0) <= count.get("base", -1) <= count.get("high", -1):
            errors.append("spec archetype %s count must satisfy low <= base <= high" % option.get("id"))
        refs = option.get("source_ids", [])
        if len(refs) != len(set(refs)) or set(refs) - archetype_source_set:
            errors.append("spec archetype %s has duplicate or unknown source IDs" % option.get("id"))
    if alternatives:
        ordered = sorted(alternatives, key=lambda item: (-float(item["band_count"]["base"]), item["id"]))
        if archetype.get("selected_id") != ordered[0]["id"]:
            errors.append("spec selected archetype must be largest-base with lexicographically smallest ID tie-break")
        expected_uncertainty = False
        if len(ordered) > 1:
            first, second = ordered[0]["band_count"], ordered[1]["band_count"]
            close_bases = (first["base"] == 0
                           or (first["base"] - second["base"]) / first["base"] < 0.10)
            ranges_overlap = second["high"] >= first["low"]
            expected_uncertainty = close_bases or ranges_overlap
        if archetype.get("selection_uncertainty") != expected_uncertainty:
            errors.append("spec selection_uncertainty must exactly reflect top-two proximity or range overlap")
    residual = archetype.get("residual", {}).get("band_count", {})
    if residual and not residual.get("low", 0) <= residual.get("base", -1) <= residual.get("high", -1):
        errors.append("spec residual count must satisfy low <= base <= high")
    coverage = archetype.get("enumeration_coverage", {})
    if coverage and not coverage.get("low", 0) <= coverage.get("base", -1) <= coverage.get("high", -1):
        errors.append("spec enumeration coverage must satisfy low <= base <= high")
    n_band = dataset.get("n_band", {}).get("value")
    if n_band is not None and alternatives and residual:
        enumerated_base = sum(float(item["band_count"]["base"]) for item in alternatives)
        reconciled_total = enumerated_base + float(residual["base"])
        if abs(reconciled_total - float(n_band)) > SHARE_TOL:
            errors.append("spec alternative base counts plus residual must equal dataset n_band")
        expected_coverage = 0.0 if n_band == 0 else enumerated_base / float(n_band)
        if not coverage or abs(float(coverage.get("base", -1)) - expected_coverage) > COVERAGE_TOL:
            errors.append("spec enumeration_coverage.base must reconcile to alternative base counts / n_band")
    return errors


def envelope_errors(envelope, packet, dataset, spec, paths):
    required = {
        "envelope_version", "kind", "naics", "title", "run_id", "run_date", "attempt",
        "remediates_run_id", "issued_by_task_path", "codex_task_path", "fork_policy",
        "role", "model_id", *HASH_KEYS,
    }
    errors = []
    if not isinstance(envelope, dict):
        return ["execution envelope must be an object"]
    missing, extra = sorted(required - set(envelope)), sorted(set(envelope) - required)
    if missing:
        errors.append("execution envelope missing keys %s" % missing)
    if extra:
        errors.append("execution envelope has unknown keys %s" % extra)
    if errors:
        return errors
    if envelope["envelope_version"] != "4.1":
        errors.append("execution envelope version must be 4.1")
    route = {"fleet": "gpt-5.6-terra", "golden": "gpt-5.6-sol"}
    if envelope["kind"] not in route:
        errors.append("execution envelope kind must be fleet or golden")
    elif envelope["model_id"] != route[envelope["kind"]]:
        errors.append("execution envelope model route is wrong")
    if envelope["issued_by_task_path"] != "/root":
        errors.append("execution envelope must be issued by /root")
    task_path = envelope["codex_task_path"]
    if not isinstance(task_path, str) or not task_path.startswith("/root/") or task_path == "/root/":
        errors.append("execution envelope codex_task_path must identify an isolated child task")
    if envelope["fork_policy"] != "none":
        errors.append("execution envelope fork_policy must be none")
    if envelope["role"] != "research":
        errors.append("execution envelope role must be research")
    if envelope["naics"] != packet.get("naics") or envelope["naics"] != dataset.get("naics") or envelope["naics"] != spec.get("naics"):
        errors.append("execution envelope NAICS identity mismatch")
    if envelope["title"] != packet.get("title") or envelope["title"] != dataset.get("title") or envelope["title"] != spec.get("title"):
        errors.append("execution envelope title identity mismatch")
    try:
        run_date = date.fromisoformat(envelope["run_date"])
        if run_date > date.today():
            errors.append("execution run_date cannot be in the future")
    except (TypeError, ValueError):
        errors.append("execution run_date must be a real ISO date")
        run_date = None
    if not isinstance(envelope["run_id"], str) or not envelope["run_id"]:
        errors.append("execution run_id must be non-empty")
    attempt, parent = envelope["attempt"], envelope["remediates_run_id"]
    if attempt == 1 and parent is not None:
        errors.append("attempt 1 requires null remediates_run_id")
    elif attempt == 2 and (not isinstance(parent, str) or not parent):
        errors.append("attempt 2 requires a non-empty remediates_run_id")
    elif attempt not in (1, 2):
        errors.append("attempt must be 1 or 2")
    for key in HASH_KEYS:
        value = envelope[key]
        if not isinstance(value, str) or len(value) != 64 or any(char not in "0123456789abcdef" for char in value):
            errors.append("%s must be lowercase SHA-256" % key)
    actual = {
        "prompt_sha256": sha256_file(paths["prompt"]),
        "dataset_sha256": sha256_file(paths["dataset"]),
        "spec_sha256": sha256_file(paths["spec"]),
        "methodology_sha256": sha256_file(paths["methodology"]),
        "thresholds_sha256": sha256_file(os.path.join(HERE, "thresholds_v4_1.json")),
        "research_packet_schema_sha256": sha256_file(os.path.join(SCHEMAS, "research_packet_v4_1.schema.json")),
        "dataset_schema_sha256": sha256_file(os.path.join(SCHEMAS, "dataset_v4_1.schema.json")),
        "industry_spec_schema_sha256": sha256_file(os.path.join(SCHEMAS, "industry_spec_v4_1.schema.json")),
        "run_record_schema_sha256": sha256_file(os.path.join(SCHEMAS, "run_record_v4_1.schema.json")),
        "scoring_sha256": sha256_file(os.path.join(HERE, "v4_1_scoring.py")),
        "finalizer_sha256": sha256_file(__file__),
    }
    for key, value in actual.items():
        if envelope[key] != value:
            errors.append("execution envelope %s does not match exact artifact" % key)
    if spec.get("dataset_snapshot", {}).get("sha256") != actual["dataset_sha256"]:
        errors.append("industry spec dataset snapshot digest mismatch")
    if run_date is not None:
        for source in packet.get("sources", []):
            try:
                accessed = date.fromisoformat(source.get("access_date", ""))
                if accessed > run_date:
                    errors.append("source %s access_date exceeds run_date" % source.get("id"))
            except (TypeError, ValueError):
                errors.append("source %s access_date must be a real ISO date" % source.get("id"))
    return errors


def packet_errors(packet, dataset, spec):
    schema = load_json(os.path.join(SCHEMAS, "research_packet_v4_1.schema.json"))
    errors = _schema_errors(packet, schema)
    if errors:
        return errors
    source_ids = [item["id"] for item in packet["sources"]]
    source_urls = [item["url"] for item in packet["sources"]]
    if len(source_ids) != len(set(source_ids)):
        errors.append("packet source IDs must be unique")
    if len(source_urls) != len(set(source_urls)):
        errors.append("packet source URLs must be unique")
    source_set = set(source_ids)
    specs = {
        "target_archetype_coverage": (0, 1, False),
        "commercial_capture_share": (0, 1, False),
        "five_year_sale_availability": (0, 1, False),
        "buy_multiple": (0, None, True),
        "downside_exit_multiple": (0, None, False),
        "operator_controlled_demand_share_y5": (0, 1, False),
    }
    for name, (low, high, strict) in specs.items():
        errors.extend(_numeric_errors("inputs.%s" % name, packet["inputs"][name], source_set, low, high, strict=strict))
    fallback = packet["dataset_fallbacks"].get("n_band")
    dataset_n_band = dataset["n_band"]["value"]
    if dataset_n_band is None:
        if fallback is not None:
            errors.extend(_numeric_errors("dataset_fallbacks.n_band", fallback, source_set, 0,
                                          dataset["n_total"]["value"], integer=True))
            errors.append("dataset_fallbacks.n_band is forbidden without a frozen deterministic spec fallback")
    elif fallback is not None:
        errors.append("dataset_fallbacks.n_band forbidden when dataset n_band is non-null")

    authored_coverage = packet["inputs"]["target_archetype_coverage"]
    if dataset_n_band is not None and authored_coverage.get("evidence_state") != "MISSING":
        selected_id = spec["target_archetype"]["selected_id"]
        selected = next(item for item in spec["target_archetype"]["alternatives"]
                        if item["id"] == selected_id)
        counts = selected["band_count"]
        if dataset_n_band == 0:
            implied = {"low": 0.0, "base": 0.0, "high": 0.0}
        else:
            implied = {name: min(1.0, float(counts[name]) / float(dataset_n_band))
                       for name in ("low", "base", "high")}
        value, numeric_range = authored_coverage["value"], authored_coverage["range"]
        if abs(float(value) - implied["base"]) > COVERAGE_TOL:
            errors.append("target_archetype_coverage.value must equal selected base band_count / n_band")
        if (float(numeric_range["low"]) > implied["low"] + COVERAGE_TOL
                or float(numeric_range["high"]) < implied["high"] - COVERAGE_TOL):
            errors.append("target_archetype_coverage range must contain the selected count-implied range")

    roles = packet["inputs"]["target_role_judgments"]
    errors.extend(_evidence_errors("inputs.target_role_judgments", roles, source_set))
    mode = spec["value_basis"]["mode"]
    expected = _spec_roles(spec, dataset)
    authored = [item["role_id"] for item in roles["roles"]]
    if len(authored) != len(set(authored)):
        errors.append("target role judgments must have unique role IDs")
    if mode == "missing":
        if roles["evidence_state"] != "MISSING" or authored:
            errors.append("missing value basis requires MISSING role judgment set with no roles")
    else:
        expected_ids = [item["role_id"] for item in expected]
        if authored != expected_ids:
            errors.append("target role judgment IDs/order must exactly equal frozen spec roles")
        for item in roles["roles"]:
            low, value, high = item["range"]["low"], item["removable_fraction"], item["range"]["high"]
            if not all(_is_number(value_) for value_ in (low, value, high)) or not 0 <= low <= value <= high <= 1:
                errors.append("role %s range must satisfy 0 <= low <= value <= high <= 1" % item["role_id"])
        if roles["evidence_state"] == "MISSING":
            errors.append("non-missing value basis may not use MISSING role judgments")

    ramp = packet["inputs"]["implementation_realization"]
    errors.extend(_evidence_errors("inputs.implementation_realization", ramp, source_set))
    values = (ramp["value"], ramp["low"], ramp["high"])
    if ramp["evidence_state"] == "MISSING":
        if any(item is not None for item in values):
            errors.append("MISSING implementation ramp requires null value/low/high")
    elif any(not isinstance(item, list) or len(item) != 5 for item in values):
        errors.append("implementation ramp requires three five-element arrays")
    else:
        for label, sequence in zip(("value", "low", "high"), values):
            if not all(_is_number(item) and 0 <= item <= 1 for item in sequence):
                errors.append("implementation ramp %s must contain fractions in [0,1]" % label)
            if any(left > right for left, right in zip(sequence, sequence[1:])):
                errors.append("implementation ramp %s must be nondecreasing" % label)
        if any(not values[1][index] <= values[0][index] <= values[2][index] for index in range(5)):
            errors.append("implementation ramp requires low <= value <= high for every year")
    return errors


def _missing_selection(rationale, quality="NONE"):
    return {
        "value": None, "range": {"low": None, "high": None},
        "authored_value": None, "authored_range": {"low": None, "high": None},
        "method": "ESTIMATE", "evidence_state": "MISSING", "evidence_quality": quality,
        "confidence": "LOW", "source_ids": [], "rationale": rationale, "caveats": [],
        "bridge_supported": False,
        "resolution_type": "UNRESOLVED_MISSING",
        "provenance": {"derivation_method": "ESTIMATE", "evidence_state": "MISSING",
                       "resolution_type": "UNRESOLVED_MISSING"},
    }


def _finalize_selection(selection):
    result = copy.deepcopy(selection)
    result["authored_value"] = copy.deepcopy(selection["value"])
    result["authored_range"] = copy.deepcopy(selection["range"])
    result["bridge_supported"] = (selection["evidence_state"] == "PROXY"
                                  and _complete_bridge(selection.get("bridge")))
    if selection["evidence_state"] == "MISSING":
        resolution = "UNRESOLVED_MISSING"
    elif selection["method"] == "CALCULATED":
        result["value"] = float(safe_calculation(selection["calculation"]))
        resolution = "SAFE_CALCULATION"
    else:
        resolution = "AUTHORED"
    result["resolution_type"] = resolution
    result["provenance"] = {
        "derivation_method": selection["method"],
        "evidence_state": selection["evidence_state"],
        "resolution_type": resolution,
    }
    return result


def _dataset_selection(item, kind):
    value = item["value"]
    if value is None:
        return _missing_selection("Normalized dataset has no defensible %s value." % kind)
    return {
        "value": value, "range": {"low": value, "high": value},
        "authored_value": value, "authored_range": {"low": value, "high": value},
        "method": "OBSERVED", "evidence_state": "DIRECT", "evidence_quality": item["quality"],
        "confidence": item["quality"] if item["quality"] in ("HIGH", "MED", "LOW") else "LOW",
        "source_ids": [], "rationale": item["basis"], "caveats": [],
        "bridge_supported": False,
        "resolution_type": "DATASET",
        "provenance": {"derivation_method": "OBSERVED", "evidence_state": "DIRECT",
                       "resolution_type": "DATASET"},
    }


def _dataset_proxy_selection(item, kind, bridge):
    value = item["value"]
    if value is None:
        return _missing_selection("Normalized dataset has no defensible %s value." % kind)
    selection = {
        "value": value, "range": {"low": value, "high": value},
        "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": item["quality"],
        "confidence": item["quality"] if item["quality"] in ("HIGH", "MED", "LOW") else "LOW",
        "source_ids": [], "rationale": item["basis"], "caveats": [],
    }
    if _complete_bridge(bridge):
        selection["bridge"] = copy.deepcopy(bridge)
    return _finalize_selection(selection)


def _spec_roles(spec, dataset):
    mode = spec["value_basis"]["mode"]
    if mode in ("target_specific", "assumption"):
        return [{"role_id": item["role_id"], "title": item["title"],
                 "cost_weight": item["role_cash_cost_weight"]} for item in spec["value_basis"]["roles"]]
    if mode == "missing":
        return []
    roles = [{"role_id": item["soc"], "title": item["title"], "cost_weight": item["wage_share"]}
             for item in dataset["role_mix"]["occupations"]]
    residual = 1.0 - sum(float(item["cost_weight"]) for item in roles)
    if residual > SHARE_TOL:
        roles.append({"role_id": "RESIDUAL", "title": "Unlisted occupations", "cost_weight": residual})
    elif abs(residual) <= SHARE_TOL and roles:
        largest = max(range(len(roles)), key=lambda index: roles[index]["cost_weight"])
        roles[largest]["cost_weight"] += residual
    return roles


def _target_labor_selection(spec, dataset):
    basis = spec["value_basis"]
    if basis["mode"] == "dataset":
        return _dataset_proxy_selection(dataset["labor_share"], "target labor share", basis.get("bridge"))
    if basis["mode"] == "missing":
        return _missing_selection("Frozen industry spec has no defensible target labor-cost share.")
    labor = basis["labor_contractor_cash_cost_share"]
    if basis["mode"] == "assumption":
        item = {
            "value": labor["base"], "range": copy.deepcopy(labor["range"]),
            "method": "ESTIMATE", "evidence_state": "ASSUMPTION",
            "evidence_quality": "NONE", "confidence": "LOW", "source_ids": [],
            "rationale": labor["rationale"], "caveats": copy.deepcopy(labor["caveats"]),
        }
        return _finalize_selection(item)
    item = {
        "value": labor["value"], "range": copy.deepcopy(labor["range"]),
        "method": "OBSERVED", "evidence_state": "DIRECT",
        "evidence_quality": labor["evidence_quality"], "confidence": labor["evidence_quality"],
        "source_ids": copy.deepcopy(labor["source_ids"]), "rationale": labor["rationale"],
        "caveats": copy.deepcopy(labor["caveats"]),
    }
    return _finalize_selection(item)


def _selected_archetype(spec):
    target = spec["target_archetype"]
    selected = next(item for item in target["alternatives"] if item["id"] == target["selected_id"])
    return {
        "selected_id": selected["id"], "selected_name": selected["name"],
        "inclusion_criteria": copy.deepcopy(selected["inclusion_criteria"]),
        "exclusion_criteria": copy.deepcopy(selected["exclusion_criteria"]),
        "selection_basis": target["selection_basis"],
        "selection_uncertainty": target["selection_uncertainty"],
        "enumeration_coverage": copy.deepcopy(target["enumeration_coverage"]),
    }


def _role_mix(packet, spec, dataset):
    frozen = _spec_roles(spec, dataset)
    mode = spec["value_basis"]["mode"]
    if mode == "missing":
        return {"spec_mode": "missing", "basis_evidence_state": "MISSING",
                "basis_evidence_quality": "NONE", "basis_bridge_supported": False, "roles": []}
    if mode == "dataset":
        basis_state, basis_quality = "PROXY", dataset["role_mix"]["quality"]
        basis_bridge = spec["value_basis"].get("bridge")
    elif mode == "assumption":
        basis_state, basis_quality, basis_bridge = "ASSUMPTION", "NONE", None
    else:
        basis_state = "DIRECT"
        basis_quality = spec["value_basis"]["labor_contractor_cash_cost_share"]["evidence_quality"]
        basis_bridge = None
    evidence = packet["inputs"]["target_role_judgments"]
    by_id = {item["role_id"]: item for item in evidence["roles"]}
    roles = []
    for role in frozen:
        judgment = by_id[role["role_id"]]
        selection = {
            "value": judgment["removable_fraction"], "range": copy.deepcopy(judgment["range"]),
            "method": evidence["method"], "evidence_state": evidence["evidence_state"],
            "evidence_quality": evidence["evidence_quality"], "confidence": evidence["confidence"],
            "source_ids": copy.deepcopy(evidence["source_ids"]), "rationale": judgment["rationale"],
            "caveats": copy.deepcopy(evidence["caveats"]),
        }
        if "bridge" in evidence:
            selection["bridge"] = copy.deepcopy(evidence["bridge"])
        roles.append({"role_id": role["role_id"], "role": role["title"],
                      "cost_weight": role["cost_weight"],
                      "removable_fraction": _finalize_selection(selection)})
    result = {"spec_mode": "frozen", "basis_evidence_state": basis_state,
              "basis_evidence_quality": basis_quality,
              "basis_bridge_supported": mode == "dataset" and _complete_bridge(basis_bridge),
              "roles": roles}
    if mode == "dataset" and _complete_bridge(basis_bridge):
        result["basis_bridge"] = copy.deepcopy(basis_bridge)
    return result


def _implementation_ramp(packet):
    authored = packet["inputs"]["implementation_realization"]
    result = {}
    for index in range(5):
        selection = {
            "value": None if authored["value"] is None else authored["value"][index],
            "range": {
                "low": None if authored["low"] is None else authored["low"][index],
                "high": None if authored["high"] is None else authored["high"][index],
            },
            "method": authored["method"], "evidence_state": authored["evidence_state"],
            "evidence_quality": authored["evidence_quality"], "confidence": authored["confidence"],
            "source_ids": copy.deepcopy(authored["source_ids"]), "rationale": authored["rationale"],
            "caveats": copy.deepcopy(authored["caveats"]),
        }
        if "bridge" in authored:
            selection["bridge"] = copy.deepcopy(authored["bridge"])
        result["r%d" % (index + 1)] = _finalize_selection(selection)
    return result


def _sanitize_computed(value):
    if isinstance(value, float) and math.isinf(value):
        return "UNBOUNDED"
    if isinstance(value, float) and math.isnan(value):
        raise ContractError("scoring returned NaN")
    if isinstance(value, dict):
        return {key: _sanitize_computed(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize_computed(item) for item in value]
    return value


def finalize(packet, dataset, spec, envelope, paths):
    errors = []
    errors.extend("dataset: " + item for item in dataset_errors(dataset))
    errors.extend("spec: " + item for item in spec_errors(spec, dataset))
    if not errors:
        errors.extend("packet: " + item for item in packet_errors(packet, dataset, spec))
        errors.extend("envelope: " + item for item in envelope_errors(envelope, packet, dataset, spec, paths))
    if errors:
        return None, errors

    fallback = packet["dataset_fallbacks"].get("n_band")
    n_band = (_dataset_selection(dataset["n_band"], "target-band count")
              if dataset["n_band"]["value"] is not None else
              _finalize_selection(fallback) if fallback is not None else
              _missing_selection("Normalized dataset and packet have no defensible target-band count."))
    inputs = {
        "target_archetype": _selected_archetype(spec),
        "target_labor_cost_share": _target_labor_selection(spec, dataset),
        "target_role_mix": _role_mix(packet, spec, dataset),
        "implementation_ramp": _implementation_ramp(packet),
        "commercial_retention": _finalize_selection(packet["inputs"]["commercial_capture_share"]),
        "target_archetype_coverage": _finalize_selection(packet["inputs"]["target_archetype_coverage"]),
        "five_year_sale_availability": _finalize_selection(packet["inputs"]["five_year_sale_availability"]),
        "buy_mult": _finalize_selection(packet["inputs"]["buy_multiple"]),
        "downside_exit_mult": _finalize_selection(packet["inputs"]["downside_exit_multiple"]),
        "y5_survival": _finalize_selection(packet["inputs"]["operator_controlled_demand_share_y5"]),
    }
    record = {
        "naics": packet["naics"], "title": packet["title"],
        "run_meta": {
            "run_id": envelope["run_id"], "run_date": envelope["run_date"], "kind": envelope["kind"],
            "attempt": envelope["attempt"], "remediates_run_id": envelope["remediates_run_id"],
            "model_id": envelope["model_id"], "issued_by_task_path": envelope["issued_by_task_path"],
            "codex_task_path": envelope["codex_task_path"], "fork_policy": envelope["fork_policy"],
            "finalizer_version": FINALIZER_VERSION, "memo_renderer_version": MEMO_RENDERER_VERSION,
        },
        "artifact_provenance": {
            "execution_envelope": copy.deepcopy(envelope),
            "execution_envelope_sha256": sha256_file(paths["envelope"]),
            "packet_sha256": sha256_file(paths["packet"]),
        },
        "narrative": copy.deepcopy(packet["narrative"]), "sources": copy.deepcopy(packet["sources"]),
        "dataset_inputs": {
            "snapshot_id": dataset["snapshot_id"], "dataset_sha256": envelope["dataset_sha256"],
            "n_total": dataset["n_total"]["value"], "n_band": n_band,
            "source_labor_share": dataset["labor_share"]["value"],
            "source_role_mix_basis": dataset["role_mix"]["basis"],
        },
        "inputs": inputs, "cross_checks": copy.deepcopy(packet["cross_checks"]),
        "confidence_overall": packet["confidence_overall"],
        "top_uncertain_inputs": copy.deepcopy(packet["top_uncertain_inputs"]),
        "reviewer_note": packet["reviewer_note"],
    }
    try:
        computed = _sanitize_computed(scoring.calculate(record))
    except (KeyError, TypeError, ValueError, ZeroDivisionError, OverflowError, ContractError) as exc:
        return None, ["v4.1 scoring failed: %s" % exc]
    record["scenarios"] = {bound: computed[bound] for bound in ("low", "base", "high")}
    record["decision"] = computed["decision"]
    schema = load_json(os.path.join(SCHEMAS, "run_record_v4_1.schema.json"))
    schema_errors = _schema_errors(record, schema)
    if schema_errors:
        return None, schema_errors
    return record, []


def render_memo(record):
    titles = (
        ("executive_view", "Executive view"), ("technical_value", "Technical value"),
        ("implementation", "Implementation"), ("commercial_capture", "Commercial capture"),
        ("buyability", "Buyability"), ("entry_and_exit", "Entry and exit"),
        ("operator_survival", "Operator survival"), ("risks_and_uncertainty", "Risks and uncertainty"),
    )
    lines = ["# %s — %s" % (record["naics"], record["title"]), "",
             "*v4.1 memo · `%s` · %s*" % (record["run_meta"]["run_id"], record["run_meta"]["run_date"]), ""]
    for key, title in titles:
        lines.extend(["## " + title, "", record["narrative"][key], ""])
    lines.extend(["## Deterministic result", "", "| Factor | Low | Base | High |", "|---|---:|---:|---:|"])
    for factor in scoring.FACTOR_NAMES:
        values = [record["scenarios"][bound]["scores"][factor] for bound in ("low", "base", "high")]
        rendered = ["—" if value is None else "%.2f" % value for value in values]
        lines.append("| %s | %s | %s | %s |" % (factor, *rendered))
    scores = [record["scenarios"][bound]["S"] for bound in ("low", "base", "high")]
    rendered = ["—" if value is None else "%.2f" % value for value in scores]
    lines.append("| **S** | **%s** | **%s** | **%s** |" % tuple(rendered))
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
    parser.add_argument("--packet", required=True)
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--spec", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--methodology", required=True)
    parser.add_argument("--execution-envelope", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--memo", required=True)
    args = parser.parse_args(argv)
    for path in (args.output, args.memo):
        if os.path.exists(path):
            print("FINALIZE FAILED: output already exists: %s" % path, file=sys.stderr)
            return 1
    try:
        packet, dataset, spec, envelope = map(load_json, (args.packet, args.dataset, args.spec, args.execution_envelope))
        paths = {"packet": args.packet, "dataset": args.dataset, "spec": args.spec,
                 "prompt": args.prompt, "methodology": args.methodology,
                 "envelope": args.execution_envelope}
        record, errors = finalize(packet, dataset, spec, envelope, paths)
    except (OSError, json.JSONDecodeError, ContractError, KeyError, TypeError, ValueError,
            OverflowError, RecursionError, MemoryError) as exc:
        record, errors = None, ["v4.1 input failed safely: %s" % exc]
    if errors:
        print("FINALIZE FAILED — v4.1:", file=sys.stderr)
        for error in errors:
            print("  " + error, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(args.memo)), exist_ok=True)
    record_bytes, memo_text = serialize_record(record), render_memo(record)
    with open(args.output, "xb") as handle:
        handle.write(record_bytes)
    with open(args.memo, "x", encoding="utf-8") as handle:
        handle.write(memo_text)
    print("OK: finalized and rendered v4.1 %s (%s)" % (record["naics"], record["run_meta"]["run_id"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
