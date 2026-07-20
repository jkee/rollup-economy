#!/usr/bin/env python3
"""Golden-set separation analysis (V3_PLAN.md 4.5).

Validates + recomputes every record in pipeline/golden/, assigns verdicts
from thresholds.json, and checks the frozen pass criteria:
  1. zero arithmetic mismatches;
  2. every melter caught by a cap (MELTING terminal or LOW confidence);
  3. no melter outranks the top live-thesis winners on verdict tier.

Run: python3 pipeline/build/golden_analysis.py
"""

import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
GOLDEN_DIR = os.path.join(REPO, "pipeline", "golden")
GOLDEN_SET = os.path.join(GOLDEN_DIR, "golden_set.json")

_spec = importlib.util.spec_from_file_location("build", os.path.join(HERE, "build.py"))
build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build)


def main():
    with open(os.path.join(HERE, "thresholds.json")) as f:
        th = json.load(f)
    with open(os.path.join(HERE, "schemas", "run_record.schema.json")) as f:
        run_schema = json.load(f)
    classes = {c["naics"]: c["class"] for c in build.load_json(GOLDEN_SET)["codes"]}

    rows, arith_fail, schema_fail = [], [], []
    for naics, cls in sorted(classes.items()):
        path = os.path.join(GOLDEN_DIR, naics + ".json")
        if not os.path.exists(path):
            print("MISSING golden record: %s" % naics)
            sys.exit(2)
        rec = build.load_json(path)
        errs = build.schema_errors(rec, run_schema, run_schema)
        if errs:
            schema_fail.append((naics, errs[:3]))
        computed, aerrs, _ = build.recompute(rec)
        if aerrs:
            arith_fail.extend(aerrs)
        factors = {k: computed[k] for k in "VCABM"}
        d = build.decide(computed["S"], factors,
                         rec["cross_checks"]["terminal_value"]["class"],
                         rec["confidence_overall"], th)
        rows.append({
            "naics": naics, "class": cls, "title": rec["title"],
            "S": round(computed["S"], 3), "factors": {k: round(v, 2) for k, v in factors.items()},
            "terminal": rec["cross_checks"]["terminal_value"]["class"],
            "confidence": rec["confidence_overall"],
            "verdict": d["verdict"], "capped_by": d["capped_by"],
            "gate_blocked": d["gate_blocked"], "borderline": d["borderline"],
        })

    rows.sort(key=lambda r: -r["S"])
    print("%-7s %-8s %-38s %6s  %-9s %-4s %-12s %s" % (
        "naics", "class", "title", "S", "terminal", "conf", "verdict", "flags"))
    for r in rows:
        flags = ",".join((["borderline"] if r["borderline"] else []) + r["capped_by"])
        print("%-7s %-8s %-38s %6.3f  %-9s %-4s %-12s %s" % (
            r["naics"], r["class"], r["title"][:38], r["S"], r["terminal"],
            r["confidence"], r["verdict"], flags))

    # pass criteria
    ok = True
    if schema_fail:
        ok = False
        print("\nSCHEMA FAILURES:")
        for n, e in schema_fail:
            print(" ", n, e)
    if arith_fail:
        ok = False
        print("\nARITHMETIC MISMATCHES:")
        for e in arith_fail:
            print(" ", e)

    melters = [r for r in rows if r["class"] == "melter"]
    uncaught = [r for r in melters
                if not (r["terminal"] == "MELTING" or r["confidence"] == "LOW"
                        or r["verdict"] in ("pass", "kill"))]
    if uncaught:
        ok = False
        print("\nUNCAUGHT MELTERS:", [r["naics"] for r in uncaught])

    tier = {"kill": 0, "pass": 1, "conditional": 2, "strong": 3, "hell_yes": 4}
    top_winner_tier = max(tier[r["verdict"]] for r in rows if r["class"] == "winner")
    bad = [r["naics"] for r in melters if tier[r["verdict"]] >= top_winner_tier]
    if bad:
        ok = False
        print("\nMELTERS AT/ABOVE TOP WINNER TIER:", bad)

    print("\nverdict counts:", {v: sum(1 for r in rows if r["verdict"] == v)
                                for v in tier})
    print("SEPARATION: %s" % ("PASS" if ok else "FAIL"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
