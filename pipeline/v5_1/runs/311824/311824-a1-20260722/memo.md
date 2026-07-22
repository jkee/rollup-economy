# 311824 — Dry Pasta, Dough, and Flour Mixes Manufacturing from Purchased Flour

*v5.1 Stage 1 research memo. Run `311824-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.75 · L 0.46 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Stable physical food demand plus repeat customer-specific supply supports a durable operator role and recurring workflow-improvement opportunity.
**Weakness:** The AI-exposed share is modest and customer bargaining can erode savings, while the exact eligible and transferable firm population is not directly observed.

## Business-model lens
- Included: Lower-middle-market manufacturers in NAICS 311824 that repeatedly supply dry pasta, prepared flour mixes, or refrigerated or frozen dough to external retail, foodservice, institutional, or food-manufacturer customers, including private-label and customer-specific production.
- Excluded: Branded manufacturers without a material repeat outsourced-supply relationship, captive plants, shell or financing entities, fresh-pasta manufacturers classified elsewhere, and businesses outside the $1-10M normalized EBITDA band.
- Customer and revenue model: Recurring product sales under private-label, institutional, ingredient, foodservice, or customer-specific arrangements; revenue is typically per unit or shipment, with some contracts adjusting prices for input costs.
- Deviation from default lens: The default recurring outsourced-service lens is narrowed to customer-specific, private-label, institutional, ingredient, and foodservice supply because the NAICS code also contains branded consumer-product manufacturers whose principal activity is not an outsourced service.

## Executive view
The coherent target is not every 311824 manufacturer but LMM private-label, ingredient, institutional, and customer-specific suppliers with repeat external relationships. They combine durable physical demand and transferable plant assets with a moderate AI opportunity concentrated in inspection, planning, administration, quality records, and production support rather than the core physical process.

## How AI changes the work
AI can improve machine vision, anomaly detection, production scheduling, demand forecasting, order handling, quality-document review, and maintenance triage. The large production and material-moving workforce limits the exposed share, and food-safety validation, legacy controls, and customer audits slow implementation.

## Value capture
Operational savings can remain with the supplier between bids and renewals, but private-label and institutional purchasing is price-sensitive. Open-book or indexed terms, transparent input economics, cost-down requests, and competitive rebids are likely to return a meaningful share to customers over five years.

## Firm availability
The dataset estimates 83 firms in the EBITDA band, but only a subset has a material outsourced-supply model. Manufacturing owners are unusually old, creating succession pressure, while specialized equipment, working capital, and a limited small-deal buyer pool reduce the fraction of intentions that become completed qualifying transfers.

## Demand durability
Dry pasta and flour-based foods are mature staples with stable aggregate demand, supported by population and convenience, but per-capita wheat use faces dietary pressure and imported pasta competes with domestic output. Nearly all remaining quantity still needs an accountable physical operator even if plants automate further.

## Risks and uncertainty
The strongest limitations are the absence of six-digit occupation and transfer data, the mixed pasta/mix/dough population, and sparse current public contract evidence. A target can also be unattractive if it is a commodity private-label supplier with concentrated customers, mandatory cost-downs, old equipment, weak food-safety systems, or branded revenue that falls outside the lens.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1002 | — | OBSERVED | — |
| n | — | 83 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.32 | PROXY | S2, S3 |
| rho | 0.35 | 0.55 | 0.72 | PROXY | S3, S9 |
| e | 0.3 | 0.48 | 0.68 | ESTIMATE | S1, S6 |
| s5 | 0.08 | 0.15 | 0.23 | PROXY | S4, S5 |
| q | 0.28 | 0.48 | 0.68 | PROXY | S6, S8 |
| d5 | 0.96 | 1.01 | 1.07 | PROXY | S7 |
| o | 0.92 | 0.97 | 1 | PROXY | S1, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.46 | 0.92 | PROXY |
| F | 1.76 | 3.12 | 4.24 | ESTIMATE |
| C | 5.60 | 9.60 | 10.00 | PROXY |
| D | 8.83 | 9.80 | 10.00 | PROXY |

## Caveats
- a: OEWS is 2023 and only available at NAICS 311800, which includes bakeries and tortillas and therefore has a materially different occupation mix.
- a: The machine-vision example is a vendor/project account from an Italian production-equipment context, not a representative US adoption study.
- a: The estimate excludes tasks already automated on continuous production and packaging lines.
- rho: No representative adoption survey for LMM US 311824 plants was found.
- rho: Five-year implementation depends on plant layout, customer audits, and whether existing lines expose usable sensor and production data.
- rho: Physical automation capex and conventional software are included only where AI enables the exposed task opportunity.
- e: The public filing that reveals channel mix is from 2007 and a large pasta producer, not the current LMM population.
- e: NAICS data do not identify private-label or contract-manufacturing revenue at firm level.
- e: The supplied n estimate is margin-bridged and may include firms whose EBITDA or business model does not meet the lens.
- s5: Gallup is cross-industry and includes transfers by gift and rare public offerings, not only qualifying control acquisitions.
- s5: McKinsey's estimates use multiple third-party datasets and define small businesses as firms with fewer than 500 employees, broader than the lens.
- s5: No 311824-specific completed-transfer denominator was found.
- q: The pasta filing is old and from a larger issuer; contract structures may have changed.
- q: The competition study covers the UK and multiple own-label food categories rather than US 311824.
- q: Branded products may retain more benefit than the outsourced private-label and institutional lens.
- d5: Wheat-flour disappearance is broader than 311824 and does not separate domestic production from imports.
- d5: The category mixes mature dry pasta with potentially different growth patterns in dough and specialty mixes.
- d5: Constant-quality unit measures are difficult where package sizes and formulations change.
- o: Some customers may insource narrow production runs or replace mixes with alternative formats.
- o: The value is about the need for an operator, not the amount of labor inside the plant.
- o: Small qualified-facility exemptions can modify some FDA requirements but do not eliminate physical production accountability.

## Sources
- **S1** — [2022 NAICS Definition: 311824 Dry Pasta, Dough, and Flour Mixes Manufacturing from Purchased Flour](https://www.census.gov/naics/?chart=2022&details=311824&input=311824) (accessed 2026-07-22): Defines the industry's included manufacturing activities and cross-references, including dry pasta, prepared flour mixes, and dough from purchased flour.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311800](https://www.bls.gov/oes/2023/may/naics4_311800.htm) (accessed 2026-07-22): Provides the broader-industry occupation mix, including 49.70% production, 13.23% transportation/material moving, 5.24% office support, 6.71% packaging-machine operators, and 1.14% inspectors.
- **S3** — [Smart sensors meet spaghetti](https://www.rina.org/en/media/news/2018/10/25/sensors-spaghetti) (accessed 2026-07-22): Describes an operating pasta-line machine-vision system that recognizes defects in real time, rejects affected pasta, and reduces reliance on manual inspection.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 52.3% of US employer businesses have owners age 55 or older and that 22% of employer-business owners planned to sell or transfer ownership within five years.
- **S5** — [Navigating the great small business ownership transition](https://www.mckinsey.com/institute-for-economic-mobility/our-insights/the-great-ownership-transfer-a-new-era-of-business-stewardship) (accessed 2026-07-22): Reports that more than 60% of owners in manufacturing, mining, and utilities are over 55, describes transfer frictions for capital-intensive firms, and estimates manufacturing ownership exits.
- **S6** — [American Italian Pasta Company Form 10-K](https://www.sec.gov/Archives/edgar/data/849667/000092290708000506/form10k_062308.htm) (accessed 2026-07-22): Documents retail private-label and institutional pasta channels, customer-specific requirements, food-processor customers, and contractual pass-through of direct-material cost changes in both directions.
- **S7** — [Wheat Sector at a Glance](https://www.ers.usda.gov/topics/crops/wheat/wheat-sector-at-a-glance) (accessed 2026-07-22): States that US wheat-flour food demand is relatively stable, gives 2025 per-capita flour use of 126.6 pounds, discusses dietary pressure, and identifies pasta and noodles as major wheat-product imports.
- **S8** — [Price inflation and competition in food and grocery manufacturing and supply](https://assets.publishing.service.gov.uk/media/65730e9633b7f2000db720e2/Price_inflation_and_competition_in_food_and_grocery_manufacturing_and_supply____.pdf) (accessed 2026-07-22): Finds strong competition among own-label food manufacturers for retailer contracts, switching, transparent supplier costs, competitive retailer pricing, and generally low or declining supplier margins.
- **S9** — [FSMA Final Rule for Preventive Controls for Human Food](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food) (accessed 2026-07-22): Requires covered food facilities to maintain hazard-based food-safety plans and preventive controls and describes binding employee qualification, training, verification, and monitoring obligations.
