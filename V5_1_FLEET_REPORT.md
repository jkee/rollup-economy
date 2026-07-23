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

## S7 — Information

**Closed:** 2026-07-22
**Coverage:** 29 attempted, 29 deterministically valid, 29 published, 0 excluded
**Independent review:** 3/29 (0 mandatory, 3 random, 0 canary)
**Review outcomes:** 3 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 0 `HIGHEST_PRIORITY`, 0 `PRIORITY`, 5 `CONDITIONAL`,
  4 `LOW_PRIORITY`, 3 `STRUCTURAL_OUT`, and 17 without a base tier.
- Readiness: 12 `MODEL_CONDITIONED`; 17 `STRESS_TEST_ONLY`.
- Actions: 12 `VALIDATE_ASSUMPTIONS`; 17 `EVIDENCE_FIRST`.
- Robust tiers: 2/29, both `STRUCTURAL_OUT`.
- Publication labels: 3 `accepted`; 26 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `512250`, `513110`, and `518210`. All three
were accepted with caveats and carried no material finding. These are sample
observations only; no S7 defect rate is estimated.

### Economic read

The screen was conservative but remained informative across a terrain with
large product, platform, infrastructure, and regulated-network components.
Motion-picture production and distribution, postproduction, sound-recording
studios, and computing infrastructure reached `CONDITIONAL`; music publishing,
record production and distribution, other sound-recording industries, and
satellite telecommunications reached `LOW_PRIORITY`. No information record
reached `PRIORITY` or an unconditional Stage 2 action.

Seventeen records had no base tier and correctly routed to `STRESS_TEST_ONLY /
EVIDENCE_FIRST`. Those gaps concentrated in publishing, broadcasting,
telecommunications, libraries, search portals, and adjacent residual codes,
where the frozen firm-count input was missing or no defensible transferable
LMM denominator could be established. The three motion-picture theater and
specialty-video records that screened `STRUCTURAL_OUT` were constrained by
physical delivery, a very small eligible operator pool, or both.

Validators' caveats centered on broad occupation and sector proxies,
judgmental implementation and retention bridges, missing LMM denominators,
aggregate demand evidence, and transfer-rate proxies that did not directly
measure qualifying control transactions. Two official Census sources could
not be reopened during review, but the affected records already disclosed the
relevant uncertainty and no correction or honest downgrade changed a base tier
or action. No review found a material defect, and the predeclared pause trigger
did not fire.

## S8 — Educational services and arts, entertainment, and recreation

**Closed:** 2026-07-22
**Coverage:** 42 attempted, 42 deterministically valid, 42 published, 0 excluded
**Independent review:** 11/42 (7 mandatory, 4 random, 0 canary)
**Review outcomes:** 11 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 0 `HIGHEST_PRIORITY`, 7 `PRIORITY`, 17 `CONDITIONAL`,
  9 `LOW_PRIORITY`, 8 `STRUCTURAL_OUT`, and 1 without a base tier.
- Readiness: 41 `MODEL_CONDITIONED`; 1 `STRESS_TEST_ONLY`.
- Actions: 41 `VALIDATE_ASSUMPTIONS`; 1 `EVIDENCE_FIRST`.
- Robust tiers: 1/42, `STRUCTURAL_OUT`.
- Publication labels: 11 `accepted`; 31 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `711130`, `711310`, `713210`, and `713950`.
All four were accepted with caveats and carried no material finding. These are
sample observations only; no S8 defect rate is estimated.

### Economic read

The screen differentiated digital, workflow-rich instruction and representation
services from physical venues, nonprofit institutions, and embodied delivery.
Computer training, professional and management development training, other
technical and trade schools, exam preparation and tutoring, educational
support services, talent agents and managers, and qualifying multi-person
creative operators reached `PRIORITY`. Their opportunity combined repeatable
knowledge or administrative workflows with a continuing need for accountable
instruction, advice, negotiation, rights control, or client delivery.

