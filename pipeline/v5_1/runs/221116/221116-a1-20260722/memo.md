# 221116 — Geothermal Electric Power Generation

*v5.1 Stage 1 research memo. Run `221116-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.21 · L 0.00 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Contracted, operator-required power demand combined with data-rich plant and reservoir operations creates credible AI-assisted efficiency potential.
**Weakness:** The frozen zero LMM-firm estimate and concentrated infrastructure ownership call the availability of any qualifying acquisition target into question.

## Business-model lens
- Included: US firms in the lower-middle-market EBITDA band that own and operate geothermal electric generating assets and repeatedly sell electricity to external utilities, corporate offtakers, or wholesale markets.
- Excluded: Regulated utilities whose geothermal generation is captive to an integrated rate base; passive tax-equity or project-finance vehicles; development-stage firms without operating generation; geothermal heating, cooling, drilling, equipment manufacturing, and consulting businesses classified elsewhere.
- Customer and revenue model: Recurring electricity sales, principally under power purchase agreements or wholesale-market arrangements, with the screened firm remaining accountable for plant and reservoir operations.
- Deviation from default lens: none

## Executive view
Geothermal generation has a real analytics opportunity in a small, technical workforce and benefits from contracted, persistent electricity demand. The investable-company lens is the problem: US assets are concentrated, capital intensive, often embedded in large portfolios, and the frozen dataset finds no firms in the target EBITDA band. The screen therefore depends less on technological feasibility than on proving that a controllable LMM operating-company population exists.

## How AI changes the work
AI can improve reservoir and plant forecasting, anomaly detection, alarm triage, predictive maintenance, dispatch support, work-order planning, and regulatory documentation. It can augment the large plant-operator cohort, but field repair, construction, switching, safety judgment, and emergency response remain operator-led and constrain substitution.

## Value capture
Fixed or long-duration PPAs can shelter operating savings until a renewal or repricing event, allowing relatively strong benefit retention. Savings may nevertheless be reinvested in reliability and reservoir performance, competed away in future PPAs, shared contractually, or exposed through regulated-cost treatment.

## Firm availability
An observed large portfolio acquisition establishes that contracted geothermal assets transfer, but it is weak evidence for LMM company availability. Institutional ownership, project debt, tax equity, minority interests, and shared operating arrangements can make nominal asset ownership different from a clean control acquisition.

## Demand durability
The service basket is durable because electricity delivery from physical geothermal assets remains operator-required. Recent installed-capacity growth and a PPA pipeline above 1,000 MWe support expansion, though drilling, permitting, interconnection, financing, and commissioning risk make the five-year outcome much less certain than announced capacity.

## Risks and uncertainty
The largest risks are an effectively nonexistent target-sized firm population, concentration among large owners, hidden project-level liabilities, reservoir decline, well remediation, induced-seismicity and permitting exposure, PPA concentration, and costly outages. AI evidence is still primarily programmatic rather than audited industry-wide labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1334 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.14 | 0.28 | 0.4 | PROXY | S1, S2 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S2 |
| e | 0.08 | 0.25 | 0.5 | ESTIMATE | S3, S4 |
| s5 | 0.03 | 0.08 | 0.16 | PROXY | S4 |
| q | 0.58 | 0.76 | 0.9 | ESTIMATE | S4, S5 |
| d5 | 0.98 | 1.16 | 1.35 | PROXY | S5, S6 |
| o | 0.97 | 0.99 | 1 | ESTIMATE | S2, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.26 | 0.82 | 1.54 | ESTIMATE |
| F | 0.00 | 0.00 | 0.00 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.51 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS employment shares are headcount rather than wage-weighted task shares.
- a: The exact-industry workforce is only about 1,250 and some detailed occupation estimates are suppressed or imprecise.
- a: DOE-funded use cases demonstrate technical opportunity, not realized labor substitution.
- rho: DOE describes funded research and intended efficiency improvements rather than industry-wide five-year adoption.
- rho: Small operators may lack the data engineering and capital available to large geothermal fleets.
- e: The frozen n estimate is zero, so this share has little practical meaning unless the size-band population is first verified.
- e: Public sources describe plants and transactions but do not identify normalized EBITDA or control rights for all owners.
- s5: One large portfolio transaction is not representative of small-firm succession.
- s5: Asset sales, project interests, and corporate control transfers are not interchangeable.
- s5: No owner-age evidence was found for the screened population.
- q: Public PPA announcements rarely disclose full pricing and repricing terms.
- q: The mix of fixed-price contracted, regulated, and merchant revenue is not measured for target-sized firms.
- d5: Capacity is not generation and announced PPAs may not reach commercial operation within five years.
- d5: New EGS demand may accrue to developers outside the current LMM operating-firm lens.
- d5: Constant-quality adjustment is judgmental because dispatchability and contract attributes vary.
- o: Accountable operator requirements can be met by a larger portfolio owner after acquisition, so demand for operation need not preserve the same firm population.
- o: The estimate concerns operator-required quantity, not staffing intensity.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 221116](https://www.bls.gov/oes/2023/may/naics5_221116.htm) (accessed 2026-07-23): Exact-industry employment of 1,250; plant and system operators 34.46%; production occupations 39.36%; maintenance 15.47%; construction 10.73%; management 11.09%; administrative support 5.78%.
- **S2** — [Machine Learning](https://www.energy.gov/hgeo/geothermal/machine-learning) (accessed 2026-07-23): DOE states that machine learning can improve geothermal exploration and plant operations and documents a $3.5 million advanced-analytics phase focused on efficiency, automation, operations, and resource management.
- **S3** — [Use of geothermal energy](https://www.eia.gov/energyexplained/geothermal/use-of-geothermal-energy.php) (accessed 2026-07-23): In 2025 US geothermal plants operated in seven states and produced about 16 billion kWh, 0.4% of utility-scale generation, evidencing the industry's small and geographically concentrated operating footprint.
- **S4** — [Ormat Completed the Acquisition of Contracted Operating Geothermal and Solar Assets From Enel Green Power North America](https://www.globenewswire.com/news-release/2024/01/04/2803882/26372/en/Ormat-Completed-the-Acquisition-of-Contracted-Operating-Geothermal-and-Solar-Assets-From-Enel-Green-Power-North-America.html) (accessed 2026-07-23): Ormat paid $271 million for a portfolio including two contracted operating geothermal plants and one geothermal hybrid plant with about 40 MW geothermal capacity, demonstrating transferability but at institutional scale.
- **S5** — [2025 U.S. Geothermal Market Report](https://www.energy.gov/hgeo/geothermal/market-report) (accessed 2026-07-23): DOE reports 3,969 MWe installed nameplate capacity in 2024, up 8% from 2020; 54 projects under development; and 26 PPAs representing more than 1,000 MWe of new capacity commitments since the 2021 report.
- **S6** — [Enhanced geothermal systems could expand geothermal power generation](https://www.eia.gov/todayinenergy/detail.php?id=67204) (accessed 2026-07-23): EIA describes successful EGS pilots, the first large-scale commercial EGS generator under construction in Utah, and Defense Department partnerships for projects across six states, supporting demand expansion with execution risk.
