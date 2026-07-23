# 337110 — Wood Kitchen Cabinet and Countertop Manufacturing

*v5.1 Stage 1 research memo. Run `337110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.15 · L 1.37 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat builder and dealer programs pair physical replacement demand with AI-addressable design, quoting, planning, and customer-service workflows.
**Weakness:** Cabinet manufacturing remains physically labor-intensive and commercially exposed to housing cycles and powerful purchasing channels.

## Business-model lens
- Included: US manufacturers of stock or custom wood and wood-laminated kitchen cabinets, bathroom vanities, and fixed countertops that provide recurring or repeat outsourced production, design-to-order, fulfillment, warranty, replacement, or support work to builders, remodelers, dealers, designers, or other external customers in the lower-middle-market band.
- Excluded: On-site finish carpentry, stone or all-plastic countertops, metal cabinets, freestanding furniture, project-only shops without recurring or repeat customer work, captive units, shells, and non-control financing vehicles.
- Customer and revenue model: Customers include homebuilders, remodelers, dealers, distributors, designers, multifamily developers, and homeowners. Revenue comes from stock programs or custom projects and may include design, measurement support, configuration, finishing, delivery coordination, warranty replacement, and repeat builder or dealer orders.
- Deviation from default lens: none

## Executive view
Eligible cabinet manufacturers combine repeat builder or dealer relationships with design-to-order and physical production. AI can improve the information flow around quoting, visualization, scheduling, procurement, and service, but a production-heavy workforce limits direct substitution. Demand is durable as a physical housing input yet cyclical with construction, remodeling, and home turnover.

## How AI changes the work
AI can assist visualization, layouts, quoting, bills of materials, order entry, purchasing, scheduling, customer communication, inspection, and production planning. Cutting, machining, assembly, sanding, finishing, packing, and delivery remain physical, while design-to-machine automation needs accurate measurements, clean catalogs, and robust exception handling.

## Value capture
Differentiated design, finish, reliability, lead time, and service can retain benefits in fixed-price work. Stock programs and concentrated builder or dealer channels face strong price comparison, procurement leverage, input-cost transparency, and renewal repricing that share gains with customers.

## Firm availability
The estimated firm population is large, but eligibility depends on repeat external-customer programs, target earnings, low owner dependence, and transferable operations. The machinery-margin bridge is imperfect for cabinet businesses, so a bottom-up company map is essential.

## Demand durability
New homes, multifamily projects, kitchen and bathroom modernization, and replacement create persistent demand for physical cabinets and vanities. Current housing indicators show continuing activity but soft permits, while the broader furniture forecast implies modest real growth. The outcome remains sensitive to rates, affordability, home turnover, and remodeling budgets.

## Risks and uncertainty
Risks include housing cyclicality, builder and dealer concentration, lumber and panel-price volatility, imports, ready-to-assemble substitution, labor and finishing constraints, measurement errors, installation failures, warranty cost, and owner dependence in custom shops. Firm eligibility and transfer rates are not observed directly.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2987 | — | OBSERVED | — |
| n | — | 660 | — | ESTIMATE | — |
| a | 0.16 | 0.25 | 0.36 | PROXY | S2, S3 |
| rho | 0.28 | 0.46 | 0.64 | ESTIMATE | S3 |
| e | 0.39 | 0.56 | 0.71 | ESTIMATE | S1 |
| s5 | 0.14 | 0.24 | 0.36 | ESTIMATE | — |
| q | 0.34 | 0.52 | 0.69 | ESTIMATE | S1, S5 |
| d5 | 0.93 | 1.05 | 1.18 | PROXY | S4, S5, S6 |
| o | 0.95 | 0.98 | 1 | ESTIMATE | S1, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.54 | 1.37 | 2.75 | ESTIMATE |
| F | 5.81 | 7.23 | 8.26 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 8.84 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source is for a broader industry group and is dated 2016.
- a: The mapping estimates current unautomated task exposure rather than observed AI deployment, and stock plants differ sharply from custom shops.
- rho: DOE examples establish technical feasibility across manufacturing rather than observed adoption in cabinet plants.
- rho: Legacy software, fragmented product catalogs, measurement variability, and small-firm digital maturity are not measured directly.
- e: The official definition covers both stock and custom production but does not measure repeat revenue or transferability.
- e: The assigned firm count is margin-bridged using a machinery margin proxy that may not reflect cabinet-manufacturing economics.
- s5: This is bounded judgment without observed industry-specific transfer rates.
- s5: Small private transactions and asset sales are often undisclosed or inconsistently classified.
- q: No source directly measures retention of AI-enabled productivity benefits.
- q: Retention is likely higher for differentiated custom programs than for stock cabinets sold through concentrated channels.
- d5: The BLS projection covers a broader furniture sector rather than NAICS 337110.
- d5: Construction spending and housing units are demand drivers rather than direct cabinet quantities.
- d5: Interest rates, home turnover, housing affordability, and repair-versus-replace choices can shift demand materially.
- o: The estimate applies after the quantity change in d5 and avoids counting cyclical volume loss twice.
- o: Imports and ready-to-assemble products may displace domestic operator work without eliminating cabinet demand itself.

## Sources
- **S1** — [Census Bureau Profile: 337110 Wood Kitchen Cabinet and Countertop Manufacturing](https://data.census.gov/profile/337110_-_Wood_kitchen_cabinet_and_countertop_manufacturing?g=010XX00US&n=337110) (accessed 2026-07-22): Official industry scope covering stock and custom wood or wood-laminated kitchen cabinets, bathroom vanities, and fixed countertops, plus cross-industry exclusions.
- **S2** — [May 2016 Industry-Specific Occupational Employment and Wage Estimates: NAICS 337100](https://www.bls.gov/oes/2016/may/naics4_337100.htm) (accessed 2026-07-22): Broader furniture and cabinet occupation mix, including the production-occupation share used for the AI-exposure bridge.
- **S3** — [Artificial Intelligence for Energy: Opportunities for a Modern Grid and Clean Energy Economy](https://www.energy.gov/sites/default/files/2024-04/AI%20EO%20Report%20Section%205.2g%28i%29_043024.pdf) (accessed 2026-07-22): Manufacturing AI applications including automated visual quality control, operations optimization, and predictive maintenance.
- **S4** — [Industry Employment and Output Projections, 2024 to 2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Employment and real-output projection for the broader furniture and related product manufacturing sector.
- **S5** — [Monthly New Residential Construction, June 2026](https://www.census.gov/construction/nrc/current/index.html) (accessed 2026-07-22): Current housing permits, starts, and completions used to contextualize cabinet demand and construction-cycle uncertainty.
- **S6** — [Construction Spending Definitions](https://www.census.gov/construction/c30/definitions.html) (accessed 2026-07-22): Definition of residential improvements, including kitchen and bathroom modernization, used to connect remodeling activity to cabinet demand.
