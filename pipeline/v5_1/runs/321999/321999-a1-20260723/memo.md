# 321999 — All Other Miscellaneous Wood Product Manufacturing

*v5.1 Stage 1 research memo. Run `321999-a1-20260723`, model `claude-sonnet-5`, 2026-07-23, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.16 · L 0.56 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Fragmented repeat B2B fabrication workflows offer practical AI gains in quoting and design-to-production coordination.
**Weakness:** The residual NAICS code combines unrelated products, leaving eligibility, demand, and capture highly dependent on an unknown mix.

## Business-model lens
- Included: US lower-middle-market miscellaneous wood-product manufacturers that repeatedly fabricate products or components for external OEM, industrial, commercial, or distribution customers under ongoing supply relationships.
- Excluded: One-off consumer craft and novelty sellers, transactional commodity product sellers, captive plants, pure retailers, shells, and firms outside the EBITDA band.
- Customer and revenue model: The qualifying subset earns per-unit, batch, or contract revenue from repeat customers that outsource wood fabrication; revenue is recurring through reorder behavior rather than subscription contracts.
- Deviation from default lens: This residual code mixes many unrelated products and predominantly product-sale models. The lens is narrowed to repeat B2B contract and program fabrication so eligibility and economics remain coherent.

## Executive view
The opportunity is a heterogeneous collection of physical manufacturers with moderate back-office and production-planning AI potential. A credible roll-up screen must isolate repeat B2B fabrication programs; transactional product sellers do not satisfy the frozen lens.

## How AI changes the work
AI can assist quoting, drawing interpretation, CAM preparation, purchasing, sequencing, inspection records, knowledge retrieval, and customer service. Cutting, machining, finishing, assembly, packing, and handling remain physical and often product-specific.

## Value capture
Custom work, short runs, qualification requirements, and responsive service can preserve benefits. Commodity suppliers with concentrated OEM or distributor buyers face rapid rebidding and strong pass-through pressure.

## Firm availability
The broad code and estimated firm count suggest fragmentation, while general succession and marketplace evidence supports some transfer flow. Actual availability depends on isolating eligible firms and excluding businesses whose relationships or know-how cannot transfer beyond the founder.

## Demand durability
Diversified end markets reduce reliance on one cycle but make aggregate forecasting weak. Construction and reshoring can help; imports, alternate materials, tariffs, and product-specific obsolescence can hurt. Physical production remains necessary for nearly all surviving demand.

## Risks and uncertainty
Residual-code heterogeneity is the central risk. Product mix, customer concentration, lumber exposure, tariffs, equipment condition, environmental liabilities, and uncertain recurring-service eligibility can overwhelm an apparently stable aggregate.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.164 | — | OBSERVED | — |
| n | — | 366 | — | ESTIMATE | — |
| a | 0.08 | 0.16 | 0.26 | PROXY | S1, S2 |
| rho | 0.32 | 0.53 | 0.73 | ESTIMATE | S1, S2 |
| e | 0.1 | 0.24 | 0.42 | ESTIMATE | S3, S4 |
| s5 | 0.12 | 0.21 | 0.34 | PROXY | S5, S6 |
| q | 0.28 | 0.5 | 0.72 | ESTIMATE | S3, S7 |
| d5 | 0.76 | 1 | 1.27 | ESTIMATE | S3, S4, S7 |
| o | 0.82 | 0.93 | 0.99 | ESTIMATE | S1, S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.56 | 1.25 | ESTIMATE |
| F | 2.71 | 4.77 | 6.39 | ESTIMATE |
| C | 5.60 | 10.00 | 10.00 | ESTIMATE |
| D | 6.23 | 9.30 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational percentage is for NAICS 321, not 321999, and does not itself measure AI exposure.
- a: The frozen labor ratio combines 2024 wages and 2022 receipts and applies a median harmonization divisor.
- rho: No representative adoption cohort specific to this residual industry was found.
- rho: The estimate excludes conventional automation not enabled by AI.
- e: The 366-firm input is an EBITDA-margin bridge rather than an observed roster.
- e: The code is explicitly residual and includes highly dissimilar products, so eligibility is sensitive to the product-family mix.
- s5: Neither proxy isolates NAICS 321999 or the $1-10M EBITDA population.
- s5: Closures, minority investments, and internal reorganizations must be removed from a qualifying-transfer census.
- q: No representative contract dataset exists publicly for this residual code.
- q: Recent lumber and finished-wood trade policy can obscure whether price changes reflect productivity, materials, or tariffs.
- d5: A residual-code aggregate can conceal offsetting growth and decline across products.
- d5: Tariff-driven nominal sales changes are not constant-quality quantity growth.
- o: This is a physical-process judgment, not an observed operator-retention measure.
- o: The wide product mix makes self-service and substitution risk uneven.

## Sources
- **S1** — [Wood Product Manufacturing - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics3_321000.htm) (accessed 2026-07-23): Reports the NAICS 321 occupation mix, including woodworkers at 20.15% of employment, providing a broad physical-work proxy.
- **S2** — [Wood Product Manufacturing: NAICS 321](https://www.bls.gov/IAG/TGS/iag321.htm) (accessed 2026-07-23): Describes wood-manufacturing processes as sawing, planing, shaping, laminating, and assembly and provides subsector workforce context.
- **S3** — [2022 Economic Census Manufacturing Summary Form MC-32196](https://bhs.econ.census.gov/ombpdfs2022/export/2022_MC-32196_su.pdf) (accessed 2026-07-23): Lists 321999 as all other miscellaneous wood product manufacturing and illustrates its varied product coverage, supporting the heterogeneity finding.
- **S4** — [2022 Economic Census Manufacturing Summary Statistics](https://data.census.gov/table/ECNBASIC2022.EC2231BASIC?q=EC2231BASIC) (accessed 2026-07-23): Provides official manufacturing sales, shipment, revenue, establishment, employment, and payroll fields used to define obtainable product- and industry-level diligence.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Reports a fall-2024 survey of employer-business owners' five-year ownership-transfer and closure plans.
- **S6** — [BizBuySell Insight Report Data Tables](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-23): Reports 2025 small-business transaction data by sector, including 83 reported other-manufacturing sales, providing a broad realized-deal-flow proxy.
- **S7** — [Industrial Production and Capacity Utilization: NAICS 321 Wood Product](https://www.federalreserve.gov/releases/g17/SandDesc/table1.03.htm) (accessed 2026-07-23): Provides Federal Reserve industrial-production source and series context for wood products, identifying broad output data available but not a clean residual-code demand measure.
