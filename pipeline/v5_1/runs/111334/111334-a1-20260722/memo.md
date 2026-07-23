# 111334 — Berry (except Strawberry) Farming

*v5.1 Stage 1 research memo. Run `111334-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Specialty-crop sensing, decision support, and machine-enabled harvesting expose meaningful berry-farm tasks to automation.
**Weakness:** Very few berry farms appear to meet the fixed outsourced-service lens, and the eligible population cannot be anchored to a frozen LMM count.

## Business-model lens
- Included: Lower-middle-market berry farms operating under recurring production contracts in which an external contractor owns or directs the commodity and compensates the grower for cultivation services.
- Excluded: Farms selling grower-owned berries through spot sales or marketing contracts, hobby and lifestyle farms, captive units, custom farm-support contractors classified outside NAICS 111334, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring or repeat production-service fees paid by processors, marketers, or other contractors for growing specified berries under contractor production requirements; ordinary farm-gate commodity sales are outside the fixed service lens.
- Deviation from default lens: none

## Executive view
Berry farming contains labor-intensive and increasingly automatable work, but the fixed screen lens is a poor fit for most of the industry because ordinary growers sell farm products rather than outsourced services. The coherent eligible population is limited to true production-contract growers, and both the frozen labor share and LMM firm count are missing.

## How AI changes the work
AI can assist crop scouting, yield and maturity estimation, irrigation and spray decisions, harvest planning, quality inspection, records, and scheduling; machine vision can also enable autonomous field equipment. Fresh-market harvest remains constrained by bruising, immature fruit, packout losses, irregular canopies, and capital requirements.

## Value capture
A contract grower may retain savings under a fixed service fee, but contractors can prescribe practices, own inputs or equipment, impose quality adjustments, and reprice renewals. Import competition and the cost-price squeeze in blueberries strengthen buyer leverage.

## Firm availability
Eligibility is the decisive weakness. Marketing contracts are common in fruit but preserve grower ownership of the crop, while true production contracts that compensate a grower for services are uncommon in crop farming. Missing LMM firm-count data adds a separate unresolved population gap.

## Demand durability
Berry consumption and blueberry production have grown, but imports increasingly meet U.S. demand and compete during domestic seasons. Biological cultivation continues to require an accountable operator, although demand for a U.S. contract grower can migrate to foreign suppliers or vertically integrated farms.

## Risks and uncertainty
Key risks are the mismatch between product farming and the service lens, missing labor and firm-count inputs, crop heterogeneity, weather and water exposure, private contract terms, import pressure, automation quality losses, equipment economics, and succession outcomes that end in closure or family continuity rather than a transferable control deal.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.18 | 0.3 | 0.43 | PROXY | S2, S3 |
| rho | 0.2 | 0.36 | 0.54 | PROXY | S2, S3 |
| e | 0.003 | 0.015 | 0.04 | PROXY | S1, S6 |
| s5 | 0.16 | 0.27 | 0.4 | PROXY | S4 |
| q | 0.25 | 0.45 | 0.64 | PROXY | S2, S6 |
| d5 | 0.94 | 1.05 | 1.18 | PROXY | S2, S5, S7 |
| o | 0.97 | 0.99 | 0.999 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 5.00 | 9.00 | 10.00 | PROXY |
| D | 9.12 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The frozen labor-share input is missing, so the scale of labor opportunity cannot be anchored to industry compensation and receipts.
- a: Blueberry evidence may not represent cranberries, raspberries, blackberries, currants, and other berries with different harvest systems.
- a: Mechanization is not automatically AI exposure, and some machine-harvest tasks are already automated.
- rho: USDA examples span specialty crops and include prototypes rather than only commercially durable berry deployments.
- rho: Implementation varies sharply between fresh and processing markets and by farm layout.
- rho: Mechanical aids may raise worker productivity without eliminating accountable labor.
- e: The frozen LMM firm count is missing, so no eligible-firm count can be derived from this share.
- e: The contract-incidence proxy is for all U.S. farms rather than berry farms or the LMM band.
- e: Some economically service-like growing arrangements may be reported as marketing contracts, creating classification error.
- s5: National farm demographics may not represent commercial berry farms or production contractors.
- s5: Producer age is not owner age when farms have several decision-makers or entities.
- s5: No observed denominator of eligible berry farms and qualifying transfers was found.
- q: Contract terms are private and no berry-specific retention sample was found.
- q: The eligible lens is unusually narrow, so ordinary farm-gate pricing evidence is only directional.
- q: Import competition affects commodity prices and contractor bargaining but is not a direct contractual pass-through measure.
- d5: Blueberries are only one component of NAICS 111334.
- d5: Production volume and consumer availability are not constant-price demand for the narrowed production service.
- d5: Imports can satisfy U.S. berry consumption without creating demand for U.S. farm operators.
- o: This is a bounded judgment rather than a directly observed operator-required share.
- o: Contractors may vertically integrate and self-operate farms, eliminating external service demand rather than operator accountability.
- o: The estimate applies only after the separate demand-ratio adjustment.

## Sources
- **S1** — [2022 NAICS 111334: Berry (except Strawberry) Farming](https://www.census.gov/naics/?details=111&input=111&year=2022) (accessed 2026-07-22): Defines the industry as establishments primarily engaged in growing berries and explains that crop production generally ends at the farm gate for first sale or price determination.
- **S2** — [Supplement to Adjusting to Higher Labor Costs in Selected U.S. Fresh Fruit and Vegetable Industries: Case Studies](https://ers.usda.gov/media/9005/ap-103.pdf?v=25929) (accessed 2026-07-22): USDA ERS documents blueberry hand and machine harvesting, harvester costs, fresh-market packout losses, rising mechanization, import competition, and an expected cost-price squeeze; it also reports fruit and tree-nut labor costs reaching 38.5% of production expenses.
- **S3** — [Automation for Specialty Crops](https://www.nifa.usda.gov/about-nifa/impacts/automation-specialty-crops) (accessed 2026-07-22): USDA NIFA describes commercializing specialty-crop sensors, imaging, machine vision, deep learning, autonomous weeding, targeted spraying, yield estimation, and robotic harvest systems, together with adoption efforts and performance limitations.
- **S4** — [2022 Census of Agriculture: Farm Producers](https://www.nass.usda.gov/Publications/Highlights/2024/Census22_HL_FarmProducers_FINAL.pdf) (accessed 2026-07-22): Reports an average U.S. producer age of 58.1, 38% of producers age 65 or older, increasing multi-producer farms, and continuing producer aging, supporting a succession-pressure proxy.
- **S5** — [Most cultivated blueberries are destined for the fresh market, while wild blueberries are bound for processing](https://ers.usda.gov/data-products/charts-of-note/113313) (accessed 2026-07-22): Reports record cultivated blueberry production of 789.5 million pounds in 2024, with 55% going to fresh markets, and describes different market destinations for cultivated and wild berries.
- **S6** — [Contracts are common in animal and crop production](https://www.ers.usda.gov/data-products/charts-of-note/103803) (accessed 2026-07-22): Distinguishes marketing contracts, where farmers retain commodity ownership, from production contracts, where contractors generally own the commodity and compensate growers for services; reports production contracts at 2% of farms in 2020 and crop contracting concentrated in marketing contracts.
- **S7** — [U.S. fresh fruit and vegetable supplies continue to rely on imports](https://ers.usda.gov/data-products/charts-of-note/110713) (accessed 2026-07-22): Reports increasing import shares of U.S. fresh-fruit availability through 2023 and identifies blueberries and raspberries among crops with substantial import-share increases, supporting the domestic-demand competition caveat.
