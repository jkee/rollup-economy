# 621493 — Freestanding Ambulatory Surgical and Emergency Centers

*v5.1 Stage 1 research memo. Run `621493-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.82 · L 1.82 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeatable revenue-cycle and documentation workflows sit inside a growing, facility-based outpatient care channel whose clinical delivery cannot be digitized away.
**Weakness:** The high-wage core is licensed hands-on care, while heterogeneous center types, payer-administered prices, regulation, and physician or hospital ownership limit implementable savings and clean control targets.

## Business-model lens
- Included: Lower-middle-market freestanding ambulatory surgery centers, urgent care centers, emergency medical centers, and trauma centers repeatedly delivering outpatient procedures or immediate medical care to external patients and payors.
- Excluded: Hospital outpatient departments, licensed hospitals, physician offices without a separately operated center, captive internal units, shells, non-control financing vehicles, nonprofit or government facilities without transferable control economics, and real-estate or equipment owners without the clinical operating service.
- Customer and revenue model: Centers deliver facility-based episodes of care to patients, with payment commonly coming from Medicare or Medicaid administered rates, commercial insurer contracts, and patient cost sharing. Surgery centers earn facility fees for covered procedures; emergency and urgent centers bill visit, facility, diagnostic, and treatment services subject to network, coverage, and state rules.
- Deviation from default lens: none

## Executive view
Freestanding surgical and emergency centers contain meaningful administrative, documentation, coding, scheduling, authorization, and communication work that AI can compress, but most wages and value remain bound to licensed, physical, safety-critical care. Procedure-based and visit-based reimbursement can preserve some benefit, while payer contracting, annual public-rate updates, regulation, and clinical reinvestment constrain capture. The industry has a visible acquisition channel and supportive outpatient migration, but its surgery, urgent care, and emergency components require separate diligence.

## How AI changes the work
AI can draft visit and procedure notes, code suggestions, discharge instructions, chart summaries, portal messages, translations, prior-authorization packages, schedule and capacity plans, supply forecasts, and quality reviews. It can assist diagnosis and triage under clinician oversight. It is much less able to replace surgery, anesthesia, nursing intervention, imaging operation, sterile processing, patient monitoring, trauma response, or accountable clinical judgment.

## Value capture
Savings inside a fixed procedure or visit payment can initially improve center economics or support more cases. Retention leaks through Medicare and Medicaid rate updates, commercial renewal and utilization management, network competition, clinician compensation, additional consumables and staffing for throughput, compliance, and reinvestment in access or safety. Ownership scale and bargaining leverage may improve commercial capture but also invite payer and regulatory scrutiny.

## Firm availability
Most ASCs are for profit and physician ownership is common, while hospital, payer, corporate, and private-equity stakes create an established transaction channel. The usable LMM pool is smaller than the legal entity count because some centers are hospital or chain affiliates, physician-dependent joint ventures, nonprofit facilities, or entities whose receipts and facility assets do not translate into transferable operating EBITDA.

## Demand durability
Aging, clinical advances, patient convenience, lower cost sharing, and continued migration of suitable procedures away from hospitals support outpatient center volume. Immediate and procedural care still requires physical delivery. Demand can nevertheless shift among ASCs, hospitals, offices, telehealth, and home pathways, and the emergency or urgent portion faces different regulation and payer economics than ambulatory surgery.

## Risks and uncertainty
The largest uncertainties are the six-digit workforce and payor mix, contracted clinical labor, the surgery-versus-emergency composition, facility-level ownership, transaction denominators, and actual retained savings after payer response. Documentation or triage errors, privacy breaches, biased decision support, cybersecurity incidents, downtime, staffing shortages, certificate-of-need rules, surprise-billing restrictions, and changes in site-neutral payment can outweigh administrative gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3246 | — | OBSERVED | — |
| n | — | 1962 | — | ESTIMATE | — |
| a | 0.18 | 0.28 | 0.4 | PROXY | S2, S3, S7 |
| rho | 0.32 | 0.5 | 0.68 | PROXY | S3 |
| e | 0.59 | 0.76 | 0.88 | PROXY | S1, S7 |
| s5 | 0.14 | 0.24 | 0.36 | PROXY | S4, S7 |
| q | 0.31 | 0.52 | 0.7 | PROXY | S5, S7, S8 |
| d5 | 0.99 | 1.16 | 1.28 | PROXY | S6, S7, S8 |
| o | 0.84 | 0.92 | 0.97 | PROXY | S1, S3, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.75 | 1.82 | 3.53 | PROXY |
| F | 8.19 | 9.46 | 10.00 | ESTIMATE |
| C | 6.20 | 10.00 | 10.00 | PROXY |
| D | 8.32 | 10.00 | 10.00 | PROXY |

## Caveats
- a: The occupation table covers all outpatient care centers and not the surgery-versus-emergency mix within 621493.
- a: Physician AI use does not establish avoided labor hours or safe substitution in procedural settings.
- a: Contracted physician and anesthesia labor may not appear in an establishment payroll mix even when economically central.
- rho: Self-reported use includes research summaries and experimentation rather than enterprise deployment.
- rho: The AMA sample does not identify facility size, NAICS code, or lower-middle-market ownership.
- rho: Clinical validation and liability requirements constrain implementation more than generic office automation.
- e: MedPAC's ownership evidence covers Medicare ASCs, not urgent care or freestanding emergency centers.
- e: A for-profit facility may still be captive to a hospital, payer, physician group, or national chain.
- e: The supplied firm count is margin-bridged and the 15.8% reference margin may not fit each center type.
- s5: Owner intentions do not equal completed arm's-length control transfers.
- s5: Corporate ownership stakes and facility counts do not identify transaction frequency or deal size.
- s5: Healthcare ownership, certificate-of-need, and corporate-practice rules can change the feasible transaction structure.
- q: No source directly measures retention of AI-derived gross benefit by independent centers.
- q: Facility, professional, anesthesia, device, drug, and diagnostic payments may accrue to different entities.
- q: Emergency, urgent care, and ambulatory surgery reimbursement and competitive dynamics differ materially.
- d5: MedPAC volume excludes Medicare Advantage and non-Medicare patients and covers ASCs only.
- d5: BLS output combines all outpatient care center industries and is not a six-digit forecast.
- d5: Procedure migration from hospitals can raise center volume without equal growth in underlying clinical need.
- o: The code combines elective procedural facilities with urgent and emergency care, which have different substitution paths.
- o: A shift to a hospital or physician office removes a freestanding operator even when the clinical service persists.
- o: AI-enabled triage may redirect low-acuity cases without substituting for higher-acuity center operations.

## Sources
- **S1** — [U.S. Census Bureau: 2022 NAICS Manual, 621493](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 621493 as freestanding centers with physicians and other medical staff providing outpatient surgery or emergency care and identifies specialized facilities, equipment, examples, and hospital exclusions.
- **S2** — [BLS May 2023 OEWS: Outpatient Care Centers](https://www.bls.gov/oes/2023/may/naics4_621400.htm) (accessed 2026-07-22): Reports the broader outpatient-center occupation mix, including 41.13% healthcare practitioners and technical occupations, 15.39% registered nurses, 11.19% healthcare support, and 15.71% office and administrative support.
- **S3** — [AMA 2026 Physician Survey on Augmented Intelligence](https://www.ama-assn.org/system/files/physician-ai-sentiment-report.pdf/) (accessed 2026-07-22): Reports physician AI adoption, documentation and summarization use cases, anticipated automation of clinical and administrative tasks, and privacy, validation, liability, training, and workflow constraints.
- **S4** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of U.S. employer-business owners planned to sell or transfer ownership within five years, based on a survey fielded in fall 2024.
- **S5** — [GAO-25-107450: Health Care Consolidation](https://files.gao.gov/reports/GAO-25-107450/index.html) (accessed 2026-07-22): Documents physician consolidation and roll-up structures, acquisition channels, varied commercial price effects, and uncertainty in access and quality outcomes.
- **S6** — [BLS Employment and Output by Industry, 2024 to 2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects broader NAICS 621400 real output from $217.8 billion in 2024 to $307.4 billion in 2034, a 3.5% annual increase.
- **S7** — [MedPAC March 2026: Ambulatory Surgical Center Services](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch11_MedPAC_Report_To_Congress_SEC.pdf) (accessed 2026-07-22): Reports ASC supply, ownership, corporate stakes, utilization, payments, site-of-care economics, procedure concentration, and the absence of national ASC cost reporting.
- **S8** — [CMS CY 2026 OPPS and ASC Final Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-2026-hospital-outpatient-prospective-payment-system-opps-ambulatory-surgical-center) (accessed 2026-07-22): Reports the 2026 ASC payment update, affected facility count, quality reporting changes, and policies supporting migration of clinically appropriate procedures to outpatient settings.