Physical attractions and institution-heavy models generally screened lower.
Museums, historical sites, nature parks, arcades, casinos, other gambling,
business and secretarial schools, and racetracks were `STRUCTURAL_OUT`, often
because nonprofit or public governance, a zero or very small target-band firm
pool, or physical and safety-critical work constrained transferability. Sports
teams and clubs were the sole gap-routed record and correctly published without
a base tier as `STRESS_TEST_ONLY / EVIDENCE_FIRST`.

Validators' caveats emphasized broad occupational and sector proxies,
judgmental eligibility and benefit-retention estimates, sparse direct
qualifying-transfer evidence, heterogeneous residual codes, and demand measures
that did not perfectly match constant-price service quantity. One dynamic NAICS
definition page could not be fully verified during review, but the affected
eligibility estimate was already disclosed as broad and no correction or honest
downgrade changed the tier or action. No review found a material defect, and
the predeclared pause trigger did not fire.

## S9 — Accommodation and food services

**Closed:** 2026-07-22
**Coverage:** 15 attempted, 15 deterministically valid, 15 published, 0 excluded
**Independent review:** 3/15 (0 mandatory, 3 random, 0 canary)
**Review outcomes:** 3 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 0 `HIGHEST_PRIORITY`, 0 `PRIORITY`, 2 `CONDITIONAL`,
  8 `LOW_PRIORITY`, 5 `STRUCTURAL_OUT`, and 0 without a base tier.
- Readiness: 15 `MODEL_CONDITIONED`.
- Actions: 15 `VALIDATE_ASSUMPTIONS`.
- Robust tiers: 0/15.
- Publication labels: 3 `accepted`; 12 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `722330`, `722513`, and `722514`. All three
were accepted with caveats and carried no material finding. These are sample
observations only; no S9 defect rate is estimated.

### Economic read

The screen was appropriately conservative in a block dominated by physical,
site-specific, customer-facing delivery. Food service contractors and
recreational and vacation camps were the only `CONDITIONAL` records: each
combined a meaningful administrative or planning layer with recurring demand,
but retained substantial physical delivery, transferability, or pass-through
risk. No record reached `PRIORITY` or an unconditional Stage 2 action.

Hotels, inns, parks, caterers, limited-service restaurants, buffets, and snack
bars generally screened `LOW_PRIORITY`. Casino hotels, rooming and boarding
houses, mobile food services, drinking places, and full-service restaurants
were `STRUCTURAL_OUT`, reflecting very small or uncertain eligible-firm pools,
asset or licensing complexity, intense price competition, and the limited
portion of core labor that software can remove. All records nevertheless had a
base tier; none was gap-routed.

Validators' caveats emphasized broad industry and occupation proxies, scarce
direct evidence on qualifying LMM control transfers, judgmental firm
eligibility, limited implemented-AI evidence, and uncertainty over whether
savings would survive contract repricing or local competition. One exact NAICS
definition URL could not be reopened, but the associated eligibility input was
already an explicit estimate and no correction or honest downgrade changed a
tier or action. No review found a material defect, and the predeclared pause
trigger did not fire.

## G1 — Construction

**Closed:** 2026-07-22
**Coverage:** 31 attempted, 31 deterministically valid, 31 published, 0 excluded
**Independent review:** 4/31 (0 mandatory, 3 random, 1 canary)
**Review outcomes:** 4 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 0 `HIGHEST_PRIORITY`, 0 `PRIORITY`, 1 `CONDITIONAL`,
  14 `LOW_PRIORITY`, 16 `STRUCTURAL_OUT`, and 0 without a base tier.
- Readiness: 31 `MODEL_CONDITIONED`.
- Actions: 31 `VALIDATE_ASSUMPTIONS`.
- Robust tiers: 2/31, both `STRUCTURAL_OUT`.
- Publication labels: 4 `accepted`; 27 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `238140`, `238310`, and `238330`. All three
were accepted with caveats and carried no material finding. The previously
reviewed canary `238910` also closed with the block. These are sample
observations only; no G1 defect rate is estimated.

