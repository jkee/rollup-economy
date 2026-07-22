# 485410 — School and Employee Bus Transportation

*v5.1 Stage 1 research memo. Run `485410-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.71 · L 1.24 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring contracted routes and a transferable compliance-heavy fleet operation support durable operator demand and acquisition eligibility.
**Weakness:** Drivers and monitors dominate labor, sharply limiting the share of wages addressable by near-term AI.

## Business-model lens
- Included: U.S. lower-middle-market private operators providing recurring outsourced school-pupil or employee bus transportation to school districts, schools, employers, and institutions under route, bus-day, unit-rate, or fixed-price service arrangements.
- Excluded: District- or employer-owned captive fleets, public transit, charter-only trips, shells, nontransferable one-person operations, and non-control financing vehicles.
- Customer and revenue model: Multi-route recurring service paid primarily by public school districts, private schools, employers, or institutions, commonly under competitively awarded fixed-price or per-bus, per-pupil, per-mile, route, or bus-day contracts with defined renewal and escalation terms.
- Deviation from default lens: none

## Executive view
School and employee bus transportation has exceptionally recurring customer demand and a transferable fleet-and-contract operating base, but its labor is concentrated in drivers and school-bus monitors whose core work is physical and safety-accountable. AI is therefore a focused coordination and back-office tool rather than a broad labor substitute.

## How AI changes the work
The strongest use cases are route and schedule exception support, substitute-driver coordination, parent and customer communications, document and incident intake, payroll checks, maintenance triage, compliance review, and bid preparation. Human dispatchers, supervisors, drivers, and monitors remain responsible for unusual events and student safety.

## Value capture
Fixed-price and unit-rate contracts can preserve savings during a term, but public procurement, competitive rebids, CPI-linked renewals, and cost scrutiny should share a meaningful portion with districts over five years. Savings that improve reliability may be retained better than visible reductions in required staffing.

## Firm availability
Most private LMM operators fit the recurring outsourced-service lens, and fleet, workforce, maintenance systems, compliance records, and contracts can form a transferable platform. Owner aging supports succession, but change-of-control consent, customer concentration, vehicle liabilities, and driver continuity can frustrate transactions.

## Demand durability
Enrollment projections are a mild headwind, yet schools continue to rely on bus transport and BLS expects school-driver employment to remain essentially flat over a decade. Remaining demand should overwhelmingly require an accountable operator because the service includes supervision, accessibility, safety, and incident response as well as driving.

## Risks and uncertainty
The principal risks are low task exposure in the largest occupations, already-deployed routing software, student-data constraints, public-sector price pressure, contract concentration, driver shortages, wage inflation, fleet replacement and electrification costs, and state-specific regulation. The employee-bus subset also makes the aggregate less uniform than school transport alone.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6264 | — | OBSERVED | — |
| n | — | 222 | — | ESTIMATE | — |
| a | 0.05 | 0.09 | 0.15 | PROXY | S1, S2 |
| rho | 0.4 | 0.55 | 0.7 | ESTIMATE | S1, S2 |
| e | 0.8 | 0.9 | 0.96 | ESTIMATE | S4 |
| s5 | 0.14 | 0.23 | 0.33 | PROXY | S5 |
| q | 0.4 | 0.55 | 0.69 | PROXY | S4 |
| d5 | 0.9 | 0.98 | 1.04 | PROXY | S2, S3 |
| o | 0.91 | 0.96 | 0.99 | PROXY | S2, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.50 | 1.24 | 2.63 | ESTIMATE |
| F | 5.23 | 6.19 | 6.86 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | PROXY |
| D | 8.19 | 9.41 | 10.00 | PROXY |

## Caveats
- a: OEWS covers employers of all sizes and does not isolate the LMM or outsourced-contract lens.
- a: Occupation shares do not reveal which tasks are already automated, and the table aggregates school and employee bus transportation.
- rho: No public study directly measures five-year AI implementation in private school-bus operators.
- rho: The estimate applies only to the exposed task pool and does not assume removal of drivers or monitors.
- e: The frozen firm count is estimated and does not disclose captive relationships or transfer restrictions.
- e: Employee shuttle and school transportation differ in customer concentration and contract duration, but both fit the recurring external-service lens.
- s5: The age evidence is economy-wide, from data year 2018, and counts responding owners rather than firms.
- s5: A sale of buses without operating contracts or qualified drivers is not a qualifying transfer.
- q: The source is New York-specific and contract rules vary by state and district.
- q: The estimate excludes implementation and demand effects and assumes unchanged safety and service quality.
- d5: NCES projections were prepared in 2022 and end in 2030, before most of the target five-year window.
- d5: Neither employment nor enrollment directly measures constant-price, constant-quality outsourced bus service quantity.
- o: NHTSA's consumer-vehicle discussion is not specific to heavy school buses or commercial pilots.
- o: Operator-required does not require every current role to remain, and district insourcing would remove quantity from the outsourced lens even if service continues.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 485400](https://www.bls.gov/oes/2023/may/naics4_485400.htm) (accessed 2026-07-22): Reports 197,550 employees: school-bus drivers were 65.47%, school-bus monitors 15.10%, maintenance and repair occupations 3.56%, office and administrative support 3.44%, and dispatchers 1.43%, with occupation-specific mean wages.
- **S2** — [Occupational Outlook Handbook: Bus Drivers](https://www.bls.gov/ooh/transportation-and-material-moving/bus-drivers.htm) (accessed 2026-07-22): Projects school-bus-driver employment at 387,300 in 2024 and 388,200 in 2034, states schools will continue relying on drivers while enrollment decline constrains demand, and describes school-driver safety, accessibility, supervision, and discipline duties.
- **S3** — [NCES Projections of Education Statistics: Elementary and Secondary Enrollment](https://nces.ed.gov/programs/PES/section-1.asp) (accessed 2026-07-22): Projects public elementary and secondary enrollment to decrease 4% from 2020 to 2030 to 47.3 million and private enrollment to decrease 12% from 2019 to 2030 to 4.8 million.
- **S4** — [New York State Education Department: Annual Extensions of Transportation Contracts](https://www.p12.nysed.gov/schoolbus/regulations/html/section156.5_annual_extensions_of_transportation_contracts.html) (accessed 2026-07-22): Documents competitive-bid eligibility for extensions and fixed-price, per-bus, per-pupil, per-mile, and combination unit-rate contracts, with extension increases generally capped by regional CPI and supported by operating-cost evidence.
- **S5** — [Business Owners' Ages: Over Half of U.S. Business Owners Were Age 55 and Over](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 Annual Business Survey, data year 2018.
- **S6** — [Automated Vehicle Safety](https://www.nhtsa.gov/vehicle-safety/automated-vehicles-safety) (accessed 2026-07-22): States that current consumer vehicles require driver attention, Level 4 and Level 5 consumer vehicles are unavailable, and higher-automation testing remains limited to restricted locations and conditions.
