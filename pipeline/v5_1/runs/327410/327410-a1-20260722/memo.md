# 327410 — Lime Manufacturing

*v5.1 Stage 1 research memo. Run `327410-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.14 · L 0.16 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High-barrier regional supply of an indispensable physical input across diversified industrial and environmental uses.
**Weakness:** An exceptionally small LMM pool and a product-centric model leave very few firms eligible under the frozen recurring-service lens.

## Business-model lens
- Included: Lower-middle-market lime manufacturers that repeatedly supply external industrial, environmental, water-treatment, metals, or construction customers and provide an accountable recurring program around product specification, testing, storage, slurrying, inventory, scheduled delivery, or application support.
- Excluded: One-off or commodity-only lime sales without substantive recurring outsourced responsibilities; captive lime plants; limestone mining without lime manufacture; shells; captive internal units; and non-control financing vehicles.
- Customer and revenue model: Repeat purchase orders, bids, and delivered-price supply arrangements for quicklime, hydrated lime, and lime slurry, with eligibility limited to relationships in which specification, availability, logistics, slurrying, inventory, or application support forms a substantive ongoing supplier obligation.
- Deviation from default lens: none

## Executive view
Lime is a capital-intensive physical commodity with strong local logistics and permitting barriers, not naturally a recurring outsourced service. Only firms with substantive ongoing specification, inventory, slurrying, delivery, or application responsibilities qualify; AI then improves a limited information and process-control layer around an operator-heavy plant.

## How AI changes the work
Applicable workflows include demand and production planning, kiln and energy optimization, predictive maintenance, laboratory trend analysis, safety and environmental documentation, purchasing, freight planning, bids, order processing, and customer support. Physical mining, calcination, maintenance execution, loading, and delivery remain the dominant constraints.

## Value capture
Scarce permitted reserves, proximity, freight economics, product specifications, and reliability can protect savings. Purchase-order bidding, delivered-price exposure, energy and diesel volatility, strong industrial procurement, and regional competition still drive sharing at repricing.

## Firm availability
The injected LMM universe contains only ten estimated firms, and most likely fail the service requirement. Strategic acquisition demand is evident in a consolidated industry, but individual plants require intensive reserve, permit, environmental, capital, labor, transport, and customer diligence.

## Demand durability
Chemical, industrial, environmental, water, metals, and construction uses diversify demand. Growth in construction, steel, and environmental customers supports the current base, while coal-plant retirements, oil-and-gas cyclicality, roof-shingle weakness, and regional construction cycles create downside.

## Risks and uncertainty
The decisive uncertainty is whether any LMM firms truly bundle a recurring outsourced service rather than simply repeat product sales. Other weaknesses are the lack of six-digit occupation exposure data, sparse transfer denominators, public-company bias, high downtime consequences, environmental and MSHA obligations, energy and freight volatility, and dependence on local reserves and customers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1493 | — | OBSERVED | — |
| n | — | 10 | — | ESTIMATE | — |
| a | 0.1 | 0.16 | 0.23 | PROXY | S2, S3 |
| rho | 0.25 | 0.42 | 0.6 | PROXY | S3, S4 |
| e | 0.02 | 0.06 | 0.15 | ESTIMATE | S1, S2 |
| s5 | 0.08 | 0.17 | 0.3 | PROXY | S2 |
| q | 0.48 | 0.64 | 0.8 | ESTIMATE | S2 |
| d5 | 0.92 | 1.03 | 1.16 | PROXY | S1, S2 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.15 | 0.40 | 0.82 | PROXY |
| F | 0.03 | 0.16 | 0.60 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.83 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No current six-digit occupation-by-wage table was available to directly measure the primitive.
- a: The public-company process may be more capital intensive and automated than the injected LMM population.
- a: The frozen compensation-to-receipts input uses 2024 wages over 2022 receipts and is harmonized to the IPS basis.
- rho: Neither adoption source isolates NAICS 327410 or the LMM band.
- rho: Industrial AI can initially augment workers without reducing headcount.
- rho: Unplanned downtime or quality errors at continuous kilns can outweigh labor savings, limiting deployment.
- e: Eligibility turns on contract substance that NAICS classification does not disclose.
- e: USGS states that more than 90% of lime consumption is chemical and industrial, but that does not make product supply a service.
- e: The injected count of ten firms is itself a margin-bridged ESTIMATE using a Paper/Forest Products margin proxy.
- s5: One public consolidator is not a complete market census.
- s5: Transactions may involve assets or mines rather than transferable operating firms.
- s5: With only ten injected LMM firms and a low eligibility share, realized opportunities are highly discrete.
- q: Observed company pricing and margins combine volume, mix, energy, freight, acquisition, and market effects rather than AI savings.
- q: Retention differs between scarce local supply and competitive accounts near overlapping plants.
- q: Large industrial and public customers may negotiate prompt pass-through.
- d5: A public company's strong volume growth may reflect acquisitions, capacity additions, or share gains.
- d5: End-market diversity masks large regional and customer-specific swings.
- d5: The primitive is constant-price quantity, while company revenue also reflects pricing and mix.
- o: USGS notes that some paper mills and water-treatment plants regenerate lime, but does not quantify displacement for the eligible lens.
- o: Operator requirement is distinct from labor intensity inside the operator.
- o: A few large customer decisions can materially affect a small regional supplier.

## Sources
- **S1** — [Lime Statistics and Information](https://www.usgs.gov/centers/national-minerals-information-center/lime-statistics-and-information) (accessed 2026-07-22): USGS describes lime's chemical, industrial, and environmental uses and states that more than 90% of current U.S. consumption is for chemical and industrial uses.
- **S2** — [United States Lime & Minerals, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/82020/000110465926020480/uslm-20251231x10k.htm) (accessed 2026-07-22): Documents production processes, purchase-order and bid sales, 675 customers, regional transport, 2025 volume growth of 11.7% and price growth of 5.6%, competitive and permitting barriers, consolidation, acquisitions, delivered-price exposure, end-market risks, plant modernization, and employee count.
- **S3** — [The Rise of Artificial Intelligence in U.S. Manufacturing — Text Only](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Manufacturing AI use cases in process optimization, maintenance, quality, inventory, document management, resource planning, and scheduling, plus data, cost, skills, cybersecurity, and legacy-system barriers.
- **S4** — [Large Firms With At Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS showed overall U.S. business AI use at 17%-20% from December 2025 to May 2026, expected use at 20%-23%, and lower adoption among the smallest firms.
