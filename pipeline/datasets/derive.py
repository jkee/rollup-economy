#!/usr/bin/env python3
"""
derive.py — deterministic derivation of the v3 dataset inputs.

Reads the trimmed extracts in raw/ (produced by download.py) and writes one
JSON per NAICS code in derived/<naics>.json for every code in the universe
(the keys of 6digit/six_data.json — 1,012 six-digit NAICS 2022 codes).

Derived fields (method + quality recorded per field, see README.md):
  labor_share  — total labor compensation / revenue
                 1) BLS IPS L02/T30 at the exact 6-digit code (HIGH)
                 2) QCEW 2024 private wages x ECEC benefits multiplier
                    / SUSB 2022 receipts at the code (MED; vintage mismatch)
                 3) same ratio computed at nearest ancestor (LOW)
                 4) economy-wide ratio (LOW)
                 All QCEW-method values (2, 3, 4) are harmonized to the IPS
                 basis: divided by the median QCEW-method/IPS-direct ratio
                 computed over the codes where both methods exist at the
                 same 6-digit code (benchmarking adjustment for the vintage
                 mismatch + concept differences; derived from the data, no
                 hardcoded factor, never looks at downstream outcomes).
  role_mix     — top 10 detailed occupations from OEWS May 2024 national
                 industry data at the closest published NAICS level
  n_total      — SUSB 2022 firm count (HIGH); QCEW establishments (LOW proxy)
  n_band       — SUSB firms-by-size x revenue per firm x margins.json EBITDA
                 margin -> firms whose implied avg EBITDA is in $1-10M
                 (always ESTIMATE)

No hand-entered per-code values. Running twice produces identical output.
Python 3 stdlib only.
"""
import csv
import json
import os
import re
import statistics
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "derived")
SIX = os.path.normpath(os.path.join(HERE, "..", "..", "6digit", "six_data.json"))

IPS_YEAR = "2024"          # matches QCEW vintage; falls back to latest common
QCEW_YEAR = "2024"
SUSB_YEAR = "2022"
OEWS_YEAR = "May 2024"
BAND_LO, BAND_HI = 1_000_000, 10_000_000

# SUSB enterprise-size classes (mutually exclusive partition; 33=<20, 37=<500
# are aggregates and skipped). Midpoint employment is the stated assumption
# used only when a class's EMPL or RCPT is suppressed.
SIZE_CLASSES = [("02", "<5", 2.5), ("03", "5-9", 7.0), ("26", "10-19", 14.5),
                ("34", "20-99", 59.5), ("35", "100-499", 299.5),
                ("36", "500+", 750.0)]

SECTOR_RANGE = {"31": "31-33", "32": "31-33", "33": "31-33",
                "44": "44-45", "45": "44-45", "48": "48-49", "49": "48-49"}


def sector_key(code):
    return SECTOR_RANGE.get(code[:2], code[:2])


def ancestors(code):
    """Ancestor keys of a 6-digit code, most specific first."""
    return [code[:5], code[:4], code[:3], sector_key(code)]


def to_int(s):
    try:
        return int(s)
    except (TypeError, ValueError):
        return None


def to_float(s):
    try:
        return float(str(s).replace(",", ""))
    except (TypeError, ValueError):
        return None


# ------------------------------------------------------------------- loaders
def load_universe():
    with open(SIX) as f:
        six = json.load(f)
    return {code: rec.get("title", "") for code, rec in six.items()}


def load_susb():
    """susb[naics][size_code] = dict(firm, estb, empl, payr, rcpt)."""
    susb = defaultdict(dict)
    with open(os.path.join(RAW, "susb_us_2022.csv"), newline="") as f:
        for row in csv.DictReader(f):
            naics = row["NAICS"].strip()
            entr = row["ENTRSIZE"].strip()
            susb[naics][entr] = {
                "firm": to_int(row["FIRM"]),
                "estb": to_int(row["ESTB"]),
                "empl": to_int(row["EMPL"]),
                "empl_fl": row["EMPLFL_N"].strip(),
                "payr": to_int(row["PAYR"]),      # $1,000
                "payr_fl": row["PAYRFL_N"].strip(),
                "rcpt": to_int(row["RCPT"]),      # $1,000
                "rcpt_fl": row["RCPTFL_N"].strip(),
            }
    return susb


