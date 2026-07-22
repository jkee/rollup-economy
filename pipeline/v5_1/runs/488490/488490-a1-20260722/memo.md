# 488490 — Other Support Activities for Road Transportation

*v5.1 Stage 1 research memo. Run `488490-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.24 · L 1.00 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical road-support demand paired with dispatch, documentation, scheduling, and billing workflows that can absorb practical AI assistance.
**Weakness:** Severe business-model heterogeneity and competitive public or unit-priced contracts make both firm eligibility and retained economics uncertain.

## Business-model lens
- Included: US lower-middle-market firms providing repeat outsourced street sweeping, road-transport inspection or weighing, truck loading and unloading, shared terminal or maintenance-facility services, and contracted toll-road, bridge, tunnel, or related road-network operations to external customers.
- Excluded: Motor vehicle towing and emergency roadside service classified in 488410; captive facilities used only by an owner's vehicles; government-operated road assets; shells, non-control financing vehicles, and businesses without transferable recurring operations.
- Customer and revenue model: Customers include municipalities and road agencies, commercial fleets and carriers, terminal users, and infrastructure owners. Revenue ranges from multi-year fixed-price or unit-price service contracts and scheduled recurring work to usage fees and availability-payment or concession arrangements.
- Deviation from default lens: The default lens is narrowed to recurring or repeat outsourced operating services because this code combines equipment-based municipal services, freight-handling services, shared facilities, inspections, and infrastructure concessions whose economics are otherwise incoherent in one operating-company screen.

## Executive view
This is a heterogeneous set of road-network support services with repeat physical work and a meaningful but bounded information-work layer. AI can improve dispatch, intake, routing, records, billing, compliance support, and exception handling, yet most wages remain tied to vehicle operation, material handling, mechanical work, and accountable field execution. Contract durability is plausible, but public procurement and transparent unit pricing can return savings to customers at renewal.

## How AI changes the work
Near-term impact is assistive and workflow-oriented: voice and text agents structure requests, dispatch tools propose schedules and routes, document systems extract work orders and compliance data, and copilots draft customer communications and reconcile billing. Human dispatchers still manage unusual events, customer conflict, safety, and crew coordination; drivers, mechanics, sweepers, and handlers continue physical execution.

## Value capture
Fixed-price and unit-price contracts can preserve savings during a contract term, especially where automation avoids new hires. Over five years, competitive rebids, CPI-linked pricing, benchmarking, customer negotiation, and visible service units should share part of the benefit, while differentiated responsiveness and reliability may protect some margin.

## Firm availability
Contract sweeping, handling, inspection, and shared-facility businesses can be transferable operating companies, but the code also contains captive facilities, public assets, and concession structures that do not fit a conventional control acquisition. Succession should create some supply, although no industry-specific transfer rate was found and small-business owners may work beyond conventional retirement ages.

## Demand durability
Road use is forecast to grow modestly, and physical cleaning, handling, inspection, and infrastructure accountability remain necessary. Demand can nevertheless be locally volatile because municipal budgets, rebids, insourcing, regulation, weather, and customer concentration matter more than national VMT for an individual operator.

## Risks and uncertainty
The largest uncertainty is activity mix: 488490 spans municipal equipment services, freight handling, inspections, facilities, and large infrastructure operations. The available occupation data include towing, the firm count is margin-bridged, and no source directly measures eligibility, transfers, benefit retention, or operator-required demand. Safety incidents, labor and insurance inflation, fleet capital needs, public-contract loss, and autonomous or remote inspection technology can overwhelm administrative AI savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3737 | — | OBSERVED | — |
| n | — | 112 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.23 | PROXY | S2, S3, S4, S5 |
| rho | 0.3 | 0.48 | 0.68 | ESTIMATE | S3, S6 |
| e | 0.4 | 0.62 | 0.8 | ESTIMATE | S1, S8 |
| s5 | 0.1 | 0.18 | 0.3 | ESTIMATE | S9 |
| q | 0.35 | 0.55 | 0.75 | ESTIMATE | S8, S10 |
| d5 | 1.01 | 1.04 | 1.08 | PROXY | S7 |
| o | 0.85 | 0.94 | 0.98 | ESTIMATE | S1, S11 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.36 | 1.00 | 2.34 | ESTIMATE |
| F | 2.74 | 4.19 | 5.35 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.59 | 9.78 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation mix is reported at NAICS 4884 and includes 488410 motor vehicle towing.
- a: O*NET reports occupation-wide tasks, not time shares or 488490-specific task execution.
- a: The estimate covers not-yet-automated current tasks and excludes autonomous driving or fully robotic field operations that are not plausibly deployable across the lens within five years.
- rho: Census AI adoption figures cover all US employer businesses rather than 488490 or the LMM band.
- rho: Implementation could be faster for standardized dispatch and clerical work but slower for public infrastructure operations and safety-critical inspection.
- rho: This primitive excludes demand, pricing, and valuation effects.
- e: No source reports eligibility under the frozen lens.
- e: The injected firm count is margin-bridged and may not reflect the code's activity mix.
- e: Government contracting and infrastructure concessions create materially different control and renewal risks.
- s5: The SBA retirement study is old, economy-wide, and based on individuals rather than 488490 firms or observed transfers.
- s5: Private small-company transactions are incompletely reported.
- s5: Concession changes and public contract awards are not automatically qualifying transfers.
- q: Public street-sweeping contracts illustrate only one activity inside the code.
- q: Toll concessions and shared-terminal fees may have very different indexation and demand-risk terms.
- q: The estimate excludes implementation difficulty, demand loss, and valuation effects.
- d5: VMT is an indirect demand driver and not an output measure for 488490.
- d5: The code combines services with different exposure to passenger, single-unit truck, and combination-truck mileage.
- d5: Municipal fiscal stress, regulatory changes, severe weather, or insourcing can dominate VMT at local firms.
- o: There is no measured 488490 operator-required share.
- o: Virtual inspection may materially reduce staffing or station stops without eliminating the accountable operator.
- o: The estimate is for the current service basket and does not credit new digital services.

## Sources
- **S1** — [2022 Economic Census Transportation and Warehousing Survey Form: Support Activities for Transportation](https://bhs.econ.census.gov/ombpdfs2022/export/2022_TW-48800_su.pdf) (accessed 2026-07-22): The Census form lists 488490 activities including street sweeping, road-transport inspection or weighing, toll road/bridge/tunnel operation, truck loading or unloading, and non-captive terminal or maintenance facilities; it separately classifies towing and emergency roadside service in 488410.
- **S2** — [BLS May 2024 OEWS Data Tables for Industry Employment Charts](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): For the broader Support Activities for Road Transportation industry, the ten largest occupations include 52,190 heavy truck drivers, 8,560 dispatchers, 5,460 laborers/material movers, 4,870 office clerks, 4,330 general and operations managers, 3,810 industrial truck operators, 3,520 automotive technicians, 3,070 diesel mechanics, 2,980 light truck drivers, and 2,960 first-line transportation/material-moving supervisors.
- **S3** — [O*NET OnLine: Dispatchers, Except Police, Fire, and Ambulance](https://www.onetonline.org/link/summary/43-5032.00) (accessed 2026-07-22): Dispatcher tasks include scheduling crews and vehicles, preparing run schedules, receiving and relaying work orders, maintaining service and charge records, monitoring locations and utilization, responding to customers, and coordinating repairs; the page also reports daily telephone use and frequent decision-making.
- **S4** — [O*NET OnLine: Heavy and Tractor-Trailer Truck Drivers](https://www.onetonline.org/link/summary/53-3032.00) (accessed 2026-07-22): The occupation includes tow truck drivers and is centered on driving, inspecting and securing loads and equipment, maintenance, physical coupling and loading tasks, with paperwork, logs, routing, and communications as subsidiary tasks; 96% report operating an enclosed vehicle or equipment every day.
- **S5** — [O*NET OnLine: Office Clerks, General](https://www.onetonline.org/link/summary/43-9061.00) (accessed 2026-07-22): Office-clerk tasks include calls, customer communications, database and file maintenance, record compilation, document review, data checking, schedules, correspondence, billing documents, forms, and basic bookkeeping.
- **S6** — [Census Bureau: Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS data from December 2025 to May 2026 show overall business AI use around 17%-20%, expected six-month use around 20%-23%, 37% use among firms with at least 250 employees, and less than 20% use among firms with four or fewer employees.
- **S7** — [FHWA 2025 Forecasts of Vehicle Miles Traveled](https://www.fhwa.dot.gov/policyinformation/tables/vmt/vmt_forecast_sum.cfm) (accessed 2026-07-22): FHWA projects baseline total VMT growth of 0.7% annually through 2043, with a 0.5%-1.0% range across pessimistic and optimistic outlooks; baseline growth is 0.6% for light-duty vehicles, 2.1% for single-unit trucks, and 1.0% for combination trucks.
- **S8** — [City of Minnetrista Street Sweeping Services Agreement](https://www.cityofminnetrista.gov/media/5706) (accessed 2026-07-22): The municipal agreement provides twice-yearly sweeping over approximately 56 paved-road miles under a three-year contract, with stated annual and per-mile fixed prices that rise by contract year.
- **S9** — [SBA Office of Advocacy: Retirement, Recessions and Older Small Business Owners](https://advocacy.sba.gov/2012/12/01/retirement-recessions-and-older-small-business-owners/) (accessed 2026-07-22): The study reports that small-business owners in 2010 expected to retire at an average age of 72.6 versus 68.4 for employees, cautioning against assuming rapid retirement-driven transfer timing.
- **S10** — [City of Palo Alto Street Sweeping Contract Staff Report](https://www.paloalto.gov/files/assets/public/v/1/agendas-minutes-reports/reports/city-manager-reports-cmrs/year-archive/2020/id-11012.pdf?t=58367.35) (accessed 2026-07-22): The report describes a five-year street-sweeping contract, competitive proposal economics, service changes, and projected annual price increases tied to CPI and operating-cost factors.
- **S11** — [FHWA Concept of Operations for Virtual Weigh Stations](https://ops.fhwa.dot.gov/publications/fhwahop09051/foreword.htm) (accessed 2026-07-22): FHWA describes virtual weigh stations as roadside technology deployments for screening and enforcement, demonstrating potential substitution of remote sensing and software for some traditional station activity without removing public or contractor accountability.
