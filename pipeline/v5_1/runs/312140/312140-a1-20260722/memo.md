# 312140 — Distilleries

*v5.1 Stage 1 research memo. Run `312140-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.72 · L 0.66 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-enabled overhead and planning efficiency inside a physically indispensable, regulated outsourced production workflow.
**Weakness:** The eligible contract-DSP population and its transaction rate are not directly measured, while recent craft-spirit demand has weakened.

## Business-model lens
- Included: U.S. lower-middle-market distilled-spirits plants that repeatedly provide contract distillation, blending, proofing, bottling, co-packing, or related production services to external brand owners.
- Excluded: Consumer-branded distillers whose economics primarily come from their own products, tasting rooms, tourism, retail, bulk inventory speculation, captive plants, inactive permit holders, and asset-only transactions.
- Customer and revenue model: Brand owners and capacity-constrained producers buy recurring batch, case, storage, formulation, and packaging services under production agreements; inputs may be customer supplied or procured and passed through by the operator.
- Deviation from default lens: Narrowed to contract production and co-packing because NAICS 312140 mixes outsourced manufacturing services with economically distinct branded-product, hospitality, and inventory-aging models.

## Executive view
The relevant opportunity is not the typical craft distillery selling its own label; it is the smaller subset acting as a repeat outsourced production partner for brand owners. That subset combines real process, compliance, and capacity value with exposure to customer concentration and a recently weak craft market.

## How AI changes the work
AI can assist demand and batch planning, purchasing, production scheduling, maintenance triage, quality anomaly review, compliance-document preparation, customer service, sales support, and forecasting. It is less able to replace sanitation, material movement, setup, maintenance, sensory judgment, and accountable control of beverage-alcohol production.

## Value capture
Savings in overhead and planning can remain with the operator between renewals, while per-case competition and powerful brand customers will reclaim part of them. Input and packaging pass-throughs mean the retainable benefit sits primarily in conversion fees and overhead, not total invoiced value.

## Firm availability
The broad industry contains thousands of small producers, but only a minority appear to provide material recurring third-party production. Craft-spirit transactions demonstrate transferability, yet disclosed deals favor brands, and permit, inventory, real-estate, and customer-contract diligence can make a contract DSP harder to transfer cleanly.

## Demand durability
Overall spirits volume has recently held up better than revenue, and RTDs remain a growth pocket suited to co-packing. Craft volumes and producer counts weakened, however, so the five-year base is near flat rather than structurally high growth. Physical, regulated production keeps operator requirement high even as software changes workflows.

## Risks and uncertainty
The central uncertainty is population definition: public data do not reveal how many LMM DSPs are truly recurring service providers or how much revenue comes from external contracts. Other risks include brand failures, customer concentration, volatile launches, alcohol-demand softness, tariffs, excise and state rules, legacy equipment, sparse data, and liabilities tied to product quality and aged inventory.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1063 | — | OBSERVED | — |
| n | — | 151 | — | ESTIMATE | — |
| a | 0.2 | 0.31 | 0.43 | PROXY | S1, S2, S3 |
| rho | 0.33 | 0.5 | 0.67 | PROXY | S2, S4 |
| e | 0.07 | 0.14 | 0.24 | ESTIMATE | S5, S6, S7 |
| s5 | 0.12 | 0.24 | 0.38 | PROXY | S8, S9 |
| q | 0.42 | 0.59 | 0.75 | ESTIMATE | S6, S7 |
| d5 | 0.86 | 0.98 | 1.14 | PROXY | S5, S10 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.66 | 1.23 | PROXY |
| F | 1.32 | 2.90 | 4.33 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.57 | 9.31 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation table is four-digit beverage manufacturing rather than six-digit distilleries.
- a: NIST use cases and BLS direction-of-change evidence do not measure avoidable labor hours.
- a: Small plants combine jobs, making occupation-title mapping imprecise.
- rho: The Census measure changed wording to AI use in any business function and is not implementation intensity.
- rho: The NIST adoption figures cite an external manufacturer survey and may not represent small plants.
- rho: Regulatory and customer approval can slow changes to production and recordkeeping.
- e: No denominator of contract-service DSPs was found.
- e: Many plants mix own-brand and third-party work, so eligibility depends on revenue mix and customer recurrence.
- e: The frozen firm-count estimate may include business models excluded from the lens.
- s5: Deal roundups are not exhaustive and mix control acquisitions with minority investments.
- s5: Most disclosed transactions emphasize brand value rather than outsourced-service cash flow.
- s5: No industry-specific owner-age distribution was located.
- q: Public sources describe services but not contract economics or renewal repricing.
- q: Customer concentration can sharply reduce retention even under nominally fixed per-case pricing.
- q: The estimate excludes volume effects and implementation cost.
- d5: Supplier sales are not contract-manufacturing revenue.
- d5: ACSA changed its active-distiller research methodology, so the 2025 count change is not a closure rate.
- d5: Constant-quality adjustment is unavailable, and category mix is shifting rapidly toward RTDs.
- o: No source directly measures operator displacement for contract DSPs.
- o: This is quantity requiring an accountable operator, not the share of labor resistant to automation.
- o: Consolidation into larger co-packers still counts as operator-supplied demand but may leave the LMM lens.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 312100 Beverage Manufacturing](https://www.bls.gov/oes/2023/may/naics4_312100.htm) (accessed 2026-07-22): Broader beverage-manufacturing occupation mix, including 21.59% production and 12.45% sales employment shares.
- **S2** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Manufacturing AI adoption, use cases in predictive maintenance, quality control and forecasting, and implementation barriers.
- **S3** — [Factors Affecting Occupational Utilization](https://www.bls.gov/emp/tables/factors-affecting-occupational-utilization.htm) (accessed 2026-07-22): BLS expects AI-driven productivity change in wholesale/manufacturing sales and automation in several office occupations.
- **S4** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS evidence on current and expected AI use, firm-size variation, and the revised business-function measure.
- **S5** — [2025 Craft Spirits Data Project](https://americancraftspirits.org/wp-content/uploads/2017/02/2025-craft-spirits-data-project-102125-final.pdf) (accessed 2026-07-22): Craft producer counts and segmentation, 2024 volume/value declines, market share, employment, and producer-size concentration.
- **S6** — [What Is Distilled Spirits Co-Packing or Contract Production?](https://www.zahnlawpc.com/what-is-distilled-spirits-co-packing-or-contract-production/) (accessed 2026-07-22): Definition, customer relationship, common craft and RTD use, and service-fee character of contract production.
- **S7** — [Bottling & Co-Packing Services](https://www.tattersalldistilling.com/bottling-co-packing-services/) (accessed 2026-07-22): Concrete outsourced service basket: bottling, labeling, case packing, blending, proofing, formulation, sourcing, and custom distillation.
- **S8** — [Craft Grows Up](https://www.marketwatchmag.com/craft-grows-up/) (accessed 2026-07-22): Examples and qualitative breadth of craft-distillery acquisitions, while showing strategic interest centers on brands with traction.
- **S9** — [Roundup of Mergers and Acquisitions in 2024 So Far](https://www.parkstreet.com/mergers-and-acquisitions-roundup-for-2024-so-far/) (accessed 2026-07-22): First-half 2024 beverage-alcohol deal count and spirits-category examples, including the mix of acquisitions and investments.
- **S10** — [Distilled Spirits Council Annual Economic Briefing: Spirits Industry Holds Steady in Market Share Amid Economic Challenges in 2024](https://distilledspirits.org/news/distilled-spirits-council-annual-economic-briefing-spirits-industry-holds-steady-in-market-share-amid-economic-challenges-in-2024/) (accessed 2026-07-22): 2024 U.S. supplier revenue, case volume, market share, category trends, RTD growth, and industry headwinds.