def load_qcew():
    """qcew_priv[industry] / qcew_gov[industry] = dict(estabs, emp, wages)."""
    priv, gov = {}, defaultdict(lambda: {"estabs": 0, "emp": 0, "wages": 0})
    with open(os.path.join(RAW, "qcew_2024_us000.csv"), newline="") as f:
        for row in csv.DictReader(f):
            if row["qtr"] != "A" or row["year"] != QCEW_YEAR:
                continue
            ind = row["industry_code"].strip()
            rec = {"estabs": to_int(row["annual_avg_estabs"]) or 0,
                   "emp": to_int(row["annual_avg_emplvl"]) or 0,
                   "wages": to_int(row["total_annual_wages"]) or 0}
            own = row["own_code"]
            if own == "5":
                priv[ind] = rec
            elif own in ("1", "2", "3"):
                g = gov[ind]
                for k in g:
                    g[k] += rec[k]
    return priv, dict(gov)


def load_ecec():
    """Parse private-industry total comp and wages from the ECEC release."""
    with open(os.path.join(RAW, "ecec.nr0.htm"), encoding="utf-8",
              errors="replace") as f:
        txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", f.read()))
    m = re.search(r"compensation costs for private industry workers averaged "
                  r"\$([\d.]+) per hour worked in ([A-Za-z]+ \d{4})\. "
                  r"Wages and salaries averaged \$([\d.]+)", txt)
    if not m:
        raise RuntimeError("ECEC private-industry sentence not found")
    total, ref, wages = float(m.group(1)), m.group(2), float(m.group(3))
    return {"multiplier": total / wages, "total": total, "wages": wages,
            "reference": ref}


def load_ips():
    """ips[naics] = {year: {'L02': v, 'T30': v}} for every NAICS level IPS
    publishes (2- to 6-digit; 'N1122__' -> '1122'). Series ids end with
    <measure> + 7 zeros for $-level series (the '1' variant is percent
    change). D-prefixed division codes are skipped."""
    ips = defaultdict(lambda: defaultdict(dict))
    with open(os.path.join(RAW, "ips_L02_T30_annual.csv"), newline="") as f:
        for row in csv.DictReader(f):
            meas = row["measure_code"]
            if not row["series_id"].endswith(meas + "0000000"):
                continue
            ind = row["industry_code"]
            if not ind.startswith("N"):
                continue                     # D…/M… division & special codes
            naics = ind[1:].rstrip("_")
            if not naics.isdigit():
                continue
            v = to_float(row["value"])
            if v is not None:
                ips[naics][row["year"]][meas] = v
    return ips


def ips_share(ips, key):
    """(value, year, l02, t30) at an IPS naics key, preferring IPS_YEAR."""
    years = ips.get(key)
    if not years:
        return None
    year = IPS_YEAR if (IPS_YEAR in years and len(years[IPS_YEAR]) == 2) \
        else max((y for y, m in years.items() if len(m) == 2), default=None)
    if not year:
        return None
    l02, t30 = years[year]["L02"], years[year]["T30"]
    return l02 / t30, year, l02, t30


OEWS_FILES = ["oews_natsector_m2024_dl.csv", "oews_nat3d_m2024_dl.csv",
              "oews_nat4d_m2024_dl.csv", "oews_nat5d_6d_m2024_dl.csv"]
IGROUP_LEN = {"sector": 2, "3-digit": 3, "4-digit": 4, "5-digit": 5,
              "6-digit": 6}