### Economic read

The screen was strongly conservative in a block where almost all delivery is
physical, site-specific, project-based, and repeatedly exposed to competitive
bidding. Land subdivision was the sole `CONDITIONAL` record, reflecting a
white-collar-heavy external-service subset whose actual eligibility remains
uncertain. No construction code reached `PRIORITY` or an unconditional Stage 2
action.

Fourteen records reached `LOW_PRIORITY`, including selected infrastructure,
building, and specialty trades where estimating, project controls, scheduling,
dispatch, procurement, and administration offer focused AI leverage around an
operator-required field service. Sixteen were `STRUCTURAL_OUT`, generally
because hands-on craft labor dominated payroll, savings were likely to pass
through in rebidding, transferable firm pools were thin or owner-dependent, or
the nominal code mixed own-account development with external contracting. All
records nevertheless had a base tier; none was gap-routed.

Validators' caveats emphasized broad task and adoption proxies, limited direct
evidence on implemented labor savings, estimated eligible-firm shares, sparse
qualifying-transfer denominators, and uncertainty over retained benefit after
competitive rebidding. One cited industry AI page could not be reopened, but
the affected primitives were already explicit estimates and the correction did
not change the base tier or action. No review found a material defect, and the
predeclared pause trigger did not fire.

## G2 — Transportation and warehousing

**Closed:** 2026-07-22
**Coverage:** 57 attempted, 57 deterministically valid, 57 published, 0 excluded
**Independent review:** 9/57 (2 mandatory, 6 random, 1 canary)
**Review outcomes:** 9 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 1 `HIGHEST_PRIORITY`, 1 `PRIORITY`, 13 `CONDITIONAL`,
  16 `LOW_PRIORITY`, 22 `STRUCTURAL_OUT`, and 4 without a base tier.
- Readiness: 53 `MODEL_CONDITIONED`; 4 `STRESS_TEST_ONLY`.
- Actions: 53 `VALIDATE_ASSUMPTIONS`; 4 `EVIDENCE_FIRST`.
- Robust tiers: 7/57, all `STRUCTURAL_OUT`.
- Publication labels: 9 `accepted`; 48 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `481212`, `483111`, `485310`, `487110`,
`488310`, and `488410`. All six were accepted with caveats and carried no
material finding. The previously reviewed canary `484110` also closed with the
block. These are sample observations only; no G2 defect rate is estimated.

### Economic read

The screen sharply separated standardized warehousing workflows from transport
modes dominated by regulated physical operation, public ownership, thin firm
pools, or competitive pass-through. General warehousing and storage was the
block's sole `HIGHEST_PRIORITY` record, and refrigerated warehousing reached
`PRIORITY`. Both combine large repeat physical and information workflows with
identifiable software, robotics, and decision-support applications while the
custody and storage service remains operator-required.

Thirteen records reached `CONDITIONAL`, mainly selected passenger services,
transit, support activities, towing, couriers, and residual warehousing where
dispatch, planning, documentation, inspection, or coordination creates a
meaningful digital layer. Twenty-two were `STRUCTURAL_OUT`, reflecting very
small or nontransferable operator pools, safety-critical labor, cost-plus or
public contracting, platform displacement, or weak retention of productivity
gains. Line-haul and short-line railroads, deep-sea passenger transport, and
postal service had no base tier and correctly routed to `STRESS_TEST_ONLY /
EVIDENCE_FIRST` because firm or transfer denominators were missing.

Validators' caveats emphasized broad modal and occupational proxies,
assumption-heavy implementation and retention bridges, sparse direct LMM
transfer evidence, public or captive ownership, and uncertainty over whether
contract repricing passes savings to customers. One Census archive page could
not be reopened, but the affected industry-boundary caveat did not alter the
record's already conservative evidence states, tier, or action. No review found
a material defect, and the predeclared pause trigger did not fire.

