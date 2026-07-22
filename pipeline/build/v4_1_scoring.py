#!/usr/bin/env python3
"""Frozen v4.1 deterministic V/I/C/B/P scoring and decision logic.

Expected finalized-record interface
-----------------------------------
Every numeric selection has ``value``, ``range.low``, ``range.high``, and
``evidence_state``. A MISSING selection has null value/low/high. Other
evidence metadata may be retained by the finalizer and does not affect scores
or gates.

record = {
  "dataset_inputs": {
    "n_band": <selection: non-negative target count>
  },
  "inputs": {
    "target_archetype": {"selection_uncertainty": <boolean>, ...},
    "target_labor_cost_share": <selection in [0,1]>,
    "target_role_mix": {
      "spec_mode": "frozen" | "missing",
      "basis_evidence_state": "DIRECT" | "PROXY" | "ASSUMPTION" | "MISSING", # optional legacy default DIRECT
      "basis_evidence_quality": "HIGH" | "MED" | "LOW" | "NONE",             # optional legacy default MED
      "basis_bridge_supported": <boolean>,                                      # optional legacy default true
      "roles": [{
        "role": <unique string>,
        "cost_weight": <number in [0,1]>,
        "removable_fraction": <selection in [0,1]>
      }]
    },
    "implementation_ramp": {"r1": <selection>, ..., "r5": <selection>},
    "commercial_retention": <selection in [0,1]>,
    "target_archetype_coverage": <selection in [0,1]>,
    "five_year_sale_availability": <selection in [0,1]>,
    "buy_mult": <strictly-positive selection>,
    "downside_exit_mult": <non-negative selection>,
    "y5_survival": <selection in [0,1]>
  }
}

``calculate`` returns low/base/high bundles plus a decision. Factor and S base
values are null when a required primitive is MISSING. Bounds remain numeric,
using the full semantic domain only for the missing primitive and retaining
tighter bounds supplied by known primitives.
"""

import json
import math
import os
from datetime import date


HERE = os.path.dirname(os.path.abspath(__file__))
FACTOR_NAMES = ("V", "I", "C", "B", "P")
BOUNDS = ("low", "base", "high")
VERDICT_ORDER = {"kill": 0, "pass": 1, "conditional": 2, "strong": 3, "hell_yes": 4}
VERDICT_DESCENDING = ("hell_yes", "strong", "conditional", "pass")
EVIDENCE_STATES = {"DIRECT", "PROXY", "ASSUMPTION", "MISSING"}
QUALITIES = {"HIGH", "MED", "LOW", "NONE"}
EPS = 1e-12


def load_thresholds(path=None):
    path = path or os.path.join(HERE, "thresholds_v4_1.json")
    with open(path, "r", encoding="utf-8") as handle:
        thresholds = json.load(handle)
    validate_thresholds(thresholds)
    return thresholds