def load_oews():
    """oews[(level, prefix)][own_code] = {'total': row|None, 'detail': [rows]}"""
    oews = defaultdict(lambda: defaultdict(lambda: {"total": None,
                                                    "detail": []}))
    for fname in OEWS_FILES:
        path = os.path.join(RAW, fname)
        if not os.path.exists(path):
            continue
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                ig = row["I_GROUP"].strip()
                if ig not in IGROUP_LEN:
                    continue
                naics = row["NAICS"].strip()
                prefix = naics if "-" in naics else naics[:IGROUP_LEN[ig]]
                tot_emp = to_float(row["TOT_EMP"])
                a_mean = row["A_MEAN"].strip()
                a_mean = 239200.0 if a_mean == "#" else to_float(a_mean)
                rec = {"occ": row["OCC_CODE"], "title": row["OCC_TITLE"],
                       "emp": tot_emp, "a_mean": a_mean}
                slot = oews[(ig, prefix)][row["OWN_CODE"].strip()]
                if row["O_GROUP"] == "total":
                    slot["total"] = rec
                elif row["O_GROUP"] == "detailed":
                    slot["detail"].append(rec)
    return oews


def load_margins():
    with open(os.path.join(HERE, "margins.json")) as f:
        m = json.load(f)["margins"]
    return m


# --------------------------------------------------------------- derivations
def susb_totals(susb, key):
    t = susb.get(key, {}).get("01")
    return t if t else None


def susb_receipts_emp(susb, key):
    """(receipts_$, employment) at a SUSB key, None if suppressed/absent."""
    t = susb_totals(susb, key)
    if not t:
        return None, None
    rcpt = t["rcpt"] * 1000 if t["rcpt"] else None
    empl = t["empl"] if t["empl"] else None
    return rcpt, empl


# SUSB's published aggregates exclude these activities entirely, so a
# QCEW-wages / SUSB-receipts ratio computed at an ANCESTOR of these codes
# mixes scopes (e.g. QCEW sector-11 wages include farms, SUSB sector-11
# receipts do not) and is skipped; IPS ancestors are used instead.
SUSB_SCOPE_EXCLUDED = ("111", "112", "482", "491", "5251", "52592", "52593",
                       "8141", "92")


def scope_excluded(code):
    return any(code.startswith(p) for p in SUSB_SCOPE_EXCLUDED)


def compute_harmonization(universe, susb, qcew_priv, ips, ecec):
    """Basis-harmonization factor for the QCEW-method labor_share.

    Over every code where BOTH the IPS-direct L02/T30 share and the
    QCEW x ECEC / SUSB share exist at the same 6-digit code, computes
    ratio = qcew_method / ips_method and takes the MEDIAN. Dividing
    QCEW-method values by this median puts them on the IPS basis
    (standard benchmarking adjustment; derived entirely from the
    dual-method overlap set — it never looks at scores or verdicts).
    """
    mult = ecec["multiplier"]
    pairs = []
    for code in sorted(universe):
        got = ips_share(ips, code)
        if not got:
            continue
        wages = qcew_priv.get(code, {}).get("wages") or 0
        rcpt, _ = susb_receipts_emp(susb, code)
        if not (wages > 0 and rcpt):
            continue
        pairs.append((code, (wages * mult / rcpt) / got[0]))
    ratios = sorted(r for _, r in pairs)
    if not ratios:
        return None
    q1, med, q3 = statistics.quantiles(ratios, n=4, method="inclusive")
    return {"ratio": med, "n": len(ratios), "p25": q1, "p75": q3,
            "min": ratios[0], "max": ratios[-1], "pairs": pairs}


