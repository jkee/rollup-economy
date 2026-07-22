# 493130 — Farm Product Warehousing and Storage

*v5.1 Stage 1 research memo. Run `493130-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.65 · L 0.00 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Stable physical crop handling combined with proven automation of weighing, sampling, records, monitoring, and routing creates a bounded labor-efficiency opportunity.
**Weakness:** The frozen dataset estimates zero LMM-band firms, consistent with a market fragmented by small sites but controlled heavily by cooperatives and strategic grain networks rather than transferable service companies.

## Business-model lens
- Included: Independent U.S. operators of nonrefrigerated bulk farm-product storage facilities, principally grain elevators, that repeatedly provide storage, handling, grading, conditioning, inventory-record, and loadout services to external farm, trading, processing, or government customers.
- Excluded: Refrigerated storage; on-farm/captive storage; grain elevators primarily engaged in merchant wholesaling; processing plants and oilseed crushers whose storage is incidental; cooperative or strategic-network facilities that are not realistically transferable control investments; and operations outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: Customers typically pay posted or negotiated per-bushel receiving, storage-time, conditioning, and loadout charges, sometimes alongside grain-marketing services. Revenue repeats with crop cycles and inventory duration but is seasonal and commodity-volume-sensitive.
- Deviation from default lens: none

## Executive view
Farm-product storage is a physical, safety-critical service with recurring seasonal demand and real opportunities to digitize scale-house, inventory, monitoring, and planning work. The larger constraint is firm availability: cooperative and strategic ownership is prominent, while the frozen margin bridge estimates no firms in the target EBITDA band.

## How AI changes the work
AI can improve ticket and document processing, inventory reconciliation, crop-flow forecasting, scheduling, customer communication, predictive maintenance, and exception triage around established sensors and controls. It is much less able to replace equipment repair, housekeeping, grain-condition interventions, bin-entry safeguards, or physical receiving and loadout, and existing automation must be excluded from the incremental opportunity.

## Value capture
Per-bushel and time-based tariffs allow an operator to keep some labor, error, and throughput benefits without an immediate contractual giveback. Public rate visibility, local competition, grain-bid economics, annual repricing, and producers' option to build or use on-farm storage should return a meaningful share to customers over five years.

## Firm availability
Independent family elevators do sell, including a documented four-elevator transaction in 2024, but the eligible universe is obscured by cooperatives, large merchant networks, multi-site branches, and mixed trading/storage models. A firm-level ownership and revenue-quality census is essential before treating apparent facilities as acquisition candidates.

## Demand durability
USDA's crop baseline implies modest growth in the dominant corn, soybean, and wheat volumes through 2030/31, while national off-farm capacity was essentially stable in 2024. Storage-days and regional demand remain volatile, but the physical need to preserve and move bulk crops should persist, and licensed/safe operation cannot be replaced by standalone software.

## Risks and uncertainty
The key risks are an empty or nearly empty target-size buyer universe, classification leakage between storage and grain wholesaling, cooperative or strategic acquirers outcompeting financial buyers, weather and trade volatility, farmer investment in on-farm storage, legacy-plant integration costs, cybersecurity, and severe safety consequences from control failures. Broad warehousing occupation data may substantially overstate the task mix of grain elevators.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.565 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.16 | 0.23 | 0.3 | PROXY | S2, S3, S4, S5 |
| rho | 0.4 | 0.52 | 0.65 | PROXY | S3, S4, S5 |
| e | 0.25 | 0.4 | 0.55 | ESTIMATE | S1, S8 |
| s5 | 0.08 | 0.15 | 0.24 | PROXY | S9 |
| q | 0.5 | 0.63 | 0.75 | PROXY | S10, S11 |
| d5 | 0.93 | 1.02 | 1.09 | PROXY | S6, S7 |
| o | 0.92 | 0.97 | 0.99 | PROXY | S4, S5, S12 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.45 | 2.70 | 4.41 | PROXY |
| F | 0.00 | 0.00 | 0.00 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | PROXY |
| D | 8.56 | 9.89 | 10.00 | PROXY |

## Caveats
- a: BLS publishes the cited occupation mix at NAICS 493100, not 493130.
- a: The fixed labor ratio uses 2024 wages over 2022 receipts and a cross-code IPS harmonization; the vintage mismatch may distort the economic weight attached downstream.
- a: Evidence demonstrates technical automation capability but does not measure remaining task hours or wages at independent LMM elevators.
- rho: Observed deployments are not a representative adoption survey.
- rho: Some cited automation is conventional controls rather than AI, so the estimate only credits AI where it improves decisions, document handling, forecasting, or exception management on top of those controls.
- rho: Safety-critical changes can require engineering and regulatory review beyond ordinary software deployment.
- e: No source measures eligibility for the exact LMM service-firm lens.
- e: Cooperative statistics cover all agricultural cooperative types and are not a 493130 ownership census.
- e: The frozen n=0 is an ESTIMATE derived from size-class counts and a transportation-sector margin bridge, so it may miss firms whose accounting revenue or margins do not align with the bridge.
- s5: One announced deal cannot establish frequency.
- s5: The buyer in the cited deal was a farmer-owned cooperative; future transfers to such buyers may be strategically attractive but do not establish an institutional roll-up exit.
- s5: Asset sales, branch sales, internal cooperative combinations, and transfers of merchant businesses may not qualify under the lens.
- q: Government-contract policy and Iowa licensing rules are not a national sample of private commercial contracts.
- q: Grain elevators may bundle storage economics into commodity bids, obscuring pass-through.
- q: The estimate excludes volume effects, which belong in demand primitives.
- d5: Crop production is not storage bushel-days and includes grain that never uses independent warehouses.
- d5: USDA baseline projections assume no major domestic or external shocks and were completed in October 2024.
- d5: Climate, trade, biofuel policy, crop mix, and rail/export flows can shift regional elevator demand materially even when national production is stable.
- o: Accountable operator does not necessarily mean full-time staff at every site; remote multi-site supervision could reduce local headcount without eliminating the operator.
- o: USWA licensing is voluntary, while state licensing regimes vary.
- o: On-farm storage is outside the lens and can substitute for outsourced service.

## Sources
- **S1** — [2022 NAICS Definition: 493130 Farm Product Warehousing and Storage](https://www.census.gov/naics/?details=49313&input=49313&year=2022) (accessed 2026-07-22): Defines the industry as nonrefrigerated bulk farm-product warehousing and storage, including grain elevators primarily engaged in storage.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 493100](https://www.bls.gov/oes/2023/may/naics4_493100.htm) (accessed 2026-07-22): Provides the broad warehousing occupation mix and wages used as a proxy for the physical, clerical, and managerial task structure.
- **S3** — [Grain Handling Automation and Controls](https://extension.okstate.edu/fact-sheets/grain-handling-automation-and-controls) (accessed 2026-07-22): Describes automated grain weighing, robotic sampling, bin routing, electronic tickets, moisture data, inventory traceability, and temperature monitoring in commercial facilities.
- **S4** — [Automated Weight Monitoring Systems](https://www.ams.usda.gov/resources/automated-weight-monitoring-systems) (accessed 2026-07-22): Documents approved export-elevator automation for flow paths, weight records, alarms, shutdowns, scale checks, smaller inspection teams, and safer monitoring.
- **S5** — [29 CFR 1910.272: Grain Handling Facilities](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.272) (accessed 2026-07-22): Establishes operator duties for emergency plans, training, permits, bin entry, housekeeping, preventive maintenance, and elevator safety controls.
- **S6** — [Grain Stocks, January 2025](https://www.nass.usda.gov/Publications/Todays_Reports/reports/grst0125.pdf) (accessed 2026-07-22): Reports 11.8 billion bushels of U.S. off-farm commercial storage capacity and 7,922 facilities on December 1, 2024, versus 13.6 billion bushels of on-farm capacity.
- **S7** — [USDA Agricultural Projections to 2034](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/110966/OCE-2025-1.pdf) (accessed 2026-07-22): Projects 2025/26-to-2030/31 production changes for corn, soybeans, wheat, and other major storable crops used to proxy physical storage demand.
- **S8** — [Agricultural Cooperative Statistics 2023](https://www.rd.usda.gov/media/file/download/sr87-agriculturalcooperativestatistics-2023-unpublishedreport.pdf) (accessed 2026-07-22): Reports 9,531 agricultural cooperative locations in 2023, 7,884 branch and other locations, and concentration of activity and assets among large cooperatives; also profiles grain-marketing cooperatives.
- **S9** — [The Equity Acquires Littlejohn Grain, Inc](https://www.theequity.com/news/littlejohnacquistion) (accessed 2026-07-22): Documents a 2024 control transfer of a 101-year-old fifth-generation family grain company and four grain elevators to a farmer-owned cooperative.
- **S10** — [USDA Announces Storage and Handling Rate Policy Changes under the Uniform Grain and Rice Storage Agreement](https://www.ams.usda.gov/content/usda-announces-storage-and-handling-rate-policy-changes-under-uniform-grain-and-rice) (accessed 2026-07-22): States that CCC accepts handling and storage rates from warehouse operators' public tariffs or commercial statements of charges and caps specified handling charges.
- **S11** — [Iowa Warehouse Licensing Information](https://iowaagriculture.gov/grain-warehouse-bureau/iowa-warehouse-licensing-information) (accessed 2026-07-22): Requires licensed warehouse operators to declare depositor handling and storage charges in a tariff and maintain capacity-linked net worth.
- **S12** — [United States Warehouse Act](https://www.ams.usda.gov/rules-regulations/uswa) (accessed 2026-07-22): Explains federal licensing of agricultural warehouse operators and the obligation of licensees to meet USDA standards, rules, and fees.
