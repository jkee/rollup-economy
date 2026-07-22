# 621210 — Offices of Dentists

*v5.1 Stage 1 research memo. Run `621210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.27 · L 2.17 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A sizable administrative workforce, procedure-based pricing, and consolidating multi-location practices create a practical channel for workflow automation and centralized operating leverage.
**Weakness:** The majority of service delivery remains physical and clinician-dependent, while modest projected real demand and scarce clinical labor limit the value of administrative automation alone.

## Business-model lens
- Included: US lower-middle-market private and group dental practices providing recurring or repeat general dentistry, preventive, cosmetic, emergency, specialty, and dental-surgery services to patients and payers.
- Excluded: Captive internal units, shell entities, non-control financing vehicles, firms outside the approximate $1-10M normalized EBITDA band, dental laboratories, denturists, independent dental hygienist practices, and operations without transferable patient, clinician, location, and payer relationships.
- Customer and revenue model: Patients and third-party dental benefit plans purchase examinations, preventive care, restorations, surgery, orthodontics, and other procedures through contracted per-procedure fee schedules, indemnity reimbursement, capitation, direct patient payment, financing, memberships, and cash-pay elective services.
- Deviation from default lens: none

## Executive view
Dental offices have meaningful administrative and diagnostic-assistance opportunities, active consolidation, and service-based pricing that can retain some efficiency gains. The opportunity is bounded because most employment supports hands-on care and the exact-industry real-output forecast is modest.

## How AI changes the work
AI can support radiograph review, treatment-plan presentation, clinical documentation, coding, claim attachments, eligibility verification, scheduling, recall, collections, and patient messaging. Dentists and clinical teams still perform examinations, hygiene, anesthesia, restorative work, surgery, sterilization, and final diagnosis and treatment decisions.

## Value capture
Procedure-based and patient-pay revenue can preserve savings in administrative work and may improve chair utilization or case acceptance. Payer fee schedules, automated claim scrutiny, capitation risk, clinician incentives, implementation expense, and local competition determine how much becomes durable operator benefit.

## Firm availability
The NAICS definition fits repeat external dental care closely, and ADA data show rising DSO and large-group affiliation. Transferability still depends on state ownership rules, dentist and hygienist retention, location density, payer contracts, clinical reputation, and the distinction between clinical ownership and DSO administrative rights.

## Demand durability
BLS projects modest exact-industry real-output and employment growth. Preventive and restorative need is durable, but coverage, affordability, workforce shortages, and shifts in procedure mix constrain growth.

## Risks and uncertainty
The largest uncertainties are task-level wage exposure, actual multi-location implementation depth, the absence of a firm-level transfer denominator, and realized retention by payer model. A weak outcome would combine low removable front-office labor, expensive integrations, dentist or hygienist turnover, weak local demand, payer pressure, and overreliance on AI-driven case acceptance.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4536 | — | OBSERVED | — |
| n | — | 369 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.35 | PROXY | S2, S4 |
| rho | 0.32 | 0.52 | 0.72 | PROXY | S3, S4 |
| e | 0.76 | 0.9 | 0.97 | ESTIMATE | S1, S5 |
| s5 | 0.14 | 0.26 | 0.4 | PROXY | S5 |
| q | 0.44 | 0.65 | 0.8 | ESTIMATE | S6 |
| d5 | 0.98 | 1.058 | 1.16 | PROXY | S7 |
| o | 0.82 | 0.92 | 0.97 | ESTIMATE | S3, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.81 | 2.17 | 4.57 | PROXY |
| F | 5.94 | 7.19 | 8.00 | ESTIMATE |
| C | 8.80 | 10.00 | 10.00 | ESTIMATE |
| D | 8.04 | 9.73 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS reports employment and wages rather than task hours, billability, or current automation and includes employers of all sizes.
- a: The occupation mix varies materially between general dentistry, orthodontics, oral surgery, pediatrics, and other specialties.
- a: ADA identifies available applications but does not quantify the share of wages exposed or distinguish new exposure from existing practice software.
- rho: The AGD survey covers participating members, is not a census of 621210 firms, and emphasizes general dentists and clinical AI.
- rho: Use of any AI system does not measure workflow coverage, reliable autonomy, or labor opportunity captured.
- rho: Adoption by multi-location groups may outpace small practices, while integration, security, and regulatory requirements can delay realized implementation.
- e: No source directly measures the eligible share of LMM-band 621210 firms.
- e: The injected count is margin-bridged from size classes and may not align precisely with normalized EBITDA or stand-alone control.
- e: Dental-practice ownership and clinical-control rules vary by state, and DSO affiliations can separate clinical ownership from administrative economics.
- s5: ADA reports dentist affiliation rather than firms, transaction counts, or control-transfer probabilities.
- s5: Growth in DSO employment includes de novo locations and associate hiring as well as acquisitions.
- s5: No exact eligible-firm denominator or comprehensive private-deal numerator is available.
- q: ADA describes plan structures but does not measure their revenue shares or benefit-retention outcomes for LMM dental groups.
- q: Payers increasingly use automated claim review and may capture some gains through stricter adjudication or future fee negotiations.
- q: Added capacity has value only where patient demand, dentists, hygienists, and chairs are not the binding constraints.
- d5: BLS uses National Employment Matrix code 621200 for Offices of Dentists, while the six-digit NAICS code is 621210.
- d5: Chained-dollar output is not a direct constant-quality procedure or patient-volume index.
- d5: Coverage, affordability, hygienist shortages, and geographic access can cause realized demand to diverge from the national projection.
- o: No source directly measures the year-five operator-required share of the current dental service basket.
- o: Operator necessity varies by preventive, restorative, surgical, orthodontic, cosmetic, diagnostic, and administrative service mix.
- o: Direct-to-consumer products, teledentistry, improved home prevention, and alternative workforce models may displace more low-complexity demand than assumed.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: 621210 Offices of Dentists](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Exact-industry definition, private and group practice settings, comprehensive and specialty care scope, and cross-references.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Offices of Dentists](https://www.bls.gov/oes/2023/may/naics4_621200.htm) (accessed 2026-07-22): Exact-industry-equivalent employment, occupational shares, and wages used to structure the task-exposure proxy.
- **S3** — [Academy of General Dentistry Member Survey on AI/AuI](https://www.agd.org/docs/default-source/default-document-library/agd-member-survey-re-ai-aui_2024-june30_cd.pdf?sfvrsn=b519d4ed_2) (accessed 2026-07-22): Current AI use, expansion intentions, use cases, benefits, concerns, and professional position that AI should remain adjunctive to dentist clinical judgment.
- **S4** — [ADA SCDI White Paper No. 1106: Artificial Intelligence and Augmented Intelligence in Dentistry](https://www.ada.org/-/media/project/ada-organization/ada/ada-org/files/resources/practice/dental-standards/ada_1106_2022.pdf?rev=6597958fb295462492935589971e27c3) (accessed 2026-07-22): Commercial and developing AI capabilities in dental imaging, claim attachments, claim review, and other clinical and nonclinical workflows.
- **S5** — [The Evolving Dental Practice Model: Data Update for 2023](https://www.ada.org/-/media/project/ada-organization/ada/ada-org/files/resources/research/hpi/hpi_evolving_dental_practice_model_2023.pdf) (accessed 2026-07-22): National DSO affiliation trend, declining solo-practice participation, growth of 100-plus-location practices, and differences by specialty and career stage.
- **S6** — [Types of Dental Plans](https://www.ada.org/resources/practice/dental-insurance/dental-plan-overview/) (accessed 2026-07-22): Dental PPO, capitation, indemnity, direct reimbursement, discount, and allowance-plan payment mechanics used to frame commercial retention.
- **S7** — [Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Offices of Dentists employment and chained-2017-dollar output projections used for the five-year demand proxy.
- **S8** — [Dentists: Occupational Outlook Handbook](https://www.bls.gov/ooh/healthcare/dentists.htm) (accessed 2026-07-22): Dentist duties, hands-on procedures, equipment use, private-practice administration, licensing, and projected employment growth.
