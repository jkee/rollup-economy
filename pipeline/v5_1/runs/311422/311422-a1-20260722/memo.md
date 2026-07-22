# 311422 — Specialty Canning

*v5.1 Stage 1 research memo. Run `311422-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.46 · L 0.59 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Customer-specific formulations and regulated physical production create recurring, operator-required co-manufacturing relationships.
**Weakness:** The eligible universe is small and heterogeneous, while powerful customers can reclaim visible productivity savings.

## Business-model lens
- Included: U.S. lower-middle-market specialty-food co-manufacturers and private-label producers providing recurring retort, canning, filling, recipe scale-up, packaging, and quality-assurance services for soups, baked and prepared beans, canned pasta and nationality foods, baby food, and similar shelf-stable products.
- Excluded: Manufacturers selling only their own brands, captive production units, brokers and distributors without production responsibility, non-control financing vehicles, and facilities primarily producing fresh, frozen, seafood, meat, or fruit-and-vegetable products classified elsewhere.
- Customer and revenue model: Retailers, foodservice operators, restaurant chains, and consumer-food brands contract for repeated production runs under customer recipes or jointly developed specifications, generally paying per case, unit, batch, or committed volume.
- Deviation from default lens: none

## Executive view
The relevant segment is the subset of specialty canners that repeatedly produce customer-specified shelf-stable foods for retailers, foodservice operators, and brands. AI opportunity sits mainly in planning, documentation, quality workflows, forecasting, maintenance, and customer administration; direct plant labor is still largely physical. Basket demand appears stable but mixed, and the regulated physical process keeps the operator central.

## How AI changes the work
AI can compress production scheduling, ingredient and packaging procurement, specification comparison, quality-record preparation, deviation investigation, customer service, forecasting, and maintenance analysis. Machine vision can assist inspection. Retort operation, sanitation, handling, cooking, filling, sealing, and exception response remain embodied tasks and require validated controls.

## Value capture
Operators can initially retain savings under fixed per-case or batch contracts and can defend gains tied to yield, service levels, faster development, fewer deviations, and capacity. Sophisticated retailer and CPG customers will seek givebacks during rebids or through open-book costing, limiting five-year retention.

## Firm availability
Private-label and co-manufacturing are established in specialty categories, but branded-only producers remain outside the lens. Cross-industry owner plans and active food-processing M&A imply transfers are plausible, while the small dataset-estimated LMM population makes actual target mapping essential.

## Demand durability
Soup and broth benefit from at-home eating and affordability, beans remain staple products, and private label can gain in value-seeking periods. Baby-food demand is constrained by low fertility, and prepared foods face fresh, frozen, pouch, and restaurant alternatives. Overall constant-quality quantity is likely roughly flat over five years.

## Risks and uncertainty
The main unknowns are eligible-firm prevalence, customer concentration, contract repricing, and product mix. Recalls, allergens, process deviations, raw-material and packaging inflation, seasonal capacity, retailer bargaining, customer insourcing, and format shifts can outweigh administrative productivity gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1273 | — | OBSERVED | — |
| n | — | 27 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.33 | PROXY | S2, S3, S6 |
| rho | 0.3 | 0.5 | 0.68 | PROXY | S3, S4, S5 |
| e | 0.15 | 0.3 | 0.48 | ESTIMATE | S1, S6, S7 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S8, S9 |
| q | 0.34 | 0.54 | 0.72 | ESTIMATE | S6, S7 |
| d5 | 0.9 | 0.99 | 1.08 | PROXY | S10, S11 |
| o | 0.91 | 0.97 | 1 | PROXY | S4, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.59 | 1.14 | PROXY |
| F | 0.64 | 1.65 | 2.71 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 8.19 | 9.60 | 10.00 | PROXY |

## Caveats
- a: The occupation source is four-digit NAICS and includes fruit, vegetable, frozen-food, and other preserving activities.
- a: AI-enabled physical automation is included only where it substitutes current labor; conventional capital automation is not treated as AI exposure.
- rho: Survey outcomes are self-reported and cross-industry.
- rho: Required accountability limits full substitution but still permits substantial decision support and administrative automation.
- e: Public directories and company marketing pages demonstrate the model but do not provide an industry denominator.
- e: The frozen firm count is an EBITDA-band estimate and may include mixed-industry operations.
- s5: Owner intentions are not realized control transfers.
- s5: Published food-processing deal counts skew toward larger and disclosed transactions.
- q: Contract economics vary materially between retailer private label, foodservice, and emerging-brand customers.
- q: No source directly measures five-year retained AI benefit in specialty canning.
- d5: Campbell data are company-specific and sales growth is not pure quantity growth.
- d5: Birth counts affect only baby food, and pouches or other formats may cross NAICS boundaries.
- o: Regulatory accountability does not guarantee that the same independent operator remains the supplier.
- o: Customer insourcing is operator displacement and should be measured separately from product-demand decline.

## Sources
- **S1** — [North American Industry Classification System: 311422 Specialty Canning](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines 311422 as canned specialty-food manufacturing and identifies baby food, baked beans, soups, spaghetti, and nationality foods as examples.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311400](https://www.bls.gov/oes/2023/may/naics4_311400.htm) (accessed 2026-07-22): Reports the broader sector's occupation mix, including 50.95% production, 17.08% transportation/material moving, 9.18% maintenance, and 5.73% office-support employment.
- **S3** — [2025 Smart Manufacturing and Operations Survey](https://www.deloitte.com/us/en/insights/industry/manufacturing-industrial-products/2025-smart-manufacturing-survey.html) (accessed 2026-07-22): A 600-respondent survey reporting 7%-20% employee-productivity improvement, 10%-15% unlocked capacity, and process automation as a top-two priority for 46% of manufacturers.
- **S4** — [Acidified and Low-Acid Canned Foods Guidance Documents and Regulatory Information](https://www.fda.gov/food/guidance-documents-regulatory-information-topic-food-and-dietary-supplements/acidified-low-acid-canned-foods-guidance-documents-regulatory-information) (accessed 2026-07-22): States that commercial processors of covered shelf-stable canned foods must register establishments and file scheduled processes by product, style, container, and method.
- **S5** — [FSMA Final Rule for Preventive Controls for Human Food](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food) (accessed 2026-07-22): Describes risk-based preventive controls, training, oversight, and management duties for covered human-food facilities.
- **S6** — [Contract Manufacturing of Food Products](https://www.foodresearchlab.com/what-we-do/pilot-contract-manufacturing/food-manufacturing/) (accessed 2026-07-22): Explains co-packing/private-label relationships, recipe transfer, quality control, retort processing, manufacturing, packaging, labeling, and regulatory compliance.
- **S7** — [Faribault Foods Organic and Co-Manufacturing Capabilities](https://www.faribaultfoods.com/organics/) (accessed 2026-07-22): Documents shelf-stable beans, pasta, and soup production across own brands, retailer private labels, and co-manufacturing partners, including more than 200 organic items.
- **S8** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of employer-business owners planned to sell or transfer ownership within five years in a fall 2024 survey of 1,264 U.S. owners.
- **S9** — [Food Production Mergers and Acquisitions Update](https://www.capstonepartners.com/insights/article-food-production-mergers-acquisitions-update/) (accessed 2026-07-22): Reports 144 food-production transactions in 2024 and a rise in food-processing deals from 20 in 2023 to 52 in 2024.
- **S10** — [Campbell's Co. Says Sales Rise as More Americans Cook Meals at Home](https://apnews.com/article/campbells-soup-broth-economy-6b5428b380b87f44e32dff07b4f9c4d9) (accessed 2026-07-22): Reports stronger broth and condensed-soup sales, including a 15% quarterly increase in broth sales, amid elevated at-home cooking in 2025.
- **S11** — [Births: Provisional Data for 2024](https://www.cdc.gov/nchs/data/vsrr/vsrr038.pdf) (accessed 2026-07-22): Reports 3,622,673 U.S. births in 2024, up 1% from 2023, and a total fertility rate still below replacement.
