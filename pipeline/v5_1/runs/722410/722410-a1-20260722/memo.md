# 722410 — Drinking Places (Alcoholic Beverages)

*v5.1 Stage 1 research memo. Run `722410-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.69 · L 0.99 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat transactional demand allows standardized AI-enabled support workflows to be deployed across multiple regulated venues while retaining local hospitality.
**Weakness:** Most wage-bearing work is physical and customer-facing, and direct evidence on transferable lower-middle-market bar firms is sparse.

## Business-model lens
- Included: US lower-middle-market firms operating bars, taverns, pubs, nightclubs, and other drinking places whose primary business is preparing and serving alcoholic beverages for immediate on-premises consumption as a repeat hospitality service to external customers.
- Excluded: Food-primary restaurants, member-only civic or social clubs, packaged-alcohol retailers, dance clubs that do not sell alcohol, beverage manufacturers, shells, captive internal units, and non-control financing vehicles.
- Customer and revenue model: Walk-in and repeat consumers generally pay posted menu prices for beverages, tabs, cover charges, and occasional event minimums; revenue is predominantly transactional rather than governed by long-term customer contracts.
- Deviation from default lens: none

## Executive view
Drinking places offer a real but bounded opportunity to automate support workflows around scheduling, marketing, inventory, hiring, ordering, payment, and compliance. The central service remains a physical, social, regulated experience, so the operating case should rest on consistent execution and avoided hiring rather than wholesale replacement of bartenders and floor staff. Transfer activity exists in the broader restaurant market, but evidence for control transfers at the assigned firm size is weak.

## How AI changes the work
AI can consolidate demand forecasting, roster creation, applicant screening, training support, promotion design, guest messaging, purchasing suggestions, and exception detection across venues. Digital ordering and payment can remove transactional steps. Beverage preparation, guest rapport, security, cleaning, crowd management, and responsible service remain difficult to substitute, and current restaurant evidence indicates augmentation is much more common than job elimination.

## Value capture
Posted menu pricing provides room to retain initial labor and administrative savings because there is no contractual cost-plus pass-through. Over time, competitors can share those gains through promotions, better service, or lower effective prices, and operators may reinvest savings in higher-skilled staff. Persistent retention therefore depends on differentiated concepts, local density, disciplined pricing, and measurable service quality.

## Firm availability
Most firms coded to this industry fit the repeat external-customer lens, but qualifying availability is less certain than basic eligibility. The visible restaurant resale market is active yet concentrated in businesses much smaller than the assigned EBITDA band. Liquor licenses, leases, founder identity, and venue-specific goodwill can complicate control transfers or turn them into asset sales.

## Demand durability
The venue experience is hard to replace with software, supporting a high operator-required share. Aggregate quantity is less certain: BLS projects modest drinking-place employment growth, while recent per-capita alcohol consumption declined. Population growth and experiential spending can support visits, but health moderation, at-home consumption, cannabis substitution, and discretionary-spending pressure can offset them.

## Risks and uncertainty
The largest evidence gaps are bar-specific task time, realized labor savings, lower-middle-market deal incidence, and inflation-adjusted on-premises quantity. Broader restaurant surveys may not transfer to nightclubs, taverns, and cocktail bars. Labor, rent, insurance, security, liquor regulation, lease assignment, and local concept risk can absorb automation gains, while aggressive self-service could damage the hospitality experience that customers are buying.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3454 | — | OBSERVED | — |
| n | — | 287 | — | ESTIMATE | — |
| a | 0.1 | 0.17 | 0.25 | PROXY | S2, S3, S4 |
| rho | 0.24 | 0.42 | 0.62 | PROXY | S3, S4 |
| e | 0.75 | 0.88 | 0.95 | ESTIMATE | S1, S9 |
| s5 | 0.1 | 0.18 | 0.3 | PROXY | S5, S6 |
| q | 0.42 | 0.62 | 0.78 | ESTIMATE | S4, S5 |
| d5 | 0.92 | 1.02 | 1.11 | PROXY | S7, S8 |
| o | 0.88 | 0.94 | 0.98 | ESTIMATE | S1, S4, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.99 | 2.14 | PROXY |
| F | 5.01 | 6.17 | 7.10 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 8.10 | 9.59 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation table is from May 2023 and covers payroll employment rather than unpaid owner labor.
- a: Task shares are judgmental and mean wages are used where detailed wage and employment cells are suppressed.
- a: Restaurant technology surveys cover the broader restaurant population rather than drinking places specifically.
- rho: Tool adoption does not measure the fraction of exposed task hours actually removed or avoided.
- rho: Surveyed restaurants include full-service and limited-service formats and are not restricted to the assigned EBITDA band.
- rho: Liquor-control, service-quality, staff acceptance, integration, and data-quality constraints vary by state and concept.
- e: No source directly measures lens eligibility among firms in the supplied EBITDA band.
- e: NAICS is assigned at the establishment level, while the supplied count and this primitive concern firms.
- e: This estimate does not discount for transfer probability, which is handled only in s5.
- s5: Reported marketplace sales are not a complete census and are concentrated below the assigned EBITDA band.
- s5: Restaurant transactions are not bar-specific, and owner age does not itself imply sale intent.
- s5: Liquor-license and lease transfer rules can convert an intended sale into an asset liquidation or failed closing.
- q: No observed study isolates AI-derived gross benefit and its pass-through in bars.
- q: Competitive intensity, concept differentiation, tipping practices, and local minimum wages create wide dispersion.
- q: The estimate excludes implementation failure and volume loss, which belong in rho and demand primitives.
- d5: Employment is affected by productivity and staffing intensity and is not a direct quantity measure.
- d5: Broader sector output includes restaurants, and total alcohol consumption includes off-premises channels.
- d5: Pandemic recovery, demographic shifts, cannabis substitution, wellness trends, and local regulation add structural uncertainty.
- o: Full-service restaurant preferences are a proxy for bar patrons and may overstate food-service-style employee interaction.
- o: State and local licensing requirements vary, and regulation can change over the horizon.
- o: This primitive concerns operator requirement, not labor intensity; staff reductions are captured in a and rho.

## Sources
- **S1** — [2022 NAICS 722410 Drinking Places (Alcoholic Beverages) definition](https://www.census.gov/naics/?details=722410.&input=722410&year=2022) (accessed 2026-07-22): Defines the industry as bars, taverns, nightclubs, and drinking places primarily preparing and serving alcoholic beverages for immediate consumption, with limited food services allowed, and identifies excluded adjacent activities.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 722400](https://www.bls.gov/oes/2023/May/naics4_722400.htm) (accessed 2026-07-22): Reports 411,940 total employees; food preparation and serving at 83.42% of employment; bartenders at 44.21%; waiters and waitresses at 12.24%; cooks at 11.90%; management at 4.20%; protective service at 4.50%; and occupation-specific mean wages.
- **S3** — [National Restaurant Association Research Insight: Hiring & Staffing Report 2026](https://go.restaurant.org/rs/078-ZLA-461/images/2026-Research-Insight_Hiring-and-Staffing.pdf?version=0) (accessed 2026-07-22): Reports 49% scheduling-software use, 26% AI-tool use, AI impact by workflow, and that 6% of operators said recent technology investment permanently eliminated jobs.
- **S4** — [National Restaurant Association Restaurant Technology Landscape Report 2024](https://go.restaurant.org/rs/078-ZLA-461/images/NatRestAssoc_TechLandscapeReport_2024.pdf) (accessed 2026-07-22): Reports operator technology plans, including 52% for back-office and inventory systems, 37% for automated labor management, 30% for flexible pricing, and 16% for AI; also reports consumer acceptance of ordering and payment technology alongside a preference for employee engagement in full-service experiences.
- **S5** — [Restaurant Sales Found Their Footing Late in 2025](https://www.bizbuysell.com/learning-center/article/restaurant-industry-analysis/) (accessed 2026-07-22): Reports 2,516 restaurant transactions in 2025, median revenue of $675,788, median cash flow of $115,252, a median sale price of $215,000, and revenue growth that substantially exceeded cash-flow growth.
- **S6** — [New Association report provides a demographic profile of restaurant owners](https://restaurant.org/research-and-media/research/restaurant-economic-insights/analysis-commentary/new-association-report-provides-a-demographic-profile-of-restaurant-owners/) (accessed 2026-07-22): Summarizes Census-based restaurant ownership demographics and reports that 29% of restaurant owners were under age 45.
- **S7** — [BLS Table 2.11 Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects drinking-place employment from 421,200 in 2024 to 439,900 in 2034, a 0.4% compound annual increase, and broader food-services-and-drinking-places real output growth of 2.2% annually.
- **S8** — [NIAAA Surveillance Report 122: Apparent Per Capita Alcohol Consumption, 1977 to 2023](https://www.niaaa.nih.gov/publications/surveillance-reports/surveillance122) (accessed 2026-07-22): Reports 2023 US per-capita ethanol consumption of 2.48 gallons, down 1.2% from 2022, with beer and wine declines offsetting continued spirits growth.
- **S9** — [TTB Beverage Alcohol Retailers](https://www.ttb.gov/ttb-audiences/business-owners/retailers-beverage-alcohol) (accessed 2026-07-22): States that bars and taverns are retail liquor dealers subject to registration and location-specific recordkeeping requirements for beverage alcohol receipts.
