# 311520 — Ice Cream and Frozen Dessert Manufacturing

*v5.1 Stage 1 research memo. Run `311520-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.97 · L 0.54 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Seasonal planning complexity, differentiated brands, and repeat retail and foodservice demand create deployable information-work opportunities.
**Weakness:** Mature declining volume and physical cold-chain production limit durable growth and software-only labor substitution.

## Business-model lens
- Included: U.S. lower-middle-market operators that repeatedly manufacture ice cream, frozen yogurt, frozen ices, sherbet, frozen tofu, and other frozen desserts for external retail, foodservice, distributor, private-label, or branded customers.
- Excluded: Frozen bakery products, dairy farms, scoop shops or restaurants without qualifying manufacturing, captive internal plants without external customers, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat unit- or volume-priced product sales through retail, foodservice, distributor, branded, club, and private-label channels, often with seasonal demand, promotions, slotting, and cold-chain requirements.
- Deviation from default lens: none

## Executive view
Ice cream and frozen dessert manufacturing offers recurring product demand, brand and private-label niches, and useful AI applications in seasonal planning and complex commercial workflows. The counterweight is a mature volume category with long-run decline, physical production labor, cold-chain intensity, retailer power, and a meaningful risk that scale processors capture share.

## How AI changes the work
AI can improve seasonal demand forecasts, SKU and production scheduling, trade-promotion analysis, ingredient procurement, quality-document review, deviation triage, maintenance support, customer service, and administrative work. It does not replace most batching, freezing, filling, sanitation, warehousing, maintenance, and refrigerated distribution activity.

## Value capture
Premium brands, distinctive formulations, innovation, and dependable service can preserve savings better than transparent private-label or co-manufacturing bids. Retail buyers, distributors, promotions, renewal pricing, and competing processors' adoption will transfer part of the benefit to customers.

## Firm availability
The frozen dataset identifies 90 LMM-band firms, but true eligibility requires independent manufacturing operations, recurring external customers, transferable brands or contracts, cold-chain capability, and limited dependence on a founder or single retailer. National owner-age evidence supports succession pressure without measuring this industry's transfers.

## Demand durability
USDA evidence shows frozen dairy production 10% below its 2003 peak and declining again after 2022, with meaningful format shifts. Regular ice cream remains dominant, and specialty, premium, nondairy, or private-label niches can grow, but the prudent base case is a modest five-year volume decline for the current basket.

## Risks and uncertainty
Major risks include category volume decline, retailer concentration, promotion dependence, brand durability, seasonality, food-safety and allergen exposure, recalls, freezer and cold-chain capex, energy cost, commodity volatility, slotting and returns, legacy systems, cybersecurity, and forecast error that creates waste. A weak brand or open-book private-label target with obsolete refrigeration and concentrated customers could erase the expected benefit.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1357 | — | OBSERVED | — |
| n | — | 90 | — | ESTIMATE | — |
| a | 0.11 | 0.2 | 0.31 | PROXY | S2 |
| rho | 0.28 | 0.5 | 0.72 | ESTIMATE | S3, S4 |
| e | 0.45 | 0.63 | 0.8 | ESTIMATE | S1 |
| s5 | 0.09 | 0.2 | 0.33 | PROXY | S5 |
| q | 0.32 | 0.58 | 0.8 | ESTIMATE | — |
| d5 | 0.82 | 0.95 | 1.1 | PROXY | S6, S7 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1, S4, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.54 | 1.21 | ESTIMATE |
| F | 2.47 | 4.04 | 5.16 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.71 | 9.31 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation evidence covers the broader dairy-manufacturing group.
- a: Counts are not wage-weighted task measures and require judgmental mapping.
- a: Physical automation and robotics are excluded unless AI directly avoids labor or hiring.
- rho: Regulatory guidance shows requirements and feasible computerized functions, not observed AI conversion rates.
- rho: Branded operators with rich sell-through data may implement faster than private-label plants dependent on customer forecasts.
- e: The frozen LMM count is accepted without re-estimation.
- e: The NAICS definition describes production activities but not recurring-customer quality, independence, or enterprise transferability.
- s5: The owner-age statistic is national, cross-industry, and based on 2018 data.
- s5: It measures responding owners rather than firms and does not observe transactions.
- q: No public source directly measures retention of AI-derived benefits in this industry.
- q: Branded premium products can retain much more than private-label or commodity-like frozen novelties.
- q: Shrinkflation and promotion changes can obscure true pass-through.
- d5: Production reflects inventories, imports, exports, and capacity as well as end demand.
- d5: USDA's cited series emphasizes frozen dairy and may not fully represent nondairy products included in NAICS 311520.
- d5: Aggregate decline can coexist with growth in premium, novelty, private-label, or nondairy niches.
- o: This estimates accountable-operator need, not employment intensity.
- o: Operator responsibility may consolidate into larger manufacturers even though software cannot eliminate it.

## Sources
- **S1** — [North American Industry Classification System: 311520 Ice Cream and Frozen Dessert Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines 311520 as manufacturing ice cream, frozen yogurt, frozen ices, sherbet, frozen tofu, and other frozen desserts, while excluding frozen bakery products.
- **S2** — [BLS OEWS Data Tables for Industry Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest dairy-manufacturing occupations, including 25,520 food batchmakers, 23,690 packaging/filling operators, 8,170 material movers, and 7,840 production supervisors.
- **S3** — [FDA: Computerized Systems in the Food Processing Industry](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-guides/computerized-systems-food-processing-industry) (accessed 2026-07-22): Describes computerized food-processing records and controls and review expectations for regulatory equivalence and safety-critical functions.
- **S4** — [FDA: Keeping Your Milk Safe From the Grass to the Glass](https://www.fda.gov/consumers/consumer-updates/keeping-your-milk-safe-grass-glass) (accessed 2026-07-22): Describes regulated dairy responsibilities for processing times and temperatures, equipment control and testing, worker safety, laboratory testing, and oversight.
- **S5** — [U.S. Census Bureau: Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding owners of U.S. employer businesses were age 55 or older in the 2019 ABS covering data year 2018.
- **S6** — [USDA ERS: Ice cream and frozen dairy production dipped from 2000 to 2024](https://ers.usda.gov/data-products/charts-of-note/112892) (accessed 2026-07-22): Reports a 10% decline from the 2003 peak of 1,542 million gallons to 1,386 million gallons in 2024, renewed decline after 2022, and regular ice cream at about 60-65% of output.
- **S7** — [USDA ERS: Low-fat and nonfat ice cream production is heating up the market](https://ers.usda.gov/data-products/charts-of-note/109566) (accessed 2026-07-22): Reports 1.3 billion gallons of U.S. ice cream production in 2023 and a decline in aggregate frozen-dairy output from 1.5 billion gallons annually in 1999-2003 to 1.4 billion in 2019-2023.
- **S8** — [USDA AMS Ice Cream Standard](https://www.ams.usda.gov/grades-standards/ice-cream) (accessed 2026-07-22): Specifies physical composition and weight requirements for ice cream, including minimum total solids, milk solids, and milkfat.
