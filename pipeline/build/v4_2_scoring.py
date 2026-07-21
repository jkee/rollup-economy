#!/usr/bin/env python3
"""Deterministic outcome-blind v4.2 V/I/C/B/P scorer and h viability gate."""

import itertools
import json
import math
import os
from datetime import date


HERE = os.path.dirname(os.path.abspath(__file__))
FACTOR_NAMES = ("V", "I", "C", "B", "P")
BOUNDS = ("low", "base", "high")
VERDICT_DESCENDING = ("hell_yes", "strong", "conditional", "pass")
INDEX = {"base": 0, "low": 1, "high": 2}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def load_thresholds(path=None):
    path = path or os.path.join(HERE, "thresholds_v4_2.json")
    with open(path, "r", encoding="utf-8") as handle:
        value = json.load(handle)
    return validate_thresholds(value)


def _exact(actual, expected, message):
    _require(actual == expected, message)


def validate_thresholds(t):
    """Fail closed on every unknown, missing, or changed frozen-candidate key."""
    _require(isinstance(t, dict), "thresholds must be an object")
    _exact(set(t), {
        "version", "frozen", "status", "authored_date", "score", "archetype_selection", "domains",
        "value_available", "implementation", "commercial_capture", "buyability", "price_discipline",
        "viability_gate", "verdict_cuts", "verdict_min_each_factor", "verdict_order", "survival_gate",
        "actions", "partial_identification", "evidence_contract", "readiness", "validation_tolerances",
        "sentinels", "display",
    }, "threshold top-level keys are incomplete or unexpected")
    _exact(t["version"], "4.2", "threshold version must be 4.2")
    _exact(t["frozen"], False, "v4.2 is an outcome-blind freeze candidate until authorization")
    _exact(t["status"], "outcome-blind freeze candidate", "threshold status differs")
    try:
        date.fromisoformat(t["authored_date"])
    except (TypeError, ValueError):
        raise ValueError("authored_date must be an ISO date")
    _exact(t["authored_date"], "2026-07-21", "authored date differs")
    _exact(t["score"], {"type": "geometric_mean", "factors": list(FACTOR_NAMES), "scale": [0.0, 10.0]},
           "score mapping differs")
    _exact(t["archetype_selection"], {
        "enumeration_min_coverage": .80, "selection_rule": "largest_base_band_count",
        "near_tie_fraction": .10, "overlap_rule": "selection_uncertainty_widens_ranges",
        "tie_break_rule": "lexicographically_smallest_stable_id",
        "record_policy": "one_primary_record_per_naics", "uncertainty_readiness": "UNPROVEN",
    }, "archetype selection mapping differs")
    _exact(t["domains"], {
        "factor": [0.0, 10.0], "enumeration_coverage": [0.0, 1.0],
        "nonnegative_money": [0.0, None], "role_cost_weight": [0.0, 1.0],
        "removable_fraction": [0.0, 1.0], "implementation_realization": [0.0, 1.0],
        "implementation_investment": [0.0, None], "commercial_retention": [0.0, 1.0],
        "n_band": [0.0, None], "archetype_coverage": [0.0, 1.0],
        "sale_availability": [0.0, 1.0], "buyer_access_win_share": [0.0, 1.0],
        "five_year_capacity": [0.0, None],
        "buy_multiple": [0.0, None], "downside_exit_multiple": [0.0, None],
        "constant_price_survival": [0.0, 1.0],
    }, "formula domains differ")
    _exact(t["value_available"], {
        "denominator": "recognized_revenue_minus_reconciled_included_third_party_pass_through",
        "gross_removable_cva_anchor": .25, "positive_bounded_denominator_required": True,
        "pass_through_double_count_policy": "cost_id_disjoint_from_v_numerator",
        "revenue_basis_modes": ["GROSS_OF_ALL", "NET_OF_ALL", "MIXED"],
        "recognized_accounting_basis": {"recognition_standard": "ACCRUAL_RECOGNIZED_REVENUE",
                                         "measurement_period": "TRAILING_TWELVE_MONTHS",
                                         "presentation_link": "must_equal_revenue_basis"},
        "empty_pass_through_basis": "GROSS_OF_ALL",
        "unsupported_nonempty_reconciliation": "R_cva_missing",
        "zero_G_annihilator": "exact_zero_costs_or_every_exact_zero_removability_forces_V_I_h_zero_even_if_R_cva_missing",
        "role_spec_modes": ["frozen", "assumption", "missing"],
    }, "V mapping differs")
    _exact(t["implementation"], {
        "years": 5, "discount_rate": .10, "realization_order": "unconstrained",
        "investment_years": [0, 1, 2, 3, 4, 5],
        "investment_unit": "fraction_of_one_full_year_of_G",
        "negative_investment_policy": "forbidden", "zero_G_scores": {"V": 0.0, "I": 0.0},
        "missing_or_unbounded_G_factors": ["V", "I"],
    }, "implementation mapping differs")
    _exact(t["commercial_capture"], {
        "years": 5, "discount_rate": .10, "schedule_order": "unconstrained",
        "weighting": "discounted_operational_realization", "zero_realization_score": 0.0,
        "support_rule": "exact_box_vertex_extrema", "vertex_years": 5,
        "vertex_coordinate_values": "per_year_realization_interval_endpoints",
        "vertex_constraints": ["per_year_bounds"],
        "retention_extrema": {"minimum": "c_low", "maximum": "c_high"},
        "zero_denominator_vertex": "include_zero_score_only_for_all_zero_schedule",
        "decision_support": "joint_projected_realization_hull",
        "joint_projection": ["A=sum_r_w", "N=sum_r_c_w"],
        "joint_edge_candidates": ["vertices", "stationary_I_times_C", "factor_floors",
                                  "aggregate_cuts", "h_zero", "interval_representatives"],
    }, "C mapping differs")
    _exact(t["buyability"], {
        "count_definition": "expected_executable_and_winnable_five_year_targets", "n5_full_score": 500.0,
        "buyer_profile": "credible_us_lmm_national_sourcing_no_privileged_access",
        "active_consolidator_penalty": "forbidden", "paid_price_channel": "P_only",
        "opportunity_formula": "O5=n_band*coverage*sale_availability*buyer_access_win_share",
        "capacity_formula": "K5=min(deal_execution_capacity_5y,integration_onboarding_capacity_5y)",
        "executable_formula": "N5=min(O5,K5)",
        "missing_capacity_support": {"low": 0.0, "base": None,
                                     "high": "min_opportunity_high_and_every_known_capacity_high"},
        "capacity_types": ["DEAL_EXECUTION", "INTEGRATION_ONBOARDING"],
        "capacity_horizon": ["ENTRY_DATE", "END_OF_YEAR_5"],
        "capacity_measure": "MAXIMUM_NON_DUPLICATIVE_COMPLETED_AND_FULLY_ONBOARDED_TARGET_COUNT",
    }, "B mapping differs")
    _exact(t["price_discipline"], {
        "entry_reference_multiple": 14.0, "entry_score_span": 10.0,
        "downside_ratio_floor": .5, "downside_ratio_slope": 20.0,
        "normalized_y5_state_required": True, "state_policy": "one_state_shared_by_low_base_high",
        "multiple_expansion_reward": "capped_at_10",
        "state_dimensions": ["accounting", "size", "service_mix", "customer_concentration",
                             "management_depth", "platform_quality"],
        "state_dimension_value": "HOLD_ENTRY_REFERENCE",
        "allowed_adjustment_channels": ["EXTERNAL_DISCOUNT_RATE_ENVIRONMENT",
            "ENTRY_EQUIVALENT_COMPARABLE_MULTIPLE_LEVEL", "PRIVATE_TRANSACTION_LIQUIDITY"],
        "anchor_channel": "ENTRY_EQUIVALENT_COMPARABLE_MULTIPLE_LEVEL",
        "anchor_state_link": "same_normalized_y5_state_digest",
        "favorable_adjustment_policy": "forbidden", "state_link": "canonical_sha256",
        "missing_exit_or_state_high_support": "known_entry_score_ceiling",
        "missing_buy_high_support": "zero_if_exit_high_zero_else_10_without_positive_buy_lower_bound",
    }, "P mapping differs")
    _exact(t["viability_gate"], {"diagnostic": "h", "kill_operator": "less_than_or_equal",
                                  "kill_threshold": 0.0,
                                  "application_order": "after_factor_verdict_before_survival",
                                  "evidence_independent": True}, "h gate mapping differs")
    cuts = {"hell_yes": 7.5, "strong": 6.0, "conditional": 4.5, "pass": 3.0}
    floors = {"hell_yes": 6.0, "strong": 4.0, "conditional": 2.0, "pass": 1.0}
    _exact(t["verdict_cuts"], cuts, "verdict cuts differ")
    _exact(t["verdict_min_each_factor"], floors, "factor floors differ")
    _exact(t["verdict_order"], ["kill", "pass", "conditional", "strong", "hell_yes"],
           "verdict order differs")
    _exact(t["survival_gate"], {
        "measure": "constant_price_operator_controlled_value_added_demand_share_y5",
        "index_method": "FIXED_BASE_LASPEYRES_CVA", "basket_mismatch_policy": "missing_[0,1]",
        "baseline_point_identification_required": True, "new_demand_cap": 1.0,
        "no_cap_at_or_above": .75, "conditional_cap_at_or_above": .50,
        "pass_cap_at_or_above": .25,
        "caps": {"no_cap": "hell_yes", "conditional": "conditional", "pass": "pass", "kill": "kill"},
        "application_order": "after_viability_gate",
    }, "survival mapping differs")
    _exact(t["actions"], {
        "ordinary": {"hell_yes": "DEEP_DIVE", "strong": "DEEP_DIVE", "conditional": "SELECTIVE",
                     "pass": "DEPRIORITIZE", "kill": "AVOID"},
        "uncertainty": "EVIDENCE_FIRST", "stable_structural_kill": "AVOID",
    }, "action mapping differs")
    _exact(t["partial_identification"], {
        "missing_base": None, "unbounded_count_token": "UNBOUNDED",
        "unbounded_negative_h": "NEGATIVE_UNBOUNDED",
        "identified_rule": "all_feasible_joint_scenarios_same_verdict",
        "different_verdict": "indeterminate", "base_requires_all_score_and_gate_inputs": True,
    }, "partial-identification mapping differs")
    _exact(t["evidence_contract"], {
        "methods": ["OBSERVED", "CALCULATED", "ESTIMATE"],
        "states": ["DIRECT", "PROXY", "ASSUMPTION", "MISSING"],
        "qualities": ["HIGH", "MED", "LOW", "NONE"],
        "direct_methods": ["OBSERVED", "CALCULATED"], "supported_qualities": ["HIGH", "MED"],
        "assumption_method": "ESTIMATE", "missing_method": "ESTIMATE",
        "source_requirement": {"DIRECT": "nonempty", "PROXY": "nonempty", "ASSUMPTION": "empty",
                               "MISSING": "empty"},
        "bridge_requirement": {"DIRECT": False, "PROXY": True, "ASSUMPTION": False, "MISSING": False},
        "endpoint_support_required": True,
        "validated_forward_proxy_fields": ["independent_validation", "longitudinal_validation"],
    }, "evidence contract differs")
    _exact(t["readiness"], {
        "statuses_in_order": ["SUBSTANTIATED", "PROVISIONAL", "UNPROVEN"],
        "unproven_states": ["ASSUMPTION", "MISSING"], "unproven_qualities": ["LOW", "NONE"],
        "core_paths": ["n_band", "recognized_revenue", "pass_through_reconciliation",
                       "third_party_pass_through", "employee_cash_cost",
                       "controllable_contractor_cash_cost", "target_role_mix_basis",
                       "target_archetype_coverage", "buy_mult"],
        "forward_paths": ["implementation_realization", "implementation_investment", "commercial_retention",
                          "five_year_sale_availability", "buyer_access_win_share",
                          "deal_execution_capacity_5y", "integration_onboarding_capacity_5y",
                          "normalized_y5_operating_state", "downside_exit_mult",
                          "operator_controlled_value_added_demand_share_y5"],
        "core_substantiation": "DIRECT_or_safely_CALCULATED_MED_HIGH",
        "forward_proxy_substantiation": "MED_HIGH_bridge_endpoints_and_independent_or_longitudinal_validation",
        "selection_uncertainty_status": "UNPROVEN", "unsupported_endpoint_status": "UNPROVEN",
        "failed_rationale_separation_status": "UNPROVEN",
        "supported_unvalidated_forward_proxy_status": "PROVISIONAL",
        "core_not_substantiated_status": "PROVISIONAL", "cross_tier_status": "PROVISIONAL",
        "action_instability_status": "PROVISIONAL",
    }, "readiness mapping differs")
    _exact(t["validation_tolerances"], {"numeric": 1e-12, "sentinel": 1e-9,
                                         "role_weight_sum": 1e-12}, "tolerances differ")
    _exact(t["display"], {"decimal_places": 2, "rounding_stage": "after_numeric_validation"},
           "display mapping differs")
    _validate_sentinels(t)
    return t


