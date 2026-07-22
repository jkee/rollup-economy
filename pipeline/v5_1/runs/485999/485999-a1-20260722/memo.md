# 485999 — All Other Transit and Ground Passenger Transportation

*v5.1 Stage 1 research memo. Run `485999-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.54 · L 2.80 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat route operations create automatable coordination work while airport and institutional passenger flows sustain physical service demand.
**Weakness:** Driver-heavy delivery and concentrated route contracts constrain both labor substitution and long-run retention of savings.

## Business-model lens
- Included: Private lower-middle-market operators of recurring or repeat shuttle, airport-transfer, hotel-transfer, carpool, vanpool, and other scheduled ground-passenger services for external customers or contracting organizations.
- Excluded: Captive hotel, airport, campus, or employer fleets; urban transit systems; taxis and ride-hail; limousine, school-bus, charter-bus, special-needs, and ambulance services; pure software platforms; and one-off event movements without repeat-service economics.
- Customer and revenue model: Repeat passenger fares, monthly vanpool payments, route or service contracts with airports, hotels, parking operators, employers, campuses, and transit sponsors, and in some cases public operating or capital support.
- Deviation from default lens: none

## Executive view
The industry is a residual but recognizable set of scheduled shuttles and administered shared rides. It has a high physical-labor base and a smaller automatable layer in booking, scheduling, dispatch, communications, billing, and contract reporting; demand depends heavily on route and customer mix.

## How AI changes the work
AI can absorb routine reservations and passenger questions, maintain manifests against flight or shift changes, propose vehicle and driver assignments, predict disruptions, draft alerts, reconcile trips, and prepare invoices and reports. Drivers, safety checks, vehicle care, boarding, and real-world exception handling remain largely human.

## Value capture
Operators with fixed fees or posted fares can initially keep labor and utilization gains, especially when reliability improves. Renewal bids, institutional procurement, public-funding conditions, route competition, and concentrated concession counterparties will share part of the benefit over five years.

## Firm availability
Recurring routes and fleet assets can support transferability, but captive fleets are outside the lens and many independent firms may depend on one airport, hotel group, parking concession, employer, or public sponsor. Assignment rights, fleet condition, insurance, and management depth are central to whether an intended sale becomes a qualifying control transfer.

## Demand durability
Airport traffic and recurring destination links support modest aggregate growth, while vanpools and institutional shuttles can be durable where parking or access is constrained. Telework, ride-hail, rail links, customer insourcing, and travel cycles produce meaningful downside and make individual contracts less durable than the service need.

## Risks and uncertainty
Six-digit occupation data are unavailable, the NAICS category mixes several business models, and the frozen LMM firm count is estimated. Customer concentration, concession rebids, insurance and driver availability, vehicle capital needs, telework, travel shocks, and uncertain autonomous-shuttle timing could all move results. The industry would be unattractive where a single nonassignable contract drives economics or where procurement rapidly passes all savings through.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.7362 | — | OBSERVED | — |
| n | — | 66 | — | ESTIMATE | — |
| a | 0.09 | 0.17 | 0.27 | PROXY | S1, S2 |
| rho | 0.35 | 0.56 | 0.74 | ESTIMATE | S2, S7 |
| e | 0.45 | 0.65 | 0.82 | ESTIMATE | S1, S4 |
| s5 | 0.14 | 0.22 | 0.33 | PROXY | S3 |
| q | 0.34 | 0.57 | 0.75 | ESTIMATE | S4, S6 |
| d5 | 0.9 | 1.04 | 1.15 | PROXY | S5, S6, S2 |
| o | 0.8 | 0.92 | 0.98 | ESTIMATE | S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.93 | 2.80 | 5.88 | ESTIMATE |
| F | 2.64 | 3.77 | 4.72 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.20 | 9.57 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source is four-digit NAICS 4859, not six-digit 485999.
- a: Employment shares are only a bridge to wage-weighted task exposure.
- a: The frozen compensation-to-receipts ratio uses 2024 wages over 2022 receipts and is harmonized to the IPS basis as stated in the assignment.
- rho: No source directly measures five-year implementation of AI labor substitution in private NAICS 485999 firms.
- rho: Autonomous driving is not assumed to contribute materially to implementation within the base case.
- rho: Regular-route shuttles and demand-responsive vanpools have different workflow complexity.
- e: The NAICS residual category combines airport and hotel shuttles, carpools, vanpools, and other passenger transport.
- e: No source identifies which LMM firms meet the transferable outsourced-service lens.
- e: The frozen firm count is a margin-bridged estimate rather than observed EBITDA-band firm data.
- s5: Gallup covers US employer businesses across industries and sizes.
- s5: Plans include gifts and rare public offerings and are not completed control transfers.
- s5: Closures and internal reorganizations do not qualify.
- q: No source directly measures automation-savings pass-through in this industry.
- q: Capture differs among public vanpool programs, private passenger fares, parking shuttles, and fixed-fee institutional contracts.
- q: Demand effects and implementation difficulty are excluded from this primitive.
- d5: Neither proxy measures constant-price, constant-quality demand for NAICS 485999.
- d5: The residual industry has heterogeneous demand drivers and customer concentration.
- d5: Employment projections embed productivity and occupational demand, not only service quantity.
- o: No source measures the five-year operator-required share for the target lens.
- o: Autonomous-shuttle readiness can change nonlinearly with regulation and vehicle capability.
- o: The accountable operator may use remote supervision or rider-drivers rather than today's staffing model.

## Sources
- **S1** — [485999: All Other Transit and Ground Passenger Transportation — Census Bureau Profile](https://data.census.gov/profile/485999_-_All_Other_Transit_and_Ground_Passenger_Transportation?codeset=naics~485999&g=010XX00US) (accessed 2026-07-22): Defines the industry to include shuttle services and car pools or vanpools, with shuttles generally operating regular routes and schedules between hotels, airports, or other destinations; reports 2,285 employer establishments in 2023 County Business Patterns.
- **S2** — [Other Transit and Ground Passenger Transportation — May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_485900.htm) (accessed 2026-07-22): Broader NAICS 4859 occupation mix: transportation occupations 74.40%, passenger-vehicle drivers 64.64%, shuttle drivers and chauffeurs 52.75%, and office/administrative support 15.10% of employment.
- **S3** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall-2024 US survey found that 22% of employer-business owners planned to sell or transfer ownership within five years, versus 9% of nonemployers.
- **S4** — [FTA Van Pool Policy — FAQs](https://www.transit.dot.gov/regulations-and-guidance/legislation/map-21/fta-van-pool-policy-faqs) (accessed 2026-07-22): Defines private public-transportation vanpool providers and commuter vanpool vehicles, including the expectation that at least 80% of mileage is for home-to-work commuter transport.
- **S5** — [Occupational projections and worker characteristics, 2024–2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): BLS projects shuttle-driver and chauffeur employment from 243,900 in 2024 to 260,300 in 2034, an increase of 16,400 or 6.7%.
- **S6** — [December 2024 U.S. Airline Traffic Data Up 5.9% from December 2023](https://www.bts.gov/newsroom/december-2024-us-airline-traffic-data-59-december-2023) (accessed 2026-07-22): BTS reported 83.3 million systemwide scheduled-service passengers in December 2024 and a seasonally adjusted all-time high, providing a directional airport-shuttle demand indicator.
- **S7** — [Future automated shuttle deployments should incorporate route design features such as dedicated lanes and simplified operating environments](https://www.itskrs.its.dot.gov/2025-l01259) (accessed 2026-07-22): NCDOT pilot lessons state automated-shuttle technology was not ready for mainstream scale, had restricted compliance and operating conditions, and required an onboard attendant.
