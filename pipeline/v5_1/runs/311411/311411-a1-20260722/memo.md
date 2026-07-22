# 311411 — Frozen Fruit, Juice, and Vegetable Manufacturing

*v5.1 Stage 1 research memo. Run `311411-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.35 · L 0.30 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Physical freezing and cold-chain services remain necessary for recurring retail, foodservice, private-label, and ingredient demand.
**Weakness:** Commodity-like bidding and excess capacity limit retained value while long-run processing-vegetable availability is declining.

## Business-model lens
- Included: US lower-middle-market processors that manufacture frozen fruits, frozen vegetables, and frozen fruit juices, drinks, cocktail mixes, or concentrates for repeat retail, foodservice, distributor, industrial-ingredient, and private-label customers.
- Excluded: Frozen prepared meals and specialty foods, seafood, frozen bakery or dairy products, fresh-only produce handlers, captive internal plants, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat physical-product sales by pound, case, shipment, contract pack, or seasonal program, commonly through private-label, branded, foodservice, industrial ingredient, and distributor channels.
- Deviation from default lens: none

## Executive view
Frozen fruit, juice, and vegetable manufacturing offers repeat, operator-required demand and a meaningful estimated LMM population, but the labor base is largely physical and commercial retention is constrained by commodity inputs, private-label bidding, and excess capacity. Structural demand evidence is softer than convenience-oriented category narratives suggest.

## How AI changes the work
AI is most relevant to crop and demand forecasting, production scheduling, vision-inspection triage, yield analysis, maintenance prioritization, cold-chain alerts, traceability documents, and administration. Receiving, washing, cutting, blanching, freezing, sanitation, packaging interventions, refrigeration maintenance, and warehouse movement remain physical.

## Value capture
Per-case and per-pound pricing lets a processor retain benefits initially, but annual customer bids, retailer and foodservice leverage, transparent crop and freight costs, and available capacity share savings. Specialized formats, dependable seasonal capacity, sourcing relationships, and quality performance support better retention.

## Firm availability
Most firms in the code are operating manufacturers and should fit the recurring-customer lens, subject to captive status, ownership structure, concentration, certification, and normalized seasonal economics. Aging manufacturing ownership creates potential transfer supply, but asset intensity and working-capital needs reduce completion.

## Demand durability
Freezing remains necessary for year-round availability and low-spoilage distribution, yet USDA data show a long decline in processing-vegetable availability. Recent trade volumes are mixed-to-positive, so a modest real quantity decline is more defensible than either collapse or strong growth.

## Risks and uncertainty
Major risks are crop and weather volatility, power and refrigeration costs, food-safety incidents, environmental compliance, import competition, labor seasonality, customer and grower concentration, and low capacity utilization. Evidence is weak on six-digit tasks, private contracts, deal completion, and separate fruit, juice, and vegetable demand.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1152 | — | OBSERVED | — |
| n | — | 46 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S2, S3, S4 |
| rho | 0.2 | 0.36 | 0.52 | PROXY | S5, S6 |
| e | 0.62 | 0.78 | 0.9 | ESTIMATE | S1 |
| s5 | 0.07 | 0.13 | 0.2 | PROXY | S7, S8, S9 |
| q | 0.25 | 0.45 | 0.67 | PROXY | S10 |
| d5 | 0.82 | 0.95 | 1.06 | PROXY | S11, S12 |
| o | 0.93 | 0.98 | 1 | ESTIMATE | S1, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.09 | 0.30 | 0.67 | PROXY |
| F | 1.77 | 2.79 | 3.58 | ESTIMATE |
| C | 5.00 | 9.00 | 10.00 | PROXY |
| D | 7.63 | 9.31 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is for all food manufacturing, not 311411.
- a: Advanced-technology exposure includes robots, dedicated equipment, cloud systems, and non-AI software.
- rho: Census AI definitions and reference periods changed.
- rho: Adoption rates do not measure captured labor opportunity and may be dominated by low-risk office uses.
- e: No source directly measures eligibility among the frozen 46-firm estimate.
- e: The common food-processing margin bridge may misclassify capital-intensive or volatile seasonal processors.
- s5: Owner-intention and age evidence does not isolate NAICS 311411.
- s5: Public-company product-line divestitures are not representative of LMM whole-company transfers.
- q: Seneca's frozen vegetables were only 8% of its fiscal 2025 food-packaging sales.
- q: Competition disclosures do not directly quantify pass-through of AI savings.
- d5: Availability is a supply-disappearance proxy, not consumption or manufacturer demand.
- d5: The NAICS includes fruit, juice, and vegetables, while the strongest evidence is vegetable-focused.
- o: Industry consolidation can remove demand from LMM operators without eliminating the processing function.
- o: Imports may shift the accountable operator outside the US and are only indirectly reflected in d5.

## Sources
- **S1** — [311411: Frozen Fruit, Juice, and Vegetable Manufacturing - Census Bureau Profile](https://data.census.gov/profile/311411_-_Frozen_Fruit%2C_Juice%2C_and_Vegetable_Manufacturing?codeset=naics~311411) (accessed 2026-07-22): Official industry definition and 218 employer establishments in 2023.
- **S2** — [Food Manufacturing: NAICS 311](https://www.bls.gov/iag/tgs/iag311.htm) (accessed 2026-07-22): Broader food-manufacturing employment and occupation mix, including production, batchmaking, packaging, and supervisory roles.
- **S3** — [Food Processing Equipment Workers](https://www.bls.gov/ooh/production/food-and-tobacco-processing-workers.htm) (accessed 2026-07-22): Physical production duties, machine tending, cleaning and lifting requirements, and use of automatic weighing and mixing equipment.
- **S4** — [Three Results From Recent Research on Advanced Technology Use and Automation](https://www.census.gov/newsroom/blogs/research-matters/2023/09/advanced-technology-use-and-automation-results.html) (accessed 2026-07-22): Manufacturing workers' 52% upper-bound exposure to advanced automating technologies versus 28% outside manufacturing.
- **S5** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS AI use of 17-20% overall in late 2025 through May 2026, expected use of 20-23%, and higher adoption at larger firms.
- **S6** — [Census Bureau's 2023 Annual Business Survey Provides Insight into Technology Adoption by Businesses](https://www.census.gov/library/stories/2025/09/technology-impact.html) (accessed 2026-07-22): Most adopters reported no overall workforce-number change and frequently experienced workflow or skill effects.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year sale or transfer plans reported by 17% of owners age 55 or older and 10% of younger owners in fall 2024.
- **S8** — [Employee Ownership for Manufacturers](https://project-equity.org/publication/employee-ownership-for-manufacturing/) (accessed 2026-07-22): Reports 60% of small and midsize manufacturers have owners at or near retirement age.
- **S9** — [B&G Foods Business Update](https://www.sec.gov/Archives/edgar/data/1278027/000110465926068744/tm2616326d2_ex99-2.htm) (accessed 2026-07-22): 2026 Green Giant US frozen business divestiture and continuing co-manufacturing arrangement; identifies frozen operations as capital-intensive, seasonal, and working-capital heavy.
- **S10** — [Seneca Foods Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/88948/000143774925020197/senea20250331_10k.htm) (accessed 2026-07-22): Frozen-vegetable share, private-label and foodservice channels, substantial competition, and downward selling-price pressure from excess industry capacity.
- **S11** — [Vegetable Availability Declined in 2024](https://www.ers.usda.gov/data-products/charts-of-note/112836) (accessed 2026-07-22): US vegetable availability fell to 376 pounds per person in 2024, a 35-year low; processing vegetables declined 32 pounds from 1996 to 2024.
- **S12** — [Vegetables and Pulses Outlook: April 2025](https://www.ers.usda.gov/sites/default/files/_laserfiche/outlooks/111478/VGS-375.pdf) (accessed 2026-07-22): Frozen-vegetable import value and volume and processed-vegetable export value and volume in 2024, including product-mix detail.
