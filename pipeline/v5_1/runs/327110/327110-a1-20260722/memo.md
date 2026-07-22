# 327110 — Pottery, Ceramics, and Plumbing Fixture Manufacturing

*v5.1 Stage 1 research memo. Run `327110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.23 · L 1.59 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Specification-based physical products create durable demand and useful AI-assisted quality and process opportunities.
**Weakness:** Heterogeneous end markets and labor-intensive physical production limit confidence in an industry-wide opportunity.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly supplying vitreous-china plumbing fixtures and accessories, porcelain electrical insulators and parts, ceramic or ferrite magnets, chemical stoneware, and other specification-based ceramic goods to external distributors, builders, OEMs, utilities, and industrial customers.
- Excluded: Captive units, shells, pottery made and sold primarily on site, artistic statuary, and predominantly direct-to-consumer tableware or decorative-pottery models; ceramic tile, brick, roofing tile, and refractories classified in NAICS 327120.
- Customer and revenue model: Repeat distributor and OEM purchase orders, builder/project bids, utility and industrial specifications, and catalog sales, generally priced per fixture, piece, lot, or project.
- Deviation from default lens: The code spans project-driven plumbing fixtures, technical electrical and magnetic components, industrial chemical stoneware, and artisan or consumer pottery. The lens is narrowed to repeat external B2B supply of specification-based fixtures and technical ceramic goods so customer behavior and transferability are coherent; the excluded share is reflected in eligibility.

## Executive view
The coherent opportunity lies in repeat B2B fixtures and technical ceramics, not the code's artisan and direct-consumer tail. AI can aid quoting, planning, kiln and quality analytics, inspection, maintenance, and paperwork, but shaping, glazing, firing, finishing, testing, and handling remain physical. End-market diversity stabilizes demand while making averages less reliable.

## How AI changes the work
Promising applications include specification and RFQ processing, production schedules, kiln anomaly detection, defect recognition, maintenance prediction, and quality documentation. Ceramic process variation, sparse defect data, destructive testing, old controls, and customer approvals limit implementation. Yield improvement alone is not labor substitution.

## Value capture
Qualified technical components can retain savings through switching friction and approval history. Standard fixtures are exposed to imports, distributor leverage, builder bids, visible retail prices, and new-project sourcing, so commercial capture decays over five years.

## Firm availability
The provided in-band count includes several distinct business models and is itself estimated. The narrowed external-supply population should contain transferable plants, but artist or owner dependence, environmental liabilities, customer concentration, and capital needs reduce eligibility and executable transfers.

## Demand durability
Replacement, renovation, construction, utility equipment, motors, and industrial processes continue to require physical ceramic products. Housing is cyclical and domestic producers face imports and alternative materials, while technical ceramics may follow different cycles from plumbing fixtures.

## Risks and uncertainty
Risks include natural-gas and electricity cost, kiln downtime, breakage, dust and worker safety, environmental compliance, product certification, imports, cyclical construction, customer concentration, and code heterogeneity. Evidence is weakest for firm product mix, contract pass-through, six-digit task hours, and control transfers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3375 | — | OBSERVED | — |
| n | — | 80 | — | ESTIMATE | — |
| a | 0.16 | 0.25 | 0.35 | PROXY | S2, S3 |
| rho | 0.28 | 0.47 | 0.64 | PROXY | S3 |
| e | 0.4 | 0.6 | 0.78 | ESTIMATE | S1 |
| s5 | 0.14 | 0.25 | 0.37 | PROXY | S5 |
| q | 0.26 | 0.46 | 0.65 | ESTIMATE | — |
| d5 | 0.94 | 1.04 | 1.16 | PROXY | S1, S4, S6 |
| o | 0.93 | 0.98 | 0.995 | ESTIMATE | S1 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.60 | 1.59 | 3.02 | PROXY |
| F | 2.74 | 4.13 | 5.12 | ESTIMATE |
| C | 5.20 | 9.20 | 10.00 | ESTIMATE |
| D | 8.74 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS evidence is broader than six-digit 327110 and the narrowed lens.
- a: Process-yield gains are not labor substitution unless they remove hours or avoid hiring.
- rho: General manufacturing adoption does not establish implementation in ceramics.
- rho: Safety, electrical, and plumbing qualification can lengthen deployment.
- e: No firm-level product-mix census was found.
- e: The provided firm count uses a broad sector margin and may misclassify firms into the EBITDA band.
- s5: No six-digit qualifying-transfer denominator was found.
- s5: Succession fragility is not a sale probability.
- q: Capture is likely lower in standard plumbing fixtures and higher in approved technical ceramic components.
- q: No representative contract dataset was found.
- d5: The sanitary-ware forecast is commercial, global, value-based, and covers only part of the code.
- d5: One month of housing starts is cyclical context, not a five-year demand forecast.
- d5: Technical ceramics and plumbing fixtures can move differently.
- o: An operator may remain necessary while production shifts to offshore or larger suppliers.
- o: The estimate does not predict domestic share.

## Sources
- **S1** — [Census 2022 NAICS definition: 327110 Pottery, Ceramics, and Plumbing Fixture Manufacturing](https://www.census.gov/naics/?details=327110&input=327110&year=2022) (accessed 2026-07-22): Defines shaping, molding, glazing, and firing pottery, ceramics, plumbing fixtures, and electrical supplies and lists fixtures, magnets, chemical stoneware, statuary, tableware, and electrical insulators.
- **S2** — [BLS 2024-34 industry-occupation matrix data, by industry](https://www.bls.gov/emp/tables/industry-occupation-matrix-industry.htm) (accessed 2026-07-22): Provides the official broader clay-product and refractory manufacturing occupation context used for the task-exposure bridge.
- **S3** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Reports 46% use of AI tools and more than 80% expecting increased use in two years, and identifies manufacturing use cases and adoption barriers.
- **S4** — [Ceramic Sanitary Ware global market overview](https://www.marketresearch.com/Global-Industry-Analysts-v1039/Ceramic-Sanitary-Ware-41343262/) (accessed 2026-07-22): Reports a global market estimate of $29.1 billion in 2025 and $43.5 billion in 2032 at 5.9% CAGR, plus a $9.0 billion US estimate for 2025; used only as a sanitary-ware demand proxy.
- **S5** — [Deloitte Private survey: generational disparities in family-business succession planning](https://www2.deloitte.com/us/en/pages/about-deloitte/articles/press-releases/deloitte-private-survey-generational-disparatires-emerge-insuccession-planning-and-priorities-shaping-family-businesses.html) (accessed 2026-07-22): Describes a January 2024 survey of 500 US family-enterprise respondents and reports that 24% of current-generation respondents strongly agreed their succession plan would withstand departure of an important family employee.
- **S6** — [Census Monthly New Residential Construction, June 2026](https://www.census.gov/construction/nrc/current/index.html) (accessed 2026-07-22): Reports June 2026 housing starts 3.0% below the revised May rate and 2.3% below the June 2025 rate, providing current US construction-cycle context.
