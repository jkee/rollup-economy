# 811122 — Automotive Glass Replacement Shops

*v5.1 Stage 1 research memo. Run `811122-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.85 · L 1.29 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digitized claims intake, part matching, scheduling, and mobile routing can raise technician utilization and reduce avoidable job friction.
**Weakness:** Physical installation and calibration remain safety-critical, while the qualifying firm population is small and the demand evidence is indirect.

## Business-model lens
- Included: U.S. lower-middle-market automotive glass businesses providing repair, replacement, tinting, mobile service, and required camera or driver-assistance recalibration to consumers, fleets, and insurers through stand-alone shops or technician routes.
- Excluded: Building-glass contractors, automotive body shops whose glass work is incidental, vehicle dealers and fleet operators performing captive work, glass manufacturing or wholesale distribution, consumer-only do-it-yourself products, shells, non-control vehicles, and owner-dependent hobby operations.
- Customer and revenue model: Revenue is earned per repair, replacement, tint, or recalibration job, paid directly by vehicle owners, commercial fleets, or insurers. The model combines appointment and claims coordination, vehicle-specific glass sourcing, mobile routing or shop capacity, physical installation, cure and leak checks, and increasingly safety-system calibration and documentation.
- Deviation from default lens: none

## Executive view
Automotive glass is a coherent outsourced service with a digitizable claims, parts, scheduling, and routing layer wrapped around a physical and increasingly safety-critical installation. AI can improve throughput and coordination, but it does not remove the technician or calibration accountability from most jobs.

## How AI changes the work
AI can handle intake, damage triage, estimate drafting, insurer documentation, VIN and part matching, customer communication, appointment changes, route suggestions, record checks, and technician knowledge retrieval. Humans remain responsible for physical glass work, vehicle protection, adhesive and cure control, leak checks, calibration setup and execution, and safety-significant exceptions.

## Value capture
Benefits can appear as higher booking conversion, fewer part errors, denser mobile routes, and more technician jobs per day. Insurer reimbursement constraints, transparent consumer quotes, software cost, technician pay, calibration investment, and rework liability cap retention.

## Firm availability
Most stand-alone glass firms fit the external-service screen, but the supplied target count is small and margin-derived. Captive work, micro mobile operators, insurer concentration, multi-location ownership, and technician or owner dependence reduce the number of transferable firms.

## Demand durability
Vehicle travel offers a modestly positive anchor, while glass damage remains weather- and incident-sensitive. More ADAS-equipped windshields support sophisticated service content, but that complexity is not treated as pure unit growth under a constant-quality demand measure.

## Risks and uncertainty
The main uncertainties are the broad occupational proxy, lack of exact job-volume data, unpredictable storm and road-debris incidence, insurer price control, calibration quality adjustment, and conversion of broad succession intentions into completed external control transfers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.313 | — | OBSERVED | — |
| n | — | 13 | — | ESTIMATE | — |
| a | 0.18 | 0.29 | 0.4 | PROXY | S1, S2, S3 |
| rho | 0.38 | 0.58 | 0.74 | ESTIMATE | S1, S3 |
| e | 0.72 | 0.86 | 0.94 | ESTIMATE | S1, S5 |
| s5 | 0.05 | 0.11 | 0.18 | PROXY | S6 |
| q | 0.43 | 0.6 | 0.75 | ESTIMATE | S3 |
| d5 | 0.97 | 1.04 | 1.12 | PROXY | S3, S4 |
| o | 0.94 | 0.98 | 0.995 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.86 | 2.11 | 3.71 | ESTIMATE |
| F | 0.62 | 1.29 | 1.87 | ESTIMATE |
| C | 8.60 | 10.00 | 10.00 | ESTIMATE |
| D | 9.12 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation shares are not direct task-hour shares and exclude self-employed workers.
- a: ADAS tools can automate diagnostics and documentation without automating the accountable calibration procedure.
- rho: Buying claims or scheduling software is not equivalent to sustained AI-enabled workflow use.
- rho: Static and dynamic calibration requirements differ across vehicles and can restrict standardized deployment.
- e: Multi-location and mobile operators make establishment-to-firm conversion uncertain.
- e: Insurer network dependence, technician concentration, and owner relationships can impair practical transferability.
- s5: The proxy spans industries and firm sizes.
- s5: Intentions, listings, and completed control transfers are different quantities.
- q: No source isolates AI-created benefit from ordinary digitization or ADAS-related ticket growth.
- q: Faster throughput may require additional calibration equipment and quality-control expense.
- d5: VMT is an exposure proxy, not a direct forecast of glass breakage.
- d5: ADAS recalibration increases service content but should not be counted mechanically as higher constant-quality demand.
- o: Operator need can remain high even if administrative labor per job falls substantially.
- o: Mobile service changes the location of accountable work, not the need for it.

## Sources
- **S1** — [2022 NAICS Definition: 811122 Automotive Glass Replacement Shops](https://www.census.gov/naics/?details=8111&input=8111&year=2022) (accessed 2026-07-22): Official activity definition and classification boundaries used for the lens and operator-need reasoning.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 811120](https://www.bls.gov/oes/2023/may/naics5_811120.htm) (accessed 2026-07-22): Five-digit body, paint, interior, and glass occupational mix used as the task-exposure proxy.
- **S3** — [ADAS Recalibration](https://www.safelite.com/windshield-camera-recalibration) (accessed 2026-07-22): Operator evidence on insurance coordination, mobile service, static and dynamic calibration, technician work, and manufacturer-required recalibration after replacement.
- **S4** — [2025 FHWA Forecasts of Vehicle Miles Traveled](https://www.fhwa.dot.gov/policyinformation/tables/vmt/vmt_forecast_sum.cfm) (accessed 2026-07-22): Light-duty vehicle-miles-traveled growth used as the primary five-year demand proxy.
- **S5** — [2022 Economic Census: Other Services Basic Statistics](https://data.census.gov/table/ECNBASIC2022.EC2281BASIC?q=personal) (accessed 2026-07-22): Exact-industry establishment and revenue context used to qualify firm availability and classification coherence.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Employer-owner five-year sale and transfer intentions used as the broad starting point for the qualifying-control-transfer proxy.