## G3 — Wholesale trade

**Closed:** 2026-07-22
**Coverage:** 69 attempted, 69 deterministically valid, 69 published, 0 excluded
**Independent review:** 8/69 (0 mandatory, 7 random, 1 canary)
**Review outcomes:** 8 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 0 `HIGHEST_PRIORITY`, 0 `PRIORITY`, 0 `CONDITIONAL`,
  7 `LOW_PRIORITY`, 61 `STRUCTURAL_OUT`, and 1 without a base tier.
- Readiness: 68 `MODEL_CONDITIONED`; 1 `STRESS_TEST_ONLY`.
- Actions: 68 `VALIDATE_ASSUMPTIONS`; 1 `EVIDENCE_FIRST`.
- Robust tiers: 39/69, all `STRUCTURAL_OUT`.
- Publication labels: 8 `accepted`; 61 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `423140`, `423420`, `423930`, `424210`,
`424410`, `424610`, and `424720`. All seven were accepted with caveats and
carried no material finding. The previously reviewed canary `423840` also
closed with the block. These are sample observations only; no G3 defect rate is
estimated.

### Economic read

The screen was highly conservative across a block dominated by physical
inventory, handling, fulfillment, and commodity pass-through. No wholesale
code reached `CONDITIONAL` or better. Photographic, office, other professional,
refrigeration, and service-establishment equipment wholesalers; book and
periodical wholesalers; and wholesale trade agents and brokers were the seven
`LOW_PRIORITY` records. Their repeat information, sales, procurement, and
coordination workflows created meaningful AI exposure, but physical delivery,
thin qualifying-transfer pools, channel displacement, or weak retention kept
the opportunity below the higher tiers.

Sixty-one records were `STRUCTURAL_OUT`, usually because the weakest-link labor
factor remained below threshold despite substantial administrative
automation potential. Clothing and clothing-accessories wholesalers had no base
tier and correctly routed to `STRESS_TEST_ONLY / EVIDENCE_FIRST` because a
required dataset anchor was unavailable. The pattern is economically
informative: wholesale workflows may adopt AI broadly without producing a
large, durable, transferable lower-middle-market labor-arbitrage opportunity.

Validators' caveats emphasized broad occupation and subsector proxies,
judgmental implementation, eligibility, transfer, retention, and demand
bridges, selected transaction examples without denominators, and large-company
evidence that may not represent independent LMM firms. Several dynamic Census
definition pages did not expose the claimed code-specific text on reopening,
and one PDF was inaccessible, but the affected inputs were already disclosed
as proxy or estimate evidence. No correction or honest downgrade changed a
base tier or action, no review found a material defect, and the predeclared
pause trigger did not fire.

## G4 — Retail trade

**Closed:** 2026-07-22
**Coverage:** 57 attempted, 57 deterministically valid, 57 published, 0 excluded
**Independent review:** 7/57 (0 mandatory, 6 random, 1 canary)
**Review outcomes:** 7 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 0 `HIGHEST_PRIORITY`, 0 `PRIORITY`, 0 `CONDITIONAL`,
  1 `LOW_PRIORITY`, 9 `STRUCTURAL_OUT`, and 47 without a base tier.
- Readiness: 10 `MODEL_CONDITIONED`; 47 `STRESS_TEST_ONLY`.
- Actions: 10 `VALIDATE_ASSUMPTIONS`; 47 `EVIDENCE_FIRST`.
- Robust tiers: 17/57, all `STRUCTURAL_OUT`.
- Publication labels: 7 `accepted`; 50 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `441330`, `445131`, `445320`, `455110`,
`456191`, and `459999`. All six were accepted with caveats and carried no
material finding. The previously reviewed canary `445110` also closed with the
block. These are sample observations only; no G4 defect rate is estimated.

