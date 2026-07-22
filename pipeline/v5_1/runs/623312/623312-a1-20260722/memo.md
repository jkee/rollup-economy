# 623312 — Assisted Living Facilities for the Elderly

*v5.1 Stage 1 research memo. Run `623312-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.20 · L 1.62 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A predominantly for-profit operator base serves rising, high-acuity residential demand under recurring monthly pricing, with active control transaction evidence.
**Weakness:** Most labor is hands-on care and hospitality, so administrative AI gains are bounded and can be absorbed by staffing, compliance, and quality demands.

## Business-model lens
- Included: Operators of assisted-living facilities, homes for the elderly, and rest homes without on-site nursing facilities that provide recurring room, board, supervision, housekeeping, and assistance with daily living to residents.
- Excluded: Continuing-care communities or assisted-living facilities with on-site nursing facilities, standalone skilled-nursing facilities, independent apartments without personal care, nonresidential home-care agencies, captive housing, passive real-estate vehicles without operations, and non-control financing interests.
- Customer and revenue model: Residents or families pay recurring monthly charges for housing, meals, supervision, personal assistance, housekeeping, activities, and related services, commonly with care-level add-ons. Some residents receive Medicaid support, but the market is substantially private pay and operators reset rates for new residents and through periodic fee increases.
- Deviation from default lens: none

## Executive view
Assisted living provides recurring housing, hospitality, supervision, and personal assistance to an aging population. Demand and transaction evidence are strong, and for-profit ownership makes control pathways more ordinary than in continuing-care communities. AI opportunity is real but bounded because frontline personal care, dining, housekeeping, and safety response dominate the labor base.

## How AI changes the work
Near-term uses center on admissions, lead handling, billing, payroll, staff scheduling, procurement, care documentation, family communication, facilities workflow, and exception detection. AI may reduce administrative burden and avoid some hiring, but it cannot perform most activities-of-daily-living assistance or replace the human accountability expected in a residential setting.

## Value capture
Recurring monthly pricing, resident tenure, and relocation friction allow some savings to remain with the operator. Retention is moderated by local competition, annual fee decisions, Medicaid exposure, referral reputation, resident and family scrutiny, and the need to reinvest in staffing and service quality.

## Firm availability
Residential care is predominantly for-profit, and assisted living has become a leading category in an active senior-care transaction market. The key diligence issue is converting facility activity into unique qualifying firm transfers because portfolios, REIT structures, management agreements, and real-estate-only sales can create misleading deal counts.

## Demand durability
Occupancy has risen while construction and inventory growth remain limited, and population aging supports continued need. Affordability and home-based alternatives are meaningful constraints, but residents with several daily-living limitations still require coordinated housing, meals, supervision, and hands-on support that software cannot supply alone.

## Risks and uncertainty
Material risks include state-by-state licensing, staffing shortages and wage pressure, resident safety and abuse liability, property age and capital expenditure, local supply cycles, affordability, Medicaid reimbursement, shallow AI governance, and confusing a facility or real-estate transfer with control of an eligible operator firm.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4946 | — | OBSERVED | — |
| n | — | 926 | — | ESTIMATE | — |
| a | 0.14 | 0.2 | 0.28 | PROXY | S2 |
| rho | 0.27 | 0.41 | 0.58 | PROXY | S3, S4 |
| e | 0.69 | 0.84 | 0.94 | PROXY | S1, S5 |
| s5 | 0.06 | 0.11 | 0.18 | PROXY | S5, S9, S10 |
| q | 0.48 | 0.65 | 0.8 | PROXY | S7, S8 |
| d5 | 1 | 1.12 | 1.25 | PROXY | S7, S11 |
| o | 0.86 | 0.94 | 0.98 | PROXY | S1, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.75 | 1.62 | 3.21 | PROXY |
| F | 5.91 | 7.18 | 8.14 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | PROXY |
| D | 8.60 | 10.00 | 10.00 | PROXY |

## Caveats
- a: The available occupation table combines two six-digit industries and all employer sizes.
- a: Task exposure within each occupation is inferred rather than directly measured.
- a: Documentation assistance may improve care time without reducing required headcount.
- rho: The AI survey is not-for-profit and broader than 623312.
- rho: EHR adoption is enabling infrastructure, not evidence of AI substitution.
- rho: Small assisted-living operators may have less integration capacity than surveyed multisite organizations.
- e: CDC's residential care definition includes personal-care, board-care, and adult foster-care settings outside 623312.
- e: The injected firm count relies on a healthcare-facilities margin bridge that may not fit small residential operators.
- e: For-profit ownership does not prove that a firm is independent, in the LMM band, or available for control.
- s5: The annual transaction source combines senior housing and skilled nursing and gives an assisted-living share only for one quarter.
- s5: JAMA measures PE acquisitions rather than all qualifying buyers and ends in 2023.
- s5: The facility denominator is broader than 623312 and is not an eligible-firm denominator.
- q: NIC reports market asking rates rather than realized in-place rates or automation savings.
- q: Retention varies with local occupancy, payer mix, care acuity, and resident contract terms.
- q: No direct contractual pass-through study was found.
- d5: NIC's primary-market sample is not the full national 623312 universe.
- d5: Recent occupancy gains include recovery from pandemic disruption.
- d5: Demographic growth does not directly measure affordability or preference for assisted living.
- o: The CDC resident study includes residential care settings beyond 623312.
- o: Current residents have higher demonstrated need than prospective marginal residents.
- o: Home-based substitution can remove demand before admission even when software cannot replace facility operations.

## Sources
- **S1** — [NAICS Sector 62 — Health Care and Social Assistance](https://www.census.gov/naics/resources/archives/sect62.html) (accessed 2026-07-22): Defines 623312 as residential and personal care without on-site nursing facilities, including room, board, supervision, housekeeping, and assistance in daily living, and provides adjacent-industry exclusions.
- **S2** — [May 2023 OEWS — Continuing Care Retirement Communities and Assisted Living Facilities for the Elderly](https://www.bls.gov/oes/2023/may/naics4_623300.htm) (accessed 2026-07-22): Provides employment shares and wages by occupation for combined NAICS 623300, including healthcare support, food service, facilities, clinical, management, sales, and office work.
- **S3** — [2025 Ziegler Link-age Funds and LeadingAge CAST CTO Hotline](https://leadingage.org/wp-content/uploads/2025/09/Ziegler-Linkage-LeadingAge-CAST-CTO-Hotline_FINAL.pdf) (accessed 2026-07-22): Measures AI competency and deployment confidence, automation plans by workflow, data governance, and implementation barriers among not-for-profit senior-living and care organizations.
- **S4** — [CDC QuickStats — Electronic Health Record Use in Residential Care Communities](https://www.cdc.gov/mmwr/volumes/73/wr/mm7317a6.htm) (accessed 2026-07-22): Reports that electronic-health-record use among residential care communities increased from 36% in 2018 to 48% in 2022 and was higher among larger communities.
- **S5** — [CDC FastStats — Residential Care Communities](https://www.cdc.gov/nchs/fastats/residential-care-communities.htm) (accessed 2026-07-22): Reports 32,200 communities, 1,313,600 licensed beds, 988,800 residents, and 81.5% for-profit ownership in 2022 for the broader residential-care population.
- **S6** — [Residential Care Community Resident Characteristics: United States, 2022](https://www.cdc.gov/nchs/products/databriefs/db506.htm) (accessed 2026-07-22): Measures resident age, payer status, chronic conditions, and need for assistance with activities of daily living across U.S. residential care communities.
- **S7** — [NIC — Occupancy Rate for Senior Living Communities Increased in 2025 as Construction Stalled](https://www.nic.org/news-press/occupancy-rate-for-senior-living-communities-increased-in-2025-as-construction-stalled/) (accessed 2026-07-22): Reports 2025 occupancy gains, assisted-living occupancy of 87.7%, occupied-unit growth above 3%, limited inventory growth, and affordability constraints in primary markets.
- **S8** — [NIC CCRC Performance — Fourth Quarter 2025](https://www.nic.org/blog/ccrc-performance-4q-2025/) (accessed 2026-07-22): Reports non-CCRC assisted-living asking-rate growth of 4.5% and inventory growth of 1.1%, providing pricing and supply evidence for assisted-living properties.
- **S9** — [2025 Seniors Housing and Care M&A Activity Smashes Multiple Records](https://www.levinassociates.com/2025-seniors-housing-and-care-ma-activity-smashes-multiple-records/) (accessed 2026-07-22): Reports 871 publicly disclosed transactions in 2025, the senior-housing share, and assisted living as the largest fourth-quarter deal category.
- **S10** — [Trends in Private Equity Acquisitions of Assisted Living Facilities](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2841451) (accessed 2026-07-22): Documents controlling PE acquisitions of assisted-living facilities, deal and facility counts, single-facility prevalence, geographic reach, and undercount limitations.
- **S11** — [Demographic Turning Points for the United States: Population Projections for 2020 to 2060](https://www.census.gov/library/publications/2020/demo/p25-1144.html) (accessed 2026-07-22): Documents the expansion of the older population as the baby-boom cohort ages through the screen horizon.
