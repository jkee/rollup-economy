# 339920 — Sporting and Athletic Goods Manufacturing

*v5.1 Stage 1 research memo. Run `339920-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.96 · L 1.66 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Rich product, order, and channel data can improve design-to-market speed and planning across a repeat product business with growing end demand.
**Weakness:** Import exposure and retailer bargaining can divert efficiency gains away from domestic manufacturers, while heterogeneous product cycles make demand difficult to underwrite.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly supplying sporting and athletic goods other than apparel and footwear, including fitness, golf, fishing, playground, protective, skating, skiing, racquet, team-sport, aquatic, and related equipment to external brands, retailers, institutions, distributors, or direct customers.
- Excluded: Apparel and footwear makers, bicycle and boat manufacturers, firearms and ammunition makers, pure retailers or wholesalers, brand licensors without US manufacturing operations, captive workshops, shells, inactive entities, non-control financing vehicles, and firms outside the normalized EBITDA band.
- Customer and revenue model: Manufacturers sell products and replacement items through wholesale, institutional, brand, retailer, and direct channels. Revenue is order and unit based, with repeat seasonal assortments, replenishment, replacement, and program purchases rather than subscriptions.
- Deviation from default lens: none

## Executive view
Sporting-goods manufacturing offers a credible AI layer in product development, merchandising, forecasting, customer service, and administration, but remains anchored in physical production and testing. Demand has grown in real terms, while import exposure, retailer power, product heterogeneity, and discretionary cycles limit visibility and benefit retention.

## How AI changes the work
AI can accelerate concepts, product variants, technical and marketing content, demand planning, sourcing analysis, compliance-document review, customer support, and order processing. Physical engineering, prototypes, athlete or user testing, materials, tooling, assembly, durability, impact and load tests, and final quality release remain human and equipment intensive.

## Value capture
Branded, proprietary, direct, or high-performance manufacturers can convert efficiency into faster launches, better availability, fewer returns, and margin. Private-label and commodity suppliers face seasonal bids, retailer concentration, transparent prices, common tools, and imports, so they are likely to share much of pure labor savings.

## Firm availability
The frozen population implies a meaningful candidate pool, but pure importers, brand licensors, retailers, and adjacent-product companies can contaminate classification. Transferability also depends on channel durability, product liability, supplier control, working capital, and whether innovation resides beyond the founder.

## Demand durability
Real spending on sporting and recreational goods rose through 2024, supporting continued demand from fitness, outdoor recreation, school and youth sports, and replacement. Post-pandemic normalization, fads, discretionary sensitivity, used goods, and imports warrant a broad range rather than extrapolation.

## Risks and uncertainty
The NAICS code mixes very different products and safety profiles, and direct evidence on AI adoption, transfers, and retained benefit is thin. Product failures, recalls, seasonality, tariffs, inventory corrections, customer concentration, and supplier dependence can overwhelm workflow savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2754 | — | OBSERVED | — |
| n | — | 220 | — | ESTIMATE | — |
| a | 0.18 | 0.32 | 0.47 | PROXY | S1, S2 |
| rho | 0.28 | 0.47 | 0.65 | PROXY | S3, S6, S7 |
| e | 0.64 | 0.8 | 0.91 | ESTIMATE | S1 |
| s5 | 0.15 | 0.26 | 0.37 | PROXY | S1, S5 |
| q | 0.34 | 0.53 | 0.71 | ESTIMATE | S4, S6 |
| d5 | 0.93 | 1.09 | 1.24 | PROXY | S1, S4 |
| o | 0.85 | 0.94 | 0.99 | ESTIMATE | S1, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.56 | 1.66 | 3.37 | PROXY |
| F | 4.98 | 6.19 | 6.95 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.91 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The exact-industry workforce data are from 2002 and predate substantial outsourcing and ecommerce change.
- a: Current BLS occupation data pool highly heterogeneous miscellaneous manufacturers.
- a: AI exposure varies sharply between branded design-heavy goods and commodity fabricated equipment.
- rho: Anthropic API use is not a representative manufacturing sample.
- rho: BLS injury incidence concerns worker safety, not product-validation burden or AI adoption.
- rho: Implementation varies by digital maturity and product safety criticality.
- e: This is a bounded judgment rather than an observed firm-level audit.
- e: Brand owners and importers may be classified as manufacturers despite limited domestic production.
- e: Seasonality, pandemic-era demand, inventory corrections, and channel concentration complicate EBITDA normalization.
- s5: The owner-age proxy is all-industry, response-based, and has data year 2018.
- s5: Historic fragmentation does not establish current transfer flow.
- s5: Owner age is not sale intent and founder dependence can reduce transferability.
- q: No source directly measures retention of AI-created benefit.
- q: Pricing power differs greatly across product categories and channels.
- q: Retail concentration and imports can force productivity gains into lower wholesale prices.
- d5: The BEA category is broader than NAICS 339920 and includes imported goods.
- d5: Pandemic and reopening effects may inflate recent growth.
- d5: Demand differs across fitness, golf, fishing, playground, protective, winter, and team-sport categories.
- o: No direct source measures the future share requiring the current US operator type.
- o: Imports can replace the lens operator without reducing end-user demand.
- o: Operator need differs between complex safety-rated equipment and simple accessories.

## Sources
- **S1** — [Sporting and Athletic Goods Manufacturing: 2002](https://www2.census.gov/library/publications/economic-census/2002/manufacturing-reports/industry-series/ec0231i339920.pdf) (accessed 2026-07-22): Reports 2,158 companies, 2,233 establishments, 62,457 employees, and 41,416 production workers, with product classes spanning fishing, golf, playground, gymnasium and exercise, and other sporting goods.
- **S2** — [Miscellaneous Manufacturing - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics3_339000.htm) (accessed 2026-07-22): Broader current occupation mix reports production at 48.81%, office and administrative support at 11.06%, sales at 4.34%, and art and design at 2.06% of employment.
- **S3** — [Anthropic Economic Index report: Uneven geographic and enterprise AI adoption](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) (accessed 2026-07-22): Reports 77% automation patterns in first-party API business usage and identifies organized contextual information and data modernization as constraints on sophisticated enterprise deployment.
- **S4** — [Real Personal Consumption Expenditures: Other Sporting and Recreational Goods](https://fred.stlouisfed.org/series/DORIRX1A020NBEA/) (accessed 2026-07-22): BEA annual real PCE via FRED increased from $307.629 billion chained 2017 dollars in 2021 to $347.273 billion in 2024, with intermediate values of $307.690 billion in 2022 and $326.195 billion in 2023.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Census 2019 Annual Business Survey graphic for data year 2018 shows 51% of responding employer-business owners age 55 or older, 43% age 35 to 54, and 6% age 34 or younger.
- **S6** — [Incidence Rates of Nonfatal Occupational Injuries and Illnesses by Industry, 2024](https://www.bls.gov/web/osh/table-1-industry-rates-national.htm) (accessed 2026-07-22): Reports a total recordable case incidence rate of 2.8 per 100 full-time workers for sporting and athletic goods manufacturing in 2024, supporting the persistence of physical operations and safety controls.
- **S7** — [Miscellaneous Manufacturing: NAICS 339](https://www.bls.gov/iag/tgs/iag339.htm) (accessed 2026-07-22): Explains that sporting and athletic goods use varied manufacturing processes and that processes for tennis racquets, golf balls, and other miscellaneous products differ significantly, supporting implementation heterogeneity.
