# 336991 — Motorcycle, Bicycle, and Parts Manufacturing

*v5.1 Stage 1 research memo. Run `336991-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.14 · L 1.06 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Transferable engineered parts, aftermarket fitment, and repeat dealer or OEM relationships can create durable revenue beyond volatile new-vehicle sales.
**Weakness:** A very small estimated target pool combines with discretionary end demand and substantial manual production, limiting both acquisition availability and AI-driven labor leverage.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers whose primary activity is making motorcycles, bicycles, tricycles, similar equipment, or their parts, including design, fabrication, assembly, finishing, testing, and related aftermarket products.
- Excluded: Children's vehicles other than bicycles and metal tricycles, powered golf carts and passenger carriers, pure importers, distributors, retailers, repair shops, and captive operations that are not independently purchasable firms.
- Customer and revenue model: Sales of complete vehicles and parts to independent dealers, distributors, OEM customers, fleets, and consumers; repeat revenue can arise from replacement parts, accessories, model refreshes, and recurring OEM or dealer relationships.
- Deviation from default lens: none

## Executive view
This is a small, heterogeneous acquisition pool with useful physical-asset and engineered-product defensibility, but modest labor leverage and uneven demand. The most attractive exact-screen targets are independent component or niche-vehicle firms with repeat OEM or aftermarket revenue, transferable engineering know-how, and limited customer concentration.

## How AI changes the work
AI should improve planning, engineering support, inspection, documentation, maintenance, and dealer or customer operations more than it replaces physical fabrication and assembly. Brownfield integration and safety validation keep realized gains below headline manufacturing use cases.

## Value capture
Tooling, fitment, certification knowledge, brand, dealer access, and installed-base parts demand can retain value, while imports, customer bargaining power, discounting, and discretionary cycles leak benefits to customers and competitors.

## Firm availability
The frozen LMM count is only seven and estimated; a few captive, import-led, or founder-dependent firms could sharply reduce actionable supply. Broad employer succession data suggest some turnover, but actual niche-manufacturer transactions are unobserved.

## Demand durability
Near-term demand is soft in both cited motorcycle and bicycle channels, yet bicycle participation and maintenance activity remain supportive. Replacement parts and installed-base service make demand more durable than complete-vehicle unit sales alone.

## Risks and uncertainty
The principal uncertainties are the tiny estimated firm population, subsegment mix, customer concentration, product liability, tariff and import exposure, inventory cycles, and reliance on broad manufacturing or public-company proxies.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1834 | — | OBSERVED | — |
| n | — | 7 | — | ESTIMATE | — |
| a | 0.15 | 0.27 | 0.4 | PROXY | S2, S3 |
| rho | 0.36 | 0.55 | 0.71 | PROXY | S3 |
| e | 0.38 | 0.58 | 0.76 | ESTIMATE | S1, S5 |
| s5 | 0.14 | 0.23 | 0.36 | PROXY | S4 |
| q | 0.28 | 0.46 | 0.65 | ESTIMATE | S5, S6, S7 |
| d5 | 0.72 | 0.93 | 1.18 | PROXY | S5, S6, S7 |
| o | 0.96 | 0.99 | 0.999 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.40 | 1.09 | 2.08 | PROXY |
| F | 0.51 | 1.06 | 1.72 | ESTIMATE |
| C | 5.60 | 9.20 | 10.00 | ESTIMATE |
| D | 6.91 | 9.21 | 10.00 | ESTIMATE |

## Caveats
- a: BLS NAICS 336000 includes motor vehicles, aerospace, rail, shipbuilding, and other industries with different capital intensity and occupational mixes.
- a: NIST describes manufacturing-wide applications rather than measured task shares for NAICS 336991.
- rho: The NIST evidence establishes use cases and adoption barriers, not realized savings in this exact industry.
- rho: Realization will vary sharply between manual assemblers, precision component shops, and scaled branded manufacturers.
- e: The frozen firm count is itself an estimate and is very small, so one classification decision materially moves the ratio.
- e: Harley-Davidson illustrates a transferable operating model but is far above the LMM screen and does not measure the candidate population.
- s5: Gallup covers employer businesses across sectors, not this manufacturing niche.
- s5: Survey intentions may not convert to arm's-length control sales within five years.
- q: Harley-Davidson's premium brand and dealer network are not representative of a typical LMM parts supplier.
- q: PeopleForBikes evidence describes the U.S. bicycle market and not motorcycle or OEM component economics.
- d5: Harley-Davidson's premium heavyweight motorcycle results are not the whole motorcycle market.
- d5: Participation does not translate one-for-one into purchases of newly manufactured bicycles.
- d5: Industry mix can make a specific firm's demand path diverge substantially from the blended range.
- o: This is a legal-structural estimate rather than an observed industry statistic.
- o: A business may be legally ownable yet economically dependent on nontransferable founder, brand, dealer, or OEM relationships.

## Sources
- **S1** — [2022 NAICS Manual: 336991 Motorcycle, Bicycle, and Parts Manufacturing](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Exact industry scope, included activities, and explicit exclusions for children's vehicles and powered golf carts/passenger carriers.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 336000 Transportation Equipment Manufacturing](https://www.bls.gov/oes/2023/may/naics3_336000.htm) (accessed 2026-07-22): Broad transportation-equipment occupational mix, including the large production share and smaller business/financial-operations share used to bound task exposure.
- **S3** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Manufacturing AI adoption, use cases in maintenance, quality, forecasting, assembly, vision, documentation, supply chain, scheduling and digital twins, plus cost, skill, data, cyber and legacy-integration barriers.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): All-industry employer-business ownership aging and five-year sell-or-transfer intentions used as the succession-supply proxy.
- **S5** — [Harley-Davidson, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/793952/000079395226000011/hog-20251231.htm) (accessed 2026-07-22): Motorcycle manufacturer revenue model, independent dealer network, parts and accessories mix, inventory reduction, and recent retail-unit contraction.
- **S6** — [If Americans Are Riding, Why Aren't They Buying?](https://www.peopleforbikes.org/news/if-americans-are-riding-why-arent-they-buying) (accessed 2026-07-22): Bicycle sales softness, pandemic pull-forward and discounting, price changes, and relative strength in service, helmets, and maintenance tools.
- **S7** — [Bicycling Participation Report 2024](https://www.peopleforbikes.org/news/bicycling-participation-report-2024) (accessed 2026-07-22): Record 2024 U.S. bicycle participation and rising youth participation as directional support for installed-base and long-run category demand.
