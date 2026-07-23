# 111331 — Apple Orchards

*v5.1 Stage 1 research memo. Run `111331-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** High fruit-sector labor intensity creates material value if sensing, workflow tools, and selective mechanization can be implemented reliably.
**Weakness:** The industry sells a seasonal commodity crop rather than a recurring outsourced service, and public evidence does not establish a pool of transferable eligible firms.

## Business-model lens
- Included: U.S. lower-middle-market operating companies whose primary establishment activity is growing apples and selling the harvested crop to external packers, processors, wholesalers, retailers, or direct customers, including orchard-level harvest and farm-gate preparation performed by the grower.
- Excluded: Mixed farms for which apples are not the primary output; independent packers, processors, distributors, and farm-service contractors; hobby or noncommercial orchards; passive landowners; captive internal units; shells; and non-control financing vehicles.
- Customer and revenue model: Seasonal crop revenue from fresh-market and processing apples sold through contracts, spot channels, cooperatives, wholesalers, retailers, and direct-to-consumer channels. Buyer relationships may repeat annually, but the economic output is a physical crop rather than a billed outsourced service.
- Deviation from default lens: none

## Executive view
Apple orchards offer a real labor-productivity problem, especially around seasonal harvest, sensing, planning, and records, but they are an awkward fit for a repeat outsourced-service screen because revenue comes from crop sales and the frozen firm-count and labor inputs are both missing. Automation economics will be strongest in modern, uniform orchards with enough scale and technical support.

## How AI changes the work
Near-term AI is more credible in crop-load estimation, maturity and quality sensing, spray and irrigation decisions, labor scheduling, compliance records, and sales planning than in universal autonomous picking. Robotic harvest is technically active, but canopy variation, occlusion, fruit damage, speed, uptime, and the short harvest season constrain broad deployment.

## Value capture
Implemented savings can accrue to the grower through lower hired-labor needs, reduced crop loss, improved quality, and better timing. Annual commodity pricing and buyer bargaining should share some gains, while branded varieties, direct sales, storage flexibility, and quality premiums can improve retention.

## Firm availability
Public data establish an aging farm-owner population but do not identify eligible apple operating companies in the specified earnings band or observe qualifying control deals. Land, orchard improvements, packing assets, water rights, and the operating entity may transfer separately, making apparent farm turnover a weak acquisition proxy.

## Demand durability
Apple availability has been broadly stable over decades, and fresh fruit and juice provide diversified end uses. Weather, climate, imports, processing economics, consumer sugar preferences, and variety shifts can still make any one orchard's realized demand and price materially less stable than aggregate consumption.

## Risks and uncertainty
The largest uncertainties are missing frozen l and n, absent apple-specific task-time data, prototype-to-commercial robotics risk, orchard-architecture heterogeneity, seasonal utilization, volatile yields and prices, and the difference between land succession and operating-company control transfer. A credible diligence case requires orchard-level labor, technology, channel, and transaction data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.18 | 0.32 | 0.48 | PROXY | S2, S3, S4, S5 |
| rho | 0.25 | 0.45 | 0.65 | PROXY | S4, S5 |
| e | 0.3 | 0.5 | 0.7 | ESTIMATE | S1, S8 |
| s5 | 0.06 | 0.13 | 0.24 | PROXY | S8, S9 |
| q | 0.22 | 0.4 | 0.6 | ESTIMATE | S6, S7 |
| d5 | 0.88 | 0.99 | 1.12 | PROXY | S6, S7 |
| o | 0.985 | 0.997 | 1 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 4.40 | 8.00 | 10.00 | ESTIMATE |
| D | 8.67 | 9.87 | 10.00 | ESTIMATE |

## Caveats
- a: The provided compensation-to-receipts input l is missing, so this task-share judgment cannot be checked against industry labor intensity in the frozen dataset.
- a: The USDA labor-cost statistic covers fruit and tree nut farms, not apple orchards alone.
- a: Research capability does not establish commercial reliability, utilization, or net labor displacement.
- rho: Public research projects do not report adoption rates for the screened firm population.
- rho: Implementation will differ sharply between high-density trellised blocks and older tree forms.
- rho: Annual harvest windows reduce equipment utilization and increase the importance of service support.
- e: The dataset input n is missing and was not re-estimated.
- e: Establishment classification does not reveal enterprise boundaries, normalized EBITDA, or whether sales are external.
- e: Farm proprietorship and family labor can make accounting earnings a poor measure of transferable operating economics.
- s5: Producer age is a national all-farm proxy and does not identify the controlling owner of an eligible apple business.
- s5: The NASS transfer statistic concerns acres and expressly excludes some inheritance routes.
- s5: A farm or land transfer may not constitute a qualifying control transfer of a transferable operating company.
- q: No source directly measures five-year retention of automation benefits by apple growers.
- q: Channel and variety mix can dominate bargaining power and price realization.
- q: The estimate excludes implementation risk and quantity changes, which belong in rho and demand primitives.
- d5: Availability is not a direct demand curve and includes inventory and trade effects.
- d5: Aggregate U.S. demand does not determine volume for a particular region, variety, or orchard.
- d5: Weather and biological cycles can move production independently of final demand.
- o: This is a structural judgment rather than an observed displacement rate.
- o: Consolidation changes who operates orchards but does not necessarily eliminate the operator role.
- o: Demand loss and orchard conversion are reflected primarily in d5, not duplicated here.

## Sources
- **S1** — [2022 NAICS definition: Apple Orchards](https://www.census.gov/naics/?details=111&input=111&year=2022) (accessed 2026-07-23): Industry boundary: apple-growing establishments and the farm-gate endpoint of crop production.
- **S2** — [Farm Labor](https://www.ers.usda.gov/topics/farm-economy/farm-labor?os=qtfT_1) (accessed 2026-07-23): Fruit and tree nut labor-cost intensity, farm occupation mix, wage trends, labor scarcity, and mechanical aids in tree-fruit harvest.
- **S3** — [Agricultural Workers: Occupational Outlook Handbook](https://www.bls.gov/ooh/farming-fishing-and-forestry/agricultural-workers.htm) (accessed 2026-07-23): Crop-worker tasks including planting, pruning, irrigation, harvesting, packing, loading, equipment, and chemical application.
- **S4** — [USDA ARS project: Integrated Design and Control of a New Multi-Arm Robotic Apple Harvesting System](https://www.ars.usda.gov/research/project/?accnNo=445530) (accessed 2026-07-23): Current apple-specific AI, perception, planning, control, and robotic-harvest research objectives and field testing.
- **S5** — [USDA ARS publication: AppleHarvestSAM2 Dataset](https://www.ars.usda.gov/research/publications/publication/?seqNo115=423936) (accessed 2026-07-23): Continued manual-harvest prevalence, harvest-cost significance, and apple-specific AI fruit-detection development.
- **S6** — [Fruit and Tree Nuts Outlook: March 2026](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/113982/FTS-384.pdf?v=11271) (accessed 2026-07-23): Apple availability, channel mix, historical consumption band, and domestic share of fresh-market supply.
- **S7** — [Fruit and Tree Nuts Outlook: September 2025](https://www.ers.usda.gov/sites/default/files/_laserfiche/outlooks/113466/FTS-383.pdf) (accessed 2026-07-23): U.S. apple production forecast and recent production comparison.
- **S8** — [2022 Census of Agriculture Highlights: Farm Producers](https://www.nass.usda.gov/Publications/Highlights/2024/Census22_HL_FarmProducers_FINAL.pdf) (accessed 2026-07-23): National farm-producer age and experience distribution.
- **S9** — [Most of the U.S. Rented Farmland is Owned by Non-Farmers](https://www.nass.usda.gov/Newsroom/2026/03-12-2026.php) (accessed 2026-07-23): Planned five-year agricultural land ownership transfers and owner age from the 2024 TOTAL survey.
