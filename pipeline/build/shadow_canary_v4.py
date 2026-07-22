#!/usr/bin/env python3
"""Deterministically re-express five reviewed v3 records under v4 for diagnostics.

This is not a v4 research packet and is never publication-eligible. It tests
whether the frozen formulas behave sensibly before isolated v4 research runs.
"""

import importlib.util
import json
import math
import os
import re


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CANARY = ("541512", "541511", "541214", "238220", "541930")
TARGETS = {
    "541512": "Contract-rich MSP and systems-integration operators",
    "541511": "Repeat-client custom development firms with fixed or outcome-linked delivery",
    "541214": "Independent local and regional payroll bureaus",
    "238220": "Residential and light-commercial HVAC service/replacement operators",
    "541930": "Blended language-service providers exposed to general translation repricing",
}
SURVIVAL = {
    "541512": "DURABLE",
    "541511": "PRESSURED",
    "541214": "DISINTERMEDIATED",
    "238220": "DURABLE",
    "541930": "PRESSURED",
}


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


scoring = load_module("v4_shadow_scoring", "v4_scoring.py")


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def numbers(text):
    found = [float(item) for item in re.findall(r"(?<![A-Za-z])(?:\d+\.\d+|\.\d+|\d+)(?![A-Za-z])", text or "")]
    return found


def numeric_range(text, base, floor=0.0, ceiling=None):
    found = numbers(text)
    candidates = []
    for value in found:
        if ceiling == 1.0 and value > 1 and value <= 100:
            value /= 100.0
        if value >= floor and (ceiling is None or value <= ceiling):
            candidates.append(value)
    if len(candidates) >= 2:
        low, high = min(candidates), max(candidates)
    else:
        width = max(abs(base) * 0.25, 0.15 if ceiling == 1.0 else 0.5)
        low, high = base - width, base + width
    low = max(floor, low)
    if ceiling is not None:
        high = min(ceiling, high)
    return {"low": min(low, base), "high": max(high, base)}


def years_range(text, base):
    """Extract year values without mistaking percentages such as t50 for years."""
    values = []
    range_pattern = r"(\d+(?:\.\d+)?)\s*(?:-|–|—|to)\s*(\d+(?:\.\d+)?)\s*years?"
    for low, high in re.findall(range_pattern, text or "", flags=re.IGNORECASE):
        values.extend((float(low), float(high)))
    without_ranges = re.sub(range_pattern, "", text or "", flags=re.IGNORECASE)
    for value in re.findall(r"(\d+(?:\.\d+)?)\s*years?", without_ranges, flags=re.IGNORECASE):
        values.append(float(value))
    if len(values) >= 2:
        return {"low": min(min(values), base), "high": max(max(values), base)}
    return numeric_range("", base, 0.0, None)


def selection(old, floor=0.0, ceiling=None, integer=False, range_parser=None):
    value = old["value"]
    source_ids = old.get("source_ids", [])
    quality = old.get("evidence_quality", "LOW")
    state = "PROXY" if source_ids else "ASSUMPTION"
    parsed_range = (range_parser(old.get("plausible_range", ""), value)
                    if range_parser else
                    numeric_range(old.get("plausible_range", ""), value, floor, ceiling))
    result = {
        "value": value,
        "range": parsed_range,
        "method": old.get("method", "ESTIMATE"),
        "evidence_state": state,
        "evidence_quality": quality if source_ids else "NONE",
        "confidence": old.get("confidence", "LOW"),
        "source_ids": source_ids,
        "rationale": old.get("rationale", ""),
        "caveats": old.get("caveats", []),
    }
    if integer:
        result["value"] = int(round(result["value"]))
    return result


def role_range(role):
    base = float(role["within_role_automatable_fraction"])
    return numeric_range(role.get("plausible_range", ""), base, 0.0, 1.0)


