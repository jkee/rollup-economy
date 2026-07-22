# 532284 — Recreational Goods Rental

*v5.1 Stage 1 research memo. Run `532284-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.76 · L 2.58 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digital reservation, pricing, customer-service, and inventory decisions can raise conversion and utilization across repeated uses of the same physical asset.
**Weakness:** A large share of work and risk remains local, seasonal, physical, and safety-sensitive, while the available firm-count and demand evidence are indirect.

## Business-model lens
- Included: U.S. lower-middle-market operators that own and rent recreational equipment such as bicycles, canoes, motorcycles, skis, sailboats, beach chairs, and umbrellas, including the reservations, fitting or handoff, inspection, maintenance, and retrieval work needed to support repeated rentals.
- Excluded: Captive rental desks inside resorts or marinas that are not separable businesses; peer-to-peer marketplaces that do not own or operate the inventory; equipment sales and tours as the primary business; shell, non-control, and subscale hobby operations; and adjacent sporting-goods, vehicle, or accommodation activities classified elsewhere.
- Customer and revenue model: Consumers and visitor groups pay time-based rental fees, often by hour or day and with strong seasonal and location effects; operators may also earn delivery, damage-waiver, instruction, or accessory revenue. The model requires local inventory utilization, safe handoff, condition control, and turnaround between users.
- Deviation from default lens: none

## Executive view
This is a coherent local rental model with automatable commercial and administrative workflows wrapped around stubbornly physical inventory operations. The opportunity depends more on improving utilization and response speed than on removing the people who inspect, maintain, fit, and hand off equipment.

## How AI changes the work
AI can absorb inquiry handling, reservation changes, multilingual communication, routine waiver and billing support, marketing content, demand forecasting, dynamic-pricing recommendations, schedule optimization, and maintenance triage. Humans remain central to equipment condition, safety, repair, fitting, transport, exceptions, and liability-bearing decisions.

## Value capture
Time-based pricing and finite local inventory permit some benefit to remain with the operator through better conversion and utilization. Competitive search marketplaces, transparent prices, software fees, seasonal bottlenecks, and added wear on heavily utilized assets limit capture.

## Firm availability
Most stand-alone recreational-goods rental companies fit the external-service screen, but the establishment count is an imprecise firm anchor and includes very small, captive, seasonal, and owner-dependent operations. Qualifying control transfers should be materially fewer than broad owner intentions suggest.

## Demand durability
Outdoor participation and broad consumer-rental revenue support modest growth, while weather, tourism, discretionary budgets, safety regulation, and ownership alternatives widen the range. Physical asset access should remain operator-mediated even as booking and access become more digital.

## Risks and uncertainty
The largest uncertainties are the absence of exact-industry task data, unknown inflation in broad rental revenue, category differences in safety and capital intensity, seasonality, and the conversion of succession intentions into completed external control transactions.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3446 | — | OBSERVED | — |
| n | — | 151 | — | ESTIMATE | — |
| a | 0.22 | 0.34 | 0.47 | PROXY | S1, S2 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S1, S2 |
| e | 0.68 | 0.82 | 0.92 | ESTIMATE | S1 |
| s5 | 0.06 | 0.12 | 0.2 | PROXY | S5 |
| q | 0.42 | 0.62 | 0.78 | ESTIMATE | S1, S3 |
| d5 | 0.96 | 1.08 | 1.18 | PROXY | S3, S4 |
| o | 0.86 | 0.94 | 0.98 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.06 | 2.58 | 4.66 | ESTIMATE |
| F | 3.17 | 4.45 | 5.40 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 8.26 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation shares are not task shares, and exposure does not imply full job removal.
- a: The broad NAICS 532 proxy contains activities with different equipment weights and customer workflows.
- rho: Implementation means sustained production use, not merely buying software.
- rho: Small seasonal operators may adopt consumer AI tools informally without measurable system integration.
- e: Establishments are not firms, and multi-location operators may be counted more than once in source datasets.
- e: Seasonality, permits, weather, and owner dependence can make nominally eligible operators unattractive or non-transferable.
- s5: Intentions are not completed transactions.
- s5: The survey spans industries, sizes, and transfer types beyond the target lens.
- q: No industry study isolates AI-created benefit from ordinary digitization or demand recovery.
- q: Higher utilization can increase maintenance, replacement, and handling costs.
- d5: The Census series is broader than 532284 and is nominal.
- d5: Two recent growth observations are not a five-year forecast and may reflect post-pandemic normalization.
- o: Operator need can persist while labor hours per rental decline.
- o: Liability and safety requirements vary sharply across bicycles, boats, motorcycles, snow gear, and beach equipment.

## Sources
- **S1** — [2022 NAICS Definition: 532284 Recreational Goods Rental](https://www.census.gov/naics/?details=532&input=532&year=2022) (accessed 2026-07-22): Official activity definition and the consumer-rental operating context used for the lens, eligibility, and operator-need reasoning.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 532000](https://www.bls.gov/oes/2023/may/naics3_532000.htm) (accessed 2026-07-22): Broad rental-and-leasing occupational mix used as the task-exposure proxy, including counter, administrative, repair, and material-moving work.
- **S3** — [Quarterly Services Survey, Second Quarter 2025](https://www2.census.gov/services/qss/2025/qssq2-25pr.pdf) (accessed 2026-07-22): Broad NAICS 5322 consumer-goods-rental revenue levels, recent growth, seasonality, and sampling limitations used directionally for demand.
- **S4** — [Outdoor Recreation Economic Statistics, U.S. and States, 2024](https://www.bea.gov/index.php/news/2026/outdoor-recreation-economic-statistics-us-and-states-2024) (accessed 2026-07-22): Real outdoor-recreation growth and activity context used as a macro demand proxy for recreational rentals.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year employer-owner sale and transfer intentions used as the broad starting point for the qualifying-control-transfer proxy.
