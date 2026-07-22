# 812930 — Parking Lots and Garages

*v5.1 Stage 1 research memo. Run `812930-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 5.25 · L 3.44 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digital payment, remote support, enforcement, pricing, and scheduling can improve a labor-intensive recurring operation with measurable client relationships.
**Weakness:** Management-contract pass-through and site-level physical obligations constrain retained economics even when automation is feasible.

## Business-model lens
- Included: US lower-middle-market firms providing hourly, daily, or monthly vehicle parking, valet parking, and outsourced parking-facility operations to motorists or property owners, including management-contract and leased-facility models.
- Excluded: Extended vehicle storage classified in 493190, property owners that only lease real estate without operating parking services, captive internal parking departments, software-only parking platforms without accountable operations, municipal departments, and firms outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: Operators collect transient or monthly parking fees from motorists and/or fixed, variable, performance, technology, and ancillary-service fees from property owners. Work spans staffing, valet, customer assistance, payment and revenue control, enforcement, facility upkeep, shuttle operations, marketing, and technology-enabled access or reservations.
- Deviation from default lens: none

## Executive view
Parking operations combine a high compensation burden with proven mobile, remote-monitoring, revenue-management, and enforcement technology, creating meaningful workflow opportunity. The service remains site-specific and operationally accountable, while management-contract economics, rebidding, and cost reimbursement limit how much benefit an operator retains.

## How AI changes the work
AI can handle routine customer contacts, detect payment or enforcement exceptions, forecast occupancy, support dynamic pricing, reconcile revenue, optimize staffing and shuttle schedules, and monitor equipment. It cannot eliminate valet and shuttle driving, patrol, cleaning, repairs, safety response, client accountability, or site-specific judgment.

## Value capture
Lease operators may retain gains until rent or pricing resets, but outsourced management clients often fund payroll and operating costs and negotiate fees on short contracts. Performance fees, technology fees, convenience fees, and better utilization provide capture paths, though competitive renewal pressure is strong.

## Firm availability
The code is centered on operating lots, garages, and valet services, and a fragmented market supports a population of independent operators. Transfer quality depends on durable client contracts and local density; the supplied LMM count is still only a margin-bridged estimate.

## Demand durability
Parking demand is diversified across many destinations but location-specific. Hybrid work and mobility substitution weaken some office facilities, while hospitals, residential properties, travel, events, and outsourced municipal or institutional operations are more durable.

## Risks and uncertainty
Key risks are missing six-digit task and transfer data, a large-operator source outside the LMM band, client contract termination or rebid, wage and insurance pressure, payment and privacy regulation, uneven site hardware, and long-run changes in commuting, land use, and vehicle ownership.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.478 | — | OBSERVED | — |
| n | — | 113 | — | ESTIMATE | — |
| a | 0.24 | 0.36 | 0.49 | ESTIMATE | S1, S2 |
| rho | 0.32 | 0.5 | 0.68 | ESTIMATE | S2 |
| e | 0.7 | 0.85 | 0.95 | ESTIMATE | S1, S2 |
| s5 | 0.11 | 0.21 | 0.34 | ESTIMATE | S2 |
| q | 0.14 | 0.29 | 0.48 | ESTIMATE | S2 |
| d5 | 0.82 | 0.99 | 1.17 | ESTIMATE | S1, S2 |
| o | 0.52 | 0.69 | 0.83 | ESTIMATE | S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.47 | 3.44 | 6.37 | ESTIMATE |
| F | 3.66 | 4.91 | 5.83 | ESTIMATE |
| C | 2.80 | 5.80 | 9.60 | ESTIMATE |
| D | 4.26 | 6.83 | 9.71 | ESTIMATE |

## Caveats
- a: No six-digit task-exposure study was found; SP Plus was a large diversified operator with aviation and technology operations beyond the LMM parking lens.
- rho: The source demonstrates technical and operational feasibility but does not measure AI adoption or realized labor substitution at LMM operators.
- e: The supplied firm count is margin-bridged and NAICS primary activity does not establish independence, contract recurrence, or the exact EBITDA band.
- s5: Industry fragmentation and one large-company acquisition do not establish an LMM annual transfer rate; purchases of isolated contracts are not necessarily qualifying control sales.
- q: SP Plus reported 88% of commercial locations under management contracts, but the revenue and contract mix of independent LMM firms may differ materially.
- d5: The cited 94% commercial-facility retention rate measures client retention at one large operator, not constant-quality parking demand or future vehicle volume.
- o: Software platforms and property owners may internalize parts of the workflow, while valet, shuttle, and maintenance-heavy locations require much more operator labor than automated garages.

## Sources
- **S1** — [2022 NAICS Definition: 812930 Parking Lots and Garages](https://www.census.gov/naics/?input=812930&year=2022&details=812930) (accessed 2026-07-22): Defines the industry as establishments providing parking space hourly, daily, or monthly and/or valet parking services, while excluding extended vehicle storage.
- **S2** — [SP Plus Corporation 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1059262/000095017024021554/sp-20231231.htm) (accessed 2026-07-22): Describes management and lease contracts, personnel and revenue-control responsibilities, mobile and online parking, remote 24-hour support, enforcement, valet, shuttle and maintenance services; reports typical management terms of 1-3 years, lease terms of 3-10 years, 88% of commercial locations under management contracts, and 94% commercial-facility retention in 2023.
