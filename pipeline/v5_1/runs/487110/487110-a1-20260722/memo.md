# 487110 — Scenic and Sightseeing Transportation, Land

*v5.1 Stage 1 research memo. Run `487110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.10 · L 1.76 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Direct ticket economics around a repeat physical experience allow back-office AI savings to remain with the operator more readily than in pass-through service contracts.
**Weakness:** Most wages sit in physical, safety-sensitive, and guest-facing work, while the eligible transaction universe is small and transferability can depend on local permits and destination access.

## Business-model lens
- Included: Privately controlled U.S. operators of repeat, ticketed local land sightseeing experiences, including sightseeing buses and trolleys, scenic rail excursions, and horse-drawn sightseeing rides, within the lower-middle-market EBITDA band.
- Excluded: Public or captive attraction transit, nonprofit museum operations, point-to-point passenger transportation, charter-only fleets, travel agencies, operators without transferable operating assets or permits, and businesses outside the lower-middle-market band.
- Customer and revenue model: Primarily direct-to-consumer, prepaid per-passenger tickets or day passes for scheduled or reservable local experiences, with secondary group, private-hire, food, merchandise, and attraction-bundle revenue; repeat service is delivered across departures and seasons rather than through long-term customer contracts.
- Deviation from default lens: none

## Executive view
Land sightseeing combines a modest digital labor pool with a stubbornly physical core. Reservations, support, marketing, scheduling, bookkeeping, and content preparation can improve, while drivers, mechanics, cleaners, attendants, and much live guiding remain tied to equipment, place, safety, and guest experience. Direct ticket pricing can preserve a meaningful portion of gains, but demand and firm transferability are locally idiosyncratic.

## How AI changes the work
AI changes the administrative perimeter more than the ride itself: automated inquiry handling, multilingual content, campaign production, demand forecasting, schedule assistance, document processing, and bookkeeping can reduce seasonal hiring pressure. Human review remains important for exceptions, accessibility, weather, refunds, group coordination, safety communications, and brand-sensitive narration.

## Value capture
Posted, prepaid ticket and pass prices do not mechanically rebate lower labor cost to customers, so early adopters can retain savings. Over several seasons, online comparison, reseller commissions, promotions, rival adoption, and customer expectations for longer hours or better service will share part of the benefit.

## Firm availability
The modeled LMM population is small and heterogeneous. Broad owner-age and exit-intent evidence suggests turnover, but qualifying external transfers will be fewer because many firms are family controlled, concession dependent, owner identified, nonprofit or public adjacent, or more naturally closed or internally succeeded than sold.

## Demand durability
National real leisure-travel spending is forecast to grow, and shorter regional and drive trips can support local sightseeing. Yet this is discretionary, destination-specific demand exposed to weather, energy costs, consumer confidence, inbound travel, and the continued appeal of each route or attraction.

## Risks and uncertainty
The largest uncertainties are the lack of task-level payroll evidence, the gap between owner exit intent and completed external sales, and the use of broad leisure spending as a quantity proxy. Asset condition, insurance, safety compliance, permits, concession rights, seasonality, and destination concentration can dominate the economics and must be diligenced firm by firm.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3676 | — | OBSERVED | — |
| n | — | 24 | — | ESTIMATE | — |
| a | 0.15 | 0.24 | 0.34 | PROXY | S2, S4 |
| rho | 0.3 | 0.5 | 0.68 | ESTIMATE | S3, S4 |
| e | 0.55 | 0.74 | 0.88 | ESTIMATE | S1, S3 |
| s5 | 0.1 | 0.23 | 0.38 | PROXY | S6, S7 |
| q | 0.45 | 0.68 | 0.82 | ESTIMATE | S8 |
| d5 | 0.9 | 1.12 | 1.28 | PROXY | S1, S5 |
| o | 0.8 | 0.91 | 0.97 | ESTIMATE | S1, S2, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.66 | 1.76 | 3.40 | ESTIMATE |
| F | 1.35 | 2.62 | 3.54 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.20 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The latest directly accessible detailed OEWS table is 2022 and covers NAICS 487100 rather than firm-size-specific LMM operators.
- a: OEWS excludes self-employed workers, which can be material in owner-operated sightseeing firms.
- a: Observed Claude usage is not equivalent to technically substitutable labor and is skewed toward digitally represented tasks.
- rho: No industry-specific five-year AI implementation cohort was found.
- rho: Current enterprise AI usage may not transfer to small seasonal operators with thin management capacity.
- rho: Passenger-safety and operating duties remain human-accountable even when adjacent paperwork is automated.
- e: The BLS private-versus-government establishment counts are for NAICS 487 as a whole, not 487110 or the LMM band.
- e: Private status does not establish control transferability or fit with the recurring-service lens.
- e: The industry mixes bus, trolley, rail, and animal-powered businesses with different capital and permit profiles.
- s5: The Census owner-age statistic is all-industry, based on 2018 responding owners, and is not a firm-level probability.
- s5: The EPI sample is voluntary, cross-industry, and likely unusually engaged in exit planning.
- s5: An ownership transition is not necessarily an external, transferable control sale.
- q: A single park-partner trolley is illustrative of posted ticket pricing, not an industry-wide contract sample.
- q: Retention is likely lower for commoditized hop-on/hop-off routes and higher for scarce concession or rail experiences.
- q: Seasonality and fixed departure capacity can convert labor savings into service expansion rather than cash margin.
- d5: Real spending is not a direct measure of trip quantity or constant service quality.
- d5: The forecast is national and broad; individual operators are highly exposed to local tourism, weather, wildfire, fuel, and concession conditions.
- d5: The published forecast ends in 2030, slightly short of a full five years from the July 2026 run date.
- o: Autonomous passenger vehicles are unlikely to diffuse uniformly within five years but could affect the high end of automation scenarios.
- o: Narration requirements vary: live guides are central to some premium tours and peripheral to basic loop transportation.
- o: Operator-required share could be lower where the destination itself, rather than transportation, creates most customer value.

## Sources
- **S1** — [North American Industry Classification System: Sector 48-49, NAICS 487110](https://www.census.gov/naics/resources/archives/sect48-49.html) (accessed 2026-07-22): Defines 487110 as local, same-day land sightseeing using buses, trolleys, steam trains, and horse-drawn rides and distinguishes it from transit, charter, and travel-arrangement activities.
- **S2** — [May 2022 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 487100](https://www.bls.gov/oes/2022/may/naics4_487100.htm) (accessed 2026-07-22): Reports 10,060 jobs and detailed occupation shares and wages, including 32.88% transportation/material moving, 25.00% personal care/service, 13.24% office/administrative support, and 7.67% installation/maintenance.
- **S3** — [Scenic and Sightseeing Transportation: NAICS 487](https://www.bls.gov/iag/tgs/iag487.htm) (accessed 2026-07-22): Describes the equipment-based, local recreation production process and reports 3,557 private establishments versus 46 government establishments in fourth-quarter 2025, plus current employment and safety data.
- **S4** — [Anthropic Economic Index report: Economic primitives](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) (accessed 2026-07-22): Finds office and administrative tasks more prevalent in automation-oriented business API usage and identifies routine email, document processing, CRM, and scheduling as delegation-suited workflows; also discusses AI-covered travel-agent tasks.
- **S5** — [U.S. Travel Forecast, Spring 2026](https://www.ustravel.org/research/travel-forecasts) (accessed 2026-07-22): Forecasts positive real travel-spending growth, lists leisure spending of $1.043 trillion in 2025 and $1.178 trillion in 2030 in the linked table, and notes a shift toward shorter, lower-cost regional and drive trips.
- **S6** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding U.S. employer-business owners were age 55 or older in the 2019 Annual Business Survey, data year 2018.
- **S7** — [2023 National State of Owner Readiness Report](https://exit-planning-institute.org/hubfs/Member%20Center%20Resources/2023%20National%20State%20of%20Owner%20Readiness%20Report.pdf) (accessed 2026-07-22): Surveyed 1,162 owners across more than 25 industries; reports 49% wanted to exit within five years and documents strong internal-exit preferences among family-business respondents.
- **S8** — [Take a Trolley Tour: Valley Forge National Historical Park](https://www.nps.gov/thingstodo/vafo-trolley-tour.htm) (accessed 2026-07-22): Shows a current operator model with scheduled 90-minute guided trolley departures, advance reservations, and posted per-passenger prices of $24 adult, $22 student/senior/military, and $14 child.
