# 444240 — Nursery, Garden Center, and Farm Supply Retailers

*v5.1 Stage 1 research memo. Run `444240-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Recurring commercial accounts combine information-heavy ordering work with physical products and local fulfillment that still need an accountable operator.
**Weakness:** Most firms in the NAICS code are product retailers rather than outsourced-service providers, and no defensible LMM firm-count input is available.

## Business-model lens
- Included: Independent nursery, garden-center, and farm-supply retailers in the lower middle market that provide external commercial customers with recurring procurement, account management, scheduled replenishment, delivery coordination, or comparable repeat outsourced fulfillment.
- Excluded: Ordinary walk-in consumer product sales without an outsourced-service component; captive operations; product growers; landscaping contractors; wholesalers; shells; non-control financing vehicles; and firms outside the normalized EBITDA band.
- Customer and revenue model: Primarily recurring B2B accounts for landscapers, farms, property operators, and institutional buyers, monetized through merchandise margins plus delivery or account-service fees where charged; contracts are generally short and switching costs are modest.
- Deviation from default lens: The code combines consumer garden retail and commercial farm-supply models. The lens is narrowed to firms with recurring external-customer procurement or fulfillment responsibilities because product-only walk-in retail is not an outsourced service and would make the screen incoherent.

## Executive view
This is fundamentally a goods-retailing code, so only a minority of firms with recurring commercial procurement and fulfillment responsibilities fit the outsourced-service lens. In that minority, AI can reduce information and coordination labor, but physical handling and product accountability remain central.

## How AI changes the work
The clearest applications are product and agronomic knowledge retrieval, quote and order capture, replenishment suggestions, customer communications, demand forecasting, marketing, invoice matching, and routine reconciliation. Plant care, yard work, loading, delivery, chemical controls, shrink supervision, and nuanced advice limit substitution.

## Value capture
Fixed merchandise margins permit initial retention, but customers can compare common SKUs and switch suppliers. Durable capture depends on using savings to improve availability, delivery reliability, and advice rather than competing only on price.

## Firm availability
Broad owner-aging evidence implies succession activity, but no industry-specific transaction denominator exists. Eligibility is the larger uncertainty because ordinary consumer garden retail does not satisfy the recurring outsourced-service requirement and the frozen LMM firm count is unavailable.

## Demand durability
Physical demand for plants, feed, fertilizer, chemicals, and related replenishment should persist, with roughly flat real demand as a reasonable center. Weather, farm economics, housing activity, discretionary gardening, and direct or online channels widen the range.

## Risks and uncertainty
The principal risks are an overly broad interpretation of service eligibility, thin gross margins, seasonal working capital, perishable inventory, weather, regulated advice, shrink, large-chain and e-commerce competition, and poor small-company data. The strongest diligence need is firm-level evidence on commercial recurring revenue and labor deployment.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1448 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.18 | 0.28 | 0.4 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.55 | 0.7 | ESTIMATE | S3, S4 |
| e | 0.08 | 0.18 | 0.32 | ESTIMATE | S1 |
| s5 | 0.1 | 0.18 | 0.28 | PROXY | S5 |
| q | 0.35 | 0.55 | 0.72 | ESTIMATE | S1 |
| d5 | 0.88 | 0.98 | 1.1 | PROXY | S6, S7 |
| o | 0.72 | 0.86 | 0.95 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.36 | 0.89 | 1.62 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.34 | 8.43 | 10.00 | ESTIMATE |

## Caveats
- a: The available BLS occupation mix is for NAICS 4442 and includes outdoor power equipment retailers.
- a: O*NET task importance is not task time or wage weight and is not specific to horticulture or farm-supply selling.
- a: The estimate excludes automation already embedded in POS, online ordering, and inventory systems.
- rho: This is implementation judgment, not an observed industry adoption rate.
- rho: Small independent retailers may lack clean SKU, customer, and inventory data.
- rho: Self-checkout evidence demonstrates feasibility for transactions but not generative-AI implementation across the full exposed task set.
- e: No source measures the share of firms providing a qualifying outsourced service.
- e: NAICS classification follows primary activity, so meaningful ancillary service revenue can exist but remain invisible.
- e: The frozen firm-count input is missing, so even a bounded eligibility share cannot yield a defensible eligible-firm count.
- s5: The age evidence covers responding owners of employer businesses across all industries and dates to 2018.
- s5: Multiple-owner firms make owner shares different from firm shares.
- s5: No observed denominator of eligible firms or qualifying transfers is available.
- q: No source directly measures contractual pass-through of AI savings in this industry.
- q: Retention will differ sharply between commodity feed or fertilizer accounts and advice-heavy nursery sales.
- q: This range excludes volume effects and implementation difficulty.
- d5: The demand evidence is not six-digit, service-lens-specific, or constant-price.
- d5: Horticultural production includes products and channels outside retail and does not measure end-customer quantity.
- d5: Weather and local construction or farm cycles create substantial regional dispersion.
- o: This is a bounded judgment rather than a measured channel-retention share.
- o: Operator need is much higher for bulky, perishable, technical, or regulated goods than for standardized repeat SKUs.
- o: The range concerns continued accountable operation, not preservation of every current frontline task.

## Sources
- **S1** — [2022 NAICS Definition: 444240 Nursery, Garden Center, and Farm Supply Retailers](https://www.census.gov/naics/?details=444240&input=444240&year=2022) (accessed 2026-07-22): Defines the industry as retailing nursery, garden, and farm-supply products and distinguishes landscaping services, wholesale farm supplies, and growers.
- **S2** — [May 2024 OEWS Data Tables for Industry Charts](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest occupations in NAICS 4442, including 66,560 retail salespersons, 12,860 nursery workers, 12,820 cashiers, 10,540 material movers, 9,940 retail supervisors, and 9,320 general and operations managers.
- **S3** — [O*NET OnLine: Retail Salespersons](https://www.onetonline.org/link/details/41-2031.00) (accessed 2026-07-22): Lists retail-sales tasks spanning customer-needs discovery, product recommendation, transaction processing, merchandise preparation, answering questions, displays, inventory requisition, returns, and security.
- **S4** — [Occupational Outlook Handbook: Cashiers](https://www.bls.gov/ooh/sales/cashiers.htm) (accessed 2026-07-22): Projects cashier employment to decline 10 percent from 2024 to 2034 and attributes the decline to self-service checkout and increasing online sales, while describing remaining transaction and customer-assistance duties.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51 percent of responding owners of employer businesses were age 55 or older, 43 percent were 35 to 54, and 6 percent were 34 or younger, using the 2019 ABS with data year 2018.
- **S6** — [Monthly State Retail Sales: Building Material and Garden Equipment and Supplies Dealers in the United States](https://fred.stlouisfed.org/data/MSRSUSA444) (accessed 2026-07-22): Provides Census-sourced year-over-year nominal retail-sales changes for the broader NAICS 444 group, including alternating positive and negative monthly changes during 2024 through early 2026.
- **S7** — [U.S. Horticulture Operations Report $18.3 Billion in Sales](https://www.nass.usda.gov/Newsroom/2026/02-26-2026.php) (accessed 2026-07-22): Reports 23,060 U.S. horticulture operations and $18.3 billion of floriculture, nursery, and specialty-crop sales in 2024, documenting the continuing scale of the upstream physical product base.