def _weights(t):
    d = t["implementation"]["discount_rate"]
    return [1.0 / ((1.0 + d) ** year) for year in range(1, t["implementation"]["years"] + 1)]


def _implementation_score(r, k, t):
    w = _weights(t); D = sum(w)
    raw = (sum(a * b for a, b in zip(r, w)) - k[0]
           - sum(a * b for a, b in zip(k[1:], w))) / D
    return t["score"]["scale"][1] * max(0.0, min(1.0, raw))


def _commercial_score(r, c, t):
    w = _weights(t)
    denominator = sum(a * weight for a, weight in zip(r, w))
    if denominator == 0:
        return t["commercial_capture"]["zero_realization_score"]
    if all(retention == c[0] for retention in c[1:]):
        # Preserve the exact constant-retention identity instead of introducing
        # roundoff through two proportional discounted sums.
        return t["score"]["scale"][1] * c[0]
    return t["score"]["scale"][1] * sum(
        realization * retention * weight
        for realization, retention, weight in zip(r, c, w)) / denominator


def _realization_vertices(resolved):
    """Enumerate the exact vertices of the unconstrained five-year interval box."""
    lows, highs = [item[1] for item in resolved], [item[2] for item in resolved]
    vertices = sorted(set(itertools.product(*[
        (low,) if low == high else (low, high) for low, high in zip(lows, highs)])))
    _require(vertices, "implementation realization intervals admit no feasible vertex")
    return vertices


def _commercial_support(resolved, ramps, captures, t):
    """Exact C extrema over feasible annual-realization box vertices."""
    w = _weights(t)
    zero = t["commercial_capture"]["zero_realization_score"]
    c_low, c_high = captures["low"], captures["high"]
    low_candidates, high_candidates = [], []
    for realization in _realization_vertices(resolved):
        denominator = sum(r * weight for r, weight in zip(realization, w))
        if denominator == 0:
            low_candidates.append(zero); high_candidates.append(zero)
            continue
        low_candidates.append(_commercial_score(realization, c_low, t))
        high_candidates.append(_commercial_score(realization, c_high, t))
    low, high = min(low_candidates), max(high_candidates)
    if ramps["base"] is None:
        base = None
    elif sum(r * weight for r, weight in zip(ramps["base"], w)) == 0:
        base = zero
    elif captures["base"] is None:
        base = None
    else:
        base = _commercial_score(ramps["base"], captures["base"], t)
    tolerance = t["validation_tolerances"]["numeric"]
    _require(low <= high + tolerance, "C vertex extrema are inconsistent")
    if base is not None:
        _require(low <= base + tolerance and base <= high + tolerance,
                 "C base is outside exact vertex support")
        if abs(low - base) <= tolerance and abs(high - base) <= tolerance:
            low = high = base
        else:
            low, high = min(low, base), max(high, base)
    elif high - low <= tolerance:
        low = high = low
    if low > high:  # floating-point equality at a collapsed support point
        low = high = min(low, high)
    return {"low": low, "base": base, "high": high}


