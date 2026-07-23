# 336310 — Motor Vehicle Gasoline Engine and Engine Parts Manufacturing

*v5.1 Stage 1 research memo. Run `336310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.15 · L 0.46 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Large installed ICE fleet supporting repeat OEM and replacement demand.
**Weakness:** Structural powertrain substitution and low information-work share.

## Business-model lens
- Included: Independent LMM manufacturers of gasoline engines and engine parts serving repeat external OEM, aftermarket, remanufacturing, and distributor customers.
- Excluded: Captive OEM plants, distributors without manufacturing, repair shops, shell brands, and financing vehicles.
- Customer and revenue model: Repeat per-unit or per-lot sales under OEM supply programs, aftermarket replenishment, and standing purchase orders.
- Deviation from default lens: none

## Executive view
A physically durable but structurally declining ICE supplier niche: AI mainly improves overhead workflows, while electrification reduces the current product basket.

## How AI changes the work
AI assists quoting, planning, procurement, engineering search, quality records, and customer support; production remains embodied.

## Value capture
OEM procurement practices reclaim much of the benefit, with better retention in differentiated aftermarket products.

## Firm availability
Most independents fit repeat supply, but only 37 estimated target firms exist and transfer data are unobserved.

## Demand durability
The installed ICE fleet and hybrids sustain near-term demand, while battery-electric adoption removes engines and many parts.

## Risks and uncertainty
Electrification speed, OEM concentration, warranty exposure, tariffs, tooling obsolescence, and policy shifts dominate uncertainty.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1239 | — | OBSERVED | — |
| n | — | 37 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S1 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S1 |
| e | 0.52 | 0.69 | 0.82 | ESTIMATE | — |
| s5 | 0.11 | 0.22 | 0.34 | ESTIMATE | — |
| q | 0.32 | 0.49 | 0.66 | ESTIMATE | — |
| d5 | 0.58 | 0.76 | 0.95 | PROXY | S2, S3, S4 |
| o | 0.88 | 0.96 | 0.99 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.46 | 0.94 | ESTIMATE |
| F | 1.83 | 3.04 | 3.90 | ESTIMATE |
| C | 6.40 | 9.80 | 10.00 | ESTIMATE |
| D | 5.10 | 7.30 | 9.40 | ESTIMATE |

## Caveats
- a: No six-digit task mix was found.
- a: The frozen labor ratio mixes 2024 wages and 2022 receipts.
- rho: No representative LMM deployment panel exists.
- e: The assigned 37-firm count is margin-bridged, not observed.
- s5: Product-line and plant asset sales are not necessarily control transfers.
- q: Contract terms vary sharply between OEM and branded aftermarket products.
- d5: EV-sales projections are not direct six-digit shipment forecasts.
- d5: Policy is subject to revision.
- o: Volume elimination belongs in d5; o applies only to remaining demand.

## Sources
- **S1** — [BLS May 2023 OEWS: Motor Vehicle Parts Manufacturing](https://www.bls.gov/oes/2023/may/naics4_336300.htm) (accessed 2026-07-22): Reports 557,020 jobs, including 23.77% miscellaneous assemblers, 18.41% metal workers, and 4.47% engine and machine assemblers.
- **S2** — [EIA Annual Energy Outlook: IRA Issues in Focus](https://www.eia.gov/outlooks/aeo/IIF_IRA/) (accessed 2026-07-22): Projects EVs at 15% of 2030 light-duty sales in the reference case, with 12% and nearly 17% in alternative cases.
- **S3** — [DOE Alternative Fuels Data Center: EV Maintenance and Safety](https://afdc.energy.gov/vehicles/electric-maintenance) (accessed 2026-07-22): States all-electric vehicles have fewer moving parts and fluids and require less maintenance, while hybrids retain internal-combustion engines.
- **S4** — [EPA Greenhouse Gas Regulations for Passenger Cars and Trucks](https://www.epa.gov/regulations-emissions-vehicles-and-engines/regulations-greenhouse-gas-emissions-passenger-cars-and) (accessed 2026-07-22): Describes standards phasing in over model years 2027-2032 that leverage advances in clean vehicle technology.
