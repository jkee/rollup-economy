#!/usr/bin/env python3
"""Frozen v4.0 scoring, sensitivity, readiness, and decision functions.

This module is deterministic and stdlib-only. It performs no model or web
calls and owns every score derived from a model-authored v4 packet.
"""

import json
import math
import os


HERE = os.path.dirname(os.path.abspath(__file__))
FACTOR_NAMES = ("V", "C", "A", "B", "M")
READINESS_CRITICAL = (
    "ai_replaceable_share",
    "target_archetype.coverage",
    "retained_savings_share_24m",
    "t50_years",
    "seller_supply_signal",
    "active_consolidators",
    "buy_mult",
    "exit_mult",
    "operator_survival",
)
VERDICT_ORDER = {"kill": 0, "pass": 1, "conditional": 2, "strong": 3, "hell_yes": 4}
SURVIVAL_ORDER = {"MELTING": 0, "DISINTERMEDIATED": 1, "PRESSURED": 2, "DURABLE": 3}


def load_thresholds(path=None):
    path = path or os.path.join(HERE, "thresholds_v4.json")
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def clamp(value, low, high):
    return max(low, min(high, value))


def geometric_mean(values):
    if any(value <= 0 for value in values):
        return 0.0
    return math.prod(values) ** (1.0 / len(values))


def _selection(record, path):
    value = record
    for part in path.split("."):
        value = value[part]
    return value


def _resolved_numeric(selection, default):
    """Return base/low/high, applying preregistered neutral missing defaults."""
    if selection.get("evidence_state") == "MISSING":
        return float(default["value"]), float(default["low"]), float(default["high"])
    value = float(selection["value"])
    numeric_range = selection["range"]
    return value, float(numeric_range["low"]), float(numeric_range["high"])


def m_score(spread, anchors):
    if spread <= anchors[0][0]:
        return float(anchors[0][1])
    if spread >= anchors[-1][0]:
        return float(anchors[-1][1])
    for (x0, y0), (x1, y1) in zip(anchors, anchors[1:]):
        if x0 <= spread <= x1:
            weight = (spread - x0) / (x1 - x0)
            return float(y0 + weight * (y1 - y0))
    raise AssertionError("spread was not bracketed by frozen M anchors")


def adoption_score(t50_years):
    return 10.0 / (1.0 + float(t50_years) / 3.0)


def target_density_score(n_effective):
    return 10.0 * clamp(math.log10(max(1.0, float(n_effective))) / 4.0, 0.0, 1.0)


def seller_adjustment(signal):
    return {"EXCESS": 1.0, "NORMAL": 0.0, "UNKNOWN": 0.0, "SCARCE": -1.0}[signal]


def competition_penalty(active_consolidators):
    return min(2.0, math.log10(1.0 + max(0.0, float(active_consolidators))))


def _role_v(record, bound):
    labor_share = float(record["dataset_inputs"]["labor_share"]["value"])
    replaceable = 0.0
    for role in record["inputs"]["ai_replaceable_share"]["breakdown_by_role"]:
        fraction = role["within_role_automatable_fraction"] if bound == "base" else role["range"][bound]
        replaceable += float(role["labor_share_of_total"]) * float(fraction)
    raw = labor_share * replaceable
    return 10.0 * min(1.0, raw / 0.25), raw, replaceable


