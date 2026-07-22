# 326140 — Polystyrene Foam Product Manufacturing

*v5.1 Stage 1 research memo. Run `326140-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.10 · L 0.64 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable insulation and engineered protective-packaging demand supports AI-enabled quality, uptime, and planning improvements.
**Weakness:** Single-use EPS bans and substitution make product mix a first-order risk, while much plant labor remains physical.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers repeatedly supplying expanded or extruded polystyrene foam insulation, protective packaging, cold-chain containers, food-service items where lawful, and other molded or cut foam products to external customers.
- Excluded: Captive foam-molding units, distributors and fabricators without primary foam manufacturing, non-polystyrene foam makers, resin producers, shell entities, and non-control financing vehicles.
- Customer and revenue model: Repeat B2B product sales under purchase orders, project quotes, distributor arrangements, and supply agreements, priced by unit, board, volume, weight, or run; the mix spans commodity foodware and insulation through custom protective packaging and molded components.
- Deviation from default lens: none

## Executive view
Polystyrene foam manufacturing has repeat external demand and useful AI opportunities around quality, maintenance, design, planning, and administration, but the industry combines relatively durable insulation and protective packaging with single-use products under active regulatory pressure. Product mix is therefore decisive.

## How AI changes the work
DOE identifies automated visual quality control, characterization, operations optimization, and predictive maintenance as feasible manufacturing uses. Foam producers can also use AI for package design, nesting, quoting, forecasting, scheduling, and documentation. Savings are constrained where work is physical or requires robotics, and by legacy controls, limited plant data, geometry changes, fire and thermal standards, and human quality accountability.

## Value capture
Custom tooling, freight radius, protective-performance design, and cold-chain qualification can create switching costs. Commodity boards, coolers, cups, trays, and standard packaging are more price-sensitive, and resin or freight escalators reveal cost changes. Retention is therefore moderate and highly dependent on product differentiation.

## Firm availability
Most independent manufacturers with repeat external customers fit the lens, but candidates need product-level diligence. A business concentrated in prohibited foodware may be economically or operationally nontransferable even if its NAICS code fits. Succession and consolidation create sale opportunities, while closures and product-line exits do not count as transfers.

## Demand durability
Broad plastics output and construction-linked insulation provide support, but Washington and Oregon already prohibit specified EPS food-service and loose-fill items, and California requires escalating recycling performance for EPS foodware. These measures do not ban insulation or most protective packaging, yet they demonstrate real substitution and regulatory risk. Stable overall quantity is plausible only if durable segments offset single-use erosion.

## Risks and uncertainty
Six-digit occupation and end-market data are missing. The same code covers businesses with very different regulatory exposure, pricing power, automation, freight economics, and capex. Material substitution, fire and building codes, resin volatility, recycling mandates, customer concentration, energy cost, and bulky-product logistics can overwhelm AI savings. A foodware-heavy plant could be a poor transfer candidate despite good operating improvement potential.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1874 | — | OBSERVED | — |
| n | — | 113 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.3 | PROXY | S1, S2 |
| rho | 0.26 | 0.43 | 0.61 | ESTIMATE | S2 |
| e | 0.58 | 0.73 | 0.85 | ESTIMATE | S4, S5 |
| s5 | 0.13 | 0.22 | 0.35 | ESTIMATE | — |
| q | 0.29 | 0.48 | 0.66 | ESTIMATE | — |
| d5 | 0.81 | 0.97 | 1.13 | PROXY | S3, S4, S5, S6 |
| o | 0.91 | 0.97 | 1 | ESTIMATE | S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.23 | 0.64 | 1.37 | ESTIMATE |
| F | 3.62 | 4.75 | 5.70 | ESTIMATE |
| C | 5.80 | 9.60 | 10.00 | ESTIMATE |
| D | 7.37 | 9.41 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is four-digit NAICS 326100 rather than 326140.
- a: Task shares are inferred rather than observed.
- a: Insulation board, custom protective packaging, and foodware plants have materially different occupation mixes.
- rho: No five-year adoption measure specific to polystyrene foam manufacturing was located.
- rho: Many apparent AI opportunities require conveyors, robots, or tooling changes, not software alone.
- e: Eligibility is estimated and the frozen firm count is margin-bridged.
- e: Public NAICS records often do not reveal the split between insulation, protective packaging, cold chain, foodware, and converting.
- s5: No six-digit transfer-rate or owner-age data was found.
- s5: Public transaction coverage is biased toward larger strategic acquisitions.
- q: Commercial terms were not observed.
- q: Retention varies sharply between commodity foodware or board and engineered protective packaging or qualified cold-chain products.
- d5: BLS data is four-digit, not 326140.
- d5: State bans cover selected products and do not prohibit all polystyrene foam.
- d5: The industry product mix is unknown, so regulatory effects cannot be precisely weighted.
- o: No direct operator-requirement measure exists.
- o: Care is needed not to double-count regulatory volume loss already included in d5.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 326100 Plastics Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-22): Broad plastics-product occupational and wage mix, including total employment and production, management, business, extrusion, molding, assembly, packing, maintenance, and material-moving roles.
- **S2** — [AI for Energy: Opportunities for a Modern Grid and Clean Energy Economy](https://www.energy.gov/sites/default/files/2024-04/AI%20EO%20Report%20Section%205.2g%28i%29_043024.pdf) (accessed 2026-07-22): DOE describes AI manufacturing uses including automated visual quality control, advanced characterization, operations optimization, predictive maintenance with IoT sensors, and material sorting.
- **S3** — [Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects NAICS 326100 real output from $190.7 billion in 2024 to $212.4 billion in 2034 at 1.1% annually; construction employment grows 4.4%, building construction 4.6%, and insulation-contractor employment 2.5%.
- **S4** — [Expanded Polystyrene Ban - Washington State Department of Ecology](https://ecology.wa.gov/waste-toxics/reducing-recycling-waste/plastics/2021-plastic-pollution-laws/expanded-polystyrene-ban) (accessed 2026-07-22): Washington bans EPS packing peanuts from June 2023 and portable coolers and food-service products including containers, plates, bowls, clamshells, trays, and cups from June 2024, while listing exemptions for certain protective and raw-food packaging.
- **S5** — [Foodware Containers and Polystyrene Foam - Oregon Department of Environmental Quality](https://www.oregon.gov/deq/mm/production/Pages/polystyrene.aspx) (accessed 2026-07-22): Effective January 1, 2025, Oregon prohibits food vendors from using polystyrene foam containers for prepared food and prohibits sales of foam containers and packing peanuts, while exempting most protective shipping material.
- **S6** — [California SB 54: Solid Waste, Packaging, and Plastic Food Service Ware](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202120220SB54) (accessed 2026-07-22): California law requires demonstrated EPS food-service recycling rates of at least 25% from 2025, 30% from 2028, 50% from 2030, and 65% from 2032 for continued sale or distribution.
