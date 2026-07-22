# 445230 — Fruit and Vegetable Retailers

*v5.1 Stage 1 research memo. Run `445230-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.29 · L 0.99 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat necessity demand plus AI-assisted replenishment, scheduling, and shrink control around a labor-intensive physical operation.
**Weakness:** A very small estimated LMM population operating in a price-transparent, low-margin market where most work remains physical.

## Business-model lens
- Included: US lower-middle-market specialty fruit and vegetable retailers with transferable store operations, repeat external customers, procurement and inventory routines, and an accountable operator.
- Excluded: Farm stands without a transferable operating organization, captive retail departments of larger chains, wholesalers, grower operations, passive entities, and stores outside the roughly $1-10 million normalized EBITDA band.
- Customer and revenue model: Primarily transaction-priced fresh produce and related grocery sales to repeat local consumers and some commercial customers, through physical stores and potentially pickup or delivery channels.
- Deviation from default lens: none

## Executive view
Fruit and vegetable retailing has a real but bounded AI opportunity: software can improve forecasting, ordering, scheduling, marketing, bookkeeping, and some customer service, while the core work remains physical and perishable. Repeat demand is durable, but transparent prices and broad grocery competition limit how much benefit stays with the operator.

## How AI changes the work
AI is most useful around the physical workflow rather than as a replacement for it. Better forecasts, replenishment suggestions, promotion design, labor scheduling, and exception detection can reduce waste and avoid hiring; receiving, inspection, rotation, sanitation, merchandising, picking, and customer trust still require people.

## Value capture
Transaction pricing allows early savings to accrue internally, yet competitive grocery markets encourage reinvestment in price, freshness, availability, and service. Retention should therefore be judged after ongoing price competition and customer sharing, not from gross labor savings alone.

## Firm availability
The frozen population contains few estimated LMM firms. Many should be operationally transferable, but aging-owner evidence is only broad-market evidence and a meaningful share of small retail exits will be closures, asset sales, or family transitions rather than qualifying acquisitions.

## Demand durability
Food-at-home demand is necessity-like and recent real spending has been stable to growing. The risk is not elimination of produce consumption but channel migration toward supermarkets, clubs, mass merchants, delivery platforms, and direct sellers; even digital fulfillment still needs accountable handling of perishables.

## Risks and uncertainty
The largest uncertainties are the absence of a six-digit occupation mix, limited evidence on closed specialty-retail transfers, and no direct measure of savings retention. Spoilage, local competition, lease quality, food safety, supplier dependence, undocumented family labor, and weak data systems can erase apparent automation economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2748 | — | OBSERVED | — |
| n | — | 24 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.3 | PROXY | S1, S2 |
| rho | 0.3 | 0.45 | 0.62 | PROXY | S3 |
| e | 0.55 | 0.72 | 0.86 | ESTIMATE | — |
| s5 | 0.12 | 0.22 | 0.35 | PROXY | S4 |
| q | 0.28 | 0.44 | 0.62 | PROXY | S5, S6 |
| d5 | 0.93 | 1.03 | 1.11 | PROXY | S7, S8 |
| o | 0.72 | 0.86 | 0.94 | PROXY | S2, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.40 | 0.99 | 2.04 | PROXY |
| F | 1.53 | 2.52 | 3.39 | ESTIMATE |
| C | 5.60 | 8.80 | 10.00 | PROXY |
| D | 6.70 | 8.86 | 10.00 | PROXY |

## Caveats
- a: The BLS occupation evidence is for broader food and beverage retail or retail occupations, not fruit and vegetable specialists.
- a: The estimate targets not-yet-automated work, so installed self-checkout is excluded even though BLS identifies it as a labor-saving technology.
- a: Task exposure is not the same as eliminable positions; many workers bundle exposed and non-exposed tasks.
- rho: BTOS retail trade is a much broader two-digit sector and measures adoption, not realized labor substitution.
- rho: Vendor use claims without audited labor-hour baselines would not resolve implementation quality.
- rho: The estimate excludes pricing, volume, and valuation effects.
- e: No source directly measures lens eligibility in the provided LMM firm population.
- e: The frozen firm-count estimate is margin-bridged and may itself misclassify firms near the band.
- e: Eligibility is lower for stores relying on undocumented family labor or the seller's personal buying relationships.
- s5: The Census owner-age statistic is for responding owners of employer businesses across all industries and reference year 2018.
- s5: Multiple owners per firm and firms with owners in different age bands make owner shares different from firm shares.
- s5: The estimate excludes closures and non-control reorganizations.
- q: FTC evidence covers food and beverage retailers broadly and pandemic-era conditions.
- q: Kroger is far larger and more diversified than the screened firms.
- q: The estimate treats demand loss separately in d5 and o and implementation difficulty separately in rho.
- d5: Food-at-home spending includes many products and outlets outside specialty produce retail.
- d5: Employment is an imperfect quantity indicator and can change with productivity.
- d5: Weather, crop supply, immigration, and local demographics can create wide store-level variation.
- o: Total-retail e-commerce penetration is not grocery or produce-specific.
- o: Operator requirement can migrate from a specialty store to a supermarket, platform, or fulfillment center; that channel loss is partly reflected in d5.
- o: The range concerns accountable-operator necessity, not the number of frontline jobs.

## Sources
- **S1** — [A Look at Jobs Paying Less Than $15.00 Per Hour](https://www.bls.gov/spotlight/2024/a-look-at-jobs-paying-less-than-15-00-per-hour/) (accessed 2026-07-22): BLS reports that cashiers and stockers/order fillers together made up nearly half of food and beverage retailer employment, grounding the broader occupation-mix proxy.
- **S2** — [Industry and occupational employment projections overview and highlights, 2024-34](https://www.bls.gov/opub/mlr/2026/article/industry-and-occupational-employment-projections-overview.htm) (accessed 2026-07-22): BLS identifies self-checkout as the main factor constraining cashier demand and online shopping as reducing in-store retail-salesperson needs.
- **S3** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Census BTOS reports retail-trade AI use around 14% and expected use around 17%, both below the national average, and lower adoption among the smallest firms.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Census reports that 51% of responding owners of employer businesses were age 55 or older in 2018, a broad succession-pressure proxy.
- **S5** — [FTC Releases Report on Grocery Supply Chain Disruptions](https://www.ftc.gov/news-events/news/press-releases/2024/03/ftc-releases-report-grocery-supply-chain-disruptions) (accessed 2026-07-22): FTC reports food and beverage retailer revenue at 7% over total costs in the first three quarters of 2023 and describes competitive and supply-chain pressures.
- **S6** — [The Kroger Co. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/56873/000110465926037723/kr-20260131x10k.htm) (accessed 2026-07-22): Kroger reports a 22.9% 2025 gross margin and describes price investment, cost savings, and intense grocery competition, supporting the pass-through proxy.
- **S7** — [As food price inflation slowed in 2024, inflation-adjusted food spending rebounded](https://www.ers.usda.gov/data-products/charts-of-note/111011) (accessed 2026-07-22): USDA ERS reports real food-at-home spending increased 1.8% in 2024 after declining 2.6% in 2023.
- **S8** — [Employees on nonfarm payrolls by industry sector and selected industry detail, seasonally adjusted](https://www.bls.gov/ces/data/employment-and-earnings/2024/table1a_202412.htm) (accessed 2026-07-22): BLS monthly 2024 payroll figures place fruit and vegetable retailers near 38,000-39,000 employees, indicating broadly stable recent activity.
- **S9** — [Quarterly Retail E-Commerce Sales, First Quarter 2026](https://www.census.gov/retail/eCommerce.html) (accessed 2026-07-22): Census reports e-commerce at 16.9% of adjusted total retail sales in first-quarter 2026, a broad proxy for digital/self-service channel migration.