def _projected_hull(realizations, capture, t):
    """Convex hull of feasible realization schedules projected to (A, N)."""
    weights = _weights(t)
    points = sorted(set((sum(r * w for r, w in zip(schedule, weights)),
                         sum(r * c * w for r, c, w in zip(schedule, capture, weights)))
                        for schedule in realizations))
    if len(points) <= 1:
        return points
    def cross(origin, left, right):
        return ((left[0] - origin[0]) * (right[1] - origin[1])
                - (left[1] - origin[1]) * (right[0] - origin[0]))
    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def _quadratic_roots(a, b, c, tolerance):
    if abs(a) <= tolerance:
        return [] if abs(b) <= tolerance else [-c / b]
    discriminant = b * b - 4 * a * c
    if discriminant < -tolerance:
        return []
    root = math.sqrt(max(0.0, discriminant))
    return [(-b - root) / (2 * a), (-b + root) / (2 * a)]


def _joint_edge_candidates(left, right, investment, other_scores, t):
    """Finite exact candidate parameters for tier changes on one projected edge."""
    tolerance = t["validation_tolerances"]["numeric"]
    a, n = left; b, d = right[0] - a, right[1] - n
    parameters = {0.0, 1.0}
    # Stationary points of (A-K)N/A, the only nonlinear score product.
    for root in _quadratic_roots(d * b * b, 2 * d * a * b,
                                 d * a * (a - investment) + investment * b * n, tolerance):
        if tolerance < root < 1 - tolerance: parameters.add(root)
    for verdict in VERDICT_DESCENDING:
        floor = t["verdict_min_each_factor"][verdict]
        # I floor: A = K + floor*D/10.
        if abs(b) > tolerance:
            root = (investment + floor * sum(_weights(t)) / 10.0 - a) / b
            if tolerance < root < 1 - tolerance: parameters.add(root)
        # C floor: N = floor*A/10.
        coefficient = d - floor * b / 10.0
        if abs(coefficient) > tolerance:
            root = (floor * a / 10.0 - n) / coefficient
            if tolerance < root < 1 - tolerance: parameters.add(root)
        # Aggregate cut: I*C equals the remaining required factor product.
        other_product = math.prod(other_scores.values())
        if other_product > 0:
            target_ic = t["verdict_cuts"][verdict] ** 5 / other_product
            target = target_ic * sum(_weights(t)) / 100.0
            qa = b * d
            qb = (a - investment) * d + b * n - target * b
            qc = (a - investment) * n - target * a
            for root in _quadratic_roots(qa, qb, qc, tolerance):
                if tolerance < root < 1 - tolerance: parameters.add(root)
    # h gate: N=K.
    if abs(d) > tolerance:
        root = (investment - n) / d
        if tolerance < root < 1 - tolerance: parameters.add(root)
    ordered = sorted(parameters)
    parameters.update((left_t + right_t) / 2.0 for left_t, right_t in zip(ordered, ordered[1:]))
    return sorted(parameters)


def _joint_decision_endpoint(realizations, capture, investment_schedule, other_scores,
                             survival, t, *, best):
    """Exact tier endpoint over the shared r polytope for fixed c/k/other endpoints.

    Projection to (A=sum(rw), N=sum(rcw)) is a convex polygon. I, C, h and the
    I*C contribution to the geometric mean depend only on (A,N). Hull vertices,
    edge stationary points, every floor/cut/h intersection, and one point in
    every resulting edge interval form a finite exact tier partition.
    """
    if any(value is None for value in investment_schedule):
        return "kill", ["operating_value_viability_h_le_0"]
    hull = _projected_hull(realizations, capture, t)
    _require(hull, "joint realization projection must be nonempty")
    weights, D = _weights(t), sum(_weights(t))
    investment = investment_schedule[0] + sum(
        value * weight for value, weight in zip(investment_schedule[1:], weights))
    candidates = []
    edges = [(hull[0], hull[0])] if len(hull) == 1 else list(zip(hull, hull[1:] + hull[:1]))
    for left, right in edges:
        for parameter in _joint_edge_candidates(left, right, investment, other_scores, t):
            A = left[0] + parameter * (right[0] - left[0])
            N = left[1] + parameter * (right[1] - left[1])
            I = 10.0 * max(0.0, min(1.0, (A - investment) / D))
            C = t["commercial_capture"]["zero_realization_score"] if A == 0 else 10.0 * N / A
            scores = {"I": I, "C": C, **other_scores}
            aggregate = geometric_mean(scores.values())
            tolerance = t["validation_tolerances"]["numeric"]
            raw = "kill"
            for candidate_verdict in VERDICT_DESCENDING:
                if (aggregate + tolerance >= t["verdict_cuts"][candidate_verdict]
                        and min(scores.values()) + tolerance
                        >= t["verdict_min_each_factor"][candidate_verdict]):
                    raw = candidate_verdict; break
            reasons = []
            if N - investment <= t["viability_gate"]["kill_threshold"]:
                raw = "kill"; reasons.append("operating_value_viability_h_le_0")
            verdict, survival_reasons = _survival_gate(raw, survival, t)
            candidates.append((verdict, reasons + survival_reasons))
    order = {name: index for index, name in enumerate(t["verdict_order"])}
    chooser = max if best else min
    return chooser(candidates, key=lambda item: order[item[0]])


def _h_value(r, k, c, t):
    w = _weights(t)
    return sum(a * b * weight for a, b, weight in zip(r, c, w)) - k[0] - sum(
        a * weight for a, weight in zip(k[1:], w))