def _finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_thresholds(thresholds):
    """Validate the complete scoring configuration, returning it unchanged."""
    _require(isinstance(thresholds, dict), "thresholds must be an object")
    expected_top = {
        "version", "frozen", "freeze_date", "score", "archetype_selection", "domains",
        "value_available", "implementation", "buyability", "price_discipline", "verdict_cuts",
        "verdict_min_each_factor", "verdict_order", "survival_gate", "actions",
        "partial_identification", "evidence_contract", "readiness", "sentinels", "display",
    }
    _require(set(thresholds) == expected_top, "threshold top-level keys are incomplete or unexpected")
    _require(thresholds.get("version") == "4.1", "threshold version must be 4.1")
    _require(thresholds.get("frozen") is True, "v4.1 thresholds must be frozen")
    try:
        date.fromisoformat(thresholds.get("freeze_date", ""))
    except (TypeError, ValueError):
        raise ValueError("freeze_date must be an ISO date")
    _require(thresholds["freeze_date"] == "2026-07-21", "freeze_date differs from the frozen contract")
    score = thresholds.get("score", {})
    _require(set(score) == {"type", "factors", "scale"}, "score threshold keys are invalid")
    _require(score.get("type") == "geometric_mean", "score type must be geometric_mean")
    _require(score.get("factors") == list(FACTOR_NAMES), "factor order must be V/I/C/B/P")
    _require(score.get("scale") == [0.0, 10.0], "score scale must be [0,10]")

    archetype = thresholds.get("archetype_selection", {})
    _require(archetype == {
        "enumeration_min_coverage": 0.80,
        "selection_rule": "largest_base_band_count",
        "near_tie_fraction": 0.10,
        "overlap_rule": "mark_selection_uncertainty_and_widen_ranges",
        "tie_break_rule": "lexicographically_smallest_stable_id",
        "record_policy": "one_primary_record_per_naics",
        "uncertainty_readiness": "UNPROVEN",
    }, "archetype-selection mapping differs from the frozen contract")

    domains = thresholds.get("domains", {})
    _require(domains == {
        "factor": [0.0, 10.0],
        "enumeration_coverage": [0.0, 1.0],
        "labor_cost_share": [0.0, 1.0],
        "role_cost_weight": [0.0, 1.0],
        "removable_fraction": [0.0, 1.0],
        "implementation_realization": [0.0, 1.0],
        "commercial_retention": [0.0, 1.0],
        "n_band": [0.0, None],
        "archetype_coverage": [0.0, 1.0],
        "sale_availability": [0.0, 1.0],
        "buy_multiple": [0.0, None],
        "downside_exit_multiple": [0.0, None],
        "y5_survival": [0.0, 1.0],
    }, "formula domains differ from the frozen contract")

    positive = (
        ("value_available.gross_savings_anchor", thresholds.get("value_available", {}).get("gross_savings_anchor")),
        ("buyability.n5_full_score", thresholds.get("buyability", {}).get("n5_full_score")),
        ("price_discipline.entry_reference_multiple", thresholds.get("price_discipline", {}).get("entry_reference_multiple")),
        ("price_discipline.entry_score_span", thresholds.get("price_discipline", {}).get("entry_score_span")),
        ("price_discipline.downside_ratio_slope", thresholds.get("price_discipline", {}).get("downside_ratio_slope")),
    )
    for name, value in positive:
        _require(_finite(value) and value > 0, "%s must be finite and positive" % name)
    _require(thresholds["value_available"] == {"gross_savings_anchor": 0.25},
             "value_available thresholds differ from the frozen contract")
    _require(set(thresholds["implementation"]) == {"years", "discount_rate"},
             "implementation threshold keys are invalid")
    implementation = thresholds.get("implementation", {})
    _require(implementation.get("years") == 5, "implementation.years must be 5")
    rate = implementation.get("discount_rate")
    _require(rate == 0.10, "implementation.discount_rate must be frozen at 10%")
    _require(thresholds["buyability"] == {"n5_full_score": 500.0},
             "buyability thresholds differ from the frozen contract")
    _require(thresholds["price_discipline"] == {
        "entry_reference_multiple": 14.0, "entry_score_span": 10.0,
        "downside_ratio_floor": 0.5, "downside_ratio_slope": 20.0},
        "price_discipline thresholds differ from the frozen contract")
    downside_floor = thresholds.get("price_discipline", {}).get("downside_ratio_floor")
    _require(_finite(downside_floor) and 0 <= downside_floor <= 1,
             "price_discipline.downside_ratio_floor must be in [0,1]")

    cuts = thresholds.get("verdict_cuts", {})
    floors = thresholds.get("verdict_min_each_factor", {})
    _require(set(cuts) == set(VERDICT_DESCENDING), "verdict_cuts keys are incomplete")
    _require(set(floors) == set(VERDICT_DESCENDING), "verdict factor-floor keys are incomplete")
    cut_values = [cuts[name] for name in VERDICT_DESCENDING]
    floor_values = [floors[name] for name in VERDICT_DESCENDING]
    _require(all(_finite(value) and 0 <= value <= 10 for value in cut_values + floor_values),
             "verdict cuts and floors must be finite in [0,10]")
    _require(all(left > right for left, right in zip(cut_values, cut_values[1:])),
             "verdict cuts must strictly descend")
    _require(all(left > right for left, right in zip(floor_values, floor_values[1:])),
             "verdict factor floors must strictly descend")
    _require(all(floors[name] <= cuts[name] for name in VERDICT_DESCENDING),
             "each verdict factor floor must not exceed its S cut")
    _require(cuts == {"hell_yes": 7.5, "strong": 6.0, "conditional": 4.5, "pass": 3.0},
             "verdict cuts differ from the frozen contract")
    _require(floors == {"hell_yes": 6.0, "strong": 4.0, "conditional": 2.0, "pass": 1.0},
             "verdict factor floors differ from the frozen contract")
    _require(thresholds["verdict_order"] == ["kill", "pass", "conditional", "strong", "hell_yes"],
             "verdict order differs from the frozen contract")

    gate = thresholds.get("survival_gate", {})
    _require(set(gate) == {"no_cap_at_or_above", "conditional_cap_at_or_above",
                           "pass_cap_at_or_above", "caps"},
             "survival_gate keys are incomplete")
    survival = [gate["pass_cap_at_or_above"], gate["conditional_cap_at_or_above"], gate["no_cap_at_or_above"]]
    _require(all(_finite(value) for value in survival) and 0 < survival[0] < survival[1] < survival[2] <= 1,
             "survival thresholds must strictly increase inside (0,1]")
    _require(gate == {"no_cap_at_or_above": 0.75, "conditional_cap_at_or_above": 0.50,
                      "pass_cap_at_or_above": 0.25,
                      "caps": {"no_cap": "hell_yes", "conditional": "conditional",
                               "pass": "pass", "kill": "kill"}},
             "survival thresholds differ from the frozen contract")
    _require(thresholds["actions"] == {
        "ordinary": {"hell_yes": "DEEP_DIVE", "strong": "DEEP_DIVE", "conditional": "SELECTIVE",
                     "pass": "DEPRIORITIZE", "kill": "AVOID"},
        "uncertainty": "EVIDENCE_FIRST"}, "action mapping differs from the frozen contract")

    partial = thresholds.get("partial_identification", {})
    _require(partial == {
        "missing_base": None,
        "unbounded_token": "UNBOUNDED",
        "identified_endpoint_rule": "gated_low_equals_gated_high",
        "identified_mapping": "shared_gated_verdict",
        "different_endpoint_verdict": "indeterminate",
        "base_verdict_requires_all_critical_bases": True,
    }, "partial-identification mapping differs from the frozen contract")

    evidence = thresholds.get("evidence_contract", {})
    _require(evidence == {
        "methods": ["OBSERVED", "CALCULATED", "ESTIMATE"],
        "states": ["DIRECT", "PROXY", "ASSUMPTION", "MISSING"],
        "qualities": ["HIGH", "MED", "LOW", "NONE"],
        "direct_methods": ["OBSERVED", "CALCULATED"],
        "unsupported_states": ["MISSING"],
        "unsupported_qualities": ["LOW", "NONE"],
        "provisional_states": ["ASSUMPTION"],
        "proxy_bridge_required": True,
    }, "evidence-quality mapping differs from the frozen contract")

    readiness = thresholds.get("readiness", {})
    _require(readiness == {
        "statuses": ["SUBSTANTIATED", "PROVISIONAL", "UNPROVEN"],
        "core_paths": ["n_band", "target_archetype_coverage", "target_labor_cost_share",
                       "target_role_mix_basis", "buy_mult"],
        "forward_bridge_paths": ["implementation_ramp.r1", "implementation_ramp.r2",
                                 "implementation_ramp.r3", "implementation_ramp.r4",
                                 "implementation_ramp.r5", "commercial_retention",
                                 "five_year_sale_availability", "downside_exit_mult", "y5_survival"],
        "unbridged_core_proxy_status": "UNPROVEN",
        "unbridged_forward_direct_status": "UNPROVEN",
        "unbridged_forward_proxy_status": "PROVISIONAL",
        "unsupported_input_status": "UNPROVEN",
        "role_basis_assumption_status": "UNPROVEN",
        "unsubstantiated_core_status": "PROVISIONAL",
        "assumption_status": "PROVISIONAL",
        "cross_tier_status": "PROVISIONAL",
        "action_instability_status": "PROVISIONAL",
    }, "readiness/status mapping differs from the frozen contract")
    _require(all(value in readiness["statuses"] for key, value in readiness.items()
                 if key.endswith("_status")), "readiness mapping names an unknown status")

    sentinels = thresholds.get("sentinels", {})
    _require(set(sentinels) == {"numeric_tolerance", "implementation_schedules"},
             "sentinel threshold keys are invalid")
    tolerance = sentinels.get("numeric_tolerance")
    _require(_finite(tolerance) and 0 < tolerance <= 1e-9,
             "sentinel numeric tolerance must be positive and no larger than 1e-9")
    schedules = sentinels.get("implementation_schedules")
    expected_schedules = [
        ([1.0, 1.0, 1.0, 1.0, 1.0], 10.0),
        ([0.0, 1.0, 1.0, 1.0, 1.0], 7.601841083684134),
        ([0.0, 0.0, 1.0, 1.0, 1.0], 5.4216966143060725),
        ([0.0, 0.0, 0.0, 1.0, 1.0], 3.4397470966896524),
        ([0.2, 0.4, 0.6, 0.8, 1.0], 5.620251920525462),
        ([0.0, 0.0, 0.0, 0.0, 0.0], 0.0),
    ]
    _require(isinstance(schedules, list) and len(schedules) == len(expected_schedules),
             "implementation sentinel schedule set is incomplete")
    rate = thresholds["implementation"]["discount_rate"]
    weights = [1.0 / ((1.0 + rate) ** year) for year in range(1, 6)]
    for item, (expected_ramp, expected_value) in zip(schedules, expected_schedules):
        _require(isinstance(item, dict) and set(item) == {"ramp", "expected"},
                 "implementation sentinel keys are invalid")
        _require(item["ramp"] == expected_ramp and item["expected"] == expected_value,
                 "implementation sentinel differs from the frozen contract")
        actual = 10.0 * sum(value * weight for value, weight in zip(item["ramp"], weights)) / sum(weights)
        _require(abs(actual - item["expected"]) <= tolerance,
                 "implementation sentinel fails exact formula validation")

    _require(thresholds.get("display") == {
        "decimal_places": 2, "rounding_stage": "after_numeric_validation",
    }, "display mapping differs from the frozen contract")
    return thresholds


