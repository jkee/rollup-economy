# 312130 — Wineries

*v5.1 Stage 1 research memo. Run `312130-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.57 · L 1.04 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Long-cycle inventory and mixed wholesale, club, and custom-production operations create valuable AI-addressable planning and commercial workflows.
**Weakness:** Falling wine consumption and fragmented winery business models can overwhelm labor-efficiency gains.

## Business-model lens
- Included: Lower-middle-market U.S. winery operators that repeatedly produce, age, blend, bottle, or supply wine for external wholesale, retail, wine-club, private-label, or custom-crush customers, including estate wineries with a material production business.
- Excluded: Hospitality- or events-dominant tasting-room properties; stand-alone vineyards without winery operations; brand-only virtual wineries that outsource all physical production; merchant wholesalers that only bottle purchased wine; captive pilot sites; shells; and firms outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: Recurring case, bottle, bulk, private-label, and custom-production sales to distributors, retailers, restaurants, club members, and brand owners, with wholesale and direct-to-consumer channels often coexisting.
- Deviation from default lens: NAICS-linked winery populations mix physical production, estate agriculture, virtual brands, tasting rooms, clubs, tourism, and events. To keep labor, retention, and operator-requirement judgments coherent, the lens retains accountable production wineries with repeat supply or club relationships and excludes brand-only and hospitality-dominant businesses.

## Executive view
Production wineries have real AI opportunity in commercial, club, planning, inventory, compliance, and administrative work, but physical and sensory production remains central. The decisive weakness is demand: estimated U.S. wine consumption fell from 1.06 billion gallons in 2021 to 870 million in 2024. Heterogeneous virtual, estate, tourism, club, and wholesale models also make eligibility and economics unusually uncertain.

## How AI changes the work
AI can improve demand and depletion forecasts, inventory allocation across vintages, club retention, order service, sales prioritization, marketing production, compliance drafting, purchasing, production scheduling, and anomaly detection. Vineyard, crush, cellar, laboratory, sanitation, barrel, bottling, warehouse, and accountable release work remains human- and equipment-intensive.

## Value capture
Direct and club sales provide more control over price and customer relationships, whereas wholesale wine passes through distributor and retail tiers. In a declining category, savings can fund discounts, promotions, shipping, service, and customer acquisition. Mixed-channel operators should retain a meaningful but incomplete share.

## Firm availability
Owner aging, winery closures, and asset sales support transfer supply, but wine transactions often split brands, vineyards, production facilities, inventory, and hospitality real estate. A buyer may find assets without a transferable operating company, so deal headlines cannot be mapped directly to a qualifying transfer probability.

## Demand durability
Wine still requires licensed physical production, but the amount demanded is falling. Premiumization props up value while gallons and cases decline, and smaller producers face distributor rationalization. Strong clubs, differentiated brands, private-label relationships, and custom-crush utilization can outperform the category.

## Risks and uncertainty
The main risks are continuing consumption decline, excess inventory, distributor concentration, club churn, discounting, agricultural and climate variability, wildfire smoke, water and insurance costs, label and shipping regulation, and vintage working capital. The 696-firm count is especially uncertain because a food-processing margin bridge spans virtual, hospitality, agricultural, and premium brand models.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1814 | — | OBSERVED | — |
| n | — | 696 | — | ESTIMATE | — |
| a | 0.15 | 0.27 | 0.39 | PROXY | S4, S5, S6 |
| rho | 0.3 | 0.53 | 0.72 | ESTIMATE | S5, S8 |
| e | 0.5 | 0.68 | 0.82 | PROXY | S1, S6, S7 |
| s5 | 0.14 | 0.26 | 0.4 | ESTIMATE | S9, S10, S11 |
| q | 0.34 | 0.57 | 0.76 | ESTIMATE | S8, S12 |
| d5 | 0.62 | 0.79 | 0.96 | PROXY | S2, S3, S12 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S7, S13 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 1.04 | 2.04 | ESTIMATE |
| F | 6.28 | 7.75 | 8.74 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 5.46 | 7.50 | 9.50 | ESTIMATE |

## Caveats
- a: The occupational mix is a three-digit beverage-and-tobacco proxy.
- a: Estate vineyard labor is difficult to separate from winery production labor.
- a: GenAI task exposure is not equivalent to current unautomated substitutable labor.
- rho: No representative U.S. winery study of realized AI labor savings was found.
- rho: Small firms may lack integrated customer, depletion, inventory, and production data.
- rho: The estimate excludes autonomous field labor and speculative general-purpose robotics.
- e: Industry databases count facilities and virtual wineries differently from Census firms.
- e: Production volume does not map cleanly to EBITDA because bottle price and DTC mix vary widely.
- e: The frozen count uses a food-processing margin bridge that may misclassify hospitality and agricultural economics.
- s5: The owner-age statistic is cross-industry and based on 2018 respondents.
- s5: Reported transaction counts emphasize notable deals and omit confidential small transactions.
- s5: Wine deals often separate brands, inventory, vineyards, and production facilities, only some of which qualify.
- q: The public-company channel mix is one Oregon winery and is not representative nationally.
- q: Channel mix, bottle price, club penetration, and distributor power vary greatly by region and brand.
- q: Discounting may absorb savings even without explicit contractual pass-through.
- d5: Consumption estimates cover imported wine and producers outside the lens.
- d5: Pandemic years amplify the apparent recent decline.
- d5: Premium, direct, private-label, and custom-crush cohorts can diverge sharply from total gallons.
- o: Operator requirement does not imply survival of each winery or brand.
- o: Custom crush preserves accountable production while shifting it to another operator.
- o: Imports and large domestic facilities can replace LMM production without software eliminating the service.

## Sources
- **S1** — [312130: Wineries - Census Bureau Profile](https://data.census.gov/profile/312130_-_Wineries?codeset=naics~312130) (accessed 2026-07-23): Identifies NAICS 312130 wineries and notes that bottling purchased wines and wholesaling bottled wines is classified in merchant wholesaling rather than wineries.
- **S2** — [U.S. Wine Consumption](https://wineinstitute.org/our-industry/statistics/us-wine-consumption/) (accessed 2026-07-23): Reports total U.S. wine consumption of 1.06 billion gallons and 3.16 gallons per resident in 2021 versus 870 million gallons and 2.54 gallons per resident in 2024.
- **S3** — [California and U.S. Wine Sales](https://wineinstitute.org/our-industry/statistics/california-us-wine-sales/) (accessed 2026-07-23): Reports California wine shipments to the U.S. of 203.5 million nine-liter cases in 2024 versus 237.9 million in 2019 and explains that retail values include intermediary markups.
- **S4** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 312000](https://www.bls.gov/oes/2023/may/naics3_312000.htm) (accessed 2026-07-23): Reports the broader beverage-and-tobacco occupation mix, including production at 22.11%, transportation/material moving at 12.33%, office support at 4.87%, and sales at 12.15% of employment.
- **S5** — [Generative AI and Jobs: A Refined Global Index of Occupational Exposure](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) (accessed 2026-07-23): Finds clerical occupations have the highest GenAI exposure and that job transformation is generally more likely than full automation.
- **S6** — [2025 Economic Impact Study: Data and Methodology](https://wineamerica.org/wp-content/uploads/2025/05/2025-WineAmerica-Methodology-4-28-25-Final.pdf) (accessed 2026-07-23): Describes winery production work, wholesale and direct channels, estate vineyards, tasting rooms, custom-crush facilities, virtual wineries, and an estimated 75,655 U.S. wine production or marketing jobs.
- **S7** — [U.S. Winery Statistics](https://winebusinessanalytics.com/statistics/winery/) (accessed 2026-07-23): Counts 11,165 unique virtual and bonded wineries in January 2026, reports winery size distribution, defines virtual wineries, and notes that production includes custom production.
- **S8** — [2025 Direct-to-Consumer Wine Report](https://www.svb.com/trends-insights/reports/dtc-wine-survey-report-2025/) (accessed 2026-07-23): Describes wine club, tasting room, and e-commerce channels, falling visitation, discounting pressure, and wineries' reassessment of DTC strategy.
- **S9** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-23): Reports that 51% of responding employer-business owners were age 55 or older in the 2019 Annual Business Survey, data year 2018.
- **S10** — [How some California wine companies took advantage of the 2025 downturn](https://www.sfchronicle.com/food/wine/article/2025-wine-industry-acquisitions-21223746.php) (accessed 2026-07-23): Reports 27 notable wine transactions through October 2025 and illustrates that buyers may acquire brands without winery facilities or vineyards.
- **S11** — [Crimson Wine Group 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1562151/000162828026018796/cwgl-20251231.htm) (accessed 2026-07-23): Discloses a 2026 acquisition of a wine brand's inventory, intellectual property, trademarks, customer lists, and related liabilities, illustrating asset-level deal structure.
- **S12** — [Willamette Valley Vineyards 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/838875/000119983526000061/wvvi-10k.htm) (accessed 2026-07-23): Reports 54.4% of 2025 sales direct and 45.6% through distributors, 6.5% lower net sales, nearly flat gross-margin percentage, higher discounts, and higher selling costs.
- **S13** — [TTB Wine Permits](https://www.ttb.gov/regulated-commodities/beverage-alcohol/wine/permits) (accessed 2026-07-23): States that bonded wineries, bonded wine cellars, and taxpaid wine bottling houses must apply to TTB and receive permission before starting operations.
