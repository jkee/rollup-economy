# 481219 — Other Nonscheduled Air Transportation

*v5.1 Stage 1 research memo. Run `481219-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.13 · L 1.66 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Mission-critical outsourced availability contracts create repeat revenue and protect demand for accountable specialty aviation operators.
**Weakness:** Safety-critical crews and maintenance dominate the work, while the industry's heterogeneous missions make scalable AI implementation and transferable-firm identification difficult.

## Business-model lens
- Included: US lower-middle-market operators providing recurring or repeat outsourced specialty air transportation with general-purpose aircraft, principally helicopter air-ambulance, utility, offshore-support, search-and-rescue, and other special-mission flying for hospitals, governments, industrial customers, and other external buyers.
- Excluded: Passenger-only and cargo-only charter classified elsewhere, scheduled service, air couriers, aircraft-only lessors, captive government or corporate flight units, aviation clubs, recreational or sightseeing-only one-offs, inactive certificate shells, and non-control financing vehicles.
- Customer and revenue model: Customers pay through multi-period availability or master-service agreements, fixed monthly standing charges plus flight-hour fees, day rates plus hourly charges, government contracts, hospital arrangements, or per-transport insurer and public-payer reimbursement.
- Deviation from default lens: NAICS 481219 combines air ambulance, helicopter utility and special-mission operations, aviation clubs, and varied specialty flying. For a coherent repeat-service screen, the lens retains externally paid recurring or repeat specialty transport and excludes club/recreational and sightseeing-only activity; this narrowing is based on business-model coherence, not attractiveness.

## Executive view
Other nonscheduled air transportation is a heterogeneous specialty-aviation category. Within the repeat-service lens, air-medical, utility, offshore-support, search-and-rescue, and special-mission operators have durable physical roles and contract recurrence, but their wage base remains dominated by regulated flight, maintenance, clinical, and field work rather than easily substituted administration.

## How AI changes the work
AI can improve mission intake, crew and aircraft scheduling, maintenance-record retrieval, safety-document search, claims and billing preparation, customer reporting, and routine dispatch support. It is much less able to replace real-time flight judgment, patient care, maintenance release, emergency coordination, or operational-control accountability over five years.

## Value capture
Fixed standing charges, availability payments, and government contract terms can preserve savings during a contract period. Competitive rebids, customer concentration, insurer and public-payer rates, utilization variability, and audit or denial risk reduce the discounted retained share.

## Firm availability
FAA data confirm a meaningful population of air-ambulance and helicopter carriers, but the NAICS code also contains clubs and miscellaneous specialty operators. Active certificates, safety history, aircraft and lease obligations, specialized personnel, and assignability of hospital, industrial, or government contracts determine whether a firm is genuinely transferable.

## Demand durability
FAA forecasts rising rotorcraft and fixed-wing turbine hours through 2031 and cites EMS, firefighting, law enforcement, and search and rescue as rotorcraft demand supports. Demand remains sensitive to public budgets, payer policy, offshore activity, aircraft supply, and the pace at which AAM or drones substitute selected missions.

## Risks and uncertainty
Evidence is mostly broader than 481219: occupations cover all nonscheduled aviation, activity forecasts cover general aviation and air taxi, succession evidence spans industries, and contract evidence comes from a global operator. The code's internal business-model diversity and uncertain AAM substitution make eligibility, demand, and operator-required share the largest judgment calls.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4016 | — | OBSERVED | — |
| n | — | 69 | — | ESTIMATE | — |
| a | 0.16 | 0.23 | 0.3 | PROXY | S1 |
| rho | 0.32 | 0.45 | 0.58 | ESTIMATE | S2, S3 |
| e | 0.42 | 0.58 | 0.72 | ESTIMATE | S2 |
| s5 | 0.14 | 0.21 | 0.3 | PROXY | S4, S3 |
| q | 0.35 | 0.53 | 0.7 | ESTIMATE | S5, S6, S7 |
| d5 | 0.94 | 1.1 | 1.24 | PROXY | S8 |
| o | 0.68 | 0.84 | 0.94 | ESTIMATE | S8, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.82 | 1.66 | 2.80 | ESTIMATE |
| F | 2.61 | 3.61 | 4.45 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.39 | 9.24 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source is four-digit NAICS 481200, not 481219 or the narrowed lens.
- a: OEWS excludes self-employed workers and does not identify clinical staff contracted by hospitals.
- a: Task exposure is a bounded judgment, not observed automation.
- rho: There is no industry-specific longitudinal study of implemented AI labor substitution.
- rho: The estimate excludes demand and autonomous-aircraft effects, which belong in d5 and o.
- e: FAA's operator study uses older 2012-2016 activity and 2012 economic data, although it was issued in 2023.
- e: The frozen firm count is margin-bridged and does not reveal active certificate or recurring-revenue status.
- s5: Gallup measures stated plans across industries, not completed aviation transactions.
- s5: Internal family transfers and gifts in the survey may not all meet the qualifying-control definition.
- q: Bristow is a large global operator rather than a US LMM peer.
- q: Air-ambulance reimbursement and industrial or government helicopter contracts have very different pass-through dynamics.
- q: Historical GAO air-ambulance pricing evidence predates the No Surprises Act.
- d5: FAA hours include private and other noncommercial activity outside NAICS 481219.
- d5: Flight hours are not a constant-quality service-quantity index and mix can shift toward different aircraft and missions.
- d5: FAA says AAM's long-term rotorcraft impact is too uncertain to include in the forecast.
- o: The code includes activities with very different susceptibility to unmanned substitution.
- o: An autonomous aircraft may still require a certificated operator; this estimate counts displacement only when the lens operator is no longer required.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 481200 Nonscheduled Air Transportation](https://www.bls.gov/oes/2023/may/naics4_481200.htm) (accessed 2026-07-22): Four-digit occupational mix, including commercial pilots at 33.84% of employment, aircraft mechanics at 12.02%, office/administrative support at 13.55%, business/financial operations at 6.82%, and management at 7.74%.
- **S2** — [FAA Updated Study of Operators Regulated Under Part 135](https://www.faa.gov/sites/faa.gov/files/PL_115-141_Study_of_Operators_Regulated_Under_Part_135.pdf) (accessed 2026-07-22): Documents on-demand air-medical, air-taxi, and air-tour activity; reports 754,000 air-medical hours in 2016 and InfoUSA counts of 151 air-ambulance and 102 helicopter-carrier operators in the studied population, illustrating the category's operating mix.
- **S3** — [FAA AC 135-14B: Helicopter Air Ambulance Operations](https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentid/1027108) (accessed 2026-07-22): Describes urgent medical transport and Part 135 Subpart L requirements for equipment, pilot testing, alternate airports, weather minima, and safety procedures.
- **S4** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 survey found 22% of employer-business owners planned to sell or transfer ownership within five years.
- **S5** — [Bristow Group 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1525221/000152522125000016/vtol-20241231.htm) (accessed 2026-07-22): Describes helicopter master-service and subscription contracts with fixed monthly fees plus flight-hour payments, terms of one month to ten years, cancellation provisions, and day-to-day charter day/hour pricing.
- **S6** — [GAO: Air Ambulance Data Collection and Transparency Needed to Enhance DOT Oversight](https://www.gao.gov/products/gao-17-637) (accessed 2026-07-22): Shows heterogeneous air-ambulance payer economics: 2014 median helicopter charges of about $30,000 per transport versus a $6,502 Medicare median payment and payment from multiple sources.
- **S7** — [CMS Ambulance Fee Schedule Public Use Files](https://www.cms.gov/medicare/payment/fee-schedules/ambulance/ambulance-fee-schedule-public-use-files) (accessed 2026-07-22): Confirms fee-schedule treatment of fixed- and rotary-wing air ambulance base services and air mileage, supporting regulated-price exposure for part of the lens.
- **S8** — [FAA Aerospace Forecast Fiscal Years 2026-2046](https://www.faa.gov/data_research/aviation/aerospace_forecasts/FY_2026-2046_Full_Forecast_Document_Tables.pdf) (accessed 2026-07-22): Forecasts rotorcraft hours from 2.994 million in 2026 to 3.316 million in 2031 and fixed-wing turbine hours from 8.789 million to 10.074 million; cites EMS and public-safety missions as demand supports and AAM as an uncertain rotorcraft competitor.
