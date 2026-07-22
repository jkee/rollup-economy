# 322110 — Pulp Mills

*v5.1 Stage 1 research memo. Run `322110-a1-20260723`, model `claude-sonnet-5`, 2026-07-23, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.03 · L 0.08 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High-value maintenance, process, energy, and compliance decisions provide a focused AI-assistance opportunity.
**Weakness:** Very few LMM pulp mills are independent recurring outsourced-service providers, and their economics are dominated by assets and commodities rather than labor.

## Business-model lens
- Included: US lower-middle-market stand-alone pulp producers only where paper, packaging, tissue, specialty-fiber, or other industrial customers repeatedly outsource fiber production under ongoing supply or toll-processing relationships.
- Excluded: Integrated captive pulp operations, spot-only commodity sellers, one-off product transactions, non-operating assets, shells, financing vehicles, and firms outside the EBITDA band.
- Customer and revenue model: Qualifying mills earn contract, tolling, or repeated per-ton supply revenue from industrial customers; pricing may be fixed, indexed, cost-plus, or market-linked.
- Deviation from default lens: Pulp is a commodity intermediate rather than a conventional service, and many mills are captive or much larger than the target band. The lens is narrowed to independent mills with recurring outsourced-production relationships.

## Executive view
Pulp mills have a narrow software-labor opportunity and an even narrower fit with the recurring outsourced-service lens. The qualifying universe is likely tiny, while physical assets, environmental obligations, and commodity pricing dominate economics.

## How AI changes the work
Practical uses include predictive-maintenance triage, process and energy advisory, purchasing, lab-data interpretation, work instructions, safety and environmental documentation, and shift knowledge. Continuous chemical processing, utilities, maintenance, and compliance still require skilled accountable operators.

## Value capture
Commodity and indexed pricing lets customers and competitors absorb much of any productivity gain. Specialty grades, constrained fiber access, qualification barriers, and reliable tolling relationships can preserve more, but input-price volatility makes attribution difficult.

## Firm availability
The frozen dataset estimates only five LMM firms, and many facilities may be captive, integrated, strategically owned, or economically unlike the margin bridge. Environmental history, permits, site infrastructure, and fiber supply determine whether a control transfer is feasible rather than a closure or asset liquidation.

## Demand durability
Printing and writing decline weighs on some grades, while packaging, tissue, recycled, absorbent, and specialty-fiber uses provide offsets. Surviving demand remains almost entirely operator-required because pulp is a physical, regulated intermediate.

## Risks and uncertainty
The main risks are near-zero eligibility, a discrete five-firm pool, commodity cycles, global overcapacity, energy and chemical costs, fiber access, environmental liabilities, outages, and irreversible closure. AI savings are small relative to capital and raw-material economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0549 | — | OBSERVED | — |
| n | — | 5 | — | ESTIMATE | — |
| a | 0.07 | 0.13 | 0.22 | PROXY | S1, S2, S3 |
| rho | 0.25 | 0.45 | 0.65 | ESTIMATE | S2, S3, S4 |
| e | 0.01 | 0.08 | 0.2 | ESTIMATE | S3, S4 |
| s5 | 0.05 | 0.13 | 0.25 | PROXY | S5, S6 |
| q | 0.18 | 0.35 | 0.58 | ESTIMATE | S3, S7 |
| d5 | 0.68 | 0.9 | 1.12 | PROXY | S3, S7 |
| o | 0.94 | 0.99 | 1 | PROXY | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.04 | 0.13 | 0.31 | ESTIMATE |
| F | 0.00 | 0.08 | 0.36 | ESTIMATE |
| C | 3.60 | 7.00 | 10.00 | ESTIMATE |
| D | 6.39 | 8.91 | 10.00 | PROXY |

## Caveats
- a: OEWS evidence covers NAICS 3221 rather than 322110 and does not measure task exposure directly.
- a: The frozen labor ratio uses 2024 wages over 2022 receipts and a cross-industry harmonization divisor.
- rho: No representative five-year adoption study specific to US pulp mills was found.
- rho: Autonomous process control is treated conservatively because safety and emissions accountability remain with the operator.
- e: The dataset estimates only five LMM firms using a sector margin bridge; pulp-mill capital intensity can make that bridge materially misleading.
- e: Recurring market-pulp sales are not automatically recurring outsourced services.
- s5: General small-business evidence is especially weak for a capital-intensive process industry.
- s5: The five-firm dataset estimate creates high discrete-event uncertainty.
- q: No public contract sample for LMM independent mills was found.
- q: Energy, chemicals, fiber, freight, and currency can swamp an AI-related cost change in observed pricing.
- d5: Industrial production is a broad output index, not constant-quality demand for the qualifying service basket.
- d5: Grade conversions can make aggregate tonnage a poor proxy for economic demand.
- o: The estimate concerns accountable operator need, not preservation of current staffing.
- o: Integrated buyers and consolidation can replace the current firm type without eliminating physical mill operation.

## Sources
- **S1** — [Pulp, Paper, and Paperboard Mills - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_322100.htm) (accessed 2026-07-23): Reports the broader mill occupation mix, including other production occupations at 42.60% of employment, supporting the physical-work exposure proxy.
- **S2** — [Kraft Pulp Mills: New Source Performance Standards](https://www.epa.gov/stationary-sources-air-pollution/kraft-pulp-mills-new-source-performance-standards-nsps-40-cfr-60) (accessed 2026-07-23): Describes chemical kraft conversion under high pressure and numeric emissions limits covering recovery furnaces, lime kilns, and smelt dissolving tanks.
- **S3** — [Subpart AA - Pulp and Paper Manufacturing](https://www.epa.gov/ghgreporting/subpart-aa-pulp-and-paper-manufacturing) (accessed 2026-07-23): Defines stand-alone market-pulp, integrated, purchased-pulp, and recycled-fiber facilities and documents greenhouse-gas reporting obligations.
- **S4** — [GHGRP Pulp and Paper Sector Profile](https://www.epa.gov/ghgreporting/ghgrp-pulp-and-paper-sector-profile) (accessed 2026-07-23): Documents facility emissions profiles, monitoring methods, reporting coverage, and trends back to 2011, supporting compliance and operational-accountability constraints.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Provides a cross-industry five-year employer-business transfer-intention proxy.
- **S6** — [BizBuySell Insight Report Data Tables](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-23): Provides broad small-manufacturing transaction evidence, useful only as a liquidity proxy given the much smaller and more capital-intensive target population.
- **S7** — [Industrial Production: Industry Subtotals and Individual Series](https://www.federalreserve.gov/releases/g17/Current/table1b_sup.htm) (accessed 2026-07-23): Reports a distinct NAICS 32211 pulp-mill industrial-production series within current G.17 data, anchoring broad physical-output direction and volatility.
