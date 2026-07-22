# 312113 — Ice Manufacturing

*v5.1 Stage 1 research memo. Run `312113-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.17 · L 1.80 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical replenishment with AI-addressable forecasting, routing, order, and administrative workflows.
**Weakness:** Most labor remains tied to physical production and delivery, while large customers can reprice savings through competitive bids.

## Business-model lens
- Included: Lower-middle-market U.S. manufacturers that repeatedly produce and supply packaged ice to external retail, foodservice, airline, event, industrial, or emergency-service customers, including direct-store delivery and co-packing relationships.
- Excluded: Dry-ice manufacturing, ice-vending-machine operators classified outside NAICS 312113, captive ice production for an owner's own premises, shell entities, and firms outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: Recurring product sales coupled with replenishment, route delivery, merchandising, emergency supply, or co-packing; larger customers commonly procure by negotiated bid and value reliable stocking and on-time delivery.
- Deviation from default lens: none

## Executive view
Ice manufacturing is a physical, route-based recurring-supply business. The clearest AI applications sit around orders, forecasting, dispatch, customer support, administrative work, and plant scheduling; the core manufacturing and delivery burden remains physical. Local route density and peak reliability can protect economics, but customer bids, consolidation, seasonality, and capital intensity limit certainty.

## How AI changes the work
AI can consolidate orders from calls, email, EDI, and portals; forecast location-level demand from weather and events; schedule production; optimize replenishment and routes; automate billing and service responses; and flag quality exceptions. These tools reduce coordination labor and avoid seasonal hiring more plausibly than they replace plant operators, maintenance technicians, handlers, or drivers.

## Value capture
Savings can be retained between renewals and through improved stock availability, route density, and reduced waste. Large chains and airlines negotiate prices and solicit bids, so visible cost reductions may be shared over time; local scarcity, reliability, and the absence of practical substitutes can slow pass-through.

## Firm availability
The industry contains hundreds of smaller local producers alongside scaled networks, and major operators use local co-packers. Broad owner aging and ongoing consolidation support some transfer flow, but there is no observed denominator-specific transfer rate for the 36 estimated LMM firms.

## Demand durability
The service basket should remain durable because ice is a physical consumable with recurring retail, foodservice, airline, event, industrial, and emergency uses. Population, restaurant activity, and hotter extremes are supportive, while weather volatility and customer-owned machines constrain growth.

## Risks and uncertainty
The largest uncertainties are the true six-digit occupation mix, current digital maturity, eligibility within the margin-bridged firm count, and five-year transfer incidence. Commercial risk is local: losing a chain bid can impair route density, while extreme peak demand, power and water costs, refrigeration reliability, food safety, and driver availability can absorb expected gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3749 | — | OBSERVED | — |
| n | — | 36 | — | ESTIMATE | — |
| a | 0.11 | 0.24 | 0.34 | PROXY | S2, S3 |
| rho | 0.3 | 0.5 | 0.7 | ESTIMATE | S3, S4 |
| e | 0.7 | 0.85 | 0.95 | ESTIMATE | S1, S4 |
| s5 | 0.1 | 0.18 | 0.3 | ESTIMATE | S4, S5 |
| q | 0.35 | 0.57 | 0.75 | ESTIMATE | S4 |
| d5 | 0.95 | 1.05 | 1.15 | PROXY | S6, S7, S8 |
| o | 0.85 | 0.94 | 0.98 | PROXY | S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.49 | 1.80 | 3.57 | ESTIMATE |
| F | 2.02 | 3.01 | 3.89 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.07 | 9.87 | 10.00 | PROXY |

## Caveats
- a: The occupational mix is a three-digit beverage-and-tobacco proxy, not a six-digit ice estimate.
- a: General GenAI task exposure is not the same as current unautomated substitutable labor.
- a: Seasonal peak staffing and owner labor may be poorly represented in establishment employment data.
- rho: No ice-industry adoption study was found.
- rho: Implementation depends on digital order capture and clean item-location-route data.
- rho: The estimate excludes autonomous trucking and speculative general-purpose robotics.
- e: The 36-firm count is frozen and margin-bridged rather than observed.
- e: Census establishment definitions do not identify recurring revenue or independent ownership.
- e: Some firms may sell a commodity product without a meaningful outsourced-service component.
- s5: The owner-age statistic covers employer businesses across industries and is dated 2018.
- s5: A recent strategic acquisition demonstrates deal activity but does not estimate LMM transfer frequency.
- s5: Family succession, recapitalizations, and asset sales may not qualify as control transfers of transferable operations.
- q: DOJ evidence emphasizes large multi-location customers and specified local markets.
- q: Independent stores and emergency-service buyers may have different bargaining power.
- q: Retention varies sharply with local route density and number of qualified rivals.
- d5: The range is a driver-based proxy rather than an industry shipment forecast.
- d5: Weather creates substantial annual and regional variance.
- d5: Restaurant sales do not isolate ice volume and airline, retail, industrial, and emergency channels differ.
- o: The DOJ finding is market- and customer-specific, not a national quantity share.
- o: Technology adoption could differ materially between large chains and independent locations.
- o: The estimate concerns operator requirement, not incumbent producer retention.

## Sources
- **S1** — [2022 NAICS Definition: 312113 Ice Manufacturing](https://www.census.gov/naics/?details=31211&input=31211&year=2022) (accessed 2026-07-23): Defines the industry as establishments primarily engaged in manufacturing ice and distinguishes dry ice and serviced vending machines.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 312000](https://www.bls.gov/oes/2023/may/naics3_312000.htm) (accessed 2026-07-23): Reports the broader subsector occupation mix, including production at 22.11%, transportation/material moving at 12.33%, office support at 4.87%, and sales at 12.15% of employment.
- **S3** — [Generative AI and Jobs: A Refined Global Index of Occupational Exposure](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) (accessed 2026-07-23): Finds clerical occupations have the highest GenAI exposure and emphasizes job transformation rather than full automation for most occupations.
- **S4** — [Competitive Impact Statement: U.S. v. Reddy Ice, LLC et al.](https://www.justice.gov/atr/media/1427386/dl) (accessed 2026-07-23): Describes packaged-ice producers, co-packers, hundreds of smaller local firms, delivery and service requirements, negotiated pricing and bids, competition, entry barriers, and limited viability of vending or self-supply for most large retail and airline customers.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-23): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 Annual Business Survey covering data year 2018.
- **S6** — [2023 National Population Projections Tables: Main Series](https://www.census.gov/data/tables/2023/demo/popproj/2023-summary-tables.html) (accessed 2026-07-23): Provides the Census Bureau's U.S. population projection series from 2023 to 2100 based on the 2020 Census and 2022 population estimates.
- **S7** — [Restaurants remain resilient despite challenging business conditions](https://restaurant.org/research-and-media/research/restaurant-economic-insights/analysis-commentary/restaurants-remain-resilient-despite-challenging-business-conditions/) (accessed 2026-07-23): Projects 2026 restaurant sales growth of 4.3% nominal and 0.8% inflation-adjusted, while noting uneven traffic.
- **S8** — [Heat wave in Southern California and the Southwest in early September 2024](https://prod-01-asg-www-climate.woc.noaa.gov/news-features/event-tracker/heat-wave-southern-california-and-southwest-early-september-2024) (accessed 2026-07-23): Reports that major-city heat waves rose from about two per year in the 1960s to more than six in the 2020s and that the average heat-wave season is 49 days longer.
