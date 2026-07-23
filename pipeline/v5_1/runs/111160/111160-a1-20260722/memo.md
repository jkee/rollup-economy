# 111160 — Rice Farming

*v5.1 Stage 1 research memo. Run `111160-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Established rice operations combine scarce suitable land and water with a proven precision-agriculture base that can support incremental AI productivity.
**Weakness:** Rice farming sells a volatile physical commodity rather than a recurring outsourced service, leaving very little lens-eligible revenue.

## Business-model lens
- Included: Lower-middle-market owner-operated, tenant-operated, and sharecropped farms primarily growing rice other than wild rice or producing rice seed, with recurring third-party crop sales and any genuinely contracted cultivation or water-management services identified at the firm level.
- Excluded: Wild-rice farming, mixed grain or oilseed farms not classified to rice, rice milling and distribution, hobby or subsistence operations, passive farmland ownership, and captive production without meaningful third-party revenue.
- Customer and revenue model: Revenue is predominantly seasonal sales of an agricultural commodity or seed to mills, merchandisers, cooperatives, and other buyers; contracted farming or management revenue may occur but is not the typical model.
- Deviation from default lens: none

## Executive view
Rice farming has a credible precision-agriculture and irrigation-automation surface, but it is an exceptionally weak fit for a recurring outsourced-service rollup because the core revenue is commodity crop sales. Missing frozen labor-share and firm-count inputs further limit confidence in scaled acquisition conclusions.

## How AI changes the work
AI can improve planting and input plans, water scheduling, field monitoring, yield forecasting, maintenance triage, records, and marketing decisions. It cannot eliminate the land, water, machinery, biological risk, and physical field execution that dominate the operating model.

## Value capture
Potential value comes from lower water and input use, fewer application overlaps, better yield consistency, faster anomaly response, and reduced administrative effort. Commodity pricing, landlord economics, and technology costs can distribute those gains away from the operator.

## Firm availability
Agricultural land markets are thin and family, trust, lease, and asset-level transfers complicate control acquisition. The number of rice farms that meet LMM economics and the outsourced-service lens is unknown and likely small.

## Demand durability
Rice is a globally important staple and U.S. production serves both domestic and export markets. Five-year operator economics nevertheless remain exposed to acreage, drought, water availability, foreign competition, trade policy, input inflation, and support programs.

## Risks and uncertainty
The principal uncertainties are missing frozen l and n, lack of task-level labor data, prototype-to-commercial automation gaps, thin transaction evidence, water security, regional heterogeneity, and export-market volatility.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.12 | 0.23 | 0.36 | PROXY | S2, S3, S4 |
| rho | 0.4 | 0.6 | 0.75 | ESTIMATE | — |
| e | 0.01 | 0.03 | 0.08 | ESTIMATE | S1 |
| s5 | 0.04 | 0.09 | 0.18 | PROXY | S5, S6 |
| q | 0.25 | 0.45 | 0.65 | ESTIMATE | S3, S7 |
| d5 | 0.88 | 1 | 1.12 | PROXY | S7, S8 |
| o | 0.96 | 0.99 | 0.999 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 5.00 | 9.00 | 10.00 | ESTIMATE |
| D | 8.45 | 9.90 | 10.00 | ESTIMATE |

## Caveats
- a: Technology adoption is measured by acreage or farms, not share of labor time.
- a: Rice systems differ materially between the Mid-South and California.
- rho: No representative autonomous-task completion dataset was located.
- rho: Prototype irrigation systems still report installation, maintenance, and reliability challenges.
- e: Repeat sales to a mill or cooperative are not, by themselves, outsourced services.
- e: Custom-work revenue may be reported outside the core establishment classification.
- s5: The source measures farmland acres rather than rice-farm firms.
- s5: The transfer evidence is older and national across all agricultural land.
- q: Water access and land scarcity differ sharply by region.
- q: Government programs can alter downside protection without creating firm-specific advantage.
- d5: The latest outlook is a one-year forecast rather than a five-year projection.
- d5: Sales-volume exposure to exports increases sensitivity to trade and foreign crop conditions.
- o: Custom operators can perform field tasks, but the accountable farming enterprise remains necessary.

## Sources
- **S1** — [North American Industry Classification System: 111160 Rice Farming](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-22): Defines the industry as establishments growing rice other than wild rice and/or producing rice seed.
- **S2** — [Precision Agriculture in the Digital Era: Recent Adoption on U.S. Farms](https://ers.usda.gov/publications/105893) (accessed 2026-07-22): Rice acreage adoption of automated guidance and the lower adoption range for yield maps, soil maps, and variable-rate technologies.
- **S3** — [Rice Farms Are Adopting Precision Agriculture Technologies](https://ers.usda.gov/data-products/charts-of-note/78088) (accessed 2026-07-22): Rice-farm use of yield monitoring and auto-steer or guidance, plus the mechanisms for reducing input overlap and operator error.
- **S4** — [Life After the Flood: Automated IoT Irrigation Technologies in Rice Production](https://www.nal.usda.gov/research-tools/food-safety-research-projects/life-after-flood-disrupting-rice-farming-integrating-automated-iot-irrigation-technologies-low-water) (accessed 2026-07-22): Rice-specific automated irrigation research targeting lower water use while maintaining or improving yield, seed quality, and returns.
- **S5** — [Land Acquisition and Transfer in U.S. Agriculture](https://www.ers.usda.gov/amber-waves/2016/august/land-acquisition-and-transfer-in-u-s-agriculture) (accessed 2026-07-22): Five-year farmland transfer mechanisms and the estimate that 2.3% of farmland would be sold to nonrelatives in the open market.
- **S6** — [Farmland Ownership and Tenure](https://www.ers.usda.gov/topics/farm-economy/land-use-land-value-tenure/farmland-ownership-and-tenure) (accessed 2026-07-22): Current national tenure context, operator ownership, succession relevance, and the advanced age of many farmers.
- **S7** — [USDA ERS Rice Overview](https://www.ers.usda.gov/topics/crops/rice) (accessed 2026-07-22): Geographic concentration of U.S. rice production and the 40–45% export share of annual U.S.-produced rice sales volume.
- **S8** — [Rice Market Outlook, July 2026](https://www.ers.usda.gov/topics/crops/rice/market-outlook) (accessed 2026-07-22): 2026/27 production, acreage-driven supply reduction, domestic consumption, exports, stocks, and farm-price outlook.
