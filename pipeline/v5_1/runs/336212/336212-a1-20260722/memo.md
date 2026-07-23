# 336212 — Truck Trailer Manufacturing

*v5.1 Stage 1 research memo. Run `336212-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.60 · L 0.87 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A depressed replacement cycle plus durable truck-freight use creates recovery upside around a necessary physical asset.
**Weakness:** Production labor is overwhelmingly physical and demand is exceptionally cyclical at the current measurement date.

## Business-model lens
- Included: US lower-middle-market firms repeatedly manufacturing truck trailers, semitrailers, truck-trailer chassis, cargo-container chassis, detachable trailer bodies, and detachable chassis for external fleets, dealers, leasing companies, and logistics customers.
- Excluded: Utility and light-truck trailers, travel trailers, captive plants, repair and rental businesses, distributors without manufacturing, and firms outside the EBITDA band.
- Customer and revenue model: Product revenue from repeat fleet orders and dealer sales of standard or configured dry van, refrigerated, flatbed, dump, tank, specialty, and chassis equipment, with options and parts as ancillary revenue.
- Deviation from default lens: none

## Executive view
Truck trailer manufacturing offers repeatable configuration, quoting, planning, and documentation workflows, but most labor remains physical. The current production trough creates both recovery potential and unusually high demand uncertainty.

## How AI changes the work
AI can assist configuration checks, quotation, engineering-document retrieval, BOM changes, procurement, schedules, inspection records, warranty triage, and dealer support. Welding, fabrication, assembly, paint, axle and brake installation, and final inspection remain embodied.

## Value capture
Specialty designs and lead-time service allow some retention; standardized fleet products face disciplined bids and rapid competitive pass-through. Operational gains may appear more in throughput and mix than list price.

## Firm availability
Independent regional and specialty producers make LMM eligibility plausible, but ownership concentration, under-scale firms, and the sharp cycle must be resolved firm by firm. Transferability depends on management depth, customer concentration, engineering records, and product liability.

## Demand durability
Trailers remain essential to truck freight, and long-run freight activity grows in official forecasts. Near-term output has fallen sharply, so recovery timing, fleet utilization, interest rates, and replacement deferrals dominate the five-year ratio.

## Risks and uncertainty
Risks include an extended freight recession, fleet overcapacity, customer concentration, steel and component volatility, product-liability and underride compliance, working capital, dealer inventory, skilled labor, imports, and misreading a cycle trough as structural value.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1601 | — | OBSERVED | — |
| n | — | 199 | — | ESTIMATE | — |
| a | 0.15 | 0.26 | 0.38 | PROXY | S2 |
| rho | 0.33 | 0.52 | 0.69 | ESTIMATE | S0, S3 |
| e | 0.44 | 0.64 | 0.8 | ESTIMATE | S0 |
| s5 | 0.12 | 0.24 | 0.37 | PROXY | S7 |
| q | 0.37 | 0.55 | 0.72 | ESTIMATE | S4 |
| d5 | 0.79 | 1.16 | 1.48 | PROXY | S5, S6 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S0, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.32 | 0.87 | 1.68 | ESTIMATE |
| F | 3.93 | 5.55 | 6.58 | ESTIMATE |
| C | 7.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.58 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation mix is four-digit, not 336212.
- a: Exposure is a task mapping rather than observed labor removal.
- rho: No trailer-industry study directly observes five-year implementation.
- rho: Safety requirements preserve accountable engineering and inspection.
- e: The provided n is margin-bridged rather than observed.
- e: Enterprise ownership cannot be inferred from establishment coding alone.
- s5: Owner age is not a direct deal-flow measure.
- s5: Private small-company transactions are incompletely reported.
- q: PPI observes industry selling prices, not AI-benefit retention.
- q: Retention differs greatly between commodity dry vans and specialized tank or lowboy trailers.
- d5: Industrial-production revisions can be large.
- d5: Freight growth does not map one-for-one to trailer purchases.
- d5: A depressed starting point makes the ratio especially cycle-sensitive.
- o: Consolidation and imports can displace lens firms even if the operator requirement persists.

## Sources
- **S0** — [2022 NAICS definition: 336212 Truck Trailer Manufacturing](https://www.census.gov/naics/?details=33&input=33&year=2022) (accessed 2026-07-23): Defines truck trailers, chassis, cargo-container chassis, detachable bodies, and detachable chassis; excludes light and travel trailers.
- **S2** — [May 2023 OEWS: Motor Vehicle Body and Trailer Manufacturing](https://www.bls.gov/oes/2023/may/naics4_336200.htm) (accessed 2026-07-23): Broader occupation mix: production occupations 65.21% and assemblers/fabricators 31.75% of employment.
- **S3** — [NHTSA final rule on truck-trailer underride protection](https://www.nhtsa.gov/press-releases/underride-protection-truck-trailers) (accessed 2026-07-23): Final rule updates FMVSS 223 and 224 and requires qualifying trailers and semitrailers to have stronger rear impact guards.
- **S4** — [Producer Price Index: Truck Trailer Manufacturing](https://fred.stlouisfed.org/series/PCU336212336212/) (accessed 2026-07-23): BLS monthly industry selling-price index, including 408.605 in May 2026.
- **S5** — [Industrial Production: Truck Trailer Manufacturing, annual](https://fred.stlouisfed.org/series/IPG336212A) (accessed 2026-07-23): Real-output index fell from 98.5466 in 2022 to 65.5501 in 2024 and 55.6499 in 2025.
- **S6** — [Freight Activity in the U.S. Expected to Grow Fifty Percent by 2050](https://www.bts.gov/newsroom/freight-activity-us-expected-grow-fifty-percent-2050) (accessed 2026-07-23): FAF5 projects freight tonnage growing 50% from 2020 to 2050 and says trucks carry 65% of US freight tonnage.
- **S7** — [ABS Characteristics of Business Owners: 2024 Tables](https://www.census.gov/data/tables/2024/econ/abs/2024-abs-characteristics-of-owners.html) (accessed 2026-07-23): Official Census Age of Owner tables for employer businesses, used only as a broad succession proxy.
- **S8** — [Industrial Production: Truck Trailer Manufacturing, monthly seasonally adjusted](https://fred.stlouisfed.org/series/IPG336212S) (accessed 2026-07-23): Current-cycle confirmation: seasonally adjusted output index was 54.8303 in May 2026.
