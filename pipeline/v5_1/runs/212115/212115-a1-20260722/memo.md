# 212115 — Underground Coal Mining

*v5.1 Stage 1 research memo. Run `212115-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → CONDITIONAL · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Sensor-rich mechanized underground operations offer material gains in planning, uptime, safety, maintenance, and production coordination.
**Weakness:** Severe physical hazards, certification barriers, legacy infrastructure, and secular thermal-coal decline sharply limit realization and acquisition supply.

## Business-model lens
- Included: Independent lower-middle-market underground bituminous and anthracite coal operators and integrated beneficiators, emphasizing high-quality metallurgical, high-calorific-value thermal, and industrial coal sold through repeat domestic or export programs, multi-year contracts, exacting quality specifications, and coordinated rail, barge, or terminal logistics.
- Excluded: Surface coal mines; contract support activities classified in NAICS 213113; pure mineral royalties, brokers, and terminals; speculative undeveloped reserves; spot-only undifferentiated thermal production; captive mines without transferable customer relationships; and large diversified or publicly traded coal groups outside the LMM band.
- Customer and revenue model: Customers include domestic and foreign steel and coke producers, electric generators, and industrial users. Revenue is earned per ton under spot, annual, or multi-year agreements, with coal quality, blending, reliable delivery, technical coordination, and transport execution creating repeat program economics rather than pure service revenue.
- Deviation from default lens: none

## Executive view
Underground coal combines meaningful automation potential with formidable realization, safety, demand, and transaction constraints. The coherent target is a low-cost, well-capitalized mine producing qualified metallurgical or specialty high-calorific-value coal under repeat contracts; a marginal thermal mine is unlikely to be rescued by AI productivity alone.

## How AI changes the work
The strongest opportunities are geological and section planning, cutting-path optimization, conveyor coordination, gas and ventilation monitoring, proximity safety, roof-risk sensing, quality control, maintenance, scheduling, and compliance. Face work, roof support, bolting, ventilation, gas checks, belts, repairs, and emergency response remain physical and tightly regulated.

## Value capture
Scarce coal quality, blend performance, qualification, transport access, and reliable fulfillment can retain some value. Formal bids, benchmark and annual repricing, global competition, quality penalties, and concentrated steel or utility buyers limit capture.

## Firm availability
The dataset provides no defensible LMM firm count, and practical availability is likely exceptionally low. Reserves, geology, mine life, permits, safety history, equipment, skilled crews, union and pension exposure, reclamation, water treatment, bonding, and contract transferability all require unusually deep diligence.

## Demand durability
Domestic thermal coal remains structurally challenged, while metallurgical, industrial, high-calorific-value, and export programs provide partial resilience. Five-year underwriting should still assume contraction and cyclicality unless the target owns scarce quality at a durable cost position.

## Risks and uncertainty
Key uncertainties include missing firm-count data, thermal versus metallurgical mix, reserve and roof conditions, production interruptions, methane and dust, safety compliance, labor, pension and health obligations, water and reclamation liabilities, equipment capex, customer qualification, logistics, export access, and price cycles.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2344 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.32 | 0.48 | 0.62 | PROXY | S1, S2, S3, S4 |
| rho | 0.22 | 0.39 | 0.56 | ESTIMATE | S3, S4 |
| e | 0.13 | 0.26 | 0.41 | PROXY | S5 |
| s5 | 0.04 | 0.1 | 0.18 | PROXY | S6 |
| q | 0.25 | 0.43 | 0.6 | PROXY | S5 |
| d5 | 0.65 | 0.82 | 0.99 | PROXY | S5, S7 |
| o | 0.91 | 0.97 | 1 | ESTIMATE | S5, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.66 | 1.76 | 3.26 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 5.00 | 8.60 | 10.00 | PROXY |
| D | 5.92 | 7.95 | 9.90 | ESTIMATE |

## Caveats
- a: NIOSH evidence describes technology adoption and safety issues rather than labor-productivity estimates.
- a: Continuous-miner and longwall operations have different task structures.
- a: Automation may relocate workers to control and maintenance roles without eliminating labor.
- rho: No representative LMM U.S. underground-coal AI adoption study was found.
- rho: Safety systems can add controls without reducing production labor.
- rho: New software failure modes raise the threshold for unattended operation.
- e: Long-term coal supply is recurring product revenue, not subscription revenue.
- e: The company proxy includes surface mines and a marine terminal.
- e: Export metallurgical contracts may reprice to volatile indices.
- s5: The dataset intentionally provides no n-band estimate.
- s5: Cross-industry owner intentions are not observed mine transactions.
- s5: A mine sold in bankruptcy may not be a viable going concern.
- q: Capture is likely higher for scarce metallurgical grades than ordinary thermal coal.
- q: Multi-year volume does not guarantee fixed margin.
- q: Customers can diversify blends and origins over time.
- d5: EIA's short-term aggregate forecast does not separate underground mining.
- d5: Company mix and merger effects are not an industry forecast.
- d5: Steel cycles, exports, regulation, weather, and gas prices create wide uncertainty.
- o: Separating AI effects from broader policy and technology trends is highly uncertain.
- o: Thermal and metallurgical coal have distinct substitution pathways.
- o: Individual mines can become obsolete because of geology, cost, or customers even if coal remains in use.

## Sources
- **S1** — [NAICS 212115 - Underground Coal Mining](https://www.naics.com/naics-code-description/?code=212115&v=2022) (accessed 2026-07-22): Industry boundary for underground mining, mine development, and beneficiation of bituminous and anthracite coal, with surface mining and fee-based support excluded.
- **S2** — [Continuous Mining Machine Operators](https://www.onetonline.org/link/summary/47-5041.00) (accessed 2026-07-22): Direct occupational evidence on cutting and conveying coal, ventilation, methane checks, roof and rib inspection, machine control and positioning, maintenance, dust control, safety supports, coordination, and physical work.
- **S3** — [NIOSH Automation and Emerging Technologies Partnership](https://www.cdc.gov/niosh/mining/partnerships/automation.html) (accessed 2026-07-22): Official evidence on growing use of autonomous vehicles, wireless communications, digital sensors, human-machine interfaces, data analytics, and automation at surface and underground mines, with safety and adoption concerns.
- **S4** — [NIOSH Mining and Machinery Struck-by Injuries](https://www.cdc.gov/niosh/mining/topics/machinery-struck-by-injuries.html) (accessed 2026-07-22): Underground coal safety and technology evidence covering programmable controls, longwall and continuous-mining equipment, software failure modes, functional safety, proximity detection, and machine hazards.
- **S5** — [Core Natural Resources 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1710366/000171036626000007/cnr-20251231.htm) (accessed 2026-07-22): Underground mine and customer mix, thermal and metallurgical sales, contract duration and renewals, domestic and export pricing, quality adjustments, logistics, competition, and market risks.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry owner-age and five-year sale, transfer, closure, and succession-intention evidence.
- **S7** — [EIA Short-Term Energy Outlook: Coal Markets, July 2026](https://www.eia.gov/outlooks/steo/report/elec_coal_renew.php) (accessed 2026-07-22): Official observed and forecast U.S. coal production, consumption, inventories, coal-fired generation, wind, and solar capacity through 2027.
