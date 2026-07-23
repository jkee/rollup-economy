# v5.1 campaign closure report

**Status:** closed on 2026-07-22. Methodology 5.1 remains frozen, all 20
blocks are closed, and the provisional sampled-validation publication covers
the full 1,012-code NAICS 2022 universe.

This is the final campaign ledger. The launch and canary gates were committed
before fleet work, every target was deterministically finalized, the frozen
sample was independently reviewed, no remediation or exclusion was required,
and the fail-closed site build publishes the complete universe. “Provisional”
remains part of the product label because 834 records were not independently
reviewed by design.

## Final disposition

| Measure | Result |
|---|---:|
| Frozen universe | 1,012 |
| Blocks closed | 20/20 |
| Unique codes attempted | 1,012 |
| Research attempts | 1,012 |
| Unique codes independently reviewed | 178 |
| Review attempts | 178 |
| Codes remediated once | 0 |
| Published | 1,012 |
| Excluded | 0 |
| Descoped | 0 |
| Published as `not_reviewed` | 834 |

Every review outcome was `publishable_with_caveats`: 178 accepted, 0
`publishable`, 0 `reject`, and 0 `invalid`. Reviews recorded zero material
findings. The predeclared pause trigger never fired.

## Block ledger

The review column is `mandatory/random/canary`; every listed sample member
has an accepted review.

| Block | Attempted | Reviewed | M/R/C | Remediated | Published | Excluded | Descoped |
|---|---:|---:|---:|---:|---:|---:|---:|
| S1 | 49 | 29 | 26/3/0 | 0 | 49 | 0 | 0 |
| S2 | 44 | 12 | 8/4/0 | 0 | 44 | 0 | 0 |
| S3 | 39 | 12 | 7/4/1 | 0 | 39 | 0 | 0 |
| S4 | 35 | 8 | 3/4/1 | 0 | 35 | 0 | 0 |
| S5 | 27 | 7 | 4/3/0 | 0 | 27 | 0 | 0 |
| S6 | 44 | 8 | 3/5/0 | 0 | 44 | 0 | 0 |
| S7 | 29 | 3 | 0/3/0 | 0 | 29 | 0 | 0 |
| S8 | 42 | 11 | 7/4/0 | 0 | 42 | 0 | 0 |
| S9 | 15 | 3 | 0/3/0 | 0 | 15 | 0 | 0 |
| G1 | 31 | 4 | 0/3/1 | 0 | 31 | 0 | 0 |
| G2 | 57 | 9 | 2/6/1 | 0 | 57 | 0 | 0 |
| G3 | 69 | 8 | 0/7/1 | 0 | 69 | 0 | 0 |
| G4 | 57 | 7 | 0/6/1 | 0 | 57 | 0 | 0 |
| G5 | 69 | 8 | 0/7/1 | 0 | 69 | 0 | 0 |
| G6 | 96 | 10 | 0/10/0 | 0 | 96 | 0 | 0 |
| G7 | 89 | 10 | 0/9/1 | 0 | 89 | 0 | 0 |
| G8 | 92 | 12 | 3/9/0 | 0 | 92 | 0 | 0 |
| G9 | 35 | 4 | 0/4/0 | 0 | 35 | 0 | 0 |
| Z1 | 64 | 9 | 1/7/1 | 0 | 64 | 0 | 0 |
| Z2 | 29 | 4 | 0/3/1 | 0 | 29 | 0 | 0 |
| **Total** | **1,012** | **178** | **64/104/10** | **0** | **1,012** | **0** | **0** |

## Campaign-wide sampled-validation statistics

Review coverage was 178/1,012, or 17.59%:

- Mandatory stratum: 64/64 reviewed. Together with one top-tier canary,
  every one of the 65 `HIGHEST_PRIORITY` or `PRIORITY` records was reviewed.
- Random stratum: 104/938 eligible non-mandatory, non-canary records reviewed.
- Canary stratum: 10/10 reviewed purposively and excluded from random
  inference.
- Unsampled publication: 834/1,012 records labeled `not_reviewed`.

The pooled random stratum contained zero material defects in 104 reviews.
Following the frozen design, each sampled record was weighted by the inverse
of its block inclusion probability (`random-frame size / random-sample size`).
Weights ranged from 5.000 to 10.000 and summed to the 938-record random frame.
The design-weighted defect-rate point estimate for the unreviewed
non-mandatory population is therefore **0.0%**. A 95% Kish-effective Wilson
interval, using effective sample size 102.74, is **0.0% to 3.6%**. The upper
bound matters: zero observed defects is not evidence that all 834 unreviewed
records are defect-free, and it does not support block-level inference.