def clamp(value, low=0.0, high=10.0):
    return max(low, min(high, value))


def geometric_mean(values):
    if any(value <= 0 for value in values):
        return 0.0
    return math.prod(values) ** (1.0 / len(values))


def _domain(thresholds, name):
    return tuple(thresholds["domains"][name])


def _selection(selection, path, domain_low, domain_high, *, thresholds=None,
               strict_low=False, integer=False):
    """Validate a selection and return (base, low, high, is_missing)."""
    _require(isinstance(selection, dict), "%s must be an object" % path)
    evidence = thresholds["evidence_contract"] if thresholds is not None else {
        "methods": ["OBSERVED", "CALCULATED", "ESTIMATE"],
        "states": list(EVIDENCE_STATES), "qualities": list(QUALITIES),
    }
    method = selection.get("method")
    _require(method in evidence["methods"], "%s has invalid method" % path)
    state = selection.get("evidence_state")
    _require(state in evidence["states"], "%s has invalid evidence_state" % path)
    quality = selection.get("evidence_quality")
    _require(quality in evidence["qualities"], "%s has invalid evidence_quality" % path)
    numeric_range = selection.get("range")
    _require(isinstance(numeric_range, dict), "%s.range must be an object" % path)
    value, low, high = selection.get("value"), numeric_range.get("low"), numeric_range.get("high")
    if state == "MISSING":
        _require(value is None and low is None and high is None,
                 "%s MISSING requires null value/low/high" % path)
        return None, domain_low, domain_high, True
    _require(all(_finite(item) for item in (value, low, high)),
             "%s requires finite numeric value/low/high" % path)
    value, low, high = float(value), float(low), float(high)
    _require(low <= value <= high, "%s requires low <= value <= high" % path)
    if strict_low:
        _require(low > domain_low, "%s range must be strictly above %s" % (path, domain_low))
    else:
        _require(low >= domain_low, "%s range is below %s" % (path, domain_low))
    if domain_high is not None:
        _require(high <= domain_high, "%s range exceeds %s" % (path, domain_high))
    if integer:
        _require(all(item.is_integer() for item in (value, low, high)),
                 "%s value/range must be integral" % path)
    return value, low, high, False


