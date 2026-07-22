# 327992 — Ground or Treated Mineral and Earth Manufacturing

*v5.1 Stage 1 research memo. Run `327992-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.97 · L 0.49 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring specification-controlled B2B relationships support repeat workflows and continuing operator responsibility.
**Weakness:** Low labor intensity and a physical production/logistics workforce cap the value available from AI substitution.

## Business-model lens
- Included: US lower-middle-market firms that repeatedly calcine, dead-burn, grind, blend, activate, or otherwise process clays, barite, ceramic and refractory minerals, fillers, absorbents, and other nonmetallic minerals for external industrial customers.
- Excluded: Mine-site beneficiation classified in mining, captive processing plants, vertically integrated internal units without external recurring customers, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat B2B sales of specification-controlled bulk or packaged mineral products under purchase orders, supply agreements, and customer formulas, with pricing influenced by grade, processing, energy, packaging, freight, and commodity competition.
- Deviation from default lens: none

## Executive view
Ground and treated minerals are a repeat B2B supply business with a physical, quality-controlled plant core. AI can improve the information layer around orders, production, maintenance, laboratories, logistics, and customer documentation, but the low labor share and large physical occupation mix limit the gross opportunity.

## How AI changes the work
Likely uses include order capture, specification matching, production and dispatch scheduling, purchasing, maintenance triage, quality-document drafting, exception detection, customer service, and commercial analytics. Process changes should remain within validated controls because chemistry, particle size, contamination, dust, heat, and equipment safety create costly failure modes.

## Value capture
Savings can be retained between price negotiations because customer formulas focus on grade, commodity inputs, energy, and freight rather than the supplier's labor hours. Over time, sophisticated buyers, substitutes, and rebids should share or compete away a meaningful portion.

## Firm availability
The code contains relatively few target-band firms. Independent processors often fit the repeat-revenue lens, but plant permits, environmental liabilities, feedstock access, customer qualification, and specialized assets make transfers slower and more diligence-intensive than generic manufacturing deals.

## Demand durability
Demand is diversified across clay, barite, fillers, absorbents, ceramics, construction, drilling, and other industrial uses. Recent physical indicators are stable to positive, though individual minerals remain exposed to end-market cycles, imports, and reformulation.

## Risks and uncertainty
The evidence is broad-sector and commodity-level rather than six-digit, firm-level operating data. A highly automated plant may have little remaining labor to remove, while a legacy plant may lack the data and controls needed to implement AI safely. Energy, freight, feedstock, environmental, and customer concentration risks can dominate labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1182 | — | OBSERVED | — |
| n | — | 63 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.29 | PROXY | S1, S2, S3 |
| rho | 0.35 | 0.52 | 0.7 | ESTIMATE | S2, S3 |
| e | 0.55 | 0.72 | 0.86 | ESTIMATE | S4 |
| s5 | 0.09 | 0.16 | 0.25 | PROXY | S5, S6 |
| q | 0.4 | 0.55 | 0.7 | PROXY | S7 |
| d5 | 0.92 | 1.05 | 1.18 | PROXY | S8, S9 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.20 | 0.49 | 0.96 | ESTIMATE |
| F | 2.28 | 3.40 | 4.31 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | PROXY |
| D | 8.65 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The OEWS occupation mix is for NAICS 327000, not 327992.
- a: The estimate excludes process automation already embedded in plant controls and targets only not-yet-automated tasks.
- a: The injected compensation ratio uses 2024 wages over 2022 receipts and is harmonized to the IPS basis as stated in the assignment.
- rho: This is bounded implementation judgment rather than an observed adoption rate.
- rho: Plants with modern historians, sensors, and ERP systems may realize more than small legacy facilities.
- e: Census reports 275 employer establishments, not firms and not the target EBITDA band.
- e: The injected 63-firm count is a margin-bridged ESTIMATE rather than observed EBITDA-band data.
- s5: Broker marketplace data skew smaller than the lens.
- s5: Economy-wide owner age does not reveal succession intentions in this industry.
- s5: Strategic purchases of plants or mineral reserves may not preserve a transferable operating firm.
- q: The cited pricing disclosure concerns iron ore rather than processed clays or industrial fillers.
- q: Contract structure varies sharply by mineral, grade, customer concentration, and freight radius.
- q: Implementation difficulty and volume changes are excluded from this primitive.
- d5: Commodity mining statistics do not isolate value-added treatment performed by firms in this code.
- d5: Different minerals face unrelated end-market cycles and substitution paths.
- d5: Trade policy and freight economics can relocate processing without changing end demand.
- o: Operator-required does not mean labor-intensive; highly automated plants still count as accountable operators.
- o: Some customers could backward-integrate processing where volumes justify capital investment.

## Sources
- **S1** — [BLS May 2023 OEWS: Nonmetallic Mineral Product Manufacturing](https://www.bls.gov/oes/2023/may/naics3_327000.htm) (accessed 2026-07-23): Reports occupation employment shares for broader NAICS 327, including production 33.97%, transportation and material moving 28.00%, office and administrative support 8.04%, and installation, maintenance and repair 6.75%.
- **S2** — [O*NET OnLine: Crushing, Grinding, and Polishing Machine Operators](https://www.onetonline.org/link/summary/51-9021.00) (accessed 2026-07-23): Documents equipment observation, adjustment, maintenance, material movement, measurement, recordkeeping, inspection, sampling, testing, and jam-clearing tasks central to mineral processing.
- **S3** — [Anthropic Economic Index report: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report) (accessed 2026-07-23): Reports that physical occupations such as transportation/material moving and construction are underrepresented in Claude usage and notes that the survey is not workforce-representative.
- **S4** — [Census Bureau Profile: NAICS 327992](https://data.census.gov/profile/327992_-_Ground_or_Treated_Mineral_and_Earth_Manufacturing?codeset=naics~327992&g=010XX00US) (accessed 2026-07-23): Defines the industry as processing beyond beneficiation clays, ceramic and refractory minerals, barite, and miscellaneous nonmetallic minerals, and reports 275 employer establishments in 2023.
- **S5** — [Manufacturing Business Valuation Multiples & Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/manufacturing/) (accessed 2026-07-23): Reports 2,303 sold manufacturing listings analyzed for 2021-2025 and median 2025 sale price of $650,000, establishing a proxy for manufacturing control-transfer liquidity.
- **S6** — [Annual Business Survey: Characteristics of Business Owners, 2022 Tables](https://www.census.gov/data/tables/2022/econ/abs/2022-abs-characteristics-of-owners.html) (accessed 2026-07-23): Provides economy-wide employer-business owner characteristics including an Age of Owner table, used as broad succession context only.
- **S7** — [Cleveland-Cliffs 2018 quarterly filing: customer supply agreements](https://www.sec.gov/Archives/edgar/data/0000764065/000076406518000088/clf-201833110xq.htm) (accessed 2026-07-23): Describes mineral supply agreements with base prices and adjustments tied to market prices, freight, industrial commodities, fuel, and steel producer-price indexes.
- **S8** — [USGS Mineral Commodity Summaries 2026: Clays](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-clays.pdf) (accessed 2026-07-23): Reports 2025 US apparent clay consumption of 23.0 million tons versus 22.8 million in 2024, increased domestic tonnage sold or used, and substitutes across filler, absorbent, and construction uses.
- **S9** — [USGS Mineral Commodity Summaries 2026: Barite chapter](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf) (accessed 2026-07-23): Reports that estimated barite sales increased in 2025 despite lower domestic and global rig counts, and that few large-scale substitutes exist in drilling fluids.
