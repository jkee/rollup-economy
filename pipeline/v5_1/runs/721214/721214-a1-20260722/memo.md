# 721214 — Recreational and Vacation Camps (except Campgrounds)

*v5.1 Stage 1 research memo. Run `721214-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.24 · L 2.05 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A sizable, higher-wage administrative and managerial layer sits beside a service whose physical core remains operator-required.
**Weakness:** Most establishments may not be transferable commercial targets, and direct evidence on completed camp control transfers is weak.

## Business-model lens
- Included: US lower-middle-market operators of overnight children's camps, family vacation camps, hunting and fishing camps, dude ranches, wilderness camps, and outdoor adventure retreats that sell bundled accommodation, food, equipment, and organized activities to external customers on a recurring or repeat basis.
- Excluded: RV parks and campgrounds; day-only and primarily instructional camps classified outside 721214; government-operated or captive programs; shells, internal units, and non-control financing vehicles; and operators outside the roughly $1 million to $10 million normalized EBITDA band.
- Customer and revenue model: Operators primarily charge households, groups, or sponsoring organizations fixed fees for a stay or session, with lodging, meals, equipment, and organized recreation bundled into the price. Repeat annual attendance and referrals matter, but revenue is seasonal and capacity-bound.
- Deviation from default lens: none

## Executive view
This is a physical, seasonal hospitality-and-recreation business with a meaningful but bounded administrative AI opportunity. The most credible gains are in reservations, communications, marketing, scheduling, bookkeeping support, and planning; the core service still depends on maintained sites, food, guides or counselors, and accountable safety. Firm availability is limited by nonprofit and affiliated ownership, while demand appears mature and roughly stable.

## How AI changes the work
AI can draft and triage parent or guest communications, extract registration and health-form data, prepare schedules, forecast staffing and supplies, support marketing, reconcile routine records, and standardize incident documentation. Human review remains necessary, and direct activity leadership, supervision, cleaning, cooking, maintenance, and emergency response dominate the non-exposed work.

## Value capture
Fixed session and stay fees provide room to retain initial labor savings. Over time, operators are likely to share value through restrained fee increases, scholarships, added programming, better communication, or competitive repricing, especially because affordability already limits participation for many families.

## Firm availability
The code contains independently owned commercial camps but also a large nonprofit, faith-based, school-affiliated, and organization-sponsored population. Cross-industry owner surveys show meaningful transfer intent, yet completed third-party camp control sales face family, culture, property, financing, licensing, and seasonality complications.

## Demand durability
The broader official industry outlook is flat, and parent research reveals both substantial participation and unmet interest. The in-person bundle is durable because customers buy a place, activities, food, community, and accountable care or guidance rather than information alone. Affordability, demographics, climate, insurance, and site capacity are the principal quantity risks.

## Risks and uncertainty
The largest evidence problem is population mismatch: federal occupation and projection data combine camps with RV parks, while the richest ownership and customer research emphasizes youth programs and often includes day camps outside 721214. Sparse transaction data, separate real-estate ownership, nonprofit structures, seasonal payroll, and extreme weather make transfer and demand estimates especially uncertain. AI errors involving minors, health data, or safety could also create outsized liability and reputational harm.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3735 | — | OBSERVED | — |
| n | — | 155 | — | ESTIMATE | — |
| a | 0.18 | 0.25 | 0.33 | PROXY | S1, S2 |
| rho | 0.38 | 0.55 | 0.7 | ESTIMATE | S3 |
| e | 0.2 | 0.32 | 0.46 | PROXY | S5, S8 |
| s5 | 0.08 | 0.16 | 0.24 | PROXY | S4, S6 |
| q | 0.4 | 0.6 | 0.77 | ESTIMATE | S5, S7 |
| d5 | 0.88 | 1 | 1.12 | PROXY | S7, S9 |
| o | 0.88 | 0.94 | 0.98 | PROXY | S2, S5, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.02 | 2.05 | 3.45 | ESTIMATE |
| F | 2.01 | 3.52 | 4.66 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.74 | 9.40 | 10.00 | PROXY |

## Caveats
- a: The available occupation and wage mix combines 721214 camps with 721211 RV parks and campgrounds.
- a: Task exposure is researcher-classified rather than directly observed, and seasonal workers may be incompletely represented.
- a: The estimate excludes tasks already automated by existing registration, payment, and scheduling systems.
- rho: The digital-adoption source is sponsored content and does not document its underlying sample or measure production AI outcomes.
- rho: Implementation may occur mainly as avoided seasonal hiring rather than layoffs, which makes realized substitution difficult to observe.
- rho: Safety, child privacy, and reputational constraints can keep human review intensive even when drafting is automated.
- e: ACA-accredited youth camps are not representative of all NAICS 721214 establishments, especially adult retreat and adventure operators.
- e: Legal nonprofit status does not by itself determine whether an operating business or its assets can undergo a qualifying control transfer.
- e: The frozen firm count is an estimate and may classify affiliations or multi-site operators differently from the evidence sources.
- s5: The Gallup survey covers all employer industries and measures intentions rather than completed deals.
- s5: Family gifts, leadership changes without control, property-only sales, and closures are not qualifying transfers here.
- s5: A small number of multi-camp portfolio transactions can distort apparent deal flow.
- q: The strongest pricing evidence concerns youth camps and summer programs, while 721214 also contains adult vacation and adventure products.
- q: Published fees do not reveal negotiated group rates, discounts, scholarships, or quality reinvestment.
- q: Capacity constraints can increase retention at full camps, whereas price-sensitive local markets can force faster sharing.
- d5: The BLS projection covers RV parks and campgrounds together with recreational camps and forecasts labor, not output quantity.
- d5: Gallup covers structured K-12 summer programs, many of which are day programs outside 721214.
- d5: Climate events, insurance availability, and site-specific capacity can produce outcomes far from national averages.
- o: Youth camps require more direct supervision than adult hunting, fishing, dude-ranch, and adventure-retreat segments.
- o: The estimate concerns the operator requirement for the service quantity, not the number of employees needed after automation.
- o: Some low-contact lodging and information services can migrate to self-service even though the overall experience remains physical.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 721200](https://www.bls.gov/oes/2023/may/naics4_721200.htm) (accessed 2026-07-22): Fetched page reports employment shares and mean wages by occupation for RV parks and recreational camps, including management, office support, recreation, food, grounds, and maintenance occupations.
- **S2** — [O*NET OnLine: Recreation Workers](https://www.onetonline.org/link/details/39-9032.00) (accessed 2026-07-22): Fetched page describes recreation-worker tasks and work context, including organized activities, rules, safety, and the current degree of automation.
- **S3** — [From Campfires to Coding: The Tech Trends Shaping Modern Camps](https://www.acacamps.org/blog/sponsored/campfires-coding-tech-trends-shaping-modern-camps) (accessed 2026-07-22): Fetched sponsored article reports broad digital-tool use among camps and gives concrete examples of online registration, chatbots, scheduling, staffing, and program-management workflows.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fetched Gallup page reports owner age, five-year sale or transfer plans, closure plans, and survey methods for US employer and nonemployer business owners.
- **S5** — [Shaping Summertime Experiences: Summertime Experiences Provided Across Agents](https://www.ncbi.nlm.nih.gov/books/NBK552662/?report=reader) (accessed 2026-07-22): Fetched National Academies chapter reports camp provider types, nonprofit prevalence, fee-based revenue, session characteristics, capacity, scholarships, and round-the-clock responsibility in overnight youth camps.
- **S6** — [Bad Blood? How to Succeed at Succession — Who Wins and Who Loses](https://www.acacamps.org/article/camping-magazine/bad-blood-how-succeed-succession-who-wins-who-loses) (accessed 2026-07-22): Fetched American Camp Association article documents family ownership, leadership succession, cultural continuity, and practical sources of friction in camp transitions.
- **S7** — [In U.S., 45% of Children Lack Summer Learning Opportunities](https://news.gallup.com/poll/647015/children-lack-summer-learning-opportunities.aspx) (accessed 2026-07-22): Fetched Gallup page reports 2023 summer-program participation, desired additional participation, and cost barriers from a 2024 probability-panel survey of US K-12 parents.
- **S8** — [2002 Economic Census: Accommodation and Food Services, NAICS 721214 Definition](https://www2.census.gov/library/publications/economic-census/2002/accomodation-food-services/geographic-area-series/ec0272anh.pdf) (accessed 2026-07-22): Fetched Census publication defines 721214 as overnight recreational camps including children's and family camps, hunting and fishing camps, and adventure retreats with accommodations, food, equipment, and organized activities.
- **S9** — [BLS National Employment Matrix: RV Parks and Recreational Camps](https://data.bls.gov/projections/nationalMatrix?ioType=i&queryParams=721200) (accessed 2026-07-22): Fetched BLS matrix reports total 721200 employment of 73.2 thousand in 2024 and 73.7 thousand projected in 2034, a 0.7% increase, and gives occupation distributions.
