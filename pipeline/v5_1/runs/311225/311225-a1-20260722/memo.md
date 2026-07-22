# 311225 — Fats and Oils Refining and Blending

*v5.1 Stage 1 research memo. Run `311225-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.16 · L 0.22 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical food demand plus growing biomass-based-diesel feedstock use supports refining throughput.
**Weakness:** Commodity input transparency and substitutable bulk oils constrain commercial retention of broadly available productivity gains.

## Business-model lens
- Included: Independent merchant firms refining or blending purchased vegetable, oilseed, tree-nut, and eligible mixed animal-vegetable fats; manufacturing shortening, margarine, nondairy butter, cooking oils, sprays, and specification blends for repeat external food, foodservice, retail, biofuel, and industrial customers.
- Excluded: Captive internal units, refining within oilseed-crushing or wet-corn-milling establishments, animal rendering and stand-alone animal-fat refining, shell entities, and non-control financing vehicles.
- Customer and revenue model: Recurring B2B and private-label sales by bulk shipment or packaged product, with revenue tied to input-oil prices, refining and blending fees, formulation, quality specifications, service reliability, and in some cases branded or specialty-product premiums.
- Deviation from default lens: none

## Executive view
Fats and oils refining remains an operator-required physical activity with recurring food and industrial demand and a biofuel tailwind. AI can improve monitoring, quality, maintenance, planning, and administration, but labor is a modest share of receipts and commodity-like pricing limits retained savings.

## How AI changes the work
The best use cases are quality-data review, batch and traceability records, anomaly detection, predictive-maintenance triage, formulation support, scheduling, procurement, and customer-specification management. Core unit operations and food-safety accountability remain physical, while modern equipment already automates important controls and tests.

## Value capture
Specialty blends, certifications, packaging, private label, short runs, technical service, yield, and reliable delivery can protect value. Bulk oils face transparent inputs, feedstock substitution, sophisticated customers, and price competition that should pass through much of a generic cost reduction.

## Firm availability
Independent LMM refiners can be separable, recurring-revenue businesses, but the NAICS category also contains captive, integrated, branded, and operationally heterogeneous plants. The frozen 28-firm estimate needs direct ownership, EBITDA, certification, and merchant-status verification.

## Demand durability
Food applications provide a resilient base and biomass-based diesel creates current growth. Five-year durability depends heavily on biofuel policy, competing feedstocks, customer integration, imports, and whether new oilseed capacity sends refining volume to independent rather than integrated plants.

## Risks and uncertainty
Key risks are an overstated target count, raw-oil and energy volatility, commodity pass-through, biofuel-policy reversal, substitution among oils, food-safety or allergen failures, oxidation and off-spec output, recalls, environmental liabilities, cyber risk, customer concentration, and incumbent automation.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0378 | — | OBSERVED | — |
| n | — | 28 | — | ESTIMATE | — |
| a | 0.14 | 0.24 | 0.36 | PROXY | S2, S3, S4 |
| rho | 0.4 | 0.6 | 0.78 | ESTIMATE | S2, S3, S4 |
| e | 0.45 | 0.65 | 0.8 | ESTIMATE | S1, S8 |
| s5 | 0.11 | 0.19 | 0.28 | PROXY | S5 |
| q | 0.22 | 0.4 | 0.6 | PROXY | S8 |
| d5 | 1 | 1.1 | 1.23 | PROXY | S6, S7, S8 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.08 | 0.22 | 0.42 | ESTIMATE |
| F | 1.40 | 2.40 | 3.19 | ESTIMATE |
| C | 4.40 | 8.00 | 10.00 | PROXY |
| D | 9.50 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No public wage-weighted task inventory specific to NAICS 311225 was found.
- a: Equipment-vendor materials may describe newer systems than those installed at LMM plants.
- rho: This is bounded implementation judgment rather than a measured adoption rate.
- rho: Packaged specialty producers and bulk commodity refiners may have very different task mixes and integration budgets.
- e: The frozen estimate of 28 LMM firms is margin-bridged rather than observed.
- e: NAICS combines bulk refining, blending, shortenings, margarine, packaged oils, and specialty products with different transferability.
- s5: Gallup covers all employer businesses, not this NAICS or EBITDA band.
- s5: Plans include gifts and may never close; internal reorganizations would not qualify.
- q: The source is an integrated global processor, not a pure-play LMM purchased-oil refiner.
- q: No public study directly measures retention of AI-enabled gross benefits.
- d5: Soybean oil and biofuel evidence covers only part of the heterogeneous service basket.
- d5: Federal and state clean-fuel policy changes can sharply alter industrial oil demand.
- o: This is a structural estimate rather than a measured five-year operator-retention share.
- o: Quantity growth or decline is captured in d5 rather than counted again here.

## Sources
- **S1** — [U.S. Census Bureau 2022 NAICS definition: 311225 Fats and Oils Refining and Blending](https://www.census.gov/naics/?details=311225&input=311225&year=2022) (accessed 2026-07-22): Defines the industry as shortening and margarine manufacturing from purchased fats and oils, refining or blending purchased vegetable, oilseed, and tree-nut oils, and blending purchased animal and vegetable fats.
- **S2** — [BLS Occupational Outlook Handbook: Food Processing Equipment Workers](https://www.bls.gov/ooh/production/food-and-tobacco-processing-workers.htm) (accessed 2026-07-22): Food-processing work combines equipment control, process monitoring, production records, sanitation, material handling, and product-quality checks; BLS notes some automatic weighing and mixing reduces worker requirements.
- **S3** — [Oklahoma State University Extension: Edible Oil Quality](https://extension.okstate.edu/fact-sheets/edible-oil-quality) (accessed 2026-07-22): Explains oxidation and quality risks, standard oil-quality parameters, refining steps, and available automated instruments; reports a voluntary refined-oil FFA standard of at most 0.05%.
- **S4** — [Alfa Laval: Edible oil refining process systems](https://www.alfalaval.com/products/process-solutions/edible-oil-solutions/edible-oil-refining-process-systems/) (accessed 2026-07-22): Describes controlled degumming, neutralization, dewaxing, bleaching, and deodorization stages needed for purity, safety, taste, appearance, yield, and utility efficiency.
- **S5** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): A fall-2024 survey found 22% of U.S. employer-business owners planned to sell or transfer ownership within five years, while 52.3% of employer firms had owners age 55 or older.
- **S6** — [USDA ERS: More soybeans being processed in United States to meet rising demand for soybean meal and oil](https://www.ers.usda.gov/data-products/charts-of-note/112861) (accessed 2026-07-22): Forecasts 2025/26 U.S. soybean crush rising nearly 3% to a record 2.49 billion bushels, with higher soybean-oil use especially in biomass-based diesel.
- **S7** — [U.S. EIA: Higher blending targets drive RIN prices close to record highs](https://www.eia.gov/todayinenergy/detail.php?id=67765) (accessed 2026-07-22): Forecasts 2026 renewable-diesel production up 24% and biodiesel production up 41% from 2025, with further increases in 2027.
- **S8** — [Bunge Global SA 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1996862/000162828026009842/bg-20251231.htm) (accessed 2026-07-22): Describes refined oil customers and commodity-like oil markets with competition based on price, quality, product and service offerings, distribution, cost structure, innovation, technical support, and substitution.
