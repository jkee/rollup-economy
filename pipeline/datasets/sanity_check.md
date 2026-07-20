# Dataset layer — sanity checks (plan item 1.3)

Run date: 2026-07-20, against the raw vintages recorded in
`raw/sources.json`. Per the no-tuning rule, nothing below was adjusted to
make a check pass; misses are reported as misses. (The basis harmonization
described in §1 is a benchmarking adjustment derived from the dual-method
overlap set itself — it never looks at scores, verdicts, or any reference
value, and the residual miss it leaves is reported below unadjusted.)

## 1. 541330 Engineering Services — labor_share vs the 0.470 reference

Reference (given): BLS IPS labor compensation $172,759M / sectoral output
$367,702M, 2024 → **0.470**.

- **Published derived value: 0.4698** (quality HIGH), method "IPS direct":
  L02 $172,759.1M / T30 $367,702.1M, year 2024, from
  `raw/ips_L02_T30_annual.csv` (BLS ip.data.1.AllData flat file).
  **Delta: −0.0002** (rounding only). Caveat stated plainly: this is the
  *same* source as the reference, so agreement confirms the pipeline reads
  IPS correctly — it is not an independent confirmation.
- **Independent cross-method** (QCEW × ECEC ÷ SUSB receipts, the method
  used for the 747 MED codes): QCEW 2024 private wages at 541330
  $144,199,665,574 × 1.4294 (ECEC private total comp $46.60/hr ÷ wages
  $32.60/hr, March 2026 reference) ÷ SUSB 2022 receipts $312,242,373,000
  = 0.6601 raw; after basis harmonization (÷1.3407, see below):
  **0.4924**. **Delta vs reference: +0.022** (raw delta was +0.190).
  Still a miss, reported as such — no further adjustment. The residual
  reflects 541330's own deviation from the median dual-method ratio
  (its ratio is ×1.405, above the ×1.3407 median divisor).
- **Basis harmonization** (applied in `derive.py`, recorded in every
  affected `method` string): across the 65 codes where both methods
  exist at the same 6-digit code, QCEW-method ÷ IPS-direct has
  **median ×1.3407** (p25 ×1.1487, p75 ×1.4528, min ×0.5439,
  max ×3.4841). Every QCEW-method labor_share (code-level, ancestor-level
  and the economy-wide fallback — 824 records) is divided by the median,
  putting all values on the IPS basis for cross-code comparability;
  IPS-derived values are unchanged and quality flags are unchanged.
  Drivers of the gap: (a) 2024 wages over 2022 receipts (~2 years of
  nominal growth in the numerator only); (b) the economy-wide ECEC
  benefits ratio vs IPS's industry-specific compensation concept (IPS
  labor compensation also covers proprietors/self-employed, its output
  concept differs from receipts). Dispersion caveat: the p25–p75 band
  [×1.15, ×1.45] sits inside the roughly-acceptable [1.1, 1.6] range for
  a single global factor, but the tails are wide (×0.54–×3.48), so
  individual harmonized values can still be off substantially; the
  factor corrects the systematic level, not code-level noise.

## 2. n_total plausibility spot checks

Cross-checked against BLS QCEW 2024 national annual averages
(`raw/qcew_2024_us000.csv`, US000, private ownership) — an independent
program (BLS admin data vs Census SUSB): establishments should be ≥ firms,
with a plausible multi-unit ratio.

| code | industry | n_total (SUSB 2022 firms) | QCEW 2024 estabs | estabs/firms |
|---|---|---|---|---|
| 524210 | Insurance Agencies & Brokerages | 120,434 | 160,547 | 1.33 |
| 621210 | Offices of Dentists | 120,488 | 136,040 | 1.13 |
| 561730 | Landscaping Services | 114,842 | 123,133 | 1.07 |
| 238220 | Plumbing/HVAC Contractors | 107,004 | 122,326 (at 5-digit 23822; QCEW national publishes no 6-digit 238 rows) | 1.14 |

All four pass: establishment counts exceed firm counts by 7–33%, largest
for insurance brokerage (most branch-office-heavy of the four), smallest
for landscaping (overwhelmingly single-location) — the ordering itself is
economically sensible. Both figures are official statistics; no further
third-party counts were cited to avoid unverifiable numbers.

## 3. End-to-end trace of one record — derived/541330.json

Every number's origin:

- `title` "Engineering Services" — `6digit/six_data.json` (universe).
- `labor_share.value` 0.4698 — L02 172,759.143 ÷ T30 367,702.147, year
  2024, series IPUMN541330L020000000 / IPUMN541330T300000000 in
  `raw/ips_L02_T30_annual.csv` (trimmed from BLS ip.data.1.AllData).
- `role_mix` — OEWS May 2024, matched level "5-digit 54133"
  (`raw/oews_nat5d_6d_m2024_dl.csv`; OEWS pads the code to "541330" and
  labels it I_GROUP "5-digit"): top occupation Civil Engineers (17-2051)
  emp_share 0.1613 = TOT_EMP 188,160 ÷ industry total 1,166,210
  (All Occupations row); wage_share 0.166 = (188,160 × A_MEAN $108,700) ÷
  Σ(TOT_EMP × A_MEAN) over all detailed occupations in 54133. Quality MED
  (5-digit parent, not the exact 6-digit code).
- `n_total.value` 45,692 — SUSB 2022, US row NAICS 541330, ENTRSIZE 01
  (total), FIRM column (`raw/susb_us_2022.csv`). Quality HIGH.
- `n_band.value` 6,137 — chain recorded in the record verbatim: margin
  0.1565 (margins.json["54"], Damodaran Jan 2026 Business & Consumer
  Services EBITDA/Sales); per-size-class avg revenue/firm from SUSB class
  receipts ÷ class firms; classes 20-99 (4,840 firms, implied EBITDA
  $1.55M) and 100-499 (1,297 firms, implied EBITDA $6.70M) fall in the
  $1–10M band → 6,137. Quality ESTIMATE by construction.
- `aux` — SUSB 2022 totals row: EMPL 1,199,635; PAYR $126,920,409k;
  RCPT $312,242,373k; firms by class as listed.

Plausibility: 6,137 band-eligible firms out of 45,692 (13%) for an
industry known for mid-size firms is reasonable; the v2 prototype's
hand-estimate for the same concept was the right order of magnitude.

## 4. Determinism

`download.py && derive.py` re-run: `diff -rq` of two consecutive
`derived/` outputs — **identical** (1,012 files). Re-verified after the
basis harmonization was added (the factor is computed from the raw data
each run, so determinism is preserved); `coverage_report.md` also
byte-identical across runs.
