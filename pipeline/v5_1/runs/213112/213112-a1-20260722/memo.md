# 213112 — Support Activities for Oil and Gas Operations

*v5.1 Stage 1 research memo. Run `213112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.31 · L 1.90 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large outsourced service base and data-rich coordination around hazardous field work create meaningful bounded automation potential.
**Weakness:** Extreme service-line heterogeneity and spot-market pricing weaken both a single demand estimate and long-run benefit retention.

## Business-model lens
- Included: US lower-middle-market firms repeatedly providing crew-and-equipment field services to external oil and gas operators across completion, intervention, production support, and end-of-life work, including hydraulic fracturing, cementing, wireline, well logging/testing, casing and tubing work, chemical treatment, cleanout, swabbing, workover, equipment servicing, and plugging.
- Excluded: Pure geological or exploration advisory firms without recurring crew-and-equipment field operations; product-only sellers; passive equipment lessors; captive service units; contract drilling classified in 213111; geophysical surveying, site construction, pipeline work, and transportation classified elsewhere; firms outside the EBITDA band.
- Customer and revenue model: Repeat outsourced field jobs for E&P operators under master service agreements, pricing schedules, per-stage or per-job quotes, daywork/hourly terms, and occasional longer contracts; activity and price depend on well completions, producing-well maintenance, decommissioning, customer budgets, and service capacity.
- Deviation from default lens: NAICS 213112 spans data/advisory exploration and many materially different field services from high-capital fracturing to low-capital well cleaning and plugging. For business-model coherence, the lens keeps recurring crew-and-equipment field operators across the well lifecycle and excludes pure advisory exploration, product-only sales, and passive rental. The narrowing is based on operating model, not perceived attractiveness.

## Executive view
Oilfield support has a large LMM-relevant establishment base and substantial labor content, but NAICS 213112 mixes many service lines with different capital, data, and demand profiles. AI can improve technical interpretation and field-service coordination; physical execution, safety accountability, commodity cyclicality, and spot pricing remain binding constraints.

## How AI changes the work
Likely uses include job design, prior-log retrieval, anomaly detection, dispatch, maintenance prediction, inventory planning, JSA/HSE documentation, field reports, invoice reconciliation, and customer support. Rig-up, pressure pumping, wireline handling, tubing/casing work, cleanout, workover, repair, and plugging remain equipment- and crew-intensive.

## Value capture
Short competitive jobs and market-adjusted pricing pass gains quickly to E&P customers. Firms with scarce technical capability, reliable crews, differentiated data, or contracted availability can retain more through higher utilization, less downtime, and fewer errors.

## Firm availability
Census shows thousands of small establishments, making the population broad, but establishment is not firm and many operators are too small, inactive, product-heavy, or financially fragile. Transferability depends on crews, equipment condition, safety record, customer concentration, environmental exposure, and through-cycle earnings.

## Demand durability
Completion work follows volatile new-well activity, while workover, cleaning, logging, treatment, and plugging are supported by a very large aging well stock. Orphan-well grants add a funded end-of-life niche, but rig and public-company activity indicate near-term pressure and long-term oil forecasts remain uncertain.

## Risks and uncertainty
Risks include oil/gas prices, E&P budget cuts, excess equipment, pricing pressure, service-line obsolescence, customer concentration, accidents and environmental liabilities, crew availability, working capital, equipment finance, bankruptcy, and confusing asset liquidations with transferable firms.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3328 | — | OBSERVED | — |
| n | — | 1347 | — | ESTIMATE | — |
| a | 0.16 | 0.28 | 0.41 | PROXY | S2 |
| rho | 0.32 | 0.51 | 0.68 | ESTIMATE | S3, S7 |
| e | 0.49 | 0.67 | 0.81 | ESTIMATE | S1, S4 |
| s5 | 0.12 | 0.25 | 0.39 | PROXY | S8 |
| q | 0.3 | 0.47 | 0.64 | PROXY | S9, S10 |
| d5 | 0.68 | 0.94 | 1.22 | PROXY | S5, S6, S9, S11 |
| o | 0.93 | 0.98 | 1 | ESTIMATE | S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.68 | 1.90 | 3.71 | ESTIMATE |
| F | 7.05 | 8.72 | 9.74 | ESTIMATE |
| C | 6.00 | 9.40 | 10.00 | PROXY |
| D | 6.32 | 9.21 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source includes mining support outside oil and gas.
- a: The code's service-line mix makes one exposure range imprecise.
- rho: Large-vendor digital capabilities may not be affordable or transferable to LMM firms.
- rho: No direct five-year implementation survey exists.
- e: Establishment counts exceed firm counts.
- e: The injected n uses one sector margin across service lines with very different capital intensity and profitability.
- s5: Owner age is not observed transaction flow.
- s5: Private deals and small-company failures are incompletely reported.
- q: Commercial structures differ sharply by service line and basin.
- q: Public-company contracts may not represent LMM bargaining power.
- d5: The service basket is heterogeneous and no single activity index covers it.
- d5: Orphan-well funding supports only one segment and is time-limited.
- d5: Producing-well count does not reveal annual outsourced service frequency.
- o: Some logging interpretation and advisory work may become software-delivered faster than physical services.
- o: Operator consolidation can reduce independent share without eliminating the work.

## Sources
- **S1** — [213112 Support Activities for Oil and Gas Operations — Census Bureau Profile](https://data.census.gov/profile/213112_-_Support_activities_for_oil_and_gas_operations?codeset=naics~213112&g=010XX00US) (accessed 2026-07-23): Current industry definition and 9,627 employer establishments in 2023 CBP.
- **S2** — [May 2023 OEWS: Support Activities for Mining](https://www.bls.gov/oes/2023/may/naics4_213100.htm) (accessed 2026-07-23): Broader occupation mix: construction/extraction 46.43%, roustabouts 11.92%, and installation/maintenance/repair 9.16%.
- **S3** — [OSHA Oil and Gas Extraction Safety Hazards](https://www.osha.gov/oil-and-gas-extraction/hazards) (accessed 2026-07-23): Documents vehicle, struck-by, explosion, fall, high-pressure, electrical, and machinery hazards and the need for training and job safety analysis.
- **S4** — [2023 County Business Patterns table for 213112](https://test.data.census.gov/table?q=213112%3A+Support+Activities+for+Oil+and+Gas+Operations) (accessed 2026-07-23): Reports 4,917 establishments with fewer than five employees, 1,397 with 5–9, 1,253 with 10–19, and 1,133 with 20–49.
- **S5** — [EIA U.S. Oil and Natural Gas Wells by Production Rate](https://www.eia.gov/petroleum/wells/) (accessed 2026-07-23): Reports 918,481 producing wells in 2024 and 78% producing 15 BOE/d or less in 2023–2024.
- **S6** — [OSHA Oil and Gas Well Servicing: Workover](https://www.osha.gov/etools/oil-and-gas/servicing/workover) (accessed 2026-07-23): Describes physical remedial operations including sand cleanout, casing repair, recompletion, sidetracking, and plug-back.
- **S7** — [Halliburton 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/45012/000004501226000015/hal-20251231.htm) (accessed 2026-07-23): Documents digital and AI solutions alongside logging, cement integrity, well intervention, completion, fluids, and project-management services; supports technical availability but not LMM implementation.
- **S8** — [ABS Characteristics of Business Owners: 2024 Tables](https://www.census.gov/data/tables/2024/econ/abs/2024-abs-characteristics-of-owners.html) (accessed 2026-07-23): Official Census Age of Owner tables for employer businesses, used only as a broad succession proxy.
- **S9** — [Nine Energy Service 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1532286/000153228626000005/nine-20251231.htm) (accessed 2026-07-23): States jobs are competitively bid or negotiated, most business is spot-like, and 2025 brought activity declines and pricing pressure across service lines.
- **S10** — [ProFrac Holding 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1680247/000168024726000028/pump-20251231.htm) (accessed 2026-07-23): Describes per-job hydraulic-fracturing pricing and turnkey, daywork, or hourly terms for wireline and cementing; demand depends on prices, completion budgets, and rig count.
- **S11** — [Department of the Interior State Orphaned Wells Program](https://www.doi.gov/state-orphaned-wells-program) (accessed 2026-07-23): Program provides about $4.2 billion to states for plugging, remediation, characterization, reclamation, and associated infrastructure removal.
- **S12** — [EIA Crude Oil and Natural Gas Drilling Activity](https://www.eia.gov/dnav/ng/ng_enr_drill_s1_m.htm) (accessed 2026-07-23): US rotary rigs averaged 553 in May 2026, including 535 onshore and 18 offshore.
