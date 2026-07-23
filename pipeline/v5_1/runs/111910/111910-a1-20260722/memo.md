# 111910 — Tobacco Farming

*v5.1 Stage 1 research memo. Run `111910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Highly specified repeat buyer contracts create some service-like production relationships.
**Weakness:** Secular cigarette decline and the dominance of marketing contracts weaken durable outsourced-service eligibility.

## Business-model lens
- Included: US lower-middle-market tobacco-growing operations that repeatedly provide customer-directed production services under contracts where the buyer meaningfully controls specifications, inputs, practices, or crop ownership.
- Excluded: Farms using ordinary cash sales or marketing contracts that only set price, quantity, quality, and delivery while the grower retains crop ownership; hobby farms; captive units; passive landowners; shells; financing vehicles; firms outside the EBITDA band; and tobacco processing or manufacturing.
- Customer and revenue model: Eligible firms are paid repeat growing or production fees by tobacco companies or other external contractors with meaningful production involvement; common marketing-contract sales of grower-owned leaf are not treated as outsourced services merely because they are contracted before harvest.
- Deviation from default lens: none

## Executive view
Tobacco farming has extensive buyer contracting but only a narrower subset resembles outsourced production service; most contracts are marketing arrangements for grower-owned leaf. Missing labor and LMM firm-count inputs and declining cigarette use limit the case.

## How AI changes the work
AI can improve scouting, visual grading, curing controls, records, contract compliance, scheduling, and equipment diagnostics. Field labor, harvest, leaf handling, curing operations, and quality accountability remain physical.

## Value capture
True production-fee contracts may preserve initial savings, but concentrated buyers, quality specifications, formula pricing, and renewals pass gains through. Yield, grade, and buyer renewal risk dominate farm economics.

## Firm availability
Eligibility cannot be measured without contract-level and EBITDA data. Producer aging suggests succession, but farms often transition through family, land, or lease transactions rather than sale of a recurring-service firm.

## Demand durability
US cigarette use is at a multidecade low, creating a secular headwind despite recent production volatility and possible export support. The remaining crop still needs growers, curing, and quality control.

## Risks and uncertainty
Missing dataset inputs, contract-type ambiguity, buyer concentration, public-health regulation, declining cigarette use, labor, weather, crop disease, leaf grade, and export volatility create substantial uncertainty.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.12 | 0.23 | 0.36 | PROXY | S2, S3 |
| rho | 0.28 | 0.47 | 0.64 | ESTIMATE | S2, S3 |
| e | — | — | — | MISSING | — |
| s5 | 0.13 | 0.25 | 0.4 | PROXY | S7 |
| q | 0.22 | 0.42 | 0.62 | ESTIMATE | S4, S5 |
| d5 | 0.62 | 0.8 | 1.02 | PROXY | S6, S8, S9 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 4.40 | 8.40 | 10.00 | ESTIMATE |
| D | 5.83 | 7.84 | 10.00 | ESTIMATE |

## Caveats
- a: No labor-share input is available, so the labor opportunity cannot be completed.
- a: OEWS omits much self-employed and family labor.
- a: Tobacco types and harvesting systems have different labor intensity.
- rho: The sources do not measure AI implementation in tobacco farming.
- rho: Mechanization and workflow differ between flue-cured, burley, fire-cured, and dark air-cured tobacco.
- e: The assignment declares no defensible LMM firm count and prohibits replacing it.
- e: Contracted commodity sales are not automatically outsourced services.
- e: Farm entities, land ownership, and operating businesses may not align.
- s5: The data cover all farm producers and allow multiple producers per farm.
- s5: The eligible population is unknown.
- s5: Loss or nonrenewal of a buyer contract can make a farm operation nontransferable.
- q: No source directly measures AI-benefit retention.
- q: The dominant marketing-contract model differs from the narrower eligible production-service model.
- q: Yield, grade, weather, and buyer renewal can dominate margins.
- d5: Smoking prevalence is an end-use proxy rather than farm-service demand.
- d5: One-year production growth is not a durable forecast.
- d5: Export demand and inventory movements can decouple US production from US consumption.
- o: The operator may consolidate into a larger grower or buyer-controlled unit.
- o: Demand destruction is captured in d5 rather than operator need.

## Sources
- **S1** — [NAICS definition: Tobacco Farming](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-23): Defines 111910 as establishments primarily engaged in growing tobacco.
- **S2** — [May 2023 OEWS: Support Activities for Crop Production](https://www.bls.gov/oes/2023/May/naics4_115100.htm) (accessed 2026-07-23): Reports a workforce dominated by farming occupations and crop laborers, providing a physical-work proxy for crop operations.
- **S3** — [Precision Agriculture in the Digital Era](https://ers.usda.gov/publications/105893) (accessed 2026-07-23): Describes digitalization and automation in US farming and the operational, cost, labor, and connectivity factors affecting adoption.
- **S4** — [Farm Structure and Contracting](https://www-tx.ers.usda.gov/topics/farm-economy/farm-structure-and-organization/farm-structure-and-contracting) (accessed 2026-07-23): Defines marketing and production contracts and reports that over 40% of tobacco production value was under marketing contracts in 2024.
- **S5** — [One-third of U.S. farm output is produced under contract, but the share differs by commodity](https://ers.usda.gov/data-products/charts-of-note/91032) (accessed 2026-07-23): Reports tobacco's contracted production share rose to 90% in 2017 as cigarette manufacturers shifted from auctions to contracts.
- **S6** — [Tobacco Product Use Among Adults — United States, 2017–2023](https://www.cdc.gov/mmwr/volumes/74/wr/mm7407a3.htm) (accessed 2026-07-23): Reports adult cigarette smoking at its lowest level in 60 years and a decline in exclusive cigarette users during 2017–2023.
- **S7** — [2022 Census of Agriculture: Farm Producers](https://www.nass.usda.gov/Publications/Highlights/2024/Census22_HL_FarmProducers_FINAL.pdf) (accessed 2026-07-23): Reports 38% of US producers age 65 or older and an average age of 58.1 in 2022.
- **S8** — [Crop Production 2025 Annual Summary](https://www.nass.usda.gov/Publications/Todays_Reports/reports/cropan26.pdf) (accessed 2026-07-23): Reports 2025 US tobacco production of 359 million pounds, up 11% from 2024, with 171,300 harvested acres.
- **S9** — [Cigarette and Electronic Cigarette Use Among Adults by Urbanization Level: United States, 2024](https://www.cdc.gov/nchs/data/hestat/hestat115.htm) (accessed 2026-07-23): Reports 9.9% of US adults used cigarettes in 2024 and documents current cigarette-use patterns.
