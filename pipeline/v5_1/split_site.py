#!/usr/bin/env python3
"""Presentation-layer splitter for the v5.1 dashboard (stdlib only, deterministic).

Derives two fast-loading artifacts from the canonical 6digit/six_data_v5_1.json
(which stays the single source of truth, written only by `build.py site`):

  6digit/fleet_index_v5_1.json   slim per-record index for list rendering,
                                 filtering, and sorting (~2% of the full file)
  6digit/records/<naics>.json    one full record per code, fetched lazily when
                                 the dashboard drawer opens

This file is NOT part of the frozen v5.1 contract surface and performs no
judgment: it copies fields verbatim and rounds only display numbers. Re-run it
whenever six_data_v5_1.json is rebuilt.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE_IN = ROOT / "6digit" / "six_data_v5_1.json"
INDEX_OUT = ROOT / "6digit" / "fleet_index_v5_1.json"
RECORDS_DIR = ROOT / "6digit" / "records"
FACTOR_NAMES = ("H", "F", "C", "D")


def rnd(value, digits):
    return None if value is None else round(value, digits)


def slim(record: dict) -> dict:
    lens = record["lens"]
    return {
        "naics": record["naics"],
        "title": record["title"],
        "A": rnd(record["A"], 4),
        "L": rnd(record["L"], 4),
        "tier": record["tier"],
        "tier_interval": record["tier_interval"],
        "robust_tier": bool(record["robust_tier"]),
        "readiness": record["readiness"],
        "action": record["action"],
        "independent_review": record["independent_review"],
        "order": record["order"],
        "heterogeneous": bool(lens["heterogeneous"]),
        "factor_bases": {name: rnd(record["factors"][name]["base"], 2)
                         for name in FACTOR_NAMES},
        "search_text": (lens["included_activities"] + " "
                        + lens["customer_and_revenue_model"]),
    }


def main() -> int:
    site = json.loads(SITE_IN.read_text(encoding="utf-8"))
    records = site["records"]

    RECORDS_DIR.mkdir(exist_ok=True)
    stale = {p.name for p in RECORDS_DIR.glob("*.json")}
    for record in records:
        name = record["naics"] + ".json"
        (RECORDS_DIR / name).write_text(
            json.dumps(record, separators=(",", ":"), ensure_ascii=False) + "\n",
            encoding="utf-8")
        stale.discard(name)
    for name in sorted(stale):
        (RECORDS_DIR / name).unlink()

    index = {
        "_generated": "pipeline/v5_1/split_site.py from six_data_v5_1.json — do not hand-edit",
        "methodology_version": site["methodology_version"],
        "label": site["label"],
        "coverage": site["coverage"],
        "summary": site["summary"],
        "records": [slim(record) for record in records],
    }
    INDEX_OUT.write_text(
        json.dumps(index, separators=(",", ":"), ensure_ascii=False) + "\n",
        encoding="utf-8")

    print(f"index: {INDEX_OUT.stat().st_size / 1024:.0f} KB "
          f"({len(records)} records) -> {INDEX_OUT.relative_to(ROOT)}")
    print(f"records: {len(records)} files, removed {len(stale)} stale "
          f"-> {RECORDS_DIR.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
