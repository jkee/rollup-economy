# 111992 — Peanut Farming

*v5.1 Stage 1 research memo. Run `111992-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** A durable physical crop-production need with an identifiable administrative and decision-support AI surface.
**Weakness:** The NAICS code overwhelmingly describes commodity growers, leaving the eligible recurring outsourced-service subset both tiny and unmeasured.

## Business-model lens
- Included: U.S. peanut-growing establishments in the lower-middle-market band that repeatedly provide accountable crop-production services to an external contractor, especially arrangements in which the contractor owns the commodity during production.
- Excluded: Ordinary cash-market and marketing-contract peanut farms that own and sell their crop, hobby and subscale farms, captive operations, passive landholding, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring seasonal production fees or economically equivalent grower compensation paid by an external contractor for field execution, quality compliance, and delivery; this is distinct from a farm simply selling its own commodity.
- Deviation from default lens: The code is narrowed to the small production-service subset because Census defines the industry as establishments growing peanuts, while USDA distinguishes production contracts, where the contractor owns the commodity, from the marketing contracts that predominate in crop farming. Combining commodity sellers with true contracted production services would make the screen incoherent.

## Executive view
Peanut Farming is primarily commodity production, not an outsourced service. The coherent lens is therefore a narrow and poorly measured subset of repeat production arrangements in which an external contractor owns or commissions the production activity. Within that subset, AI can improve planning, records, compliance, and decision support, but most field execution remains physical and buyer leverage is material.

## How AI changes the work
The practical AI surface is concentrated in office and management work: production records, scheduling, purchasing support, agronomic information synthesis, contract and compliance documentation, and exception detection. Core planting, chemical application, maintenance, harvest, and delivery are equipment- and field-dependent; precision guidance is already established, so already-automated work is not counted again.

## Value capture
Savings may persist where they improve reliability or quality, but concentrated shellers and recurring bilateral contract negotiation make pass-through plausible. Open-book or formula-based production arrangements would compress retention further. Commodity price movements, government support, and crop insurance are separate from retention of an implemented operating benefit.

## Firm availability
Eligibility is the central constraint. Most peanut farms sell a crop they own, including through marketing contracts, rather than deliver an outsourced service. Aging U.S. producers create succession activity, but family transfers, land leases, asset-only sales, and nonassignable buyer relationships reduce the share that becomes a transferable control transaction.

## Demand durability
Peanut consumption has a stable anchor in peanut butter, and longer-run production expanded, but the latest outlook shows flat total use alongside weaker food and export use and rising stocks. Physical cultivation should still require an accountable operator, although processors can alter the mix between independent contracted farms, ordinary procurement, and vertical integration.

## Risks and uncertainty
The eligible production-service population is not directly counted, the frozen LMM firm count and labor share are missing, and the best contract and owner-age evidence comes from broader populations. A bad outcome is that virtually all apparent candidates are commodity sellers, family farms, or asset-heavy land operations rather than recurring service businesses, while concentrated buyers reclaim most efficiency gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.09 | 0.17 | 0.28 | PROXY | S1, S2, S3 |
| rho | 0.27 | 0.47 | 0.67 | ESTIMATE | S2, S3 |
| e | 0.01 | 0.05 | 0.12 | PROXY | S0, S4 |
| s5 | 0.07 | 0.16 | 0.27 | PROXY | S5 |
| q | 0.22 | 0.38 | 0.56 | PROXY | S4, S6 |
| d5 | 0.93 | 1.02 | 1.12 | PROXY | S7, S8 |
| o | 0.97 | 0.995 | 1 | ESTIMATE | S0, S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 4.40 | 7.60 | 10.00 | PROXY |
| D | 9.02 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No peanut-specific occupational wage mix was found.
- a: The peanut technology evidence is from 2013 and measures precision equipment, not generative AI.
- a: Owner and family labor may not translate into cash wage savings.
- rho: The estimate extrapolates from precision-agriculture adoption to newer AI workflows.
- rho: Capital availability and rural connectivity differ greatly by farm size and region.
- rho: Implementation is measured only against the exposed opportunity in a, not against total farm labor.
- e: No count of peanut production-contract farms was found.
- e: Contract value shares do not equal firm shares.
- e: The frozen dataset provides no defensible LMM firm count for this activity.
- s5: The demographic source is national and covers all farm producers, not principal owners of peanut firms.
- s5: Producer counts include multiple decision makers per farm.
- s5: No observed qualifying-control-transfer rate for the lens population was found.
- q: The concentration evidence concerns marketing contracts and shelling, not directly observed production-service fees.
- q: The key contract form in the eligible population may be extremely rare.
- q: Crop insurance and farm-program payments affect farm economics but are not treated as retention of implemented gross benefit.
- d5: Commodity quantity is not the same as demand for outsourced accountable production.
- d5: Weather, crop rotation, yields, exports, and competing-crop economics can move acreage sharply.
- d5: The low and high cases reflect quantity uncertainty, not commodity price changes.
- o: This is a bounded structural judgment rather than a measured industry share.
- o: Operator requirement does not imply that the current independent firm or ownership structure survives.
- o: Vertical integration could remove outsourced operators even if physical farming remains.

## Sources
- **S0** — [North American Industry Classification System: 111992 Peanut Farming](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-22): Defines 111992 as establishments primarily engaged in growing peanuts, establishing that the code is production-oriented rather than inherently a service industry.
- **S1** — [Farmers, Ranchers, and Other Agricultural Managers](https://www.bls.gov/ooh/management/farmers-ranchers-and-other-agricultural-managers.htm) (accessed 2026-07-22): Lists crop-production supervision, market and disease decisions, purchasing, equipment and facility maintenance, sales, and recordkeeping duties; also describes the physical and seasonal nature of farm work.
- **S2** — [Peanut farms are adopting precision agriculture technologies](https://ers.usda.gov/data-products/charts-of-note/78202) (accessed 2026-07-22): Reports that in 2013, 42 percent of peanut farms used auto-steer or guidance systems, 8 percent used yield monitors, 6 percent yield maps, and 22 percent variable-rate application.
- **S3** — [Precision agriculture use increases with farm size and varies widely by technology](https://ers.usda.gov/data-products/charts-of-note/110550) (accessed 2026-07-22): Reports 2023 guidance/autosteering use of 52 percent among midsize and 70 percent among large-scale crop farms and identifies labor time savings among common adoption reasons.
- **S4** — [Contracts are common in animal and crop production](https://www.ers.usda.gov/data-products/charts-of-note/103803) (accessed 2026-07-22): Distinguishes marketing contracts, where farmers retain commodity ownership, from production contracts, where the contractor owns the commodity, and reports that more than half of peanut production value was under marketing contracts in 2020.
- **S5** — [2022 Census of Agriculture: Farm Producers](https://www.nass.usda.gov/Publications/Highlights/2024/Census22_HL_FarmProducers_FINAL.pdf) (accessed 2026-07-22): Reports an average U.S. farm-producer age of 58.1 in 2022 and that 38 percent of producers were age 65 or older.
- **S6** — [Thinning Markets in U.S. Agriculture](https://ers.usda.gov/sites/default/files/_laserfiche/publications/44034/56926_eib148.pdf?v=51919) (accessed 2026-07-22): Reports that two processors accounted for about 70 percent of U.S. peanut shelling, that shellers offer fixed-price grower contracts, and that after signing a producer has one processor buyer.
- **S7** — [Peanut butter consumption up 6 percent from the 10-year average](https://ers.usda.gov/data-products/charts-of-note/114009) (accessed 2026-07-22): Reports peanut butter at more than 60 percent of U.S. peanut food use, consumption 6 percent above the preceding ten-year average, and 2024/25 production 25 percent above 2014/15.
- **S8** — [Oil Crops Outlook: February 2026](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/113803/OCS-26b.pdf?v=35461) (accessed 2026-07-22): Forecasts 2025/26 U.S. peanut production at 7.2 billion pounds, total use nearly unchanged, food use down 1.6 percent, exports at 1.3 billion pounds, and ending stocks at 2.3 billion pounds.