def _v_bundle(record, bound, missing_paths):
    inputs = record["inputs"]
    role_mix = inputs["target_role_mix"]
    _require(isinstance(role_mix, dict), "inputs.target_role_mix must be an object")
    mode = role_mix.get("spec_mode")
    _require(mode in ("frozen", "missing"), "target_role_mix.spec_mode must be frozen or missing")
    if mode == "missing":
        _require(not role_mix.get("roles"), "missing target role spec must not contain roles")
        missing_paths.add("target_role_mix")
        factor_low, factor_high = _domain(record["_thresholds"], "factor")
        score = {"low": factor_low, "base": record["_thresholds"]["partial_identification"]["missing_base"],
                 "high": factor_high}[bound]
        return score, {"spec_mode": mode, "gross_removable_cost_share": None}

    labor = _selection(inputs["target_labor_cost_share"], "inputs.target_labor_cost_share",
                       *_domain(record["_thresholds"], "labor_cost_share"),
                       thresholds=record["_thresholds"])
    if labor[3]:
        missing_paths.add("target_labor_cost_share")
    roles = role_mix.get("roles")
    _require(isinstance(roles, list) and roles, "frozen target role spec requires roles")
    names, weights, resolved = [], [], []
    for index, role in enumerate(roles):
        path = "inputs.target_role_mix.roles[%d]" % index
        _require(isinstance(role, dict), "%s must be an object" % path)
        name, weight = role.get("role"), role.get("cost_weight")
        _require(isinstance(name, str) and name, "%s.role must be non-empty" % path)
        weight_low, weight_high = _domain(record["_thresholds"], "role_cost_weight")
        _require(_finite(weight) and weight_low <= float(weight) <= weight_high,
                 "%s.cost_weight must be in [0,1]" % path)
        names.append(name)
        weights.append(float(weight))
        fraction = _selection(role.get("removable_fraction"), path + ".removable_fraction",
                              *_domain(record["_thresholds"], "removable_fraction"),
                              thresholds=record["_thresholds"])
        if fraction[3]:
            missing_paths.add("target_role_mix.%s.removable_fraction" % name)
        resolved.append(fraction)
    _require(len(names) == len(set(names)), "target role names must be unique")
    _require(abs(sum(weights) - 1.0) <= EPS, "target role cost weights must sum to 1")
    index = {"base": 0, "low": 1, "high": 2}[bound]
    labor_value = labor[index]
    fractions = [item[index] for item in resolved]
    base_missing = labor[3] or any(item[3] for item in resolved)
    if bound == "base" and base_missing:
        return None, {"spec_mode": mode, "labor_cost_share": None if labor[3] else labor_value,
                      "weighted_removable_fraction": None, "gross_removable_cost_share": None}
    gross = labor_value * sum(weight * fraction for weight, fraction in zip(weights, fractions))
    anchor = record["_thresholds"]["value_available"]["gross_savings_anchor"]
    score = record["_thresholds"]["score"]["scale"][1] * min(1.0, gross / anchor)
    return score, {
        "spec_mode": mode,
        "labor_cost_share": labor_value if not (bound == "base" and labor[3]) else None,
        "weighted_removable_fraction": None if (bound == "base" and any(item[3] for item in resolved)) else sum(
            weight * fraction for weight, fraction in zip(weights, fractions)),
        "gross_removable_cost_share": gross,
    }


