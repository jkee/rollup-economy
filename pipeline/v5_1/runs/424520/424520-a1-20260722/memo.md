# 424520 — Livestock Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `424520-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.90 · L 0.31 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat, regulated livestock transactions create automatable administrative work around a durable physical flow.
**Weakness:** Only a minority of firms clearly fit the outsourced-service lens, and commodity throughput makes both eligibility and LMM sizing unusually uncertain.

## Business-model lens
- Included: Lower-middle-market cattle, hog, sheep, and goat merchant wholesalers, livestock auction-market merchants, and commission buyers with recurring producer, feedlot, or packer relationships and transferable operating teams.
- Excluded: Horse and mule wholesalers; feedlots; livestock producers; captive purchasing units; one-person relationship books that cannot transfer; pure speculative inventory traders without repeat customer service; and shells or financing vehicles.
- Customer and revenue model: The coherent service is repeated livestock sourcing, matching, price discovery, physical handling, settlement, and compliance for producers and downstream buyers. Revenue is earned either as an inventory spread on principal transactions or as commissions and related market fees.
- Deviation from default lens: The code mixes own-account commodity merchants with auction and commission intermediaries. The lens keeps firms where recurring intermediation is a meaningful outsourced service and excludes pure inventory speculation because service eligibility, billing, and transferability otherwise would not be comparable.

## Executive view
Livestock merchants combine information-rich trading administration with a physical, regulated, relationship-intensive core. AI can reduce office work, but only a subset of the NAICS population resembles a recurring outsourced service and much of the economic throughput is commodity value rather than service revenue.

## How AI changes the work
Near-term applications are market-report synthesis, lead and lot matching, customer communication, contract and document preparation, order entry, reconciliation triage, and compliance support. Animal assessment, auction calling, yard work, final price negotiation, credit judgment, and payment accountability remain human-led.

## Value capture
Savings should initially accrue to the operator because principal spreads and auction commissions are not explicit labor-cost reimbursement. Transparent prices and competitive local alternatives create meaningful renewal and spread compression, so durable retention is only moderate.

## Firm availability
The frozen population estimate is sizable but likely overinclusive for this lens. Transferable targets are concentrated among recurring auction, commission, clearing, and relationship-led dealers with teams and systems; broad wholesale sale evidence shows a market exists, but livestock-specific transfer incidence is not observed.

## Demand durability
USDA projects roughly mid-single-digit growth in cattle and hog inventories from 2026 to 2031. Physical animals, settlement risk, weighing, custody, and compliance preserve operator demand, though direct producer-packer contracting and digital venues can bypass traditional merchants.

## Risks and uncertainty
The largest uncertainties are business-model mix inside the code, the revenue-to-EBITDA bridge in a high-throughput commodity sector, owner dependence, cattle-cycle volatility, direct-channel migration, disease and trade shocks, and the absence of livestock-specific task, succession, and pass-through data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0447 | — | OBSERVED | — |
| n | — | 243 | — | ESTIMATE | — |
| a | 0.2 | 0.32 | 0.45 | PROXY | S2, S3 |
| rho | 0.35 | 0.55 | 0.72 | PROXY | S2, S3, S4 |
| e | 0.18 | 0.32 | 0.5 | ESTIMATE | S1, S4 |
| s5 | 0.08 | 0.16 | 0.28 | ESTIMATE | S5, S6 |
| q | 0.35 | 0.52 | 0.7 | ESTIMATE | S4, S7 |
| d5 | 0.92 | 1.06 | 1.15 | PROXY | S8 |
| o | 0.74 | 0.86 | 0.94 | ESTIMATE | S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.13 | 0.31 | 0.58 | PROXY |
| F | 2.42 | 4.18 | 5.72 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.81 | 9.12 | 10.00 | ESTIMATE |

