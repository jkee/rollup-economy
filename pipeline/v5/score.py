#!/usr/bin/env python3
"""Deterministic v5 Stage 1 scoring.

Ported from the verified v4.3 minimal scorer. Owns only arithmetic:
H/F/C/D factor formulas, the A/L pair, tier cuts, the finite 3^4 factor
envelope, and the readiness/action mapping. Anchors and tier cuts are read
from the adjacent thresholds.json so there is one source of truth.

Evidence states are the four v5 states: OBSERVED, PROXY, ESTIMATE, MISSING.
"""

from __future__ import annotations

import json
from decimal import Context, Decimal, ROUND_HALF_EVEN, localcontext
from itertools import product
from pathlib import Path

_THRESHOLDS = json.loads((Path(__file__).resolve().parent / "thresholds.json").read_text(encoding="utf-8"))

CTX = Context(prec=50, rounding=ROUND_HALF_EVEN)
Q = Decimal(_THRESHOLDS["quantum"])
H_ANCHOR = Decimal(_THRESHOLDS["anchors"]["H_receipts_share"])
F_ANCHOR = Decimal(_THRESHOLDS["anchors"]["F_expected_transfers"])
C_ANCHOR = Decimal(_THRESHOLDS["anchors"]["C_retention_share"])
TIER_CUTS = [(row["tier"], Decimal(row["A"]), Decimal(row["L"])) for row in _THRESHOLDS["tier_cuts"]]

FACTOR_NAMES = ("H", "F", "C", "D")
EVIDENCE_STATES = ("OBSERVED", "PROXY", "ESTIMATE", "MISSING")
TIER_ORDER = {
    "STRUCTURAL_OUT": 0,
    "LOW_PRIORITY": 1,
    "CONDITIONAL": 2,
    "PRIORITY": 3,
    "HIGHEST_PRIORITY": 4,
}


def dec(value) -> Decimal:
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def quantize(value: Decimal) -> Decimal:
    with localcontext(CTX):
        return value.quantize(Q, rounding=ROUND_HALF_EVEN)


def clamp(value: Decimal, low: Decimal, high: Decimal) -> Decimal:
    return min(high, max(low, value))


def h_score(labor_share, task_share, implementation) -> Decimal:
    with localcontext(CTX):
        raw = dec(labor_share) * dec(task_share) * dec(implementation)
        return quantize(Decimal(10) * min(Decimal(1), raw / H_ANCHOR))


def f_score(firm_count, eligible_share, transfer_probability) -> Decimal:
    with localcontext(CTX):
        expected = dec(firm_count) * dec(eligible_share) * dec(transfer_probability)
        if expected < 0:
            raise ValueError("expected transfers cannot be negative")
        value = (Decimal(1) + expected).log10(context=CTX) / (Decimal(1) + F_ANCHOR).log10(context=CTX)
        return quantize(Decimal(10) * clamp(value, Decimal(0), Decimal(1)))


def c_score(retention_share) -> Decimal:
    with localcontext(CTX):
        return quantize(Decimal(10) * min(Decimal(1), dec(retention_share) / C_ANCHOR))


def d_score(demand_ratio, operator_share) -> Decimal:
    with localcontext(CTX):
        return quantize(Decimal(10) * clamp(dec(demand_ratio) * dec(operator_share), Decimal(0), Decimal(1)))


def tier_for(A: Decimal, L: Decimal) -> str:
    for tier, a_cut, l_cut in TIER_CUTS:
        if tier == "STRUCTURAL_OUT":
            return tier
        if A >= a_cut and L >= l_cut:
            return tier
    return "STRUCTURAL_OUT"


def aggregate(factors: dict[str, Decimal]) -> dict:
    missing = [name for name in FACTOR_NAMES if factors.get(name) is None]
    if missing:
        raise ValueError("aggregate requires complete factors: %s" % missing)
    with localcontext(CTX):
        A = quantize(sum((factors[name] for name in FACTOR_NAMES), Decimal(0)) / Decimal(4))
        L = quantize(min(factors[name] for name in FACTOR_NAMES))
    return {"A": A, "L": L, "tier": tier_for(A, L)}


def scenario_envelope(factor_ranges: dict[str, dict]) -> dict:
    """Enumerate the closed 3^4 factor state set; missing factors span [0, 10]."""
    missing = [name for name in FACTOR_NAMES if factor_ranges[name]["base"] is None]
    state_values = {}
    for name in FACTOR_NAMES:
        if name in missing:
            state_values[name] = (("semantic_low", Decimal(0)), ("semantic_high", Decimal(10)))
        else:
            state_values[name] = tuple(
                (label, dec(factor_ranges[name][label])) for label in ("low", "base", "high")
            )

    states = []
    for combination in product(*(state_values[name] for name in FACTOR_NAMES)):
        labels = {name: pair[0] for name, pair in zip(FACTOR_NAMES, combination)}
        factors = {name: pair[1] for name, pair in zip(FACTOR_NAMES, combination)}
        result = aggregate(factors)
        state_id = "|".join("%s:%s" % (name, labels[name]) for name in FACTOR_NAMES)
        states.append({"state_id": state_id, "factors": factors, **result})

    def key(state):
        return (TIER_ORDER[state["tier"]], state["A"], state["L"], state["state_id"])

    low = min(states, key=key)
    high = max(states, key=key)
    tiers = sorted({state["tier"] for state in states}, key=TIER_ORDER.get)
    base = None
    if not missing:
        base_factors = {name: dec(factor_ranges[name]["base"]) for name in FACTOR_NAMES}
        base = {"state_id": "|".join("%s:base" % name for name in FACTOR_NAMES),
                "factors": base_factors, **aggregate(base_factors)}
    return {
        "missing_factors": missing,
        "state_count": len(states),
        "base": base,
        "low": low,
        "high": high,
        "attainable_tiers": tiers,
        "tier_interval": [tiers[0], tiers[-1]],
        "robust_tier": tiers[0] if len(tiers) == 1 else None,
    }


def readiness_and_action(evidence_states: list[str], envelope: dict) -> tuple[str, str]:
    unknown = set(evidence_states) - set(EVIDENCE_STATES)
    if unknown:
        raise ValueError("unknown evidence states: %s" % sorted(unknown))
    if envelope["missing_factors"]:
        return "STRESS_TEST_ONLY", "EVIDENCE_FIRST"
    if "ESTIMATE" in evidence_states:
        return "MODEL_CONDITIONED", "VALIDATE_ASSUMPTIONS"
    readiness = "PROVISIONAL" if "PROXY" in evidence_states else "SUBSTANTIATED"

    tiers = set(envelope["attainable_tiers"])
    if tiers <= {"HIGHEST_PRIORITY", "PRIORITY"}:
        return readiness, "ADVANCE_TO_STAGE2"
    if "CONDITIONAL" in tiers or ({"HIGHEST_PRIORITY", "PRIORITY"} & tiers and
                                  {"LOW_PRIORITY", "STRUCTURAL_OUT"} & tiers):
        return readiness, "SELECTIVE_VALIDATE"
    if readiness == "SUBSTANTIATED":
        return readiness, "DEPRIORITIZE"
    return readiness, "SELECTIVE_VALIDATE"


def json_decimal(value):
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, dict):
        return {key: json_decimal(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_decimal(item) for item in value]
    return value
