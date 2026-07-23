# 337121 — Upholstered Household Furniture Manufacturing

*v5.1 Stage 1 research memo. Run `337121-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.19 · L 0.69 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat retailer and private-label programs create recurring demand where AI can improve design, planning, ordering, and customer-service workflows.
**Weakness:** Highly physical production, strong channel bargaining, discretionary demand, and import substitution constrain implementable and retainable gains.

## Business-model lens
- Included: US stock or custom upholstered household-furniture manufacturers in the lower-middle-market band that provide recurring or repeat outsourced production, private-label, retailer, designer, dealer, hospitality, warranty, or replenishment work to external customers.
- Excluded: Reupholstery and repair shops, transportation seating, mattresses, nonupholstered furniture, one-off craft production without recurring or repeat customers, captive units, shells, and non-control financing vehicles.
- Customer and revenue model: Customers include furniture retailers, dealers, designers, private-label brands, hospitality buyers, distributors, and households. Revenue comes from stock collections or custom orders and can include repeat retailer replenishment, private-label programs, options and fabrics, warranty replacement, and after-sale support.
- Deviation from default lens: none

## Executive view
Eligible firms are upholstered-furniture manufacturers with repeat retailer, private-label, dealer, designer, or hospitality programs. AI can improve design visualization, merchandising, planning, ordering, support, and inspection, but the production process remains intensely physical. Durable product demand is offset by discretionary timing, channel power, and import displacement risk.

## How AI changes the work
AI can accelerate concept visualization, option configuration, merchandising content, demand planning, procurement, order entry, customer support, quality documentation, and some vision inspection. Cutting, sewing, padding, upholstering, assembly, finishing, packing, and delivery remain physical and variable-material work.

## Value capture
Customization, design, domestic responsiveness, lead time, and quality support retention. Large retailers and private-label customers can demand lower prices or allowances, while promotions, comparable styles, returns, warranties, and imports increase pass-through.

## Firm availability
The assigned firm population is estimated using a margin bridge that may not fit furniture economics. Eligibility further depends on target earnings, repeat external-customer programs, transferable operations, and manageable concentration, requiring a bottom-up company map.

## Demand durability
Households continue to require physical seating, and flammability testing, labeling, delivery, and warranty preserve operator accountability. Purchase timing is discretionary and linked to moves, housing, credit, and retailer inventory cycles. Broad furniture output is projected to rise modestly, but domestic production can lose share to imports.

## Risks and uncertainty
Key risks are retailer concentration, imports, promotions, freight, fabric and foam costs, inventory corrections, fashion obsolescence, returns, flammability compliance, product liability, and labor-intensive variable-material production. Firm eligibility, domestic demand share, and transfer rates are not observed directly.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1661 | — | OBSERVED | — |
| n | — | 203 | — | ESTIMATE | — |
| a | 0.14 | 0.22 | 0.32 | PROXY | S2, S3 |
| rho | 0.29 | 0.47 | 0.64 | ESTIMATE | S3, S5 |
| e | 0.28 | 0.44 | 0.6 | ESTIMATE | S1 |
| s5 | 0.12 | 0.22 | 0.34 | ESTIMATE | — |
| q | 0.29 | 0.47 | 0.64 | ESTIMATE | S1, S5 |
| d5 | 0.88 | 1.03 | 1.17 | PROXY | S4, S6 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.27 | 0.69 | 1.36 | ESTIMATE |
| F | 3.31 | 4.87 | 6.03 | ESTIMATE |
| C | 5.80 | 9.40 | 10.00 | ESTIMATE |
| D | 7.74 | 9.79 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source is broader than the six-digit industry and dated 2016.
- a: The task mapping estimates exposure rather than observed AI use and may not capture differences between stock, custom, and private-label producers.
- rho: Manufacturing AI evidence establishes feasibility rather than adoption rates in upholstered furniture.
- rho: Legacy systems, highly variable materials, visual quality judgments, and small-firm digital maturity are not directly measured.
- e: The official definition confirms stock and custom production but not recurring relationships or transferability.
- e: The assigned firm count uses a machinery margin bridge that may be materially different from upholstered-furniture economics.
- s5: This is bounded judgment without observed industry-specific transfer rates.
- s5: Small private transactions, plant acquisitions, and brand-only deals are incompletely disclosed and may not represent control transfers of eligible operations.
- q: No source directly measures commercial retention of AI-enabled benefits.
- q: Retention is likely higher for differentiated custom work than for replenishment programs sold through concentrated retailers.
- d5: The output projection covers the entire furniture sector rather than NAICS 337121.
- d5: Housing units are a driver rather than a direct measure of upholstered-furniture quantity.
- d5: Retail inventory corrections and import share can cause domestic production to diverge sharply from final demand.
- o: The estimate applies after the demand change in d5 and avoids counting cyclical volume loss twice.
- o: Physical product demand can persist while accountable supply shifts from US lens firms to imported or retailer-controlled products.

## Sources
- **S1** — [2022 NAICS Definition: 337121 Upholstered Household Furniture Manufacturing](https://www.census.gov/naics/?details=337&input=337&year=2022) (accessed 2026-07-22): Official industry scope covering stock or custom upholstered household furniture and distinguishing reupholstery and other furniture categories.
- **S2** — [May 2016 Industry-Specific Occupational Employment and Wage Estimates: NAICS 337100](https://www.bls.gov/oes/2016/may/naics4_337100.htm) (accessed 2026-07-22): Broader furniture and cabinet occupation mix, including the production-occupation share used for the AI-exposure bridge.
- **S3** — [Artificial Intelligence for Energy: Opportunities for a Modern Grid and Clean Energy Economy](https://www.energy.gov/sites/default/files/2024-04/AI%20EO%20Report%20Section%205.2g%28i%29_043024.pdf) (accessed 2026-07-22): Manufacturing AI applications including automated visual quality control, operations optimization, and predictive maintenance.
- **S4** — [Industry Employment and Output Projections, 2024 to 2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Employment and real-output projection for the broader furniture and related product manufacturing sector.
- **S5** — [Flammable Fabrics Act Business Guidance: Upholstered Furniture](https://www.cpsc.gov/Business--Manufacturing/Business-Education/Business-Guidance/Flammable-Fabrics-Act) (accessed 2026-07-22): Federal upholstered-furniture flammability testing, labeling, and certification requirements supporting continued accountable product work.
- **S6** — [Monthly New Residential Construction, June 2026](https://www.census.gov/construction/nrc/current/index.html) (accessed 2026-07-22): Current housing permits, starts, and completions used as context for household-furniture demand and housing-cycle uncertainty.
