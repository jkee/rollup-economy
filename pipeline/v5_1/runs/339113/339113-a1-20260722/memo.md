# 339113 — Surgical Appliance and Supplies Manufacturing

*v5.1 Stage 1 research memo. Run `339113-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.07 · L 1.56 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring care, rehabilitation, replenishment, and workplace-protection needs sustain a broad physical product base.
**Weakness:** The same code combines highly defensible implants and custom products with price-driven commodity supplies and industrial safety goods.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers of surgical appliances and supplies, including orthopedic and prosthetic devices, implants, dressings, sutures, medical masks and gloves, specialized hospital furniture, mobility aids, and personal industrial safety devices, with manufacturer-attributable repeat product and service revenue.
- Excluded: Dental equipment and laboratories, general-purpose furniture, electronic hearing aids, protective eyewear, pure distributors and rental businesses, captive internal units, and service businesses that do not manufacture in-scope products.
- Customer and revenue model: Repeat outsourced revenue from hospitals, clinics, distributors, rehabilitation providers, industrial users, government buyers, and medical-device OEMs through replenishable supplies, durable appliances, replacement parts, customization, maintenance, and related support.
- Deviation from default lens: none

## Executive view
Surgical appliances and supplies offer recurring clinical, rehabilitation, and safety demand but span an unusually wide range from commodity consumables to regulated implants and custom prosthetics. AI can improve office, design, planning, and quality workflows; hands-on production and finished-device accountability remain durable.

## How AI changes the work
The strongest applications are documentation, design assistance, customization, forecasting, scheduling, procurement, quality analytics, inspection support, and customer service. Fabrication, sterile processes, fitting, physical testing, and release decisions limit substitution.

## Value capture
Differentiation, validation, clinical familiarity, customization, and channel relationships protect value in some products. Commodity supplies, tenders, distributors, imports, and institutional purchasing sharply reduce capture in others.

## Firm availability
A sizable specialist-manufacturer population is plausible, but product, ownership, recurring-revenue, distributor, practitioner, and size-band screens remove a material share. Exact transfer evidence is absent.

## Demand durability
Broad official output projections support moderate growth, with aging, procedures, chronic care, rehabilitation, replenishment, and safety requirements as drivers. Budgets, reimbursement, imports, inventory cycles, and substitution remain important risks.

## Risks and uncertainty
Principal risks are category heterogeneity, recalls and product liability, regulatory compliance, reimbursement, institutional purchasing leverage, commodity pricing, imports, supply-chain quality, inventory cycles, and weak exact-industry transaction evidence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.317 | — | OBSERVED | — |
| n | — | 394 | — | ESTIMATE | — |
| a | 0.18 | 0.3 | 0.43 | PROXY | S2, S3, S5 |
| rho | 0.22 | 0.41 | 0.6 | PROXY | S3, S5 |
| e | 0.4 | 0.62 | 0.78 | ESTIMATE | S1 |
| s5 | 0.13 | 0.26 | 0.39 | ESTIMATE | — |
| q | 0.4 | 0.61 | 0.79 | ESTIMATE | S1, S5 |
| d5 | 0.99 | 1.12 | 1.27 | PROXY | S4 |
| o | 0.94 | 0.985 | 0.998 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.50 | 1.56 | 3.27 | PROXY |
| F | 4.93 | 6.70 | 7.71 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.31 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS data span all medical equipment and supplies manufacturing and may not reflect this industry's unusually broad material and product mix.
- a: General manufacturing AI use cases do not prove labor savings in regulated or customized product workflows.
- rho: NIST's manufacturer survey and use cases cover industries with different process controls and digital maturity.
- rho: Some personal safety products may face less FDA constraint, while implants and many clinical supplies face more.
- e: No public source measures the exact intersection of six-digit activity, independence, recurring external revenue, and the target EBITDA band.
- e: The NAICS scope ranges from commodity dressings and gloves to implants, prosthetics, hospital beds, and protective equipment.
- s5: This is a structured estimate without an exact-industry transaction denominator.
- s5: Very different buyer universes and consolidation dynamics apply to implants, disposables, prosthetics, furniture, and industrial safety products.
- q: Retention varies sharply across differentiated implants, custom appliances, durable equipment, and commodity consumables.
- q: The estimate concerns retained gross benefit rather than reported accounting margin.
- d5: BLS projects NAICS 339100 rather than 339113 and does not separate clinical products from industrial safety devices.
- d5: Output value can reflect mix and quality changes rather than physical demand available to LMM domestic producers.
- o: This estimates persistence of an accountable operator of the lens's kind, not the survival of each incumbent or product line.
- o: On-site additive manufacturing and custom fabrication could shift selected prosthetic or appliance work closer to providers.

## Sources
- **S1** — [2022 NAICS Definition: 339113 Surgical Appliance and Supplies Manufacturing](https://www.census.gov/naics/?details=3391&input=339&year=2022) (accessed 2026-07-22): Exact six-digit scope and examples including orthopedic and prosthetic devices, dressings, sutures, protective devices, hospital beds, and operating-room tables.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Medical Equipment and Supplies Manufacturing](https://www.bls.gov/oes/2023/may/naics4_339100.htm) (accessed 2026-07-22): Broad medical-equipment occupational structure, including production, engineering, business, and computer work, used for the task-exposure bridge.
- **S3** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing: Text Only](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Manufacturing AI adoption, use cases, expected expansion, and barriers involving data, cost, skills, cybersecurity, and legacy systems.
- **S4** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Official ten-year employment and output projection for broad medical equipment and supplies manufacturing.
- **S5** — [Quality Management System Regulation (QMSR)](https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr) (accessed 2026-07-22): Finished-device quality-system applicability, ISO 13485 incorporation, risk-management requirements, and inspection framework.
