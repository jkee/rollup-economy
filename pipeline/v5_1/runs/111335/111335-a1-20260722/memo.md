# 111335 — Tree Nut Farming

*v5.1 Stage 1 research memo. Run `111335-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Long-lived bearing orchards and established domestic and export consumption create recurring seasonal crop supply.
**Weakness:** Missing denominator data, commodity price-taking, concentrated export markets, and water and climate exposure make both opportunity size and retained benefit unusually uncertain.

## Business-model lens
- Included: U.S. lower-middle-market commercial farms primarily growing almonds, pistachios, walnuts, pecans, hazelnuts, macadamias, and other tree nuts for repeated sale to external handlers, processors, cooperatives, wholesalers, exporters, retailers, or food manufacturers.
- Excluded: Coconut and coffee farms, mixed fruit-and-nut farms not primarily classified in tree nuts, hobby and subsistence farms, passive landholding vehicles, captive orchards without external revenue, shell ownership entities, processors that do not grow nuts, and non-control financing vehicles.
- Customer and revenue model: Recurring seasonal crop sales under spot, pool, cooperative, handler, processor, export, or contracted arrangements, with yield, grade, variety, and commodity price determining revenue.
- Deviation from default lens: none

## Executive view
Tree-nut farming combines long-lived physical assets, recurring crop sales, family succession pressure, and practical sensing and precision-spray opportunities with commodity pricing, water and climate exposure, export dependence, and missing core firm-count and labor-share data.

## How AI changes the work
AI can improve scouting, irrigation and spray decisions, yield estimation, weather and pest monitoring, work planning, grading support, and administration. Physical orchard care, repair, harvest logistics, and agronomic accountability remain operator-intensive, and major harvest tasks may already be mechanized.

## Value capture
Premium varieties, quality, certifications, genetics, contracts, and water security protect some value, but handlers, global markets, expanding acreage, inventories, and commodity pricing pass much productivity benefit to buyers.

## Firm availability
Commercial orchards often have repeat external revenue, and producer age signals succession pressure. Passive entities, family structures, parcel-level ownership, intra-family transfers, mixed operations, and the absence of a defensible LMM denominator materially weaken availability estimates.

## Demand durability
Acreage and per-capita availability have grown, especially for pistachios, but five-year demand is exposed to exports, stocks, prices, water, heat, pests, trade policy, and long biological production lags.

## Risks and uncertainty
Principal risks are missing labor and firm-count inputs, water rights and drought, heat and wildfire, pests and disease, alternate bearing, export and tariff exposure, commodity price cycles, land and orchard valuation, family ownership complexity, and long replanting cycles.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.12 | 0.24 | 0.37 | PROXY | S2, S3, S4 |
| rho | 0.2 | 0.4 | 0.59 | PROXY | S3, S4 |
| e | 0.48 | 0.7 | 0.84 | ESTIMATE | S1, S2 |
| s5 | 0.17 | 0.32 | 0.47 | PROXY | S2 |
| q | 0.26 | 0.44 | 0.62 | ESTIMATE | S5, S6 |
| d5 | 0.91 | 1.08 | 1.28 | PROXY | S2, S5, S6 |
| o | 0.985 | 0.997 | 1 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 5.20 | 8.80 | 10.00 | ESTIMATE |
| D | 8.96 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No defensible industry compensation-to-receipts input is available, so this task share cannot be combined with an observed labor base.
- a: USDA evidence covers fruit, tree nut, and berry farms or specialty crops broadly and emphasizes selected technologies rather than the complete wage-weighted task mix.
- rho: Research prototypes and successful commercial cases may run ahead of typical LMM adoption.
- rho: Fruit-harvest robots are imperfect analogues because major tree-nut crops already use different harvest mechanization.
- e: The dataset supplies no defensible LMM firm count for agriculture, so the denominator to which this conditional share would apply is missing.
- e: Farm, parcel, operating company, management company, and landholding entity may be different units, making firm eligibility difficult to classify.
- s5: USDA reports fruit, tree nut, and berry farms together rather than eligible LMM tree-nut farms.
- s5: Producer age counts people rather than control owners, and succession or parcel transfer does not necessarily constitute a qualifying operating-company control transfer.
- q: Capture varies substantially across almonds, pistachios, walnuts, pecans, hazelnuts, macadamias, regions, varieties, and marketing channels.
- q: Commodity price cycles and orchard yield changes can swamp the retained effect of labor or input productivity.
- d5: Acreage and availability trends measure supply and consumption for broader or selected products rather than constant-quality demand for the current LMM farm basket.
- d5: Tree crops have long planting lags, alternate-bearing cycles, geographic concentration, and extreme weather sensitivity, making a five-year point ratio unusually uncertain.
- o: This estimates persistence of an accountable operator of the lens's kind, not survival of every current orchard or ownership entity.
- o: Severe water or climate constraints can permanently remove particular orchards even while aggregate nut demand continues.

## Sources
- **S1** — [2022 NAICS Definition: 111335 Tree Nut Farming](https://www.census.gov/naics/?details=111335&input=111335&year=2022) (accessed 2026-07-22): Exact industry scope, illustrative crops, and mixed-farming exclusions.
- **S2** — [2022 Census of Agriculture: Fruit, Tree Nut, and Berry Production Highlights](https://data.nass.usda.gov/Publications/Highlights/2024/Census22_HL_FruitNutBerry.pdf) (accessed 2026-07-22): Acreage trends, farm economics, hired-labor expense, producer age, family ownership, and concentration for specialized fruit, tree nut, and berry farms.
- **S3** — [Automation for Specialty Crops](https://www.nifa.usda.gov/about-nifa/impacts/automation-specialty-crops) (accessed 2026-07-22): USDA-supported automation, sensing, robotic, throughput, labor-saving, and adoption evidence for specialty crops and orchards.
- **S4** — [Reducing Labor and Advancing Precision Agriculture through Automation](https://www.ars.usda.gov/research/annual-report-on-science-accomplishments/fy-2020/reducing-labor-and-advancing-precision-agriculture-through-automation/) (accessed 2026-07-22): Commercial intelligent-sprayer testing, adoption in fruit and nut orchards, and measured input and drift reductions.
- **S5** — [Fruit and Tree Nuts Outlook: March 2026](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/113982/FTS-384.pdf) (accessed 2026-07-22): Current tree-nut production, stocks, consumption availability, and alternate-bearing market context.
- **S6** — [Tree Nuts: World Markets and Trade, October 2024](https://www.fas.usda.gov/sites/default/files/2024-11/TreeNuts.pdf) (accessed 2026-07-22): U.S. export dependence, concentrated destination markets, global competition, and trade-driven pricing context.