def derive_labor_share(code, susb, qcew_priv, qcew_gov, ips, ecec, harm):
    mult = ecec["multiplier"]
    mult_txt = (f"ECEC private-industry total comp ${ecec['total']:.2f}/hr / "
                f"wages ${ecec['wages']:.2f}/hr = {mult:.4f} "
                f"({ecec['reference']} reference period)")

    def qcew_susb_at(key, level, quality):
        wages = qcew_priv.get(key, {}).get("wages") or 0
        rcpt, _ = susb_receipts_emp(susb, key)
        if not (wages > 0 and rcpt):
            return None
        return {
            "value": round(wages * mult / rcpt / harm["ratio"], 4),
            "method": (f"QCEW {QCEW_YEAR} private total annual wages at "
                       f"{key} (${wages:,}) x benefits multiplier "
                       f"{mult:.4f} [{mult_txt}] / SUSB {SUSB_YEAR} "
                       f"receipts at {key} (${rcpt:,}). Vintage mismatch: "
                       f"2024 wages over 2022 receipts, stated. Level: "
                       f"{level}. Harmonized to IPS basis "
                       f"÷{harm['ratio']:.4f} (median of {harm['n']} "
                       f"dual-method codes)."),
            "sources": ["BLS QCEW 2024 annual averages (US000, private)",
                        "BLS ECEC news release (raw/ecec.nr0.htm)",
                        "Census SUSB 2022 (receipts by NAICS)"],
            "year": f"{QCEW_YEAR} wages / {SUSB_YEAR} receipts",
            "quality": quality}

    def ips_at(key, level, quality):
        got = ips_share(ips, key)
        if not got:
            return None
        val, year, l02, t30 = got
        lvl_txt = "direct" if level == "6-digit" else f"at ancestor {key}"
        return {
            "value": round(val, 4),
            "method": (f"BLS Industry Productivity (IPS) {lvl_txt}: labor "
                       f"compensation (L02) ${l02:,.1f}M / sectoral output "
                       f"(T30) ${t30:,.1f}M, year {year}"),
            "sources": ["BLS Industry Productivity and Costs flat files "
                        "(ip.data.1.AllData), measures L02 and T30"],
            "year": year, "quality": quality}

    # 1) IPS direct at the exact 6-digit code
    r = ips_at(code, "6-digit", "HIGH")
    if r:
        return r
    # 2) QCEW wages x ECEC / SUSB receipts at the exact code
    r = qcew_susb_at(code, "6-digit", "MED")
    if r:
        return r
    # 3) IPS at the nearest ancestor (consistent numerator/denominator)
    for key, q in [(code[:5], "MED"), (code[:4], "MED"),
                   (code[:3], "LOW"), (code[:2], "LOW")]:
        r = ips_at(key, f"ancestor {key}", q)
        if r:
            return r
    # 4) QCEW/SUSB ratio at the nearest ancestor — skipped where SUSB's
    #    scope excludes this code's activity (ratio would mix scopes)
    if not scope_excluded(code):
        for a in ancestors(code):
            r = qcew_susb_at(a, f"ancestor {a}", "LOW")
            if r:
                return r
    # 5) government-dominated codes (e.g. sector 92): no receipts exist
    gov = qcew_gov.get(code)
    if gov and gov["wages"] > 0:
        return {
            "value": None,
            "method": ("No receipts concept for this code (government / "
                       "SUSB out of scope). QCEW government wages exist "
                       f"(${gov['wages']:,}) but there is no revenue "
                       "denominator; labor_share left null."),
            "sources": ["BLS QCEW 2024 annual averages (US000, government)"],
            "year": QCEW_YEAR, "quality": "ESTIMATE"}
    # 6) scope-excluded codes with no IPS series either: no consistent
    #    revenue denominator exists in the downloaded sources
    if scope_excluded(code):
        return {
            "value": None,
            "method": ("SUSB scope excludes this activity, no IPS "
                       "labor-compensation/output series at any level, and "
                       "no other receipts source downloaded; labor_share "
                       "left null (recorded gap)."),
            "sources": [], "year": "", "quality": "ESTIMATE"}
    # 7) economy-wide fallback
    wages = qcew_priv.get("10", {}).get("wages") or 0
    rcpt, _ = susb_receipts_emp(susb, "--")
    val = round(wages * mult / rcpt / harm["ratio"], 4) \
        if (wages and rcpt) else None
    return {
        "value": val,
        "method": ("Economy-wide fallback: QCEW total private wages x "
                   f"multiplier {mult:.4f} / SUSB total receipts. Used only "
                   "when no code- or ancestor-level series exists. "
                   f"Harmonized to IPS basis ÷{harm['ratio']:.4f} (median "
                   f"of {harm['n']} dual-method codes)."),
        "sources": ["BLS QCEW 2024", "BLS ECEC", "Census SUSB 2022"],
        "year": f"{QCEW_YEAR}/{SUSB_YEAR}", "quality": "LOW"}


