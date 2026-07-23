# 336413 — Other Aircraft Parts and Auxiliary Equipment Manufacturing

*v5.1 Stage 1 research memo. Run `336413-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.46 · L 1.72 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Qualification and traceability create sticky repeat revenue around growing fleet and spares demand.
**Weakness:** Certification accountability and concentrated OEM programs constrain implementation and transferability.

## Business-model lens
- Included: Independent LMM manufacturers and approved suppliers of aircraft parts, subassemblies, auxiliary equipment, modification and replacement articles, and prototypes sold repeatedly to external OEMs, airlines, maintenance organizations, defense customers, or distributors.
- Excluded: Aircraft engines and fluid-power subassemblies classified elsewhere, captive plants, pure distributors, maintenance-only firms, shells, and firms outside the EBITDA band.
- Customer and revenue model: Repeat qualified B2B program, spares, replacement, and prototype-to-production revenue supported by engineering, configuration control, inspection, traceability, certification, and customer quality systems.
- Deviation from default lens: none

## Executive view
Aircraft parts combine high labor intensity, dense engineering and quality documentation, strong qualification barriers, and favorable fleet demand. AI can improve knowledge workflows, but certification and traceability constrain autonomous implementation.

## How AI changes the work
Likely uses include requirements and drawing review, quote preparation, engineering search, configuration documentation, inspection-data analysis, nonconformance support, scheduling, procurement, and customer quality responses. Machining, forming, assembly, NDT, inspection execution, and release remain physical and accountable.

## Value capture
Qualification, traceability, revalidation expense, program knowledge, and spares urgency support retention. OEM cost-downs, long-term agreements, open-book economics, and competitive sourcing still share benefits.

## Firm availability
Most independent qualified manufacturers fit repeat external supply, but approvals, program concentration, customer consent, export controls, quality history, and strategic ownership materially shrink transferable supply.

## Demand durability
Fleet expansion, aging-aircraft maintenance, defense programs, modifications, and OEM backlogs support parts demand. Program cancellations, OEM production interruptions, airline cycles, and customer concentration remain material.

## Risks and uncertainty
Certification, product liability, quality escapes, counterfeit or untraceable material, export controls, cybersecurity, customer concentration, long qualification cycles, and margin-bridge uncertainty dominate.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3068 | — | OBSERVED | — |
| n | — | 76 | — | ESTIMATE | — |
| a | 0.18 | 0.28 | 0.39 | PROXY | S1, S2, S3, S4 |
| rho | 0.32 | 0.5 | 0.67 | ESTIMATE | S2, S4 |
| e | 0.56 | 0.72 | 0.85 | ESTIMATE | S1, S2, S5 |
| s5 | 0.12 | 0.22 | 0.33 | PROXY | S6 |
| q | 0.55 | 0.71 | 0.84 | ESTIMATE | S2, S5 |
| d5 | 1.01 | 1.14 | 1.29 | PROXY | S4 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S1, S2, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.71 | 1.72 | 3.21 | ESTIMATE |
| F | 2.91 | 4.13 | 5.00 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.70 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No public six-digit task study.
- a: Defense and commercial documentation burdens differ.
- rho: Bounded judgment rather than observed adoption.
- rho: AI outputs cannot replace formal engineering and airworthiness accountability.
- e: Injected firm count uses an auto-parts margin bridge and is estimated.
- e: Classification does not prove FAA approval, independence, or LMM economics.
- s5: Economy-wide demographic proxy.
- s5: No public code-specific transfer denominator.
- q: No public contract sample quantifies pass-through.
- q: PMA spares and proprietary equipment likely retain more than build-to-print OEM parts.
- d5: FAA fleet forecast is not a direct industry shipment forecast.
- d5: Target program concentration dominates aggregate demand.
- o: Operator share can migrate to OEMs or other approved suppliers.
- o: This is distinct from internal labor automation.

## Sources
- **S1** — [2022 NAICS Definition: Other Aircraft Parts and Auxiliary Equipment](https://www.census.gov/naics/?details=336413&input=336413&year=2022) (accessed 2026-07-22): Census defines 336413 as manufacturing or prototyping aircraft parts and auxiliary equipment other than engines and aircraft fluid-power subassemblies.
- **S2** — [FAA Production Approvals](https://www.faa.gov/aircraft/air_cert/production_approvals) (accessed 2026-07-22): FAA states that production certificates authorize duplicate products under approved type designs and that PMA combines design and production approval for modification and replacement articles.
- **S3** — [Assemblers and Fabricators](https://www.bls.gov/ooh/production/assemblers-and-fabricators.htm) (accessed 2026-07-22): BLS describes physical alignment and assembly tasks and specifically notes physical demands for aerospace assemblers.
- **S4** — [FAA Aerospace Forecast FY 2026-2046](https://www.faa.gov/data_research/aviation/aerospace_forecasts/2026_FAA_Aerospace_Forecasts_FY2026-2046-2.pdf) (accessed 2026-07-22): FAA forecasts commercial aircraft increasing from 6,949 in 2025 to 10,677 in 2046, used as a fleet-demand proxy.
- **S5** — [Acquisition of FAA-Certified Consumable Parts](https://www.acquisition.gov/dlad/11.9201-acquisition-faa-certified-parts-consumable-items.) (accessed 2026-07-22): Federal acquisition rules require approval checks and an unbroken lot, batch, or serial-number traceability chain for relevant FAA-certified parts.
- **S6** — [2024 Chartbook on Firms by Age of Primary Owner](https://www.fedsmallbusiness.org/-/media/project/smallbizcredittenant/fedsmallbusinesssite/fedsmallbusiness/files/2024/firms-in-focus/sbcs_chartbook2024_ownerage.pdf) (accessed 2026-07-22): Federal Reserve owner-age evidence used only as a broad succession proxy.
