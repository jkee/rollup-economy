# 622210 — Psychiatric and Substance Abuse Hospitals

*v5.1 Stage 1 research memo. Run `622210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.84 · L 0.65 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent high-acuity behavioral-health need and prospective daily reimbursement support selective AI gains in documentation, intake, utilization, scheduling, and discharge workflows.
**Weakness:** Core work depends on human therapeutic judgment and continuous safety supervision, while the true transferable LMM inpatient target pool is obscured by government, nonprofit, system-unit, outpatient, and residential boundaries.

## Business-model lens
- Included: Lower-middle-market licensed psychiatric and substance-abuse hospital operating firms repeatedly providing inpatient diagnostic, medical treatment, monitoring, nursing, psychiatric, psychological, social-work, and related services to external patients and payers through a transferable operation.
- Excluded: Government-owned hospitals, captive or non-control units within general hospitals or larger systems, outpatient-only mental health and substance-abuse centers, counseling-led residential facilities without hospital-level medical treatment, intellectual-disability residential facilities, shell or real-estate-only entities, and operators outside the lower-middle-market EBITDA band.
- Customer and revenue model: Recurring admissions and patient days reimbursed by Medicare, Medicaid, commercial insurers, public purchasers, employers, and patients through prospective per-diem systems, negotiated daily or case rates, fee schedules, bundled arrangements, and limited cost-based or supplemental payments.
- Deviation from default lens: none

## Executive view
Psychiatric and substance-abuse hospitals have targeted AI opportunities in documentation, intake, coding, utilization review, discharge coordination, scheduling, quality reporting, and risk support. Core care remains relationship-intensive, licensed, physical, and safety-critical. Demand is durable, but the investable LMM population and transfer rate are uncertain because government, nonprofit, system-unit, outpatient, residential, and facility-versus-firm boundaries overlap.

## How AI changes the work
AI can summarize histories, draft notes and care-plan updates, structure intake, flag missing documentation, support coding and denials, coordinate discharge resources, forecast census and staffing, and assist risk review. It cannot safely replace therapeutic relationships, continuous observation, medication administration, vital-sign monitoring, withdrawal management, de-escalation, restraint, or accountable decisions about suicide, violence, and discharge. False reassurance and biased risk scores are especially consequential.

## Value capture
Prospective daily and case rates allow an operator to retain some verified process savings during a contract period. Capture erodes through payer authorization and length-of-stay management, annual public rate updates, commercial renewals, quality reporting, staffing requirements, and reinvestment in scarce clinicians, security, privacy, and model governance. Benefits may appear as safer coverage, fewer denials, or added capacity rather than direct headcount reduction.

## Firm availability
Broad behavioral-health M&A is active, but published deal growth is driven largely by outpatient counseling and psychiatric care. A qualifying inpatient target needs transferable licenses, payer contracts, medical leadership, beds, real estate, compliant staffing, clean quality history, and normalized EBITDA in band. Government ownership, nonprofit control, distinct-part units, certificate-of-need rules, investigations, patient-safety liabilities, and workforce dependence narrow the true pool.

## Demand durability
Behavioral-health workforce projections and rapid projected growth for psychiatric technicians and aides point to persistent need, and severe crises and medically managed withdrawal retain an inpatient role. Paid inpatient volume will grow more slowly than broad need if care shifts to outpatient, residential, crisis, or telehealth settings, or if bed and clinician shortages suppress admissions. Local payer authorization, public budgets, bed capacity, and referral networks determine realized demand.

## Risks and uncertainty
A facility becomes unattractive if it depends on one public payer, lacks psychiatrists or nurses, faces restraint, seclusion, abuse, billing, or quality investigations, has weak referral relationships, or owns obsolete and hard-to-secure real estate. AI can amplify bias, miss suicide or violence risk, breach sensitive data, and produce unsafe documentation. The largest measurement uncertainty is translating broad facility, workforce, and M&A evidence into standalone LMM hospital firms.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2775 | — | OBSERVED | — |
| n | — | 208 | — | ESTIMATE | — |
| a | 0.1 | 0.19 | 0.3 | PROXY | S2, S3 |
| rho | 0.14 | 0.31 | 0.49 | PROXY | S4, S7 |
| e | 0.3 | 0.5 | 0.7 | ESTIMATE | S1, S5, S7 |
| s5 | 0.06 | 0.13 | 0.25 | PROXY | S5, S6 |
| q | 0.24 | 0.42 | 0.61 | PROXY | S7 |
| d5 | 0.92 | 1.07 | 1.21 | PROXY | S3, S8 |
| o | 0.86 | 0.94 | 0.99 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.16 | 0.65 | 1.63 | PROXY |
| F | 2.50 | 4.30 | 5.83 | ESTIMATE |
| C | 4.80 | 8.40 | 10.00 | PROXY |
| D | 7.91 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation counts do not measure task time, wages by task, or current automation within the frozen firm lens.
- a: Psychiatric hospitals and substance-abuse hospitals may have materially different staffing, acuity, length of stay, and security needs.
- a: AI assistance to documentation may improve care time without permitting lower licensed or observation staffing.
- rho: The predictive-AI adoption source covers nonfederal acute-care hospitals, not psychiatric and substance-abuse hospitals.
- rho: Use of a model does not establish broad implementation, labor substitution, or acceptable safety performance.
- rho: CMS quality reporting requirements add digital workflow opportunities but also preserve human validation and compliance work.
- e: CMS inpatient psychiatric facility populations include psychiatric units inside acute-care hospitals that are not standalone 622210 firms.
- e: Nonprofit governance and membership transfers differ from conventional equity control sales.
- e: The supplied n value is a margin-bridged estimate and may misclassify facility units, system entities, or operators with atypical payer mixes.
- s5: The transaction series has no denominator aligned to LMM psychiatric and substance-abuse hospital firms.
- s5: Most cited counseling and psychiatric-care deals were outpatient and do not establish inpatient hospital liquidity.
- s5: Publicly announced transaction counts can omit small private deals and include multi-site platforms as one event.
- q: Medicare IPF payment does not describe the full Medicaid, commercial, public-contract, and self-pay mix.
- q: Per-diem payment can reward lower daily cost but also creates exposure if efficiency changes length of stay or authorization behavior.
- q: Payment form is not direct evidence of the discounted share of AI benefits retained.
- d5: BLS employment growth is not a direct forecast of constant-quality hospital service quantity and includes replacement and staffing effects.
- d5: HRSA models behavioral-health provider demand across settings rather than NAICS 622210 inpatient utilization.
- d5: Unmet clinical need may remain unpaid or unserved because of workforce, bed, payer, and public-budget constraints.
- o: The estimate concerns whether surviving demand needs an accountable operator, not how much labor AI can assist inside that operator.
- o: Site-of-care substitution differs sharply between severe psychiatric crises, detoxification, rehabilitation, and lower-acuity conditions.
- o: Remote monitoring may supplement inpatient staff but does not remove licensure, custody, medication, and safety accountability.

## Sources
- **S1** — [U.S. Census Bureau — 2022 NAICS Manual: Psychiatric and Substance Abuse Hospitals](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 622210 as licensed psychiatric and substance-abuse hospitals providing inpatient diagnostic, medical treatment, and monitoring, often for extended stays, with beds, organized medical staff, and psychiatric, psychological, and social-work services; distinguishes outpatient and residential facilities.
- **S2** — [BLS — May 2024 OEWS Industry Employment Charts](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Lists the largest occupations in psychiatric and substance-abuse hospitals, including 41,760 registered nurses, 30,420 psychiatric technicians, 17,530 substance-abuse and mental-health counselors, 14,180 psychiatric aides, 8,640 mental-health and substance-abuse social workers, and major nursing, management, and human-service roles.
- **S3** — [BLS Occupational Outlook Handbook — Psychiatric Technicians and Aides](https://www.bls.gov/ooh/healthcare/psychiatric-technicians-and-aides.htm) (accessed 2026-07-22): Describes observation and recording, therapeutic activities, medication, intake and discharge, vital signs, daily-living assistance, safety monitoring, escort, cleaning, and restraint duties; projects 16% employment growth from 2024 to 2034.
- **S4** — [HealthIT.gov — Hospital Trends in the Use, Evaluation, and Governance of Predictive AI, 2023–2024](https://healthit.gov/data/data-briefs/hospital-trends-use-evaluation-and-governance-predictive-ai-2023-2024/) (accessed 2026-07-22): Reports 71% predictive-AI adoption among responding nonfederal acute-care hospitals in 2024, 37% among independent hospitals versus 86% among system-affiliated hospitals, growing billing and scheduling uses, and incomplete evaluation across all models.
- **S5** — [American Hospital Association — Fast Facts on U.S. Hospitals, 2026](https://www.aha.org/statistics/fast-facts-us-hospitals) (accessed 2026-07-22): Reports 656 nonfederal psychiatric hospitals and provides ownership and system-affiliation context for the wider U.S. hospital population.
- **S6** — [LevinPro HC / GlobeNewswire — Behavioral Health Care M&A Activity Increases 42% in 2025](https://www.globenewswire.com/news-release/2026/01/13/3218180/0/en/behavioral-health-care-m-a-activity-increases-42-in-2025.html) (accessed 2026-07-22): Reports 104 publicly announced behavioral-health transactions in 2025 versus 73 in 2024, including 52 counseling and psychiatric-care deals, while identifying outpatient mental-health services and talk therapy as the main driver.
- **S7** — [CMS — FY 2025 Inpatient Psychiatric Facility PPS Final Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/fiscal-year-2025-medicare-inpatient-psychiatric-facilities-prospective-payment-system-ipf-pps-and-0) (accessed 2026-07-22): Describes IPF prospective payment, patient-level adjustments for MS-DRG, comorbidities, age, and variable per diem, annual rate updates, outliers, quality reporting, cost data, and payment refinements.
- **S8** — [HRSA Bureau of Health Workforce — Behavioral Health Care Provider Model Components](https://bhw.hrsa.gov/data-research/projecting-health-workforce-supply-demand/technical-documentation/behavioral-health-care-provider) (accessed 2026-07-22): Publishes behavioral-health demand adjustment scalars rising from 100% in 2023 to 116.92% in 2028 for the combined adult-and-child population and explains status-quo and unmet-need workforce demand scenarios, including a starting psychiatrist shortfall.
