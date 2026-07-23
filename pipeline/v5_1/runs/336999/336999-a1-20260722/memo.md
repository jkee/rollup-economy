# 336999 — All Other Transportation Equipment Manufacturing

*v5.1 Stage 1 research memo. Run `336999-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.01 · L 0.77 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat vehicles, proprietary parts, fleet uptime, and dealer support create durable physical demand plus AI-addressable engineering and service workflows.
**Weakness:** The residual code is highly heterogeneous, and narrowed demand remains cyclical while much of the workforce performs physical production and repair.

## Business-model lens
- Included: US manufacturers of powered off-road and low-speed specialty transportation equipment, including all-terrain vehicles, snowmobiles, golf carts, similar passenger carriers, and go-carts, with repeat model, parts, accessory, warranty, fleet-support, or service revenue sold to external customers in the lower-middle-market band.
- Excluded: Animal-drawn vehicle businesses, bespoke race-car builders, one-off fabricators without recurring or repeat customer work, businesses assigned to motorcycles, bicycles, military vehicles, boats, rail, aerospace, or ordinary motor vehicles, and captive units, shells, or financing vehicles.
- Customer and revenue model: Customers include dealers, rental and resort fleets, golf courses, commercial sites, recreational users, municipalities, and specialty distributors. Revenue combines vehicles with repeat model orders, replacement parts, accessories, warranty work, fleet support, and sometimes direct maintenance or refurbishment.
- Deviation from default lens: The residual code combines animal-drawn vehicles, bespoke race cars, and powered recreational or low-speed vehicles, which have incompatible demand and operating models. The lens is narrowed to powered off-road and low-speed specialty vehicles with repeat or aftermarket work for coherence, not attractiveness.

## Executive view
A coherent screen requires narrowing this residual code to powered off-road and low-speed specialty vehicles with repeat model or aftermarket work. AI can assist engineering, dealer support, warranty, and administration, but production and repair dominate much of the labor base. The addressable firms face real product demand alongside pronounced discretionary and product-cycle risk.

## How AI changes the work
AI can improve quoting, product configuration, engineering documentation, procurement, scheduling, marketing, dealer support, warranty triage, visual inspection, and connected diagnostics. Welding, machining, assembly, testing, repair, and material handling remain physical, while safety-critical uses require validated data and human review.

## Value capture
Brands, dealer networks, regulatory know-how, installed fleets, and proprietary parts help retain value. Competitive model pricing, promotions, dealer economics, procurement leverage, warranty commitments, and component-cost transparency limit how much productivity remains with the manufacturer.

## Firm availability
The estimated firm population must be filtered heavily because the code includes incompatible products and the dataset margin bridge uses an auto-parts proxy. A bottom-up map is required to identify businesses with qualifying earnings, recurring or repeat customer work, and transferable dealer or fleet relationships.

## Demand durability
The broad transportation-equipment forecast shows real output growth, but it contains products outside the narrowed lens. ATVs, snowmobiles, golf carts, and low-speed carriers remain physical products with parts and support needs, yet demand can move sharply with weather, leisure spending, financing, dealer inventories, and fleet replacement cycles.

## Risks and uncertainty
Principal risks include residual-code aggregation, discretionary demand, model obsolescence, electrification investment, battery and component supply, dealer concentration, product recalls, safety liability, emissions compliance, and import competition. Firm eligibility and transfer rates are unobserved, and broad output growth may be driven by excluded segments.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1553 | — | OBSERVED | — |
| n | — | 68 | — | ESTIMATE | — |
| a | 0.2 | 0.31 | 0.43 | PROXY | S1, S3 |
| rho | 0.23 | 0.4 | 0.58 | ESTIMATE | S3, S5, S6 |
| e | 0.27 | 0.44 | 0.61 | ESTIMATE | S2 |
| s5 | 0.12 | 0.22 | 0.34 | ESTIMATE | — |
| q | 0.37 | 0.57 | 0.73 | ESTIMATE | S5, S6 |
| d5 | 0.88 | 1.07 | 1.26 | PROXY | S4, S5, S6 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S2, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.29 | 0.77 | 1.55 | ESTIMATE |
| F | 1.87 | 3.26 | 4.37 | ESTIMATE |
| C | 7.40 | 10.00 | 10.00 | ESTIMATE |
| D | 8.36 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source includes motorcycles, bicycles, and military armored vehicles outside the narrowed lens.
- a: The task mapping estimates exposure rather than observed automation and does not measure firm-level variation in production integration.
- rho: Manufacturing AI examples establish technical feasibility rather than adoption rates for specialty-vehicle firms.
- rho: Safety, emissions, product-liability, dealer-system, and legacy-data constraints are not directly measured.
- e: The official industry definition establishes product breadth but not recurring revenue or transferability.
- e: The assigned firm count is a margin-bridged estimate using an auto-parts margin proxy that may not fit the residual industry's product mix.
- s5: This is bounded judgment without observed six-digit control-transfer evidence.
- s5: Small private transactions and product-line divestitures are incompletely disclosed.
- q: No source directly measures sharing of AI-enabled benefits.
- q: Retention is likely higher in proprietary parts and diagnostics than in competitively sold new vehicles.
- d5: The BLS output series is broader than both the six-digit code and narrowed lens.
- d5: Real output is not a pure unit measure and may reflect product mix or quality change.
- d5: The narrowed products have different seasonality, end markets, and sensitivity to discretionary spending.
- o: The estimate applies after the demand change in d5 and avoids double counting volume loss.
- o: Direct-to-consumer distribution and embedded remote diagnostics can reduce some dealer or field-service work without replacing physical production.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 336900 Other Transportation Equipment Manufacturing](https://www.bls.gov/oes/2023/may/naics4_336900.htm) (accessed 2026-07-22): Broader-industry occupation mix and wages, including production, repair, engineering, office, business, computer, sales, and material-moving roles.
- **S2** — [2022 NAICS Definition: 336999 All Other Transportation Equipment Manufacturing](https://www.census.gov/naics/?details=336999&input=336999&year=2022) (accessed 2026-07-22): Official industry scope and illustrative products, establishing the need to narrow the heterogeneous residual code.
- **S3** — [Artificial Intelligence for Energy: Opportunities for a Modern Grid and Clean Energy Economy](https://www.energy.gov/sites/default/files/2024-04/AI%20EO%20Report%20Section%205.2g%28i%29_043024.pdf) (accessed 2026-07-22): Manufacturing AI applications including automated visual quality control, advanced characterization, operations optimization, and predictive maintenance.
- **S4** — [Industry Employment and Output Projections, 2024 to 2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Employment and real-output projection for broader NAICS 336900 used as the demand-growth proxy.
- **S5** — [All-Terrain Vehicles: Business Guidance](https://www.cpsc.gov/Business--Manufacturing/Business-Education/Business-Guidance/ATV) (accessed 2026-07-22): Mandatory ATV safety-standard, certification, labeling, action-plan, and compliance obligations supporting accountable product work.
- **S6** — [Regulations for Emissions from Recreational Vehicles](https://www.epa.gov/regulations-emissions-vehicles-and-engines/regulations-emissions-recreational-vehicles) (accessed 2026-07-22): Current federal emissions standards, testing, certification, and compliance framework covering snowmobiles and all-terrain vehicles.