def _ramp_intervals(record, missing_paths):
    ramp = record["inputs"].get("implementation_ramp")
    _require(isinstance(ramp, dict) and set(ramp) == {"r1", "r2", "r3", "r4", "r5"},
             "implementation_ramp must contain exactly r1..r5")
    resolved = []
    for year in range(1, 6):
        path = "inputs.implementation_ramp.r%d" % year
        item = _selection(ramp["r%d" % year], path,
                          *_domain(record["_thresholds"], "implementation_realization"),
                          thresholds=record["_thresholds"])
        if item[3]:
            missing_paths.add("implementation_ramp.r%d" % year)
        resolved.append(item)

    # Componentwise minimum and maximum feasible nondecreasing ramps. Authored
    # endpoints remain exact; only missing years are filled from [0,1].
    lows, highs = [item[1] for item in resolved], [item[2] for item in resolved]
    missing = [item[3] for item in resolved]
    ramp_domain_low, ramp_domain_high = _domain(record["_thresholds"], "implementation_realization")
    low_ramp = []
    for low, high, is_missing in zip(lows, highs, missing):
        previous = low_ramp[-1] if low_ramp else ramp_domain_low
        candidate = previous if is_missing else low
        _require(candidate + EPS >= previous, "implementation low endpoints must be nondecreasing")
        _require(candidate <= high + EPS, "implementation ramp intervals admit no nondecreasing path")
        low_ramp.append(candidate)
    high_ramp = [0.0] * 5
    next_value = ramp_domain_high
    for index in range(4, -1, -1):
        candidate = next_value if missing[index] else highs[index]
        _require(candidate <= next_value + EPS, "implementation high endpoints must be nondecreasing")
        _require(candidate + EPS >= lows[index], "implementation ramp intervals admit no nondecreasing path")
        high_ramp[index] = candidate
        next_value = candidate
    bases = [item[0] for item in resolved]
    if not any(missing):
        _require(all(left <= right + EPS for left, right in zip(bases, bases[1:])),
                 "implementation ramp base values must be nondecreasing")
    else:
        previous = ramp_domain_low
        for value, is_missing in zip(bases, missing):
            if not is_missing:
                _require(value + EPS >= previous, "known implementation base values admit no nondecreasing path")
                previous = value
        bases = None
    return {"low": low_ramp, "base": bases, "high": high_ramp}


def _implementation_score(ramp, thresholds):
    rate = thresholds["implementation"]["discount_rate"]
    weights = [1.0 / ((1.0 + rate) ** year) for year in range(1, 6)]
    return thresholds["score"]["scale"][1] * sum(
        value * weight for value, weight in zip(ramp, weights)) / sum(weights)


def _simple_factor(selection, path, bound, missing_paths, thresholds, domain_name):
    resolved = _selection(selection, path, *_domain(thresholds, domain_name), thresholds=thresholds)
    if resolved[3]:
        missing_paths.add(path.removeprefix("inputs."))
    value = resolved[{"base": 0, "low": 1, "high": 2}[bound]]
    missing_base = thresholds["partial_identification"]["missing_base"]
    return (missing_base if bound == "base" and resolved[3]
            else thresholds["score"]["scale"][1] * value), value, resolved[3]


def _n5_and_b(record, bound, missing_paths):
    n_band = _selection(record["dataset_inputs"]["n_band"], "dataset_inputs.n_band",
                        *_domain(record["_thresholds"], "n_band"),
                        thresholds=record["_thresholds"], integer=True)
    coverage = _selection(record["inputs"]["target_archetype_coverage"],
                          "inputs.target_archetype_coverage",
                          *_domain(record["_thresholds"], "archetype_coverage"),
                          thresholds=record["_thresholds"])
    sale = _selection(record["inputs"]["five_year_sale_availability"],
                      "inputs.five_year_sale_availability",
                      *_domain(record["_thresholds"], "sale_availability"),
                      thresholds=record["_thresholds"])
    for name, item in (("n_band", n_band), ("target_archetype_coverage", coverage),
                       ("five_year_sale_availability", sale)):
        if item[3]:
            missing_paths.add(name)
    base_missing = any(item[3] for item in (n_band, coverage, sale))
    index = {"base": 0, "low": 1, "high": 2}[bound]
    values = [item[index] for item in (n_band, coverage, sale)]
    if bound == "base" and base_missing:
        return None, {"n_band": None if n_band[3] else values[0],
                      "coverage": None if coverage[3] else values[1],
                      "five_year_sale_availability": None if sale[3] else values[2], "N5": None}
    if bound == "high" and n_band[3]:
        # An unbounded count yields B=10 unless a known high fraction proves N5=0.
        if coverage[2] == 0 or sale[2] == 0:
            n5, score = 0.0, 0.0
        else:
            n5 = record["_thresholds"]["partial_identification"]["unbounded_token"]
            score = record["_thresholds"]["domains"]["factor"][1]
    else:
        n5 = values[0] * values[1] * values[2]
        full = record["_thresholds"]["buyability"]["n5_full_score"]
        factor_low, factor_high = _domain(record["_thresholds"], "factor")
        score = clamp(factor_high * math.log10(1.0 + n5) / math.log10(1.0 + full),
                      factor_low, factor_high)
    return score, {"n_band": None if n_band[3] else values[0],
                   "coverage": None if bound == "base" and coverage[3] else values[1],
                   "five_year_sale_availability": None if bound == "base" and sale[3] else values[2],
                   "N5": n5}


def _price_scores(buy, exit_, thresholds):
    config = thresholds["price_discipline"]
    factor_low, factor_high = _domain(thresholds, "factor")
    entry = clamp(config["entry_reference_multiple"] - buy, factor_low,
                  min(factor_high, config["entry_score_span"]))
    resilience = clamp(config["downside_ratio_slope"] *
                       (exit_ / buy - config["downside_ratio_floor"]), factor_low, factor_high)
    return min(entry, resilience), entry, resilience


