# 331313 — Alumina Refining and Primary Aluminum Production

*v5.1 Stage 1 research memo. Run `331313-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.52 · L 0.08 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High energy and downtime costs make reliable AI improvements in process control, maintenance, yield, and planning economically meaningful.
**Weakness:** The LMM acquisition universe may be effectively empty because viable primary-aluminum assets are capital-intensive and concentrated in large or strategic owners.

## Business-model lens
- Included: Independent U.S. businesses repeatedly refining alumina from bauxite or producing primary aluminum and aluminum alloys from alumina for sale to external customers, including integrated primary forming where it is part of the same operating business.
- Excluded: Bauxite mining alone, secondary aluminum and scrap remelting, downstream processors using purchased aluminum, captive or idle assets without external recurring revenue, passive entities, and operations without transferable control.
- Customer and revenue model: High-volume sales of alumina, primary aluminum, billet, slab, ingot, and related alloy forms to smelters, rolling mills, extruders, foundries, fabricators, and industrial customers, priced from commodity benchmarks, regional and product premiums, alloy and shape specifications, energy economics, freight, tariffs, and contractual terms.
- Deviation from default lens: none

## Executive view
Primary aluminum is a sensor-rich, energy-intensive continuous industry where AI can improve process stability, energy use, maintenance, quality, and planning. The acquisition lens is the central weakness: the already-low frozen count is likely overstated because ordinary LMM firms rarely own viable refineries or smelters.

## How AI changes the work
Models can detect cell and equipment anomalies, predict failures, optimize energy and material inputs, support laboratory and quality decisions, and improve scheduling, logistics, procurement, sales, and administrative work. Hazardous physical operations, maintenance, permitting, environmental controls, and responsible release remain.

## Value capture
Energy, yield, reliability, alloy differentiation, qualification, and delivery can protect some gains. Transparent LME pricing, observable premiums, global capacity, imports, tariffs, and customer bargaining pass much of the benefit through.

## Firm availability
Only 32 employer establishments are reported, and most viable assets are likely large-group operations. Machinery-margin bridging is especially unreliable here, so few if any businesses may satisfy independent external revenue, $1 million to $10 million EBITDA, and transferable-control requirements.

## Demand durability
Aluminum serves transportation, packaging, construction, electrical, aerospace, and industrial markets, but growing use can be supplied by imports and recycled metal rather than domestic primary production. Nearly all remaining primary volume still requires an accountable physical operator.

## Risks and uncertainty
Key risks are energy prices and contracts, curtailment or closure, commodity and premium volatility, imports and tariffs, recycled-metal substitution, environmental liabilities, catastrophic process errors, legacy integration, cyber-physical security, capital intensity, and severe LMM misclassification.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2415 | — | OBSERVED | — |
| n | — | 4 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.31 | PROXY | S1, S2, S3 |
| rho | 0.32 | 0.49 | 0.65 | ESTIMATE | S2, S3, S4 |
| e | 0.02 | 0.1 | 0.25 | ESTIMATE | S1, S4, S5 |
| s5 | 0.05 | 0.12 | 0.25 | PROXY | S4, S7 |
| q | 0.18 | 0.35 | 0.52 | PROXY | S4, S5 |
| d5 | 0.85 | 1.01 | 1.2 | PROXY | S4, S5, S6 |
| o | 0.99 | 0.998 | 1 | ESTIMATE | S1, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.37 | 0.99 | 1.95 | ESTIMATE |
| F | 0.01 | 0.08 | 0.36 | ESTIMATE |
| C | 3.60 | 7.00 | 10.00 | PROXY |
| D | 8.41 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS combines primary production with downstream aluminum processing.
- a: Manufacturing AI examples establish capability, not adoption or incremental labor displacement at U.S. smelters.
- rho: Energy, yield, and uptime improvements do not necessarily substitute labor.
- rho: Alumina refineries, modern smelters, older potlines, and integrated casthouses have different data and control maturity.
- e: Establishments are not firms and include units of large corporate groups.
- e: The frozen n is margin-bridged from Machinery, an especially poor analogue for energy- and capital-intensive primary aluminum.
- s5: The SBA statistic is cross-industry and is not a completed-transfer rate.
- s5: Plant or asset sales, closures, and changes in joint-venture interests may not qualify as transfers of eligible firms.
- q: Alumina, commodity primary metal, value-added alloys, and casthouse products have different pricing power.
- q: Alcoa is much larger and more vertically integrated than the target lens.
- d5: BLS output covers downstream aluminum processing as well as NAICS 331313 activities.
- d5: USGS industry totals do not isolate the eligible LMM lens, and recycled metal can satisfy end demand without domestic primary output.
- o: Imports or recycled aluminum can displace a domestic operator without making software the supplier.
- o: Operator requirement does not imply unchanged headcount or ownership.

## Sources
- **S1** — [331313: Alumina Refining and Primary Aluminum Production - Census Bureau Profile](https://data.census.gov/profile/331313_-_Alumina_Refining_and_Primary_Aluminum_Production?codeset=naics~331313) (accessed 2026-07-23): Defines the industry and reports 32 employer establishments in the 2023 County Business Patterns profile.
- **S2** — [Alumina and Aluminum Production and Processing - May 2023 OEWS](https://www.bls.gov/oes/2023/may/naics4_331300.htm) (accessed 2026-07-23): Provides the broader 331300 occupational mix, including a 51.25% production-occupation share and employment across maintenance, materials, technical, management, commercial, and office roles.
- **S3** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-23): Documents manufacturing AI applications in predictive maintenance, quality, demand forecasting, energy and resource management, scheduling, and digital twins, plus adoption barriers.
- **S4** — [Alcoa Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1675149/000119312526077167/aa-20251231.htm) (accessed 2026-07-23): Documents vertical integration, primary-aluminum end markets, LME and premium pricing, supply-demand and inventory exposure, tariffs, transportation, energy, capacity, and operating risks.
- **S5** — [Mineral Commodity Summaries 2026 - Aluminum](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf) (accessed 2026-07-23): Provides U.S. primary aluminum value and industry statistics and reports about 3.6 million tons of aluminum recovered from purchased scrap in 2025, supporting primary-versus-secondary substitution analysis.
- **S6** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-23): Projects broader 331300 real output from $38.1 billion in 2024 to $39.9 billion in 2034, approximately 0.5% annually.
- **S7** — [5 Challenges for Family-Owned Businesses](https://www.sba.gov/blog/5-challenges-family-owned-businesses) (accessed 2026-07-23): Reports that 47% of owners expecting to retire within five years do not have a successor, used only as a broad succession-pressure proxy.
