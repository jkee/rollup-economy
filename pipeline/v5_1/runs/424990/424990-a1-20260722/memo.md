# 424990 — Other Miscellaneous Nondurable Goods Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `424990-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.94 · L 0.80 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat replenishment economics plus AI-addressable catalog, order, purchasing, service, and administrative workflows.
**Weakness:** The residual NAICS population is highly heterogeneous, and the eligible share cannot be established from public product-line firm counts.

## Business-model lens
- Included: Independent US merchant wholesalers in the band that repeatedly replenish non-living, nondurable supplies for external retailers, commercial users, and manufacturers, including pet supplies excluding food and live pets, art supplies, textile bags and canvas goods, industrial yarns, brushes, plant food, packaging-like goods, and similar catalog products.
- Excluded: Live pets, aquarium fish and live bait; cut Christmas trees and highly seasonal novelty-only businesses; prepaid calling-card distribution; commodity-only oils, meals, pulp, skins, or rubber traders whose economics are brokerage-like; manufacturer-owned branches, captive units, retailers, shells, and firms outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: Repeat product distribution through quoted, catalog, contract, or account prices, supported by inventory ownership, sourcing, credit, order processing, customer service, and delivery coordination.
- Deviation from default lens: The residual NAICS mixes live-animal handling, seasonal products, commodity trading, prepaid communications, consumer novelties, and recurring supply distribution, so one operating screen would be incoherent. The lens retains non-living recurring replenishment distributors with comparable inventory-and-account-service workflows and excludes the operationally distinct categories listed above; the narrowing is for business-model coherence, not attractiveness.

## Executive view
The residual code is too heterogeneous to screen coherently as a whole. A narrowed population of recurring, non-living supply distributors has a repeat inventory-and-account-service model with substantial information work, but its opportunity is diluted by product-line variation, fragmented data, physical fulfillment, channel bypass, and competitive pass-through.

## How AI changes the work
AI can normalize supplier catalogs, answer routine product questions, prepare quotes, capture and validate orders, forecast replenishment, draft customer communications, classify invoices, flag pricing or credit exceptions, and coordinate freight. Physical handling, merchandising, nuanced product advice, relationship selling, and accountability remain human and operational.

## Value capture
Savings are not contractually tied to labor hours, so distributors can initially retain them as margin or capacity. Catalog price comparison, procurement sophistication, retailer concentration, competitive bids, and direct channels should force meaningful sharing over five years, with better retention in differentiated assortments and service-intensive niches.

## Firm availability
Eligibility is the weakest population question because the NAICS bucket spans live animals, seasonal goods, commodities, communications products, and many small specialty categories. Transfer supply is plausible given mature owner demographics and observed wholesale business sales, but niche supplier rights and founder knowledge can impede control transfers.

## Demand durability
Recurring replacement and consumption support the retained basket, and moderate real economic growth is a tailwind. Category decline, product substitution, retailer consolidation, direct sourcing, and marketplaces create a wide range around modest base-case quantity growth.

## Risks and uncertainty
No public data reveal the product-line mix of EBITDA-band firms, and broader 4249 data include several other six-digit industries. Occupation exposure, implementation, transfer rates, pass-through, and channel migration are consequently proxies or estimates; diligence must begin with firm-level classification rather than treating the NAICS label as homogeneous.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1121 | — | OBSERVED | — |
| n | — | 808 | — | ESTIMATE | — |
| a | 0.25 | 0.38 | 0.52 | PROXY | S2, S3, S4, S6 |
| rho | 0.26 | 0.47 | 0.68 | PROXY | S5, S6 |
| e | 0.42 | 0.58 | 0.72 | ESTIMATE | S1, S9 |
| s5 | 0.11 | 0.21 | 0.33 | PROXY | S7, S8 |
| q | 0.38 | 0.58 | 0.76 | ESTIMATE | S1, S10 |
| d5 | 0.94 | 1.03 | 1.12 | PROXY | S9, S10 |
| o | 0.84 | 0.93 | 0.98 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.29 | 0.80 | 1.59 | PROXY |
| F | 5.87 | 7.40 | 8.47 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.90 | 9.58 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation data cover a broader wholesale population than 424990 or the narrowed lens.
- a: O*NET task importance is neither hours worked nor wage weight.
- a: Exposure varies materially between catalog-rich pet or art supplies and commodity or irregular novelty products.
- rho: BTOS usage is economy-wide and does not measure labor substitution intensity.
- rho: The customer-support productivity study is not a wholesale-distribution deployment.
- rho: The retained product categories differ in data quality, service complexity, and implementation economics.
- e: The injected firm count is margin-bridged from size-class data and may not align with actual EBITDA-band operating companies.
- e: NAICS classification is establishment-based, while eligibility is firm-based.
- e: The absence of public product-line firm counts makes the retained share particularly uncertain.
- s5: Owner-age evidence is all-industry, not NAICS 424990.
- s5: BizBuySell represents advertised smaller businesses and does not measure probability per eligible firm.
- s5: Closures and internal reorganizations are excluded from qualifying transfers.
- q: No source directly measures five-year AI-benefit pass-through in the narrowed industry.
- q: Commercial retention differs sharply across the residual code's product lines.
- q: The estimate excludes implementation failure and quantity loss, which belong in other primitives.
- d5: NAICS 4249 sales include farm supplies, books, flowers, tobacco, and paint as well as 424990.
- d5: Monthly wholesale sales are nominal and volatile; they do not directly measure constant-quality quantity.
- d5: Real GDP is an economy-wide proxy and may not track the residual industry's product mix.
- o: No observed dataset measures future operator-required share for this narrowed population.
- o: Channel bypass risk is much higher for standardized catalog goods than for fragmented or service-heavy assortments.
- o: Requiring an operator does not require today's staffing or branch footprint.

