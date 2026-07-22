# 487210 — Scenic and Sightseeing Transportation, Water

*v5.1 Stage 1 research memo. Run `487210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.91 · L 0.97 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Direct ticket and event-package revenue surrounds a recurring physical experience whose administrative workflows are automatable but whose safe delivery remains locally operator controlled.
**Weakness:** Nearly half of employment is transportation work, and transfer value can be impaired by owner-captain dependence, vessel liabilities, dock access, and regulatory requirements.

## Business-model lens
- Included: Privately controlled U.S. operators of repeat, ticketed local water experiences in the lower-middle-market EBITDA band, including excursion and harbor sightseeing boats, dinner cruises, airboat tours, whale and nature watches, and charter fishing boats with operators.
- Excluded: Water taxis and point-to-point passenger transport, bareboat rentals, guide-only recreation without vessel transport, floating casinos, public or captive attraction vessels, nonprofit operations, overnight cruises, firms without transferable operating assets or rights, and businesses outside the lower-middle-market band.
- Customer and revenue model: Primarily direct-to-consumer prepaid per-passenger tickets for scheduled or reservable trips, with meaningful private-charter, group-event, food-and-beverage, and fishing-party revenue; repeat service is delivered across departures and seasons rather than mainly through long-term customer contracts.
- Deviation from default lens: none

## Executive view
Water sightseeing has a clear digital administrative perimeter but an unusually physical, licensed, and safety-accountable core. Reservations, support, events, marketing, scheduling, and reporting can improve, while captains, deck crew, passenger attendants, mechanics, galley staff, and much live guiding remain attached to each departure. Direct ticket pricing supports retention, but vessel condition, dock rights, regulation, weather, and destination demand can dominate firm economics.

## How AI changes the work
AI can handle routine inquiries, multilingual content, event proposals, campaign production, schedule assistance, booking follow-up, document extraction, and financial administration. Humans still resolve weather and refund exceptions, coordinate bespoke groups, perform safety and hospitality work, maintain vessels, and navigate under credential and manning requirements.

## Value capture
Posted fares and private-event packages do not automatically rebate lower overhead to customers, allowing early savings to remain with operators. Over time, commissions, promotions, group negotiations, competing departures, and higher service expectations share some of the benefit.

## Firm availability
Aging-owner and exit-intent evidence suggests turnover, but completed external transfers should be substantially lower than stated intent. Owner-captain dependence, vessel-only sales, family succession, dock and concession rights, inspection status, and maintenance liabilities can prevent a nominal business from becoming a transferable going concern.

## Demand durability
Broad real leisure demand is forecast to grow, supporting local cruises, nature tours, dinner boats, and fishing parties. Outcomes remain highly local and exposed to discretionary spending, severe weather, ecology, fuel, insurance, tourism flows, and the continuing appeal and access of each waterfront destination.

## Risks and uncertainty
The main uncertainties are task-level labor evidence, the conversion of exit intention into closed control sales, and use of broad travel spending as a passenger proxy. Hidden vessel capex, inspection findings, casualty history, insurance availability, environmental rules, permits, dockage, seasonality, and customer concentration can outweigh administrative savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2777 | — | OBSERVED | — |
| n | — | 28 | — | ESTIMATE | — |
| a | 0.12 | 0.19 | 0.28 | PROXY | S2, S4 |
| rho | 0.28 | 0.46 | 0.64 | ESTIMATE | S4, S5 |
| e | 0.5 | 0.7 | 0.84 | ESTIMATE | S1, S3, S5 |
| s5 | 0.1 | 0.22 | 0.37 | PROXY | S6, S7 |
| q | 0.46 | 0.69 | 0.83 | ESTIMATE | S8 |
| d5 | 0.87 | 1.11 | 1.27 | PROXY | S1, S8, S9 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S2, S5, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.37 | 0.97 | 1.99 | ESTIMATE |
| F | 1.41 | 2.69 | 3.66 | ESTIMATE |
| C | 9.20 | 10.00 | 10.00 | ESTIMATE |
| D | 7.66 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS covers employers of all sizes and excludes self-employed workers, including some owner-captains.
- a: The occupation table predates the run date by three years and does not identify already-automated tasks.
- a: Observed Claude usage is not the same as technically substitutable labor and underrepresents physical work.
- rho: No industry-specific longitudinal AI implementation cohort was found.
- rho: Coast Guard credential and safe-manning requirements constrain labor removal even if adjacent tasks are automated.
- rho: Dinner and private-event operators have more complex service workflows than simple narrated harbor tours.
- e: Private-establishment counts are for NAICS 487 overall, not the water industry or LMM band.
- e: A vessel credential belongs to the mariner, while inspection and ownership documents may require action after a sale.
- e: The code mixes dinner cruises, narrated excursions, nature tours, airboats, and charter fishing with different transfer profiles.
- s5: The Census owner-age figure is all-industry and based on 2018 responding owners.
- s5: The EPI sample is voluntary and likely more exit-aware than typical operators.
- s5: A vessel sale, captain retirement, or change in minority ownership is not necessarily a qualifying control transfer.
- q: One seasonal nature-cruise operator illustrates the billing structure but not every subsegment.
- q: Scarce dockage or concession rights can support higher retention, while commoditized harbor loops can support less.
- q: Savings may be reinvested in service, safety, or additional departures rather than realized as cash margin.
- d5: Real travel spending is not a direct quantity measure.
- d5: The national forecast masks harbor-specific tourism, ecology, and severe-weather risk.
- d5: Charter fishing, dinner cruises, and narrated sightseeing may follow different demand paths.
- o: Some uninspected six-passenger operations face different manning rules than larger excursion vessels.
- o: Self-guided rentals and shore-based experiences can substitute for a portion of sightseeing demand without reproducing the same service.
- o: Automation of navigation may advance, but commercial passenger certification and adoption within five years remain uncertain.

## Sources
- **S1** — [North American Industry Classification System: Sector 48-49, NAICS 487210](https://www.census.gov/naics/resources/archives/sect48-49.html) (accessed 2026-07-22): Defines 487210 as local, usually same-day scenic and sightseeing transportation on water, including airboats, charter fishing, dinner cruises, excursion boats, and harbor tours.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 487200](https://www.bls.gov/oes/2023/may/naics4_487200.htm) (accessed 2026-07-22): Reports 16,790 jobs and detailed shares and wages, including 48.52% transportation/material moving, 12.24% office/administrative support, 10.80% food service, and 7.01% management.
- **S3** — [Scenic and Sightseeing Transportation: NAICS 487](https://www.bls.gov/iag/tgs/iag487.htm) (accessed 2026-07-22): Describes equipment-based local recreation and reports 3,557 private establishments versus 46 government establishments in the broader subsector in fourth-quarter 2025.
- **S4** — [Anthropic Economic Index report: Economic primitives](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) (accessed 2026-07-22): Reports automation-oriented business API use concentrated in routine back-office workflows including email, document processing, CRM, and scheduling, and discusses AI-covered travel-planning tasks.
- **S5** — [U.S. Coast Guard National Maritime Center: Charter Boat Captain](https://www.dco.uscg.mil/nmc/charter_boat_captain/) (accessed 2026-07-22): Explains passenger-vessel credential categories, including OUPV vessels limited to six or fewer passengers for hire and Master credentials for inspected small passenger vessels carrying more than six.
- **S6** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding U.S. employer-business owners were age 55 or older in the 2019 Annual Business Survey, data year 2018.
- **S7** — [2023 National State of Owner Readiness Report](https://exit-planning-institute.org/hubfs/Member%20Center%20Resources/2023%20National%20State%20of%20Owner%20Readiness%20Report.pdf) (accessed 2026-07-22): Surveyed 1,162 owners across more than 25 industries; reports 49% wanted to exit within five years and documents strong internal-exit preferences among family-business respondents.
- **S8** — [Seals, Fjord & More Cruise with Island Visit](https://barharborcruises.com/cruises/acadia-national-park-morning-cruise/) (accessed 2026-07-22): Shows a 2026 seasonal, fully narrated scheduled cruise with posted fares of $41 adult, $38 senior, $30 child, and $19 toddler/infant, illustrating direct ticket economics.
- **S9** — [U.S. Travel Forecast, Spring 2026](https://www.ustravel.org/research/travel-forecasts) (accessed 2026-07-22): Forecasts positive real leisure-travel spending, including $1.043 trillion in 2025 and $1.178 trillion in 2030 in the linked table, and notes shorter regional and drive trips.
