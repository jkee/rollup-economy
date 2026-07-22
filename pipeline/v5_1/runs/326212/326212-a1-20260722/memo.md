# 326212 — Tire Retreading

*v5.1 Stage 1 research memo. Run `326212-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.38 · L 1.26 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring fleet tire cycles and sticky local programs create repeat work with optimizable inspection, routing, and production support.
**Weakness:** Safety-critical casing judgment and physical processing limit substitution, while sophisticated fleets pressure pricing.

## Business-model lens
- Included: US lower-middle-market tire retreaders and rebuilders that repeatedly inspect customer or program casings, apply new tread, test and identify finished retreads, and supply external trucking fleets, bus operators, dealers, off-road users, and tire-management programs.
- Excluded: New-tire manufacturing, tire repair or installation without retreading, retail-only dealers, captive fleet shops not serving external customers, casing brokers without processing, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring B2B service and product revenue per retread, casing, or tire-management program, often tied to fleet routes and replacement cycles, with pickup and delivery, casing acceptance, tread choice, warranty, and volume pricing.
- Deviation from default lens: none

## Executive view
Tire retreading closely fits a recurring outsourced-service lens through repeat fleet programs, casing cycles, routes, and quality accountability. AI can improve inspection support, scheduling, logistics, documentation, maintenance, billing, and reporting, but hands-on safety-critical processing remains central.

## How AI changes the work
Computer vision and anomaly models can prioritize casing defects and standardize records; optimization can improve production sequencing, route density, inventory, and turnaround; language tools can automate fleet reports, work instructions, claims, and administration. Human acceptance decisions and physical buffing, repair, building, curing, and final inspection remain constrained.

## Value capture
Local service density, casing history, quality, turnaround, warranty, and fleet integration create stickiness. Large fleets and chains measure cost per mile and rebid, so part of visible productivity flows to customers over time.

## Firm availability
The estimated target pool is meaningful and likely contains many regional external-service firms, although captive operations and dealer-owned plants require exclusion. General succession evidence supports availability but verified owner and transaction data are missing.

## Demand durability
Fleet mileage and tire wear recur, while retreading offers casing reuse and potentially fuel-efficient options. Freight cycles, cheap new tires, casing design and quality, and fleet acceptance can reduce volumes, yet fulfilled demand still requires an accountable processor.

## Risks and uncertainty
Safety and warranty failures, poor casing supply, large-fleet concentration, route inefficiency, equipment age, environmental and worker-safety exposure, cheap imports, and skilled labor are material. Evidence is weakest on retread-specific task mix, firm eligibility, closed transfers, and contract-level retention.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2429 | — | OBSERVED | — |
| n | — | 91 | — | ESTIMATE | — |
| a | 0.16 | 0.24 | 0.34 | PROXY | S1, S2 |
| rho | 0.39 | 0.54 | 0.68 | ESTIMATE | S2 |
| e | 0.5 | 0.65 | 0.78 | ESTIMATE | S3 |
| s5 | 0.13 | 0.22 | 0.32 | PROXY | S6 |
| q | 0.39 | 0.56 | 0.72 | ESTIMATE | — |
| d5 | 0.96 | 1.04 | 1.13 | PROXY | S4, S5 |
| o | 0.96 | 0.99 | 0.998 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.61 | 1.26 | 2.25 | ESTIMATE |
| F | 3.11 | 4.25 | 5.09 | ESTIMATE |
| C | 7.80 | 10.00 | 10.00 | ESTIMATE |
| D | 9.22 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Four-digit rubber-product employment is not retread-specific.
- a: Safety-critical casing judgment may be assistable but not fully substitutable.
- rho: NHTSA requirements show accountability but not implementation rates.
- rho: Truck and passenger retreads face different process and regulatory conditions.
- e: The NAICS definition does not distinguish captive from external operations.
- e: The frozen firm count is margin-bridged rather than an observed eligible count.
- s5: The evidence is cross-industry intention rather than completed deal flow.
- s5: Chain acquisitions and dealer transactions may not be coded as 326212.
- q: No public contract sample quantifies pass-through.
- q: Local small fleets likely offer greater retention than national fleets or dealer networks.
- d5: VMT is not retread volume and light-duty vehicles use few retreads.
- d5: EPA fuel-saving verification supports customer value, not total market demand.
- o: The estimate is inferred from the physical process and accountability requirements.
- o: New-tire substitution affects d5 more than operator requirement and is not double-counted here.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 326200 Rubber Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326200.htm) (accessed 2026-07-22): Provides the broader rubber-product occupation and wage mix, including 63.29 percent production employment and substantial maintenance and material-moving work, used as a retreading task-mix proxy.
- **S2** — [NHTSA Interpretation: New Holland Tire](https://www.nhtsa.gov/interpretations/new-holland-tire) (accessed 2026-07-22): Defines a retread as tread attached to a casing, explains that passenger retreads are subject to FMVSS No. 117, and states that Part 574 applies to retreads and requires the retreader's tire identification number, grounding accountability and process constraints.
- **S3** — [2012 NAICS Definition: Tire Manufacturing](https://www2.census.gov/econ2012/Reference_materials/htm%20files/32621m.htm) (accessed 2026-07-22): Defines 326212 as establishments primarily engaged in retreading or rebuilding tires and distinguishes it from new-tire manufacturing, grounding the lens.
- **S4** — [EPA SmartWay Low Rolling Resistance Retread Verification Protocols](https://www.epa.gov/system/files/documents/2022-03/retread-verification-protocols-2022-02-25.pdf) (accessed 2026-07-22): States that verified low-rolling-resistance retread products can reduce fuel consumption by at least 3 percent versus higher-resistance tires or retreads when used as specified, supporting fleet customer value.
- **S5** — [2025 FHWA Forecasts of Vehicle Miles Traveled](https://www.fhwa.dot.gov/policyinformation/tables/vmt/vmt_forecast_sum.cfm) (accessed 2026-07-22): Projects total national vehicle miles traveled growing at a 0.6 percent average annual rate between 2023 and 2053, used only as a directional tire-wear demand proxy.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of employer-business owners surveyed in fall 2024 planned to sell or transfer ownership within five years, used as a cross-industry transfer proxy.
