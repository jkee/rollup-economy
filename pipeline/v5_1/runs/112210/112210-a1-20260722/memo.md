# 112210 — Hog and Pig Farming

*v5.1 Stage 1 research memo. Run `112210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Dense recurring animal, feed, health, and environmental data can support targeted care and operational decisions across standardized production barns.
**Weakness:** Integrator control and commodity or contract pricing limit firm eligibility and value retention, while the screen lacks both core dataset denominators.

## Business-model lens
- Included: US lower-middle-market commercial hog and pig farms with recurring external revenue from breeding, farrowing, nursery, feeder-pig, finishing, or farrow-to-finish production sold to integrators, processors, livestock buyers, or other farms, including independent and production-contract growers.
- Excluded: Hobby and subsistence farms, pork processors without farming, livestock transport and stockyards, captive internal facilities without external revenue, genetics or veterinary businesses outside farm production, shells, and non-control land or financing vehicles.
- Customer and revenue model: Repeat livestock revenue through formula or negotiated hog sales, marketing contracts, packer programs, and production contracts that pay growers for housing and caring for pigs owned by an integrator, with economics affected by feed, productivity, mortality, weight, quality, facility terms, and environmental compliance.
- Deviation from default lens: none

## Executive view
Hog farming offers credible AI value in continuous animal monitoring, targeted care, feed and environment decisions, forecasting, records, and administration. Physical husbandry remains operator-required, while consolidation, contract production, integrator control, commodity pricing, and missing labor and firm-count inputs weaken the opportunity case.

## How AI changes the work
Vision, acoustic, vibration, weight, feed, and environmental data can identify distress, farrowing, illness, behavior, growth, and equipment anomalies, directing staff to the right pens and improving forecasts. Humans still treat and move animals, maintain barns, clean, manage manure, enforce biosecurity, and respond to failures.

## Value capture
Feed efficiency, mortality, weight, throughput, and labor gains can be valuable, but benefit ownership depends on who owns pigs, feed, buildings, data, and technology. Integrators, packers, contract renewals, and transparent hog prices can absorb a large share.

## Firm availability
The industry has shifted toward fewer, larger, phase-specialized and contracted operations. Eligible LMM farms may exist among independent producers and contract growers, but integrator ownership, small farms, single-customer dependence, environmental liabilities, and the missing denominator require entity-level diligence.

## Demand durability
USDA expects modest pork production growth and stronger exports, but productivity gains can serve that demand with fewer farms. Disease, feed costs, trade, processing capacity, environmental regulation, and continued consolidation determine whether LMM operators participate.

## Risks and uncertainty
African swine fever and other disease, biosecurity, mortality, feed prices, packer and integrator concentration, contract terms, barn debt, manure and water rules, odor litigation, animal-welfare mandates, labor, and power failures are material. Evidence is weakest because labor share and LMM firm count are both missing.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.19 | 0.3 | 0.42 | PROXY | S1, S2, S3 |
| rho | 0.47 | 0.62 | 0.75 | ESTIMATE | S2, S3 |
| e | 0.27 | 0.44 | 0.61 | ESTIMATE | S4, S5 |
| s5 | 0.16 | 0.27 | 0.4 | PROXY | S6 |
| q | 0.25 | 0.41 | 0.58 | ESTIMATE | S4, S5 |
| d5 | 0.97 | 1.06 | 1.15 | PROXY | S5, S7, S8 |
| o | 0.985 | 0.996 | 1 | ESTIMATE | S1, S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 5.00 | 8.20 | 10.00 | ESTIMATE |
| D | 9.55 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No labor-compensation ratio is available in the frozen dataset, so aggregate labor opportunity remains unevidenced.
- a: Production phase, barn age, ownership of pigs, and outsourced veterinary or feed services materially change the task mix.
- rho: Research demonstrations are not industry-wide adoption evidence.
- rho: Integrators may own data and prescribe technology, leaving contract growers little implementation discretion.
- e: The frozen dataset has no defensible LMM firm count.
- e: Farm counts include small or diversified operations, while inventory and revenue are highly concentrated among large producers.
- s5: National producer age is not hog-specific and does not measure completed transfers.
- s5: Multiple family producers and corporate or integrator ownership weaken the age-to-control bridge.
- q: No contract sample directly measures automation pass-through.
- q: Independent ownership, integrator-owned pigs, and specialized phase contracts allocate costs and benefits differently.
- d5: Pork output is downstream of farms and can grow through productivity rather than more farm-service quantity.
- d5: Industry growth may concentrate in large integrated operations outside the LMM lens.
- o: The accountable operator may consolidate across sites or shift from grower to integrator.
- o: Cultivated-meat substitution belongs primarily in demand rather than operator requirement and is not double-counted here.

## Sources
- **S1** — [2022 NAICS Manual: 112210 Hog and Pig Farming](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines the industry as establishments raising hogs and pigs, including breeding, farrowing, weanling pigs, feeder pigs, market hogs, and farrow-to-finish and finishing operations.
- **S2** — [Automated Swine Phenotyping for Management and Research](https://www.nal.usda.gov/research-tools/food-safety-research-projects/automated-swine-phenotyping-management-and-research) (accessed 2026-07-22): Describes a USDA-funded precision-livestock project using detection, tracking, posture, identity, body-condition, activity, and feeder-interaction measurements, grounding monitorable tasks without claiming commercial adoption.
- **S3** — [Sensors monitor farrowing activity and piglet care](https://www.ars.usda.gov/research/project?accnNo=442712&fy=2024) (accessed 2026-07-22): Reports USDA research using seismic sensors and predictive modeling to identify sow and piglet activities and direct timely care, illustrating potential labor targeting and the need for human intervention.
- **S4** — [Hogs and Pork: Sector at a Glance](https://www.ers.usda.gov/topics/animal-products/hogs-pork/sector-at-a-glance) (accessed 2026-07-22): Reports that farms with hogs declined more than 70 percent since 1990 as operations grew, phase specialization and production contracts increased, and scale and technology drove productivity, grounding consolidation and business-model risks.
- **S5** — [Quarterly Hogs and Pigs, December 2024](https://www.nass.usda.gov/Publications/Todays_Reports/reports/hgpg1224.pdf) (accessed 2026-07-22): Reports 75.8 million hogs and pigs, 11.92 pigs saved per litter, and that hogs owned by operations above 5,000 head but raised by contractees accounted for 50 percent of US inventory, grounding scale and contracting.
- **S6** — [USDA releases 2022 Census of Agriculture data](https://www.nass.usda.gov/Newsroom/2024/02-13-2024.php) (accessed 2026-07-22): Reports an average US producer age of 58.1 in 2022, up 0.6 years from 2017, used as a broad succession-pressure proxy rather than hog-specific transfer evidence.
- **S7** — [Hogs and Pork: Market Outlook](https://www.ers.usda.gov/topics/animal-products/hogs-pork/market-outlook) (accessed 2026-07-22): Forecasts 2026 pork production at 27.995 billion pounds, 1.5 percent above 2025, and 2027 production at 28.290 billion pounds, 1.1 percent above 2026, while projecting lower hog prices.
- **S8** — [U.S. pork exports projected to grow, remain higher than broiler chicken and beef exports](https://ers.usda.gov/data-products/charts-of-note/114093) (accessed 2026-07-22): Projects US pork exports to increase 8.6 percent from 7.2 billion pounds in 2026 to 7.8 billion in 2035, supported by higher weights, pigs per litter, inventories, and foreign demand.