ROLE_QUALITY = {"6-digit": "HIGH", "5-digit": "MED", "4-digit": "MED",
                "3-digit": "LOW", "sector": "LOW"}


def derive_role_mix(code, oews):
    for level, key in [("6-digit", code), ("5-digit", code[:5]),
                       ("4-digit", code[:4]), ("3-digit", code[:3]),
                       ("sector", sector_key(code))]:
        slot = oews.get((level, key))
        if not slot:
            continue
        own = "5" if "5" in slot else sorted(slot)[0]
        data = slot[own]
        detail = [d for d in data["detail"] if d["emp"]]
        if not detail:
            continue
        total_emp = (data["total"]["emp"] if data["total"] and
                     data["total"]["emp"] else sum(d["emp"] for d in detail))
        wage_bill = sum(d["emp"] * d["a_mean"] for d in detail if d["a_mean"])
        top = sorted(detail, key=lambda d: (-d["emp"], d["occ"]))[:10]
        occs = []
        for d in top:
            occs.append({
                "soc": d["occ"], "title": d["title"],
                "emp_share": round(d["emp"] / total_emp, 4),
                "wage_share": round(d["emp"] * d["a_mean"] / wage_bill, 4)
                if (d["a_mean"] and wage_bill) else None})
        note = "" if own == "5" else f" (ownership code {own})"
        return {"oews_level": f"{level} {key}{note}",
                "occupations": occs,
                "quality": ROLE_QUALITY[level]}
    return {"oews_level": "none", "occupations": [], "quality": "ESTIMATE"}


def derive_n_total(code, susb, qcew_priv, qcew_gov):
    t = susb_totals(susb, code)
    if t and t["firm"]:
        return {"value": t["firm"], "source": "SUSB 2022 (firms, all "
                "enterprise sizes)", "year": SUSB_YEAR, "quality": "HIGH"}
    p = qcew_priv.get(code)
    if p and p["estabs"]:
        return {"value": p["estabs"],
                "source": "QCEW 2024 private annual avg establishments "
                          "(SUSB out of scope for this code; establishments "
                          "are a proxy for firms — overcounts multi-unit "
                          "firms)",
                "year": QCEW_YEAR, "quality": "LOW"}
    g = qcew_gov.get(code)
    if g and g["estabs"]:
        return {"value": g["estabs"],
                "source": "QCEW 2024 government annual avg establishments "
                          "(government activity; firm concept does not "
                          "apply)",
                "year": QCEW_YEAR, "quality": "LOW"}
    return {"value": 0, "source": "no SUSB or QCEW series found",
            "year": "", "quality": "ESTIMATE"}


def margin_for(code, margins):
    for key in (code[:4], code[:3], code[:2]):
        if key in margins:
            return key, margins[key]
    return None, None


