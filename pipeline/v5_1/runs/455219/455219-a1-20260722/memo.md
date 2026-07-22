# 455219 — All Other General Merchandise Retailers

*v5.1 Stage 1 research memo. Run `455219-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Frequent essential-product demand combined with automatable decision and administrative workflows in a repeat-purchase store model.
**Weakness:** Fragmented classification and weak evidence on the count and transfer rate of genuinely independent, transferable LMM operators.

## Business-model lens
- Included: US lower-middle-market operators of fixed-location general, variety, and small-box value stores that repeatedly retail broad lines of new merchandise and associated checkout, fulfillment, return, and customer-support services to external consumers.
- Excluded: General-merchandise auction businesses, pure online or mail-order sellers without a store operating model, used-goods-led merchants, locations captive to public or very large chains, shells, and non-control financing vehicles.
- Customer and revenue model: Mostly repeat but non-contractual consumer merchandise transactions at posted or promoted prices, often emphasizing convenience, value, household essentials, and limited assortments across many categories; ancillary delivery, advertising, or other services may supplement merchandise margin.
- Deviation from default lens: Narrowed to fixed-location general, variety, and small-box value stores because 455219 also spans new-and-used general merchandise, auction-led retail, and online selling; those models have materially different labor, customer-acquisition, inventory, and transfer economics and cannot support one coherent screen.

## Executive view
Independent fixed-location general and variety stores have a real but bounded AI opportunity in ordering, pricing, promotion, scheduling, service, checkout, and administration. Essential and convenience-led demand can be durable, yet physical store coverage, stocking, shrink control, and intense price competition limit both labor substitution and retained economics.

## How AI changes the work
Lean store teams combine service, checkout, stocking, and management, so AI is most useful as an assistant and avoided-hiring mechanism rather than as a fully autonomous replacement. The large-scale reversal of self-checkout in response to shrink and service concerns is a concrete warning that labor-saving technology must be evaluated on whole-store economics.

## Value capture
There is no contractual pass-through on ordinary merchandise sales, but value positioning and transparent alternatives push savings toward lower prices, promotions, staffing, or better availability. Local convenience, private labels, and differentiated assortment can preserve a moderate retained share.

## Firm availability
The narrowed format is more compatible with LMM ownership than department stores or supercenters, but chain branches, owner dependence, leases, inventory quality, and informal controls reduce transferability. The missing LMM firm-count input and lack of a closed-deal denominator remain major evidence gaps.

## Demand durability
Household essentials and convenient local trips support roughly stable real quantity, while chain evidence shows durable traffic and same-store sales. Independents can still lose share to dollar chains, mass merchants, and online sellers, and surviving physical-store volume generally continues to need an accountable merchant.

## Risks and uncertainty
The NAICS code spans materially different models, occupation evidence is broader than the lens, and the main operating comparator is a giant chain. The case deteriorates if buying power is too weak, leases or supplier terms are nontransferable, shrink absorbs automation savings, or chain and online competition drive sustained real volume loss.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.2 | 0.33 | 0.46 | PROXY | S2, S4 |
| rho | 0.3 | 0.48 | 0.63 | ESTIMATE | S4, S5 |
| e | 0.28 | 0.52 | 0.72 | ESTIMATE | S1, S4 |
| s5 | 0.09 | 0.16 | 0.24 | ESTIMATE | — |
| q | 0.42 | 0.6 | 0.76 | ESTIMATE | S4 |
| d5 | 0.92 | 1.02 | 1.14 | PROXY | S4, S6 |
| o | 0.84 | 0.92 | 0.97 | ESTIMATE | S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.24 | 0.64 | 1.18 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.73 | 9.38 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source combines department stores, supercenters, warehouse clubs, and other general-merchandise retailers.
- a: Dollar General is a very large chain rather than an LMM operator.
- a: Cross-trained small-store roles make occupation-to-task mapping especially imprecise.
- rho: Self-checkout is an automation analogue rather than a pure generative-AI deployment.
- rho: Large-chain integration difficulty can differ from smaller operators in both directions.
- rho: The estimate assumes vendor tools integrate with common small-retailer POS, accounting, inventory, and scheduling systems.
- e: The injected LMM firm-count input is missing, so the share cannot be converted into a defensible eligible target count.
- e: The NAICS code changed in 2022 and spans store and nonstore methods, increasing classification noise.
- e: The large-chain comparator demonstrates format feasibility but not the prevalence of independent LMM ownership.
- s5: No industry-specific closed-deal series with a defensible denominator was found.
- s5: Distressed retail events frequently end in liquidation rather than transfer of a going concern.
- s5: Owner age alone would not establish a qualifying transfer.
- q: The narrowed population ranges from rural general stores to urban value stores, with different pricing power.
- q: Private-label mix and local competition materially affect retention.
- q: This is discounted retention of an implemented gross benefit, not the accounting gross-margin rate.
- d5: A large public chain's growth may reflect share capture from independents rather than category growth.
- d5: Nominal sales and same-store sales are not constant-quality quantity measures.
- d5: The narrowed lens excludes auction and pure-online segments present in the NAICS code.
- o: The self-checkout evidence comes from a large chain and reflects shrink as well as customer preference.
- o: Online orders can still be fulfilled by the same store operator, so digital adoption is not automatically operator displacement.
- o: Volume loss belongs in d5 and is not double-counted here.

## Sources
- **S1** — [2022 NAICS Definition: 455219 All Other General Merchandise Retailers](https://www.census.gov/naics/?details=455&input=455&year=2022) (accessed 2026-07-22): Defines 455219 as retailers of new and used general merchandise other than department stores, warehouse clubs, superstores, and supercenters, with no merchandise line predominating; supports the heterogeneity finding and lens.
- **S2** — [May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates: NAICS 455000 General Merchandise Retailers](https://www.bls.gov/oes/2023/may/naics4_455000.htm) (accessed 2026-07-22): Reports the adjacent-industry occupation mix, including 43.63% sales, 8.41% office support, and 33.00% transportation/material-moving employment; supports the task-exposure proxy.
- **S3** — [Cashiers: Occupational Outlook Handbook](https://www.bls.gov/ooh/sales/cashiers.htm) (accessed 2026-07-22): Projects cashier employment to decline 10% from 2024 to 2034 and attributes the decline partly to self-service checkout and online sales; supports automation context.
- **S4** — [Dollar General Corporation 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/29534/000155837025003413/dg-20250131x10k.htm) (accessed 2026-07-22): Describes small-box staffing and low-price economics, AI and machine-learning integration, 82.2% consumables mix, historical same-store-sales durability, and 2024 sales, traffic, margin, inventory, and labor results.
- **S5** — [Dollar General Corporation Form 10-Q for Quarter Ended May 3, 2024](https://www.sec.gov/Archives/edgar/data/29534/000155837024008742/dg-20240503x10q.htm) (accessed 2026-07-22): Reports conversion of some or all self-checkout registers to assisted checkout in about 12,000 stores to address shrink and improve customer and associate experience; informs implementation and operator-required judgments.
- **S6** — [Quarterly Retail E-Commerce Sales, First Quarter 2026](https://www.census.gov/retail/eCommerce.html) (accessed 2026-07-22): Reports retail e-commerce growth of 9.8% year over year versus 3.9% for total retail and a 16.9% e-commerce share; supports channel-substitution and demand caveats.
