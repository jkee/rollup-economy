# 485113 — Bus and Other Motor Vehicle Transit Systems

*v5.1 Stage 1 research memo. Run `485113-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.26 · L 2.35 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A credible private-operator population with recurring contracts and repeatable dispatch, planning, customer-service, maintenance, recruiting, and administrative workflows.
**Weakness:** Most labor cost is tied to safety-critical driving and field work, while public procurement steadily passes savings back to the authority.

## Business-model lens
- Included: US lower-middle-market private firms that repeatedly operate local or suburban fixed-route bus or other motor-vehicle transit service for external public authorities, institutions, or system owners under operating or purchased-transportation contracts.
- Excluded: Public transit authorities and municipal departments, school bus operations, interurban and rural bus carriers, charter buses, taxis and ridesharing, demand-responsive-only special-needs providers, hotel or airport captive shuttles, support-only vendors, software-only suppliers, non-control financing vehicles, and firms outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: The core customer is a public transit authority or other system owner paying recurring fees under a multiyear competitively procured operating contract, with fixed-price, indexed, cost-reimbursement, or management-fee structures; the authority generally controls fares, routes, service levels, and subsidy.
- Deviation from default lens: none

## Executive view
Fixed-route bus contractors combine a high labor burden with recurring public-service contracts and a plausible LMM firm population. AI opportunity is meaningful in dispatch, planning, customer service, maintenance administration, recruiting, and compliance, but driver-heavy work and public procurement cap both implementation and retained economics.

## How AI changes the work
Near-term tools can automate service alerts and routine contacts, assist dispatchers, optimize schedules and crews, triage maintenance, accelerate recruiting and training administration, and draft incident and compliance records. Full-size unattended urban buses are not the base case; driving, maintenance, cleaning, and frontline passenger support remain labor-intensive.

## Value capture
Savings are most defensible inside fixed-price contract periods. Cost-reimbursement, staffing commitments, change clauses, authority cost review, option pricing, and competitive rebids share benefits with the customer over five years, while large strategic competitors can imitate software-enabled bids.

## Firm availability
Unlike mixed-mode and commuter-rail systems, private fixed-route bus contractors plausibly occupy the target band, and the frozen dataset estimates 42 LMM firms. Eligibility still requires confirming independence, recurring external contracts, correct NAICS coding, and normalized EBITDA rather than treating local subsidiaries as acquisition targets.

## Demand durability
Bus service has continued its post-pandemic recovery, and authorities are expected to expand or redesign networks. Fiscal pressure and driver shortages can suppress delivered service, but urban mobility, accessibility, and public-policy obligations make wholesale demand elimination unlikely.

## Risks and uncertainty
The largest risks are that labor intensity sits in non-automatable driving, contracts prevent headcount removal, union or ADA requirements slow deployment, public agencies capture savings, a route contract is lost at rebid, or the apparent LMM firm is actually a strategic subsidiary. Autonomous buses are a longer-range disruption and a near-term diligence variable, not a five-year base assumption.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6274 | — | OBSERVED | — |
| n | — | 42 | — | ESTIMATE | — |
| a | 0.09 | 0.17 | 0.27 | ESTIMATE | S2, S3 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S3, S4, S9 |
| e | 0.35 | 0.55 | 0.75 | ESTIMATE | S1, S7, S9, S10 |
| s5 | 0.12 | 0.25 | 0.4 | ESTIMATE | S7, S11 |
| q | 0.33 | 0.48 | 0.63 | ESTIMATE | S6, S8, S10 |
| d5 | 0.99 | 1.07 | 1.18 | PROXY | S5, S6 |
| o | 0.92 | 0.97 | 0.995 | PROXY | S3, S4, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.79 | 2.35 | 4.88 | ESTIMATE |
| F | 1.64 | 3.08 | 4.20 | ESTIMATE |
| C | 6.60 | 9.60 | 10.00 | ESTIMATE |
| D | 9.11 | 10.00 | 10.00 | PROXY |

## Caveats
- a: The BLS chart covers Urban Transit Systems rather than only private 485113 LMM contractors.
- a: It reports employment rather than wage-weighted task shares and only the ten largest occupations.
- a: The frozen compensation-to-receipts input uses 2024 wages over 2022 receipts and an IPS harmonization; the vintage mismatch and high reported labor ratio may not reflect contract-level economics.
- rho: FTA automation evidence emphasizes vehicles, whereas much of the implementable estimate is office and operations-support AI.
- rho: Small operators may move faster organizationally but have less integration capacity and lower-quality data than large agencies.
- rho: Commercial sharing and demand effects are excluded from this primitive.
- e: NTD identifies contracts and contractors but does not directly map to the SUSB firm universe or normalized EBITDA.
- e: Large strategic operators may establish local subsidiaries that look like small firms or establishments but are not independently transferable.
- e: The provided count of 42 is an ESTIMATE produced from size-class firm counts, average receipts, and a sector EBITDA margin bridge.
- s5: No source directly measures five-year control-transfer probability for eligible 485113 LMM firms.
- s5: The cited strategic transaction is much larger than the target band and can overstate LMM deal flow.
- s5: A change in transit-service contractor is not a transfer of the contractor's equity.
- q: National fare and expense totals cover publicly and privately operated bus service and do not measure retention of AI savings.
- q: Contract structures and renewal calendars vary widely, making retention highly firm-specific.
- q: Failure to remove labor because of service or staffing obligations belongs in implementation, not commercial retention.
- d5: Service supplied is not the same as passenger demand and can be politically or fiscally set.
- d5: The BLS occupation combines transit and intercity drivers and its ten-year employment outlook is not an output forecast.
- d5: Capacity-equivalent normalization and shifts between directly operated and purchased service can obscure demand for private contractors.
- o: Automation can reduce driver hours materially without eliminating the accountable operator.
- o: Simple segregated BRT or circulator routes may automate sooner than ordinary urban fixed-route networks.
- o: Unexpected safety validation and regulatory change could lower operator-required quantity faster than assumed.

## Sources
- **S1** — [North American Industry Classification System, United States, 2022](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 485113 as establishments operating local and suburban passenger systems using buses or other motor vehicles over regular routes and schedules and distinguishes adjacent bus industries.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest Urban Transit Systems occupations, including 24,540 transit/intercity bus drivers, 2,640 mechanics, 2,080 shuttle drivers, 1,150 dispatchers, 740 customer-service representatives, and 650 general and operations managers.
- **S3** — [Transit Automation Research](https://www.transit.dot.gov/automation-research) (accessed 2026-07-22): Identifies bus-automation use cases and describes ongoing demonstrations and work on technology, market, insurance, accessibility, business-case, and policy questions.
- **S4** — [When will driverless buses operate on public roads?](https://www.transit.dot.gov/when-will-driverless-buses-operate-public-roads) (accessed 2026-07-22): States most piloted systems assist drivers; Level 4 shuttles generally carry 6-15 passengers at 10-15 mph, retain on-board attendants, and may not match regular service in complex environments.
- **S5** — [Bus Drivers: Occupational Outlook Handbook](https://www.bls.gov/ooh/transportation-and-material-moving/bus-drivers.htm) (accessed 2026-07-22): Projects transit and intercity bus-driver employment to grow 4% from 2024 to 2034 and links growth to authority network redesigns, service expansion, and BRT deployment.
- **S6** — [2024 National Transit Summaries and Trends](https://www.transit.dot.gov/sites/fta.dot.gov/files/2026-04/2024%20National%20Transit%20Summaries%20and%20Trends_1.2.pdf) (accessed 2026-07-22): Reports bus capacity-equivalent vehicle revenue miles of 1,925 million in 2019 and 1,719, 1,753, 1,771, and 1,812 million in 2021-2024, plus 2024 bus operating expense of $28.884 billion and fares of $3.249 billion.
- **S7** — [2024 Annual Database Contractual Relationship](https://www.transit.dot.gov/ntd/data-product/2024-annual-database-contractual-relationship) (accessed 2026-07-22): Provides contract information by agency, contractor, mode, and service type, including private providers, procurement method, contract duration, financial data, and operating statistics.
- **S8** — [FTA Circular 4220.1G: Third Party Contracting Guidance](https://www.transit.dot.gov/sites/fta.dot.gov/files/2025-01/Third-Party-Contracting-Guidance-%28Circular-4220.1G%29.pdf) (accessed 2026-07-22): Requires reasonable contract periods that preserve full and open competition and federally assisted costs that are necessary, reasonable, and allocable.
- **S9** — [49 CFR Part 37: Transportation Services for Individuals with Disabilities](https://www.transit.dot.gov/regulations-and-guidance/civil-rights-ada/part-37-transportation-services-individuals-disabilities) (accessed 2026-07-22): Requires private entities operating fixed-route or demand-responsive service for public entities to meet the applicable public-entity accessibility obligations.
- **S10** — [What is meant by acquisition of public transportation service?](https://www.transit.dot.gov/32-section-5310-program-what-meant-%E2%80%9Cacquisition-public-transportation-service%E2%80%9D) (accessed 2026-07-22): Defines acquisition of public transportation service as procurement of third-party service and states that only competitively procured service qualifies in the Section 5310 context.
- **S11** — [Transdev completes the acquisition of First Transit](https://www.transdev.com/actualite/amerique-du-nord/communique-de-presse/transdev-finalise-acquisition-de-first-transit) (accessed 2026-07-22): Confirms the March 2023 acquisition of First Transit, combining major North American private public-transport operators across bus, paratransit, shuttle, rail, tram, and maintenance services.
