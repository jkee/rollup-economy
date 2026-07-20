# Dataset layer (v3 pipeline, Phase 1 / Stage 1)

Deterministic, identically-derived inputs for every code in the map:
`labor_share`, `role_mix`, `n_total`, `n_band` — one JSON per code in
`derived/<naics>.json`, produced by scripts from bulk public extracts.
No model touches these values; no hand-entered per-code values anywhere.

**Universe:** the 1,012 six-digit NAICS 2022 codes that are the keys of
`6digit/six_data.json` (all sectors, including 11 and 92).

## How to re-run

```bash
cd pipeline/datasets
python3 download.py   # idempotent; fetches raw sources, writes checksums,
                      # produces trimmed national extracts from big files
python3 derive.py     # writes derived/<naics>.json x 1012 + coverage_report.md
```

Python 3 stdlib only (no pandas/openpyxl; download.py includes a minimal
stdlib xlsx reader for the OEWS files). Running derive.py twice produces
byte-identical output. Raw originals >10MB are gitignored
(`raw/.gitignore`); the committed trimmed extracts are pure deterministic
filters of them, so the derivation is reproducible from the committed
files alone. `raw/checksums.txt` records sha256 of everything;
`raw/sources.json` records source URL + retrieval date per file.

## Sources and vintages

