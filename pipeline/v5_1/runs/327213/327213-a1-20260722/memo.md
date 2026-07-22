# 327213 — Glass Container Manufacturing

*v5.1 Stage 1 research memo. Run `327213-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.92 · L 0.42 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repetitive, sensor-rich production supports tangible AI-assisted quality and uptime improvements while every surviving unit of glass demand needs a physical manufacturer.
**Weakness:** A steep recent domestic production decline and possibly near-empty independent LMM target pool make demand and transferability the central concerns.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers of glass packaging, bottling, and canning containers that repeatedly supply external beverage, food, pharmaceutical, cosmetic, or other packaging customers.
- Excluded: Captive internal plants, non-control investment vehicles, pure distributors, container fillers, cullet processors that do not manufacture containers, and manufacturers of non-container glass products are excluded.
- Customer and revenue model: Repeat business-to-business container sales under volume programs, forecasts, purchase orders, or supply contracts, priced primarily by unit and specification with energy, freight, and raw-material economics influencing negotiations.
- Deviation from default lens: none

## Executive view
Glass containers are a repeat B2B product with sensor-rich continuous manufacturing, but the domestic output trend is weak and the true independent LMM pool may be tiny. AI can improve inspection, process control, maintenance, scheduling, and administration, while physical production and customer bargaining limit labor substitution and retained economics.

## How AI changes the work
Repetitive high-speed lines create practical uses for vision inspection, anomaly detection, furnace and forming optimization, maintenance prediction, scheduling, and technical documentation. Deployment must integrate with legacy controls and quality systems without disrupting continuous furnaces, making supervised implementation more credible than autonomous labor replacement.

## Value capture
Avoided scrap, downtime, energy, overtime, and back-office hiring can create value. Large packaging customers, recurrent negotiations, and competitive bids recapture part of it; qualification, molds, freight, consistent color and quality, and dependable capacity preserve some producer retention.

## Firm availability
The injected LMM estimate is only 11 firms, and receipts do not reveal normalized EBITDA or ownership independence. Integrated groups, captive plants, and heavy capital requirements may leave very few eligible control targets, while no six-digit transfer cohort was available.

## Demand durability
Glass containers remain necessary in beverage, food, pharmaceutical, cosmetic, and other packaging streams, but domestic real production dropped sharply from 2022 through 2025. Material substitution, imports, lightweighting, reuse, and customer packaging decisions create downside, even as inertness and recyclability support a continuing base.

## Risks and uncertainty
Key unknowns are plant-level eligibility, current tasks, AI adoption and realized savings, contract pass-through, and qualifying transfers. Energy exposure, furnace outages, environmental liabilities, customer concentration, line utilization, import competition, and continued packaging substitution can dominate the AI case.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1523 | — | OBSERVED | — |
| n | — | 11 | — | ESTIMATE | — |
| a | 0.09 | 0.17 | 0.27 | PROXY | S2, S3 |
| rho | 0.22 | 0.41 | 0.6 | PROXY | S3 |
| e | 0.2 | 0.4 | 0.62 | ESTIMATE | S1 |
| s5 | 0.08 | 0.18 | 0.3 | ESTIMATE | — |
| q | 0.28 | 0.47 | 0.68 | ESTIMATE | — |
| d5 | 0.75 | 0.9 | 1.06 | PROXY | S4, S5 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.12 | 0.42 | 0.99 | PROXY |
| F | 0.26 | 0.94 | 1.79 | ESTIMATE |
| C | 5.60 | 9.40 | 10.00 | ESTIMATE |
| D | 7.12 | 8.91 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational mix is 2016 and four-digit rather than current six-digit data.
- a: The machine-learning case is from flat-glass furnace control and only an adjacent process proxy.
- rho: No representative 327213 implementation or realized-savings dataset was found.
- rho: This is the implementation share of exposed opportunity, not a prediction for total productivity.
- e: The injected n of 11 is an ESTIMATE derived from receipts and a sector margin rather than observed 327213 EBITDA.
- e: Firm and establishment boundaries can differ substantially in a multi-plant manufacturing industry.
- s5: Neither the eligible denominator nor qualifying transfer numerator is observed.
- s5: A single transaction materially changes the measured rate when the population is this small.
- q: No representative contract-level pass-through data was available.
- q: Retention can differ sharply between specialized pharmaceutical or cosmetic containers and high-volume beverage bottles.
- d5: Production is not demand and can move with imports, exports, inventories, and plant closures.
- d5: EPA's material data are from 2018 and document the installed container stream, not a current growth forecast.
- o: This is bounded judgment rather than a measured share.
- o: Extensive automation can reduce staffing without eliminating the accountable operating firm under this definition.

## Sources
- **S1** — [2022 NAICS Definition: 327213 Glass Container Manufacturing](https://www.census.gov/naics/?details=3272&input=3272&year=2022) (accessed 2026-07-22): Defines the industry as establishments manufacturing glass packaging, bottling, and canning containers.
- **S2** — [May 2016 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 327200](https://www.bls.gov/oes/2016/may/naics4_327200.htm) (accessed 2026-07-22): Reports 85,250 jobs and broad occupation shares including production 55.08%, office support 8.50%, management 3.97%, engineering 2.79%, business and financial operations 2.22%, and sales 2.35%.
- **S3** — [High Performance Computing Improves Manufacturing Productivity and Competitiveness in the Glass Industry](https://www.energy.gov/cmei/ammto/articles/high-performance-computing-improves-manufacturing-productivity-and) (accessed 2026-07-22): Adjacent process evidence: a Vitro/LLNL machine-learning surrogate reduced glass-furnace analysis from as much as two weeks to minutes and was suitable for real-time control.
- **S4** — [Industrial Production: Glass Container Manufacturing (NAICS 327213)](https://fred.stlouisfed.org/series/IPG327213A) (accessed 2026-07-22): Federal Reserve six-digit real-output proxy: 108.9957 in 2022, 98.9677 in 2023, 86.4477 in 2024, and 80.5928 in 2025, with 2017=100.
- **S5** — [EPA Glass: Material-Specific Data](https://19january2021snapshot.epa.gov/facts-and-figures-about-materials-waste-and-recycling/glass-material-specific-data_.html) (accessed 2026-07-22): Documents major container uses and reports 3.1 million tons of recycled glass containers in 2018, a 31.3% recycling rate.
