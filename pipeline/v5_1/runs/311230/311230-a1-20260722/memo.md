# 311230 — Breakfast Cereal Manufacturing

*v5.1 Stage 1 research memo. Run `311230-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.57 · L 0.67 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A real outsourced co-manufacturing niche with recurring physical production and meaningful planning, quality, and documentation workflows.
**Weakness:** A tiny, poorly enumerated eligible pool operating in a cereal category with persistent unit-volume decline and strong customer repricing leverage.

## Business-model lens
- Included: Independent US breakfast-cereal co-manufacturers and private-label manufacturers repeatedly producing cereal for external brand and retail customers, within the lower-middle-market EBITDA band.
- Excluded: Branded cereal manufacturers selling their own products, captive plants, firms focused only on adjacent snacks or dry blending, non-control financing vehicles, and operations outside the EBITDA band.
- Customer and revenue model: Recurring batch production, formulation, packaging, and private-label supply for food brands and retailers, generally priced per case or production run under fixed, indexed, or periodically renewed commercial terms.
- Deviation from default lens: The NAICS definition covers product manufacturing generally, so the lens is narrowed to contract and private-label cereal manufacturing because only that subset supplies a recurring outsourced service to external customers.

## Executive view
The coherent opportunity is the small subset of cereal plants acting as repeat outsourced manufacturers for brands and retailers. AI can improve planning, documentation, quality workflows, and selective line monitoring, but physical production dominates labor and long-run cereal unit demand is weak.

## How AI changes the work
Near-term gains should come first from demand forecasting, production scheduling, procurement, maintenance triage, customer documentation, label and specification review, and computer-assisted inspection. Batchmaking, sanitation, changeovers, repairs, and material handling require equipment and human execution, keeping implementable substitution below generic knowledge-work benchmarks.

## Value capture
Fixed-term conversion pricing can let the operator retain savings initially. At renewal, transparent materials and conversion economics, competitive bids, and concentrated retail or brand customers are likely to reclaim part of the benefit through price concessions or tighter service terms.

## Firm availability
Contract and private-label cereal manufacturers demonstrably exist, but NAICS 311230 also includes branded manufacturers outside the lens. With only seven dataset-estimated LMM firms and uncertain service revenue mix, the eligible pool is likely very small and each owner decision matters.

## Demand durability
The physical manufacturing need remains operator-required, supported by food-safety accountability and specialized plant assets. However, cold-cereal box volumes have continued a long decline; niche health positioning, snack occasions, hot cereal, and private label offer offsets rather than a clear return to broad volume growth.

## Risks and uncertainty
The largest uncertainties are the eligible-firm denominator, actual plant automation baseline, customer concentration and repricing terms, and whether co-manufacturers gain share while the category contracts. Food-safety failures, recalls, allergen controls, commodity volatility, and capital-intensive line upgrades can overwhelm administrative AI savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.134 | — | OBSERVED | — |
| n | — | 7 | — | ESTIMATE | — |
| a | 0.16 | 0.25 | 0.36 | PROXY | S2, S3, S4 |
| rho | 0.34 | 0.5 | 0.66 | PROXY | S3, S4, S10 |
| e | 0.12 | 0.28 | 0.48 | ESTIMATE | S1, S5, S6, S7 |
| s5 | 0.14 | 0.27 | 0.43 | PROXY | S11, S12, S13 |
| q | 0.28 | 0.46 | 0.66 | PROXY | S8, S9 |
| d5 | 0.7 | 0.82 | 0.96 | PROXY | S14 |
| o | 0.88 | 0.94 | 0.98 | PROXY | S10, S15 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.29 | 0.67 | 1.27 | PROXY |
| F | 0.18 | 0.68 | 1.44 | ESTIMATE |
| C | 5.60 | 9.20 | 10.00 | PROXY |
| D | 6.16 | 7.71 | 9.41 | PROXY |

## Caveats
- a: The occupational source reports headcount shares, not wage-weighted task shares.
- a: Manufacturing-wide AI adoption does not establish cereal-specific technical exposure.
- a: Existing conventional automation is excluded conceptually, but plant-level installed equipment is unknown.
- rho: Survey definitions of AI include light-touch use that may not remove labor or avoid hiring.
- rho: The lens firms may have fewer engineering and data resources than surveyed manufacturers.
- rho: Food-safety and customer approval requirements vary by process and contract.
- e: The directory is not an official census and includes adjacent granola, snacks, and packaging capabilities.
- e: Public websites do not reveal EBITDA, customer mix, or whether cereal is the primary NAICS activity.
- e: The frozen n estimate is margin-bridged and may not identify the same firms represented in supplier directories.
- s5: No source measures qualifying transfers for NAICS 311230 or the contract-manufacturing subset.
- s5: Survey intentions do not equal closed transactions.
- s5: With a very small eligible population, one transaction materially changes the rate.
- q: Observed contract structures come from adjacent food categories and one older agreement.
- q: Customer concentration and private-label tender frequency are unknown for the eligible firms.
- q: This estimate excludes demand-volume loss, which is captured in d5 and o.
- d5: The observed period includes pandemic normalization and is not a clean structural forecast.
- d5: Box counts do not control for package size or distinguish branded from contract-manufactured output.
- d5: The estimate is constant-price and constant-quality, unlike reported retail revenue growth.
- o: Regulation ensures accountable facilities, not survival of any particular firm.
- o: The lens may lose quantity to larger co-manufacturers or customer-owned plants.
- o: Technological change could reduce staffing substantially without eliminating the operator entity.

## Sources
- **S1** — [2022 NAICS definition: Breakfast Cereal Manufacturing](https://www.census.gov/naics/?details=31123&input=31123&year=2022) (accessed 2026-07-23): Defines 311230 as establishments primarily manufacturing breakfast cereal foods, establishing that the code is product-based rather than limited to outsourced manufacturers.
- **S2** — [Breakfast Cereal Manufacturing Industry - Market Research Report](https://pellresearch.com/food-manufacturing/breakfast-cereal-manufacturing) (accessed 2026-07-23): Reports industry employment shares including production occupations 49%, food processing workers 17%, food batchmakers 14%, packaging and filling operators 10%, material moving 14%, maintenance 9%, and office/administrative support 7%.
- **S3** — [Monitoring AI Adoption in the US Economy](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html) (accessed 2026-07-23): Reports about 18% firm-level AI adoption at year-end 2025, 41% work-related GenAI adoption, and faster recent growth in manufacturing while noting substantial survey and population differences.
- **S4** — [NAM to White House: Here's How to Boost AI Adoption in Manufacturing](https://nam.org/nam-to-white-house-heres-how-to-boost-ai-adoption-in-manufacturing/) (accessed 2026-07-23): Reports a 2025 Manufacturing Leadership Council survey in which 51% of manufacturers used AI, 60% expected to by 2027, and 80% considered it vital by 2030.
- **S5** — [Stephano Group Co-Manufacturing & Private Label](https://stephanosbakedgoods.com/co-man-private-label.html) (accessed 2026-07-23): Confirms an operating firm offers contract and private-label manufacturing of granola, extruded cereal, and hot cereal, with R&D and regulatory support.
- **S6** — [Organic Milling - a Roskam Foods Company](https://organicmilling.roskamfoods.com/) (accessed 2026-07-23): Describes a cereal and granola contract manufacturer serving food companies and retailers, confirming the outsourced business model within the category.
- **S7** — [Cereal Manufacturers Private Label - US Supplier Directory](https://www.kokoquest.com/companies/food-beverage/cereal-manufacturers-private-label) (accessed 2026-07-23): Lists 64 US private-label cereal manufacturers as of January 2026, while descriptions show inclusion of adjacent cereal, granola, dry-goods, and packaging capabilities.
- **S8** — [Contract Manufacturing and Packaging Agreement](https://www.sec.gov/Archives/edgar/data/1431897/000119312512444185/d406800dex103.htm) (accessed 2026-07-23): Shows a food manufacturing contract that separately details material, packaging, conversion, and waste-factor costs; ingredient cost variances are reconciled and conversion cost is fixed for the initial term.
- **S9** — [Food manufacturer quarterly filing describing pricing arrangements](https://www.sec.gov/Archives/edgar/data/1669792/000110465916139289/a16-15949_110q.htm) (accessed 2026-07-23): Reports price-list, index, and annually renewed fixed-price arrangements and explains that index pricing passes through raw-material or conversion-cost changes.
- **S10** — [Frequently Asked Questions on FSMA](https://www.fda.gov/food/food-safety-modernization-act-fsma/frequently-asked-questions-fsma) (accessed 2026-07-23): States that covered facilities generally need facility-specific written food-safety plans and qualified individuals overseeing hazard controls, validation, and record review.
- **S11** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Reports a fall 2024 survey asking business owners about the next five years and finds 74% of employer-business owners plan eventually to sell or transfer ownership, while succession preparation is often weak.
- **S12** — [State of Owner Readiness](https://exit-planning-institute.org/state-of-owner-readiness) (accessed 2026-07-23): Reports that 51% of the current American business market is owned by Baby Boomers expected to transition over zero to ten years, providing broad succession context.
- **S13** — [BizBuySell Insight Report - 2024 Market Trends](https://www-tsm2.bizbuysell.com/insight-report/) (accessed 2026-07-23): Reports 9,546 closed small-business transactions in 2024, up 5%, with manufacturing among the sectors showing the strongest acquisition growth.
- **S14** — [Breakfast cereal sales declined for decades before Kellogg's sale](https://apnews.com/article/kellogg-cereal-general-mills-db705c5cbb828e31b31ac02cc4d5a886) (accessed 2026-07-23): Reports nearly 2.5 billion cereal boxes sold in the 52 weeks ending July 3, 2021 versus 2.1 billion in the comparable 2025 period, down more than 13%, within a decline lasting at least 25 years.
- **S15** — [FSMA Final Rule for Preventive Controls for Human Food](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food) (accessed 2026-07-23): States that covered food facilities must comply with risk-based preventive controls and CGMPs and maintain food-safety plans with hazard analysis and controls.