def _score_bundle(record, thresholds, bound):
    defaults = thresholds["missing_defaults"]
    V, v_raw, replaceable = _role_v(record, bound)

    c_sel = record["inputs"]["retained_savings_share_24m"]
    c_base, c_low, c_high = _resolved_numeric(c_sel, defaults["retained_savings_share_24m"])
    retained = {"base": c_base, "low": c_low, "high": c_high}[bound]
    C = 10.0 * retained

    a_sel = record["inputs"]["t50_years"]
    a_base, a_low, a_high = _resolved_numeric(a_sel, defaults["t50_years"])
    # More years is economically worse, so pessimistic score uses range.high.
    t50 = {"base": a_base, "low": a_high, "high": a_low}[bound]
    A = adoption_score(t50)

    coverage_sel = record["inputs"]["target_archetype"]["coverage"]
    cov_base, cov_low, cov_high = _resolved_numeric(coverage_sel, defaults["target_archetype_coverage"])
    coverage = {"base": cov_base, "low": cov_low, "high": cov_high}[bound]
    n_band = float(record["dataset_inputs"]["n_band"]["value"])
    n_effective = n_band * coverage
    TD = target_density_score(n_effective)

    seller = record["inputs"]["seller_supply_signal"]
    seller_base = seller["value"]
    if bound == "base":
        seller_signal = seller_base
    else:
        plausible = seller.get("plausible_values") or [seller_base]
        adjustments = [(seller_adjustment(item), item) for item in plausible]
        seller_signal = (min if bound == "low" else max)(adjustments)[1]

    con_sel = record["inputs"]["active_consolidators"]
    con_base, con_low, con_high = _resolved_numeric(con_sel, defaults["active_consolidators"])
    consolidators = {"base": con_base, "low": con_high, "high": con_low}[bound]
    B = clamp(TD + seller_adjustment(seller_signal) - competition_penalty(consolidators), 0.0, 10.0)

    buy_sel, exit_sel = record["inputs"]["buy_mult"], record["inputs"]["exit_mult"]
    if buy_sel.get("evidence_state") == "MISSING" or exit_sel.get("evidence_state") == "MISSING":
        M = float(defaults["M"][bound if bound != "base" else "value"])
        buy = exit_ = None
        spread = None
    else:
        buy_base, buy_low, buy_high = _resolved_numeric(buy_sel, {"value": 1, "low": 1, "high": 1})
        exit_base, exit_low, exit_high = _resolved_numeric(exit_sel, {"value": 1, "low": 1, "high": 1})
        buy = {"base": buy_base, "low": buy_high, "high": buy_low}[bound]
        exit_ = {"base": exit_base, "low": exit_low, "high": exit_high}[bound]
        spread = exit_ / buy - 1.0
        M = m_score(spread, thresholds["m_anchors"])

    scores = {"V": V, "C": C, "A": A, "B": B, "M": M}
    return {
        "scores": scores,
        "S": geometric_mean(scores.values()),
        "subfactors": {
            "V_raw": v_raw,
            "ai_replaceable_share": replaceable,
            "retained_savings_share_24m": retained,
            "t50_years": t50,
            "target_archetype_coverage": coverage,
            "n_effective": n_effective,
            "TD": TD,
            "seller_supply_signal": seller_signal,
            "active_consolidators": consolidators,
            "competition_penalty": competition_penalty(consolidators),
            "buy_mult": buy,
            "exit_mult": exit_,
            "multiple_spread": spread,
        },
    }


def evidence_readiness(record):
    selections = {
        "ai_replaceable_share": record["inputs"]["ai_replaceable_share"],
        "target_archetype.coverage": record["inputs"]["target_archetype"]["coverage"],
        "retained_savings_share_24m": record["inputs"]["retained_savings_share_24m"],
        "t50_years": record["inputs"]["t50_years"],
        "seller_supply_signal": record["inputs"]["seller_supply_signal"],
        "active_consolidators": record["inputs"]["active_consolidators"],
        "buy_mult": record["inputs"]["buy_mult"],
        "exit_mult": record["inputs"]["exit_mult"],
        "operator_survival": record["inputs"]["operator_survival"],
    }
    missing = sorted(name for name, selection in selections.items() if selection["evidence_state"] == "MISSING")
    operator_assumption = selections["operator_survival"]["evidence_state"] == "ASSUMPTION"
    assumptions = sorted(name for name, selection in selections.items() if selection["evidence_state"] == "ASSUMPTION")
    low_quality = sorted(name for name, selection in selections.items() if selection["evidence_quality"] in ("LOW", "NONE"))
    if missing or operator_assumption:
        readiness = "UNPROVEN"
    elif assumptions or len(low_quality) >= 2:
        readiness = "PROVISIONAL"
    else:
        readiness = "SUBSTANTIATED"
    return {
        "status": readiness,
        "missing_critical_inputs": missing,
        "assumption_critical_inputs": assumptions,
        "low_quality_critical_inputs": low_quality,
    }


def _raw_verdict(S, scores, thresholds):
    cuts = thresholds["verdict_cuts"]
    if S >= cuts["hell_yes"] and min(scores.values()) >= thresholds["hell_yes_min_each_factor"]:
        return "hell_yes"
    if S >= cuts["strong"]:
        return "strong"
    if S >= cuts["conditional"]:
        return "conditional"
    if S >= cuts["pass"]:
        return "pass"
    return "kill"


def _cap_verdict(verdict, cap):
    return verdict if VERDICT_ORDER[verdict] <= VERDICT_ORDER[cap] else cap


def _survival_scenario(selection, bound):
    values = selection.get("plausible_values") or [selection["value"]]
    chooser = min if bound == "low" else max
    return chooser(values, key=lambda value: SURVIVAL_ORDER[value])


