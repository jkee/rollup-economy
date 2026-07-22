# 481212 — Nonscheduled Chartered Freight Air Transportation

*v5.1 Stage 1 research memo. Run `481212-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.90 · L 0.96 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat outsourced cargo programs create a durable physical service base where AI can compress document- and coordination-heavy overhead.
**Weakness:** Most wage cost sits in regulated, safety-critical flight and maintenance work that AI is unlikely to substitute materially within five years.

## Business-model lens
- Included: US lower-middle-market certificated air carriers providing recurring or repeat outsourced, nonscheduled cargo-only charter, CMI, or ACMI flying to freight forwarders, integrators, government, airlines, and direct shippers.
- Excluded: Scheduled freight carriers, passenger charter, air couriers, aircraft-only lessors, captive internal flight departments, inactive certificate shells, and non-control financing vehicles.
- Customer and revenue model: Customers buy aircraft capacity by trip or block hour under full-service charter, CMI, or ACMI arrangements; repeat programs can guarantee flying, while spot charters are transaction-based. Fuel and other direct costs may be borne by the customer under ACMI or included in a fixed charter price.
- Deviation from default lens: none

## Executive view
Nonscheduled charter freight combines durable physical demand and meaningful repeat-contract models with a labor base dominated by safety-critical pilots and mechanics. The practical AI opportunity is concentrated in quoting, dispatch support, customer service, compliance documentation, maintenance records, scheduling, and finance rather than aircraft operation itself.

## How AI changes the work
AI can triage requests, draft quotes and flight documentation, reconcile operating records, support route and crew planning, search maintenance manuals, flag compliance exceptions, and automate billing. Human accountability and review remain central because operational control, airworthiness, training, hazardous materials, and flight decisions are regulated and safety consequential.

## Value capture
Fixed-price charter and predetermined-rate ACMI/CMI structures let an operator retain some productivity gains before renewal. Capture weakens as concentrated buyers rebid contracts, benchmark block-hour rates, demand service credits, or negotiate productivity into renewals.

## Firm availability
The industry includes small single-aircraft Part 135 operators as well as large feeder networks, but not every modeled LMM firm is an active, independent, repeat-service platform. Aircraft ownership, certificate status, management qualifications, customer concentration, and maintenance obligations are central transfer diligence issues.

## Demand durability
FAA projects broad US air-cargo RTMs to grow over the next five years, supporting the physical service need. Charter freight nevertheless remains exposed to trade cycles, tariffs, integrator network decisions, modal substitution, and volatile special-mission or government demand.

## Risks and uncertainty
The occupational evidence is only available at four-digit nonscheduled air transportation and blends passenger activity; the demand forecast blends scheduled and nonscheduled cargo; transfer evidence is cross-industry; and commercial evidence comes from a much larger carrier. Autonomous feeder aircraft and drones can change who operates some routes, while pilot, maintenance, insurance, aircraft, and regulatory constraints can overwhelm back-office savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.213 | — | OBSERVED | — |
| n | — | 28 | — | ESTIMATE | — |
| a | 0.17 | 0.24 | 0.31 | PROXY | S1 |
| rho | 0.34 | 0.47 | 0.61 | ESTIMATE | S2, S3 |
| e | 0.5 | 0.68 | 0.82 | ESTIMATE | S2, S4 |
| s5 | 0.15 | 0.22 | 0.31 | PROXY | S5, S3 |
| q | 0.36 | 0.54 | 0.72 | ESTIMATE | S6 |
| d5 | 0.94 | 1.16 | 1.31 | PROXY | S7 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S8, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.49 | 0.96 | 1.61 | ESTIMATE |
| F | 1.82 | 2.65 | 3.37 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 8.46 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS source is four-digit nonscheduled air transportation and includes passenger charter and specialty flying.
- a: OEWS excludes self-employed workers and is a 2023 occupational snapshot.
- a: Task exposure is researcher judgment, not a measured AI adoption or automation statistic.
- rho: No source directly measures five-year AI implementation in nonscheduled cargo charter.
- rho: The estimate excludes autonomous-aircraft displacement and counts only implementation of the task opportunity in a.
- e: The frozen firm count is margin-bridged and may include entities whose economics or certificate status do not match the lens.
- e: No public dataset identifies repeat external revenue at the firm level.
- s5: Gallup measures intentions, not completed qualifying transfers.
- s5: The survey population spans industries and business sizes and may not represent asset-heavy air carriers.
- q: The SEC filing is from a much larger operator than the firms in the lens.
- q: Commercial terms vary sharply between spot charter, government flying, CMI, and ACMI.
- d5: FAA's forecast combines scheduled and nonscheduled cargo and passenger-belly freight.
- d5: The forecast is model-based and sensitive to GDP, trade, tariff, fuel-price, and modal-share assumptions.
- o: Future BVLOS and autonomous-aircraft regulation may change operator staffing and certificate structures.
- o: The estimate distinguishes operator requirement from employment intensity; automation may reduce labor without eliminating the operator.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 481200 Nonscheduled Air Transportation](https://www.bls.gov/oes/2023/may/naics4_481200.htm) (accessed 2026-07-22): Four-digit occupation and wage mix: 58,340 total jobs; management 7.74%, business/financial 6.82%, office/administrative 13.55%, maintenance/repair 15.99%, commercial pilots 33.84%, and detailed administrative, dispatch, cargo, and mechanic roles.
- **S2** — [FAA Charter-Type Services (Part 135)](https://www.faa.gov/hazmat/air_carriers/operations/part_135) (accessed 2026-07-22): Part 135 authorizes on-demand unscheduled service; operators range from small single-aircraft firms to large cargo feeder networks; hazardous-materials compliance and approved programs are mandatory.
- **S3** — [FAA Part 135 Certification: General Information](https://www.faa.gov/licenses_certificates/airline_certification/135_certification/general_info) (accessed 2026-07-22): Operational-control responsibility, named pilots for limited certificates, and manual, training-program, and required-management-position obligations for basic and standard operators.
- **S4** — [US Census Bureau NAICS 481212 Definition](https://www.census.gov/naics/resources/archives/sect48-49.html) (accessed 2026-07-22): Defines 481212 as cargo-only air transportation without regular routes and schedules and distinguishes scheduled freight, couriers, passenger/cargo charter, and specialty flying.
- **S5** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 survey: 22% of employer-business owners reported plans to sell or transfer ownership within five years; 17% of owners age 55+ planned a sale or transfer.
- **S6** — [Air Transport Services Group 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/894081/000143774925005937/atsg20241231_10k.htm) (accessed 2026-07-22): Describes CMI/ACMI and charter structures: customers typically supply fuel and cargo handling under ACMI and reimburse certain direct expenses, while full-service charter generally includes fuel and operating costs for a fixed all-inclusive price.
- **S7** — [FAA Aerospace Forecast Fiscal Years 2026-2046](https://www.faa.gov/data_research/aviation/aerospace_forecasts/FY_2026-2046_Full_Forecast_Document_Tables.pdf) (accessed 2026-07-22): Forecasts total US commercial-air-carrier cargo RTMs from 50.427 billion in 2026 to 59.934 billion in 2031; discusses GDP linkage, modal competition, and growing UAS/AAM cargo-feeder activity.
- **S8** — [FAA Package Delivery by Drone (Part 135)](https://www.faa.gov/uas/advanced_operations/package_delivery_drone) (accessed 2026-07-22): States that BVLOS package-delivery operators must obtain Part 135 certification and airspace authorization and documents seven approved UAS package-delivery operators through April 2025.
