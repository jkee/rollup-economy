# 311514 — Dry, Condensed, and Evaporated Dairy Product Manufacturing

*v5.1 Stage 1 research memo. Run `311514-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.30 · L 0.30 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Essential food and nutrition ingredient uses preserve demand for accountable physical processing.
**Weakness:** Commodity exposure, mixed product trajectories, and integrated ownership limit both benefit retention and transferable-firm availability.

## Business-model lens
- Included: U.S. lower-middle-market operators that repeatedly manufacture dry, condensed, evaporated, concentrated, whey, or related dairy and dairy-substitute products for external food, beverage, nutrition, foodservice, distributor, or export customers.
- Excluded: Fluid milk, creamery butter, cheese, frozen dairy products, captive internal facilities without external customers, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat ingredient or packaged-product supply, commonly priced by weight or unit under contracts, purchase orders, commodity formulas, specifications, or private-label arrangements.
- Deviation from default lens: none

## Executive view
Dry, condensed, and evaporated dairy manufacturing has persistent physical-ingredient demand and meaningful information workflows, but its product basket and commercial economics are unusually mixed. AI is more likely to improve planning, documentation, quality, and maintenance support than to replace plant labor, while commodity pricing and integrated ownership constrain capture and availability.

## How AI changes the work
Useful applications include demand and milk-component forecasting, production scheduling, specification matching, certificate and export-document preparation, quality-data triage, deviation investigation, maintenance support, procurement, and customer service. Dryers, evaporators, filtration, sanitation, laboratory work, packaging, and material movement remain physical and already use conventional control systems.

## Value capture
Specialized proteins and qualification-intensive ingredients can retain more benefit than commodity powders. Formula pricing, global tenders, open-book customers, trade volatility, and competing processors' adoption can pass a substantial share of implemented savings through to buyers.

## Firm availability
The frozen dataset identifies 40 LMM-band firms, but standalone eligibility is uncertain because many plants may be cooperative, captive, strategically integrated, or dependent on a narrow export or customer channel. Broad owner-age evidence suggests succession pressure without measuring control sales in this capital-intensive niche.

## Demand durability
Recent evidence is mixed: nonfat dry milk output was roughly stable, skim milk powder contracted, high-protein whey exports grew, and NFDM/SMP exports fell. Durable ingredient uses support a stable base, but product substitution, milk-component economics, trade, and large-scale capacity determine which operators benefit.

## Risks and uncertainty
Principal risks include commodity and milk-component volatility, export concentration, tariffs and freight, food-safety and recall exposure, customer qualification, environmental and energy intensity, legacy controls, cybersecurity, capex needs, and a shift from commodity powders toward specialized proteins. A target with open-book pricing, obsolete drying assets, weak environmental compliance, or captive supply economics could destroy the expected benefit.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0919 | — | OBSERVED | — |
| n | — | 40 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S2 |
| rho | 0.25 | 0.46 | 0.68 | ESTIMATE | S3, S4 |
| e | 0.35 | 0.55 | 0.75 | ESTIMATE | S1, S6 |
| s5 | 0.08 | 0.17 | 0.29 | PROXY | S5 |
| q | 0.2 | 0.42 | 0.68 | ESTIMATE | S7 |
| d5 | 0.88 | 1.02 | 1.18 | PROXY | S6, S7 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1, S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.09 | 0.30 | 0.70 | ESTIMATE |
| F | 1.21 | 2.50 | 3.65 | ESTIMATE |
| C | 4.00 | 8.40 | 10.00 | ESTIMATE |
| D | 8.27 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source covers all dairy product manufacturing rather than this six-digit industry.
- a: Employment counts require judgmental task and wage mapping.
- a: The estimate excludes substitutions that require new physical automation rather than AI-enabled workflows.
- rho: Regulatory sources establish control requirements and feasibility, not observed AI adoption.
- rho: Modern high-throughput dryers may implement faster than small plants with legacy controls.
- e: The frozen LMM firm count is used as provided and not re-estimated.
- e: Industry definitions and survey universes do not identify which enterprises are standalone, recurring external suppliers.
- s5: The source is cross-industry and based on 2018 owner data.
- s5: Owner age is not a transaction measure and the source counts responding owners rather than firms.
- q: No source directly measures retained AI benefit over five years.
- q: Commodity nonfat dry milk and skim milk powder should retain less than specialized high-protein or customer-qualified ingredients.
- q: Export exposure introduces currency, tariff, freight, and global-supply effects not included in implementation difficulty.
- d5: Production and exports are affected by milk-component availability, capacity, inventory, and trade conditions as well as end demand.
- d5: The NAICS basket spans products with materially different trajectories.
- d5: National category growth may accrue mainly to large integrated plants.
- o: The estimate concerns accountable-operator necessity, not labor intensity.
- o: The required operator can migrate to a large integrated or overseas producer even if software cannot eliminate the role.

## Sources
- **S1** — [North American Industry Classification System: 311514 Dry, Condensed, and Evaporated Dairy Product Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines 311514 as manufacturing dry, condensed, and evaporated milk and dairy-substitute products and identifies adjacent exclusions.
- **S2** — [BLS OEWS Data Tables for Industry Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest dairy-manufacturing occupations, including 25,520 food batchmakers, 23,690 packaging/filling operators, 8,170 material movers, and 7,840 production supervisors.
- **S3** — [FDA: Computerized Systems in the Food Processing Industry](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-guides/computerized-systems-food-processing-industry) (accessed 2026-07-22): Describes acceptable computerized food-processing records and controls and the review expected for regulatory equivalence and safety-critical functions.
- **S4** — [FDA: Keeping Your Milk Safe From the Grass to the Glass](https://www.fda.gov/consumers/consumer-updates/keeping-your-milk-safe-grass-glass) (accessed 2026-07-22): Describes regulated dairy responsibilities for process temperatures, equipment controls and testing, worker safety, laboratory testing, and oversight.
- **S5** — [U.S. Census Bureau: Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding owners of U.S. employer businesses were age 55 or older in the 2019 ABS covering data year 2018.
- **S6** — [USDA NASS Dairy Products 2025 Summary](https://www.nass.usda.gov/Publications/Todays_Reports/reports/daryan26.pdf) (accessed 2026-07-22): Reports 2025 U.S. human nonfat dry milk production of 1.66 billion pounds, up slightly, and skim milk powder production of 504 million pounds, down 15.9%, and describes the surveyed product categories.
- **S7** — [U.S. Dairy Export Council: Cheese and butter fuel dairy export growth in 2025](https://www.usdec.org/newsroom/news-releases/news-releases/news-release-2/24/2026) (accessed 2026-07-22): Reports 2025 high-protein whey exports up 6%, growth in milk protein concentrate and whole milk powder, and NFDM/SMP exports down 9%; also documents the importance and volatility of export markets.
