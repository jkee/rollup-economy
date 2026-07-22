# 325314 — Fertilizer (Mixing Only) Manufacturing

*v5.1 Stage 1 research memo. Run `325314-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.13 · L 0.74 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring local custom formulations create a coherent service model and an AI-addressable order-to-batch workflow.
**Weakness:** Transparent nutrient pricing and low labor intensity limit retained benefit even when workflow automation succeeds.

## Business-model lens
- Included: US lower-middle-market fertilizer blenders that repeatedly formulate and mix purchased nutrient ingredients to external customer, retailer, agronomist, or private-label specifications.
- Excluded: Upstream nitrogenous or phosphatic material manufacturers, compost producers, pure distributors that do no mixing, captive farm or integrated internal blending units, one-off spot traders, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring seasonal or programmatic blend orders priced per ton, batch, or formulation, combining purchased straight fertilizers and micronutrients with ingredient, freight, handling, storage, and blending economics.
- Deviation from default lens: none

## Executive view
Mixing-only fertilizer manufacturing fits the outsourced-service lens better than upstream fertilizer production because the core activity is repeatedly combining purchased nutrients to customer specifications. AI can materially improve the order-to-batch workflow, while recurring local demand and operational execution preserve an accountable operator; low labor intensity and transparent input pricing still cap the upside.

## How AI changes the work
Strong applications include order capture, recipe validation, inventory allocation, purchasing, seasonal scheduling, dispatch, batch records, quality exceptions, maintenance knowledge, and customer communications. Loading, weighing verification, equipment tending, housekeeping, sampling, repairs, and physical safety remain on-site tasks.

## Value capture
Agronomic trust, accurate formulations, inventory availability, local storage, fast loadout, and delivery performance support partial retention. Transparent commodity nutrients and frequent per-ton quotes make pass-through and price competition unavoidable.

## Firm availability
Many independent custom blenders plausibly meet the recurring-service lens, though resale-heavy retailers and captive sites do not. Broad owner aging supports succession-driven supply, but clean transfers depend on customer relationships, environmental records, working capital, and separation from adjacent retail or application operations.

## Demand durability
Fertilizer is a recurring crop input and field-specific nutrient needs support blending, while USDA data show a mature and cyclical rather than rapidly growing volume market. Precision agronomy may increase formulation complexity even if total nutrient tons remain flat.

## Risks and uncertainty
Key uncertainties are true custom-blend revenue share, customer concentration, weather and crop cycles, commodity working capital, hazardous-chemical reporting, seasonal labor, scale and recipe errors, self-blending, cooperative ownership, and a lack of plant-level workflow and contract data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0909 | — | OBSERVED | — |
| n | — | 93 | — | ESTIMATE | — |
| a | 0.22 | 0.35 | 0.49 | PROXY | S2, S3 |
| rho | 0.38 | 0.58 | 0.75 | ESTIMATE | S4, S5 |
| e | 0.42 | 0.64 | 0.82 | ESTIMATE | S1, S4, S6 |
| s5 | 0.14 | 0.27 | 0.41 | PROXY | S7 |
| q | 0.34 | 0.54 | 0.72 | ESTIMATE | S4, S8 |
| d5 | 0.86 | 0.99 | 1.12 | PROXY | S8 |
| o | 0.84 | 0.93 | 0.98 | ESTIMATE | S1, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.30 | 0.74 | 1.34 | ESTIMATE |
| F | 3.00 | 4.56 | 5.59 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.22 | 9.21 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation evidence is not unique to NAICS 325314.
- a: Generic process automation is included only where AI can substitute decisions or avoid hiring; already automated tasks are excluded.
- rho: This is bounded judgment rather than observed industry adoption.
- rho: Plants with modern automated loadout and ERP systems have less remaining opportunity than paper-driven operators.
- e: The NAICS definition confirms mixing activity but not recurring-service revenue share or LMM independence.
- e: Retail fertilizer sites may combine eligible blending with substantial noneligible product resale and application services.
- s5: The Census statistic covers all responding employer-business owners, not this industry or firm band.
- s5: It measures age rather than intended sale, transferability, or transaction completion.
- q: No public contract sample was available.
- q: Capture depends on whether the firm sells advice and logistics with the blend or competes on a transparent toll fee alone.
- d5: Aggregate fertilizer consumption does not isolate mixing-only establishments.
- d5: Constant nutrient tons can generate different blending-service demand as formulations and number of field-specific recipes change.
- o: Software may enable self-service ordering without eliminating the physical blender.
- o: The estimate excludes labor automation already captured in a and rho and focuses on whether the accountable operator remains required.

## Sources
- **S1** — [2022 NAICS definition: 325314 Fertilizer (Mixing Only) Manufacturing](https://www.census.gov/naics/?details=325&input=325&year=2022) (accessed 2026-07-22): Defines the industry as establishments primarily engaged in mixing ingredients made elsewhere into fertilizers.
- **S2** — [Mixing and Blending Machine Setters, Operators, and Tenders, May 2023](https://www.bls.gov/oes/2023/may/oes519023.htm) (accessed 2026-07-22): Defines the occupation as setting up, operating, or tending mixing and blending machinery and reports 10,570 workers in chemical manufacturing groups including 3253.
- **S3** — [Factors affecting occupational utilization](https://www.bls.gov/emp/tables/factors-affecting-occupational-utilization.htm) (accessed 2026-07-22): States that the employment share of mixing and blending machine operators decreases as automated manufacturing processes require fewer manual tasks.
- **S4** — [Profile of the Agricultural Chemical, Pesticide, and Fertilizer Industry](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=50000EGG.TXT) (accessed 2026-07-22): Describes fertilizer mixing facilities purchasing bulk fertilizer materials and mixing many materials into formulations for sale, including common nitrogen, phosphate, potash, and micronutrient inputs.
- **S5** — [Fertilizer Manufacturing Effluent Guidelines](https://www.epa.gov/eg/fertilizer-manufacturing-effluent-guidelines) (accessed 2026-07-22): Explains that mixed fertilizers contain two or more primary nutrients and can be produced by mechanically blending straight fertilizers; includes NAICS 325314 and mixed/blend production under Part 418.
- **S6** — [EPCRA reporting and retail fertilizer exemptions](https://www.epa.gov/epcra/epcra-hazardous-chemical-inventory-reporting-agricultural-operations-and-retail-fertilizer) (accessed 2026-07-22): States that retailers mixing or blending on site do not receive the retail fertilizer exemption for material intended for mixing and may need hazardous-chemical inventory reporting above thresholds.
- **S7** — [Business Owners' Ages: Over Half of U.S. Business Owners Were Age 55 and Over](https://www.census.gov/library/visualizations/2020/comm/business-owners-ages.html) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 ABS, data year 2018.
- **S8** — [U.S. fertilizer consumption rebounds from 2021 drop](https://www.ers.usda.gov/data-products/charts-of-note/113348) (accessed 2026-07-22): Reports 21 million metric tons of US fertilizer consumption in 2013, 20 million in 2014 with stability through 2020, a 9.4% decline to 18.3 million in 2021, and stable nutrient shares over 2006-23.
