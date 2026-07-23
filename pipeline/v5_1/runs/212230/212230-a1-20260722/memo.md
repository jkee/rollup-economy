# 212230 — Copper, Nickel, Lead, and Zinc Mining

*v5.1 Stage 1 research memo. Run `212230-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.21 · L 0.39 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Electrification and critical-mineral demand support physical base-metal extraction and beneficiation.
**Weakness:** Most mine owners sell commodities rather than a recurring outsourced service, leaving very few verifiably eligible firms.

## Business-model lens
- Included: US lower-middle-market firms classified in copper, nickel, lead, or zinc mine development, extraction, and beneficiation that repeatedly provide externally contracted or customer-dedicated mining and concentrate supply operations.
- Excluded: Mine-owning commodity producers lacking an outsourced-service relationship, exploration shells without operating revenue, captive mine units, royalty and financing vehicles, dormant properties, firms outside the EBITDA band, and standalone support contractors classified elsewhere.
- Customer and revenue model: Eligible firms earn repeat revenue under external operating, processing, tolling, dedicated offtake, or customer-specific supply arrangements; ordinary spot or merchant sale of ore from a firm's own resource is not by itself an outsourced service.
- Deviation from default lens: none

## Executive view
Base-metal mining has durable physical demand and useful AI applications, but it fits the frozen recurring outsourced-service lens poorly. Most operators monetize owned mineral output, not an outsourced customer service, and the estimated LMM population is very small.

## How AI changes the work
AI can improve geology, scheduling, fleet dispatch, predictive maintenance, recovery optimization, safety monitoring, procurement, and reporting. Drilling, blasting, extraction, haulage, maintenance, beneficiation, and accountable safety remain physical and site-specific.

## Value capture
Global commodity pricing can let a low-cost producer retain savings initially, but depletion, grades, royalties, labor, suppliers, contract resets, and cost-curve competition absorb benefits. Commodity-price movements can overwhelm the measured AI effect.

## Firm availability
Most 212230 firms are ineligible because repeated commodity sales are not an outsourced service. Any qualifying contract, tolling, or customer-dedicated operators require firm-level verification, and control transfers face environmental and permitting diligence.

## Demand durability
BLS projects growth in broader metal-ore output, while copper and nickel benefit from electrification and supply-security priorities. Domestic output remains exposed to permits, depletion, capital intensity, imports, recycling, and price cycles.

## Risks and uncertainty
The lens mismatch, tiny firm count, four-digit proxies, commodity volatility, environmental liabilities, reserve quality, permitting, water and energy needs, labor safety, and long capital cycles make the result highly uncertain.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.134 | — | OBSERVED | — |
| n | — | 9 | — | ESTIMATE | — |
| a | 0.1 | 0.19 | 0.3 | PROXY | S2, S4 |
| rho | 0.27 | 0.46 | 0.63 | ESTIMATE | S4, S5 |
| e | 0.05 | 0.18 | 0.35 | ESTIMATE | S1 |
| s5 | 0.07 | 0.17 | 0.3 | PROXY | S8 |
| q | 0.38 | 0.59 | 0.76 | ESTIMATE | S6, S7 |
| d5 | 0.98 | 1.14 | 1.32 | PROXY | S3, S6, S7 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S1, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.14 | 0.47 | 1.01 | ESTIMATE |
| F | 0.05 | 0.39 | 1.07 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 9.41 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source covers all metal ore mining.
- a: Task exposure is inferred rather than observed.
- a: The supplied compensation ratio has a wage/receipts vintage mismatch and may be distorted by volatile metal prices.
- rho: NIOSH evidence establishes active automation research and safety barriers, not realized labor substitution.
- rho: Implementation economics differ sharply between open-pit and underground operations.
- e: No source measures the eligible share directly.
- e: Establishment classification does not reveal contract structure or firm ownership.
- e: The supplied count is margin-bridged in a highly cyclical industry and may include explorers, subsidiaries, or temporarily profitable mines.
- s5: The source is cross-industry, owner-level, and dated 2018.
- s5: Property acquisitions are not necessarily qualifying firm control transfers.
- s5: Owner age is less relevant for public, sponsor-owned, and joint-venture mines.
- q: No source directly measures pass-through of AI-enabled mining savings.
- q: Global commodity prices can dominate firm margins and obscure retention.
- q: Cost reductions may extend mine life rather than appear as near-term retained cash benefit.
- d5: BLS output is four-digit and includes other metals.
- d5: End-use demand does not guarantee US mine production.
- d5: Commodity price volatility complicates constant-price quantity inference.
- o: The accountable entity may consolidate into a larger miner or contract operator.
- o: Autonomous equipment reduces onsite labor but does not remove an accountable mine operator.

## Sources
- **S1** — [2022 NAICS definition: Copper, Nickel, Lead, and Zinc Mining](https://www.census.gov/naics/?details=212230&input=212230&year=2022) (accessed 2026-07-23): Defines the industry as mine-site development, mining, and beneficiation of ores valued chiefly for copper, nickel, lead, or zinc, including concentrate production.
- **S2** — [May 2023 OEWS: Metal Ore Mining](https://www.bls.gov/oes/2023/may/naics4_212200.htm) (accessed 2026-07-23): Reports the broader-industry occupational mix, including 44.75% construction and extraction, 5.76% architecture and engineering, 3.87% science, 3.35% office support, and 4.97% transportation and material moving.
- **S3** — [Employment and output by industry, 2024–34](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-23): Projects metal ore mining real output from $26.0 billion in 2024 to $33.5 billion in 2034, a 2.6% annual compound rate.
- **S4** — [NIOSH Mining Health and Safety Research Contracts](https://www.cdc.gov/niosh/mining/about/contracts.html) (accessed 2026-07-23): Documents research on autonomous mining systems, automated rockfall detection, machine-learning perception, safety analytics, and barriers to automation.
- **S5** — [Mining and Machinery Struck-by Injuries](https://www.cdc.gov/niosh/mining/topics/machinery-struck-by-injuries.html) (accessed 2026-07-23): Describes programmable electronic control, proximity detection, automation benefits, new failure modes, and mining functional-safety challenges.
- **S6** — [Mineral Commodity Summaries 2026](https://pubs.usgs.gov/publication/mcs2026) (accessed 2026-07-23): Provides USGS production, consumption, trade, recycling, import-reliance, price, reserve, and industry information for individual mineral commodities.
- **S7** — [2023 Critical Materials Assessment](https://www.energy.gov/sites/default/files/2023-05/2023-critical-materials-assessment.pdf) (accessed 2026-07-23): Assesses copper and nickel energy demand and supply risks, including electrification-driven demand and constraints on suitable nickel supply.
- **S8** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-23): Reports that 51% of responding owners of US employer businesses were age 55 or older in 2018.
