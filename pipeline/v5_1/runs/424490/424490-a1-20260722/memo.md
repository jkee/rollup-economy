# 424490 — Other Grocery and Related Products Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `424490-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.80 · L 0.34 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High-frequency ordering, assortment, and delivery coordination creates recurring automatable work around an essential physical product flow.
**Weakness:** A heterogeneous residual category and competitive merchant margins make savings difficult to generalize and retain.

## Business-model lens
- Included: Independent merchant wholesalers repeatedly buying and reselling the grocery and related products classified in 424490, including bakery products, canned foods, dried or canned dairy and meat products, soft drinks, bottled water processed by others, and other grocery specialties, to external retail, foodservice, institutional, and wholesale customers.
- Excluded: Manufacturer-owned sales branches, captive distribution operations, pure brokers and agents, producers whose principal activity is manufacturing or bottling their own goods, shells, non-control financing vehicles, and firms outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: Repeat B2B product resale earning a merchant gross margin, with varying combinations of sourcing, assortment, warehousing, route delivery, merchandising, inventory availability, and customer service.
- Deviation from default lens: none

## Executive view
Other grocery wholesaling offers repeat demand and a meaningful layer of sales, clerical, planning, and coordination work that AI can compress. The physical distribution role is durable, but the residual category's product heterogeneity and competitive merchant-margin model make benefit retention and firm-level repeatability uncertain.

## How AI changes the work
AI can normalize inbound orders, map customer descriptions to SKUs, draft quotes and promotions, forecast replenishment, reconcile invoices and allowances, prepare account calls, answer routine product questions, and optimize routes. Humans remain accountable for supplier and customer negotiations, food-safety exceptions, credit, substitutions, warehouse execution, merchandising judgment, and delivery.

## Value capture
Efficiency can improve gross margin and service levels, especially for fragmented customers and specialty assortments. Standardized branded products and concentrated buyers make savings visible and contestable, so operators should expect significant pass-through over renewals and competitive bids.

## Firm availability
The supplied LMM population is substantial and many businesses should be transferable as operating distributors. Screening must remove manufacturer-affiliated or captive units and test owner dependence, customer concentration, supplier rights, route economics, working capital, and true merchant status.

## Demand durability
The underlying food basket is essential and aggregate real food spending continues to grow modestly. Independent wholesaler demand is less secure than end demand because manufacturers and large customers can integrate or transact directly, with risk varying considerably by product line.

## Risks and uncertainty
The occupation evidence is old, the category mixes materially different products, and there is no direct pass-through or completed-transfer study. A target with commodity-like pricing, low service differentiation, weak data, high customer or supplier concentration, or adverse health-driven product trends could be a poor opportunity despite stable industry demand.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0516 | — | OBSERVED | — |
| n | — | 2135 | — | ESTIMATE | — |
| a | 0.18 | 0.28 | 0.38 | PROXY | S1, S2, S3 |
| rho | 0.36 | 0.58 | 0.75 | ESTIMATE | S2, S3 |
| e | 0.62 | 0.77 | 0.88 | ESTIMATE | S2, S3, S4 |
| s5 | 0.12 | 0.2 | 0.3 | PROXY | S5 |
| q | 0.25 | 0.43 | 0.63 | ESTIMATE | S3, S6, S7 |
| d5 | 0.97 | 1.04 | 1.12 | PROXY | S2, S4, S6 |
| o | 0.75 | 0.86 | 0.94 | ESTIMATE | S3, S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.13 | 0.34 | 0.59 | ESTIMATE |
| F | 8.16 | 9.33 | 10.00 | ESTIMATE |
| C | 5.00 | 8.60 | 10.00 | ESTIMATE |
| D | 7.28 | 8.94 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation evidence is from 2008 and covers EEO-1 filers rather than all LMM firms.
- a: EEOC job groups are coarser than SOC occupations and do not measure task exposure or wages.
- a: The code contains materially different product and route models.
- rho: No code-specific longitudinal implementation study was found.
- rho: Digital maturity likely varies more than industry averages reveal.
- e: The supplied LMM count is an estimate.
- e: NAICS 424490 is a residual category spanning unlike products, and public channel statistics are broader than the target band.
- s5: The Gallup sample spans all industries and sizes.
- s5: Plans are not realized transactions, and gifts or reorganizations may not qualify.
- q: No direct evidence measures pass-through of AI benefits in 424490.
- q: The range is wide because branded beverages, bakery routes, canned goods, and specialty/import products have different pricing power.
- d5: Aggregate food spending is much broader than this residual NAICS category.
- d5: Constant-dollar expenditures are not a direct physical-quantity measure.
- d5: Product-line trends inside 424490 may offset one another.
- o: Operator requirement is distinct from the market share of current independent firms.
- o: Packaged shelf-stable goods are easier to procure directly than niche, route-served, or frequently replenished products.

## Sources
- **S1** — [2008 EEO-1 National Aggregate Report by NAICS-5 Code: 42449 - Other Grocery and Related Products Merchant Wholesalers](https://www.eeoc.gov/eeo-1/2008-eeo-1-national-aggregate-report-naics-5-code-42449-other-grocery-and-related-products) (accessed 2026-07-22): Reports 114,580 workers across 462 units by job group, including 22,208 sales, 14,212 office/clerical, 13,599 managers, 6,168 professionals, 35,116 operatives, and 19,201 laborers.
- **S2** — [2022 NAICS Definition: 424490 Other Grocery and Related Products Merchant Wholesalers](https://www.census.gov/naics/?details=42449&input=42449&year=2022) (accessed 2026-07-22): Defines the industry's merchant-wholesale activity and enumerates included products such as bakery products, canned goods, soft drinks, and bottled water processed by others.
- **S3** — [Retailing & Wholesaling - Wholesaling](https://www.ers.usda.gov/topics/food-markets-prices/retailing-wholesaling/wholesaling) (accessed 2026-07-22): Defines third-party grocery merchants as buying and reselling to businesses, describes specialty distributors and customers, and documents direct, manufacturer-branch, broker, and merchant channels.
- **S4** — [42449: Other grocery and related products merchant wholesalers - Census Bureau Profile](https://data.census.gov/profile/42449_-_Other_grocery_and_related_products_merchant_wholesalers?codeset=naics~42449) (accessed 2026-07-22): Confirms the industry scope and reports 14,991 employer establishments in 2023, while distinguishing excluded adjacent wholesale categories.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 survey found 22% of employer-business owners planned to sell or transfer ownership within five years and separately measured closure and uncertainty.
- **S6** — [Total U.S. food spending reached $2.51 trillion in 2025](https://www.ers.usda.gov/data-products/charts-of-note/114212) (accessed 2026-07-22): Inflation-adjusted U.S. food expenditures rose from $2.49 trillion in 2024 to $2.51 trillion in 2025; both at-home and away-from-home spending increased.
- **S7** — [Wholesale and retail Producer Price Indexes: margin prices](https://www.bls.gov/opub/btn/volume-1/wholesale-and-retail-producer-price-indexes-margin-prices.htm) (accessed 2026-07-22): Explains that trade-industry output prices are margins received by wholesalers and retailers and shows their sensitivity to small selling-price changes.
