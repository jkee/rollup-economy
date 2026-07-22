# 333514 — Special Die and Tool, Die Set, Jig, and Fixture Manufacturing

*v5.1 Stage 1 research memo. Run `333514-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.52 · L 3.55 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Very high labor content and information-rich quoting, design, CAM, planning, and quality workflows across a large specialized supplier base.
**Weakness:** Simple fixtures and gauges can migrate to customers' additive cells while complex work remains craftsmanship- and cycle-dependent.

## Business-model lens
- Included: US lower-middle-market tool and die shops that repeatedly design, engineer, manufacture, modify, repair, validate, and support special dies, die sets, jigs, fixtures, gauges, and related production tooling for external manufacturers.
- Excluded: Industrial molds classified under 333511, cutting dies for nonmetal materials classified elsewhere, captive internal toolrooms, commodity machine shops without special-tooling work, brokers without production capability, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat B2B project and program revenue from custom tooling design and build, engineering changes, repair, refurbishment, spares, tryout, and support, priced through quotations, milestones, time and materials, or purchase orders, often with customer-owned tools.
- Deviation from default lens: none

## Executive view
Special tool, die, jig, and fixture manufacturing combines very high labor content with digital design and planning, supporting meaningful AI opportunity. The sector also faces a distinctive self-service threat: customers can increasingly print simple fixtures and gauges internally while still outsourcing complex precision tooling.

## How AI changes the work
AI can accelerate RFQ interpretation, similar-job search, DFM, estimating, CAD and CAM support, toolpaths, setup and scheduling, inspection plans, quality records, and knowledge transfer. Precision machining, fitting, assembly, tryout, repair, and final accountability remain skilled physical work.

## Value capture
Fixed-price jobs, urgent repairs, customer process knowledge, qualification, and delivery reliability protect benefits. Competitive bids, procurement benchmarks, change-order negotiations, and additive alternatives pass some gains to customers.

## Firm availability
The industry has many establishments and a plausible independent target base, but captive shops, owner dependence, customer concentration, workforce depth, equipment, quality systems, and backlog require verification. General succession evidence is directionally supportive but not industry-specific.

## Demand durability
Manufacturing continues to need tooling, and reshoring may support domestic shops. Additive manufacturing can both improve external shops and let customers self-produce simple jigs, fixtures, and gauges; complex dies and qualified precision tools remain operator-required.

## Risks and uncertainty
Owner and estimator dependence, apprenticeship gaps, fixed-price overruns, automotive and industrial cyclicality, offshore competition, customer concentration, machine capex, quality escapes, and customer insourcing are central. Evidence is weakest on task-level exposure, qualifying owners, completed transactions, retained savings, and additive displacement.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.402 | — | OBSERVED | — |
| n | — | 457 | — | ESTIMATE | — |
| a | 0.24 | 0.34 | 0.45 | PROXY | S1, S2 |
| rho | 0.49 | 0.65 | 0.78 | PROXY | S2, S3 |
| e | 0.44 | 0.6 | 0.74 | ESTIMATE | S4 |
| s5 | 0.15 | 0.24 | 0.35 | PROXY | S6 |
| q | 0.45 | 0.62 | 0.77 | ESTIMATE | — |
| d5 | 0.95 | 1.04 | 1.15 | ESTIMATE | S3, S4, S5 |
| o | 0.86 | 0.94 | 0.985 | PROXY | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.89 | 3.55 | 5.64 | PROXY |
| F | 5.53 | 6.76 | 7.69 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.17 | 9.78 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational proxy covers all metalworking machinery rather than 333514.
- a: Current CAD/CAM, quoting, ERP, robotics, and metrology automation are unknown.
- rho: Occupation projections and additive examples do not measure firm adoption probability.
- rho: Standard fixture families are more implementable than complex transfer dies and safety-critical tooling.
- e: Establishments are not firms and are not the frozen LMM denominator.
- e: The estimated firm count may include captive, project-fragile, or subscale operations.
- s5: The evidence measures cross-industry intentions rather than completed transfers.
- s5: Small shop asset sales and internal successions are poorly captured by deal databases.
- q: No public contract corpus measures pass-through.
- q: Emergency repair and qualified complex dies retain more than simple fixtures or competitively bid greenfield tools.
- d5: NIST sources describe technology and reshoring opportunities rather than a five-year demand forecast.
- d5: Automotive dies, aerospace fixtures, gauges, assembly jigs, and general industrial tools follow different cycles.
- o: The cited examples do not provide an industry displacement rate.
- o: Product elimination and total tooling demand remain in d5; o isolates insourcing and self-service.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 333500](https://www.bls.gov/oes/2023/may/naics4_333500.htm) (accessed 2026-07-22): Reports 59.81 percent production employment in broader metalworking machinery, including 12.71 percent machinists, and supplies the occupational wage mix used for the exposure proxy.
- **S2** — [Machinists and Tool and Die Makers, Occupational Outlook Handbook](https://www.bls.gov/ooh/production/machinists-and-tool-and-die-makers.htm) (accessed 2026-07-22): Describes CAD/CAM, CNC programming and operation, precision machining, fitting, polishing, and testing and projects tool-and-die maker employment declining 11 percent from 2024 to 2034 as automation reduces some tasks.
- **S3** — [Additive Manufacturing/3D Printing](https://www.nist.gov/mep/additive-manufacturing3d-printing) (accessed 2026-07-22): States that additive manufacturing enables customized jigs and fixtures, can bypass tooling lead time and costs for rapid design iterations, and improves low-volume economics, supporting both implementation and self-service displacement.
- **S4** — [Census Bureau Profile: 333514 Special Die and Tool, Die Set, Jig, and Fixture Manufacturing](https://data.census.gov/profile/333514_-_Special_Die_and_Tool%2C_Die_Set%2C_Jig%2C_and_Fixture_Manufacturing?codeset=naics~333514&g=010XX00US) (accessed 2026-07-22): Defines the industry as tool and die shops manufacturing special tools and fixtures such as cutting dies and jigs and reports 1,976 employer establishments in 2023, supporting scope and breadth without replacing the frozen firm count.
- **S5** — [How Smaller Manufacturers Can Leverage Reshoring Opportunities for Growth](https://www.nist.gov/blogs/manufacturing-innovation-blog/how-smaller-manufacturers-can-leverage-reshoring-opportunities) (accessed 2026-07-22): States that reshoring has gained momentum as firms reconsider offshore supply chains because of cost, geopolitical risk, and disruption, used as directional demand support rather than a forecast.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of employer-business owners surveyed in fall 2024 planned to sell or transfer ownership within five years, used as a cross-industry transfer proxy.
