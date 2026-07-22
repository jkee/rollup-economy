# 326220 — Rubber and Plastics Hoses and Belting Manufacturing

*v5.1 Stage 1 research memo. Run `326220-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.11 · L 1.04 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat physical demand plus practical AI assistance in planning, quality, inspection, and maintenance.
**Weakness:** Most labor is embodied in physical production, while powerful buyers can reclaim savings through repricing.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly supplying rubber or reinforced-plastics hose, belting, and purchased-hose garden-hose products to external OEM, distributor, replacement, and industrial customers.
- Excluded: Captive internal plants, financial shells, rubber tubing, plastics tubing, molded mechanical rubber goods, and fluid-power hose assemblies classified outside NAICS 326220.
- Customer and revenue model: Repeat purchase orders, supply agreements, catalog and distributor sales, and OEM programs; revenue is predominantly product sales rather than time-based professional fees.
- Deviation from default lens: none

## Executive view
This is a repeat-supply physical manufacturing business with a bounded AI labor opportunity. The practical thesis is operational: improve quoting, planning, quality analysis, inspection, maintenance prediction, and administrative throughput while preserving process know-how and customer qualification. Hands-on production remains dominant, and procurement pressure limits how much benefit stays with the operator.

## How AI changes the work
AI can assist demand forecasts, production schedules, engineering and quality documentation, computer-vision inspection, root-cause analysis, and predictive maintenance. It is less able to replace material preparation, extrusion or forming, reinforcement, curing, changeovers, physical testing, packing, and maintenance execution. Legacy equipment and sparse labeled defect histories make implementation plant-specific.

## Value capture
Engineered and qualified SKUs can protect savings until a renewal or program negotiation, but OEM price-downs, distributor leverage, competitive rebids, and commodity comparisons return part of the benefit to customers. Capture depends more on qualification depth and switching cost than on the mere existence of an AI tool.

## Firm availability
The estimated LMM population should contain many transferable operating companies, but the count is margin-bridged rather than observed. Succession evidence is broad and does not reveal a six-digit transaction rate; family transfers, closures, and owner-dependent firms reduce qualifying deal supply.

## Demand durability
Industrial maintenance and vehicle replacement sustain hose and belt demand. Electrification can remove some engine-related products while adding thermal-management needs, and software does not replace the physical product. Real US basket growth is therefore likely near stable to modestly positive rather than matching headline global market forecasts.

## Risks and uncertainty
Major risks are raw-material and energy volatility, customer concentration, OEM qualification liability, safety-critical defects, offshore competition, legacy equipment integration, and confusing quality or throughput gains with removable labor. The weakest evidence concerns six-digit occupation tasks, contract pass-through, and completed control transfers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2365 | — | OBSERVED | — |
| n | — | 74 | — | ESTIMATE | — |
| a | 0.15 | 0.23 | 0.32 | PROXY | S2, S3 |
| rho | 0.3 | 0.48 | 0.65 | PROXY | S3 |
| e | 0.65 | 0.82 | 0.93 | ESTIMATE | S1 |
| s5 | 0.14 | 0.24 | 0.36 | PROXY | S5 |
| q | 0.28 | 0.45 | 0.62 | ESTIMATE | — |
| d5 | 0.95 | 1.03 | 1.12 | PROXY | S4, S6 |
| o | 0.93 | 0.97 | 0.99 | ESTIMATE | S1 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.43 | 1.04 | 1.97 | PROXY |
| F | 3.29 | 4.42 | 5.23 | ESTIMATE |
| C | 5.60 | 9.00 | 10.00 | ESTIMATE |
| D | 8.84 | 9.99 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation evidence is available at the broader rubber-product level, not six-digit 326220.
- a: NIST use cases show technical applicability, not realized labor substitution.
- rho: The adoption survey covers US manufacturing generally and includes chatbots, which need not affect plant labor.
- rho: Implementation is not the same as headcount removal; avoidable hiring is included but quality rework is not counted as labor substitution unless it removes labor hours.
- e: The provided firm count is margin-bridged and may misclassify firms into the EBITDA band.
- e: The NAICS definition identifies establishments, while transfer eligibility applies to firms and may span multiple establishments or codes.
- s5: No six-digit control-transfer denominator was found.
- s5: Succession-plan resilience is not an observed transaction probability.
- q: Capture varies sharply between proprietary qualified hose, OEM programs, industrial distribution, and garden-hose products.
- q: No representative contract dataset was found.
- d5: The Census figure is nominal and a level, not a five-year constant-price forecast.
- d5: The commercial forecast is global and automotive-only.
- d5: The provided receipts input uses a different vintage and should not be treated as a demand trend.
- o: Operator requirement can migrate to larger automated suppliers even when the physical product remains.
- o: The estimate concerns quantity requiring an accountable operator, not domestic production share.

## Sources
- **S1** — [2017 NAICS definition: 326220 Rubber and Plastics Hoses and Belting Manufacturing](https://www.census.gov/naics/?details=326220&input=326220&year=2017) (accessed 2026-07-22): Defines the included physical products and cross-references rubber tubing, plastics tubing, mechanical rubber goods, and fluid-power hose assemblies to other industries.
- **S2** — [BLS 2024-34 industry-occupation matrix data, by industry](https://www.bls.gov/emp/tables/industry-occupation-matrix-industry.htm) (accessed 2026-07-22): Provides the official occupation-matrix entry for rubber product manufacturing (NAICS 326200), the closest published BLS industry occupation aggregate used for the task-exposure bridge.
- **S3** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Reports 46% current AI-tool use and more than 80% expecting increased use in two years; identifies inspection, predictive maintenance, quality control and forecasting uses plus data, cost, skills, cyber, and legacy-system barriers.
- **S4** — [Census AIES manufacturing summary statistics for 32622](https://data.census.gov/table/AIESBASICTIMESERIES.AIES31BASIC01?codeset=naics~32622&g=010XX00US) (accessed 2026-07-22): Reports 2023 US sales, value of shipments, or revenue of $8,319,512,000 for rubber and plastics hoses and belting manufacturing.
- **S5** — [Deloitte Private survey: generational disparities in family-business succession planning](https://www2.deloitte.com/us/en/pages/about-deloitte/articles/press-releases/deloitte-private-survey-generational-disparatires-emerge-insuccession-planning-and-priorities-shaping-family-businesses.html) (accessed 2026-07-22): Describes a January 2024 survey of 500 US family-enterprise respondents and reports that 24% of current-generation respondents strongly agreed their succession plan would withstand departure of an important family employee.
- **S6** — [Automotive Rubber Hoses global market overview](https://www.marketresearch.com/Global-Industry-Analysts-v1039/Automotive-Rubber-Hoses-41276685/) (accessed 2026-07-22): Reports a global automotive-rubber-hose market estimate of $10.3 billion in 2025 and $12.3 billion in 2032, corresponding to stated 2.5% annual growth; used only as a directional end-market proxy.
