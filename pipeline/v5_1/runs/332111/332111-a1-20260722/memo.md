# 332111 — Iron and Steel Forging

*v5.1 Stage 1 research memo. Run `332111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.89 · L 0.52 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Qualified repeat programs and scarce forging capacity support durable operator demand and retention of less visible yield and reliability gains.
**Weakness:** A tiny capital-intensive population with predominantly physical labor limits scalable AI substitution and transferable-firm volume.

## Business-model lens
- Included: Independent US iron and steel open-die, impression-die, press, hammer, and seamless rolled-ring forging firms in the approximately $1-10 million normalized EBITDA band repeatedly producing qualified forged components for external customers.
- Excluded: Captive forging departments, steel mills without outsourced forging programs, custom roll formers, nonferrous forgers, firms manufacturing primarily proprietary finished products, shells, non-control financing vehicles, and firms outside the EBITDA band.
- Customer and revenue model: Recurring engineered business-to-business programs priced per part, weight, or lot, with tooling, setup, heat treatment, testing, finishing, steel surcharges, purchase orders, releases, and multiyear qualification or supply agreements.
- Deviation from default lens: none

## Executive view
Iron and steel forging is a durable, qualified physical manufacturing service with moderate labor intensity but a very small estimated LMM pool. AI is useful around quoting, process records, quality analytics, maintenance knowledge, scheduling, and administration rather than the hot-forming operation itself.

## How AI changes the work
AI can retrieve analogous jobs, assist estimates and work instructions, optimize schedules, summarize inspection trends, prioritize maintenance, and draft records. Heating, manipulation, hammer or press operation, die work, trimming, heat treatment, testing release, and repair remain physical or human-supervised.

## Value capture
Qualification, tooling, scarce press capacity, and switching costs help retain yield, energy, uptime, and delivery gains. Steel surcharges, cost-down clauses, open-book costing, and rebids return part of recurring savings.

## Firm availability
The frozen dataset estimates only 40 firms in the band and uses a machinery margin bridge. Captive status, qualified programs, environmental obligations, equipment, customer concentration, capital plans, and stand-alone management determine the transferable pool.

## Demand durability
Defense, aerospace, transportation, energy, and industrial replacement support forged parts, while imports, cycles, and process substitution create downside. Broad fabricated-metal growth and current steel shipments support a flat central five-year quantity case despite falling forging-machine employment.

## Risks and uncertainty
The largest gaps are six-digit task and shipment data, current automation, customer program mix, imports, pricing terms, environmental liabilities, equipment condition, and true EBITDA. The small population and high customer concentration make aggregate estimates fragile.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2191 | — | OBSERVED | — |
| n | — | 40 | — | ESTIMATE | — |
| a | 0.07 | 0.13 | 0.21 | PROXY | S1, S2, S3 |
| rho | 0.28 | 0.46 | 0.63 | ESTIMATE | S3, S4 |
| e | 0.5 | 0.69 | 0.83 | ESTIMATE | S1, S4 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S5, S4 |
| q | 0.38 | 0.61 | 0.79 | ESTIMATE | S1 |
| d5 | 0.87 | 1 | 1.16 | PROXY | S6, S7, S3 |
| o | 0.97 | 0.99 | 1 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.52 | 1.16 | ESTIMATE |
| F | 1.97 | 3.15 | 4.04 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.44 | 9.90 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is national and not specific to 332111.
- a: The estimate excludes conventional mechanization or robotics unless AI directly enables labor substitution.
- rho: No representative LMM implementation study was found.
- rho: Operator employment decline can result from mechanization and should not be attributed wholly to AI.
- e: No observed eligibility denominator was found.
- e: The injected n=40 is an ESTIMATE using a machinery EBITDA margin and may misclassify steel forgers.
- s5: Owner-age evidence is all-industry and data year 2018.
- s5: The number of potential buyers and sellers is small, making annual deal flow lumpy.
- q: No contract-level retention dataset was found.
- q: Retention varies between defense or aerospace qualifications and price-competed automotive or industrial programs.
- d5: Upstream steel shipments are not forging demand.
- d5: Broad fabricated-metal real output can diverge from the small steel-forging segment.
- o: Manufacturing-process substitution affects quantity and is captured mainly in d5.
- o: Self-service ordering can remove transaction labor without removing the accountable forger.

## Sources
- **S1** — [NAICS 332111: Iron and Steel Forging](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Census defines iron and steel forging and notes that establishments may perform surface finishing such as cleaning and deburring on their forgings.
- **S2** — [Forging Machine Setters, Operators, and Tenders, May 2023](https://www.bls.gov/oes/2023/may/oes514022.htm) (accessed 2026-07-22): BLS reports 9,170 forging-machine setters, operators, and tenders nationally in 2023 and defines their work as setting up, operating, or tending machines that taper, shape, or form parts.
- **S3** — [Occupational projections and worker characteristics, 2024-2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): BLS reports 8,800 forging-machine setters, operators, and tenders in 2024 and projects 7,200 in 2034, an 18.9% decline.
- **S4** — [Iron and Steel Manufacturing Effluent Guidelines](https://www.epa.gov/eg/iron-and-steel-manufacturing-effluent-guidelines) (accessed 2026-07-22): EPA identifies forging among regulated iron and steel manufacturing processes alongside hot forming, heat treatment, pickling, descaling, surface cleaning, and finishing.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The 2019 Annual Business Survey infographic reports 51% of responding employer-business owners were age 55 or older; estimates cover 4.1 million responding owners in data year 2018.
- **S6** — [Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects fabricated-metal-product real output increasing from $303.5 billion in 2024 to $329.5 billion in 2034, a 0.8% annual rate, while employment declines 3.9%.
- **S7** — [AISI Releases Revised 2025 Steel Shipment Data](https://www.steel.org/2026/03/aisi-releases-revised-2025-steel-shipment-data/) (accessed 2026-07-22): The American Iron and Steel Institute reports full-year 2025 steel shipments of 91,158,528 net tons, up 5.1% from 86,698,917 in 2024.
