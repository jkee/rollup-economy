# 331110 — Iron and Steel Mills and Ferroalloy Manufacturing

*v5.1 Stage 1 research memo. Run `331110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.58 · L 0.51 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Sensor-rich continuous operations create implementable AI opportunities in maintenance, quality, process control, and scheduling.
**Weakness:** Commodity pricing and the scarcity of genuinely LMM independent mills constrain both retention and transferable-firm opportunity.

## Business-model lens
- Included: Independent U.S. operators repeatedly producing raw steel, pig iron, ferroalloys, and mill shapes, sheet, strip, plate, bar, rod, wire, pipe, or tube from their own steelmaking for external customers.
- Excluded: Captive internal mills, passive asset entities, coke-only plants, purchased-steel rollers, downstream fabricators, nonferrous producers, and operations without a transferable going concern.
- Customer and revenue model: Repeat spot and contract product sales to automotive, construction, energy, machinery, appliance, service-center, infrastructure, and manufacturing customers, priced by ton, grade, form, processing, freight, and market or raw-material indices.
- Deviation from default lens: none

## Executive view
Steel mills offer real AI use cases in process monitoring, quality, maintenance, energy, scheduling, and administration, but decades of automation leave a limited incremental labor share. The more severe screen issue is firm eligibility: many establishments are large integrated assets, and the frozen LMM count relies on an imperfect machinery-margin bridge.

## How AI changes the work
AI can predict failures, detect defects, recommend furnace and rolling settings, optimize sequencing and energy, and automate laboratory, maintenance, logistics, and commercial paperwork. Human oversight remains essential for high-stakes process control, safety, metallurgy, maintenance, and incident response.

## Value capture
Specialty grades, yield, uptime, and quality improvements can retain value. Spot pricing, index-adjusted contracts, import competition, and periodic negotiations erode visible cost advantages over five years.

## Firm availability
The establishment base is much larger than the plausible independent LMM target set. Ultimate ownership, environmental obligations, capital needs, labor commitments, and cyclically normalized earnings must be resolved before treating the 58-firm estimate as actionable.

## Demand durability
Steel remains essential across infrastructure, construction, energy, transportation, and manufacturing, supporting roughly stable-to-growing physical demand. Remaining domestic volume still requires an accountable industrial producer even as AI changes internal work.

## Risks and uncertainty
Key risks are catastrophic process or model errors, cybersecurity, labor acceptance, environmental liabilities, decarbonization capex, electricity and raw-material volatility, tariffs, imports, global overcapacity, product substitution, cycle timing, and target-size misclassification.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1269 | — | OBSERVED | — |
| n | — | 58 | — | ESTIMATE | — |
| a | 0.11 | 0.2 | 0.3 | PROXY | S1, S2, S3 |
| rho | 0.32 | 0.5 | 0.66 | ESTIMATE | S2, S3 |
| e | 0.3 | 0.52 | 0.72 | ESTIMATE | S4 |
| s5 | 0.1 | 0.21 | 0.36 | PROXY | S8 |
| q | 0.25 | 0.43 | 0.62 | PROXY | S6, S7 |
| d5 | 0.88 | 1.07 | 1.25 | PROXY | S5, S6, S9 |
| o | 0.985 | 0.997 | 1 | ESTIMATE | S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.18 | 0.51 | 1.01 | ESTIMATE |
| F | 1.62 | 3.21 | 4.46 | ESTIMATE |
| C | 5.00 | 8.60 | 10.00 | PROXY |
| D | 8.67 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS data are for NAICS 331100 rather than 331110 and exclude self-employed workers.
- a: Large integrated and electric-arc-furnace mills may have materially different remaining automation opportunity from small specialty alloy producers.
- rho: NIST evidence is manufacturing-wide rather than steel-specific.
- rho: Process optimization that saves energy or material but not labor is outside this primitive unless it avoids labor or hiring.
- e: Census reports 359 establishments, not firms or LMM candidates.
- e: The frozen n uses a Machinery margin despite steel's distinct commodity cycles and capital structure, so band classification may be materially misleading.
- s5: The proxy covers family businesses generally rather than steel mills.
- s5: Internal strategic reorganizations and asset purchases do not necessarily qualify as control transfers of eligible firms.
- q: Public-company disclosures reflect far larger and more diversified producers than the frozen LMM lens.
- q: Retention differs sharply by spot versus contract sales, product grade, import exposure, and cycle point.
- d5: BLS output is not a direct physical-demand measure.
- d5: Tariffs and import restrictions can shift domestic production without equivalent change in total U.S. demand.
- o: Software may reduce operator headcount without eliminating the operator entity.
- o: Material substitution and imports primarily affect demand quantity rather than the need for an operator for remaining domestic production.

## Sources
- **S1** — [Iron and Steel Mills and Ferroalloy Manufacturing - May 2023 OEWS](https://www.bls.gov/oes/2023/may/naics4_331100.htm) (accessed 2026-07-23): Provides industry occupational employment and wage structure across production, maintenance, material-moving, engineering, office, sales, and management roles.
- **S2** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-23): Reports manufacturing AI adoption, barriers, and uses in predictive maintenance, quality, process control, resource management, scheduling, and digital twins.
- **S3** — [2026 Roadmap on AI and Machine Learning for Smart Manufacturing](https://www.nist.gov/publications/2026-roadmap-artificial-intelligence-and-machine-learning-smart-manufacturing) (accessed 2026-07-23): Identifies industrial-data, sensing, integration, trust, explainability, and reliability requirements for AI deployment in high-stakes manufacturing.
- **S4** — [331110: Iron and Steel Mills and Ferroalloy Manufacturing - Census Bureau Profile](https://data.census.gov/profile/331110_-_Iron_and_steel_mills_and_ferroalloy_manufacturing?codeset=naics~331110) (accessed 2026-07-23): Defines the industry and reports 359 employer establishments in 2023 County Business Patterns.
- **S5** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-23): Shows the BLS decade projection for 331110 output rising from 103.9 to 124.3, with 1.8% indicated annual growth.
- **S6** — [Nucor 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/73309/000119312526071575/nue-20251231.htm) (accessed 2026-07-23): Documents spot and contract pricing, monthly or quarterly index adjustments, 2025 demand conditions, end markets, and mill operating rates.
- **S7** — [Steel Dynamics 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1022671/000110465926021395/stld-20251231x10k.htm) (accessed 2026-07-23): Documents commodity cycles, raw-material pass-through risk, price competition, unexpected downtime, and 2025 stable steel demand.
- **S8** — [5 Challenges for Family-Owned Businesses](https://www.sba.gov/blog/5-challenges-family-owned-businesses) (accessed 2026-07-23): Reports that 47% of owners expecting to retire within five years do not have a successor.
- **S9** — [USGS Mineral Commodity Summaries 2026](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf) (accessed 2026-07-23): Estimates 2025 U.S. raw steel production and net steel mill product shipments at 82 million tons each, versus 79.5 million and 78.7 million tons in 2024.
