# 484220 — Specialized Freight (except Used Goods) Trucking, Local

*v5.1 Stage 1 research memo. Run `484220-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.67 · L 1.35 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large fragmented operating base performs repeat freight movements with document-heavy dispatch and billing workflows around an enduring physical service.
**Weakness:** Most wages remain tied to drivers and field operations, while pricing competition and cargo-cycle volatility can dissipate or obscure digital-work savings.

## Business-model lens
- Included: Independent local carriers using specialized vehicles or handling processes to transport freight other than used household and office goods, generally within a metropolitan area with same-day return, for external commercial customers.
- Excluded: Captive private fleets, pure brokers, owner-operators without a transferable operating organization, waste collection, general freight trucking, used-goods movers, and financing or shell entities.
- Customer and revenue model: Commercial and industrial shippers buy recurring or repeat local haulage by trip, hour, load, ton, mile, route, or negotiated contract, often with fuel and accessorial charges; the cargo and equipment vary but dispatch, compliance, fleet, and driver workflows are shared.
- Deviation from default lens: none

## Executive view
Local specialized trucking combines a durable need for physical, regulated operators with an addressable layer of dispatch, pricing, paperwork, billing, and customer-service labor. The opportunity is operational rather than driverless: AI can improve coordination around trucks and crews while the carrier remains responsible for the load.

## How AI changes the work
Useful applications include order intake, load classification, quote support, schedule and route suggestions, document extraction, proof-of-delivery processing, invoice reconciliation, safety-file review, exception messaging, and collections. Physical equipment operation and cargo-specific decisions limit substitution of drivers and field staff.

## Value capture
Savings can remain with the carrier during fixed-rate contract periods or when scarce equipment and reliability support pricing. Procurement rebids, rate transparency, fuel formulas, and competitive capacity progressively share gains with shippers.

## Firm availability
The census profile shows 32,207 employer establishments in 2023, confirming a broad operating base, but establishments are not firms and the frozen LMM estimate needs roster validation. Transferable candidates must have real authority, equipment access, management depth, customer relationships, and compliance systems rather than a driver-owned job or broker shell.

## Demand durability
National freight flows are forecast to grow and trucks remain the dominant tonnage mode. Local specialized demand should persist because physical commodities must move between sites, though the mix is exposed to construction, industrial, agricultural, and energy cycles.

## Risks and uncertainty
The code contains varied cargo and equipment niches, so a single average obscures segment economics. Safety incidents, insurance, driver availability, equipment utilization, maintenance, permits, fuel volatility, customer concentration, and misclassification can overwhelm back-office gains. Direct evidence on AI implementation, private transfers, and benefit pass-through is sparse.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3091 | — | OBSERVED | — |
| n | — | 2317 | — | ESTIMATE | — |
| a | 0.13 | 0.21 | 0.31 | PROXY | S1, S2, S3, S4 |
| rho | 0.34 | 0.52 | 0.7 | ESTIMATE | S3, S4, S5 |
| e | 0.62 | 0.78 | 0.9 | ESTIMATE | S1, S6, S7 |
| s5 | 0.12 | 0.18 | 0.27 | PROXY | S8 |
| q | 0.38 | 0.55 | 0.72 | ESTIMATE | S1, S5 |
| d5 | 0.98 | 1.06 | 1.15 | PROXY | S5, S9, S10 |
| o | 0.9 | 0.96 | 0.99 | PROXY | S1, S4, S11 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.55 | 1.35 | 2.68 | ESTIMATE |
| F | 8.29 | 9.31 | 10.00 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.82 | 10.00 | 10.00 | PROXY |

## Caveats
- a: No fetched source measures wage-weighted AI exposure for NAICS 484220.
- a: Cargo segments such as bulk liquids, construction materials, refrigerated goods, and heavy equipment have different field and office task mixes.
- a: Owner-operators often combine driving and administrative work in one role.
- rho: Observed productivity growth does not isolate AI or prove labor substitution.
- rho: Implementation can increase service quality or fleet utilization without reducing labor.
- rho: Compliance and safety decisions remain accountable to people and the carrier.
- e: The frozen firm count is margin-bridged and may include firms outside the intended EBITDA band.
- e: FMCSA files cover regulated entities and do not cleanly identify NAICS or transferable enterprise value.
- e: Eligibility varies materially by cargo niche and contract structure.
- s5: The Census statistic is all-industry and based on 2018 responding owners.
- s5: A carrier can sell assets without transferring an operating company.
- s5: Small private deals are underreported in commercial transaction databases.
- q: No public source directly measures pass-through of AI savings in local specialized trucking.
- q: Pricing differs across dedicated routes, project hauling, emergency work, and commodity-linked activity.
- q: The estimate excludes demand and implementation effects.
- d5: The national freight forecast is a broad multimodal proxy, not an industry revenue forecast.
- d5: Tonnage does not equal constant-quality service quantity when haul distance, payload, or specialized handling changes.
- d5: Construction and resource-linked segments can diverge sharply from aggregate freight.
- o: Automation technology can progress nonlinearly after the older GAO study.
- o: The primitive concerns the accountable operating firm, not the number of drivers.
- o: Closed-site or fixed-route segments could automate sooner than mixed-road local hauling.

## Sources
- **S1** — [484220: Specialized freight (except used goods) trucking, local - Census Bureau Profile](https://data.census.gov/profile/484220_-_Specialized_freight_%28except_used_goods%29_trucking%2C_local?codeset=naics~484220&g=010XX00US) (accessed 2026-07-22): Defines local specialized trucking as metropolitan-area service generally returning the same day and reports 32,207 employer establishments for 2023.
- **S2** — [National Industry-Specific Occupational Employment and Wage Estimates: Specialized Freight Trucking](https://www.bls.gov/oes/2016/may/naics4_484200.htm) (accessed 2026-07-22): Provides occupational employment and wage structure for the broader specialized-freight industry, used only as an occupation-mix proxy.
- **S3** — [Generative AI and Jobs: A Refined Global Index of Occupational Exposure](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) (accessed 2026-07-22): Provides task-level GenAI exposure methodology and finds clerical occupations most exposed while job transformation is more likely than complete replacement.
- **S4** — [Anthropic Economic Index report: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report) (accessed 2026-07-22): Reports that transportation and material-moving occupations are underrepresented in observed Claude use and its user survey.
- **S5** — [One-year percent change in hours and output, and current employment level](https://www.bls.gov/charts/productivity-service-providing-industries/1-year-percent-change-hours-and-output-and-employment.htm) (accessed 2026-07-22): Reports 2024 specialized-freight-trucking hours down 1.9%, output up 1.0%, and employment of 468,100 for the broader industry.
- **S6** — [FMCSA Open Data Program](https://www.fmcsa.dot.gov/registration/fmcsa-data-dissemination-program) (accessed 2026-07-22): Identifies the Company Census File and monthly motor-carrier census data containing regulated-entity, equipment, driver, and operating information for firm-level diligence.
- **S7** — [FMCSA Registration Statistics](https://ai.fmcsa.dot.gov/RegistrationStatistics?os=av) (accessed 2026-07-22): Provides current registration data for motor carriers, brokers, and freight forwarders and distinguishes operating entities from arrangers.
- **S8** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding employer-business owners were age 55 or older in the 2019 Annual Business Survey for data year 2018.
- **S9** — [Freight Activity in the U.S. Expected to Grow Fifty Percent by 2050](https://www.bts.gov/newsroom/freight-activity-us-expected-grow-fifty-percent-2050) (accessed 2026-07-22): Reports FAF projections of 50% growth in US freight tonnage from 2020 to 2050 and that trucks carry 65% of US freight tonnage.
- **S10** — [Freight Analysis Framework](https://www.bts.gov/faf) (accessed 2026-07-22): Describes FAF estimates by weight, value, activity, commodity, mode, geography, and forecast scenario, including data through 2050.
- **S11** — [Automated Trucking: Federal Agencies Should Take Additional Steps to Prepare for Potential Workforce Effects](https://www.gao.gov/products/gao-19-161) (accessed 2026-07-22): Reports that widespread automated-truck deployment was expected to remain years or decades away and that some workforce scenarios retain operators.
