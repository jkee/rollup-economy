# 311511 — Fluid Milk Manufacturing

*v5.1 Stage 1 research memo. Run `311511-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.15 · L 0.40 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Regulatory and cold-chain requirements make surviving fluid-product volume inseparable from an accountable physical processor.
**Weakness:** Secular beverage-milk decline, low labor intensity, customer bargaining, and retailer insourcing limit both opportunity size and retention.

## Business-model lens
- Included: U.S. lower-middle-market dairy and beverage processors providing recurring private-label or contract pasteurization, homogenization, blending, filling, packaging, cold-chain, quality-assurance, and related manufacturing services for fluid milk, cream, sour cream, and fluid dairy substitutes classified in 311511.
- Excluded: Own-brand-only dairies, captive retailer plants, dairy farms, distributors without processing responsibility, dry or ultra-high-temperature milk operations classified in 311514, frozen-dessert plants, non-control financing vehicles, and facilities primarily classified outside 311511.
- Customer and revenue model: Retailers, institutions, foodservice operators, and beverage brands contract for repeated production and packaging runs, generally under per-gallon, per-unit, tolling, or supply agreements with raw-material, packaging, freight, and commodity-price adjustment mechanisms.
- Deviation from default lens: none

## Executive view
The relevant opportunity is limited to independent fluid processors with recurring external private-label or co-manufacturing revenue. AI can improve planning, routing, quality records, maintenance, order handling, and inspection support, but low labor intensity and physical cold-chain operations cap the opportunity. Long-running beverage-milk decline and retailer insourcing pressure demand, while the surviving production remains tightly regulated and operator-required.

## How AI changes the work
AI can reduce work in production and route scheduling, demand forecasting, procurement, laboratory and quality-data review, regulatory documentation, deviation investigation, predictive maintenance, customer service, and visual inspection. Pasteurization, sanitation, filling, cooling, driving, maintenance execution, sampling, and exception handling remain embodied, and process-control changes require validation.

## Value capture
Value retention is constrained by commodity-linked formulas, customer audits, frequent rebids, and concentrated retailers or institutions. Operators can better defend benefits tied to reduced spoilage, higher yield, uptime, service levels, route density, fewer quality events, and faster product development than transparent direct-labor savings.

## Firm availability
Private-label and co-packing models exist, including plants that span dairy and dairy alternatives, but many firms are own-brand, cooperative, or captive facilities. Employer-owner intentions and a recent multi-generation dairy transfer show availability, while continued consolidation and vertical integration can reduce the independent pool.

## Demand durability
Per-capita fluid-milk demand has declined for decades and continues to face generational beverage substitution. Population, school programs, cream and cultured products, flavored milk, private label, and dairy substitutes soften the decline. Surviving volume must still pass through an accountable physical processing and packaging operation.

## Risks and uncertainty
Major risks are continued volume decline, retailer insourcing, customer concentration, thin margins, raw-milk and packaging volatility, spoilage, cold-chain failure, recalls, PMO compliance, environmental pathogens, route density, and capital needs. The exact eligible-firm share and contract economics are not publicly measured.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0932 | — | OBSERVED | — |
| n | — | 79 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.33 | PROXY | S2, S3 |
| rho | 0.28 | 0.47 | 0.65 | PROXY | S3, S4, S5 |
| e | 0.1 | 0.22 | 0.36 | ESTIMATE | S1, S6, S7 |
| s5 | 0.1 | 0.2 | 0.31 | PROXY | S8, S9 |
| q | 0.28 | 0.48 | 0.66 | ESTIMATE | S6, S7, S11 |
| d5 | 0.76 | 0.87 | 0.98 | PROXY | S10, S11 |
| o | 0.84 | 0.94 | 0.99 | PROXY | S4, S5, S11 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.15 | 0.40 | 0.80 | PROXY |
| F | 0.94 | 2.41 | 3.67 | ESTIMATE |
| C | 5.60 | 9.60 | 10.00 | ESTIMATE |
| D | 6.38 | 8.18 | 9.70 | PROXY |

## Caveats
- a: OEWS covers all dairy manufacturing, including cheese, butter, and dry dairy products, not fluid milk alone.
- a: Physical automation is counted only where AI changes current tasks, not as a generic capital-equipment opportunity.
- rho: Reported smart-manufacturing gains are self-reported, cross-industry, and not AI-specific.
- rho: PMO constraints limit autonomous control changes more than back-office and decision-support workflows.
- e: Public co-packer examples establish the model but do not measure industry prevalence.
- e: The frozen firm count is an EBITDA-band estimate and may include cooperatives, mixed-product plants, or branded-only firms.
- s5: Cross-industry owner intentions are not completed transfers.
- s5: Consolidation can create transactions while simultaneously shrinking the independent target population.
- q: Contract terms vary among regional retail, school, institutional, and branded-beverage customers.
- q: No public evidence directly measures retained AI benefit for fluid-milk co-packers.
- d5: Per-capita beverage-milk decline is not the same as total eligible co-manufacturing volume.
- d5: The NAICS definition includes fluid dairy substitutes, while some long-shelf-life products are classified elsewhere.
- o: Operator necessity is high, but the relevant independent operator can be displaced by a captive customer plant.
- o: Quantity eliminated by beverage substitution belongs in d5 and is not deducted again here.

## Sources
- **S1** — [2022 NAICS Definition: 311511 Fluid Milk Manufacturing](https://www.census.gov/naics/?details=311&input=311&year=2022) (accessed 2026-07-22): Defines 311511 as manufacturing processed milk products such as pasteurized milk, cream, and sour cream, and fluid milk substitutes from soybeans and other nondairy substances.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311500](https://www.bls.gov/oes/2023/may/naics4_311500.htm) (accessed 2026-07-22): Reports dairy-manufacturing employment and wages, including 47.64% production, 18.61% transportation/material moving, 7.60% maintenance, and 6.77% office-support employment.
- **S3** — [2025 Smart Manufacturing and Operations Survey](https://www.deloitte.com/us/en/insights/industry/manufacturing-industrial-products/2025-smart-manufacturing-survey.html) (accessed 2026-07-22): A 600-respondent manufacturing survey reporting 7%-20% employee-productivity improvement, 10%-15% unlocked capacity, and process automation as a top-two priority for 46% of respondents.
- **S4** — [Grade A Pasteurized Milk Ordinance, 2023 Revision](https://www.fda.gov/media/180975/download) (accessed 2026-07-22): Specifies chemical, physical, bacteriological, temperature, sanitation, equipment, pasteurization, aseptic-processing, packaging, and related standards for Grade A milk and milk products.
- **S5** — [Keeping Your Milk Safe From the Grass to the Glass](https://www.fda.gov/consumers/consumer-updates/keeping-your-milk-safe-grass-glass) (accessed 2026-07-22): Explains PMO coverage of heating, cooling, transport, storage, processing and packaging equipment, worker safety, laboratory testing, and plant traceability codes.
- **S6** — [Scott Brothers Dairy Private Label and Co-Packing Capabilities](https://www.scottbrothers.com/) (accessed 2026-07-22): Documents private-label and co-packing for pasteurized and homogenized fluid milk, dairy products, and nondairy items.
- **S7** — [Byrne Dairy Private Label and Beverage Co-Manufacturing Capabilities](https://byrne1933.com/capabilities/) (accessed 2026-07-22): Documents private-label beverage co-manufacturing, formulation, scale-up, shelf-life and analytical testing, ESL processing, and aseptic milk capabilities.
- **S8** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of employer-business owners planned to sell or transfer ownership within five years in a fall 2024 survey of 1,264 U.S. owners.
- **S9** — [Prairie Farms Acquires Dairy Manufacturer SmithFoods](https://www.dairyprocessing.com/articles/2784-prairie-farms-acquires-dairy-manufacturer-smithfoods) (accessed 2026-07-22): Reports Prairie Farms' October 2024 acquisition of fourth-generation SmithFoods and its Ohio dairy facilities producing milk, cultured products, custom blends, and plant-based beverages.
- **S10** — [Fluid Milk Consumption Continues Downward Trend, Proving Difficult to Reverse](https://www.ers.usda.gov/amber-waves/2022/june/fluid-milk-consumption-continues-downward-trend-proving-difficult-to-reverse) (accessed 2026-07-22): Reports more than 70 years of per-capita decline, including a 20.7% fall from 2010 to 2019, and documents generational changes, school-channel shares, and limited explanatory power of plant alternatives.
- **S11** — [Walmart Will Build a $350 Million Milk Plant in South Georgia](https://apnews.com/article/walmart-milk-dairy-georgia-a5c9b8b8dab6876e5f6155aacc38ad28) (accessed 2026-07-22): Reports Walmart's planned captive milk-processing plant, the retailer's move from external dairy suppliers toward production control, and a USDA-cited 22% per-capita milk decline from 2011 to 2021.
