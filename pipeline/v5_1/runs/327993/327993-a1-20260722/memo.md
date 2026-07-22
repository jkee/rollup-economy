# 327993 — Mineral Wool Manufacturing

*v5.1 Stage 1 research memo. Run `327993-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.86 · L 0.86 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Energy, fire, and acoustic requirements sustain repeat demand for certified physical insulation products.
**Weakness:** A capital-intensive, already-automated production process and thin transfer population limit the realizable opportunity.

## Business-model lens
- Included: US lower-middle-market firms that repeatedly manufacture mineral wool and fiberglass insulation from rock, slag, glass, or combinations thereof for external residential, commercial, industrial, acoustic, fire-protection, and equipment customers.
- Excluded: Insulation installers, distributors without manufacturing, captive internal plants without external recurring customers, metallic wool, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat product sales through distributors, lumberyards, home centers, installers, contractors, retailers, and direct industrial channels, with revenue driven by volume, product mix, service, location, quality, building specifications, and negotiated selling prices.
- Deviation from default lens: none

## Executive view
Mineral wool is a recurring, specification-driven building-material business with durable physical operator need but a continuous, already-automated production core. AI is most credible around planning, maintenance, quality, orders, service, and administrative work; the limited target-firm population and capital intensity constrain transfer availability.

## How AI changes the work
AI can assist anomaly detection, visual quality inspection, maintenance prioritization, furnace and line decision support, demand forecasting, scheduling, order handling, product selection, technical-document drafting, and customer service. Autonomous process changes face high hurdles because downtime, fire, heat, emissions, fiber quality, and certification failures are costly.

## Value capture
Unit-based product pricing lets producers retain internal savings initially, as buyers do not receive an hourly labor bill. Over time, strong price competition, distributors, large retail accounts, substitutes, and capacity expansion should share much of the benefit.

## Firm availability
Independent operators generally fit the recurring external-customer lens, but relatively few target-band firms exist. Specialized plants, environmental and energy exposure, certifications, and concentrated channels favor strategic buyers and make qualifying transfers episodic.

## Demand durability
Housing weakness is a real near-term risk, while repair, renovation, nonresidential construction, efficiency codes, fire safety, acoustics, and existing-building retrofits support a positive five-year base. Material substitution and code-adoption variability justify a wide range.

## Risks and uncertainty
Evidence is dominated by large public producers and broad occupation data. Smaller firms may have either more manual opportunity or less digital infrastructure. Energy prices, furnace downtime, emissions rules, product liability, capacity cycles, housing starts, and channel concentration can dominate AI savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2042 | — | OBSERVED | — |
| n | — | 45 | — | ESTIMATE | — |
| a | 0.13 | 0.21 | 0.3 | PROXY | S1, S2, S3 |
| rho | 0.32 | 0.5 | 0.68 | ESTIMATE | S3, S4 |
| e | 0.5 | 0.68 | 0.82 | ESTIMATE | S1, S4 |
| s5 | 0.07 | 0.13 | 0.22 | PROXY | S5, S6 |
| q | 0.35 | 0.5 | 0.66 | PROXY | S4 |
| d5 | 0.9 | 1.07 | 1.24 | PROXY | S4, S7, S8, S9 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.34 | 0.86 | 1.67 | ESTIMATE |
| F | 1.52 | 2.58 | 3.56 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | PROXY |
| D | 8.46 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Exact-industry staffing evidence is more than two decades old.
- a: Broader NAICS 327 includes many processes unlike mineral wool.
- a: The injected compensation ratio uses 2024 wages over 2022 receipts and is harmonized to the IPS basis as stated in the assignment.
- rho: No source measures five-year implementation for the target firm population.
- rho: Large producers' digital capabilities may not represent lower-middle-market operators.
- e: Public company evidence demonstrates channel structure but not the ownership mix of the full LMM population.
- e: The injected 45-firm count is a margin-bridged ESTIMATE rather than a directly observed EBITDA-band census.
- s5: Small-business marketplace deals are not representative of target-size mineral-wool plants.
- s5: Owner age does not measure sale intent or plant transferability.
- s5: Asset sales and internal reorganizations must be excluded from qualifying transfers.
- q: Owens Corning is much larger than the lens and has products outside NAICS 327993.
- q: Public segment results do not identify AI-derived savings or contractual pass-through.
- q: Volume and implementation effects are excluded from this primitive.
- d5: Company data are global or multi-product and not a US industry census.
- d5: Model-code efficiency gains do not guarantee state adoption or mineral-wool share.
- d5: Foam, cellulose, wood fiber, and other insulation materials are substitutes.
- o: Operator-required does not mean current staffing is durable; a highly automated plant still counts as the operator.
- o: Certification and liability practices could change with new materials and modular systems.

## Sources
- **S1** — [US Census Bureau NAICS definition: 327993 Mineral Wool Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-23): Defines the industry as manufacturing mineral wool and fiberglass insulation products from rock, slag, glass, or combinations thereof.
- **S2** — [US Census Bureau Economic Census: Mineral Wool Manufacturing, 2002](https://www2.census.gov/library/publications/economic-census/2002/manufacturing-reports/industry-series/ec0231i327993t.pdf) (accessed 2026-07-23): Reports 19,318 employees and 15,788 production workers for NAICS 327993 in 2002, used only as a historical exact-industry staffing proxy.
- **S3** — [O*NET OnLine: Furnace, Kiln, Oven, Drier, and Kettle Operators](https://www.onetonline.org/link/details/51-9051.00) (accessed 2026-07-23): Describes the physical and monitoring occupation that operates or tends industrial heating equipment, including glass annealing and material processing.
- **S4** — [Owens Corning 2025 Annual Report on Form 10-K](https://www.sec.gov/Archives/edgar/data/1370946/000137094626000067/oc-20251231.htm) (accessed 2026-07-23): Documents insulation channels and demand drivers; reports 2025 insulation sales down 6%, volume down about 5%, higher selling prices of $27 million, lower manufacturing costs of $30 million, and competition on price, service, location, quality, and design.
- **S5** — [Manufacturing Business Valuation Multiples & Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/manufacturing/) (accessed 2026-07-23): Reports 2,303 sold manufacturing listings analyzed for 2021-2025, providing a broad proxy for manufacturing transfer liquidity.
- **S6** — [Annual Business Survey: Characteristics of Business Owners, 2022 Tables](https://www.census.gov/data/tables/2022/econ/abs/2022-abs-characteristics-of-owners.html) (accessed 2026-07-23): Provides economy-wide employer-business owner characteristics including the Age of Owner table, used only as broad succession context.
- **S7** — [ROCKWOOL Annual Report Highlights 2025](https://www.rockwool.com/group/about-us/investors/financial-reports/annual-report-highlights-2025/) (accessed 2026-07-23): Reports 1% local-currency revenue growth in 2025, a slightly positive 2026 outlook, and solid long-term US growth potential amid low construction activity in other regions.
- **S8** — [US Department of Energy: Model Energy Code Determinations](https://www.energycodes.gov/determinations) (accessed 2026-07-23): Reports DOE's determination that the 2024 IECC improves residential efficiency, estimating 7.8% site-energy, 6.8% source-energy, and 6.6% energy-cost savings.
- **S9** — [US Department of Energy: Opaque Envelope](https://www.energy.gov/cmei/buildings/opaque-envelope) (accessed 2026-07-23): States that opaque envelopes affect 28% of building energy use and that nearly 93% of residential and 60% of commercial buildings existing today will still exist in 2050, supporting retrofit relevance.
