# 336350 — Motor Vehicle Transmission and Power Train Parts Manufacturing

*v5.1 Stage 1 research memo. Run `336350-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.71 · L 0.58 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A relatively broad firm base and durable demand for precision driveline hardware support continued operator need.
**Weakness:** Electrification can structurally reduce conventional transmission content faster than AI productivity or aftermarket demand can compensate.

## Business-model lens
- Included: Independent U.S. manufacturers of transmissions, clutches, torque converters, gears, differentials, axles, drive shafts, transfer cases, and other motor-vehicle power-train parts or tested subassemblies.
- Excluded: Captive OEM operations; complete-vehicle assembly; engine manufacturing outside this code; repair shops; pure distributors; software-only businesses; and firms dominated by unrelated parts.
- Customer and revenue model: Repeat B2B supply to vehicle OEMs, tier-one integrators, rebuilders, distributors, fleets, and aftermarket customers, screened for external-customer firms plausibly producing $1-10 million of normalized EBITDA.
- Deviation from default lens: none

## Executive view
Power-train manufacturing offers a sizable independent-firm universe and process-heavy operating work, but its central investment issue is product-specific electrification exposure. AI can improve the information layer without transforming most factory labor, and customer leverage constrains capture.

## How AI changes the work
Likely applications include RFQ and drawing review, process-plan drafting, CNC support, quality-document preparation, scheduling, procurement, predictive maintenance, defect-image triage, root-cause analysis, and engineering knowledge retrieval. Precision machining, heat treatment, assembly, balancing, metrology, durability testing, and release remain embodied and safety-sensitive.

## Value capture
Difficult tolerances, validated processes, tooling, and switching friction support some retention. OEM annual cost-downs, platform rebids, excess legacy capacity, and concentrated customers push savings outward; specialty aftermarket, defense, off-highway, and EV-compatible niches may retain more.

## Firm availability
The frozen estimate of 123 firms suggests meaningful breadth, but eligibility depends on true manufacturing activity, independence, size, transferability, and product mix. Legacy ICE revenue can turn an apparent target into a runoff asset.

## Demand durability
The aggregate current basket faces real five-year pressure as BEVs simplify conventional transmissions and eliminate some engine-linked parts. Hybrids, slow fleet turnover, aftermarket needs, commercial vehicles, and continued demand for gears, axles, shafts, housings, differentials, and reduction drives prevent wholesale disappearance.

## Risks and uncertainty
The dominant uncertainties are candidate-level powertrain mix, platform timing, policy-sensitive EV adoption, stranded tooling, customer concentration, warranty exposure, environmental liabilities, and lack of six-digit task and transaction data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1577 | — | OBSERVED | — |
| n | — | 123 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.27 | PROXY | S1 |
| rho | 0.34 | 0.51 | 0.67 | ESTIMATE | S1 |
| e | 0.52 | 0.7 | 0.84 | ESTIMATE | — |
| s5 | 0.11 | 0.23 | 0.35 | ESTIMATE | — |
| q | 0.29 | 0.46 | 0.62 | ESTIMATE | — |
| d5 | 0.7 | 0.85 | 1 | PROXY | S2, S3, S4 |
| o | 0.88 | 0.96 | 1 | ESTIMATE | S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.58 | 1.14 | ESTIMATE |
| F | 3.35 | 4.88 | 5.82 | ESTIMATE |
| C | 5.80 | 9.20 | 10.00 | ESTIMATE |
| D | 6.16 | 8.16 | 10.00 | ESTIMATE |

## Caveats
- a: Four-digit occupation shares are not six-digit wage-weighted task shares.
- a: The current level of automation is not separately measured.
- rho: Large electrified-drivetrain suppliers likely adopt faster than the screened population.
- e: The frozen count is margin-bridged and likely includes heterogeneous products and ownership structures.
- s5: No observed six-digit transfer-rate source was available.
- q: Aftermarket and low-volume specialty products can retain substantially more than high-volume build-to-print programs.
- d5: EIA projections are scenario-dependent and policy-sensitive.
- d5: The NAICS basket combines products with sharply different electrification exposure.
- o: Electrification-driven quantity loss is captured in d5 and is not repeated here.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 336300](https://www.bls.gov/oes/2023/may/naics4_336300.htm) (accessed 2026-07-22): Broader motor-vehicle-parts employment totals 557,020; production occupations are 63.07%, assemblers/fabricators 30.51%, inspectors/testers 4.26%, multiple-machine-tool operators 2.32%, and CNC operators/programmers 2.07%.
- **S2** — [Annual Energy Outlook 2026 Narrative](https://www.eia.gov/outlooks/aeo/narrative/index.php) (accessed 2026-07-22): EIA reports battery-electric vehicles reach 50% of light-duty sales by 2032 in most cases, while reaching 46% of on-road stock takes an additional 28 years, supporting rapid sales-mix but slow fleet-turnover assumptions.
- **S3** — [Alternative Fuels Data Center: Maintenance and Safety of Electric Vehicles](https://afdc.energy.gov/vehicles/electric-maintenance) (accessed 2026-07-22): DOE states all-electric vehicles require less maintenance because they have fewer fluids and far fewer moving parts than conventional fuel-engine vehicles.
- **S4** — [Vehicle Technologies Office Electrification 2023 Annual Progress Report](https://www.energy.gov/sites/default/files/2024-11/VTO_2023_APR_ELECTRIFICATION%20REPORT_compliant_.pdf) (accessed 2026-07-22): DOE describes an EV powertrain as including the battery, power-electronic system, electric motor, transmission, drive shafts, and wheels, supporting continued but changed physical driveline content.
