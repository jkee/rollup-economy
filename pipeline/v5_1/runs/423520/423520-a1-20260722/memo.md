# 423520 — Coal and Other Mineral and Ore Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423520-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.77 · L 0.13 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Complex contracts, shipment documents, market intelligence, and logistics coordination offer repeatable AI-assisted workflows around physical commodities.
**Weakness:** Domestic thermal-coal decline and an extremely low labor-to-receipts ratio limit the benefit, while the code's commodity mix is opaque.

## Business-model lens
- Included: US merchant wholesalers that repeatedly take title to and supply coal, coke, metal ores, ore concentrates, and nonconstruction nonmetallic minerals to external utilities, steelmakers, processors, exporters, and industrial customers.
- Excluded: Mining and beneficiation operations when not merchant-wholesale establishments; commission agents and brokers that do not take title; precious-metal bullion dealers; construction sand and gravel distributors; captive internal trading desks; shells; and firms outside the stated EBITDA band.
- Customer and revenue model: Commodity resale spreads and logistics/service margin on physical bulk materials, under a mixture of spot, indexed, bid, fixed-price, and multi-year supply arrangements, sometimes including blending, quality assurance, storage, terminal, transportation, and working-capital support.
- Deviation from default lens: none

## Executive view
The code contains a modest AI opportunity in document-, contract-, and market-heavy workflows, but its very low labor share limits the economic magnitude. Physical and counterparty accountability remain durable, while domestic thermal-coal exposure creates a material demand overhang that cannot be solved with workflow automation.

## How AI changes the work
AI can compare contracts, prepare bids, summarize markets, reconcile shipment and quality documents, draft customer updates, support compliance, and prioritize credit or logistics exceptions. Human traders, contract owners, quality personnel, and logistics operators remain accountable for prices, grades, quantities, sanctions, transport, and delivery.

## Value capture
Merchants may retain savings in spreads and fees between bid or renewal events, but transparent indexes, large customers, cost and price reopeners, and commodity competition drive sharing. Savings are small relative to the underlying commodity and freight value at risk.

## Firm availability
Repeat external contracts and logistics relationships can transfer, but commodity concentration, environmental diligence, customer dependence, and coal transition risk narrow both eligibility and the buyer universe. Generic small-business succession intent is therefore discounted.

## Demand durability
US power-sector coal consumption is forecast to decline and remains highly policy-sensitive. Export and metallurgical coal plus nonfuel ores and critical minerals diversify the basket, producing a wide five-year range rather than a uniform decline assumption.

## Risks and uncertainty
The unknown mix of thermal coal, metallurgical coal, coke, and dozens of minerals is the central evidence gap. Broad occupation data, producer rather than merchant contracting evidence, policy-sensitive coal forecasts, sanctions, commodity and freight volatility, credit exposure, and potential direct contracting all weaken precision.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0203 | — | OBSERVED | — |
| n | — | 221 | — | ESTIMATE | — |
| a | 0.18 | 0.29 | 0.41 | PROXY | S2, S3 |
| rho | 0.35 | 0.54 | 0.7 | ESTIMATE | S3, S4 |
| e | 0.45 | 0.66 | 0.82 | ESTIMATE | S1, S4 |
| s5 | 0.08 | 0.16 | 0.26 | PROXY | S6, S7 |
| q | 0.32 | 0.5 | 0.66 | ESTIMATE | S4 |
| d5 | 0.68 | 0.88 | 1.1 | PROXY | S4, S8, S9 |
| o | 0.78 | 0.89 | 0.96 | PROXY | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.05 | 0.13 | 0.23 | ESTIMATE |
| F | 3.53 | 5.13 | 6.23 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 5.30 | 7.83 | 10.00 | PROXY |

