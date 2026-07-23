# 112410 — Sheep Farming

*v5.1 Stage 1 research memo. Run `112410-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Remote monitoring, electronic identification, and grazing technologies can reduce costly search, recordkeeping, and supervision across dispersed flocks.
**Weakness:** A structurally declining, import-exposed industry with mostly small flocks and missing market-size inputs offers limited scalable labor economics.

## Business-model lens
- Included: Independent U.S. operating farms and ranches repeatedly raising sheep and lambs or feeding lambs for external sale, including wool production, within the specified EBITDA band.
- Excluded: Goat farming, hobby flocks, passive grazing-land ownership, livestock transport or stockyards, slaughter and processing, custom herding or shearing services classified elsewhere, captive units, non-control financing vehicles, and operations without transferable control.
- Customer and revenue model: Recurring sales of feeder and slaughter lambs, breeding stock, cull animals, wool, and related byproducts to auctions, feedlots, processors, marketers, cooperatives, textile buyers, restaurants, and direct customers, priced by live or carcass weight, grade, timing, wool quality, contracts, and market conditions.
- Deviation from default lens: none

## Executive view
Sheep farming has targeted AI opportunities in flock monitoring, grazing, animal health, identification, scheduling, and records, but core work remains physical and the industry is small and structurally declining. Missing labor-share and LMM-count inputs prevent confident economic sizing.

## How AI changes the work
GPS collars, electronic identification, cameras, and models can improve animal location, grazing, lambing and health alerts, traceability, feed planning, marketing, and bookkeeping. Handling, lambing, fencing, shearing, transport, veterinary response, and predator control remain.

## Value capture
Direct, ethnic, breeding, local, and high-quality channels can retain value. Commodity auctions, packers, imports, feed, grazing costs, and wool weakness erode gains.

## Firm availability
Many farms own sheep, but most flocks are small and many operations are diversified. Land, permits, livestock, equipment, and entities often transfer separately, and no defensible frozen LMM count exists.

## Demand durability
Domestic inventory and wool production continue to weaken while imports support stable consumption. Specialty niches may grow, but national domestic operator demand is more likely to contract modestly; almost all remaining output still requires an accountable operator.

## Risks and uncertainty
Risks include predators, drought, disease, lamb mortality, feed and grazing costs, labor and shearing availability, processor access, import competition, wool prices, public-land permits, connectivity, animal-welfare acceptance, and missing labor-share and firm-count inputs.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.12 | 0.22 | 0.34 | PROXY | S3, S4, S5 |
| rho | 0.25 | 0.42 | 0.6 | ESTIMATE | S3, S4, S5 |
| e | 0.24 | 0.46 | 0.65 | ESTIMATE | S2, S6 |
| s5 | 0.18 | 0.33 | 0.49 | PROXY | S7 |
| q | 0.3 | 0.49 | 0.67 | PROXY | S2, S8 |
| d5 | 0.78 | 0.92 | 1.08 | PROXY | S2, S8, S9 |
| o | 0.985 | 0.997 | 1 | ESTIMATE | S1, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 6.00 | 9.80 | 10.00 | PROXY |
| D | 7.68 | 9.17 | 10.00 | ESTIMATE |

## Caveats
- a: No defensible compensation-to-receipts denominator was provided, and employee wage data would omit much owner and family labor.
- a: Most virtual-fencing evidence is broader grazing-livestock evidence, and sheep adoption and collar economics may differ from cattle.
- rho: Animal health, grazing, and loss reductions are not all labor substitution.
- rho: Range flocks, small pasture flocks, feedlots, wool operations, and hair-sheep systems have different implementation economics.
- e: The frozen dataset explicitly provides no defensible LMM firm count, so this conditional share cannot establish target volume.
- e: Flock inventory farms are not necessarily 112410-primary firms, and farm income does not map cleanly to EBITDA.
- s5: Producer age is not owner age or sale intent, and one farm can have several producers.
- s5: Intra-family succession and asset liquidation may not qualify as control transfers.
- q: National import and consumption data do not isolate eligible LMM farms or specialty channels.
- q: Meat, breeding stock, wool, direct sales, and grazing-service economics differ substantially.
- d5: Inventory and production are supply measures and can move differently from customer demand.
- d5: Per-capita disappearance includes imports and therefore overstates demand for domestic sheep operators.
- o: Operations may consolidate, vertically integrate, or shift to contract grazing without eliminating the operator requirement.
- o: Imports can displace domestic operators without making software the supplier.

## Sources
- **S1** — [NAICS Definition: 112410 Sheep Farming](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-23): Defines the industry as raising sheep and lambs or feeding lambs for fattening, for sale or wool production.
- **S2** — [Sheep, Lamb and Mutton - Sector at a Glance](https://www.ers.usda.gov/topics/animal-products/sheep-lamb-mutton/sector-at-a-glance) (accessed 2026-07-23): Documents long-run inventory, production, revenue, and operation declines, market structure, regional concentration, consumption, and imports exceeding half of U.S. supply.
- **S3** — [Virtual Fencing](https://www.nrcs.usda.gov/sites/default/files/2024-12/Virtual%20Fence%20SD-FS-126%2010-29-24.pdf) (accessed 2026-07-23): Describes GPS-collar virtual fencing for cattle, sheep, and goats, including operating needs, connectivity, batteries, and base stations.
- **S4** — [Virtual Fencing: A Climate Adaptation Strategy](https://www.climatehubs.usda.gov/hubs/northwest/topic/virtual-fencing-climate-adaptation-strategy) (accessed 2026-07-23): Describes virtual-fence control of grazing livestock and notes documented success with sheep and goats.
- **S5** — [Sheep and Goat Identification](https://www.aphis.usda.gov/animal-disease/sheep-goat/scrapie-tag) (accessed 2026-07-23): Documents official animal identification and USDA encouragement of electronic identification for faster disease traceability.
- **S6** — [2022 Census of Agriculture - U.S. Sheep and Lamb Data](https://www.nass.usda.gov/Publications/AgCensus/2022/Full_Report/Volume_1%2C_Chapter_2_US_State_Level/usv1.pdf) (accessed 2026-07-23): Reports 88,853 farms with sheep inventory and flock-size distribution, including only 582 farms with 1,000 or more head.
- **S7** — [2022 Census of Agriculture Farm Producers Demographic Profile](https://www.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/Demographic_Profiles/cpd99000.pdf) (accessed 2026-07-23): Reports average producer age of 58.1, 38% age 65 or older, and 95% family farms.
- **S8** — [Sheep and Goats - January 2026](https://www.nass.usda.gov/Publications/Todays_Reports/reports/shep0126.pdf) (accessed 2026-07-23): Reports 4.99 million sheep and lambs, inventory down 1%, a slightly lower lamb crop, wool production down 5%, and wool value down 7%.
- **S9** — [USDA Agricultural Projections to 2035](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/113817/OCE-2026-1.pdf) (accessed 2026-07-23): Projects per-capita lamb and mutton disappearance near 1.2 pounds through 2031 before a modest increase later.
