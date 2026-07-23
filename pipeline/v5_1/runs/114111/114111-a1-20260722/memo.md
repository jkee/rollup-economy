# 114111 — Finfish Fishing

*v5.1 Stage 1 research memo. Run `114111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.16 · L 1.02 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digital navigation, reporting, monitoring, and catch-analysis workflows can reduce wasted trips and administrative or review labor on costly vessels.
**Weakness:** Biological and regulatory quantity constraints plus owner-captain and permit dependence make outcomes highly fishery-specific and can prevent a clean transfer of operating control.

## Business-model lens
- Included: U.S. lower-middle-market operating companies primarily engaged in commercially catching finfish from natural habitat and repeatedly selling landed catch to external processors, dealers, wholesalers, auctions, restaurants, or other buyers, including vessel operation, navigation, gear deployment, catch handling, and required reporting.
- Excluded: Aquaculture and hatcheries; shellfish and other marine-product fishing; recreational charter services; seafood processing detached from the fishing operation; passive vessel or permit ownership; captive internal fleets; shells; and non-control financing vehicles.
- Customer and revenue model: Trip- and season-based product revenue from ex-vessel sales of wild finfish, often through repeat dealer or processor relationships. Realized revenue depends on landed weight, species, grade, market price, quota or allocation, season, bycatch rules, fuel and crew-share economics, and permit access.
- Deviation from default lens: none

## Executive view
Finfish fishing has a credible but bounded digital opportunity in route and location support, electronic reporting, catch monitoring, machine vision, compliance, and administration. Physical deck work, safety-critical vessel operations, quota and stock constraints, commodity pricing, permit complexity, and owner-captain dependence limit both labor substitution and transferability.

## How AI changes the work
AI can combine weather, ocean, sonar, historical catch, and market data to support trip planning, while vision systems can help identify, count, and measure catch and reduce manual video review. It can also automate logbooks, document checks, maintenance alerts, and buyer administration. Gear handling, sorting in irregular conditions, repairs, navigation accountability, and emergency response remain human work.

## Value capture
Value can come from fewer unproductive vessel hours, lower fuel use, better targeting within legal limits, reduced reporting burden, improved quality, and fewer compliance errors. Buyers and competing vessels may capture part of cost savings through ex-vessel pricing, while scarce permits and catch rights can preserve more value in constrained fisheries.

## Firm availability
The frozen dataset estimates only ten firms in the target earnings band, and the margin bridge is not fishery-specific. Aging participants and high entry costs create transition pressure, but permits, quota, vessels, and operating entities may transfer separately, and owner-captain knowledge can be difficult to replace.

## Demand durability
Seafood demand is established, but imported product and aquaculture meet much of U.S. consumption. Domestic wild-finfish quantity depends as much on biological stocks, catch limits, climate-driven range shifts, protected-species rules, and processor capacity as on consumer appetite.

## Risks and uncertainty
The most material uncertainties are fishery and gear heterogeneity, current automation by vessel class, field reliability, regulatory acceptance, cyber and connectivity risk, fuel and quota economics, volatile landings and prices, climate and stock changes, buyer concentration, crew-share accounting, permit transfer rules, and the dataset's broad-margin estimate of n.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1551 | — | OBSERVED | — |
| n | — | 10 | — | ESTIMATE | — |
| a | 0.18 | 0.3 | 0.42 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.55 | 0.72 | PROXY | S3, S4 |
| e | 0.4 | 0.6 | 0.8 | ESTIMATE | S1, S2, S9 |
| s5 | 0.07 | 0.16 | 0.3 | PROXY | S7, S8, S9 |
| q | 0.25 | 0.45 | 0.68 | ESTIMATE | S5, S6, S9 |
| d5 | 0.82 | 0.96 | 1.1 | PROXY | S2, S5, S6 |
| o | 0.97 | 0.995 | 1 | ESTIMATE | S1, S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.39 | 1.02 | 1.88 | PROXY |
| F | 0.40 | 1.08 | 1.97 | ESTIMATE |
| C | 5.00 | 9.00 | 10.00 | ESTIMATE |
| D | 7.95 | 9.55 | 10.00 | ESTIMATE |

## Caveats
- a: BLS combines fishing and hunting workers and does not publish a finfish-specific wage-weighted occupation mix.
- a: NOAA electronic monitoring primarily serves data collection and compliance, so labor savings may accrue partly to regulators or observers rather than vessel operators.
- a: The frozen l uses wages and receipts from different vintages and an IPS harmonization factor, which can misstate current labor intensity.
- rho: Regulatory mandates can accelerate adoption without creating an operator-level economic return.
- rho: Systems proven on conveyor-equipped vessels may not translate to small boats or catch handled irregularly on deck.
- rho: Connectivity, corrosion, vibration, lighting, species mix, and weather can degrade field performance.
- e: The frozen n equals 10 but is an estimate derived using a broad Farming and Agriculture EBITDA margin rather than observed finfish-company profitability.
- e: NAICS establishment classification may split or combine vessels differently from a transferable enterprise.
- e: A vessel and permit can be saleable even when the operating company lacks transferable management or stable earnings.
- s5: The crew survey covers New England and the Mid-Atlantic and includes hired captains rather than owners alone.
- s5: Permit transferability and ownership rules vary substantially by fishery and jurisdiction.
- s5: Retirement may produce family succession, lease, vessel sale, permit sale, or liquidation rather than a company control transaction.
- q: No source directly observes discounted five-year retention of an implemented AI benefit for finfish operators.
- q: Imported seafood affects downstream prices but is not a like-for-like substitute for every domestic species and quality grade.
- q: Crew-share arrangements can distribute savings or added catch differently from conventional payroll businesses.
- d5: Seafood consumption combines finfish, shellfish, imports, and aquaculture and is not a direct measure of domestic wild-finfish demand.
- d5: National stock counts do not weight stocks by the revenue mix of eligible firms.
- d5: Climate-driven range shifts, closures, rebuilding plans, and quota changes can create much larger local swings than the national range.
- o: This is a structural estimate rather than an observed operator-displacement rate.
- o: Remote monitoring and decision support change operator work but do not transfer navigational and safety accountability to software.
- o: Quantity loss or substitution is reflected primarily in d5 rather than duplicated here.

## Sources
- **S1** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-23): Industry boundary for commercial catching of finfish from natural habitat and exclusions for aquaculture and seafood processing.
- **S2** — [Fishing and Hunting Workers: Occupational Outlook Handbook](https://www.bls.gov/ooh/farming-fishing-and-forestry/fishers-and-related-fishing-workers.htm) (accessed 2026-07-23): Fishing duties, captain and deckhand work, navigation technology, physical tasks, licensing, retirement replacement, and employment outlook.
- **S3** — [Electronic Technologies](https://www.fisheries.noaa.gov/national/fisheries-observers/electronic-technologies) (accessed 2026-07-23): Electronic reporting, electronic monitoring, vessel tracking, gear sensors, and AI-assisted video processing in fisheries.
- **S4** — [Developing Machine Vision to Collect More Timely Fisheries Data](https://www.fisheries.noaa.gov/feature-story/developing-machine-vision-collect-more-timely-fisheries-data) (accessed 2026-07-23): Machine-vision development for identifying and measuring commercial catch and the operational challenges of electronic monitoring.
- **S5** — [Fisheries of the United States](https://www.fisheries.noaa.gov/national/sustainable-fisheries/fisheries-united-states) (accessed 2026-07-23): Commercial landings and value, seafood consumption, import reliance, aquaculture output, regions, and leading species.
- **S6** — [Status of Stocks 2024](https://www.fisheries.noaa.gov/national/sustainable-fisheries/status-stocks-2024) (accessed 2026-07-23): Managed-stock counts, overfishing and overfished status, catch-limit compliance, rebuilding, and biological demand constraints.
- **S7** — [Building the Next Generation of U.S. Commercial Fishermen](https://www.fisheries.noaa.gov/feature-story/building-next-generation-us-commercial-fishermen) (accessed 2026-07-23): Retirement pressure, graying of the fleet, high entry costs, and succession challenges.
- **S8** — [2026 Commercial Fishing Crew Survey](https://www.fisheries.noaa.gov/new-england-mid-atlantic/socioeconomics/2026-commercial-fishing-crew-survey) (accessed 2026-07-23): Regional evidence on young entrants, crew tenure, family participation, and consideration of leaving fishing.
- **S9** — [Groundfish Limited Entry Change of Ownership and Vessel Registration](https://www.fisheries.noaa.gov/permit/groundfish-limited-entry-change-ownership-vessel-registration) (accessed 2026-07-23): One finfish permit regime's limited-entry, ownership-change, vessel-registration, leasing, and transferability rules.
