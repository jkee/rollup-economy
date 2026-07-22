# 311920 — Coffee and Tea Manufacturing

*v5.1 Stage 1 research memo. Run `311920-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.20 · L 0.50 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Habitual category demand and qualification-heavy custom programs support repeat outsourced production relationships.
**Weakness:** Eligibility is unmeasured, and most roasting, packing, sanitation, and material-handling labor is physical rather than AI-substitutable.

## Business-model lens
- Included: US lower-middle-market coffee roasters and tea blenders that repeatedly provide contract roasting, blending, grinding, private-label manufacturing, co-packing, custom packaging, and related fulfillment to external retailers, cafés, restaurants, hospitality programs, distributors, and consumer brands.
- Excluded: Retail cafés, proprietary consumer brands without material outsourced-production revenue, captive plants, green-bean importers without manufacturing, bottled ready-to-drink beverage plants classified elsewhere, shells, non-control financing vehicles, and firms outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: Repeat B2B orders under wholesale, private-label, toll-roasting, contract-manufacturing, and co-packing arrangements, typically priced per pound, case, capsule, package, or production run, sometimes bundled with sourcing, formulation, certification, packaging, and fulfillment.
- Deviation from default lens: NAICS 311920 contains proprietary-brand manufacturers as well as outsourced roasters and blenders. The lens is narrowed to firms with recurring custom, wholesale-program, contract, co-packing, or private-label production for external customers so the screened activity is a coherent outsourced service.

## Executive view
The relevant subset is contract and private-label roasting, blending, and packaging, not coffee and tea manufacturing in general. Demand is habitual and physical production remains necessary, while differentiated blends and certifications create customer stickiness; however, the true eligible share is unknown and plant work is mainly physical.

## How AI changes the work
AI is most applicable to order intake, roast and packing schedules, green-coffee purchasing analysis, forecasting, specification and label drafting, quality-record review, maintenance triage, customer service, and administration. Roasting, blending, sanitation, packing, warehousing, sensory approval, and food-safety accountability continue to require equipment and people.

## Value capture
Custom profiles, sourcing, packaging qualification, certifications, and dependable service can preserve savings through a contract term and deter switching. Customer bids, commodity-cost transparency, indexation, and retailer or hospitality buyer power can recapture those gains at renewal.

## Firm availability
Many public operator examples confirm that contract roasting and private label are established services, but no source measures their share of the 311920 LMM population. Broad manufacturing owner-age data imply succession supply, tempered by the low completion rate of businesses brought to market.

## Demand durability
Coffee participation has remained high and stable since 2022, specialty participation has increased, and tea retains very broad household reach. Mature penetration and format shifts constrain growth, yet the service still requires physical roasting or blending, packaging, traceability, and release by an accountable operator.

## Risks and uncertainty
Green-coffee and tea-price volatility, tariffs and import disruptions, crop and climate shocks, customer concentration, certification failures, recalls, stale inventory, and sensory inconsistency can overwhelm labor savings. The eligible-firm share, contract pass-through, and plant-specific data readiness need direct diligence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1308 | — | OBSERVED | — |
| n | — | 147 | — | ESTIMATE | — |
| a | 0.12 | 0.19 | 0.28 | PROXY | S2, S3 |
| rho | 0.3 | 0.5 | 0.7 | ESTIMATE | S4, S10 |
| e | 0.2 | 0.38 | 0.55 | ESTIMATE | S1, S5, S6, S7 |
| s5 | 0.14 | 0.24 | 0.36 | PROXY | S8, S9 |
| q | 0.42 | 0.65 | 0.82 | ESTIMATE | S5, S6, S7 |
| d5 | 0.96 | 1.06 | 1.18 | PROXY | S11, S12 |
| o | 0.92 | 0.97 | 1 | PROXY | S4, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.19 | 0.50 | 1.03 | ESTIMATE |
| F | 2.63 | 4.29 | 5.48 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 8.83 | 10.00 | 10.00 | PROXY |

## Caveats
- a: The occupational proxy covers all NAICS 3119 and may differ materially from small coffee and tea plants.
- a: Conventional automated roasters, fillers, and palletizers already in use are excluded from the not-yet-automated AI opportunity.
- rho: No public source measures five-year AI implementation in the lens population.
- rho: Small specialty plants may lack clean data and integration staff; larger private-label plants may implement materially faster.
- e: Operator websites prove the business model exists but do not measure its prevalence.
- e: Many firms mix eligible wholesale/private-label revenue with proprietary-brand sales.
- e: The broad NAICS code also includes concentrates and extracts whose contract structure may differ from roasting.
- s5: The 62.4% figure is for all manufacturing owners and comes from data year 2020.
- s5: The sell-intent statistic is Washington-specific and not industry-specific.
- s5: Internal succession and minority investments are excluded even when publicly announced.
- q: No public evidence quantifies contractual pass-through for LMM coffee and tea co-manufacturers.
- q: Retention should be lower in toll roasting with customer-owned beans and higher in differentiated full-service programs.
- d5: Trade-association surveys may have sponsor and sampling limitations.
- d5: Tea data are for 2023 and include channels and formats not necessarily manufactured by the lens firms.
- d5: Demand is held constant for price and quality and is not a nominal sales forecast.
- o: Regulation establishes facility accountability but does not ensure the same independent firm keeps the work.
- o: Customer insourcing, direct-to-consumer micro-roasting, or consolidation into larger manufacturers can reduce demand for lens operators.

## Sources
- **S1** — [NAICS 311920 Coffee and Tea Manufacturing definition](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Census defines the industry to include coffee roasting, coffee and tea concentrates, tea blending, herbal tea, and coffee extracts, flavorings, and syrups, while bottled or canned iced tea is classified elsewhere.
- **S2** — [Largest Occupations in Other Food Manufacturing, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): BLS lists packaging-machine operators (31,240), food batchmakers (30,470), material movers (16,180), hand packers (11,280), and production supervisors (9,850) as the five largest occupations in NAICS 3119.
- **S3** — [Industry-occupation matrix data by industry](https://www.bls.gov/emp/tables/industry-occupation-matrix-industry.htm) (accessed 2026-07-22): BLS publishes occupation matrices for Other Food Manufacturing at the 311900 level, confirming that detailed public occupational projections are broader than 311920.
- **S4** — [FSMA Final Rule for Preventive Controls for Human Food](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food) (accessed 2026-07-22): FDA states covered facilities must implement written food-safety plans with hazard analysis and risk-based preventive controls and ensure food workers are qualified for their duties.
- **S5** — [Copan Coffee Roasters Manufacturing Services](https://www.copancoffeeroasters.com/pages/manufacturing-services) (accessed 2026-07-22): A US operator offers full-service private-label coffee manufacturing from green-bean sourcing through roasting, blending, packaging, custom blends, and wholesale programs.
- **S6** — [McCullagh Coffee Roasters Contract Roasting and Packaging](https://www.mccullaghcoffee.com/pages/contract-roasting) (accessed 2026-07-22): A US roaster offers private-label cups, bags, filter packs, proprietary roast-profile development, customer-supplied coffee co-packing, and contract manufacturing.
- **S7** — [Joe's Garage Coffee Contract Manufacturing](https://joesgaragecoffee.com/services/contract-manufacturing/) (accessed 2026-07-22): A contract manufacturer describes multi-location private-label programs, co-packaging in pods, bags, and portion packs, and FDA-registered, certified production.
- **S8** — [The Metamorphosis of Women Business Owners: A Focus on Age](https://www2.census.gov/ces/wp/2024/CES-WP-24-71.pdf) (accessed 2026-07-22): A Census working paper using 2021 ABS data reports that 62.4% of manufacturing employer-business owners were age 55 or older.
- **S9** — [New Research Details Effects of Silver Tsunami on Local Washington Economies](https://project-equity.org/press-releases/new-research-details-effects-of-silver-tsunami-on-local-washington-economies-and-what-to-do-about-it/) (accessed 2026-07-22): Project Equity reports six in ten Washington owners planned to sell within a decade, roughly 15% pass to family, one-third of owners over 50 had trouble finding a buyer, and only 20% of listed companies sold.
- **S10** — [Registration of Food Facilities and Other Submissions](https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/registration-food-facilities-and-other-submissions) (accessed 2026-07-22): FDA states facilities manufacturing, processing, packing, or holding food for US consumption generally must register, permit inspection, and renew registration every other year.
- **S11** — [Coffee Tops Americans' Beverage Choices](https://www.ncausa.org/Newsroom/Coffee-tops-Americans-beverage-choices) (accessed 2026-07-22): NCA's Spring 2026 nationally representative survey of 1,850 adults reports past-day and past-week coffee participation unchanged since 2022 at 66% and 73%; specialty weekly participation rose from 53% to 58%.
- **S12** — [Tea Association of the USA Fact Sheet 2024](https://teausa.org/teausa/images/Tea_Association_Fact_Sheet_2024.pdf) (accessed 2026-07-22): The Tea Association reports almost 86 billion US tea servings, or nearly 4 billion gallons, in 2023; tea appears in more than 80% of US households and 75-80% of US tea is consumed iced.
