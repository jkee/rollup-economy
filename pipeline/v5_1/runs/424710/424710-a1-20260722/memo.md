# 424710 — Petroleum Bulk Stations and Terminals

*v5.1 Stage 1 research memo. Run `424710-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.87 · L 0.01 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent physical storage and transfer needs make demand strongly operator-required even as workflows become more automated.
**Weakness:** The labor base is tiny relative to receipts and safety, environmental, and asset-transfer complexity constrain both realizable AI savings and target availability.

## Business-model lens
- Included: Independent US lower-middle-market operators of bulk liquid storage stations or terminals that repeatedly receive, store, meter, document, sell, and transfer crude petroleum, refined petroleum products, biofuel blends, or liquefied petroleum gas to external customers.
- Excluded: Captive refinery or integrated-oil terminals, pipeline-only transportation, retail fuel stations, passive real-estate or tank-lease vehicles without operating control, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring B2B wholesale distribution and throughput operations earning commodity spreads and, where applicable, storage, handling, throughput, blending, loading, or ancillary service fees; working capital and inventory values are large relative to labor.
- Deviation from default lens: none

## Executive view
Petroleum bulk stations and terminals are indispensable physical infrastructure but an unusually low labor-share setting. AI can improve the information layer around scheduling, reconciliation, nominations, dispatch, compliance records, and alarm triage; it cannot replace tanks, pumps, containment, field inspections, or accountable operating control. The opportunity therefore depends more on operational quality than on large labor substitution.

## How AI changes the work
Useful applications include demand and inventory forecasting, automated document capture, scheduling and berth or rack optimization, reconciliation of meter and invoice data, predictive-maintenance support, and prioritized exception review. Safety-critical pump, valve, loading, and emergency actions should remain behind deterministic controls and trained human authorization.

## Value capture
Fixed-term storage and throughput arrangements can temporarily preserve savings, and fewer losses, outages, or demurrage events can create customer value. Transparent fuel markets and sophisticated counterparties make clerical cost savings difficult to retain indefinitely, while commodity inventory swings can overwhelm the contribution of labor productivity.

## Firm availability
The injected population is meaningful but likely overstates clean targets. Captive facilities, strategic infrastructure, asset-only structures, environmental liabilities, permits, land rights, pipeline links, and large inventory-finance needs reduce eligibility and complicate control transfers. Marketplace wholesale data show transactions occur but are a weak proxy for petroleum terminals.

## Demand durability
Domestic gasoline volumes are declining with fuel efficiency, but export flows and other petroleum products support continued throughput. Over five years, service quantity is more likely to edge down than collapse. Almost all surviving quantity still needs physical storage and transfer infrastructure plus a responsible operator.

## Risks and uncertainty
Material risks include spills, legacy contamination, tank integrity, fire, cyber intrusion into operational technology, permits, climate and transition policy, geographic concentration, customer and supplier dependence, basis and inventory exposure, and catastrophic working-capital needs. Evidence is weakest on six-digit task weights, firm eligibility, private transfer incidence, and retained automation economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0038 | — | OBSERVED | — |
| n | — | 654 | — | ESTIMATE | — |
| a | 0.1 | 0.19 | 0.3 | PROXY | S2, S3 |
| rho | 0.25 | 0.46 | 0.64 | ESTIMATE | S4, S5 |
| e | 0.35 | 0.57 | 0.74 | ESTIMATE | S1, S4 |
| s5 | 0.06 | 0.13 | 0.23 | PROXY | S6 |
| q | 0.2 | 0.39 | 0.58 | ESTIMATE | S7 |
| d5 | 0.85 | 0.97 | 1.1 | PROXY | S1, S7, S8, S9 |
| o | 0.9 | 0.97 | 0.995 | PROXY | S1, S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.00 | 0.01 | 0.03 | ESTIMATE |
| F | 4.33 | 6.28 | 7.59 | ESTIMATE |
| C | 4.00 | 7.80 | 10.00 | ESTIMATE |
| D | 7.65 | 9.41 | 10.00 | PROXY |

## Caveats
- a: The occupation task source includes refinery operators as well as terminal pump operators and gaugers.
- a: The broader NAICS 424 employment mix is not a six-digit 424710 wage distribution.
- a: The injected compensation-to-receipts ratio is exceptionally low because receipts include high-value fuel throughput, so it should not be interpreted as a direct task mix.
- rho: No representative five-year AI adoption cohort for independent petroleum terminals was found.
- rho: Operational-technology integration and insurance approval may dominate model capability.
- e: The Census definition is establishment-oriented, while eligibility is a firm-level construct.
- e: The injected margin-bridged count may be distorted by volatile fuel receipts and may include firms whose normalized EBITDA lies outside the target band.
- s5: No six-digit control-transfer rate or owner-age series was found.
- s5: Asset purchases and portfolio transactions may not map cleanly to firm control transfers.
- q: No causal study directly measures pass-through of terminal automation savings.
- q: Commodity-price volatility can swamp labor benefits in reported gross margins.
- d5: Fuel volumes are proxies for terminal service quantity and can bypass merchant-owned facilities.
- d5: Export growth is concentrated and sensitive to geopolitics, refinery runs, and foreign demand.
- d5: Constant-quality aggregation across crude, refined products, LPG, and biofuel blends is inherently approximate.
- o: Operator-required does not mean labor-intensive; control systems may sharply reduce headcount.
- o: Demand can migrate from LMM independents to integrated or large-network operators without being eliminated.

## Sources
- **S1** — [2017 NAICS Definition: 424710 Petroleum Bulk Stations and Terminals](https://www.census.gov/naics/?details=4247&input=4247&year=2017) (accessed 2026-07-22): Defines the industry as establishments with bulk liquid storage facilities primarily engaged in merchant wholesale distribution of crude petroleum and petroleum products, including liquefied petroleum gas.
- **S2** — [Merchant Wholesalers, Nondurable Goods: NAICS 424](https://www.bls.gov/iag/tgs/iag424.htm) (accessed 2026-07-22): Reports the broader subsector's 2025 employment in common occupations, including 269,740 nontechnical sales representatives, 174,610 heavy truck drivers, 162,830 material movers, 54,000 technical sales representatives, and 43,040 shipping/receiving/traffic clerks.
- **S3** — [Petroleum Pump System Operators, Refinery Operators, and Gaugers](https://www.onetonline.org/link/details/51-8093.00) (accessed 2026-07-22): Lists core tasks including monitoring instruments, operating pumps and valves, coordinating flow, verifying meters, maintaining or reporting equipment problems, and patrolling tanks for safe and compliant operations.
- **S4** — [Overview of the Spill Prevention, Control, and Countermeasure Regulation](https://www.epa.gov/oil-spills-prevention-and-preparedness-regulations/overview-spill-prevention-control-and) (accessed 2026-07-22): States that covered facilities must prevent, prepare for, and respond to oil discharges; develop and implement SPCC plans; and follow procedures, methods, and equipment requirements.
- **S5** — [Secondary Containment for Each Container under SPCC](https://www.epa.gov/oil-spills-prevention-and-preparedness-regulations/secondary-containment-each-container-under-spcc) (accessed 2026-07-22): States that covered facilities must provide containment or diversionary structures and that bulk storage installations must contain the largest single container plus precipitation freeboard.
- **S6** — [Wholesale/Distribution Business Valuation Multiples and Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/wholesale-distribution/) (accessed 2026-07-22): Reports sold wholesale/distribution business data for 2021-2025, including $600,000 median sale price, $1,378,849 median revenue, $236,484 median owner earnings, and 199 median days on market.
- **S7** — [Increasing Fuel Efficiency Leads to Decreasing Gasoline Consumption](https://www.eia.gov/todayinenergy/detail.php?id=67426) (accessed 2026-07-22): Reports 2025 US motor-gasoline consumption of 8.9 million barrels per day, 1% below 2024 and 4% below 2019, and forecasts continued declines in 2026 and 2027 as fuel efficiency rises.
- **S8** — [Maritime Exports of Petroleum Products Increased in January 2026](https://www.eia.gov/Todayinenergy/detail.php?id=67184) (accessed 2026-07-22): Reports refined-product exports on clean tankers of 6.3 million barrels per day in January 2026, about 10% above January 2025, with diesel, gasoline, and LPG driving growth.
- **S9** — [EIA Releases the Annual Energy Outlook 2026](https://www.eia.gov/pressroom/releases/press587.php) (accessed 2026-07-22): States that US energy consumption is flat or slightly lower through 2050 in most cases, crude production is 12.4-12.7 million barrels per day in most 2050 cases versus 13.6 in 2025, and the United States remains a net petroleum exporter in nearly all cases with liquids exports increasing.
