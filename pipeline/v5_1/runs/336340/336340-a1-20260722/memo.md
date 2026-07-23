# 336340 — Motor Vehicle Brake System Manufacturing

*v5.1 Stage 1 research memo. Run `336340-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.76 · L 0.67 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Safety-mandated physical content and an aging installed fleet sustain operator-required demand.
**Weakness:** Regenerative braking pressures wear-component demand while concentrated OEM customers can appropriate productivity gains.

## Business-model lens
- Included: Independent U.S. manufacturers of motor-vehicle brake systems and components, including calipers, rotors, drums, friction assemblies, hydraulic and electromechanical brake hardware, and related tested subassemblies.
- Excluded: Captive OEM plants; vehicle assembly; repair and installation shops; pure distributors; software-only braking businesses; and firms dominated by unrelated motor-vehicle parts.
- Customer and revenue model: Repeat B2B supply to vehicle OEMs, tier-one integrators, distributors, fleets, and aftermarket channels, limited to externally serving firms plausibly in the $1-10 million normalized EBITDA band.
- Deviation from default lens: none

## Executive view
Brake-system manufacturing has durable, safety-mandated physical demand and meaningful qualification barriers. AI can improve the information layer around production, but most work is embodied and powerful customers limit commercial retention.

## How AI changes the work
Likely applications include quote preparation, drawing and specification search, APQP and quality documentation, scheduling, procurement, predictive maintenance, defect-image triage, root-cause support, and engineering simulation assistance. Physical processing, assembly, metrology, endurance testing, and accountable release remain operator-intensive.

## Value capture
Qualified processes, traceability, warranty stakes, and switching friction support some retention. OEM cost-downs, competitive rebids, and customer concentration push the other way; aftermarket brands and specialized electronic or high-performance products should retain more than commodity build-to-print work.

## Firm availability
The frozen estimate suggests a modest target universe, but eligibility is reduced by global tier ownership, captive facilities, distributors, and diversified parts businesses. Product scope and program concentration require establishment-level verification.

## Demand durability
Physical braking remains mandatory across powertrains. An aging vehicle stock supports aftermarket demand, while regenerative braking lengthens wear life and shifts content from friction components toward sensors, actuators, controls, and integrated systems.

## Risks and uncertainty
The largest uncertainties are product-mix heterogeneity, electrification-driven replacement changes, warranty and recall exposure, customer pass-through, program concentration, and the absence of six-digit task and transaction data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1702 | — | OBSERVED | — |
| n | — | 43 | — | ESTIMATE | — |
| a | 0.11 | 0.19 | 0.28 | PROXY | S1 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S1, S4 |
| e | 0.5 | 0.68 | 0.82 | ESTIMATE | — |
| s5 | 0.1 | 0.21 | 0.33 | ESTIMATE | — |
| q | 0.3 | 0.47 | 0.63 | ESTIMATE | S4 |
| d5 | 0.92 | 1 | 1.09 | PROXY | S2, S3, S4 |
| o | 0.92 | 0.98 | 1 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.26 | 0.67 | 1.30 | ESTIMATE |
| F | 1.85 | 3.16 | 4.08 | ESTIMATE |
| C | 6.00 | 9.40 | 10.00 | ESTIMATE |
| D | 8.46 | 9.80 | 10.00 | ESTIMATE |

## Caveats
- a: BLS reports four-digit motor-vehicle-parts employment, not six-digit brake manufacturing.
- a: Employment shares are not wage-weighted task shares.
- rho: Electronic-braking suppliers may implement faster than traditional friction-component shops.
- e: The frozen firm count is margin-bridged and can misclassify diversified or captive operations.
- s5: No six-digit observed transfer-rate series was found.
- q: Capture varies sharply between build-to-print OEM programs and branded aftermarket products.
- d5: Fleet age is not a direct measure of brake-component demand.
- d5: The code mixes friction, hydraulic, and electronic products with different trajectories.
- o: Ordinary demand effects are assigned to d5 rather than double-counted here.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 336300](https://www.bls.gov/oes/2023/may/naics4_336300.htm) (accessed 2026-07-22): Broader motor-vehicle-parts employment totals 557,020; production occupations are 351,330 (63.07%) and assemblers/fabricators 169,960 (30.51%), grounding the task-mix proxy.
- **S2** — [Table 1-26: Average Age of Automobiles and Trucks in Operation in the United States](https://www.bts.gov/archive/publications/national_transportation_statistics/table_01_26) (accessed 2026-07-22): Average age of all light vehicles increased from 8.4 years in 1995 to 11.4 years in 2014, supporting an aging installed-base proxy.
- **S3** — [Alternative Fuels Data Center: Maintenance and Safety of Electric Vehicles](https://afdc.energy.gov/vehicles/electric-maintenance) (accessed 2026-07-22): DOE states electric-vehicle brake systems generally last longer than conventional-vehicle systems because regenerative braking reduces friction-brake use.
- **S4** — [Safety Recall 24V-589](https://static.nhtsa.gov/odi/rcl/2024/RCRIT-24V589-9711.pdf) (accessed 2026-07-22): A 2024 Cadillac LYRIQ recall describes false ABS activation continuing to release service-brake pressure, illustrating safety criticality and physical/electronic system integration.
