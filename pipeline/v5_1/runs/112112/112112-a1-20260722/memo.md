# 112112 — Cattle Feedlots

*v5.1 Stage 1 research memo. Run `112112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Continuous animal and feed data can improve decisions and administration within a recurring custom-feeding relationship.
**Weakness:** Only part of the NAICS population is a qualifying outsourced service, and consolidation can preserve cattle volume while eroding independent operator availability.

## Business-model lens
- Included: Independent LMM cattle feedlots that repeatedly provide custom finishing and related feeding, animal-care, recordkeeping, and marketing-support services for cattle owned by external ranchers, producers, or investors.
- Excluded: Feedlots that only own and trade their cattle, packer-captive or vertically integrated lots, cow-calf and backgrounding operations, passive facilities, hobby farms, and firms outside the EBITDA band.
- Customer and revenue model: Recurring production contracts with cattle owners, typically combining per-head or per-day yardage, feed and input charges or markups, animal-health charges, and performance reporting; cattle may be marketed to packers for the owner.
- Deviation from default lens: NAICS 112112 mixes fee-based custom feeding with principal-risk cattle ownership. The lens keeps custom-feeding operators because they provide a repeat outsourced service and excludes own-cattle-only production so one service-business screen remains coherent.

## Executive view
Independent custom feedlots have useful data and administrative workflows, but the service lens captures only part of a concentrated, asset-heavy cattle-production industry. Missing firm-count and labor-share inputs materially limit confidence.

## How AI changes the work
Likely uses include ration and intake analysis, camera and sensor alert triage, health and performance forecasting, feed procurement, pen and labor scheduling, environmental records, billing, and customer reporting. Feed delivery, animal handling, treatment, pen maintenance, manure management, repairs, and shipping remain physical.

## Value capture
Custom feeders can retain some operational gains through yardage and service margin, but transparent feed charges, customer sophistication, performance benchmarking, contract renewal, and feedlot competition share benefits with cattle owners.

## Firm availability
USDA evidence confirms custom feeding is common but not universal and varies sharply by capacity. Own-cattle operations, captive lots, partial custom activity, family structures, concentration, and missing band-count data reduce the eligible pool.

## Demand durability
Grain-finished beef requires physical feeding and live-animal custody, while the cattle cycle, high beef prices, imports, herd rebuilding, packer behavior, and concentration drive volume uncertainty. Aggregate demand may persist even as activity migrates away from independent LMM lots.

## Risks and uncertainty
The largest risks are missing l and n, dated custom-feeding incidence, cattle and feed-price volatility, customer and packer concentration, leverage, animal disease, mortality, labor, water, manure and air regulation, weather, and cyclic capacity utilization.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.08 | 0.15 | 0.24 | PROXY | S2, S3, S4 |
| rho | 0.36 | 0.54 | 0.7 | ESTIMATE | S2, S3, S4, S5 |
| e | 0.27 | 0.44 | 0.61 | PROXY | S1, S6 |
| s5 | 0.13 | 0.24 | 0.36 | PROXY | S7 |
| q | 0.31 | 0.47 | 0.64 | ESTIMATE | S6 |
| d5 | 0.9 | 1 | 1.11 | PROXY | S5, S8 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S1, S2, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 6.20 | 9.40 | 10.00 | ESTIMATE |
| D | 8.55 | 9.90 | 10.00 | ESTIMATE |

## Caveats
- a: No labor-compensation ratio is available for this industry.
- a: Public occupation evidence is not feedlot- or custom-feeding-specific.
- rho: Bounded judgment rather than an observed adoption rate.
- rho: Animal-welfare and environmental accountability constrain unattended automation.
- e: The direct custom-feeding evidence is from the 2011 Feedlot study.
- e: Feedlot, establishment, cattle owner, and operating company are not equivalent.
- e: The supplied firm count is missing and must not be inferred.
- s5: Economy-wide demographic proxy.
- s5: No denominator-based control-transfer series for independent custom feedlots.
- q: No public contract panel quantifies pass-through.
- q: Retention differs between fixed yardage, cost-plus feed, and gain- or performance-linked arrangements.
- d5: Monthly inventory is a weak five-year predictor.
- d5: Aggregate fed-cattle volume does not equal independent custom-feedlot service demand.
- o: Operator identity may shift toward larger integrated firms even if physical feeding persists.
- o: This primitive excludes labor automation already reflected in a and rho.

## Sources
- **S1** — [2022 NAICS Definition: 112112 Cattle Feedlots](https://www.census.gov/naics/?details=112&input=112&year=2022) (accessed 2026-07-22): Census defines 112112 as establishments primarily engaged in feeding cattle for fattening and separates cattle ranching and dairy production.
- **S2** — [Agricultural Workers](https://www.bls.gov/ooh/farming-fishing-and-forestry/agricultural-workers.htm) (accessed 2026-07-22): BLS describes animal farmworkers feeding, herding, weighing, loading, examining, medicating, and maintaining housing for livestock, supporting the physical-task boundary.
- **S3** — [Farmers, Ranchers, and Other Agricultural Managers](https://www.bls.gov/ooh/management/farmers-ranchers-and-other-agricultural-managers.htm) (accessed 2026-07-22): BLS describes agricultural managers as supervising workers and production while also working in physically demanding and hazardous operating environments.
- **S4** — [Animal Feeding Operations](https://www.epa.gov/npdes/animal-feeding-operations-afos) (accessed 2026-07-22): EPA defines confined animal feeding operations and explains that qualifying CAFOs are regulated under NPDES, supporting compliance and accountable-operator constraints.
- **S5** — [Cattle on Feed: June 2026](https://www.nass.usda.gov/Publications/Todays_Reports/reports/cofd0626.pdf) (accessed 2026-07-22): USDA reports 11.682 million cattle on feed in large feedlots on June 1, 2026, 102 percent of the prior year, and defines the feeding, placement, and marketing production flow.
- **S6** — [Feedlot 2011 Part I: Management Practices on U.S. Feedlots with Capacity of 1,000 or More Head](https://www.aphis.usda.gov/sites/default/files/Feed11_dr_PartI_1.pdf) (accessed 2026-07-22): USDA reports that 50.2 percent of surveyed feedlots custom fed some cattle, with custom feeding more common at larger capacities, and distinguishes cattle owned by the feedlot from cattle fed for others.
- **S7** — [2024 Chartbook on Firms by Age of Primary Owner](https://www.fedsmallbusiness.org/-/media/project/smallbizcredittenant/fedsmallbusinesssite/fedsmallbusiness/files/2024/firms-in-focus/sbcs_chartbook2024_ownerage.pdf) (accessed 2026-07-22): Federal Reserve owner-age evidence used only as a broad succession proxy for qualifying control transfers.
- **S8** — [Cattle and Beef Market Outlook](https://ers.usda.gov/topics/animal-products/cattle-beef/market-outlook) (accessed 2026-07-22): USDA ERS reports that 2026 and 2027 beef-production forecasts were lowered by less than 1 percent due to slower expected fed-cattle slaughter and provides current price and trade context.
