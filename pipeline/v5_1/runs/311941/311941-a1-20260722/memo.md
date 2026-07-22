# 311941 — Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing

*v5.1 Stage 1 research memo. Run `311941-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.74 · L 0.27 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical food demand preserves the need for an accountable contract manufacturer while AI improves planning, documentation, quality support, and capacity utilization.
**Weakness:** The eligible contract-manufacturing share and achievable labor substitution are both inferred from broad proxies rather than measured directly for LMM sauce plants.

## Business-model lens
- Included: Lower-middle-market U.S. manufacturers that repeatedly produce mayonnaise, dressings, vinegar, mustard, soy sauce, and other non-tomato prepared sauces for external brand, retailer, distributor, or foodservice customers under private-label, contract-manufacturing, or custom-product relationships.
- Excluded: Own-brand-only product companies without a recurring outsourced-production relationship, captive plants, tomato-based sauce and gravy manufacturers, shell entities, and non-control financing vehicles.
- Customer and revenue model: Recurring business-to-business sales of manufactured sauces, generally by purchase order or supply contract, with revenue tied to unit volumes and negotiated product specifications; some contracts contain commodity-cost pass-through or periodic repricing mechanisms.
- Deviation from default lens: none

## Executive view
The coherent opportunity is contract, private-label, and customized sauce production rather than branded packaged-food ownership. Demand is likely durable and the accountable manufacturing role is hard to eliminate, but most labor is physical and regulated, so implementable AI savings are concentrated in supporting workflows rather than wholesale plant labor replacement.

## How AI changes the work
AI can compress forecasting, production scheduling, specification and certificate review, customer-service drafting, procurement analysis, quality-document review, maintenance triage, and some vision-assisted inspection. Batch operation, sanitation, material handling, packaging intervention, sensory judgment, preventive-control verification, and corrective action remain equipment- and human-intensive.

## Value capture
Savings can be retained during fixed-price periods and converted into capacity, service, or margin, but large brands and retailers buy competitively and often have termination or repricing leverage. Commodity pass-through clauses separate input volatility from labor productivity, yet renewals and rebids will still share gains with customers.

## Firm availability
Co-manufacturing is material in food, but only part of this NAICS population qualifies because many manufacturers primarily sell their own brands. Owner aging and an active small-manufacturing sale market support transfer supply, although asset intensity, customer concentration, compliance history, and founder dependence can prevent a completed control sale.

## Demand durability
Sauces and condiments are recurring complements across at-home and away-from-home eating. Broad real foodservice growth and low expenditure sensitivity support roughly stable-to-modestly-growing five-year quantity, while changes in diet, restaurant traffic, SKU rationalization, and customer insourcing create downside.

## Risks and uncertainty
The largest evidence gaps are the six-digit wage-weighted task mix, the share of LMM firms with true outsourced-service revenue, and target-level contract economics. AI projects may augment rather than eliminate jobs, older equipment and fragmented data can delay deployment, and food-safety or allergen failures can overwhelm expected savings. Concentrated customers may reprice gains or move volume.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1132 | — | OBSERVED | — |
| n | — | 56 | — | ESTIMATE | — |
| a | 0.09 | 0.15 | 0.24 | PROXY | S2, S3, S4 |
| rho | 0.22 | 0.4 | 0.6 | PROXY | S4, S5 |
| e | 0.22 | 0.38 | 0.55 | PROXY | S1, S6 |
| s5 | 0.1 | 0.2 | 0.32 | PROXY | S7, S8 |
| q | 0.38 | 0.58 | 0.75 | PROXY | S9 |
| d5 | 0.97 | 1.04 | 1.1 | PROXY | S10, S11, S12 |
| o | 0.95 | 0.98 | 1 | ESTIMATE | S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.09 | 0.27 | 0.65 | PROXY |
| F | 1.29 | 2.67 | 3.84 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | PROXY |
| D | 9.21 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No public six-digit occupation-by-wage table was located; the occupation mix is for all food manufacturing.
- a: The estimate excludes already-automated tasks but public sources do not identify the current automation baseline for sauce plants.
- a: Industrial AI and conventional automation overlap, making attribution to AI substitution uncertain.
- rho: BTOS adoption is economy-wide and includes light uses such as writing; it does not measure the fraction of exposed wage work implemented.
- rho: Manufacturing research combines multiple industrial AI technologies and subsectors.
- rho: FDA obligations do not prohibit automation, but they raise validation, documentation, and human-accountability requirements.
- e: No source directly measures the eligible firm share in NAICS 311941.
- e: The buyer-side outsourcing share is sales-weighted and spans product categories beyond sauces.
- e: Private-label manufacturing is treated as a recurring outsourced service only where an external customer specifies or owns the market proposition.
- s5: Owner-age evidence is old, broad, and limited to linked single-unit firms.
- s5: BizBuySell is a reported marketplace sample and its other-manufacturing category is much broader than 311941.
- s5: The estimate excludes internal reorganizations and deaths that do not result in a transferable operating-company sale.
- q: The SEC filing is an adjacent diversified food-and-beverage manufacturer, not a representative sample of private sauce companies.
- q: Retention varies sharply between custom formulations with switching costs and commodity private-label bids.
- q: The estimate isolates contractual and competitive pass-through and does not include volume loss or implementation failure.
- d5: The USDA foodservice series is broader than sauces and measures real spending rather than constant-quality physical output.
- d5: The sauce elasticity estimate is based on older household data and does not cover business-to-business procurement directly.
- d5: The estimate holds the current service basket and quality constant and therefore excludes premiumization.
- o: There is no direct measure of operator-required quantity for this industry.
- o: The accountable operator could be a different manufacturer after rebidding; this primitive concerns persistence of the operator role, not incumbent retention.
- o: Future autonomous equipment may reduce staffing substantially without eliminating the manufacturing operator entity.

## Sources
- **S1** — [North American Industry Classification System: 311941 Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing](https://www.census.gov/naics/?details=311&input=311&year=2022) (accessed 2026-07-23): Defines 311941 as manufacturing mayonnaise, salad dressing, vinegar, mustard, horseradish, soy sauce, tartar sauce, Worcestershire sauce, and other prepared sauces except tomato-based sauces and gravy.
- **S2** — [Food Manufacturing: NAICS 311](https://www.bls.gov/iag/tgs/iag311.htm) (accessed 2026-07-23): Shows broader food-manufacturing employment of about 1.78 million versus about 1.40 million production and nonsupervisory employees in spring 2026, and common 2025 occupations including 144,690 food batchmakers and 168,370 packaging and filling machine operators.
- **S3** — [Generative AI and Jobs: A Refined Global Index of Occupational Exposure](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) (accessed 2026-07-23): Task-level 2025 ILO research finds clerical occupations remain the most exposed and job transformation is more likely than full replacement for most occupations.
- **S4** — [The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html) (accessed 2026-07-23): Reports 18% firm AI use and 32% employment-weighted use in late 2025/early 2026, limited functional breadth among most adopters, augmentation-only use by 66% of users, and AI-related employment decreases at only 2% of firms.
- **S5** — [FSMA Final Rule for Preventive Controls for Human Food](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food) (accessed 2026-07-23): Documents requirements for written food-safety plans, hazard analysis, process, allergen and sanitation controls, monitoring, corrective actions, verification, supply-chain programs, and recall plans.
- **S6** — [The Hain Celestial Group, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/910406/000119312525203534/hain-20250630.htm) (accessed 2026-07-23): Reports that independent contract manufacturers produced products representing approximately 36% of fiscal-2025 sales and states that competent high-quality co-manufacturers are limited and may supply all requirements for a brand.
- **S7** — [A Comparison of Firm Age in the Survey of Business Owners and the Longitudinal Business Database](https://www2.census.gov/ces/tn/CES-TN-2020-08.pdf) (accessed 2026-07-23): Reports primary-owner age distributions for linked single-unit employer firms, including 49.55% above age 54 in the 2007 Survey of Business Owners sample.
- **S8** — [Business Acquisitions Favor Value Over Volume as Buyer Competition Intensifies](https://www.bizbuysell.com/news/bizbuysell-2026-first-quarter-insight-report/) (accessed 2026-07-23): Reports 83 closed other-manufacturing transactions in BizBuySell's full-year 2025 sector table and describes changing manufacturing acquisition volumes, demonstrating observable but selective small-business transfer activity.
- **S9** — [SunOpta Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/351834/000106299326001270/form10k.htm) (accessed 2026-07-23): Describes private-label and co-manufacturing competition on quality, reliability, innovation and price; customer relationships through terminable purchase orders or contracts; customer concentration; and pass-through pricing clauses where possible.
- **S10** — [Food Service Industry: Market Segments](https://ers.usda.gov/topics/food-markets-prices/food-service-industry/market-segments) (accessed 2026-07-23): Reports inflation-adjusted foodservice sales of $1.41 trillion in 2025 versus $818 billion in 1997 and that food-away-from-home represented 56.3% of nominal food expenditure in 2025.
- **S11** — [The Demand for Disaggregated Food-Away-from-Home and Food-at-Home Products in the United States](https://ers.usda.gov/sites/default/files/_laserfiche/publications/45003/30438_err139.pdf) (accessed 2026-07-23): Estimates an unconditional expenditure elasticity of 0.07 and own-price elasticity of -1.92 for condiments, sauces, and seasonings in the report's household-demand model.
- **S12** — [U.S. Population Growth Slows Due to Historic Decline in Net International Migration](https://www.census.gov/newsroom/press-releases/2026/population-growth-slows.html) (accessed 2026-07-23): Reports U.S. population growth of 1.8 million, or 0.5%, from July 2024 to July 2025, supporting a modest demographic tailwind rather than rapid category-volume growth.
