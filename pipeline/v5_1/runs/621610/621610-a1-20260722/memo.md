# 621610 — Home Health Care Services

*v5.1 Stage 1 research memo. Run `621610-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.44 · L 3.63 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can remove meaningful documentation and coordination burden from a large recurring home-based care workforce under partly bundled reimbursement.
**Weakness:** Hands-on care, travel, clinical accountability, payer oversight, and workforce scarcity limit substitutable labor and complicate implementation.

## Business-model lens
- Included: US lower-middle-market home health agencies providing recurring or repeat skilled nursing, therapy, home health aide, home infusion, in-home hospice, medical social, and related clinical services in patients' homes to external patients and payers.
- Excluded: Nonmedical homemaker and companion services classified outside 621610, independent practitioner offices, equipment-only rental or retail, facility-based care, captive internal programs, shells, and non-control financing vehicles.
- Customer and revenue model: Patients receive episodic or ongoing home-based clinical care ordered under plans of care; agencies are paid by Medicare, Medicare Advantage, Medicaid, commercial insurers, health systems, or private pay through prospective 30-day bundles, per-visit rates, case rates, or contracted fee schedules.
- Deviation from default lens: none

## Executive view
Home health combines a large hands-on clinical workforce with documentation-heavy, centralized administrative workflows. AI can improve intake, scheduling, coding, care-plan review, monitoring, and clinician documentation, while most direct nursing, therapy, infusion, and aide visits remain physically and legally operator-dependent.

## How AI changes the work
AI can summarize referrals and records, draft notes and care plans, support OASIS and coding review, predict scheduling gaps, optimize routes, flag deterioration, automate routine patient communication, and assist quality audits. Clinicians and aides still travel, observe the home, touch and move patients, administer care, exercise licensed judgment, and own escalation decisions.

## Value capture
Prospective 30-day Medicare payment can let agencies retain workflow productivity within the payment period, but payer rate updates, behavior adjustments, Medicare Advantage and Medicaid negotiation, denials, quality obligations, competition, software cost, and wage pressure share or absorb the benefit.

## Firm availability
The industry definition fits repeat external care, and agencies can carry transferable payer enrollments, staff, referral channels, and patient census. Eligibility is reduced by compliance history, owner dependence, referral concentration, fragile staffing, nontransferable approvals, and uncertainty in the margin-bridged LMM count.

## Demand durability
Aging and preference for home-based care support growth, while declining FFS Medicare use, fewer hospitalizations, authorization controls, and labor shortages temper the outlook. Patient-facing service remains durable because in-person clinical and personal care cannot broadly be replaced by software.

## Risks and uncertainty
Key risks are reimbursement cuts, payer concentration, claim denials, audit and recoupment exposure, clinician shortages, wage inflation, turnover, referral concentration, state licensing, privacy, weak interoperability, unsafe automation, and service-line heterogeneity. The firm-count margin bridge and mixed vintages in the compensation ratio add dataset uncertainty.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6718 | — | OBSERVED | — |
| n | — | 1983 | — | ESTIMATE | — |
| a | 0.16 | 0.26 | 0.38 | PROXY | S2, S3 |
| rho | 0.3 | 0.52 | 0.72 | PROXY | S4, S5 |
| e | 0.65 | 0.82 | 0.93 | ESTIMATE | S1, S4 |
| s5 | 0.07 | 0.13 | 0.21 | PROXY | S6 |
| q | 0.22 | 0.4 | 0.58 | ESTIMATE | S4, S5 |
| d5 | 0.98 | 1.08 | 1.18 | PROXY | S3, S5 |
| o | 0.78 | 0.88 | 0.95 | PROXY | S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.29 | 3.63 | 7.35 | PROXY |
| F | 7.26 | 8.62 | 9.59 | ESTIMATE |
| C | 4.40 | 8.00 | 10.00 | ESTIMATE |
| D | 7.64 | 9.50 | 10.00 | PROXY |

## Caveats
- a: The occupation table is for 2023 NAICS 621600 employers of all sizes, not the exact LMM acquisition lens.
- a: Employment shares are not wage-weighted task shares and do not identify the current automation baseline.
- a: Exposure varies materially among skilled nursing, therapy, aide, infusion, hospice, and administrative workflows.
- a: The injected compensation ratio combines 2024 wages with 2022 receipts.
- rho: Telehealth and remote-monitoring claims are not a direct measure of AI use or back-office automation.
- rho: Medicare rules do not describe implementation across Medicaid, commercial, or private-pay business.
- rho: Clinical safety, HIPAA, state licensure, and integration constraints vary by service line and agency.
- e: The NAICS and Medicare definitions do not measure recurring-revenue quality, transferable payer contracts, or normalized EBITDA.
- e: In-home hospice, infusion, therapy, and skilled home health can have different referral, reimbursement, and compliance economics.
- e: The injected count of 1,983 relies on a broad healthcare-facilities margin bridge that may not represent agency-level home health margins.
- s5: Gallup covers all US employer businesses and intentions rather than completed transactions.
- s5: No source measures five-year control-transfer probability for eligible LMM home health agencies.
- s5: Regulatory, payer, quality, and referral-concentration issues can prevent an intended sale from qualifying.
- q: No source directly measures the discounted share of implemented AI benefits retained by LMM agencies.
- q: Retention differs across Medicare prospective payment, Medicare Advantage, Medicaid, commercial, and private-pay contracts.
- q: MedPAC's 20.2% aggregate 2023 FFS Medicare margin for freestanding agencies is not a total-company margin and varies widely across providers.
- d5: The BLS forecast covers an occupation employed heavily outside skilled home health agencies.
- d5: MedPAC's volume series is limited to fee-for-service Medicare and does not measure total industry demand.
- d5: Demand can be capacity-constrained by clinician and aide availability rather than patient need.
- o: Medicare's in-person rule does not govern all payer segments or every service in the NAICS code.
- o: The source evidence does not quantify the fraction of visits that technology can safely replace.
- o: Operator requirement varies by acuity, discipline, state scope-of-practice rules, caregiver availability, and home conditions.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: 621610](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 621610 around skilled nursing in the home with personal care, therapy, medical social, medication, equipment, counseling, 24-hour, nutrition, speech, audiology, infusion, hospice, and related services, and distinguishes nonmedical home care and equipment-only businesses.
- **S2** — [May 2023 OEWS: Home Health Care Services](https://www.bls.gov/oes/2023/may/naics4_621600.htm) (accessed 2026-07-22): Reports the home-health occupation mix, including 58.14% home health and personal care aides, 11.21% registered nurses, 20.44% healthcare practitioner and technical occupations, and 6.27% office and administrative support.
- **S3** — [Home Health and Personal Care Aides — Occupational Outlook Handbook](https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm) (accessed 2026-07-22): Describes hands-on daily living, housekeeping, medication, vital-sign, exercise, recordkeeping, and reporting duties; projects 17% occupation growth from 2024 to 2034 and cites aging and movement toward home and community care.
- **S4** — [Home Health Prospective Payment System](https://www.cms.gov/medicare/payment/prospective-payment-systems/home-health) (accessed 2026-07-22): Explains case-mix-adjusted 30-day payments, per-visit low-utilization payments, OASIS assessment, bundled services, and the rule that telecommunications may be included in a plan of care but cannot substitute for an ordered in-person visit.
- **S5** — [March 2025 Report to Congress, Chapter 7: Home Health Care Services](https://www.medpac.gov/wp-content/uploads/2025/03/Mar25_Ch7_MedPAC_Report_To_Congress_SEC.pdf) (accessed 2026-07-22): Reports 2.7 million FFS Medicare users and $15.7 billion of spending in 2023, 12,057 participating agencies, declining FFS users and periods, only 1.2% of 2023 periods with telehealth or remote monitoring, and a 20.2% aggregate FFS Medicare margin for freestanding agencies.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of US employer-business owners planned to sell or transfer ownership within five years in a fall 2024 survey.
