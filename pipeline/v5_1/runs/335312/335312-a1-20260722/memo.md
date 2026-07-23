# 335312 — Motor and Generator Manufacturing

*v5.1 Stage 1 research memo. Run `335312-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.54 · L 1.27 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Essential installed-base equipment and electrification create recurring custom, replacement, and rebuild demand around data-rich engineering and test workflows.
**Weakness:** Physical production, certification, and OEM price pressure limit substitution and retained savings.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly engineering, winding, assembling, testing, rebuilding on a factory basis, and supplying electric motors, power generators, and motor-generator sets to external OEM, industrial, commercial, utility, contractor, and distributor customers.
- Excluded: Automotive starting motors and alternators, turbine generator sets, nonfactory repair shops, import-only distributors, captive plants, firms outside the EBITDA band, shells, and non-control financing vehicles.
- Customer and revenue model: Quoted per-unit, program, or project sales, often configured or engineered to OEM and industrial specifications, with design, materials, testing, documentation, warranty, repair, and lifecycle support bundled under repeat accounts.
- Deviation from default lens: none

## Executive view
Motor and generator manufacturing combines broad installed-base demand with engineering, specification, planning, test, and service workflows that AI can improve. Physical winding, machining, assembly, balancing, and certification remain essential. The service lens fits custom, OEM-program, and factory-rebuild suppliers better than commodity catalog producers.

## How AI changes the work
AI can parse specifications, assist electromagnetic and mechanical design, quote jobs, substitute constrained materials, plan windings and production, analyze vibration and test curves, predict maintenance, generate compliance records, and triage field service. Skilled staff still build, wind, insulate, machine, balance, assemble, test, and release equipment.

## Value capture
Custom requirements, approvals, installed-base knowledge, downtime avoidance, reliability, and turnaround defend value. OEM tenders, annual cost-downs, material escalators, distributor power, and imports pass common gains through, making reliability and speed most defensible.

## Firm availability
The estimated population should include meaningful custom and rebuild suppliers, but transferability depends on recurring external programs, management depth, certifications, skilled labor, customer concentration, warranty history, equipment, working capital, and classification versus repair services.

## Demand durability
Motors remain central to industrial electricity use, while electrification, automation, data centers, grid investment, backup generation, efficiency upgrades, and replacement support growth. Imports, economic cycles, drive integration, and material constraints temper the outlook.

## Risks and uncertainty
Key risks are copper, electrical steel, and magnet supply; imports; efficiency-rule redesign; field failures; skilled labor; customer concentration; working capital; product mix; strategic ownership; classification ambiguity; and margin-bridge error.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2131 | — | OBSERVED | — |
| n | — | 234 | — | ESTIMATE | — |
| a | 0.16 | 0.27 | 0.4 | PROXY | S1, S2 |
| rho | 0.35 | 0.55 | 0.71 | ESTIMATE | S3, S4 |
| e | 0.28 | 0.47 | 0.65 | ESTIMATE | S2 |
| s5 | 0.1 | 0.18 | 0.29 | PROXY | S5 |
| q | 0.32 | 0.5 | 0.67 | ESTIMATE | S3, S4 |
| d5 | 0.96 | 1.1 | 1.26 | PROXY | S4, S6 |
| o | 0.92 | 0.97 | 0.995 | ESTIMATE | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.48 | 1.27 | 2.42 | ESTIMATE |
| F | 3.25 | 4.88 | 6.13 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 8.83 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupation-by-task dataset was located.
- a: Standard motors, specialty motors, generator sets, and factory rewinding have different labor and engineering profiles.
- rho: Standards and energy-use evidence establish constraints and value, not an observed implementation rate.
- rho: Smaller custom manufacturers may lack standardized data and digital machines.
- e: Eligibility depends on treating engineered-to-order and factory rebuild manufacturing as outsourced service.
- e: The frozen count is a margin-bridged ESTIMATE and may include product-only suppliers or firms outside the band.
- s5: Gallup is not industry- or size-specific and measures plans rather than completed transfers.
- s5: Some factory rebuild operations may be classified inconsistently with repair services.
- q: No representative contract or pass-through dataset was located.
- q: Retention differs between commodity catalog motors, custom units, generators, and urgent factory rebuilds.
- d5: Electricity demand is not a direct motor or generator shipment forecast.
- d5: Imports, permanent-magnet supply, efficiency-driven downsizing, variable-speed drives, and economic cycles can change domestic demand.
- o: Manufacturing may consolidate into large global operators outside the lens.
- o: Variable-speed drives and equipment integration can reduce some standalone motor demand without eliminating accountable rotating machinery.

## Sources
- **S1** — [Electrical Equipment, Appliance, and Component Manufacturing: NAICS 335](https://www.bls.gov/iag/tgs/iag335.htm) (accessed 2026-07-22): Reports 2025 broader-subsector employment including 65,350 electrical and electronic assemblers, 57,660 team assemblers, 5,790 coil winders, and 14,050 inspectors.
- **S2** — [335312 Motor and Generator Manufacturing](https://data.census.gov/profile/335312_-_Motor_and_generator_manufacturing?codeset=naics~335312&g=010XX00US) (accessed 2026-07-22): Defines the industry as electric motors, power generators, motor-generator sets, and factory armature rewinding, with relevant exclusions, and reports 398 employer establishments in 2023.
- **S3** — [Electric Motors](https://www.energy.gov/cmei/buildings/electric-motors) (accessed 2026-07-22): Documents DOE efficiency standards, test procedures, labeling, certification, and record-maintenance requirements for electric motors, including new compliance dates.
- **S4** — [Motors: Better Buildings and Better Plants](https://betterbuildingssolutioncenter.energy.gov/better-plants/motors) (accessed 2026-07-22): States motors account for about 54% of industrial electricity use in US manufacturing and emphasizes system specification, maintenance, efficiency, and reliability.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey found 22% of employer-business owners planned to sell or transfer ownership within five years, while 5% planned closure and 5% had no plan.
- **S6** — [U.S. electricity generation in 2025 hit a record, again](https://www.eia.gov/todayinenergy/detail.php?id=67284) (accessed 2026-07-22): Reports 2025 US electricity generation at 4.43 thousand TWh, up 2.8%, with demand growth in commercial, industrial, and residential sectors and further growth expected in 2026 and 2027.