### Economic read

The block was economically uninformative for ranking most retail industries
because 47 of 57 records lacked the required firm-count anchor and therefore
correctly published without a base tier as `STRESS_TEST_ONLY / EVIDENCE_FIRST`.
That gap-routing dominated specialty, general-merchandise, health, apparel,
fuel, and miscellaneous retail; the resulting records remain provisional
evidence packages rather than ranked opportunities.

Among the ten records with complete anchors, paint and wallpaper retailers was
the sole `LOW_PRIORITY` result. New and used car dealers, recreational-vehicle
and boat dealers, home centers, supermarkets, and selected specialty food
retailers were `STRUCTURAL_OUT`. Physical inventory and fulfillment, narrow
eligible service tails, low transfer incidence, channel competition, and weak
retention constrained the screen even where ordering, pricing, forecasting,
customer service, and administration offered meaningful AI exposure. No retail
record reached `CONDITIONAL` or better.

Validators' caveats emphasized broad occupation mixes rather than wage-weighted
six-digit task evidence, unmeasured eligible service tails, owner-age proxies
without qualifying-transfer denominators, nominal or adjacent-market demand
bridges, and large-chain technology examples that may not represent LMM
operators. Several client-rendered Census definitions could not be fully
reopened, and one aggregate-series endpoint differed slightly, but these issues
were nonmaterial to already disclosed proxy/estimate states or to records
deterministically gap-routed by missing firm counts. No review found a material
defect, and the predeclared pause trigger did not fire.

## G5 — Manufacturing: food, beverage, textiles, apparel, and leather

**Closed:** 2026-07-22
**Coverage:** 69 attempted, 69 deterministically valid, 69 published, 0 excluded
**Independent review:** 8/69 (0 mandatory, 7 random, 1 canary)
**Review outcomes:** 8 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 0 `HIGHEST_PRIORITY`, 0 `PRIORITY`, 0 `CONDITIONAL`,
  15 `LOW_PRIORITY`, 50 `STRUCTURAL_OUT`, and 4 without a base tier.
- Readiness: 65 `MODEL_CONDITIONED`; 4 `STRESS_TEST_ONLY`.
- Actions: 65 `VALIDATE_ASSUMPTIONS`; 4 `EVIDENCE_FIRST`.
- Robust tiers: 25/69, all `STRUCTURAL_OUT`.
- Publication labels: 8 `accepted`; 61 `not_reviewed` by the frozen sampling
  contract.

The random stratum consisted of `311119`, `311213`, `311225`, `311352`,
`311811`, `312112`, and `313320`. All seven were accepted with caveats and
carried no material finding. The previously reviewed canary `311612` also
closed with the block. These are sample observations only; no G5 defect rate is
estimated.

### Economic read

The screen was conservative in industries where value creation remains tied to
physical conversion, food safety, quality control, plant throughput, and
commodity or retailer bargaining. Fifteen records reached `LOW_PRIORITY`,
including poultry and seafood processing, retail bakeries and tortillas,
ice, beer, and wine production, and selected textile, apparel-contracting, and
footwear activities. These cases offered useful planning, scheduling,
inspection, formulation, merchandising, or administrative workflows, but not
enough transferable and retainable labor benefit for a higher tier.

Fifty records were `STRUCTURAL_OUT`, spanning most primary food processing,
packaged foods, dairy, slaughter, beverages, tobacco, and capital-intensive
textile operations. Cane sugar, apparel knitting, noncontract cut-and-sew
apparel, and other leather products lacked a required anchor and correctly
routed to `STRESS_TEST_ONLY / EVIDENCE_FIRST`. No record reached
`CONDITIONAL` or better.

