# 456120 — Cosmetics, Beauty Supplies, and Perfume Retailers

*v5.1 Stage 1 research memo. Run `456120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Repeat beauty replenishment plus rich product, loyalty and transaction data makes recommendation, marketing and inventory work readily AI-assistable.
**Weakness:** Most industry revenue is transactional product retail that can migrate to transparent online channels, leaving few service-led firms in the target EBITDA band.

## Business-model lens
- Included: US independent and regional specialty beauty retailers in the $1-10 million normalized-EBITDA band whose external customers repeatedly use product-replenishment, professional beauty-supply, consultation, loyalty, omnichannel fulfillment, or in-store beauty-service offerings.
- Excluded: National chains, manufacturer-owned or captive distribution, pure product brands and manufacturers, salons without meaningful beauty retail, very small owner-operated shops below the EBITDA band, one-off kiosks, and passive or non-control vehicles.
- Customer and revenue model: Consumers and beauty professionals buy replenishment and discretionary products at posted retail prices; qualifying operators add repeat advisory, loyalty, ordering, delivery, education, or in-store services, typically paid per transaction rather than under long-term contracts.
- Deviation from default lens: This NAICS is primarily transactional merchandise retail, not outsourced service. To keep the screen coherent, it is narrowed to independent and regional operators where repeat replenishment or professional supply is paired with an ongoing advisory, fulfillment, loyalty, education, or in-store service relationship; pure one-off retail is excluded.

## Executive view
Beauty retail contains AI-friendly recommendation, marketing, planning and service workflows, but the frozen lens fits only a narrow slice of this transactional industry. Regional professional-supply and service-led concepts can have recurring customer relationships; ordinary stores and national chains do not qualify. The main issue is not technical feasibility but whether a differentiated operator can retain savings amid transparent prices and rapid channel migration.

## How AI changes the work
AI can personalize product discovery, draft campaigns, answer routine questions, forecast SKU demand, automate purchase suggestions, support training, triage service, and coordinate omnichannel fulfillment. Large chains already use personalized recommendations and virtual try-on, reducing the remaining greenfield opportunity. Associates still matter for demonstration, tactile matching, trust, merchandising, shrink control, physical stock and hands-on services.

## Value capture
Retailers initially keep administrative and selling-efficiency gains because prices are not contractually cost-plus. Over time, duplicate products across marketplaces, mass merchants, brand-direct sites and specialty stores force savings into promotions, customer acquisition, convenience and service. Private label, exclusives, professional access and distinctive in-store services improve retention.

## Firm availability
Single-store beauty shops are visible in the small-business sale market, but most appear below the target EBITDA band. National specialists are too large. The investable middle consists of scarce regional groups, professional-supply distributors with stores, and differentiated omnichannel or service-led operators; the lack of owner-level EBITDA and transfer data is material.

## Demand durability
Beauty units grew in both prestige and mass channels in 2025, supporting modest real growth rather than decline. Demand remains discretionary and category trends can reverse quickly. The operator-required portion is less durable than the product need because routine research and replenishment can move to marketplaces or brand-direct channels, while professional supply, discovery, immediate pickup and hands-on services remain stickier.

## Risks and uncertainty
Key risks are a lens that fits only a small part of the NAICS, a missing defensible LMM firm count, national-chain proxies, consumer trade-down, trend and inventory obsolescence, shrink, supplier and brand concentration, marketplace competition, high digital-acquisition costs, and AI recommendations that damage trust. A poor target is a regional store group whose apparent loyalty is promotion-driven and whose advisory experience customers can replicate online.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.2 | 0.31 | 0.42 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S4 |
| e | 0.02 | 0.07 | 0.15 | ESTIMATE | S1, S4, S8 |
| s5 | 0.08 | 0.15 | 0.25 | PROXY | S6, S7 |
| q | 0.28 | 0.45 | 0.62 | PROXY | S4, S8 |
| d5 | 0.98 | 1.11 | 1.25 | PROXY | S5 |
| o | 0.38 | 0.57 | 0.73 | PROXY | S2, S4, S5, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.65 | 1.16 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 5.60 | 9.00 | 10.00 | PROXY |
| D | 3.72 | 6.33 | 9.12 | PROXY |

## Caveats
- a: O*NET is an occupation-level source and does not measure the industry wage mix or AI exposure.
- a: Ulta is a national-scale operator excluded from the lens and is more digitized than typical LMM firms.
- a: The provided labor ratio is an ancestor 44-45 estimate with a 2024-wage/2022-receipts mismatch and IPS harmonization.
- rho: Large-chain digital capabilities may not be affordable or portable to LMM operators.
- rho: Revenue uplift is excluded; this primitive counts only implemented labor substitution or avoided hiring.
- rho: Conventional self-checkout and warehouse automation are excluded unless AI is the enabling layer.
- e: The frozen firm-count input is a declared gap and will be injected as MISSING, so this share cannot support a firm-count estimate.
- e: Public-company examples show viable models but not the distribution of private-firm EBITDA.
- e: Ancillary salon or advisory activity may be reported inconsistently across establishments.
- s5: Marketplace transactions are voluntarily reported and skew far smaller than the lens.
- s5: Listings demonstrate sale intent, not completed qualifying control transfers.
- s5: Beauty M&A data often mix manufacturers, brands, distributors, salons and retailers.
- q: Ulta is larger, more diversified and more vertically advantaged than the lens population.
- q: Private-label, professional-only and salon-service mixes can retain materially different shares.
- q: This is retention of implemented gross benefit, not merchandise gross margin.
- d5: Circana's mass channel extends well beyond this NAICS and its prestige channel includes non-specialty sellers.
- d5: One strong year is a weak basis for a five-year range.
- d5: Unit measures do not fully hold quality or pack size constant.
- o: A digital transaction still has an operator, but often not an operator of the lens's kind.
- o: Hands-on salon services are ancillary within a retail NAICS and may be classified elsewhere when primary.
- o: Category behavior differs sharply among fragrance, color cosmetics, hair, skincare and professional products.

## Sources
- **S1** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Official 456120 classification and its 2022 combination of legacy cosmetics-store, electronic-shopping and direct-selling activity.
- **S2** — [O*NET OnLine: Retail Salespersons](https://www.onetonline.org/link/details/41-2031.00) (accessed 2026-07-22): Retail tasks include needs discovery, recommendations, questions, demonstrations, transaction processing, records, inventory monitoring, purchasing and delivery arrangements; the work remains highly customer-facing.
- **S3** — [O*NET OnLine: Stockers and Order Fillers](https://www.onetonline.org/link/summary/53-7065.00) (accessed 2026-07-22): Physical retail tasks include receiving, storing, issuing, shelf filling, order filling, price marking and display setup.
- **S4** — [Ulta Beauty, Inc. Form 10-K for Fiscal Year Ended January 31, 2026](https://www.sec.gov/Archives/edgar/data/1403568/000110465926035243/ulta-20260131x10k.htm) (accessed 2026-07-22): Workforce, loyalty, personalized recommendations, virtual try-on, omnichannel behavior, replenishment systems, store and salon model, competition, margin, expense and supplier concentration evidence.
- **S5** — [Circana: US Prestige and Mass Beauty Retail Deliver Positive Performance in 2025](https://www.globenewswire.com/news-release/2026/02/10/3235596/0/en/US-Prestige-and-Mass-Beauty-Retail-Deliver-a-Positive-Performance-in-2025-Circana-Reports.html) (accessed 2026-07-22): Prestige beauty dollar and unit sales rose 4% in 2025; mass dollars rose 5% and units 2%, with category and online-replenishment detail.
- **S6** — [BizBuySell Insight Report](https://www.bizbuysell.com/insight-report/) (accessed 2026-07-22): Marketplace scope of about 50,000 listed and recently sold businesses and current small-business transaction-market methodology.
- **S7** — [BizBuySell Beauty Supply Stores for Sale](https://www.bizbuysell.com/beauty-supply-stores-for-sale/) (accessed 2026-07-22): Direct evidence that standalone, wholesale/retail and hybrid beauty-supply businesses are marketed for transfer, without proving completion or lens eligibility.
- **S8** — [Sally Beauty Holdings, Inc. Form 10-K for Fiscal Year Ended September 30, 2025](https://www.sec.gov/Archives/edgar/data/1368458/000119312525280122/sbh-20250930.htm) (accessed 2026-07-22): Specialty and professional beauty retail model and competition based on price, assortment, service, location, inventory, digital checkout and delivery.
