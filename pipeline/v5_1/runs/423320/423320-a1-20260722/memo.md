# 423320 — Brick, Stone, and Related Construction Material Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423320-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.74 · L 0.76 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A high compensation input combines with recurring quote, order, purchasing, pricing, credit, and dispatch workflows around indispensable physical materials.
**Weakness:** Most labor and operational risk remain physical, local, and safety-critical, limiting the share of wages AI can actually remove.

## Business-model lens
- Included: US lower-middle-market merchant wholesalers that repeatedly source, inventory, quote, sell, dispatch, and support stone, cement, lime, sand, gravel, brick, asphalt and concrete mixtures, and concrete, stone, or structural-clay products for external construction customers.
- Excluded: Quarries, mines, manufacturers including ready-mix concrete producers, manufacturers' sales branches, pure brokers and commission agents, consumer-only retailers, captive internal supply units, shells, and operations that cannot transfer independently of the owner.
- Customer and revenue model: Repeat product sales to masonry, concrete, paving, civil, landscape, residential, and commercial contractors and dealers; the wholesaler earns merchandise margin while providing local availability, credit, estimating or product support, load coordination, and jobsite delivery.
- Deviation from default lens: none

## Executive view
Brick, stone, aggregate, and related wholesalers have a smaller information-work share than lighter distributors but a higher labor-to-receipts input and an unusually durable local-operator role. AI can improve commercial and coordination workflows; it cannot remove the yard, load, haul, credit, and jobsite accountability that define the service.

## How AI changes the work
AI can support quantity and product lookup, quote drafting, price guidance, order intake, account prioritization, purchasing, demand alerts, dispatch messages, invoice matching, and service triage. Humans remain central to site and application judgment, negotiation, credit, equipment and yard safety, load construction, routing exceptions, driving, and commitments to contractors.

## Value capture
Own-account resale allows initial retention of workflow savings, while contractor bids and commodity or haul transparency share them over time. Savings are more defensible when converted into reliable stock, faster answers, accurate loads, and on-time delivery rather than simple overhead reduction.

## Firm availability
Repeat contractor relationships and physical operating assets can make these firms transferable, and strategic interest in building-products distribution exists. Owner-held accounts, local permits and real estate, environmental exposure, working capital, fleet condition, and cyclicality narrow the actual acquisition pool.

## Demand durability
Construction is cyclical, but aggregate, cement, asphalt, masonry, and concrete products remain essential to building, repair, roads, bridges, and public works. Housing weakness is offset partly by remodeling and infrastructure work, and the low level of IIJA outlays relative to obligations indicates work can continue after awards.

## Risks and uncertainty
The largest uncertainties are broad labor and adoption proxies, the mixed product basket, estimated target-band count, and no direct pass-through study. Construction cycles, fuel and fleet costs, safety, environmental liabilities, credit losses, project concentration, commodity exposure, and producer-direct sales can overwhelm automation benefit.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1498 | — | OBSERVED | — |
| n | — | 422 | — | ESTIMATE | — |
| a | 0.19 | 0.29 | 0.39 | PROXY | S1, S2 |
| rho | 0.29 | 0.44 | 0.59 | PROXY | S3 |
| e | 0.5 | 0.68 | 0.83 | ESTIMATE | S5 |
| s5 | 0.12 | 0.2 | 0.3 | PROXY | S3, S4 |
| q | 0.44 | 0.61 | 0.77 | ESTIMATE | S3, S5 |
| d5 | 0.92 | 1.06 | 1.2 | ESTIMATE | S6, S7, S8 |
| o | 0.82 | 0.91 | 0.97 | ESTIMATE | S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.76 | 1.38 | PROXY |
| F | 5.26 | 6.54 | 7.50 | ESTIMATE |
| C | 8.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.54 | 9.65 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational mix is a broad durable-goods proxy rather than a six-digit observation.
- a: O*NET task importance does not measure time, wage share, AI feasibility, or current automation.
- a: The injected compensation ratio uses 2024 wages over 2022 receipts and a stated harmonization factor.
- rho: Survey respondents and examples are broader and generally larger than the target population.
- rho: Sales opportunity and management productivity are not equivalent to labor substitution.
- rho: Implementation likely differs sharply between multi-branch systems and locally managed yards.
- e: No public source directly measures default-lens eligibility within the injected 422-firm estimate.
- e: The injected count is inferred from receipts size classes and a sector margin rather than observed EBITDA.
- e: The code mixes masonry products, aggregates, cement-related goods, asphalt, and concrete products with different logistics and repeat-service patterns.
- s5: Plans may not close and can include gifts, minority transactions, or internal succession.
- s5: McKinsey's M&A evidence is dominated by large distribution transactions.
- s5: Real estate, environmental liabilities, permits, cyclicality, and fleet or yard capital can impede transfer.
- q: No direct study measures five-year pass-through of AI-derived savings in this industry.
- q: Fuel, freight, commodity costs, inventory timing, and breakage can obscure the economic effect of labor savings.
- q: This estimate excludes implementation probability and demand-volume effects.
- d5: Employment is an input measure rather than constant-price, constant-quality service-basket demand.
- d5: Infrastructure authorization, obligation, outlay, project construction, and wholesaler sales occur on different schedules.
- d5: Product price inflation, local project cycles, direct quarry or producer sales, and channel share can separate spending from wholesale physical quantity.
- o: Distribution-wide bypass evidence may overstate substitution for heavy local materials.
- o: Operator need is lower for full-truck or full-rail producer-direct movements than for mixed, staged, short-notice local orders.
- o: The estimate separates operator requirement from total construction demand and implementation difficulty.

