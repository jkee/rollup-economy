# 445320 — Beer, Wine, and Liquor Retailers

*v5.1 Stage 1 research memo. Run `445320-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** A regulated, repeat-purchase physical product supports operator durability while AI improves inventory, purchasing, marketing, and back-office execution.
**Weakness:** Most labor is physical and customer-facing, and declining alcohol volume plus transparent-price channel competition limits both automation depth and retained economics.

## Business-model lens
- Included: US lower-middle-market operators of beer, wine, and liquor retail stores that repeatedly provide consumers with licensed product access, assortment, advice, order fulfillment, and related retail service.
- Excluded: State-operated or captive outlets, corporate chain units not independently transferable, passive license or real-estate holding vehicles, wholesalers, producers, bars and restaurants, and non-store businesses outside NAICS 445320.
- Customer and revenue model: Predominantly repeat consumer transactions at posted retail prices, with gross profit earned as the spread between merchandise sales and product cost; delivery, events, and memberships are secondary for most operators.
- Deviation from default lens: none

## Executive view
Beer, wine, and liquor retailing combines durable need for a licensed local operator with a limited but real AI opportunity in planning, administration, merchandising, and assisted selling. The core work is physical and customer-facing, so the opportunity is operational optimization rather than wholesale labor replacement. Transferable stores demonstrably trade, although the missing firm-count input prevents a defensible target count.

## How AI changes the work
AI can improve demand forecasting, purchasing, assortment, promotion design, product recommendations, scheduling, bookkeeping, and exception review. It can also assist associates with inventory and product knowledge. Cash handling, stocking, receiving, loss prevention, age verification, and in-person service constrain substitution, especially in smaller stores with weak system integration.

## Value capture
Posted-price retail lets an operator retain early cost and working-capital gains, but nationally branded products are easy to compare and larger competitors can price aggressively. Some benefit will therefore be competed into lower prices, better availability, broader assortment, or service. Local licensing scarcity and differentiated specialty inventory create the upper-case retention scenario.

## Firm availability
Liquor-store transaction comparables show that licensed locations with staff, inventory, leases, and customer traffic can transfer as going concerns. Broad small-business evidence points to aging owners and material five-year transfer intent, but closure is more common than sale across SMB exits. License, lease, owner-dependence, and chain-control filters reduce the eligible pool.

## Demand durability
The underlying product basket remains repeat-purchase and requires accountable physical fulfillment, but US alcohol volumes recently declined and moderation, affordability, health concerns, and alternative beverages are headwinds. RTDs and no/low products can preserve store occasions, while grocery, convenience, warehouse clubs, and digital delivery can take share from specialist operators.

## Risks and uncertainty
The largest uncertainties are the absent LMM firm count, lack of industry-specific ownership-transfer denominators, and the gap between retail-wide AI claims and independent-store implementation. State regulation can either shelter local stores or enable channel expansion by larger competitors. Thin margins, shrink, lease exposure, and a continued structural fall in alcohol consumption could outweigh administrative efficiencies.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0897 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.18 | 0.29 | 0.42 | PROXY | S2, S3 |
| rho | 0.3 | 0.48 | 0.65 | PROXY | S3 |
| e | 0.45 | 0.62 | 0.78 | ESTIMATE | S1, S6 |
| s5 | 0.1 | 0.16 | 0.25 | PROXY | S4, S5, S6 |
| q | 0.35 | 0.56 | 0.75 | ESTIMATE | S7, S9 |
| d5 | 0.75 | 0.9 | 1.02 | PROXY | S8, S9, S10 |
| o | 0.72 | 0.84 | 0.93 | ESTIMATE | S1, S2, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.19 | 0.50 | 0.98 | PROXY |
| F | — | — | — | MISSING |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 5.40 | 7.56 | 9.49 | ESTIMATE |

## Caveats
- a: The BLS table excludes self-employed owners, who may perform a broad mix of exposed administrative and non-exposed store tasks.
- a: NAICS 445300 is the direct four-digit predecessor/aggregate used by BLS for the 2022-code industry.
- a: Accenture's affected-hours concept includes augmentation and revenue-enhancing work, not only substitution or avoided hiring.
- rho: Investment intention does not establish successful implementation or labor removal.
- rho: State-by-state compliance, delivery, and age-verification rules create uneven feasibility.
- rho: Small-store data quality and vendor dependence are not measured by the source.
- e: The frozen firm-count input is missing, so this share cannot establish the number of eligible targets.
- e: Public transaction comparables are selected toward businesses that brokers considered sellable.
- e: Licenses and lease assignments may be transferable only with regulator or landlord approval.
- s5: Gallup covers all industries and includes gifts and rare public offerings in its transfer response.
- s5: Broker comparables show transactions but not the population at risk.
- s5: A license transfer without continuing operations may not be a qualifying transfer.
- q: There is no direct measurement of benefit retention after AI implementation in this industry.
- q: Local license scarcity can protect margins, while big-box, grocery, convenience, and delivery competition can sharply reduce retention.
- q: The mix of national brands versus differentiated wine and specialty products materially changes price transparency.
- d5: Recent annual declines may reflect macroeconomic conditions rather than a stable five-year trajectory.
- d5: Dollar sales can rise despite lower constant-quality volume because of inflation and mix.
- d5: The code excludes grocery, convenience, warehouse-club, and on-premise channels that compete for the same consumption occasions.
- o: State laws make the durable role of specialist stores highly geography dependent.
- o: This estimate treats channel migration away from eligible operators as loss of operator-required quantity even when alcohol consumption persists.
- o: Autonomous checkout may reduce labor without eliminating the licensed operating entity.

## Sources
- **S1** — [2022 NAICS Definition: Beer, Wine, and Liquor Retailers](https://www.census.gov/naics/?details=44&input=44&year=2022) (accessed 2026-07-22): Defines NAICS 445320 as establishments primarily retailing packaged alcoholic beverages and separates packaged retail from on-premise drinking places.
- **S2** — [Beer, Wine, and Liquor Retailers - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_445300.htm) (accessed 2026-07-22): Reports 173,760 jobs and the detailed industry occupation mix, including cashiers at 43.97%, retail salespersons at 20.03%, retail supervisors at 11.99%, and stockers/order fillers at 5.97%.
- **S3** — [Unleashing the Power of Generative AI in Retail](https://www.accenture.com/us-en/insights/retail/unleashing-power-generative-ai) (accessed 2026-07-22): Reports that 50% of retail working hours could be affected by generative AI and 93% of retail CxOs planned to increase AI investment over three to five years; identifies customer, inventory, forecasting, and supply-chain use cases.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of US employer-business owners planned to sell or transfer ownership within five years, versus 9% of nonemployers, from a fall 2024 survey.
- **S5** — [Navigating the great small business ownership transition](https://www.mckinsey.com/institute-for-economic-mobility/our-insights/the-great-ownership-transfer-a-new-era-of-business-stewardship) (accessed 2026-07-22): Estimates more than half of US small-business owners are over 55 and six million small businesses will exit ownership over the next decade; estimates 2022 SMB exits were 92% closures, 5% sales, and 3% transfers.
- **S6** — [Small Business Comparables Report - Liquor Store](https://www.bizbuysell.com/shared/listings/228/2286616/b8554bc4-b9b5-4082-bef3-09d0dc69687a.pdf) (accessed 2026-07-22): Lists numerous completed 2021-2024 NAICS 445310 liquor-store transactions, including stores with roughly $1.1 million to $10.7 million in annual sales in 2024, demonstrating transferability but not an industry transaction rate.
- **S7** — [Sales versus margins: alternative measures of output and productivity for retail trade](https://www.bls.gov/opub/mlr/2025/article/sales-versus-margins.htm) (accessed 2026-07-22): Reports packaged alcohol was 90% of NAICS 4453 sales in 2017, describes product homogeneity, and shows margin output moving with sales output; documents 2007-2022 employment and productivity trends.
- **S8** — [Economic pressures drive continued US beverage alcohol decline](https://www.theiwsr.com/insight/economic-pressures-drive-continued-us-beverage-alcohol-decline/) (accessed 2026-07-22): Reports US total beverage-alcohol volume fell 5% in 2025, with beer down 5%, wine down 6%, spirits down 4%, and RTDs down 1%; cost was cited by 31% of drinkers moderating consumption.
- **S9** — [WSWA's SipSource Releases 2024 Year-End Report](https://www.wswa.org/news/wswas-sipsource-releases-2024-year-end-report) (accessed 2026-07-22): Reports 2024 wine and spirits volume and revenue declines, changing moderation behavior, rapid RTD growth, and expansion in convenience-store alcohol accounts.
- **S10** — [U.S. Alcohol Market Report](https://www.vinetur.com/documentos/article/88940/U.S.%20Alcohol%20Market%20Report.pdf) (accessed 2026-07-22): Reports specialized beer, wine, and liquor store sales of $73.8 billion in 2024, up 2.4%, while documenting competition from supermarkets, warehouse clubs, and convenience stores.
