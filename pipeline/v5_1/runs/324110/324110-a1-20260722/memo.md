# 324110 — Petroleum Refineries

*v5.1 Stage 1 research memo. Run `324110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 3.69 · L 0.05 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Dense operational and maintenance data can support valuable AI decision tools in a continuously operating asset.
**Weakness:** The industry is capital-intensive commodity manufacturing, not a recurring outsourced service, and almost no firms are likely to fit the LMM lens.

## Business-model lens
- Included: US lower-middle-market petroleum-refining firms that operate accountable processing assets and earn recurring external-customer revenue, including merchant or specialty refiners and any genuine toll-processing arrangements.
- Excluded: Integrated oil-company divisions outside the EBITDA band, terminals and pipelines, petroleum wholesalers, renewable-fuel plants classified elsewhere, captive internal units, shells, and non-control financing vehicles.
- Customer and revenue model: Primarily commodity and specialty petroleum-product sales to distributors, marketers, industrial users, airlines, and other external buyers; qualifying tolling or processing fees are included where present.
- Deviation from default lens: none

## Executive view
Petroleum refining has useful AI applications in maintenance, planning, documentation, laboratory analytics, and decision support, but the frozen roll-up lens fits poorly because refineries principally manufacture commodities rather than provide outsourced services. Low labor share, extreme safety obligations, capital intensity, and a tiny estimated firm population further limit the implementable opportunity.

## How AI changes the work
AI can organize operating procedures, interpret equipment histories, prioritize inspections, assist maintenance and turnaround planning, forecast quality, optimize schedules, and automate reporting. Safety-critical control, field work, mechanical integrity, emergency response, and release accountability must remain governed by qualified humans and formal management-of-change processes.

## Value capture
Better uptime, yield, and energy use can have large dollar value, but refined-product pricing is governed mainly by commodity inputs, regional supply, and crack spreads. Savings may support margins temporarily, while competition and formula pricing transfer broadly available improvements to buyers.

## Firm availability
The estimated six firms should not be treated as six eligible targets. Most refinery businesses fail the recurring outsourced-service test, and any small candidate requires detailed validation of tolling revenue, permits, environmental liabilities, capital needs, ownership, and transferability.

## Demand durability
US petroleum demand remains large and regional refinery closures can tighten supply, but five-year outcomes vary by gasoline, diesel, jet fuel, asphalt, lubricants, and specialty products. Electrification, efficiency, biofuels, imports, conversions, and policy create meaningful downside without eliminating operator-required processing.

## Risks and uncertainty
The primary risks are lens ineligibility, erroneous LMM firm-count bridging, environmental and remediation liabilities, catastrophic process hazards, volatile cracks, capital expenditure, and a transaction universe so small that population averages are unstable.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0151 | — | OBSERVED | — |
| n | — | 6 | — | ESTIMATE | — |
| a | 0.1 | 0.2 | 0.32 | PROXY | S1, S2 |
| rho | 0.22 | 0.42 | 0.6 | ESTIMATE | S2 |
| e | 0.01 | 0.06 | 0.18 | ESTIMATE | S3, S4 |
| s5 | 0.06 | 0.13 | 0.23 | PROXY | S3, S5 |
| q | 0.12 | 0.28 | 0.48 | ESTIMATE | S3, S4 |
| d5 | 0.8 | 0.94 | 1.04 | PROXY | S3, S4 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.01 | 0.05 | 0.12 | ESTIMATE |
| F | 0.01 | 0.07 | 0.36 | ESTIMATE |
| C | 2.40 | 5.60 | 9.60 | ESTIMATE |
| D | 7.20 | 9.02 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit LMM occupation mix or current-AI task audit was located.
- a: Existing distributed-control and advanced-process-control systems may mean much of the obvious optimization opportunity is already automated.
- rho: OSHA evidence establishes operational constraints, not an AI implementation rate.
- rho: A single process-safety incident or cybersecurity event could materially tighten adoption standards.
- e: The frozen firm count is especially fragile because refinery economics and scale differ sharply from the margin bridge used.
- e: Operable-refinery counts include facilities and ownership structures far outside the LMM lens.
- s5: Gallup is not industry- or size-specific and measures intentions rather than consummated transfers.
- s5: With very few eligible firms, one transaction changes the realized share sharply.
- q: No LMM refinery contract sample or automation pass-through study was located.
- q: Regional logistics constraints and product specialization can make retention materially higher than commodity averages.
- d5: Capacity and national consumption are not direct measures of demand for an LMM refinery's current output mix.
- d5: Five-year policy, electric-vehicle adoption, crude differentials, and regional closures are unusually consequential.
- o: An operator may remain required while ownership consolidates into a larger enterprise outside the lens.
- o: The estimate separates operator necessity from employment intensity; it does not imply current staffing levels persist.

## Sources
- **S1** — [Petroleum and Coal Products Manufacturing: NAICS 324](https://www.bls.gov/iag/tgs/iag324.htm) (accessed 2026-07-22): Reports 2025 broader-subsector employment including 18,720 petroleum pump system operators, refinery operators, and gaugers and 4,980 first-line production supervisors; reports 109,900 employees in June 2026.
- **S2** — [Petroleum Refinery Process Safety Management National Emphasis Program](https://www.osha.gov/enforcement/directives/cpl-03-00-004) (accessed 2026-07-22): Identifies catastrophic-release hazards in NAICS 324110 and process-safety requirements covering management of change, mechanical integrity, operating and emergency procedures, human factors, training, incident investigation, and implementation verification.
- **S3** — [U.S. refining capacity decreased during 2025](https://www.eia.gov/todayinenergy/detail.php?id=67807) (accessed 2026-07-22): Reports 18.2 million barrels per calendar day of US operable atmospheric distillation capacity at January 1, 2026, down over 250,000 barrels per day, with 130 operable refineries after two 2025 closures.
- **S4** — [Refinery closures and rising consumption will reduce U.S. petroleum inventories in 2026](https://www.eia.gov/TODAYINENERGY/detail.php?id=64644) (accessed 2026-07-22): Forecasts rising US petroleum consumption alongside reduced domestic refining from two closures and lower inventories for gasoline, distillate, and jet fuel in 2026.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey found 22% of employer-business owners planned to sell or transfer ownership within five years, while 5% planned closure and 5% had no plan.
