# 312230 — Tobacco Manufacturing

*v5.1 Stage 1 research memo. Run `312230-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.14 · L 0.15 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A regulated physical manufacturing role that remains necessary while AI can compress planning, documentation, quality-review, and support work.
**Weakness:** Eligibility and transferability are poorly measured, and combustible decline plus product-authorization risk can overwhelm operational gains.

## Business-model lens
- Included: U.S. lower-middle-market tobacco and nicotine-product manufacturers providing recurring contract, private-label, formulation, processing, packaging, or labeling services to external brand owners for legally marketable adult products.
- Excluded: Manufacturers whose economics primarily come from proprietary brands, foreign-only plants, leaf growers, distributors, retailers, unauthorized-product businesses, captive factories, product-IP holding companies, and non-control investments.
- Customer and revenue model: External brand owners purchase repeat production runs, often priced per unit or batch with formulation, packaging, regulatory documentation, and input terms governed by manufacturing agreements.
- Deviation from default lens: Narrowed to third-party contract and private-label manufacturing because NAICS 312230 combines outsourced production with economically distinct proprietary-brand manufacturing, and only the former fits the recurring outsourced-service lens.

## Executive view
The coherent population is the small subset of tobacco and nicotine manufacturers that repeatedly produce for external brand owners. Physical production and regulatory accountability make the service durable, but the eligible universe is narrow, category demand is shifting away from combustible products, and regulatory authorization can determine whether a customer relationship has value at all.

## How AI changes the work
AI can support planning, forecasting, documentation, regulatory-file retrieval, complaint triage, quality anomaly detection, maintenance, inspection review, purchasing, and customer service. It is less able to replace controlled formulation, machine operation, maintenance, testing, packaging, material movement, or accountable release.

## Value capture
Contract pricing should preserve some gains between renewals, and validated processes or scarce regulatory capabilities can create switching costs. Open-book costing, volume-linked economics, powerful brand customers, and portable specifications can instead push savings through to customers.

## Firm availability
FDA recognizes third-party manufacturers and reports substantial domestic establishment activity, but public data do not separate own-brand, contract, relabeling, and ENDS businesses. A disclosed nicotine-pouch transaction confirms contract continuity after product-IP transfer, not a broad market of plant-control sales.

## Demand durability
Adult tobacco use has shifted from cigarettes toward e-cigarettes rather than disappearing overall, while nicotine-pouch sales have grown quickly. Eligible plants tied to legacy combustibles face contraction; those with authorized modern-oral capacity may grow. The resulting service-basket outlook is near flat with unusually wide regulatory and mix risk.

## Risks and uncertainty
Principal risks are a tiny eligible population, dependence on a few products or customers, FDA authorization and enforcement, state taxes and restrictions, litigation, reputational constraints, import competition, product recalls, and rapidly shifting category preferences. Public data provide no direct contract-manufacturing revenue share, pricing, owner age, or control-transfer rate.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0247 | — | OBSERVED | — |
| n | — | 23 | — | ESTIMATE | — |
| a | 0.23 | 0.34 | 0.46 | PROXY | S1, S2 |
| rho | 0.28 | 0.44 | 0.61 | PROXY | S2, S3, S4 |
| e | 0.12 | 0.24 | 0.4 | ESTIMATE | S4, S5, S6 |
| s5 | 0.1 | 0.22 | 0.36 | PROXY | S5, S6 |
| q | 0.4 | 0.58 | 0.74 | ESTIMATE | S4, S6 |
| d5 | 0.72 | 0.94 | 1.2 | PROXY | S7, S8, S9 |
| o | 0.91 | 0.97 | 1 | ESTIMATE | S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.06 | 0.15 | 0.28 | PROXY |
| F | 0.39 | 1.28 | 2.35 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.55 | 9.12 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation table covers all employer sizes and proprietary-brand manufacturers.
- a: NIST use cases do not quantify avoidable labor hours.
- a: The very low frozen compensation-to-output ratio means even substantial task exposure applies to a small cost base.
- rho: Current AI use is not the implemented share of exposed labor.
- rho: Contract plants may lack the data and IT staff of large manufacturers.
- rho: Regulatory documentation can create both automatable work and severe error costs.
- e: FDA's 900-establishment universe is broader than NAICS 312230 and is not a firm count.
- e: Public descriptions do not disclose the share of revenue derived from contract manufacturing.
- e: The frozen LMM count is margin-bridged with a food-processing margin that may be poorly matched to tobacco.
- s5: The cited transaction acquired a product range rather than control of the contract manufacturer.
- s5: FDA's 4% rate combines entry and exit assumptions and does not observe transfers.
- s5: Unauthorized-product exposure can make an otherwise operating business nontransferable.
- q: No public sample of tobacco contract-manufacturing fee structures was found.
- q: Customer and product concentration can dominate bargaining power.
- q: This estimate excludes implementation cost and demand effects.
- d5: Consumer prevalence and sales are not outsourced manufacturing demand.
- d5: FTC data are from major manufacturers and lag the five-year horizon.
- d5: Product regulation, enforcement, taxation, and import rules can shift demand abruptly.
- o: No direct displacement measure exists for contract tobacco manufacturers.
- o: Operator requirement is distinct from the amount of labor required.
- o: Demand moved to imported products still requires an operator but may leave the U.S. lens.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 312200 Tobacco Manufacturing](https://www.bls.gov/oes/2023/may/naics4_312200.htm) (accessed 2026-07-22): Tobacco-manufacturing employment and wage mix, including production, material moving, maintenance, office, management, business, sales, science, and legal roles.
- **S2** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Manufacturing AI uses in predictive maintenance, quality control, and demand forecasting, plus adoption barriers.
- **S3** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): National current and expected business AI use and firm-size differences from BTOS.
- **S4** — [Manufacturing](https://www.fda.gov/tobacco-products/compliance-enforcement-training/manufacturing) (accessed 2026-07-22): FDA definition of tobacco manufacturing and domestic establishment registration, product listing, reporting, and compliance requirements.
- **S5** — [Establishment Registration and Product Listing for Tobacco Products: Preliminary Regulatory Impact Analysis](https://www.fda.gov/media/193313/download?attachment=) (accessed 2026-07-22): Recognition of third-party manufacturing; 900 active domestic registrations in August 2025; estimated 4% annual entry and exit; regulatory baseline and market characterization.
- **S6** — [Imperial Acquires US Nicotine Pouches Range from TJP](https://www.imperialbrandsplc.com/news/key-announcements/2023/imperial-acquires-us-nicotine-pouches-range-from-tjp) (accessed 2026-07-22): Acquisition of 14 nicotine-pouch variants for initial £65 million plus volume-linked deferred consideration, with TJP continuing as contract manufacturer.
- **S7** — [Tobacco Product Use Among Adults — United States, 2017–2023](https://www.cdc.gov/mmwr/volumes/74/wr/mm7407a3.htm) (accessed 2026-07-22): Adult use shift from exclusive cigarettes to exclusive e-cigarettes and no net change in overall current adult tobacco use.
- **S8** — [FTC Releases Reports on Cigarette and Smokeless Tobacco Sales and Marketing Expenditures for 2022](https://search.ftc.gov/news-events/news/press-releases/2023/10/ftc-releases-reports-cigarette-smokeless-tobacco-sales-marketing-expenditures-2022) (accessed 2026-07-22): Traditional smokeless volume decline, revenue, promotions, and growth of non-tobacco nicotine lozenge, puck, and pouch sales.
- **S9** — [Swedish Match USA, Inc. Modified Risk Tobacco Product Applications for ZYN Products](https://www.fda.gov/tobacco-products/advertising-and-promotion/swedish-match-usa-inc-modified-risk-tobacco-product-mrtp-applications-zyn-products) (accessed 2026-07-22): FDA marketing authorization and modified-risk orders for 20 nicotine-pouch products, illustrating product-specific authorization and category development.
