# 311513 — Cheese Manufacturing

*v5.1 Stage 1 research memo. Run `311513-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.09 · L 0.25 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent consumption and a varied base of specialty and outsourced cheese producers support recurring operator demand.
**Weakness:** Physical production dominates labor, while commodity benchmarks and concentrated buyers can compress retained benefits.

## Business-model lens
- Included: U.S. lower-middle-market operators that repeatedly manufacture natural, processed, specialty, private-label, or substitute cheese products for external retail, foodservice, distributor, or industrial customers.
- Excluded: Cottage-cheese manufacturing, cheese-based salad dressings, dairy farms without qualifying manufacturing operations, captive internal plants, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat product sales under distributor, retailer, foodservice, ingredient, branded, and private-label relationships; revenue is primarily unit- or weight-priced rather than explicitly billed labor.
- Deviation from default lens: none

## Executive view
Cheese manufacturing combines durable physical demand, a broad set of potentially transferable specialty and private-label operators, and modest AI opportunity in information-heavy plant and commercial workflows. The limiting fact is that most labor and operational risk remain tied to physical food production, while commodity and buyer power can erode retained savings.

## How AI changes the work
AI can improve scheduling, demand forecasts, milk and ingredient procurement, quality-document review, deviation triage, maintenance diagnostics, label compliance, customer service, and SKU profitability analysis. It cannot by itself replace most batching, handling, sanitation, packaging, maintenance, laboratory, and aging-room work.

## Value capture
Differentiated specialty, branded, aged, and service-intensive products offer better retention than commodity blocks or transparent private-label contracts. Renewals, benchmark formulas, retailer procurement, and competing processors' adoption will share a material part of implemented savings with customers.

## Firm availability
The frozen dataset identifies 95 LMM-band firms, but eligibility depends on independence, recurring external customers, plant and brand transferability, customer concentration, and separation from farms, cooperatives, or larger parents. National owner-age evidence supports succession pressure, though cheese-specific control-transfer data are absent.

## Demand durability
Long-run USDA evidence shows cheese consumption has expanded substantially, even as the latest annual reading softened slightly. Mature penetration, dietary shifts, alternatives, and large-processor share gains temper the five-year outlook for the exact LMM service basket.

## Risks and uncertainty
Key diligence risks are existing automation, six-digit task mix, food-safety and recall exposure, customer concentration, milk and commodity volatility, brand durability, aging inventory, cybersecurity, contract repricing, plant capex, and the true frequency of control sales. A poor target can combine low differentiation, open-book pricing, legacy systems, and substantial compliance or maintenance debt.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0692 | — | OBSERVED | — |
| n | — | 95 | — | ESTIMATE | — |
| a | 0.11 | 0.2 | 0.3 | PROXY | S2 |
| rho | 0.25 | 0.45 | 0.68 | ESTIMATE | S3, S4 |
| e | 0.45 | 0.65 | 0.82 | ESTIMATE | S1 |
| s5 | 0.09 | 0.19 | 0.31 | PROXY | S5 |
| q | 0.3 | 0.55 | 0.78 | ESTIMATE | — |
| d5 | 0.97 | 1.08 | 1.2 | PROXY | S6, S7 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.08 | 0.25 | 0.56 | ESTIMATE |
| F | 2.54 | 4.09 | 5.19 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.12 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation mix covers all dairy product manufacturing, not cheese alone.
- a: Employment counts require judgmental conversion to wage-weighted task exposure.
- a: Robotics-only opportunities are outside the AI-substitution construct.
- rho: Public regulatory guidance does not measure cheese-plant AI implementation rates.
- rho: Implementation will differ sharply between modern high-throughput plants and small specialty facilities.
- e: The frozen LMM firm count is used without re-estimation.
- e: The NAICS definition does not reveal enterprise separability, recurring-customer quality, or control availability.
- s5: Owner-age evidence is national, cross-industry, and based on 2018 data.
- s5: The statistic covers owners rather than firms and does not measure transaction incidence.
- q: No public evidence directly measures five-year retention of AI-derived benefit in cheese manufacturing.
- q: Retention varies widely between commodity, private-label, branded, aged, and specialty cheese.
- d5: National consumption is not restricted to domestically manufactured or LMM-supplied cheese.
- d5: Loss-adjusted availability remains an estimate rather than transaction-level consumption.
- d5: Aggregate growth can mask declines in individual cheese formats or eligible-firm market share.
- o: This estimates operator necessity, not the number of workers required.
- o: Operator responsibility can shift to larger integrated manufacturers even when it cannot be removed from the chain.

## Sources
- **S1** — [North American Industry Classification System: 311513 Cheese Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines 311513 as manufacturing cheese products except cottage cheese from milk or processed milk products, or cheese substitutes from nondairy substances, and identifies cross-references.
- **S2** — [BLS OEWS Data Tables for Industry Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest dairy-manufacturing occupations, including 25,520 food batchmakers, 23,690 packaging/filling operators, 8,170 material movers, and 7,840 production supervisors.
- **S3** — [FDA: Computerized Systems in the Food Processing Industry](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-guides/computerized-systems-food-processing-industry) (accessed 2026-07-22): Describes computerized food-processing records and controls and the review needed for regulatory equivalence and safety-critical functions.
- **S4** — [FDA: Keeping Your Milk Safe From the Grass to the Glass](https://www.fda.gov/consumers/consumer-updates/keeping-your-milk-safe-grass-glass) (accessed 2026-07-22): Describes regulated dairy responsibilities for processing times and temperatures, equipment control and testing, worker safety, laboratory testing, and oversight.
- **S5** — [U.S. Census Bureau: Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding owners of U.S. employer businesses were age 55 or older in the 2019 ABS covering data year 2018.
- **S6** — [USDA ERS: Cheese per capita consumption from 2014-24](https://ers.usda.gov/data-products/chart-gallery/113732) (accessed 2026-07-22): Shows U.S. per-capita cheese consumption increasing from 2014 through 2023 and falling slightly in 2024.
- **S7** — [USDA ERS: Cheese and yogurt popularity grew over last four decades](https://www.ers.usda.gov/data-products/charts-of-note/105777) (accessed 2026-07-22): Reports loss-adjusted daily cheese consumption of 0.74 cup-equivalents per person in 2021 versus 0.36 in 1981 and explains the loss adjustment.
