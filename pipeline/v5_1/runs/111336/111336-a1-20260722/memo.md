# 111336 — Fruit and Tree Nut Combination Farming

*v5.1 Stage 1 research memo. Run `111336-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** High specialty-crop labor dependence and multi-crop planning complexity create credible opportunities in vision, forecasting, targeted inputs, scheduling, and administration.
**Weakness:** Farm availability is unmeasured, physical work is difficult to automate across heterogeneous crops, and much of a transition's value may reside in land rather than a transferable operating company.

## Business-model lens
- Included: US lower-middle-market farm operators that grow a combination of fruits and tree nuts, with no one fruit family or tree-nut family accounting for half of agricultural production value, and repeatedly supply external packers, processors, cooperatives, wholesalers, retailers, foodservice buyers, or consumers while retaining accountable responsibility for land, crops, labor, compliance, and delivery.
- Excluded: Shells, captive internal units, non-control financing vehicles, passive farmland lessors, hobby or subsistence farms, custom farm-labor and harvesting contractors, packing or processing businesses without qualifying crop production, farms outside the screened EBITDA band, and operations whose production concentration places them in another fruit or tree-nut NAICS industry are excluded.
- Customer and revenue model: Revenue comes from repeated seasonal crop sales through spot markets, cooperatives, marketing contracts, processors, packing houses, wholesale channels, retailers, foodservice buyers, and direct-to-consumer outlets. Price depends on crop, grade, timing, yield, contract terms, storage, certification, and market conditions; diversified farms can sell several crops across different harvest windows.
- Deviation from default lens: none

## Executive view
Combination fruit and tree-nut farms have meaningful labor and planning complexity, but the most visible AI opportunities are in scouting, forecasting, targeted inputs, scheduling, records, and marketing rather than wholesale replacement of field work. Mixed crops can diversify harvest and market exposure while making technology integration harder. The missing firm-count input is a central diligence gap, and operating-company transferability must be separated from land and family ownership.

## How AI changes the work
Computer vision and predictive tools can improve yield estimates, pest detection, spray targeting, irrigation advice, labor planning, compliance records, and market decisions. Commercial intelligent spraying demonstrates practical sensor-guided adoption, while robotic harvesting remains crop- and orchard-specific. Human work persists in pruning, selective handling, repairs, quality control, food safety, and exception response across variable field conditions.

## Value capture
Transparent commodity and wholesale prices, buyer leverage, cooperatives, import competition, and seasonal oversupply limit retention. Fixed contracts, differentiated grades, organic or local positioning, direct sales, storage, and scarce varieties can protect it. Farm-level diligence must distinguish labor savings from yield gains because extra market supply can lower price.

## Firm availability
Most commercial farms sell repeatedly to external buyers, but exact lower-middle-market availability is unknown and must not be inferred from the broad farm census. Producer age creates succession potential, yet family ownership and separated land structures mean that many transitions will be internal, parcel-based, or lease-based rather than acquisitions of transferable operating companies.

## Demand durability
Fruit and nuts have durable food and ingredient uses, and broader acreage expanded in the last census interval. Combination production provides some crop diversification, but imports, weather, water, disease, long orchard replacement cycles, and crop-specific oversupply can move real domestic output sharply. Revenue-share classification can change after a single crop's price or yield shock.

## Risks and uncertainty
The largest uncertainties are the absent firm count, exact occupation mix, crop basket, land and operating-company structure, transfer mechanism, technology readiness by crop, and constant-price demand. Water availability, wildfire, frost, heat, hurricanes, pests, food-safety incidents, labor access, H-2A compliance, buyer concentration, cooperative terms, imports, crop insurance gaps, and orchard age can dominate administrative productivity gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.18 | 0.32 | 0.47 | PROXY | S3, S4, S5, S6, S7 |
| rho | 0.25 | 0.43 | 0.62 | PROXY | S2, S4, S5, S6, S7 |
| e | 0.7 | 0.84 | 0.93 | ESTIMATE | S1, S2 |
| s5 | 0.18 | 0.3 | 0.43 | PROXY | S2 |
| q | 0.23 | 0.4 | 0.58 | PROXY | S7, S8 |
| d5 | 0.92 | 1.02 | 1.14 | PROXY | S2, S7, S9 |
| o | 0.91 | 0.97 | 0.995 | ESTIMATE | S1, S3, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 4.60 | 8.00 | 10.00 | PROXY |
| D | 8.37 | 9.89 | 10.00 | ESTIMATE |

## Caveats
- a: No exact NAICS 111336 occupation or task distribution was found, and the provided labor-share input is missing.
- a: Mechanization and AI are related but not identical; equipment productivity is relevant only where it substitutes current work or avoids hiring.
- a: Task exposure varies sharply by fruit softness, tree architecture, terrain, fresh-versus-processing destination, and existing mechanization.
- rho: USDA technology evidence spans research projects, demonstrations, and broad precision tools with different commercial readiness.
- rho: Farm internet access does not establish usable field connectivity, integrated data, or implementation capability.
- rho: Weather and crop variability can make results from one orchard system fail to transfer to another.
- e: The code is defined by a moving crop-revenue mix, so a farm can change classification after price or yield shifts without changing its underlying assets.
- e: The provided lower-middle-market firm count is missing and must not be inferred from broad farm counts.
- e: Family farms may separate land, equipment, labor, packing, and crop sales across related legal entities.
- s5: The source covers specialized fruit, tree-nut, and berry farms, not the exact combination code or EBITDA band.
- s5: Producer counts include up to four people per farm, so producer age is not a farm-level transfer probability.
- s5: A land sale, lease, or family succession may not transfer a standalone operating company with customers and workforce.
- q: No public evidence directly measures pass-through of AI-enabled farm labor savings.
- q: Commercial structure differs by crop, market window, processing destination, cooperative membership, certification, and storage life.
- q: Yield gains can reduce market prices and should not be confused with retention of a fixed gross benefit.
- d5: The acreage and sales evidence covers all fruit, tree-nut, and berry production, not combination farms.
- d5: Sales growth is nominal and mixes price, yield, acreage, quality, and commodity composition.
- d5: Permanent crops face large geographic and crop-specific risks that an aggregate range can conceal.
- o: The operator can change while the orchard and quantity persist, especially through leases or management contracts.
- o: Import substitution reduces domestic operator-required quantity and is also reflected in demand durability.
- o: Robotics may centralize management across farms but does not remove accountable land and crop operations.

## Sources
- **S1** — [2022 NAICS Definition: 111336 Fruit and Tree Nut Combination Farming](https://www.census.gov/naics/?details=11133&input=11133&year=2022) (accessed 2026-07-22): Defines the industry as establishments growing a combination of fruits and tree nuts with no fruit family or tree-nut family accounting for half of agricultural production value, and identifies concentration-based cross-references.
- **S2** — [2022 Census of Agriculture Highlights: Fruit, Tree Nut, and Berry Production](https://data.nass.usda.gov/Publications/Highlights/2024/Census22_HL_FruitNutBerry.pdf) (accessed 2026-07-22): Reports broader sector farms, acreage and sales changes, producer age, family-farm share, internet access, hired labor, economic classes, expenses, income, and geographic concentration.
- **S3** — [Farm Labor](https://www.ers.usda.gov/topics/farm-economy/farm-labor) (accessed 2026-07-22): Reports that wages, salaries, and contract labor represented 40 percent of fruit and tree-nut production expenses in the 2022 Census of Agriculture and describes hired farm occupations and labor-force constraints.
- **S4** — [Developing Automation and Mechanization for Specialty Crops](https://ers.usda.gov/publications/95827) (accessed 2026-07-22): Documents high specialty-crop labor dependence and USDA programs supporting automation and mechanization in production, harvesting, and processing.
- **S5** — [Reducing Labor and Advancing Precision Agriculture through Automation](https://www.ars.usda.gov/research/annual-report-on-science-accomplishments/fy-2020/reducing-labor-and-advancing-precision-agriculture-through-automation/) (accessed 2026-07-22): Reports commercial orchard testing and deployment of intelligent spraying, including reductions in drift, ground loss, pesticide use, and chemical cost, demonstrating a practical sensor-guided workflow.
- **S6** — [Precision Agriculture Use Increases With Farm Size and Varies Widely by Technology](https://www.ers.usda.gov/data-products/charts-of-note/110550) (accessed 2026-07-22): Shows that precision-agriculture adoption rises sharply with farm size, reports high use of selected technologies at larger crop farms, and identifies labor saving among adoption motives.
- **S7** — [U.S. Fruit and Vegetable Industries Try To Cope With Rising Labor Costs](https://www.ers.usda.gov/amber-waves/2022/december/u-s-fruit-and-vegetable-industries-try-to-cope-with-rising-labor-costs) (accessed 2026-07-22): Documents labor-intensive orchard tasks, mechanization constraints, rising labor costs, import competition, changes in domestic production, and crop-specific differences in harvest mechanization.
- **S8** — [Specialty Crops Market News](https://www.ams.usda.gov/market-news/fruits-vegetables) (accessed 2026-07-22): Describes frequent public reporting of specialty-crop prices, volumes, quality, condition, shipping-point, wholesale, retail, movement, and import-market information used by buyers and sellers.
- **S9** — [Fruit and Tree Nuts](https://www.ers.usda.gov/topics/crops/fruit-and-tree-nuts) (accessed 2026-07-22): Reports the broader sector's continuing farm cash receipts and identifies USDA time series for acreage, production, prices, trade, stocks, and per-capita use.
