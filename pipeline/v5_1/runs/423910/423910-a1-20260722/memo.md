# 423910 — Sporting and Recreational Goods and Supplies Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.24 · L 0.51 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Catalog-heavy recurring and seasonal B2B workflows are AI-addressable against a broadly durable participation-driven demand base.
**Weakness:** Independent-wholesaler necessity and benefit retention are vulnerable to brand-direct commerce, marketplaces, and highly transparent product pricing.

## Business-model lens
- Included: Lower-middle-market sporting and recreational goods wholesalers serving external retailers, teams, schools, clubs, gyms, institutions, facilities, and specialty dealers through repeat or seasonal replenishment, bulk orders, account-specific catalogs, parts, warranty, and fulfillment support.
- Excluded: Manufacturers and brand owners whose economics are primarily product IP, direct-to-consumer retailers, captive sales branches, brokers, one-off marine pleasure-craft or major-equipment sellers without repeat supply activity, financing vehicles, and nontransferable owner-personal operations.
- Customer and revenue model: Product gross margin on bulk and seasonal B2B orders, retailer replenishment, institutional contracts, and specialty dealer supply, with negotiated price lists, credit terms, freight, multi-location fulfillment, returns, warranty, parts, and occasional repair or service agreements.
- Deviation from default lens: none

## Executive view
Sporting-goods wholesaling offers automatable catalog, order, forecasting, and account-service work, while participation supports end demand. The harder issue is whether an independent intermediary remains necessary and can retain savings in a transparent, brand-controlled, increasingly digital channel. A viable target should have repeat institutional or specialty-dealer accounts, differentiated assortment, credit and logistics value, and low dependence on one brand or product fad.

## How AI changes the work
AI can ingest purchase orders, match SKUs and variants, enrich catalogs, forecast seasonal demand, allocate inventory, draft campaigns, recommend replenishment, handle routine service, and assist returns and warranty triage. Physical picking, bulky freight, equipment assembly or repair, product demonstrations, key-account negotiation, and relationship-based assortment selling remain operator-led.

## Value capture
Faster service and lower administrative cost initially accrue to the wholesaler, but digital experience is becoming table stakes and comparable branded goods invite price competition. Benefits will pass through rapidly in open-catalog products. Exclusive distribution, scarce inventory, institutional contracts, custom team programs, credit, complex freight, and parts or warranty support offer the strongest protection.

## Firm availability
Aging owners and an active wholesale transaction market imply opportunities, while sports-sector investor activity confirms strategic interest. Transferability is fragile where a brand authorization, founder relationship, or trend-sensitive inventory position drives value. It is stronger where accounts, pricing, demand planning, and vendor relationships are diversified and institutionalized. Only a minority-to-middle share of the broad code likely meets the recurring lens.

## Demand durability
Participation and industry sales remain healthy, supporting continued equipment and supply demand. However, category demand is fad-prone and cyclical, and nominal growth is affected by tariffs and price mix. The physical basket endures more strongly than the current channel: brands, marketplaces, and retailers can internalize procurement and fulfillment, reducing the share requiring an independent merchant wholesaler.

## Risks and uncertainty
The NAICS code mixes sporting goods, firearms, billiards, pools, bicycles, fitness equipment, playground products, and marine pleasure craft. Demand, regulation, capital intensity, and reorder cadence vary sharply. Brand loss, retailer concentration, DTC expansion, e-commerce price transparency, tariffs, seasonal inventory, returns, fads, counterfeit goods, and working capital can overwhelm labor savings. Weak SKU and variant data can also block implementation.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0746 | — | OBSERVED | — |
| n | — | 927 | — | ESTIMATE | — |
| a | 0.22 | 0.35 | 0.48 | PROXY | S1, S2, S3, S4 |
| rho | 0.3 | 0.49 | 0.66 | PROXY | S3, S5, S6 |
| e | 0.22 | 0.4 | 0.58 | ESTIMATE | S7, S8 |
| s5 | 0.1 | 0.18 | 0.28 | PROXY | S9, S10, S11 |
| q | 0.2 | 0.36 | 0.55 | PROXY | S2, S3, S12 |
| d5 | 0.98 | 1.08 | 1.2 | PROXY | S12, S13, S14 |
| o | 0.4 | 0.6 | 0.78 | PROXY | S2, S3, S12 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.20 | 0.51 | 0.95 | PROXY |
| F | 4.93 | 6.78 | 8.08 | ESTIMATE |
| C | 4.00 | 7.20 | 10.00 | PROXY |
| D | 3.92 | 6.48 | 9.36 | PROXY |

## Caveats
- a: No current 423910-specific occupational mix was located.
- a: B2B commerce vendor material shows feasible workflows but not realized substitution.
- a: Exposure varies widely between institutional team supply, commodity accessories, firearms, pools, fitness equipment, and pleasure craft.
- rho: Adoption intention is not implementation.
- rho: General distributor evidence may not capture fashion-like variants and returns.
- rho: Platform case studies can select digitally mature firms.
- e: The industry contains materially different product and regulatory niches.
- e: Repeat product orders are less contractually recurring than many service businesses.
- e: The injected LMM count is an estimate and includes brand-led or one-off models.
- s5: Owner plans do not equal completed transactions.
- s5: Sports asset deals include teams, brands, media, and other businesses outside wholesaling.
- s5: BizBuySell transactions skew smaller than the target EBITDA band.
- q: No direct five-year benefit-retention measure exists.
- q: Branded footwear and apparel economics differ from hard goods, team equipment, firearms, pools, and boats.
- q: Tariffs and vendor allowances can obscure AI-related retention.
- d5: Wholesale-sales growth includes price and mix effects.
- d5: Participation does not translate uniformly into equipment purchases.
- d5: Category booms such as pickleball can reverse while other categories mature.
- o: A warehouse or platform operator may remain necessary even when the independent wholesaler is bypassed.
- o: Institutional and specialty-dealer channels are more durable than consumer-branded goods.
- o: Channel strategies can reverse, as recent wholesale resurgence demonstrates.

