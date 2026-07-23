# 337910 — Mattress Manufacturing

*v5.1 Stage 1 research memo. Run `337910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.50 · L 0.56 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring replacement of an essential physical sleep product supports long-run demand.
**Weakness:** Weak current units, imports, and promotion-heavy retail severely constrain domestic growth and value capture.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly supplying innerspring, box spring, hybrid, foam, latex, compressed, and other noninnerspring mattresses on stock, custom, branded, private-label, hospitality, healthcare, or institutional bases to external retailers, distributors, direct consumers, and commercial customers.
- Excluded: Captive internal units, shells, mattress-fabric or spring-component suppliers, furniture retailers without manufacturing, used or refurbished mattress sellers, and sleep accessories classified outside NAICS 337910.
- Customer and revenue model: Wholesale retailer and distributor programs, private-label supply, direct-to-consumer e-commerce, contract hospitality or institutional sales, and replacement purchases, generally priced per mattress, foundation, set, or program.
- Deviation from default lens: none

## Executive view
Mattresses have durable replacement demand but are emerging from an unusually weak unit cycle. AI can assist forecasts, marketing, service, orders, warranty, quality, and scheduling, while most plant work remains physical. Retail promotions, e-commerce comparison, powerful channels, and imports make benefit retention difficult.

## How AI changes the work
AI can improve demand and promotion planning, product content, customer service, order checks, warranty triage, component scheduling, and visual inspection. Cutting, sewing, spring and foam work, quilting, tape edging, compression, packing, and handling remain physical. Soft-material variability and subjective comfort limit automated judgment.

## Value capture
Brands, differentiated construction, retailer slots, delivery, and warranty create some defensibility. Frequent sales events, online price transparency, retailer leverage, returns, private-label bids, and compressed imports share most savings with channels and consumers.

## Firm availability
The estimated in-band count needs correction for a machinery-sector margin, ultimate ownership, imported content, and assembly-only models. Regional brands and contract manufacturers may transfer, but weak demand, concentration, and warranties can make distressed closures more common than qualifying sales.

## Demand durability
Replacement demand stabilizes the category over long periods, but cited industry units remain sharply below the prior year and supplier commentary points to historically low volumes. Housing, affordability, post-pandemic normalization, and imports determine whether stabilization becomes recovery.

## Risks and uncertainty
Risks include prolonged consumer weakness, import and tariff shifts, retailer concentration, promotions, returns, warranty and flammability compliance, foam and textile costs, brand spending, inventory, and an unreliable EBITDA-band estimate. Direct task, contract, and transfer data are sparse.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.131 | — | OBSERVED | — |
| n | — | 79 | — | ESTIMATE | — |
| a | 0.14 | 0.22 | 0.31 | PROXY | S2, S3 |
| rho | 0.31 | 0.49 | 0.65 | PROXY | S3 |
| e | 0.58 | 0.76 | 0.9 | ESTIMATE | S1, S5 |
| s5 | 0.15 | 0.27 | 0.41 | PROXY | S6 |
| q | 0.18 | 0.36 | 0.55 | ESTIMATE | S5 |
| d5 | 0.87 | 0.98 | 1.11 | PROXY | S4, S5 |
| o | 0.94 | 0.985 | 0.998 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.23 | 0.56 | 1.06 | PROXY |
| F | 3.32 | 4.58 | 5.48 | ESTIMATE |
| C | 3.60 | 7.20 | 10.00 | ESTIMATE |
| D | 8.18 | 9.65 | 10.00 | ESTIMATE |

## Caveats
- a: BLS evidence is broader than six-digit mattress manufacturing.
- a: Already-automated cutting, quilting, and compression tasks are excluded from the remaining opportunity.
- rho: AI-tool adoption does not establish labor substitution.
- rho: Marketing productivity may support volume rather than reduce labor.
- e: The provided count uses a machinery EBITDA margin that may materially misclassify mattress firms.
- e: Industry sources describe increasing imports and US assembly-only models, complicating the manufacturer lens.
- s5: No six-digit qualifying-transfer denominator was found.
- s5: Succession-plan fragility is not a transaction probability.
- q: Culp's filing documents channel and import pressure but is a fabric supplier rather than a mattress manufacturer.
- q: Capture varies greatly between differentiated premium brands, regional wholesale, private label, and commodity boxed mattresses.
- d5: The cited ISPA comparison is a short-period industry result rather than a five-year forecast.
- d5: Import share affects domestic manufacturer demand even when US consumer quantity is stable.
- d5: Market value and unit demand moved differently.
- o: An accountable operator may be offshore or a large brand even when a physical mattress remains necessary.
- o: Domestic operator demand can decline faster than US consumption because compressed products are easier to import.

## Sources
- **S1** — [Census 2022 NAICS definition: 337910 Mattress Manufacturing](https://www.census.gov/naics/?details=33&input=33&year=2022) (accessed 2026-07-22): Defines innerspring, box spring, and noninnerspring mattresses made on stock or custom and assembled or knockdown bases.
- **S2** — [BLS May 2023 occupation estimates for Furniture and Related Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_3370A1.htm) (accessed 2026-07-22): Provides occupation-level employment and wages for the broader furniture industries, including sewing, upholstery, finishing, machine operation, and other production work.
- **S3** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Reports 46% manufacturing AI-tool use and more than 80% expecting increased use in two years, with operational use cases and adoption barriers.
- **S4** — [ISPA 2026 Mattress Industry Trends Report overview](https://sleepproducts.org/2026/07/mattress-industry-trends-report-2026-overview/) (accessed 2026-07-22): Reports US mattress market value down 6.5% year over year and unit shipments down 13.2%, documenting current consumer-demand softness.
- **S5** — [Culp 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/723603/000095017025095233/culp-20250427.htm) (accessed 2026-07-22): Describes historically low domestic mattress volume, replacement demand, consumer and housing pressure, imports, assembly-only models, e-commerce and warehouse-club channels, and compressed mattresses.
- **S6** — [Deloitte Private survey: generational disparities in family-business succession planning](https://www2.deloitte.com/us/en/pages/about-deloitte/articles/press-releases/deloitte-private-survey-generational-disparatires-emerge-insuccession-planning-and-priorities-shaping-family-businesses.html) (accessed 2026-07-22): Describes a January 2024 survey of 500 US family-enterprise respondents and reports that 24% of current-generation respondents strongly agreed their succession plan would withstand departure of an important family employee.
