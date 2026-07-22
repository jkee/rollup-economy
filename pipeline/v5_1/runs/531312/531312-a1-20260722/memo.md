# 531312 — Nonresidential Property Managers

*v5.1 Stage 1 research memo. Run `531312-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 6.90 · L 4.38 · interval CONDITIONAL → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is the combination of recurring commercial property-management mandates and automatable lease, accounting, reporting, communication, and work-order workflows.
**Weakness:** The principal weakness is that many labor costs are reimbursed or operationally essential, while commercial real-estate cycles and client rebids can pass savings through or erode mandates.

## Business-model lens
- Included: U.S. lower-middle-market firms that repeatedly manage office, industrial, retail, and other nonresidential real estate for external owners and investors, including lease administration, property accounting, tenant coordination, vendor oversight, inspections, maintenance coordination, and owner reporting.
- Excluded: Residential property management, property ownership and leasing for the firm's own account, brokerage-only and transaction-only work, facilities or project management without recurring property-management responsibility, captive owner departments, shell entities, non-control financing situations, and firms outside the target normalized-EBITDA band.
- Customer and revenue model: Commercial property owners and investors pay recurring monthly fees based on a fixed amount or a percentage of rental income or receipts; contracts may also reimburse property-dedicated administrative and payroll costs and may include separately priced leasing, engineering, or project services.
- Deviation from default lens: none

## Executive view
Nonresidential property management is a recurring outsourced service with a meaningful administrative layer that AI can compress, while physical operations, tenant relationships, vendor control, and accountable client service keep a human operator central. Commercial real-estate cycles and reimbursed-cost billing temper the value-capture case.

## How AI changes the work
AI can assist lease abstraction, accounts payable, rent-roll review, owner reporting, budgeting, tenant communications, work-order triage, vendor documentation, and portfolio analytics. Managers still inspect properties, direct contractors, negotiate, resolve disputes, manage emergencies, and own the accuracy and service consequences of decisions.

## Value capture
Fixed monthly and rent-linked fees can preserve part of productivity gains, especially in central administration. Savings on reimbursed property-level payroll and administrative costs pass to owners, and renewal rebids or expanded service expectations can share the rest.

## Firm availability
The industry definition already centers on management for others, making recurring external service common. Transferable candidates still need diversified mandates, assignable contracts, durable staff and systems, limited owner dependence, and economics genuinely inside the target band despite the broad margin bridge.

## Demand durability
Commercial properties continue to need lease, tenant, vendor, accounting, maintenance, inspection, and compliance coordination. Outsourcing can expand, but office weakness, property sales, owner insourcing, rent pressure, and consolidation create a wide demand range.

## Risks and uncertainty
Key risks are client and property concentration, contract termination, owner insourcing, commercial vacancy, rent-collection weakness, cyber and privacy failures, accounting errors, vendor fraud, service incidents, licensing and compliance obligations, reimbursed-cost pass-through, and a firm-count estimate built on a broad low margin.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4091 | — | OBSERVED | — |
| n | — | 124 | — | ESTIMATE | — |
| a | 0.34 | 0.48 | 0.62 | ESTIMATE | S2, S3, S4 |
| rho | 0.4 | 0.58 | 0.72 | ESTIMATE | S3, S4 |
| e | 0.68 | 0.82 | 0.92 | ESTIMATE | S1, S4 |
| s5 | 0.07 | 0.14 | 0.22 | PROXY | S5 |
| q | 0.28 | 0.47 | 0.65 | ESTIMATE | S4 |
| d5 | 0.92 | 1.03 | 1.14 | PROXY | S2, S4 |
| o | 0.78 | 0.9 | 0.97 | PROXY | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.23 | 4.56 | 7.30 | ESTIMATE |
| F | 3.11 | 4.38 | 5.25 | ESTIMATE |
| C | 5.60 | 9.40 | 10.00 | ESTIMATE |
| D | 7.18 | 9.27 | 10.00 | PROXY |

## Caveats
- a: BLS combines residential, commercial, and community-association managers rather than measuring 531312 alone.
- a: IREM measures perceived proptech opportunities, not wage-weighted task exposure or realized AI labor savings.
- a: CBRE is far larger and more integrated than a lower-middle-market property manager.
- rho: IREM respondents reported cost, integration, and training barriers but did not report five-year AI realization rates.
- rho: CBRE's technology resources and integration capabilities may exceed those of target firms.
- rho: AI adoption can improve service quality without reducing labor or avoiding future hiring.
- e: The frozen firm count uses a 3.96% broad real-estate-operations margin rather than observed property-manager EBITDA.
- e: Large integrated firms mix property management with facilities, project, leasing, and advisory services.
- e: Contracts may be terminable on sale of a managed property or change of control, weakening practical eligibility.
- s5: Gallup covers all U.S. employer-business owners and intentions rather than completed property-management control transfers.
- s5: The survey includes internal and family transfers that may not qualify for the screen.
- s5: Property-management mandates may terminate or be rebid when properties or managers change hands.
- q: CBRE's global contract mix may not represent independent lower-middle-market managers.
- q: The filing documents billing structures but not savings-sharing outcomes after automation.
- q: A percentage-of-rent fee can preserve pricing while exposing revenue to occupancy and rent-collection cycles.
- d5: BLS employment projections combine residential, commercial, and community-association work and are not service-quantity forecasts.
- d5: CBRE is global, very large, and acquisitive; its revenue growth includes mix, price, scope, and acquisitions.
- d5: Office distress, property sales, insourcing, and rent-collection weakness can reduce management-fee demand even when physical space persists.
- o: Continued need for property operations does not guarantee continued use of an independent manager.
- o: The BLS task list includes residential and community-association work as well as commercial management.
- o: Integrated owner platforms may unbundle administrative tasks while retaining only field or specialist services.

## Sources
- **S1** — [North American Industry Classification System: Sector 53](https://www.census.gov/naics/resources/archives/sect53.html) (accessed 2026-07-22): Official 531312 definition and cross-references; lens and e
- **S2** — [Property, Real Estate, and Community Association Managers](https://www.bls.gov/ooh/management/property-real-estate-and-community-association-managers.htm?search=Spring_TX) (accessed 2026-07-22): Manager duties, physical and interpersonal work, contracting context, automation note, and 2024-2034 employment projection; a, d5, and o
- **S3** — [IREM Proptech Insights 2024](https://www.irem.org/file%20library/globalnavigation/learning/tech%20hub/irem-proptech-insights-24-final.pdf) (accessed 2026-07-22): Proptech-solvable tasks and reported cost, integration, and training barriers; a, rho, and o
- **S4** — [CBRE Group, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1138118/000113811826000005/cbre-20251231.htm) (accessed 2026-07-22): Commercial property-management scope, monthly fixed and rent-linked fees, reimbursed costs, multi-year contracts, AI investment, competitive risks, and 2025 and 2024 revenue; a, rho, e, q, d5, and o
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year sale or transfer intentions among U.S. employer-business owners; s5
