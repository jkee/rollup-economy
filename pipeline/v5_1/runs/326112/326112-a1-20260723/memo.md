# 326112 — Plastics Packaging Film and Sheet (including Laminated) Manufacturing

*v5.1 Stage 1 research memo. Run `326112-a1-20260723`, model `claude-sonnet-5`, 2026-07-23, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.11 · L 0.53 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring specification-based film demand and rich process data create targeted opportunities in quality, yield, uptime, planning, and commercial workflows.
**Weakness:** Capital intensity, resin-linked pricing, and policy-driven material reduction can compress the transferable pool and pass operational savings to customers.

## Business-model lens
- Included: US lower-middle-market manufacturers that repeatedly supply flexible plastic packaging film or packaging sheet, including laminated plastic-to-plastic structures, to external converters, packagers, and industrial or consumer-goods customers.
- Excluded: Captive internal film production, pure resin or film distribution, finished bag and pouch conversion, nonpackaging unlaminated film and sheet, paper-foil-plastic combinations classified elsewhere, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring rolls or sheet sold by weight, area, specification, or supply program, with pricing often influenced by resin indices and differentiation based on gauge, barrier, seal, printability, qualification, recyclability, and delivery reliability.
- Deviation from default lens: none

## Executive view
Packaging film and sheet is a capital-intensive repeat-supply business. AI is most credible in planning, process and quality analytics, maintenance, specification handling, and commercial administration, while continuous physical production remains operator- and equipment-dependent. Demand is supported by flexible packaging functions but reshaped by downgauging, recyclability, reuse, and plastic policy.

## How AI changes the work
Extrusion, coating, lamination, winding, changeovers, maintenance, sampling, and accountable quality release remain physical. AI can assist with recipe and structure retrieval, schedule optimization, process anomaly detection, vision inspection, predictive maintenance, documentation, quoting, and customer service.

## Value capture
Differentiated barriers, sealing performance, food-contact qualification, reliable tolerances, and recyclable designs create switching friction. Commodity film is more exposed to resin-index pricing, transparent conversion spreads, high-volume bids, and customer demands for productivity sharing.

## Firm availability
Transferable independents likely exist, especially in specialty structures, but the nominal count must be screened for integrated captive plants, large-company ownership, outdated assets, maintenance capital, customer concentration, utilization, and qualification portability. General owner-age data are only a weak transaction proxy.

## Demand durability
Food protection, healthcare, industrial wrap, consumer goods, and shipping sustain film functions. E-commerce remains supportive, but lightweighting, reuse, producer responsibility, recycled-content requirements, and paper or other material substitution can reduce virgin-plastic tonnage even when packaged-unit demand grows.

## Risks and uncertainty
Principal risks are resin and energy volatility, capital intensity, uptime, quality escapes, food-contact compliance, concentrated customers, environmental policy, recycling compatibility, and rapid materials innovation. Broad sector measures poorly identify the exact product mix of an eligible firm.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1203 | — | OBSERVED | — |
| n | — | 101 | — | ESTIMATE | — |
| a | 0.11 | 0.21 | 0.32 | PROXY | S2, S3 |
| rho | 0.32 | 0.52 | 0.69 | ESTIMATE | S2, S3 |
| e | 0.38 | 0.58 | 0.74 | ESTIMATE | S1, S7 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S4, S5 |
| q | 0.28 | 0.49 | 0.69 | ESTIMATE | S1, S6 |
| d5 | 0.82 | 1.03 | 1.2 | PROXY | S6, S7, S8, S9 |
| o | 0.88 | 0.96 | 0.995 | ESTIMATE | S1, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.53 | 1.06 | ESTIMATE |
| F | 2.77 | 4.23 | 5.27 | ESTIMATE |
| C | 5.60 | 9.80 | 10.00 | ESTIMATE |
| D | 7.22 | 9.89 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation evidence is at four-digit plastics manufacturing.
- a: Employment shares do not directly measure wage-weighted task exposure.
- rho: The cited automation evidence is occupational and not a film-plant AI outcome study.
- rho: Benefits may appear as yield or throughput rather than avoidable labor.
- e: The injected firm count is model-derived.
- e: Flexible-packaging sources include downstream converters and nonplastic substrates outside this code.
- s5: ABS is not observed industry deal flow.
- s5: A plant or line sale may not constitute a qualifying transferable firm.
- q: No source measures five-year retention of AI-generated benefit.
- q: Specialty multilayer film and commodity monolayer film have materially different bargaining power.
- d5: Broad flexible-packaging measures cover formats and materials outside 326112.
- d5: Revenue and economic impact are not constant-quality quantity.
- d5: Policy direction does not equal uniform national implementation.
- o: The estimate is conditional on quantity remaining after material reduction.
- o: The lens's external operator can be displaced even if film demand persists.

## Sources
- **S1** — [2022 NAICS Definition: Plastics Packaging Film and Sheet Manufacturing](https://www.census.gov/naics/?chart=2022&details=324&input=31) (accessed 2026-07-23): Defines 326112 as converting plastic resins into flexible packaging film and packaging sheet and distinguishes adjacent activities.
- **S2** — [May 2023 OEWS: Plastics Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-23): Provides broader plastics-product occupation counts, including extruding, forming, inspection, engineering, printing, and other production roles used as an occupation-mix proxy.
- **S3** — [Metal and Plastic Machine Workers](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-23): Describes machine setup, test runs, adjustments, repairs, inspection, monitoring, and automation that allows one operator to control multiple machines.
- **S4** — [ABS Characteristics of Business Owners: 2022 Tables](https://www.census.gov/data/tables/2022/econ/abs/2022-abs-characteristics-of-owners.html) (accessed 2026-07-23): Provides age-of-owner tables used solely as a broad succession proxy.
- **S5** — [Annual Business Survey Methodology: 2022](https://www.census.gov/programs-surveys/abs/technical-documentation/methodology.2022.html) (accessed 2026-07-23): Explains ABS employer-business coverage, sampling, and limitations.
- **S6** — [2025 Flexible Packaging Achievement Awards](https://www.flexpack.org/achievement-awards/2025) (accessed 2026-07-23): Shows current innovation around recyclable flexible structures, barrier performance, product protection, and reduced environmental impact.
- **S7** — [U.S. Flexible Packaging Industry Economic Impact](https://www.flexpack.org/economic-impact) (accessed 2026-07-23): Describes flexible packaging's broad use across agriculture, food, healthcare, and e-commerce and its 2025 US economic footprint.
- **S8** — [Quarterly Retail E-Commerce Sales: First Quarter 2026](https://www.census.gov/retail/eCommerce.html) (accessed 2026-07-23): Reports $326.7 billion of seasonally adjusted first-quarter 2026 e-commerce sales, 9.8% above a year earlier and 16.9% of retail sales, as a demand-adjacent indicator.
- **S9** — [National Strategy to Prevent Plastic Pollution](https://www.epa.gov/circulareconomy/national-strategy-prevent-plastic-pollution) (accessed 2026-07-23): Documents the federal strategy's focus on reducing and recovering plastics and preventing pollution, while noting the strategy is under current-administration review.