def _validate_sentinels(t):
    sent = t.get("sentinels", {})
    _exact(set(sent), {"implementation_schedules_zero_investment", "implementation_investment_cases",
                       "realization_ramp_decay_case",
                       "commercial_constant_schedules", "commercial_timing_case",
                       "r_cva_reconciliation_cases", "r_cva_double_subtraction_forbidden",
                       "zero_g_missing_denominator_cases",
                       "buyability_capacity_cases", "buyability_missing_capacity_support",
                       "survival_laspeyres_case", "survival_ranged_baseline_case",
                       "price_adjustment_case", "price_missing_exit_entry_ceiling_case",
                       "price_missing_buy_zero_exit_case",
                       "mixed_component_validation_case", "joint_realization_decision_case",
                       "viability_negative_case", "factor_verdicts"}, "sentinel keys differ")
    expected_i = [
        ([1., 1., 1., 1., 1.], 10.), ([0., 1., 1., 1., 1.], 7.601841083684134),
        ([0., 0., 1., 1., 1.], 5.4216966143060725),
        ([0., 0., 0., 1., 1.], 3.4397470966896524),
        ([.2, .4, .6, .8, 1.], 5.620251920525462), ([0., 0., 0., 0., 0.], 0.),
    ]
    _require(len(sent["implementation_schedules_zero_investment"]) == len(expected_i),
             "I sentinels incomplete")
    tol = t["validation_tolerances"]["sentinel"]
    for item, (r, expected) in zip(sent["implementation_schedules_zero_investment"], expected_i):
        _exact(item, {"r": r, "expected": expected}, "I sentinel differs")
        _require(abs(_implementation_score(r, [0.] * 6, t) - expected) <= tol, "I sentinel fails")
    D = sum(_weights(t))
    investment_cases = [
        {"r": [1.] * 5, "k0_annuity_fraction": 1.0, "expected": 0.0},
        {"r": [1.] * 5, "k0_annuity_fraction": 1.25, "expected": 0.0},
    ]
    _exact(sent["implementation_investment_cases"], investment_cases, "investment sentinels differ")
    for item in investment_cases:
        _require(abs(_implementation_score(item["r"], [item["k0_annuity_fraction"] * D] + [0.] * 5, t)
                     - item["expected"]) <= tol, "investment sentinel fails")
    ramp_decay = {"decayed_r": [.2, .8, .9, .4, .1], "sustained_r": [.2, .8, .9, .9, .9],
                  "c": [0., 0., 0., 1., 1.], "k": [0., 0., 0., 0., 0., 0.],
                  "expected_decayed": {"I": 4.8920083209120255, "C": 1.8080639652851715,
                                       "h": .3352975144519437},
                  "expected_sustained": {"I": 7.103274311641087, "C": 4.3582329095009475,
                                         "h": 1.173541300581803}}
    _exact(sent["realization_ramp_decay_case"], ramp_decay, "ramp-decay sentinel differs")
    for path, expected_key in ((ramp_decay["decayed_r"], "expected_decayed"),
                               (ramp_decay["sustained_r"], "expected_sustained")):
        actual = {"I": _implementation_score(path, ramp_decay["k"], t),
                  "C": _commercial_score(path, ramp_decay["c"], t),
                  "h": _h_value(path, ramp_decay["k"], ramp_decay["c"], t)}
        _require(all(abs(actual[key] - ramp_decay[expected_key][key]) <= tol
                     for key in actual), "ramp-decay sentinel fails")
    expected_c = [(0., 0.), (.2, 2.), (.5, 5.), (.8, 8.), (1., 10.)]
    for item, (value, expected) in zip(sent["commercial_constant_schedules"], expected_c):
        _exact(item, {"value": value, "expected": expected}, "C sentinel differs")
        _require(abs(_commercial_score([1.] * 5, [value] * 5, t) - expected) <= tol, "C sentinel fails")
    timing = {"r": [0., 0., 0., 0., 1.], "c": [1., 1., 1., 1., .001], "expected": .01}
    _exact(sent["commercial_timing_case"], timing, "C timing sentinel differs")
    _require(abs(_commercial_score(timing["r"], timing["c"], t) - timing["expected"]) <= tol,
             "C timing sentinel fails")
    expected_reconciliation = [
        {"basis": "GROSS_OF_ALL", "revenue": 100., "included": [20.], "already_netted": [], "expected": 80.},
        {"basis": "NET_OF_ALL", "revenue": 80., "included": [], "already_netted": [20.], "expected": 80.},
        {"basis": "MIXED", "revenue": 90., "included": [10.], "already_netted": [10.], "expected": 80.},
        {"basis": "GROSS_OF_ALL", "revenue": 100., "included": [], "already_netted": [], "expected": 100.},
    ]
    _exact(sent["r_cva_reconciliation_cases"], expected_reconciliation, "R_cva sentinels differ")
    for item in expected_reconciliation:
        _require(abs(item["revenue"] - sum(item["included"]) - item["expected"]) <= tol,
                 "R_cva reconciliation sentinel fails")
    _exact(sent["r_cva_double_subtraction_forbidden"], True, "double subtraction sentinel differs")
    zero_g_cases = [
        {"case": "EXACT_ZERO_EMPLOYEE_AND_CONTRACTOR_COST", "expected_V": 0.,
         "expected_I": 0., "expected_h": 0., "expected_verdict": "kill"},
        {"case": "EVERY_EXACT_ZERO_REMOVABILITY_CONTRIBUTION", "expected_V": 0.,
         "expected_I": 0., "expected_h": 0., "expected_verdict": "kill"},
    ]
    _exact(sent["zero_g_missing_denominator_cases"], zero_g_cases,
           "zero-G annihilator sentinels differ")
    capacity_cases = [
        {"O5": 100., "deal_capacity": 30., "integration_capacity": 40., "expected_K5": 30., "expected_N5": 30.},
        {"O5": 25., "deal_capacity": 50., "integration_capacity": 40., "expected_K5": 40., "expected_N5": 25.},
    ]
    _exact(sent["buyability_capacity_cases"], capacity_cases, "capacity sentinels differ")
    for item in capacity_cases:
        _require(min(item["deal_capacity"], item["integration_capacity"]) == item["expected_K5"]
                 and min(item["O5"], item["expected_K5"]) == item["expected_N5"],
                 "capacity sentinel fails")
    _exact(sent["buyability_missing_capacity_support"],
           {"O5_high": 100., "known_capacity_high": 40., "expected_low": 0.,
            "expected_base": None, "expected_high": 40.},
           "missing capacity sentinel differs")
    missing_capacity = sent["buyability_missing_capacity_support"]
    _require(min(missing_capacity["O5_high"], missing_capacity["known_capacity_high"])
             == missing_capacity["expected_high"], "known capacity ceiling sentinel fails")
    survival_case = {"weights": [.6, .4], "quantity_relatives": [.5, .75], "expected": .6}
    _exact(sent["survival_laspeyres_case"], survival_case, "survival sentinel differs")
    _require(abs(sum(a * b for a, b in zip(survival_case["weights"],
                                            survival_case["quantity_relatives"]))
                 - survival_case["expected"]) <= tol, "survival sentinel fails")
    ranged_baseline = {"q0": {"low": 50., "base": 100., "high": 400.},
                       "q5": 80., "expected": "MISSING"}
    _exact(sent["survival_ranged_baseline_case"], ranged_baseline,
           "ranged survival baseline sentinel differs")
    _require(len(set(ranged_baseline["q0"].values())) > 1,
             "ranged survival baseline sentinel must remain non-point-identified")
    price_case = {"anchor": 5., "adjustments": [-1., -.5], "expected": 3.5,
                  "positive_adjustment_forbidden": True}
    _exact(sent["price_adjustment_case"], price_case, "price sentinel differs")
    _require(abs(price_case["anchor"] + sum(price_case["adjustments"]) - price_case["expected"]) <= tol,
             "price sentinel fails")
    price_ceiling = {"buy_low": 13., "expected_P_high": 1.}
    _exact(sent["price_missing_exit_entry_ceiling_case"], price_ceiling,
           "missing price support sentinel differs")
    _require(_clamp(t["price_discipline"]["entry_reference_multiple"] - price_ceiling["buy_low"], t)
             == price_ceiling["expected_P_high"], "entry ceiling sentinel fails")
    zero_exit = {"buy": "MISSING_POSITIVE", "exit_high": 0., "expected_P_high": 0.}
    _exact(sent["price_missing_buy_zero_exit_case"], zero_exit,
           "missing buy zero-exit sentinel differs")
    _require(_clamp(t["price_discipline"]["downside_ratio_slope"]
                    * (0.0 - t["price_discipline"]["downside_ratio_floor"]), t)
             == zero_exit["expected_P_high"], "zero-exit resilience sentinel fails")
    validation_case = {"component_validation_kinds": ["independent_corroboration",
                                                        "longitudinal_validation"],
                       "expected_complete": True}
    _exact(sent["mixed_component_validation_case"], validation_case,
           "mixed validation sentinel differs")
    _require(all(kind in ("independent_corroboration", "longitudinal_validation")
                 for kind in validation_case["component_validation_kinds"]),
             "mixed validation sentinel fails")
    joint_case = {"x": .043293960941, "c": [.05, .05, .05, .05, 1.],
                  "k": [0., 0., 0., 0., 0., 0.],
                  "fixed_factors": {"V": 6.5, "B": 6.5, "P": 6.5}, "survival": .8,
                  "expected_low_verdict": "conditional", "expected_high_verdict": "conditional",
                  "expected_action": "SELECTIVE"}
    _exact(sent["joint_realization_decision_case"], joint_case,
           "joint realization sentinel differs")
    resolved = [(joint_case["x"], joint_case["x"], 1., False)] * 4 + [(1., 1., 1., False)]
    realizations = _realization_vertices(resolved)
    lower = _joint_decision_endpoint(realizations, joint_case["c"], joint_case["k"],
                                     joint_case["fixed_factors"], joint_case["survival"], t,
                                     best=False)[0]
    upper = _joint_decision_endpoint(realizations, joint_case["c"], joint_case["k"],
                                     joint_case["fixed_factors"], joint_case["survival"], t,
                                     best=True)[0]
    _require(lower == joint_case["expected_low_verdict"]
             and upper == joint_case["expected_high_verdict"],
             "joint realization decision sentinel fails")
    _exact(sent["viability_negative_case"], {"r": 1.0, "c": .2, "k0_annuity_fraction": .25,
                                               "expected_relation": "h_less_than_zero"},
           "h sentinel differs")
    _require(_h_value([1.] * 5, [.25 * D] + [0.] * 5, [.2] * 5, t) < 0, "h sentinel fails")
    _exact(sent["factor_verdicts"], [
        {"factors": [8., 8., 8., 8., 8.], "expected": "hell_yes"},
        {"factors": [7., 7., 7., 7., 7.], "expected": "strong"},
        {"factors": [5., 5., 5., 5., 5.], "expected": "conditional"},
        {"factors": [10., 1.5, 10., 10., 10.], "expected": "pass"},
        {"factors": [10., .9, 10., 10., 10.], "expected": "kill"},
    ], "factor sentinels differ")


