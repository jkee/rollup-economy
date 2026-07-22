# 311213 — Malt Manufacturing

*v5.1 Stage 1 research memo. Run `311213-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.79 · L 0.00 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring need for accountable physical conversion and quality assurance keeps most surviving malt demand operator-required.
**Weakness:** The frozen estimate of zero LMM-band firms combines with declining brewing demand to make target availability exceptionally weak.

## Business-model lens
- Included: Independent malt houses manufacturing barley, rye, or other-grain malt for repeat sale to external breweries, distillers, and food customers.
- Excluded: Captive malt operations inside breweries, brewing itself, malt extracts and syrups, shell entities, and businesses without transferable operating assets or external customers.
- Customer and revenue model: Recurring business-to-business sales of specification-grade malt, typically by shipment or supply agreement, with revenue tied to physical volume and negotiated product specifications.
- Deviation from default lens: none

## Executive view
Malt manufacturing is a physical, specification-driven business with repeat B2B demand, but the frozen dataset estimates no firms in the target EBITDA band and brewing demand is contracting. AI can improve information flows around a plant more readily than it can replace the plant's core work.

## How AI changes the work
The clearest opportunities are batch-record automation, certificate and specification handling, production scheduling, maintenance triage, anomaly detection, and assisted quality review. Core sanitation, material movement, equipment operation, sampling, and accountable food-safety decisions remain physical or tightly supervised, while much laboratory analysis is already automated.

## Value capture
Yield and consistency improvements can be retained where specialty products and customer-specific specifications matter. Commodity base-malt competition, contract renewal, raw-material indexation, and pressure on brewery margins create meaningful pass-through risk.

## Firm availability
Independent merchant maltsters can be transferable operating businesses, but the industry is tiny and may include captive or strategically owned plants. The frozen LMM count of zero is the central availability constraint; the broad employer-business succession survey cannot establish that a malt target will trade.

## Demand durability
Physical malt production remains operator-required, but quantity demand faces a persistent beer-volume headwind. Distilling, specialty malt, food uses, exports, and merchant-share gains can soften rather than erase that pressure.

## Risks and uncertainty
Key risks are no actionable target in band, customer concentration, falling beer output, barley quality and crop variability, energy-intensive kilning, food-safety failures, environmental liabilities, incumbent process automation, and limited public evidence on contracts or labor mix. A plant-by-plant market map could materially change the conclusion.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1023 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.18 | 0.28 | 0.4 | PROXY | S1, S2, S3 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S2, S3 |
| e | 0.55 | 0.75 | 0.9 | ESTIMATE | S4 |
| s5 | 0.12 | 0.2 | 0.28 | PROXY | S5 |
| q | 0.35 | 0.55 | 0.75 | ESTIMATE | S6 |
| d5 | 0.8 | 0.88 | 0.98 | PROXY | S6, S7 |
| o | 0.92 | 0.97 | 1 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.26 | 0.63 | 1.18 | ESTIMATE |
| F | 0.00 | 0.00 | 0.00 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.36 | 8.54 | 9.80 | ESTIMATE |

## Caveats
- a: No public wage-weighted task inventory specific to malt manufacturing was found.
- a: The Thermo Fisher paper is vendor-affiliated and describes laboratory automation, not the whole plant.
- rho: This is implementation judgment, not a measured adoption rate.
- rho: Large modern plants and small craft maltsters may have very different control-system maturity.
- e: The frozen dataset estimates zero firms in the $1-10M EBITDA band, so this conditional eligibility share does not imply an available target count.
- e: Public establishment counts do not reveal firm ownership, profitability, or captive status.
- s5: Gallup covers all U.S. employer businesses, not malt manufacturing or the LMM EBITDA band.
- s5: Intentions may not become completed transfers and include gifts or rare public offerings.
- q: No public contract sample or post-productivity pricing study specific to U.S. maltsters was located.
- q: Craft-brewery conditions are only part of the customer base and may overstate pricing pressure for distilling or food customers.
- d5: Barley FAI includes uses other than malt and is not identical to merchant malt shipments.
- d5: Craft beer is a subset of beer demand and uses malt at a different intensity from large-scale brewing.
- o: This is a structural judgment rather than a measured five-year retention share.
- o: The construct separates operator requirement from declining end-market volume, which is captured in d5.

## Sources
- **S1** — [O*NET OnLine: Food Batchmakers (51-3092.00)](https://www.onetonline.org/link/details/51-3092.00) (accessed 2026-07-22): Food-batchmaker tasks include recording production and test data, cleaning vats, operating processing equipment, following recipes, monitoring conditions, and evaluating product quality.
- **S2** — [BLS Occupational Outlook Handbook: Food Processing Equipment Workers](https://www.bls.gov/ooh/production/food-and-tobacco-processing-workers.htm) (accessed 2026-07-22): Food-processing workers set controls, monitor mixes and gauges, record batch data, clean equipment, and check quality; BLS also notes automated weighing and mixing can require fewer workers.
- **S3** — [Automated Malt Analysis using Discrete Analyzers](https://assets.thermofisher.com/TFS-Assets/CMD/Reference-Materials/execsum-061016-automated-malt-analysis-execsum-061016-v1-en.pdf) (accessed 2026-07-22): Commercial malt houses use analysis for process and product quality control and trade specifications; the paper says automation is used in most malt testing facilities and describes already automated routine assays.
- **S4** — [U.S. Census Bureau profile: 311213 Malt manufacturing](https://data.census.gov/profile/311213_-_Malt_manufacturing?codeset=naics~311213) (accessed 2026-07-22): Defines the industry as establishments manufacturing malt from barley, rye, or other grains; the fetched profile reports 42 employer establishments for 2023.
- **S5** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall-2024 survey of 1,264 U.S. working business owners: 22% of employer-business owners planned to sell or transfer ownership within five years; 52.3% of employer businesses were owned by people age 55 or older.
- **S6** — [Brewers Association Reports 2024 U.S. Craft Brewing Industry Figures](https://www.brewersassociation.org/association-news/brewers-association-reports-2024-u-s-craft-brewing-industry-figures/) (accessed 2026-07-22): Craft beer volume fell 3.9% in 2024, overall U.S. beer volume fell 1.2%, and small brewers faced rising ingredient costs and competition in a saturated market.
- **S7** — [USDA ERS: Barley use declining as U.S. beer production trends lower](https://www.ers.usda.gov/data-products/charts-of-note/112968) (accessed 2026-07-22): Beer production fell more than 13% from 2016/17 to 2023/24; 2024/25 barley food, alcohol, and industrial use was forecast at 110.7 million bushels, 27% below 2016/17.
