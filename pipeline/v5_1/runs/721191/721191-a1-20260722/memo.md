# 721191 — Bed-and-Breakfast Inns

*v5.1 Stage 1 research memo. Run `721191-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.87 · L 1.55 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Automatable reservation, communication, pricing-support, marketing, and back-office work can reduce the administrative burden of a labor-intensive lodging operation.
**Weakness:** Only nine firms are estimated in-band, and no source directly measures qualifying five-year control transfers or AI labor outcomes for LMM U.S. B&B inns.

## Business-model lens
- Included: U.S. bed-and-breakfast inn operators providing short-term guest lodging, a full breakfast, personalized service, reservation handling, housekeeping, and related guest support to external travelers.
- Excluded: Pure real-estate holdings, residences without an operating lodging business, informal short-term rentals lacking the bed-and-breakfast service bundle, captive lodging, non-control financing vehicles, and establishments classified as hotels, motels, casino hotels, hostels, or vacation cabins.
- Customer and revenue model: Guests buy short stays, usually at a property-set room rate that includes breakfast; bookings arrive directly or through online travel agencies that use commission or net-rate models. Revenue repeats with room-night demand but is not generally contractual or subscription-based.
- Deviation from default lens: none

## Executive view
Bed-and-breakfast inns combine a useful seam of automatable front-office and owner-manager work with a service core that remains physical and personal. Reservation handling, routine guest messaging, marketing content, rate support, bookkeeping, and scheduling can absorb AI, but cleaning, breakfast, maintenance, and guest recovery limit the exposed labor share. The LMM population is tiny under the frozen dataset estimate, and transfer evidence is materially weaker than operating evidence.

## How AI changes the work
AI changes the administrative layer more than the stay itself. Desk-clerk workflows include reservations, account records, billing, messages, recommendations, nightly audit, and schedules (S3), while lodging managers set rates, monitor revenue, market the property, purchase services, and coordinate staff (S5). Those activities can be compressed with integrated agents and workflow tools. Housekeeping and food-service work dominate the broader occupation mix and remain difficult to substitute (S2, S4).

## Value capture
Guests pay room rates rather than reimbursing labor inputs, so there is no direct mechanism forcing an inn to pass labor savings through. Properties also set prices in a common OTA commission model (S9). Retention is nonetheless constrained by transparent comparison shopping, local lodging competition, channel fees, and the possibility that rivals spend savings on better service or lower rates.

## Firm availability
The frozen estimate supplies only nine firms in the target earnings band before eligibility. Most firms at that scale should be operating businesses, but owner-occupied real estate and proprietor-dependent goodwill can frustrate clean transfer. Gallup's employer-owner plans and BizBuySell's completed B&B sales establish a transfer channel, yet neither provides an LMM B&B transaction probability (S7, S8).

## Demand durability
National accommodation real output is projected to expand over the decade, although the near-term hotel forecast is subdued (S10, S11). Leisure cycles, international travel, destination shocks, and competition from short-term rentals create real downside. The surviving quantity still needs a property operator because the category's defining room, breakfast, cleaning, safety, and personalized-service bundle cannot be delivered entirely by software (S1, S4, S5).

## Risks and uncertainty
The largest empirical gaps are six-digit occupation mix, proprietor labor, LMM eligibility, and an at-risk denominator for control transfers. The broader hotel evidence may overstate both technology resources and specialized clerical work. A bad outcome would combine owner-dependent properties that cannot transfer, weak leisure demand, fragmented legacy systems, guest resistance to automated service, and competitors rapidly matching any cost advantage.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3742 | — | OBSERVED | — |
| n | — | 9 | — | ESTIMATE | — |
| a | 0.18 | 0.27 | 0.36 | PROXY | S2, S3, S4, S5 |
| rho | 0.3 | 0.48 | 0.65 | PROXY | S6, S12 |
| e | 0.65 | 0.82 | 0.95 | ESTIMATE | S1, S8 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S7, S8 |
| q | 0.42 | 0.67 | 0.82 | ESTIMATE | S1, S9, S10 |
| d5 | 0.96 | 1.08 | 1.17 | PROXY | S10, S11 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S3, S4, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.81 | 1.94 | 3.50 | PROXY |
| F | 0.86 | 1.55 | 2.19 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 8.45 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS does not publish a six-digit 721191 occupation mix and excludes self-employed owner labor.
- a: NAICS 721100 includes hotels and casino-related employment patterns that differ materially from small inns.
- a: Task exposure is a judgmental mapping, not an observed automation share.
- rho: The principal adoption study covers hotel chains globally, not single-property U.S. inns.
- rho: Survey expectations for full automation are intentions, not realized deployments.
- rho: Small inns may adopt inexpensive tools quickly but lack integration staff and clean operating data.
- e: The frozen firm count is itself an estimate bridged from receipts and a sector margin.
- e: B&B businesses often bundle operating goodwill with owner-occupied real estate.
- e: No source measures eligibility among the nine frozen LMM firms directly.
- s5: Gallup measures plans, not completed transactions, and spans all industries and firm sizes.
- s5: BizBuySell does not disclose the at-risk B&B population or the number of underlying observations on the benchmark page.
- s5: The observed BizBuySell firms have median revenue far below the frozen LMM earnings-band population.
- q: No source directly observes benefit retention after AI adoption in B&B inns.
- q: Local lodging markets vary sharply in seasonality, supply constraints, and price competition.
- q: OTA fees affect distribution economics, while q concerns retention of the implemented benefit rather than the gross room rate.
- d5: The BLS projection is for NAICS 721 and reports real output, not B&B room-night quantity.
- d5: The STR forecast is for U.S. hotels and covers only the near term.
- d5: B&B demand is concentrated in leisure destinations and can be more seasonal and locally idiosyncratic than national lodging demand.
- o: The estimate distinguishes task automation from elimination of the accountable property operator.
- o: Some jurisdictions and guests may accept remote management, but physical service delivery still requires accountable coordination.
- o: A property that removes personalized service and breakfast may migrate outside NAICS 721191 rather than represent software-only supply of the same basket.

## Sources
- **S1** — [North American Industry Classification System: 721191 Bed-and-Breakfast Inns](https://www.census.gov/naics/resources/archives/sect72.html) (accessed 2026-07-22): Defines NAICS 721191 as short-term lodging in private homes or converted small buildings characterized by highly personalized service and a full breakfast included in the room rate.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 721100 Traveler Accommodation](https://www.bls.gov/oes/2023/may/naics4_721100.htm) (accessed 2026-07-22): Provides the broader traveler-accommodation occupation and wage mix, including office and administrative support at 18.70% of employment, desk clerks at 13.18%, food preparation and serving at 23.74%, building and grounds cleaning at 26.76%, and housekeeping cleaners at 21.49%.
- **S3** — [O*NET OnLine: Hotel, Motel, and Resort Desk Clerks](https://www.onetonline.org/link/summary/43-4081.00) (accessed 2026-07-22): Lists desk-clerk tasks including reservations, guest accounts, charges, checkout, messages, inquiries, bookkeeping, housekeeping coordination, basic food setup, and staff scheduling.
- **S4** — [O*NET OnLine: Maids and Housekeeping Cleaners](https://www.onetonline.org/link/details/37-2012.00) (accessed 2026-07-22): Documents physical housekeeping tasks such as cleaning rooms, carrying linens and supplies, replenishing items, removing waste, cleaning floors, disinfecting, and protecting guest property.
- **S5** — [O*NET OnLine: Lodging Managers](https://www.onetonline.org/link/summary/11-9081.00) (accessed 2026-07-22): Identifies Bed and Breakfast Innkeeper as a lodging-manager title and lists tasks spanning rates, budgets, complaints, facilities, staffing, cleanliness, payments, procurement, marketing, and outside-service coordination.
- **S6** — [AI and Automation in Hospitality: h2c Global Study 2025](https://static.hospitalityinside.com/image/convert/hos/2025/10/02/ai-automation-study-tech-report-2025-by-h2c-68ded2240bb74641639205.pdf?s=3947eb40ead3257b94cc413e73d38f35) (accessed 2026-07-22): Reports AI integration and staffing effects from 189 responses representing 171 hotel chains; 35% had some integrated AI features, 25% had pilots, and respondents most often expected reservations, customer data, revenue management, and digital marketing to be fully automated within five years, while 26% expected widespread full automation to remain out of reach.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 52.3% of U.S. employer businesses are owned by people age 55 or older and that 22% of employer-business owners planned to sell or transfer ownership within five years.
- **S8** — [Bed and Breakfast Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/bed-breakfast/) (accessed 2026-07-22): Provides benchmarks from B&B businesses reported sold from 2021 through 2025, including a median sale price of $1.2 million, median revenue of $439,716, median owner earnings of $167,609, median 302 days on market, and an average 0.78 sale-to-ask ratio.
- **S9** — [Booking.com Connectivity: Managing Business Models](https://developers.booking.com/connectivity/docs/business-models-api/managing-business-models) (accessed 2026-07-22): Explains OTA commission and net-rate models; under the commission model the property sets the room price and the OTA retains a percentage of booking value.
- **S10** — [U.S. Hotel Forecast Assumptions: February 2026](https://www.costar.com/products/str-benchmark/resources/data-insights-blog/us-hotel-forecast-assumptions-february-2026) (accessed 2026-07-22): Reports that U.S. hotel demand declined 0.5% in 2025 and was forecast to rebound 0.4% in 2026 amid economic, geopolitical, government, and international-travel headwinds.
- **S11** — [BLS Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects accommodation-sector real output, measured in chained 2017 dollars, to increase from $309.1 billion in 2024 to $411.1 billion in 2034, a 2.9% compound annual rate.
- **S12** — [AI Beds Down in Hospitality but Cost Pressures Constrain Investment](https://nielseniq.com/global/en/insights/analysis/2025/ai-beds-down-in-hospitality-but-cost-pressures-constrain-investment/) (accessed 2026-07-22): Reports a 2025 hospitality-leader survey covering more than 13,100 venues: 72% were likely to implement AI within a year, but only 26% felt equipped for large-scale implementation and 53% had canceled some investment plans.
