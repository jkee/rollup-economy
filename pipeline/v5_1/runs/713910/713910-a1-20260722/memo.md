# 713910 — Golf Courses and Country Clubs

*v5.1 Stage 1 research memo. Run `713910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.44 · L 2.68 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A durable physical service with direct pricing and repeat customers supports retention of targeted administrative and scheduling automation benefits.
**Weakness:** Most labor is physical or high-touch, while eligible-firm share and qualifying control-transfer probability are poorly observed.

## Business-model lens
- Included: Independently controlled, for-profit golf-course and country-club operators serving repeat golfers or members through green fees, memberships, dues, instruction, events, food and beverage, and related facility services.
- Excluded: Municipally owned facilities, member-owned nonprofit clubs, captive resort or residential-development amenities, shells, internal operating units, and financing vehicles.
- Customer and revenue model: Direct-to-consumer repeat play and recurring membership revenue, supplemented by cart rental, instruction, events, food and beverage, and pro-shop sales; pricing is posted, seasonal, membership-based, or dynamically adjusted by tee-time demand.
- Deviation from default lens: The NAICS population mixes commercial daily-fee operators with municipal, nonprofit member-owned, resort-captive, and residential-amenity facilities whose transferability and objectives are fundamentally different. The lens therefore keeps only independently controlled for-profit operators while retaining both repeat-fee and membership models.

## Executive view
Golf operators combine a durable physical venue with repeat direct-to-consumer demand. The practical AI opportunity is concentrated in administrative interruption, customer communications, yield management and selected repetitive grounds tasks, not the core hospitality and agronomy workforce. Transferability is meaningful only after removing municipal, nonprofit and captive facilities, and the available ownership evidence is weak.

## How AI changes the work
AI phone agents, member communications, marketing content, reporting, scheduling and tee-sheet analytics can reduce interruptions and avoid incremental hiring. Autonomous mowing can take repetitive work, but skilled staff remain necessary for greens, bunkers, weather response, safety and presentation. The broad recreation occupation mix supports a moderate ceiling because food service, grounds work and in-person recreation dominate many facilities.

## Value capture
Direct posted pricing and dues allow savings to remain with the operator initially, with no contractual pass-through. Over time, competing courses, member renewal pressure, discounting of perishable tee times and required reinvestment share part of the benefit with customers. Strong local capacity utilization improves capture; weak or seasonal markets reduce it.

## Firm availability
Commercial courses change hands and an aging owner population creates succession pressure, but public data do not reveal a qualifying transfer rate. Municipal ownership, member nonprofits, captive resorts and multi-site platforms materially shrink the eligible firm set, while property value, deferred maintenance and environmental diligence complicate transactions.

## Demand durability
US rounds have remained above 500 million for six consecutive years and participation has broadened, supporting a near-flat to modestly growing five-year real demand base. The downside is material because golf is discretionary, weather-sensitive, land-intensive and exposed to affordability constraints. Digital off-course formats are more likely to complement or modestly substitute than eliminate green-grass play.

## Risks and uncertainty
The largest evidence gaps are golf-specific occupational wages, technology penetration and a denominator-based transaction history. NAICS 713900 proxies include other recreation businesses, AI adoption evidence is selected and small, and facility counts do not map cleanly to firms. Deferred course capital, water regulation, climate, insurance and local land economics can overwhelm operating savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4607 | — | OBSERVED | — |
| n | — | 696 | — | ESTIMATE | — |
| a | 0.18 | 0.28 | 0.4 | PROXY | S1, S2, S3 |
| rho | 0.32 | 0.52 | 0.7 | PROXY | S2, S3, S4 |
| e | 0.42 | 0.58 | 0.72 | PROXY | S5, S6 |
| s5 | 0.13 | 0.24 | 0.36 | PROXY | S7, S8 |
| q | 0.48 | 0.68 | 0.84 | ESTIMATE | S9 |
| d5 | 0.88 | 1.02 | 1.13 | PROXY | S5 |
| o | 0.9 | 0.95 | 0.99 | ESTIMATE | S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.06 | 2.68 | 5.16 | PROXY |
| F | 5.89 | 7.37 | 8.37 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.92 | 9.69 | 10.00 | ESTIMATE |

## Caveats
- a: The available federal occupation table is for NAICS 713900, which includes fitness centers and other recreation businesses as well as golf.
- a: The AI-phone survey covered current product users and did not disclose a sample size, creating selection and vendor-adjacent bias.
- a: Robotic-mower adoption evidence is from the UK and Ireland and includes conventional autonomy enhanced by AI, not purely generative AI.
- rho: Current-adopter results are not representative penetration data.
- rho: Capital replacement cycles for turf equipment can push implementation beyond five years.
- rho: Member experience, safety and agronomic judgment constrain unattended operation.
- e: Course, facility, establishment and firm are different units.
- e: Public accessibility does not imply private ownership.
- e: The frozen LMM-band count is an estimate and may be distorted by real-estate-heavy or nonprofit economics.
- s5: The owner-age statistic is all-industry and vintage 2018.
- s5: The NGF transaction page confirms transaction tracking but exposes no count or denominator.
- s5: A course real-estate sale is not always a qualifying transfer of an operating firm.
- q: No source directly measures retained AI benefit.
- q: Capture differs sharply between waitlisted private clubs, competitive daily-fee courses and seasonal markets.
- q: Some labor savings may be reinvested in service or maintenance rather than retained as cash benefit.
- d5: Rounds are utilization, not a constant-price demand curve.
- d5: National growth can conceal local oversupply or weather deterioration.
- d5: The eligible for-profit LMM subset may not track all US facilities.
- o: The estimate separates operator necessity from labor intensity; a highly automated course still has an accountable operator.
- o: Technology-enabled off-course golf may either substitute for or recruit customers into green-grass golf.
- o: Climate or land-use constraints could eliminate facilities independently of software substitution.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 713900](https://www.bls.gov/oes/2023/may/naics4_713900.htm) (accessed 2026-07-22): Broader recreation occupation mix: office and administrative support 10.37% of employment, food preparation and serving 16.47%, building and grounds maintenance 9.91%, plus management and sales shares and wages used to bound wage-weighted AI task exposure.
- **S2** — [AI in Golf Ops: Why Innovators Lead While Operators Lag](https://www.golfcoursetechnologyreviews.org/blog/ai-was-not-the-headline-in-these-conversations-that-might-be-the-point) (accessed 2026-07-22): 2026 survey of facilities using AI telephone management: all respondents reported weekly time savings; 60% reported four to six hours and 40% one to three hours, while the article emphasizes interruption absorption rather than staff replacement.
- **S3** — [How Robot Mowers Are Transforming Golf Courses](https://www.golfmonthly.com/features/golf-monthly/how-robot-mowers-are-transforming-golf-courses) (accessed 2026-07-22): Reports around 150 UK and Ireland clubs using one vendor's robotic mowers and describes repetitive mowing automation, continued skilled greenkeeper tasks, and an AI vision accessory for obstacle avoidance.
- **S4** — [A Survey of Current and Future Challenges Facing the Golf Course Maintenance Industry](https://www.usga.org/content/usga/home-page/course-care/green-section-record/63/issue-02/what-are-the-biggest-challenges-facing-the-golf-course-maintenan.html) (accessed 2026-07-22): USGA survey reports lack of qualified and skilled labor as a leading current and future superintendent concern, supporting adoption incentive while underscoring skill constraints.
- **S5** — [Golf Industry Facts](https://www.ngf.org/the-clubhouse/golf-industry-research/) (accessed 2026-07-22): NGF reports more than 500 million US rounds in each of the past six years, 2025 rounds 21% above the 2015-2019 average, about 14,000 facilities, roughly three-quarters public accessibility, and substantial latent demand and participation breadth.
- **S6** — [Which Way is Municipal Golf Going?](https://www.ngf.org/short-game/which-way-is-municipal-golf-going/) (accessed 2026-07-22): NGF reports 2,939 municipal courses in 2024, just over 18% of US course supply, and explains municipal acquisitions, public-service objectives and nonstandard accounting.
- **S7** — [Annual Business Survey Visualizations](https://www.census.gov/programs-surveys/abs/library/visualizations.html) (accessed 2026-07-22): Census states that over half of US business owners were age 55 and over in the 2019 ABS, a cross-industry succession-pressure proxy.
- **S8** — [National Golf Foundation New Owner Leads](https://secure.ngf.org/pages/ccnewowner.asp) (accessed 2026-07-22): Confirms NGF tracks recently transacted US golf courses under new ownership and records facility details and estimated transaction dates, but publishes no transaction count or denominator.
- **S9** — [The Truth About Golf's Rising Green Fees](https://www.ngf.org/short-game/the-truth-about-golfs-rising-green-fees/) (accessed 2026-07-22): NGF reports peak public playing fees rose about 29% from 2019-2025 versus 27% cumulative inflation, an approximately $41 average municipal/daily-fee 18-hole price, and widespread seasonal and dynamic pricing.
