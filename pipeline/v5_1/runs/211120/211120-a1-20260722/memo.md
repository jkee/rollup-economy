# 211120 — Crude Petroleum Extraction

*v5.1 Stage 1 research memo. Run `211120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.99 · L 0.36 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Sensor, subsurface, drilling, production, and maintenance data support AI that can improve high-cost operating and technical decisions.
**Weakness:** Labor is only a small share of receipts, while commodity prices and reservoir performance overwhelm the economic effect of task automation.

## Business-model lens
- Included: Independent U.S. operating businesses repeatedly exploring for, developing, producing, treating, measuring, and selling crude petroleum from wells or other deposits to external purchasers, including operators working wells for others where the operating business is transferable.
- Excluded: Passive royalty and mineral interests, non-operating financing vehicles, shell leaseholders, oilfield service contractors classified elsewhere, midstream and refining operations, gas-only producers, captive units, and businesses without transferable control.
- Customer and revenue model: Recurring commodity sales by barrel to refiners, marketers, gatherers, and traders, generally priced from WTI or other market benchmarks adjusted for quality, location, transportation, and contract terms; some operators also earn contract or fee revenue for operating wells.
- Deviation from default lens: none

## Executive view
Crude extraction has credible AI uses in subsurface interpretation, drilling, production optimization, maintenance, reporting, and back office, but its extraordinarily low compensation intensity limits aggregate labor economics. Commodity volatility, reserve decline, environmental liabilities, and property-level rather than firm-level transactions dominate investment risk.

## How AI changes the work
AI can predict well performance, optimize drilling and completions, detect production and equipment anomalies, prioritize maintenance, monitor emissions, and automate land, accounting, reporting, and procurement workflows. Hazardous field interventions, maintenance, emergency response, and accountable operating decisions remain.

## Value capture
Benchmark-linked crude pricing means internal savings are not automatically passed through to buyers, supporting initial retention. Service and acreage competition, purchaser differentials, royalties, taxes, and sustaining capital erode the benefit over time.

## Firm availability
The large establishment base and frozen 708 firms suggest many independents, but operating status, oil versus gas mix, passive interests, normalized cycle EBITDA, reserves, hedges, and plugging liabilities must be verified. The high sector-margin bridge is fragile.

## Demand durability
Near-term U.S. production remains near records, while EIA's longer-run cases point to modest decline around the five-year horizon under lower prices. Mature LMM assets may decline faster than national totals, yet nearly every remaining barrel still needs an accountable operator.

## Risks and uncertainty
Key risks are oil-price shocks, reserve and decline-curve error, dry holes, environmental and plugging liabilities, spills and safety incidents, regulation, mineral and working-interest complexity, customer and transport constraints, cyber-physical failures, capital intensity, and asset-sale versus company-sale mismatch.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0618 | — | OBSERVED | — |
| n | — | 708 | — | ESTIMATE | — |
| a | 0.17 | 0.28 | 0.4 | PROXY | S1, S3, S4 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S3, S4, S5 |
| e | 0.36 | 0.56 | 0.72 | ESTIMATE | S2, S6 |
| s5 | 0.18 | 0.34 | 0.5 | PROXY | S7, S8 |
| q | 0.42 | 0.61 | 0.78 | PROXY | S6, S9 |
| d5 | 0.86 | 0.97 | 1.1 | PROXY | S3, S10 |
| o | 0.992 | 0.999 | 1 | ESTIMATE | S2, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.15 | 0.36 | 0.67 | ESTIMATE |
| F | 6.19 | 7.90 | 8.92 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | PROXY |
| D | 8.53 | 9.69 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS combines crude petroleum and natural gas extraction and includes employers of all sizes.
- a: Technology evidence shows operational efficiency and capability, not a measured share of labor displaced.
- rho: Production uplift and reduced drilling time are not all labor substitution.
- rho: Shale, conventional mature fields, offshore, Alaska, and enhanced-recovery assets have different data and implementation economics.
- e: Establishments are not firms, and one producer can operate many establishments or properties.
- e: The 43.21% sector margin bridge is highly sensitive to commodity prices, hedges, depletion conventions, and development spending and may misclassify firms.
- s5: EIA deal value is not a firm-count transfer rate and is dominated by large transactions.
- s5: The SBA statistic is cross-industry and does not measure completed sales.
- q: Public producers have scale, marketing, and transport options unlike many LMM firms.
- q: Commodity price exposure can swamp automation savings even when the saving itself is retained.
- d5: AEO projections are scenarios, not forecasts, and policy and price assumptions can change materially.
- d5: Industry output can be sustained by large producers while LMM mature-field volumes decline.
- o: Production may shift to larger or foreign operators without eliminating the operator requirement.
- o: Contract operating can change who performs field work but not the need for an accountable producer.

## Sources
- **S1** — [Oil and Gas Extraction - May 2023 OEWS](https://www.bls.gov/oes/2023/may/naics4_211100.htm) (accessed 2026-07-23): Provides combined 211100 employment and wage shares across management, business, engineering, science, extraction, maintenance, production, office, and logistics occupations.
- **S2** — [211120: Crude Petroleum Extraction - Census Bureau Profile](https://data.census.gov/profile/211120_-_Crude_petroleum_extraction?codeset=naics~211120&g=010XX00US) (accessed 2026-07-23): Defines the industry, including own-account and contract operation of oil wells, and reports 3,863 employer establishments in 2023 CBP.
- **S3** — [Improved Efficiency Is Enabling Record U.S. Crude Oil Production from Fewer Rigs](https://www.eia.gov/TODAYINENERGY/detail.php?id=64124) (accessed 2026-07-23): Reports fewer rigs alongside record Lower 48 output and industry use of AI, electronic fracturing, and automated drilling to improve productivity and reduce downtime.
- **S4** — [Using Artificial Intelligence in Fossil Energy R&D](https://www.energy.gov/hgeo/articles/using-artificial-intelligence-fossil-energy-rd) (accessed 2026-07-23): Describes AI models using subsurface and operational data to predict well performance and optimize stimulation and production.
- **S5** — [Oil and Gas Extraction Hazards](https://www.osha.gov/oil-and-gas-extraction/hazards) (accessed 2026-07-23): Documents physical and safety-critical field hazards including vehicles, struck-by events, fires, falls, high-pressure equipment, electrical energy, and machinery.
- **S6** — [EOG Resources 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/821189/000082118926000054/eog-20251231.htm) (accessed 2026-07-23): Documents benchmark commodity-price exposure, purchaser concentration, drilling and completion efficiencies, production growth, and large revenue sensitivity to realized crude prices.
- **S7** — [M&A Activity in 2023 Furthers Consolidation of U.S. Crude Oil and Natural Gas Firms](https://www.eia.gov/TODAYINENERGY/detail.php?id=61603) (accessed 2026-07-23): Reports $234 billion of E&P merger and acquisition spending in 2023, the highest real value since 2012, while illustrating megadeal concentration.
- **S8** — [5 Challenges for Family-Owned Businesses](https://www.sba.gov/blog/5-challenges-family-owned-businesses) (accessed 2026-07-23): Reports that 47% of owners expecting retirement within five years do not have a successor, used only as a broad succession proxy.
- **S9** — [TXO Partners 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1559432/000119312526076813/txo-20251231.htm) (accessed 2026-07-23): Explains that WTI is a widely used U.S. oil benchmark and realized prices differ for location, quality, and other adjustments, while commodity prices affect economic production.
- **S10** — [Annual Energy Outlook 2026 Narrative - Oil and Natural Gas](https://www.eia.gov/outlooks/aeo/narrative/index.php) (accessed 2026-07-23): Projects crude production in a narrow band with prices below $70 in real 2025 dollars through 2030 and declining U.S. production through the mid-2030s in nearly all cases.
