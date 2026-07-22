# 311821 — Cookie and Cracker Manufacturing

*v5.1 Stage 1 research memo. Run `311821-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.88 · L 0.75 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat retailer and distributor replenishment creates durable customer relationships and rich planning data.
**Weakness:** Mechanized physical production limits AI-addressable labor, while retailers and promotions can recapture much of the benefit.

## Business-model lens
- Included: Lower-middle-market manufacturers of cookies, crackers, ice cream cones, and similar products that repeatedly supply external supermarkets, discounters, warehouse clubs, food distributors, foodservice customers, private-label owners, or contract-manufacturing customers.
- Excluded: Immediate-consumption cookie shops, baked-goods retailers, pretzel manufacturing, pasta and purchased-flour mix manufacturing, captive internal plants without external customers, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat wholesale product supply priced per unit, case, shipment, negotiated retail program, private-label contract, or co-manufacturing arrangement, often accompanied by discounts, rebates, volume incentives, displays, and other trade promotions.
- Deviation from default lens: none

## Executive view
Cookie and cracker manufacturing strongly fits repeat outsourced supply, but factory work is physical and commonly mechanized, so AI opportunity is concentrated in demand and promotion forecasting, planning, quality documentation, procurement, customer administration, and maintenance rather than direct line substitution. Retailer bargaining power and category softness constrain retained value.

## How AI changes the work
AI can improve forecasts, promotional planning, retailer deductions and claims, production and labor schedules, purchasing, specification search, quality-record review, allergen documentation, customer service, marketing content, and maintenance planning. Baking, changeovers, sanitation, packaging, warehousing, and safety-critical release remain equipment- and operator-dependent.

## Value capture
Case pricing allows initial retention, but retail programs include discounts, rebates, coupons, volume incentives, displays, and other trade spending. Consolidated retailers can demand price concessions or promote their own brands, and recent pricing elasticity illustrates how higher prices can reduce volumes; differentiated brands and formulations retain more than commodity contract production.

## Firm availability
Most target firms should have repeat external customers, although captive, seasonal, and customer-concentrated plants require screening. Transferability depends on food-safety performance, retailer approvals, plant condition, customer durability, brand or formula rights, and capital requirements; weak situations may liquidate assets instead of transferring as going concerns.

## Demand durability
Shelf stability, convenience, broad retail access, and habitual snacking support continuing demand. Health and nutrition trends, price elasticity, discretionary-cookie softness, private-label competition, pack-size changes, and substitution to other snacks create a wider demand range than physical operator dependence alone would suggest.

## Risks and uncertainty
Six-digit occupation and real-output data, transfer rates, target-firm eligibility, and AI benefit-retention cohorts are unavailable. Food allergens, labeling, recalls, retailer concentration, trade spend, commodity costs, category maturity, brand erosion, plant utilization, and equipment capital can dominate administrative savings. The provided compensation ratio mixes 2024 wages with 2022 receipts and is harmonized, while the target-band firm count is margin-bridged rather than directly observed.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2466 | — | OBSERVED | — |
| n | — | 121 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.22 | PROXY | S1, S2 |
| rho | 0.35 | 0.54 | 0.71 | ESTIMATE | S2, S3 |
| e | 0.78 | 0.9 | 0.97 | ESTIMATE | S4, S5 |
| s5 | 0.08 | 0.17 | 0.29 | ESTIMATE | — |
| q | 0.2 | 0.4 | 0.62 | ESTIMATE | S5 |
| d5 | 0.94 | 1.05 | 1.16 | PROXY | S6, S5 |
| o | 0.97 | 0.995 | 1 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.75 | 1.54 | ESTIMATE |
| F | 3.45 | 4.78 | 5.72 | ESTIMATE |
| C | 4.00 | 8.00 | 10.00 | ESTIMATE |
| D | 9.12 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS combines all NAICS 311800 segments and excludes self-employed workers.
- a: The FDA cookie examples are illustrative regulatory guidance, not a representative time study.
- a: The mapping is judgmental and cannot precisely isolate tasks already automated.
- rho: No 311821-specific five-year AI implementation cohort was located.
- rho: Large branded firms have richer data and integration capacity than many LMM private-label or regional manufacturers.
- e: Mondelēz is global and far larger than the target band, so it demonstrates channels rather than the eligible share.
- e: The provided target-band firm count is margin-bridged and may misclassify firms with unusual brand economics or capital intensity.
- s5: No source directly measures qualifying five-year control transfers for eligible target-band cookie and cracker manufacturers.
- s5: Private strategic acquisitions and distressed plant sales can be difficult to distinguish in public records.
- q: Mondelēz has unusually strong brands and global scale, which may increase pricing power relative to target firms, while its large retailers may exert greater bargaining power.
- q: Observed input-cost pricing elasticity is not a direct measure of pass-through of AI-enabled labor savings.
- d5: BLS output is four-digit and includes multiple bakery and tortilla categories.
- d5: Mondelēz's North American result includes biscuits and baked snacks and reflects one large branded portfolio rather than the full U.S. industry.
- o: Persistence of operator-required demand does not guarantee persistence of independent target firms; larger manufacturers or retailer-owned brands may take share.
- o: The estimate separates operator displacement from ordinary category demand loss, which is captured in d5.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311800](https://www.bls.gov/oes/2023/may/naics4_311800.htm) (accessed 2026-07-22): Reports broader-industry occupation employment and wages, including production at 49.70%, transportation and material moving at 13.23%, sales at 10.79%, office support at 5.24%, management at 3.75%, and business operations at 1.68%.
- **S2** — [FDA Draft Guidance: Hazard Analysis and Risk-Based Preventive Controls for Human Food, Chapter 6](https://www.fda.gov/media/107327/download) (accessed 2026-07-22): Provides cookie-processor examples with automated temperature or speed recording plus manual checks, dough-weight monitoring, QC review, corrective actions, calibration, and documented verification.
- **S3** — [FDA Food Allergies](https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies) (accessed 2026-07-22): Describes allergen preventive controls, written cross-contact and labeling procedures, inspections, and notes bakery products among the food types most often involved in allergen recalls.
- **S4** — [2022 NAICS Definition: 311821 Cookie and Cracker Manufacturing](https://www.census.gov/naics/?details=311821&input=311821&year=2022) (accessed 2026-07-22): Defines the industry as establishments primarily manufacturing cookies, crackers, and products such as ice cream cones, while distinguishing immediate-consumption and retail activities.
- **S5** — [Mondelēz International 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1103982/000162828026005345/mdlz-20251231.htm) (accessed 2026-07-22): Documents biscuit and baked-snack operations, retail and distributor channels, competition and retailer bargaining power, trade incentives and rebates, North American category softness, unfavorable volume/mix from pricing elasticity, and lower manufacturing costs from productivity.
- **S6** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects broader NAICS 311800 real output from 62.1 to 74.4 billion chained 2017 dollars between 2024 and 2034, a 1.8% annual growth rate.
