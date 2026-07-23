# 112390 — Other Poultry Production

*v5.1 Stage 1 research memo. Run `112390-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** A contract grower provides recurring, physically indispensable husbandry and facility capacity that software alone cannot replace.
**Weakness:** Other-poultry-specific evidence is sparse, the industry code mixes incompatible species and revenue models, and concentrated integrators can appropriate AI savings or eliminate an outsourced grower relationship.

## Business-model lens
- Included: U.S. lower-middle-market contract growers that repeatedly raise non-chicken, non-turkey poultry such as ducks, geese, quail, pheasants, emus, and ostriches for external integrators or processors, providing housing, equipment, utilities, husbandry, biosecurity, records, and labor for a grow-out fee.
- Excluded: Independent farms whose primary revenue is the sale of owned birds, meat, eggs, breeding stock, or hunting-release birds; backyard and hobby flocks; poultry hatcheries; chicken and turkey producers; integrator-owned captive farms; processors; and ornamental-bird operations.
- Customer and revenue model: The coherent outsourced-service model is recurring production-contract revenue from an integrator or processor, commonly linked to delivered bird or live-weight performance and sometimes adjusted for mortality, feed conversion, or relative results. Independent spot and product sales exist in the NAICS code but fall outside the fixed service lens.
- Deviation from default lens: Narrowed to contract grow-out establishments because NAICS 112390 combines contract husbandry services with economically different owned-flock product and niche game-bird models; only contract grow-out is a recurring outsourced service under the fixed lens.

## Executive view
The coherent acquisition lens is contract grow-out, not independent bird sales. This creates repeat revenue and a clear physical operating role, but the addressable population is uncertain and the code is fragmented across ducks, geese, quail, pheasants, and ratites. AI can improve monitoring and administration, yet contract terms and integrator power may capture much of the benefit. Missing compensation intensity and firm-count inputs prevent sizing either labor economics or absolute target availability.

## How AI changes the work
AI can interpret environmental and behavioral sensors, detect mortality or abnormal flock distribution, predict equipment failures, automate compliance records, benchmark flock performance, optimize energy and schedules, and support purchasing and reporting. Existing feeding, watering, and ventilation automation narrows the incremental opportunity; cleaning, catching, loading, repair, biosecurity execution, and animal handling remain physical.

## Value capture
Growers may retain reduced labor, utility, mortality, and maintenance costs when those costs are theirs, but integrators can capture gains through performance comparisons, fee formulas, mandated upgrades, or renewal pricing. Short formal contracts and geographically concentrated buyers weaken retention even when relationships last many years.

## Firm availability
Broad farm demographics imply succession pressure, but transfer requires viable specialized houses and a continuing integrator relationship. Independent product growers are outside the service lens, captive farms are excluded, and no current source isolates other-poultry contract growers by size. The firm-count dataset input is missing, so no target count is inferred.

## Demand durability
Other-poultry demand is likely broadly stable but unusually heterogeneous and exposed to restaurant cycles, game-bird demand, processor capacity, imports, and disease. HPAI is a material tail risk for ducks, pheasants, geese, and other covered birds and can cause flock loss, movement restrictions, and interrupted placements.

## Risks and uncertainty
The largest uncertainties are the current share and economics of contract grow-out within NAICS 112390, species-specific demand, local integrator concentration, contract assignability, and real-world AI returns outside chickens. Additional risks include HPAI, biosecurity failures, welfare compliance, energy costs, specialized asset obsolescence, processor closure, short contracts, and capital-upgrade mandates.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.12 | 0.21 | 0.32 | PROXY | S2, S3, S5, S6, S7 |
| rho | 0.32 | 0.5 | 0.68 | ESTIMATE | S5, S6, S7, S8 |
| e | 0.12 | 0.28 | 0.5 | ESTIMATE | S1, S4, S9 |
| s5 | 0.07 | 0.15 | 0.25 | PROXY | S10, S11 |
| q | 0.18 | 0.33 | 0.5 | PROXY | S4, S8, S9 |
| d5 | 0.82 | 0.99 | 1.16 | ESTIMATE | S1, S11, S12 |
| o | 0.86 | 0.94 | 0.99 | ESTIMATE | S3, S6, S7, S11 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 3.60 | 6.60 | 10.00 | PROXY |
| D | 7.05 | 9.31 | 10.00 | ESTIMATE |

## Caveats
- a: No NAICS 112390 occupation-by-hours dataset was located.
- a: Most precision-poultry research concerns broilers or layers rather than the species in this code.
- a: Technical exposure should not be interpreted as safe removal of human animal-welfare or biosecurity accountability.
- rho: Research prototypes and grant objectives are not adoption measurements.
- rho: Small flocks may not support the fixed cost of advanced sensors or robotics.
- rho: Integrator control over specifications may slow or accelerate adoption independently of grower economics.
- e: The code spans multiple species and both food and game-bird markets.
- e: The evidence does not measure lower-middle-market status or current other-poultry contract prevalence.
- e: The firm-count dataset input is missing and was not researched or replaced.
- s5: The demographic proxy covers all farms, not other-poultry contract growers.
- s5: Producer age does not identify sale intent or completed control transfers.
- s5: Highly specialized houses and local integrator dependence may reduce marketability.
- q: Broiler tournament systems may not represent duck, quail, pheasant, goose, or ratite contracts.
- q: Long relationship tenure does not imply durable written pricing protection.
- q: Integrator concentration can vary sharply by geography and species.
- d5: No unified NAICS 112390 demand series was located.
- d5: Food poultry, breeding stock, and hunting-release birds follow different demand cycles.
- d5: Highly pathogenic avian influenza can abruptly destroy flocks, halt placements, and restrict trade.
- o: This is a structural judgment rather than an observed displacement rate.
- o: Automation proven for chickens may not transfer economically to smaller species niches.
- o: Vertical integration can remove the outsourced grower while leaving physical operator work intact.

## Sources
- **S1** — [U.S. Census Bureau NAICS 112390 Other Poultry Production](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-23): Defines the industry as raising poultry other than chickens for meat or eggs and turkeys, with examples including ducks, emus, geese, ostriches, pheasants, and quail.
- **S2** — [BLS Occupational Outlook Handbook: Agricultural Workers](https://www.bls.gov/ooh/farming-fishing-and-forestry/agricultural-workers.htm) (accessed 2026-07-23): Describes animal-farmworker tasks such as feeding, weighing, loading, recordkeeping, disease and injury inspection, medication, and daily housing-area cleaning.
- **S3** — [BLS Occupational Outlook Handbook: Farmers, Ranchers, and Other Agricultural Managers](https://www.bls.gov/ooh/management/farmers-ranchers-and-other-agricultural-managers.htm) (accessed 2026-07-23): Describes poultry manager responsibilities spanning animal care, breeding, records, machinery, buildings, budgets, transport, sales, and supervision.
- **S4** — [USDA ERS: Marketing and Production Contracts Are Widely Used in U.S. Agriculture](https://www.ers.usda.gov/amber-waves/2019/july/marketing-and-production-contracts-are-widely-used-in-u-s-agriculture) (accessed 2026-07-23): Explains that most poultry is contract-produced and defines production contracts in which the contractor owns the commodity and pays the grower a fee for raising it.
- **S5** — [Penn State Extension: Poultry Facilities and Technology](https://extension.psu.edu/animals-and-livestock/poultry/facilities-and-technology) (accessed 2026-07-23): Documents poultry-house ventilation, ammonia monitoring, automatic watering, lighting, feeding, egg handling, and biosecurity equipment.
- **S6** — [USDA National Agricultural Library: Poultry Caretaker Robot to Improve Animal Well-Being](https://www.nal.usda.gov/research-tools/food-safety-research-projects/poultry-caretaker-robot-improve-animal-well-being) (accessed 2026-07-23): Describes a USDA-funded commercial prototype using autonomous navigation and computer vision for flock stimulation, litter work, mortality detection, and barn routing.
- **S7** — [Computer Vision Models for Precision Poultry Farming: A Narrative Review](https://pubmed.ncbi.nlm.nih.gov/41955872/) (accessed 2026-07-23): Reviews machine-learning and object-detection research for poultry health, welfare, behavior, and production monitoring, while showing that the evidence base remains research-heavy.
- **S8** — [USDA ERS: Broiler Contracts Often Specify Very Short Durations](https://www.ers.usda.gov/data-products/charts-of-note/74983) (accessed 2026-07-23): Shows the contrast between long grower-integrator relationships and short written production-contract terms, supporting renewal and repricing risk by proxy.
- **S9** — [USDA ERS: Contracting in the Poultry Industry](https://ers.usda.gov/sites/default/files/_laserfiche/publications/42203/13405_aib748c_1_.pdf?v=11890) (accessed 2026-07-23): Documents production contracts across broilers, turkeys, other poultry, and eggs and contrasts contract farms with integrated or independent operations.
- **S10** — [USDA NASS 2022 Census of Agriculture Highlights: Farm Producers](https://www.nass.usda.gov/Publications/Highlights/2024/Census22_HL_FarmProducers_FINAL.pdf) (accessed 2026-07-23): Reports that 38% of U.S. farm producers were age 65 or older and that average producer age was 58.1 in 2022.
- **S11** — [USDA APHIS: Avian Influenza](https://www.aphis.usda.gov/livestock-poultry-disease/avian/avian-influenza) (accessed 2026-07-23): Explains that HPAI can kill domestic poultry rapidly and that biosecurity, contaminated materials, equipment, and human movement are central operating risks.
- **S12** — [USDA APHIS HPAI Epidemiologic and Other Analyses: Seventh Interim Report](https://direct.aphis.usda.gov/sites/default/files/epi-analyses-avian-flu-poultry-7th-interim-rpt.pdf) (accessed 2026-07-23): Documents HPAI impacts across multiple commercial poultry types, including duck and upland gamebird premises, supporting species-specific disease volatility.
