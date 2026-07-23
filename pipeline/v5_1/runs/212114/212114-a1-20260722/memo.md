# 212114 — Surface Coal Mining

*v5.1 Stage 1 research memo. Run `212114-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Autonomous haulage and mine optimization can materially lower cost per ton in repetitive, equipment-intensive surface operations.
**Weakness:** Secular thermal-coal contraction and large, difficult-to-transfer reclamation and customer risks can overwhelm productivity gains.

## Business-model lens
- Included: Independent lower-middle-market surface coal operators and beneficiators, emphasizing mines serving adjacent power or industrial facilities under long-term cost-reimbursement, management-fee, requirements, or indexed supply agreements, together with specialized high-quality coal programs where reliability, consistent specifications, and mine-to-customer logistics matter.
- Excluded: Underground coal mines; contract support activities classified in NAICS 213113; pure mineral royalties and brokers; captive mines with no transferable customer relationship; speculative undeveloped reserves; spot-only commodity production; and large diversified or publicly traded coal groups outside the LMM band.
- Customer and revenue model: Customers include electric generators, industrial facilities, and steel producers. Revenue is typically recognized per ton delivered under spot or term supply contracts; the service-like subset earns inflation-linked management fees or agreed profit per ton under long-duration, dedicated-mine arrangements that may reimburse operating, capital, and reclamation costs.
- Deviation from default lens: none

## Executive view
Surface coal mining has meaningful automation potential, especially in haulage, dispatch, planning, and maintenance, but demand and availability dominate the investment case. The coherent target is a dedicated, low-cost surface mine with a long-term reimbursed or management-fee contract, not a spot-exposed thermal producer carrying open-ended reclamation and reinvestment risk.

## How AI changes the work
Autonomous haulage, fleet orchestration, geological modeling, blast and mine planning, quality blending, equipment monitoring, predictive maintenance, safety analytics, and environmental documentation can reduce cost per ton. Drilling, blasting, excavation, repair, sampling, preparation, and reclamation remain heavily physical and safety-critical.

## Value capture
Dedicated-mine geography, coal specifications, transport constraints, and long-term contracts can preserve part of the benefit. Cost-plus contracts may pass savings to customers, while competitive bids, price reopeners, indices, and substitute fuels limit capture for ordinary suppliers.

## Firm availability
The dataset has no defensible LMM firm count, and practical supply is likely thin. Permit transfer, reserve life, bonding, environmental and reclamation obligations, customer concentration, fleet condition, labor, and financing must be resolved before ordinary commercial diligence matters.

## Demand durability
AI-related electricity load may delay some plant retirements, and metallurgical or export demand offers diversification. EIA nevertheless forecasts falling U.S. coal production and power-sector consumption, so a five-year underwriting case should assume contraction unless protected by a durable dedicated-customer arrangement.

## Risks and uncertainty
Principal uncertainties are missing target-count data, coal type and basin mix, power-plant retirement, regulation, natural-gas prices, export markets, reserve quality, strip ratios, equipment capex, permits, reclamation and water liabilities, bonding, labor, and contract transferability.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2344 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.38 | 0.55 | 0.7 | PROXY | S1, S2, S3 |
| rho | 0.3 | 0.48 | 0.65 | ESTIMATE | S2, S3 |
| e | 0.16 | 0.3 | 0.45 | PROXY | S4, S5 |
| s5 | 0.05 | 0.12 | 0.2 | PROXY | S6 |
| q | 0.3 | 0.48 | 0.65 | PROXY | S4, S5 |
| d5 | 0.58 | 0.75 | 0.91 | PROXY | S5, S7 |
| o | 0.92 | 0.98 | 1 | ESTIMATE | S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.07 | 2.48 | 4.27 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 6.00 | 9.60 | 10.00 | PROXY |
| D | 5.34 | 7.35 | 9.10 | ESTIMATE |

## Caveats
- a: Autonomous haulage evidence spans large global mines and multiple commodities.
- a: O*NET covers excavating and loading operators rather than every mine occupation.
- a: Automation may shift labor to remote operations, maintenance, and systems support rather than eliminate it.
- rho: No representative LMM U.S. surface-coal AI adoption study was found.
- rho: Greenfield fleets are easier to automate than mixed legacy equipment.
- rho: Regulatory and customer approval can slow operational changes.
- e: The strongest fee-based examples are specialized and may not represent small independent mines.
- e: Long-term coal supply is recurring but still product revenue.
- e: Contract support activity can fall in NAICS 213113 rather than 212114.
- s5: The dataset intentionally provides no n-band estimate.
- s5: Cross-industry owner intentions are not observed coal-mine transactions.
- s5: Asset sales in bankruptcy may not be viable going concerns.
- q: Some cost-plus structures pass savings directly to the customer.
- q: Dedicated-mine contracts create bilateral dependence rather than supplier power alone.
- q: Spot and export pricing sharply reduce capture.
- d5: A two-year STEO is not a five-year industry forecast.
- d5: National coal trends may understate resilience of low-cost surface basins or metallurgical products.
- d5: Weather, gas prices, regulation, exports, and power demand create wide uncertainty.
- o: Separating AI effects from broader energy policy and technology trends is highly uncertain.
- o: Thermal and metallurgical coal have different substitution pathways.
- o: Mine-level obsolescence can be severe even when the commodity remains in use.

## Sources
- **S1** — [NAICS 212114 - Surface Coal Mining](https://www.naics.com/naics-code-description/?code=212114&v=2022) (accessed 2026-07-22): Industry boundary for surface mining, mine development, and beneficiation of bituminous coal, lignite, and anthracite, with contract support activities excluded.
- **S2** — [Excavating and Loading Machine and Dragline Operators, Surface Mining](https://www.onetonline.org/link/summary/47-5022.00) (accessed 2026-07-22): Direct occupational evidence on surface excavation and loading, equipment inspection and maintenance, coordination, material movement, outdoor and hazardous work, machine control, and physical task content.
- **S3** — [Cat MineStar Command for Autonomous Hauling](https://www.cat.com/en_US/by-industry/mining/minexpo2024/news/press-releases/cat-minestar-command-for-hauling-manages-the-autonomous-ecosystem-to-increase-haulage-efficiency-enhance-safety.html) (accessed 2026-07-22): Deployed mining-autonomy evidence for coal and other commodities covering haulage, fleet assignment, tracking, production records, material management, maintenance, safety, productivity, and fuel use.
- **S4** — [NACCO Industries 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/789933/000078993326000088/ncar25entire.htm) (accessed 2026-07-22): Surface-coal service-model proxy with dedicated mines, inflation-linked management fees per ton, customer-funded operating, capital and reclamation costs, predictable cash flow, and compensated reclamation services.
- **S5** — [Peabody Energy 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1064728/000106472826000006/btu-20251231.htm) (accessed 2026-07-22): Coal customers, long-term and spot supply structures, backlog, reliability and service rationale, pricing and quality terms, and U.S. thermal market exposure.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry owner-age and five-year sale, transfer, closure, and succession-intention evidence.
- **S7** — [EIA Short-Term Energy Outlook: Coal Markets, July 2026](https://www.eia.gov/outlooks/steo/report/elec_coal_renew.php) (accessed 2026-07-22): Official observed and forecast U.S. coal production, consumption, inventories, coal-fired generation, wind, and solar capacity through 2027.
