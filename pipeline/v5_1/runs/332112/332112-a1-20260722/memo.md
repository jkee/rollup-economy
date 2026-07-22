# 332112 — Nonferrous Forging

*v5.1 Stage 1 research memo. Run `332112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.76 · L 0.60 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Scarce qualified nonferrous capacity and switching costs support durable demand and retention of yield, quality, and reliability improvements.
**Weakness:** The transferable population is exceptionally small, while most labor remains physical and customer qualification constrains implementation.

## Business-model lens
- Included: Independent US aluminum, titanium, nickel, copper, magnesium, and other nonferrous forging firms in the approximately $1-10 million normalized EBITDA band repeatedly producing qualified forged components for external customers.
- Excluded: Captive forging departments, iron and steel forgers, nonferrous mills without outsourced forging programs, firms manufacturing primarily proprietary finished products, shells, non-control financing vehicles, and firms outside the EBITDA band.
- Customer and revenue model: Recurring engineered business-to-business programs priced per part, weight, or lot with tooling, setup, heat treatment, testing, machining or finishing, alloy surcharges, purchase orders, releases, and multiyear qualification or supply agreements.
- Deviation from default lens: none

## Executive view
Nonferrous forging offers durable, highly qualified physical programs and potentially strong retention, but the frozen LMM universe is only 25 estimated firms. AI is a support layer for quoting, engineering records, quality, maintenance, scheduling, and administration rather than a substitute for the forging operation.

## How AI changes the work
AI can retrieve analogous jobs, assist estimates and instructions, optimize heating and schedules, summarize inspection trends, prioritize maintenance, and draft records. Billet handling, heating, press or hammer operation, die work, heat treatment, testing release, and repair remain physical or human-supervised.

## Value capture
Scarce alloys, qualifications, tooling, traceability, and switching costs help retain yield, energy, delivery, and reliability gains. Metal pass-through, open-book costing, cost-down provisions, and productivity sharing return a portion to customers.

## Firm availability
The frozen estimate of 25 band firms is exceptionally small and depends on a machinery margin bridge. Captive status, end-market qualifications, export controls, equipment, customer concentration, management, and environmental liabilities determine the already narrow transferable pool.

## Demand durability
Aerospace, defense, lightweight transportation, and specialized industrial applications support modest growth, while imports, alloy prices, cycles, and alternative processes create downside. Broad data are positive but only indirect for this small segment.

## Risks and uncertainty
Key gaps are six-digit tasks and shipments, alloy and end-market mix, current automation, program backlogs, customer contracts, export controls, equipment, environmental liabilities, and true EBITDA. One program loss or seller misclassification can materially change the opportunity.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2276 | — | OBSERVED | — |
| n | — | 25 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.22 | PROXY | S1, S2, S3 |
| rho | 0.29 | 0.47 | 0.64 | ESTIMATE | S4, S5 |
| e | 0.48 | 0.67 | 0.82 | ESTIMATE | S1, S5 |
| s5 | 0.11 | 0.21 | 0.33 | PROXY | S6, S5 |
| q | 0.4 | 0.63 | 0.81 | ESTIMATE | S1, S7 |
| d5 | 0.9 | 1.05 | 1.22 | PROXY | S3, S7, S8 |
| o | 0.97 | 0.99 | 1 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.60 | 1.28 | ESTIMATE |
| F | 1.35 | 2.43 | 3.30 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.73 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is national and not specific to 332112.
- a: Highly regulated aerospace and defense programs can have unusually high documentation labor but also unusually low substitutability.
- rho: Digital-twin research demonstrates technical potential, not economical LMM implementation.
- rho: Existing simulation and process control must be separated from new AI benefit.
- e: No observed eligible-firm denominator was found.
- e: The injected n=25 uses a machinery margin bridge and is so small that a few misclassifications materially change the pool.
- s5: Owner-age evidence is all-industry and data year 2018.
- s5: Sparse transactions make any annualized transfer estimate unstable.
- q: No contract-level retention dataset was found.
- q: Retention is likely higher in scarce aerospace and defense qualifications than in automotive or general industrial programs.
- d5: Transportation aluminum consumption includes sheet, extrusions, castings, and other products, not just forgings.
- d5: Broad fabricated-metal output can diverge sharply from this tiny qualified segment.
- o: Process substitution is captured primarily in d5.
- o: Digital ordering and reporting can become self-service without eliminating the physical operator.

## Sources
- **S1** — [NAICS 332112: Nonferrous Forging](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Census identifies 332112 as nonferrous forging within fabricated metal product manufacturing and distinguishes it from iron and steel forging and adjacent forming processes.
- **S2** — [Forging Machine Setters, Operators, and Tenders, May 2023](https://www.bls.gov/oes/2023/may/oes514022.htm) (accessed 2026-07-22): BLS reports 9,170 forging-machine setters, operators, and tenders nationally in 2023 and defines their work as setting up, operating, or tending machines that shape parts.
- **S3** — [Occupational projections and worker characteristics, 2024-2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): BLS reports 8,800 forging-machine setters, operators, and tenders in 2024 and projects 7,200 in 2034, an 18.9% decline.
- **S4** — [Using Deep Reinforcement Learning for Zero Defect Smart Forging](https://arxiv.org/abs/2201.10268) (accessed 2026-07-22): The research develops a digital-twin optimization strategy for induction-heating control in a forging line using pyrometer temperature data, supporting technical feasibility while not establishing LMM economics.
- **S5** — [Aluminum Forming Effluent Guidelines](https://www.epa.gov/eg/aluminum-forming-effluent-guidelines) (accessed 2026-07-22): EPA identifies NAICS 332112 within the aluminum-forming effluent-guideline scope, supporting environmental process controls and accountable operation.
- **S6** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The 2019 Annual Business Survey infographic reports 51% of responding employer-business owners were age 55 or older; estimates cover 4.1 million responding owners in data year 2018.
- **S7** — [USGS Mineral Commodity Summaries 2025: Aluminum](https://pubs.usgs.gov/periodicals/mcs2025/mcs2025.pdf) (accessed 2026-07-22): USGS reports that transportation applications accounted for 36% of US aluminum consumption in 2024 and that primary aluminum production value was about $1.9 billion.
- **S8** — [Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects fabricated-metal-product real output increasing from $303.5 billion in 2024 to $329.5 billion in 2034, a 0.8% annual rate, while employment declines 3.9%.
