# 623110 — Nursing Care Facilities (Skilled Nursing Facilities)

*v5.1 Stage 1 research memo. Run `623110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.52 · L 1.62 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Core output requires recurring physical nursing and personal care that AI software is unlikely to eliminate over five years.
**Weakness:** Much of the quantified evidence is proxied from broader healthcare, Medicare fee-for-service, facility-level ownership, or broader 623100 employment rather than direct operator-level 623110 measurements.

## Business-model lens
- Included: Recurring or repeat outsourced external services sold to operators of inpatient nursing and rehabilitation facilities providing skilled nursing, post-acute rehabilitation, and long-term nursing and personal care.
- Excluded: Assisted-living or continuing-care communities without a separately operated nursing facility, residential psychiatric or intellectual-disability facilities, home health, captive internal service departments, real-estate ownership and financing shells, and one-time construction or equipment sales.
- Customer and revenue model: Customers are skilled nursing and nursing-facility operators spanning independent, chain, nonprofit, public, and health-system ownership. Operator revenue commonly combines Medicare post-acute per-diem reimbursement, Medicaid long-stay reimbursement, managed-care contracts, and private pay; external services are purchased through recurring contracts, subscriptions, per-resident arrangements, or repeat project work.
- Deviation from default lens: none

## Executive view
Nursing facilities combine unusually durable, place-based care output with a real but bounded opportunity to improve documentation, assessment, scheduling, billing, and administrative workflows. The sector is heterogeneous: post-acute Medicare rehabilitation, long-stay Medicaid care, payer mix, chain affiliation, and local regulation materially change economics and service purchasing.

## How AI changes the work
The credible five-year AI opportunity is concentrated around MDS and clinical documentation, coding, records review, care-plan preparation, scheduling, claims, and centralized administration. Hands-on nursing and personal care dominate employment and remain constrained by resident contact, licensure, judgment, safety, and staffing rules.

## Value capture
Predetermined or administered reimbursement can let operators retain some efficiency within rate periods, particularly through avoided agency labor, reduced denials, and more efficient administrative capacity. Capture is limited by Medicaid and managed-care bargaining, rate rebasing, quality programs, compliance obligations, and the practical likelihood that time savings fill staffing gaps or improve care.

## Firm availability
The operator universe includes independents and multi-facility platforms, with active ownership transfer but a material distinction between facilities, operating companies, ultimate owners, and real-estate entities. Chain-centralized functions, captive health-system operations, nonprofit or public ownership, and related-party structures narrow the eligible external-service market.

## Demand durability
Aging supports long-term care need, while home- and community-based alternatives and lower Medicare post-acute admissions pressure facility volume. Recent occupancy recovery and longer Medicare stays temper that downside, so a near-flat central outlook carries a wide range rather than a strong directional claim.

## Risks and uncertainty
The largest uncertainties are the absence of skilled-nursing-specific task-time and AI productivity studies, the translation from facility ownership changes to firm sales, payer-mix effects on savings retention, fragmented technology adoption, regulatory and privacy exposure, labor shortages, and continued substitution toward care outside institutions.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5628 | — | OBSERVED | — |
| n | — | 2883 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.29 | PROXY | S2, S3, S4 |
| rho | 0.22 | 0.4 | 0.6 | PROXY | S3, S4 |
| e | 0.48 | 0.68 | 0.84 | ESTIMATE | S1, S9, S10 |
| s5 | 0.1 | 0.16 | 0.24 | PROXY | S8 |
| q | 0.27 | 0.48 | 0.67 | PROXY | S6, S7, S9 |
| d5 | 0.84 | 0.98 | 1.1 | PROXY | S7, S11 |
| o | 0.94 | 0.98 | 0.995 | PROXY | S1, S5, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.50 | 1.62 | 3.92 | PROXY |
| F | 7.94 | 9.25 | 10.00 | ESTIMATE |
| C | 5.40 | 9.60 | 10.00 | PROXY |
| D | 7.90 | 9.60 | 10.00 | PROXY |

## Caveats
- a: BLS 623100 includes a broader nursing and residential-care population than 623110 and reports employment, not task-time shares.
- a: GAO evidence spans healthcare settings rather than skilled nursing facilities specifically.
- a: Exposure is not equivalent to realized labor removal because documentation is coupled to regulated clinical workflows and review.
- rho: Published healthcare AI outcomes may not transfer to the staffing, software, and reimbursement environment of nursing facilities.
- rho: Time savings may be absorbed by compliance improvement or unmet care needs rather than reducing paid labor.
- rho: The range excludes speculative physical robotics and autonomous clinical decisions.
- e: No direct source measures the share of LMM operating firms eligible for the defined external-service lens.
- e: Facility counts and owner records do not map one-to-one to operating firms.
- e: Real-estate ownership and operating control can be split across related entities.
- s5: The 2016-2021 transfer window predates the current five-year outlook and includes pandemic disruption.
- s5: PECOS ownership changes may include reorganizations or asset transfers rather than arm's-length firm sales.
- s5: The bridge assumes a roughly stable annual hazard only to form a proxy.
- q: Medicare and Medicaid payment rules vary by resident, state, plan, and service and do not directly reveal retained savings.
- q: Quality reporting and value-based payment can offset nominal savings when outcomes deteriorate.
- q: Labor shortages may cause efficiency to improve coverage rather than reduce expense.
- d5: MedPAC utilization figures focus on Medicare fee-for-service, not total industry resident-days.
- d5: The post-acute and long-stay segments can move in different directions.
- d5: CBO's demographic discussion is directionally useful but old and not a five-year facility forecast.
- o: This primitive deliberately excludes general home- and community-based substitution already reflected in d5.
- o: Robotics could affect selected physical tasks, but broad autonomous deployment in frail-resident care is not evidenced here.
- o: Regulatory staffing requirements may preserve labor inputs even where technology becomes capable.

## Sources
- **S1** — [2022 NAICS Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 623110 as establishments providing inpatient nursing and rehabilitative services, generally with a permanent core of registered or licensed practical nurses and continuous personal care.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 623100](https://www.bls.gov/oes/2023/may/naics4_623100.htm) (accessed 2026-07-22): Reports 1,379,430 workers and the occupational mix, including nursing assistants at 33.25%, LPN/LVNs at 12.42%, RNs at 9.01%, and office and administrative support at 4.91%.
- **S3** — [Artificial Intelligence in Health Care: Applications, Benefits, and Challenges](https://www.gao.gov/products/gao-26-109116) (accessed 2026-07-22): Describes AI use in clinical notes and coding, increased clinician use for documentation and coding, a cited 20% documentation-time reduction, and accuracy, cost, privacy, and oversight constraints.
- **S4** — [Minimum Data Set Frequency](https://data.cms.gov/quality-of-care/minimum-data-set-frequency) (accessed 2026-07-22): Describes MDS as a federally mandated assessment for residents of Medicare- or Medicaid-certified nursing homes, completed at admission, periodically, and at discharge and transmitted electronically.
- **S5** — [CMS Staffing Study to Inform Minimum Staffing Requirements for Nursing Homes](https://www.cms.gov/newsroom/blog/centers-medicare-medicaid-services-staffing-study-inform-minimum-staffing-requirements-nursing-homes) (accessed 2026-07-22): States existing federal requirements for 24-hour licensed nursing services, an RN for at least eight consecutive hours daily seven days a week, and facility assessments sufficient to meet resident needs.
- **S6** — [Medicare Payment Systems](https://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/html/medicare-payment-systems.html) (accessed 2026-07-22): Explains that the SNF prospective payment system pays a predetermined per diem covering routine, ancillary, and capital-related costs under Part A.
- **S7** — [Skilled Nursing Facility Services: Assessing Payment Adequacy and Updating Payments](https://www.medpac.gov/wp-content/uploads/2025/12/Tab-F-SNF-update-Dec-2025.pdf) (accessed 2026-07-22): Reports roughly 14,400 SNFs, Medicare at 8% of median facility days, 2024 admissions down 4% while days rose 1%, provider counts down 1%, occupancy at 83%, and continued investor interest.
- **S8** — [Changes in Ownership of Hospital and Skilled Nursing Facilities: An Analysis of Newly-Enrolled Medicare Providers](https://aspe.hhs.gov/sites/default/files/documents/4d960147d5fd8e2ea9af508f115ca7b7/aspe-datapoint-change-ownership-pecos.pdf) (accessed 2026-07-22): Finds 3,236 skilled nursing facilities were sold during 2016-2021 and that roughly 3.5% of SNFs were sold annually, providing a facility-level transfer proxy.
- **S9** — [Nursing Facilities](https://www.medicaid.gov/medicaid/long-term-services-supports/institutional-long-term-care/nursing-facilities) (accessed 2026-07-22): Describes nursing-facility nursing, rehabilitation, and long-term care services; Medicaid coverage requirements; multiple payer arrangements; and policy support for transitions to community settings.
- **S10** — [Skilled Nursing Facility All Owners](https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/skilled-nursing-facility-all-owners) (accessed 2026-07-22): Provides monthly PECOS-derived records of all owners of currently enrolled skilled nursing facilities, supporting the distinction among facilities, operators, and owners.
- **S11** — [Rising Demand for Long-Term Services and Supports for Elderly People](https://www.cbo.gov/publication/44363) (accessed 2026-07-22): Explains that population aging increases long-term-services need while nursing-home use had declined as home- and community-based alternatives expanded.
