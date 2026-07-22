# 623210 — Residential Intellectual and Developmental Disability Facilities

*v5.1 Stage 1 research memo. Run `623210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.50 · L 0.94 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Essential recurring care, aging caregivers, and severe frontline labor scarcity make administrative relief valuable even when substitution is modest.
**Weakness:** Hands-on care dominates wages, while public reimbursement and quality obligations sharply limit labor removal and commercial retention.

## Business-model lens
- Included: United States lower-middle-market operators providing recurring residential care to people with intellectual and developmental disabilities through group homes, intermediate care facilities, and related staffed residential settings, with room, board, protective supervision, habilitation, counseling, and incidental health care.
- Excluded: Nonresidential day programs, home-care agencies without a residential operation, residential mental-health or substance-use treatment, skilled nursing, state-operated facilities, shell entities, captive units, and non-control financing vehicles.
- Customer and revenue model: Residents and families are the service recipients, while Medicaid agencies and managed-care plans are major payers. Revenue is recurring and commonly paid through fixed per-diem, per-unit, tiered, bundled, or negotiated rates tied to assessed need, with separate resident funds or other payers sometimes covering room and food.
- Deviation from default lens: none

## Executive view
Residential I/DD care is a recurring, essential, and highly accountable service, but its labor base is dominated by hands-on aides rather than automatable office work. AI can ease documentation and coordination burden; Medicaid pricing, nonprofit ownership, and stringent care obligations constrain both addressable labor and retained value.

## How AI changes the work
Useful applications include shift scheduling, training support, policy retrieval, incident and progress-note drafting, billing checks, care-plan preparation, family communication, and monitoring triage. Direct supervision, personal care, de-escalation, community participation, medication support, and safeguarding remain human work.

## Value capture
Fixed prospective rates can preserve some savings between rate reviews, especially in administration. Capture is limited by state rate setting, managed-care negotiation, cost reporting, direct-care compensation policy, workforce scarcity, and the practical need to reinvest in staff stability and service quality.

## Firm availability
Disability-services transactions and residential I/DD add-ons demonstrate a buyer market, while aging business owners create succession supply. The investable set is narrowed by nonprofit and public ownership, mixed-service organizations, licensing, property arrangements, payer enrollment, and care-quality scrutiny.

## Demand durability
Underlying need is durable because people with I/DD live longer and family caregivers age. Funding and workforce capacity restrict realized volume, and the service mix continues moving away from institutions toward community settings, favoring small group homes and supported living over congregate facilities.

## Risks and uncertainty
The main uncertainties are the task mix within the broad aide category, state-by-state Medicaid rates, whether savings must be passed to wages or payers, the portion of private firms that can transfer, and whether community integration moves demand to services outside this NAICS code. Quality failures create severe human, regulatory, and reputational risk.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4909 | — | OBSERVED | — |
| n | — | 1572 | — | ESTIMATE | — |
| a | 0.09 | 0.16 | 0.25 | PROXY | S1, S2, S5, S10 |
| rho | 0.18 | 0.3 | 0.45 | PROXY | S5, S6 |
| e | 0.5 | 0.68 | 0.82 | ESTIMATE | S1, S9, S10 |
| s5 | 0.1 | 0.18 | 0.28 | PROXY | S7, S8, S9 |
| q | 0.24 | 0.38 | 0.55 | PROXY | S6, S10 |
| d5 | 0.94 | 1.02 | 1.13 | PROXY | S2, S3, S4, S6, S9 |
| o | 0.78 | 0.88 | 0.96 | ESTIMATE | S1, S3, S4, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.32 | 0.94 | 2.21 | PROXY |
| F | 7.04 | 8.47 | 9.48 | ESTIMATE |
| C | 4.80 | 7.60 | 10.00 | PROXY |
| D | 7.33 | 8.98 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation shares do not measure task-level AI exposure.
- a: The industry lacks a dedicated direct-support-professional occupation code, so aides span varied duties and acuity.
- rho: Public initiatives emphasize home and community care broadly rather than this exact NAICS industry.
- rho: Technology pilots do not establish durable labor removal.
- e: The best ownership evidence covers intermediate care facilities, only one part of the industry.
- e: Nonprofit asset transactions and management conversions may not qualify as ordinary control transfers.
- s5: The deal series combines I/DD, autism, home care, and other disability services.
- s5: Gallup measures stated plans rather than completed transactions.
- q: Payment methods and rebasing practices differ materially by state and waiver.
- q: The New Jersey audit describes one nonprofit provider and should not be generalized mechanically.
- d5: Employment is an input proxy rather than a direct constant-quality demand measure.
- d5: HCBS statistics combine populations and services outside residential I/DD care.
- o: Operator requirement is distinct from the number of labor hours the operator needs.
- o: Policy can shift service volume outside the facility lens even when recipients still need human support.

## Sources
- **S1** — [2022 NAICS Definition: 623210 Residential Intellectual and Developmental Disability Facilities](https://www.census.gov/naics/?details=62&input=62&year=2022) (accessed 2026-07-22): Industry boundary, facility types, and the room, board, supervision, counseling, and incidental-health-care service basket.
- **S2** — [BLS National Employment Matrix for Industry 623210](https://data.bls.gov/projections/nationalMatrix?ioType=i&queryParams=623210) (accessed 2026-07-22): Detailed industry occupation mix and projected industry employment change.
- **S3** — [Medicaid Home and Community Based Services](https://www.medicaid.gov/medicaid/home-community-based-services) (accessed 2026-07-22): Scale of HCBS use and spending and policy preference for home and community settings over institutions.
- **S4** — [Supporting Adults with Intellectual and Developmental Disabilities and Their Aging Caregivers](https://www.medicaid.gov/medicaid/home-community-based-services/home-community-based-services-guidance-additional-resources/supporting-adults-intellectual-and-developmental-disabilities-and-their-aging-caregivers) (accessed 2026-07-22): Aging-caregiver population, community-living trend, and expected demand for Medicaid-funded services.
- **S5** — [ACL Launches Caregiver AI Prize Competition](https://www.hhs.gov/press-room/acl-launches-phase-1-caregiver-ai-prize-competition.html) (accessed 2026-07-22): Emerging AI applications for caregiver documentation, monitoring, scheduling, training, and workforce support.
- **S6** — [Medicaid Payment Policies to Support the Home and Community-Based Services Workforce](https://www.macpac.gov/wp-content/uploads/2026/03/Chapter-1-Medicaid-Payment-Policies-to-Support-the-Home-and-Community-Based-Services-Workforce.pdf) (accessed 2026-07-22): Medicaid payer role, workforce shortage, rate methods, rate components, state variation, and direct-care compensation policy.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year sale and transfer intentions among United States employer-business owners.
- **S8** — [Private Equity Healthcare Deals: 2024 in Review](https://pestakeholder.org/reports/healthcare-deals-2024-in-review/) (accessed 2026-07-22): Disability-services transaction activity and identified acquisitions of residential I/DD providers.
- **S9** — [Intermediate Care Facilities for Individuals With Intellectual Disabilities: Does Ownership Type Affect Quality of Care?](https://law.stanford.edu/wp-content/uploads/2022/12/Intermediate_Care_Facilities_for_Individuals_With_Intellectual_Disabilities-_Does_Ownership_Type_Affect_Quality_of_Care_.pdf) (accessed 2026-07-22): Ownership mix, facility-size differences, long-run institutional decline, continuing residential need, and quality-data limitations in an industry subset.
- **S10** — [New Jersey Office of the State Comptroller Closing Report on Community Options](https://www.nj.gov/comptroller/reports/2026/20260225.shtml) (accessed 2026-07-22): Group-home operating duties, licensed-provider accountability, per-diem tiered billing, payer scale, documentation, and one provider's cost allocation.
