# 311224 — Soybean and Other Oilseed Processing

*v5.1 Stage 1 research memo. Run `311224-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.72 · L 0.07 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Rising meal and biomass-based-diesel feedstock demand supports growing physical throughput.
**Weakness:** Very low labor intensity and commodity margin transmission sharply limit the economic effect and retention of AI labor gains.

## Business-model lens
- Included: Independent merchant processors that crush soybeans, cottonseed, canola, sunflower seed, peanuts, flaxseed, or other oilseeds and tree nuts into oils, meal, hulls, cakes, protein concentrates, and related co-products for repeat sale to external feed, food, biofuel, and industrial customers.
- Excluded: Captive internal plants, stand-alone refining or blending of purchased oils, wet corn milling, farming, commodity trading without processing assets, shell entities, and non-control financing vehicles.
- Customer and revenue model: Recurring B2B sales of commodity or specification-based meal, oil, hulls, protein, and co-products, with economics driven by throughput, local origination and logistics, crush spreads, quality, and product mix.
- Deviation from default lens: none

## Executive view
Oilseed processing has strong near-term quantity demand and remains an operator-required physical business, but labor is only a small portion of receipts and commodity competition limits benefit retention. The investable universe may also be materially smaller than the frozen count suggests because U.S. soybean crush is highly concentrated.

## How AI changes the work
AI can improve monitoring, maintenance triage, production and freight planning, commodity analytics, documentation, quality review, and customer service. Crushing and extraction remain physical, continuous, safety-critical processes, so the likely outcome is better utilization and avoided hiring rather than extensive direct substitution.

## Value capture
Localized yield, reliability, energy, logistics, and specialty-product advantages can persist. Generic labor or process savings are vulnerable to competitive soybean bids, product pricing, crush-spread normalization, and large incumbents with lower costs.

## Firm availability
Independent regional processors can be transferable, but the sector is mature, vertically integrated, and dominated by four firms. Cooperative, joint-venture, shared-infrastructure, and environmental constraints further narrow eligibility; the estimated 28 LMM firms requires direct verification.

## Demand durability
Record domestic soybean crush, expanding facilities, meal demand, and biofuel use support growth. The key uncertainty is whether policy-backed oil demand and feed/export demand absorb new capacity without substitution by other oils or imported products.

## Risks and uncertainty
Key risks are an overstated target count, compressed crush margins, commodity and energy volatility, biofuel-policy reversal, excess capacity, crop and trade disruption, major-processor scale, explosions or outages, solvent and environmental liability, feed and food compliance, and low incremental labor leverage.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0132 | — | OBSERVED | — |
| n | — | 28 | — | ESTIMATE | — |
| a | 0.1 | 0.2 | 0.3 | PROXY | S2, S4 |
| rho | 0.45 | 0.65 | 0.8 | ESTIMATE | S2, S4, S7 |
| e | 0.3 | 0.5 | 0.7 | ESTIMATE | S1, S7 |
| s5 | 0.08 | 0.15 | 0.24 | PROXY | S5, S7 |
| q | 0.2 | 0.35 | 0.55 | PROXY | S6, S7 |
| d5 | 1.05 | 1.15 | 1.28 | PROXY | S3, S6, S7 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S1, S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.02 | 0.07 | 0.13 | ESTIMATE |
| F | 0.83 | 1.82 | 2.80 | ESTIMATE |
| C | 4.00 | 7.00 | 10.00 | PROXY |
| D | 10.00 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No public wage-weighted task inventory specific to oilseed processing was found.
- a: Food-processing occupation data are broader than oilseed crushing and may miss commodity-origination and laboratory roles.
- rho: This is bounded implementation judgment, not an observed adoption rate.
- rho: Mechanical-press specialty plants may have different economics and automation maturity from large solvent-extraction facilities.
- e: The frozen estimate of 28 LMM firms is margin-bridged, not observed.
- e: A public processor reports that four companies control nearly 85% of U.S. soybean processing, which may mean the size-class bridge materially overstates independent targets.
- s5: Gallup covers all employer businesses, not 311224 or the LMM EBITDA band.
- s5: Planned sales and gifts are not completed qualifying control transfers.
- q: Public-company segments include origination, trading, refining, and other activities beyond the frozen lens.
- q: No source directly measures the retained share of an AI-enabled benefit.
- d5: The evidence is soybean-heavy while NAICS 311224 includes other oilseeds and tree nuts.
- d5: Biofuel-driven demand is policy-sensitive and added capacity can pressure margins even as quantity grows.
- o: This is a structural estimate, not an observed five-year operator-retention share.
- o: Demand volume is handled in d5 rather than counted again here.

## Sources
- **S1** — [U.S. Census Bureau 2022 NAICS definition: 311224 Soybean and Other Oilseed Processing](https://www.census.gov/naics/?details=311224&input=311224&year=2022) (accessed 2026-07-22): Defines the industry as crushing oilseeds and tree nuts into oilseed oils, cakes, meals, and protein isolates and concentrates.
- **S2** — [BLS Occupational Outlook Handbook: Food Processing Equipment Workers](https://www.bls.gov/ooh/production/food-and-tobacco-processing-workers.htm) (accessed 2026-07-22): Food-processing workers set controls, monitor processes and gauges, record batch data, clean equipment, and check quality; automatic weighing and mixing can reduce worker requirements.
- **S3** — [USDA ERS: More soybeans being processed in United States to meet rising demand for soybean meal and oil](https://www.ers.usda.gov/data-products/charts-of-note/112861) (accessed 2026-07-22): Forecasts 2025/26 U.S. soybean crush rising nearly 3% to a record 2.49 billion bushels and reaching 57% of soybean production, driven by meal and biomass-diesel oil demand.
- **S4** — [BLS: Food-processing duties, work environment, and automation](https://www.bls.gov/ooh/production/food-and-tobacco-processing-workers.htm) (accessed 2026-07-22): Documents the mix of control, monitoring, recording, sanitation, equipment tending, and quality duties used as the occupation proxy for implementation constraints.
- **S5** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): A fall-2024 survey found 22% of U.S. employer-business owners planned to sell or transfer ownership within five years and 52.3% of employer firms had owners age 55 or older.
- **S6** — [Archer-Daniels-Midland Company 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/7084/000000708426000011/adm-20251231.htm) (accessed 2026-07-22): Describes oilseed crushing outputs and customers, agricultural commodity price transmission, capacity operation, margin compression, operational risks, and extensive hedging of anticipated soybean crush.
- **S7** — [South Dakota Soybean Processors 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1163609/000116360926000010/sdsp-20251231.htm) (accessed 2026-07-22): Reports cyclical variable crush margins, meal/oil uses, industry structure of about 20 companies and 70 facilities, and nearly 85% control by four processors; also documents plant energy and regulatory requirements.
- **S8** — [U.S. EIA: Higher blending targets drive RIN prices close to record highs](https://www.eia.gov/todayinenergy/detail.php?id=67765) (accessed 2026-07-22): Forecasts 2026 renewable-diesel production up 24% and biodiesel production up 41% from 2025, with further increases in 2027.
