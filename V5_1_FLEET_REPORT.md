# v5.1 fleet block report

This report records block-level observations for the provisional
sampled-validation campaign. Block samples are not used for defect-rate
inference; that analysis is reserved for the campaign closure report.

## S1 — Professional, scientific, and technical services

**Closed:** 2026-07-22  
**Coverage:** 49 attempted, 49 deterministically valid, 49 published, 0 excluded  
**Independent review:** 29/49 (26 mandatory, 3 random, 0 canary)  
**Review outcomes:** 29 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`  
**Material findings:** 0  
**Remediations:** 0

### Screen distribution

- Base tiers: 14 `HIGHEST_PRIORITY`, 12 `PRIORITY`, 18 `CONDITIONAL`,
  2 `LOW_PRIORITY`, 2 `STRUCTURAL_OUT`, and 1 without a base tier.
- Readiness: 48 `MODEL_CONDITIONED`; 1 `STRESS_TEST_ONLY`.
- Actions: 48 `VALIDATE_ASSUMPTIONS`; 1 `EVIDENCE_FIRST`.
- Robust tiers: 1/49.
- Publication labels: 29 `accepted`; 20 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `541330`, `541850`, and `541921`. All three
were accepted with caveats and carried no material finding. These are sample
observations only; no S1 defect rate is estimated.

### Economic read

The screen remained differentiating in the professional-services territory.
High labor intensity and transferable-firm depth produced 26 top-tier base
records, while narrow or very small firm pools, weaker labor opportunity, or
missing dataset anchors kept other codes conditional or below. Readiness did
not follow the high economics: every scored record remained model-conditioned,
so none received an unconditional Stage 2 action. `541120` correctly routed its
missing firm-count anchor to `STRESS_TEST_ONLY / EVIDENCE_FIRST`.

Validators repeatedly noted that task exposure, implementation, transfer, and
retention values rely on disclosed cross-population proxies or bounded
judgment. Those weaknesses are visible in the readiness/action layer and the
review caveats. No accepted review identified a correction that met the frozen
base-tier-or-action materiality test, and the predeclared pause trigger did not
fire.

### v5.0 drift observation

All 49 S1 codes overlap the immutable v5.0 output. Base tier matched for 26/49
and changed for 23/49; every changed tier moved upward in v5.1. Among the 48
records with a base A in both versions, the median A change was +0.814 (mean
+0.916; range -0.240 to +2.657). Despite this score drift, action matched for
49/49 because the records remained evidence-constrained.

This is a researcher-to-researcher drift observation, not a calibration change
or a reason to alter the frozen scorer. It reinforces the provisional label and
the value of the future full-validation campaign; the v5.1 inputs are not tuned
back toward v5.0 outcomes.
