# 622310 — Specialty (except Psychiatric and Substance Abuse) Hospitals

*v5.1 Stage 1 research memo. Run `622310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.18 · L 2.03 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Fixed episode payments and information-heavy clinical administration create a credible productivity channel while licensed inpatient care remains operator-bound.
**Weakness:** The code mixes materially different hospital types, and the margin-bridged firm count does not reveal which entities are independent, controllable LMM operators.

## Business-model lens
- Included: US lower-middle-market firms operating licensed specialty hospitals that repeatedly provide inpatient and related outpatient diagnostic, medical, long-term acute, rehabilitation, restorative, or condition-specific care to patients and payers.
- Excluded: General medical and surgical hospitals, psychiatric and substance-abuse hospitals, skilled nursing facilities, non-hospital residential care, hospital departments that are captive units rather than separately controlled firms, shells, and non-control financing or real-estate vehicles.
- Customer and revenue model: Hospitals receive prospective case or discharge payments, negotiated commercial payments, public-program reimbursement, and patient cost sharing for staffed episodes of inpatient care, often with related outpatient, diagnostic, therapy, and assessment services.
- Deviation from default lens: none

## Executive view
Specialty hospitals combine a meaningful digital administrative layer with a care product that remains intensely physical, licensed, and accountable. AI can compress documentation, coding, scheduling, assessment, and utilization workflows, but the code is heterogeneous and many apparent firms may be system-owned, nonprofit, public, or outside a clean control transaction.

## How AI changes the work
Near-term AI can draft clinical notes, suggest codes, summarize records, prepare care plans and discharge materials, support utilization review, forecast capacity, schedule staff and patients, and automate claims follow-up. It does not independently deliver bedside nursing, intensive therapy, procedures, monitoring, infection control, nutrition, or final clinical judgment.

## Value capture
Prospective per-discharge and case-based payments can let an operator retain workflow productivity within an episode. Annual public rate updates, commercial renegotiation, quality reporting, payer audits, and the practical need to reinvest saved time in capacity and care limit the discounted retained share.

## Firm availability
The supplied firm count is not a verified list of freestanding controllable hospitals. Licensure, certificate-of-need rules, nonprofit and public ownership, health-system affiliation, real-estate separation, payer enrollment, capital intensity, and clinical leadership requirements narrow the eligible pool, although specialty platforms and long-term-care hospitals do change ownership.

## Demand durability
Complex illness, disability, rehabilitation needs, and aging support specialty inpatient demand, and recent Medicare rehabilitation volume has grown. Counterweights are payer authorization, referral management, substitution toward skilled nursing or home health, reimbursement pressure, and the possibility that recent rehabilitation share gains slow.

## Risks and uncertainty
Principal risks are code heterogeneity, clinical and cyber liability, privacy, regulatory validation, denial and coding exposure, staffing shortages, public-payer dependence, system concentration, capital needs, certificate-of-need barriers, payer steering, and weak firm-level eligibility evidence. AI adoption statistics for acute-care hospitals may not transfer to smaller independent specialty operators.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3913 | — | OBSERVED | — |
| n | — | 117 | — | ESTIMATE | — |
| a | 0.13 | 0.25 | 0.38 | PROXY | S2, S3 |
| rho | 0.3 | 0.52 | 0.71 | PROXY | S3, S4 |
| e | 0.25 | 0.46 | 0.68 | ESTIMATE | S1, S6, S8 |
| s5 | 0.03 | 0.08 | 0.15 | PROXY | S8 |
| q | 0.38 | 0.58 | 0.75 | PROXY | S5, S9 |
| d5 | 0.95 | 1.1 | 1.24 | PROXY | S7, S9 |
| o | 0.91 | 0.96 | 0.99 | PROXY | S1, S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.61 | 2.03 | 4.22 | PROXY |
| F | 1.01 | 2.68 | 4.12 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | PROXY |
| D | 8.64 | 10.00 | 10.00 | PROXY |

## Caveats
- a: The 2023 OEWS table measures occupational employment and wages, not task time or AI exposure.
- a: GAO's documentation evidence spans healthcare providers and is not specific to specialty hospitals.
- a: The code mixes rehabilitation, long-term acute, children's, cancer, and other specialty hospitals with different occupation and documentation mixes.
- rho: ASTP's survey covers non-federal acute-care hospitals rather than specialty hospitals.
- rho: Tool use is not the same as realized labor substitution or avoided hiring.
- rho: Small independent hospitals adopt predictive AI substantially less often than system-affiliated hospitals.
- e: Eligibility is bounded judgment rather than an observed share.
- e: CMS IRF counts include hospital units, while NAICS and the dataset are organized around establishments and firms.
- e: The 15.80% margin bridge may misclassify capital-intensive or low-margin specialty hospitals into the LMM band.
- s5: The ASPE observation period predates the five-year forecast horizon.
- s5: The hospital denominator includes general, psychiatric, rehabilitation, and long-term-care providers outside the exact firm lens.
- s5: A provider change of ownership is not always a qualifying control transfer of an independent firm.
- q: IRF payment is only one component of the heterogeneous code's payer and service mix.
- q: Medicare rate updates can share industry productivity with the payer over time.
- q: Gross workflow benefit may be reinvested in quality, compliance, or capacity rather than retained financially.
- d5: The strongest volume evidence is for inpatient rehabilitation, not every specialty-hospital subtype.
- d5: Medicare FFS trends may diverge from Medicare Advantage, Medicaid, and commercial demand.
- d5: Nominal payment updates are not constant-price service-volume growth.
- o: IRF requirements do not describe every specialty-hospital subtype.
- o: Payer substitution to other care settings can reduce operator need even when medical demand persists.
- o: The distinction between demand reduction and migration to a different operator is difficult to observe.

## Sources
- **S1** — [2022 NAICS Manual: 622310 Specialty (except Psychiatric and Substance Abuse) Hospitals](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines licensed specialty hospitals, included long-term chronic-care and rehabilitation hospitals, inpatient beds, organized medical staffs, related services, and exclusions from adjacent hospital and nursing-facility codes.
- **S2** — [BLS OEWS: Specialty Hospitals Occupational Employment and Wages, May 2023](https://www.bls.gov/oes/2023/may/naics4_622300.htm) (accessed 2026-07-22): Reports 285,770 jobs and the detailed occupation mix, including 50.97% healthcare practitioners and technical workers, 16.27% healthcare support, 10.04% office and administrative support, 22.42% registered nurses, and substantial therapist employment.
- **S3** — [GAO: AI for Medical Notes and Coding](https://www.gao.gov/products/gao-26-109116) (accessed 2026-07-22): Documents AI scribes and coding tools, clinician administrative time, 28% surveyed clinician use for documentation or coding in 2026, a study reporting 20% documentation-time reduction, and accuracy, cost, privacy, and oversight limitations.
- **S4** — [ASTP: Hospital Trends in Predictive AI Use, 2023-2024](https://healthit.gov/data/data-briefs/hospital-trends-use-evaluation-and-governance-predictive-ai-2023-2024/) (accessed 2026-07-22): Reports 71% predictive-AI use among responding non-federal acute-care hospitals in 2024, lower use among small and independent hospitals, and rapid growth in billing and scheduling applications.
- **S5** — [CMS Medicare Payment Systems: IRF Prospective Payment](https://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/html/medicare-payment-systems.html) (accessed 2026-07-22): Explains that IRFs receive predetermined per-discharge payments covering routine, ancillary, and capital costs and must complete IRF patient assessments.
- **S6** — [CMS: Inpatient Rehabilitation Facilities](https://www.cms.gov/medicare/health-safety-standards/certification-compliance/inpatient-rehabilitation-facilities) (accessed 2026-07-22): Describes freestanding rehabilitation hospitals and hospital units, intensive rehabilitation requirements, patient ability to tolerate three hours of therapy per day, certification, and IRF assessment submission.
- **S7** — [MedPAC March 2026: Post-Acute Care Trends and Key Issues](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch6_MedPAC_Report_To_Congress_SEC.pdf) (accessed 2026-07-22): Reports 1,170 IRFs, 377,000 FFS users, $11 billion in 2024 spending, 31% IRF volume growth per FFS beneficiary from 2015 to 2024, a 5.3% share of hospital discharges in 2024, intensive care requirements, and substitution risks across post-acute settings.
- **S8** — [ASPE: Changes in Ownership of Hospitals and Skilled Nursing Facilities, 2016-2021](https://aspe.hhs.gov/sites/default/files/documents/4d960147d5fd8e2ea9af508f115ca7b7/aspe-datapoint-change-ownership-pecos.pdf) (accessed 2026-07-22): Reports 348 hospital sales, an annualized 9.8 changes per 1,000 hospitals and 4.6% over the study period, with changes more common among medium or larger hospitals, low-margin hospitals, and long-term-care hospitals.
- **S9** — [CMS: FY 2026 IRF Prospective Payment System Final Rule](https://www.cms.gov/newsroom/fact-sheets/fy-2026-inpatient-rehabilitation-facilities-prospective-payment-system-final-rule-cms-1829-f) (accessed 2026-07-22): Finalizes a 2.6% IRF payment-rate increase from a 3.3% market basket less a 0.7-point productivity adjustment, with case-mix, wage-index, outlier, and quality-reporting updates.