def _scenario_verdict(record, bundle, survival, thresholds):
    verdict = _cap_verdict(
        _raw_verdict(bundle["S"], bundle["scores"], thresholds),
        thresholds["operator_survival_caps"][survival],
    )
    if survival == "MELTING":
        return "kill"
    coverage = record["inputs"]["target_archetype"]["coverage"]
    deterministic_zero_targets = (
        float(record["dataset_inputs"]["n_band"]["value"]) == 0
        or (coverage["evidence_state"] == "DIRECT" and float(coverage["value"]) == 0)
    )
    if deterministic_zero_targets:
        return "kill"
    if thresholds["hard_floor"]["requires_direct_evidence"]:
        c_direct = record["inputs"]["retained_savings_share_24m"]["evidence_state"] == "DIRECT"
        m_direct = all(record["inputs"][name]["evidence_state"] == "DIRECT" for name in ("buy_mult", "exit_mult"))
        if ((c_direct and bundle["scores"]["C"] < thresholds["hard_floor"]["C"])
                or (m_direct and bundle["scores"]["M"] < thresholds["hard_floor"]["M"])):
            return "kill"
    return verdict


def decide(record, base_bundle, low_bundle, high_bundle, thresholds):
    scores, S = base_bundle["scores"], base_bundle["S"]
    raw = _raw_verdict(S, scores, thresholds)
    survival = record["inputs"]["operator_survival"]["value"]
    verdict = _cap_verdict(raw, thresholds["operator_survival_caps"][survival])
    gate_reasons = []

    if survival == "MELTING":
        verdict = "kill"
        gate_reasons.append("operator_survival:MELTING")

    coverage = record["inputs"]["target_archetype"]["coverage"]
    deterministic_zero_targets = (
        float(record["dataset_inputs"]["n_band"]["value"]) == 0
        or (coverage["evidence_state"] == "DIRECT" and float(coverage["value"]) == 0)
    )
    if deterministic_zero_targets:
        verdict = "kill"
        gate_reasons.append("deterministic_target_absence")

    if thresholds["hard_floor"]["requires_direct_evidence"]:
        for factor, input_name in (("C", "retained_savings_share_24m"), ("M", None)):
            if factor == "C":
                direct = record["inputs"][input_name]["evidence_state"] == "DIRECT"
            else:
                direct = all(record["inputs"][name]["evidence_state"] == "DIRECT" for name in ("buy_mult", "exit_mult"))
            if direct and scores[factor] < thresholds["hard_floor"][factor]:
                verdict = "kill"
                gate_reasons.append("direct_%s_below_floor" % factor)

    readiness = evidence_readiness(record)
    if verdict in ("hell_yes", "strong"):
        action = "EVIDENCE_FIRST" if readiness["status"] == "UNPROVEN" else "DEEP_DIVE"
    elif verdict == "conditional":
        action = "SELECTIVE"
    elif verdict == "pass":
        action = "DEPRIORITIZE"
    else:
        action = "AVOID"

    survival_selection = record["inputs"]["operator_survival"]
    low_survival = _survival_scenario(survival_selection, "low")
    high_survival = _survival_scenario(survival_selection, "high")
    low_verdict = _scenario_verdict(record, low_bundle, low_survival, thresholds)
    high_verdict = _scenario_verdict(record, high_bundle, high_survival, thresholds)

    return {
        "raw_verdict": raw,
        "economic_verdict": verdict,
        "operator_survival": survival,
        "gate_reasons": gate_reasons,
        "evidence_readiness": readiness,
        "action": action,
        "sensitivity": {
            "low_verdict": low_verdict,
            "high_verdict": high_verdict,
            "low_operator_survival": low_survival,
            "high_operator_survival": high_survival,
            "cross_tier": low_verdict != high_verdict,
        },
    }


def calculate(record, thresholds=None):
    thresholds = thresholds or load_thresholds()
    low = _score_bundle(record, thresholds, "low")
    base = _score_bundle(record, thresholds, "base")
    high = _score_bundle(record, thresholds, "high")
    for name in FACTOR_NAMES:
        if low["scores"][name] > base["scores"][name] + 1e-12 or base["scores"][name] > high["scores"][name] + 1e-12:
            raise ValueError("non-monotonic %s sensitivity: low=%s base=%s high=%s" % (
                name, low["scores"][name], base["scores"][name], high["scores"][name]))
    if low["S"] > base["S"] + 1e-12 or base["S"] > high["S"] + 1e-12:
        raise ValueError("non-monotonic S sensitivity")
    decision = decide(record, base, low, high, thresholds)
    return {"low": low, "base": base, "high": high, "decision": decision}
