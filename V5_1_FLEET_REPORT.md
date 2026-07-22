# v5.1 fleet block report

> **Governance exception:** Research sessions were reused across 39 S1 records.
> Victor directly instructed the operator on 2026-07-22 to ignore the
> single-purpose-session rule, accepting S1 and allowing the campaign to resume.
> See `V5_1_INCIDENT_REPORT.md`. All deterministic validation and sampled-review
> requirements remain in force.

This report records block-level observations for the provisional
sampled-validation campaign. Block samples are not used for defect-rate
inference; that analysis is reserved for the campaign closure report.

## S1 — Professional, scientific, and technical services

**Ledger status:** closed 2026-07-22; provenance exception accepted by Victor
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

## S2 — Administrative and support and waste management services

**Closed:** 2026-07-22
**Coverage:** 44 attempted, 44 deterministically valid, 44 published, 0 excluded
**Independent review:** 12/44 (8 mandatory, 4 random, 0 canary)
**Review outcomes:** 12 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 3 `HIGHEST_PRIORITY`, 5 `PRIORITY`, 20 `CONDITIONAL`,
  14 `LOW_PRIORITY`, and 2 `STRUCTURAL_OUT`.
- Readiness: 44 `MODEL_CONDITIONED`.
- Actions: 44 `VALIDATE_ASSUMPTIONS`.
- Robust tiers: 0/44.
- Publication labels: 12 `accepted`; 32 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `561431`, `561520`, `561910`, and `562998`.
All four were accepted with caveats and carried no material finding. These are
sample observations only; no S2 defect rate is estimated.

### Economic read

The screen remained differentiating across this mixed terrain. Office
administration, placement and executive search combined larger labor
opportunity with plausible transferable-firm depth and reached the highest
base tier. Contact centers, collection agencies, travel arrangement, guard
services, and other nonhazardous treatment/disposal reached `PRIORITY` through
different combinations of automation opportunity, firm availability,
retention, and demand.

Physical, route-, asset-, or site-intensive services concentrated lower:
facilities support, armored cars, building services, waste collection,
landfills, remediation, and materials recovery were mostly `LOW_PRIORITY`.
Professional employer organizations and waste combustors were
`STRUCTURAL_OUT`. Every record nevertheless remained model-conditioned, and no
base tier proved robust across its research-input envelope, so the block
produced no unconditional Stage 2 action.

Validators' caveats centered on broad occupational or sector proxies,
unobserved LMM implementation depth, weak direct transfer-rate denominators,
and judgmental retention/operator-necessity estimates. No accepted review found
a correction meeting the frozen base-tier-or-action materiality threshold, and
the predeclared pause trigger did not fire.

## S3 — Health care and social assistance

**Closed:** 2026-07-22
**Coverage:** 39 attempted, 39 deterministically valid, 39 published, 0 excluded
**Independent review:** 12/39 (7 mandatory, 4 random, 1 canary)
**Review outcomes:** 12 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 7 `PRIORITY`, 15 `CONDITIONAL`, 11 `LOW_PRIORITY`,
  5 `STRUCTURAL_OUT`, and 1 without a base tier.
- Readiness: 38 `MODEL_CONDITIONED`; 1 `STRESS_TEST_ONLY`.
- Actions: 38 `VALIDATE_ASSUMPTIONS`; 1 `EVIDENCE_FIRST`.
- Robust tiers: 2/39, both `STRUCTURAL_OUT`.
- Publication labels: 12 `accepted`; 27 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `621493`, `621498`, `621512`, and `624229`.
All four were accepted with caveats and carried no material finding. The
previously reviewed canary `621111` also closed with the block. These are sample
observations only; no S3 defect rate is estimated.

### Economic read

The screen separated ambulatory, practitioner-led, and social-service models
from institution- and asset-heavy care. Seven records reached `PRIORITY`:
mental-health physician and practitioner offices, therapy/audiology practices,
other health practitioners, outpatient behavioral-health centers, other
residential care, and other individual/family services. Their opportunity was
still evidence-conditioned; none reached `HIGHEST_PRIORITY` or an unconditional
Stage 2 action.

Hospitals, dialysis, ambulatory surgery/emergency centers, ambulance services,
blood/organ banks, nursing facilities, senior living, relief services, and
child care generally screened low or out as physical delivery, regulated care,
institutional form, or thin transferable-firm depth constrained the frozen
lens. `624221` Temporary Shelters correctly followed the declared-gap route to
no base tier and `STRESS_TEST_ONLY / EVIDENCE_FIRST`.

Validators repeatedly caveated broad occupation and adoption proxies, limited
LMM-specific implementation evidence, estimated eligible-firm counts, sparse
transaction denominators, and judgmental transfer/retention bridges. No review
found a correction meeting the frozen base-tier-or-action materiality test, and
the predeclared pause trigger did not fire.

## S4 — Finance and insurance

**Closed:** 2026-07-22
**Coverage:** 35 attempted, 35 deterministically valid, 35 published, 0 excluded
**Independent review:** 8/35 (3 mandatory, 4 random, 1 canary)
**Review outcomes:** 8 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 1 `HIGHEST_PRIORITY`, 3 `PRIORITY`, 6 `CONDITIONAL`,
  6 `LOW_PRIORITY`, 8 `STRUCTURAL_OUT`, and 11 without a base tier.
- Readiness: 24 `MODEL_CONDITIONED`; 11 `STRESS_TEST_ONLY`.
- Actions: 24 `VALIDATE_ASSUMPTIONS`; 11 `EVIDENCE_FIRST`.
- Robust tiers: 4/35, all `STRUCTURAL_OUT`.
- Publication labels: 8 `accepted`; 27 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `522320`, `523150`, `525110`, and `525990`.
All four were accepted with caveats and carried no material finding; the two
financial-vehicle records remained honestly gap-routed. The previously reviewed
canary `522310` also closed with the block. These are sample observations only;
no S4 defect rate is estimated.

