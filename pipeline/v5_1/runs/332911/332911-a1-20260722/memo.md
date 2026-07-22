# 332911 — Industrial Valve Manufacturing

*v5.1 Stage 1 research memo. Run `332911-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.84 · L 1.18 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Safety-critical physical infrastructure preserves demand and makes technical documentation and configuration workflows valuable.
**Weakness:** The industry predominantly sells proprietary products, so the recurring outsourced-service subset is small and unmeasured.

## Business-model lens
- Included: US lower-middle-market industrial-valve manufacturers repeatedly providing build-to-print, private-label, configured-to-order, or customer-engineered valve production programs to external industrial, water, energy, and infrastructure customers.
- Excluded: Standard catalog-product manufacturers without an outsourced production relationship, captive plants, fluid-power and plumbing-valve makers classified elsewhere, distributors, repair-only shops, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring engineered or contract production billed per valve or program, often with material surcharges, testing and documentation, drawings, pressure class, metallurgy, actuation, trim, inspection, and delivery requirements.
- Deviation from default lens: The NAICS definition is broad product manufacturing rather than inherently outsourced service. The lens is narrowed to repeat build-to-print, private-label, configured-to-order, and customer-engineered production programs to avoid mixing service-like contract manufacturers with standard catalog sellers.

## Executive view
Industrial valves have durable physical and safety-critical demand, and custom programs contain AI-addressable engineering and order workflows. The principal problem is lens fit: most firms sell products rather than an outsourced service, leaving a small and poorly measured build-to-print, private-label, or customer-engineered subset.

## How AI changes the work
Useful applications include specification comparison, configured quotes, drawing and bill-of-material analysis, production planning, procurement, quality-document generation, test-record review, nonconformance triage, maintenance knowledge, and customer communication. Machining, welding, assembly, inspection, pressure testing, material control, and engineering release remain operator-bound.

## Value capture
Approved designs, standards compliance, traceability, performance risk, and qualification support switching costs. Competitive bids, multiple approved suppliers, material escalation, framework agreements, and annual cost-down requests share efficiency gains.

## Firm availability
Only repeat contract, private-label, build-to-print, or customer-engineered manufacturers meet the service lens; standard catalog sellers do not. Succession may create supply among independent niche producers, but IP, approvals, strategic buyers, and customer concentration affect transferability.

## Demand durability
Valves remain essential in water, wastewater, pipeline, chemical, power, and process systems. Planned pipeline capacity and water modernization support end markets, but broader real valve output declined sharply through 2023, justifying a near-flat base with wide upside and downside.

## Risks and uncertainty
Major risks are low eligible share, project cyclicality, customer concentration, imports, metal costs, warranty and product liability, qualification failures, nuclear or pipeline standards, long sales cycles, obsolete designs, and lack of direct contract-manufacturer demand data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1867 | — | OBSERVED | — |
| n | — | 96 | — | ESTIMATE | — |
| a | 0.19 | 0.31 | 0.43 | PROXY | S2, S3, S4 |
| rho | 0.32 | 0.51 | 0.68 | ESTIMATE | S5, S6, S7 |
| e | 0.05 | 0.14 | 0.28 | ESTIMATE | S1, S2 |
| s5 | 0.11 | 0.23 | 0.36 | PROXY | S8 |
| q | 0.31 | 0.5 | 0.68 | ESTIMATE | S5, S6, S7 |
| d5 | 0.79 | 1.01 | 1.24 | PROXY | S9, S10, S11, S12 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1, S5, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.45 | 1.18 | 2.18 | ESTIMATE |
| F | 0.68 | 2.27 | 3.81 | ESTIMATE |
| C | 6.20 | 10.00 | 10.00 | ESTIMATE |
| D | 7.43 | 9.90 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation sources cover broader fabricated metal or manufacturing populations, not NAICS 332911.
- a: Engineering-to-order and catalog assembly plants have materially different exposure profiles.
- rho: No source directly observes five-year AI implementation in industrial-valve manufacturing.
- rho: Nuclear, pipeline, and severe-service valves should implement more slowly than low-criticality waterworks products.
- e: No public dataset separates contract manufacturing from proprietary product sales.
- e: Configured-to-order products can resemble a service but remain ordinary product sales unless the manufacturer is executing an outsourced customer program.
- s5: The owner-age proxy is not industry- or size-specific and measures owners rather than transactions.
- s5: Corporate and sponsor-owned manufacturers have no individual-owner retirement trigger.
- q: No public contract sample was available.
- q: Capture is stronger for severe-service and highly qualified valves than for standard build-to-print products with multiple approved suppliers.
- d5: The output series covers broader NAICS 33291 and ends in 2023.
- d5: Pipeline capacity and water funding do not translate one-for-one into domestic LMM contract-valve revenue.
- o: An accountable manufacturer remains necessary, but it may be a large integrated or offshore supplier rather than an LMM lens firm.
- o: Labor automation is captured in a and rho and is not deducted again here.

## Sources
- **S1** — [NAICS definition: 332911 Industrial Valve Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines industrial and municipal-water valve manufacturing and lists ball, butterfly, check, gate, globe, plug, solenoid, steam-trap, hydrant, and nuclear examples.
- **S2** — [2022 NAICS manufacturing-sector definition](https://www.census.gov/naics/?details=31&input=31&year=2022) (accessed 2026-07-22): Explains that manufacturing transforms materials into new products and that contract processors generally remain classified in the manufacturing industry of the processed materials.
- **S3** — [Fabricated Metal Product Manufacturing: NAICS 332](https://www.bls.gov/iag/tgs/iag332.htm) (accessed 2026-07-22): Lists machinists, team assemblers, production supervisors, welders, and machine operators among common fabricated-metal occupations and provides current earnings and hours.
- **S4** — [Producing the goods of the future: Job opportunities in manufacturing](https://www.bls.gov/careeroutlook/2026/article/manufacturing.htm) (accessed 2026-07-22): Reports that production occupations represented about half of manufacturing employment in 2024 and describes continuing automation and maintenance needs.
- **S5** — [ASME B16.34 Valves—Flanged, Threaded, and Welding End](https://www.asme.org/codes-standards/find-codes-standards/b16-34-valves-flanged-threaded-welding-end/2017/pdf) (accessed 2026-07-22): Covers valve pressure-temperature ratings, dimensions, tolerances, materials, nondestructive examination, testing, and marking.
- **S6** — [49 CFR 195.116 Valves](https://www.law.cornell.edu/cfr/text/49/195.116) (accessed 2026-07-22): Requires sound engineering design, material compatibility, hydrostatic shell and seat testing without leakage, position indication, and valve marking for hazardous-liquid pipelines.
- **S7** — [49 CFR 192.145 Valves](https://www.law.cornell.edu/cfr/text/49/192.145) (accessed 2026-07-22): Requires gas-pipeline valves to meet API 6D or equivalent performance, pressure-temperature limits, manufacturing tests, and anticipated operating conditions.
- **S8** — [Business Owners' Ages: Over Half of U.S. Business Owners Were Age 55 and Over](https://www.census.gov/library/visualizations/2020/comm/business-owners-ages.html) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 ABS, data year 2018.
- **S9** — [Real Sectoral Output for Metal Valve Manufacturing](https://fred.stlouisfed.org/data/IPUEN33291T010000000) (accessed 2026-07-22): Provides broader NAICS 33291 real-output index values, including 100.360 in 2019, 94.463 in 2022, and 86.353 in 2023.
- **S10** — [Sectoral Output for Metal Valve Manufacturing](https://fred.stlouisfed.org/series/IPUEN33291T300000000) (accessed 2026-07-22): Reports broader NAICS 33291 current-dollar sectoral output of $33.931 billion in 2022 and $33.807 billion in 2023.
- **S11** — [Most planned natural gas pipeline capacity additions in 2026 and 2027 originate in Texas](https://www.eia.gov/todayinenergy/detail.php?id=67707) (accessed 2026-07-22): Reports 44.9 Bcf per day of planned US pipeline capacity for 2026-27, with 70% already under construction.
- **S12** — [EPA Water Infrastructure](https://www.epa.gov/water-infrastructure) (accessed 2026-07-22): States that US water infrastructure is aging and requires repair and identifies federal financing and grant programs for drinking-water, wastewater, and stormwater projects.
