# 562119 — Other Waste Collection

*v5.1 Stage 1 research memo. Run `562119-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.87 · L 1.60 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is the ability to combine locally defensible physical service with AI-enabled improvement in lead handling, job estimation, route density, dispatch, billing, and pricing discipline.
**Weakness:** The principal weakness is that most labor and customer value remain tied to vehicles, travel, handling, and site-specific execution, while a substantial share of demand may be episodic and construction-sensitive.

## Business-model lens
- Included: Lower-middle-market firms providing local collection and hauling of waste other than nonhazardous solid waste and hazardous waste, including brush, rubble, and similar debris removal, where revenue comes from repeat outsourced service or a repeatable stream of jobs for external customers.
- Excluded: Long-distance freight trucking, nonhazardous solid-waste collection, hazardous-waste collection, combined collection and disposal operations, materials recovery, landfill operation, and firms whose economics are primarily disposal rather than collection and hauling.
- Customer and revenue model: Customers include households, property managers, contractors, businesses, and public entities. Revenue is generated through scheduled or on-call pickup, container or equipment rental, hauling, and charges influenced by service frequency, volume or weight, distance, and disposal cost; some demand is recurring while construction debris, storm cleanup, and household cleanouts are episodic.
- Deviation from default lens: none

## Executive view
Other Waste Collection is a physically anchored local service with modest but useful AI leverage in commercial and coordination work. The recurring-service lens is coherent, though episodic debris and cleanup work lowers eligibility relative to route-dense subscription collection. Value creation is more likely to come from faster response, better estimates, fuller routes, reduced back-office burden, and disciplined pricing than from automating pickup itself.

## How AI changes the work
Current exposure is concentrated in quoting, scheduling, dispatch, customer communications, billing, collections, marketing, and analysis of photos or job notes. Five-year implementation should expand as these functions are bundled into field-service, routing, CRM, and accounting tools, but weak data, small teams, and variable site conditions will keep adoption incomplete.

## Value capture
Operators can retain some productivity and conversion gains because customers buy a completed local service rather than clerical inputs. Retention is limited by competitive quote comparison, common software availability, and pricing structures that explicitly reflect fuel, disposal, distance, weight, volume, and equipment costs.

## Firm availability
The industry has an estimated 99 firms in the target size band from the frozen dataset, but the share meeting the recurring or repeat-service lens is uncertain. Broad owner succession intentions and observed waste-sector marketplace transactions support deal flow, while realized qualifying transfers should remain below stated intentions.

## Demand durability
Demand is supported by population, property maintenance, renovation, turnover, brush removal, and cleanup, but it is less uniformly recurring than conventional municipal solid-waste collection. Construction-linked work is cyclical, and current nominal construction spending is soft; a roughly flat five-year real base with a wide range is warranted.

## Risks and uncertainty
The central evidence problem is that public statistics usually combine Other Waste Collection with larger solid-waste operations. Six-digit occupational mix, recurrence, pricing power, transaction incidence, and real output are not directly observed. The target industry may range from route-based specialty collectors to irregular junk, brush, and rubble haulers, creating meaningful operator-level dispersion even though the industry definition itself is coherent.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3881 | — | OBSERVED | — |
| n | — | 99 | — | ESTIMATE | — |
| a | 0.13 | 0.21 | 0.31 | PROXY | S2, S3 |
| rho | 0.3 | 0.49 | 0.67 | PROXY | S3 |
| e | 0.46 | 0.64 | 0.8 | ESTIMATE | — |
| s5 | 0.08 | 0.15 | 0.23 | PROXY | S6, S7 |
| q | 0.3 | 0.48 | 0.66 | PROXY | S4 |
| d5 | 0.87 | 0.99 | 1.11 | PROXY | S5, S8 |
| o | 0.74 | 0.86 | 0.94 | PROXY | S2, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.61 | 1.60 | 3.22 | PROXY |
| F | 2.47 | 3.78 | 4.75 | ESTIMATE |
| C | 6.00 | 9.60 | 10.00 | PROXY |
| D | 6.44 | 8.51 | 10.00 | PROXY |

## Caveats
- a: The occupational evidence covers NAICS 562100 rather than six-digit NAICS 562119.
- a: Task exposure is inferred from occupations and business functions, not observed as an industry-specific wage-weighted measure.
- rho: The Census evidence spans all industries and firm sizes rather than Other Waste Collection.
- rho: Five-year implementation is a forward projection from current adoption and adoption depth.
- e: No direct denominator of firms meeting the size, independence, and recurring or repeat-service criteria was found.
- e: The estimate distinguishes economic eligibility from the separately supplied firm-count primitive.
- s5: Gallup covers all U.S. employer-business owners rather than this industry or size band.
- s5: BizBuySell is a voluntary marketplace sample and does not provide the eligible-firm denominator.
- q: Waste Management is a large integrated operator and is not representative of the target size band or exact six-digit industry.
- q: The source describes pricing drivers rather than directly measuring AI benefit retention.
- d5: BLS reports the refuse-collector occupation across industries, not output for NAICS 562119.
- d5: Construction spending is a broad nominal activity indicator and only part of this industry's demand base.
- o: The evidence uses broader waste-collection and cross-industry occupational data.
- o: Operator-required share is inferred from current physical workflows and plausible five-year mechanization.

## Sources
- **S1** — [North American Industry Classification System: Sector 56, 562119 Other Waste Collection](https://www.census.gov/naics/resources/archives/sect56.html) (accessed 2026-07-22): Defines Other Waste Collection as local hauling of waste other than nonhazardous solid and hazardous waste, including brush and rubble removal, and identifies excluded adjacent activities.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 562100 Waste Collection](https://www.bls.gov/oes/2023/may/naics4_562100.htm) (accessed 2026-07-22): Reports 208,430 jobs and the occupational distribution for broader Waste Collection, including 67.93% transportation and material-moving employment, 32.77% refuse collectors, 23.07% heavy truck drivers, and smaller office, management, sales, and analytical shares.
- **S3** — [Firm Data on AI: Insights from the Business Trends and Outlook Survey](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html) (accessed 2026-07-22): Reports late-2025 business AI adoption, employment-weighted use, adoption depth by business function, worker-task use, leading generative-AI tasks, and the prevalence of augmentation-only use.
- **S4** — [Waste Management, Inc. 2024 Form 10-K](https://investors.wm.com/static-files/d312d36b-3f6c-46e8-bd19-426f3ef64545) (accessed 2026-07-22): Describes collection revenue as fees influenced by service frequency, equipment, waste volume or weight, hauling distance, and disposal costs, providing a pricing-mechanics proxy for benefit retention.
- **S5** — [Occupational Outlook Handbook: Hand Laborers and Material Movers](https://www.bls.gov/ooh/Transportation-and-Material-Moving/Hand-laborers-and-material-movers.htm) (accessed 2026-07-22): Describes physical material-moving and refuse-collection duties, use of hydraulic lifts, injury exposure, 2024 employment, projected 2034 employment, and the countervailing effects of population demand, automation, and improved routing.
- **S6** — [Most U.S. Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 52.3% of employer businesses are owned by people age 55 or older and 22% of employer-business owners planned a sale or transfer within five years, based on a fall-2024 survey.
- **S7** — [BizBuySell 2025 Fourth Quarter Insight Report](https://www.bizbuysell.com/news/bizbuysell-2025-fourth-quarter-insight-report/) (accessed 2026-07-22): Reports flat overall 2025 transaction volume, 4% service-sector transaction growth, and 43 Waste Management and Recycling business transactions in its annual marketplace data.
- **S8** — [Monthly Construction Spending, May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-22): Reports May 2026 total construction spending 1.5% below May 2025 and first-five-month 2026 spending 2.7% below the comparable 2025 period, plus current private and public construction movements.
