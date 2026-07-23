# 111930 — Sugarcane Farming

*v5.1 Stage 1 research memo. Run `111930-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Scarce suitable acreage near mills, specialized operating knowledge, and a protected domestic sugar market create durable physical production value.
**Weakness:** The business produces a physical commodity rather than recurring outsourced services and depends heavily on local mill access and agricultural policy.

## Business-model lens
- Included: Lower-middle-market farms primarily growing sugarcane for third-party mills or processors, including owner-operated and tenant-operated acreage and any genuinely contracted cultivation or crop-management services at the firm level.
- Excluded: Sugar refining, standalone mills, sugar-beet farming, mixed farms not classified to sugarcane, passive farmland ownership, hobby operations, and captive plantations without meaningful third-party recurring revenue.
- Customer and revenue model: Revenue is mainly seasonal sale of harvested cane under processor or mill arrangements, with value linked to tonnage and sugar recovery; contract farming or management can occur but is not the standard industry output.
- Deviation from default lens: none

## Executive view
Sugarcane farming has a useful precision-agriculture surface and policy-supported domestic demand, but it is a poor recurring outsourced-service rollup target because revenue is crop sales. Missing frozen labor-share and firm-count inputs, geographic concentration, and mill dependence further constrain an acquisition thesis.

## How AI changes the work
AI can improve field mapping, agronomic recommendations, yield forecasts, harvest scheduling, billet-quality inspection, records, and maintenance triage. The crop still requires substantial physical cultivation, harvesting, hauling, equipment care, and coordination with mills.

## Value capture
Value can arise from better yield and sugar recovery, reduced input waste, longer ratoon life, tighter harvest timing, and lower administrative effort. Mills, landlords, policy allocations, and commodity pricing influence how much of that value the farm retains.

## Firm availability
Control opportunities are constrained by thin farmland markets, family transfers, highly localized suitable acreage, processor catchments, and long-lived operating relationships. The lens-eligible service subset is smaller than the already uncertain firm population.

## Demand durability
Domestic food use and sugar policy support steady demand, and recent USDA data indicate strong deliveries and cane output. Weather, disease, processing capacity, substitute sweeteners, imports, and future policy can materially alter farm economics.

## Risks and uncertainty
Major uncertainties are missing l and n, limited task-level adoption evidence, thin transaction data, grower-mill bargaining, extreme-weather exposure, policy dependence, and whether research technologies scale economically.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.1 | 0.2 | 0.32 | PROXY | S2, S3 |
| rho | 0.38 | 0.58 | 0.72 | ESTIMATE | — |
| e | 0.01 | 0.03 | 0.07 | ESTIMATE | S1 |
| s5 | 0.03 | 0.08 | 0.16 | PROXY | S4, S5 |
| q | 0.35 | 0.55 | 0.72 | ESTIMATE | S6, S7 |
| d5 | 0.92 | 1.03 | 1.15 | PROXY | S6, S8 |
| o | 0.97 | 0.995 | 0.999 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.92 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Research capabilities do not establish broad commercial adoption.
- a: Perennial ratoon management and regional production systems create nonstandard exceptions.
- rho: No representative autonomous-task completion study for U.S. sugarcane farms was located.
- rho: AI performance will depend on data density and integration with machinery and mills.
- e: Recurring deliveries to one mill remain product sales rather than an outsourced service.
- e: Custom agricultural services may be classified outside sugarcane farming.
- s5: The transfer evidence is national, all-farmland, acreage-based, and older.
- s5: Sugarcane operations can change control without a farmland sale.
- q: Policy support is sector-wide rather than unique to an individual farm.
- q: Dependence on a nearby mill can be both a barrier to entry and a customer-concentration risk.
- d5: Downstream sugar deliveries do not map one-for-one to domestic sugarcane volume.
- d5: The current outlook is a one-year forecast rather than a five-year projection.
- o: Field tasks may be contracted without removing the accountable farming enterprise.

## Sources
- **S1** — [North American Industry Classification System: 111930 Sugarcane Farming](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-22): Defines the industry as establishments primarily engaged in growing sugarcane.
- **S2** — [The Role of Precision Agriculture in Sugarcane Production](https://www.ars.usda.gov/oc/utm/the-role-of-precision-agriculture-in-sugarcane-production/) (accessed 2026-07-22): Sugarcane production cycle, ratoon and nutrient complexity, harvest timing, and USDA precision-agriculture research.
- **S3** — [Robotics for Sugarcane Cultivation: Analysis of Billet Quality Using Computer Vision](https://www.ars.usda.gov/research/publications/publication/?seqNo115=353173) (accessed 2026-07-22): Sugarcane-specific application of computer vision to classify harvested billet damage as an early robotics capability.
- **S4** — [Land Acquisition and Transfer in U.S. Agriculture](https://www.ers.usda.gov/amber-waves/2016/august/land-acquisition-and-transfer-in-u-s-agriculture) (accessed 2026-07-22): Five-year farmland transfer mechanisms and the estimate that 2.3% of farmland would be sold to nonrelatives.
- **S5** — [Farmland Ownership and Tenure](https://www.ers.usda.gov/topics/farm-economy/land-use-land-value-tenure/farmland-ownership-and-tenure) (accessed 2026-07-22): Current national tenure and succession context, including operator ownership and advanced farmer age.
- **S6** — [Sugar and Sweeteners: Background](https://www.ers.usda.gov/topics/crops/sugar-and-sweeteners/background) (accessed 2026-07-22): Domestic cane share, long-run U.S. sugar production growth, technology and variety adoption, acreage expansion, and farm-count decline.
- **S7** — [Sugar and Sweeteners: Policy](https://www.ers.usda.gov/topics/crops/sugar-and-sweeteners/policy) (accessed 2026-07-22): Domestic marketing allotments, tariff-rate quotas, price support, and state and processor allocation mechanics for cane sugar.
- **S8** — [Sugar and Sweeteners Market Outlook, July 2026](https://www.ers.usda.gov/topics/crops/sugar-and-sweeteners/market-outlook) (accessed 2026-07-22): 2026/27 U.S. sugar supply, cane production, human-consumption deliveries, imports, ending stocks, and stocks-to-use forecast.
