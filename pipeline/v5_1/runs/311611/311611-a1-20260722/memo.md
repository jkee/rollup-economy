# 311611 — Animal (except Poultry) Slaughtering

*v5.1 Stage 1 research memo. Run `311611-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.09 · L 0.19 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable regulated physical throughput paired with still-manual documentation, monitoring, scheduling, and selective production workflows.
**Weakness:** The eligible outsourced-service subset is not measured nationally and may be much smaller than the full LMM firm population.

## Business-model lens
- Included: Lower-middle-market slaughter and meat-processing operators that repeatedly provide custom, toll, or inspected processing services to livestock owners, farms, brands, and other external customers.
- Excluded: Large integrated packers, firms principally buying livestock and selling meat on their own account, captive plants, poultry slaughter, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring or repeat business-to-business and owner-paid processing, commonly billed as a slaughter fee plus a per-pound processing charge, with optional packaging and value-added service fees.
- Deviation from default lens: The lens is narrowed to custom and toll slaughter/processing because NAICS 311611 combines fee-for-service processors with integrated commodity packers whose principal revenue is product sales; mixing the two would make retention and eligibility incoherent.

## Executive view
The coherent opportunity is not commodity meatpacking broadly but small and midsize custom or toll processors that repeatedly serve livestock owners and food brands. Their physical, regulated workflow is durable, while practical AI value is concentrated in documentation, scheduling, sensing, quality alerts, and selective robotic assistance rather than wholesale labor replacement.

## How AI changes the work
AI can reduce manual logs, monitor temperature and equipment, flag compliance deviations, optimize appointments and cut sheets, and assist vision-guided cutting. Variable carcasses, food-safety precision, humane-handling duties, washdown environments, and limited small-plant capital slow physical automation.

## Value capture
Fee menus typically separate slaughter from per-pound processing and add charges for packaging or value-added work. That structure permits initial retention, but transparent local price lists, farmer bargaining, renewal repricing, and replicable software will share benefits with customers over time.

## Firm availability
Only the custom and toll portion of LMM 311611 fits the recurring outsourced-service lens. Transfer supply is uncertain because aging ownership can create sales, but environmental, labor, inspection, facility, and livestock-supply risks can turn intended succession into closure or an asset transaction rather than a transferable going concern.

## Demand durability
USDA projections support broadly stable-to-growing beef and pork consumption and pork exports. Physical slaughter and custody remain necessary, though cattle cycles, poultry substitution, integrated-plant share, and local livestock availability can make individual facility volumes volatile.

## Risks and uncertainty
The largest uncertainties are the national prevalence of fee-for-service revenue inside 311611, plant-level automation economics, and qualifying transfer rates. Food-safety incidents, humane-handling failures, wastewater constraints, labor scarcity, livestock shortages, and customer concentration can erase operational gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0731 | — | OBSERVED | — |
| n | — | 177 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.3 | PROXY | S1, S2, S3 |
| rho | 0.18 | 0.32 | 0.48 | PROXY | S2, S3 |
| e | 0.2 | 0.35 | 0.55 | PROXY | S4 |
| s5 | 0.12 | 0.2 | 0.3 | ESTIMATE | — |
| q | 0.45 | 0.65 | 0.8 | PROXY | S4, S6 |
| d5 | 0.96 | 1.04 | 1.11 | PROXY | S5 |
| o | 0.9 | 0.96 | 0.99 | PROXY | S2, S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.06 | 0.19 | 0.42 | PROXY |
| F | 2.67 | 4.17 | 5.48 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | PROXY |
| D | 8.64 | 9.98 | 10.00 | PROXY |

## Caveats
- a: OEWS is NAICS 311600, includes poultry and processing, and is employment-weighted rather than wage-weighted.
- a: USDA automation projects demonstrate technical targets, not commercial adoption or realized labor removal.
- rho: Grant project descriptions may emphasize unmet needs and anticipated benefits.
- rho: Implementation varies sharply between digital compliance tools and physical robotics.
- e: The source is a North Carolina guide rather than a national census.
- e: Custom-exempt and federally inspected fee-for-service operations have different addressable customers and economics.
- s5: No industry-specific denominator-based transfer study was found.
- s5: A license or establishment-name change does not necessarily represent a qualifying control transfer.
- q: Published fee structures do not reveal discounts, utilization, or contract duration.
- q: Large-packer market concentration is an imperfect proxy for local custom-processing competition.
- d5: The projection includes poultry in some comparisons, while this code excludes poultry.
- d5: Commodity production and exports are only proxies for custom/toll service demand.
- o: Operator-required does not mean every current labor task persists.
- o: State and federal inspection regimes differ, and custom-exempt product has restricted end use.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311600](https://www.bls.gov/oes/2023/may/naics4_311600.htm) (accessed 2026-07-22): Broader-industry employment mix: 542,990 total jobs; food-processing workers 39.85%; cutters/trimmers 18.64%; slaughterers and meat packers 12.20%.
- **S2** — [Collaborative Cutting: Agile Robot Learners for Multipurpose Meat Industry Automation](https://www.nal.usda.gov/research-tools/food-safety-research-projects/collaborative-cutting-agile-robot-learners-multipurpose-meat-industry-automation) (accessed 2026-07-22): USDA project states robotic uptake in U.S. meat and hoofstock facilities is limited because systems are expensive, single-purpose, and infrastructure-intensive, and describes human-in-the-loop robotic cutting.
- **S3** — [Edge Computing Driven Automation for Small and Medium Poultry and Meat Processors](https://www.nal.usda.gov/research-tools/food-safety-research-projects/edge-computing-driven-automation-small-and-medium-poultry-and-meat-processors) (accessed 2026-07-22): USDA project describes manual logbook and clipboard data collection, physical equipment and temperature monitoring, and low-cost edge automation needs at small and midsize processors.
- **S4** — [Frequently Asked Questions About Processing and Marketing Your Own Meats](https://www.ncagr.gov/meat-poultry-inspection/FAQsaboutProcessingandMarketing/download?attachment=) (accessed 2026-07-22): North Carolina agriculture guidance describes custom and inspected processing, repeat farm-processor relationships, labeling obligations, and the common flat slaughter fee plus per-pound processing charge.
- **S5** — [U.S. Pork Exports Projected to Surpass Chicken in the Next Decade](https://ers.usda.gov/amber-waves/2024/february/u-s-pork-exports-projected-to-surpass-chicken-in-the-next-decade) (accessed 2026-07-22): USDA projects pork exports rising from 6.95 billion pounds in 2024 to 9.34 billion in 2033 and 2033 domestic per-capita beef and pork consumption above 2024.
- **S6** — [Concentration in U.S. Meatpacking Industry and How It Affects Competition and Cattle Prices](https://www.ers.usda.gov/amber-waves/2024/january/concentration-in-u-s-meatpacking-industry-and-how-it-affects-competition-and-cattle-prices) (accessed 2026-07-22): USDA documents four-firm shares of 85% for steer/heifer purchases and 67% for hog purchases, scale economies, changing capacity, new entry, and price-spread behavior.
- **S7** — [Federal Meat Inspection Act](https://www.fsis.usda.gov/policy/food-safety-acts/federal-meat-inspection-act) (accessed 2026-07-22): Statutory framework requires ante-mortem and post-mortem examination, humane slaughter, sanitary inspection, labeling, and other controls for meat establishments.
