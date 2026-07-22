# 333914 — Measuring, Dispensing, and Other Pumping Equipment Manufacturing

*v5.1 Stage 1 research memo. Run `333914-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.61 · L 0.85 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is a durable physical installed base paired with high-value, repeatable engineering and commercial workflows that can be accelerated by AI.
**Weakness:** The principal weakness is that nearly half of broader machinery employment is production work, while heterogeneous end markets and engineered-product validation constrain uniform implementation.

## Business-model lens
- Included: US lower-middle-market manufacturers of measuring and dispensing pumps, centrifugal, turbine, reciprocating, rotary, diaphragm, water-system, oilfield, sump, and related pumping equipment and parts sold repeatedly to external industrial, municipal, commercial, agricultural, energy, and distribution customers.
- Excluded: Fluid-power pumps and motors, air and gas compressors, automotive pumps, captive internal plants, shells, non-control financing vehicles, pure distributors without qualifying manufacturing, and establishments outside the United States.
- Customer and revenue model: Business-to-business and business-to-government sales of configured equipment, replacement pumps, and parts through direct sales, specifications, distributors, and projects; repeat revenue follows installed-base replacement, maintenance, efficiency upgrades, and customer capital programs.
- Deviation from default lens: none

## Executive view
Pump manufacturing combines an essential physical installed base with meaningful engineering, configuration, sales, planning, and administrative workflows. AI can improve those information-heavy activities, while fabrication, assembly, testing, and service execution remain physical and demand is diversified across water and industrial systems.

## How AI changes the work
Credible applications include application selection, specification review, quote and proposal drafting, engineering-document retrieval, order validation, production and inventory planning, procurement support, customer service, field troubleshooting, quality documentation, and reporting. Final hydraulic, materials, compliance, and safety decisions remain accountable human work.

## Value capture
Performance differentiation, energy efficiency, application expertise, and high lifecycle costs support retention through speed, accuracy, and avoided hiring. Standardized products, distributor channels, competitive bids, and procurement comparisons should return part of the gain to customers.

## Firm availability
The estimated band-sized population is meaningful, but firm eligibility depends on separating true manufacturers from distributors, captive divisions, adjacent-equipment businesses, and non-operating entities. Broad owner demographics indicate succession potential without proving a five-year sale.

## Demand durability
Pumps serve essential water, wastewater, industrial, commercial, agricultural, and energy functions, with recurring replacement and efficiency-upgrade demand. Water infrastructure needs support growth, but diversified exposure does not remove industrial capital, construction, energy, and inventory cycles.

## Risks and uncertainty
Key uncertainties are six-digit task mix, existing automation, product complexity, implementation integration, channel pricing, firm separability, owner intent, import competition, and end-market cycles. Firm-level workflow, margin, shipment, and ownership data would resolve the largest gaps.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1407 | — | OBSERVED | — |
| n | — | 150 | — | ESTIMATE | — |
| a | 0.18 | 0.29 | 0.4 | PROXY | S1 |
| rho | 0.3 | 0.52 | 0.68 | PROXY | S2, S5, S6 |
| e | 0.72 | 0.84 | 0.93 | ESTIMATE | — |
| s5 | 0.15 | 0.25 | 0.35 | PROXY | S3 |
| q | 0.48 | 0.65 | 0.8 | ESTIMATE | S6, S7 |
| d5 | 0.94 | 1.08 | 1.22 | PROXY | S4, S5, S6 |
| o | 0.9 | 0.97 | 0.995 | ESTIMATE | S4, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.30 | 0.85 | 1.53 | PROXY |
| F | 4.58 | 5.60 | 6.29 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.46 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source covers several machinery industries rather than NAICS 333914.
- a: Occupation shares do not directly measure not-yet-automated tasks.
- a: Application engineering intensity varies sharply between standardized and engineered-to-order pumps.
- rho: Anthropic data are not pump-industry deployments.
- rho: System optimization tools demonstrate digitizable analysis but not autonomous commercial workflows.
- rho: Engineered and safety-critical applications require accountable review.
- e: The frozen firm count is an estimate derived from size classes and an industry margin bridge.
- e: Diversified machinery companies may not have separable pump operations.
- e: Manufacturing, distribution, installation, and aftermarket service can be mixed within one company.
- s5: The owner-age data are all-industry and use 2018 observations.
- s5: Owner age is not a direct sale-intent measure.
- s5: Strategic subsidiaries and sponsor-owned firms follow different transfer dynamics.
- q: Lifecycle-cost figures are association guidance and vary by application.
- q: The measuring-and-dispensing PPI series is a narrow and discontinued-like subseries, not a retention measure.
- q: Standard pumps and engineered pumps face different pricing pressure.
- d5: The EPA need horizon is twenty years and includes large non-pump spending.
- d5: DOE sources describe use and efficiency opportunity rather than pump shipments.
- d5: The code spans end markets with different cycles.
- o: The estimate is based on physical operating requirements rather than a direct substitution study.
- o: Digital monitoring may shift value toward controls and software without eliminating pump manufacturing.
- o: Imports can replace a domestic operator even though physical equipment remains necessary.

## Sources
- **S1** — [May 2023 Occupational Employment and Wage Estimates: Machinery Manufacturing (3331, 3332, 3334, and 3339)](https://www.bls.gov/oes/2023/may/naics4_3330A1.htm) (accessed 2026-07-23): Broader machinery occupation mix, including production, engineering, management, business, sales, office support, planning, and shipping roles.
- **S2** — [Anthropic Economic Index: September 2025 Report](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) (accessed 2026-07-23): Cross-industry enterprise evidence that 77% of sampled first-party API business uses involved automation patterns.
- **S3** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-23): Owner-age proxy showing 51% of responding employer-business owners were age 55 or older in the 2018 data year.
- **S4** — [Seventh Drinking Water Infrastructure Needs Survey and Assessment](https://www.epa.gov/system/files/documents/2023-09/Seventh%20DWINSA_September2023_Final.pdf) (accessed 2026-07-23): Twenty-year state drinking-water infrastructure needs of $625 billion, including distribution, treatment, storage, and source categories.
- **S5** — [Pump Systems](https://www.energy.gov/cmei/ito/pump-systems) (accessed 2026-07-23): DOE evidence on pump-system optimization, maintenance, selection, testing, variable-speed control, and water, sewage, mining, and facility applications.
- **S6** — [Pump Pros Know: Lifecycle Cost Analysis](https://www.pumps.org/pump-pros-know-lifecycle-cost-analysis/) (accessed 2026-07-23): Pump lifecycle cost structure, efficiency opportunity, maintenance components, and value of design and reliability support.
- **S7** — [Producer Price Index: Measuring and Dispensing Pumps and Parts and Attachments](https://fred.stlouisfed.org/series/PCU3339143339143) (accessed 2026-07-23): BLS producer-price observations for a directly relevant NAICS 333914 product subset, used only as pricing context.
