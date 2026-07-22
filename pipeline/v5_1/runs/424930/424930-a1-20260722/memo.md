# 424930 — Flower, Nursery Stock, and Florists' Supplies Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `424930-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.66 · L 0.60 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat ordering plus costly perishability creates a strong case for AI-assisted forecasting, substitution, and exception management around an operator that remains physically necessary.
**Weakness:** The low labor ratio and irreducible handling, delivery, and quality-control work limit how much AI exposure can become removable labor.

## Business-model lens
- Included: Independent merchant wholesalers repeatedly sourcing, receiving, conditioning, merchandising, holding, selling, and delivering cut flowers, nursery stock, plants, and florist supplies to external florists, garden centers, landscapers, event professionals, institutions, and retailers.
- Excluded: Grower-owned captive sales arms, vertically integrated retailer distribution centers, pure growers, pure retailers, non-inventory brokers, shells, and firms outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: Repeat B2B product sales, generally earning a wholesale spread and sometimes delivery or service fees; fresh-product value also depends on availability, grading, freshness, conditioning, cold-chain execution, credit, and rapid exception resolution.
- Deviation from default lens: none

## Executive view
The industry offers repeat B2B relationships and operationally rich workflows, but only a modest labor-to-receipts ratio and a large physical component. Demand appears durable rather than fast-growing. The most coherent targets are independent wholesalers with dense routes, diverse customers and suppliers, measurable shrink, repeat ordering, and systems capable of integrating AI-assisted commercial and inventory workflows.

## How AI changes the work
AI can improve supplier-list ingestion, product matching and substitutions, quote and order capture, event and holiday forecasting, purchasing, route prioritization, collections, and customer communications. It cannot replace receiving inspection, conditioning, stock movement, cold-chain custody, delivery, or accountable judgment about freshness and substitutions. Human approval and exception design remain central.

## Value capture
Value should arise through avoided administrative hiring, faster response, higher fill rates, lower spoilage, better purchasing, improved inventory turns, and fewer credits. Competitive product pricing will share some gains with customers; less visible improvements in shrink and working capital should be more retainable.

## Firm availability
The frozen band estimate is large, and floral wholesaling remains fragmented enough to support sourcing. Transferability depends on moving supplier and customer relationships, credit lines, facilities, refrigeration, leases, route density, and operating knowledge beyond the selling owner.

## Demand durability
Flowers and plants serve recurring holidays, life events, landscaping, garden, retail, and institutional uses. Recent producer sales were essentially flat while nominal consumer spending grew, implying a stable real-demand center with cyclical and weather-driven variation. Imported supply and direct retail programs may change the channel without eliminating physical handling.

## Risks and uncertainty
Key risks are spoilage, seasonality, weather and disease, import and tariff shocks, customer concentration, retailer direct sourcing, facility and cold-chain dependence, and weak item master data. The code also mixes fresh flowers, nursery stock, and hardgoods, whose economics and automation potential differ materially.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.13 | — | OBSERVED | — |
| n | — | 467 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.34 | PROXY | S1, S2 |
| rho | 0.3 | 0.5 | 0.68 | ESTIMATE | S2, S3 |
| e | 0.65 | 0.82 | 0.92 | ESTIMATE | S4 |
| s5 | 0.11 | 0.21 | 0.33 | ESTIMATE | S5 |
| q | 0.43 | 0.63 | 0.8 | ESTIMATE | S3 |
| d5 | 0.88 | 1.02 | 1.15 | PROXY | S4, S6 |
| o | 0.76 | 0.88 | 0.95 | ESTIMATE | S3, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.22 | 0.60 | 1.20 | ESTIMATE |
| F | 5.69 | 7.08 | 7.98 | ESTIMATE |
| C | 8.60 | 10.00 | 10.00 | ESTIMATE |
| D | 6.69 | 8.98 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS staffing pattern pools several unrelated nondurable wholesale industries.
- a: O*NET task importance is not task time, wage weight, current automation, or end-to-end substitutability.
- a: The frozen labor ratio mixes 2024 wages with 2022 receipts and is harmonized separately to the IPS basis.
- rho: No direct study measures AI implementation in independent 424930 firms.
- rho: Weather shocks, biological variation, and holiday peaks can reduce model reliability exactly when operational stakes are highest.
- e: SAF's operation count is an industry estimate with a different, unstated size scope.
- e: The frozen 467-firm count is margin-bridged rather than an observed list of qualifying firms.
- s5: The transaction source covers all nondurable wholesaling and reports only deals known to its marketplace.
- s5: There is no exact eligible-firm denominator or observed owner-age distribution.
- q: No public study measures pass-through of productivity benefits for floral wholesalers.
- q: Capture varies sharply between spot cut-flower sales, recurring florist accounts, nursery programs, hardgoods, and large retail contracts.
- d5: Consumer spending is nominal and includes retail channels and seeds outside the exact wholesale construct.
- d5: USDA floriculture sales include both retail and wholesale producer sales and omit some nursery and supply categories.
- d5: Tariffs, exchange rates, plant disease, and weather could materially alter real volume within five years.
- o: The operator-required share differs between fresh cut flowers, nursery stock, potted plants, and nonperishable florist supplies.
- o: Consolidation into national importers or retailer distribution centers still preserves an operator but can eliminate the independent local wholesaler.