def translate(record):
    inputs = record["evidence"]["inputs"]
    dataset = record["evidence"]["dataset_inputs"]
    owner = inputs["owners_60plus_pct"]
    documented = owner.get("succession_shortage_documented", {}).get("value", False)
    seller_sources = owner.get("succession_shortage_documented", {}).get("source_ids", [])
    seller_state = "PROXY" if seller_sources else "ASSUMPTION"
    seller_value = "EXCESS" if documented else "UNKNOWN"
    translated = {
        "dataset_inputs": dataset,
        "inputs": {
            "ai_replaceable_share": {
                "evidence_state": "PROXY" if inputs["ai_replaceable_share"].get("source_ids") else "ASSUMPTION",
                "evidence_quality": inputs["ai_replaceable_share"].get("evidence_quality", "NONE")
                if inputs["ai_replaceable_share"].get("source_ids") else "NONE",
                "breakdown_by_role": [{
                    **role,
                    "range": role_range(role),
                } for role in inputs["ai_replaceable_share"]["breakdown_by_role"]]
            },
            "target_archetype": {
                "name": TARGETS[record["naics"]],
                "coverage": {
                    "value": None, "range": {"low": None, "high": None},
                    "method": "ESTIMATE", "evidence_state": "MISSING",
                    "evidence_quality": "NONE", "confidence": "LOW", "source_ids": [],
                    "rationale": "v3 did not estimate target-archetype share of n_band.", "caveats": []
                }
            },
            # v3 pi_dist was the direct predecessor of v4 24-month retention;
            # pi_moat is intentionally not multiplied again.
            "retained_savings_share_24m": selection(inputs["pi_dist"], 0.0, 1.0),
            "t50_years": selection(inputs["t50_years"], 0.0, None, range_parser=years_range),
            "seller_supply_signal": {
                "value": seller_value, "plausible_values": ["SCARCE", "NORMAL", "EXCESS"],
                "method": "ESTIMATE", "evidence_state": seller_state,
                "evidence_quality": owner.get("succession_shortage_documented", {}).get("evidence_quality", "NONE") if seller_sources else "NONE",
                "confidence": owner.get("succession_shortage_documented", {}).get("confidence", "LOW"),
                "source_ids": seller_sources, "rationale": "Mapped from the v3 documented succession signal.", "caveats": []
            },
            "active_consolidators": selection(inputs["active_consolidators"], 0.0, None, integer=True),
            "buy_mult": selection(inputs["buy_mult"], 0.01, None),
            "exit_mult": selection(inputs["exit_mult"], 0.01, None),
            "operator_survival": {
                "value": SURVIVAL[record["naics"]],
                "plausible_values": [SURVIVAL[record["naics"]]],
                "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED",
                "confidence": record["confidence"], "source_ids": [source["id"] for source in record["sources"][:1]],
                "rationale": "Shadow-only operator-level reinterpretation of the reviewed v3 narrative.", "caveats": ["Requires fresh v4 research and independent review."]
            }
        }
    }
    return translated


def main():
    data = load_json(os.path.join(REPO, "6digit", "six_data_v3.json"))
    by_code = {item["naics"]: item for item in data["records"]}
    results = []
    for code in CANARY:
        old = by_code[code]
        translated = translate(old)
        computed = scoring.calculate(translated)
        results.append({
            "naics": code,
            "title": old["title"],
            "target_archetype": TARGETS[code],
            "v3": {"S": old["S"], "verdict": old["verdict"], "scores": old["scores"], "confidence": old["confidence"]},
            "v4_shadow": {
                "scores": {name: {bound: computed[bound]["scores"][name] for bound in ("low", "base", "high")} for name in scoring.FACTOR_NAMES},
                "S": {bound: computed[bound]["S"] for bound in ("low", "base", "high")},
                "decision": computed["decision"],
            }
        })
    output = {
        "_warning": "FORMULA DIAGNOSTIC ONLY — migrated v3 evidence, not a v4 packet, research run, or accepted canary.",
        "methodology_version": "4.0",
        "records": results,
    }
    path = os.path.join(REPO, "pipeline", "v4", "shadow_canary.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    print("wrote %s" % path)
    for item in results:
        v4 = item["v4_shadow"]
        print("%s  v3 %.2f %-11s -> v4 %.2f [%.2f, %.2f] %-11s %-10s" % (
            item["naics"], item["v3"]["S"], item["v3"]["verdict"],
            v4["S"]["base"], v4["S"]["low"], v4["S"]["high"],
            v4["decision"]["economic_verdict"], v4["decision"]["evidence_readiness"]["status"]))


if __name__ == "__main__":
    main()
