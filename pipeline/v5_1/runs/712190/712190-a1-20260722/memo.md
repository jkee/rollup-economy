# 712190 — Nature Parks and Other Similar Institutions

*v5.1 Stage 1 research memo. Run `712190-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.96 · L 0.90 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Posted-price admissions and tours can preserve much of the value from automating visitor-information and administrative workflows.
**Weakness:** Site stewardship, safety, and maintenance remain physical, while nonprofit ownership and land restrictions sharply narrow transferable supply.

## Business-model lens
- Included: US lower-middle-market firms operating preserved natural areas, nature centers, wildlife sanctuaries, natural-wonder attractions such as caverns and waterfalls, and similar settings that repeatedly serve paying visitors, members, schools, or program customers.
- Excluded: Government park agencies, conservation-program administration, passive landholding without a recurring external-customer service, captive preserves, commercial hunting or fishing preserves classified elsewhere, accommodation-led properties classified elsewhere, shells, and non-control financing vehicles.
- Customer and revenue model: Mostly posted-price admissions, tours, passes, memberships, education and events, with ancillary food and merchandise; nonprofit operators also rely on donations and grants. Customers are predominantly individuals, families, members, schools, and organized groups.
- Deviation from default lens: none

## Executive view
Nature parks pair a high-compensation operating model with an automatable information layer, but the core product is physical stewardship and access to a site. AI can improve reservations, visitor support, content, schedules, memberships, reporting, and resource data analysis. Transferability is limited by nonprofit ownership, land and conservation restrictions, and highly site-specific assets.

## How AI changes the work
The most implementable uses are trip-planning and FAQ support, fee and permit workflows, marketing and interpretive content drafts, scheduling, member communications, records, and analytics. Maintenance, patrol, field surveys, habitat work, emergency response, guided engagement, and safety decisions remain human and on-site.

## Value capture
Private nature attractions historically earned most receipts from posted-price admissions and ancillary merchandise, a structure that does not mechanically pass efficiency savings to visitors. Retention is reduced by competitive discounts, attendance elasticity, wages, conservation duties, and the need to reinvest in trails, facilities, and safety.

## Firm availability
Paid caverns and natural-wonder attractions can be conventional closely held businesses, but many nature centers, preserves, and sanctuaries are tax-exempt, public, or constrained by mission and land covenants. Even a willing owner may face a thin buyer set and complex environmental, permit, title, or concession diligence.

## Demand durability
Current public visitation and broad real outdoor-recreation output support stable-to-modestly-growing demand for physical nature experiences. Demand remains discretionary and unusually vulnerable to local weather, wildfire, flood, ecosystem protection, road access, tourism cycles, and catastrophic closure.

## Risks and uncertainty
The main gaps are a current private six-digit occupation mix, current taxable-versus-exempt ownership by EBITDA band, modern revenue mix, and closed transaction history. The most precise industry revenue and tax-status evidence is from 1997, while current workflow and demand sources mostly describe public parks or the broader outdoor economy.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5474 | — | OBSERVED | — |
| n | — | 18 | — | ESTIMATE | — |
| a | 0.18 | 0.27 | 0.38 | PROXY | S2, S3, S4, S7 |
| rho | 0.32 | 0.5 | 0.66 | PROXY | S3, S5, S6 |
| e | 0.28 | 0.38 | 0.52 | PROXY | S1, S8 |
| s5 | 0.07 | 0.11 | 0.16 | PROXY | S9 |
| q | 0.58 | 0.72 | 0.84 | PROXY | S8, S10 |
| d5 | 0.94 | 1.06 | 1.15 | PROXY | S11, S12 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S2, S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.26 | 2.96 | 5.49 | PROXY |
| F | 0.49 | 0.90 | 1.47 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | PROXY |
| D | 8.27 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No current six-digit wage-weighted occupational mix was found for the eligible private population.
- a: Federal park jobs are a functional proxy and may differ from smaller private attractions.
- a: Generic GenAI exposure is not evidence of substitution, and the injected compensation-to-receipts ratio has the assignment's stated 2024-wage/2022-receipt vintage mismatch and IPS harmonization.
- rho: Cashless payment and online permits demonstrate digitization rather than AI implementation.
- rho: The NPS technology discussion is a draft advisory document for a public system, not measured LMM adoption.
- rho: Implementation must preserve human escalation for weather, wildlife, accessibility, emergencies, and route-safety questions.
- e: The tax-status split is from 1997 and is establishment-based, while the primitive is firm-based and current.
- e: Taxable status is not sufficient proof of transferable control, and some nonprofit operating assets or contracts may transfer without equity ownership.
- e: The injected LMM firm count is a margin-bridged ESTIMATE and is not re-estimated here.
- s5: The owner survey is cross-industry and self-reported, with no nature-park subsample.
- s5: A real-estate conveyance may not preserve a transferable operating service, while a concession or lease may change hands without the underlying land.
- s5: Internal restructurings and deaths without transferable operations are excluded.
- q: The only detailed six-digit revenue mix located is from 1997.
- q: Historic taxable firms may differ from today's eligible EBITDA-band operators in size, attraction type, and ancillary revenue.
- q: Savings may be required for conservation, safety, trail, or facility reinvestment rather than retained as distributable margin.
- d5: Outdoor-recreation output is far broader than 712190 and includes substantial supporting travel and hospitality activity.
- d5: NPS visitation measures public parks and counts visits, not private paid-service quantity or unique customers.
- d5: A single flood, fire, access failure, or ecological restriction can dominate demand for an individual site.
- o: This is bounded judgment, not a measured operator-required share.
- o: Operator intensity varies sharply between a guided cavern or wildlife sanctuary and a lightly serviced preserve.
- o: Digital self-guidance may reduce front-line labor without removing the accountable operating entity.

## Sources
- **S1** — [NAICS 712190 Nature Parks and Other Similar Institutions](https://www.census.gov/naics/resources/archives/sect71.html) (accessed 2026-07-22): Defines the industry as establishments preserving and exhibiting natural areas or settings, including sanctuaries, conservation areas, natural-wonder attractions, nature centers and preserves, and national parks.
- **S2** — [O*NET OnLine: Park Naturalists](https://www.onetonline.org/link/details/19-1031.03) (accessed 2026-07-22): Lists visitor service, facility operation, program scheduling and delivery, event planning, staff supervision, emergency duty, curriculum, displays, research, writing, records, photography, maintenance, animal care, and field-survey tasks.
- **S3** — [Generative AI and Jobs: A Refined Global Index of Occupational Exposure](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) (accessed 2026-07-22): Uses task evidence and expert validation to estimate GenAI exposure; finds clerical occupations most exposed while full automation remains limited, supporting task-level rather than whole-job interpretation.
- **S4** — [National Park Service Careers: Interpretation, Education, and Visitor Services](https://www.nps.gov/articles/000/nps-careers-interpretation.htm) (accessed 2026-07-22): Describes park work spanning visitor desks, calls, email, websites, fees, programs, trails, curricula, visual information, volunteers, scheduling, and in-person public engagement.
- **S5** — [Black Canyon Moves to Cashless Fee Collection](https://www.nps.gov/blca/learn/news/black-canyon-moves-cashless-fee-collection.htm?pubDate=20250415) (accessed 2026-07-22): Reports that electronic payment reduces transaction time and cash-processing work and that online entrance, camping, reservation, and permit payments are available across hundreds of federal recreation sites.
- **S6** — [Draft Recommendations: Strategies for Advancing Stewardship, Tourism, Conservation, and Partnerships](https://home.nps.gov/subjects/policy/upload/Tourism_Committee_Draft_Recommendations_12-2-2024.pdf) (accessed 2026-07-22): Describes digital visitor journeys, mobile and contactless service, AI-enabled data analysis, and constraints involving privacy, regulation, useful data, user preferences, and park-specific tailoring.
- **S7** — [Forest and Conservation Workers, Occupational Outlook Handbook](https://www.bls.gov/ooh/farming-fishing-and-forestry/forest-and-conservation-workers.htm) (accessed 2026-07-22): Documents physical conservation work including planting, trail and campground clearing, measuring trees, vegetation treatment, fire prevention and suppression, equipment maintenance, and cleaning public facilities.
- **S8** — [1997 Economic Census: Arts, Entertainment, and Recreation Subject Series Summary](https://www2.census.gov/library/publications/economic-census/1997/arts-entertainment-recreation-industries/97s71-sm.pdf) (accessed 2026-07-22): For 712190, reports 166 taxable and 276 tax-exempt employer establishments; taxable receipts were 66.7% admissions, 6.9% food and beverage, 21.7% merchandise, and 4.6% other, while tax-exempt revenue included 33.8% memberships and 5.2% admissions.
- **S9** — [2023 National State of Owner Readiness Report](https://exit-planning-institute.org/hubfs/Member%20Center%20Resources/2023%20National%20State%20of%20Owner%20Readiness%20Report.pdf) (accessed 2026-07-22): Surveys 1,162 US business owners across more than 25 industries and reports that 49% want to exit within five years, with substantial family ownership and internal-exit preferences.
- **S10** — [NAPCS Product List for NAICS 712](https://www2.census.gov/library/reference/napcs/product-list/web_712_final_reformatted_edited_US012209.pdf) (accessed 2026-07-22): Defines 712190 admission products to include single and multiple tickets, season passes, guided-tour or bundled benefits, and access-oriented memberships, and separately defines cultural-institution memberships.
- **S11** — [Outdoor Recreation Economic Statistics, U.S. and States, 2024](https://www.bea.gov/news/2026/outdoor-recreation-economic-statistics-us-and-states-2024) (accessed 2026-07-22): Reports 2024 real outdoor-recreation GDP growth of 2.7%, real gross-output growth of 2.0%, employment growth of 1.1%, and the broader composition of conventional, other, and supporting outdoor activities.
- **S12** — [National Park Service Visitor Use Data](https://www.nps.gov/subjects/socialscience/visitor-use-statistics-dashboard.htm?pubDate=20260314) (accessed 2026-07-22): Reports 323 million National Park Service recreation visits in calendar 2025 and describes the annual and monthly historical visitor-use data series.
