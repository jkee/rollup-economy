# 212290 — Other Metal Ore Mining

*v5.1 Stage 1 research memo. Run `212290-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Strategic demand and supply-security policy support physical production of specialty and critical metal ores.
**Weakness:** The eligible firm population is unknown, and most classified businesses likely monetize owned commodities rather than recurring outsourced services.

## Business-model lens
- Included: US lower-middle-market firms classified in development, extraction, or beneficiation of metal ores other than iron, gold, silver, copper, nickel, lead, and zinc that repeatedly provide externally contracted or customer-dedicated mining, custom milling, or concentrate-supply operations.
- Excluded: Mine-owning commodity producers without an outsourced-service relationship, exploration shells without operating revenue, captive units, royalty and financing vehicles, dormant properties, firms outside the EBITDA band, uranium enrichment, and support contractors classified elsewhere.
- Customer and revenue model: Potentially eligible revenue comes from repeat contract operation, custom beneficiation, toll milling, customer-dedicated processing, or service-like long-term supply arrangements involving ores such as uranium-vanadium, molybdenum, tungsten, tantalum, antimony, ilmenite, and related specialty metals; ordinary merchant sales of owned ore are not by themselves outsourced services.
- Deviation from default lens: The default lens is retained, but the activity description explicitly spans materially different commodity and mine models; no commodity subset is selected because the code must be assessed as assigned.

## Executive view
Other metal ore mining has strategically important physical demand but is a poor and unquantifiable fit for the recurring outsourced-service lens. The code combines very different commodities and development stages, and the LMM firm-count denominator is explicitly unavailable.

## How AI changes the work
AI can improve geology, planning, process control, predictive maintenance, environmental reporting, safety monitoring, and administration. Physical extraction, beneficiation, equipment repair, sampling, radiation or chemical protection, and statutory accountability remain operator-intensive.

## Value capture
Global or negotiated mineral prices may preserve some cost savings initially, but grades, royalties, suppliers, environmental liabilities, contract resets, financing, and volatile commodity cycles absorb benefits. Economics differ materially by mineral and project stage.

## Firm availability
Eligibility cannot be estimated without a defensible LMM firm roster and contract data. Most mine owners sell commodities rather than services, while custom mills or contract operations could qualify if they exist in the target band.

## Demand durability
Critical-mineral, defense, nuclear, and advanced-manufacturing needs support several included ores, but the industry's output can be dominated by a few project openings, restarts, or closures. Imports, processing capacity, permits, substitution, and recycling matter.

## Risks and uncertainty
Missing firm-count data, severe commodity heterogeneity, four-digit proxies, commodity volatility, project-stage risk, environmental liabilities, permits, processing bottlenecks, financing, and long development cycles make this record unusually uncertain.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2248 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.1 | 0.2 | 0.32 | PROXY | S2, S4 |
| rho | 0.25 | 0.44 | 0.62 | ESTIMATE | S4, S5 |
| e | — | — | — | MISSING | — |
| s5 | 0.07 | 0.17 | 0.31 | PROXY | S8 |
| q | 0.36 | 0.58 | 0.76 | ESTIMATE | S6, S7 |
| d5 | 0.9 | 1.14 | 1.43 | PROXY | S3, S6, S7 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S1, S4, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.22 | 0.79 | 1.78 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 8.64 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation mix covers all metal ore mining.
- a: Task exposure is inferred.
- a: The supplied compensation ratio is measured at ancestor 2122 and may not represent this small, heterogeneous six-digit industry.
- rho: NIOSH sources show research priorities and barriers rather than realized savings.
- rho: Implementation varies widely across open-pit, underground, in-situ recovery, and beneficiation operations.
- e: The assignment declares no defensible LMM firm-count value and prohibits estimating it.
- e: NAICS establishment classification does not reveal firm economics or customer contract structure.
- e: The product and operating models are exceptionally heterogeneous.
- s5: The evidence is cross-industry, owner-level, and dated 2018.
- s5: The underlying eligible population is unknown.
- s5: Property acquisitions and financing rounds are not necessarily qualifying control transfers.
- q: No source directly measures AI-benefit retention.
- q: Pricing and cost structure vary sharply by mineral.
- q: Commodity prices and project stage can overwhelm productivity effects.
- d5: The BLS series is four-digit and dominated by other metals.
- d5: Critical-material importance does not ensure domestic mine output.
- d5: A small number of project starts or shutdowns can dominate the ratio.
- o: Recycling and material substitution can reduce primary-mining quantity but are mainly reflected in demand.
- o: The accountable entity may consolidate into a larger miner or government-backed operator rather than disappear.

## Sources
- **S1** — [212290: Other Metal Ore Mining](https://data.census.gov/profile/212290_-_Other_Metal_Ore_Mining?codeset=naics~212290) (accessed 2026-07-23): Defines the industry and lists illustrative ores including antimony, tantalum, columbite, tungsten, ilmenite, uranium-radium-vanadium, and molybdenum.
- **S2** — [May 2023 OEWS: Metal Ore Mining](https://www.bls.gov/oes/2023/may/naics4_212200.htm) (accessed 2026-07-23): Reports the broader-industry occupational composition, including a large construction and extraction workforce plus engineering, science, office, and material-moving roles.
- **S3** — [Employment and output by industry, 2024–34](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-23): Projects metal ore mining real output from $26.0 billion in 2024 to $33.5 billion in 2034, a 2.6% annual compound rate.
- **S4** — [NIOSH Mining Health and Safety Research Contracts](https://www.cdc.gov/niosh/mining/about/contracts.html) (accessed 2026-07-23): Documents current work on autonomous mining, machine-learning perception, automated hazard recognition, safety analytics, and automation implementation barriers.
- **S5** — [Mining and Machinery Struck-by Injuries](https://www.cdc.gov/niosh/mining/topics/machinery-struck-by-injuries.html) (accessed 2026-07-23): Describes mining use of programmable control and proximity technology alongside functional-safety challenges and new software failure modes.
- **S6** — [Mineral Commodity Summaries 2026](https://pubs.usgs.gov/publication/mcs2026) (accessed 2026-07-23): Provides commodity-specific production, consumption, trade, recycling, prices, reserves, industry structure, and five-year statistics for more than 90 minerals and materials.
- **S7** — [2023 Critical Materials Assessment](https://www.energy.gov/sites/default/files/2023-05/2023-critical-materials-assessment.pdf) (accessed 2026-07-23): Assesses demand and supply risks for energy-relevant critical materials, including several specialty metals connected to the 212290 commodity basket.
- **S8** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-23): Reports that 51% of responding owners of US employer businesses were age 55 or older in 2018.
