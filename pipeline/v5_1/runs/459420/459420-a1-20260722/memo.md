# 459420 — Gift, Novelty, and Souvenir Retailers

*v5.1 Stage 1 research memo. Run `459420-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Recurring venue partnerships with automatable merchandise, planning, e-commerce, and reporting work layered over durable physical operations.
**Weakness:** Only a small fraction of a transactional, discretionary retail NAICS appears to provide a qualifying outsourced service.

## Business-model lens
- Included: US lower-middle-market operators that provide recurring outsourced gift-shop or merchandise-program services to attractions, museums, zoos, aquariums, historic sites, hospitality properties, destinations, campuses, airports, or comparable venue partners, including store operation, product development and sourcing, merchandising, staffing, fulfillment, and branded e-commerce.
- Excluded: Standalone consumer gift, greeting-card, novelty, holiday, and souvenir shops without an external venue or institutional service contract; one-off product sales; artisan microbusinesses; pure wholesalers; captive venue-owned stores; shells; and non-control financing vehicles.
- Customer and revenue model: The operator assumes responsibility for a partner venue's retail program and earns product gross margin under a multiyear operating, concession, lease, or revenue-share arrangement. The venue may receive a percentage of gross sales or minimum guarantee, while visitors buy in-store or online merchandise tied to the venue's mission, destination, or brand.
- Deviation from default lens: Narrowed to outsourced experiential-retail and merchandise-program operators because NAICS 459420 is primarily transactional merchandise retail, whereas ordinary standalone gift shops do not supply an outsourced service. The distinction is necessary for a coherent screen and is not an attractiveness selection.

## Executive view
The coherent service business is outsourced experiential retail, not the typical standalone gift shop. A qualifying operator owns a venue partner's store, merchandise, people, systems, and fulfillment problem, producing recurring contracts and meaningful administrative and commercial workflows for AI; the universe is likely very small, and venue concentration, concession economics, and discretionary spending are central risks.

## How AI changes the work
AI can accelerate assortment analysis, design ideation, product copy, localized marketing, purchasing support, forecasts, schedules, customer inquiries, e-commerce operations, and partner reporting. It does much less for physical store design, stocking, visual merchandising, packaging, guest interaction, construction, vendor execution, and accountable onsite leadership.

## Value capture
Percentage-of-sales concession fees do not automatically share a labor saving, supporting initial retention. Minimum guarantees, public bids, contract renewals, venue demands, and consumer price competition eventually redistribute value, so durable benefit depends on contract tenure, renewal advantage, and differentiated operating quality.

## Firm availability
The broad NAICS contains many standalone stores and microbusinesses that do not qualify. Turnkey external operators demonstrably exist, but no public source counts LMM firms with transferable venue contracts. General employer-owner surveys and broad retail transactions support only a proxy for five-year control transfer.

## Demand durability
Real domestic leisure travel is forecast to grow and national-park visitation remains high, supporting destination retail. Museum recovery is uneven and gift purchases remain discretionary; lower visitor conversion, consumer trade-down, tariffs, weak inbound travel, or a shift from merchandise to experiences can offset attendance growth.

## Risks and uncertainty
The principal uncertainties are classification leakage, a very low eligible share, absent firm-count data, reliance on one scaled operator's claims, and the lack of contract or operating benchmarks across venues. A transaction can be unattractive if one venue dominates revenue, change of control triggers rebidding, guarantees are aggressive, inventory ages quickly, or merchandise relevance depends on founder taste.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.27 | 0.39 | PROXY | S2, S3, S4 |
| rho | 0.28 | 0.44 | 0.61 | ESTIMATE | S4, S5 |
| e | 0.03 | 0.08 | 0.17 | ESTIMATE | S1, S4, S5 |
| s5 | 0.07 | 0.14 | 0.24 | PROXY | S9, S10 |
| q | 0.34 | 0.52 | 0.68 | PROXY | S4, S11, S12 |
| d5 | 0.91 | 1.06 | 1.18 | PROXY | S6, S7, S8 |
| o | 0.68 | 0.82 | 0.92 | PROXY | S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.18 | 0.48 | 0.96 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 6.80 | 10.00 | 10.00 | PROXY |
| D | 6.19 | 8.69 | 10.00 | PROXY |

## Caveats
- a: The occupation distribution uses the broader predecessor industry and is not specific to outsourced venue operators.
- a: Task exposure is judgmentally mapped and does not measure technically feasible substitution in this industry.
- a: The frozen compensation-to-receipts input is at ancestor 44-45, has a 2024-wage/2022-receipts vintage mismatch, and is LOW quality; it may materially under- or overstate the narrowed multisite service model.
- rho: This is bounded judgment, not an observed adoption cohort.
- rho: The documented turnkey operator is likely more technologically capable than an LMM operator.
- rho: Demand, pricing, concession economics, and valuation are excluded from rho.
- e: No source measures the share of LMM firms that are outsourced operators.
- e: Some qualifying operators may be classified under another retail, concession, management, or services NAICS code.
- e: The frozen n input is a declared dataset gap and will be MISSING, so this packet does not infer an eligible firm count.
- s5: Gallup spans all industries and firm sizes, and stated plans are not completed transactions.
- s5: BizBuySell retail businesses are generally far smaller than the specified EBITDA band and are not industry-specific.
- s5: Venue contracts may require consent or rebidding upon change of control, reducing transferability.
- q: The cited concession documents are venue-specific and not a distribution of LMM contract terms.
- q: Revenue share as a percentage of sales is not the same as sharing an AI-generated gross benefit.
- q: Volume loss and implementation difficulty are excluded and represented in d5, o, and rho.
- d5: Travel spending is not gift-shop unit demand and includes price and unrelated categories.
- d5: The published travel forecast ends in 2030, one year short of the requested year-five endpoint from 2026.
- d5: Museum recovery and international travel remain uneven, creating material venue-level dispersion.
- o: A vendor-reported renewal rate is not a direct measure of service quantity requiring an operator.
- o: The cited operator is larger and more integrated than many LMM firms.
- o: Demand quantity is handled in d5 and is not reduced again here.

## Sources
- **S1** — [2022 NAICS definition: Gift, Novelty, and Souvenir Retailers](https://www.census.gov/naics/?chart=2022&details=459420&input=459420) (accessed 2026-07-22): Defines 459420 as establishments primarily retailing new gifts, novelty merchandise, souvenirs, greeting cards, seasonal and holiday decorations, and curios; supports treating ordinary merchandise retail as distinct from outsourced operation.
- **S2** — [Data USA: Gift, novelty, and souvenir shops](https://datausa.io/profile/naics/gift-novelty-souvenir-shops) (accessed 2026-07-22): Reports a 2022 workforce of 137,931 and identifies 40,718 retail salespersons, 30,939 first-line supervisors of retail sales workers, and 16,916 cashiers as the three largest occupations.
- **S3** — [O*NET Retail Salespersons job duties](https://www.onetonline.org/search/task/choose/41-2031.00) (accessed 2026-07-22): Lists tasks including customer-needs discovery, recommendations, payments, product explanation, displays, inventory requisition, returns, security, special orders, records, contracts, packaging, and delivery arrangements.
- **S4** — [Event Network: What We Do](https://www.eventnetwork.com/what-we-do) (accessed 2026-07-22): Documents a turnkey outsourced attraction-retail model with more than 100 partnerships and a vendor-reported 97% renewal rate, covering operations, staff, product development, purchasing, merchandising, design, e-commerce, fulfillment, technology, and partner collaboration.
- **S5** — [Event Network: Experiential retail solutions](https://www.eventnetwork.com/our-services) (accessed 2026-07-22): Describes outsourced retail services for zoos, aquariums, art and science museums, natural-history and historic sites, hospitality gift shops, tourist destinations, and campuses, including bespoke brand-linked shopping experiences.
- **S6** — [U.S. Travel Forecast, Spring 2026](https://www.ustravel.org/research/travel-forecasts) (accessed 2026-07-22): Projects inflation-adjusted travel spending growth of 1% in 2026 and 3% in 2027 and 2028; reports $909 billion of domestic leisure spending in 2026, an extended forecast through 2030, and elevated consumer and geopolitical risks.
- **S7** — [National Park Service: 2025 visitation statistics](https://www.nps.gov/orgs/1207/03-13-26-2025-visitation-statsitics.htm?pubDate=20260512) (accessed 2026-07-22): Reports more than 323 million recreation visits and over 13 million overnight stays in 2025, with 26 parks setting visitation records; supports current attraction traffic, not gift-shop conversion.
- **S8** — [American Alliance of Museums 2024 Annual National Snapshot](https://www.aam-us.org/2024/11/14/2024-annual-national-snapshot-of-united-states-museums/) (accessed 2026-07-22): Survey of more than 400 museum directors covering attendance and finances reports that recovery remains uneven and many museums have not returned to pre-pandemic attendance or financial health.
- **S9** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 52.3% of US employer businesses are owned by people age 55 or older and that 22% of employer-business owners in its fall-2024 survey planned to sell or transfer ownership within five years; plans are not completed qualifying transfers.
- **S10** — [BizBuySell retail business valuation benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/retail-business/) (accessed 2026-07-22): Documents completed transactions for broad, mostly independent retail businesses from 2021-2025 and reports a five-year average earnings multiple of 2.62; establishes transfer-market activity but not an industry-specific probability.
- **S11** — [Griffith Observatory Bookstore and Gift Shop Concession Agreement](https://recreation.parks.lacity.gov/sites/default/files/pdf/commissioner/2016/jun15/Package%202.pdf) (accessed 2026-07-22): Public agreement sets tiered revenue-sharing fees at 25%, 30%, 35%, and 38% of gross receipts across annual-sales thresholds, illustrating direct venue participation in sales economics.
- **S12** — [Durango-La Plata County Airport Terminal Gift Shop Retail Concession Agreement, 2025](https://govtribe.com/file/government-file/dro-terminal-gift-shop-retail-concession-agreement-2025-final-dot-docx) (accessed 2026-07-22): Specifies operator responsibility for costs and service standards, street-pricing constraints, and annual payment of the greater of a minimum guarantee or a percentage of gross gift-shop revenue.
