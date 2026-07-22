# 621340 — Offices of Physical, Occupational and Speech Therapists, and Audiologists

*v5 Stage 1 research memo. Run `621340-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.71 · L 3.04 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable, aging-linked outpatient rehabilitation demand combined with automatable administrative workflows around a licensed clinical core.
**Weakness:** The largest wages buy direct clinical care that is difficult to substitute, while reimbursement and ownership constraints can limit both savings capture and transferability.

## Business-model lens
- Included: Independent and regional outpatient offices furnishing physical therapy, occupational therapy, speech-language pathology, or audiology to external patients and referral sources, where the service is a repeat care episode and the firm is in the lower-middle-market EBITDA band.
- Excluded: Hospital departments, school-district staff, home-health and nursing-facility operations classified elsewhere, captive employer clinics, shells, internal service units, and financing vehicles without operating control.
- Customer and revenue model: Patient-facing professional therapy and audiology services, paid principally per visit or episode by Medicare, Medicaid, commercial insurers, employers, and self-pay patients; referrals and repeat treatment visits create recurring demand.
- Deviation from default lens: none

## Executive view
These outpatient therapy and audiology offices combine a large licensed, patient-facing clinical core with a substantial administrative burden. AI is more credible as a workflow and capacity tool than as a replacement for therapy delivery. Demand indicators are favorable, and fragmentation creates a plausible operating population, but reimbursement exposure, labor scarcity, and professional-ownership constraints require firm-level diligence.

## How AI changes the work
The strongest near-term uses are intake, scheduling, call handling, referral processing, benefits verification, authorization packets, documentation drafting, coding support, denial follow-up, and patient communication. Clinical evaluation, treatment selection, manual care, supervised exercise, safety decisions, and clinician accountability remain the limiting work. Aides may gain productivity in clerical tasks, but their patient-facing set-up and movement assistance also remain physical.

## Value capture
Revenue is commonly tied to visits, episodes, or payer fee schedules rather than cost-plus contracts, so a clinic can retain part of internal efficiency gains. That retention is not permanent or complete: Medicare schedules, commercial renewals, payer utilization management, referral competition, and local labor markets can redirect gains to payers, patients, or staffing. Benefits should be modeled from the actual payer contract book and not from generic automation claims.

## Firm availability
The market is described as fragmented and increasingly active in M&A. Publicly disclosed PT transaction data show activity including small-clinic deals, while a broader independent-practice survey shows owner sale and retirement intent. Neither source supplies a completed-transfer rate for lower-middle-market therapy offices, so the transfer estimate remains a deliberately discounted proxy rather than a market fact.

## Demand durability
Therapy demand is supported by aging, chronic conditions, disability, rehabilitation needs, and nonopioid pain management. BLS forecasts growth for physical and occupational therapists, and workforce evidence shows shortages and administrative pressure. The service should continue to require accountable operators because assessment, treatment planning, physical assistance, and licensed oversight are central to the current basket.

## Risks and uncertainty
The code mixes PT, OT, SLP, and audiology, whose payer structures and digital-substitution paths differ. Public occupational data do not reveal time by task, eligible-firm ownership, EBITDA normalization, payer mix, or actual transfer rates. Small practices can be referral-concentrated and founder-dependent. The relevant diligence set is payer contracts and denials, clinician retention, referral concentration, EHR and revenue-cycle data, state ownership rules, and sale-process evidence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6007 | — | OBSERVED | — |
| n | — | 821 | — | ESTIMATE | — |
| a | 0.16 | 0.23 | 0.32 | PROXY | S1, S2, S3 |
| rho | 0.38 | 0.55 | 0.68 | ESTIMATE | S4, S5 |
| e | 0.75 | 0.85 | 0.93 | ESTIMATE | S6, S7 |
| s5 | 0.1 | 0.18 | 0.27 | PROXY | S7, S8 |
| q | 0.42 | 0.58 | 0.72 | ESTIMATE | S5, S8 |
| d5 | 1.025 | 1.065 | 1.095 | PROXY | S2, S9, S4 |
| o | 0.9 | 0.95 | 0.98 | ESTIMATE | S2, S3, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.46 | 3.04 | 5.23 | ESTIMATE |
| F | 6.65 | 7.79 | 8.58 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 9.22 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: S1 is May 2023 employment and wage data, not a task survey.
- a: The industry includes several therapy disciplines with different documentation and payer workflows.
- a: Owner-clinician compensation and contracted billing labor may not be fully represented in payroll occupations.
- rho: No source directly measures five-year implementation of the defined opportunity in lower-middle-market therapy offices.
- rho: Rates will vary sharply with EHR maturity, payer mix, and multi-state compliance requirements.
- e: The frozen firm count is margin-bridged rather than a census of eligible practices.
- e: S6 is a market-report announcement rather than a public microdata tabulation.
- e: Eligibility requires facts about operating control and service recurrence that NAICS data do not provide.
- s5: S8 is a small, unweighted, cross-specialty survey and does not identify therapy practices separately.
- s5: Publicly announced transactions omit many small private deals and cannot reveal the number of eligible firms offered for sale.
- s5: Corporate-practice and professional-ownership rules can affect whether an economic deal is a qualifying control transfer.
- q: No public source measures five-year benefit retention for the defined AI changes in this industry.
- q: Payer mix and local competition can dominate the result.
- q: This estimate excludes volume changes and implementation feasibility, which belong in other primitives.
- d5: National occupational projections include hospitals, schools, home health, and other settings outside the frozen lens.
- d5: Employment growth is not identical to quantity demand because productivity and staffing mix may change.
- d5: The basket includes speech and audiology, for which this proxy is less direct.
- o: The estimate is for the current service basket, not for all future digital rehabilitation products.
- o: Some low-acuity exercise and education visits may migrate to self-service or software-assisted models.
- o: The degree of direct physical contact differs across PT, OT, SLP, and audiology.

## Sources
- **S1** — [Offices of Physical, Occupational and Speech Therapists, and Audiologists - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics5_621340.htm) (accessed 2026-07-22): Direct NAICS 621340 occupational employment and wage mix, including 457,060 total jobs, 44.30% healthcare practitioners and technical occupations, and detail employment for therapists and support roles.
- **S2** — [Physical Therapists - Occupational Outlook Handbook](https://www.bls.gov/ooh/healthcare/physical-therapists.htm) (accessed 2026-07-22): Physical therapist direct-care duties, licensure requirement, office employment share, and projected 11% employment growth from 2024 to 2034.
- **S3** — [Physical Therapist Assistants and Aides - Occupational Outlook Handbook](https://www.bls.gov/ooh/healthcare/physical-therapist-assistants-and-aides.htm) (accessed 2026-07-22): Assistant and aide direct-care, physical, and clerical duties; supervision; offices as major employers; and projected employment growth.
- **S4** — [APTA Physical Therapy Supply and Demand Forecast: 2022-2037](https://www.apta.org/contentassets/787bafc2ef664074ace8914f748ee4cd/apta-2025-workforce-forecast-companion-report.pdf) (accessed 2026-07-22): APTA workforce-survey evidence on local therapist shortages, administrative burden, payment concerns, retirement or departure intent, and aging workforce dynamics.
- **S5** — [CMS-1832-F: CY 2026 Medicare Physician Fee Schedule Final Rule](https://www.cms.gov/medicare/payment/fee-schedules/physician/federal-regulation-notices/cms-1832-f) (accessed 2026-07-22): CMS source confirming the 2026 Physician Fee Schedule final rule and the fee-schedule payment-policy context for therapy providers.
- **S6** — [U.S. Physical Therapy Clinics Market Analysis 2025](https://www.globenewswire.com/news-release/2025/05/02/3073073/0/en/U-S-Physical-Therapy-Clinics-Market-Analysis-2025-53-Billion-Industry-Primed-for-Consolidation-M-A-Activity-Surges-in-Fragmented-Therapy-Sector.html) (accessed 2026-07-22): Market-report announcement stating that physical, occupational, speech therapy, and audiology are included; the fifty largest competitors capture 29% of revenue; small and medium regional providers predominate; and M&A activity is increasing.
- **S7** — [PT Market Update - December 2025](https://img1.wsimg.com/blobby/go/2c62a220-c762-4dae-857e-2ad976ca4388/downloads/861d41d8-7400-451b-af62-e77499ae18d2/PT%20Market%20Update%20Dec%202025.pdf?ver=1767902772500) (accessed 2026-07-22): Broker market update reporting 65 publicly disclosed PT transactions closed in 2025, the change from 2024, and the share of transactions by clinic-count category.
- **S8** — [High anxiety: New data on the state of independent practice ownership](https://www.tebra.com/theintake/medical-deep-dives/independent-practices/state-of-independent-healthcare-practice-ownership) (accessed 2026-07-22): Independent healthcare-practice owner survey reporting sale or retirement likelihood, sale reasons, observed owner exits, reimbursement concerns, respondent composition, and non-probability sample limitations.
- **S9** — [Occupational Therapists - Occupational Outlook Handbook](https://www.bls.gov/ooh/Healthcare/Occupational-therapists.htm) (accessed 2026-07-22): Occupational therapist duties, state licensure, employment in therapist offices, and projected 14% employment growth from 2024 to 2034.