Validators' caveats emphasized broader-industry occupation and adoption
proxies, judgmental eligible-firm and five-year implementation shares, sparse
qualifying-transfer denominators, selected large-plant examples, and demand
bridges that mix nominal revenue, end-market growth, and constant-quality
quantity. Evidence consistently supported automation direction more strongly
than the magnitude or retention of LMM labor savings. These limitations were
disclosed in proxy or estimate states; no review found a tier- or action-changing
defect, and the predeclared pause trigger did not fire.

## G6 — Manufacturing: wood through nonmetallic minerals

**Closed:** 2026-07-22
**Coverage:** 96 attempted, 96 deterministically valid, 96 published, 0 excluded
**Independent review:** 10/96 (0 mandatory, 10 random, 0 canary)
**Review outcomes:** 10 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 0 `HIGHEST_PRIORITY`, 0 `PRIORITY`, 1 `CONDITIONAL`,
  18 `LOW_PRIORITY`, 74 `STRUCTURAL_OUT`, and 3 without a base tier.
- Readiness: 93 `MODEL_CONDITIONED`; 3 `STRESS_TEST_ONLY`.
- Actions: 93 `VALIDATE_ASSUMPTIONS`; 3 `EVIDENCE_FIRST`.
- Robust tiers: 33/96, all `STRUCTURAL_OUT`.
- Publication labels: 10 `accepted`; 86 `not_reviewed`.

The random stratum consisted of `321212`, `321219`, `323117`, `323120`,
`324191`, `325194`, `325212`, `325413`, `326122`, and `326299`.
All ten were accepted with caveats and no material finding. These are sample
observations only; no G6 defect rate is estimated.

### Economic read

The largest block remained strongly physical and process-bound: 74 records
were `STRUCTURAL_OUT`, 18 were `LOW_PRIORITY`, and only one reached
`CONDITIONAL`. Three missing-anchor records correctly routed to
`STRESS_TEST_ONLY / EVIDENCE_FIRST`. Planning, formulation, inspection,
maintenance, and administration offered automation potential, but plant,
materials, safety, and throughput constraints limited transferable retained
labor benefit.

Validators emphasized broad occupation and subsector proxies, estimated
implementation and eligibility, sparse transfer denominators, and indirect
demand and retention bridges. All limitations were disclosed; no review found
a tier- or action-changing defect, and the predeclared pause trigger did not
fire.

## G7 — Manufacturing: primary metals, fabricated metals, and machinery

**Closed:** 2026-07-22
**Coverage:** 89 attempted, 89 deterministically valid, 89 published, 0 excluded
**Independent review:** 10/89 (0 mandatory, 9 random, 1 canary)
**Review outcomes:** 10 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 0 `HIGHEST_PRIORITY`, 0 `PRIORITY`, 12 `CONDITIONAL`,
  37 `LOW_PRIORITY`, 37 `STRUCTURAL_OUT`, and 3 without a base tier.
- Readiness: 86 `MODEL_CONDITIONED`; 3 `STRESS_TEST_ONLY`.
- Actions: 86 `VALIDATE_ASSUMPTIONS`; 3 `EVIDENCE_FIRST`.
- Robust tiers: 9/89, all `STRUCTURAL_OUT`.
- Publication labels: 10 `accepted`; 79 `not_reviewed`.

The random stratum was `332420`, `332722`, `332913`, `332993`,
`333310`, `333511`, `333618`, `333995`, and `333996`; all were
accepted with caveats and no material finding. Canary `332710` also closed.
These are sample observations only; no G7 defect rate is estimated.

### Economic read

G7 was more differentiated than preceding manufacturing blocks: twelve
records reached `CONDITIONAL` and 37 `LOW_PRIORITY`, reflecting repeatable
engineering, quoting, scheduling, inspection, maintenance, and machine-control
workflows around still-essential plants and operators. Thirty-seven records
remained `STRUCTURAL_OUT`; three missing-anchor records routed to
`STRESS_TEST_ONLY / EVIDENCE_FIRST`. No record reached `PRIORITY`.