def derive_n_band(code, susb, margins, n_total):
    mkey, m = margin_for(code, margins)
    if m is None:
        return {"value": 0, "derivation": "no margin entry for sector",
                "margin_used": None, "margin_source": "missing",
                "quality": "ESTIMATE"}
    margin, msrc = m["ebitda_margin"], m["source"]
    # revenue per employee at the code, else nearest ancestor
    rev_per_emp = None
    rpe_key = None
    for key in [code] + ancestors(code) + ["--"]:
        rcpt, empl = susb_receipts_emp(susb, key)
        if rcpt and empl:
            rev_per_emp, rpe_key = rcpt / empl, key
            break
    sizes = susb.get(code, {})
    chain = [f"margin {margin:.4f} (margins.json[{mkey}]: {msrc})"]
    if rev_per_emp:
        chain.append(f"revenue/employee ${rev_per_emp:,.0f} "
                     f"(SUSB {SUSB_YEAR} receipts/employment at {rpe_key})")
    n_band = 0
    counted = False
    for sc, label, mid_emp in SIZE_CLASSES:
        row = sizes.get(sc)
        if not row or not row["firm"]:
            continue
        firms = row["firm"]
        if row["rcpt"]:
            rev_firm = row["rcpt"] * 1000 / firms
            how = "class receipts/firms"
        elif row["empl"] and rev_per_emp:
            rev_firm = row["empl"] / firms * rev_per_emp
            how = "class emp/firms x rev/emp"
        elif rev_per_emp:
            rev_firm = mid_emp * rev_per_emp
            how = f"midpoint {mid_emp} emp x rev/emp (class data suppressed)"
        else:
            chain.append(f"class {label}: {firms} firms, no revenue basis")
            continue
        ebitda = rev_firm * margin
        in_band = BAND_LO <= ebitda <= BAND_HI
        counted = True
        chain.append(f"class {label}: {firms:,} firms, avg revenue/firm "
                     f"${rev_firm:,.0f} ({how}), implied EBITDA "
                     f"${ebitda:,.0f} -> {'IN' if in_band else 'out of'} "
                     f"$1-10M band")
        if in_band:
            n_band += firms
    if not counted:
        chain.append("no SUSB size-class data for this code; n_band=0")
    chain.append(f"n_band = {n_band:,}")
    return {"value": n_band, "derivation": "; ".join(chain),
            "margin_used": margin, "margin_source": msrc,
            "quality": "ESTIMATE"}


def derive_aux(code, susb, qcew_priv):
    t = susb_totals(susb, code)
    sizes = susb.get(code, {})
    fbs = {label: sizes[sc]["firm"] for sc, label, _ in SIZE_CLASSES
           if sc in sizes and sizes[sc]["firm"] is not None}
    q = qcew_priv.get(code, {})
    return {
        "emp": (t["empl"] if t else None) or q.get("emp") or 0,
        "payroll_annual": (t["payr"] * 1000 if t and t["payr"] else None)
        or q.get("wages") or 0,
        "receipts_total": t["rcpt"] * 1000 if t and t["rcpt"] else 0,
        "firms_by_size_class": fbs,
    }