| file (raw/) | source | vintage |
|---|---|---|
| `susb_us_state_6digitnaics_2022.txt` → `susb_us_2022.csv` (US rows) | Census SUSB, firms/estabs/employment/payroll/**receipts** by enterprise employment-size class, all NAICS levels. 2022 is an Economic Census year, so SUSB publishes receipts. | 2022 |
| `qcew_2024_annual_singlefile.zip` → `qcew_2024_us000.csv` (US000 rows) | BLS QCEW annual averages (establishments, employment, total annual wages, by ownership) | 2024 |
| `oesm24in4.zip` → `oews_nat{sector,3d,4d,5d_6d}_m2024_dl.csv` | BLS OEWS national industry-specific estimates (occupations x industry; columns trimmed, `total`+`detailed` rows) | May 2024 |
| `ip.data.1.AllData` (+`ip.series`, `ip.industry`) → `ips_L02_T30_annual.csv` | BLS Industry Productivity & Costs: labor compensation (L02, $M) and sectoral output (T30, $M) by detailed industry | annual, used at 2024 |
| `ecec.nr0.htm` | BLS ECEC news release (benefits multiplier) | March 2026 reference period at retrieval |
| `damodaran_margin.html` | Damodaran (NYU Stern) margins by sector, `EBITDA/Sales` column — source document for the hand-curated `margins.json` | January 2026 |

Note: the Economic Census API (`api.census.gov/data/2022/ecnbasic`) rejected
keyless requests at retrieval time; SUSB 2022 receipts (same underlying EC
collection) are used as the receipts source instead.

## Method per derived field

### labor_share (= total labor compensation / revenue)
Priority chain; the first step that has data wins. Method, sources, year and
quality are recorded per code in the output.

1. **IPS direct** (quality HIGH): L02 / T30 at the exact 6-digit code,
   year 2024 (latest common year if 2024 missing). 67 codes.
2. **QCEW × ECEC / SUSB** at the exact code (MED): QCEW 2024 private total
   annual wages × benefits multiplier ÷ SUSB 2022 receipts. The multiplier
   is the ECEC private-industry total-compensation-to-wages ratio parsed
   from the downloaded release ($46.60/hr ÷ $32.60/hr = 1.4294, March 2026
   reference period). **Stated vintage mismatch:** 2024 wages over 2022
   receipts. Values are **harmonized to the IPS basis** (see "Basis
   harmonization" below).
3. **IPS at nearest ancestor** (5→2-digit; MED at 5/4-digit, LOW at 3/2).
4. **QCEW × ECEC / SUSB at nearest ancestor** (LOW; harmonized to the IPS
   basis like step 2). Skipped for codes whose activity is outside SUSB
   scope (111, 112, 482, 491, 5251x, 8141, 92) — the ratio would mix
   scopes (e.g. QCEW sector-11 wages include farms, SUSB sector-11
   receipts do not).
5. **Government codes** with QCEW government wages but no revenue concept:
   value null, quality ESTIMATE, gap recorded.
6. **Scope-excluded codes with no IPS series** (crop/animal production,
   funds/trusts, private households): value null, quality ESTIMATE, gap
   recorded. Recommended future source for sector 11: USDA ERS farm income
   accounts.
7. Economy-wide ratio (LOW) — last resort; currently unused. Would also be
   harmonized to the IPS basis.

#### Basis harmonization

The QCEW × ECEC / SUSB method and the IPS L02/T30 method measure the same
concept on different bases (2024 wages over 2022 receipts vs a single-year
industry account; economy-wide ECEC benefits ratio vs IPS's
industry-specific compensation concept, which also covers
proprietors/self-employed). Left unadjusted, the two bases are not
cross-code comparable — the whole point of the dataset layer. So
`derive.py` computes, over every code where **both** methods exist at the
same 6-digit code (65 codes at current vintages), the ratio QCEW-method ÷
IPS-direct, takes the **median** (×1.3407), and divides every QCEW-method
labor_share (code-level, ancestor-level, and the fallback) by it. This is
a standard benchmarking adjustment in official statistics: the factor is
derived entirely from the dual-method overlap set, recomputed from the raw
data on every run (no hardcoded constant), and never looks at downstream
scores, verdicts, or reference values. IPS-derived values are unchanged;
quality flags are unchanged; each adjusted record's `method` string
records "Harmonized to IPS basis ÷<ratio> (median of N dual-method
codes)". Dispersion of the ratio (median/p25/p75/min/max) is reported in
`coverage_report.md` and `sanity_check.md` — the single global factor
corrects the systematic level, not code-level noise.

### role_mix
Top 10 detailed occupations by employment from OEWS May 2024 national
industry data at the closest published NAICS level (exact 6-digit → 5-digit
→ 4-digit → 3-digit → sector; the matched level is recorded in
`oews_level`). `emp_share` = occupation employment / industry total
employment; `wage_share` = occupation wage bill (TOT_EMP × A_MEAN) / sum of
wage bills over all detailed occupations in the industry. A_MEAN top-code
`#` is treated as $239,200 (BLS convention). Private-ownership rows
preferred; the ownership code is noted when only combined-ownership data
exists. Quality: 6-digit HIGH, 5/4-digit MED, 3-digit/sector LOW.

### n_total
SUSB 2022 firm count (all enterprise sizes) at the code — quality HIGH.
Where SUSB has no row (its scope excludes 111, 112, 482, 491, 5251x, 8141,
92; a few codes are simply not published), QCEW 2024 annual average
establishments are used as a proxy (private first, then government) —
quality LOW, proxy nature stated. 3 codes have neither series (see
coverage_report.md).

### n_band ($1–10M EBITDA firm-count chain; always quality ESTIMATE)
For each SUSB employment-size class (<5, 5-9, 10-19, 20-99, 100-499, 500+):
average revenue per firm = class receipts ÷ class firms (where class
receipts are suppressed: class employment/firms × code-level revenue per
employee; where both suppressed: stated midpoint employment × revenue per
employee). Implied EBITDA = revenue per firm × the EBITDA margin from
`margins.json` (longest NAICS-prefix match). A class's firms count toward
`n_band` when its implied average EBITDA falls in $1–10M. The full chain —
margin source, revenue/employee, per-class revenue, implied EBITDA, band
verdict — is recorded as text in `derivation`.

`margins.json` is the only hand-curated file: a coarse 2-digit/selected
3-digit EBITDA-margin table, each entry citing Damodaran (Jan 2026)
`EBITDA/Sales` or explicitly marked ESTIMATE. Values were fixed from the
named source before any derived output was computed and were not adjusted
afterwards (no-tuning rule).

### aux
SUSB 2022 employment, annual payroll ($), total receipts ($) and the
firms-by-size-class map used in the chain (QCEW values fill employment/
payroll where SUSB is out of scope).

## Quality flags

- **HIGH** — direct series at the exact code from the preferred source
- **MED** — identical method at the exact code with a stated vintage
  mismatch, or a consistent series inherited from a 4/5-digit parent
- **LOW** — inherited from 3-digit/sector level, or a proxy concept
  (establishments for firms)
- **ESTIMATE** — no defensible series (value may be null), or, for n_band,
  the by-construction label for the margin-based chain

## Companion documents

- `coverage_report.md` — generated by derive.py: per-field coverage counts,
  which codes use which fallback, anomalies (labor_share > 1), known gaps.
- `sanity_check.md` — plan item 1.3: 541330 vs the independent 0.470
  reference, n_total spot checks, one record traced end-to-end.

## Refresh cadence

QCEW/OEWS/IPS are annual (next: 2025 data, spring–autumn 2026); SUSB
receipts refresh only with Economic Census years (next: 2027 data,
published ~2029/30). The ECEC release updates quarterly — re-running
download.py after a new release changes the multiplier, so the retrieval
date in `raw/sources.json` pins the vintage actually used.