Validators emphasized broad occupation and adoption proxies, estimated
implementation and eligible-firm shares, sparse transfer denominators, and
indirect benefit-retention and demand bridges. These limitations were
disclosed; no review found a tier- or action-changing defect, and the pause
trigger did not fire.

## G8 — Manufacturing: electronics through miscellaneous

**Closed:** 2026-07-22
**Coverage:** 92 attempted, 92 deterministically valid, 92 published, 0 excluded
**Independent review:** 12/92 (3 mandatory, 9 random, 0 canary)
**Review outcomes:** 12 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 0 `HIGHEST_PRIORITY`, 3 `PRIORITY`, 20 `CONDITIONAL`,
  34 `LOW_PRIORITY`, 28 `STRUCTURAL_OUT`, and 7 without a base tier.
- Readiness: 85 `MODEL_CONDITIONED`; 7 `STRESS_TEST_ONLY`.
- Actions: 85 `VALIDATE_ASSUMPTIONS`; 7 `EVIDENCE_FIRST`.
- Robust tiers: 7/92, all `STRUCTURAL_OUT`.
- Publication labels: 12 `accepted`; 80 `not_reviewed`.

The mandatory stratum was `334118`, `334412`, and `334413`; the random
stratum was `334111`, `334419`, `334513`, `334514`, `335929`, `336213`,
`336390`, `336412`, and `336991`. All were accepted with caveats and no
material finding. These are sample observations only; no G8 defect rate is
estimated.

### Economic read

G8 produced the campaign's first three `PRIORITY` manufacturing screens:
computer peripherals (`334118`), bare printed circuit boards (`334412`), and
semiconductors (`334413`). Twenty additional records reached `CONDITIONAL`,
concentrated in electronics, controls, instruments, medical devices, and
selected miscellaneous manufacturing where digitized design, testing,
inspection, quoting, and production data support multiple AI workflows.
Thirty-four records were `LOW_PRIORITY`, 28 were `STRUCTURAL_OUT`, and seven
missing-anchor records routed to `STRESS_TEST_ONLY / EVIDENCE_FIRST`.

Validators emphasized broad occupation and adoption proxies, estimated
implementation and eligible-firm shares, sparse transfer denominators, and
indirect retention and demand bridges. The three mandatory anomaly reviews
also passed without a tier- or action-changing defect. All limitations were
disclosed, and the predeclared pause trigger did not fire.

## G9 — Mining and utilities

**Closed:** 2026-07-22
**Coverage:** 35 attempted, 35 deterministically valid, 35 published, 0 excluded
**Independent review:** 4/35 (0 mandatory, 4 random, 0 canary)
**Review outcomes:** 4 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 0 `HIGHEST_PRIORITY`, 0 `PRIORITY`, 3 `CONDITIONAL`,
  11 `LOW_PRIORITY`, 15 `STRUCTURAL_OUT`, and 6 without a base tier.
- Readiness: 29 `MODEL_CONDITIONED`; 6 `STRESS_TEST_ONLY`.
- Actions: 29 `VALIDATE_ASSUMPTIONS`; 6 `EVIDENCE_FIRST`.
- Robust tiers: 7/35, all `STRUCTURAL_OUT`.
- Publication labels: 4 `accepted`; 31 `not_reviewed`.

The random stratum was `212290`, `221116`, `221118`, and `221330`; all were
accepted with caveats and no material finding. These are sample observations
only; no G9 defect rate is estimated.

### Economic read

G9 did not produce a `PRIORITY` screen. Construction sand and gravel mining
(`212321`), solar generation (`221114`), and other electric generation
(`221118`) reached `CONDITIONAL`, while eleven records were `LOW_PRIORITY` and
fifteen were `STRUCTURAL_OUT`. Six missing-anchor mining records routed to
`STRESS_TEST_ONLY / EVIDENCE_FIRST`, reflecting the block's sparse and
heterogeneous operating base rather than a tuned outcome.

