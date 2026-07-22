# 311421 — Fruit and Vegetable Canning

*v5.1 Stage 1 research memo. Run `311421-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.56 · L 0.59 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Regulated, recurring physical production makes the surviving co-manufacturing relationship operationally sticky and operator-required.
**Weakness:** Only a minority of the NAICS population fits the outsourced-service lens, and core canned-product demand is under secular substitution pressure.

## Business-model lens
- Included: U.S. lower-middle-market contract manufacturers and co-packers whose recurring customer work is the canning, pickling, brining, retort processing, filling, labeling, and related quality-control of fruit- and vegetable-based products.
- Excluded: Branded manufacturers that only sell their own goods, captive plants, distributors, brokers, non-control financing vehicles, and establishments whose primary activity falls outside NAICS 311421.
- Customer and revenue model: Brand owners, retailers, foodservice companies, and other food businesses purchase recurring production runs under private-label or co-manufacturing arrangements, usually priced per case, unit, or run with customer specifications and volume commitments.
- Deviation from default lens: none

## Executive view
The relevant opportunity is a minority of 311421 firms that repeatedly manufacture private-label or customer-formulated canned, pickled, brined, and sauce products. AI can improve planning, quality records, inspection triage, maintenance, inventory, and customer administration, but the industry's labor base is dominated by physical production and material movement. Demand faces a long-run shift toward fresh alternatives, while regulatory accountability makes the surviving service difficult to replace with software alone.

## How AI changes the work
Near-term AI value is primarily decision support and workflow compression around production scheduling, procurement, demand forecasting, quality documentation, deviation investigation, customer service, and machine-vision review. Direct substitution on retort, filling, sanitation, maintenance, and material-handling work is limited unless paired with capital-intensive physical automation, which is outside the pure AI effect.

## Value capture
Savings can remain with the operator during fixed-price contract periods and through better yield, uptime, fewer errors, and improved service. Retention erodes at rebids and renewals when sophisticated brand owners or retailers demand productivity sharing, especially under open-book or cost-plus arrangements. High customer concentration would make capture weaker.

## Firm availability
Most firms in the NAICS code are product manufacturers rather than outsourced-service providers, so eligibility is the first major filter. Transfer evidence is cross-industry, but employer-owner intentions and active food-processing deal flow suggest that control transfers occur often enough to warrant direct market mapping.

## Demand durability
Canned and processed fruit and vegetable categories face substitution toward fresh and other formats, producing a likely modest five-year decline in the current basket. Yet shelf stability, affordability, foodservice use, sauces, pickled products, and private label preserve a substantial base. Any surviving volume still requires a compliant physical processor.

## Risks and uncertainty
The largest uncertainties are the true share of contract-manufacturing firms inside 311421, customer-contract economics, product mix, and the lack of task-level labor studies for smaller canners. Food-safety failures, recalls, raw-material volatility, steel/container cost, seasonal capacity, retailer concentration, and customer insourcing can overwhelm administrative productivity gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1346 | — | OBSERVED | — |
| n | — | 118 | — | ESTIMATE | — |
| a | 0.13 | 0.22 | 0.32 | PROXY | S2, S3 |
| rho | 0.3 | 0.5 | 0.68 | PROXY | S3, S4, S5 |
| e | 0.08 | 0.2 | 0.35 | ESTIMATE | S1, S6 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S7, S8 |
| q | 0.35 | 0.55 | 0.72 | ESTIMATE | S6 |
| d5 | 0.78 | 0.9 | 1.02 | PROXY | S9, S10 |
| o | 0.9 | 0.97 | 1 | PROXY | S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.59 | 1.17 | PROXY |
| F | 1.22 | 2.93 | 4.36 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.02 | 8.73 | 10.00 | PROXY |

## Caveats
- a: OEWS is for NAICS 311400 rather than 311421 and covers employers of all sizes.
- a: The estimate concerns current not-yet-automated tasks; installed physical automation and conventional control systems are not counted as new AI opportunity.
- rho: Smart manufacturing includes non-AI technologies, so reported outcomes do not isolate AI.
- rho: FDA requirements constrain implementation but do not prohibit decision support or administrative automation.
- e: No census source identifies contract-manufacturing revenue within 311421.
- e: The provided firm count is an EBITDA-band estimate and may include branded manufacturers or firms with mixed NAICS activities.
- s5: Owner plans are not completed transfers and the Gallup sample is cross-industry.
- s5: Published food M&A counts skew toward reportable and larger transactions.
- q: Contract structures and customer concentration vary widely by product and customer.
- q: No public source measures five-year retained AI benefit for 311421 co-packers.
- d5: Processing vegetables include frozen products outside 311421.
- d5: Aggregate per-capita series obscure population growth and divergent product trends.
- o: Regulation proves accountability requirements, not continued use of independent co-packers.
- o: Demand eliminated by product-format substitution is accounted for in d5, not again here.

## Sources
- **S1** — [North American Industry Classification System: 311421 Fruit and Vegetable Canning](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines 311421 as establishments manufacturing canned, pickled, and brined fruits and vegetables and lists representative products and exclusions.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311400](https://www.bls.gov/oes/2023/may/naics4_311400.htm) (accessed 2026-07-22): Reports employment and wages by occupation for the broader preserving and specialty-food sector, including 50.95% production, 17.08% transportation/material moving, 9.18% maintenance, and 5.73% office-support employment shares.
- **S3** — [2025 Smart Manufacturing and Operations Survey](https://www.deloitte.com/us/en/insights/industry/manufacturing-industrial-products/2025-smart-manufacturing-survey.html) (accessed 2026-07-22): Reports a 600-respondent manufacturing survey, including 7%-20% employee-productivity improvement, 10%-20% output improvement, and 46% ranking process automation as a top-two investment priority.
- **S4** — [Acidified and Low-Acid Canned Foods Guidance Documents and Regulatory Information](https://www.fda.gov/food/guidance-documents-regulatory-information-topic-food-and-dietary-supplements/acidified-low-acid-canned-foods-guidance-documents-regulatory-information) (accessed 2026-07-22): States that commercial processors of shelf-stable acidified and low-acid canned foods must register establishments and file scheduled processes for each product, style, container, and method.
- **S5** — [FSMA Final Rule for Preventive Controls for Human Food](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food) (accessed 2026-07-22): Describes risk-based preventive-control, training, oversight, and management requirements for covered food facilities.
- **S6** — [Contract Manufacturing of Food Products](https://www.foodresearchlab.com/what-we-do/pilot-contract-manufacturing/food-manufacturing/) (accessed 2026-07-22): Explains the co-packing/private-label relationship, customer recipe and specification transfer, recurring manufacturing steps, quality control, labeling, and regulatory compliance.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of employer-business owners planned to sell or transfer ownership in the next five years, based on a fall 2024 survey of 1,264 U.S. business owners.
- **S8** — [Food Production Mergers and Acquisitions Update](https://www.capstonepartners.com/insights/article-food-production-mergers-acquisitions-update/) (accessed 2026-07-22): Reports 144 food-production transactions in 2024 and an increase in food-processing deals from 20 in 2023 to 52 in 2024.
- **S9** — [Vegetable Availability Declined in 2024](https://www.ers.usda.gov/data-products/charts-of-note/112836) (accessed 2026-07-22): Reports U.S. vegetable and pulse availability of 376 pounds per person in 2024 and a 32-pound decline in processing vegetables since 1996.
- **S10** — [Pineapple Availability Pivots from Processed to Fresh](https://www.ers.usda.gov/data-products/charts-of-note/113353) (accessed 2026-07-22): Reports fresh pineapple rising from about 17% of availability in 1995-97 to two-thirds in 2024, evidencing substitution away from canned and juice forms.
