# 333131 — Mining Machinery and Equipment Manufacturing

*v5.1 Stage 1 research memo. Run `333131-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.36 · L 1.00 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring replacement, wear, and qualification needs support a durable physical operator while AI improves engineering and operating workflows.
**Weakness:** Commodity-cycle volatility and concentrated sophisticated buyers can depress demand and reclaim productivity gains.

## Business-model lens
- Included: US lower-middle-market manufacturers of underground mining machinery, stationary mineral-processing and beneficiating machinery, and related repeat equipment or parts programs supplied to external mining customers.
- Excluded: Captive internal shops, shells, non-control financing vehicles, surface mining machinery, well-drilling machinery, coal and ore conveyors, underground mining locomotives, pure distributors, rental-only operations, and repair businesses classified outside NAICS 333131.
- Customer and revenue model: Project and repeat B2B sales of engineered machines, modules, replacement units, and manufacturer-supplied parts to mines, mineral processors, contractors, and equipment integrators; revenue is usually quoted per machine, system, or order, with recurring demand tied to wear, capacity, mine plans, and installed equipment.
- Deviation from default lens: none

## Executive view
Mining machinery manufacturing combines repeat, specification-heavy physical work with meaningful engineering and planning workflows. AI can improve the information layer, but fabrication, assembly, testing, and accountability remain central; commodity cyclicality and large-customer bargaining power are the principal commercial constraints.

## How AI changes the work
AI can accelerate design retrieval and reuse, bills of material, quoting, scheduling, procurement, technical documentation, service knowledge, defect analysis, inspection, and predictive maintenance. It is less able to remove skilled welding, machining, assembly, commissioning, and safety-critical review.

## Value capture
Fixed or quoted equipment orders can preserve savings until repricing, and proprietary performance, qualification, uptime, and lifecycle support create differentiation. Rebid pressure, global competition, cost-escalation clauses, and sophisticated mining customers can reclaim direct cost savings.

## Firm availability
The dataset estimates 94 LMM firms, but that figure is margin-bridged rather than observed. Independent specialty OEMs with recurring parts, replacement, and upgrade demand should qualify, while captive shops, one-off fabricators, distributors, repair businesses, classification errors, and non-stand-alone operations reduce the eligible pool.

## Demand durability
Equipment wear, fleet age, mine replacement, mineral processing, and critical-mineral investment support demand. Commodity prices, coal exposure, capital discipline, permitting, project delays, and mine cycles can still produce severe five-year volatility.

## Risks and uncertainty
The evidence relies on broad machinery occupations and output, manufacturing-wide AI adoption, general employer succession, and large-OEM market signals. Actual outcomes hinge on product niche, commodity exposure, installed base, customer concentration, engineering ownership, safety validation, legacy systems, and the cyclicality at transaction time.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1901 | — | OBSERVED | — |
| n | — | 94 | — | ESTIMATE | — |
| a | 0.13 | 0.24 | 0.37 | PROXY | S1, S2, S3 |
| rho | 0.36 | 0.55 | 0.72 | PROXY | S3 |
| e | 0.5 | 0.68 | 0.84 | ESTIMATE | S1, S5 |
| s5 | 0.14 | 0.23 | 0.35 | PROXY | S4 |
| q | 0.4 | 0.57 | 0.74 | ESTIMATE | S5 |
| d5 | 0.78 | 1.05 | 1.28 | PROXY | S6, S7 |
| o | 0.93 | 0.98 | 0.998 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.36 | 1.00 | 2.03 | PROXY |
| F | 3.26 | 4.43 | 5.40 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.25 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation mix is for a broad machinery aggregate rather than this six-digit industry.
- a: NIST use cases establish manufacturing applicability but not mining-machinery task exposure.
- a: The injected compensation ratio uses 2024 wages over 2022 receipts and is harmonized, but it is not used to set this task share.
- rho: Use of general AI tools is not the same as implementing a share of exposed wage opportunity.
- rho: Project-based, low-volume engineering and fragmented legacy systems may slow adoption relative to repetitive manufacturing.
- e: No source measures eligibility under the fixed lens.
- e: Large OEM lifecycle-service models may overstate recurring revenue available to LMM specialty manufacturers.
- e: The injected count of 94 LMM firms is an estimate based on a margin bridge.
- s5: Gallup covers employer firms across industries and sizes, not NAICS 333131 LMM manufacturers.
- s5: Plans are not completed qualifying control transfers.
- s5: Corporate product-line divestitures and internal reorganizations require separate treatment.
- q: Caterpillar's integrated lifecycle model and scale are not representative of LMM bargaining power.
- q: Retention differs between proprietary machines, custom systems, build-to-print components, and commodity wear parts.
- q: Demand changes and implementation difficulty are excluded and represented in d5, o, and rho.
- d5: BLS combines several machinery industries and does not isolate NAICS 333131.
- d5: Caterpillar serves surface mining, heavy construction, and quarry markets beyond this code and is a much larger global manufacturer.
- d5: Mining cycles can dominate a five-year window even when long-run mineral demand is favorable.
- o: End-market contraction belongs in d5; o concerns only whether surviving demand still requires this kind of external accountable operator.
- o: Large-OEM autonomy evidence does not measure displacement of LMM manufacturers.

## Sources
- **S1** — [2022 NAICS Manual — 333131 Mining Machinery and Equipment Manufacturing](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines underground mining and mineral-beneficiation machinery in the industry and identifies excluded adjacent equipment.
- **S2** — [May 2023 OEWS: Machinery Manufacturing (3331, 3332, 3334, and 3339)](https://www.bls.gov/oes/2023/may/naics4_3330A1.htm) (accessed 2026-07-22): Provides the broader machinery occupational mix used to bridge wage-weighted task exposure.
- **S3** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Reports manufacturing AI adoption, applicable use cases, expected investment, and implementation barriers.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports employer-business owner age and five-year plans to sell or transfer ownership.
- **S5** — [Caterpillar 2025 Annual Report Highlights](https://www.caterpillar.com/en/investors/reports/annual-report/segment-highlights.html) (accessed 2026-07-22): Describes lifecycle solutions, customer agreements, connected assets, AI-enabled tools, autonomous mining equipment, and the role of uptime and productivity.
- **S6** — [Caterpillar 2025 Chairman and CEO Message](https://www.caterpillar.com/en/investors/reports/annual-report/ceo-message.html) (accessed 2026-07-22): Provides a current manufacturer perspective on critical-mineral extraction and long-duration physical-infrastructure demand.
- **S7** — [BLS Employment and Output by Industry, 2024–2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects real output for the broader machinery grouping containing 3331 from 241.2 to 266.8 billion chained 2017 dollars.
