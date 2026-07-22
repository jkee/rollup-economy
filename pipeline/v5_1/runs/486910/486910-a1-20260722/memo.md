# 486910 — Pipeline Transportation of Refined Petroleum Products

*v5.1 Stage 1 research memo. Run `486910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.05 · L 0.26 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent physical distribution of liquid transportation fuels keeps most surviving throughput dependent on an accountable pipeline operator.
**Weakness:** Only four firms are estimated in band before removing captive and integrated systems, and route-specific demand can fall abruptly after a refinery or terminal change.

## Business-model lens
- Included: US lower-middle-market operators that transport refined petroleum products by pipeline for external refiners, marketers, airports, terminals, distributors, or other shippers on a recurring basis.
- Excluded: Captive refinery or terminal transfer lines, crude-oil pipelines, natural-gas and other-product pipelines, pipeline construction and maintenance contractors, shells, non-control financing vehicles, and businesses outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: Recurring tariffed or contracted transportation and related terminal-interface services, generally priced by barrel, distance, product, batch, or committed capacity, with interstate rates commonly subject to FERC ceilings and intrastate service subject to state or contractual regimes.
- Deviation from default lens: none

## Executive view
Refined-products pipelines provide recurring, operator-required transport on a stable installed network, but labor is a small share of receipts and the dataset indicates only four LMM-band firms. AI can improve administrative and technical-support workflows; the harder questions are whether any target is truly independent and whether corridor-specific fuel volumes remain durable.

## How AI changes the work
Likely applications include batch and nomination support, tariff billing, document search, integrity-record review, work-order triage, regulatory drafting, customer inquiries, and finance. Pumping, control-room judgment, inspection, maintenance, product-quality assurance, cybersecurity, and incident response remain human- and operator-accountable.

## Value capture
FERC indexing can let an efficient interstate carrier retain savings because ceilings follow an industry cost index rather than immediate company costs. Actual capture remains sensitive to ceiling headroom, negotiated contracts, shipper bargaining, state regulation, and competition from alternative routes or modes.

## Firm availability
The starting population is only four estimated firms, and captive or integrated systems may leave one or two eligible independent operators. Transfer events are therefore sporadic and each candidate requires entity-level ownership and customer diligence.

## Demand durability
The service remains necessary for gasoline, diesel, jet fuel, and related products, and network mileage is stable to slightly higher. Over five years, declining gasoline and biofuel substitution are offset partly by jet fuel, exports, and overall economic activity; route-level refinery and terminal changes dominate the national average.

## Risks and uncertainty
Major risks are the tiny target universe, corridor and shipper concentration, refinery closures, electrification and efficiency, product-specification limits for renewable fuels, environmental liabilities, integrity capex, cybersecurity, and rate or contract pass-through. Task exposure and implementation evidence are broader-industry proxies rather than direct measurements.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0817 | — | OBSERVED | — |
| n | — | 4 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S1, S2 |
| rho | 0.28 | 0.44 | 0.6 | PROXY | S2, S3, S4 |
| e | 0.25 | 0.45 | 0.7 | ESTIMATE | S3, S4, S5 |
| s5 | 0.08 | 0.18 | 0.32 | ESTIMATE | S3, S5 |
| q | 0.35 | 0.52 | 0.7 | PROXY | S5 |
| d5 | 0.86 | 0.97 | 1.08 | PROXY | S4, S6, S7 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.09 | 0.26 | 0.55 | PROXY |
| F | 0.12 | 0.45 | 1.03 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | PROXY |
| D | 8.08 | 9.51 | 10.00 | ESTIMATE |

## Caveats
- a: BLS data cover NAICS 486 and list common occupations rather than a complete wage-weighted task inventory for 486910.
- a: Corporate-function AI evidence is cross-industry and weighted toward firms much larger than the target lens.
- a: The frozen compensation-to-receipts ratio uses 2024 wages over 2022 receipts and is harmonized to the IPS basis; it may understate or overstate current labor intensity.
- rho: Neither adoption source is specific to pipeline transportation or lower-middle-market firms.
- rho: Safety reporting obligations demonstrate implementation friction but do not quantify AI deployment.
- rho: A small firm may buy mature embedded automation faster than it could develop bespoke AI.
- e: No public source directly identifies the four dataset-inferred LMM firms or measures their eligibility.
- e: PHMSA records count reporting systems or operators, not necessarily independent transferable firms.
- e: The frozen firm count is margin-bridged from size classes and explicitly ESTIMATE.
- s5: There is no observed control-transfer rate for eligible 486910 LMM firms.
- s5: The very small denominator makes realized five-year transfer frequency extremely lumpy.
- s5: Internal reorganizations and sales of minority interests or isolated pipe segments do not qualify.
- q: Intrastate lines and negotiated services may not follow the federal index.
- q: A carrier already pricing below its ceiling may be constrained more by competition than regulation.
- q: This primitive addresses retention after implementation, not whether the operational savings can be achieved.
- d5: National fuel demand can diverge sharply from a particular pipeline corridor after a refinery closure or terminal reconfiguration.
- d5: Liquid-fuels consumption includes products outside the current refined-products service basket.
- d5: Mileage measures network stock, not utilization or constant-quality service quantity.
- o: No source directly measures the operator-required share of year-five quantity.
- o: Consolidation may eliminate an independent firm while leaving operator-required service intact.
- o: Fuel-demand erosion and modal substitution belong primarily in d5, not o.

## Sources
- **S1** — [Pipeline Transportation: NAICS 486](https://www.bls.gov/iag/tgs/iag486.htm) (accessed 2026-07-22): Defines the pipeline subsector and reports 2025 employment in prominent operator, mechanic, pumping, and valve occupations; used as a broader-industry occupation proxy for a.
- **S2** — [Gen AI in corporate functions: Looking beyond efficiency gains](https://www.mckinsey.com/capabilities/operations/our-insights/gen-ai-in-corporate-functions-looking-beyond-efficiency-gains) (accessed 2026-07-22): Reports a 2024 survey of 276 corporate-function leaders, AI use cases, partial-role automation, barriers, and a three-to-five-year value horizon; supports a and rho by proxy.
- **S3** — [From promising to productive: Real results from gen AI in services](https://www.mckinsey.com/capabilities/operations/our-insights/from-promising-to-productive-real-results-from-gen-ai-in-services) (accessed 2026-07-22): Reports that only 3% of surveyed large-company respondents had scaled an operations-related gen-AI use case in early 2024 and discusses governance and change constraints; supports rho by proxy.
- **S4** — [Annual Report Mileage for Hazardous Liquid or Carbon Dioxide Systems](https://www.phmsa.dot.gov/data-and-statistics/pipeline/annual-report-mileage-hazardous-liquid-or-carbon-dioxide-systems) (accessed 2026-07-22): Reports 65,067 miles of petroleum/refined-products systems in 2025 versus 64,231 in 2024 and 656 hazardous-liquid records in 2025; supports network durability and operator diligence.
- **S5** — [FERC Finalizes Five-Year Review of the Oil Pipeline Index](https://www.ferc.gov/news-events/news/ferc-finalizes-five-year-review-oil-pipeline-index) (accessed 2026-07-22): States that the 2026-2031 oil-pipeline index is PPI-FG minus 0.55%, that indexed carriers may charge up to applicable ceilings, and that the regime aims to reflect industry costs and keep rates just and reasonable; supports q.
- **S6** — [Short-Term Energy Outlook: U.S. Petroleum Products, July 2026](https://www.eia.gov/outlooks/steo/report/petro_prod.php) (accessed 2026-07-22): Projects US liquid-fuels consumption of 20.5 million b/d in 2024 and 20.8 million b/d in 2027 and describes below-average gasoline consumption; supports d5 by proxy.
- **S7** — [Refinery closures and rising consumption will reduce U.S. petroleum inventories in 2026](https://www.eia.gov/todayinenergy/detail.php?amp=&id=64644) (accessed 2026-07-22): Forecasts a roughly 1% gasoline-consumption decline in 2026, biofuels at about 9% of distillate consumption, and record jet-fuel consumption; supports the mixed refined-products demand outlook.
