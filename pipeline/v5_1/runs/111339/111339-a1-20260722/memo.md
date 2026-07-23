# 111339 — Other Noncitrus Fruit Farming

*v5.1 Stage 1 research memo. Run `111339-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Labor scarcity and high harvest intensity create real demand for AI-enabled counting, planning, and selective automation.
**Weakness:** Very few growers appear to provide a qualifying outsourced service, and both frozen dataset inputs are missing.

## Business-model lens
- Included: US lower-middle-market growers of peaches, cherries, pears, avocados, bananas, coffee, dates, figs, pineapples, prunes, and other noncitrus fruits that repeatedly provide external customers with contract-growing, customer-specific crop programs, or another substantive outsourced production service.
- Excluded: Farms making only ordinary spot or recurring product sales, apple orchards, vineyards, berry farms, fruit and tree-nut combination farms, protected-culture fruit operations classified elsewhere, processors, distributors, captive farms, shells, and non-control financing vehicles.
- Customer and revenue model: Eligible farms earn repeat B2B revenue through contracted production or customer-specific growing programs for packers, processors, brands, retailers, foodservice buyers, or institutions; fruit delivery remains the output, but the relationship must include substantive outsourced production responsibility rather than simple repeat sales.
- Deviation from default lens: none

## Executive view
AI and robotics can address labor-intensive orchard tasks, but the code is fundamentally agricultural production rather than outsourced service. The investable lens is limited to substantive contract-growing or customer-specific crop programs, not farms that merely sell fruit repeatedly.

## How AI changes the work
The strongest applications are yield estimation, crop counting, disease and vigor imaging, thinning decisions, spray targeting, irrigation support, labor and harvest planning, quality grading, and selective robotic picking. Field variability, fruit damage, weather, and orchard architecture keep humans central.

## Value capture
Fixed contracts can preserve early labor and input savings, while powerful packers, processors, and retailers can demand lower prices or tighter grades at renewal. Scarce varieties, consistent quality, traceability, and reliable delivery improve retention.

## Firm availability
Most farms fail the service test because ordinary crop sales are product revenue. Eligible targets require documented outsourced production duties, and the missing dataset firm count prevents any defensible statement about target abundance.

## Demand durability
Food consumption is durable, but domestic grower demand is exposed to weather, water, pests, labor shortages, bearing cycles, trade, imports, and customer sourcing changes. Physical production remains operator-required even as the supplying geography changes.

## Risks and uncertainty
The principal uncertainties are lens eligibility, missing labor and firm-count inputs, crop heterogeneity, climate and water risk, seasonal labor, immigration policy, perishability, customer concentration, grade rejection, and whether orchard robotics becomes commercially reliable within five years.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.31 | 0.47 | PROXY | S2, S3 |
| rho | 0.24 | 0.43 | 0.62 | PROXY | S2, S3 |
| e | 0.02 | 0.08 | 0.17 | ESTIMATE | S1, S4 |
| s5 | 0.12 | 0.27 | 0.44 | PROXY | S4 |
| q | 0.24 | 0.43 | 0.63 | ESTIMATE | S2, S5 |
| d5 | 0.9 | 1.01 | 1.13 | PROXY | S1, S5, S6 |
| o | 0.93 | 0.98 | 1 | ESTIMATE | S1, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 4.80 | 8.60 | 10.00 | ESTIMATE |
| D | 8.37 | 9.90 | 10.00 | ESTIMATE |

## Caveats
- a: The direct robotic field evidence is from apples, which are outside this six-digit code.
- a: The frozen labor-share input is missing, so this task-exposure estimate cannot repair the dataset gap.
- rho: Pilot accuracy and field success do not establish economic implementation at scale.
- rho: Perennial orchard redesign can extend beyond the five-year horizon.
- e: No source measures the prevalence of substantive contract-growing relationships in the exact code.
- e: The frozen LMM firm count is missing and must not be inferred from the broader agriculture census.
- s5: The proxy covers fruit, tree nuts, and berries rather than this code alone.
- s5: Older producer age does not measure a completed or likely control transfer.
- q: No public source directly measures pass-through of automation savings in contract fruit growing.
- q: Weather-driven price volatility can obscure benefit retention.
- d5: The industry combines crops with very different geographies and biological risks.
- d5: Import growth can satisfy US consumption without supporting US grower-service demand.
- o: Imports preserve fruit consumption while displacing the US lens operator.
- o: Software cannot grow fruit, but it can enable a buyer to coordinate farms directly and disintermediate a service-qualified operator.

## Sources
- **S1** — [NAICS 111339 Other Noncitrus Fruit Farming](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-22): Official industry boundary and crop examples, including peaches, cherries, pears, bananas, coffee, dates, figs, pineapples, and prunes.
- **S2** — [Artificial Intelligence for Yield Estimations at Fruit Orchards](https://www.nal.usda.gov/research-tools/food-safety-research-projects/artificial-intelligence-yield-estimations-fruit) (accessed 2026-07-22): AI-enabled crop counting, fruit measurement, vigor analysis, thinning, labor planning, logistics, and reported pilots with applicability beyond apples.
- **S3** — [Automated Apple Harvesting Robot Field Evaluation](https://www.ars.usda.gov/research/publications/publication/?seqNo115=403763) (accessed 2026-07-22): Peer-reviewed USDA summary of labor pressure, computer-vision harvesting, field performance, orchard-architecture sensitivity, and remaining commercialization work.
- **S4** — [2022 Census of Agriculture Fruit, Tree Nut, and Berry Production Snapshot](https://data.nass.usda.gov/Publications/Highlights/2024/Census22_HL_FruitNutBerry.pdf) (accessed 2026-07-22): Producer age, family ownership, hired-labor intensity, farm economics, internet access, and the broader specialized-fruit farm population.
- **S5** — [Fruit and Tree Nuts Outlook: March 2026](https://www.ers.usda.gov/media/20866/fts-384.pdf?v=55721) (accessed 2026-07-22): Current USDA evidence on supply, production, consumption proxies, prices, imports, weather effects, and trade across fruit markets.
- **S6** — [USDA ERS Fruit and Tree Nuts Overview](https://www.ers.usda.gov/topics/crops/fruit-and-tree-nuts) (accessed 2026-07-22): Sector-level context on US fruit and tree-nut cash receipts and USDA data coverage for production, prices, trade, and demand.
