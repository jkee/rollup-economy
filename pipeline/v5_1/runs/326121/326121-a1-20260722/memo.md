# 326121 — Unlaminated Plastics Profile Shape Manufacturing

*v5.1 Stage 1 research memo. Run `326121-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.42 · L 0.72 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-enabled quality, planning, maintenance, and administrative workflows layered onto repeat physical production.
**Weakness:** Six-digit evidence is scarce, and the dominant production work is physical while OEM pricing pressure can share savings away.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers of unlaminated plastic rods, tubes, and other profile shapes that repeatedly supply external OEM, distributor, and construction customers.
- Excluded: Captive profile-extrusion departments, shell entities, non-control financing vehicles, resin producers, and firms whose main activity belongs to plastic film, sheet, pipe, or laminated products.
- Customer and revenue model: Repeat business-to-business product sales, commonly quoted per unit, weight, or production run under purchase orders and supply agreements; customer-specific tooling and qualification can support recurring revenue.
- Deviation from default lens: none

## Executive view
Unlaminated plastic profile extrusion is a repeat B2B manufacturing activity with durable need for a physical operator and a meaningful but bounded AI opportunity. The best use cases sit around inspection, planning, quoting, documentation, maintenance, and process optimization; core extrusion and material handling remain capital- and labor-dependent.

## How AI changes the work
AI can combine machine vision with quality records, predict equipment failure from sensor histories, improve schedules and changeovers, assist quote and specification review, and automate routine back-office work. DOE identifies automated visual quality control, predictive maintenance, and operational optimization as practical manufacturing applications. Actual labor removal depends on sensor coverage, data quality, controls integration, and customers accepting AI-supported quality systems.

## Value capture
Savings may be retained during a quote or contract period, especially where qualification and tooling create switching friction. Renewal repricing, competitive rebids, resin-index clauses, and OEM cost-down demands return part of the gain to customers, so gross technical savings should not be treated as permanent margin.

## Firm availability
The frozen estimate indicates a nontrivial LMM population, but only independent firms with repeat external customers and transferable operations qualify. The central transfer assumption reflects normal private-company turnover and succession pressure, while excluding internal succession, minority deals, closures, and failed sales.

## Demand durability
BLS projects real output for broad plastics-product manufacturing to rise at 1.1% annually through 2034. Profiles should retain demand where corrosion resistance, low weight, insulation, and complex cross-sections matter, though construction cycles, imports, environmental regulation, recycled-content requirements, and material substitution create a wider six-digit range.

## Risks and uncertainty
The strongest evidence is four-digit rather than six-digit. Profile plants vary greatly by run length, customer concentration, product tolerance, and installed automation. A plant with commodity profiles, annual rebids, and one dominant buyer could pass productivity gains through quickly; a custom, qualified, data-rich extruder could retain more. Environmental restrictions or customer insourcing can impair demand independently of AI success.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2057 | — | OBSERVED | — |
| n | — | 128 | — | ESTIMATE | — |
| a | 0.14 | 0.22 | 0.31 | PROXY | S1, S2 |
| rho | 0.25 | 0.4 | 0.58 | ESTIMATE | S2 |
| e | 0.6 | 0.74 | 0.86 | ESTIMATE | — |
| s5 | 0.13 | 0.22 | 0.34 | ESTIMATE | — |
| q | 0.38 | 0.56 | 0.72 | ESTIMATE | — |
| d5 | 0.93 | 1.05 | 1.17 | PROXY | S3, S4 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.29 | 0.72 | 1.48 | ESTIMATE |
| F | 3.85 | 4.96 | 5.87 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.74 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is four-digit NAICS 326100 rather than six-digit 326121.
- a: Task shares are inferred from occupation groups and workflow knowledge, not directly measured.
- a: DOE documents feasible manufacturing applications, not realized labor substitution.
- rho: No source measures five-year implementation specifically for profile extrusion.
- rho: Implementation will vary sharply by production volume, SKU complexity, and installed controls.
- e: Eligibility is not directly observed and the frozen firm count is margin-bridged.
- e: Contract manufacturers with concentrated customer books may technically qualify but be unattractive or fragile transfer targets.
- s5: No six-digit deal-flow or owner-age series was located.
- s5: Aging ownership can lead to internal succession or closure rather than a qualifying external control transfer.
- q: Contract structure and customer power are not observed.
- q: The estimate concerns retention of implemented gross benefit, not implementation success or demand volume.
- d5: BLS projection is four-digit and ten-year, not six-digit and five-year.
- d5: The Plastics Industry Association figures cover the wider plastics value chain.
- d5: Construction-linked profile demand can deviate materially from broad plastics output.
- o: No direct study measures operator requirement for 326121.
- o: Automation could reduce headcount substantially without removing the need for a legally and operationally accountable manufacturer.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 326100 Plastics Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-22): Observed broad-industry employment and wage mix: 605,750 total employees; management 5.09%; business and financial operations 3.51%; metal and plastic workers 25.97%; miscellaneous assemblers 11.29%; detailed extrusion, molding, packaging, and material-handling employment shares.
- **S2** — [AI for Energy: Opportunities for a Modern Grid and Clean Energy Economy](https://www.energy.gov/sites/default/files/2024-04/AI%20EO%20Report%20Section%205.2g%28i%29_043024.pdf) (accessed 2026-07-22): DOE describes AI in manufacturing for generative design, automated visual quality control, advanced characterization, operational optimization, predictive maintenance with IoT sensors, and material sorting.
- **S3** — [Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects NAICS 326100 real output from $190.7 billion in 2024 to $212.4 billion in 2034, a 1.1% compound annual increase, and employment from 592,500 to 618,800.
- **S4** — [2025 Size and Impact of the U.S. Plastics Industry](https://www.plasticsindustry.org/data-report/size-and-impact-2025/) (accessed 2026-07-22): The industry association reports more than one million plastics-sector jobs and $551 billion of shipments in 2024 and describes sector growth and a two-year outlook, providing broad market context rather than a six-digit forecast.
