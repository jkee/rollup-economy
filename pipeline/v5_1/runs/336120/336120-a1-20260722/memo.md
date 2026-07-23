# 336120 — Heavy Duty Truck Manufacturing

*v5.1 Stage 1 research memo. Run `336120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.30 · L 0.43 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring fleet replacement and freight activity support a durable need for accountable manufacturers while AI improves the information workflows around complex builds.
**Weakness:** Very limited LMM eligibility and capital-intensive physical production constrain both availability and implementable labor opportunity.

## Business-model lens
- Included: US lower-middle-market establishments repeatedly manufacturing heavy-duty truck chassis, complete heavy-duty trucks, buses, heavy-duty motor homes, or special-purpose highway vehicles for external fleet, dealer, municipal, and commercial customers.
- Excluded: Large integrated OEMs outside the EBITDA band; captive plants; military armored vehicles; off-highway equipment; bodies assembled on purchased chassis; light trucks; distributors and repair-only businesses.
- Customer and revenue model: Repeat production and configured-order sales of capital equipment, generally through fleet contracts, dealers, or direct commercial and public-sector procurement; revenue is product and option pricing rather than hourly service billing.
- Deviation from default lens: none

## Executive view
Heavy-duty truck manufacturing has real document, engineering-support, planning, and commercial workflow opportunity, but the physical core is difficult to automate with AI and the genuinely eligible LMM firm pool appears narrow. Demand is necessary but highly cyclical and exposed to technology-transition execution.

## How AI changes the work
AI should first reduce labor in quote preparation, configuration checks, engineering-document search, supplier communication, production scheduling, warranty triage, and quality paperwork. Safety-critical design approval, skilled trades, assembly, paint, final test, and regulatory sign-off remain human- and equipment-intensive.

## Value capture
Configured products and temporary information advantages permit retention, but fleet procurement and repeated bids will share gains with customers. Proprietary specialty applications should retain more than standardized fleet configurations.

## Firm availability
The Census establishment count is small and establishment does not equal independent firm. Large OEM plants, captive units, certification burden, and fixed capital sharply constrain the transferable LMM population despite the injected estimate of 23 band firms.

## Demand durability
Freight growth and fleet replacement sustain the need for heavy trucks, while historic real output and monthly retail sales show pronounced cyclicality. Emissions rules create design and replacement activity but also add cost, infrastructure dependence, and powertrain uncertainty.

## Risks and uncertainty
Key risks are recession and freight-cycle drawdowns, customer concentration, warranty or recall exposure, working-capital demands, union and skilled-labor constraints, battery or hydrogen infrastructure delays, regulation changes, and an overestimated independent-firm denominator.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0979 | — | OBSERVED | — |
| n | — | 23 | — | ESTIMATE | — |
| a | 0.14 | 0.24 | 0.35 | PROXY | S2 |
| rho | 0.27 | 0.46 | 0.64 | ESTIMATE | S0, S3 |
| e | 0.05 | 0.13 | 0.25 | ESTIMATE | S1 |
| s5 | 0.1 | 0.21 | 0.34 | PROXY | S7 |
| q | 0.37 | 0.55 | 0.72 | ESTIMATE | — |
| d5 | 0.82 | 1.01 | 1.2 | PROXY | S4, S5, S6, S8 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S0, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.15 | 0.43 | 0.88 | ESTIMATE |
| F | 0.18 | 0.78 | 1.74 | ESTIMATE |
| C | 7.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.87 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is four-digit NAICS and 2023 vintage.
- a: Exposure is task judgment, not observed displacement.
- rho: No industry survey directly measures implemented AI opportunity.
- rho: Regulatory change may accelerate digital engineering while also increasing validation burden.
- e: The 109 figure is establishments, not firms.
- e: The injected n is margin-bridged and may be particularly fragile for this concentrated industry.
- s5: ABS owner age is cross-industry and does not observe transactions.
- s5: Strategic acquisitions may dominate reported deals and are not necessarily representative of LMM availability.
- q: No public evidence isolates AI-benefit pass-through.
- q: Retention varies sharply between proprietary specialty vehicles and competitively bid fleet trucks.
- d5: Historical output series ends in 2021.
- d5: Freight tonnage does not translate one-for-one into new-truck purchases.
- d5: Retail sales cover heavy-weight trucks broadly and not only domestic 336120 output.
- o: Consolidation or insourcing could remove some independent operators even though physical production persists.

## Sources
- **S0** — [2022 NAICS definition: 336120 Heavy Duty Truck Manufacturing](https://www.census.gov/naics/?input=336120&year=2022&details=336120) (accessed 2026-07-23): Industry scope and cross-references for heavy-duty chassis, complete trucks, buses, motor homes, and special-purpose highway vehicles.
- **S1** — [336120 Heavy duty truck manufacturing — Census Bureau Profile](https://data.census.gov/profile/336120_-_Heavy_duty_truck_manufacturing?codeset=naics~336120) (accessed 2026-07-23): The fetched profile states the industry definition and reports 109 employer establishments for 2023 CBP.
- **S2** — [May 2023 OEWS: Motor Vehicle Manufacturing](https://www.bls.gov/oes/2023/may/naics4_336100.htm) (accessed 2026-07-23): Broader-industry occupation mix; 286,420 total employment and presence of management, business, computer, engineering, sales, office, production, maintenance, and material-moving work.
- **S3** — [Final Rule: Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles — Phase 3](https://www.epa.gov/regulations-emissions-vehicles-and-engines/final-rule-greenhouse-gas-emissions-standards-heavy-duty) (accessed 2026-07-23): Standards phase in from model year 2027, cover vocational vehicles and tractors, and are technology-neutral and performance-based.
- **S4** — [Real Sectoral Output for Heavy Duty Truck Manufacturing](https://fred.stlouisfed.org/series/IPUEN336120T010000000) (accessed 2026-07-23): BLS/FRED annual real-output index values: 99.016 in 2019, 63.760 in 2020, and 71.647 in 2021.
- **S5** — [Motor Vehicle Retail Sales: Heavy Weight Trucks — Table Data](https://fred.stlouisfed.org/data/HTRUCKSSA) (accessed 2026-07-23): BEA monthly heavy-weight truck retail-sales series, thousands of units, through June 2026.
- **S6** — [DOT Releases 30-Year Freight Projections](https://www.bts.gov/newsroom/dot-releases-30-year-freight-projections) (accessed 2026-07-23): FAF projected truck tonnage rising 44% from 2015 to 2045 and reported trucks carried 64% of freight tonnage in 2015.
- **S7** — [ABS Characteristics of Business Owners: 2024 Tables](https://www.census.gov/data/tables/2024/econ/abs/2024-abs-characteristics-of-owners.html) (accessed 2026-07-23): Official Census owner-characteristics program includes employer-business Age of Owner tables, supporting owner-age as a broad succession proxy.
- **S8** — [Freight Analysis Framework 5.7.1 Updated](https://www.bts.gov/newsroom/freight-analysis-framework-81525-updated) (accessed 2026-07-23): Latest cited FAF release provides freight tonnage, value, and ton-miles estimates plus forecast years 2030–2050.
