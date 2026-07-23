# 114112 — Shellfish Fishing

*v5.1 Stage 1 research memo. Run `114112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.03 · L 0.00 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High operator necessity and durable high-value shellfish demand preserve the operating role even as AI improves monitoring and administration.
**Weakness:** The frozen dataset identifies no LMM firms, and commodity-catching businesses rarely satisfy the recurring outsourced-service lens.

## Business-model lens
- Included: U.S. lower-middle-market operating firms that control commercial vessels, fishing permits, crews, and recurring wild-capture shellfish harvesting for sales to external dealers, processors, auctions, or other wholesale buyers.
- Excluded: Shellfish aquaculture, seafood processing and distribution, recreational or charter fishing, passive permit or vessel lessors, captive fleets, shells, and non-control financing vehicles.
- Customer and revenue model: Operators earn predominantly variable ex-vessel revenue from repeated landings of crab, lobster, shrimp, scallops, and other wild shellfish; dealers or auctions typically pay by landed weight, species, grade, and prevailing dockside price rather than under a recurring service fee.
- Deviation from default lens: none

## Executive view
Shellfish fishing has narrow but real AI opportunities in monitoring, documentation, species measurement, and trip planning. The operating core remains physical and safety-critical, while the fixed roll-up lens fits poorly because operators sell commodity catch rather than a recurring outsourced service and the injected dataset finds no LMM-band firms.

## How AI changes the work
Computer vision can reduce video-review effort and help identify, count, and measure catch; language and forecasting tools can assist logbooks, compliance, maintenance, weather synthesis, and trip planning. They do not remove the need to operate vessels, set and haul gear, sort and ice catch, repair equipment, or make safety judgments at sea.

## Value capture
Operators can keep some savings through lower shore-side review and administrative labor, fewer reporting errors, and better vessel utilization. Retention is limited by commodity dockside pricing, dealer bargaining, competitive fishing effort, imports, aquaculture alternatives, crew-share economics, and quota constraints.

## Firm availability
Availability is the central problem. The frozen LMM count is zero, most workers are self-employed or in small crews, and the few scaled fleets may not meet the recurring-service lens. Retiring owners can transfer vessels and permits, but many exits may be asset sales rather than transfers of a qualifying operating company.

## Demand durability
Consumer demand for shellfish is durable and several shellfish groups are among the highest-value U.S. catches. Quantity is nevertheless governed as much by biological supply, quotas, climate, and species geography as by end-market appetite, producing a flat central outlook with wide downside and upside cases.

## Risks and uncertainty
The NAICS category spans fisheries with very different gear, vessel scale, stocks, regions, rules, prices, and climate exposure. Evidence on AI task hours, adoption economics, firm EBITDA, common ownership, and control transfers is sparse. A roll-up thesis fails if scaled operators are absent, repeat buyer relationships do not satisfy the service lens, or stock and quota pressure overwhelms modest productivity gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2556 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.08 | 0.18 | 0.32 | PROXY | S1, S2, S3 |
| rho | 0.2 | 0.4 | 0.6 | ESTIMATE | S2, S3 |
| e | 0.01 | 0.05 | 0.15 | ESTIMATE | S1, S4 |
| s5 | 0.08 | 0.18 | 0.3 | ESTIMATE | S1 |
| q | 0.28 | 0.48 | 0.68 | ESTIMATE | S4, S6 |
| d5 | 0.84 | 0.99 | 1.14 | ESTIMATE | S4, S5, S6 |
| o | 0.97 | 0.99 | 1 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.16 | 0.74 | 1.96 | ESTIMATE |
| F | 0.00 | 0.00 | 0.00 | ESTIMATE |
| C | 5.60 | 9.60 | 10.00 | ESTIMATE |
| D | 8.15 | 9.80 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source covers fishing and hunting workers, not only shellfish vessels.
- a: NOAA describes technical capabilities and pilots, not a measured wage-weighted automation share.
- a: Exposure varies sharply between one- or two-person trap boats and larger dredge or trawl vessels.
- rho: The estimate excludes savings already embedded in GPS, sonar, radar, mechanized hauling, and existing electronic reporting.
- rho: Regulator approval may lag technical feasibility where AI affects compliance evidence or protected-species monitoring.
- e: The injected LMM firm-count input is zero, so even a nonzero eligibility share does not imply an available target count.
- e: BLS reports that 57 percent of the broader fishing-and-hunting occupation is self-employed, but that is a worker statistic rather than a firm-size distribution.
- e: Repeated commodity sales are not necessarily a recurring outsourced service under the fixed lens.
- s5: The BLS retirement evidence is for occupational openings, not qualifying control transfers.
- s5: Permit transferability and fleet consolidation rules differ by fishery and jurisdiction.
- s5: With the frozen LMM firm count at zero, this probability has no practical target-count effect unless the size data are materially incomplete.
- q: Price formation differs across auctions, dealer relationships, cooperatives, and vertically integrated fleets.
- q: Crew-share arrangements may cause labor savings and catch-productivity gains to be divided differently from salaried-workforce savings.
- q: This estimate excludes catch-volume effects, which belong in demand durability.
- d5: National seafood totals combine finfish, shellfish, wild capture, aquaculture, and imports.
- d5: Crab, lobster, shrimp, scallop, clam, and oyster fisheries can move in opposite directions.
- d5: The range is demand for the current service basket at constant price and quality, not nominal dockside revenue.
- o: Remote monitoring and autonomous navigation may reduce crew requirements without removing the accountable operator.
- o: Aquaculture substitution reduces demand in d5 rather than this operator-required share.

## Sources
- **S1** — [Fishing and Hunting Workers](https://www.bls.gov/ooh/farming-fishing-and-forestry/fishers-and-related-fishing-workers.htm) (accessed 2026-07-22): Typical fishing duties, small-crew shellfish methods, physical and hazardous work, self-employment share, owner-captain structure, permit requirements, retirement-related openings, and employment outlook.
- **S2** — [Electronic Monitoring](https://www.fisheries.noaa.gov/national/fisheries-observers/electronic-monitoring) (accessed 2026-07-22): NOAA use and development of computer vision and machine learning for species identification, catch measurement, gear enumeration, fishing-activity detection, and lower-cost or faster monitoring review.
- **S3** — [Developing Machine Vision to Collect More Timely Fisheries Data](https://www.fisheries.noaa.gov/feature-story/developing-machine-vision-collect-more-timely-fisheries-data) (accessed 2026-07-22): Potential for machine vision to automate at-sea image analysis, reduce manual onshore video processing, and accelerate fisheries data.
- **S4** — [Fisheries of the United States](https://www.fisheries.noaa.gov/national/sustainable-fisheries/fisheries-united-states) (accessed 2026-07-22): 2023 commercial landings context, leading shellfish species by catch value, the importance of sea scallops to the top-value port, and competing aquaculture production.
- **S5** — [Status of Stocks 2024](https://www.fisheries.noaa.gov/national/sustainable-fisheries/status-stocks-2024) (accessed 2026-07-22): Stock and harvest-rate regulation context, including biological, climate, habitat, pollution, and disease risks and a shellfish example added to the overfishing list.
- **S6** — [Commercial Fisheries Landings](https://www.fisheries.noaa.gov/national/sustainable-fisheries/commercial-fisheries-landings) (accessed 2026-07-22): How U.S. wild fish and shellfish landings and ex-vessel values are measured through dealer reports, trip tickets, logbooks, interviews, and species-level databases.
