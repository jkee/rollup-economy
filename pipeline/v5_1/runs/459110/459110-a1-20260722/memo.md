# 459110 — Sporting Goods Retailers

*v5.1 Stage 1 research memo. Run `459110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Repeat institutional relationships and physical repair, fitting, rental, and customization preserve an accountable operator while administrative workflows offer selective AI savings.
**Weakness:** The eligible recurring-service subset is small and not directly measured inside a predominantly transactional retail NAICS code.

## Business-model lens
- Included: Lower-middle-market sporting-goods firms whose external-customer proposition includes repeat team or institutional supply, equipment fitting, decoration, repair, maintenance, or rental services alongside merchandise.
- Excluded: Pure transactional stores and e-commerce sellers, captive operations, product manufacturers and wholesalers, fitness facilities, shells, non-control financing vehicles, and firms without a recurring or repeat outsourced-service relationship.
- Customer and revenue model: Repeat sales and service to schools, leagues, clubs, institutions, and consumers, generally through merchandise margin plus service, rental, repair, fitting, or decoration fees; contracts and standing accounts may exist but much revenue remains order-based.
- Deviation from default lens: The NAICS population mixes predominantly transactional merchandise retailers with a much smaller set of repeat team/institutional dealers and repair, fitting, decoration, or rental operators. The lens is narrowed to the latter for business-model coherence because pure retail does not supply a recurring outsourced service.

## Executive view
Sporting-goods retail is mostly outside the recurring outsourced-service lens. The coherent target is the narrow subset of team and institutional dealers and specialist repair, rental, fitting, or decoration operators. Within that subset, AI can reduce quoting, order-entry, customer-service, marketing, purchasing, and administrative work, but physical service and relationship accountability limit substitution.

## How AI changes the work
The largest practical opportunities are product and inventory search, team-order configuration, quote generation, customer communications, order-status handling, scheduling, purchasing suggestions, marketing content, and routine bookkeeping. Physical fitting, repair, customization, stocking, loss prevention, and exception handling remain human-heavy, and the industry's dominant retail-sales workforce caps wage-weighted exposure.

## Value capture
Posted merchandise and service prices permit initial retention of labor savings, especially when automation improves turnaround or availability. Over time, transparent online comparison, direct-to-consumer brands, competitive bids, and fragmented local competition should share part of the benefit with customers through lower prices or better service.

## Firm availability
Only a small share of sporting-goods retailers appears eligible because ordinary product sales are transactional. Succession pressure is real across small business and a retail resale market exists, but public marketplace transactions skew far below the target EBITDA range and owner-dependent shops may not transfer cleanly.

## Demand durability
Record sports participation and recent industry growth support broadly stable to modestly growing real demand. The service-bearing basket should retain a local operator for repair, fitting, customization, rental, and institutional fulfillment, although product discovery, checkout, and some team ordering can move to self-service or vendor-direct channels.

## Risks and uncertainty
The main uncertainty is population fit: recurring-service operators are a small, poorly measured slice of a broad retail code and may be classified elsewhere. Tariffs, discretionary spending, weather, category fashion, inventory shrink, e-commerce, and vendor direct-to-consumer strategies can pressure volumes and margins. Evidence on LMM deal flow and actual AI labor savings is especially thin.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.24 | 0.34 | PROXY | S1, S2, S3 |
| rho | 0.35 | 0.52 | 0.68 | PROXY | S2, S3, S4 |
| e | 0.03 | 0.07 | 0.14 | PROXY | S1 |
| s5 | 0.08 | 0.14 | 0.22 | PROXY | S5, S6 |
| q | 0.42 | 0.58 | 0.74 | PROXY | S4 |
| d5 | 0.96 | 1.04 | 1.12 | PROXY | S7, S4 |
| o | 0.64 | 0.78 | 0.9 | PROXY | S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.23 | 0.51 | 0.94 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 8.40 | 10.00 | 10.00 | PROXY |
| D | 6.14 | 8.11 | 10.00 | PROXY |

## Caveats
- a: OEWS covers all employer establishments in NAICS 459110 rather than the narrowed recurring-service subset and excludes self-employed owners.
- a: Occupation shares are employment-weighted, while the primitive is wage-weighted; published industry mean wages inform but do not fully identify task-level wage exposure.
- a: Current automation already embedded in POS, e-commerce, and inventory systems is not separately measured.
- rho: Employment projections are national and ten-year, not direct five-year implementation measures.
- rho: DICK'S is much larger and better capitalized than the target population.
- rho: Some projected employment change reflects e-commerce and self-checkout rather than AI.
- e: Occupation presence does not reveal whether service revenue is recurring or whether a firm has normalized EBITDA of $1–10 million.
- e: Team dealers may be classified partly in wholesale trade or apparel decoration, creating boundary leakage.
- e: The frozen n input is missing, so eligible count cannot be derived from this share in the packet.
- s5: The Census age statistic is for responding owners across all employer industries and is dated to data year 2018.
- s5: BizBuySell is a marketplace sample, not a census, and its median retail transaction is below the target LMM band.
- s5: Owner age is not the same as intent to sell, and qualifying control transfers exclude closures and internal reorganizations.
- q: A large public retailer's competitive environment may not match local institutional accounts or specialist repair niches.
- q: The estimate separates demand volume and implementation difficulty but cannot fully isolate AI savings from merchandising and procurement gains.
- q: Customer concentration and rebid cadence vary substantially across schools, clubs, and consumers.
- d5: SFIA sales growth is not explicitly constant-price and covers manufacturers and wholesale categories beyond the lens.
- d5: DICK'S comparable sales include price, mix, digital subscriptions, and media revenue.
- d5: World Cup and Olympics effects may be temporary and category-specific.
- o: BLS projections cover occupations across industries and do not isolate sporting-goods service transactions.
- o: Vendor direct-to-consumer capabilities and remote fitting or customization technology could improve faster than assumed.
- o: The estimate applies to the narrowed service-bearing subset, not the full NAICS retail basket.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 459110 Sporting Goods Retailers](https://www.bls.gov/oes/2023/may/naics5_459110.htm) (accessed 2026-07-22): Industry employment of 302,960; occupation shares including sales 64.86%, retail salespersons 48.60%, cashiers 6.42%, office and administrative support 10.47%, customer service 2.80%, counter/rental clerks 0.62%, and installation, maintenance, and repair 5.94%.
- **S2** — [Occupational Outlook Handbook: Cashiers](https://www.bls.gov/ooh/sales/cashiers.htm) (accessed 2026-07-22): Cashier employment is projected to decline 10% from 2024 to 2034; BLS attributes the decline to technology such as self-service checkout and increasing online sales.
- **S3** — [Occupational Outlook Handbook: Customer Service Representatives](https://www.bls.gov/ooh/office-and-administrative-support/customer-service-representatives.htm) (accessed 2026-07-22): Customer-service-representative employment is projected to decline 5% from 2024 to 2034; duties include complaints, orders, questions, returns, billing, and account changes.
- **S4** — [DICK'S Sporting Goods, Inc. Form 10-K for fiscal year ended February 1, 2025](https://www.sec.gov/Archives/edgar/data/1089063/000108906325000012/dks-20250201.htm) (accessed 2026-07-22): Comparable sales rose 5.2% in fiscal 2024 after 2.6% in 2023; the company disclosed a customer-support-center workforce optimization, intense fragmented competition, real-time price comparison, online and vendor-direct channels, and continued digital and store investments.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The 2019 Annual Business Survey, data year 2018, found 51% of responding U.S. employer-business owners were age 55 or older, with explicit limits on representativeness.
- **S6** — [Retail Business Valuation Multiples and Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/retail-business/) (accessed 2026-07-22): Reported independent retail-business transactions had a 2025 median sale price of $273,647; the broader benchmark reports median revenue of $720,000, median owner earnings of $131,498, and median 165 days on market.
- **S7** — [Sports and Fitness Industry Association Press Releases](https://sfia.org/resource_categories/press-release/) (accessed 2026-07-22): SFIA reported 3.4% sporting-goods industry growth in 2025, record sports and fitness participation, and 3.7% year-over-year growth in wholesale sporting-goods sales to $130 billion, while identifying tariffs and costs as constraints.
