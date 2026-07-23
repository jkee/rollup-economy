# 336611 — Ship Building and Repairing

*v5.1 Stage 1 research memo. Run `336611-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.24 · L 1.37 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Aging, mission-critical fleets require recurring physical repair and modernization at qualified facilities with scarce drydock and trade capacity.
**Weakness:** Large, irregular contracts and unstable government workload signals can leave expensive facilities and skilled workforces underutilized.

## Business-model lens
- Included: U.S. lower-middle-market shipyards with fixed facilities and fabrication equipment that build, repair, convert, alter, dismantle, or scale commercial, government, and other nonrecreational ships, barges, workboats, and floating platforms for external customers.
- Excluded: Boat building outside shipyards, floating-drydock repairs classified as water-transport support, component fabrication or trade subcontracting classified by production process, captive government yards, and firms without repeat external-customer work.
- Customer and revenue model: Recurring or repeat outsourced revenue from shipowners and government agencies through maintenance availabilities, repair, overhaul, conversion, modernization, emergency work, and repeat new-build programs.
- Deviation from default lens: none

## Executive view
Ship building and repair is a physical, qualification-heavy industry with modest AI exposure in planning, engineering, documentation, and selected fabrication. Deferred maintenance and fleet goals support demand, but government schedules, project timing, and regional capacity produce material volatility.

## How AI changes the work
AI can assist design, estimating, scheduling, procurement, inspection, documentation, inventory, predictive maintenance, and robotic fabrication, while drydock trades, variable repair discovery, testing, certification, and accountable engineering remain labor-intensive.

## Value capture
Drydock access, customer qualifications, local fleet proximity, scarce trades, and emergency response protect value; competitive procurement, audits, fixed-price risk, change orders, and rebids share benefits with customers.

## Firm availability
Independent repair and modernization yards can have repeat customers, but public yards, outside-code subcontractors, project-only builders, recreational-boat firms, and nontransferable distressed facilities reduce eligibility. Broad succession data suggest a material transfer pool.

## Demand durability
Aging vessels, deferred maintenance, modernization, and national-security goals support five-year work, but Navy forecasts have fluctuated and commercial cycles, decommissioning, funding, and scheduling can sharply alter yard-level volume.

## Risks and uncertainty
Risks include project overruns, hidden repair scope, workforce scarcity, safety and environmental liabilities, bonding and working-capital needs, customer concentration, procurement changes, vessel retirement, facility utilization, and demand moving between regions or years.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3096 | — | OBSERVED | — |
| n | — | 53 | — | ESTIMATE | — |
| a | 0.13 | 0.23 | 0.34 | PROXY | S2, S3 |
| rho | 0.32 | 0.48 | 0.64 | PROXY | S3, S5 |
| e | 0.48 | 0.68 | 0.82 | ESTIMATE | S1, S5 |
| s5 | 0.14 | 0.23 | 0.35 | PROXY | S4 |
| q | 0.35 | 0.53 | 0.7 | ESTIMATE | S5 |
| d5 | 0.9 | 1.08 | 1.28 | PROXY | S5, S6 |
| o | 0.97 | 0.992 | 0.999 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.52 | 1.37 | 2.69 | PROXY |
| F | 2.44 | 3.59 | 4.48 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.73 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS combines ship and boat building rather than measuring 336611 alone.
- a: Occupation shares are not task shares and do not distinguish already automated CAD, CNC, and planning work.
- rho: NIST covers manufacturing generally, not shipyards.
- rho: Navy evidence describes industrial constraints rather than directly measuring AI implementation.
- e: No source measures the exact share of LMM firms meeting all scope, independence, repeat-revenue, and transferability tests.
- e: Government and commercial shipyards have materially different customer and contract structures.
- s5: Gallup covers employer businesses across industries rather than shipyards or the target EBITDA band.
- s5: Stated intentions do not equal completed qualifying control changes.
- q: This is discounted retained gross benefit rather than accounting margin.
- q: Navy repair contracting may be more transparent and competitive than commercial or emergency work, while major new construction may be more concentrated.
- d5: GAO evidence is Navy-heavy and does not cover all commercial shipyard demand.
- d5: Maintenance backlog is unmet work, not guaranteed funded revenue, and the most recent Navy plan rests on assumptions GAO found unrealistic.
- o: This measures persistence of the accountable shipyard role, not survival of any specific yard.
- o: Some repair quantity can migrate outside 336611 without the underlying maintenance need disappearing.

## Sources
- **S1** — [2022 NAICS Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-23): Exact shipyard scope, included building and repair activities, and exclusions for component trades and floating-drydock repair.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Ship and Boat Building](https://www.bls.gov/oes/2023/may/naics4_336600.htm) (accessed 2026-07-23): Occupational structure used to bridge to wage-weighted task exposure.
- **S3** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-23): Manufacturing AI adoption, use cases, expected expansion, and implementation barriers.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Employer-business owner age and five-year sale or transfer intentions.
- **S5** — [Shipbuilding and Repair: Navy Needs a Strategic Approach for Private Sector Industrial Base Investments](https://files.gao.gov/reports/GAO-25-106286/index.html) (accessed 2026-07-23): Private-yard structure, repair qualifications, backlog, workforce and capacity constraints, competition, grants, forecast volatility, and projected fleet and repair workload.
- **S6** — [Navy and Coast Guard Shipbuilding: A Disciplined, Strategy-Driven Approach Is Needed to Achieve Ambitious Goals](https://files.gao.gov/reports/GAO-26-109068/index.html) (accessed 2026-07-23): Current assessment that the latest Navy shipbuilding plan relies on historically unsupported backlog, cost, and schedule assumptions.