## Caveats
- a: No public occupation-by-task distribution was found for this six-digit industry.
- a: The frozen compensation-to-receipts input uses 2024 wages over 2022 receipts and is harmonized to an IPS basis; it may understate labor intensity in commission agencies and overstate it in high-throughput principal traders.
- rho: BLS evidence concerns national occupations and a ten-year employment outlook, not adoption in this industry or the five-year primitive.
- rho: Implementation depends on data quality and connectivity at rural sale facilities.
- e: No public census separates commission, auction, and pure own-account models within the six-digit code.
- e: The frozen LMM firm count is an ESTIMATE margin-bridged from size-class receipts; commodity throughput can make revenue a weak proxy for EBITDA and may materially misclassify firms.
- s5: Workforce age is not owner age and does not establish sale intent.
- s5: BizBuySell covers listed and reported small-business sales, is much broader than livestock wholesaling, and provides no eligible-firm denominator.
- s5: A prominent stockyard sale driven partly by land value illustrates transfer pressure but is not an incidence estimate.
- q: No source directly measures pass-through of AI-enabled savings in livestock intermediation.
- q: Retention differs sharply between commission auctions and principal merchants exposed to volatile inventory spreads.
- d5: USDA projections were completed in October 2024 and can miss disease, drought, trade, feed-cost, and cattle-cycle shocks.
- d5: Production and inventory are imperfect proxies for the number and complexity of wholesale transactions.
- o: The estimate may be high if large producers and packers accelerate direct contracting.
- o: The regulated entity may become a thin accountable layer over software, preserving operator need while reducing labor and local market count.

## Sources
- **S1** — [2022 NAICS Definition: 424520 Livestock Merchant Wholesalers](https://www.census.gov/naics/?details=424520&input=424520&year=2022) (accessed 2026-07-22): Defines the industry as merchant wholesale distribution of livestock other than horses and mules, with cattle, hogs, goats, sheep, and livestock auction markets among the examples or index entries.
- **S2** — [Wholesale and Manufacturing Sales Representatives](https://www.bls.gov/ooh/sales/wholesale-and-manufacturing-sales-representatives.htm) (accessed 2026-07-22): Lists prospecting, customer contact, needs analysis, price and availability questions, negotiation, contracts, order submission, and follow-up; says online wholesale mostly complements face-to-face selling and AI/chatbots may limit employment growth.
- **S3** — [Purchasing Managers, Buyers, and Purchasing Agents](https://www.bls.gov/ooh/business-and-financial/purchasing-managers-buyers-and-purchasing-agents.htm) (accessed 2026-07-22): Describes sales-record and inventory analysis, supplier identification, demand monitoring, contracts, and ordering; says procurement tasks will continue to automate and may use AI while humans remain needed for complex supply chains and negotiation.
- **S4** — [Dealer, Market Agency Buying on Commission, and Clearing Agency](https://www.ams.usda.gov/rules-regulations/packers-and-stockyards-act/regulated-entities/dealer) (accessed 2026-07-22): Distinguishes own-account livestock dealers, commission buyers, and clearing agencies and documents registration, bonding, next-business-day payment, accurate-scale, annual-report, and records-inspection responsibilities.
- **S5** — [Firms in Production Sectors and Northern States Have Some of the Highest Shares of Older Workers](https://www.census.gov/library/stories/2025/12/older-workers.html) (accessed 2026-07-22): Reports that over 40 percent of wholesale-trade employment in 2022 was at firms where at least one-quarter of workers were over 55, up from 14 percent in 2000; this is workforce, not owner, evidence.
- **S6** — [Wholesale/Distribution Business Valuation Multiples & Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/wholesale-distribution/) (accessed 2026-07-22): Reports sales of wholesale and distribution businesses during 2021-2025, including annual median sale prices, a five-year median revenue of $1.379 million, median owner earnings of $236,484, and median sold earnings multiple of 2.68.
- **S7** — [How to Comply with the Bond Requirement](https://www.ams.usda.gov/rules-regulations/packers-and-stockyards-act/regulated-entities/how-to-comply-bond-requirement) (accessed 2026-07-22): Explains that livestock dealers and commission or clearing agencies require bonds protecting payment obligations, with formulas tied to two business days of activity and a $10,000 minimum, illustrating transaction accountability that cannot simply be removed with labor savings.
- **S8** — [USDA Agricultural Projections to 2034](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/110966/OCE-2025-1.pdf) (accessed 2026-07-22): Projects cattle inventory from 86.1 million head in 2026 to 91.592 million in 2031 and hog inventory from 77.1 million to 81.428 million; also provides beef and pork production, disappearance, export, and price paths.