## Sources
- **S1** — [BLS Data Tables for OEWS Industry Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): For the broader 4241/4247/4249 group, identifies the largest occupations including 66,350 nontechnical sales representatives, 56,820 heavy-truck drivers, 45,270 material movers, 25,980 stockers/order fillers, 15,980 office clerks, and 15,630 customer-service representatives.
- **S2** — [O*NET OnLine: Sales Representatives, Wholesale and Manufacturing, Except Technical and Scientific Products](https://www.onetonline.org/link/details/41-4012.00) (accessed 2026-07-22): Lists wholesale-sales tasks including answering product and availability questions, recommending products, quoting terms and delivery dates, preparing contracts and orders, monitoring markets, reporting, checking stock, and forwarding orders.
- **S3** — [USDA Agricultural Marketing Service: Specialty Crops Market News](https://www.ams.usda.gov/market-news/fruits-vegetables) (accessed 2026-07-22): Explains that reporters gather and publish current wholesale-market information on price, volume, quality, and condition using direct contacts with sales personnel, suppliers, brokers, and buyers.
- **S4** — [Society of American Florists: Floral Industry Facts](https://safnow.org/trends-statistics/floral-industry-facts/) (accessed 2026-07-22): Reports BEA-derived nominal spending on flowers, seeds, and potted plants of $71.0 billion in 2024 versus $68.9 billion in 2023, estimates 400 floral wholesale operations, and reports 11,262 domestic producers and $6.71 billion of floriculture sales in 2024.
- **S5** — [BizBuySell 2026 First-Quarter Insight Report: Full-Year 2025 Data Tables](https://www.bizbuysell.com/news/bizbuysell-2026-first-quarter-insight-report/) (accessed 2026-07-22): Reports 16 nondurable-goods wholesaler/distributor transactions for 2025, with median sale price $525,000, median revenue $1,301,710, and median cash flow $225,000.
- **S6** — [USDA NASS 2024 Floriculture Crops Highlights](https://www.nass.usda.gov/Publications/Highlights/2026/2024-floriculture-highlights.pdf) (accessed 2026-07-22): Reports 11,262 producers and $6.71 billion of floriculture sales in 2024, less than 1% above 2023; defines included fresh cut flowers, potted plants, bedding and garden plants, perennials, greens, and propagative material and states that sales include retail and wholesale.
- **S7** — [USDA NASS: U.S. Horticulture Operations Report $18.3 Billion in Sales](https://www.nass.usda.gov/Newsroom/2026/02-26-2026.php) (accessed 2026-07-22): Reports $18.3 billion in 2024 floriculture, nursery, and specialty-crop sales across 23,060 U.S. horticulture operations.
