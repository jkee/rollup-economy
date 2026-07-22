# 325412 — Pharmaceutical Preparation Manufacturing

*v5.1 Stage 1 research memo. Run `325412-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.82 · L 0.96 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring, physically indispensable drug production with a sizeable documentation and analytical labor layer.
**Weakness:** Regulated quality responsibility and validation sharply constrain how much exposed work can become removed labor.

## Business-model lens
- Included: Independent lower-middle-market manufacturers of finished pharmaceutical preparations serving repeat external drug sponsors, brands, wholesalers, health-system channels, or private-label customers.
- Excluded: Captive internal plants, pure drug-development or IP entities without manufacturing, pharmacies and compounders classified elsewhere, distributors without production, shell applicants, and non-control financing vehicles.
- Customer and revenue model: Repeat batch, product, and contract-manufacturing revenue under supply agreements, purchase orders, private-label arrangements, and sponsor quality agreements; pricing is generally per batch, unit, or product rather than per labor hour.
- Deviation from default lens: none

## Executive view
Pharmaceutical preparation manufacturing offers meaningful information-heavy work on top of a substantial compensation base, but GMP accountability and validation make realized substitution materially harder than technical exposure suggests. Demand remains physical and operator-required; eligible-firm and transfer counts need firm-level reconciliation.

## How AI changes the work
AI can improve knowledge retrieval, drafting, planning, batch-record and deviation triage, supplier-document review, forecasting, and customer support. Validated data, inspections, testing, responsible checks, and final quality release keep humans in control.

## Value capture
Batch and unit pricing plus switching qualification support retention, but generic competition, sponsor concentration, procurement organizations, rebids, and cost-plus contracting return a significant portion to customers.

## Firm availability
Independent contract and repeat-supply manufacturers fit the lens well, yet the assigned 345 firms are a margin bridge. Captive plants, applicants without operating production, and IP-led developers must be removed, and product divestitures must not be mistaken for control transfers.

## Demand durability
Downstream drug spending is projected to grow, but it is a nominal proxy for the exact manufacturing basket. Product churn and sourcing shifts are substantial; nevertheless, any physical preparation still requires qualified manufacturing, testing, and release.

## Risks and uncertainty
Warning letters, recalls, contamination, data-integrity failures, customer concentration, reimbursement and pricing reform, litigation, product attrition, and capital requirements can overwhelm administrative savings. Contract mix and plant modality drive wide variation.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2391 | — | OBSERVED | — |
| n | — | 345 | — | ESTIMATE | — |
| a | 0.17 | 0.28 | 0.39 | PROXY | S1, S2 |
| rho | 0.2 | 0.36 | 0.52 | ESTIMATE | S2, S3 |
| e | 0.5 | 0.69 | 0.82 | ESTIMATE | S3 |
| s5 | 0.11 | 0.21 | 0.33 | ESTIMATE | — |
| q | 0.4 | 0.57 | 0.72 | ESTIMATE | S4 |
| d5 | 0.99 | 1.12 | 1.28 | PROXY | S4, S5 |
| o | 0.94 | 0.99 | 1 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.96 | 1.94 | ESTIMATE |
| F | 4.82 | 6.32 | 7.31 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.31 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No direct six-digit occupation-by-task exposure study was found.
- a: The frozen compensation ratio combines 2024 wages with 2022 receipts and may include business models unlike screened contract or repeat-supply manufacturers.
- rho: Implementation evidence for LMM pharmaceutical plants is not representative or publicly standardized.
- rho: Sterile, solid-dose, liquid, and specialty preparations have different validation and operational constraints.
- e: The assigned 345-firm population is margin-bridged and not an observed EBITDA-band census.
- e: FDA establishments, applicants, labels, and operating firms are different units and cannot be counted interchangeably.
- s5: No owner-age or succession panel specific to eligible firms was found.
- s5: Distressed closures and asset divestitures must be excluded unless a transferable going concern changes control.
- q: No representative contract dataset was available.
- q: Retention differs between proprietary products, commodity generics, scarce capacity, and sponsor-owned formulations.
- d5: CMS forecasts spending rather than constant-quality manufacturing volume.
- d5: Retail prescriptions omit institutional and non-retail products and include value unrelated to manufacturing quantity.
- o: This measures operator requirement for the current service basket, not whether the same independent operator retains the customer.
- o: Some individualized production may migrate to pharmacies or healthcare facilities classified outside this NAICS.

## Sources
- **S1** — [BLS Data tables for OEWS industry charts](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): For other chemical-manufacturing groups, lists major occupations such as equipment, packaging and mixing operators, supervisors, material movers, inspectors, chemists, and managers, used only as an occupation-mix proxy.
- **S2** — [FDA Dosage Form Drug Manufacturers CGMP Inspection Guide](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-guides/dosage-form-drug-manufacturers-cgmps-1093) (accessed 2026-07-22): Details batch records, process validation, annual reviews, deviations, testing, yield calculations, equipment and facility controls, and responsible checks for critical manufacturing steps.
- **S3** — [FDA Current Good Manufacturing Practice Regulations](https://www.fda.gov/drugs/pharmaceutical-quality-resources/current-good-manufacturing-practice-cgmp-regulations) (accessed 2026-07-22): States that FDA monitors manufacturer CGMP compliance and assesses whether firms have the facilities, equipment, and ability to manufacture intended drugs, including under 21 CFR Parts 210 and 211.
- **S4** — [FDA Drug Shortages: Root Causes and Potential Solutions](https://www.fda.gov/drugs/drug-shortages/report-drug-shortages-root-causes-and-potential-solutions) (accessed 2026-07-22): Identifies weak incentives for less-profitable drugs, lack of rewards for mature quality systems, and logistical and regulatory recovery challenges; reports that 42% of 2013-2017 shortage drugs had a significant production increase and 30% were fully restored.
- **S5** — [CMS National Health Expenditure Projections 2024-2033](https://www.cms.gov/files/document/nhe-projections-infographic.pdf) (accessed 2026-07-22): Projects retail prescription-drug spending average growth of 4.9% during 2026-2033, used as a broader nominal downstream demand proxy.
