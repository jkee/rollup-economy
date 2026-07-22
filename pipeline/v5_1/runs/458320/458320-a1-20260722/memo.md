# 458320 — Luggage and Leather Goods Retailers

*v5.1 Stage 1 research memo. Run `458320-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** AI can reduce routine sales, warranty, customer-service, inventory, and corporate-account administration around a physical product flow.
**Weakness:** The eligible repeat-service population is extremely small, historically immaterial to revenue, and exposed to e-commerce and merchandise price transparency.

## Business-model lens
- Included: Lower-middle-market luggage and leather-goods retailers with a material repeat external service offering, such as managed corporate luggage programs, repeat warranty administration, personalization, maintenance coordination, or repair intake combined with new-product retail.
- Excluded: Ordinary one-off merchandise retail, product-only brand stores, pure e-commerce sellers, captive corporate procurement, repair establishments classified in NAICS 811430, used-goods retailers, and firms outside the normalized EBITDA band.
- Customer and revenue model: Consumers or organizational accounts pay mainly per product, with the small eligible subset also charging or embedding fees and margin for repeat personalization, warranty, maintenance coordination, repair intake, or managed replenishment.
- Deviation from default lens: The code is heterogeneous relative to the screen because nearly all activity is product retail. The lens is narrowed to retailers with a material repeat service relationship so isolated luggage or leather-goods purchases are not treated as outsourced services.

## Executive view
Luggage and leather-goods retail is overwhelmingly product-led, with only a very small historical service footprint. AI can streamline sales and account administration, but the recurring outsourced-service population is scarce and merchandise price competition limits retained benefit.

## How AI changes the work
Useful applications include product comparison, customer messaging, corporate-order administration, warranty triage, CRM, marketing, scheduling, inventory support, and bookkeeping. Physical inspection, customization, packaging, repair handoff, custody, and complex exceptions remain human, and stores still need customer-facing coverage.

## Value capture
Most savings arise inside merchandise economics where online comparison and promotions drive pass-through. Personalization and managed corporate relationships can preserve more value, while brand-controlled warranty rules can cap fees and shift savings to manufacturers or customers.

## Firm availability
Historical Census data found nonmerchandise receipts at only 5.1% of establishments and just 0.3% of industry sales, and current classification places repair specialists elsewhere. Broad owner-aging evidence suggests some transfers, but public data provide no defensible LMM firm count or current service-model share.

## Demand durability
Near-record airline passenger volumes support luggage use, yet durable products are replaced infrequently and store demand continues moving online. Warranty, repair intake, personalization, and corporate programs are more defensible than ordinary retail but still face self-service substitution.

## Risks and uncertainty
The largest risk is mistaking product sales or incidental service for a recurring outsourced-service model. Other weaknesses are the old service-incidence proxy, a combined-industry occupation mix, the ancestor-level labor ratio, the missing firm-count input, and absent real-volume data for the eligible service basket.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.12 | 0.21 | 0.32 | PROXY | S2, S3, S4 |
| rho | 0.29 | 0.47 | 0.65 | ESTIMATE | S3, S4 |
| e | 0.015 | 0.045 | 0.1 | PROXY | S1, S5, S6 |
| s5 | 0.12 | 0.2 | 0.29 | PROXY | S8 |
| q | 0.18 | 0.31 | 0.47 | ESTIMATE | S1, S5 |
| d5 | 0.84 | 0.95 | 1.07 | PROXY | S7, S9, S10 |
| o | 0.62 | 0.79 | 0.91 | ESTIMATE | S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.14 | 0.40 | 0.84 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 3.60 | 6.20 | 9.40 | ESTIMATE |
| D | 5.21 | 7.50 | 9.74 | ESTIMATE |

## Caveats
- a: OEWS combines jewelry, luggage, and leather-goods retailers and excludes self-employed workers.
- a: O*NET and occupational-requirements evidence is cross-retail rather than luggage-specific.
- a: The dataset labor ratio is only available at ancestor 44-45, uses 2024 wages over 2022 receipts, and is harmonized to the IPS basis; it may not represent this narrow service subset.
- rho: No source directly measures five-year implementation for service-bearing luggage retailers.
- rho: Implemented tools may improve response speed or avoid hiring rather than remove scheduled store labor.
- rho: Pricing and demand effects are excluded here.
- e: The quantitative proxy is from 2002 and is establishment-based, not conditional on LMM EBITDA.
- e: Incidental engraving or forwarding a warranty claim does not by itself establish a repeat outsourced-service model.
- e: The provided n input is a declared dataset gap and will be injected as MISSING; it was not replaced or estimated here.
- s5: The source is cross-industry and includes firms outside the lens and EBITDA band.
- s5: Planned transfers are not observed completed transfers.
- s5: Deaths without transferable operations and internal reorganizations are excluded.
- q: No direct study measures benefit pass-through in this narrow service subset.
- q: Corporate programs may retain more benefit than consumer product sales, while brand-paid warranty work may retain less.
- q: Volume loss is addressed in d5 and o rather than here.
- d5: Air passenger counts are a demand-driver proxy, not luggage or service transactions.
- d5: E-commerce data cover all retail and do not isolate luggage.
- d5: The estimate concerns the current service basket, not total consumer spending on luggage and leather goods.
- o: No source directly measures operator displacement for eligible luggage-retailer services.
- o: The estimate is conditional on year-five demand and does not repeat channel loss already reflected in d5.
- o: The small eligible population may contain very different corporate, warranty, personalization, and repair-intake models.

## Sources
- **S1** — [2022 NAICS Definition: 458320 Luggage and Leather Goods Retailers](https://www.census.gov/naics/?details=458320&input=458320&year=2022) (accessed 2026-07-22): Defines the industry as retailing new luggage, briefcases, trunks, and related leather items, establishing its product-retail nature.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 458300](https://www.bls.gov/oes/2023/may/naics4_458300.htm) (accessed 2026-07-22): Reports the combined industry's 124,200 employees, including 63.96% sales, 9.89% management, and 9.58% office and administrative support.
- **S3** — [O*NET OnLine: 41-2031.00 Retail Salespersons](https://www.onetonline.org/link/details/41-2031.00) (accessed 2026-07-22): Lists retail-sales tasks including needs discovery, recommendations, transactions, records, inventory, returns, delivery arrangements, and product explanation.
- **S4** — [BLS Occupational Requirements Survey: Retail Salespersons](https://www.bls.gov/ors/factsheet/retails-salesperson.htm) (accessed 2026-07-22): Reports that work was controlled by people for 99.1% of retail salespersons in 2024, telework was under 0.5%, and workers spent an average 84.3% of the day standing.
- **S5** — [U.S. Census Bureau 2022 Retail Trade Questionnaire: Luggage and Leather Goods Stores](https://bhs.econ.census.gov/ombpdfs2022/export/2022_RT-44832_su.pdf) (accessed 2026-07-22): Lists luggage and leather-goods retail activity and separately classifies footwear, luggage, handbag, briefcase, and leather-goods repair under 811430.
- **S6** — [2002 Economic Census: Clothing and Clothing Accessories Stores Industry Series](https://www2.census.gov/library/publications/economic-census/2002/retail-trade/industry-series/ec0244i20t.pdf) (accessed 2026-07-22): For 448320, reports 1,733 establishments and $1.554 billion total sales; 88 establishments reported $4.927 million of nonmerchandise receipts, equal to 0.3% of all-establishment sales, with labor, repair parts, and printing or engraving subcategories.
- **S7** — [Bureau of Transportation Statistics: December 2025 U.S. Airline Traffic Data](https://www.bts.gov/newsroom/december-2025-us-airline-traffic-data-down-26-same-month-last-year) (accessed 2026-07-22): Reports 81.2 million systemwide passengers in December 2025, seasonally adjusted enplanements 2.7% below the June 2024 all-time high, and a record 11.3 million international passengers for December.
- **S8** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 52.3% of employer businesses owned by people age 55 or older and 22% of employer-business owners planning to sell or transfer ownership within five years.
- **S9** — [U.S. Census Bureau Quarterly Retail E-Commerce Sales, First Quarter 2026](https://www.census.gov/retail/eCommerce.html) (accessed 2026-07-22): Reports adjusted e-commerce sales up 9.8% year over year versus 3.9% for total retail and e-commerce at 16.9% of retail sales.
- **S10** — [BLS Occupational Outlook Handbook: Retail Sales Workers](https://www.bls.gov/ooh/sales/retail-sales-workers.htm) (accessed 2026-07-22): Projects little or no overall retail-sales-worker employment change from 2024 to 2034 and states that online sales will limit physical stores and retail-sales-worker demand.
