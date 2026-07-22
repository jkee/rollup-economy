# 311221 — Wet Corn Milling and Starch Manufacturing

*v5.1 Stage 1 research memo. Run `311221-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.25 · L 0.53 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Diverse physical ingredient uses preserve operator-required demand beyond declining corn sweeteners.
**Weakness:** Existing automation and formula-driven competitive pricing limit both incremental labor opportunity and retained benefit.

## Business-model lens
- Included: Independent merchant wet corn milling and starch plants selling recurring volumes of starches, glucose, dextrose, fructose, corn oil, feed co-products, and related functional ingredients to external food, beverage, paper, packaging, pharmaceutical, personal-care, and industrial customers.
- Excluded: Captive internal plants, dry corn milling, wet milling whose primary purpose is nonpotable ethyl alcohol, purchased-oil refining, shell entities, and non-control financing vehicles.
- Customer and revenue model: Recurring B2B ingredient shipments under spot, annual, and multi-year contracts; pricing may be fixed or fee-based with raw-material adjustments, and differentiation ranges from commodity sweeteners and native starches to higher-function specialty ingredients.
- Deviation from default lens: none

## Executive view
Wet corn milling is an operator-required physical process with diversified recurring ingredient demand, but it is already centrally controlled and much output competes on price under short or input-adjusted contracts. AI is more likely to improve planning, reliability, quality workflows, and administration than replace core processing labor.

## How AI changes the work
Useful applications include batch and certificate documentation, control-room decision support, predictive-maintenance triage, inspection, laboratory review, production planning, commodity procurement support, and customer-specification work. Existing process-control systems and the physical, safety-critical nature of the mill constrain incremental substitution.

## Value capture
Specialty functionality, reliability, and technical service can preserve part of a productivity gain. Commodity substitutes, annual or shorter contracts, raw-material pass-through, and sophisticated buyers should force substantial sharing of broad cost savings.

## Firm availability
Separable independent merchant plants can qualify, but many wet mills are large, integrated, strategically owned, or dependent on shared infrastructure. The frozen estimate of 17 LMM firms needs a plant-by-plant ownership and profitability check before it can be treated as a target universe.

## Demand durability
Long-run corn-sweetener availability has fallen sharply, yet starch, oil, feed, packaging, pharmaceutical, personal-care, industrial, and biomaterial uses diversify the basket. The central five-year view is roughly flat real demand with meaningful downside and upside around mix.

## Risks and uncertainty
Major risks include overestimated target count, commodity pricing, corn and energy volatility, customer reformulation away from sweeteners, process and food-safety failures, environmental liabilities, cyber risk in connected controls, large-competitor scale, and already-automated operations. Contract diligence and plant-level labor mapping are decisive.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1 | — | OBSERVED | — |
| n | — | 17 | — | ESTIMATE | — |
| a | 0.12 | 0.22 | 0.34 | PROXY | S2, S3, S4 |
| rho | 0.4 | 0.6 | 0.75 | ESTIMATE | S3, S4 |
| e | 0.45 | 0.65 | 0.8 | ESTIMATE | S1, S7 |
| s5 | 0.1 | 0.18 | 0.27 | PROXY | S5 |
| q | 0.25 | 0.45 | 0.65 | PROXY | S7 |
| d5 | 0.9 | 0.98 | 1.08 | PROXY | S2, S6, S7 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S1, S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.19 | 0.53 | 1.02 | ESTIMATE |
| F | 0.91 | 1.76 | 2.48 | ESTIMATE |
| C | 5.00 | 9.00 | 10.00 | PROXY |
| D | 8.64 | 9.70 | 10.00 | ESTIMATE |

## Caveats
- a: No public wage-weighted 311221 task inventory was located.
- a: Trade-association descriptions may reflect larger and more automated member plants than LMM firms.
- rho: The range is implementation judgment rather than an observed adoption rate.
- rho: Brownfield control systems and cybersecurity posture may vary materially across facilities.
- e: The frozen estimate of 17 LMM-band firms is margin-bridged rather than observed and may be strained in a capital-intensive concentrated industry.
- e: A large public producer's structure may not represent hypothetical LMM operators.
- s5: The source covers all employer businesses, not this industry or EBITDA band.
- s5: Planned transfers are not completed deals and can include non-sale gifts.
- q: Ingredion is much larger and more diversified than the lens firms.
- q: The filing does not isolate the retained share of AI-enabled benefits.
- d5: Per-capita food availability is not producer shipment volume and covers only corn sweeteners.
- d5: Public-company product breadth may exceed that of LMM plants.
- o: This is structural judgment, not a measured retention rate.
- o: Demand volume changes are captured in d5 rather than counted again here.

## Sources
- **S1** — [U.S. Census Bureau NAICS definition: 311221 Wet Corn Milling](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines 311221 as wet milling corn and other vegetables, except to make ethyl alcohol, producing corn sweeteners, corn oil, and starches other than laundry starch.
- **S2** — [Corn Refiners Association: Frequently Asked Questions](https://corn.org/about-cra/faq/) (accessed 2026-07-22): The wet-milling process separates corn into starch, germ, fiber, and protein; corn-derived products serve food, beverage, adhesives, textiles, building materials, personal care, pharmaceuticals, paper, animal feed, and industrial uses.
- **S3** — [Corn Refiners Association Industry Overview 2018](https://corn.org/wp-content/uploads/2021/02/CRA-Industry-Overview-2018.pdf) (accessed 2026-07-22): Describes a multi-stage physical refining process and states that modern corn wet millers use central process-control computer systems and stainless-steel membranes.
- **S4** — [BLS Occupational Outlook Handbook: Food Processing Equipment Workers](https://www.bls.gov/ooh/production/food-and-tobacco-processing-workers.htm) (accessed 2026-07-22): Food-processing workers set controls, monitor and adjust processes, record batch data, clean equipment, and check quality; BLS notes automatic weighing and mixing can require fewer workers.
- **S5** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): In a fall-2024 survey, 22% of U.S. employer-business owners reported plans to sell or transfer ownership within five years, while 52.3% of employer businesses were owned by people age 55 or older.
- **S6** — [USDA ERS: Corn sweeteners availability declined over the last two decades](https://www.ers.usda.gov/data-products/chart-gallery/58332) (accessed 2026-07-22): U.S. total corn-sweetener availability fell from 85.7 pounds per person in 1999 to 53.0 pounds in 2023.
- **S7** — [Ingredion Incorporated 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1046257/000162828026008603/ingr-20251231.htm) (accessed 2026-07-22): U.S./Canada starch and sweetener competition is based on functionality, price, and quality; contracts are usually one year or less, one-third of sales are multi-year fee-based, and 2025 sales included pass-through of lower corn costs.
