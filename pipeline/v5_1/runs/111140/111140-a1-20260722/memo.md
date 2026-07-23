# 111140 — Wheat Farming

*v5.1 Stage 1 research memo. Run `111140-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Existing precision-guidance adoption creates a practical base for further AI-assisted wheat operations.
**Weakness:** Most wheat farms sell commodities rather than outsourced services, and the target firm population cannot be measured.

## Business-model lens
- Included: US lower-middle-market wheat-growing or wheat-seed operations that repeatedly provide externally contracted, customer-dedicated production or managed growing services.
- Excluded: Ordinary farms selling owned wheat into commodity channels without an outsourced-service relationship, hobby and lifestyle farms, captive growing units, passive landowners, shells, financing vehicles, firms outside the EBITDA band, and custom planting or harvesting contractors classified elsewhere.
- Customer and revenue model: Potentially eligible firms earn repeat revenue through production contracts, managed growing, or customer-specific seed and grain arrangements; ordinary merchant grain sales at cash or futures-linked prices are not by themselves outsourced services.
- Deviation from default lens: none

## Executive view
Wheat farming has real precision-technology potential but fits the recurring outsourced-service lens poorly. Most farms sell owned grain, both labor and firm-count dataset inputs are missing, and eligible contract-growing operations cannot be enumerated.

## How AI changes the work
AI can improve scouting, disease recognition, weather and yield decisions, variable-rate inputs, machinery guidance, maintenance, records, marketing, and compliance. Field execution, repairs, land control, agronomy, harvest timing, and weather risk remain operator responsibilities.

## Value capture
Global commodity pricing may temporarily preserve cost savings, while production-contract renewals, land rents, suppliers, and buyer bargaining share gains. Weather and crop prices can overwhelm the AI contribution.

## Firm availability
The eligible LMM population is unknown. Producer aging suggests succession, but farm transitions often occur through family transfer, land sale, or lease rather than sale of a recurring-service operating company.

## Demand durability
Wheat remains a staple, but US acreage and production have trended down as other crops compete for land and export share declines. Yield gains partly offset acreage pressure.

## Risks and uncertainty
Missing dataset inputs, lens mismatch, owner labor outside OEWS, weather, commodity prices, crop insurance, land tenure, machinery cycles, broadband, and regional agronomy make the record highly uncertain.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.14 | 0.25 | 0.38 | PROXY | S2, S3, S4, S5 |
| rho | 0.37 | 0.56 | 0.72 | ESTIMATE | S3, S4, S5 |
| e | — | — | — | MISSING | — |
| s5 | 0.12 | 0.24 | 0.38 | PROXY | S7, S8 |
| q | 0.27 | 0.46 | 0.66 | ESTIMATE | S6, S8 |
| d5 | 0.88 | 0.98 | 1.1 | PROXY | S6, S9 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 5.40 | 9.20 | 10.00 | ESTIMATE |
| D | 8.36 | 9.70 | 10.00 | ESTIMATE |

## Caveats
- a: No compensation-to-receipts input is available, so this primitive cannot support a complete labor-opportunity calculation.
- a: OEWS poorly captures self-employed producers and unpaid family labor.
- a: Technology adoption and task mix differ greatly by acreage and region.
- rho: Precision guidance adoption is not equivalent to AI substitution.
- rho: The smallest farms have materially lower technology adoption.
- e: The assignment declares no defensible LMM firm count and prohibits replacing it.
- e: USDA farm measures are not directly comparable with consolidated-firm EBITDA.
- e: Most wheat revenue is commodity sale rather than service revenue.
- s5: Producer counts are not firm counts and farms can have multiple producers.
- s5: The data cover all farms, not wheat farms or the LMM band.
- s5: The eligible population is unknown.
- q: No source directly measures AI-benefit retention.
- q: Commodity price, weather, yield, insurance, and government payments can dominate farm margins.
- d5: The BLS series covers all crops.
- d5: Wheat output is highly weather-dependent.
- d5: Production quantity is not the same as service demand for the narrow eligible lens.
- o: The accountable operator could consolidate into a larger farm manager or equipment-enabled platform.
- o: Automation may reduce onsite staffing without eliminating the operator.

## Sources
- **S1** — [NAICS definition: Wheat Farming](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-23): Defines 111140 as establishments growing wheat and/or producing wheat seeds.
- **S2** — [Agricultural Workers](https://www.bls.gov/ooh/farming-fishing-and-forestry/agricultural-workers.htm) (accessed 2026-07-23): Describes agricultural work and reports that crop production employs a majority of crop, nursery, and greenhouse farmworkers.
- **S3** — [Precision Agriculture in the Digital Era](https://ers.usda.gov/publications/105893) (accessed 2026-07-23): Reports automated guidance on well over half of winter-wheat acreage, while several mapping and variable-rate technologies covered only 5% to 25% of winter-wheat acreage.
- **S4** — [AI-Powered Wheat FHB and FDK Assessment Tool Development](https://www.ars.usda.gov/research/project/?accnNo=449940) (accessed 2026-07-23): Describes a USDA project to deploy AI smartphone-image tools for wheat disease and damaged-kernel assessment.
- **S5** — [Most Row Crop Acreage Managed Using Auto-steer and Guidance Systems](https://ers.usda.gov/amber-waves/2023/april/most-row-crop-acreage-managed-using-auto-steer-and-guidance-systems) (accessed 2026-07-23): Documents much lower guidance-system adoption among the smallest winter-wheat farms and identifies connectivity as a requirement.
- **S6** — [Wheat Sector at a Glance](https://www.ers.usda.gov/topics/crops/wheat/wheat-sector-at-a-glance) (accessed 2026-07-23): Reports long-term declines in US wheat plantings and production, partly offset by yields, and a declining US share of world wheat exports.
- **S7** — [2022 Census of Agriculture: Farm Producers](https://www.nass.usda.gov/Publications/Highlights/2024/Census22_HL_FarmProducers_FINAL.pdf) (accessed 2026-07-23): Reports 38% of US producers age 65 or older and an average producer age of 58.1 in 2022.
- **S8** — [Farmland Ownership and Tenure](https://ers.usda.gov/topics/farm-economy/land-use-land-value-tenure/farmland-ownership-and-tenure) (accessed 2026-07-23): Describes farm ownership, rental, and succession dynamics and notes that grain-production areas commonly have more than half of farmland rented.
- **S9** — [Employment and output by industry, 2024–34](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-23): Projects crop-production real output from $175.8 billion in 2024 to $201.8 billion in 2034, a 1.4% annual compound rate.
