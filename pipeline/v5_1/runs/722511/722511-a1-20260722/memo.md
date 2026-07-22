# 722511 — Full-Service Restaurants

*v5.1 Stage 1 research memo. Run `722511-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.74 · L 0.96 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A very large labor base contains repeatable administrative and transaction workflows that connected AI and restaurant software can streamline.
**Weakness:** Core production and hospitality are physical, while easy technology diffuses quickly through a fiercely competitive, low-margin market.

## Business-model lens
- Included: U.S. operating full-service restaurant firms in the roughly $1-10M normalized EBITDA band that provide repeat, seated food-and-beverage service to external guests, including independent and franchised operators when control of the operating company is transferable.
- Excluded: Firms outside the EBITDA band, non-operating shells, captive internal dining units, passive non-control interests, and establishments whose primary model belongs in limited-service restaurants, bars, catering, institutional food service, or another NAICS industry.
- Customer and revenue model: Consumers pay posted menu prices per visit for prepared food, beverages, table service, and the dining experience; repeat use is frequent but generally non-contractual, with some additional delivery, takeout, events, and loyalty-program revenue.
- Deviation from default lens: none

## Executive view
Full-service restaurants combine a large labor bill with many repeat consumer transactions, but most labor sits in physical cooking, carrying, cleaning, and live hospitality. The credible AI opportunity is therefore a bounded layer of administrative, analytical, ordering, payment, reservation, scheduling, recruiting, and service-support work rather than wholesale labor replacement. Demand is expected to grow modestly, while intense local competition and fragile margins constrain durable capture.

## How AI changes the work
AI can forecast traffic and labor needs, draft schedules and marketing, answer routine inquiries, optimize menus and inventory, screen applicants, summarize operating data, and support ordering and payment. Connected restaurant systems are already moving into these workflows. Kitchen production, sensory judgment, food safety, service recovery, and the social experience remain difficult to substitute; adoption evidence also shows augmentation far more often than permanent job removal.

## Value capture
Savings arrive first as restaurant-level margin because guests pay menu prices rather than reimbursing costs. Over five years, competitors can adopt the same tools and customers can respond to price and service differences on every visit, forcing some benefit into value offers, better service, wages, or lower menu-price growth. Differentiated concepts can retain more than commodity, price-sensitive restaurants.

## Firm availability
Operating firms in the target EBITDA band usually satisfy the repeat external-customer lens, but transferability is reduced by chef or owner dependence, weak records, lease and franchise consents, and location-specific goodwill. Sector ownership is demonstrably purchased as well as founded, and restaurant sales are frequent in the small-business marketplace, but public evidence does not isolate qualifying LMM control transfers.

## Demand durability
BLS projects exact-industry real output to grow 2.0% annually from 2024 to 2034, implying about 10% growth over five years if that path holds. The service remains operator-required because meals, safety, premises, licensing, and hospitality are physical accountabilities. The principal demand risks are recession sensitivity, consumer budget pressure, and substitution toward grocery, limited-service, delivery, or self-service occasions.

## Risks and uncertainty
The largest uncertainties are the absence of a measured wage-weighted task-exposure study, the gap between stated technology use and verified labor hours avoided, and the lack of a clean transfer-rate denominator for $1-10M EBITDA full-service firms. Restaurant margins, traffic, cuisine mix, alcohol exposure, local wage rules, leases, and brand strength vary widely. Technology can also degrade hospitality or shift work rather than remove it.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3562 | — | OBSERVED | — |
| n | — | 3131 | — | ESTIMATE | — |
| a | 0.1 | 0.15 | 0.22 | PROXY | S1, S2, S3, S5 |
| rho | 0.25 | 0.45 | 0.65 | PROXY | S4, S5, S3 |
| e | 0.6 | 0.8 | 0.92 | ESTIMATE | — |
| s5 | 0.12 | 0.24 | 0.38 | PROXY | S6, S7, S8 |
| q | 0.35 | 0.55 | 0.75 | ESTIMATE | S9 |
| d5 | 0.96 | 1.1 | 1.2 | PROXY | S9, S10 |
| o | 0.92 | 0.97 | 0.99 | PROXY | S3, S4, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.36 | 0.96 | 2.04 | PROXY |
| F | 8.72 | 10.00 | 10.00 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.83 | 10.00 | 10.00 | PROXY |

## Caveats
- a: The latest reachable static six-digit OEWS table is May 2023 and excludes self-employed workers.
- a: Occupation-level task descriptions do not reveal time shares or which tasks are already automated.
- a: Tips and owner labor are imperfectly represented by OEWS wage measures, affecting wage weights.
- rho: National Restaurant Association surveys mix firm sizes and may overrepresent operators engaged with the trade group.
- rho: Reported use of AI does not establish depth, persistence, or labor substitution.
- rho: The five-year technology frontier is unusually uncertain.
- e: No source directly measures eligibility under this bespoke lens.
- e: The frozen count is margin-bridged from receipts and may include firms whose true normalized EBITDA lies outside the band.
- e: Eligibility can vary sharply between scalable multi-unit concepts and chef-led single-location businesses.
- s5: The evidence does not provide a clean LMM full-service-firm denominator.
- s5: Stated plans to sell have no specified timing and may never produce a transaction.
- s5: Restaurant marketplace transactions disproportionately represent small owner-operated businesses and asset sales.
- q: No public study isolates the pass-through of AI-derived labor savings in full-service restaurants.
- q: Local competition, cuisine, alcohol mix, and concept differentiation create wide dispersion.
- q: This range excludes volume effects, which belong in demand primitives, and implementation failure, which belongs in rho.
- d5: The BLS forecast starts in 2024 rather than the July 2026 run date and spans ten years rather than five.
- d5: The Restaurant Association outlook covers the broader restaurant industry, not only NAICS 722511.
- d5: Recession exposure and shifts toward grocery, delivery, or limited-service dining widen the downside.
- o: Employment persistence is not the same as operator-required quantity.
- o: Operator survey beliefs may lag technical change and are not five-year realized outcomes.
- o: The estimate treats technology-assisted restaurants as still operator-required, consistent with the primitive definition.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 722511 Full-Service Restaurants](https://www.bls.gov/oes/2023/May/naics5_722511.htm) (accessed 2026-07-22): Exact-industry occupation mix and wages: 5,289,580 jobs; 91.30% in food preparation and serving; waiters 32.12%, restaurant cooks 19.75%, supervisors 5.57%, dishwashers 5.79%, hosts 6.79%, and food-service managers 1.64%.
- **S2** — [O*NET OnLine: Food Service Managers](https://www.onetonline.org/link/summary/11-9051.00) (accessed 2026-07-22): Manager task content including scheduling, payroll and budgets, inventory, purchasing, compliance records, reservations, staffing, complaints, menu analysis, and physical service and quality-control duties.
- **S3** — [BLS Factors Affecting Occupational Utilization, Projected 2024-34](https://www.bls.gov/emp/tables/factors-affecting-occupational-utilization.htm) (accessed 2026-07-22): For NAICS 722511, BLS expects technology-enabled self-service ordering and payment to reduce waiter intensity and robots to assist hosts, while other occupational changes reflect substitution and changing service formats.
- **S4** — [National Restaurant Association Restaurant Technology Landscape Report 2024](https://go.restaurant.org/rs/078-ZLA-461/images/NatRestAssoc_TechLandscapeReport_2024.pdf) (accessed 2026-07-22): Full-service investment intentions: 52% back office, 53% inventory, 41% contactless ordering/payment, 36% labor management, 20% self-order/pay, 15% AI integration, and 7% robotics; 68% expected technology to augment rather than replace labor.
- **S5** — [National Restaurant Association Research Insight: Hiring and Staffing Report 2026](https://go.restaurant.org/rs/078-ZLA-461/images/2026-Research-Insight_Hiring-and-Staffing.pdf?version=0) (accessed 2026-07-22): Twenty-eight percent of full-service operators reported using AI; among restaurant AI users, cited full-service use cases included marketing 66%, administrative tasks 41%, menu optimization 28%, ordering 23%, scheduling 21%, and reservations 32%; 94% of operators reported no permanent job elimination from recent technology investment.
- **S6** — [SBA Office of Advocacy Small Business Facts: Paths to Business Ownership](https://advocacy.sba.gov/wp-content/uploads/2021/03/Paths-to-Business-Ownership-fact-sheet.pdf) (accessed 2026-07-22): Accommodation and food-services owners were more likely to have purchased their firms at 38%; 64.5% of current owners across businesses reported plans to sell, without a specified timing horizon.
- **S7** — [BizBuySell Guide to Selling a Restaurant Business](https://www.bizbuysell.com/learning-center/guide/sell-restaurant/) (accessed 2026-07-22): BizBuySell reports 2,516 restaurant sales in 2025, a median 181 days on market, and a $215,000 median sale price, demonstrating active but predominantly small-business transaction flow.
- **S8** — [BizBuySell Restaurant Business Valuation Multiples and Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/restaurants/) (accessed 2026-07-22): Restaurant businesses sold from 2021 through 2025 had median reported revenue of $718,271, showing the marketplace evidence skews far below the target EBITDA band.
- **S9** — [National Restaurant Association State of the Restaurant Industry 2026 Executive Summary](https://go.restaurant.org/rs/078-ZLA-461/images/SOI-2026-ExecutiveSummary.pdf?version=1) (accessed 2026-07-22): Forecasts 1.3% real restaurant sales growth in 2026; reports 61% of adults view dining out as essential and 42% of operators were not profitable in 2025; notes persistent costs, soft traffic, and technology investment.
- **S10** — [BLS Employment and Output by Industry, 2024-34](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): For NAICS 722511, BLS projects employment from 5.3851 million in 2024 to 5.5177 million in 2034 and real output from $452.7 billion to $550.2 billion chained 2017 dollars, a 2.0% annual output growth rate.
