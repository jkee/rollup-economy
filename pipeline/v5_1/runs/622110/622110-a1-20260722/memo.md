# 622110 — General Medical and Surgical Hospitals

*v5.1 Stage 1 research memo. Run `622110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.70 · L 1.38 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Fixed-case reimbursement and data-rich hospital workflows create room for AI-assisted documentation, revenue-cycle, scheduling, and capacity gains while inpatient demand remains operator-required.
**Weakness:** Most clinical labor remains physical and accountable, and the apparent LMM firm universe is heavily blurred by nonprofit governance, system ownership, public facilities, and hospital-scale economics.

## Business-model lens
- Included: Lower-middle-market hospital operating firms repeatedly providing inpatient diagnostic, medical, surgical, nursing, accommodation, and related outpatient services to external patients and payers through a transferable operating business.
- Excluded: Government-owned hospitals, captive or non-control hospital campuses within systems, shell or real-estate-only entities, physician offices, outpatient centers, psychiatric and substance-abuse hospitals, other specialty hospitals, and operators outside the lower-middle-market EBITDA band.
- Customer and revenue model: Recurring patient episodes reimbursed by Medicare, Medicaid, commercial insurers, employers, and patients through case-based prospective payments, negotiated rates, fee schedules, bundled arrangements, and limited cost-based or supplemental payments.
- Deviation from default lens: none

## Executive view
General hospitals offer a real but bounded AI opportunity in documentation, revenue cycle, scheduling, decision support, capacity, and operational coordination. The service itself remains capital-intensive, regulated, physically delivered, and clinically accountable. The investable population is the central uncertainty: the code contains many nonprofit, government, system-owned, or economically large facilities that do not map cleanly to a transferable LMM firm.

## How AI changes the work
AI can draft and summarize clinical documentation, prioritize worklists, support coding and denials, forecast census and staffing, optimize operating-room and bed schedules, review supply use, flag deterioration, and assist patient communication. Clinicians still must examine, counsel, diagnose, treat, administer medications, operate equipment, perform procedures, respond to emergencies, and own final decisions. Existing predictive-AI adoption also means part of the apparent exposure is already automated rather than remaining opportunity.

## Value capture
Prospective case payments and negotiated rates can let hospitals retain verified cost or throughput gains during a rate period. Capture erodes through annual public-payer updates, commercial negotiations, utilization review, quality penalties, shared savings, mandated staffing, and the need to reinvest in cybersecurity, integration, clinical validation, and service capacity. Savings that prevent burnout or preserve beds may be economically valuable without appearing as direct payroll reduction.

## Firm availability
Hospitals continue to transact, often because of financial distress, scale needs, or system strategy. A qualifying target needs transferable licenses, payer contracts, medical-staff relationships, real estate, service-line economics, and governance, with normalized EBITDA in band. Nonprofit membership structures, system affiliation, public ownership, debt, pension obligations, malpractice exposure, and deferred capital sharply reduce the clean target pool represented by the frozen count.

## Demand durability
Population aging, chronic disease, emergencies, and rising acuity support durable need for inpatient care, while CMS projects continued hospital-spending growth. Real inpatient quantity should grow more slowly than nominal spending because care keeps shifting to ambulatory, home, and virtual settings and because price and intensity explain part of expenditure growth. Local demographics, payer mix, physician alignment, and bed supply matter more than the national average.

## Risks and uncertainty
A hospital can destroy value through weak payer contracts, physician leakage, nurse shortages, quality failures, cyber incidents, underfunded capital needs, service-line losses, compliance liabilities, or a closure-prone local market. AI adds hallucination, bias, alert fatigue, privacy, and malpractice risks. The main screen-level measurement problem is that establishment counts and broad margin bridges do not reveal which hospitals are independent, transferable, recurring-service LMM businesses.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3573 | — | OBSERVED | — |
| n | — | 1130 | — | ESTIMATE | — |
| a | 0.12 | 0.23 | 0.35 | PROXY | S2, S3 |
| rho | 0.24 | 0.42 | 0.6 | PROXY | S4 |
| e | 0.18 | 0.36 | 0.56 | ESTIMATE | S1, S5 |
| s5 | 0.04 | 0.09 | 0.18 | PROXY | S5, S6 |
| q | 0.3 | 0.48 | 0.65 | PROXY | S7 |
| d5 | 0.96 | 1.08 | 1.2 | PROXY | S1, S8 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.41 | 1.38 | 3.00 | PROXY |
| F | 3.56 | 5.83 | 7.63 | ESTIMATE |
| C | 6.00 | 9.60 | 10.00 | PROXY |
| D | 8.64 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Published BLS occupation counts do not measure time by task or current automation within NAICS 622110.
- a: The LMM independent-hospital occupation mix may differ from the national industry mix because small hospitals outsource some specialist and administrative functions.
- a: Clinical documentation may be AI-assistable without reducing licensed staffing ratios or bedside coverage.
- rho: Predictive-AI adoption is not the same as labor substitution or full workflow implementation.
- rho: The HealthIT.gov population is nonfederal acute-care hospitals of all sizes, not the frozen LMM firm lens.
- rho: Already-deployed predictive models do not belong in the remaining opportunity measured by a.
- e: Hospital ownership, establishment, certification, and firm boundaries do not align cleanly.
- e: Nonprofit control can transfer through membership substitution or affiliation without a conventional equity sale.
- e: The supplied n value is margin-bridged from broad public data and may include system campuses or entities whose economics cannot transfer independently.
- s5: Announced hospital-system transactions have no denominator aligned to independent LMM 622110 firms.
- s5: A transaction may cover many hospitals or only a parent entity and may not represent a separately qualifying business transfer.
- s5: Distress can cause closure or public rescue rather than an investable control transfer.
- q: Medicare IPPS does not describe the full commercial, Medicaid, self-pay, and supplemental-payment mix.
- q: Payment form does not directly measure the discounted share of AI benefits retained.
- q: Some benefits increase capacity, quality, or clinician retention rather than reducing reported expense.
- d5: CMS national expenditure projections are nominal and cover hospital care broadly rather than NAICS 622110 LMM operators.
- d5: Constant-quality inpatient quantity is difficult to separate from rising acuity, technology, and prices.
- d5: Demand varies sharply between growing urban markets and rural or over-bedded markets.
- o: The estimate concerns operator requirement after demand changes, not the amount of labor automation inside the hospital.
- o: Hospital-at-home preserves accountable clinical operation but may move revenue and assets outside a traditional hospital facility.
- o: Different service lines have materially different site-of-care substitution potential.

## Sources
- **S1** — [U.S. Census Bureau — 2022 NAICS Manual: General Medical and Surgical Hospitals](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 622110 as licensed general medical and surgical hospitals providing inpatient diagnostic and medical treatment with beds, organized medical staff, and related outpatient, laboratory, imaging, operating-room, and pharmacy services; describes specialized hospital facilities and equipment.
- **S2** — [BLS — May 2024 OEWS Industry Employment Charts](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Lists the largest occupations in general medical and surgical hospitals, including 1,843,130 registered nurses, 425,740 nursing assistants, 195,930 medical secretaries and administrative assistants, 155,670 medical and health services managers, and major laboratory, imaging, physician, respiratory, and pharmacy roles.
- **S3** — [BLS Occupational Outlook Handbook — Registered Nurses](https://www.bls.gov/ooh/healthcare/registered-nurses.htm) (accessed 2026-07-22): Describes nursing duties spanning assessment, documentation, observation, care planning, coordination, medication and treatment administration, equipment operation, testing, education, physical work, and round-the-clock hospital coverage.
- **S4** — [HealthIT.gov — Hospital Trends in the Use, Evaluation, and Governance of Predictive AI, 2023–2024](https://healthit.gov/data/data-briefs/hospital-trends-use-evaluation-and-governance-predictive-ai-2023-2024/) (accessed 2026-07-22): Reports 71% predictive-AI adoption among responding nonfederal acute-care hospitals in 2024, 37% adoption among independent hospitals versus 86% among system-affiliated hospitals, use in inpatient risk, billing, and scheduling, and incomplete evaluation across all models.
- **S5** — [American Hospital Association — Fast Facts on U.S. Hospitals, 2026](https://www.aha.org/statistics/fast-facts-us-hospitals) (accessed 2026-07-22): Reports 6,100 U.S. hospitals and 5,121 community hospitals, including 2,984 nongovernment nonprofit, 1,224 investor-owned, and 913 state and local government community hospitals, with 3,567 community hospitals in systems.
- **S6** — [Kaufman Hall — Hospital and Health System M&A Activity Ends 2025 With Momentum](https://www.kaufmanhall.com/news/hospital-and-health-system-ma-activity-ends-2025-momentum) (accessed 2026-07-22): Reports 46 announced hospital and health-system transactions in 2025, $18.5 billion of transacted revenue, stronger fourth-quarter activity, and a record 43.5% of transactions involving a financially distressed party.
- **S7** — [CMS — Inpatient Prospective Payment System](https://www.cms.gov/cms-guide-medical-technology-companies-and-other-interested-parties/payment/ipps) (accessed 2026-07-22): Explains that acute inpatient hospital payment is generally predetermined per discharge under MS-DRGs and based on average resource use rather than the specific cost of each individual case, subject to wage and other adjustments.
- **S8** — [CMS — National Health Expenditure Projections 2025–2034](https://www.cms.gov/files/document/nhe-projections-infographic.pdf) (accessed 2026-07-22): Projects average annual nominal hospital-care spending growth of 5.7% from 2025 through 2034 and shows hospital care remaining about 31% of national health expenditures.
