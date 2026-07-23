# 212312 — Crushed and Broken Limestone Mining and Quarrying

*v5.1 Stage 1 research memo. Run `212312-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.60 · L 0.59 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Essential local demand for aggregate and limestone inputs combined with scarce permitted reserves near customers.
**Weakness:** A capital- and equipment-intensive commodity model with cyclical volumes, environmental liabilities, and minimal direct labor displacement from AI.

## Business-model lens
- Included: Independent lower-middle-market operators principally developing quarry sites, mining or quarrying crushed and broken limestone and related calcareous rocks, and mechanically beneficiating limestone through crushing, grinding, pulverizing, screening, or sizing for construction aggregate, cement and lime feedstock, agriculture, and industrial uses.
- Excluded: Dimension-stone quarries, granite and other non-limestone crushed-stone operations, sand and gravel pits, bituminous limestone mining, lime and cement manufacturing, ready-mix and asphalt production, hauling-only and distribution-only businesses, mineral-rights-only owners, and captive quarries not independently marketable.
- Customer and revenue model: High-volume, shipment-based B2B sales to road contractors, ready-mix and asphalt producers, cement and lime plants, agricultural distributors, industrial users, and public infrastructure projects. Economics depend on permitted reserves, plant throughput, product gradations, quality, utilization, energy and maintenance, and delivered freight radius.
- Deviation from default lens: none

## Executive view
Crushed-limestone quarrying is an essential, local, freight-constrained materials business. AI can improve planning, uptime, process control, dispatch, and paperwork, but the core value remains permitted reserves, plant and mobile equipment, haul economics, and safe physical production.

## How AI changes the work
The best applications are resource and mine planning, blast and fragmentation support, predictive maintenance, crusher and screen optimization, computer-vision safety and quality monitoring, dispatch, truck-cycle analysis, ticketing, forecasting, compliance documentation, and back-office automation. Drilling, blasting, loading, processing, maintenance, sampling, and hauling remain embodied work.

## Value capture
Because small improvements in uptime, fuel, yield, and truck turns apply to large volumes, operational AI can matter despite limited knowledge-worker exposure. Local scarcity and permit barriers support capture, while bids, large customers, and unsold incremental capacity can dissipate benefits.

## Firm availability
The fragmented local-market structure creates many independent quarries and small platforms, but asset quality varies widely. Transferable permits, reserve life, stripping needs, plant condition, reclamation obligations, haul radius, customer concentration, and embedded environmental liabilities are central to marketability.

## Demand durability
Limestone is fundamental to aggregate, cement, lime, agriculture, and industrial processes. Infrastructure maintenance and expansion provide a durable floor, though shipment timing follows construction cycles and weather, and recycling can take a growing share of selected applications.

## Risks and uncertainty
Key risks are reserve and quality variation, permitting and zoning, reclamation, dust and water management, blasting and worker safety, energy and maintenance cost, equipment downtime, truck availability, customer concentration, construction cycles, project timing, recycled-material adoption, and local competitive capacity.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1855 | — | OBSERVED | — |
| n | — | 301 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S1, S4 |
| rho | 0.28 | 0.44 | 0.6 | ESTIMATE | S1, S4 |
| e | 0.62 | 0.75 | 0.86 | ESTIMATE | S3, S4 |
| s5 | 0.08 | 0.16 | 0.28 | ESTIMATE | S3, S4 |
| q | 0.55 | 0.73 | 0.87 | ESTIMATE | S3, S4 |
| d5 | 0.99 | 1.08 | 1.19 | ESTIMATE | S3, S4, S5, S6 |
| o | 0.97 | 0.99 | 1 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.59 | 1.25 | ESTIMATE |
| F | 4.45 | 5.81 | 6.91 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.60 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation evidence covers all NAICS 212300 nonmetallic mining rather than limestone quarries specifically.
- a: Occupation shares are not task shares.
- a: Large automated quarries and small local operations have materially different digital readiness.
- rho: No direct task-level AI adoption evidence was available for six-digit limestone operations.
- rho: Realization depends on sensor coverage, fleet age, geological data, connectivity, and the repeatability of plant processes.
- e: Capture depends on local competition, reserve and permit position, plant utilization, fleet ownership, data quality, and whether gains relieve a bottleneck or merely create unsold capacity.
- s5: Substitution varies by specification, geology, local recycled supply, cement chemistry, and customer acceptance.
- s5: Decarbonization of cement may reduce some limestone demand while infrastructure reuse increases recycled aggregate availability.
- q: No direct customer-retention data were available.
- q: Quality varies sharply by metropolitan proximity, remaining reserve life, permitted capacity, rail or water access, and the number of competing quarries within an economic haul radius.
- d5: Construction spending reflects price as well as material volume.
- d5: Funding announcements and obligations may convert to quarry shipments with long and variable lags.
- d5: Cement, lime, agriculture, and industrial markets can diverge from road aggregate demand.
- o: Centralized dispatch and shared back offices can consolidate support across multi-site platforms.
- o: Small operators may already combine management functions, limiting further layer removal.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 212300](https://www.bls.gov/oes/2023/may/naics4_212300.htm) (accessed 2026-07-22): Broader nonmetallic-mining occupation mix used as the task-exposure proxy.
- **S2** — [NAICS Sector 21: Crushed and Broken Limestone Mining and Quarrying](https://www.census.gov/naics/resources/archives/sect21.html) (accessed 2026-07-22): Official scope, included beneficiation, related rock types, and industry exclusions.
- **S3** — [Crushed Stone Statistics and Information](https://www.usgs.gov/centers/national-minerals-information-center/crushed-stone-statistics-and-information) (accessed 2026-07-22): Official commodity context, uses, supply, demand, and current publication series for crushed stone.
- **S4** — [Building America: USGS and the Nation's Construction Materials](https://www.usgs.gov/mission-areas/geology-energy-minerals/science/building-america-usgs-and-nations-construction) (accessed 2026-07-22): Construction-material essentiality, local supply constraints, mapping technology, infrastructure uses, and material-quality risk.
- **S5** — [Monthly Construction Spending, May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-22): Current total, private nonresidential, public, educational, and highway construction conditions.
- **S6** — [Better Utilizing Investments to Leverage Development Grant Program](https://www.transportation.gov/BUILDgrants) (accessed 2026-07-22): Current federal surface-transportation project funding and award evidence.