def _domain(t, name):
    return tuple(t["domains"][name])


def _selection(item, path, domain, t, *, integer=False, strict_low=False):
    _require(isinstance(item, dict), "%s must be an object" % path)
    contract = t["evidence_contract"]
    method, state, quality = item.get("method"), item.get("evidence_state"), item.get("evidence_quality")
    sources = item.get("source_ids")
    _require(method in contract["methods"], "%s has invalid method" % path)
    _require(state in contract["states"], "%s has invalid evidence_state" % path)
    _require(quality in contract["qualities"], "%s has invalid evidence_quality" % path)
    _require(isinstance(sources, list) and all(isinstance(x, str) and x for x in sources),
             "%s.source_ids must be a string array" % path)
    _require(len(sources) == len(set(sources)), "%s.source_ids must be unique" % path)
    bridge = item.get("bridge_supported", False)
    endpoints = item.get("endpoints_supported", False)
    _require(isinstance(bridge, bool) and isinstance(endpoints, bool),
             "%s bridge/endpoints attestations must be boolean" % path)
    for field in contract["validated_forward_proxy_fields"]:
        _require(isinstance(item.get(field, False), bool), "%s.%s must be boolean" % (path, field))
    if state == "DIRECT":
        _require(method in contract["direct_methods"] and quality in contract["supported_qualities"] and sources,
                 "%s DIRECT evidence contract failed" % path)
    elif state == "PROXY":
        _require(quality in ("HIGH", "MED", "LOW") and sources and bridge,
                 "%s PROXY evidence contract failed" % path)
    elif state == "ASSUMPTION":
        _require(method == contract["assumption_method"] and quality == "NONE" and not sources,
                 "%s ASSUMPTION evidence contract failed" % path)
    else:
        _require(method == contract["missing_method"] and quality == "NONE" and not sources,
                 "%s MISSING evidence contract failed" % path)
    rng = item.get("range")
    _require(isinstance(rng, dict) and set(rng) == {"low", "high"}, "%s.range must contain low/high" % path)
    value, low, high = item.get("value"), rng["low"], rng["high"]
    if state == "MISSING":
        _require(value is None and low is None and high is None,
                 "%s MISSING requires null value/low/high" % path)
        return (None, domain[0], domain[1], True)
    _require(all(_finite(x) for x in (value, low, high)), "%s requires finite value/range" % path)
    value, low, high = float(value), float(low), float(high)
    _require(low <= value <= high, "%s requires low <= value <= high" % path)
    if strict_low:
        _require(low > domain[0], "%s must be strictly positive" % path)
    else:
        _require(low >= domain[0], "%s is below its domain" % path)
    if domain[1] is not None:
        _require(high <= domain[1], "%s exceeds its domain" % path)
    if integer:
        _require(all(x.is_integer() for x in (value, low, high)), "%s must be integral" % path)
    return (value, low, high, False)


def _meta(item, path, t, *, allow_missing=True):
    """Validate evidence metadata for a nonnumeric construct."""
    clone = dict(item)
    state = clone.get("evidence_state")
    state_id = clone.get("state_id")
    fake = {"value": None if state == "MISSING" else 1.0,
            "range": {"low": None if state == "MISSING" else 1.0,
                      "high": None if state == "MISSING" else 1.0},
            **{key: clone.get(key) for key in ("method", "evidence_state", "evidence_quality", "source_ids",
                                                "bridge_supported", "endpoints_supported",
                                                "independent_validation", "longitudinal_validation")}}
    resolved = _selection(fake, path, (0.0, 1.0), t)
    if resolved[3]:
        _require(allow_missing and state_id is None, "%s missing state requires null state_id" % path)
    else:
        _require(isinstance(state_id, str) and state_id, "%s.state_id must be nonempty" % path)
    return resolved[3]


def _clamp(value, t):
    low, high = _domain(t, "factor")
    return max(low, min(high, value))


def geometric_mean(values):
    if any(x <= 0 for x in values):
        return 0.0
    return math.prod(values) ** (1.0 / len(values))


def _ramp(resolved, t):
    missing = [x[3] for x in resolved]
    return {"low": [x[1] for x in resolved],
            "base": None if any(missing) else [x[0] for x in resolved],
            "high": [x[2] for x in resolved]}


def _raw_verdict(S, scores, t):
    if S is None or any(scores[name] is None for name in FACTOR_NAMES):
        return "indeterminate"
    for verdict in VERDICT_DESCENDING:
        if S >= t["verdict_cuts"][verdict] and min(scores.values()) >= t["verdict_min_each_factor"][verdict]:
            return verdict
    return "kill"


def _cap(verdict, cap, t):
    if verdict == "indeterminate":
        return verdict
    order = {name: index for index, name in enumerate(t["verdict_order"])}
    return verdict if order[verdict] <= order[cap] else cap


def _survival_gate(verdict, survival, t):
    gate = t["survival_gate"]
    if survival < gate["pass_cap_at_or_above"]:
        return gate["caps"]["kill"], ["constant_price_survival_below_0.25"]
    if survival < gate["conditional_cap_at_or_above"]:
        return _cap(verdict, gate["caps"]["pass"], t), ["constant_price_survival_cap:pass"]
    if survival < gate["no_cap_at_or_above"]:
        return _cap(verdict, gate["caps"]["conditional"], t), ["constant_price_survival_cap:conditional"]
    return _cap(verdict, gate["caps"]["no_cap"], t), []


def _action(verdict, t):
    return t["actions"]["uncertainty"] if verdict == "indeterminate" else t["actions"]["ordinary"][verdict]


def _readiness(record, labeled, missing_paths, denominator_missing, role_missing,
               h_base_missing, cross_tier, action_instability, t):
    config, contract = t["readiness"], t["evidence_contract"]
    target = record["inputs"]["target_archetype"]
    uncertainty = target["selection_uncertainty"]
    _require(isinstance(uncertainty, bool), "selection_uncertainty must be boolean")
    role_mix = record["inputs"]["target_role_mix"]
    basis = {
        "evidence_state": role_mix.get("basis_evidence_state"),
        "evidence_quality": role_mix.get("basis_evidence_quality"),
        "method": role_mix.get("basis_method"), "source_ids": role_mix.get("basis_source_ids"),
        "bridge_supported": role_mix.get("basis_bridge_supported", False),
        "endpoints_supported": role_mix.get("basis_endpoints_supported", False),
        "independent_validation": role_mix.get("basis_independent_validation", False),
        "longitudinal_validation": role_mix.get("basis_longitudinal_validation", False),
        "value": None if role_mix.get("basis_evidence_state") == "MISSING" else 1,
        "range": {"low": None if role_mix.get("basis_evidence_state") == "MISSING" else 1,
                  "high": None if role_mix.get("basis_evidence_state") == "MISSING" else 1},
    }
    _selection(basis, "inputs.target_role_mix.basis", (0, 1), t)
    labeled = list(labeled) + [("target_role_mix_basis", basis)]
    states = [item.get("evidence_state") for _path, item in labeled]
    qualities = [item.get("evidence_quality") for _path, item in labeled]
    unsupported_endpoint = [path for path, item in labeled if item.get("endpoints_supported") is not True]
    rationale_failed = any(item.get("rationale_separation_passed") is False for _path, item in labeled)
    status = config["statuses_in_order"][0]
    order = {name: index for index, name in enumerate(config["statuses_in_order"])}
    def worsen(candidate):
        nonlocal status
        if order[candidate] > order[status]: status = candidate
    if (missing_paths or any(x in config["unproven_states"] for x in states)
            or any(x in config["unproven_qualities"] for x in qualities)
            or denominator_missing or role_missing or h_base_missing):
        worsen("UNPROVEN")
    if uncertainty: worsen(config["selection_uncertainty_status"])
    if unsupported_endpoint: worsen(config["unsupported_endpoint_status"])
    if rationale_failed: worsen(config["failed_rationale_separation_status"])
    by_path = dict(labeled)
    for path in config["core_paths"]:
        matches = [(name, item) for name, item in labeled
                   if name == path or (path == "third_party_pass_through" and name.startswith(path + "."))
                   or (path == "target_role_mix_basis" and name.startswith("target_role_mix."))]
        if not matches: continue
        for _name, item in matches:
            if not (item.get("evidence_state") == "DIRECT"
                    and item.get("method") in contract["direct_methods"]
                    and item.get("evidence_quality") in contract["supported_qualities"]):
                worsen(config["core_not_substantiated_status"])
    forward_prefixes = tuple(config["forward_paths"])
    for path, item in labeled:
        if not any(path == prefix or path.startswith(prefix + ".") for prefix in forward_prefixes):
            continue
        if item.get("evidence_state") == "PROXY" and not (
                item.get("independent_validation") or item.get("longitudinal_validation")):
            worsen(config["supported_unvalidated_forward_proxy_status"])
    if cross_tier: worsen(config["cross_tier_status"])
    if action_instability: worsen(config["action_instability_status"])
    return {"status": status, "missing_critical_inputs": sorted(missing_paths),
            "assumption_critical_input_count": states.count("ASSUMPTION"),
            "low_quality_critical_input_count": sum(x in config["unproven_qualities"] for x in qualities),
            "selection_uncertainty": uncertainty}


