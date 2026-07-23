# 336510 — Railroad Rolling Stock Manufacturing

*v5.1 Stage 1 research memo. Run `336510-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.23 · L 1.53 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Aging fleets and safety-regulated physical equipment create durable replacement and aftermarket demand.
**Weakness:** Heavy fabrication and long, buyer-controlled procurement cycles constrain substitution and retention.

## Business-model lens
- Included: Independent LMM manufacturers and rebuilders of locomotives, freight and passenger cars, rapid-transit equipment, railcar parts and equipment, and track-maintenance machinery sold repeatedly to external railroads, transit agencies, lessors, fleets, or OEMs.
- Excluded: Rail operations, repair-only shops, lessors without manufacturing, captive plants, shells, and firms outside the EBITDA band.
- Customer and revenue model: Repeat new-build, rebuild, component, replacement, and fleet-program revenue under bids and long-term contracts, supported by engineering, safety compliance, inspection, documentation, warranty, and parts service.
- Deviation from default lens: none

## Executive view
Rolling stock combines high labor intensity, durable physical replacement demand, and strong safety and compatibility barriers. AI can improve bidding, engineering, planning, and quality administration, while welding and assembly cap substitution.

## How AI changes the work
Uses include tender and specification extraction, engineering and parts search, configuration records, work instructions, scheduling, procurement, quality trend analysis, warranty triage, and fleet support. Forming, welding, machining, assembly, painting, inspection, and dynamic testing remain physical.

## Value capture
Safety qualification, installed-base compatibility, long life cycles, tooling, and scarce suppliers protect gains. Public procurement, railroad and lessor bargaining, open-book terms, and escalation clauses share savings.

## Firm availability
The estimated population includes attractive parts, rebuild, and maintenance-equipment niches, but large strategic plants, captive shops, leasing, repair-only models, customer concentration, and project economics reduce eligibility.

## Demand durability
Aging passenger and freight fleets, replacement grants, safety standards, modernization, and track maintenance sustain physical demand. Public-budget delays, freight cycles, imports, and long order timing create volatility.

## Risks and uncertainty
Public procurement, Buy America compliance, product liability, welding and quality capacity, customer concentration, cyclical freight orders, working capital, project overruns, and the auto-parts margin bridge are key risks.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3289 | — | OBSERVED | — |
| n | — | 52 | — | ESTIMATE | — |
| a | 0.13 | 0.22 | 0.32 | PROXY | S1, S2, S3 |
| rho | 0.36 | 0.53 | 0.69 | ESTIMATE | S3, S4 |
| e | 0.49 | 0.66 | 0.81 | ESTIMATE | S1, S5 |
| s5 | 0.11 | 0.21 | 0.32 | PROXY | S6 |
| q | 0.52 | 0.68 | 0.82 | ESTIMATE | S1, S3, S4 |
| d5 | 0.95 | 1.08 | 1.23 | PROXY | S4, S5 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.62 | 1.53 | 2.90 | ESTIMATE |
| F | 2.15 | 3.39 | 4.30 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.03 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No wage-weighted six-digit task survey.
- a: Complete vehicles, parts, and rebuilders have different labor mixes.
- rho: Bounded judgment rather than observed adoption.
- rho: Safety-critical outputs require accountable review.
- e: Injected count uses an auto-parts margin bridge and is estimated.
- e: Establishments may not equal transferable firms.
- s5: Economy-wide demographic proxy.
- s5: No public code-specific transfer denominator.
- q: No public contract sample measures automation pass-through.
- q: Aftermarket components may retain more than publicly bid new vehicles.
- d5: Federal grant funding is only part of demand and not delivered units.
- d5: Passenger, freight, locomotive, and maintenance equipment cycles differ.
- o: Operator share may shift to foreign or captive plants.
- o: This is separate from labor automation within manufacturers.

## Sources
- **S1** — [NAICS 336510 Railroad Rolling Stock Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Census defines the industry to include locomotives and parts, freight and passenger rail cars, rapid-transit equipment, and railway track-maintenance equipment.
- **S2** — [Railroad Rolling Stock Manufacturing OEWS](https://www.bls.gov/oes/2023/may/naics4_336500.htm) (accessed 2026-07-22): BLS reports 2,400 welders representing 11.26% of industry employment, supporting the production-heavy task proxy.
- **S3** — [FRA Motive Power and Equipment](https://railroads.dot.gov/railroad-safety/divisions/motive-power-and-equipment) (accessed 2026-07-22): FRA administers safety programs for locomotives and freight, passenger, and commuter equipment, supporting regulatory accountability.
- **S4** — [FY2026 Rail Vehicle Replacement Grant Notice](https://www.transit.dot.gov/notices-funding/fy-2026-notice-funding-opportunity-competitive-grants-rail-vehicle-replacement) (accessed 2026-07-22): FTA announces $166,050,322 for FY2026 rail-vehicle replacement and directs consideration of cars reaching end of useful life within five years.
- **S5** — [FRA Final Rule Strengthening Freight Car Safety Standards](https://railroads.fra.dot.gov/about-fra/communications/newsroom/press-releases/fra-issues-final-rule-strengthen-freight-car-0) (accessed 2026-07-22): FRA states its final rule introduces tougher safety, security, and manufacturing standards for newly built freight cars.
- **S6** — [2024 Chartbook on Firms by Age of Primary Owner](https://www.fedsmallbusiness.org/-/media/project/smallbizcredittenant/fedsmallbusinesssite/fedsmallbusiness/files/2024/firms-in-focus/sbcs_chartbook2024_ownerage.pdf) (accessed 2026-07-22): Federal Reserve owner-age evidence used only as a broad succession proxy.
