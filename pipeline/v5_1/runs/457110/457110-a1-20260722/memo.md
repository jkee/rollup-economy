# 457110 — Gasoline Stations with Convenience Stores

*v5.1 Stage 1 research memo. Run `457110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** A repair-bearing station can use AI in customer and shop administration while retaining indispensable physical service work.
**Weakness:** Substantive outsourced repair is optional and probably rare in this product-retail NAICS, leaving a very small eligible population.

## Business-model lens
- Included: U.S. lower-middle-market gasoline stations with convenience stores that also provide a substantive repeat automotive inspection, maintenance, and repair service to external vehicle owners or fleets.
- Excluded: Stations limited to fuel, grocery, prepared-food, lottery, tobacco, or other merchandise sales; fuel-card accounts without a supplied service; standalone charging sites; incidental air or vacuum machines; captive fleet facilities; shells; and non-control financing vehicles.
- Customer and revenue model: Included firms combine high-frequency retail fuel and convenience sales with externally purchased repeat automotive service, typically billed as flat-rate or actual-time labor plus parts and sometimes through fleet-account arrangements.
- Deviation from default lens: none

## Executive view
Gasoline stations with convenience stores are overwhelmingly product retailers, so the outsourced-service screen applies only to the small minority with substantive repeat automotive repair and maintenance. That edge has some administrative and diagnostic AI potential, but physical work, environmental and site complexity, and a gradual powertrain transition bound the opportunity.

## How AI changes the work
AI can assist intake, scheduling, customer explanations, maintenance reminders, parts lookup, diagnostics, bookkeeping, inventory, and surveillance review. Existing pay-at-pump and checkout automation already remove some easy work, while vehicle inspection, repair, forecourt operations, food handling, and safety exceptions remain human and physical.

## Value capture
Flat-rate repair pricing can let operators retain administrative and productivity gains initially. Local competition, fleet-account negotiation, visible parts prices, rework obligations, and customer switching share some benefit over time; fuel-price competition is economically important to the firm but is outside the qualifying repair benefit.

## Firm availability
Only an unmeasured minority of 457110 businesses appear eligible because the official definition requires fuel plus convenience retail and only optionally repair. Broad owner aging supports succession supply, but tanks, contamination, fuel agreements, franchise rules, and mixed real-estate structures complicate control transfers.

## Demand durability
The five-year repair basket is likely near flat: a large combustion-vehicle fleet continues to age, while fuel consumption trends down and battery-electric vehicles require less routine maintenance. The accountable service operator remains durable because safe diagnosis and physical repair cannot be reduced to software alone.

## Risks and uncertainty
The principal empirical risk is mistaking repeat product transactions for a recurring service and therefore overstating eligibility. Other material risks are environmental liabilities, declining fuel visits, EV adoption, technician scarcity, theft, low product margins, fuel-supplier and franchise constraints, real-estate entanglement, and AI-driven diagnostic or safety errors.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.25 | 0.36 | PROXY | S2, S3, S4, S5 |
| rho | 0.42 | 0.57 | 0.7 | ESTIMATE | S3, S4, S5 |
| e | 0.02 | 0.06 | 0.15 | ESTIMATE | S1, S2 |
| s5 | 0.13 | 0.22 | 0.34 | PROXY | S9 |
| q | 0.38 | 0.55 | 0.7 | ESTIMATE | S8 |
| d5 | 0.9 | 0.98 | 1.05 | PROXY | S5, S6, S7 |
| o | 0.78 | 0.89 | 0.96 | ESTIMATE | S5, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.27 | 0.58 | 1.02 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.02 | 8.72 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source covers all gasoline stations, not specifically 457110 establishments with substantive repair operations.
- a: Task sources do not supply industry wage weights or current automation penetration.
- a: The supplied compensation-to-receipts ratio is a low-quality retail-sector ancestor and may dilute the labor intensity of repair service.
- rho: No implementation study specific to gasoline-station repair businesses was found.
- rho: The estimate excludes pricing, demand, and valuation effects and applies only to exposed tasks in a.
- e: Public data do not report the share of 457110 firms with substantive automotive repair operations.
- e: Repeat fuel purchase and fuel-card billing are treated as recurring merchandise, not an outsourced service.
- e: Repair-heavy gasoline stations without convenience stores may instead be classified in 457120, which depresses eligibility in this code.
- s5: The owner-age source is all-industry and data year 2018.
- s5: No qualifying-transfer denominator for the narrow eligible subset was found.
- s5: A real-estate sale, fuel-brand change, or lease transfer is not necessarily a control transfer of the service operating company.
- q: No source directly measures AI cost pass-through in station-based automotive repair.
- q: Retention differs between walk-in consumers, fleets, warranty work, and insurer-influenced repairs.
- q: The range excludes demand loss and implementation difficulty.
- d5: Occupational employment is not direct service quantity and covers all automotive repair settings.
- d5: National gasoline consumption is not a direct measure of demand for station-based repair.
- d5: Powertrain transition, vehicle age, miles traveled, and local station closures may move in offsetting directions.
- o: The operator may use centralized or remote support, so this estimate does not imply current store staffing remains unchanged.
- o: Simple diagnostics and software resets are more substitutable than mechanical inspection and repair.
- o: The estimate applies to year-five service quantity after d5, not fuel or grocery transaction volume.

## Sources
- **S1** — [2022 NAICS Definition: 457110 Gasoline Stations with Convenience Stores](https://www.census.gov/naics/?details=457110&input=457110&year=2022) (accessed 2026-07-22): Defines the industry as retail automotive fuels combined with a limited grocery line and states that establishments may also provide automotive repair services.
- **S2** — [Data Tables for OEWS Industry Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports gasoline-station employment concentrated in 586,370 cashiers, 104,010 first-line retail supervisors, 52,710 retail salespersons, 41,360 fast-food/counter workers, 33,820 general and operations managers, and 17,470 service attendants.
- **S3** — [O*NET OnLine: Cashiers 41-2011.00](https://www.onetonline.org/link/summary/41-2011.00) (accessed 2026-07-22): Lists cashier tasks including receiving payments, refunds, customer questions, complaints, phone calls, pricing, transaction reconciliation, reporting, stocking, bagging, and cleaning.
- **S4** — [Occupational Outlook Handbook: Cashiers](https://www.bls.gov/ooh/sales/cashiers.htm) (accessed 2026-07-22): Projects cashier employment to decline 10% from 2024 to 2034 and attributes the decline to technology such as self-service checkout and increasing online sales.
- **S5** — [Occupational Outlook Handbook: Automotive Service Technicians and Mechanics](https://www.bls.gov/ooh/installation-maintenance-and-repair/automotive-service-technicians-and-mechanics.htm) (accessed 2026-07-22): States that technicians inspect, maintain, and repair cars and light trucks, often diagnose with computers but work with physical parts and tools, and projects 4% employment growth from 2024 to 2034.
- **S6** — [Increasing Fuel Efficiency Leads to Decreasing Gasoline Consumption](https://www.eia.gov/todayinenergy/detail.php?id=67426) (accessed 2026-07-22): Reports U.S. motor-gasoline consumption averaged 8.9 million barrels per day in 2025, 1% below 2024 and 4% below 2019, and forecasts continued decline in 2026 and 2027.
- **S7** — [Battery-Electric Vehicles Have Lower Scheduled Maintenance Costs Than Other Light-Duty Vehicles](https://www.energy.gov/cmei/vehicles/articles/fotw-1190-june-14-2021-battery-electric-vehicles-have-lower-scheduled) (accessed 2026-07-22): Reports estimated scheduled maintenance cost of 6.1 cents per mile for battery-electric vehicles versus 10.1 cents for conventional internal-combustion vehicles, reflecting fewer service items.
- **S8** — [Auto Repair Basics](https://consumer.ftc.gov/sites/default/files/articles/pdf/pdf-0078-auto-repair.pdf) (accessed 2026-07-22): Explains that some repair shops charge a flat labor rate based on independent or manufacturer time estimates, while others charge for actual technician time, supporting the value-capture billing analysis.
- **S9** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding owners of U.S. employer businesses were age 55 or older in the 2019 Annual Business Survey, data year 2018.
