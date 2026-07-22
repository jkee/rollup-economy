# 722513 — Limited-Service Restaurants

*v5.1 Stage 1 research memo. Run `722513-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.93 · L 1.91 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat transaction volume and standardized ordering, scheduling, inventory, and administrative workflows create implementable labor and waste-reduction opportunities without removing the restaurant operator.
**Weakness:** Most labor is physical and site-specific, while the LMM transfer denominator and the share of savings retained under intense local price competition are only indirectly evidenced.

## Business-model lens
- Included: US limited-service restaurant operating firms in the roughly $1-10M normalized EBITDA band that repeatedly prepare and sell meals for immediate consumption, takeout, or restaurant-provided delivery, including independent and franchisee-owned multiunit operators.
- Excluded: Shells, captive internal food operations, non-control financing vehicles, franchisor-only entities without restaurant operations, independent order-and-delivery services classified outside 722513, and locations or concepts lacking a transferable going-concern operation.
- Customer and revenue model: High-frequency transactional sales to consumers who generally order or select items and pay before eating; revenue is primarily fixed menu pricing, with on-premises, takeout, drive-through, digital-order, and delivery channels and possible franchise royalties paid by operators.
- Deviation from default lens: none

## Executive view
Limited-service restaurants combine a large, repeat-purchase operating base with standardized workflows, but only a minority of wage-weighted work is readily exposed because cooking, cleaning, food safety, and exception handling remain physical and local. The most credible five-year opportunity is coordinated automation of ordering, payment, scheduling, inventory, marketing, and back-office work, with selective standardized-kitchen assistance. Commercial benefits can be retained initially under posted menu pricing, though visible competition, promotions, and franchise economics should share a substantial portion with customers and counterparties.

## How AI changes the work
AI changes front-counter and drive-through ordering, demand and labor forecasting, schedule creation, inventory and waste control, local marketing, training, and administrative reconciliation. Kiosks and apps can remove transactions from cashiers, while voice systems can handle routine drive-through orders. The harder boundary is embodied work: preparing variable food orders, cleaning, verifying sanitation, resolving mistakes, maintaining equipment, and supervising a fast-changing frontline workforce still need people and accountable operating routines.

## Value capture
Restaurant customers buy transaction by transaction at posted prices, so savings are not contractually passed through. Operators can keep benefits through lower labor hours, avoided hiring, reduced waste, better throughput, and fewer errors, but competitors can respond with discounts, value menus, longer hours, or better service. Franchise royalties, required technology vendors, delivery commissions, and reinvestment needs can also absorb part of the gross benefit.

## Firm availability
The segment has many standardized franchise and independent operations, and an active restaurant resale market, but firm-level availability in the specified EBITDA band is not directly measured. Transfer probability is lower than broad owner exit intention because some restaurants close, sell assets only, fail financing or franchisor approval, or depend too heavily on the departing owner. The provided firm count is especially uncertain because it bridges receipts to EBITDA using a public-sector margin that may not represent private operators.

## Demand durability
Food away from home is a large, recurring consumer category, and convenience supports limited-service formats. Federal real-output projections and current industry forecasts indicate modest growth rather than displacement of meal demand. Household budget pressure and food-at-home substitution create downside, but software does not itself prepare and safely fulfill most meals, so an accountable operator remains necessary for most of the current service basket.

## Risks and uncertainty
The weakest evidence concerns LMM firm eligibility, qualifying control-transfer incidence, and post-implementation benefit retention. Surveyed technology intentions may not survive capital constraints, integration problems, customer errors, regulation, or franchise mandates, and evidence from large branded operators can overstate LMM capability. Demand estimates use broader restaurant aggregates, while the occupational mix includes full-service restaurants. A severe consumer downturn, sustained trading-down to groceries, or unexpectedly capable kitchen robotics would materially worsen the outlook.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3309 | — | OBSERVED | — |
| n | — | 4713 | — | ESTIMATE | — |
| a | 0.22 | 0.3 | 0.4 | PROXY | S2, S3, S4 |
| rho | 0.32 | 0.48 | 0.64 | PROXY | S5, S6 |
| e | 0.55 | 0.72 | 0.85 | ESTIMATE | S1, S7 |
| s5 | 0.16 | 0.28 | 0.42 | PROXY | S8, S9 |
| q | 0.35 | 0.52 | 0.68 | ESTIMATE | S1, S12 |
| d5 | 0.98 | 1.09 | 1.18 | PROXY | S10, S11, S12 |
| o | 0.78 | 0.9 | 0.96 | ESTIMATE | S1, S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.93 | 1.91 | 3.39 | PROXY |
| F | 9.70 | 10.00 | 10.00 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.64 | 9.81 | 10.00 | ESTIMATE |

## Caveats
- a: The latest detailed BLS occupation table found is for NAICS 722500 and includes full-service restaurants; it is not a six-digit 722513 staffing pattern.
- a: Occupation employment shares are not task-time shares, and mean wages do not reveal within-occupation wage-weighted exposure.
- a: Kitchen robotics and conventional automation are included only where AI can enable substitution or avoidable hiring; purely mechanical automation is not treated as AI exposure by default.
- a: The injected compensation-to-receipts ratio uses 2024 wages over 2022 receipts and a cross-industry harmonization factor, so the labor pool to which this share is later applied has vintage and basis uncertainty.
- rho: Investment intention is not deployment, sustained use, or labor substitution.
- rho: The National Restaurant Association survey includes restaurant operators outside the LMM firm band, and Deloitte surveyed 375 executives across 11 countries and branded operating groups.
- rho: Food safety, error handling, customer acceptance, franchise technology mandates, fragmented data, and capital constraints can slow implementation.
- rho: The range excludes pricing, demand, and valuation effects.
- e: No source directly measures eligibility among firms in the specified EBITDA band.
- e: Census franchise evidence is from 2012, is establishment-based rather than firm-based, and predates substantial digital-ordering and delivery-channel change.
- e: Franchise affiliation can improve operational transferability but can also require franchisor consent and capital upgrades on transfer.
- e: The injected firm count is an ESTIMATE based on size-class receipts and a 19.47% public Restaurant/Dining EBITDA margin; if private LMM restaurant margins are lower, it may overstate the number actually in the EBITDA band.
- s5: The owner-exit statistics are cross-industry, survey-based, and not specific to the EBITDA band.
- s5: BizBuySell covers only transactions reported on its marketplace and combines restaurant types; its median deal is much smaller than the lens.
- s5: Planned exits can be delayed, become closures, or fail buyer financing and franchisor approval.
- s5: The injected LMM firm denominator is estimated and sensitive to the public-company EBITDA-margin bridge.
- q: No source directly measures five-year retention of AI benefits in limited-service restaurants.
- q: Pricing power varies sharply by brand, geography, daypart, franchise agreement, delivery platform, and local competition.
- q: The estimate excludes demand-volume effects, which belong in demand primitives, and implementation shortfalls, which belong in rho.
- d5: The BLS output projection is for NAICS 722, not 722513, and its 2024-2034 horizon does not exactly match the run-date five-year horizon.
- d5: Real sales and chained-dollar output may not fully remove menu-mix, portion, quality, and channel-fee changes.
- d5: Demand is cyclical and exposed to household income, food-at-home substitution, demographic shifts, and relative menu-price inflation.
- o: This is a bounded judgment rather than a direct measurement.
- o: Software-mediated ordering is not counted as eliminating the operator when the same operator remains responsible for preparing and fulfilling the meal.
- o: Independent third-party delivery is outside NAICS 722513; migration of fulfillment to such firms could reduce the operator-required share only at the delivery edge.
- o: Breakthrough kitchen robotics or autonomous micro-factories could push the share lower than current adoption evidence suggests.

## Sources
- **S1** — [2022 NAICS Definition: 722513 Limited-Service Restaurants](https://www.census.gov/naics/?details=722513&input=722513&year=2022) (accessed 2026-07-22): Defines the industry as food-service establishments where patrons generally order or select items and pay before eating; food may be consumed on premises, taken out, or delivered, while independent order-and-delivery services are classified elsewhere.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Restaurants and Other Eating Places](https://www.bls.gov/oes/2023/may/naics4_722500.htm) (accessed 2026-07-22): Reports 10,870,290 total jobs, 88.97% in food-preparation and serving occupations, including 28.16% fast-food and counter workers, 17.74% cooks, 4.02% food-preparation workers, and 8.34% first-line food-service supervisors.
- **S3** — [O*NET OnLine: Fast Food and Counter Workers](https://www.onetonline.org/link/summary/35-3023.00) (accessed 2026-07-22): Lists the role's mix of order taking, payment, receipt balancing, customer communication, inventory monitoring, food and beverage preparation, packaging, serving, stocking, and cleaning tasks.
- **S4** — [Occupational Outlook Handbook: Cooks](https://www.bls.gov/ooh/food-preparation-and-serving/cooks.htm) (accessed 2026-07-22): Describes cooks' physical preparation and sanitation duties and projects fast-food-cook employment to decline 13% from 2024 to 2034 because of automated systems, combined roles, and operating-streamlining efforts.
- **S5** — [National Restaurant Association Restaurant Technology Landscape Report 2024](https://go.restaurant.org/rs/078-ZLA-461/images/NatRestAssoc_TechLandscapeReport_2024.pdf) (accessed 2026-07-22): For limited-service operators, reports planned resources for AI integration at 17%, self-order/self-pay at 30%, labor management at 37%, inventory systems at 50%, and back-office systems at 51%; 49% expected technology used for labor shortages to become more common, 69% expected augmentation rather than replacement, and 3% planned robotics investment.
- **S6** — [Deloitte: Restaurant AI Investments Heat Up, But Adoption Still Appears to be on the Back Burner](https://www.deloitte.com/us/en/about/press-room/deloitte-how-ai-is-revolutionizing-restaurants.html) (accessed 2026-07-22): A Q4 2024 survey of 375 restaurant executives in 11 countries found 82% planned increased AI investment, while readiness was 43% for strategy, 39% infrastructure, 34% operations, 28% risk and governance, and 27% talent.
- **S7** — [Economic Census Shows Franchising Key to Many Industries](https://www.census.gov/library/stories/2018/03/franchises.html) (accessed 2026-07-22): Reports that 2012 limited-service franchise restaurants were about 54% of establishments, nearly 70% of sales, and about 73% of employment in the segment.
- **S8** — [Project Equity: 20 Key Business Owner Statistics on Exits and Succession](https://project-equity.org/news/employee-ownership-insider/business-owner-statistics-exit-planning/) (accessed 2026-07-22): Compiles owner-transition evidence including 49% planning an exit within five years, 17% preferring external sales, and one-third lacking or being unsure of a long-term plan; the cited underlying surveys are cross-industry.
- **S9** — [BizBuySell: Restaurant Sales Found Their Footing Late in 2025](https://www.bizbuysell.com/learning-center/article/restaurant-industry-analysis/) (accessed 2026-07-22): Reports 2,516 restaurant transactions in 2025 versus 2,653 in 2024, with median revenue of $675,788, median cash flow of $115,252, and median sale price of $215,000.
- **S10** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects food-services-and-drinking-places real output from $994.2 billion in 2024 to $1,230.1 billion in 2034, a 2.2% compound annual growth rate, and employment growth of 3.8%.
- **S11** — [USDA Economic Research Service: Food Service Industry Market Segments](https://ers.usda.gov/topics/food-markets-prices/food-service-industry/market-segments) (accessed 2026-07-22): Reports limited-service restaurant sales of $550.7 billion in 2024, 36.3% of food-away-from-home spending, and describes convenience-led outlet expansion and recurring seasonal demand.
- **S12** — [National Restaurant Association: Restaurant Sales to Hit $1.55T in 2026 Despite Challenging Business Environment](https://www.restaurant.org/education-and-resources/resource-library/report-sales-to-hit-%241-55t-in-2026-despite-challenging-business-environment/) (accessed 2026-07-22): Forecasts 1.3% real restaurant sales growth in 2026 and reports that 42% of operators were unprofitable in 2025 with limited pricing ability, while 61% of consumers considered restaurants essential and value offers affected choice.