Across all reviewed strata, validators audited 1,505 cited sources: 1,038
supported, 398 partially supported, 68 unsupported, and 1 not score-driving.
Unsupported or partial decorative claims remained caveats unless correction
could change the frozen tier or action mechanism; none met that materiality
test.

## Published distributions

| Dimension | Count |
|---|---:|
| Tier — `HIGHEST_PRIORITY` | 19 |
| Tier — `PRIORITY` | 46 |
| Tier — `CONDITIONAL` | 161 |
| Tier — `LOW_PRIORITY` | 228 |
| Tier — `STRUCTURAL_OUT` | 367 |
| Tier — no base tier | 191 |
| Readiness — `MODEL_CONDITIONED` | 821 |
| Readiness — `STRESS_TEST_ONLY` | 191 |
| Action — `VALIDATE_ASSUMPTIONS` | 821 |
| Action — `EVIDENCE_FIRST` | 191 |
| Robust tier present | 167 |

The 191 unscored records comprise the 181 predeclared frozen `n_band` gaps
plus 10 records with additional missing research primitives. Missing evidence
remained unscored and routed to `EVIDENCE_FIRST`; it was never converted into
a low score.

## S1 drift comparison with v5.0

All 49 S1 codes overlap immutable v5.0. Base tier matched for 26/49 and
changed for 23/49; every changed tier moved upward in v5.1. Among the 48
records with a base A in both versions, median A change was +0.814, mean change
was +0.916, and the range was -0.240 to +2.657. Action matched for 49/49
because all scored records remained evidence-constrained.

This is researcher-to-researcher drift, not a calibration change. No formula,
anchor, tier cut, evidence rule, frozen brief, or scoring code was adjusted to
move v5.1 toward or away from v5.0 outcomes.

## Cross-sector calibration observations

- Top-tier screens concentrated in labor- and information-rich services.
  Goods sectors mostly resolved to `CONDITIONAL`, `LOW_PRIORITY`, or
  `STRUCTURAL_OUT`, consistent with the frozen revenue-scale labor lens and
  physical-operator constraints.
- Electronics was the goods-sector exception: G8 produced three `PRIORITY`
  records (`334118`, `334412`, and `334413`) and 20 `CONDITIONAL` records,
  supported by digitized design, test, inspection, and production workflows.
- Wholesale, retail, and much of manufacturing screened low or out for stated
  economics rather than mechanical noise. Their weak dimensions were usually
  labor opportunity, firm-transfer depth, retention, or operator-required
  demand.
- Gap-heavy Z1 and Z2 behaved as predeclared. Z1 produced one `PRIORITY` and
  six `CONDITIONAL` farm-support records while 50 records remained unscored;
  all 29 public-administration records remained `EVIDENCE_FIRST`.
- All 821 scored records are still `MODEL_CONDITIONED`. No v5.1 record is an
  unconditional acquisition recommendation; the publication is a research
  map for assumption validation.

## Integrity and publication state

- `pipeline/v5_1/targets.json` contains exactly the 1,012 published codes.
- All blocks in `pipeline/v5_1/campaign_state.json` are closed with their
  immutable deterministic sample assignments.
- Every run passes deterministic packet, score, and memo reproduction checks;
  every sampled review passes `build.py validate-review` and binds to the
  reviewed artifact bytes.
- `python3 pipeline/v5_1/build.py audit-state` reports no errors or warnings.
- `python3 pipeline/v5_1/build.py site` publishes 1,012 records, excludes zero,
  labels 178 `accepted`, and labels 834 `not_reviewed`.
- `6digit/six_data_v5_1.json` is the canonical provisional
  sampled-validation dashboard output. Immutable `six_data_v5.json` remains
  the closed v5.0 publication.

## Maintenance handoff

Campaign artifacts are immutable history. The research date for every final
run is 2026-07-22, so market-sensitive evidence should be treated as stale at
about 12 months and reviewed by roughly **2027-07-22**. Refreshes create a new
date-stamped run series and new publication output; they never overwrite
`pipeline/v5_1/runs/` or `six_data_v5_1.json`.

Check the deterministic dataset layer at least annually and rebuild it when
newer applicable releases arrive. QCEW, OEWS, and IPS update annually; SUSB
receipts refresh with Economic Census years. Pinned vintages, source cadence,
and rebuild procedures are documented in
[`pipeline/datasets/README.md`](pipeline/datasets/README.md).

The next governed work is a separate full-validation campaign for the 834
`not_reviewed` records, or Stage 2 target/buyer diligence for reviewed top-tier
records. Neither may mutate this closed campaign. A formula, anchor, tier-cut,
or evidence-rule change requires a new methodology version.

## Usage disclosure

The repository records 1,012 finalized record assignments and 178 review
assignments, within the launch-fixed 1,400 assignment ceiling. It does not
contain a campaign-wide platform cost export, so no aggregate dollar total is
asserted or extrapolated.
