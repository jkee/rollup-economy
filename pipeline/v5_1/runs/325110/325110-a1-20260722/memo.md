# 325110 — Petrochemical Manufacturing

*v5.1 Stage 1 research memo. Run `325110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.10 · L 0.19 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Physical molecular conversion and pervasive downstream uses support durable operator-required demand.
**Weakness:** Industry concentration and capital intensity leave a tiny, poorly observed independent LMM contract-processing population.

## Business-model lens
- Included: Independent lower-middle-market petrochemical processors that repeatedly provide toll, contract, or customer-specific production of acyclic or aromatic hydrocarbons to external industrial customers.
- Excluded: Integrated oil-major and refinery complexes, captive units, world-scale commodity crackers without meaningful external contract-processing relationships, trading-only entities, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat B2B sales and contract-processing revenue under term supply agreements, formula or index-adjusted pricing, and customer specifications; customers are downstream chemical, resin, materials, and industrial manufacturers.
- Deviation from default lens: The code is dominated by highly concentrated, integrated commodity production whose economics are unlike outsourced LMM service supply. The lens is narrowed to independent toll, contract, and customer-specific processors so the recurring external-customer model is coherent.

## Executive view
Petrochemical manufacturing is a concentrated, capital- and feedstock-intensive industry with only a very small plausible LMM contract-processing niche. AI can improve indirect labor and plant decision support, but it does not alter the dominance of physical assets, compliance, and commodity economics.

## How AI changes the work
Useful applications include engineering search, maintenance triage, planning, procurement, laboratory and environmental documentation, incident analysis, contract administration, and customer service. Operators, technicians, engineers, and accountable managers remain necessary for continuous-process safety, field intervention, testing, emissions control, and product release.

## Value capture
Term and indexed contracts can pass feedstock costs while leaving conversion savings with the operator initially. Benchmark pricing, specification equivalence, buyer sophistication, and renewal competition erode retention, particularly for undifferentiated molecules.

## Firm availability
Four firms control 74.2% of shipments, and the injected LMM-band population is just five firms. A qualifying independent toll processor may be transferable, but specialized assets, permits, liabilities, and a narrow strategic-buyer set reduce control-transfer probability.

## Demand durability
Petrochemical molecules remain foundational inputs across many end markets, so operator-required quantity persists. The five-year path is cyclical and exposed to global capacity, imports, substitution, recycling, and small-firm share loss rather than software elimination.

## Risks and uncertainty
The screen is most vulnerable to finding no truly eligible firm. Environmental liabilities, catastrophic process risk, feedstock and customer concentration, unplanned outages, commodity spreads, carbon policy, global overcapacity, and enormous sustaining-capital needs can dominate achievable labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0605 | — | OBSERVED | — |
| n | — | 5 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.3 | PROXY | S1, S2 |
| rho | 0.28 | 0.45 | 0.61 | ESTIMATE | S3, S4 |
| e | 0.06 | 0.16 | 0.32 | ESTIMATE | S5, S6 |
| s5 | 0.08 | 0.16 | 0.27 | PROXY | S7 |
| q | 0.36 | 0.52 | 0.68 | PROXY | S8 |
| d5 | 0.94 | 1.04 | 1.15 | PROXY | S9 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.08 | 0.22 | 0.44 | ESTIMATE |
| F | 0.04 | 0.19 | 0.58 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | PROXY |
| D | 8.84 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is three-digit chemical manufacturing, not petrochemical manufacturing.
- a: Exposure mapping excludes already-automated distributed-control-system tasks.
- rho: No implementation study specific to LMM independent petrochemical processors was found.
- rho: The range excludes autonomous safety-critical process control.
- e: Concentration is shipment-weighted and does not directly identify the five modeled LMM firms.
- e: With only five firms, eligibility is discrete and the range corresponds to roughly zero to two firms.
- s5: The source is cross-industry and usually smaller than the LMM lens.
- s5: Owner intention is not a completed qualifying transfer rate.
- q: The issuer is a specialty chemical and biofuel manufacturer, not a representative petrochemical firm.
- q: No contract evidence directly measures AI savings or five-year benefit sharing.
- d5: The forecast is short-term and broader than six-digit eligible processors.
- d5: Output is used as a proxy for constant-price, constant-quality demand.
- o: Operator persistence is inferred from physical and regulatory requirements rather than observed directly.
- o: Integrated producers could displace independent operators even if aggregate molecule demand persists.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 325000](https://www.bls.gov/oes/2023/may/naics3_325000.htm) (accessed 2026-07-22): Chemical-manufacturing occupation employment and wage mix used to bound task exposure.
- **S2** — [Chemical Manufacturing: NAICS 325](https://www.bls.gov/iag/tgs/iag325.htm) (accessed 2026-07-22): Current production-occupation counts, workforce composition, and productivity context.
- **S3** — [2026 Roadmap on Artificial Intelligence and Machine Learning for Smart Manufacturing](https://www.nist.gov/publications/2026-roadmap-artificial-intelligence-and-machine-learning-smart-manufacturing) (accessed 2026-07-22): Industrial AI applications and barriers involving data, controls integration, reliability, explainability, and safety.
- **S4** — [Ethylene Manufacturing Process Units: National Emission Standards for Hazardous Air Pollutants](https://www.epa.gov/stationary-sources-air-pollution/heat-exchange-systems-and-waste-operations-ethylene-manufacturing) (accessed 2026-07-22): Recordkeeping, reporting, compliance, operation, and maintenance requirements for ethylene process units.
- **S5** — [Chemical Manufacturers Produce Everything from Medicine to Fertilizer](https://www.census.gov/library/stories/2026/03/chemical-manufacturing.html) (accessed 2026-07-22): 2022 petrochemical shipment concentration: four largest firms accounted for 74.2% of $77.6 billion.
- **S6** — [2022 NAICS: Chemical Manufacturing](https://www.census.gov/naics/?details=325&input=325&year=2022) (accessed 2026-07-22): Official classification context for acyclic and aromatic petrochemical manufacturing.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry U.S. employer-business five-year sale and transfer intentions.
- **S8** — [FutureFuel Corp. 2025 Annual Report](https://www.sec.gov/Archives/edgar/data/1337298/000143774926008411/ff20251231_10k.htm) (accessed 2026-07-22): Chemical term-contract market-price adjustment protections and residual conversion-cost exposure.
- **S9** — [Tables Accompanying the ACC Situation and Outlook, December 2025](https://www.americanchemistry.com/media/files/acc/chemistry-in-america/data-industry-statistics/landing-page-media/files/acc-year-end-situation-outlook-2025-tables) (accessed 2026-07-22): U.S. bulk petrochemical and organic chemical production-volume history and near-term forecast.
