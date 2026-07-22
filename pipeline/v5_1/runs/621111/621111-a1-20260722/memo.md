# 621111 — Offices of Physicians (except Mental Health Specialists)

*v5.1 Stage 1 research memo. Run `621111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 8.36 · L 3.45 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High-cost clinical and administrative information work creates avoidable hiring and throughput potential while the practice remains the accountable service operator.
**Weakness:** Broad AI use is not evidence of realized labor removal, and the remaining transferable firm pool is obscured by consolidation, specialty variation, and owner dependence.

## Business-model lens
- Included: US physician-owned, sponsor-owned, and other transferable physician practices that repeatedly provide non-mental-health professional medical services to patients and payers, including office-based and facility-based professional services when the practice is the billing operating entity.
- Excluded: Mental-health-specialist offices classified elsewhere; hospital departments or other captive internal units without a separately transferable operating business; shell entities; non-control financing vehicles; and firms outside the frozen lower-middle-market EBITDA band.
- Customer and revenue model: Practices serve patients as the clinical customers while collecting chiefly from commercial insurers and public payers through fee-for-service schedules, supplemented by capitation, shared savings, bundled payments, performance payments, and patient cost sharing.
- Deviation from default lens: none

## Executive view
Physician practices combine a large wage base with repeat patient demand and a sizable layer of document, coding, access, inbox, and revenue-cycle work. The opportunity is operational rather than autonomous-clinical: AI can compress information work and avoid hiring, while licensed clinicians and billable entities remain responsible for most of the service basket. The main uncertainties are whether tool use becomes durable labor redesign and how many attractive practices remain independently transferable.

## How AI changes the work
The clearest uses are ambient and downstream documentation, chart summarization, coding support, patient-message drafting, translation, prior authorization, scheduling, and work-queue triage. Clinical summarization and assistive diagnosis can raise throughput, but examination, procedures, final judgment, and accountability are much less substitutable. Current physician adoption is broad, yet observed use is not the same as realized payroll savings.

## Value capture
Fee-for-service remains the majority revenue source, so internal productivity gains are not automatically passed through when realized. Retention can erode through public fee updates, commercial renewal pressure, local competition, and alternative-payment reconciliation; CMS's explicit efficiency adjustment shows that payers can eventually incorporate assumed productivity. Specialty and local bargaining power will dominate the realized result.

## Firm availability
Small private practices remain numerous, and reported corporate acquisitions show a live transfer market. At the same time, physician ownership and solo practice have declined, corporate consolidation has already removed some inventory, and many small entities depend heavily on owner goodwill. Firm-level ownership, EBITDA, and transaction data are needed before treating the frozen count as actionable supply.

## Demand durability
Demographic and utilization evidence supports stable to modestly growing physician-service quantity. Insurance losses, site-of-care shifts, team-based care, and productivity can restrain the current office basket, but diagnosis, treatment, procedures, and prescribing are unlikely to become software-only at scale within five years. AI is more likely to alter the production function than eliminate the accountable practice.

## Risks and uncertainty
The industry code hides major specialty differences in task mix, capital intensity, reimbursement, referral concentration, and acquisition appetite. AI can add review work or safety risk instead of removing labor; privacy, EHR integration, validation, and liability may slow deployment. Reimbursement cuts can absorb savings, and regulatory ownership restrictions or nonassignable payer contracts can impede transfers. A bad case is a heavily consolidated local market where the remaining firms are owner-dependent, weakly contracted, and unable to convert AI assistance into vacancies avoided.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5409 | — | OBSERVED | — |
| n | — | 14540 | — | ESTIMATE | — |
| a | 0.2 | 0.29 | 0.38 | PROXY | S1, S2, S3 |
| rho | 0.35 | 0.55 | 0.72 | PROXY | S3 |
| e | 0.72 | 0.82 | 0.92 | PROXY | S4 |
| s5 | 0.08 | 0.14 | 0.22 | PROXY | S4 |
| q | 0.5 | 0.68 | 0.82 | ESTIMATE | S5, S6 |
| d5 | 0.98 | 1.04 | 1.1 | PROXY | S7, S8 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S9, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.51 | 3.45 | 5.92 | PROXY |
| F | 10.00 | 10.00 | 10.00 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.82 | 9.98 | 10.00 | ESTIMATE |

## Caveats
- a: The available OEWS page is 2023 and NAICS 621100, so it is broader than the target code and includes mental-health physician offices.
- a: Occupation-level task mapping cannot distinguish augmentation from true substitution or avoided hiring.
- a: Specialty mix matters greatly: diagnostic, procedural, and primary-care practices carry different clinical and administrative task profiles.
- a: The frozen labor ratio l=0.5409 uses 2024 wages over 2022 receipts and an IPS harmonization divisor; its vintage mismatch and harmonization affect the downstream labor opportunity even though a is independently estimated here.
- rho: The AMA survey is physician-reported and spans practice settings, ownership forms, and specialties rather than only LMM NAICS 621111 firms.
- rho: Reported use can mean occasional assistance and does not demonstrate cost removal, headcount avoidance, or durable workflow adoption.
- rho: Privacy, cybersecurity, EHR integration, clinical validation, and unresolved liability can delay implementation after a tool appears technically capable.
- e: The AMA Benchmark Survey is physician-weighted, not firm-weighted, and excludes physicians providing less than 20 hours of patient care per week and federal physicians.
- e: A practice can be clinically viable but have substantial personal goodwill, restrictive ownership rules, or payer-contract assignment barriers that reduce practical eligibility.
- e: The frozen n=14540 is an ESTIMATE margin-bridged with a 15.80% public Hospitals/Healthcare Facilities EBITDA margin; specialty-level physician-office margins may differ materially.
- s5: The acquisition-timing denominator contains only physicians in currently corporate-owned practices and is subject to recall, survivor, and size weighting biases.
- s5: A physician's move from ownership to employment is not necessarily a qualifying transfer of a standalone operating firm.
- s5: Deal incidence differs substantially by specialty, geography, payer mix, ancillary assets, and state corporate-practice-of-medicine restrictions.
- q: No source directly measures how much AI-enabled labor savings physician practices retain over five years.
- q: Revenue mix and negotiating leverage vary sharply by specialty, local concentration, ownership, and payer mix.
- q: The estimate excludes volume effects, implementation difficulty, and valuation effects as required; those belong in other primitives.
- d5: Neither employment nor nominal spending is the target constant-price, constant-quality quantity measure.
- d5: The target NAICS spans specialties with different demographics, technology substitution, and site-of-care trends.
- d5: Coverage losses and payer policy can suppress paid utilization even when underlying medical need rises.
- o: There is no direct measure of the share of year-five physician-office quantity that will require the same kind of accountable operator.
- o: Operator requirement does not imply that every task must be performed by a physician; advanced practitioners, centralized teams, and software can change staffing while leaving the practice accountable.
- o: Regulation, payer policy, and liability can change faster than historical clinical workflows.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 621100 Offices of Physicians](https://www.bls.gov/oes/2023/may/naics4_621100.htm) (accessed 2026-07-22): Actual page tables show 2,842,350 total jobs; healthcare practitioners and technical occupations at 45.24% of employment and $158,340 mean annual wage; physicians at 13.41% and $293,860; surgeons at 1.34% and $364,100; office and administrative support at 26.73% and $43,630.
- **S2** — [Doctors work fewer hours, but the EHR still follows them home](https://www.ama-assn.org/practice-management/physician-health/doctors-work-fewer-hours-ehr-still-follows-them-home) (accessed 2026-07-22): Actual page content reports a 57.8-hour physician workweek in 2024, including 27.2 hours of direct patient care, 13.0 hours of indirect patient care, and 7.3 hours of administrative tasks.
- **S3** — [2026 Physician Survey on Augmented Intelligence](https://www.ama-assn.org/system/files/physician-ai-sentiment-report.pdf) (accessed 2026-07-22): Fetched report content shows 81% physician awareness or use in 2026; use-case shares including 39% research summaries, 30% discharge or care-plan creation, and 28% each for documentation and chart summaries; it also reports privacy, validation, training, and liability constraints.
- **S4** — [Physician Practice Characteristics in 2024: Private Practices Account for Less Than Half of Physicians in Most Specialties](https://www.ama-assn.org/system/files/2024-prp-pp-characteristics.pdf) (accessed 2026-07-22): Fetched report content shows 42.2% of physicians in private practice, 47% in practices with 10 or fewer physicians, 35.4% with an ownership stake, and acquisition timing including 15.1% of physicians in corporate-owned practices reporting purchase after 2019.
- **S5** — [Alternative Payment and Delivery Models: A Decade in Review Shows Stagnant Growth Between 2014 and 2024](https://www.ama-assn.org/system/files/2024-prp-aco-apm.pdf) (accessed 2026-07-22): Fetched report content shows 2024 practice revenue shares of 67.7% fee-for-service and 32.3% alternative payment methods, with 82.8% of physicians reporting at least some fee-for-service payment.
- **S6** — [Calendar Year 2026 Medicare Physician Fee Schedule Final Rule](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-medicare-physician-fee-schedule-final-rule-cms-1832-f) (accessed 2026-07-22): Actual CMS page content explains administered physician-office payment and finalizes a 2.5% efficiency adjustment for many non-time-based services, with specified time-based exemptions.
- **S7** — [Physicians and Surgeons: Occupational Outlook Handbook](https://www.bls.gov/ooh/healthcare/physicians-and-surgeons.htm) (accessed 2026-07-22): Actual BLS page content projects 3% physician and surgeon employment growth from 2024 to 2034 and 23,600 openings per year.
- **S8** — [National Health Expenditure Projections 2025-2034: Forecast Summary](https://www.cms.gov/files/document/nhe-projections-forecast-summary.pdf) (accessed 2026-07-22): Fetched forecast shows projected average nominal physician and clinical services spending growth of 5.5% from 2025 to 2034 and identifies utilization, coverage, Medicare aging, and demographic drivers.
- **S9** — [Clinical Decision Support Software: Guidance for Industry and FDA Staff](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software) (accessed 2026-07-22): Actual FDA page content states that only certain clinical decision-support functions meet non-device criteria and that device software, including functions intended for patients or caregivers, remains subject to digital-health policies.
- **S10** — [Advanced Practice Registered Nurses](https://www.cms.gov/medicare/payment/fee-schedules/physician-fee-schedule/advanced-practice-non-physician-practitioners/advanced-practice-registered-nurses-aprns) (accessed 2026-07-22): Actual CMS page content sets licensure, certification, medical-necessity, personal-performance, billing-identity, collaboration, and supervision requirements for Medicare-covered advanced-practice services.