## Caveats
- a: The BLS occupation population spans multiple durable-goods wholesale groups and is not specific to coal and ores.
- a: Anthropic conversations are a self-selected usage sample and do not measure labor substitution.
- a: The code mixes office-heavy commodity merchants with physical terminal and handling operations.
- rho: No controlled AI implementation study for 423520 was found.
- rho: Long-term contracts and bespoke shipping terms require human legal and commercial approval.
- rho: Small firms may lack integrated data while larger traders may already automate much of the addressable work.
- e: The NAICS definition combines structurally declining US thermal coal with export metallurgical coal and diverse nonfuel minerals.
- e: A coal producer's contracting model is only a proxy for independent merchants.
- e: The provided firm count is margin-bridged and may include businesses with volatile EBITDA or limited service content.
- s5: Owner-intent and owner-age evidence is broad, not 423520-specific.
- s5: Transactions may be structured as contract, reserve, terminal, or asset purchases rather than transfers of a going merchant business.
- s5: Distress and closure are excluded from qualifying control transfers.
- q: No public evidence directly measures pass-through of AI savings in 423520.
- q: Retention differs sharply between indexed bulk commodity contracts and specialized minerals with quality or logistics differentiation.
- q: Commodity-price and freight movements can overwhelm workflow savings.
- d5: Coal consumption and mineral production are end-market proxies, not direct merchant-wholesale service volumes.
- d5: The coal forecast is highly policy-sensitive, and EIA presents alternative futures rather than a single prediction.
- d5: The code's commodity mix is unknown, making the base especially sensitive to thermal-coal weight.
- o: Operator requirement is distinct from the shrinking quantity of thermal coal demand.
- o: Direct long-term contracts can bypass independent merchants, especially for large utilities and steelmakers.
- o: Digital marketplaces may reduce intermediation in standardized spot trades but still rely on physical logistics and accountable counterparties.

## Sources
- **S1** — [NAICS definition: 423520 Coal and Other Mineral and Ore Merchant Wholesalers](https://www.census.gov/naics/?details=4235&input=4235&year=2017) (accessed 2026-07-22): Defines the industry as merchant wholesale distribution of coal, coke, metal ores, and nonmetallic minerals, excluding precious and semiprecious stones and construction minerals such as sand and gravel.
- **S2** — [May 2023 OEWS: Merchant Wholesalers, Durable Goods, selected groups including NAICS 4235](https://www.bls.gov/oes/2023/may/naics4_4230A1.htm) (accessed 2026-07-22): Reports the broad occupation mix including sales 22.11%, office/administrative support 15.27%, management 9.96%, production 7.97%, and transportation/material moving 26.54%.
- **S3** — [Anthropic Economic Index: Mapping AI usage across occupational tasks](https://www.anthropic.com/news/the-anthropic-economic-index) (accessed 2026-07-22): Finds AI usage concentrated in digital tasks, physical-labor categories least represented, moderate task-level diffusion across occupations, and more augmentation than automation in observed conversations.
- **S4** — [Core Natural Resources, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1710366/000171036626000007/cnr-20251231.htm) (accessed 2026-07-22): Describes coal sales to established customers through relationships and bids, contracts from single shipments to multi-year volumes, renewal practices, approximately 110 customers, and 56% of 2025 coal revenue from export markets.
- **S5** — [Peabody Energy Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1064728/000106472826000006/btu-20251231.htm) (accessed 2026-07-22): Describes competitive bidding and negotiated long-term coal supply agreements with price adjustments, quality requirements, quantity parameters, environmental constraints, extensions, and termination provisions.
- **S6** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall-2024 survey reports 22% of employer-business owners planned to sell or transfer within five years and 17% of owners age 55 or older planned a sale or transfer.
- **S7** — [McKinsey: Navigating the great small business ownership transition](https://www.mckinsey.com/institute-for-economic-mobility/our-insights/the-great-ownership-transfer-a-new-era-of-business-stewardship) (accessed 2026-07-22): Estimates more than half of US small-business owners are over 55 and reports closure dominates observed SMB exits, indicating execution risk beyond stated transfer plans.
- **S8** — [EIA Short-Term Energy Outlook, February 2026: Coal markets](https://www.eia.gov/outlooks/steo/archives/feb26.pdf) (accessed 2026-07-22): Forecasts US electric-power coal consumption at 391 million short tons in 2026, down 7% year over year, and a further decline to 375 million short tons in 2027.
- **S9** — [USGS: Value of U.S. mineral production rose in 2025](https://www.usgs.gov/news/national-news-release/value-us-mineral-production-rose-last-year-driven-precious-metals-prices) (accessed 2026-07-22): Reports overall US mineral production value rose 5.6% to $112 billion in 2025 and mineral-reliant industries represented $4.09 trillion, while documenting the breadth and importance of nonfuel minerals.
- **S10** — [EIA releases the Annual Energy Outlook 2026](https://www.eia.gov/pressroom/releases/press587.php) (accessed 2026-07-22): States coal plant retirements drive US coal demand lower and that coal generation could mostly disappear from the power sector if the specified 2024 emissions regulations are enforced; emphasizes that AEO cases are alternative futures, not predictions.
