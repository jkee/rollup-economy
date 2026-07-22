# 484110 — General Freight Trucking, Local

*v5.1 Stage 1 research memo. Run `484110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.61 · L 1.28 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent physical freight demand plus automatable coordination and document workflows creates a focused operating-improvement opportunity.
**Weakness:** Most compensation remains in physical driver work while competitive contract renewal can transfer a large share of visible savings to shippers.

## Business-model lens
- Included: U.S. lower-middle-market employer firms providing recurring or repeat, for-hire local transportation of palletized general freight for external shippers, including local truckload and less-than-truckload operations and incidental terminal or storage activity, typically on same-day metropolitan-area routes.
- Excluded: Captive private fleets, shells, non-control financing vehicles, freight brokers and independent terminals, couriers and small-item delivery, specialized freight, household moving, long-distance trucking, independent drivers without transferable operations, and firms outside the roughly $1-10 million normalized EBITDA band.
- Customer and revenue model: Business shippers and logistics intermediaries buy recurring lane, route, pickup-and-delivery, or dedicated-capacity service under negotiated contracts, with overflow and irregular loads priced transactionally; revenue is generally tied to loads, miles, stops, weight, time, or committed capacity.
- Deviation from default lens: none

## Executive view
Local general freight is a physically indispensable, repeat business service with a substantial pool of LMM firms, but it is not a broad labor-replacement story. The implementable AI case is concentrated in dispatch, routing, customer updates, document handling, billing, and maintenance decisions. Durable shipment demand and continued carrier accountability support the model; competitive rebidding and uneven firm quality limit retained economics.

## How AI changes the work
AI can optimize multi-stop routes, triage exceptions, answer routine tracking questions, process invoices and bills of lading, and flag maintenance needs. Those workflows sit mainly in the administrative and coordination layer. Driving, loading, cargo securement, inspection, customer-site handling, and safety responsibility dominate the workforce and remain much less substitutable over five years.

## Value capture
Savings should initially accrue to the operator where rates are fixed or relationship-based, especially when better routing and service reduce empty miles or support more volume. Retention erodes as contracts renew, shippers benchmark lanes, and competitors bid away visible cost advantages. Differentiated reliability and embedded customer workflows matter more than raw automation savings.

## Firm availability
Most in-band employer carriers should satisfy the outsourced repeat-service lens, but some are spot-dependent, owner-driven, customer-concentrated, poorly documented, or operationally inseparable from the seller. National employer-owner surveys indicate meaningful five-year transfer intent, yet actual qualifying control transfers will be fewer than stated plans.

## Demand durability
The current basket is anchored in physical goods movement, and national freight tonnage is forecast to expand. Local trucking also benefits from metropolitan pickup, sorting, transfer, and delivery needs. Cyclicality, insourcing by large shippers, network redesign, and changing shipment density can still reduce demand for a given carrier even when systemwide freight grows.

## Risks and uncertainty
The largest evidence gaps are six-digit occupation and task data, realized AI labor outcomes at small fleets, contract-level pass-through, and completed trucking control transfers. Safety and compliance errors, weak data, legacy TMS integration, customer concentration, equipment liabilities, driver availability, insurance, and rate competition can overwhelm back-office productivity. A weak acquisition thesis would combine spot exposure, commoditized lanes, deferred maintenance, poor safety records, and an owner who personally dispatches and drives.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3423 | — | OBSERVED | — |
| n | — | 573 | — | ESTIMATE | — |
| a | 0.1 | 0.17 | 0.25 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S3, S4 |
| e | 0.65 | 0.82 | 0.92 | ESTIMATE | S1 |
| s5 | 0.1 | 0.18 | 0.26 | PROXY | S5 |
| q | 0.2 | 0.4 | 0.62 | ESTIMATE | S7, S8 |
| d5 | 0.96 | 1.07 | 1.15 | PROXY | S6, S9 |
| o | 0.88 | 0.96 | 0.99 | PROXY | S1, S4, S9, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.48 | 1.28 | 2.46 | ESTIMATE |
| F | 5.86 | 7.16 | 7.93 | ESTIMATE |
| C | 4.00 | 8.00 | 10.00 | ESTIMATE |
| D | 8.45 | 10.00 | 10.00 | PROXY |

## Caveats
- a: The occupational mix is for four-digit NAICS 484 and employers of all sizes, not six-digit local general freight or the LMM band.
- a: OEWS excludes self-employed workers and reports occupations, not task shares or prior automation.
- a: The estimate treats autonomous driving separately from near-term generative and analytical AI exposure and does not count wholesale driver replacement as exposed current work.
- rho: USDOT identifies applications and risks but does not measure five-year adoption or labor realization in NAICS 484110.
- rho: Implementation can improve service or throughput without reducing payroll, so productivity adoption is not automatically avoidable hiring.
- rho: Small-carrier data quality and legacy-system integration are not quantified.
- e: No public dataset measures the frozen lens's recurring-revenue, transferability, and control-eligibility tests jointly.
- e: The frozen firm-count input is an estimate and may include firms whose normalized EBITDA or owner dependence is misclassified.
- e: NAICS is establishment-based, while eligibility is assessed at the firm level.
- s5: Gallup covers employer businesses across industries and sizes, not NAICS 484110 or the LMM band.
- s5: Survey responses measure plans, not completed transactions, and the category includes gifts and rare public offerings.
- s5: Owner age is national employer-business context, not a trucking-specific age distribution.
- q: The competition study is old and not restricted to NAICS 484110, although its structural description remains directionally relevant.
- q: BTS's one-tenth statistic concerns the overall common-carrier spot market, not local general freight specifically.
- q: Savings from better utilization may be retained differently from visible reductions in labor or accessorial charges.
- d5: The FAF forecast is national, multimodal, and long-horizon rather than a direct five-year forecast for local general freight.
- d5: Tonnage is an imperfect proxy for constant-quality local trucking service quantity because stops, shipment size, distance, and handling complexity can change.
- d5: The 2020 base year was affected by pandemic-era freight patterns.
- o: Driver employment is not identical to operator-required service quantity and can grow even while automation penetrates selected routes.
- o: GAO's automation evidence is from 2019 and focused on long-haul trucking; technology can advance nonlinearly.
- o: The estimate concerns retention of an accountable carrier, not retention of every current driving job.

## Sources
- **S1** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines NAICS 484110 as local general freight trucking of generally palletized commodities in containers or van trailers, usually within a metropolitan area and generally on same-day return trips; distinguishes long-distance, specialized freight, terminals, and other activities.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 484000 Truck Transportation](https://www.bls.gov/oes/2023/may/naics4_484000.htm) (accessed 2026-07-22): Reports 1,577,900 jobs; driver/sales workers and truck drivers at 62.99% of employment, transportation and material moving at 74.75%, office and administrative support at 11.32%, and dispatchers at 2.42%, with occupation-level mean wages used to approximate wage weights.
- **S3** — [Formal Recommendations of the Transforming Transportation Advisory Committee, December 2024](https://www.transportation.gov/sites/dot.gov/files/2025-01/TTAC%202024%20Report.pdf) (accessed 2026-07-22): Documents freight and transportation uses of AI for multi-stop route optimization, predictive fleet maintenance, customer inquiries, shipment tracking and updates, invoices, bills of lading, and document processing; also identifies hallucination, context, privacy, cybersecurity, and data-quality risks.
- **S4** — [Incorporating AI impacts in BLS employment projections: occupational case studies](https://www.bls.gov/opub/mlr/2025/article/incorporating-ai-impacts-in-bls-employment-projections.htm) (accessed 2026-07-22): Explains that technology employment effects tend to occur gradually; BLS judged autonomous-trucking effects too uncertain for short-to-medium-term adjustment, cites regulatory and public-safety constraints, and reports no meaningful employment impact through 2023.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports a fall-2024 U.S. survey in which 22% of employer-business owners planned to sell or transfer ownership within five years, versus 9% of nonemployers; also reports 52.3% of employer businesses owned by people age 55 or older.
- **S6** — [Freight Activity in the U.S Expected to Grow Fifty Percent by 2050](https://www.bts.gov/newsroom/freight-activity-us-expected-grow-fifty-percent-2050) (accessed 2026-07-22): Reports FAF5 projections of 50% growth in U.S. freight tonnage from 2020 to 2050, with trucks carrying 65% of current tonnage and expected to remain the predominant mode.
- **S7** — [Latest Supply Chain and Freight Indicators](https://www.bts.gov/freight-indicators) (accessed 2026-07-22): States that truck spot-market loads are approximately one-tenth of the overall common-carrier trucking market and defines them as shipments outside pre-existing hauling contracts, supporting the prevalence of contract or relationship pricing.
- **S8** — [A Novel Approach to Routing and Dispatching Trucks Based on Partial Information in a Dynamic Environment](https://rosap.ntl.bts.gov/view/dot/37454) (accessed 2026-07-22): A DOT-sponsored research abstract describes trucking as highly competitive, easy to enter, relatively undifferentiated, and thin-margin, and describes routing and dispatch under uncertain orders, congestion, and travel times.
- **S9** — [Heavy and Tractor-trailer Truck Drivers](https://www.bls.gov/ooh/transportation-and-material-moving/heavy-and-tractor-trailer-truck-drivers.htm) (accessed 2026-07-22): Projects heavy and tractor-trailer truck-driver employment to grow 4% from 2024 to 2034 and describes physical, regulatory, inspection, cargo-securement, routing, logging, and maintenance-reporting duties.
- **S10** — [Automated Trucking: Federal Agencies Should Take Additional Steps to Prepare for Potential Workforce Effects](https://www.gao.gov/products/gao-19-161) (accessed 2026-07-22): Reports that automated-truck development focused on highway portions of long-haul routes, widespread deployment was viewed as years or decades away, and one scenario retained operators for complex driving and non-driving tasks.
