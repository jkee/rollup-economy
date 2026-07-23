# 212311 — Dimension Stone Mining and Quarrying

*v5.1 Stage 1 research memo. Run `212311-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.48 · L 1.42 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Scarce permitted reserves with distinctive, consistently recoverable stone and durable specification demand.
**Weakness:** A highly physical and cyclical extraction model exposed to imports, substitutes, reserve variability, and site-specific liabilities.

## Business-model lens
- Included: Independent lower-middle-market operators whose principal activity is developing quarry sites and extracting dimension stone as rough blocks or slabs, including granite, limestone, marble, sandstone, slate, quartzite, dolomite, and specialty natural stone sold for architectural, building, landscape, monument, and related uses.
- Excluded: Crushed and broken stone mining, sand and gravel mining, lime production, downstream dressing and fabrication of cut-stone products, installation and masonry contracting, distributors and importers without quarry operations, mineral-rights-only owners, and captive quarries not independently marketable.
- Customer and revenue model: B2B sales of rough blocks, slabs, and irregular stone to fabricators, distributors, monument companies, landscape suppliers, architects' specified supply chains, and construction customers. Revenue is shipment- and project-driven, with economics shaped by deposit quality, permitted reserves, extraction yield, freight radius, stone aesthetics, and construction cycles.
- Deviation from default lens: none

## Executive view
Dimension-stone quarrying is a reserve-, permit-, equipment-, and craft-intensive physical business. AI has useful roles in mapping, selective extraction planning, maintenance, dispatch, sales matching, and paperwork, but does not remove the quarry, heavy equipment, material handling, or accountable operating team.

## How AI changes the work
The most credible applications are drone and geological-data interpretation, cut and recovery planning, equipment diagnostics, image-based defect review, scheduling, dispatch, estimating, permitting support, inventory description, and customer service. Extraction, splitting, rigging, inspection, maintenance, and safe movement of heavy blocks remain physically constrained.

## Value capture
The strongest economic transmission comes from more saleable stone per bench, fewer equipment failures, lower waste, and better placement of unique inventory. Small scale, uneven data, capital needs, and construction-channel bargaining may limit conversion into sustained margin.

## Firm availability
The industry includes numerous regional and specialty quarry operators across granite, limestone, sandstone, slate, marble, and other stones. Marketable firms require transferable mineral rights or leases, permitted reserves, reliable yield, equipment and labor depth, environmental compliance, and customer relationships that survive the owner.

## Demand durability
Natural stone remains valued for appearance, provenance, durability, restoration, monuments, landscape, and premium architecture. Demand is cyclical and fashion-sensitive, while alternative surfaces and imported stone constrain domestic quarry growth.

## Risks and uncertainty
Key risks are reserve quality and life, permitting and reclamation liabilities, safety, geotechnical conditions, yield variability, equipment downtime, skilled-labor availability, freight, customer concentration, imported material, substitutes, project cycles, and the separation between quarrying and downstream fabrication economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3599 | — | OBSERVED | — |
| n | — | 83 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.32 | PROXY | S1 |
| rho | 0.3 | 0.47 | 0.63 | ESTIMATE | S1, S3 |
| e | 0.55 | 0.68 | 0.8 | ESTIMATE | S1, S3 |
| s5 | 0.15 | 0.27 | 0.42 | ESTIMATE | S3 |
| q | 0.48 | 0.67 | 0.82 | ESTIMATE | S3 |
| d5 | 0.92 | 1.02 | 1.15 | ESTIMATE | S3, S4 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.52 | 1.42 | 2.90 | ESTIMATE |
| F | 3.31 | 4.48 | 5.41 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.83 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS data cover all NAICS 212300 nonmetallic mining rather than dimension stone alone.
- a: Occupation shares are not task shares.
- a: Dimension-stone quarries may use more selective extraction and manual quality judgment than high-volume aggregate operations.
- rho: No direct task-level AI adoption study was available for dimension-stone quarries.
- rho: Digitally mapped, well-instrumented quarries may realize more substitution than small legacy sites with limited data infrastructure.
- e: Actual capture depends on quarry scale, equipment age, data quality, reserve characteristics, utilization, and whether the operator can sell incremental recovery without discounting.
- s5: Substitution differs substantially by monument, structural, veneer, countertop, landscape, restoration, and prestige architectural uses.
- s5: The extraction-only industry may lose or gain share independently of downstream fabricators and imported finished products.
- q: No direct customer-retention data were available.
- q: Quality is strongest for distinctive or historically specified stones and weaker for common colors and undifferentiated rough material.
- d5: Construction spending covers many materials and reflects price as well as volume.
- d5: Dimension stone is a small, specification-driven share of construction, and quarry demand can diverge from aggregate building activity.
- d5: Regional freight economics and individual stone fashions can dominate national trends.
- o: Very small quarries may already combine leadership roles.
- o: Remote monitoring and centralized back offices could consolidate some functions across multi-site operators.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 212300](https://www.bls.gov/oes/2023/may/naics4_212300.htm) (accessed 2026-07-22): Broader nonmetallic-mining occupation mix used as the task-exposure proxy.
- **S2** — [NAICS Sector 21: Dimension Stone Mining and Quarrying](https://www.census.gov/naics/resources/archives/sect21.html) (accessed 2026-07-22): Official industry scope and distinction between quarry extraction and downstream stone-product manufacturing.
- **S3** — [Dimension Stone Statistics and Information](https://www.usgs.gov/centers/national-minerals-information-center/dimension-stone-statistics-and-information) (accessed 2026-07-22): Stone types, product definition, selection criteria, and official production, trade, and demand publication context.
- **S4** — [Monthly Construction Spending, May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-22): Current total, private nonresidential, public, and educational construction-spending conditions.
