# 484230 — Specialized Freight (except Used Goods) Trucking, Long-Distance

*v5.1 Stage 1 research memo. Run `484230-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.23 · L 0.99 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat, document-intensive freight operations offer back-office automation today and selective highway-driving automation over time while cargo remains physically anchored.
**Weakness:** The largest theoretical exposure is driving, but specialized cargo and deployment constraints make its five-year implementation and retained economics unusually uncertain.

## Business-model lens
- Included: Independent carriers transporting specialized freight other than used household and office goods between metropolitan areas, including cross-border North American routes, with their own operating organization and responsibility for vehicles, cargo, safety, and service.
- Excluded: Captive private fleets, pure brokers and dispatch-only firms, general freight carriers, used-goods movers, independent drivers without a transferable operating organization, and financing or shell entities.
- Customer and revenue model: Commercial shippers buy repeat or contracted long-distance transport of cargo requiring flatbeds, tankers, refrigerated trailers, auto carriers, livestock or other specialized equipment, priced by load, mile, ton, lane, dedicated capacity, or negotiated contract with fuel and accessorial adjustments.
- Deviation from default lens: none

## Executive view
Long-distance specialized trucking has two AI opportunity layers: near-term digital coordination and a larger but harder-to-implement exposure in highway driving. Specialized cargo keeps the service operator-intensive and regulated, so the credible five-year case depends more on back-office execution and selective route automation than universal driver removal.

## How AI changes the work
AI can assist quoting, lane selection, dispatch, route and fuel planning, document extraction, ELD and safety review, billing, collections, and customer exceptions. Driving automation could cover selected highway segments, but securement, loading interfaces, inspections, border activity, weather, emergencies, and cargo-specific obligations still require people and accountable processes.

## Value capture
Dedicated routes and specialized capabilities can retain gains during contract periods. Freight procurement is nevertheless benchmarked and frequently rebid, so brokers, shippers, and competing capacity are likely to capture a material share of savings over five years.

## Firm availability
Census reports 10,701 firms and 12,372 establishments in the 2022 Economic Census for the industry, and the frozen LMM estimate indicates a meaningful candidate pool. Those totals do not establish eligibility: real targets need durable authority, insurance, equipment access, compliance, management, drivers, and customer relationships beyond the owner.

## Demand durability
Freight projections and driver demand support continued physical interregional movement. The cargo mix is diverse and cyclical, but most of it cannot turn into software; even automated transport generally preserves the need for a carrier of record.

## Risks and uncertainty
Autonomy timing is highly uncertain and announcements may not translate into scaled, insured operations. Cargo concentration, commodity cycles, fuel, insurance, accidents, equipment residual values, driver turnover, regulation, border rules, maintenance, and shipper bargaining can swamp administrative savings. Direct data on AI labor effects, private transfers, and benefit pass-through are limited.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2143 | — | OBSERVED | — |
| n | — | 1036 | — | ESTIMATE | — |
| a | 0.21 | 0.32 | 0.46 | PROXY | S1, S2, S3, S4, S5 |
| rho | 0.18 | 0.36 | 0.55 | ESTIMATE | S3, S4, S6, S7 |
| e | 0.6 | 0.76 | 0.88 | ESTIMATE | S1, S8, S9 |
| s5 | 0.11 | 0.18 | 0.27 | PROXY | S10 |
| q | 0.32 | 0.5 | 0.69 | ESTIMATE | S11, S12 |
| d5 | 0.98 | 1.07 | 1.17 | PROXY | S1, S13, S14, S15 |
| o | 0.84 | 0.93 | 0.98 | PROXY | S1, S3, S4, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.32 | 0.99 | 2.17 | ESTIMATE |
| F | 6.82 | 7.98 | 8.86 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 8.23 | 9.95 | 10.00 | PROXY |

## Caveats
- a: Autonomous-driving capability is not equivalent to safe or lawful labor substitution.
- a: Cargo niches differ sharply in securement, inspection, temperature, hazardous-material, animal-welfare, and border requirements.
- a: The available specialized-freight occupational evidence is broader than this six-digit industry.
- rho: Government automation assessments predate some recent technical advances.
- rho: Pilot miles and announced routes do not establish scaled driver removal.
- rho: Efficiency may appear as more miles or better utilization rather than reduced headcount.
- e: The frozen count is margin-bridged and may misclassify firms around the EBITDA band.
- e: Census establishments are not firms, and FMCSA registrations are not proof of an active transferable enterprise.
- e: Transferability varies by whether value resides in contracts, permits, equipment, drivers, or the owner relationship.
- s5: The owner-age evidence covers all industries and reference year 2018.
- s5: An operating-authority or equipment transfer may not be a qualifying company control transfer.
- s5: Private trucking transactions are incompletely reported.
- q: Producer-price indexes show received-price movement, not causal pass-through of a specific productivity gain.
- q: Pricing power varies substantially across hazardous materials, refrigeration, autos, bulk products, livestock, and oversize loads.
- q: The estimate excludes implementation costs and demand effects.
- d5: Freight tonnage is not constant-quality specialized trucking service quantity.
- d5: The national driver forecast spans industries and does not isolate demand from labor supply or productivity.
- d5: Cross-border, energy, agricultural, and construction cycles can dominate particular fleets.
- o: The estimate is about the accountable operating firm rather than driver employment.
- o: Autonomous-network operators may still satisfy the lens even if traditional carriers lose the load.
- o: Regulatory approvals and insurance availability can change quickly and unevenly by state.

## Sources
- **S1** — [2022 NAICS Definition: 484230 Specialized Freight (except Used Goods) Trucking, Long-Distance](https://www.census.gov/naics/?details=484230&input=484230&year=2022) (accessed 2026-07-22): Defines long-distance specialized trucking between metropolitan areas, potentially across North American borders, and lists representative cargo and equipment niches.
- **S2** — [National Industry-Specific Occupational Employment and Wage Estimates: Specialized Freight Trucking](https://www.bls.gov/oes/2016/may/naics4_484200.htm) (accessed 2026-07-22): Provides employer-survey occupational employment and wage estimates for broader specialized freight trucking, used only as an occupation-mix proxy.
- **S3** — [Automated Trucking: Federal Agencies Should Take Additional Steps to Prepare for Potential Workforce Effects](https://www.gao.gov/products/gao-19-161) (accessed 2026-07-22): Finds automation development focused on long-haul trucking, describes driver-reducing and operator-retaining scenarios, and reports widespread deployment likely years or decades away.
- **S4** — [Preliminary Analysis of Potential Workforce Impacts Report](https://www.transportation.gov/av/workforce/report) (accessed 2026-07-22): Provides the US DOT report framework for driving-automation effects in long-haul trucking and bus transit.
- **S5** — [Generative AI and Jobs: A Refined Global Index of Occupational Exposure](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) (accessed 2026-07-22): Provides task-level GenAI exposure methodology, with clerical occupations most exposed and job transformation more likely than full replacement.
- **S6** — [ELD Carrier-Driver Training](https://www.fmcsa.dot.gov/hours-service/elds/eld-carrier-driver-training) (accessed 2026-07-22): Documents required ELD workflows, automatic engine and driving-time records, driver certification, and hours-of-service constraints relevant to implementation.
- **S7** — [Anthropic Economic Index report: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report) (accessed 2026-07-22): Reports that transportation and material-moving occupations are underrepresented in observed Claude use and its user survey.
- **S8** — [FMCSA Open Data Program](https://www.fmcsa.dot.gov/registration/fmcsa-data-dissemination-program) (accessed 2026-07-22): Identifies carrier census datasets with regulated-entity, business-operation, equipment, driver, and safety-review fields for diligence.
- **S9** — [2022 Economic Census Comparative Statistics for NAICS 484230](https://data.census.gov/table/ECNCOMP2022.EC2200COMP?codeset=naics~484230&g=010XX00US) (accessed 2026-07-22): Reports 10,701 firms and 12,372 establishments for NAICS 484230 in 2022, compared with 9,222 firms and 10,939 establishments in 2017.
- **S10** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding employer-business owners were age 55 or older in the 2019 Annual Business Survey for data year 2018.
- **S11** — [Producer Price Index by Industry: Specialized Freight (except Used Goods) Trucking, Long-Distance](https://fred.stlouisfed.org/series/PCU484230484230) (accessed 2026-07-22): Provides the monthly BLS producer-price index for prices received by NAICS 484230, including a May 2026 observation of 175.056 on a December 2003 base of 100.
- **S12** — [Producer Price Indices](https://www.bts.gov/archive/publications/transportation_economics_trends/tables/ch3/box3_1) (accessed 2026-07-22): Explains that trucking PPI measures average changes in selling prices received by producers and is revenue-weighted from establishment surveys.
- **S13** — [Freight Activity in the U.S. Expected to Grow Fifty Percent by 2050](https://www.bts.gov/newsroom/freight-activity-us-expected-grow-fifty-percent-2050) (accessed 2026-07-22): Reports FAF projections of 50% growth in US freight tonnage from 2020 to 2050 and that trucks carry 65% of freight tonnage.
- **S14** — [Freight Analysis Framework](https://www.bts.gov/faf) (accessed 2026-07-22): Describes US freight-flow estimates and forecasts by commodity, mode, origin-destination geography, tonnage, value, and ton-miles.
- **S15** — [Heavy and Tractor-trailer Truck Drivers](https://www.bls.gov/ooh/transportation-and-material-moving/heavy-and-tractor-trailer-truck-drivers.htm) (accessed 2026-07-22): Projects heavy and tractor-trailer driver employment to grow 4% from 2024 to 2034 and states that trucks carry most US freight.