def _p_bundle(record, bound, missing_paths):
    buy = _selection(record["inputs"]["buy_mult"], "inputs.buy_mult",
                     *_domain(record["_thresholds"], "buy_multiple"),
                     thresholds=record["_thresholds"], strict_low=True)
    exit_ = _selection(record["inputs"]["downside_exit_mult"], "inputs.downside_exit_mult",
                       *_domain(record["_thresholds"], "downside_exit_multiple"),
                       thresholds=record["_thresholds"])
    if buy[3]:
        missing_paths.add("buy_mult")
    if exit_[3]:
        missing_paths.add("downside_exit_mult")
    base_missing = buy[3] or exit_[3]
    if bound == "base" and base_missing:
        return record["_thresholds"]["partial_identification"]["missing_base"], {
                      "buy_mult": None if buy[3] else buy[0],
                      "downside_exit_mult": None if exit_[3] else exit_[0],
                      "entry_score": None, "downside_resilience_score": None}
    if bound == "low":
        if buy[3] or exit_[3]:
            return record["_thresholds"]["domains"]["factor"][0], {
                         "buy_mult": None if buy[3] else buy[2],
                         "downside_exit_mult": None if exit_[3] else exit_[1],
                         "entry_score": None, "downside_resilience_score": None}
        buy_value, exit_value = buy[2], exit_[1]
    else:  # high
        if buy[3]:
            factor_low, factor_high = _domain(record["_thresholds"], "factor")
            score = factor_low if (not exit_[3] and exit_[2] == 0) else factor_high
            return score, {"buy_mult": None, "downside_exit_mult": None if exit_[3] else exit_[2],
                           "entry_score": None, "downside_resilience_score": None}
        buy_value = buy[1]
        if exit_[3]:
            config = record["_thresholds"]["price_discipline"]
            factor_low, factor_high = _domain(record["_thresholds"], "factor")
            entry = clamp(config["entry_reference_multiple"] - buy_value,
                          factor_low, min(factor_high, config["entry_score_span"]))
            return entry, {"buy_mult": buy_value, "downside_exit_mult": None,
                           "entry_score": entry, "downside_resilience_score": factor_high}
        exit_value = exit_[2]
    score, entry, resilience = _price_scores(buy_value, exit_value, record["_thresholds"])
    return score, {"buy_mult": buy_value, "downside_exit_mult": exit_value,
                   "entry_score": entry, "downside_resilience_score": resilience}


def _raw_verdict(S, scores, thresholds):
    if S is None or any(scores[name] is None for name in FACTOR_NAMES):
        return "indeterminate"
    for verdict in VERDICT_DESCENDING:
        if (S >= thresholds["verdict_cuts"][verdict]
                and min(scores.values()) >= thresholds["verdict_min_each_factor"][verdict]):
            return verdict
    return "kill"


def _cap(verdict, cap, thresholds):
    if verdict == "indeterminate":
        return verdict
    order = {name: index for index, name in enumerate(thresholds["verdict_order"])}
    return verdict if order[verdict] <= order[cap] else cap


def _gate_verdict(raw, survival, thresholds):
    reasons = []
    verdict = raw
    gate = thresholds["survival_gate"]
    if survival < gate["pass_cap_at_or_above"]:
        verdict = gate["caps"]["kill"]
        reasons.append("y5_survival_below_0.25")
    elif survival < gate["conditional_cap_at_or_above"]:
        verdict = _cap(verdict, gate["caps"]["pass"], thresholds)
        reasons.append("y5_survival_cap:pass")
    elif survival < gate["no_cap_at_or_above"]:
        verdict = _cap(verdict, gate["caps"]["conditional"], thresholds)
        reasons.append("y5_survival_cap:conditional")
    else:
        verdict = _cap(verdict, gate["caps"]["no_cap"], thresholds)
    return verdict, reasons


