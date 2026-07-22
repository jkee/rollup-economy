# 621330 — Offices of Mental Health Practitioners (except Physicians)

*v5.1 Stage 1 research memo. Run `621330-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 7.95 · L 5.88 · interval CONDITIONAL → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring reimbursed visits create a large base of documentation and administrative work around a durable licensed clinical service.
**Weakness:** The service and enterprise value depend on clinicians whose relationships, licenses, judgment, and continued employment are difficult to automate or guarantee after a sale.

## Business-model lens
- Included: U.S. lower-middle-market private and group practices of nonphysician psychologists, counselors, marriage and family therapists, social workers, and related licensed mental health practitioners providing recurring or repeat diagnosis, psychotherapy, assessment, and behavioral treatment to external patients and payors.
- Excluded: Solo practices without transferable operations, physician psychiatry, inpatient and residential facilities, general outpatient centers classified elsewhere, nonclinical coaching, captive employee-assistance units, and software-only mental health products.
- Customer and revenue model: Patients receive scheduled in-person or virtual clinical visits; practices collect negotiated fee-for-service reimbursement from commercial and government payors and patient payments, with each counseling session generally constituting a separate service obligation.
- Deviation from default lens: none

## Executive view
Mental health group practices combine high labor intensity with addressable documentation, intake, scheduling, billing, and care-coordination work. The core therapeutic encounter is far less substitutable, and privacy, clinical risk, licensed ownership, clinician retention, and payor concentration limit the simple conversion of AI capability into transferable value.

## How AI changes the work
AI can draft notes and care plans, summarize records, prepare intake, support measurement-based care, code claims, schedule patients, route messages, and automate routine follow-up. Licensed clinicians must still establish the alliance, interpret context, assess suicide and safety risk, diagnose, choose treatment, manage crises, and take responsibility for the record.

## Value capture
Negotiated fee-for-service reimbursement does not automatically fall when documentation cost falls, supporting near-term margin or capacity capture. Durable retention is reduced by payer repricing, utilization management, fee-schedule changes, clinician productivity pay, mandatory review, and competition for scarce clinicians.

## Firm availability
The code includes independent private and group practices, and completed platform acquisitions show that practices can transfer. A buyer must distinguish durable group infrastructure from a collection of clinician relationships and must navigate professional-ownership, credentialing, payor-assignment, and clinician-retention constraints.

## Demand durability
Coverage expansion, unmet need, and strong counselor employment projections support continuing demand. Realized growth is constrained by workforce supply, reimbursement, affordability, patient engagement, and software or primary-care substitution for lower-acuity services.

## Risks and uncertainty
The principal risks are confidential-data exposure, hallucinated or biased documentation, clinical liability, payer audits, clinician departures, corporate-practice restrictions, concentrated contracts, telehealth rule changes, and the gap between broad owner intentions and completed control transfers. Exact evidence on workflow hours, implementation, benefit sharing, and group-practice transactions is limited.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6334 | — | OBSERVED | — |
| n | — | 460 | — | ESTIMATE | — |
| a | 0.29 | 0.4 | 0.53 | PROXY | S1, S2, S3, S4 |
| rho | 0.38 | 0.58 | 0.72 | PROXY | S3, S4 |
| e | 0.66 | 0.82 | 0.93 | ESTIMATE | S1, S6 |
| s5 | 0.06 | 0.13 | 0.22 | PROXY | S5, S6 |
| q | 0.38 | 0.55 | 0.7 | PROXY | S6, S8 |
| d5 | 0.93 | 1.07 | 1.18 | PROXY | S7, S8, S9 |
| o | 0.78 | 0.9 | 0.97 | ESTIMATE | S3, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.79 | 5.88 | 9.67 | PROXY |
| F | 4.75 | 6.29 | 7.33 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | PROXY |
| D | 7.25 | 9.63 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS reports employment and wages but not task time or current automation penetration.
- a: The exact-industry table excludes self-employed practitioners and may not mirror lower-middle-market group practices.
- a: AI can assist clinical preparation without substituting the therapeutic encounter or licensed judgment.
- rho: The AMA survey covers physicians, not this industry's practitioner population.
- rho: Professional guidance establishes feasible use cases and constraints but does not measure production adoption.
- rho: Privacy, consent, malpractice, and documentation-integrity requirements can turn gross time savings into review work.
- e: No source measures eligibility within the frozen lower-middle-market firm count.
- e: Corporate-practice and fee-splitting rules can separate clinical ownership from management economics.
- e: A group practice can meet the revenue test yet remain economically dependent on one clinician-owner or a few payor contracts.
- s5: Gallup measures intentions among employer-business owners across all industries, not completed mental health practice transfers.
- s5: LifeStance is much larger than screened firms and includes physician services outside the exact code.
- s5: Management-service transactions or licensed-owner substitutions may not represent clean control transfers of the clinical practice.
- q: LifeStance's payor mix and bargaining position are not representative of smaller practices.
- q: No source measures how AI benefits are shared through mental health reimbursement or clinician compensation.
- q: Capacity gains have little value where clinician supply, appointment demand, supervision, or payor panels bind.
- d5: Occupational employment growth is not the same quantity as constant-quality demand for the current service basket.
- d5: The principal BLS projection is for one major practitioner occupation and does not cover every profession in the code.
- d5: Coverage expansions can raise billed demand while fee cuts, network closures, or workforce scarcity suppress realized visits.
- o: No source directly measures year-five operator-required share for this exact industry.
- o: Low-acuity coaching and structured interventions may migrate to employer, primary-care, or software channels.
- o: Regulation preserves licensed accountability but does not guarantee that incumbent group practices retain the patient relationship.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: 621330 Offices of Mental Health Practitioners (except Physicians)](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Exact-industry scope, independent private and group practice structure, covered clinical activities, and cross-references.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 621330](https://www.bls.gov/oes/2023/may/naics5_621330.htm) (accessed 2026-07-22): Exact-industry employment and wage mix, including counselors, social workers, psychologists, health practitioners, and office-administrative occupations.
- **S3** — [American Counseling Association Response on the Development of an Artificial Intelligence Action Plan](https://www.counseling.org/docs/default-source/advocacy/aca-ai-rfi_submission.pdf?sfvrsn=9be45bd0_2) (accessed 2026-07-22): Counseling-specific AI uses in notes, billing, paperwork, and intake, and requirements for human diagnosis, treatment planning, privacy, and oversight.
- **S4** — [Physicians' Greatest Use for AI? Cutting Administrative Burdens](https://www.ama-assn.org/practice-management/digital-health/physicians-greatest-use-ai-cutting-administrative-burdens) (accessed 2026-07-22): Adjacent clinical-provider evidence on documentation and administrative AI relevance, ambient-scribe deployment, efficiency expectations, and implementation governance.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry five-year sale or transfer intentions among U.S. employer-business owners and survey population details.
- **S6** — [LifeStance Health Group, Inc. 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1845257/000095017025029100/lfst-20241231.htm) (accessed 2026-07-22): Outpatient mental health delivery, fee-for-service reimbursement, clinician productivity, payor and regulatory risks, acquisition strategy, and completed practice acquisitions.
- **S7** — [Occupational Outlook Handbook: Substance Abuse, Behavioral Disorder, and Mental Health Counselors](https://www.bls.gov/ooh/community-and-social-service/substance-abuse-behavioral-disorder-and-mental-health-counselors.htm) (accessed 2026-07-22): National occupation outlook and projected openings used as a demand proxy.
- **S8** — [Marriage and Family Therapists and Mental Health Counselors](https://www.cms.gov/medicare/payment/fee-schedules/physician-fee-schedule/marriage-family-therapists-mental-health-counselors) (accessed 2026-07-22): Independent Medicare billing eligibility, licensed-practitioner criteria, and Physician Fee Schedule payment structure.
- **S9** — [Calendar Year 2025 Medicare Physician Fee Schedule Final Rule](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2025-medicare-physician-fee-schedule-final-rule) (accessed 2026-07-22): Behavioral telehealth policy, additional behavioral-health coding, and payment for digital mental health treatment devices used with ongoing practitioner-led treatment.
