# 331523 — Nonferrous Metal Die-Casting Foundries

*v5.1 Stage 1 research memo. Run `331523-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.09 · L 0.60 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat engineered programs create recurring quoting, quality, maintenance, scheduling, and documentation workflows around a durable physical service.
**Weakness:** Physical production dominates labor while projected foundry contraction and OEM bargaining power constrain durable retained gains.

## Business-model lens
- Included: Independent US nonferrous die-casting foundries in the approximately $1-10 million normalized EBITDA band repeatedly producing customer-designed cast components under external supply programs.
- Excluded: Captive foundries, firms that cast and further manufacture their own finished products, primary or secondary metal producers without contract die casting, shells, non-control financing vehicles, and firms outside the EBITDA band.
- Customer and revenue model: Recurring business-to-business programs priced per part or lot, usually supported by tooling, qualification, quality requirements, metal surcharges, purchase orders, releases, and annual or multiyear supply agreements.
- Deviation from default lens: none

## Executive view
Nonferrous die casting provides repeat, qualified contract-manufacturing programs and moderate labor intensity, but most work is physical and capital-linked. AI has credible uses in quoting, engineering documentation, quality analytics, maintenance support, scheduling, and administration rather than molten-metal production itself.

## How AI changes the work
AI can retrieve prior quotes and process knowledge, draft routings and documentation, identify defect patterns, prioritize maintenance, assist schedules, and automate routine purchasing and customer updates. Die changes, machine tending, melting, trimming, finishing, inspection release, handling, and repair remain physical or human-supervised.

## Value capture
Yield, uptime, and quality gains are less visible and more retainable than back-office savings, but concentrated OEM buyers use cost-down clauses, open-book costing, and rebids. Metal-price movements are commonly separated from conversion economics.

## Firm availability
The frozen dataset estimates 81 firms in the band, but eligibility depends on captive status, customer programs, environmental liabilities, equipment condition, management depth, and a margin bridge borrowed from machinery. General owner aging provides only indirect transfer evidence.

## Demand durability
BLS projects declining foundry output, while nonferrous lightweighting and part consolidation offer offsets. Powertrain transition, imports, industrial cycles, and program concentration create a wide range around a modest decline.

## Risks and uncertainty
The main gaps are a six-digit wage-weighted task map, current automation, direct die-casting shipments, end-market mix, contract terms, environmental exposure, customer approvals, and the true EBITDA-band population. One lost platform can overwhelm incremental AI savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1995 | — | OBSERVED | — |
| n | — | 81 | — | ESTIMATE | — |
| a | 0.09 | 0.15 | 0.23 | PROXY | S1, S2 |
| rho | 0.32 | 0.5 | 0.67 | ESTIMATE | S3, S4 |
| e | 0.5 | 0.68 | 0.82 | ESTIMATE | S1, S4 |
| s5 | 0.13 | 0.24 | 0.37 | PROXY | S5, S4 |
| q | 0.32 | 0.54 | 0.73 | ESTIMATE | S1 |
| d5 | 0.84 | 0.96 | 1.1 | PROXY | S6, S1 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.23 | 0.60 | 1.23 | ESTIMATE |
| F | 2.95 | 4.27 | 5.21 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 8.06 | 9.50 | 10.00 | ESTIMATE |

## Caveats
- a: The OEWS source covers all foundries, not 331523.
- a: The estimate excludes gains requiring new physical automation rather than AI substitution or avoided hiring.
- rho: Published technical feasibility does not establish economical deployment in LMM plants.
- rho: Environmental and customer controls limit autonomous changes to furnace and casting parameters.
- e: No observed eligibility denominator was found.
- e: The injected n=81 is an ESTIMATE using a machinery margin rather than a die-casting-specific margin.
- s5: Owner-age data are all-industry and from data year 2018.
- s5: Owner age is a succession-pressure proxy rather than an observed transfer probability.
- q: No contract-level retention dataset was found.
- q: Retention varies by customer concentration, qualification difficulty, tooling ownership, and available foundry capacity.
- d5: Foundry-wide value output is not constant-quality die-casting volume.
- d5: Automotive program mix can make individual firms diverge sharply from the industry trend.
- o: Process substitution affects quantity and belongs primarily in d5.
- o: Digital customer interfaces can remove transaction work without eliminating the foundry operator.

## Sources
- **S1** — [NAICS 331523: Nonferrous Metal Die-Casting Foundries](https://www.census.gov/naics/?details=331523&input=331523&year=2022) (accessed 2026-07-22): Census defines the industry as introducing purchased molten nonferrous metal under high pressure into molds or dies to make castings and excludes establishments that further manufacture castings into finished products.
- **S2** — [Foundries - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_331500.htm) (accessed 2026-07-22): BLS provides employer-survey occupation and wage estimates for foundries across production, maintenance, engineering, management, and administrative occupations, used as the broader occupation-mix proxy.
- **S3** — [Occupational projections and worker characteristics, 2024-2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): BLS reports 154,600 molding, coremaking, and casting machine setters, operators, and tenders in 2024 and projects 148,800 in 2034, a 3.8% decline.
- **S4** — [Secondary Aluminum Production: National Emission Standards for Hazardous Air Pollutants](https://www.epa.gov/stationary-sources-air-pollution/secondary-aluminum-production-national-emission-standards) (accessed 2026-07-22): EPA identifies furnace and related secondary-aluminum operations as sources of organic and inorganic hazardous air pollutants and particulate metals subject to process and emissions controls, supporting compliance and accountability constraints.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The 2019 Annual Business Survey infographic reports 51% of responding employer-business owners were age 55 or older; estimates cover 4.1 million responding owners in data year 2018.
- **S6** — [Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects foundry employment declining from 106,000 in 2024 to 90,400 in 2034 and real output from $26.9 billion to $24.8 billion, a 0.8% annual output decline.
