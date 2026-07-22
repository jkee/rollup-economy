# 621410 — Family Planning Centers

*v5.1 Stage 1 research memo. Run `621410-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 5.99 · L 3.36 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is scaling recurring reproductive-health access by automating administrative and documentation work around a trusted clinical endpoint.
**Weakness:** The principal weakness is a heterogeneous, policy-sensitive provider pool whose most valuable services still require licensed clinical labor and whose transferable ownership base is poorly measured.

## Business-model lens
- Included: U.S. lower-middle-market family planning centers providing recurring or repeat outpatient contraceptive, fertility, pregnancy, genetic, prenatal, sterilization, and medically indicated reproductive-health services to external patients.
- Excluded: Hospital departments, captive health-system units, physician offices classified elsewhere, product-only sellers, shell entities, non-control financing situations, and centers without transferable operations or normalized EBITDA in the target band.
- Customer and revenue model: Patient-service revenue paid through Medicaid, commercial insurance, self-pay, grants, and program funding for consultations, examinations, testing, counseling, prescriptions, procedures, fertility services, and related follow-up care.
- Deviation from default lens: none

## Executive view
Family planning centers combine recurring clinical relationships and high administrative burden with a service basket that remains clinically accountable and often physical. AI is more credible as a documentation, access, and revenue-cycle layer than as a replacement for medical staff.

## How AI changes the work
AI can assist intake, history capture, scheduling, eligibility, coding, prior authorization, ambient documentation, patient messaging, translation, care-gap outreach, and routine education. Licensed staff remain responsible for counseling, prescribing, examinations, specimens, devices, procedures, consent, complications, and sensitive exceptions.

## Value capture
Capacity expansion and lower administrative rework can retain value between payer resets, and self-pay fertility services may offer more pricing discretion. Medicaid fee schedules, grants, insurer negotiation, affordability obligations, and competitive repricing limit how much gross benefit stays with the operator.

## Firm availability
The frozen firm count is estimate-based and the code includes nonprofit, public, affiliated, fertility, counseling, and procedure-led models. Tax status, ownership, licenses, payer enrollment, grants, clinician concentration, and policy exposure can materially reduce the transferable pool.

## Demand durability
Contraception, testing, counseling, pregnancy-related services, fertility support, and procedures create continuing demand, but provision can shift among dedicated centers, primary care, telehealth, pharmacies, and home testing. Policy and funding changes can move local volumes abruptly.

## Risks and uncertainty
Key risks are the heterogeneous service mix, margin-bridged firm count, nonprofit or public ownership, reimbursement pressure, grant dependence, state policy divergence, privacy and safety obligations, clinician scarcity, reputation exposure, and digital or primary-care substitution for simpler visits.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4575 | — | OBSERVED | — |
| n | — | 110 | — | ESTIMATE | — |
| a | 0.23 | 0.34 | 0.47 | PROXY | S1, S2, S3, S4 |
| rho | 0.36 | 0.54 | 0.7 | ESTIMATE | S3, S4, S9 |
| e | 0.38 | 0.56 | 0.74 | ESTIMATE | S1, S7, S9 |
| s5 | 0.06 | 0.12 | 0.22 | PROXY | S8 |
| q | 0.24 | 0.41 | 0.59 | ESTIMATE | S7, S9 |
| d5 | 0.91 | 1.02 | 1.14 | ESTIMATE | S5, S6 |
| o | 0.77 | 0.88 | 0.96 | PROXY | S1, S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.52 | 3.36 | 6.02 | ESTIMATE |
| F | 2.02 | 3.42 | 4.73 | ESTIMATE |
| C | 4.80 | 8.20 | 10.00 | ESTIMATE |
| D | 7.01 | 8.98 | 10.00 | ESTIMATE |

## Caveats
- a: BLS reports the broader NAICS 621400 outpatient-center workforce rather than 621410 and provides employment shares rather than wage-weighted task hours.
- a: O*NET task descriptions are cross-industry occupational profiles and do not identify tasks already automated in family planning centers.
- a: The six-digit industry mixes counseling-led clinics, fertility centers, and procedure-intensive services with materially different task exposure.
- rho: No representative survey measures AI implementation or realized labor-hour reduction in NAICS 621410.
- rho: Digitized forms, portal messaging, and scheduling are workflow automation and are not necessarily AI.
- rho: Large networks may deploy integrated tools faster than independent or grant-dependent clinics.
- e: No representative firm-level source measures the combined recurrence, control, transferability, concentration, compliance, and normalized-earnings screens.
- e: The frozen firm count is margin-bridged using a broad healthcare-facilities margin and may misclassify specialized fertility and grant-supported centers.
- e: The industry definition combines business models with different payer, ownership, and regulatory structures.
- s5: Gallup covers all U.S. employer-business owners and measures intentions rather than completed qualifying healthcare transactions.
- s5: Family planning ownership, tax status, and regulatory conditions may make the broad employer-business proxy systematically high.
- s5: No source measures five-year control transfers specifically for 621410.
- q: Medicaid's coverage requirement establishes a major administered-payment channel but does not measure the payer mix or retained automation benefit of 621410 firms.
- q: No representative source reports family planning contract repricing, self-pay competition, grant treatment of savings, or post-automation margins.
- q: Retention varies sharply between grant-supported contraceptive clinics and self-pay fertility services.
- d5: CDC measures national use and receipt of services across all provider settings, not demand at NAICS 621410 centers.
- d5: The current service basket includes contraception, fertility, counseling, and procedures with different demand paths.
- d5: Recent utilization snapshots do not establish a five-year constant-price trend, so this primitive remains an estimate.
- o: Service definitions and occupation tasks establish accountable clinical work but do not measure the fraction that will still require a dedicated center in year five.
- o: Telehealth may preserve a licensed operator while eliminating some physical-site demand.
- o: Substitution differs materially between counseling or prescription visits and device, specimen, fertility, sterilization, or other procedural services.

## Sources
- **S1** — [2022 NAICS Definition: Outpatient Care Centers, including 621410 Family Planning Centers](https://www.census.gov/naics/?details=6214&input=6214&year=2022) (accessed 2026-07-22): Official 621410 service definition and industry heterogeneity; lens, a, e, and o
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 621400](https://www.bls.gov/oes/2023/may/naics4_621400.htm) (accessed 2026-07-22): Broad outpatient-center occupational mix, including healthcare, social-service, support, and administrative employment; a
- **S3** — [O*NET OnLine: Medical Assistants](https://www.onetonline.org/link/summary/31-9092.00) (accessed 2026-07-22): Administrative, records, billing, scheduling, clinical preparation, specimen, medication, and equipment tasks; a, rho, and o
- **S4** — [O*NET OnLine: Registered Nurses](https://www.onetonline.org/link/summary/29-1141.00) (accessed 2026-07-22): Clinical assessment, records, medication, care planning, education, testing, and examination tasks; a, rho, and o
- **S5** — [Receipt of Family Planning Services in the United States: 2022-2023](https://www.cdc.gov/nchs/products/databriefs/db520.htm) (accessed 2026-07-22): National receipt of family planning services from medical providers and service categories; d5 and o
- **S6** — [Current Contraceptive Status Among Females Ages 15-49: United States, 2022-2023](https://www.cdc.gov/nchs/products/databriefs/db539.htm) (accessed 2026-07-22): Current national contraceptive use and method mix; d5
- **S7** — [Mandatory and Optional Medicaid Benefits](https://www.medicaid.gov/medicaid/benefits/mandatory-optional-medicaid-benefits) (accessed 2026-07-22): Family planning as a mandatory Medicaid benefit and administered-payment context; e and q
- **S8** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year employer-business sale or transfer intentions; s5
- **S9** — [HHS Office of Population Affairs Research and Evaluation Activities](https://opa.hhs.gov/research-evaluation/about-opa-activities) (accessed 2026-07-22): Title X grantee reporting of clients, services, staffing, revenue, and program context; rho, e, and q
