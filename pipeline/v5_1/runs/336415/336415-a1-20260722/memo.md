# 336415 — Guided Missile and Space Vehicle Propulsion Unit and Propulsion Unit Parts Manufacturing

*v5.1 Stage 1 research memo. Run `336415-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.27 · L 0.53 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Strategic propulsion capacity is scarce while missile and space programs require more qualified physical output.
**Weakness:** The transferable LMM population is extremely small and operational risk is unusually high.

## Business-model lens
- Included: Independent LMM manufacturers and prototype-to-production suppliers of guided-missile and space-vehicle propulsion units and propulsion-unit parts sold repeatedly to external primes, government programs, and commercial-space customers.
- Excluded: Complete vehicles, aircraft engines, unrelated propulsion products, captive divisions, government facilities, shells, and firms outside the EBITDA band.
- Customer and revenue model: Long-cycle development and production-lot contracts with repeat qualification, hot-fire or component testing, configuration control, mission assurance, spares, and technical support.
- Deviation from default lens: none

## Executive view
Propulsion demand is strong and strategically scarce, but acquisition supply is tiny. AI can assist engineering and test information work only within strict security, hazardous-process, and mission-assurance boundaries.

## How AI changes the work
Uses include requirements and document search, proposal and schedule support, simulation assistance, configuration checks, test-plan drafting, test-data analysis, procurement, and quality trend review. Propellant handling, precision manufacture, assembly, hot-fire test execution, inspection, and safety disposition remain human-controlled.

## Value capture
Scarce test assets, qualification, mission criticality, and unique designs support retention. Government cost analysis, cost-type contracts, prime cost-downs, and later competition share gains.

## Firm availability
Only seven estimated LMM firms exist before filtering, and true independents with repeat funded programs, cleared staff, qualified facilities, and transferable control are likely fewer.

## Demand durability
Missile replenishment, missile defense, hypersonics, and expanding commercial and government space activity support strong demand. Technical failures, budget timing, qualification bottlenecks, and program concentration create volatility.

## Risks and uncertainty
Hazardous materials, catastrophic test or mission failure, security and export controls, cyber accreditation, facility clearances, program concentration, contract novation, and an ill-fitting margin bridge dominate.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1222 | — | OBSERVED | — |
| n | — | 7 | — | ESTIMATE | — |
| a | 0.17 | 0.27 | 0.38 | PROXY | S1, S2, S3, S4 |
| rho | 0.23 | 0.4 | 0.57 | ESTIMATE | S2, S3, S4 |
| e | 0.25 | 0.45 | 0.65 | ESTIMATE | S1, S2, S5 |
| s5 | 0.06 | 0.13 | 0.23 | PROXY | S6 |
| q | 0.61 | 0.78 | 0.9 | ESTIMATE | S2, S4, S5 |
| d5 | 1.06 | 1.28 | 1.55 | PROXY | S3, S5 |
| o | 0.98 | 0.997 | 1 | ESTIMATE | S1, S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.19 | 0.53 | 1.06 | ESTIMATE |
| F | 0.16 | 0.55 | 1.15 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 10.00 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No public six-digit occupation study.
- a: Classified and proprietary workflows limit evidence.
- rho: Bounded judgment, not observed adoption.
- rho: Autonomous propulsion control or safety disposition is excluded.
- e: Auto-parts margin bridge is especially weak for propulsion development and production.
- e: Establishments may not equal transferable firms.
- s5: Economy-wide demographic proxy.
- s5: Tiny denominator causes high uncertainty.
- q: No public contract sample quantifies pass-through.
- q: Commercial fixed-price and government cost-type programs differ.
- d5: Budget and testing activity are not delivered quantity.
- d5: Demand is concentrated in a few programs.
- o: Operator share may migrate to primes or government facilities.
- o: This is distinct from labor automation.

## Sources
- **S1** — [Guided Missile and Space Vehicle Propulsion Manufacturing](https://www2.census.gov/library/publications/economic-census/2002/manufacturing-reports/industry-series/ec0231i336415.pdf) (accessed 2026-07-22): Census defines the industry as manufacturing guided-missile or space-vehicle propulsion units and propulsion-unit parts.
- **S2** — [NASA Propulsion Test Engineering](https://www.nasa.gov/stennis/engineering-and-test-directorate/) (accessed 2026-07-22): NASA identifies rocket propulsion testing as a major engineering and test mission, supporting physical test and accountability requirements.
- **S3** — [DoD Background Briefing on FY 2026 Defense Budget](https://www.defense.gov/News/Transcripts/Transcript/Article/4228828/background-briefing-on-fy-2026-defense-budget/) (accessed 2026-07-22): DoD states $6.5 billion supports conventional and hypersonic munitions and nearly 2,000 critical weapons, many produced at maximum industrial-base capacity.
- **S4** — [NASA Standard for Propellants and Pressurants Used in Testing](https://standards.nasa.gov/node/1012) (accessed 2026-07-22): NASA specifies minimum certification and maintenance requirements for propellant and pressurant systems used in rocket-engine testing and support operations.
- **S5** — [NASA Parts Quality Control Process](https://oig.nasa.gov/office-of-inspector-general-oig/ig-17-016/) (accessed 2026-07-22): NASA OIG describes quality-control obligations for parts used in launch vehicles and propulsion systems.
- **S6** — [2024 Chartbook on Firms by Age of Primary Owner](https://www.fedsmallbusiness.org/-/media/project/smallbizcredittenant/fedsmallbusinesssite/fedsmallbusiness/files/2024/firms-in-focus/sbcs_chartbook2024_ownerage.pdf) (accessed 2026-07-22): Federal Reserve owner-age evidence used only as a broad succession proxy.