# ------------------------------------------------------------------ coverage
def coverage_report(records, universe, harm):
    def count(pred):
        return sum(1 for r in records.values() if pred(r))

    lines = ["# Dataset layer — coverage report",
             "",
             "Generated by `derive.py` (plan item 1.4). "
             f"Universe: {len(universe)} six-digit NAICS 2022 codes "
             "(keys of `6digit/six_data.json`).", ""]

    lines += ["## labor_share", "",
              "| method | quality | codes |", "|---|---|---|"]
    ls_groups = defaultdict(int)
    for r in records.values():
        q = r["labor_share"]["quality"]
        m = r["labor_share"]["method"]
        if m.startswith("BLS Industry Productivity (IPS) direct"):
            key = ("IPS direct (L02/T30)", q)
        elif m.startswith("BLS Industry Productivity (IPS) at ancestor"):
            key = ("IPS at ancestor (L02/T30)", q)
        elif "Level: 6-digit" in m:
            key = ("QCEW x ECEC / SUSB receipts at the code", q)
        elif "Level: ancestor" in m:
            key = ("QCEW x ECEC / SUSB receipts at ancestor", q)
        elif m.startswith("No receipts concept"):
            key = ("no revenue denominator (null)", q)
        elif m.startswith("SUSB scope excludes"):
            key = ("scope gap, no series at any level (null)", q)
        else:
            key = ("economy-wide fallback", q)
        ls_groups[key] += 1
    for (meth, q), n in sorted(ls_groups.items(), key=lambda x: -x[1]):
        lines.append(f"| {meth} | {q} | {n} |")
    null_ls = [c for c, r in records.items()
               if r["labor_share"]["value"] is None]
    lines += ["", f"Codes with null labor_share ({len(null_ls)}): "
              + (", ".join(null_ls) if null_ls else "none"), ""]
    over1 = sorted(((c, r["labor_share"]["value"]) for c, r in records.items()
                    if r["labor_share"]["value"] and
                    r["labor_share"]["value"] > 1.0), key=lambda x: -x[1])
    lines += [f"Anomalies — labor_share > 1.0 ({len(over1)} codes; kept "
              "as-published, no clamping): compensation genuinely exceeds "
              "receipts/output for subsidized or loss-making activities "
              "(transit, USPS) and for codes where the 2024-wages/"
              "2022-receipts vintage mismatch bites; treat as LOW-trust "
              "regardless of stated quality:", ""]
    lines += [", ".join(f"{c} ({v:.2f})" for c, v in over1), ""]

    lines += ["### Basis harmonization (QCEW-method values → IPS basis)", "",
              "All QCEW x ECEC / SUSB labor_share values (code-level, "
              "ancestor-level and the economy-wide fallback) are divided by "
              "the median QCEW-method/IPS-direct ratio over the codes where "
              "both methods exist at the same 6-digit code — a benchmarking "
              "adjustment for the 2024-wages/2022-receipts vintage mismatch "
              "and concept differences, derived only from the dual-method "
              "overlap set (never from downstream scores). IPS-derived "
              "values are unchanged.", "",
              f"- dual-method overlap set: {harm['n']} codes",
              f"- median ratio (the divisor): ×{harm['ratio']:.4f}",
              f"- dispersion: p25 ×{harm['p25']:.4f}, p75 ×{harm['p75']:.4f},"
              f" min ×{harm['min']:.4f}, max ×{harm['max']:.4f}", ""]
    if harm["p25"] < 1.1 or harm["p75"] > 1.6:
        lines += ["**Dispersion warning:** the p25–p75 range extends beyond "
                  "roughly [1.1, 1.6]; a single global factor is a crude "
                  "correction for some codes. It is still applied globally "
                  "— per-sector factors from small overlap samples would be "
                  "less defensible.", ""]

    lines += ["## role_mix", "",
              "| OEWS level matched | quality | codes |", "|---|---|---|"]
    rm_groups = defaultdict(int)
    for r in records.values():
        lvl = r["role_mix"]["oews_level"].split(" ")[0]
        rm_groups[(lvl, r["role_mix"]["quality"])] += 1
    for (lvl, q), n in sorted(rm_groups.items(), key=lambda x: -x[1]):
        lines.append(f"| {lvl} | {q} | {n} |")
    none_rm = [c for c, r in records.items()
               if r["role_mix"]["oews_level"] == "none"]
    lines += ["", f"Codes with no OEWS match ({len(none_rm)}): "
              + (", ".join(none_rm) if none_rm else "none"), ""]

    lines += ["## n_total", "",
              "| source | quality | codes |", "|---|---|---|"]
    nt_groups = defaultdict(int)
    for r in records.values():
        src = r["n_total"]["source"].split(" (")[0]
        nt_groups[(src, r["n_total"]["quality"])] += 1
    for (src, q), n in sorted(nt_groups.items(), key=lambda x: -x[1]):
        lines.append(f"| {src} | {q} | {n} |")
    qcew_nt = sorted(c for c, r in records.items()
                     if r["n_total"]["quality"] == "LOW")
    zero_nt = sorted(c for c, r in records.items()
                     if r["n_total"]["quality"] == "ESTIMATE")
    lines += ["", f"Codes using the QCEW establishment proxy ({len(qcew_nt)}):",
              "", ", ".join(qcew_nt) or "none", "",
              f"Codes with no firm/establishment series at all "
              f"({len(zero_nt)}): " + (", ".join(zero_nt) or "none"), ""]

    lines += ["## n_band", "",
              f"All {len(records)} codes: quality ESTIMATE by construction "
              "(public-company margins applied to small-firm revenue).",
              ""]
    nb_zero = count(lambda r: r["n_band"]["value"] == 0)
    lines += [f"- codes with n_band = 0: {nb_zero}",
              f"- codes with n_band > 0: {len(records) - nb_zero}", ""]

    lines += ["## Known gaps", "",
              "- **Economic Census API**: `api.census.gov/data/2022/ecnbasic` "
              "rejected keyless requests (302 -> missing_key) at retrieval "
              "time; receipts come instead from SUSB 2022 (an Economic "
              "Census year, so SUSB publishes receipts at 6-digit NAICS). "
              "Same underlying collection, one less join.",
              "- **SUSB scope**: crop & animal production (111, 112), rail "
              "(482), postal (491), certain funds/trusts (5251x), private "
              "households (8141) and public administration (92) are out of "
              "SUSB scope -> n_total falls back to QCEW establishments "
              "(LOW), receipts-based fields fall back or go null.",
              "- **Sector 92 / government codes**: no receipts concept; "
              "labor_share is null with quality ESTIMATE; n_band margin is "
              "0 by design (margins.json['92']).",
              "- **OEWS granularity**: industry detail is mostly 3/4-digit "
              "with selected 5/6-digit; the matched level is recorded in "
              "`role_mix.oews_level` per code.",
              "- **IPS coverage**: L02+T30 published for only a subset of "
              "6-digit industries; those codes get labor_share HIGH, the "
              "rest use the QCEW/SUSB chain.",
              "- **Vintage mismatch**: QCEW/OEWS/IPS are 2024, SUSB "
              "receipts are 2022; stated in every affected method string.",
              ""]
    with open(os.path.join(HERE, "coverage_report.md"), "w") as f:
        f.write("\n".join(lines))


