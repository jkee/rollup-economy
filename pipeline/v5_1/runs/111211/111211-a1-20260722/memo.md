# 111211 — Potato Farming

*v5.1 Stage 1 research memo. Run `111211-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Recurring contracted crop supply and data-rich agronomic decisions support bounded workflow automation around a durable food demand base.
**Weakness:** Missing labor and firm-count inputs, existing mechanization, and processor bargaining make the measurable opportunity highly uncertain.

## Business-model lens
- Included: US lower-middle-market farms repeatedly growing ware and/or seed potatoes for external processors, packers, wholesalers, retailers, or other growers, including recurring seasonal delivery under marketing or production arrangements.
- Excluded: Hobby and subsistence farms; land-only lessors; captive processor-owned farms without external customers; pure packing, storage, brokerage, and transportation businesses; farms outside the EBITDA band; shells and non-control financing vehicles.
- Customer and revenue model: Annual crop sales through processor and buyer contracts, cooperatives, negotiated marketing arrangements, or spot channels, with payment based on quantity, grade, variety, delivery timing, and market or formula pricing; seed-potato growers sell recurring certified inputs to farms.
- Deviation from default lens: none

## Executive view
Potato farming is a necessary physical crop business with stable long-run national volume and recurring processor or buyer relationships. AI can improve decisions and paperwork, but much field labor is already mechanized, the labor-share and firm-count inputs are missing, and buyer power constrains retention.

## How AI changes the work
AI can assist crop plans, weather and scouting interpretation, irrigation and nutrient decisions, labor and equipment schedules, traceability, food-safety records, contracts, and accounting. Planting, cultivation, irrigation maintenance, harvest, grading, handling, storage, and repair remain physical and often already mechanized.

## Value capture
A farm can retain savings during a crop cycle and benefit from grade, yield, or storage consistency, but annual marketing contracts, formula pricing, processor concentration, commodity substitution, and oversupply pressure return much of the benefit to buyers.

## Firm availability
Commercial farms commonly have recurring external buyers, but the dataset provides no defensible LMM firm count. Eligibility and transferability require separating operating economics from land value, family labor, diversified crops, and processor-captive arrangements.

## Demand durability
National potato output has been broadly flat over a decade. Falling per-capita availability is partly offset by population, processed forms, and exports, producing a near-flat five-year base with weather, trade, restaurant, and processor-capacity uncertainty.

## Risks and uncertainty
Risks include weather and water availability, disease, input costs, processor concentration, contract acreage cuts, grade rejection, storage loss, trade, restaurant demand, equipment capital, land value, seasonal labor, missing labor and firm-count inputs, and family/asset transfers that are not operating-company deals.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.1 | 0.19 | 0.3 | PROXY | S2, S3 |
| rho | 0.33 | 0.52 | 0.69 | ESTIMATE | S3 |
| e | 0.48 | 0.67 | 0.82 | ESTIMATE | S0, S5 |
| s5 | 0.1 | 0.21 | 0.34 | PROXY | S7, S8 |
| q | 0.24 | 0.4 | 0.57 | PROXY | S4, S6 |
| d5 | 0.87 | 0.98 | 1.1 | PROXY | S1, S9 |
| o | 0.97 | 0.995 | 1 | ESTIMATE | S0, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 4.80 | 8.00 | 10.00 | PROXY |
| D | 8.44 | 9.75 | 10.00 | ESTIMATE |

## Caveats
- a: The frozen labor-share input is missing, so exposure cannot be translated into a measured industry labor opportunity.
- a: The occupation proxy is from crop-support contractors, not farms.
- a: Self-employed owner labor is omitted from OEWS.
- rho: No potato-specific five-year implementation study was found.
- rho: Yield or input improvements are not counted unless they substitute labor or avoid hiring.
- e: The frozen n input is missing and must not be reconstructed, so no eligible-firm count can be inferred from this share.
- e: USDA reports farms and acres, not normalized EBITDA-band firms.
- s5: Producer age is not owner age and multiple producers can be attached to one farm.
- s5: Farm transfer structures frequently do not constitute qualifying control transactions.
- q: Fresh-potato retail share is not a pass-through rate.
- q: Seed, fresh, chip, dehydrated, and frozen-processing channels have different bargaining structures.
- d5: Production is supply as well as demand and is weather-sensitive.
- d5: Per-capita availability includes trade and stocks and is not direct consumption.
- d5: No official five-year potato forecast was found.
- o: Consolidation can reduce the number of independent operators without eliminating farm operation.

## Sources
- **S0** — [2022 NAICS definition: 111211 Potato Farming](https://www.census.gov/naics/?details=111&input=111&year=2022) (accessed 2026-07-23): Defines establishments growing potatoes and/or producing seed potatoes in annual open-field cycles.
- **S1** — [USDA NASS North American Potatoes, February 2026](https://www.nass.usda.gov/Publications/Todays_Reports/reports/uscp0226.pdf) (accessed 2026-07-23): US production history: 412.688 million cwt in 2016 and 412.860 million cwt in 2025, with 2025 harvested area 896,800 acres and yield 460 cwt per acre.
- **S2** — [May 2023 OEWS: Support Activities for Crop Production](https://www.bls.gov/oes/2023/May/naics4_115100.htm) (accessed 2026-07-23): Proxy occupation mix: farming occupations 67.20%, crop/nursery laborers 56.10%, and agricultural equipment operators 4.23%.
- **S3** — [Precision Agriculture in the Digital Era](https://www.ers.usda.gov/publications/105893) (accessed 2026-07-23): USDA documents adoption of yield maps, soil maps, variable-rate technology, guidance, and other digital agricultural technologies through 2019.
- **S4** — [USDA ERS Farm Structure and Contracting](https://www.ers.usda.gov/topics/farm-economy/farm-structure-and-organization/farm-structure-and-contracting) (accessed 2026-07-23): Defines marketing and production contracts and reports 26% of US production value under contract in 2024; crop contracts are more commonly marketing contracts.
- **S5** — [2022 Census of Agriculture: Historical Highlights](https://www.nass.usda.gov/Publications/AgCensus/2022/Full_Report/Volume_1%2C_Chapter_2_US_State_Level/usv1.pdf) (accessed 2026-07-23): Reports 15,099 farms harvested 1,076,285 potato acres in 2022 versus 16,554 farms and 1,133,128 acres in 2017.
- **S6** — [Farmers receive about 15 to 18 percent of retail price for fresh potatoes](https://www.ers.usda.gov/data-products/charts-of-note/104420) (accessed 2026-07-23): USDA reports fresh-potato farm share fluctuated between 15% and 18%; 2021 retail price averaged $0.78/lb and farm price $0.12/lb.
- **S7** — [2022 Census of Agriculture Farm Producers Highlights](https://www.nass.usda.gov/Publications/Highlights/2024/Census22_HL_FarmProducers_FINAL.pdf) (accessed 2026-07-23): Reports average producer age 58.1 and 38% of producers age 65 or older.
- **S8** — [Number of US farms decreased 10 percent from 2012 to 2022](https://www.ers.usda.gov/data-products/charts-of-note/108720) (accessed 2026-07-23): USDA reports US farms declined from 2,109,303 in 2012 to 1,900,487 in 2022.
- **S9** — [From fresh to frozen: Potato per capita availability changes over time](https://ers.usda.gov/data-products/charts-of-note/113195) (accessed 2026-07-23): Average 2022–2024 potato availability was 115 pounds per person, about 20 pounds below the early 2000s; frozen products accounted for about half.