def _readiness(record, missing_paths, cross_tier, action_instability):
    thresholds = record["_thresholds"]
    config = thresholds["readiness"]
    evidence = thresholds["evidence_contract"]
    selection_uncertainty = record["inputs"].get("target_archetype", {}).get("selection_uncertainty", False)
    _require(isinstance(selection_uncertainty, bool),
             "inputs.target_archetype.selection_uncertainty must be boolean")
    role_selections = [("target_role_mix.%s.removable_fraction" % role.get("role", role.get("role_id", index)),
                        role.get("removable_fraction"))
                       for index, role in enumerate(record["inputs"].get("target_role_mix", {}).get("roles", []))]
    ramp_selections = [("implementation_ramp.r%d" % year,
                        record["inputs"].get("implementation_ramp", {}).get("r%d" % year))
                       for year in range(1, 6)]
    labeled = [
        ("target_labor_cost_share", record["inputs"].get("target_labor_cost_share")),
        *role_selections, *ramp_selections,
        ("commercial_retention", record["inputs"].get("commercial_retention")),
        ("n_band", record["dataset_inputs"].get("n_band")),
        ("target_archetype_coverage", record["inputs"].get("target_archetype_coverage")),
        ("five_year_sale_availability", record["inputs"].get("five_year_sale_availability")),
        ("buy_mult", record["inputs"].get("buy_mult")),
        ("downside_exit_mult", record["inputs"].get("downside_exit_mult")),
        ("y5_survival", record["inputs"].get("y5_survival")),
    ]
    labeled = [(path, item) for path, item in labeled if isinstance(item, dict)]
    assumptions = sorted(path for path, item in labeled
                         if item.get("evidence_state") in evidence["provisional_states"])
    unsupported_states = sorted(path for path, item in labeled
                                if item.get("evidence_state") in evidence["unsupported_states"])
    low_quality = sorted(path for path, item in labeled
                         if item.get("evidence_quality") in evidence["unsupported_qualities"])

    role_mix = record["inputs"].get("target_role_mix", {})
    basis_state = role_mix.get("basis_evidence_state", "DIRECT")
    basis_quality = role_mix.get("basis_evidence_quality", "MED")
    basis_bridge_supported = role_mix.get("basis_bridge_supported", True)
    _require(basis_state in evidence["states"], "target_role_mix has invalid basis_evidence_state")
    _require(basis_quality in evidence["qualities"], "target_role_mix has invalid basis_evidence_quality")
    _require(isinstance(basis_bridge_supported, bool),
             "target_role_mix.basis_bridge_supported must be boolean")
    if basis_state in evidence["provisional_states"]:
        assumptions.append("target_role_mix_basis")
    if basis_quality in evidence["unsupported_qualities"]:
        low_quality.append("target_role_mix_basis")

    # Current population/cost/entry facts require direct or safely calculated
    # target-archetype evidence. Forward proxies need an explicit
    # machine-readable bridge attestation; without it the scorer conservatively
    # caps readiness at PROVISIONAL and leaves publication review to inspect it.
    by_path = dict(labeled)
    core_paths = tuple(path for path in config["core_paths"] if path != "target_role_mix_basis")
    core_unsubstantiated = []
    for path in core_paths:
        item = by_path.get(path, {})
        if item.get("evidence_state") != "DIRECT" or item.get("method") not in evidence["direct_methods"]:
            core_unsubstantiated.append(path)
    if basis_state != "DIRECT":
        core_unsubstantiated.append("target_role_mix_basis")
    bridge_required = evidence["proxy_bridge_required"]
    unbridged_core_proxy = sorted(path for path in core_paths
                                  if by_path.get(path, {}).get("evidence_state") == "PROXY"
                                  and bridge_required
                                  and by_path[path].get("bridge_supported") is not True)
    if basis_state == "PROXY" and bridge_required and not basis_bridge_supported:
        unbridged_core_proxy.append("target_role_mix_basis")
    forward_unbridged = sorted(path for path, item in labeled
                               if path not in core_paths and item.get("evidence_state") == "PROXY"
                               and bridge_required
                               and item.get("bridge_supported") is not True)
    forward_paths = set(config["forward_bridge_paths"])
    unsupported_forward_direct = sorted(path for path, item in labeled
                                        if path in forward_paths and item.get("evidence_state") == "DIRECT"
                                        and bridge_required
                                        and item.get("bridge_supported") is not True)

    order = {name: index for index, name in enumerate(config["statuses"])}
    status = config["statuses"][0]
    def worsen(candidate):
        nonlocal status
        if order[candidate] > order[status]:
            status = candidate

    if missing_paths or unsupported_states or low_quality:
        worsen(config["unsupported_input_status"])
    if selection_uncertainty:
        worsen(thresholds["archetype_selection"]["uncertainty_readiness"])
    if unsupported_forward_direct:
        worsen(config["unbridged_forward_direct_status"])
    if unbridged_core_proxy:
        worsen(config["unbridged_core_proxy_status"])
    if basis_state in ("ASSUMPTION", "MISSING"):
        worsen(config["role_basis_assumption_status"])
    if assumptions:
        worsen(config["assumption_status"])
    if core_unsubstantiated:
        worsen(config["unsubstantiated_core_status"])
    if forward_unbridged:
        worsen(config["unbridged_forward_proxy_status"])
    if cross_tier:
        worsen(config["cross_tier_status"])
    if action_instability:
        worsen(config["action_instability_status"])
    return {"status": status, "missing_critical_inputs": sorted(missing_paths),
            "assumption_critical_input_count": len(assumptions),
            "low_quality_critical_input_count": len(low_quality),
            "selection_uncertainty": selection_uncertainty}


def _default_action(verdict, thresholds):
    if verdict == "indeterminate":
        return thresholds["actions"]["uncertainty"]
    return thresholds["actions"]["ordinary"][verdict]


