# 487990 — Scenic and Sightseeing Transportation, Other

*v5.1 Stage 1 research memo. Run `487990-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.50 · L 0.87 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A 20% office-and-administrative employment share surrounds high-priced direct consumer experiences, creating a real but bounded digital labor opportunity.
**Weakness:** The eligible firm pool is extremely small and heterogeneous, while pilots, mechanics, permissions, safety history, and location-specific access can impair transferability.

## Business-model lens
- Included: Privately controlled U.S. operators of repeat, ticketed local scenic transportation other than land or water in the lower-middle-market EBITDA band, principally helicopter, airplane, glider, and hot-air-balloon sightseeing excursions and scenic aerial tramways or cable cars.
- Excluded: Point-to-point or charter air transportation, flight training, specialty aviation services, commuter tramways, public or captive attraction systems, nonprofit operations, firms without transferable operating assets or authorities, and businesses outside the lower-middle-market band.
- Customer and revenue model: Primarily prepaid per-passenger tickets or private-flight pricing for local same-day aerial experiences and admission fares for scenic tramways, with secondary photography, transfer, premium-package, retail, and attraction revenue; repeat service occurs across departures and visitor seasons rather than under long-term contracts.
- Deviation from default lens: none

## Executive view
Other scenic transportation is a tiny, heterogeneous set of premium aerial experiences and scenic lifts. It has a larger administrative share than land or water sightseeing, creating room in reservations, customer service, dispatch support, sales, and office work, but pilots, mechanics, attendants, safety systems, and site operations remain physical and regulated. Transferability and demand must be evaluated operator by operator.

## How AI changes the work
AI can automate routine inquiries, multilingual marketing and narration, booking follow-up, document intake, CRM, reporting, and portions of schedule and dispatch preparation. It should assist rather than replace weather, weight-and-balance, operational-control, piloting, maintenance, lift-safety, and irregular-operations decisions.

## Value capture
Prepaid consumer tickets and private packages allow early administrative savings to remain with operators. Reseller commissions, promotions, competing operators, fee visibility, and expectations for a premium booking and guest experience will share part of the benefit over five years.

## Firm availability
The modeled LMM universe contains only eight firms and mixes aviation with aerial lift operations. Aging-owner evidence supports turnover, but owner-pilot dependence, public or captive tramways, regulatory authority, aircraft or lift condition, insurance, concessions, and asset-only exits can sharply reduce eligible going-concern transfers.

## Demand durability
Broad real leisure demand is forecast to grow, but premium aerial sightseeing can be more volatile than travel overall. Weather, wildfire, safety events, noise restrictions, fuel, insurance, destination access, and consumer risk perception can cause abrupt local contraction; iconic scarce experiences can outperform.

## Risks and uncertainty
The main uncertainties are the composition of the eight-firm universe, task-level payroll exposure, exit completion, and use of broad leisure spending as a quantity proxy. Safety record, maintenance reserves, life-limited parts, regulatory compliance, route permissions, leases, concessions, and insurance availability can dominate administrative economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2198 | — | OBSERVED | — |
| n | — | 8 | — | ESTIMATE | — |
| a | 0.15 | 0.23 | 0.32 | PROXY | S2, S4 |
| rho | 0.24 | 0.43 | 0.62 | ESTIMATE | S4, S5, S6 |
| e | 0.4 | 0.63 | 0.8 | ESTIMATE | S1, S2, S5 |
| s5 | 0.08 | 0.2 | 0.35 | PROXY | S7, S8 |
| q | 0.48 | 0.71 | 0.86 | ESTIMATE | S9 |
| d5 | 0.76 | 1.07 | 1.25 | PROXY | S1, S5, S10 |
| o | 0.91 | 0.97 | 0.995 | ESTIMATE | S2, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.32 | 0.87 | 1.74 | ESTIMATE |
| F | 0.37 | 1.12 | 1.89 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 6.92 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS covers employers of all sizes, excludes self-employed pilots, and does not separate aerial tramways from flight operators.
- a: Dispatch and scheduling tasks that look digital may include nondelegable safety judgment.
- a: Observed Claude usage is not equivalent to current not-yet-automated substitution potential.
- rho: No longitudinal AI adoption cohort specific to scenic air or tram operators was found.
- rho: FAA operating, certification, maintenance, and medical requirements restrict removal of accountable personnel.
- rho: Hot-air-balloon and aerial-tram workflows differ materially from Part 135 helicopter or airplane operations.
- e: The frozen firm count is an estimate, so eligibility applied to eight firms is highly sensitive to classification error.
- e: OEWS confirms aviation is prominent but does not quantify the share of firms that are tramways, balloons, or aircraft operators.
- e: An aircraft, lift, or customer list may transfer while operating authority or key-person capability does not.
- s5: The Census owner-age statistic is all-industry and dated to 2018 responding owners.
- s5: The EPI sample is voluntary, cross-industry, and likely unusually focused on exit planning.
- s5: With only eight estimated LMM firms, one transaction materially changes an observed five-year rate.
- q: A single balloon operator illustrates direct posted pricing but not helicopter, airplane, or tramway billing.
- q: High fixed aircraft or lift costs can cause savings to support resilience or capacity rather than reported margin.
- q: Retention can be lower in destinations with many interchangeable operators and higher where routes or concessions are scarce.
- d5: Real leisure spending is not a direct measure of ride quantity.
- d5: Helicopter, balloon, fixed-wing, and tramway demand have different weather, price, and risk sensitivities.
- d5: Local regulatory or safety changes can overwhelm the national forecast.
- o: Regulatory regimes differ among Part 91 and Part 135 air tours, balloons, gliders, and state-regulated tramways.
- o: Ground-based or virtual substitutes can displace demand without reproducing the same service.
- o: Autonomous flight may progress technologically, but commercial sightseeing certification and adoption within five years remain uncertain.

## Sources
- **S1** — [U.S. Census Bureau NAICS Detail for 487990](https://www.census.gov/naics/?details=487990&input=487990&year=2007) (accessed 2026-07-22): Identifies aerial cable cars, aerial tramways, glider excursions, helicopter rides, hot-air-balloon rides, and other aerial sightseeing within 487990.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 487900](https://www.bls.gov/oes/2023/may/naics4_487900.htm) (accessed 2026-07-22): Reports 2,510 jobs and detailed shares and wages, including 38.24% transportation, 20.22% office/administrative support, 8.36% maintenance, 6.93% sales, and 6.74% management.
- **S3** — [Scenic and Sightseeing Transportation: NAICS 487](https://www.bls.gov/iag/tgs/iag487.htm) (accessed 2026-07-22): Describes the subsector's equipment-based local recreation model and current employment, establishment, and safety context.
- **S4** — [Anthropic Economic Index report: Economic primitives](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) (accessed 2026-07-22): Reports automation-oriented business API use in routine back-office workflows such as email, document processing, CRM, and scheduling and discusses AI-covered travel-planning tasks.
- **S5** — [Federal Aviation Administration: 135 Flight Operations Section](https://www.faa.gov/about/office_org/headquarters_offices/avs/offices/afx/afs/afs200/afs220/135_flt_ops) (accessed 2026-07-22): States that the FAA branch develops policy and guidance for all commercial Part 91 and Part 135 air-tour operations, including specified low-altitude and national-park operations.
- **S6** — [FAA Final Rule: Medical Certification Standards for Commercial Balloon Operations](https://www.faa.gov/newsroom/final-rule-medical-certification-standards-commercial-balloon-operations) (accessed 2026-07-22): States that commercial hot-air-balloon pilots carrying paying passengers must hold second-class medical certificates, the same standard required for other commercial pilots.
- **S7** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding U.S. employer-business owners were age 55 or older in the 2019 Annual Business Survey, data year 2018.
- **S8** — [2023 National State of Owner Readiness Report](https://exit-planning-institute.org/hubfs/Member%20Center%20Resources/2023%20National%20State%20of%20Owner%20Readiness%20Report.pdf) (accessed 2026-07-22): Surveyed 1,162 owners across more than 25 industries; reports 49% wanted to exit within five years and documents strong internal-exit preferences among family-business respondents.
- **S9** — [Hot Air Expeditions: 2026 Hot Air Balloon Ride Pricing](https://hotairexpeditions.com/pricing/) (accessed 2026-07-22): Shows direct posted 2026 per-person pricing, including $239 Phoenix morning adult shared rides, $649 private adult rides, and separately priced add-ons and fees.
- **S10** — [U.S. Travel Forecast, Spring 2026](https://www.ustravel.org/research/travel-forecasts) (accessed 2026-07-22): Forecasts positive real leisure-travel spending, including $1.043 trillion in 2025 and $1.178 trillion in 2030 in the linked table, while identifying elevated economic and geopolitical risks.