## Sources
- **S1** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): For the selected durable-goods wholesale grouping, leading occupations include 229,190 nontechnical wholesale/manufacturing sales representatives, 146,830 hand material movers, 77,370 general and operations managers, 62,040 stockers/order fillers, 42,160 customer service representatives, and 38,620 shipping/receiving/inventory clerks.
- **S2** — [B2B Sporting Goods: Build a Scalable Operation](https://www.shopify.com/in/enterprise/blog/b2b-sporting-goods) (accessed 2026-07-22): Describes sporting-goods B2B workflows as bulk and recurring or seasonal replenishment using SKU lists, purchase orders, approvals, negotiated catalogs, invoices, net terms, multi-location freight, service agreements, repairs, replacement parts, warranty tracking, and contract renewals.
- **S3** — [Sporting Goods Industry Trends for 2025](https://www.shopify.com/enterprise/blog/sporting-good-industry-trends) (accessed 2026-07-22): Reports 30% of global sports and recreation purchases occur online, describes self-serve B2B ordering and automated replenishment, and cites a survey in which 75% of B2B buyers would switch suppliers for a smoother web-store experience.
- **S4** — [The 2025 State of AI in Distribution](https://distributionstrategy.com/wp-content/uploads/2025/03/DSG-Report-The-2025-State-of-AI-in-Distribution.pdf) (accessed 2026-07-22): Documents distributor AI use cases in invoicing, reorder prediction, cross-sell, quote/order automation, product substitution, and warehouse planning, including reported quote/order productivity examples of 25%-70%.
- **S5** — [Practical AI for Industrial Distribution](https://www.inddist.com/home/article/22950770/practical-ai-for-industrial-distribution) (accessed 2026-07-22): Reports 29% AI use, about 10% positive business impact, more than 43% expected adoption within two years, and 50% ERP use in a 2025 distributor survey; identifies data fragmentation and integration barriers.
- **S6** — [AI in distribution: driving digital transformation today](https://www.mckinsey.com/industries/industrials/our-insights/where-value-is-won-and-lost-in-distribution) (accessed 2026-07-22): Reports 90% of distributors had AI initiatives but only 11% had fully adopted and only 25% of adopters realized expected cost savings, illustrating the gap between initiative and implementation.
- **S7** — [NAICS Definition: 423910 Sporting and Recreational Goods and Supplies Merchant Wholesalers](https://www.census.gov/naics/?details=423910&input=423910&year=2012) (accessed 2026-07-22): Defines the code as merchant wholesale distribution of sporting goods and accessories, billiard and pool supplies, sporting firearms and ammunition, and marine pleasure craft, equipment, and supplies; index entries include sports, swimming-pool, tennis, and trapshooting equipment.
- **S8** — [2022 Economic Census wholesale questionnaire for NAICS 42391](https://bhs.econ.census.gov/ombpdfs2022/export/2022_WH-42391_mu.pdf) (accessed 2026-07-22): Lists sporting and recreational goods and supplies including bingo supplies, bicycles, exercise equipment, playground equipment, and related products, supporting the breadth of activities inside the code.
- **S9** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 52.3% of U.S. employer businesses are owned by people age 55 or older and 22% of employer-business owners planned to sell, transfer, or go public within five years.
- **S10** — [Wholesale and Distribution Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/wholesale-distribution/) (accessed 2026-07-22): Documents wholesale/distribution businesses sold during 2021-2025; durable-goods wholesalers had median revenue of $1.8 million, median owner earnings of $322,000, and median sale price of $800,000.
- **S11** — [Sporting Goods Industry Trends for 2025: private equity section](https://www.shopify.com/enterprise/blog/sporting-good-industry-trends) (accessed 2026-07-22): Reports global sports-asset deal volume rose 44% in 2024 and private-equity capital deployed in North America more than doubled, providing broad evidence of sports-sector investor activity while not isolating wholesalers.
- **S12** — [Sporting Goods 2025: The New Balancing Act](https://www.mckinsey.com/~/media/mckinsey/industries/retail/our%20insights/sporting%20goods%20industry%20trends/2025/sporting-goods-2025-the-new-balancing-act-turning-uncertainty-into-opportunity-v3.pdf) (accessed 2026-07-22): Describes major brands' pivot toward direct-to-consumer channels and challengers' wholesale-first strategies with specialist retailers, showing that both disintermediation and selective wholesale reach are active channel forces.
- **S13** — [Sporting Goods Industry Reaches Nearly $130B Amid Trade and Tariff Pressures](https://sfia.org/resources/new-sfia-report-sporting-goods-industry-reaches-nearly-130b-amid-trade-and-tariff-pressures/) (accessed 2026-07-22): Reports nearly $130 billion of 2025 U.S. sporting-goods wholesale sales, up 3.7% year over year and 34.7% since 2020; pickleball sales grew 22% and baseball/softball 7.9%.
- **S14** — [SFIA Releases the 2026 Topline Participation Report](https://sfia.org/resources/participation-hits-new-high-but-majority-of-americans-not-yet-meeting-recommended-guidelines-of-150-minutes-of-weekly-activity-sfias-2026-topline-report-finds/) (accessed 2026-07-22): Reports 250 million Americans participated in at least one sport, fitness, or leisure activity in 2025, total participation rose 1.2% year over year, and core participation reached 158.8 million, up 1.3%.
