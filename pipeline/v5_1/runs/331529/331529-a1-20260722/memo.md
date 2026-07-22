# 331529 — Other Nonferrous Metal Foundries (except Die-Casting)

*v5.1 Stage 1 research memo. Run `331529-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.25 · L 0.93 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High labor intensity and scarce, qualified specialty programs support AI assistance in quoting, quality, maintenance, engineering, and scheduling.
**Weakness:** Most labor is physical and alloy-specific, while the population is small and direct demand and transaction evidence are weak.

## Business-model lens
- Included: Independent US copper, brass, bronze, zinc, magnesium, titanium, and other nonaluminum nonferrous foundries outside die casting, in the approximately $1-10 million normalized EBITDA band, repeatedly producing customer-designed castings for external customers.
- Excluded: Aluminum foundries, die casters, captive foundries, establishments further manufacturing castings into their own finished products, primary smelters, shells, non-control financing vehicles, and firms outside the EBITDA band.
- Customer and revenue model: Recurring engineered business-to-business casting programs priced per part or lot with pattern, tooling, alloy, testing, finishing, and metal-surcharge economics under quotes, releases, purchase orders, and supply agreements.
- Deviation from default lens: none

## Executive view
Other nonferrous foundries combine very high injected labor intensity, scarce metallurgy, qualified repeat programs, and a meaningful estimated LMM population. AI opportunity remains confined mainly to quoting, engineering support, quality analytics, maintenance knowledge, scheduling, and administration because core work is physical.

## How AI changes the work
AI can retrieve comparable jobs, assist estimates and routings, analyze defect histories, prioritize maintenance, schedule work, and draft quality records. Molding, coremaking, alloying, melting, pouring, shakeout, finishing, test release, handling, and repair remain physical or human-supervised.

## Value capture
Special alloys, qualifications, patterns, and scarce alternative suppliers can protect operational gains. Metal surcharges, rebids, and customer cost-down demands still distribute a meaningful share of recurring savings.

## Firm availability
The frozen estimate of 78 band firms depends on a machinery margin bridge. Captive status, environmental obligations, concentrated customers, equipment, management depth, and retention of metallurgical knowledge determine actual eligibility and transferability.

## Demand durability
Electrification, infrastructure, defense, and specialty applications offset broad foundry contraction, while imports and process substitution remain threats. The result is a near-flat central demand case with large alloy- and customer-specific dispersion.

## Risks and uncertainty
The largest gaps are alloy-level tasks and shipments, current automation, end-market exposure, import competition, customer contracts, environmental liabilities, key-person risk, and true EBITDA. A single qualification loss or alloy-market shock can dominate incremental AI gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3541 | — | OBSERVED | — |
| n | — | 78 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.22 | PROXY | S1, S2, S3 |
| rho | 0.29 | 0.47 | 0.64 | ESTIMATE | S3, S4 |
| e | 0.5 | 0.68 | 0.82 | ESTIMATE | S1, S4 |
| s5 | 0.14 | 0.25 | 0.38 | PROXY | S5, S4 |
| q | 0.36 | 0.59 | 0.78 | ESTIMATE | S1, S6 |
| d5 | 0.86 | 0.99 | 1.15 | PROXY | S6, S7 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.93 | 1.99 | ESTIMATE |
| F | 3.00 | 4.27 | 5.20 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 8.26 | 9.80 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS data cover all foundries, not 331529.
- a: Copper-alloy, magnesium, titanium, and specialty foundries may have different engineering and inspection intensity.
- rho: No representative LMM implementation study was found.
- rho: Conventional casting simulation and statistical process control already automate part of the analytical work.
- e: No direct eligible-firm denominator was found.
- e: The injected n=78 uses a machinery margin bridge rather than a specialty-foundry margin.
- s5: Owner-age evidence is all-industry and data year 2018.
- s5: Owner age does not directly measure a firm's willingness or ability to transfer.
- q: No observed contract-level retention dataset was found.
- q: Retention is likely lower for standardized copper-alloy castings and higher for highly qualified specialty components.
- d5: AFS sales growth is nominal, one-year, and covers all metalcasting.
- d5: BLS output covers all foundries and is not physical 331529 constant-quality quantity.
- o: Process and material substitution are captured principally in d5.
- o: Digital interfaces can eliminate transactional labor without eliminating the operator.

## Sources
- **S1** — [NAICS 331529: Other Nonferrous Metal Foundries (except Die-Casting)](https://www.census.gov/naics/?details=331529&input=331529&year=2022) (accessed 2026-07-22): Census classifies establishments pouring nonaluminum nonferrous molten metal into molds without high-pressure die casting and distinguishes firms further manufacturing castings into finished products.
- **S2** — [Foundries - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_331500.htm) (accessed 2026-07-22): BLS provides employer-survey occupation and wage estimates for foundries across production, maintenance, engineering, management, and administrative work, used as the occupation-mix proxy.
- **S3** — [Occupational projections and worker characteristics, 2024-2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): BLS reports 154,600 molding, coremaking, and casting machine setters, operators, and tenders in 2024 and projects 148,800 in 2034, a 3.8% decline.
- **S4** — [Aluminum, Copper, and Other Nonferrous Foundries: NESHAP for Area Sources](https://www.epa.gov/stationary-sources-air-pollution/aluminum-copper-and-other-nonferrous-foundries-national-emission) (accessed 2026-07-22): EPA states that smaller aluminum, copper, and other nonferrous foundries are subject to air-toxics standards regulating metals including beryllium, cadmium, chromium, lead, manganese, and nickel.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The 2019 Annual Business Survey infographic reports 51% of responding employer-business owners were age 55 or older; estimates cover 4.1 million responding owners in data year 2018.
- **S6** — [Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects foundry employment declining from 106,000 in 2024 to 90,400 in 2034 and real output declining from $26.9 billion to $24.8 billion, a 0.8% annual rate.
- **S7** — [AFS Projects 1.9 Percent Casting Sales Growth for 2025](https://www.afsinc.org/news/2025/07/22/afs-projects-19-percent-casting-sales-growth-2025) (accessed 2026-07-22): The American Foundry Society projected 1.9% casting sales growth for 2025 in its Metalcasting Forecast & Trends release.
