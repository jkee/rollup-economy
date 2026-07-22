# 311512 — Creamery Butter Manufacturing

*v5.1 Stage 1 research memo. Run `311512-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.29 · L 0.10 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable physical consumption and the continuing need for a regulated manufacturing operator support the opportunity.
**Weakness:** Most labor is hands-on production work and much of the small industry may be captive, concentrated, or commercially price-takers.

## Business-model lens
- Included: U.S. lower-middle-market operators that repeatedly manufacture and supply creamery butter from milk or processed milk products to external retail, foodservice, private-label, or industrial customers.
- Excluded: Margarine and butter-substitute manufacturing, dairy farming, captive plants without external customers, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat product sales under distributor, retailer, foodservice, industrial-ingredient, or private-label relationships; pricing is typically per unit or pound rather than an explicit labor fee.
- Deviation from default lens: none

## Executive view
Creamery butter manufacturing has durable physical demand and an unavoidable accountable-operator role, but the implementable AI opportunity is confined mainly to information work around a capital-intensive production process. Commercial attractiveness depends on finding genuinely independent, repeat-supply operators rather than captive or strategically inseparable plants.

## How AI changes the work
AI is most relevant to production planning, procurement forecasts, quality-document review, deviation triage, maintenance troubleshooting, customer service, and administrative work. The dominant jobs remain batching, filling, moving, supervising, maintaining, and inspecting physical production, so large labor substitution would require conventional automation or robotics beyond this screen's AI construct.

## Value capture
Unit-priced product sales allow initial retention of efficiency benefits, but commodity benchmarks, concentrated buyers, private-label bids, and competitive renewal pricing can transfer a material share to customers over five years. Differentiated branded or specialty output should retain more than open-book or commodity supply.

## Firm availability
The frozen dataset identifies 15 LMM-band firms, but only an estimated subset will be independent, externally recurring suppliers with transferable operations. National owner-age evidence suggests succession pressure, while the absence of butter-specific transfer data makes timing uncertain.

## Demand durability
USDA-derived evidence shows record 2024 per-capita butter consumption and decade growth, supporting a modestly positive five-year volume base case. Demand can nevertheless migrate toward large integrated processors, imports, substitutes, or customer-owned capacity even if national consumption holds up.

## Risks and uncertainty
The main uncertainties are six-digit occupation mix, existing automation, plant-level AI readiness, customer concentration and contract repricing, eligible ownership structure, and transaction incidence. Food-safety validation, cybersecurity, data quality, commodity input volatility, recalls, and buyer bargaining power can limit realized benefit.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0312 | — | OBSERVED | — |
| n | — | 15 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S2 |
| rho | 0.25 | 0.45 | 0.65 | ESTIMATE | S3, S4 |
| e | 0.35 | 0.55 | 0.75 | ESTIMATE | S1 |
| s5 | 0.08 | 0.18 | 0.3 | PROXY | S5 |
| q | 0.25 | 0.48 | 0.7 | ESTIMATE | — |
| d5 | 0.94 | 1.06 | 1.16 | PROXY | S6, S7 |
| o | 0.95 | 0.98 | 1 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.03 | 0.10 | 0.23 | ESTIMATE |
| F | 0.56 | 1.46 | 2.37 | ESTIMATE |
| C | 5.00 | 9.60 | 10.00 | ESTIMATE |
| D | 8.93 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source is NAICS 311500, not six-digit butter manufacturing.
- a: Employment counts are not wage-weighted task shares and require judgmental task mapping.
- a: The estimate excludes robotics-only substitution and assumes current, not-yet-automated tasks.
- rho: FDA guidance demonstrates feasibility and control requirements but does not measure AI adoption or butter-plant implementation rates.
- rho: Small plants may lack clean data and integration staff; modern plants may implement faster than the base case.
- e: The frozen firm-count estimate is not re-estimated here.
- e: Public NAICS descriptions identify activities but not recurring external-customer eligibility or enterprise separability.
- s5: The owner-age statistic is national and cross-industry, with 2018 vintage.
- s5: The source covers responding owners, not firms, and ownership age does not observe transfers.
- q: No public source directly measures five-year retention of AI-derived gross benefit in butter manufacturing.
- q: Branded and differentiated specialty butter may retain more than commodity or private-label supply.
- d5: Apparent consumption does not account fully for waste and is not limited to U.S.-manufactured output.
- d5: The most recent figures are reported by an industry publication citing USDA/IDFA rather than extracted directly from the USDA file.
- d5: Product demand can grow while the eligible LMM supplier share declines.
- o: The estimate concerns accountable-operator need, not employment intensity.
- o: Large customers may vertically integrate even though a responsible manufacturing operator remains somewhere in the chain.

## Sources
- **S1** — [North American Industry Classification System: 311512 Creamery Butter Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines 311512 as establishments manufacturing creamery butter from milk or processed milk products and excludes margarine or margarine-butter blends.
- **S2** — [BLS OEWS Data Tables for Industry Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest occupations in dairy product manufacturing, including 25,520 food batchmakers, 23,690 packaging and filling operators, 8,170 material movers, and 7,840 production supervisors.
- **S3** — [FDA: Computerized Systems in the Food Processing Industry](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-guides/computerized-systems-food-processing-industry) (accessed 2026-07-22): Describes acceptable computerized record keeping and real-time control functions and the need to assess equivalence and safety-critical controls.
- **S4** — [FDA: Keeping Your Milk Safe From the Grass to the Glass](https://www.fda.gov/consumers/consumer-updates/keeping-your-milk-safe-grass-glass) (accessed 2026-07-22): Details operator responsibilities for process temperatures, equipment control and testing, worker safety, laboratory testing, and interstate dairy compliance.
- **S5** — [U.S. Census Bureau: Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding owners of U.S. employer businesses were age 55 or older in the 2019 ABS covering data year 2018.
- **S6** — [US per capita butter consumption reaches all-time high](https://www.dairyprocessing.com/articles/3768-us-per-capita-butter-consumption-reaches-all-time-high) (accessed 2026-07-22): Reports USDA-derived U.S. per-capita butter consumption of 6.8 pounds in 2024 versus 6.5 pounds in 2023 and 21% growth over the prior decade.
- **S7** — [USDA ERS Dairy Data Documentation](https://www.ers.usda.gov/data-products/dairy-data/documentation) (accessed 2026-07-22): Explains that dairy per-capita consumption estimates cover butter and generally use domestic disappearance divided by population, without full accounting for spoilage and waste.