def calculate(record, thresholds=None):
    """Validate inputs, calculate score bundles, and derive the v4.1 decision."""
    thresholds = load_thresholds() if thresholds is None else thresholds
    validate_thresholds(thresholds)
    _require(isinstance(record, dict), "record must be an object")
    _require(isinstance(record.get("dataset_inputs"), dict), "dataset_inputs must be an object")
    _require(isinstance(record.get("inputs"), dict), "inputs must be an object")
    record = dict(record)
    record["_thresholds"] = thresholds

    target = record["inputs"].get("target_archetype", {})
    _require(isinstance(target, dict), "inputs.target_archetype must be an object")
    enumeration = target.get("enumeration_coverage")
    if enumeration is not None:
        _require(isinstance(enumeration, dict) and set(enumeration) == {"base", "low", "high"},
                 "target_archetype.enumeration_coverage must contain exactly base/low/high")
        base, low, high = enumeration["base"], enumeration["low"], enumeration["high"]
        domain_low, domain_high = _domain(thresholds, "enumeration_coverage")
        _require(all(_finite(value) for value in (base, low, high))
                 and domain_low <= low <= base <= high <= domain_high,
                 "target_archetype enumeration coverage must be ordered inside [0,1]")
        _require(base >= thresholds["archetype_selection"]["enumeration_min_coverage"],
                 "target archetypes must enumerate at least the frozen minimum coverage")

    missing_paths = set()
    ramps = _ramp_intervals(record, missing_paths)
    survival = _selection(record["inputs"]["y5_survival"], "inputs.y5_survival",
                          *_domain(thresholds, "y5_survival"), thresholds=thresholds)
    if survival[3]:
        missing_paths.add("y5_survival")

    bundles = {}
    for bound in BOUNDS:
        V, v_sub = _v_bundle(record, bound, missing_paths)
        ramp = ramps[bound]
        I = None if ramp is None else _implementation_score(ramp, thresholds)
        C, retained, _c_missing = _simple_factor(
            record["inputs"]["commercial_retention"], "inputs.commercial_retention", bound,
            missing_paths, thresholds, "commercial_retention")
        B, b_sub = _n5_and_b(record, bound, missing_paths)
        P, p_sub = _p_bundle(record, bound, missing_paths)
        scores = {"V": V, "I": I, "C": C, "B": B, "P": P}
        S = None if any(value is None for value in scores.values()) else geometric_mean(scores.values())
        bundles[bound] = {
            "scores": scores,
            "S": S,
            "subfactors": {"V": v_sub, "implementation_ramp": ramp,
                           "commercial_retention": None if (bound == "base" and _c_missing) else retained,
                           "B": b_sub, "P": p_sub},
        }

    for factor in FACTOR_NAMES:
        low, base, high = (bundles[bound]["scores"][factor] for bound in BOUNDS)
        factor_low, factor_high = _domain(thresholds, "factor")
        _require(_finite(low) and _finite(high) and factor_low <= low <= high <= factor_high,
                 "factor %s bounds must be finite, ordered, and in [0,10]" % factor)
        if base is not None:
            _require(low <= base + EPS <= high + EPS, "factor %s base is outside bounds" % factor)
    if bundles["base"]["S"] is not None:
        _require(bundles["low"]["S"] <= bundles["base"]["S"] + EPS <= bundles["high"]["S"] + EPS,
                 "aggregate base is outside bounds")

    raw = {bound: _raw_verdict(bundles[bound]["S"], bundles[bound]["scores"], thresholds) for bound in BOUNDS}
    scenario = {}
    for bound, survival_index in (("low", 1), ("high", 2)):
        verdict, reasons = _gate_verdict(raw[bound], survival[survival_index], thresholds)
        scenario[bound] = {"verdict": verdict, "reasons": reasons, "survival": survival[survival_index]}

    partial = thresholds["partial_identification"]
    has_missing = bool(missing_paths)
    endpoints_identified = scenario["low"]["verdict"] == scenario["high"]["verdict"]
    economic = (scenario["low"]["verdict"] if endpoints_identified
                else partial["different_endpoint_verdict"])
    if has_missing:
        base_reasons = sorted(set(scenario["low"]["reasons"]) & set(scenario["high"]["reasons"]))
    else:
        _base_verdict, base_reasons = _gate_verdict(raw["base"], survival[0], thresholds)

    low_action, high_action = (_default_action(scenario[bound]["verdict"], thresholds) for bound in ("low", "high"))
    action_instability = low_action != high_action
    cross_tier = scenario["low"]["verdict"] != scenario["high"]["verdict"]
    readiness = _readiness(record, missing_paths, cross_tier, action_instability)
    stable_structural_kill = scenario["high"]["verdict"] == "kill"
    if stable_structural_kill:
        action = thresholds["actions"]["ordinary"]["kill"]
    elif economic == "indeterminate" or action_instability or readiness["status"] == "UNPROVEN":
        action = thresholds["actions"]["uncertainty"]
    else:
        action = _default_action(economic, thresholds)

    decision = {
        "raw_verdict": raw["base"],
        "economic_verdict": economic,
        "gate_reasons": base_reasons,
        "evidence_readiness": readiness,
        "action": action,
        "sensitivity": {
            "low_verdict": scenario["low"]["verdict"],
            "high_verdict": scenario["high"]["verdict"],
            "low_y5_survival": scenario["low"]["survival"],
            "high_y5_survival": scenario["high"]["survival"],
            "cross_tier": cross_tier,
            "action_instability": action_instability,
            "stable_structural_kill": stable_structural_kill,
        },
    }
    return {"low": bundles["low"], "base": bundles["base"], "high": bundles["high"], "decision": decision}
