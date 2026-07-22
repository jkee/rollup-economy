# 424590 — Other Farm Product Raw Material Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `424590-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.74 · L 0.39 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Document-heavy, specification-sensitive recurring trades offer practical AI assistance around physical commodities.
**Weakness:** The code's extreme product heterogeneity and own-account merchant economics make eligibility, demand, and normalized EBITDA unusually uncertain.

## Business-model lens
- Included: Lower-middle-market merchants of storable, nonliving farm raw materials such as raw cotton, hemp and other fibers, hides and pelts, leaf tobacco, raw nuts, oil kernels, raw spices, and raw sugar, where recurring sourcing, aggregation, grading, market access, documentation, and logistics are provided to external counterparties by a transferable team.
- Excluded: Live chicks, bees, horses, and mules; bovine semen; sod; cannabis businesses whose legality or product model prevents a comparable national screen; captive procurement units; pure speculative positions without repeat external customers; owner-only books that cannot transfer; shells; and financing vehicles.
- Customer and revenue model: Merchants generally buy raw materials on their own account from farms or assemblers and resell to processors, manufacturers, exporters, or other wholesalers. The recurring service embedded in the spread is aggregation, quality matching, inventory and price-risk management, documentation, and delivery coordination rather than a separately billed service fee.
- Deviation from default lens: NAICS 424590 combines living-animal, highly perishable, regulated cannabis, and storable industrial or food raw-material models. The lens keeps storable nonliving raw-material merchants because their workflows, risks, and revenue model can be assessed coherently; the narrowing is based on business-model incompatibility rather than attractiveness.

## Executive view
This residual NAICS code is too heterogeneous to screen as one operating model. Within storable nonliving farm raw materials, recurring sourcing, quality matching, documentation, and logistics create useful AI workflows, but low labor intensity, commodity-spread economics, and uncertain service eligibility limit the addressable benefit.

## How AI changes the work
AI can synthesize market and quality data, draft quotes and contracts, extract trade documents, prioritize counterparties, answer routine status questions, and flag inventory or shipment exceptions. Physical sampling, quality disputes, price-risk decisions, supplier relationships, working-capital control, and final accountability remain human-led.

## Value capture
Merchant spreads avoid automatic contractual pass-through, but benchmark transparency and competitive sourcing should return a meaningful share of savings to producers and processors. Retention is better where the merchant provides scarce inventory, trusted grading, credit, or complex export execution.

## Firm availability
The frozen firm count is large but likely contains many ineligible product and operating models. Broad wholesale transaction evidence supports some availability, yet qualifying control-transfer incidence and the transferability of relationship books are not observed for this lens.

## Demand durability
Cotton has modest projected volume growth and hemp is expanding from a volatile base, while hides and tobacco are weaker. Physical quality, inventory, title, finance, and delivery preserve operator demand, but standardized data and direct channels can reduce traditional intermediation.

## Risks and uncertainty
The dominant risks are unknown commodity weights, an EBITDA-band estimate based on broad distributor margins, commodity cycles and trade policy, legal fragmentation in cannabis, working-capital needs, inventory losses, customer and supplier concentration, and direct-channel substitution.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0476 | — | OBSERVED | — |
| n | — | 381 | — | ESTIMATE | — |
| a | 0.22 | 0.35 | 0.48 | PROXY | S2, S3, S7 |
| rho | 0.38 | 0.58 | 0.75 | PROXY | S2, S3, S7 |
| e | 0.15 | 0.3 | 0.48 | ESTIMATE | S1, S4 |
| s5 | 0.08 | 0.16 | 0.27 | ESTIMATE | S8, S9 |
| q | 0.28 | 0.46 | 0.65 | ESTIMATE | S4, S7 |
| d5 | 0.86 | 1.04 | 1.25 | PROXY | S5, S6, S10 |
| o | 0.68 | 0.83 | 0.93 | ESTIMATE | S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.16 | 0.39 | 0.69 | PROXY |
| F | 2.76 | 4.76 | 6.30 | ESTIMATE |
| C | 5.60 | 9.20 | 10.00 | ESTIMATE |
| D | 5.85 | 8.63 | 10.00 | ESTIMATE |

