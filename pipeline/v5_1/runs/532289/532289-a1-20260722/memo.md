# 532289 — All Other Consumer Goods Rental

*v5.1 Stage 1 research memo. Run `532289-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.31 · L 3.42 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-assisted quoting, scheduling, inventory allocation, and route planning can raise conversion and utilization in a repeated-rental network.
**Weakness:** The official category combines materially different contract and product models, and the physical logistics base limits the share of work that AI can directly remove.

## Business-model lens
- Included: U.S. lower-middle-market operators that own and repeatedly rent miscellaneous consumer goods not assigned to more specific rental codes, principally party and event supplies and short-duration residential furniture or specialty household goods, together with quoting, reservation, warehouse, preparation, delivery, setup, pickup, inspection, cleaning, and maintenance work.
- Excluded: Lease-to-own or installment-sale portfolios designed primarily to transfer ownership; consumer electronics and appliances, formal wear and costumes, prerecorded video, home-health equipment, and recreational goods classified in separate codes; peer-to-peer marketplaces without operated inventory; captive internal fleets; shells, non-control vehicles, and subscale hobby operators.
- Customer and revenue model: Households, event hosts, venues, and planners pay time-based fees for access to operator-owned goods, with additional delivery, setup, damage-waiver, cleaning, or service revenue. Revenue depends on inventory turns, route and warehouse execution, return condition, and local event or household demand.
- Deviation from default lens: Narrowed for coherence to operating rental businesses earning predominantly temporary-use and related service revenue. Sales-heavy lease-to-own arrangements are excluded because their consumer-credit, collections, and ownership-transfer economics differ materially from repeat rent-to-rent operations; the narrowing is not based on attractiveness.

## Executive view
The official residual category is too mixed to model as one undifferentiated business, so the lens is narrowed to repeat rent-to-rent operators in party supplies, furniture, and similar goods. Within that lens, AI can materially improve commercial coordination and asset utilization, while warehouse, preparation, delivery, setup, recovery, and condition work remain operator-intensive.

## How AI changes the work
AI is most useful in inquiry capture, complex quote drafting, product matching, availability checks, schedule and route suggestions, customer messaging, billing support, catalog maintenance, and demand forecasting. Physical order picking, cleaning, loading, driving, setup, pickup, inspection, repair, and exception handling remain human or conventional-automation work.

## Value capture
Better conversion, route density, utilization, and inventory accuracy can create meaningful benefit. Local bid competition, planner bargaining, visible prices, software expense, added throughput costs, and finite warehouse and delivery capacity prevent full retention.

## Firm availability
The supplied population is substantial but cannot be read directly as eligible firms because the code includes multiple models and the underlying count is establishment-based. Excluding lease-to-own and sales-heavy businesses is necessary for coherence and materially reduces the eligible share before applying the transfer-rate haircut.

## Demand durability
Broad consumer-rental revenue is growing, but it is nominal, seasonal, and not specific to this lens. Event formation, household mobility, temporary-use preferences, and avoidance of ownership support demand; discretionary pressure, purchases, disposable goods, venue inventories, and economic cycles work against it.

## Risks and uncertainty
The main risks are residual-category heterogeneity, lack of exact task and real-volume data, misclassification between rent-to-rent and lease-to-own models, establishment-versus-firm distortion, and uncertainty about whether succession intentions become external control transactions.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4951 | — | OBSERVED | — |
| n | — | 446 | — | ESTIMATE | — |
| a | 0.2 | 0.32 | 0.45 | PROXY | S1, S2, S4 |
| rho | 0.34 | 0.54 | 0.7 | ESTIMATE | S1, S2, S4 |
| e | 0.48 | 0.68 | 0.84 | ESTIMATE | S1, S4 |
| s5 | 0.06 | 0.12 | 0.2 | PROXY | S5 |
| q | 0.38 | 0.58 | 0.74 | ESTIMATE | S1, S3, S4 |
| d5 | 0.94 | 1.05 | 1.16 | PROXY | S3 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.35 | 3.42 | 6.24 | ESTIMATE |
| F | 4.23 | 5.83 | 6.96 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.27 | 9.97 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation shares are a broad proxy for time spent on tasks.
- a: The residual NAICS category contains goods with materially different handling and service intensity.
- rho: The residual category has no single representative technology stack.
- rho: Digitized customer intake may shift exceptions into operations rather than eliminate them.
- e: The NAICS residual is heterogeneous by product, rental duration, and customer mission.
- e: Establishment counts do not identify firms or qualifying control opportunities.
- s5: The survey measures stated plans rather than completions.
- s5: Its industry and size mix is broader than the target lens.
- q: No primary study isolates AI-specific benefit in the narrowed industry.
- q: Utilization improvements can add cleaning, repair, handling, and replacement cost.
- d5: The source is nominal, not seasonally adjusted, and broader than the coherent lens.
- d5: A residual industry can change composition even when total revenue grows.
- o: Accountable operation may remain even when third parties perform delivery or setup.
- o: Furniture and party supplies differ in contract duration, logistics, and substitution risk.

## Sources
- **S1** — [2022 NAICS Definition: 532289 All Other Consumer Goods Rental](https://www.census.gov/naics/?details=532&input=532&year=2022) (accessed 2026-07-22): Official inclusion and exclusion boundaries, including furniture rental centers and party rental supply centers, used for the coherence lens.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 532000](https://www.bls.gov/oes/2023/may/naics3_532000.htm) (accessed 2026-07-22): Broad occupational structure used to bridge from rental-industry jobs to exposed and physical task shares.
- **S3** — [Quarterly Services Survey, Second Quarter 2025](https://www2.census.gov/services/qss/2025/qssq2-25pr.pdf) (accessed 2026-07-22): Broad NAICS 5322 revenue, recent nominal growth, seasonality, and sampling limitations used for the demand proxy.
- **S4** — [Upbound Group, Inc. 2024 Annual Report on Form 10-K](https://www.sec.gov/Archives/edgar/data/933036/000093303625000042/upbd-20241231.htm) (accessed 2026-07-22): Primary-company evidence that furniture-oriented lease-to-own operations combine digital decisioning with delivery, installation, maintenance, inventory control, and ownership-transfer economics, supporting both physical-task reasoning and the lens exclusion.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year employer-owner sale and transfer intentions used as the starting point for the qualifying-control-transfer proxy.
