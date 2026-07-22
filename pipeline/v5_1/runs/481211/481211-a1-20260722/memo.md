# 481211 — Nonscheduled Chartered Passenger Air Transportation

*v5.1 Stage 1 research memo. Run `481211-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.00 · L 1.14 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A fragmented base of repeat-service operators with high-value coordination workflows and pricing flexibility around aircraft utilization.
**Weakness:** Most payroll and risk remain tied to regulated physical flight operations, aircraft availability and scarce aviation personnel rather than automatable office work.

## Business-model lens
- Included: US lower-middle-market Part 135 passenger charter operators providing repeat on-demand flights, jet-card or membership service, corporate shuttle, managed-aircraft charter or recurring specialized passenger transport to external customers.
- Excluded: Brokers without operational control, Part 91 captive flight departments, fractional programs without charter operations, scheduled passenger airlines, cargo-only operators, air tours where transportation is incidental, dormant certificate shells and non-control aircraft financing vehicles.
- Customer and revenue model: Customers buy individual flights quoted by aircraft, route, daily or hourly rate and incidentals, or prepay through memberships and jet-card programs; managed-aircraft and partner programs can add recurring availability and contract revenue.
- Deviation from default lens: none

## Executive view
Passenger charter combines a sizeable fragmented operator pool with useful AI opportunities in quoting, dispatch support, scheduling, maintenance planning and customer operations. The flight itself remains human- and operator-accountable, and differentiated service can preserve more savings than commodity air travel, but aircraft intensity and safety obligations cap the addressable payroll share.

## How AI changes the work
AI can accelerate quote construction, trip feasibility, broker and customer responses, crew and aircraft scheduling, repositioning, records review and maintenance planning. It is unlikely to replace pilots, mechanics, cabin service or final operational-control decisions within five years.

## Value capture
Trip-specific pricing, peak premiums, memberships and repeat corporate relationships allow operators to retain part of better utilization and lower overhead. Transparent broker markets, customer switching and costly substitute lift still pressure savings, especially for small undifferentiated fleets.

## Firm availability
Many active Part 135 passenger operators fit the recurring external-service lens, and recent acquisitions show transferability. Diligence must separate real operating companies from brokers, captive managers and certificate shells and confirm that aircraft access, management personnel and customers survive control transfer.

## Demand durability
FAA turbine and jet forecasts support moderate growth, with charter demand remaining above pre-pandemic levels. Demand is discretionary and cyclical, and national fractional fleets may capture disproportionate growth from smaller local charter operators.

## Risks and uncertainty
The largest uncertainties are the true eligible share of the injected firm pool, existing software penetration, customer concentration and whether AI gains improve owned-fleet utilization rather than simply lower quoted prices. Safety incidents, pilot scarcity, maintenance downtime and fleet financing can dominate economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2235 | — | OBSERVED | — |
| n | — | 397 | — | ESTIMATE | — |
| a | 0.14 | 0.22 | 0.32 | PROXY | S1, S2, S3 |
| rho | 0.36 | 0.58 | 0.74 | ESTIMATE | S3, S4, S5 |
| e | 0.48 | 0.66 | 0.8 | ESTIMATE | S4, S6 |
| s5 | 0.15 | 0.27 | 0.4 | PROXY | S7, S8 |
| q | 0.36 | 0.56 | 0.72 | PROXY | S3, S9 |
| d5 | 0.9 | 1.12 | 1.25 | PROXY | S10, S11 |
| o | 0.95 | 0.985 | 1 | ESTIMATE | S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.45 | 1.14 | 2.12 | ESTIMATE |
| F | 5.45 | 6.87 | 7.81 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | PROXY |
| D | 8.55 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS industry includes nonscheduled cargo and specialty operations outside passenger charter.
- a: Employment counts are not wage weights and do not measure task exposure.
- a: Required flight crew, maintenance sign-off and final operational-control decisions are excluded from substitution.
- rho: Evidence of digital optimization is from a large public operator rather than the LMM population.
- rho: Implementation capacity varies sharply between single-aircraft, basic and standard Part 135 certificate holders.
- rho: This value excludes pricing, demand and acquisition effects.
- e: The injected firm count is an ESTIMATE from size classes and an industry margin, not a verified list of 397 firms.
- e: Part 135 authority also covers cargo and limited scheduled operations.
- e: Aircraft management and charter may be intertwined with adjacent MRO and FBO economics.
- s5: One announced operator acquisition is not a representative transfer rate.
- s5: Broad small-business transaction data are a different population.
- s5: A certificate or aircraft sale alone does not qualify unless a viable operating company and control transfer together.
- q: Large program operators have denser fleets and stronger brands than many LMM firms.
- q: Fuel, maintenance and third-party lift can be explicitly or implicitly passed through to customers.
- q: This estimate excludes demand loss and implementation difficulty.
- d5: General-aviation forecasts are broader than NAICS 481211 and include owner-flown and fractional activity.
- d5: Flight hours are an imperfect proxy for constant-quality passenger charter demand.
- d5: Business aviation is exposed to corporate profits, wealth, fuel prices, aircraft supply and recession.
- o: Digital brokerage can eliminate sales and service interactions while leaving operator-required demand intact.
- o: Advanced air mobility may alter the supplier form first on short routes but remains certification-dependent.
- o: The primitive concerns the charter transport service, not every element of today's customer journey.

## Sources
- **S1** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Lists the largest nonscheduled-air occupations, including 20,400 commercial pilots, 7,060 mechanics, 1,880 managers, 1,350 sales representatives and 1,330 customer-service representatives.
- **S2** — [Airline and Commercial Pilots](https://www.bls.gov/ooh/Transportation-and-Material-Moving/Airline-and-commercial-pilots.htm) (accessed 2026-07-22): Reports that nonscheduled air transportation employs 39% of commercial pilots and describes the variable schedules and safety-accountable work.
- **S3** — [flyExclusive, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1843973/000184397326000013/flyx-20251231.htm) (accessed 2026-07-22): Describes proprietary daily/hourly quoting, membership programs, contractual pricing premiums, scheduling optimization and fulfillment of more than 95% of customer flights on its own fleet.
- **S4** — [Part 135 Certification General Information](https://www.faa.gov/licenses_certificates/airline_certification/135_certification/general_info) (accessed 2026-07-22): Defines on-demand authority and certificate scopes and states that basic and standard operators must maintain manuals, training programs and required management positions.
- **S5** — [Technical Discipline: Artificial Intelligence – Machine Learning](https://www.faa.gov/aircraft/air_cert/step/disciplines/artificial_intelligence) (accessed 2026-07-22): FAA states that aviation AI/ML functionality and performance must be evaluated within a certification framework to assure safety.
- **S6** — [Safe Air Charter](https://www.faa.gov/charter) (accessed 2026-07-22): Explains that legitimate air charter requires Part 135-level pilot, maintenance and safety compliance and emphasizes operator authorization and operational control.
- **S7** — [Valiair Acquires Superior Air Charter](https://www.valiair.com/news/valiair-acquires-superior-air-charter) (accessed 2026-07-22): Reports the completed February 24, 2026 acquisition of a Dallas-based Part 135 on-demand charter operator.
- **S8** — [2025 Year in Review: BizBuySell Market Recap](https://www.bizbuysell.com/blog/2025-year-in-review/) (accessed 2026-07-22): Reports 9,586 US small-business transactions in 2025; used only as broad transfer-market context, not a charter-operator rate.
- **S9** — [Jet.AI Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1861622/000149315226009165/form10-k.htm) (accessed 2026-07-22): States that charter competition depends on price, reliability, safety, reputation, aircraft availability, service quality and investment requirements and details third-party operator and charter-related costs.
- **S10** — [FAA Aerospace Forecast Fiscal Years 2026–2046: General Aviation](https://www.faa.gov/data_research/aviation/aerospace_forecasts/2026_FAA_Aerospace_Forecasts_FY2026-2046-2.pdf) (accessed 2026-07-22): Forecasts turbine aircraft hours, including rotorcraft, to grow 2.6% annually from 2024 to 2046 and jet aircraft hours to grow 3.2% annually.
- **S11** — [Honeywell Forecasts Record Demand for Business Jets for Next Decade](https://www.honeywellaerospace.com/us/en/company/newsroom/2025/10/business-jet-demand-forecast) (accessed 2026-07-22): Reports business-jet flight hours up about 3% year over year in 2025 and charter demand stabilized well above 2019 levels.
