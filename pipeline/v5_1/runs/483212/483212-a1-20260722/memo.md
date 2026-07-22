# 483212 — Inland Water Passenger Transportation

*v5.1 Stage 1 research memo. Run `483212-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.03 · L 2.09 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical crossings preserve operator-required demand while administrative and planning workflows offer implementable, if bounded, labor savings.
**Weakness:** Only a small, route-specific firm pool is modeled, and transferability can be defeated by concessions, public assets, vessel capital needs, or owner dependence.

## Business-model lens
- Included: Privately owned lower-middle-market operators providing recurring or repeat passenger ferry and water-taxi transportation on U.S. lakes, rivers, and intracoastal waterways outside the Great Lakes System.
- Excluded: Government-owned operators, captive internal transportation, shells, non-control financing vehicles, sightseeing or excursion cruises classified elsewhere, coastal and Great Lakes service, and freight-only operations.
- Customer and revenue model: Riders or sponsoring organizations buy trips, passes, or contracted service; revenue is typically posted passenger and vehicle fares, multi-trip products, or fixed/unit-rate public or institutional service contracts.
- Deviation from default lens: none

## Executive view
Inland passenger-water operators combine durable physical service with a limited administrative AI opportunity. The useful work is concentrated in reservations, customer contact, dispatch assistance, finance, documentation, staffing, and maintenance triage; most wages remain tied to licensed command, deck work, engineering, maintenance, and passenger safety. A small modeled firm universe and route-specific transfer restrictions make availability the larger uncertainty than technical feasibility.

## How AI changes the work
AI can answer routine trip questions, process changes and refunds, draft manifests and compliance records, reconcile payments, forecast demand, suggest schedules, and prioritize maintenance. Humans still need to supervise exceptions, weather and navigation decisions, emergency response, vessel condition, and regulatory compliance. The largest onboard labor pools therefore offer decision support and avoided incremental hiring more readily than direct substitution.

## Value capture
Posted fares and multi-trip products do not mechanically pass productivity savings back to riders, allowing initial retention. Over time, competition, public fare processes, contract rebids, and customer expectations share part of the benefit. Operators with exclusive or hard-to-replicate route rights and direct retail fares should retain more than vendors under transparent public unit-rate contracts.

## Firm availability
The frozen estimate identifies only twelve firms in the target earnings band. Most private firms in this NAICS should fit the external repeat-service lens, but acquisition eligibility can be impaired by owner dependence, public asset use, concession consent, vessel financing, and weak standalone records. Broad owner surveys indicate exit intent, yet completed qualifying transfers should be materially less frequent than stated intentions.

## Demand durability
Ferries and water taxis meet recurring crossing needs that software cannot fulfill, and the accountable-operator role remains. Aggregate ferry usage is large, but national census response changes prevent a clean trend reading. Route demand can be stable for decades where water creates a natural barrier, while an individual operator can still lose volume to remote work, alternative transit, bridge projects, tourism cycles, weather, or service unreliability.

## Risks and uncertainty
The main evidence gaps are passenger-only occupation weights, firm-level ownership and transferability, and route-level real demand. The broad labor data include inland freight, autonomous-vessel rules are evolving, and the ferry census has material nonresponse and changing coverage. A business would be unattractive if its concession blocks control transfer, its route can be displaced, its fleet requires near-term capital beyond normalized EBITDA, or its savings case depends on eliminating statutorily required crew.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4746 | — | OBSERVED | — |
| n | — | 12 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.3 | PROXY | S1, S2, S3, S4 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S2, S3, S4 |
| e | 0.82 | 0.9 | 0.97 | ESTIMATE | S5 |
| s5 | 0.15 | 0.26 | 0.4 | PROXY | S6, S7 |
| q | 0.4 | 0.6 | 0.75 | ESTIMATE | S8, S9, S10 |
| d5 | 0.92 | 1.01 | 1.1 | PROXY | S11, S12, S13 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.80 | 2.09 | 4.10 | ESTIMATE |
| F | 1.46 | 2.15 | 2.79 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.65 | 9.90 | 10.00 | ESTIMATE |

## Caveats
- a: BLS publishes the relevant occupation mix at NAICS 483200, which is dominated by freight activity and is not the passenger-only code.
- a: O*NET describes occupations economy-wide, not ferry-specific task frequency or wage weights.
- a: The frozen compensation-to-receipts input uses 2024 wages over 2022 receipts and is harmonized to an IPS basis as stated in the assignment.
- rho: No source directly measures five-year AI implementation for U.S. inland passenger operators.
- rho: Small fleets may lack clean data, systems integration staff, and enough transaction volume to justify bespoke automation.
- rho: Cybersecurity and operational reliability requirements can delay otherwise feasible deployments.
- e: Eligibility is not observed firm by firm.
- e: The frozen n of 12 is a margin-bridged estimate from older SUSB size data and a sector margin, not an observed list of qualifying firms.
- e: Some nominally private operators may rely on public assets or concessions whose change-of-control terms impair transferability.
- s5: The owner-readiness survey is self-selected and not industry-specific.
- s5: Reported desire to exit is not observed transaction probability.
- s5: With an assigned population of only twelve firms, one transaction materially changes the realized share.
- q: The mix of direct-fare and contracted operators inside the target firm set is unknown.
- q: Publicly influenced fares and competitive tenders can force more pass-through than discretionary private routes.
- q: This estimate excludes demand changes and implementation difficulty, which are assigned to other primitives.
- d5: NCFO response coverage changed from 139 operators in 2022 to 165 in 2024, preventing direct inference from headline totals.
- d5: The BLS projection covers all water-transportation occupations and a ten-year horizon, not 483212 five-year real demand.
- d5: Demand is highly route-specific and can be disrupted by one bridge, concession decision, staffing shortage, or severe-weather pattern.
- o: A five-year statutory change or successful autonomous-passenger pilot could lower the range.
- o: The construct requires an accountable operator, not necessarily today's onboard staffing model.
- o: Route displacement by bridges or other modes is captured primarily in d5 to avoid double counting.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 483200 Inland Water Transportation](https://www.bls.gov/oes/2023/may/naics4_483200.htm) (accessed 2026-07-22): Broader-industry occupation mix: 75.93% transportation/material moving, 62.37% water-transportation workers, 7.39% office/administrative support, 5.21% management, and 2.69% business/financial operations.
- **S2** — [O*NET OnLine: Customer Service Representatives](https://www.onetonline.org/link/summary/43-4051.00) (accessed 2026-07-22): Customer-service tasks include routine inquiries, orders, complaint records, billing, payments, notifications, and transactional documentation, establishing task-level AI exposure.
- **S3** — [O*NET OnLine: Dispatchers, Except Police, Fire, and Ambulance](https://www.onetonline.org/link/summary/43-5032.00) (accessed 2026-07-22): Dispatch tasks include scheduling operations and employees, coordinating activities, maintaining records, relaying information, and selecting resources.
- **S4** — [Coast Guard: Autonomous Ships and Efforts to Regulate Them](https://www.gao.gov/products/gao-24-107059) (accessed 2026-07-22): Commercial autonomous uses remained narrow as of June 2024; U.S. vessels must comply with statutory minimum crew sizes, and Coast Guard officials identified limited authority to reduce them.
- **S5** — [U.S. Census Bureau NAICS Sector 48-49 Definitions](https://www.census.gov/naics/resources/archives/sect48-49.html) (accessed 2026-07-22): Defines 483212 as establishments primarily providing passenger transportation on lakes, rivers, or intracoastal waterways except the Great Lakes and distinguishes sightseeing, coastal, and freight activities.
- **S6** — [2023 National State of Owner Readiness Report](https://exit-planning-institute.org/hubfs/Member%20Center%20Resources/2023%20National%20State%20of%20Owner%20Readiness%20Report.pdf) (accessed 2026-07-22): Reports that 49% of surveyed business owners wanted to exit their company within five years, versus 48% in 2013.
- **S7** — [BizBuySell Insight Report: Q2 2026](https://www.bizbuysell.com/insight-report/) (accessed 2026-07-22): Provides observed small-business transaction context: 2,117 businesses changed hands in Q2 2026, retirement led stated sale motivations at 45%, and preparation and financing affected sale completion.
- **S8** — [Federal Transit Administration National Transit Database Glossary](https://www.transit.dot.gov/ntd/national-transit-database-ntd-glossary) (accessed 2026-07-22): Defines passenger fares, purchased transportation, and contract structures in which sellers may retain fares or return them to the public buyer.
- **S9** — [Washington State Ferries Fares](https://wsdot.wa.gov/ferries/fares/) (accessed 2026-07-22): Shows route- and customer-specific posted fares, passes and reservations, plus a 3% card cost-recovery surcharge effective March 1, 2026.
- **S10** — [NY Waterway South Amboy Ferry Fares](https://www.nywaterway.com/GetTickets.aspx/SouthAmboyPier11Route.aspx) (accessed 2026-07-22): Shows direct retail one-way, ten-trip, forty-trip, and monthly fares and a separately stated 5.55% fuel surcharge.
- **S11** — [BLS Occupational Projections and Worker Characteristics, 2024-2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Projects water-transportation-worker employment from 84,300 in 2024 to 85,400 in 2034, a 1.3% increase.
- **S12** — [BTS Releases Results from the 2022 National Census of Ferry Operators](https://www.bts.gov/newsroom/bts-releases-results-biennial-national-census-ferry-operators) (accessed 2026-07-22): Reports 139 responding operators and 112.1 million passengers for the 2022 release, documenting both service scale and survey coverage.
- **S13** — [BTS Releases 2024 Ferry Data](https://www.bts.gov/newsroom/bts-releases-ferry-new-data) (accessed 2026-07-22): Reports 165 responses from 260 known operators, 105.8 million annual passengers, 723 vessels, 575 terminals, and 897 route segments in the 2024 NCFO.
