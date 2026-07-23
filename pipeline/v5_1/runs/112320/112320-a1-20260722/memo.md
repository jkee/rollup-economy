# 112320 — Broilers and Other Meat Type Chicken Production

*v5.1 Stage 1 research memo. Run `112320-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Repeated integrator-owned flock placements create recurring outsourced grow-out demand supported by long-run chicken consumption growth.
**Weakness:** Powerful local integrators control placements, technology requirements, inputs, benchmarking, and contract terms, sharply limiting grower capture and transferability.

## Business-model lens
- Included: U.S. lower-middle-market independent contract growers raising broilers, fryers, roasters, and other meat-type chickens for external poultry integrators, with growers providing housing, equipment, utilities, labor, and daily husbandry.
- Excluded: Integrator-owned captive farms, poultry hatcheries, egg farms, turkey and other-poultry farms, chicken processors without grow-out operations, shell landholding entities, hobby flocks, and financing vehicles without operating control.
- Customer and revenue model: Repeated flock-placement production contracts, commonly with one local integrator, paying grower fees based on delivered live weight, contract base rates, and relative flock performance while the integrator owns birds and supplies feed, veterinary services, and transportation.
- Deviation from default lens: The NAICS code includes captive integrator production and independent contract growers; the lens retains only independent growers providing repeated outsourced grow-out service to external integrators because captive farms are excluded by the fixed screen.

## Executive view
Contract broiler production is an unusually clear recurring outsourced service, but grower economics are controlled by concentrated integrators, short placement commitments, tournament pay, specialized debt-financed houses, and missing core labor and firm-count data. AI monitoring is technically credible yet likely to be captured heavily by integrators.

## How AI changes the work
AI can improve flock and behavior monitoring, environmental alerts, mortality detection, records, scheduling, maintenance planning, and integrator support. Physical house work, repairs, emergencies, welfare, and accountable husbandry remain operator-intensive, and feeding and climate controls are already automated.

## Value capture
Early adopters may earn relative-performance premiums or save utilities and labor, but tournament benchmarking, integrator ownership of birds and inputs, technology mandates, base-rate resets, and few local buyers strongly constrain retention.

## Firm availability
Near-universal production contracting supports eligibility, and grower age creates succession pressure. The missing LMM denominator, split farm entities, specialized real estate, debt, family transfers, and integrator approval make actual transferable-firm availability uncertain.

## Demand durability
USDA projects steady national broiler growth from domestic and foreign demand. Independent grower demand is more local and can fall sharply with integrator consolidation, processing-plant changes, disease, trade, or contract termination.

## Risks and uncertainty
Principal risks are missing labor and firm-count inputs, integrator concentration, tournament compensation, flock-to-flock contracts, required upgrades, specialized debt, disease and biosecurity, feed and energy costs, animal welfare, plant closure, and environmental and manure obligations.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.11 | 0.23 | 0.35 | PROXY | S2, S3, S4 |
| rho | 0.16 | 0.34 | 0.53 | PROXY | S3, S4 |
| e | 0.8 | 0.93 | 0.98 | PROXY | S1, S2 |
| s5 | 0.14 | 0.27 | 0.41 | PROXY | S4 |
| q | 0.16 | 0.32 | 0.5 | ESTIMATE | S2, S4 |
| d5 | 0.98 | 1.07 | 1.16 | PROXY | S5, S6 |
| o | 0.98 | 0.995 | 1 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 3.20 | 6.40 | 10.00 | ESTIMATE |
| D | 9.60 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No defensible industry labor-share input or occupation mix is available, so the task range cannot be tied to an observed wage base.
- a: USDA technical studies focus on monitoring feasibility and selected manual tasks rather than total farm labor, and research-house performance may not transfer to commercial conditions.
- rho: ARS evidence establishes proof of concept rather than representative commercial adoption or realized labor savings.
- rho: Integrator-specified technology upgrades can speed adoption but may also shift capital cost to growers without increasing fees.
- e: The frozen LMM firm denominator is missing, so this conditional share cannot establish the number of eligible firms.
- e: Production value under contract is not the same as the share of LMM legal firms, and farms may split land, houses, and operating activity among entities.
- s5: The available broiler grower age evidence is old and measures principal operators rather than controlling owners or succession intent.
- s5: A property transfer or new flock contract may not constitute a qualifying control transfer of a continuing eligible operating company.
- q: Contract terms and local alternatives vary by integrator, complex, house age, bird size, and region.
- q: Savings in mortality, feed, or veterinary inputs often accrue primarily to the integrator because it owns birds and supplies major inputs.
- d5: USDA projects national meat production, not demand for independent LMM grower services in a particular processing complex.
- d5: The baseline assumes no major future shocks, while disease, trade policy, feed costs, and processing-plant closure can abruptly redirect placements.
- o: This estimates persistence of an accountable grow-out operator, not survival of each independent grower or current contract.
- o: Integrator vertical integration can eliminate an outsourced grower while leaving the physical operator function inside the integrator.

## Sources
- **S1** — [2022 NAICS Definition: 112320 Broilers and Other Meat Type Chicken Production](https://www.census.gov/naics/?details=112&input=112&year=2022) (accessed 2026-07-22): Exact industry scope for raising broilers, fryers, roasters, and other meat-type chickens.
- **S2** — [Fees Paid to Growers for Raising Broiler Chickens Varied Widely in 2020](https://www.ers.usda.gov/data-products/charts-of-note/104642) (accessed 2026-07-22): Contract-production prevalence, grower and integrator responsibilities, tournament compensation, and observed payment dispersion.
- **S3** — [Detecting Broiler Chickens on Litter Floor with the YOLOv5-CBAM Deep Learning Model](https://www.ars.usda.gov/research/publications/publication/?seqNo115=401186) (accessed 2026-07-22): Manual monitoring burden, commercial-house scale, deep-learning monitoring feasibility, and measured detection performance.
- **S4** — [Financial Risks and Incomes in Contract Broiler Production](https://www.ers.usda.gov/amber-waves/2014/august/financial-risks-and-incomes-in-contract-broiler-production) (accessed 2026-07-22): Grower demographics, specialized housing and debt, contract duration, integrator responsibilities, tournament design, placement risk, and production organization.
- **S5** — [USDA Agricultural Projections to 2035](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/113817/OCE-2026-1.pdf) (accessed 2026-07-22): Official long-run broiler production growth projection and domestic and foreign demand drivers.
- **S6** — [Livestock Production Cycles Affect Long-Term Price Outlook for Cattle, Hogs, and Chickens](https://www.ers.usda.gov/amber-waves/2025/march/livestock-production-cycles-affect-long-term-price-outlook-for-cattle-hogs-and-chickens) (accessed 2026-07-22): Broiler production, consumption, export, biological-cycle, feed-efficiency, and disease outlook through 2034.
