# 459510 — Used Merchandise Retailers

*v5.1 Stage 1 research memo. Run `459510-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Repeat, data-rich listing, pricing, support, and settlement workflows can be improved while managed resale demand continues to expand.
**Weakness:** Only a small, unmeasured subset of used-merchandise retailers fits the recurring outsourced-service lens, and the eligible LMM firm count is missing.

## Business-model lens
- Included: U.S. lower-middle-market operators in NAICS 459510 that repeatedly perform managed resale or consignment for external sellers, including intake, valuation, merchandising, sale, fulfillment, and seller settlement.
- Excluded: Pure inventory-owning used-goods stores, one-off dealers, charities without transferable commercial operations, owner-hobby antique shops, software-only marketplaces, pawnshops, motor-vehicle dealers, and firms outside the roughly $1-10 million normalized EBITDA band.
- Customer and revenue model: The qualifying model earns repeat consignment commissions, seller fees, or a managed-resale spread from households, estates, brands, and institutions while also completing retail transactions with end buyers.
- Deviation from default lens: The code is heterogeneous between ordinary goods retail and managed resale/consignment. The lens retains only firms whose repeated intake-to-sale workflow constitutes an outsourced service to external sellers; ordinary inventory-owning retailers are excluded because they do not satisfy the fixed service lens.

## Executive view
The qualifying opportunity is much narrower than the NAICS label: most used-merchandise businesses sell goods rather than provide an outsourced service. Managed consignment and resale operators do have repeat seller workflows, growing demand in important categories, and automatable digital work, but physical item handling and trust remain central.

## How AI changes the work
AI can draft listings from images and notes, enrich attributes, recommend prices, match inventory to demand, answer routine buyer and seller questions, localize marketing, and automate bookkeeping and settlement exceptions. It is less able to remove intake, cleaning, condition grading, authentication, display, packing, pickup, and relationship-heavy sourcing.

## Value capture
Transaction pricing gives an operator room to retain initial labor savings, especially when convenience, curation, supply access, and trust differentiate the service. Retention erodes as sellers compare payout rates, buyers compare identical or similar goods across platforms, and competitors deploy the same tools.

## Firm availability
A visible market exists for independent retail-business sales, but most observed transactions are far below the stated EBITDA band. The harder constraint is eligibility: only managed resale or consignment models meet the outsourced-service lens, and no denominator-based count or transfer rate exists for that subset.

## Demand durability
Secondhand apparel research indicates strong category growth and wider consumer adoption, while affordability and sustainability support reuse more broadly. The current service basket will still need custody, inspection, fulfillment, and accountability, though peer-to-peer platforms and brand-owned programs can bypass independent operators.

## Risks and uncertainty
The principal uncertainties are the tiny and unmeasured eligible share, the missing LMM firm-count input, broad proxy occupation data, and a category-biased demand forecast. Inventory uniqueness limits standardization, fraud and authenticity errors can create losses, and online marketplaces can capture both sellers and buyers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.14 | 0.22 | 0.32 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.55 | 0.7 | ESTIMATE | S3, S4 |
| e | 0.01 | 0.03 | 0.08 | ESTIMATE | S1 |
| s5 | 0.12 | 0.2 | 0.3 | ESTIMATE | S5 |
| q | 0.3 | 0.48 | 0.65 | ESTIMATE | S1, S4 |
| d5 | 0.95 | 1.12 | 1.28 | PROXY | S4 |
| o | 0.58 | 0.72 | 0.85 | ESTIMATE | S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.20 | 0.49 | 0.91 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 6.00 | 9.60 | 10.00 | ESTIMATE |
| D | 5.51 | 8.06 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS industry group combines NAICS 4594 and 4595 and excludes self-employed workers.
- a: The task mapping is judgmental and measures technical exposure, not realized five-year implementation.
- a: The supplied compensation-to-receipts ratio is LOW quality, measured at ancestor 44-45, uses 2024 wages over 2022 receipts, and is harmonized to the IPS basis; it may not represent managed resale labor intensity.
- rho: ThredUp is a large technology-led apparel operator and may implement faster than independent LMM firms.
- rho: No source measures implemented substitution for the qualifying six-digit population.
- e: There is no observed share of LMM firms using a managed-resale or consignment model.
- e: The finalizer will inject MISSING for the declared dataset gap in n, so the absolute eligible-firm count is unavailable.
- s5: BizBuySell reports sold-business characteristics rather than a transfer rate against the eligible-firm population.
- s5: Small retail transaction data skew toward much smaller firms: the five-year median sold-business owner earnings were $131,498, far below the lens EBITDA floor.
- q: The code spans commission, donated-inventory, auction, and owned-inventory models with different pass-through mechanics.
- q: Competitive response over five years is not directly observed.
- d5: The source is commissioned by a major apparel resale platform and is not a whole-industry forecast.
- d5: The published forecast is market value, not constant-price, constant-quality quantity.
- d5: The projection ends in 2030, one year before the five-year horizon from 2026.
- o: Operator requirement differs sharply by category: luxury authentication and bulky goods need more intervention than books or standardized apparel.
- o: The estimate concerns quantity still requiring an accountable qualifying operator, not whether individual tasks remain manual.

## Sources
- **S1** — [2022 NAICS 459510 — Used Merchandise Retailers](https://www.census.gov/naics/?details=459510&input=459510&year=2022) (accessed 2026-07-22): Official industry boundary: used merchandise, antiques, secondhand goods, and used-merchandise auctions; illustrative and cross-reference detail includes consignment shops and exclusions.
- **S2** — [May 2023 OEWS — Miscellaneous Store Retailers (4594 and 4595 only)](https://www.bls.gov/oes/2023/may/naics4_4590A1.htm) (accessed 2026-07-22): Observed adjacent-industry occupation mix and wages, including 61.34% sales, 9.27% office and administrative support, 11.22% material moving, and 6.49% management employment shares.
- **S3** — [Labor market impacts of AI: A new measure and early evidence](https://www.anthropic.com/research/labor-market-impacts) (accessed 2026-07-22): Task-based theoretical and observed AI exposure methodology; customer service and data entry are among highly covered occupations; actual coverage remains below theoretical capability and physical tasks remain beyond reach.
- **S4** — [ThredUp's 14th Annual Resale Report](https://newsroom.thredup.com/news/thredup-14th-resale-report) (accessed 2026-07-22): GlobalData-derived U.S. apparel resale forecast to $78.8 billion by 2030, $23.3 billion incremental value, survey methodology, social discovery, AI use in pricing and authentication, and managed resale operating context.
- **S5** — [Retail Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/retail-business/) (accessed 2026-07-22): Reported retail business transaction and financial benchmarks for 2021-2025, including mostly independent local ownership and median sold-business owner earnings of $131,498.
