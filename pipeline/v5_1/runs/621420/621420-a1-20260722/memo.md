# 621420 — Outpatient Mental Health and Substance Abuse Centers

*v5.1 Stage 1 research memo. Run `621420-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 7.47 · L 4.48 · interval CONDITIONAL → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is expanding clinician capacity by automating documentation and coordination around recurring, accountable treatment relationships.
**Weakness:** The principal weakness is that core therapeutic and crisis work remains licensed, interpersonal, and liability-intensive while payer and ownership structures limit retained benefit and transferable supply.

## Business-model lens
- Included: U.S. lower-middle-market outpatient centers providing recurring or repeat diagnosis, counseling, psychotherapy, medication-supported care, crisis stabilization, case management, and related treatment for mental health and substance use conditions to external patients.
- Excluded: Psychiatric hospitals, residential treatment facilities, captive hospital departments, independent practitioner offices classified elsewhere, peer-support groups without accountable clinical operations, shell entities, non-control financing situations, and centers without transferable operations or normalized EBITDA in the target band.
- Customer and revenue model: Episode-based and recurring outpatient revenue paid by Medicaid, Medicare, commercial insurers, self-pay patients, grants, and public programs for assessments, individual and group therapy, medication-related services, intensive outpatient care, case management, crisis services, and care coordination.
- Deviation from default lens: none

## Executive view
Outpatient mental health and substance abuse centers combine recurring demand, high labor intensity, and substantial documentation burden. AI can improve clinician capacity and administrative throughput, but the core service depends on licensed relationships, judgment, safety, and crisis accountability.

## How AI changes the work
AI can assist intake, screening, scheduling, eligibility, coding, progress notes, treatment-plan drafts, measurement, patient messaging, referral coordination, and routine follow-up. Clinicians remain responsible for diagnosis, therapy, risk assessment, crisis intervention, medication decisions, group dynamics, consent, mandated reporting, and escalation.

## Value capture
Administrative savings and increased clinician capacity can be retained between payer resets or converted into additional visits. Administered rates, insurer utilization management, prospective payment, grants, sliding fees, staffing rules, and access obligations constrain retention.

## Firm availability
The frozen firm count is estimate-based and the industry includes nonprofit, public, affiliated, independent, mental health, substance use, crisis, and intensive outpatient models. Ownership, payer contracts, grants, licenses, accreditation, clinician retention, referral concentration, and compliance can materially shrink the transferable pool.

## Demand durability
Persistent behavioral-health need and expanded remote delivery support continued outpatient demand. Realized growth depends on clinician supply, payer access, referral capacity, policy, program funding, and whether patients shift to independent practitioners, primary care, or digital models.

## Risks and uncertainty
Key risks are clinician scarcity and turnover, reimbursement pressure, grant dependence, state licensure variation, privacy and safety failures, crisis liability, weak outcomes, referral concentration, nonprofit or public ownership, telehealth disintermediation, and overestimating labor savings in relationship-intensive care.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5817 | — | OBSERVED | — |
| n | — | 1229 | — | ESTIMATE | — |
| a | 0.24 | 0.35 | 0.48 | PROXY | S1, S2, S3, S4 |
| rho | 0.36 | 0.55 | 0.72 | ESTIMATE | S3, S5 |
| e | 0.52 | 0.7 | 0.85 | ESTIMATE | S1, S7 |
| s5 | 0.08 | 0.15 | 0.22 | PROXY | S9 |
| q | 0.24 | 0.39 | 0.55 | ESTIMATE | S6, S7 |
| d5 | 0.98 | 1.1 | 1.24 | PROXY | S4, S7 |
| o | 0.79 | 0.89 | 0.96 | PROXY | S1, S3, S4, S5, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.01 | 4.48 | 8.04 | ESTIMATE |
| F | 6.36 | 7.83 | 8.75 | ESTIMATE |
| C | 4.80 | 7.80 | 10.00 | ESTIMATE |
| D | 7.74 | 9.79 | 10.00 | PROXY |

## Caveats
- a: BLS occupational shares cover broad NAICS 621400 and are not specific to outpatient mental health and substance abuse centers.
- a: O*NET and the Occupational Outlook Handbook describe occupations across employers and do not measure wage-weighted hours or current automation in 621420.
- a: Mental health, substance use, intensive outpatient, crisis, and medication-supported programs have different task mixes.
- rho: No representative survey measures AI implementation or labor realization in NAICS 621420.
- rho: Medicare telehealth policy demonstrates remote delivery feasibility rather than AI adoption or labor substitution.
- rho: High-acuity, crisis, and substance use workflows may implement more slowly than routine outpatient psychotherapy.
- e: No representative firm-level source measures the combined recurrence, control, transferability, concentration, compliance, and normalized-earnings screens.
- e: The frozen firm count is margin-bridged using a broad healthcare-facilities margin and may misclassify grant-funded, nonprofit, or program-intensive centers.
- e: The code combines mental health and substance use centers with materially different reimbursement, staffing, licensing, and acuity.
- s5: Gallup covers all U.S. employer-business owners and measures intentions rather than completed qualifying control sales.
- s5: The proxy does not capture nonprofit, public, health-system, or sponsor-backed ownership patterns in 621420.
- s5: No representative source reports five-year control-transfer completion for outpatient behavioral-health centers.
- q: Medicare and SAMHSA sources establish administered rates, insurance coverage, and patient cost sharing but do not measure the industry's payer mix or retained automation benefit.
- q: No representative source reports contract repricing, grant treatment of savings, or post-automation margins for 621420.
- q: Retention varies between fee-for-service therapy, intensive programs, CCBHC-style payment, grants, and self-pay services.
- d5: BLS projects counselor employment rather than constant-price demand for the current 621420 service basket.
- d5: Insurance coverage statements do not measure utilization or demand growth and state Medicaid benefits vary.
- d5: Workforce shortages can prevent underlying need from becoming realized center volume.
- o: Licensure and task evidence establishes accountable work but does not quantify how much year-five demand will remain with centers rather than independent clinicians, primary care, or digital providers.
- o: Telehealth often preserves a licensed operator while bypassing a physical center, so operator retention and site retention are not identical.
- o: Digital substitution is more plausible for screening and low-acuity support than for crisis, severe illness, medication, and intensive substance use treatment.

## Sources
- **S1** — [2022 NAICS Definition: Outpatient Care Centers, including 621420 Outpatient Mental Health and Substance Abuse Centers](https://www.census.gov/naics/?details=6214&input=6214&year=2022) (accessed 2026-07-22): Official 621420 service definition and exclusions; lens, a, e, and o
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 621400](https://www.bls.gov/oes/2023/may/naics4_621400.htm) (accessed 2026-07-22): Broad outpatient-center occupational mix, including counselors, social workers, clinicians, support, and administrative employment; a
- **S3** — [O*NET OnLine: Mental Health Counselors](https://www.onetonline.org/link/details/21-1014.00) (accessed 2026-07-22): Counseling, crisis, risk, treatment-plan, documentation, record, referral, and coordination tasks; a, rho, and o
- **S4** — [Occupational Outlook Handbook: Substance Abuse, Behavioral Disorder, and Mental Health Counselors](https://www.bls.gov/ooh/community-and-social-service/substance-abuse-behavioral-disorder-and-mental-health-counselors.htm) (accessed 2026-07-22): Counselor duties, licensure, outpatient-center employment, and 2024-2034 employment projection; a, d5, and o
- **S5** — [CMS Telehealth FAQ for Calendar Year 2025](https://www.cms.gov/files/document/telehealth-faq-calendar-year-2025.pdf) (accessed 2026-07-22): Behavioral-health telehealth payment, home access, audio-only rules, and removal of geographic restrictions; rho and o
- **S6** — [Medicare Costs](https://www.medicare.gov/basics/costs/medicare-costs) (accessed 2026-07-22): Medicare-approved payment and patient cost sharing for outpatient mental health services; q
- **S7** — [SAMHSA: Mental Health Treatment - What Does Health Insurance Cover?](https://www.samhsa.gov/find-support/how-to-pay-for-treatment/know-what-your-insurance-covers) (accessed 2026-07-22): Commercial, Medicare, Medicaid, and CHIP coverage and plan variation for mental health and substance use treatment; e, q, and d5
- **S8** — [SAMHSA: Treatment Types for Mental Health, Drugs and Alcohol](https://www.samhsa.gov/find-support/learn-about-treatment/types-of-treatment) (accessed 2026-07-22): Licensed behavioral-health professionals, therapy, counseling, telehealth, and treatment-setting context; o
- **S9** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year employer-business sale or transfer intentions; s5
