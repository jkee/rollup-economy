# 481111 — Scheduled Passenger Air Transportation

*v5.1 Stage 1 research memo. Run `481111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.84 · L 1.08 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable need for a certificated operator combined with meaningful automation potential in reservations, operations coordination and administration.
**Weakness:** A small, hard-to-verify pool of transferable independent operators with thin margins, safety-critical complexity and strong pass-through pressure.

## Business-model lens
- Included: US certificated scheduled passenger airlines in the lower-middle-market EBITDA band that repeatedly transport external passengers or operate scheduled regional capacity for airline customers.
- Excluded: Cargo-only airlines, nonscheduled charter and air-taxi operators, captive internal flight departments, dormant certificate shells, financing vehicles, and firms outside the lower-middle-market band.
- Customer and revenue model: Passenger carriers earn primarily ticket and ancillary-fee revenue; regional carriers may instead receive recurring capacity-purchase payments from major airlines under long-term agreements.
- Deviation from default lens: none

## Executive view
Scheduled passenger airlines offer a real but bounded AI labor opportunity concentrated away from cockpit and cabin safety work. The accountable operator and physical transport service remain durable, but eligibility, transferability, integration burden and weak commercial retention make this a difficult operating-company acquisition category.

## How AI changes the work
The clearest near-term applications are reservations, disruption communications, document review, workforce and maintenance planning, revenue analytics and administrative support. Required crew, hands-on ramp and maintenance work, and final safety judgments remain largely operator- and human-dependent.

## Value capture
Direct-ticket carriers face transparent fare competition, while regional carriers often bargain with a few major-airline customers at contract renewal. Productivity may protect margins and service quality, but a substantial share is likely competed or negotiated away.

## Firm availability
The apparent LMM firm pool requires substantial cleaning for active certificates, passenger activity, independence and transferable customer agreements. Airline transfers do occur, but fleet financing, regulatory approvals, labor obligations and concentrated counterparties make clean control transfers less routine than ordinary small-business sales.

## Demand durability
FAA forecasts imply moderate passenger growth, and software cannot substitute for physical air transport. Demand remains exposed to recessions, pandemics, aircraft shortages, fuel costs and route-level economics, especially for small regional operators.

## Risks and uncertainty
The largest uncertainties are whether the injected firm-count estimate corresponds to active independent airlines, how much payroll is truly addressable after existing automation, and whether savings survive fare or capacity-contract repricing. Safety failures, operational disruptions and customer concentration can overwhelm incremental AI gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2837 | — | OBSERVED | — |
| n | — | 99 | — | ESTIMATE | — |
| a | 0.12 | 0.19 | 0.28 | PROXY | S1, S2 |
| rho | 0.3 | 0.5 | 0.68 | ESTIMATE | S3, S4 |
| e | 0.28 | 0.45 | 0.62 | ESTIMATE | S4, S5 |
| s5 | 0.1 | 0.2 | 0.32 | ESTIMATE | S6, S7 |
| q | 0.25 | 0.43 | 0.62 | ESTIMATE | S8, S9 |
| d5 | 0.94 | 1.1 | 1.17 | PROXY | S10 |
| o | 0.94 | 0.985 | 1 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.41 | 1.08 | 2.16 | ESTIMATE |
| F | 2.14 | 3.69 | 4.87 | ESTIMATE |
| C | 5.00 | 8.60 | 10.00 | ESTIMATE |
| D | 8.84 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation chart is NAICS 4811 scheduled air transportation rather than the six-digit passenger-only code.
- a: Employment counts are not wage weights and do not reveal which tasks are already automated.
- a: Exposure excludes replacing required crew or accountable safety decisions within five years.
- rho: FAA evidence addresses safety assurance, not adoption rates for airline back-office tools.
- rho: Smaller airlines may lack the data and integration capacity of major carriers.
- rho: The estimate excludes demand, pricing and valuation effects.
- e: The injected firm count is an ESTIMATE derived from size classes and an industry margin, not a verified list of 99 operators.
- e: Part 121 includes cargo operators and large airlines, so certification evidence does not itself establish lens eligibility.
- e: Capacity-purchase dependence may leave an otherwise eligible regional carrier commercially captive to one major airline.
- s5: One large regional-airline merger is not representative of lower-middle-market firms.
- s5: BizBuySell transactions are a broad small-business benchmark with no airline denominator.
- s5: The range excludes internal reorganizations and asset liquidations that do not transfer a viable operator.
- q: Public carrier economics skew larger than the lens firms.
- q: Capacity-purchase contracts can retain savings differently from direct ticket sales.
- q: This estimate addresses commercial retention only, not implementation success or traffic volume.
- d5: FAA forecast scope is broader than NAICS 481111 LMM operators.
- d5: Passenger miles are an imperfect proxy for a constant-quality service basket.
- d5: Pandemics, fuel shocks, aircraft availability and recessions create substantial tail risk.
- o: The quantity is the transportation service, not each customer-service interaction.
- o: Advanced air mobility could change the supplier form beyond five years.
- o: Digital channels may eliminate parts of the current service basket even while the carrier remains accountable.

## Sources
- **S1** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Lists the largest scheduled-air-transportation occupations and employment counts, including 125,680 flight attendants, 86,450 pilots, 77,850 reservation/ticket agents, 28,520 mechanics and operational labor categories.
- **S2** — [Airline and Commercial Pilots](https://www.bls.gov/ooh/Transportation-and-Material-Moving/Airline-and-commercial-pilots.htm) (accessed 2026-07-22): Reports that 87% of airline pilot jobs were in scheduled air transportation and describes coordination, training and safety-accountable pilot duties.
- **S3** — [Technical Discipline: Artificial Intelligence – Machine Learning](https://www.faa.gov/aircraft/air_cert/step/disciplines/artificial_intelligence) (accessed 2026-07-22): FAA states that aviation AI/ML functionality and performance are evaluated within the certification framework to assure safety.
- **S4** — [Introduction to Part 121 Air Carrier Certification](https://www.faa.gov/licenses_certificates/airline_certification/air_carrier/intro_to_certification) (accessed 2026-07-22): Explains that applicants must design, document, implement and audit safety-critical processes and comply with regulations before receiving an air-carrier certificate.
- **S5** — [Regularly Scheduled Air Carriers (Part 121)](https://www.faa.gov/hazmat/air_carriers/operations/part_121) (accessed 2026-07-22): States that Part 121 certificate holders include large airlines, regional carriers and cargo operators and must maintain approved hazardous-materials programs.
- **S6** — [Regional airlines Republic Airways, Mesa Air Group are combining in an all-stock deal](https://apnews.com/article/republic-airways-mesa-american-delta-united-e93c911c6253f57e040cf8ae6e8af7d8) (accessed 2026-07-22): Documents a 2025 regional-airline control combination and Republic's long-term capacity-purchase agreements with three major airlines.
- **S7** — [2025 Year in Review: BizBuySell Market Recap](https://www.bizbuysell.com/blog/2025-year-in-review/) (accessed 2026-07-22): Reports 9,586 small-business transactions in 2025 and describes the broad transaction market; used only as contextual evidence, not an airline transfer rate.
- **S8** — [US Airlines profited $6.0 billion in 2025, a decrease over 2024](https://www.bts.gov/newsroom/us-airlines-profited-60-billion-2025-decrease-over-2024) (accessed 2026-07-22): Reports 2025 system operating margin of 4.5%; domestic revenue of $187.8 billion, with fares representing 70.8%; and labor as 37.5% of domestic operating expense.
- **S9** — [Refunds and Other Consumer Protections](https://www.transportation.gov/regulations/federal-register-documents/2024-07177) (accessed 2026-07-22): DOT final rule requires automatic, prompt refunds after qualifying cancellations or significant changes, evidencing regulated limits on retaining revenue for unprovided service.
- **S10** — [FAA Aerospace Forecast Fiscal Years 2026–2046](https://www.faa.gov/data_research/aviation/aerospace_forecasts/FY_2026-2046_Full_Forecast_Document_Tables.pdf) (accessed 2026-07-22): Baseline forecast shows passenger-carrier miles flown growing about 2.0% annually in the first forecast decade and passenger-carrier departures about 1.6% annually.