# ---------------------------------------------------------------------- main
def main():
    os.makedirs(OUT, exist_ok=True)
    universe = load_universe()
    susb = load_susb()
    qcew_priv, qcew_gov = load_qcew()
    ecec = load_ecec()
    ips = load_ips()
    oews = load_oews()
    margins = load_margins()

    print(f"universe={len(universe)} susb_naics={len(susb)} "
          f"qcew_priv={len(qcew_priv)} ips_naics={len(ips)} "
          f"ips_exact={sum(1 for c in universe if c in ips)} "
          f"oews_groups={len(oews)} ecec_mult={ecec['multiplier']:.4f} "
          f"({ecec['reference']})")

    harm = compute_harmonization(universe, susb, qcew_priv, ips, ecec)
    if harm is None:
        raise RuntimeError("no dual-method codes; cannot harmonize basis")
    print(f"harmonization: n={harm['n']} median={harm['ratio']:.4f} "
          f"p25={harm['p25']:.4f} p75={harm['p75']:.4f} "
          f"min={harm['min']:.4f} max={harm['max']:.4f}")

    records = {}
    for code in sorted(universe):
        n_total = derive_n_total(code, susb, qcew_priv, qcew_gov)
        rec = {
            "naics": code,
            "title": universe[code],
            "labor_share": derive_labor_share(code, susb, qcew_priv,
                                              qcew_gov, ips, ecec, harm),
            "role_mix": derive_role_mix(code, oews),
            "n_total": n_total,
            "n_band": derive_n_band(code, susb, margins, n_total),
            "aux": derive_aux(code, susb, qcew_priv),
        }
        records[code] = rec
        with open(os.path.join(OUT, f"{code}.json"), "w") as f:
            json.dump(rec, f, indent=2)
            f.write("\n")

    coverage_report(records, universe, harm)
    print(f"wrote {len(records)} records to derived/ + coverage_report.md")


if __name__ == "__main__":
    main()
