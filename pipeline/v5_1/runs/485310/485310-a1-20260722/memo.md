# 485310 — Taxi and Ridesharing Services

*v5.1 Stage 1 research memo. Run `485310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.31 · L 2.12 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Very high reported compensation intensity and a broad, already-digital dispatch, service, billing, compliance, and analytics workload.
**Weakness:** Commercial autonomous ride-hailing and software marketplaces can displace the local fleet/dispatch operator itself, not merely automate its staff.

## Business-model lens
- Included: Locally or regionally controlled taxi and ridesharing fleet or dispatch operators in the roughly $1-10M normalized EBITDA band that remain accountable for recurring passenger transportation, including contracted and retail trips.
- Excluded: Global software-only ride-hailing marketplaces, individual owner-drivers, limousine-only and shuttle-only businesses, nonemergency medical transportation classified elsewhere, captive fleets, vehicle lessors without operating responsibility, and financing vehicles.
- Customer and revenue model: Repeated metered, zone, app-dispatched, account, or contracted passenger trips paid by riders, institutions, insurers, or public programs; operators may own vehicles, lease them to drivers, employ drivers, or charge dispatch and affiliation fees.
- Deviation from default lens: NAICS 485310 mixes global software marketplaces, individual independent drivers, and locally accountable fleet/dispatch businesses whose labor models, economics, and transferability are not coherent in one screen. The lens retains the LMM fleet/dispatch operator population and excludes software-only marketplaces and individual owner-drivers for business-model coherence.

## Executive view
Local taxi and ridesharing fleet/dispatch operators have substantial workflow automation potential, especially in dispatch, customer service, account billing, driver administration, compliance, and fleet analytics. The opportunity is offset by the most direct AI-native substitution threat in the screen: software marketplaces and commercially scaled autonomous ride-hailing can remove the local operator layer from part of the trip base.

## How AI changes the work
Generative and predictive systems can handle bookings, routine calls and messages, trip assignment, ETA communication, driver onboarding, billing documents, lost-item workflows, fraud triage, demand forecasting, and maintenance diagnostics. These are implementable around a human-driven fleet. Fully autonomous driving is analytically separate: it changes who supplies the ride and therefore reduces operator-required demand for traditional LMM fleets rather than merely improving their back office.

## Value capture
Regulated fares, fixed institutional prices, and affiliation fees can preserve savings between repricing events. Driver-pay rules, insurance, accessibility, vehicle investment, platform competition, and contract renewals share or consume the gain. Capture varies sharply by whether the operator employs drivers, leases vehicles, charges dispatch fees, or holds fixed-price customer accounts.

## Firm availability
The frozen dataset estimates 22 firms in the EBITDA band, but the coherent target population is smaller after excluding platforms, individuals, limousine or shuttle models, and firms without transferable licenses or operating responsibility. Fleet, account, permit, and driver-network transferability must be proven. Competitive pressure may prompt sales, but can just as easily cause asset liquidation.

## Demand durability
Underlying demand for paid point-to-point mobility should grow modestly with ride-hailing adoption, aging, disability transport, events, tourism, and urban travel. The crucial issue is not trip disappearance but supplier substitution: independent app-based drivers and autonomous fleets can take quantity from local operators. Smaller markets and accessible or contracted service should be more durable than dense-city retail taxi trips.

## Risks and uncertainty
The NAICS code is unusually heterogeneous and public employment data are distorted by global platforms and widespread self-employment. Key risks are rapid autonomous expansion, platform network effects, regulated driver pay, insurance, fleet electrification, accessibility investment, customer concentration, weak permit transferability, and inability of small operators to integrate modern dispatch systems. The compensation ratio is also distorted by a 2024 wage/2022 receipts vintage mismatch and platform-heavy payrolls, while n is estimated.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 1.5233 | — | OBSERVED | — |
| n | — | 22 | — | ESTIMATE | — |
| a | 0.2 | 0.31 | 0.45 | PROXY | S1, S2 |
| rho | 0.33 | 0.52 | 0.68 | ESTIMATE | S1, S4 |
| e | 0.28 | 0.48 | 0.68 | ESTIMATE | S2, S4 |
| s5 | 0.12 | 0.26 | 0.42 | ESTIMATE | S4 |
| q | 0.36 | 0.56 | 0.73 | ESTIMATE | S4 |
| d5 | 0.96 | 1.07 | 1.2 | PROXY | S2, S3, S4 |
| o | 0.45 | 0.68 | 0.87 | PROXY | S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 4.02 | 9.82 | 10.00 | ESTIMATE |
| F | 0.89 | 2.12 | 3.19 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 4.32 | 7.28 | 10.00 | PROXY |

## Caveats
- a: The BLS industry is broader than both NAICS 485310 and the narrowed lens.
- a: Largest-occupation counts omit a complete wage matrix and are heavily influenced by large platform employers.
- a: Driving exposure is kept low because deployable autonomous service is treated mainly in o, not double-counted as ordinary five-year implementation.
- rho: No source directly measures five-year implementation across LMM taxi fleets.
- rho: Large platforms have software capabilities and data volumes that small operators may not replicate.
- rho: Regulated service, accessibility, and driver-pay rules constrain workflow redesign.
- e: No source directly identifies eligible firms within frozen n.
- e: BLS reports that 92% of taxi-driver jobs are self-employed, illustrating a large population outside the transferable-firm lens but not measuring the firm count.
- e: The frozen n is itself a margin-bridged estimate.
- s5: No direct control-transfer series exists for the narrowed lens.
- s5: Medallion, permit, vehicle, or customer-account sales are not qualifying unless control of transferable operations changes.
- s5: Competitive distress can produce liquidation rather than a going-concern transfer.
- q: Revenue models vary materially across metered taxi, driver-affiliation, app-dispatched, and contracted accounts.
- q: New York regulation is evidence of the mechanism, not a national estimate.
- q: Savings may be absorbed by driver retention, insurance, fleet electrification, or accessibility mandates.
- d5: Employment projections are not direct quantity forecasts and contain conflicting industry and occupation signals.
- d5: Large metropolitan ride-hailing growth may not represent smaller local markets.
- d5: Trips depend on tourism, commuting, public transit quality, household vehicle ownership, fares, and regulation.
- o: Waymo volume is company-reported and concentrated in selected geographies.
- o: Autonomous fleets still require an accountable fleet-management organization, but not necessarily one of the lens's local taxi/dispatch kind.
- o: Regulatory reversals, safety events, capital constraints, weather, and accessibility requirements could materially slow displacement.

## Sources
- **S1** — [Data Tables for OEWS Industry Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Largest occupation counts for Taxi and Limousine Service, including 24,300 shuttle drivers/chauffeurs, 16,660 taxi drivers, 6,720 software developers, 4,550 dispatchers, 1,150 customer service representatives, and 990 data scientists.
- **S2** — [Taxi Drivers, Shuttle Drivers, and Chauffeurs: Occupational Outlook Handbook](https://www.bls.gov/ooh/transportation-and-material-moving/taxi-drivers-and-chauffeurs.htm) (accessed 2026-07-22): Reports 92% of taxi drivers are self-employed, describes dispatch-company fee relationships, and projects 9% combined occupation growth from 2024 to 2034, including 11% for taxi drivers.
- **S3** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects Taxi and Limousine Service wage-and-salary employment from 71,200 in 2024 to 67,900 in 2034, a 4.6% decline.
- **S4** — [New York City Taxi and Limousine Commission 2024 Annual Report](https://www.nyc.gov/assets/tlc/downloads/pdf/annual_report_2024.pdf) (accessed 2026-07-22): Documents regulated taxis and for-hire vehicles, permanent flexible-fare rules, increased minimum per-trip rideshare driver pay, accessibility requirements, and expanded regulator data reporting.
- **S5** — [Waypoint: The Official Waymo Blog](https://waymo.com/blog/) (accessed 2026-07-22): Waymo reports more than half a million fully autonomous trips per week across ten U.S. cities by March 2026 and ongoing expansion, while also describing fleet-management operations partners.
- **S6** — [California Public Utilities Commission Resolution TL-19144](https://docs.cpuc.ca.gov/PublishedDocs/Published/G000/M512/K885/512885814.PDF) (accessed 2026-07-22): Official approval for Waymo to offer fare-charging passenger service without a safety driver throughout San Francisco, demonstrating legally deployed driverless taxi service.