def calculate(record, thresholds=None):
    t = load_thresholds() if thresholds is None else validate_thresholds(thresholds)
    _require(isinstance(record, dict) and isinstance(record.get("dataset_inputs"), dict)
             and isinstance(record.get("inputs"), dict), "record requires dataset_inputs and inputs")
    inputs = record["inputs"]
    target = inputs.get("target_archetype")
    _require(isinstance(target, dict) and isinstance(target.get("selection_uncertainty"), bool),
             "target_archetype is invalid")
    enum = target.get("enumeration_coverage")
    _require(isinstance(enum, dict) and set(enum) == {"base", "low", "high"},
             "enumeration_coverage must contain base/low/high")
    elow, ehigh = _domain(t, "enumeration_coverage")
    _require(all(_finite(enum[x]) for x in ("base", "low", "high"))
             and elow <= enum["low"] <= enum["base"] <= enum["high"] <= ehigh
             and enum["base"] >= t["archetype_selection"]["enumeration_min_coverage"],
             "enumeration coverage violates the frozen contract")

    missing_paths, labeled = set(), []
    def resolve(item, path, domain_name, **kwargs):
        value = _selection(item, "inputs." + path if not path.startswith("dataset_inputs.") else path,
                           _domain(t, domain_name), t, **kwargs)
        labeled.append((path.removeprefix("dataset_inputs."), item))
        if value[3]: missing_paths.add(path.removeprefix("dataset_inputs."))
        return value

    n_band = resolve(record["dataset_inputs"]["n_band"], "dataset_inputs.n_band", "n_band", integer=True)
    revenue = resolve(inputs["recognized_revenue"], "recognized_revenue", "nonnegative_money")
    reconciliation = inputs.get("pass_through_reconciliation")
    _require(isinstance(reconciliation, dict) and set(reconciliation) == {
        "revenue_basis", "included_cost_ids", "already_netted_cost_ids", "supported", "method",
        "evidence_state", "evidence_quality", "source_ids", "bridge_supported",
        "independent_validation", "longitudinal_validation", "rationale", "caveats"},
        "pass-through reconciliation keys are invalid")
    pass_items = inputs.get("third_party_pass_through")
    _require(isinstance(pass_items, list), "third_party_pass_through must be an array")
    pass_resolved, pass_ids = [], []
    for index, item in enumerate(pass_items):
        _require(isinstance(item, dict) and set(item) == {"category", "cost_id", "amount"},
                 "pass-through item keys are invalid")
        _require(isinstance(item["category"], str) and item["category"]
                 and isinstance(item["cost_id"], str) and item["cost_id"], "pass-through identity is invalid")
        pass_ids.append(item["cost_id"])
        pass_resolved.append(resolve(item["amount"], "third_party_pass_through.%s" % item["cost_id"],
                                     "nonnegative_money"))
    _require(len(pass_ids) == len(set(pass_ids)), "pass-through cost IDs must be unique")
    included_ids, netted_ids = reconciliation["included_cost_ids"], reconciliation["already_netted_cost_ids"]
    _require(isinstance(included_ids, list) and isinstance(netted_ids, list)
             and len(included_ids) == len(set(included_ids)) and len(netted_ids) == len(set(netted_ids))
             and not set(included_ids) & set(netted_ids)
             and set(included_ids) | set(netted_ids) == set(pass_ids),
             "pass-through reconciliation partition is invalid")
    _require(isinstance(reconciliation["supported"], bool), "reconciliation support must be boolean")
    reconciliation_meta = {
        "method": reconciliation["method"], "evidence_state": reconciliation["evidence_state"],
        "evidence_quality": reconciliation["evidence_quality"], "source_ids": reconciliation["source_ids"],
        "bridge_supported": reconciliation["bridge_supported"],
        "endpoints_supported": reconciliation["supported"],
        "independent_validation": reconciliation["independent_validation"],
        "longitudinal_validation": reconciliation["longitudinal_validation"],
    }
    labeled.append(("pass_through_reconciliation", reconciliation_meta))
    pass_by_id = dict(zip(pass_ids, pass_resolved))
    included_resolved = [pass_by_id[cost_id] for cost_id in included_ids]
    numerator_ids = inputs.get("numerator_cost_ids")
    _require(isinstance(numerator_ids, list) and all(isinstance(x, str) and x for x in numerator_ids)
             and len(numerator_ids) == len(set(numerator_ids)), "numerator_cost_ids must be unique strings")
    _require(not set(pass_ids) & set(numerator_ids), "pass-through cost cannot also appear in V numerator")
    employee = resolve(inputs["employee_cash_cost"], "employee_cash_cost", "nonnegative_money")
    contractor = resolve(inputs["controllable_contractor_cash_cost"],
                         "controllable_contractor_cash_cost", "nonnegative_money")

    role_mix = inputs.get("target_role_mix")
    _require(isinstance(role_mix, dict)
             and role_mix.get("spec_mode") in t["value_available"]["role_spec_modes"],
             "target_role_mix is invalid")
    role_missing = role_mix["spec_mode"] == "missing"
    roles = role_mix.get("roles")
    _require(isinstance(roles, list) and ((role_missing and not roles) or (not role_missing and roles)),
             "target_role_mix roles conflict with spec_mode")
    role_values, names, weights = [], [], []
    for index, role in enumerate(roles):
        _require(isinstance(role, dict) and set(role) == {"role", "cost_weight", "removable_fraction"},
                 "role keys are invalid")
        name, weight = role["role"], role["cost_weight"]
        wlow, whigh = _domain(t, "role_cost_weight")
        _require(isinstance(name, str) and name and _finite(weight) and wlow <= weight <= whigh,
                 "role identity/weight is invalid")
        names.append(name); weights.append(float(weight))
        role_values.append(resolve(role["removable_fraction"],
                                   "target_role_mix.%s.removable_fraction" % name, "removable_fraction"))
    _require(len(names) == len(set(names)), "role names must be unique")
    if not role_missing:
        _require(abs(sum(weights) - 1.0) <= t["validation_tolerances"]["role_weight_sum"],
                 "role weights must sum to one")
    if role_missing: missing_paths.add("target_role_mix")

    realization_input = inputs.get("implementation_realization")
    _require(isinstance(realization_input, dict)
             and set(realization_input) == {"r1", "r2", "r3", "r4", "r5"},
             "implementation_realization keys are invalid")
    r_resolved = [resolve(realization_input["r%d" % year],
                          "implementation_realization.r%d" % year, "implementation_realization")
                  for year in range(1, 6)]
    ramps = _ramp(r_resolved, t)
    investment_input = inputs.get("implementation_investment")
    _require(isinstance(investment_input, dict)
             and set(investment_input) == {"k0", "k1", "k2", "k3", "k4", "k5"},
             "implementation_investment keys are invalid")
    k_resolved = [resolve(investment_input["k%d" % year],
                          "implementation_investment.k%d" % year, "implementation_investment")
                  for year in range(6)]
    investments = {
        "base": None if any(x[3] for x in k_resolved) else [x[0] for x in k_resolved],
        "low": [x[2] for x in k_resolved], "high": [x[1] for x in k_resolved],
    }
    commercial_input = inputs.get("commercial_retention")
    _require(isinstance(commercial_input, dict)
             and set(commercial_input) == {"c1", "c2", "c3", "c4", "c5"},
             "commercial_retention keys are invalid")
    c_resolved = [resolve(commercial_input["c%d" % year],
                          "commercial_retention.c%d" % year, "commercial_retention") for year in range(1, 6)]
    captures = {"base": None if any(x[3] for x in c_resolved) else [x[0] for x in c_resolved],
                "low": [x[1] for x in c_resolved], "high": [x[2] for x in c_resolved]}
    commercial_scores = _commercial_support(r_resolved, ramps, captures, t)
    coverage = resolve(inputs["target_archetype_coverage"], "target_archetype_coverage", "archetype_coverage")
    sale = resolve(inputs["five_year_sale_availability"], "five_year_sale_availability", "sale_availability")
    access = resolve(inputs["buyer_access_win_share"], "buyer_access_win_share", "buyer_access_win_share")
    deal_capacity = resolve(inputs["deal_execution_capacity_5y"], "deal_execution_capacity_5y",
                            "five_year_capacity")
    integration_capacity = resolve(inputs["integration_onboarding_capacity_5y"],
                                   "integration_onboarding_capacity_5y", "five_year_capacity")
    buy = resolve(inputs["buy_mult"], "buy_mult", "buy_multiple", strict_low=True)
    exit_ = resolve(inputs["downside_exit_mult"], "downside_exit_mult", "downside_exit_multiple")
    state = inputs.get("normalized_y5_operating_state")
    _require(isinstance(state, dict), "normalized_y5_operating_state must be an object")
    state_missing = _meta(state, "inputs.normalized_y5_operating_state", t)
    if state_missing:
        missing_paths.add("normalized_y5_operating_state")
    if not state_missing:
        _require(isinstance(state.get("state_digest"), str) and len(state["state_digest"]) == 64,
                 "normalized y5 state digest must be canonical SHA-256")
    labeled.append(("normalized_y5_operating_state", state))
    linked_state = inputs["downside_exit_mult"].get("normalized_y5_state_digest")
    if not state_missing and not exit_[3]:
        _require(linked_state == state["state_digest"], "downside exit multiple must link the frozen y5 state digest")
    survival = resolve(inputs["operator_controlled_value_added_demand_share_y5"],
                       "operator_controlled_value_added_demand_share_y5", "constant_price_survival")

    denominator_missing = (revenue[3] or any(x[3] for x in included_resolved)
                           or (bool(pass_items) and not reconciliation["supported"]))
    costs_identified_zero = (not employee[3] and not contractor[3]
                             and employee[2] == 0 and contractor[2] == 0)
    removability_identified_zero = (not role_missing and all(
        weight == 0 or (not value[3] and value[2] == 0)
        for weight, value in zip(weights, role_values)))
    gross_identified_zero = costs_identified_zero or removability_identified_zero
    gross_missing = (employee[3] or contractor[3] or role_missing or any(x[3] for x in role_values))
    gross_unresolved = gross_missing and not gross_identified_zero
    if denominator_missing: missing_paths.add("R_cva")
    if gross_unresolved: missing_paths.add("G")
    if not denominator_missing:
        r_cva = {
            "base": revenue[0] - sum(x[0] for x in included_resolved),
            "low": revenue[1] - sum(x[2] for x in included_resolved),
            "high": revenue[2] - sum(x[1] for x in included_resolved),
        }
        _require(0 < r_cva["low"] <= r_cva["base"] <= r_cva["high"],
                 "R_cva must be positive, bounded, and internally consistent")
    if not employee[3] and not contractor[3]:
        total_cost = {bound: employee[INDEX[bound]] + contractor[INDEX[bound]] for bound in BOUNDS}
    else:
        total_cost = {bound: None for bound in BOUNDS}
    if not role_missing and not any(x[3] for x in role_values):
        weighted = {bound: sum(weight * value[INDEX[bound]] for weight, value in zip(weights, role_values))
                    for bound in BOUNDS}
    else:
        weighted = {bound: None for bound in BOUNDS}
    if gross_identified_zero:
        gross = {bound: 0.0 for bound in BOUNDS}
    elif not gross_unresolved:
        gross = {bound: total_cost[bound] * weighted[bound] for bound in BOUNDS}

    bundles, h_gate = {}, {}
    factor_low, factor_high = _domain(t, "factor")
    for bound in BOUNDS:
        index = INDEX[bound]
        if gross_identified_zero:
            G = V = 0.0
            denominator_bound = {"low": "high", "base": "base", "high": "low"}[bound]
            revenue_index = {"low": 2, "base": 0, "high": 1}[bound]
            pass_index = {"low": 1, "base": 0, "high": 2}[bound]
            v_sub = {"recognized_revenue": None if denominator_missing else revenue[revenue_index],
                     "included_pass_through": None if denominator_missing else
                         sum(x[pass_index] for x in included_resolved),
                     "already_netted_pass_through": None if denominator_missing else
                         sum(pass_by_id[cost_id][pass_index] for cost_id in netted_ids),
                     "R_cva": None if denominator_missing else r_cva[denominator_bound],
                     "total_cash_cost": total_cost[bound],
                     "weighted_removable_fraction": weighted[bound],
                     "G": 0.0, "g": None if denominator_missing else 0.0}
        elif denominator_missing or gross_unresolved:
            V = {"low": factor_low, "base": None, "high": factor_high}[bound]
            v_sub = {"recognized_revenue": None, "included_pass_through": None,
                     "already_netted_pass_through": None, "R_cva": None,
                     "total_cash_cost": None, "weighted_removable_fraction": None, "G": None, "g": None}
            G = None
        else:
            G = gross[bound]
            denominator_bound = {"low": "high", "base": "base", "high": "low"}[bound]
            g = G / r_cva[denominator_bound]
            V = factor_high * min(1.0, g / t["value_available"]["gross_removable_cva_anchor"])
            revenue_index = {"low": 2, "base": 0, "high": 1}[bound]
            pass_index = {"low": 1, "base": 0, "high": 2}[bound]
            v_sub = {"recognized_revenue": revenue[revenue_index],
                     "included_pass_through": sum(x[pass_index] for x in included_resolved),
                     "already_netted_pass_through": sum(pass_by_id[cost_id][pass_index]
                                                          for cost_id in netted_ids),
                     "R_cva": r_cva[denominator_bound],
                     "total_cash_cost": total_cost[bound], "weighted_removable_fraction": weighted[bound],
                     "G": G, "g": g}
        ramp, investment, capture = ramps[bound], investments[bound], captures[bound]
        if G is None:
            I = {"low": factor_low, "base": None, "high": factor_high}[bound]
        elif G == 0:
            I = t["implementation"]["zero_G_scores"]["I"]
        elif ramp is None or investment is None:
            I = None
        elif any(x is None for x in investment):
            I = factor_low
        else:
            I = _implementation_score(ramp, investment, t)
        C = commercial_scores[bound]

        opportunity_missing = n_band[3] or coverage[3] or sale[3] or access[3]
        capacity_missing = deal_capacity[3] or integration_capacity[3]
        opportunity_values = [x[index] for x in (n_band, coverage, sale, access)]
        if bound == "base" and opportunity_missing:
            opportunity = None
        elif bound == "high" and n_band[3] and all(x[2] > 0 for x in (coverage, sale, access)):
            opportunity = t["partial_identification"]["unbounded_count_token"]
        elif any(x is None for x in opportunity_values):
            opportunity = 0.0
        else:
            opportunity = math.prod(opportunity_values)
        if capacity_missing:
            if bound == "base":
                capacity = None
            elif bound == "low":
                capacity = 0.0
            else:
                known_capacity_highs = [resolved[2] for resolved in (deal_capacity, integration_capacity)
                                        if not resolved[3]]
                if opportunity == t["partial_identification"]["unbounded_count_token"]:
                    capacity = (min(known_capacity_highs) if known_capacity_highs else opportunity)
                else:
                    capacity = min([opportunity] + known_capacity_highs)
        else:
            capacity = min(deal_capacity[index], integration_capacity[index])
        if bound == "base" and (opportunity is None or capacity is None):
            B, n5 = None, None
        elif opportunity == t["partial_identification"]["unbounded_count_token"]:
            n5 = capacity if capacity is not None else opportunity
            B = factor_high if n5 == opportunity else _clamp(
                factor_high * math.log10(1 + n5) / math.log10(1 + t["buyability"]["n5_full_score"]), t)
        else:
            n5 = min(opportunity, capacity) if capacity is not None else opportunity
            B = _clamp(factor_high * math.log10(1 + n5) /
                       math.log10(1 + t["buyability"]["n5_full_score"]), t)
        b_sub = {"n_band": None if n_band[3] else n_band[index],
                 "coverage": None if bound == "base" and coverage[3] else coverage[index],
                 "sale_availability": None if bound == "base" and sale[3] else sale[index],
                 "buyer_access_win_share": None if bound == "base" and access[3] else access[index],
                 "deal_execution_capacity_5y": None if bound == "base" and deal_capacity[3] else deal_capacity[index],
                 "integration_onboarding_capacity_5y": None if bound == "base" and integration_capacity[3] else integration_capacity[index],
                 "O5": opportunity, "K5": capacity, "N5": n5}

        p_missing = buy[3] or exit_[3] or state_missing
        if bound == "base" and p_missing:
            P = None; entry = resilience = None; buy_value = exit_value = None
        elif p_missing:
            buy_value = None if buy[3] else (buy[2] if bound == "low" else buy[1])
            entry = None if buy_value is None else _clamp(
                t["price_discipline"]["entry_reference_multiple"] - buy_value, t)
            exit_value = None if exit_[3] else (exit_[1] if bound == "low" else exit_[2])
            resilience = None
            if bound == "high" and buy[3] and exit_value == 0:
                resilience = 0.0
                P = 0.0
            else:
                P = factor_low if bound == "low" else (entry if entry is not None else factor_high)
        else:
            buy_value = buy[2] if bound == "low" else buy[1] if bound == "high" else buy[0]
            exit_value = exit_[1] if bound == "low" else exit_[2] if bound == "high" else exit_[0]
            pc = t["price_discipline"]
            entry = _clamp(pc["entry_reference_multiple"] - buy_value, t)
            resilience = _clamp(pc["downside_ratio_slope"] *
                                (exit_value / buy_value - pc["downside_ratio_floor"]), t)
            P = min(entry, resilience)
        p_sub = {"buy_mult": buy_value, "downside_exit_mult": exit_value,
                 "normalized_y5_state_digest": None if state_missing else state["state_digest"],
                 "entry_score": entry, "resilience_score": resilience}

        h_unknown = G is None or ramp is None or investment is None or capture is None
        if h_unknown:
            h = None
            gate_triggered = None if bound == "base" else bound == "low"
            retained = invested = None
        elif any(x is None for x in investment):
            h = None; gate_triggered = True
            retained = sum(a * b * w for a, b, w in zip(ramp, capture, _weights(t))); invested = None
        elif G == 0:
            h = 0.0; gate_triggered = True; retained = invested = 0.0
        else:
            retained = sum(a * b * w for a, b, w in zip(ramp, capture, _weights(t)))
            invested = investment[0] + sum(a * w for a, w in zip(investment[1:], _weights(t)))
            h = retained - invested
            gate_triggered = h <= t["viability_gate"]["kill_threshold"]
        h_gate[bound] = gate_triggered
        scores = {"V": V, "I": I, "C": C, "B": B, "P": P}
        S = None if any(x is None for x in scores.values()) else geometric_mean(scores.values())
        bundles[bound] = {"scores": scores, "S": S,
                          "subfactors": {"V": v_sub, "implementation_realization": ramp,
                                         "implementation_investment": investment,
                                         "commercial_retention": capture, "B": b_sub, "P": p_sub,
                                         "h": {"discounted_retained_realization": retained,
                                               "discounted_investment": invested, "h": h,
                                               "gate_triggered": gate_triggered}}}

    tolerance = t["validation_tolerances"]["numeric"]
    for factor in FACTOR_NAMES:
        low, base, high = (bundles[bound]["scores"][factor] for bound in BOUNDS)
        _require(_finite(low) and _finite(high) and factor_low <= low <= high <= factor_high,
                 "factor %s support must be finite and ordered" % factor)
        if base is not None:
            _require(low <= base + tolerance <= high + tolerance,
                     "factor %s base is outside support" % factor)
    if bundles["base"]["S"] is not None:
        _require(bundles["low"]["S"] <= bundles["base"]["S"] + tolerance
                 <= bundles["high"]["S"] + tolerance, "aggregate base is outside support")
    low_h = bundles["low"]["subfactors"]["h"]["h"]
    base_h = bundles["base"]["subfactors"]["h"]["h"]
    high_h = bundles["high"]["subfactors"]["h"]["h"]
    if all(value is not None for value in (low_h, base_h, high_h)):
        _require(low_h <= base_h + tolerance <= high_h + tolerance, "h support must be ordered")

    raw = {bound: _raw_verdict(bundles[bound]["S"], bundles[bound]["scores"], t) for bound in BOUNDS}
    realizations = _realization_vertices(r_resolved)
    joint_low = _joint_decision_endpoint(
        realizations, captures["low"], investments["low"],
        {name: bundles["low"]["scores"][name] for name in ("V", "B", "P")},
        survival[1], t, best=False)
    joint_high = _joint_decision_endpoint(
        realizations, captures["high"], investments["high"],
        {name: bundles["high"]["scores"][name] for name in ("V", "B", "P")},
        survival[2], t, best=True)
    scenario = {
        "low": {"verdict": joint_low[0], "reasons": joint_low[1], "survival": survival[1]},
        "high": {"verdict": joint_high[0], "reasons": joint_high[1], "survival": survival[2]},
    }
    endpoints_same = scenario["low"]["verdict"] == scenario["high"]["verdict"]
    economic = scenario["low"]["verdict"] if endpoints_same else t["partial_identification"]["different_verdict"]
    base_reasons = []
    if not missing_paths and h_gate["base"] is not None:
        base_verdict = raw["base"]
        if h_gate["base"]: base_verdict = "kill"; base_reasons.append("operating_value_viability_h_le_0")
        _base, sr = _survival_gate(base_verdict, survival[0], t); base_reasons += sr
    else:
        base_reasons = sorted(set(scenario["low"]["reasons"]) & set(scenario["high"]["reasons"]))
    low_action, high_action = _action(scenario["low"]["verdict"], t), _action(scenario["high"]["verdict"], t)
    cross_tier = not endpoints_same; action_instability = low_action != high_action
    readiness = _readiness(record, labeled, missing_paths, denominator_missing, role_missing,
                           h_gate["base"] is None, cross_tier, action_instability, t)
    stable_kill = scenario["high"]["verdict"] == "kill"
    if stable_kill: action = t["actions"]["stable_structural_kill"]
    elif economic == "indeterminate" or action_instability or readiness["status"] == "UNPROVEN":
        action = t["actions"]["uncertainty"]
    else: action = _action(economic, t)
    decision = {"raw_verdict": raw["base"], "economic_verdict": economic, "gate_reasons": base_reasons,
                "evidence_readiness": readiness, "action": action,
                "sensitivity": {"low_verdict": scenario["low"]["verdict"],
                                "high_verdict": scenario["high"]["verdict"],
                                "low_h": bundles["low"]["subfactors"]["h"]["h"],
                                "high_h": bundles["high"]["subfactors"]["h"]["h"],
                                "low_h_gate_triggered": h_gate["low"],
                                "high_h_gate_triggered": h_gate["high"],
                                "low_constant_price_survival": scenario["low"]["survival"],
                                "high_constant_price_survival": scenario["high"]["survival"],
                                "cross_tier": cross_tier, "action_instability": action_instability,
                                "stable_structural_kill": stable_kill}}
    return {"low": bundles["low"], "base": bundles["base"], "high": bundles["high"], "decision": decision}
