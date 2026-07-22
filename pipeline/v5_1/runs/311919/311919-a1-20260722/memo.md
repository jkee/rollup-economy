# 311919 — Other Snack Food Manufacturing

*v5.1 Stage 1 research memo. Run `311919-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.78 · L 0.34 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring outsourced production plus regulated physical accountability makes the service relationship hard to replace with software alone.
**Weakness:** The addressable co-manufacturer subset is unmeasured and AI exposure is modest because production labor is predominantly physical.

## Business-model lens
- Included: US lower-middle-market contract manufacturers, co-manufacturers, and private-label producers of potato chips, corn chips, popped popcorn, pretzels, and similar snack foods that repeatedly manufacture and package products for external brand owners, retailers, or foodservice customers.
- Excluded: Manufacturer-owned branded snack portfolios, captive plants, commodity-only sellers without a recurring outsourced-production relationship, shell entities, non-control financing vehicles, and firms outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: Repeat B2B production runs priced per unit, case, pound, or run under co-manufacturing, co-packing, and private-label agreements, often with additional product-development, sourcing, packaging, and logistics services.
- Deviation from default lens: The industry combines proprietary-brand manufacturers with outsourced co-manufacturers. The lens is narrowed to contract, co-manufacturing, co-packing, and private-label operations because only those firms supply the recurring outsourced service specified by the default screen.

## Executive view
The coherent opportunity is the outsourced private-label and co-manufacturing subset, not branded snack manufacturing as a whole. It combines repetitive B2B production with durable physical demand, but the AI-addressable wage base is limited because most plant work remains physical and regulated.

## How AI changes the work
Near-term AI is most credible in production scheduling, forecasting, procurement, specification and quality-document drafting, maintenance triage, customer service, and machine-vision-assisted inspection. Human operators, mechanics, sanitation staff, and qualified food-safety personnel remain central; legacy systems and validation requirements limit implementation speed.

## Value capture
Fixed-price or per-unit contract terms can let the manufacturer retain savings until renewal, especially where formulation, qualification, reliability, and scarce capacity create switching costs. Open-book costing, retailer bargaining power, tenders, and contract rebids can transfer a material share of gains to customers.

## Firm availability
Public evidence confirms an active ecosystem of co-manufacturers and private-label snack producers, but no source measures their share of LMM firms. Aging-owner evidence supports recurring sale supply, while weak broker completion rates argue against equating retirement intent with executable transfers.

## Demand durability
Snacking is broad and repeat-oriented, while contract customers continue to need physical production, packaging, food-safety controls, and accountable lot release. The quantity outlook is closer to stable than high-growth because health preferences, category maturity, and retailer assortment changes can offset convenience-led demand.

## Risks and uncertainty
The largest uncertainties are the true eligible-firm share, customer concentration and contract pass-through, and plant-specific implementation economics. Commodity inputs, recalls, allergen control, private-label bargaining, obsolete equipment, and customer insourcing can erase gains; AI should not be credited for conventional robotics already embedded in lines.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.118 | — | OBSERVED | — |
| n | — | 70 | — | ESTIMATE | — |
| a | 0.1 | 0.16 | 0.24 | PROXY | S2, S3 |
| rho | 0.25 | 0.45 | 0.65 | ESTIMATE | S3, S8 |
| e | 0.15 | 0.3 | 0.45 | ESTIMATE | S1, S4, S5 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S6, S7 |
| q | 0.4 | 0.62 | 0.8 | ESTIMATE | S4, S5 |
| d5 | 0.88 | 1.02 | 1.15 | ESTIMATE | S9, S10 |
| o | 0.94 | 0.98 | 1 | PROXY | S8, S11 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.12 | 0.34 | 0.74 | ESTIMATE |
| F | 1.31 | 2.78 | 3.96 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.27 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation figures cover NAICS 311, not 311919 or the contract-manufacturing subset.
- a: The estimate excludes conventional non-AI robotics and counts only current tasks not already automated.
- rho: No source measures five-year AI implementation in snack co-manufacturers.
- rho: Implementation may be lower in small plants with legacy equipment and higher in scaled co-manufacturers with modern MES and ERP systems.
- e: Public websites demonstrate existence, not population share.
- e: Establishment counts are not firm counts and predate the injected firm estimate.
- e: Some manufacturers mix proprietary brands and contract production; eligibility should be revenue-weighted in diligence.
- s5: Owner-age data are all-industry and not limited to LMM firms.
- s5: The sale-intention evidence is Washington-specific and the broker completion figure is not snack-industry-specific.
- s5: The estimate excludes plant closures and asset sales that do not transfer the operating firm.
- q: No public source quantifies contractual pass-through in this niche.
- q: Retention varies sharply between proprietary formulations, turnkey private label, and commodity co-packing.
- d5: The near-universal household-purchase evidence is from 1999 and establishes breadth, not current growth.
- d5: Potato availability is only one input category and is not identical to finished snack demand.
- d5: The estimate holds quality and price constant and therefore differs from nominal market forecasts.
- o: FDA requirements establish accountability but do not guarantee that the same independent operator retains the work.
- o: Volume can shift to customers' captive plants or larger co-manufacturers even when an operator remains necessary.

## Sources
- **S1** — [Snack Food and Beverages - Manufacturing Stats for the Big Game](https://www.census.gov/content/dam/Census/library/visualizations/2024/comm/snack-food-and-beverages.pdf) (accessed 2026-07-22): Census reports 2021 NAICS 311919 sales/value of shipments of $26.533 billion, annual payroll of $1.942 billion, 37,250 employees, and 441 establishments.
- **S2** — [Food Manufacturing: NAICS 311](https://www.bls.gov/iag/tgs/iag311.htm) (accessed 2026-07-22): BLS reports 2025 food-manufacturing employment including 144,690 food batchmakers, 168,370 packaging and filling machine operators, and 71,790 first-line production supervisors.
- **S3** — [Annual Survey of Manufactures Industrial Robotic Equipment: 2018-2021](https://www.census.gov/library/publications/2024/econ/2021-asm-robotic-equipment.html) (accessed 2026-07-22): Census describes plant-level measures of robot presence, worker exposure, purchases, and capital expenditures, tabulated only to broad manufacturing levels, and labels the product experimental.
- **S4** — [SnackCo of America - Full-service private label and co-packing](https://www.snackco.com/services) (accessed 2026-07-22): An industry operator describes private-label production, co-packing to customer specifications, co-manufacturing from raw-material sourcing through palletized goods, and product-development services.
- **S5** — [Ballreich Snack Food Company - Private Label and Co-Manufacturing](https://www.ballreich.com/private-label/) (accessed 2026-07-22): A snack manufacturer states that it develops, plans, produces, and delivers private-label and co-manufactured products for partners.
- **S6** — [Annual Business Survey Visualizations - Business Owners' Ages](https://www.census.gov/programs-surveys/abs/library/visualizations.html) (accessed 2026-07-22): Census states that over half of US business owners were age 55 and over according to the 2019 Annual Business Survey.
- **S7** — [New Research Details Effects of Silver Tsunami on Local Washington Economies](https://project-equity.org/press-releases/new-research-details-effects-of-silver-tsunami-on-local-washington-economies-and-what-to-do-about-it/) (accessed 2026-07-22): Project Equity reports six in ten Washington business owners planned to sell within ten years, about 15% pass to family, one-third of owners over 50 have trouble finding a buyer, and only 20% of companies listed by a leading broker sell.
- **S8** — [FSMA Final Rule for Preventive Controls for Human Food](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food) (accessed 2026-07-22): FDA states covered food facilities must maintain a written food-safety plan with hazard analysis and preventive controls, and management must ensure food workers are qualified for assigned duties.
- **S9** — [Taxing Snack Foods: What to Expect for Diet and Tax Revenues](https://ers.usda.gov/sites/default/files/_laserfiche/publications/42194/15277_aib74708_1_.pdf) (accessed 2026-07-22): USDA ERS reports that in 1999 about 91% of households purchased potato chips, about 96% purchased all chips, and 99% purchased some salty snack.
- **S10** — [From fresh to frozen: Potato per capita availability changes over time](https://ers.usda.gov/data-products/charts-of-note/113195) (accessed 2026-07-22): USDA ERS reports that annual US potato availability is about 20 pounds below the early 2000s and notes slowed growth in frozen potato products.
- **S11** — [Registration of Food Facilities and Other Submissions](https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/registration-food-facilities-and-other-submissions) (accessed 2026-07-22): FDA states facilities manufacturing, processing, packing, or holding food for US consumption must register, allow inspection, and renew registration every other year.
