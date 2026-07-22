# 811192 — Car Washes

*v5.1 Stage 1 research memo. Run `811192-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.74 · L 2.41 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High-frequency transaction and equipment data can improve membership retention, labor deployment, chemical use, and tunnel uptime.
**Weakness:** The core exterior process is already automated, leaving a relatively small incremental AI task pool and a highly format-dependent firm population.

## Business-model lens
- Included: U.S. lower-middle-market fixed-site professional car-wash operators providing conveyorized express-exterior or staffed exterior-and-interior cleaning, washing, waxing, vacuuming, and membership services to retail and fleet customers.
- Excluded: Unattended coin-operated self-service bay businesses, purely mobile hand-detailing routes, captive washes at gasoline stations, dealerships, fleets, or parking operations, equipment and chemical suppliers, household do-it-yourself washing, shells, non-control vehicles, and owner-dependent microbusinesses.
- Customer and revenue model: Retail and corporate customers buy single washes, prepaid packages, or recurring monthly memberships. Fixed sites combine automated payment and conveyor equipment with traffic management, customer assistance, chemistry control, equipment maintenance, site safety, and, for full-service formats, manual vacuuming and interior cleaning.
- Deviation from default lens: Narrowed for coherence to professionally operated fixed-site conveyor formats. Unattended self-service bays and purely mobile hand-detailing routes are excluded because their capital, labor, throughput, and automation economics are opposites; the narrowing is based on model coherence rather than attractiveness.

## Executive view
Fixed-site conveyor car washes are already heavily automated in payment and exterior cleaning, so incremental AI value lies in membership, staffing, chemistry, maintenance, and customer operations rather than replacing the wash tunnel. The lens excludes business models with opposite labor and capital structures so the primitives remain coherent.

## How AI changes the work
AI can improve member acquisition and retention, promotion targeting, customer support, staffing, chemical usage, equipment monitoring, preventive maintenance, incident review, and manager reporting. Existing kiosks and tunnels are the automation baseline; humans remain important for vehicle loading, prep, interior cleaning, equipment repair, chemistry, site safety, and exceptions.

## Value capture
Recurring memberships and local pricing allow some benefit to remain with the operator through retention, uptime, and lower variable use. Competitive site growth, discounting, cancellation, technology cost, maintenance, labor reassignment, and property economics limit retention.

## Firm availability
The official category is broad, while the fixed-site conveyor lens is narrower. Establishment counts overstate firms because many operators own multiple sites, and captive, mobile, unattended, micro, or out-of-band businesses further reduce the eligible control population.

## Demand durability
Light-duty travel offers a modest tailwind, and memberships can increase wash frequency. Weather, drought restrictions, household budgets, home washing, coatings, and new-site competition produce meaningful regional and cyclical risk.

## Risks and uncertainty
The main uncertainties are format mix, already-automated versus newly AI-exposed work, one-chain demand evidence, membership frequency economics, weather normalization, site-versus-company transaction structure, and conversion of owner intentions into external control sales.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4348 | — | OBSERVED | — |
| n | — | 186 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.31 | PROXY | S1, S2, S3 |
| rho | 0.45 | 0.66 | 0.82 | ESTIMATE | S3 |
| e | 0.55 | 0.72 | 0.86 | ESTIMATE | S1, S3, S5 |
| s5 | 0.06 | 0.12 | 0.2 | PROXY | S6 |
| q | 0.35 | 0.52 | 0.68 | ESTIMATE | S3 |
| d5 | 0.96 | 1.06 | 1.17 | PROXY | S3, S4 |
| o | 0.9 | 0.97 | 0.995 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.94 | 2.41 | 4.42 | ESTIMATE |
| F | 3.16 | 4.56 | 5.62 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.64 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational proxy covers oil change and other repair activities as well as car washes.
- a: Full-service interior sites are much more labor-intensive than express-exterior sites.
- rho: Existing tunnel and kiosk automation is not counted as new AI implementation.
- rho: Large chains have more data and integration capacity than typical lower-middle-market operators.
- e: Formats differ materially in labor, capital, throughput, and customer proposition.
- e: A portfolio of sites may be one firm, while one site can be held in multiple legal entities.
- s5: The Gallup survey is cross-industry and intention-based.
- s5: Real-estate ownership and operating control can transfer separately in this industry.
- q: Membership growth can shift timing and frequency without increasing constant-quality value per wash.
- q: Maintenance optimization benefits may accrue partly to equipment vendors or software providers.
- d5: One public chain is not representative of all regions and formats.
- d5: Revenue growth combines quantity, mix, price, memberships, and new-site effects.
- o: Accountable operator need is distinct from the number of employees physically present during each wash.
- o: Interior cleaning retains more direct operator labor than express exterior service.

## Sources
- **S1** — [2022 NAICS Definition: 811192 Car Washes](https://www.census.gov/naics/?details=8111&input=8111&year=2022) (accessed 2026-07-22): Official definition spanning fixed-site, self-service, mobile, and detailing activities, used to define and disclose the coherence narrowing.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 811190](https://www.bls.gov/oes/2023/may/naics5_811190.htm) (accessed 2026-07-22): Broad other-automotive occupational mix used cautiously as the task and attendant-labor proxy.
- **S3** — [Mister Car Wash, Inc. 2025 Annual Report on Form 10-K](https://www.sec.gov/Archives/edgar/data/1853513/000119312526078965/mcw-20251231.htm) (accessed 2026-07-22): Primary-company evidence on express and interior formats, kiosks, tunnels, self-vacuuming, memberships, labor and chemicals, comparable-store sales, and revenue drivers.
- **S4** — [2025 FHWA Forecasts of Vehicle Miles Traveled](https://www.fhwa.dot.gov/policyinformation/tables/vmt/vmt_forecast_sum.cfm) (accessed 2026-07-22): Light-duty vehicle-use growth used as a broad demand exposure proxy.
- **S5** — [2022 Economic Census: Other Services Basic Statistics](https://data.census.gov/table/ECNBASIC2022.EC2281BASIC?q=personal) (accessed 2026-07-22): Exact-industry establishment and revenue context used to qualify the firm population.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Employer-owner five-year sale and transfer intentions used as the broad starting point for the qualifying-control-transfer proxy.
