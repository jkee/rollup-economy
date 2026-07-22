# 721110 — Hotels (except Casino Hotels) and Motels

*v5.1 Stage 1 research memo. Run `721110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.44 · L 1.61 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable physical lodging demand combined with automatable front-desk and administrative workflows under persistent staffing pressure.
**Weakness:** Most hotel labor is physical, while the frozen firm count and public transfer data do not cleanly distinguish eligible operating companies from property-owning structures.

## Business-model lens
- Included: U.S. hotel and motel operating firms in the roughly $1-10M normalized EBITDA band that repeatedly provide rooms and related guest services to external travelers, including franchised and independent operators with operating responsibility.
- Excluded: Casino hotels, passive real-estate holding shells, captive internal lodging units, non-control financing vehicles, and entities that own an interest in a property but do not operate or control the lodging service.
- Customer and revenue model: Primarily nightly room revenue paid by leisure, business, group, and other travelers, with ancillary food, beverage, meeting, parking, and service revenue where offered; prices are generally market-set per stay rather than cost-plus.
- Deviation from default lens: none

## Executive view
Hotels and motels have a real but bounded AI labor opportunity. Front-desk, reservation, messaging, accounting, scheduling, marketing, and revenue workflows are amenable to automation, but the labor base remains heavily physical. Durable travel demand and the need for a responsible physical operator are strengths; property-heavy economics, fragmented operating structures, cyclical demand, and uncertain control-transfer availability are central limitations.

## How AI changes the work
AI should first reshape the digital perimeter of a property: inquiry handling, reservation support, pre-arrival and in-stay messaging, check-in assistance, review responses, staff scheduling, bookkeeping support, and revenue analysis. It can also improve housekeeping dispatch and maintenance triage, but those tools coordinate rather than eliminate much of the physical work. Guest exceptions and service recovery keep humans in the loop.

## Value capture
Unlike cost-plus service contracts, nightly room pricing does not automatically pass labor savings to customers. Operators can retain early gains, particularly in labor-constrained markets, but competitive rates, franchise and distribution fees, brand standards, wage pressure, and guest-experience reinvestment erode retention over five years. Poorly executed labor removal can also reduce ratings and repeat demand.

## Firm availability
Many hotels are franchised but locally owned or operated, so brand affiliation does not preclude a control investment. The harder screen is whether the LMM firm actually controls operations rather than being a passive property entity. General employer-business succession intent and a liquid hotel asset market suggest recurring opportunities, but public deal data do not isolate qualifying operating-company transfers.

## Demand durability
Travel forecasts support modest real growth across domestic and recovering international segments. Physical lodging cannot be delivered entirely by software, and even self-service hotels require accountability for rooms, safety, access, cleaning, maintenance, and exceptions. The demand case is nevertheless cyclical and exposed to travel budgets, local supply additions, geopolitical conditions, and alternative accommodation.

## Risks and uncertainty
The largest research gaps are task-level paid-hour exposure in LMM properties, actual post-implementation labor outcomes, the separation between real-estate ownership and operating control, and retention of savings after competitive repricing. Other risks include legacy-system integration, payment and identity security, franchise approvals, guest backlash, service-quality failures, labor rules, property capital needs, and the possibility that technology improves service without reducing labor.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3045 | — | OBSERVED | — |
| n | — | 1091 | — | ESTIMATE | — |
| a | 0.16 | 0.24 | 0.33 | PROXY | S1, S2 |
| rho | 0.35 | 0.55 | 0.74 | PROXY | S2, S3 |
| e | 0.58 | 0.76 | 0.9 | ESTIMATE | S5 |
| s5 | 0.12 | 0.19 | 0.3 | PROXY | S4, S6 |
| q | 0.34 | 0.56 | 0.75 | ESTIMATE | S8 |
| d5 | 0.95 | 1.07 | 1.18 | PROXY | S7, S8 |
| o | 0.9 | 0.96 | 0.99 | PROXY | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.68 | 1.61 | 2.97 | PROXY |
| F | 6.99 | 8.15 | 9.15 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 8.55 | 10.00 | 10.00 | PROXY |

## Caveats
- a: The closest public occupation table is NAICS 721100 and includes casino hotels, all firm sizes, and establishments rather than LMM firms.
- a: Employment shares are not wage shares or task shares, and the estimate excludes work already automated.
- a: Guest-facing service quality can prevent technically exposed tasks from translating into avoidable labor.
- rho: S2 is global, includes large operators, is based on plans and preferences, and predates the current generative-AI cycle.
- rho: Contactless investment is broader than AI labor substitution and can improve experience without reducing labor.
- rho: Staffing shortages create incentive but do not prove that exposed work can be implemented safely or reliably.
- e: The frozen firm count is a margin-bridged estimate and may map imperfectly to hotel operating firms because ownership and management entities can be separated.
- e: Public hotel counts are property counts, not firms, and one firm may own or operate multiple properties.
- e: No public source directly measures lens eligibility within the $1-10M normalized EBITDA band.
- s5: The Gallup survey is cross-industry and measures stated plans, including some non-qualifying gifts or public offerings.
- s5: Hotel transaction dollars are dominated by larger assets and do not supply a count or LMM denominator.
- s5: A hotel real-estate transfer may leave the manager or franchise operating arrangement unchanged.
- q: No public study directly measures five-year retention of implemented AI labor savings for LMM hotels.
- q: Retention varies sharply by local supply, chain scale, franchise agreement, distribution mix, and service level.
- q: The estimate excludes demand-volume effects, which belong in d5 and o, and implementation difficulty, which belongs in rho.
- d5: S7 covers all travel spending, not only hotels and motels, and the published forecast ends in 2030 rather than July 2031.
- d5: Inflation-adjusted spending is not a pure room-night quantity measure and may retain mix or quality effects.
- d5: Hotel demand is cyclical and varies substantially by geography, chain scale, business versus leisure mix, and international gateways.
- o: Self-service is not the same as absence of an accountable operator.
- o: Local lodging, fire, accessibility, safety, and employment rules may preserve operator responsibilities even as staffing changes.
- o: The estimate could fall if software-enabled alternative accommodations materially displace the current hotel service basket.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 721100 Traveler Accommodation](https://www.bls.gov/oes/2023/may/naics4_721100.htm) (accessed 2026-07-22): All-size traveler-accommodation occupation mix: building and grounds cleaning 26.76% of employment, food preparation and serving 23.74%, office and administrative support 18.70%, hotel desk clerks 13.18%, and maids and housekeeping cleaners 21.49%; page notes that NAICS 721100 includes casino hotels.
- **S2** — [Travelers Want High-Tech, Low-Touch Hotel Stays Shows New Oracle Survey](https://www.oracle.com/news/announcement/oracle-hospitality-in-2025-consumer-research-study-2022-06-01/) (accessed 2026-07-22): Spring 2022 survey of 5,266 consumers and 633 hotel executives across nine countries: 96% of hoteliers investing in contactless technology, 54% prioritizing technology that improves or eliminates the front-desk experience, 38% of travelers wanting a fully self-service model with staff on request, and 77% interested in automated messaging or chatbots.
- **S3** — [76% of surveyed hotels report staffing shortages](https://www.ahla.com/news/76-surveyed-hotels-report-staffing-shortages) (accessed 2026-07-22): AHLA May 2024 survey of 456 hoteliers: 76% reported staffing shortages, 79% could not fill openings, respondents sought an average of seven workers per property, and 50% ranked housekeeping as the most critical staffing need.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 Gallup Pathways to Wealth Survey of 1,264 U.S. business owners: 14% of all owners and 22% of employer-business owners planned a sale or ownership transfer within five years; older owners reported higher transfer intent than younger owners.
- **S5** — [Franchising](https://www.ahla.com/issue/franchising) (accessed 2026-07-22): AHLA reports that 57% of U.S. hotels are franchised and projected 36,173 franchised hotels in 2024, indicating that franchise affiliation is a common operating structure rather than a rare exception.
- **S6** — [2024 hotel transaction volume drops by 15% from prior year](https://www.costar.com/article/8541178/2024-hotel-transaction-volume-drops-by-15-from-prior-year) (accessed 2026-07-22): CoStar reports $21 billion of U.S. hotel transaction volume in 2024, $3.6 billion below 2023 and down 15%, evidencing an active but cyclical hotel asset-transfer market.
- **S7** — [U.S. Travel Forecast: Spring 2026](https://www.ustravel.org/sites/default/files/2026-05/US_Travel-Forecast_Spring26.pdf) (accessed 2026-07-22): Inflation-adjusted travel-spending forecast through 2030: domestic spending rises from 99% of 2019 in 2025 to 110% in 2030, domestic leisure from 104% to 115%, domestic business from 88% to 97%, and international from 80% to 99%; the report separately publishes the lodging-away-from-home price index.
- **S8** — [2025 State of the Industry Report](https://www.ahla.com/resource/2025-state-industry-report) (accessed 2026-07-22): AHLA describes normalized travel demand, rising operating costs and regulatory pressure, growing interest in experience-driven travel, and generative AI as relevant to guest experience and operating efficiency while emphasizing satisfaction, loyalty, innovation, and new revenue streams.
