# 311314 — Cane Sugar Manufacturing

*v5.1 Stage 1 research memo. Run `311314-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** High-throughput sensor-rich mills and refineries can benefit from AI-enabled maintenance, optimization, quality, and planning.
**Weakness:** The frozen LMM firm count is zero, preventing defensible estimates of eligibility, transfer probability, or commercial retention.

## Business-model lens
- Included: US lower-middle-market independent cane mills or refineries repeatedly providing toll milling, toll refining, or comparable outsourced conversion services to external cane growers, raw-sugar owners, or food customers.
- Excluded: Vertically integrated farm-to-sugar operations, grower-owned cooperative processing of member cane, commodity or branded sugar sales without an outsourced-service relationship, captive facilities, and firms outside the EBITDA band.
- Customer and revenue model: Recurring conversion fees or processing margins for transforming customer-directed cane or raw sugar into raw or refined sugar; the eligible operator is paid for accountable manufacturing rather than merely selling its own sugar inventory.
- Deviation from default lens: The 2022 NAICS code combines sugarcane processing and raw-cane-sugar refining, and observed firms include vertically integrated, cooperative, and stand-alone stages. The lens is narrowed to independent repeat toll or contract conversion so the screened activity is a coherent outsourced service.

## Executive view
Cane sugar offers credible plant-optimization use cases for AI, but the frozen dataset estimates no firms in the target EBITDA band. Public industry evidence is dominated by vertically integrated and cooperative operations, leaving no defensible current LMM outsourced-service population.

## How AI changes the work
Predictive maintenance, energy and recovery optimization, raw-material scheduling, quality analytics, production reporting, and back-office copilots can improve performance. Most remaining work is physical, safety critical, and embedded in already automated process plants.

## Value capture
Value capture cannot be estimated for the lens without current toll contracts. Commodity prices, federal allotments, and integrated economics do not reveal whether an external customer would reclaim conversion savings at renewal.

## Firm availability
The frozen n input is zero. Large integrated Florida operations, Louisiana cooperatives and mills, and major refineries demonstrate a functioning industry, but not an acquirable LMM recurring-service firm; historical tolling does not cure the current evidence gap.

## Demand durability
US sugar use is broadly stable and physical cane processing remains necessary, although domestic cane output varies with crops, weather, water, closures, imports, and beet competition. Operator-required demand is durable in the industry, not necessarily in the absent target lens.

## Risks and uncertainty
The principal uncertainty is whether an eligible firm exists at all. Additional risks are legacy OT integration, cyber and food safety, campaign downtime, environmental compliance, commodity and energy exposure, federal policy dependence, and consolidation into much larger operators.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0888 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.11 | 0.2 | 0.31 | PROXY | S3, S4, S5 |
| rho | 0.31 | 0.48 | 0.65 | PROXY | S4, S5, S6 |
| e | — | — | — | MISSING | — |
| s5 | — | — | — | MISSING | — |
| q | — | — | — | MISSING | — |
| d5 | 0.9 | 1 | 1.11 | PROXY | S7, S8, S9 |
| o | 0.95 | 0.99 | 1 | PROXY | S2, S5, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.12 | 0.34 | 0.72 | PROXY |
| F | — | — | — | MISSING |
| C | — | — | — | MISSING |
| D | 8.55 | 9.90 | 10.00 | PROXY |

## Caveats
- a: No eligible LMM operator exists in the frozen dataset estimate, so this is an overall-industry proxy.
- a: The BLS occupation source includes confectionery and is not cane-specific.
- a: Installed DCS, laboratory, logistics, and packaging automation is not observed plant by plant.
- rho: The cane-specific AI case is outside the United States.
- rho: Manufacturing survey definitions may count pilots or lightweight office tools.
- rho: The absence of a current LMM lens firm makes capital and staffing assumptions hypothetical.
- e: Missing is not equivalent to zero eligibility; the denominator is estimated as zero.
- e: The frozen n input is itself an ESTIMATE based on margin-bridged size classes.
- e: NAICS entity and establishment boundaries may differ for integrated corporate groups.
- s5: Sales of integrated corporate groups, member-interest changes, internal reorganizations, and plant closures are not automatically qualifying transfers.
- s5: Historical toll-refining evidence does not establish current independent ownership.
- s5: A tiny population would make any observed rate unstable.
- q: Commodity sugar prices and federal policy do not reveal how an outsourced processor shares AI savings.
- q: Vertically integrated and cooperative economics are not substitutes for external-customer contracts.
- q: The frozen LMM count of zero leaves no observed operator whose commercial terms can anchor retention.
- d5: The current-service-basket demand is unobserved because no eligible LMM provider is identified.
- d5: USDA use data combine beet, cane, and imported sugar.
- d5: Production forecasts can differ from demand through inventories and trade adjustments.
- o: Operator requirement does not imply survival of a qualifying LMM outsourced provider.
- o: Cane, beet, and imported refined sugar can substitute at the customer level.
- o: Automation may reduce staffing sharply while leaving the facility operator necessary.

## Sources
- **S1** — [2022 NAICS definition: Cane Sugar Manufacturing](https://www.census.gov/naics/?details=311&input=311&year=2022) (accessed 2026-07-23): Defines 311314 as establishments processing sugarcane and/or refining cane sugar from raw cane sugar, confirming that the code combines milling and refining stages.
- **S2** — [Florida Crystals Sugar Refining](https://www.floridacrystalscorp.com/sugar-refining) (accessed 2026-07-23): Describes a fully vertically integrated cane sugar company that harvests, mills, refines, packages, and delivers sugar and runs its Florida refinery year-round.
- **S3** — [May 2023 OEWS: Sugar and Confectionery Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_311300.htm) (accessed 2026-07-23): Reports broader-industry employment and wages, including 42.74% production, 15.26% transportation/material moving, 5.54% maintenance, 5.73% office support, and 5.40% management.
- **S4** — [British Sugar builds an AI-powered data organization](https://www.ibm.com/case-studies/british-sugar) (accessed 2026-07-23): Documents AI, IoT sensors, machine learning, and data analytics used to create predictive-maintenance capabilities at a sugar producer.
- **S5** — [U.S. Sugar: Our Purpose and Operations](https://www.ussugar.com/purpose/) (accessed 2026-07-23): Describes a fully integrated, advanced sugarcane processing facility and states that the Clewiston mill and refinery can process up to 42,000 tons of cane per day.
- **S6** — [NAM to White House: Here's How to Boost AI Adoption in Manufacturing](https://nam.org/nam-to-white-house-heres-how-to-boost-ai-adoption-in-manufacturing/) (accessed 2026-07-23): Reports a 2025 survey in which 51% of manufacturers used AI, 60% expected to by 2027, and 80% said AI would be vital by 2030.
- **S7** — [USDA Sugar and Sweeteners Outlook: May 2026](https://ers.usda.gov/media/20880/sss-m-453.pdf?v=98857) (accessed 2026-07-23): Forecasts US total sugar use at 12.389 million STRV in both 2025/26 and 2026/27 and cane sugar production declining from 4.218 million to 4.088 million STRV.
- **S8** — [American Sugar Producers File Section 301 Comments](https://sugaralliance.org/dont-offshore-family-farms-or-american-food-production-american-sugar-producers-file-section-301-comments/41204) (accessed 2026-07-23): Reports that 12% of US cane sugar mills and refineries closed over the prior decade, including the loss of Texas cane farming in 2024.
- **S9** — [Louisiana Raw Sugar Factories](https://www.amscl.org/education/raw-sugar-factories/) (accessed 2026-07-23): Reports 11 operating Louisiana raw-sugar factories and attributes fewer mills alongside high production to increasing factory efficiency.
- **S10** — [FSMA Final Rule for Preventive Controls for Human Food](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food) (accessed 2026-07-23): Requires covered food facilities to maintain hazard analysis, preventive controls, food-safety plans, and current good manufacturing practices.
- **S11** — [Customs Ruling HQ 224418 on toll refining](https://www.customsmobile.com/rulings/docview?doc_id=HQ+224418&highlight=HQ+224418) (accessed 2026-07-23): Provides historical evidence of a US arrangement under which raw sugar was tolled into refined sugar, but does not establish current LMM eligibility or contract economics.