## Sources
- **S1** — [May 2024 OEWS data tables for industry employment charts](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): For the durable-goods wholesaler group including NAICS 4233, BLS lists 229,190 nontechnical sales representatives, 146,830 hand material movers, 77,370 managers, 62,040 stockers, and substantial driver, customer-service, inventory-clerk, equipment, and office employment.
- **S2** — [O*NET: Sales Representatives, Wholesale and Manufacturing, Except Technical and Scientific Products](https://www.onetonline.org/link/details/41-4012.00) (accessed 2026-07-22): Documents core tasks including answering product and price questions, recommending products, quoting terms and delivery dates, preparing orders, monitoring markets, maintaining records, negotiating, and coordinating delivery.
- **S3** — [AI in distribution: driving digital transformation today](https://www.mckinsey.com/industries/industrials/our-insights/where-value-is-won-and-lost-in-distribution) (accessed 2026-07-22): Reports 90% of distributors with AI initiatives but 11% full adoption and 25% of adopters realizing expected savings; it gives construction-material distributor examples, describes building-products M&A, and reports digital purchasing and supplier-bypass pressure.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Gallup's fall-2024 survey reports that 22% of employer-business owners planned to sell or transfer within five years, with 5% planning closure and 5% reporting no plan.
- **S5** — [NAICS definition: 423320 Brick, Stone, and Related Construction Material Merchant Wholesalers](https://www.census.gov/naics/?details=423&input=423&year=2012) (accessed 2026-07-22): Defines the industry as merchant wholesale distribution of stone, cement, lime, construction sand and gravel, brick, asphalt and concrete mixtures, and concrete, stone, and structural-clay products.
- **S6** — [Employees on nonfarm payrolls by industry detail, April 2025](https://www.bls.gov/ces/data/employment-and-earnings/2025/table1b_202504.htm) (accessed 2026-07-22): The table reports brick, stone, and related construction-material wholesaler employment observations of 67.8, 66.6, 64.4, 64.7 and 65.2 thousand, softer than the earliest displayed observation.
- **S7** — [2026 Housing Outlook: Ongoing Challenges, Cautious Optimism and Incremental Gains](https://www.nahb.org/news-and-economics/press-releases/2026/02/2026-housing-outlook-ongoing-challenges-cautious-optimism-and-incremental-gains) (accessed 2026-07-22): NAHB forecasts single-family starts rising 1% in 2026 and 5% in 2027, multifamily starts falling 5% and 6%, real remodeling growth of 3% and 2%, and remodeling expenditures 19% higher by 2030.
- **S8** — [Infrastructure Investment and Jobs Act funding status as of May 31, 2026](https://www.transportation.gov/mission/budget/infrastructure-investment-and-jobs-act-iija-funding-status) (accessed 2026-07-22): USDOT reports about $545.7 billion of enacted budget authority with adjustments, $392.5 billion obligated and $237.2 billion outlayed as of May 31, 2026, showing substantial funded infrastructure activity still progressing from obligation to expenditure.