## Sources
- **S1** — [2022 NAICS index entries for 424990](https://www.census.gov/naics/?chart=2022&details=424990&input=424990) (accessed 2026-07-22): Lists the unusually broad product population, including aquarium fish, art goods, Christmas trees, canvas products, pet supplies, textile bags, prepaid calling cards, oils, pulp, rubber, novelties, and industrial yarns.
- **S2** — [Merchant Wholesalers, Nondurable Goods: NAICS 424](https://www.bls.gov/iag/tgs/iag424.htm) (accessed 2026-07-22): Reports 2025 broader-industry employment of 269,740 nontechnical wholesale sales representatives, 54,000 technical sales representatives, 174,610 heavy truck drivers, 162,830 hand material movers, and 43,040 shipping and traffic clerks.
- **S3** — [O*NET: Sales Representatives, Wholesale and Manufacturing, Except Technical and Scientific Products](https://www.onetonline.org/link/details/41-4012.00) (accessed 2026-07-22): Shows core information tasks such as answering product and price questions, recommending products, quoting terms and delivery, preparing order forms, monitoring competitors, and maintaining records.
- **S4** — [O*NET: Shipping, Receiving, and Inventory Clerks](https://www.onetonline.org/link/details/43-5071.00) (accessed 2026-07-22): Shows both information tasks such as documents, records, carrier arrangements, routing and charge calculations and physical tasks such as packing and moving shipments.
- **S5** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Census BTOS data for December 2025-May 2026 put overall business AI use at 17-20% and expected use over the next six months at 20-23%, with material size and sector variation.
- **S6** — [Generative AI at Work](https://www.nber.org/papers/w31161) (accessed 2026-07-22): A field study of 5,179 customer-support agents finds a 14% average productivity increase from an AI assistant and larger effects for novice and lower-skilled workers.
- **S7** — [Financing, Ownership, and Performance](https://www2.census.gov/library/working-papers/2024/adrm/ces/CES-WP-24-73.pdf) (accessed 2026-07-22): Census research reports that 72.7% of mature employer firms in the 2022 ABS had at least one owner age 55 or older.
- **S8** — [Wholesale/Distribution Business Valuation Multiples and Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/wholesale-distribution/) (accessed 2026-07-22): Aggregates listed and sold wholesale/distribution businesses and reports movement in median sale price through 2025, evidencing a functioning small-business transfer market without providing a population rate.
- **S9** — [Monthly Wholesale Trade Report, February 2026](https://www2.census.gov/wholesale/pdf/mwts/historic/mwts_202602.pdf) (accessed 2026-07-22): Reports February 2026 not-seasonally-adjusted NAICS 4249 sales 5.0% above February 2025 and explicitly states that the survey data are not adjusted for price changes.
- **S10** — [The Budget and Economic Outlook: economic outlook for 2026 to 2031](https://www.cbo.gov/publication/56991) (accessed 2026-07-22): Projects the US economy to continue expanding from 2026 to 2031, with real GDP growth averaging 1.6% annually.
