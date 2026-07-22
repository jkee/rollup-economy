# 445110 — Supermarkets and Other Grocery Retailers (except Convenience Retailers)

*v5.1 Stage 1 research memo. Run `445110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.17 · L 0.50 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable physical grocery demand combined with repetitive forecasting, ordering, checkout, scheduling, and back-office workflows.
**Weakness:** Nearly all industry firms are merchandise retailers rather than recurring outsourced-service providers, leaving very few firms eligible under the fixed lens.

## Business-model lens
- Included: U.S. firms primarily classified as supermarkets or other grocery retailers, with eligibility limited by the fixed screen to firms that also earn meaningful recurring or repeat revenue from an outsourced service delivered to external customers, such as contracted workplace pantry replenishment, managed grocery programs, or service-led ordering and fulfillment bundled with the grocery relationship.
- Excluded: Convenience retailers; warehouse clubs and supercenters; pure grocery delivery or local messenger firms acting on behalf of retailers; wholesalers; restaurants; captive internal units; shells; non-control financing vehicles; and conventional grocery retailers whose customer proposition is only the resale of merchandise.
- Customer and revenue model: The underlying industry is predominantly consumer-facing, transaction-priced merchandise resale through stores and online channels. The rare eligible subset must have a repeat external-customer service relationship, generally combining grocery procurement with ordering, replenishment, fulfillment, or account management; this screen does not treat ordinary repeat shopping or a loyalty program as an outsourced service.
- Deviation from default lens: none

## Executive view
Grocery retail has durable physical demand and meaningful repetitive-work automation potential, but the fixed screen is a poor fit for the industry's dominant business model. Most supermarkets sell merchandise transaction by transaction rather than provide an outsourced service; only a very small service-led tail is eligible. Any diligence should first prove that a target's recurring managed-service revenue is real and separable from ordinary grocery sales.

## How AI changes the work
AI can improve demand forecasting, ordering, workforce scheduling, promotion design, customer inquiries, fraud and shrink review, and administrative workflows. Checkout and online ordering show that retail work can move to software or customers, but much store labor remains physical: receiving, shelf replenishment, food preparation, cleaning, age checks, and exception handling. Current retail AI use is still modest, especially for smaller firms.

## Value capture
Transaction pricing lets a grocer keep early labor savings, but visible prices, low switching costs, promotions, supplier bargaining, and intense competition should erode a meaningful portion over five years. The eligible service-led subset could retain more under sticky managed-service contracts, but that must be established contract by contract and should not be inferred from loyalty-program repeat purchases.

## Firm availability
The injected LMM-band count is an estimate, and only a near-zero share appears eligible under the fixed outsourced-service lens. Aging small-business ownership supports some five-year transfer flow, but viable grocery transfers depend heavily on leases, licenses, supplier or cooperative relationships, local competitive position, management depth, and whether the service relationship survives a change of control.

## Demand durability
Real food-at-home spending has a long record of growth, and physical grocery demand is unlikely to be eliminated by software. Channels can change: online ordering, third-party delivery, supercenters, clubs, direct-to-consumer supply, and food-away-from-home can all reduce the amount served by this exact operator type. AI is more likely to alter ordering and fulfillment than eliminate accountable food handling.

## Risks and uncertainty
The largest uncertainty is classification and lens fit, not whether people will keep buying food. Additional risks include thin margins, price competition, supplier power, perishability and shrink, food-safety and licensing obligations, labor relations, capital-intensive stores and automation, location and lease dependence, and the possibility that independent operators cannot match chains' technology or purchasing economics. A target lacking genuine contracted service revenue would fail the screen regardless of its automation potential.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.129 | — | OBSERVED | — |
| n | — | 961 | — | ESTIMATE | — |
| a | 0.16 | 0.24 | 0.34 | PROXY | S1, S2 |
| rho | 0.28 | 0.4 | 0.62 | PROXY | S1, S3, S4 |
| e | 0.002 | 0.01 | 0.03 | ESTIMATE | S4 |
| s5 | 0.12 | 0.22 | 0.35 | PROXY | S8 |
| q | 0.25 | 0.42 | 0.6 | ESTIMATE | S4, S5 |
| d5 | 0.98 | 1.05 | 1.12 | PROXY | S6 |
| o | 0.88 | 0.95 | 0.99 | PROXY | S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.23 | 0.50 | 1.09 | PROXY |
| F | 0.33 | 1.83 | 3.87 | ESTIMATE |
| C | 5.00 | 8.40 | 10.00 | ESTIMATE |
| D | 8.62 | 9.97 | 10.00 | PROXY |

## Caveats
- a: The key occupation-share observation is from 2018 and covers NAICS 4451 and 4452, broader than NAICS 445110.
- a: Task shares within occupations are judgmental, and the estimate excludes gains from automation already implemented.
- a: The frozen compensation-to-output input is a high-quality 2024 direct BLS measure, but it does not resolve the occupation/task allocation used here.
- rho: BTOS reports business use, not labor-opportunity implementation intensity.
- rho: Retail Trade is broader than grocery retail and the eligible service-led subset may differ from both.
- rho: Self-checkout and conventional rules-based automation are informative implementation precedents but are not themselves evidence of future AI implementation.
- e: No source enumerates the fixed-lens eligible subset directly.
- e: The public-company example confirms the dominant retail model but may not represent niche independent operators.
- e: The frozen firm count of 961 is an ESTIMATE margin-bridged from SUSB size classes using a 5.40% sector EBITDA margin; both band assignment and this eligibility filter are uncertain.
- s5: The owner-age statistic is secondary reporting of Census data and is not grocery-specific or LMM-specific.
- s5: No observed denominator of eligible firms or completed qualifying transfers was found.
- s5: The very small eligible subset makes the probability especially sensitive to a few atypical firms.
- q: No source directly measures five-year retention of AI-created gross benefit.
- q: FTC margin evidence reflects pandemic-era food and beverage retailers and is not a clean measure of competitive pass-through from automation.
- q: The rare outsourced-service subset may use contracts and pricing structures unlike conventional supermarkets.
- d5: Food-at-home expenditure is broader than supermarket output and is not a constant-quality quantity index.
- d5: The long historical interval includes structural shifts that may not repeat over the next five years.
- d5: Demand for the eligible service-led subset may diverge from household grocery demand.
- o: Online shopping incidence is not sales share or operator displacement.
- o: The 2022 consumer survey predates further growth in AI agents and rapid-delivery platforms.
- o: The distinction between software interface, third-party delivery, and accountable grocery operator can vary by transaction.

## Sources
- **S1** — [Checking out productivity in grocery stores](https://www.bls.gov/opub/btn/volume-8/checking-out-productivity-in-grocery-stores.htm) (accessed 2026-07-22): BLS identifies NAICS 445110, reports that cashiers and stock clerks/order fillers were 49.6% of Food and Beverage Stores employment in May 2018, describes self-checkout and related technologies, and documents grocery productivity history and channel change.
- **S2** — [Occupational Outlook Handbook: Cashiers](https://www.bls.gov/ooh/sales/cashiers.htm) (accessed 2026-07-22): BLS lists cashier tasks, reports food and beverage retailers employed 29% of cashiers in 2024, and projects cashier employment to decline 10% from 2024 to 2034 because of technologies including self-service checkout and online sales.
- **S3** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Census BTOS data through May 3, 2026 show about 14% of Retail Trade businesses currently using AI and about 17% expecting use within six months; adoption is higher at larger firms.
- **S4** — [Village Super Market, Inc. Form 10-K for fiscal year ended July 26, 2025](https://www.sec.gov/Archives/edgar/data/103595/000010359525000015/vlgea-20250726.htm) (accessed 2026-07-22): The filing describes supermarket competition and narrow margins, transaction and loyalty economics, online ordering and third-party delivery, physical operations, licensing, capital needs, labor structure, and the 2024 closure of an automated micro-fulfillment center.
- **S5** — [FTC Releases Report on Grocery Supply Chain Disruptions](https://www.ftc.gov/news-events/news/press-releases/2024/03/ftc-releases-report-grocery-supply-chain-disruptions) (accessed 2026-07-22): FTC reports smaller grocery retailers faced disproportionate supply difficulty and that food and beverage retailer revenue exceeded total costs by more than 6% in 2021 and 7% in the first three quarters of 2023, illustrating supplier power and variable margin retention.
- **S6** — [Total U.S. food spending reached $2.51 trillion in 2025](https://www.ers.usda.gov/data-products/charts-of-note/114212) (accessed 2026-07-22): USDA ERS reports inflation-adjusted food-at-home expenditures increasing from $738 billion in 1997 to $1.10 trillion in 2025.
- **S7** — [Nearly 20 percent of U.S. shoppers bought groceries online in 2022](https://www.ers.usda.gov/data-products/charts-of-note/108618) (accessed 2026-07-22): USDA ERS reports 19.3% of regular U.S. grocery shoppers bought groceries online at least once in the prior 30 days in 2022 and provides purchase-frequency detail.
- **S8** — [Starting a small business is hard. Exiting can be even harder, but planning early is the key](https://apnews.com/article/small-business-succession-retirement-sale-transition-d582a18f1e440846a6ff5bb425ba6daa) (accessed 2026-07-22): Associated Press reports, citing the U.S. Census, that about 51% of small-business owners are over age 55 and distinguishes sale, internal succession, and closure as exit paths.
