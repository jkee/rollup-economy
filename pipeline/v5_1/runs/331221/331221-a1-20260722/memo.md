# 331221 — Rolled Steel Shape Manufacturing

*v5.1 Stage 1 research memo. Run `331221-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.01 · L 0.59 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Sensor-rich rolling processes offer implementable AI improvements in inspection, shape control, uptime, and scheduling.
**Weakness:** Transparent steel pricing and mature automation limit both remaining labor substitution and five-year retained benefit.

## Business-model lens
- Included: Independent U.S. manufacturers repeatedly rolling or drawing plate, sheet, strip, rod, bar, rebar, light structural sections, rails, and other non-wire shapes from purchased steel for external customers.
- Excluded: Captive rolling lines, integrated steelmakers rolling their own steel, wire drawing, downstream fabrication, service-center distribution, passive entities, and firms without transferable operations.
- Customer and revenue model: Repeat spot, program, and contract sales to construction, infrastructure, service-center, automotive, machinery, agricultural, energy, petrochemical, and general manufacturing customers, priced by ton, dimensions, grade, finish, processing, freight, and steel-market conditions.
- Deviation from default lens: none

## Executive view
Rolled-shape manufacturers have credible AI opportunities in surface inspection, dimensional control, roll and bearing maintenance, process settings, scheduling, quality records, and commercial workflows. Mature industrial controls and transparent steel-product markets limit incremental labor opportunity and long-term benefit retention.

## How AI changes the work
Models can classify surface defects, correct shape, predict roll wear, optimize furnace and rolling parameters, sequence orders, and automate documentation. Physical handling, roll changes, maintenance, safety, metallurgy, and responsible quality release remain.

## Value capture
Better yield, tolerances, uptime, and specialty products preserve some value, while short order cycles, bids, input-cost visibility, imports, and price-per-ton comparisons pass benefits through.

## Firm availability
Independent niche rerollers can fit the lens, but many establishments are subsidiaries, captive, outside the LMM band, or too capital- and liability-intensive. The machinery-margin bridge makes the 82-firm estimate uncertain through a steel cycle.

## Demand durability
Infrastructure, industrial construction, energy, manufacturing, and data centers support physical demand, with cyclical downside from housing, rates, imports, and project delays. Remaining domestic volume still requires an accountable mill.

## Risks and uncertainty
Important risks include model error at line speed, legacy integration, cyber-physical security, worker acceptance, raw-material and energy volatility, imports, tariffs, construction cycles, customer concentration, environmental liabilities, and target-size misclassification.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1267 | — | OBSERVED | — |
| n | — | 82 | — | ESTIMATE | — |
| a | 0.13 | 0.22 | 0.32 | PROXY | S1, S2, S3, S4 |
| rho | 0.35 | 0.53 | 0.69 | ESTIMATE | S2, S3, S4 |
| e | 0.5 | 0.7 | 0.85 | ESTIMATE | S5, S7 |
| s5 | 0.14 | 0.26 | 0.41 | PROXY | S9 |
| q | 0.27 | 0.45 | 0.64 | PROXY | S7 |
| d5 | 0.89 | 1.08 | 1.28 | PROXY | S6, S7, S8 |
| o | 0.98 | 0.995 | 1 | ESTIMATE | S2, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.23 | 0.59 | 1.12 | ESTIMATE |
| F | 3.07 | 4.45 | 5.45 | ESTIMATE |
| C | 5.40 | 9.00 | 10.00 | PROXY |
| D | 8.72 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS combines pipe, tube, wire, and rolled-shape manufacturing.
- a: The technology evidence includes non-U.S. and integrated mills and does not measure adoption among LMM rerollers.
- rho: Automatic control can improve quality without proportionate labor substitution.
- rho: Small specialty rerollers and high-volume flat-product operations have different data and capital readiness.
- e: Census reports 244 establishments, not firms or LMM candidates.
- e: The frozen n uses a Machinery margin rather than observed reroller economics, making band assignment uncertain.
- s5: The source is not steel-specific and does not measure completed transfers.
- s5: Plant or product-line sales may not qualify as control transfers of eligible firms.
- q: Plate, strip, rebar, merchant bar, rail, and specialty sections have different commercial dynamics.
- q: CMC also melts steel and fabricates rebar, extending beyond the exact purchased-steel lens.
- d5: BLS output covers all 331200 products rather than 331221 and is real value, not physical tons.
- d5: Public infrastructure funding timing does not map one-for-one to rolled-shape shipments.
- o: Imports can replace domestic operators without making software the supplier.
- o: Operator requirement does not imply unchanged labor intensity.

## Sources
- **S1** — [Steel Product Manufacturing from Purchased Steel - May 2023 OEWS](https://www.bls.gov/oes/2023/may/naics4_331200.htm) (accessed 2026-07-23): Provides occupational employment structure for broader purchased-steel manufacturing across plant, maintenance, technical, commercial, office, and management roles.
- **S2** — [Hitachi Develops AI Real-Time Control Technology for Cold Rolling Plants](https://www.hitachi.com/en/press/articles/2017/10/1031c/) (accessed 2026-07-23): Describes deep-learning control based on operator records and steel shape patterns to automate shape correction and reduce operator burden.
- **S3** — [Usage of Real Time Machine Vision in Rolling Mill](https://www.mdpi.com/2071-1050/13/7/3851) (accessed 2026-07-23): Reports real-operating-condition machine-vision work for automated billet inspection and rolling-mill quality control.
- **S4** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-23): Documents AI uses and adoption barriers in predictive maintenance, quality, process control, scheduling, and legacy manufacturing systems.
- **S5** — [331221: Rolled Steel Shape Manufacturing - Census Bureau Profile](https://data.census.gov/profile/331221_-_Rolled_steel_shape_manufacturing?codeset=naics~331221&g=010XX00US) (accessed 2026-07-23): Defines rolling and drawing non-wire shapes from purchased steel and reports 244 employer establishments in 2023.
- **S6** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-23): Projects broader 331200 real output from $25.6 billion in 2024 to $30.9 billion in 2034, a 1.9% annual rate.
- **S7** — [Commercial Metals Company 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/22444/000002244425000138/cmc-20250831.htm) (accessed 2026-07-23): Describes rebar and merchant-bar markets, short order cycles, competitive bids, price-per-ton economics, construction end uses, raw-material volatility, and product flexibility.
- **S8** — [Commercial Metals Company Q2 FY2026 Supplemental Slides](https://www.sec.gov/Archives/edgar/data/22444/000002244426000025/q22026-supplementalslide.htm) (accessed 2026-07-23): Identifies infrastructure, reshoring, energy, housing, and data centers as demand supports and states 60% of IIJA funding remained to be spent at December 2025.
- **S9** — [5 Challenges for Family-Owned Businesses](https://www.sba.gov/blog/5-challenges-family-owned-businesses) (accessed 2026-07-23): Reports that 47% of owners expecting to retire within five years do not have a successor.