Validators emphasized broad workforce and adoption proxies, estimated
implementation and eligible-firm shares, indirect demand and retention
bridges, and sector-level evidence applied to narrow industries. These
limitations were disclosed; no review found a tier- or action-changing defect,
and the predeclared pause trigger did not fire.

## Z1 — Agriculture, forestry, fishing, and hunting

**Closed:** 2026-07-22
**Coverage:** 64 attempted, 64 deterministically valid, 64 published, 0 excluded
**Independent review:** 9/64 (1 mandatory, 7 random, 1 canary)
**Review outcomes:** 9 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 0 `HIGHEST_PRIORITY`, 1 `PRIORITY`, 6 `CONDITIONAL`,
  2 `LOW_PRIORITY`, 5 `STRUCTURAL_OUT`, and 50 without a base tier.
- Readiness: 14 `MODEL_CONDITIONED`; 50 `STRESS_TEST_ONLY`.
- Actions: 14 `VALIDATE_ASSUMPTIONS`; 50 `EVIDENCE_FIRST`.
- Robust tiers: 2/64, both `STRUCTURAL_OUT`.
- Publication labels: 9 `accepted`; 55 `not_reviewed`.

The mandatory stratum was `115116`; the random stratum was `111320`,
`111419`, `112340`, `112410`, `112920`, `113210`, and `114112`; canary
`111998` was also included. All were accepted with caveats and no material
finding. These are sample observations only; no Z1 defect rate is estimated.

### Economic read

Z1 behaved as the declared gap-heavy block. Forty-nine records lacked the
frozen dataset anchor, and one additional record (`114119`) lacked sufficient
research evidence, leaving 50 records at `STRESS_TEST_ONLY / EVIDENCE_FIRST`.
Among the fourteen model-conditioned records, farm management services
(`115116`) reached `PRIORITY`; six support-activity industries reached
`CONDITIONAL`, two were `LOW_PRIORITY`, and five were `STRUCTURAL_OUT`.

Validators emphasized broad workforce and adoption proxies, estimated
implementation and eligible-firm shares, indirect retention and demand
bridges, and sector evidence applied to narrow farm-support industries. The
one-record difference from the predeclared 49 dataset gaps was transparently
caused by an additional evidence gap, not outcome tuning. No review found a
tier- or action-changing defect, and the predeclared pause trigger did not
fire.

## Z2 — Public administration

**Closed:** 2026-07-22
**Coverage:** 29 attempted, 29 deterministically valid, 29 published, 0 excluded
**Independent review:** 4/29 (0 mandatory, 3 random, 1 canary)
**Review outcomes:** 4 `publishable_with_caveats`; 0 `publishable`; 0 `reject`; 0 `invalid`
**Material findings:** 0
**Remediations:** 0

### Screen distribution

- Base tiers: 29 without a base tier; no scored tier assignments.
- Readiness: 29 `STRESS_TEST_ONLY`.
- Actions: 29 `EVIDENCE_FIRST`.
- Robust tiers: 0/29.
- Publication labels: 4 `accepted`; 25 `not_reviewed`.

The random stratum was `922150`, `923110`, and `926130`; canary `921190`
was also included. All were accepted with caveats and no material finding.
These are sample observations only; no Z2 defect rate is estimated.

### Economic read

As predeclared, Z2 was economically uninformative as a scored roll-up screen:
all 29 public-administration records lacked the frozen private-firm dataset
anchor and therefore routed to `STRESS_TEST_ONLY / EVIDENCE_FIRST`. The
records still preserve sourced workflow and market observations for a future
dataset upgrade, but none receives a base tier.

Validators emphasized the public/private boundary, broad government-wide
proxies, missing transfer or retention evidence, and the inapplicability of
private-firm economics to many records. These limitations were disclosed; no
review found a tier- or action-changing defect, and the predeclared pause
trigger did not fire.
