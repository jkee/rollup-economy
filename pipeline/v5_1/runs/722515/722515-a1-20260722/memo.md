# 722515 — Snack and Nonalcoholic Beverage Bars

*v5.1 Stage 1 research memo. Run `722515-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.16 · L 1.71 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat consumer occasions and digitizable counter-service workflows create a practical path to labor avoidance without requiring the physical service itself to disappear.
**Weakness:** Most labor remains tied to physical preparation, sanitation, stocking, and in-person exception handling, while intense menu-price competition limits long-run retention of savings.

## Business-model lens
- Included: U.S. lower-middle-market employer firms whose primary activity is fixed-location preparation or serving of specialty snacks or nonalcoholic beverages for immediate consumption, including coffee shops, juice bars, ice cream parlors, and on-premise-baking bagel, doughnut, cookie, and pretzel shops.
- Excluded: Mobile food services, street vendors, packaged-food retail without immediate-consumption service, captive internal foodservice units, shells, non-control financing vehicles, firms outside the specified EBITDA band, and operations that cannot continue independently of the seller's personal labor.
- Customer and revenue model: Primarily per-transaction sales to external consumers, with recurring demand expressed through repeat visits, loyalty programs, digital ordering, and local traffic rather than long-term contracts; some firms also sell related packaged goods.
- Deviation from default lens: none

## Executive view
Snack and nonalcoholic beverage bars combine high repeat consumer frequency with a labor model dominated by counter service and physical preparation. The credible AI opportunity is selective: order capture, payment, scheduling, inventory, marketing, training, bookkeeping, and service recovery can reduce hiring needs, while brewing, assembling, cleaning, stocking, and food-safety execution remain operator work. The industry has an active small-business transfer market, but target-sized deals are less directly evidenced than Main Street restaurant sales.

## How AI changes the work
AI can improve digital and voice ordering, menu recommendations, demand forecasting, workforce scheduling, inventory replenishment, local marketing, loyalty personalization, training, bookkeeping, and complaint triage. Its labor effect is constrained because the dominant occupations combine these information tasks with manual production and customer-facing work; implementation should be designed around fewer exceptions and better throughput rather than assuming a largely staffless shop.

## Value capture
Because consumers pay menu prices, there is no contractual clause that automatically returns savings to customers. A capable operator can initially retain benefits through avoided hires, better scheduling, higher throughput, reduced waste, and improved mix. Over time, however, local competition, franchise promotions, delivery commissions, and price-sensitive repeat customers are likely to convert part of those gains into lower effective prices, loyalty offers, or better service.

## Firm availability
Most target-sized employer firms should satisfy the repeat external-service lens, but lease transferability, franchise consent, owner dependence, and normalized earnings require diligence. Employer-owner surveys indicate meaningful five-year transfer intent, and thousands of completed restaurant sales demonstrate transaction infrastructure, yet typical marketplace transactions are much smaller than the specified EBITDA band. The frozen firm count also relies on a broad restaurant margin bridge rather than direct target-band observation.

## Demand durability
Demand is supported by convenience, habitual coffee and snack occasions, beverage innovation, and the social value of going out. Broad restaurant research points to modest real growth even amid tighter budgets. Self-service will alter the front end, but physical preparation, sanitation, location operation, and accountable food-safety oversight make pure-software displacement of the current service basket unlikely within five years.

## Risks and uncertainty
The largest evidence gaps are the absence of a six-digit wage-weighted task study, completed AI labor-removal cohorts for independent operators, target-band transfer data, and channel-specific constant-price traffic forecasts. Broad restaurant proxies may miss differences among coffee, juice, dessert, and bakery concepts. Thin margins and soft traffic can both motivate automation and prevent funding it. The frozen labor ratio has a wage-receipts vintage mismatch and IPS harmonization, while the frozen firm count is an EBITDA-margin-bridged estimate.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3797 | — | OBSERVED | — |
| n | — | 507 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.34 | PROXY | S1, S2, S3 |
| rho | 0.32 | 0.49 | 0.67 | PROXY | S2, S3 |
| e | 0.7 | 0.82 | 0.92 | ESTIMATE | S0, S5 |
| s5 | 0.14 | 0.22 | 0.3 | PROXY | S4, S5 |
| q | 0.42 | 0.59 | 0.76 | ESTIMATE | S3, S7 |
| d5 | 0.94 | 1.07 | 1.15 | PROXY | S6, S7 |
| o | 0.8 | 0.9 | 0.97 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.68 | 1.71 | 3.46 | PROXY |
| F | 6.31 | 7.28 | 7.96 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.52 | 9.63 | 10.00 | ESTIMATE |

## Caveats
- a: The available occupation mix is four-digit restaurant data and includes full-service and meal-focused concepts unlike the target industry.
- a: O*NET reports occupation tasks rather than time shares, so task exposure is model judgment rather than a directly measured industry quantity.
- a: The frozen compensation-to-receipts input uses 2024 wages over 2022 receipts and is harmonized to the IPS basis, so the labor intensity combined with this primitive has vintage and methodology uncertainty.
- rho: The technology survey combines quick-service restaurants, delis, and coffee shops and reports intentions rather than realized operating changes.
- rho: Large chains likely have better integration resources than the lower-middle-market firms in the lens, which can make observed sector enthusiasm optimistic for implementation.
- rho: This primitive excludes pricing, demand, and valuation effects and addresses only operational implementation.
- e: No source directly measures eligibility under this bespoke roll-up lens.
- e: Franchise consent and location-specific leases may make control transfers less feasible than ordinary restaurant sale records imply.
- e: The frozen count of 507 firms is itself an ESTIMATE based on size classes and a broad restaurant EBITDA margin bridge, so applying eligibility compounds classification uncertainty.
- s5: Gallup measures stated plans across industries, not completed transactions in this NAICS code.
- s5: BizBuySell's median restaurant economics are below the lower-middle-market band and its marketplace does not capture private off-market deals.
- s5: Closures, internal reorganizations, minority investments, and transfers of only a lease or equipment do not qualify and are excluded from the estimate.
- q: There are no long-duration customer contracts to observe pass-through or renewal repricing directly.
- q: The 2026 restaurant survey found persistent margin pressure and 42% of operators unprofitable in 2025, but this is a broad-sector condition rather than a measurement of benefit retention.
- q: Brand strength, local density, franchise rules, and delivery mix can move retention materially across firms.
- d5: The central path extrapolates a single-year broad-restaurant real-sales forecast rather than a direct five-year quantity forecast.
- d5: Employment growth is an imperfect demand proxy because labor productivity and automation can change.
- d5: Coffee, juice, frozen dessert, and bakery-snack concepts can have materially different traffic cycles.
- o: Robotics and unattended formats may progress faster than current restaurant surveys indicate.
- o: Self-service changes who performs ordering and payment but does not necessarily eliminate the accountable operating firm, so those effects are not treated as full demand loss.
- o: This estimate concerns the current service basket at constant quality, not newly invented automated formats.

## Sources
- **S0** — [2022 North American Industry Classification System Manual: NAICS 722515](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines the target industry as fixed-location establishments preparing or serving specialty snacks or nonalcoholic beverages for consumption on or near the premises and lists coffee shops, juice bars, frozen-dessert parlors, and bakery-snack concepts.
- **S1** — [May 2023 OEWS Industry-Specific Estimates: Restaurants and Other Eating Places](https://www.bls.gov/oes/2023/may/naics4_722500.htm) (accessed 2026-07-22): Measures broad-restaurant occupation employment shares and wages, including 88.97% in food preparation and serving, 28.16% fast-food and counter workers, and 8.34% first-line food-service supervisors.
- **S2** — [O*NET OnLine: Fast Food and Counter Workers](https://www.onetonline.org/link/summary/35-3023.00) (accessed 2026-07-22): Documents the occupation's digital and cognitive tasks such as order entry, payment, receipt balancing, customer communication, and inventory alongside physical serving, preparation, cleaning, stocking, and food-safety work.
- **S3** — [Restaurant Technology Landscape Report 2024](https://go.restaurant.org/rs/078-ZLA-461/images/NatRestAssoc_TechLandscapeReport_2024.pdf) (accessed 2026-07-22): Reports limited-service customer acceptance of apps and kiosks, operator plans for self-ordering, AI, labor management, inventory, and back-office technology, and the expectation among 69% of limited-service operators that technology will augment rather than replace labor.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Finds 22% of employer-business owners planned a sale or ownership transfer within five years, 30% among older employer owners, and 52.3% of employer businesses owned by people at least 55.
- **S5** — [Restaurant Business Valuation Multiples and Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/restaurants/) (accessed 2026-07-22): Reports 8,692 analyzed sold restaurant listings, a 178-day median time on market, and median revenue and owner earnings that reveal active but predominantly Main Street transaction flow.
- **S6** — [Food and Beverage Serving and Related Workers: Occupational Outlook Handbook](https://www.bls.gov/ooh/food-preparation-and-serving/food-and-beverage-serving-and-related-workers.htm) (accessed 2026-07-22): Projects 5% employment growth for food and beverage serving and related workers and explains that growing dining-out, takeout, and delivery demand supports the occupation.
- **S7** — [State of the Restaurant Industry 2026](https://restaurant.org/research-and-media/research/research-reports/state-of-the-industry) (accessed 2026-07-22): Projects 1.3% real restaurant sales growth in 2026, reports that 61% of adults consider dining out essential, and describes soft traffic, rising costs, technology investment, and profitability pressure.
