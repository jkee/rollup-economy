# 485119 — Other Urban Transit Systems

*v5.1 Stage 1 research memo. Run `485119-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.63 · L 1.12 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-enabled dispatch, scheduling, customer communication, and back-office throughput inside recurring operating contracts.
**Weakness:** A tiny, contract-concentrated target universe whose core vehicle-operation labor is difficult to substitute safely within five years.

## Business-model lens
- Included: Privately owned operators of other urban transit modes that provide recurring, accountable operations, dispatch, maintenance, or integrated transit service to public agencies, institutions, or passengers and fall in the roughly $1-10M normalized EBITDA band.
- Excluded: Public authorities, captive municipal operations, financing vehicles, pure software vendors, construction-only contractors, and firms without transferable operating responsibility.
- Customer and revenue model: Recurring agency or institutional operating contracts, commonly paid per revenue hour or mile with possible fixed administrative fees or cost pass-throughs; some operators also receive passenger fares or subsidies.
- Deviation from default lens: none

## Executive view
Other urban transit offers a real but bounded AI labor opportunity. Digital dispatch, reservations, customer communications, reporting, and administrative workflows can improve meaningfully, while the dominant driving, maintenance, safety, and on-site service functions remain operator-intensive. Public-contract economics permit retention during a term but expose savings to audits, rebids, and renewal repricing.

## How AI changes the work
The most credible five-year changes are AI-assisted scheduling and dispatch, automated passenger updates, no-show prediction, contact-center deflection, document and compliance drafting, workforce scheduling, and maintenance diagnostics. The FTA's deployed paratransit example demonstrates that the same dispatcher base can manage more rides, but ordinary urban operations still require humans for exceptions, safety, accessibility, and vehicle control.

## Value capture
Per-hour and per-mile service fees can let an operator retain productivity gains between pricing events. Retention erodes when costs are passed through, staffing is contractually specified, service metrics require reinvestment, or procurement competition resets pricing. Contract duration provides a temporary shelter, not permanent ownership of the whole benefit.

## Firm availability
The frozen dataset suggests only ten LMM-band firms before applying eligibility. The investable set is smaller because a qualifying target needs private control, recurring external customers, separable operations, assignable contracts, and credible regulatory and safety capabilities. Ownership transfers are plausible but customer consent and concentrated contracts create execution risk.

## Demand durability
Transit ridership and supplied service have recovered, and accessibility, congestion, population, and essential-worker mobility create a durable service need. Remote work, local fiscal pressure, ride-hailing, and uneven geography cap confidence in rapid growth. Even where software automates coordination tasks, an accountable operating organization remains necessary for almost all service quantity over five years.

## Risks and uncertainty
The six-digit category is small and poorly represented by public datasets; most evidence is broader urban transit or fixed-route bus. Key downside risks are a firm universe dominated by nontransferable concessions, adverse change-of-control clauses, union restrictions, cyber or safety failures, customer capture of savings, and local funding cuts. The 2024 wage/2022 receipts vintage mismatch and estimated firm count add baseline uncertainty.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3441 | — | OBSERVED | — |
| n | — | 10 | — | ESTIMATE | — |
| a | 0.15 | 0.24 | 0.36 | PROXY | S1, S2 |
| rho | 0.28 | 0.43 | 0.58 | PROXY | S2, S3 |
| e | 0.25 | 0.42 | 0.62 | ESTIMATE | S3 |
| s5 | 0.12 | 0.24 | 0.38 | ESTIMATE | S3, S4 |
| q | 0.35 | 0.55 | 0.72 | PROXY | S4 |
| d5 | 0.94 | 1.06 | 1.18 | PROXY | S5, S6 |
| o | 0.86 | 0.94 | 0.98 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.58 | 1.42 | 2.87 | PROXY |
| F | 0.42 | 1.12 | 1.95 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | PROXY |
| D | 8.08 | 9.96 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source is 2023 and covers NAICS 485100, not the six-digit code.
- a: Employment shares are not wage shares; higher-paid administrative and managerial jobs receive an approximate wage adjustment in the judgment.
- a: Autonomous driving is treated conservatively because technical exposure is not the same as deployable labor substitution.
- rho: The strongest implementation example is rural paratransit rather than urban rail or specialty transit.
- rho: The estimate excludes pricing and demand effects and does not assume unattended autonomous vehicles.
- e: No source directly identifies which frozen-band NAICS 485119 firms meet the lens.
- e: GAO's contracting survey covers transit agencies and all modes rather than the private firms counted in this six-digit code.
- e: The frozen n is an estimate derived from older receipts and size-class data.
- s5: No industry-specific ownership-transfer series was found.
- s5: The long contract terms documented for fixed-route bus contracts may not carry over to specialty urban transit modes.
- s5: A transfer of an operating contract without equity control is not a qualifying event.
- q: Contract evidence is from fixed-route bus service and may not represent rail, ferry, automated guideway, or mixed specialty services.
- q: The range is a discounted five-year retention judgment, not an observed margin outcome.
- d5: Observed ridership recovery partly reflects rebound from an abnormal pandemic trough.
- d5: National aggregate demand is geographically concentrated and does not map cleanly to small private operators.
- d5: Vehicle miles are an imperfect measure of constant-quality customer demand.
- o: Automated guideway and closed-route applications could reduce operator labor faster than the base case.
- o: The estimate separates continued need for an accountable firm from the number of employees required inside it.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 485100 Urban Transit Systems](https://www.bls.gov/oes/2023/may/naics4_485100.htm) (accessed 2026-07-22): Occupation mix: 72.63% transportation/material moving, 60.73% passenger vehicle drivers, 8.72% office/administrative support, 2.97% dispatchers, and 2.22% business/financial operations.
- **S2** — [Providing a Dynamic, Data-Driven Micro-Transit Service with Smart Dispatch Using Artificial Intelligence (FTA Report 0269)](https://www.transit.dot.gov/research-innovation/providing-dynamic-data-driven-micro-transit-service-smart-dispatch-using) (accessed 2026-07-22): Documents deployment of an AI-based paratransit dispatch system enabling management of more rides with the same number of dispatchers.
- **S3** — [Public Transit: Transit Agencies' Use of Contracting to Provide Service](https://www.gao.gov/products/gao-13-782) (accessed 2026-07-22): GAO survey found 61% of 463 responding agencies contracted some or all operations/services; operations were most frequently contracted and oversight commonly used reports, inspections, performance metrics, and real-time monitoring.
- **S4** — [Third-Party Contracts for Fixed-Route Bus Operations and Maintenance: Performance Metrics, Chapter 3](https://www.nationalacademies.org/read/27074/chapter/5) (accessed 2026-07-22): Survey evidence on contract duration and payment: 81% designed for maximum terms of 5-10 years; 69% fee per revenue hour/mile, 31% cost pass-through, and 39% administrative/overhead fee.
- **S5** — [2024 National Transit Summaries and Trends](https://www.transit.dot.gov/sites/fta.dot.gov/files/2026-04/2024%20National%20Transit%20Summaries%20and%20Trends_1.2.pdf) (accessed 2026-07-22): FTA reports 7.7 billion trips in 2024, about 78% of 2019 ridership, and total capacity-equivalent vehicle revenue miles of 5.977 billion in 2024 versus 5.929 billion in 2014.
- **S6** — [APTA Public Transportation Ridership Update, May 2025](https://www.apta.com/wp-content/uploads/2026/03/APTA-POLICY-BRIEF-Transit-Ridership-05-17-2025.pdf) (accessed 2026-07-22): Reports 7.7 billion trips in 2024, 7% growth over 2023, 25% growth since 2022, and recovery to 85% of pre-pandemic levels in the first four months of 2025.
