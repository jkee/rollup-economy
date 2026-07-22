# 445291 — Baked Goods Retailers

*v5.1 Stage 1 research memo. Run `445291-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.33 · L 0.20 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat product demand plus automatable ordering and administrative workflows supports a modest implementable labor opportunity.
**Weakness:** Very few 445291 firms appear eligible because ordinary walk-in product retail is not a recurring outsourced service, leaving a tiny transferable pool.

## Business-model lens
- Included: US baked-goods retailers selling products made off premises through recurring or repeat supply relationships, such as standing business, institutional, hospitality, or event accounts, within the lower-middle-market EBITDA band.
- Excluded: Walk-in consumer-only shops without a recurring outsourced supply relationship; products baked on premises; bakery cafes and immediate-consumption food service; captive outlets, shells, and non-control financing vehicles.
- Customer and revenue model: The eligible model earns predominantly fixed-price product revenue from repeated orders or scheduled deliveries to external customers, with merchandising, ordering, fulfillment, and account service embedded in the product margin.
- Deviation from default lens: none

## Executive view
Baked-goods retailing is mainly a product-merchant model, so only a small B2B standing-account subset fits the recurring outsourced-service lens. That subset offers modest AI-enabled labor opportunity in administrative, ordering, marketing, and customer-service work, but physical fulfillment and intense channel competition limit both implementation and retained economics.

## How AI changes the work
AI is most relevant to demand forecasts, replenishment suggestions, promotion generation, order intake, customer questions, bookkeeping, and scheduling. Checkout and inventory software already automate part of the workflow, while stocking, packing, freshness control, delivery, and relationship selling remain operator-intensive.

## Value capture
Fixed prices permit initial retention of savings, especially in differentiated local accounts, but transparent product pricing and numerous substitutes invite repricing and customer sharing over renewal cycles. Durable capture depends more on service reliability and account embeddedness than on proprietary technology.

## Firm availability
The frozen data imply only 11 firms in the EBITDA band before eligibility. Most are unlikely to meet the service lens, and general small-business succession pressure does not guarantee a sale, so the practical acquisition pool may be zero or one firm in a given period.

## Demand durability
Underlying baked-goods quantity should be broadly stable, supported by habitual consumption, convenience, population, and specialty demand. Dedicated retailers nevertheless face continuing substitution toward grocery, mass retail, online marketplaces, and direct distribution.

## Risks and uncertainty
The largest uncertainties are the absence of six-digit occupation and AI-adoption data, the unknown share of revenue tied to recurring business accounts, and the difference between stable product demand and survival of the dedicated retail channel. Thin margins, perishability, vendor concentration, and local competition can overwhelm modest labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2497 | — | OBSERVED | — |
| n | — | 11 | — | ESTIMATE | — |
| a | 0.12 | 0.22 | 0.33 | PROXY | S2, S3, S4 |
| rho | 0.3 | 0.48 | 0.65 | PROXY | S5 |
| e | 0.02 | 0.06 | 0.15 | ESTIMATE | S1 |
| s5 | 0.1 | 0.2 | 0.32 | PROXY | S7 |
| q | 0.22 | 0.4 | 0.58 | ESTIMATE | S6 |
| d5 | 0.94 | 1.01 | 1.09 | PROXY | S6, S8 |
| o | 0.62 | 0.8 | 0.93 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.36 | 1.05 | 2.14 | PROXY |
| F | 0.04 | 0.20 | 0.68 | ESTIMATE |
| C | 4.40 | 8.00 | 10.00 | ESTIMATE |
| D | 5.83 | 8.08 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is for NAICS 445 or national occupations, not 445291 specifically.
- a: Self-checkout is conventional automation and is excluded except where new AI changes residual work.
- a: The frozen compensation ratio has a 2024-wage/2022-receipts vintage mismatch and is harmonized from an unadjusted six-digit input.
- rho: BTOS is sector-wide and measures any AI use, not the share of exposed labor opportunity implemented.
- rho: Implementation may improve service or sales without reducing labor, which is not counted here.
- e: No published source measures the recurring external-customer service share inside 445291.
- e: The frozen n=11 is a margin-bridged estimate from size-class firm counts and average receipts, not an observed EBITDA-band census.
- s5: The source covers all US businesses and a ten-year need-for-buyer concept, not completed five-year control transfers.
- s5: Few eligible firms are implied after applying e to the frozen n, so one transaction would change the realized rate sharply.
- q: No source directly observes benefit sharing following AI implementation in 445291.
- q: The estimate excludes volume loss, which is handled in demand and operator-required share.
- d5: BLS projections are employment measures and cover broader populations than 445291 demand.
- d5: Constant-quality product mix is difficult to distinguish from premiumization and package-size changes.
- o: The estimate distinguishes elimination of the lens operator from digitization of customer interaction.
- o: A channel shift can preserve baked-goods demand while removing the dedicated 445291 operator.

## Sources
- **S1** — [2022 NAICS Definition: 445291 Baked Goods Retailers](https://www.census.gov/naics/?details=44529&input=44529&year=2022) (accessed 2026-07-22): Defines 445291 as establishments retailing baked goods not for immediate consumption and not made on premises, and distinguishes on-premises baking and food service.
- **S2** — [Food and Beverage Stores: NAICS 445](https://www.bls.gov/iag/tgs/iag445.htm) (accessed 2026-07-22): Shows common 2025 NAICS 445 occupations including 933,680 cashiers, 666,380 stock clerks/order fillers, 190,880 retail supervisors, and 187,430 food-preparation workers.
- **S3** — [O*NET OnLine: Cashiers](https://www.onetonline.org/link/summary/41-2011.00) (accessed 2026-07-22): Lists cashier tasks including receiving payments, issuing receipts/refunds, assisting customers, stocking shelves, and packaging merchandise.
- **S4** — [O*NET OnLine: Retail Salespersons](https://www.onetonline.org/link/details/41-2031.00) (accessed 2026-07-22): Lists retail-sales activities including transaction processing, sales records, customer questions, inventory monitoring, purchasing stock, product selection, and packaging.
- **S5** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports spring 2026 Retail Trade AI use around 14% and expected six-month use around 17%, below the national average.
- **S6** — [Industry and occupational employment projections overview and highlights, 2024-34](https://www.bls.gov/opub/mlr/2026/article/industry-and-occupational-employment-projections-overview.htm) (accessed 2026-07-22): Projects grocery and specialty food retailer employment down 1.0% from 2024 to 2034 and describes competitive pressure and cashier job losses.
- **S7** — [The employee ownership pipeline: What we've learned](https://project-equity.org/news/employee-ownership-insider/the-employee-ownership-pipeline-what-weve-learned/) (accessed 2026-07-22): States that 2.9 million US businesses need to find buyers in the next decade, supporting broad succession pressure while not measuring completed transfers.
- **S8** — [Occupational Outlook Handbook: Bakers](https://www.bls.gov/ooh/production/bakers.htm) (accessed 2026-07-22): Projects baker employment growth of 6% from 2024 to 2034 and attributes demand partly to population, income, convenience, and specialty baked goods.
