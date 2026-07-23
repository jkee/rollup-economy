# 111219 — Other Vegetable (except Potato) and Melon Farming

*v5.1 Stage 1 research memo. Run `111219-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Labor scarcity and high specialty-crop labor costs create strong incentives for AI-enabled field and postharvest automation.
**Weakness:** Missing firm data, low price power, and crop-specific biological complexity make value capture and scalable implementation uncertain.

## Business-model lens
- Included: Independent U.S. farms primarily growing open-field vegetables other than potatoes and melons for repeat sale to packers, processors, wholesalers, retailers, foodservice buyers, or direct-market customers.
- Excluded: Potato farms; greenhouse-only production; home-consumption plots; captive growing operations; pure packers, distributors, and brokers; hobby farms; non-control financing vehicles; and operations outside the lower-middle-market earnings band.
- Customer and revenue model: Repeat seasonal and program sales of harvested vegetables or melons to external commercial customers, including contracted processing acreage and recurring fresh-market relationships, screened for transferable operations plausibly generating $1-10 million normalized EBITDA.
- Deviation from default lens: none

## Executive view
Vegetable and melon farming has recurring food demand and unusually high labor intensity, but biological variability makes AI implementation capital-heavy and crop-specific. Missing labor-share and firm-count inputs materially limit screen confidence.

## How AI changes the work
AI can improve crop scouting, yield and harvest forecasting, irrigation, targeted spraying, labor scheduling, traceability, grading, packing inspection, and selected robotic harvest tasks. Delicate crops, uneven maturity, weather, terrain, and narrow harvest windows preserve manual field work.

## Value capture
Perishability, commodity pricing, processors, retailers, and imports pressure growers to pass productivity into lower prices. Retention improves with proprietary varieties, differentiated quality, direct channels, local freshness, brand, and constrained supply windows.

## Firm availability
The eligible universe is unresolved because the frozen firm count is missing. Many farms are family, land, or seasonal businesses rather than transferable operating platforms in the target EBITDA band.

## Demand durability
Vegetables are staple foods, yet per-capita availability has softened and imports supply a substantial share. Population growth and specialty/local demand support volume while water, climate, trade, and crop-switching risks remain material.

## Risks and uncertainty
Key risks include missing dataset inputs, weather and water, labor availability, food safety, crop disease, perishability, buyer concentration, imports, seasonal working capital, and automation technology that fails outside controlled trials.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.27 | 0.4 | PROXY | S1, S2, S3 |
| rho | 0.27 | 0.43 | 0.61 | ESTIMATE | S2, S3 |
| e | 0.2 | 0.4 | 0.6 | ESTIMATE | — |
| s5 | 0.08 | 0.18 | 0.31 | ESTIMATE | — |
| q | 0.18 | 0.34 | 0.53 | ESTIMATE | S4 |
| d5 | 0.87 | 0.97 | 1.08 | PROXY | S4, S5 |
| o | 0.9 | 0.97 | 1 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 3.60 | 6.80 | 10.00 | ESTIMATE |
| D | 7.83 | 9.41 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS excludes many self-employed farm operators and does not publish a direct 111219 occupation mix.
- a: The range blends software AI with AI-enabled machinery and excludes already mechanized work.
- rho: Adoption varies sharply across commodities, regions, acreage, and processing versus fresh markets.
- e: The frozen firm-count input is missing, so the size and composition of the eligible universe cannot be reconciled.
- s5: No observed five-year transfer rate specific to eligible 111219 farms was found.
- q: Capture differs materially by crop, region, brand, and direct-versus-wholesale channel.
- d5: The available demand series is broader than this six-digit industry.
- d5: Weather creates annual volatility distinct from underlying constant-quality demand.
- o: Automation within a farm changes labor needs but not operator requirement; quantity effects remain in d5.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Support Activities for Crop Production](https://www.bls.gov/oes/2023/may/naics4_115100.htm) (accessed 2026-07-22): Adjacent crop-support employment totals 337,310 and agricultural workers account for 216,230 jobs, or 64.10%, grounding the physical-task proxy.
- **S2** — [Automation for Specialty Crops](https://www.nifa.usda.gov/about-nifa/impacts/automation-specialty-crops) (accessed 2026-07-22): USDA describes manual-labor dependence and recent automated sensing, inspection, and harvesting systems; one cited apple robot detected fruit at 100% and picked about 70% successfully.
- **S3** — [USDA Agencies Funded $287.7 Million for Specialty Crop Automation or Mechanization Projects](https://www.ers.usda.gov/amber-waves/2020/april/usda-agencies-funded-287-7-million-for-specialty-crop-automation-or-mechanization-projects) (accessed 2026-07-22): USDA reports $287.7 million funded 213 automation or mechanization projects in 2008-2018 and explains why hand harvest and produce handling remain difficult to automate.
- **S4** — [Vegetables and Pulses: Market Outlook](https://www.ers.usda.gov/topics/crops/vegetables-and-pulses/market-outlook) (accessed 2026-07-22): USDA estimates imports supplied about one-third of U.S. vegetable availability in 2025; Mexico supplied 77% and Canada 13% of fresh vegetable imports excluding potatoes.
- **S5** — [Vegetables and Pulses](https://ers.usda.gov/topics/crops/vegetables-and-pulses) (accessed 2026-07-22): USDA reports vegetable and pulse availability averaged 414 pounds per person in 2017-2022, about 4% below the 431-pound average a decade earlier.
