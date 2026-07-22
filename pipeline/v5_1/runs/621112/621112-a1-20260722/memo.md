# 621112 — Offices of Physicians, Mental Health Specialists

*v5.1 Stage 1 research memo. Run `621112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 7.34 · L 4.27 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring psychiatric demand and service-based reimbursement create room to convert documentation and administrative automation into clinician capacity and lower support cost.
**Weakness:** High-value work remains licensed, judgment-intensive, and relationship-dependent, while clinician retention and payer constraints can prevent technical efficiency from becoming transferable cash flow.

## Business-model lens
- Included: US lower-middle-market private and group practices of MD and DO mental health specialists providing recurring or repeat psychiatry and psychoanalysis services to patients and payers, including evaluation, medication management, psychotherapy, and related clinical administration.
- Excluded: Captive internal units, shell entities, non-control financing vehicles, firms outside the approximate $1-10M normalized EBITDA band, nonphysician mental health practices, outpatient mental health and substance-abuse centers, general physician practices, and operations without transferable clinical and payer relationships.
- Customer and revenue model: Patients and third-party payers purchase recurring evaluations, psychotherapy, medication management, and care coordination through per-visit fee schedules, negotiated commercial rates, Medicare and Medicaid reimbursement, value-based arrangements, and some cash-pay packages.
- Deviation from default lens: none

## Executive view
Mental-health physician practices combine high compensation intensity with repeat, reimbursement-backed clinical demand. AI can compress documentation and administrative work, but the opportunity is narrower than the labor ratio alone suggests because psychiatrist judgment, prescribing accountability, and therapeutic relationships dominate the valuable service.

## How AI changes the work
AI can capture and draft notes, suggest codes, summarize charts, prepare care plans, automate intake and eligibility work, triage messages, and support clinical information retrieval. Clinicians remain responsible for diagnosis, medication decisions, crisis assessment, patient communication, and review of generated content.

## Value capture
Per-service reimbursement can preserve administrative savings and added visit capacity until payer updates or contract changes. Realized capture depends on whether automation removes paid support work, changes clinician compensation, reduces denials, or merely relieves after-hours documentation.

## Firm availability
The exact NAICS definition fits independent psychiatry practices, but the estimated LMM population may include controlled affiliates or clinician-dependent groups. Physician ownership has shifted toward hospitals and private equity, showing transfer activity while also shrinking the independent seller pool.

## Demand durability
Broader physician-office real output is projected to grow, and BLS specifically expects growing psychiatric-care demand. Scarce clinicians and access constraints support durable need but can limit realizable volume and encourage substitution toward nonphysician and digital channels.

## Risks and uncertainty
The largest uncertainties are the absence of an exact-industry occupation study, unknown implementation depth, no psychiatry transaction denominator, and no evidence on realized benefit retention. A weak outcome would combine clinician departure after acquisition, payer-rate pressure, low removable support payroll, compliance-heavy AI deployment, and rapid substitution of low-acuity care to lower-cost channels.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6374 | — | OBSERVED | — |
| n | — | 214 | — | ESTIMATE | — |
| a | 0.16 | 0.27 | 0.4 | PROXY | S2, S3 |
| rho | 0.42 | 0.62 | 0.78 | PROXY | S3 |
| e | 0.7 | 0.84 | 0.94 | ESTIMATE | S1, S4 |
| s5 | 0.1 | 0.2 | 0.32 | PROXY | S4 |
| q | 0.42 | 0.62 | 0.78 | ESTIMATE | S5 |
| d5 | 1.05 | 1.176 | 1.32 | PROXY | S6, S7 |
| o | 0.62 | 0.79 | 0.9 | ESTIMATE | S1, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.71 | 4.27 | 7.95 | PROXY |
| F | 4.46 | 5.81 | 6.72 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 6.51 | 9.29 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is reported at broader NAICS 621100, includes all physician specialties and employer sizes, and measures jobs rather than task hours.
- a: AMA adoption is physician-wide and measures use of at least one AI task, not the share of wages technically substitutable or not already automated.
- a: Psychiatry has unusually high conversational and relationship content, so exposure differs substantially by medication-management, psychotherapy, and administrative service mix.
- rho: The AMA sample spans specialties, employment settings, ownership types, and firm sizes rather than LMM 621112 practices.
- rho: Any-use adoption is not implementation depth, autonomous completion, or labor opportunity captured.
- rho: Mental-health records, sensitive conversations, state rules, malpractice exposure, and patient trust can slow adoption even when tools are available.
- e: No source directly measures the eligible share of LMM-band 621112 firms.
- e: The injected count is margin-bridged from establishment-size data and may not align precisely with normalized EBITDA or independent control.
- e: NAICS permits practices located in hospitals or HMO medical centers, and statistical firm status does not guarantee a transferable stand-alone operation.
- s5: AMA ownership statistics describe physicians, not firms or control transactions, and are not psychiatry-specific.
- s5: Movement from private to hospital or corporate practice can occur through employment changes, closures, or affiliations rather than a transferable control sale.
- s5: No exact-industry transaction numerator or eligible-firm denominator is available.
- q: CMS describes Medicare payment mechanics, not the full commercial, Medicaid, value-based, and cash-pay mix of 621112 practices.
- q: No source measures the share of implemented AI gross benefit retained by psychiatry operators.
- q: Savings may accrue as reduced after-hours work or added clinical capacity rather than removable payroll or durable margin.
- d5: BLS industry output is for all offices of physicians, not mental-health specialists, and chained-dollar output is not a direct constant-quality visit index.
- d5: Employment growth is a supply and utilization indicator, not a direct demand measure.
- d5: Demand can remain unmet when clinician shortages, network adequacy, coverage losses, or affordability prevent service delivery.
- o: No source directly measures the year-five operator-required share of the current 621112 service basket.
- o: State scope-of-practice rules, prescribing rules, acuity, payer policy, and practice mix create large variation in substitution risk.
- o: The estimate separates direct software displacement from implementation difficulty but cannot fully distinguish software self-service from substitution by nonphysician human providers.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: 621112 Offices of Physicians, Mental Health Specialists](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Exact-industry definition, MD/DO psychiatry and psychoanalysis scope, practice settings, and cross-references excluding nonphysician practices and outpatient centers.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Offices of Physicians](https://www.bls.gov/oes/2023/may/naics4_621100.htm) (accessed 2026-07-22): Broader physician-office employment, occupational shares, and wages used to structure the task-exposure proxy.
- **S3** — [2 in 3 physicians are using health AI—up 78% from 2023](https://www.ama-assn.org/practice-management/digital-health/2-3-physicians-are-using-health-ai-78-2023) (accessed 2026-07-22): AMA physician AI adoption, task-specific use, administrative opportunity, and stated trust, privacy, integration, training, oversight, accuracy, and liability constraints.
- **S4** — [Smaller share of doctors in private practice than ever before](https://www.ama-assn.org/practice-management/private-practices/smaller-share-doctors-private-practice-ever) (accessed 2026-07-22): Physician-wide ownership shifts, hospital and private-equity practice participation, sale motivations, and practice-size trends used as transfer and eligibility context.
- **S5** — [Physician Fee Schedule Look-Up Tool Overview](https://www.cms.gov/medicare/physician-fee-schedule/search/overview) (accessed 2026-07-22): Medicare service-level payment amounts and calculation using work, practice-expense, and malpractice RVUs with geographic adjustment.
- **S6** — [Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Broader Offices of Physicians employment and chained-2017-dollar output projections used for the five-year demand proxy.
- **S7** — [Physicians and Surgeons: Occupational Outlook Handbook](https://www.bls.gov/ooh/healthcare/physicians-and-surgeons.htm) (accessed 2026-07-22): Psychiatrist duties, licensing and training, projected psychiatrist employment, and BLS statement that growing psychiatric-care demand supports job growth.
