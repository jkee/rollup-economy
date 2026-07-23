# 111333 — Strawberry Farming

*v5.1 Stage 1 research memo. Run `111333-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Severe labor pressure and rich agronomic, harvest-planning, traceability, and administrative workflows create focused AI value around a high-volume crop.
**Weakness:** Repeated delicate hand harvest remains the largest labor block, while the screen lacks both a defensible labor share and LMM firm denominator.

## Business-model lens
- Included: US lower-middle-market farms primarily growing strawberries for recurring external sale to shippers, packers, wholesalers, retailers, processors, foodservice distributors, branded marketers, or direct commercial customers, including farm-level planning, cultivation, harvest, cooling coordination, food-safety records, and sales administration.
- Excluded: Diversified fruit or tree-nut farms not primarily classified as strawberry growers, nurseries, processors and packers without farming, captive internal farms, hobby farms, shells, and non-control land or financing vehicles.
- Customer and revenue model: Seasonal but repeat product revenue from fresh and processing strawberries sold through contracts, marketer or shipper programs, spot channels, cooperatives, and direct accounts, generally priced per flat, tray, pound, or hundredweight with quality, grade, timing, cooling, and rejection risk.
- Deviation from default lens: none

## Executive view
Strawberry farming has useful AI opportunities in scouting, forecasts, irrigation, scheduling, traceability, and administration, but repeated hand harvest dominates labor and remains difficult to mechanize. Consumer demand is durable, while imports, labor, water, perishability, and the absence of defensible labor and firm-count inputs sharply limit confidence.

## How AI changes the work
AI can prioritize disease and pest scouting, forecast yield and harvest timing, optimize irrigation and inputs, schedule crews, automate food-safety and traceability records, and support purchasing and sales. Delicate fruit, dense foliage, uneven ripening, repeated passes, field packing, and rapid cooling preserve substantial physical work.

## Value capture
Yield, grade, timing, water, and reduced waste can produce value, but growers sell into concentrated, transparent, perishable channels and renegotiate frequently. Marketers, retailers, imports, and consumer prices therefore absorb part of observable cost savings.

## Firm availability
Commercial growers generally have repeat external sales, yet the eligible LMM population is unknown. Small and diversified farms, vertical integration, leased land, owner dependency, volatile earnings, and buyer, labor, and water concentration must be screened directly.

## Demand durability
Long-run strawberry demand and recent domestic production are supportive, but imported supply has expanded and can displace domestic growers. Weather, water, disease, labor availability, spoilage, and annual planting decisions make volume materially more volatile than underlying consumer demand.

## Risks and uncertainty
Hand-labor dependence, H-2A and immigration policy, wage inflation, water, fumigants, disease, weather, perishability, buyer rejection, food safety, imports, land tenure, and owner dependence are material. Evidence is weakest because both frozen labor share and LMM firm count are missing.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.11 | 0.19 | 0.29 | PROXY | S1, S2 |
| rho | 0.39 | 0.54 | 0.68 | ESTIMATE | S2 |
| e | 0.32 | 0.5 | 0.67 | ESTIMATE | S1, S3 |
| s5 | 0.17 | 0.28 | 0.41 | PROXY | S5 |
| q | 0.31 | 0.47 | 0.63 | ESTIMATE | S6 |
| d5 | 0.9 | 1 | 1.11 | PROXY | S3, S4 |
| o | 0.985 | 0.996 | 1 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 6.20 | 9.40 | 10.00 | ESTIMATE |
| D | 8.87 | 9.96 | 10.00 | ESTIMATE |

## Caveats
- a: No industry labor-compensation ratio is available in the frozen dataset, so this primitive cannot translate into an evidenced aggregate labor opportunity.
- a: Farm size, region, fresh versus processing mix, and use of labor contractors materially change the wage-weighted task mix.
- rho: No direct five-year adoption survey for strawberry farms was found.
- rho: Prototype harvest mechanization does not establish commercial labor savings across terrain, varieties, and dense foliage.
- e: The frozen dataset provides no defensible LMM firm count, so even a plausible eligible share cannot establish target quantity.
- e: NAICS classifies by primary production and may exclude diversified farms with economically important strawberry acreage.
- s5: National producer age is not an observed strawberry ownership-transfer rate.
- s5: Multiple producers per farm and family entities make owner age difficult to map to control timing.
- q: The 53 percent farm share of retail price is not a savings-retention measure.
- q: Direct, branded, organic, contracted, processing, and open-market channels have different bargaining structures.
- d5: Historical demand and a single-year production increase are not a five-year forecast.
- d5: Total US consumption can grow while domestic farm demand falls because imports gain share.
- o: Imports and controlled-environment substitution affect domestic demand in d5 rather than operator requirement.
- o: Operator responsibility could consolidate into integrated growers or marketers even though farming remains necessary.

## Sources
- **S1** — [NAICS 111333 Strawberry Farming](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-22): Defines the industry as establishments primarily growing strawberries and distinguishes mixed fruit and tree-nut farms where strawberries do not account for half of agricultural production.
- **S2** — [The Changing Landscape of U.S. Strawberry and Blueberry Markets: Production, Trade, and Challenges from 2000 to 2020](https://ers.usda.gov/sites/default/files/_laserfiche/publications/107358/EIB-257.pdf) (accessed 2026-07-22): Reports that fresh strawberries are mostly hand-picked over more than 30 to 50 passes, labor often exceeds half of variable cost, and harvest mechanization is difficult because fruit is delicate, plants must be repicked, and foliage and clustering obstruct machines.
- **S3** — [Noncitrus Fruits and Nuts 2024 Summary](https://www.nass.usda.gov/Publications/Todays_Reports/reports/ncit0525.pdf) (accessed 2026-07-22): Reports 2024 US strawberry utilized production of 32.2 million hundredweight, up 12 percent from 2023, 61,200 harvested acres, and $4.00 billion of crop value, providing recent scale and production context rather than a forecast.
- **S4** — [Global Markets and Trade](https://www.ers.usda.gov/about-ers/plans-and-accomplishments/ers-fy-2023-year-in-review/global-markets-and-trade) (accessed 2026-07-22): States that US strawberry and blueberry demand, domestic production, and imports increased from 2000 to 2020 and that Mexican fresh strawberry imports reached 431 million pounds in 2020, illustrating both demand and import competition.
- **S5** — [USDA releases 2022 Census of Agriculture data](https://www.nass.usda.gov/Newsroom/2024/02-13-2024.php) (accessed 2026-07-22): Reports an average US producer age of 58.1 in 2022, up 0.6 years from 2017, used as a broad succession-pressure proxy rather than strawberry-specific transfer evidence.
- **S6** — [Farmers received about half of what consumers paid for fresh strawberries from 2020–23](https://www.ers.usda.gov/data-products/charts-of-note/109007) (accessed 2026-07-22): Reports a 53 percent farm share of the 2023 fresh-strawberry retail price after adjusting for spoilage and trimming, illustrating the substantial downstream marketing layer but not directly measuring pass-through.
