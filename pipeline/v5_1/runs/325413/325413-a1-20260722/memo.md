# 325413 — In-Vitro Diagnostic Substance Manufacturing

*v5.1 Stage 1 research memo. Run `325413-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.96 · L 0.80 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat consumable demand tied to ongoing diagnosis and monitoring, with physical reagents that software cannot replace outright.
**Weakness:** A small estimated target-firm universe and strict quality-system accountability constrain scale and implementation certainty.

## Business-model lens
- Included: Independent lower-middle-market manufacturers of in-vitro diagnostic reagents, substances, calibrators, controls, and related consumable preparations supplied repeatedly to external laboratories, device companies, distributors, or healthcare customers.
- Excluded: Captive internal reagent production, diagnostic laboratories performing tests without manufacturing substances for external customers, instrument-only makers, distributors without manufacturing, research-only entities, and shell or financing vehicles.
- Customer and revenue model: Recurring or repeat consumable sales and contract-manufacturing revenue under supply agreements, standing orders, distributor arrangements, or OEM and private-label programs, generally priced per kit, vial, lot, or unit.
- Deviation from default lens: none

## Executive view
IVD substance manufacturing has recurring consumable demand, scientific and quality documentation suited to supervised AI, and strong physical operator requirement. Realized labor savings remain constrained by QMSR and validation, while only an estimated 41 firms sit in the target band and their transfer rate is unobserved.

## How AI changes the work
AI can aid specification and literature search, first drafts, complaint and quality-event triage, planning, customer support, and commercial analysis. Wet-lab work, validation, production, metrology, labeling control, and final release remain human-accountable.

## Value capture
Specialized assays and validation or platform ties can preserve savings, but laboratory consolidation, distributors, reimbursement pressure, tenders, OEM cost-downs, and generic reagents push benefits toward customers.

## Firm availability
Independent consumables suppliers naturally serve repeat external customers, yet the 41-firm population is margin-bridged. Captive plants, labs, instrument makers, and research entities require careful removal, and product transfers are not control transfers.

## Demand durability
Aging, chronic disease burden, and precision diagnostics support testing, while reimbursement, multiplexing, and assay replacement limit volume. Most remaining demand still requires physical regulated substances and accountable manufacturing.

## Risks and uncertainty
False results, recalls, lot inconsistency, contamination, regulatory changes, reimbursement cuts, platform obsolescence, customer concentration, and rapid assay substitution can overwhelm efficiencies. Direct task, contract, transfer, and shipment evidence is limited.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1579 | — | OBSERVED | — |
| n | — | 41 | — | ESTIMATE | — |
| a | 0.19 | 0.3 | 0.41 | PROXY | S1, S2, S3 |
| rho | 0.25 | 0.42 | 0.58 | ESTIMATE | S2, S3 |
| e | 0.48 | 0.66 | 0.8 | ESTIMATE | S4 |
| s5 | 0.11 | 0.21 | 0.33 | ESTIMATE | — |
| q | 0.43 | 0.6 | 0.76 | ESTIMATE | S5 |
| d5 | 1 | 1.14 | 1.32 | PROXY | S6, S7, S8 |
| o | 0.88 | 0.96 | 0.99 | ESTIMATE | S2, S4, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.30 | 0.80 | 1.50 | ESTIMATE |
| F | 1.85 | 3.06 | 3.97 | ESTIMATE |
| C | 8.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.80 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No direct six-digit occupational distribution or task-exposure study was found.
- a: The frozen compensation ratio combines 2024 wages with 2022 receipts and may not represent the screened LMM customer and product mix.
- rho: Representative LMM implementation evidence is unavailable.
- rho: Class, intended use, laboratory modality, and software content create materially different validation burdens.
- e: The assigned 41-firm count is a margin bridge rather than an observed EBITDA-band census.
- e: FDA devices, listings, establishments, laboratories, and legal firms are different units.
- s5: No industry-specific owner-age or succession dataset was found.
- s5: Acquisition of a test portfolio or intellectual property without the operating firm must be excluded.
- q: No representative contract dataset was available.
- q: Retention differs between proprietary assay consumables, general-purpose reagents, controls, calibrators, and OEM production.
- d5: Population health and aging are demand drivers, not direct measures of NAICS 325413 output.
- d5: Test utilization does not translate one-for-one into substance volume because of multiplexing and platform efficiency.
- o: This measures operator requirement for remaining physical-substance demand, not continued outsourcing to the same firm.
- o: The 2024 FDA laboratory-developed-test rule was vacated in 2025, leaving regulatory and insourcing uncertainty.

## Sources
- **S1** — [BLS Data tables for OEWS industry charts](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): For other chemical-manufacturing groups, lists major embodied and technical occupations including equipment, packaging and mixing operators, supervisors, material movers, inspectors, chemists, and managers, used only as a task-mix proxy.
- **S2** — [FDA Quality Management System Regulation](https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr) (accessed 2026-07-22): States that QMSR became effective February 2, 2026, incorporates ISO 13485:2016, requires manufacturers to ensure products meet requirements and specifications, and covers design, production, lifecycle controls, and risk management.
- **S3** — [FDA In Vitro Diagnostic Device Labeling Requirements](https://www.fda.gov/medical-devices/device-labeling/in-vitro-diagnostic-device-labeling-requirements) (accessed 2026-07-22): Defines IVD products as reagents, instruments, and systems used for diagnosis or determining health status and details labeling obligations for reagents and systems.
- **S4** — [FDA Overview of IVD Regulation](https://www.fda.gov/medical-devices/ivd-regulatory-assistance/overview-ivd-regulation) (accessed 2026-07-22): Explains IVD classification, premarket and postmarket controls, CLIA categorization, establishment registration, device listing, and quality-system obligations for design, manufacture, packaging, labeling, storage, installation, and servicing.
- **S5** — [CMS Clinical Laboratory Fee Schedule](https://www.cms.gov/medicare/payment/fee-schedules/clinical-laboratory-fee-schedule-clfs) (accessed 2026-07-22): States that Medicare pays most clinical diagnostic laboratory tests from weighted median private-payor rates and that annual payment reductions may reach 15% in 2027-2029, supporting reimbursement pressure as a customer pass-through risk.
- **S6** — [CDC Trends in Multiple Chronic Conditions Among US Adults, 2013-2023](https://www.cdc.gov/pcd/issues/2025/24_0539.htm) (accessed 2026-07-22): Reports that 76.4% of U.S. adults, about 194 million people, had one or more selected chronic conditions in 2023 and 51.4%, about 130 million, had multiple conditions.
- **S7** — [U.S. Census Bureau: Older Adults Outnumber Children in 11 States and Nearly Half of U.S. Counties](https://www.census.gov/newsroom/press-releases/2025/older-adults-outnumber-children.html) (accessed 2026-07-22): Reports that the U.S. population age 65 and older rose 3.1% to 61.2 million from 2023 to 2024 and reached 18.0% of the population.
- **S8** — [FDA Precision Medicine](https://www.fda.gov/medical-devices/in-vitro-diagnostics/precision-medicine) (accessed 2026-07-22): Describes routine molecular testing in cancer care and the clinical role of next-generation sequencing tests that can examine large genomic regions and guide diagnosis and treatment.
- **S9** — [FDA Laboratory Developed Tests](https://www.fda.gov/medical-devices/in-vitro-diagnostics/laboratory-developed-tests) (accessed 2026-07-22): Documents that the May 2024 LDT final rule was vacated by a federal court in March 2025 and FDA reverted the regulatory text in September 2025, supporting uncertainty around laboratory-manufactured alternatives.