## Caveats
- a: No public occupation distribution or time-on-task study was found for this six-digit code or narrowed lens.
- a: The frozen compensation-to-receipts ratio combines 2024 wages with 2022 receipts and is harmonized to an IPS basis; high commodity pass-through can suppress the apparent labor intensity.
- rho: The evidence is occupational and cotton-specific rather than a measured adoption rate across the narrowed multi-commodity lens.
- rho: Cybersecurity, data entitlements, and integration with warehouse and trade-finance systems can delay deployment.
- e: Public data do not reveal the six-digit code's firm or receipt mix by commodity.
- e: The frozen 381-firm LMM estimate is margin-bridged using a broad distributor margin; commodity turnover and inventory gains can make sales a poor EBITDA proxy.
- s5: BizBuySell observations skew toward smaller publicly marketed businesses and are far broader than this lens.
- s5: Workforce age is not owner age, sale intent, or evidence that customer and supplier relationships will transfer.
- q: No source directly measures AI-benefit pass-through in these commodities.
- q: Commodity price and inventory gains can overwhelm small operating-cost changes and obscure true retention.
- d5: Commodity weights inside NAICS 424590 are unknown, making any blend highly uncertain.
- d5: USDA long-term projections were completed in October 2024, while the hemp and trade snapshots are newer but short-horizon and volatile.
- d5: Underlying commodity volume can grow even if producers and processors bypass merchants.
- o: Operator need varies materially by commodity and by domestic versus export transaction.
- o: Software may reduce local headcount while preserving only a thin accountable merchant layer; this primitive measures operator presence, not labor intensity.

## Sources
- **S1** — [2022 NAICS Definition: 424590 Other Farm Product Raw Material Merchant Wholesalers](https://www.census.gov/naics/?details=424590&input=424590&year=2022) (accessed 2026-07-22): Defines the residual farm-raw-material merchant category and lists examples including live chicks, hemp, horses and mules, hides, raw cotton, nuts, pelts, leaf tobacco, sod, wool, cocoa beans, sugar, spices, and cannabis, establishing product heterogeneity.
- **S2** — [Wholesale and Manufacturing Sales Representatives](https://www.bls.gov/ooh/sales/wholesale-and-manufacturing-sales-representatives.htm) (accessed 2026-07-22): Lists prospecting, customer communication, needs analysis, price and availability responses, negotiation, contracts, orders, and follow-up; says online wholesale mostly complements face-to-face selling and AI/chatbots may limit employment growth.
- **S3** — [Purchasing Managers, Buyers, and Purchasing Agents](https://www.bls.gov/ooh/business-and-financial/purchasing-managers-buyers-and-purchasing-agents.htm) (accessed 2026-07-22): Describes sales-record and inventory analysis, supplier identification, demand monitoring, contracts, and ordering; says procurement tasks will continue to automate and may use AI while humans remain needed for supply-chain and negotiation work.
- **S4** — [2022 Economic Census Frequently Asked Questions - Wholesale](https://www.census.gov/programs-surveys/economic-census/year/2022/about/faq/faq-wholesale.html) (accessed 2026-07-22): Defines a merchant wholesaler as buying merchandise on its own account and reselling it, and a farm-products assembler as purchasing directly from farmers; clarifies the spread-based operating model.
- **S5** — [USDA Agricultural Projections to 2034](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/110966/OCE-2025-1.pdf) (accessed 2026-07-22): Projects upland-cotton production from 15.4 million bales in 2026/27 to 15.8 million in 2031/32 and exports from 13.4 million to 14.1 million, while domestic mill use remains flat at 1.79 million bales.
- **S6** — [National Hemp Report, April 16, 2026](https://esmis.nal.usda.gov/sites/default/release-files/795862/hempan26.txt) (accessed 2026-07-22): Reports 2025 U.S. hemp value of $739 million, up 64 percent; open-field planted acreage up 9 percent, harvested acreage up 34 percent, fiber production up 11 percent, and grain production up 112 percent from 2024.
- **S7** — [Cotton Classing Services](https://www.ams.usda.gov/services/grading/cotton-classing) (accessed 2026-07-22): States that USDA grades every U.S. cotton bale, issues bale-level electronic data used in marketing and sourcing, and measures color, trash, micronaire, length, uniformity, and strength with instrument and visual controls.
- **S8** — [Wholesale/Distribution Business Valuation Multiples & Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/wholesale-distribution/) (accessed 2026-07-22): Reports observed sales of wholesale and distribution businesses during 2021-2025, including annual median prices and a five-year median revenue of $1.379 million and owner earnings of $236,484; the population is broader and smaller than this lens.
- **S9** — [Firms in Production Sectors and Northern States Have Some of the Highest Shares of Older Workers](https://www.census.gov/library/stories/2025/12/older-workers.html) (accessed 2026-07-22): Reports that over 40 percent of wholesale-trade employment in 2022 was at firms where at least one-quarter of workers were over 55, up from 14 percent in 2000; this concerns workforces, not owners.
- **S10** — [Outlook for U.S. Agricultural Trade: May 2026](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/114207/AES-136.pdf) (accessed 2026-07-22): Forecasts fiscal-2026 export values of $0.6 billion for hides, skins, and furs versus $0.727 billion in 2025; $4.8 billion for cotton versus $4.910 billion; $11.0 billion for tree nuts versus $10.535 billion; and $1.6 billion for tobacco and products versus $1.5 billion.
