# 322299 — All Other Converted Paper Product Manufacturing

*v5.1 Stage 1 research memo. Run `322299-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.18 · L 0.70 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat custom specifications and fragmented quote-to-production workflows create usable opportunities in estimating, order handling, planning, procurement, and quality documentation.
**Weakness:** A residual, heterogeneous NAICS code makes product mix, firm eligibility, demand, and transferability unusually hard to infer from industry-level evidence.

## Business-model lens
- Included: US lower-middle-market converters supplying repeat business-to-business runs of molded-pulp egg cartons, food trays and containers, industrial or protective paper components, and other specification-driven die-cut or converted paper products not classified elsewhere.
- Excluded: One-off or trend-driven consumer paper novelties and decorative crepe-paper businesses, captive converters, upstream mills, pure distributors, non-control financing vehicles, and owner-dependent craft operations without transferable production and customer relationships.
- Customer and revenue model: Repeat unit sales and production runs to food producers, distributors, industrial customers, packers, and private-label buyers under purchase orders, supply agreements, or recurring specifications.
- Deviation from default lens: The residual NAICS category combines molded-pulp food packaging, industrial converted components, crepe paper, and paper novelties with materially different demand and commercial models. For coherence, the lens retains repeat B2B molded-pulp and specification-driven converted-product suppliers and excludes novelty-led consumer businesses.

## Executive view
The coherent B2B core of this residual industry has repeat specification-driven orders and a moderate administrative and planning layer that AI can improve. Most labor remains physical, and opportunity varies sharply by product family, customer concentration, and plant systems.

## How AI changes the work
AI can parse customer specifications, assist estimating and tooling documentation, check order and artwork changes, recommend schedules, triage inventory and quality exceptions, draft compliance records, and accelerate customer service. Molding, die-cutting, machine tending, maintenance, material movement, packing, and accountable physical release remain operator work.

## Value capture
Customized tooling and qualifications can protect savings for a period, while commodity molded-pulp and standard converted products face competitive rebids and buyer negotiation. Improvements tied to speed, reduced errors, and reliable service may retain better than transparent unit-cost reductions.

## Firm availability
The supplied dataset estimates 112 firms in the broad economic band, but the residual code mixes fundamentally different products. Actual eligibility under the narrowed B2B lens requires firm-level product, ownership, customer, and earnings verification, and control-transfer evidence is not denominator-matched.

## Demand durability
Molded-fiber food and protective products benefit from recurring physical shipment needs and potential substitution toward fiber, while material reduction, reuse, imports, and varied niche-product cycles create uncertainty. Remaining quantity still requires a physical converter.

## Risks and uncertainty
The largest uncertainty is category heterogeneity, followed by six-digit occupation mix, firm-level eligibility, real shipment volumes, customer concentration, food-contact requirements, and implementation readiness. The provided compensation and firm-count inputs mix vintages and apply a common margin bridge to diverse products.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2205 | — | OBSERVED | — |
| n | — | 112 | — | ESTIMATE | — |
| a | 0.09 | 0.18 | 0.29 | PROXY | S1, S2 |
| rho | 0.25 | 0.44 | 0.63 | ESTIMATE | S4 |
| e | 0.37 | 0.56 | 0.72 | ESTIMATE | S3 |
| s5 | 0.09 | 0.18 | 0.3 | ESTIMATE | — |
| q | 0.3 | 0.52 | 0.72 | ESTIMATE | S4 |
| d5 | 0.93 | 1.05 | 1.19 | ESTIMATE | S3, S4, S5 |
| o | 0.9 | 0.97 | 1 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.20 | 0.70 | 1.61 | ESTIMATE |
| F | 2.50 | 4.04 | 5.19 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.37 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS population is NAICS 322, not 322299 or the narrowed lens.
- a: Occupational employment is not itself a measure of task substitutability or current AI adoption.
- rho: This is bounded judgment rather than an observed five-year adoption rate.
- rho: Food-contact requirements apply only to part of the narrowed lens.
- e: The provided n uses a common paper-industry margin bridge despite diverse products.
- e: Narrowing makes eligibility especially sensitive to unknown product mix.
- s5: No six-digit, lens-matched control-transfer series was found.
- s5: Asset-only plant closures and internal reorganizations must be excluded.
- q: No source directly measures retention of AI-derived savings.
- q: Capture differs greatly between custom molded components and commodity trays or cartons.
- d5: No constant-price, constant-quality forecast exists for the narrowed lens.
- d5: EPA waste data are broad, historical, and not a forecast of 322299 demand.
- d5: Policy-driven fiber substitution can be offset by material reduction or alternative reusable formats.
- o: Import displacement can remove a US operator even when end demand persists.
- o: The residual category includes products with different substitution pathways.

## Sources
- **S1** — [Paper Manufacturing - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics3_322000.htm) (accessed 2026-07-22): For NAICS 322, BLS reports production occupations at 193,250 workers and 53.51% of employment, material-moving occupations at 12.88%, maintenance/repair at 8.47%, office/administrative support at 7.48%, management at 5.06%, and business/financial operations at 3.22%.
- **S2** — [Paper Manufacturing: NAICS 322](https://www.bls.gov/iag/tgs/iag322.htm) (accessed 2026-07-22): BLS describes converted paper products as being made through cutting and shaping techniques and reports 87,050 paper-goods machine operators in the broader subsector in 2025.
- **S3** — [2022 NAICS Definition: 322299 All Other Converted Paper Product Manufacturing](https://www.census.gov/naics/?details=32229&input=32229&year=2022) (accessed 2026-07-22): Census defines this residual industry and lists molded-pulp egg cartons, food containers and trays, crepe paper, non-office die-cut products, and paper novelties, supporting the heterogeneity judgment.
- **S4** — [Meat and Poultry Packaging Materials](https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/meat-and-poultry-packaging) (accessed 2026-07-22): USDA states that food-packaging materials such as food dishes and egg cartons are approved for specific uses, are generally single-use, and that packaging materials must be regulated for specific food uses because chemicals can migrate into food.
- **S5** — [Paper and Paperboard: Material-Specific Data](https://19january2021snapshot.epa.gov/facts-and-figures-about-materials-waste-and-recycling/paper-and-paperboard-material-specific-data_.html) (accessed 2026-07-22): EPA reports 67.39 million tons of paper and paperboard generated in municipal solid waste in 2018, 45.97 million tons recycled, and a 20.8% recycling rate for non-corrugated paper containers and packaging; used as broad context for physical scale and end-of-life constraints, not a demand forecast.
