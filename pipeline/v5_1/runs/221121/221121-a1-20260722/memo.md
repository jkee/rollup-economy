# 221121 — Electric Bulk Power Transmission and Control

*v5.1 Stage 1 research memo. Run `221121-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.63 · L 0.33 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Rising load, grid congestion, interconnection, and resilience needs support durable transmission and control demand alongside rich AI-addressable planning and asset data.
**Weakness:** The tiny mostly regulated target population combines low firm availability with formula-rate pass-through that limits retained operating savings.

## Business-model lens
- Included: US lower-middle-market firms operating high-voltage electric transmission lines, transformer stations, control centers, or related bulk-power control systems and providing recurring transmission or control service to generators, distribution utilities, load-serving entities, market participants, or other external customers.
- Excluded: Electric generation, final-customer distribution, construction and equipment vendors, engineering consultants without operating responsibility, captive internal departments, government agencies, public or nonprofit system operators outside transferable control ownership, passive asset shells, and non-control financing vehicles.
- Customer and revenue model: Recurring regulated or contracted transmission and control revenue through FERC-approved tariffs and formula rates, state-regulated arrangements where applicable, network or point-to-point service, interconnection and congestion-related services, or long-term contracts; revenue commonly recovers operating costs, depreciation, taxes, and an allowed return on invested capital.
- Deviation from default lens: none

## Executive view
Bulk power transmission has substantial data and planning workflows suited to AI, but real-time control remains safety-critical and tightly regulated. Demand is durable and likely growing; the larger obstacles are an exceptionally small transferable target pool and rapid pass-through of O&M savings under formula-rate regulation.

## How AI changes the work
AI can accelerate load and generation forecasts, contingency screening, interconnection and long-term studies, asset-health analysis, vegetation and image review, outage planning, alarm prioritization, compliance evidence, and regulatory drafting. Human operators, engineers, cybersecurity staff, and field crews retain authority for switching, emergencies, protection, maintenance, and grid reliability.

## Value capture
Annual cost-of-service formula updates tend to return lower operating costs to transmission customers, limiting durable retention. Operators can retain more when improvements increase availability or throughput, defer penalties, support incremental capital, shorten project cycles, or sit inside fixed-price and performance-based arrangements.

## Firm availability
The frozen count is only eight before screening, and public, cooperative, nonprofit, captive, and large-utility entities dominate much of the function. Standalone eligibility requires transferable assets, tariffs, people, control responsibility, external service, and LMM economics, so entity-level verification is decisive.

## Demand durability
DOE identifies pressing transmission need from load and generation interconnection, congestion, resilience, and industrial and data-center growth and plans more long-distance capacity. Permitting, cost allocation, supply chains, and long construction schedules create timing risk, but fulfilled service remains operator-required.

## Risks and uncertainty
Cybersecurity, reliability events, wildfire and severe weather, aging assets, transformer supply, permitting, eminent-domain and siting disputes, formula-rate challenges, capital intensity, operator consolidation, and regulatory change are material. Evidence is weakest on eligible firms, wage-weighted tasks, implementation economics, qualifying transfers, and savings retention by tariff.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2556 | — | OBSERVED | — |
| n | — | 8 | — | ESTIMATE | — |
| a | 0.19 | 0.29 | 0.4 | PROXY | S1, S2, S3 |
| rho | 0.38 | 0.54 | 0.68 | ESTIMATE | S2, S3, S4 |
| e | 0.08 | 0.22 | 0.38 | ESTIMATE | S1, S5, S6 |
| s5 | 0.05 | 0.13 | 0.24 | ESTIMATE | S6 |
| q | 0.17 | 0.33 | 0.51 | PROXY | S5 |
| d5 | 0.99 | 1.1 | 1.22 | PROXY | S7, S8 |
| o | 0.985 | 0.997 | 1 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.74 | 1.60 | 2.78 | ESTIMATE |
| F | 0.05 | 0.33 | 0.88 | ESTIMATE |
| C | 3.40 | 6.60 | 10.00 | PROXY |
| D | 9.75 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation data are broader than 221121 and not wage-weighted for the screened firms.
- a: The mix between asset owner, independent transmission company, and control-center operator materially changes exposure.
- rho: DOE programs demonstrate technical direction, not realized five-year savings in eligible firms.
- rho: High-consequence grid operations require validation and cybersecurity controls beyond ordinary enterprise AI.
- e: The frozen eight-firm estimate is margin-bridged and highly sensitive to a single classification or size-band error.
- e: Establishment NAICS does not reveal whether operating capability and regulated assets reside in a transferable standalone firm.
- s5: No direct qualifying-transfer rate for LMM 221121 firms was found.
- s5: Affiliate restructurings, passive line interests, and integrated-utility mergers may not qualify under the lens.
- q: Formula-rate mechanics differ by operator and jurisdiction.
- q: The source explains rate design but does not measure AI savings or pass-through timing.
- d5: Capacity growth is not identical to constant-price operating-service demand.
- d5: National needs and plans may benefit large utilities and public entities rather than the small eligible population.
- o: Operator consolidation can reduce the number of entities without eliminating the accountable function.
- o: Some planning, market coordination, or control responsibilities may migrate to larger regional organizations.

## Sources
- **S1** — [2022 NAICS Definition: 221121 Electric Bulk Power Transmission and Control](https://www.census.gov/naics/?details=221121&input=221121&year=2022) (accessed 2026-07-22): Defines the industry as operating electric power transmission systems and/or controlling voltage from generating sources to distribution centers or other utilities, including lines and transformer stations, while excluding generation and final-customer distribution.
- **S2** — [Power Plant Operators, Distributors, and Dispatchers](https://www.bls.gov/ooh/production/power-plant-operators-distributors-and-dispatchers.htm) (accessed 2026-07-22): Describes system operators monitoring converters, transformers, breakers, voltage, and flows; issuing switching orders; routing around maintenance; and responding to transmission failures, and notes smart-grid automation alongside continuing need for operators.
- **S3** — [Grid Controls and Communications](https://www.energy.gov/oe/grid-controls-and-communications) (accessed 2026-07-22): Describes DOE work on situational awareness, real-time operations, secure communications, optimized human-machine interfaces, grid modeling, and advanced analytics including AI, grounding implementation opportunities and constraints.
- **S4** — [CIP-010-4: Cyber Security — Configuration Change Management and Vulnerability Assessments](https://prod.nerc.com/standards/reliability-standards/cip/cip-010-4) (accessed 2026-07-22): States enforceable configuration-change and vulnerability-assessment requirements intended to prevent unauthorized changes and compromise that could cause Bulk Electric System misoperation or instability, grounding cybersecurity implementation friction.
- **S5** — [Formula Rates in Electric Transmission Proceedings: Key Concepts and How to Participate](https://www.ferc.gov/formula-rates-electric-transmission-proceedings-key-concepts-and-how-participate) (accessed 2026-07-22): Explains annual formula-rate updates based on transmission cost of service, including O&M, depreciation, taxes, and a reasonable return on invested capital, and safeguards against overearning, grounding the pass-through proxy.
- **S6** — [Mergers and Sections 201 and 203 Transactions](https://www.ferc.gov/electric/general-information/mergers-and-sections-201-and-203-transactions) (accessed 2026-07-22): Explains FERC public-interest review of utility mergers and acquisitions and the statutory authorization requirement for jurisdictional facilities and securities above $10 million, grounding transfer friction and obtainable deal evidence.
- **S7** — [Grid Deployment and Transmission](https://www.energy.gov/topics/grid-deployment-and-transmission) (accessed 2026-07-22): States a DOE plan to expand long-distance transmission-line capacity 16 percent by 2030, including 7,500 miles of new lines, and describes transmission modernization for growing electricity demand.
- **S8** — [National Transmission Needs Study](https://www.energy.gov/oe/national-transmission-needs-study) (accessed 2026-07-22): The July 2026 draft-study summary finds pressing need for additional transmission from new generation and load interconnection and congestion relief, notes most congestion is concentrated in 5 percent of hours, and reports several regions approving their largest portfolios.
