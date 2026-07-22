#!/usr/bin/env python3
"""Adapt reviewed v3 Phase 4 evidence into separate v4.3 Stage 1 outputs."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

from v4_3_minimal_scoring import (
    c_score, clamp, d_score, dec, f_score, h_score, json_decimal,
    readiness_and_action, scenario_envelope, TIER_ORDER,
)


ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / "pipeline" / "build"
TARGETS = ROOT / "pipeline" / "blocks" / "targets_phase3.json"
V3_DATA = ROOT / "6digit" / "six_data_v3.json"
CONFIG_PATH = BUILD / "thresholds_v4_3_minimal.json"
OUT_ROOT = ROOT / "pipeline" / "v4_3"
SITE_OUT = ROOT / "6digit" / "six_data_v4.json"
CANARIES = ("238220", "541214", "541511", "541512", "541930")
RANGE_RE = re.compile(r"(?<![A-Za-z])(-?\d+(?:\.\d+)?)\s*(?:%|x|×)?\s*(?:-|–|to)\s*(-?\d+(?:\.\d+)?)\s*%?", re.I)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def numeric_range(selection: dict, *, lower=0, upper=None) -> tuple[float, float, float]:
    value = selection.get("value")
    if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
        raise ValueError("selection has no finite numeric value")
    match = RANGE_RE.search(str(selection.get("plausible_range", "")))
    if match:
        low, high = map(float, match.groups())
        if "%" in match.group(0) and max(abs(low), abs(high)) > 1:
            low, high = low / 100, high / 100
    else:
        width = max(abs(float(value)) * 0.25, 0.05)
        low, high = float(value) - width, float(value) + width
    low, high = min(low, high), max(low, high)
    low = max(lower, low)
    if upper is not None:
        high = min(upper, high)
    return low, float(value), high


def ai_range(selection: dict) -> tuple[float, float, float]:
    roles = selection.get("breakdown_by_role", [])
    if not roles:
        return numeric_range(selection, lower=0, upper=1)
    lows, highs = 0.0, 0.0
    for role in roles:
        match = RANGE_RE.search(str(role.get("plausible_range", "")))
        base = float(role["within_role_automatable_fraction"])
        low, high = (map(float, match.groups()) if match else (base * 0.75, min(1, base * 1.25)))
        weight = float(role["labor_share_of_total"])
        lows += weight * max(0, min(low, high))
        highs += weight * min(1, max(low, high))
    return max(0, lows), float(selection["value"]), min(1, highs)


def implementation_range(t50: dict, bridge_error: float) -> tuple[float, float, float]:
    low_t, base_t, high_t = numeric_range(t50, lower=0)

    def transform(years):
        return max(0.25, min(0.85, 0.85 - 0.07 * years))

    return max(0.25, transform(high_t) - bridge_error), transform(base_t), min(0.85, transform(low_t) + bridge_error)


def _source_state(selection: dict) -> str:
    if selection.get("value") is None:
        return "MISSING"
    method = selection.get("method")
    if method in ("OBSERVED", "CALCULATED") and selection.get("source_ids"):
        return "BRIDGED_PROXY"
    return "ELICITED_ASSUMPTION"


def _dataset_missing(name: str, selection: dict, naics: str) -> bool:
    value = selection.get("value")
    text = " ".join(str(selection.get(key, "")) for key in ("method", "derivation", "source"))
    if value is None:
        return True
    return naics == "541120" and name in ("labor_share", "n_band") and float(value) == 0 or (
        float(value) == 0 and re.search(r"no (?:direct )?(?:series|data)|gap|missing", text, re.I) is not None
    )


def raw_record_for_exclusion(naics: str, run_id: str, exclusion: dict) -> dict:
    raw = load_json(ROOT / "pipeline" / "runs" / naics / (run_id + ".json"))
    return {
        "naics": naics,
        "title": raw["title"],
        "sector": {"code": naics[:2], "name": "Professional Services" if naics.startswith("54") else "Phase 4"},
        "S": raw["S"],
        "verdict": raw["decision"]["verdict"],
        "confidence": raw["confidence_overall"],
        "terminal_value": raw["cross_checks"]["terminal_value"]["class"],
        "heterogeneous": raw["heterogeneous"],
        "run_meta": raw["run_meta"],
        "scores": {key: value["score"] for key, value in raw["scores"].items()},
        "evidence": {"dataset_inputs": raw["dataset_inputs"], "inputs": raw["inputs"]},
        "sources": raw["sources"],
        "publication_caveats": [],
        "source_review": {
            "outcome": exclusion.get("outcome"),
            "summary": exclusion.get("summary"),
            "material_findings": [
                {"category": item.get("category"), "materiality": item.get("materiality")}
                for item in exclusion.get("findings", []) if item.get("severity") == "material"
            ],
        },
    }


def v3_records() -> dict[str, dict]:
    data = load_json(V3_DATA)
    records = {record["naics"]: record for record in data["records"]}
    for record in records.values():
        record["source_review"] = record.get("acceptance", {}).get("review", {})
    campaign = load_json(BUILD / "campaign_report_v3_1_2.json")
    for exclusion in campaign.get("exclusions", []):
        records[exclusion["naics"]] = raw_record_for_exclusion(exclusion["naics"], exclusion["run_id"], exclusion)
    return records


def factor_record(v3: dict, config: dict) -> dict:
    naics = v3["naics"]
    inputs = v3["evidence"]["inputs"]
    datasets = v3["evidence"]["dataset_inputs"]
    adapter = config["adapters"]

    evidence = {}
    factor_ranges = {}

    labor = datasets["labor_share"]
    labor_missing = _dataset_missing("labor_share", labor, naics)
    if labor_missing:
        factor_ranges["H"] = {"low": None, "base": None, "high": None}
        evidence["H"] = {"state": "missing", "leaves": {"l": {"state": "MISSING", "value": None}}}
    else:
        l = float(labor["value"])
        a_low, a_base, a_high = ai_range(inputs["ai_replaceable_share"])
        rho_low, rho_base, rho_high = implementation_range(
            inputs["t50_years"], float(adapter["implementation_haircut"]["bridge_error"])
        )
        factor_ranges["H"] = {
            "low": h_score(l, a_low, rho_low), "base": h_score(l, a_base, rho_base),
            "high": h_score(l, a_high, rho_high),
        }
        evidence["H"] = {
            "state": "mixed",
            "leaves": {
                "l": {"state": "DIRECT_INDUSTRY", "value": l, "quality": labor.get("quality"), "detail": labor.get("method")},
                "a": {"state": _source_state(inputs["ai_replaceable_share"]), "low": a_low, "value": a_base, "high": a_high,
                      "rationale": inputs["ai_replaceable_share"].get("rationale"), "source_ids": inputs["ai_replaceable_share"].get("source_ids", [])},
                "rho": {"state": "BRIDGED_PROXY", "low": rho_low, "value": rho_base, "high": rho_high,
                        "rationale": "Fixed outcome-blind transform of the v3 t50 adoption estimate, widened by the declared bridge error.",
                        "source_ids": inputs["t50_years"].get("source_ids", [])},
            },
        }

    n_sel = datasets["n_band"]
    n_missing = _dataset_missing("n_band", n_sel, naics)
    if n_missing:
        factor_ranges["F"] = {"low": None, "base": None, "high": None}
        evidence["F"] = {"state": "missing", "leaves": {"n": {"state": "MISSING", "value": None}}}
    else:
        n = float(n_sel["value"])
        lens_key = "heterogeneous" if v3.get("heterogeneous") else "ordinary"
        e = {key: float(value) for key, value in adapter["lens_eligibility"][lens_key].items()}
        owner_low, owner_base, owner_high = numeric_range(inputs["owners_60plus_pct"], lower=0, upper=1)
        s5 = {
            "low": max(0.05, min(0.45, 0.05 + 0.20 * owner_low)),
            "base": max(0.05, min(0.45, 0.08 + 0.30 * owner_base)),
            "high": max(0.05, min(0.45, 0.12 + 0.40 * owner_high)),
        }
        factor_ranges["F"] = {key: f_score(n, e[key], s5[key]) for key in ("low", "base", "high")}
        evidence["F"] = {
            "state": "mixed",
            "leaves": {
                "n": {"state": "BRIDGED_PROXY", "value": n, "quality": n_sel.get("quality"), "detail": n_sel.get("derivation")},
                "e": {"state": "ELICITED_ASSUMPTION", **e,
                      "rationale": "Global eligible-union share; heterogeneous records use the predeclared wider/lower class-count row."},
                "s5": {"state": "BRIDGED_PROXY", **s5, "rationale": "Fixed transform of the disclosed v3 owner-age range into five-year qualifying control-transfer propensity.",
                       "source_ids": inputs["owners_60plus_pct"].get("source_ids", [])},
            },
        }

    dist = inputs["pi_dist"]
    moat = inputs["pi_moat"]
    if dist.get("value") is None or moat.get("value") is None:
        factor_ranges["C"] = {"low": None, "base": None, "high": None}
        evidence["C"] = {"state": "missing", "leaves": {"q": {"state": "MISSING", "value": None}}}
    else:
        dl, db, dh = numeric_range(dist, lower=0, upper=1)
        ml, mb, mh = numeric_range(moat, lower=0, upper=1)
        q = {"low": dl * ml, "base": db * mb, "high": dh * mh}
        factor_ranges["C"] = {key: c_score(q[key]) for key in ("low", "base", "high")}
        evidence["C"] = {"state": "elicited", "leaves": {"q": {"state": "ELICITED_ASSUMPTION", **q,
                         "rationale": "The existing v3 distribution-retention × moat-retention judgment is reused as a bounded Stage 1 commercial-retention proxy.",
                         "source_ids": sorted(set(dist.get("source_ids", []) + moat.get("source_ids", [])))}}}

    terminal = v3.get("terminal_value")
    demand = adapter["operator_demand"].get(terminal)
    if demand is None:
        factor_ranges["D"] = {"low": None, "base": None, "high": None}
        evidence["D"] = {"state": "missing", "leaves": {"d5_o": {"state": "MISSING", "value": None}}}
    else:
        d5 = {key: float(value) for key, value in demand["d5"].items()}
        operator = {key: float(value) for key, value in demand["o"].items()}
        factor_ranges["D"] = {key: d_score(d5[key], operator[key]) for key in ("low", "base", "high")}
        evidence["D"] = {"state": "elicited", "leaves": {
            "d5": {"state": "ELICITED_ASSUMPTION", **d5},
            "o": {"state": "ELICITED_ASSUMPTION", **operator},
            "terminal_class": terminal,
            "rationale": "Predeclared bounded demand/operator row for the inherited v3 terminal class; unknown classes remain missing.",
        }}

    envelope = scenario_envelope(factor_ranges)
    leaf_states = [leaf.get("state") for factor in evidence.values() for leaf in factor.get("leaves", {}).values() if isinstance(leaf, dict)]
    readiness, action = readiness_and_action(leaf_states, envelope)
    base = envelope["base"]
    base_factors = base["factors"] if base else {name: None for name in ("H", "F", "C", "D")}
    numeric = [item for item in base_factors.items() if item[1] is not None]
    driver = max(numeric, key=lambda item: item[1])[0] if numeric else None
    weakness = min(numeric, key=lambda item: item[1])[0] if numeric else None

    return json_decimal({
        "naics": naics,
        "title": v3["title"],
        "sector": v3["sector"],
        "heterogeneous": bool(v3.get("heterogeneous")),
        "methodology_version": config["version"],
        "source_run": v3["run_meta"],
        "source_review": v3.get("source_review", {}),
        "factors": {name: {**factor_ranges[name], "evidence_state": evidence[name]["state"]} for name in ("H", "F", "C", "D")},
        "evidence": evidence,
        "envelope": envelope,
        "A": base["A"] if base else None,
        "L": base["L"] if base else None,
        "tier": base["tier"] if base else None,
        "tier_interval": envelope["tier_interval"],
        "robust_tier": envelope["robust_tier"],
        "readiness": readiness,
        "action": action,
        "principal_driver": driver,
        "principal_weakness": weakness,
        "sources": v3.get("sources", []),
        "caveats": list(v3.get("publication_caveats", [])),
        "v3": {"S": v3["S"], "verdict": v3["verdict"], "confidence": v3["confidence"], "scores": v3["scores"]},
    })


def build_records() -> tuple[list[dict], dict]:
    config = load_json(CONFIG_PATH)
    source = v3_records()
    membership = load_json(TARGETS)["codes"]
    missing = [item["naics"] for item in membership if item["naics"] not in source]
    if missing:
        raise SystemExit("missing v3 source records: %s" % missing)
    records = [factor_record(source[item["naics"]], config) for item in membership]
    records.sort(
        key=lambda item: (
            item["A"] is not None,
            TIER_ORDER.get(item["tier"], -1),
            item["A"] or -1,
            item["L"] or -1,
            -int(item["naics"]),
        ),
        reverse=True,
    )
    for index, record in enumerate(records, 1):
        record["rank"] = index if record["A"] is not None else None
    return records, config


def summary(records: list[dict]) -> dict:
    complete = [record for record in records if record["A"] is not None]
    return {
        "membership": len(records),
        "complete_base": len(complete),
        "missing_base": len(records) - len(complete),
        "tier_counts": dict(Counter(record["tier"] or "UNKNOWN" for record in records)),
        "readiness_counts": dict(Counter(record["readiness"] for record in records)),
        "action_counts": dict(Counter(record["action"] for record in records)),
        "robust_tier_count": sum(record["robust_tier"] is not None for record in records),
    }


def write_outputs(records: list[dict], config: dict, scope: str) -> None:
    selected = records if scope == "full" else [record for record in records if record["naics"] in CANARIES]
    run_root = OUT_ROOT / "runs"
    run_root.mkdir(parents=True, exist_ok=True)
    for record in selected:
        path = run_root / record["naics"] / "v4_3_minimal.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    report = {
        "_generated": "pipeline/build/build_v4_3_minimal.py — deterministic v4.3 Stage 1 output",
        "scope": scope,
        "methodology_version": config["version"],
        "canaries": list(CANARIES),
        "summary": summary(selected),
        "records": selected,
    }
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    report_path = OUT_ROOT / ("full_report.json" if scope == "full" else "canary_report.json")
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if scope == "full":
        SITE_OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scope", choices=("canary", "full"), default="canary")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    records, config = build_records()
    selected = records if args.scope == "full" else [item for item in records if item["naics"] in CANARIES]
    print(json.dumps(summary(selected), indent=2, sort_keys=True))
    if not args.check:
        write_outputs(records, config, args.scope)


if __name__ == "__main__":
    main()
