# 325998 — All Other Miscellaneous Chemical Product and Preparation Manufacturing

*v5.1 Stage 1 research memo. Run `325998-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.90 · L 0.84 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring consumable chemistry across many physical end markets supports repeat demand and selective AI-enabled workflow improvement.
**Weakness:** A residual NAICS category this heterogeneous can hide low-quality, regulated, commoditized, or non-transferable businesses behind attractive aggregate data.

## Business-model lens
- Included: US LMM manufacturers that repeatedly formulate, blend, activate, package, or custom-produce miscellaneous chemical preparations for external customers, including activated carbon, water-treatment compounds, industrial process aids, lubricants and maintenance chemicals, and other recurring specialty formulations captured by 325998.
- Excluded: Captive internal plants, one-off R&D without repeat production, pure distribution, commodity resale without preparation, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat B2B or channel sales of consumable formulations and materials, often supported by technical service, qualification, application know-how, private-label arrangements, or recurring custom production; some branded maintenance products also sell through distribution.
- Deviation from default lens: none

## Executive view
This residual specialty-chemical category offers a broad pool of repeat consumables businesses, but its heterogeneity is the central underwriting problem. AI can improve commercial, planning, quality, regulatory, and maintenance workflows; it is less likely to replace batch operation, material handling, packaging, and accountable release work.

## How AI changes the work
Near-term use cases include order and demand forecasting, formulation and specification retrieval, SDS and regulatory-document assistance, batch-record review, quality anomaly detection, machine vision, predictive maintenance, purchasing, and customer-support triage. Legacy controls, sparse labeled data, plant safety, validation, and fragmented product lines limit five-year implementation.

## Value capture
Differentiated performance, customer qualification, proprietary know-how, brands, and technical service support retention. Tolling, open-book contracts, commodity bids, powerful buyers, and frequent rebids share benefits, making contract structure more important than the label 'specialty chemical.'

## Firm availability
The injected population of 373 estimated LMM firms is substantial, and many should sell repeat consumables externally. Eligibility and transferability still require firm-level work because the residual NAICS category can include distribution, one-off projects, owner-dependent formulations, captive production, contaminated sites, and businesses with severe customer concentration.

## Demand durability
The basket benefits from physical-world maintenance, water and air purification, environmental remediation, infrastructure, and industrial production. Activated carbon and maintenance products show favorable demand signals, while paving cycles, weather, industrial activity, product regulation, electrification, and formulation bans create dispersion and periodic contraction.

## Risks and uncertainty
The largest risks are product-mix opacity, environmental liabilities, raw-material volatility, regulatory bans or reformulation, customer qualification loss, end-market cyclicality, and the possibility that apparent manufacturers are mainly distributors. Public evidence comes from larger selected companies and broad chemical occupations rather than the LMM lens.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1443 | — | OBSERVED | — |
| n | — | 373 | — | ESTIMATE | — |
| a | 0.16 | 0.27 | 0.39 | PROXY | S2, S3, S4 |
| rho | 0.36 | 0.54 | 0.7 | ESTIMATE | S4 |
| e | 0.61 | 0.76 | 0.87 | ESTIMATE | S1, S5, S7 |
| s5 | 0.14 | 0.23 | 0.34 | PROXY | S6 |
| q | 0.46 | 0.64 | 0.79 | ESTIMATE | S5, S7 |
| d5 | 0.94 | 1.08 | 1.24 | PROXY | S1, S5, S7, S8 |
| o | 0.89 | 0.96 | 0.99 | ESTIMATE | S1, S5, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.84 | 1.58 | ESTIMATE |
| F | 5.62 | 6.74 | 7.58 | ESTIMATE |
| C | 9.20 | 10.00 | 10.00 | ESTIMATE |
| D | 8.37 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation evidence is three-digit NAICS 325 and not wage-weighted to 325998.
- a: The code is a residual category spanning products with very different labor and automation intensity.
- a: LLM task exposure is not the same as substitution and may include tasks already automated.
- rho: DOE evidence covers chemical and thermal processing broadly rather than the 325998 residual category.
- rho: Implementation will differ sharply between simple blending and highly engineered activated-carbon or specialty-chemical production.
- e: No source measures lens eligibility within the injected LMM population.
- e: The broad residual NAICS definition makes database classification errors and mixed revenue models likely.
- e: The injected firm count is an estimate derived from size-class receipts and an industry margin bridge.
- s5: Gallup is cross-industry and includes employers far below the LMM EBITDA band.
- s5: Owner plans may include gifts, internal family transfers, or public offerings that do not meet the qualifying-control definition.
- s5: Public-company portfolio divestitures illustrate transfer activity but do not measure LMM probability.
- q: The public-company sources have scale and brands that many LMM firms lack.
- q: Retention differs materially among activated carbon, custom process aids, toll blends, commodity preparations, and branded maintenance chemicals.
- q: Demand and implementation effects are excluded here.
- d5: Public-company sales mix includes activities that may sit outside 325998 and includes price and geographic effects.
- d5: The residual category can change mix even if aggregate shipments grow.
- d5: Environmental rules can increase treatment demand while simultaneously eliminating particular chemical formulations.
- o: The value is conditional on demand remaining in d5, so banned or eliminated products are not counted twice.
- o: Simple blends are more vulnerable to customer insourcing than engineered activated carbon or qualified performance chemicals.

## Sources
- **S1** — [U.S. Census Bureau NAICS 325998 industry definition](https://www2.census.gov/econ2012/Reference_materials/htm%20files/32599n.htm) (accessed 2026-07-22): Defines the residual miscellaneous chemical product and preparation manufacturing industry and distinguishes it from other named chemical-manufacturing categories.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 325 Chemical Manufacturing](https://www.bls.gov/oes/2023/may/naics3_325000.htm) (accessed 2026-07-22): Reports production occupations at 39.02% of chemical employment, including chemical-equipment operators at 12.28%, packaging/filling operators at 6.43%, mixing/blending operators at 3.57%, and inspectors/testers at 3.33%.
- **S3** — [GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models](https://arxiv.org/abs/2303.10130) (accessed 2026-07-22): Finds about 15% of US tasks could be completed significantly faster with an LLM alone and 47%-56% with complementary software, without predicting adoption timing.
- **S4** — [DOE Advanced Manufacturing Office: Thermal Process Intensification Workshop Report](https://www.energy.gov/sites/default/files/2022-05/TPI%20Workshop%20Report_AMO.pdf) (accessed 2026-07-22): Describes AI and sensors for industrial process control and chemical-manufacturing implementation barriers including application specificity, complex data acquisition, capital intensity, testing, scale-up, disruption, and regulation.
- **S5** — [Arq, Inc. 2024 Annual Report on Form 10-K](https://www.sec.gov/Archives/edgar/data/1515156/000151515625000014/arq-20241231.htm) (accessed 2026-07-22): Describes activated carbon as a consumable across water, gas, emissions, remediation, food, and industrial markets, with environmental regulation and PFAS treatment as demand drivers.
- **S6** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 52.3% of US employer businesses are owned by people age 55 or older and 22% of employer owners planned a sale or transfer within five years.
- **S7** — [WD-40 Company Fiscal Year 2025 Results](https://investor.wd40company.com/investors/press-releases/news-details/2025/WD-40-Company-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results/default.aspx) (accessed 2026-07-22): Reports maintenance-product sales of $590.966 million in fiscal 2025, up 6%, total net sales of $619.985 million, and full-year gross margin of 55.1%.
- **S8** — [Ingevity Corporation 2024 Annual Report on Form 10-K](https://www.sec.gov/Archives/edgar/data/1653477/000165347725000015/ngvt-20241231.htm) (accessed 2026-07-22): Describes critical-input uses in roads, lubricants, adhesives, rubber, agrochemicals, water and chemical purification, application expertise, automotive emissions requirements, and weather-sensitive paving demand.
