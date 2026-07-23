# 111110 — Soybean Farming

*v5.1 Stage 1 research memo. Run `111110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Large commercial soybean farms already generate field, yield, equipment, and market data that can support implementable AI decision tools.
**Weakness:** Missing labor-share and LMM-count inputs, plus unpaid family labor and asset-level farm transfers, make the economic opportunity difficult to size.

## Business-model lens
- Included: Independent U.S. farm operating businesses repeatedly planting, managing, harvesting, storing, marketing, and selling soybeans to external elevators, processors, exporters, cooperatives, or other buyers, within the specified EBITDA band.
- Excluded: Passive farmland ownership, cash-rent-only entities, hobby and subsistence farms, captive production, grain merchandising without farming, custom crop services classified elsewhere, non-control financing vehicles, and operations without transferable control.
- Customer and revenue model: Recurring seasonal commodity sales by bushel through cash markets, cooperatives, forward or marketing contracts, futures-linked arrangements, and specialty or identity-preserved contracts, with prices shaped by national and global supply, demand, quality, basis, delivery, and storage.
- Deviation from default lens: none

## Executive view
Soybean farming is already highly mechanized, so AI's remaining opportunity is concentrated in agronomic decisions, scouting, equipment utilization, marketing, records, and administration rather than replacing core field execution. The declared gaps in labor share and LMM firm count prevent confident market sizing.

## How AI changes the work
AI can combine weather, imagery, yield, soil, telematics, and price data to support prescriptions, scouting, maintenance, logistics, hedging, insurance, compliance, and bookkeeping. Planting, application, repairs, harvest, grain handling, and accountable agronomy remain.

## Value capture
Commodity buyers generally do not reimburse or audit farm labor costs, so efficiencies can stay with the farm initially. Cash rents, machinery and input prices, basis, and acreage competition absorb durable gains over time.

## Firm availability
Commercial operations may be transferable, but family ownership, personally owned land, nontransferable leases, mixed-crop classification, and asset-level succession complicate eligibility. No defensible frozen LMM count exists for this code.

## Demand durability
USDA baselines support modest production growth from yield and crush demand, but exports, Brazilian competition, trade, weather, and policy create wide uncertainty. Almost all remaining output requires an accountable farm operator.

## Risks and uncertainty
Major risks are weather, commodity and basis volatility, trade, crop disease, input costs, land rents, equipment capital, interest rates, insurance and policy changes, fragmented data, vendor lock-in, rural connectivity, and the absence of reliable labor-share and firm-count inputs.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.13 | 0.23 | 0.34 | PROXY | S2, S3, S4 |
| rho | 0.3 | 0.47 | 0.64 | ESTIMATE | S2, S3 |
| e | 0.34 | 0.55 | 0.72 | ESTIMATE | S1, S5 |
| s5 | 0.17 | 0.31 | 0.47 | PROXY | S5, S6 |
| q | 0.4 | 0.58 | 0.74 | PROXY | S7, S8 |
| d5 | 0.92 | 1.06 | 1.2 | PROXY | S8, S9 |
| o | 0.985 | 0.997 | 1 | ESTIMATE | S1, S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 8.00 | 10.00 | 10.00 | PROXY |
| D | 9.06 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No defensible compensation-to-receipts denominator was provided, and agricultural wage data omit much owner and family labor.
- a: Adoption statistics measure tools and acreage, not labor hours or AI substitution, and larger farms adopt much more rapidly.
- rho: Yield and input improvements are not all labor substitution.
- rho: Farm size, tenancy, equipment age, field variability, and operator skill produce wide implementation differences.
- e: The frozen dataset explicitly provides no defensible LMM firm count, so this conditional share cannot establish target volume.
- e: Farm sales, household income, and accounting profit do not map cleanly to normalized EBITDA.
- s5: Producer age is not owner age or sale intent, and one farm can have several producers.
- s5: Most agricultural transfers are not necessarily arm's-length control acquisitions of an eligible operating firm.
- q: Marketing and pricing evidence covers corn and wheat as well as soybeans.
- q: Weather and commodity-price movements can swamp an efficiency gain even when the gain itself is retained.
- d5: The long-term baseline used here was completed before current 2026 market conditions and is not a forecast.
- d5: Production bushels mix biological yield and acreage and do not isolate eligible LMM farms.
- o: Operations may consolidate or shift to custom farming without eliminating the operator requirement.
- o: Automation can sharply reduce on-farm labor even when an accountable operator remains.

## Sources
- **S1** — [2022 NAICS Definition: Soybean Farming](https://www.census.gov/naics/?details=111110&input=111110&year=2022) (accessed 2026-07-23): Defines establishments primarily engaged in growing soybeans and oilseed combinations in which soybeans predominate.
- **S2** — [Precision Agriculture in the Digital Era: Recent Adoption on U.S. Farms](https://www.ers.usda.gov/publications/105893) (accessed 2026-07-23): Documents adoption of yield and soil mapping, variable-rate technology, and automated guidance, including use on well over half of soybean acreage.
- **S3** — [Largest Farms Most Likely to Adopt Precision Agriculture Guidance Systems](https://www.ers.usda.gov/data-products/charts-of-note/105914) (accessed 2026-07-23): Reports guidance adoption by 68% of the largest soybean farms versus 11% of the smallest in 2018.
- **S4** — [U.S. Soybean Production Expands as Farmers Adopt New Practices and Technologies](https://ers.usda.gov/amber-waves/2023/july/u-s-soybean-production-expands-since-2002-as-farmers-adopt-new-practices-technologies) (accessed 2026-07-23): Describes soybean use of yield monitors, maps, variable-rate application, GPS guidance, and auto-steering for agronomic management.
- **S5** — [2022 Census of Agriculture Farm Producers Demographic Profile](https://data.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/Demographic_Profiles/cpd99000.pdf) (accessed 2026-07-23): Reports average producer age of 58.1, 38% age 65 or older, 95% family farms, land tenure, off-farm work, and broad crop-farm structure.
- **S6** — [USDA Releases 2022 Census of Agriculture Data](https://data.nass.usda.gov/Newsroom/2024/02-13-2024.php) (accessed 2026-07-23): Provides national farm and producer context, including beginning and young producers and the scope of Census of Agriculture data.
- **S7** — [Farm Structure and Contracting](https://www-tx.ers.usda.gov/topics/farm-economy/farm-structure-and-organization/farm-structure-and-contracting) (accessed 2026-07-23): Defines marketing and production contracts and reports that less than 20% of soybean, corn, and wheat production was under marketing contracts.
- **S8** — [Corn and Soybean Farmers Combine Futures, Options, and Marketing Contracts](https://ers.usda.gov/amber-waves/2020/november/corn-and-soybean-farmers-combine-futures-options-and-marketing-contracts-to-manage-financial-risks) (accessed 2026-07-23): Explains commodity price discovery and how soybean farmers use futures, options, and marketing contracts to manage price risk.
- **S9** — [USDA Agricultural Projections to 2033](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/108567/OCE-2024-01.pdf) (accessed 2026-07-23): Projects soybean production rising from 4.520 billion bushels in 2025/26 to 4.780 billion in 2031/32 with flat acreage and rising yield.
