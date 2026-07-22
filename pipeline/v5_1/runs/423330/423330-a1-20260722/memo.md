# 423330 — Roofing, Siding, and Insulation Material Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423330-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.48 · L 0.36 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat contractor demand plus AI-addressable sales and branch administration layered on an operator-intensive physical fulfillment network.
**Weakness:** AI exposure is only indirectly measured, and scaled strategic consolidation may reduce the availability and affordability of transferable independent firms.

## Business-model lens
- Included: Independent US merchant wholesalers in the lower-middle-market band that repeatedly source, stock, quote, sell, and deliver nonwood roofing, siding, and insulation materials to contractors and other trade customers.
- Excluded: Manufacturers' sales branches, captive internal distribution, pure brokers without transferable operations, retailers, distributors outside the EBITDA band, and wood roofing or siding wholesalers classified elsewhere.
- Customer and revenue model: Repeat B2B product sales to roofing and exterior contractors, builders, and dealers, with value delivered through local inventory, product knowledge, credit, order accuracy, and job-site delivery; revenue is mainly product resale margin rather than a separately billed service fee.
- Deviation from default lens: none

## Executive view
This is a physical, repeat-purchase distribution business with a useful but bounded digital labor layer. AI can improve quoting, order administration, credit, lead prioritization, and planning, while the core local-inventory and job-site-delivery obligation remains human- and asset-accountable.

## How AI changes the work
The most implementable gains are copiloted inside sales, automated order intake, product and substitution lookup, collections prioritization, purchasing recommendations, and branch reporting. Warehouse handling, loading, driving, damage inspection, and relationship ownership remain much less substitutable.

## Value capture
Savings should initially remain with the distributor because service is bundled into product margin rather than billed by labor hour. Over five years, contractor negotiations, e-commerce transparency, supplier-direct moves, and competitor adoption share part of the gain with customers.

## Firm availability
The sector has many establishments and active building-products consolidation, but the available LMM pool is smaller after excluding manufacturer branches, concentrated or non-transferable owner businesses, and internal successions. Public deal counts are a weak denominator for the actual transfer probability.

## Demand durability
Aging buildings, reroofing cycles, weather damage, and insulation upgrades support the material basket, while rates and construction cycles create volatility. Distribution's operator role remains durable because bulky inventory, trade credit, substitutions, and timed delivery cannot be supplied entirely by software.

## Risks and uncertainty
The largest research gaps are 423330-specific occupation tasks, real shipment forecasts, and private-firm transfer cohorts. Supplier bypass, national-platform consolidation, ERP data quality, volatile material prices, customer concentration, and storm-driven demand can each overwhelm modest AI labor gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.065 | — | OBSERVED | — |
| n | — | 246 | — | ESTIMATE | — |
| a | 0.2 | 0.31 | 0.43 | PROXY | S3, S4 |
| rho | 0.28 | 0.45 | 0.62 | ESTIMATE | S4 |
| e | 0.64 | 0.77 | 0.88 | ESTIMATE | S1, S2 |
| s5 | 0.14 | 0.23 | 0.34 | PROXY | S4, S7 |
| q | 0.43 | 0.61 | 0.75 | PROXY | S2, S4 |
| d5 | 0.96 | 1.04 | 1.13 | PROXY | S5, S6 |
| o | 0.82 | 0.91 | 0.97 | ESTIMATE | S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.15 | 0.36 | 0.69 | ESTIMATE |
| F | 5.05 | 6.11 | 6.94 | ESTIMATE |
| C | 8.60 | 10.00 | 10.00 | PROXY |
| D | 7.87 | 9.46 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational mix is for all durable-goods merchant wholesalers and is from May 2022.
- a: The estimate concerns substitutable tasks or avoided hiring, not entire jobs.
- a: The supplied compensation ratio is a 2024-wage/2022-receipts hybrid and was harmonized to the IPS basis.
- rho: The public implementation example is a large distributor with more than 400 branches and may not transfer to LMM firms.
- rho: Implementation depends on clean product, customer, and inventory master data.
- rho: This excludes pricing, demand, and valuation effects.
- e: Census reports establishments or merchant-wholesaler firms, not lens eligibility among LMM firms.
- e: The provided firm count is an ESTIMATE derived from size-class receipts and an EBITDA-margin bridge.
- e: Eligibility can vary sharply with customer concentration and supplier authorizations.
- s5: Published distribution deal counts cover mixed end markets and deal sizes.
- s5: The McKinsey count includes targets in the Americas and Europe and emphasizes disclosed transactions.
- s5: No industry-specific owner-age or succession cohort was found.
- q: Gross margin is not a direct measure of benefit retention.
- q: Large national accounts may reprice savings faster than fragmented contractor accounts.
- q: Supplier-direct investment can intensify price competition independently of AI.
- d5: Construction spending is nominal and broader than this product basket.
- d5: NAHB's forecast is for all residential remodeling and is nominal.
- d5: Weather events can cause large regional year-to-year swings.
- o: The cited supplier-direct survey spans distribution categories rather than 423330.
- o: This primitive distinguishes elimination of the operator role from a change in operator ownership.
- o: Large contractors may adopt direct procurement faster than small local roofers.

## Sources
- **S1** — [Census Bureau Profile: 42333 Roofing, Siding, and Insulation Material Merchant Wholesalers](https://data.census.gov/profile/42333_-_Roofing%2C_Siding%2C_and_Insulation_Material_Merchant_Wholesalers?codeset=naics~42333) (accessed 2026-07-22): Defines the industry as nonwood roofing, siding, and insulation merchant wholesale distribution and reports 3,581 employer establishments in 2023.
- **S2** — [2022 Economic Census Wholesale Trade Gross Margin Profile](https://data.census.gov/table/ECNGRMARGPROF2022.EC2242GRMARGPROF) (accessed 2026-07-22): Reports 3,383 merchant-wholesaler firms and a 28.7% gross margin for NAICS 423330 in 2022.
- **S3** — [May 2022 OEWS: Merchant Wholesalers, Durable Goods](https://www.bls.gov/oes/2022/may/naics3_423000.htm) (accessed 2026-07-22): Provides the broader durable-goods wholesaler occupation mix, including wholesale/manufacturing sales representatives at 16.08% of employment and detailed office occupations.
- **S4** — [Where value is won and lost in distribution](https://www.mckinsey.com/industries/industrials/our-insights/where-value-is-won-and-lost-in-distribution) (accessed 2026-07-22): Documents distributor AI use in pricing, inventory, procurement, and commercial decisions; a 400-plus-branch building-material example; supplier-direct pressure; and 2025 distribution M&A counts and major building-products transactions.
- **S5** — [Monthly Construction Spending, May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-22): Reports May 2026 total construction spending 1.5% below May 2025 and first-five-month spending 2.7% below the same 2025 period.
- **S6** — [Remodeling Market Poised for Growth in 2025](https://www.nahb.org/news-and-economics/press-releases/2025/02/remodeling-market-poised-for-growth-in-2025) (accessed 2026-07-22): Attributes remodeling support to aging housing stock and forecasts nominal residential remodeling gains of 5% in 2025 and 3% in 2026.
- **S7** — [Distribution M&A Activity Rebounds in Q1 as Strategic Buyers Accelerate Dealmaking](https://distributionstrategy.com/2026/05/distribution-ma-activity-rebounds-in-q1-as-strategic-buyers-accelerate-dealmaking/) (accessed 2026-07-22): Reports 87 wholesale-distribution transactions in 2026 Q1 versus 74 in 2025 Q4, with private-equity-backed activity concentrated in industrial and building products.