### Economic read

The screen strongly distinguished service intermediaries from balance-sheet,
institutional, and vehicle structures. Insurance agencies and brokerages were
the sole `HIGHEST_PRIORITY` record. Claims adjusting and other insurance-related
activities joined mortgage and nonmortgage loan brokers at `PRIORITY`. Those
models combine recurring workflow, meaningful labor opportunity, and a more
plausible transferable operating-company population than banks, carriers,
funds, or special-purpose vehicles.

Eleven records had no base tier and routed to `STRESS_TEST_ONLY /
EVIDENCE_FIRST`, including savings institutions, selected securities/credit
intermediation codes, portfolio management/investment advice, and all six
5251/5259 fund or vehicle codes. This is the frozen gap mechanism working as
designed, not a zero score. Eight more records were `STRUCTURAL_OUT`, reflecting
thin eligible-firm depth or an incoherent LMM recurring-service lens for their
institutional form.

Validators' caveats emphasized broad financial-sector proxies, weak direct LMM
implementation measures, sparse transfer denominators, estimated eligible-firm
populations, and judgmental retention/operator-necessity bridges. No review
found a correction meeting the frozen base-tier-or-action materiality test, and
the predeclared pause trigger did not fire.

## S5 — Real estate, rental and leasing, and management of companies

**Closed:** 2026-07-22
**Coverage:** 27 attempted, 27 deterministically valid, 27 published, 0 excluded
**Independent review:** 7/27 (4 mandatory, 3 random, 0 canary)
**Review outcomes:** 7 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 4 `PRIORITY`, 8 `CONDITIONAL`, 8 `LOW_PRIORITY`,
  5 `STRUCTURAL_OUT`, and 2 without a base tier.
- Readiness: 25 `MODEL_CONDITIONED`; 2 `STRESS_TEST_ONLY`.
- Actions: 25 `VALIDATE_ASSUMPTIONS`; 2 `EVIDENCE_FIRST`.
- Robust tiers: 2/27, both `STRUCTURAL_OUT`.
- Publication labels: 7 `accepted`; 20 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `531210`, `532412`, and `532490`. All three
were accepted with caveats and carried no material finding. These are sample
observations only; no S5 defect rate is estimated.

### Economic read

The screen favored recurring operating services over ownership and asset-heavy
models. Residential and nonresidential property managers, other real-estate
support activities, and general rental centers reached `PRIORITY`. None reached
`HIGHEST_PRIORITY`, and every scored record remained model-conditioned.

Building lessors, vehicle/equipment rental categories, and several specialty
rental models concentrated in `LOW_PRIORITY`, `CONDITIONAL`, or
`STRUCTURAL_OUT` as low labor opportunity, asset intensity, or thin
transferable-firm depth constrained the frozen lens. Offices of bank and other
holding companies had no base tier and correctly routed to `STRESS_TEST_ONLY /
EVIDENCE_FIRST`.

The frozen `551114` dataset anomaly mechanically maxed its base H factor at
10.0, but the record still screened `LOW_PRIORITY` and
`MODEL_CONDITIONED / VALIDATE_ASSUMPTIONS`; no input was edited or tuned around
the anomaly. Validators' caveats centered on broad real-estate/rental proxies,
estimated eligibility and transaction depth, limited LMM implementation
evidence, and judgmental retention/operator-necessity bridges. No review found
a correction meeting the frozen materiality test, and the predeclared pause
trigger did not fire.

## S6 — Other services

**Closed:** 2026-07-22
**Coverage:** 44 attempted, 44 deterministically valid, 44 published, 0 excluded
**Independent review:** 8/44 (3 mandatory, 5 random, 0 canary)
**Review outcomes:** 8 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 3 `PRIORITY`, 14 `CONDITIONAL`, 11 `LOW_PRIORITY`,
  12 `STRUCTURAL_OUT`, and 4 without a base tier.
- Readiness: 40 `MODEL_CONDITIONED`; 4 `STRESS_TEST_ONLY`.
- Actions: 40 `VALIDATE_ASSUMPTIONS`; 4 `EVIDENCE_FIRST`.
- Robust tiers: 7/44, all `STRUCTURAL_OUT`.
- Publication labels: 8 `accepted`; 36 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `811121`, `812199`, `813212`, `813219`, and
`813990`. All five were accepted with caveats and carried no material finding.
These are sample observations only; no S6 defect rate is estimated.

### Economic read

The screen differentiated recurring route or membership services from
physical, local, and highly fragmented activities. Linen supply, business
associations, and professional organizations reached `PRIORITY`. Repair,
personal-care, death-care, laundry, civic, grantmaking, and membership models
spread across `CONDITIONAL`, `LOW_PRIORITY`, and `STRUCTURAL_OUT` as labor
opportunity, eligible-firm depth, demand, and transferability varied.

Four records had no base tier and routed to `STRESS_TEST_ONLY /
EVIDENCE_FIRST`: specialized automotive repair, electronic and precision
equipment repair, one-hour photofinishing, and private households. The
`814110` gap therefore remained explicit rather than being converted to zero.
No scored record reached an unconditional action.

Validators' caveats emphasized broad occupational and association proxies,
estimated implementation and eligibility, sparse transaction denominators,
and judgmental retention/operator-necessity bridges. No review found a
correction meeting the frozen materiality test, and the predeclared pause
trigger did not fire.
