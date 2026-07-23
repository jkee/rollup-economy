# 221112 — Fossil Fuel Electric Power Generation

*v5.1 Stage 1 research memo. Run `221112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.87 · L 0.53 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Dispatchable gas generation retains physical value as electricity demand grows and variable resources expand.
**Weakness:** Coal decline, regulated or competitive pass-through, and non-transferable project ownership sharply reduce the screenable opportunity.

## Business-model lens
- Included: Independent LMM operators of coal-, petroleum-, or natural-gas-fired generation facilities that repeatedly sell electricity, capacity, ancillary services, or contracted output to external utilities, markets, cooperatives, or large customers.
- Excluded: Vertically integrated captive generation, municipal and cooperative internal units, passive project-finance vehicles without operations, shells, transmission and distribution, and firms outside the EBITDA band.
- Customer and revenue model: Recurring wholesale market, power-purchase agreement, capacity, tolling, ancillary-service, or regulated generation revenue from dispatchable physical plants.
- Deviation from default lens: none

## Executive view
Fossil generation offers a meaningful operational analytics opportunity, but eligibility and benefit retention are constrained by utility ownership, project structures, market pricing, and regulation. Gas demand is resilient while coal decline weakens the combined basket.

## How AI changes the work
Likely uses include predictive maintenance, alarm and document support, outage planning, heat-rate analysis, fuel and power-market forecasting, environmental reporting, and work management. Control-room accountability, field operations, maintenance, safety response, and compliance sampling remain human-led.

## Value capture
Merchant markets, capacity auctions, tolling, and regulated cost recovery transmit savings to customers or bids. Fixed-price contracts and operational differentiation can preserve a share, but average retention is limited.

## Firm availability
The estimated population overstates actionable supply because many plants sit inside utilities, portfolios, cooperatives, municipalities, or passive project entities. Standalone independent operators with transferable permits, staff, contracts, and interconnection are fewer.

## Demand durability
Coal generation continues to decline, while gas remains a large dispatchable source and can benefit from electricity-load growth. Policy, fuel prices, renewables, storage, and data-center load drive a wide range.

## Risks and uncertainty
Environmental liability, decommissioning, carbon and air rules, fuel and power prices, PPA assignment, capacity-market reform, reliability mandates, cyber risk, project debt, and the mapping from establishments to firms dominate.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1287 | — | OBSERVED | — |
| n | — | 77 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.3 | PROXY | S1, S2, S3 |
| rho | 0.34 | 0.51 | 0.68 | ESTIMATE | S1, S3, S4 |
| e | 0.24 | 0.4 | 0.58 | ESTIMATE | S4, S5 |
| s5 | 0.09 | 0.17 | 0.28 | PROXY | S6 |
| q | 0.2 | 0.36 | 0.55 | ESTIMATE | S4 |
| d5 | 0.75 | 0.9 | 1.08 | PROXY | S4, S5 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.53 | 1.05 | ESTIMATE |
| F | 1.58 | 2.94 | 4.19 | ESTIMATE |
| C | 4.00 | 7.20 | 10.00 | ESTIMATE |
| D | 7.05 | 8.82 | 10.00 | ESTIMATE |

## Caveats
- a: Public occupation data combine generation technologies and network functions.
- a: Coal and modern gas plants have different staffing intensity.
- rho: Bounded judgment rather than observed industry implementation.
- rho: Autonomous safety-critical control is excluded.
- e: The injected count is margin-bridged and estimated.
- e: Plants, establishments, project entities, and transferable firms are not equivalent.
- s5: Economy-wide demographic proxy is weak for capital assets.
- s5: Asset sales and qualifying operating-company transfers must be separated.
- q: Commercial structures vary from merchant to regulated and contracted plants.
- q: No public contract sample directly measures AI-benefit retention.
- d5: Coal and gas trajectories diverge sharply.
- d5: Policy, fuel prices, and electricity-load growth are unusually uncertain.
- o: Fuel switching and plant retirement belong mainly in d5.
- o: Operator share may migrate to larger portfolios.

## Sources
- **S1** — [Power Plant Operators, Distributors, and Dispatchers](https://www.bls.gov/ooh/production/power-plant-operators-distributors-and-dispatchers.htm) (accessed 2026-07-22): BLS states power-plant operators control systems that generate electricity and operate generating equipment, supporting the physical and accountable work characterization.
- **S2** — [Power Plant Operators Occupational Employment and Wages](https://www.bls.gov/oes/2023/may/oes518013.htm) (accessed 2026-07-22): BLS reports 21,990 power-plant operators in electric generation, transmission, and distribution, used as a broader occupation proxy.
- **S3** — [Electric Utilities Occupational Survey Form](https://www.bls.gov/respondents/oes/pdf/forms/221000.pdf) (accessed 2026-07-22): BLS defines power-plant operators as controlling, operating, or maintaining machinery that generates electric power.
- **S4** — [EIA Short-Term Energy Outlook: Electricity, Coal, and Renewables](https://www.eia.gov/outlooks/steo/report/elec_coal_renew.php) (accessed 2026-07-22): EIA forecasts summer 2026 coal-fired generation 6% below the prior summer amid increased generation from multiple fuels.
- **S5** — [EIA Short-Term Energy Outlook](https://www.eia.gov/outlooks/steo/) (accessed 2026-07-22): EIA expects record natural-gas consumption in the electric-power sector next year, driven by load growth, fleet expansion, and relatively low gas prices.
- **S6** — [2024 Chartbook on Firms by Age of Primary Owner](https://www.fedsmallbusiness.org/-/media/project/smallbizcredittenant/fedsmallbusinesssite/fedsmallbusiness/files/2024/firms-in-focus/sbcs_chartbook2024_ownerage.pdf) (accessed 2026-07-22): Federal Reserve owner-age evidence used only as a broad succession proxy.
