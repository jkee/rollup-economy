# 326211 — Tire Manufacturing (except Retreading)

*v5.1 Stage 1 research memo. Run `326211-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.19 · L 0.70 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring wear-driven replacement demand and improvable quality, maintenance, planning, and documentation workflows.
**Weakness:** A tiny, concentrated eligible-firm pool combined with capital and safety burdens.

## Business-model lens
- Included: US lower-middle-market manufacturers of new tires and inner tubes from natural or synthetic rubber that repeatedly supply external vehicle OEM, fleet, distributor, dealer, agricultural, industrial, specialty, or private-label customers.
- Excluded: Tire retreading and rebuilding, tire repair and installation, retail-only dealers, captive internal production, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring and repeat B2B product sales through OEM programs, distributors, dealers, fleets, and specialty channels, priced by tire unit or program with raw-material, freight, brand, performance, warranty, and volume economics.
- Deviation from default lens: none

## Executive view
New-tire manufacturing has durable physical demand and meaningful production-support opportunities, but the eligible LMM universe is exceptionally small and the process is capital-, safety-, and compliance-intensive. AI is more credible in planning, quality, maintenance, testing documentation, and administration than in replacing tire building.

## How AI changes the work
AI can assist compound and process analytics, scheduling, visual inspection, anomaly detection, predictive maintenance, laboratory and compliance documentation, warranty analysis, and commercial workflows. Mixing, calendaring, building, curing, handling, testing, and process intervention remain tightly controlled physical work.

## Value capture
Specialty design, tooling, qualification, brand, and availability may protect savings. Global competition and powerful OEM, distributor, fleet, and private-label buyers should capture part through bids, material formulas, and program negotiations.

## Firm availability
The activity is coherent but dominated by large strategic manufacturers; the provided LMM count is only 11 and likely contains few clean, independent controls. Succession evidence is generic and transaction rates are highly sensitive to single deals.

## Demand durability
Gradually rising road travel supports replacement tire use, though domestic production also depends on imports, OEM mix, tread life, and plant share. An accountable manufacturer remains essential for a safety-critical physical product.

## Risks and uncertainty
The main risks are scarce targets, high capex, global competitors, raw-material volatility, warranty and recall exposure, environmental liabilities, labor relations, customer concentration, and technology or product qualification. Evidence is weakest on eligible ownership, completed transfers, task-level exposure, and contract capture.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2108 | — | OBSERVED | — |
| n | — | 11 | — | ESTIMATE | — |
| a | 0.12 | 0.19 | 0.28 | PROXY | S1 |
| rho | 0.4 | 0.55 | 0.68 | PROXY | S2, S3 |
| e | 0.15 | 0.29 | 0.45 | ESTIMATE | S4 |
| s5 | 0.09 | 0.17 | 0.28 | PROXY | S6 |
| q | 0.3 | 0.46 | 0.63 | ESTIMATE | — |
| d5 | 0.97 | 1.03 | 1.1 | PROXY | S5 |
| o | 0.97 | 0.992 | 0.999 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.40 | 0.88 | 1.61 | PROXY |
| F | 0.22 | 0.70 | 1.40 | ESTIMATE |
| C | 6.00 | 9.20 | 10.00 | ESTIMATE |
| D | 9.41 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Four-digit data include rubber products other than tires.
- a: The data do not distinguish highly automated major plants from smaller specialty producers.
- rho: The automation source is not tire-specific.
- rho: Safety and compliance evidence establishes constraints but does not measure adoption speed.
- e: The Census definition does not measure independence or transferability.
- e: The frozen firm count of 11 is itself margin-bridged and may be unstable in a concentrated industry.
- s5: Cross-industry intentions are not completed tire transactions.
- s5: With few eligible firms, one transaction materially changes the rate.
- q: No public contract sample measures pass-through.
- q: Retention differs greatly between branded specialty tires, private label, and OEM fitments.
- d5: VMT is not domestic tire-production volume.
- d5: Aviation, agricultural, industrial, and off-road tires follow different drivers.
- o: The estimate is inferred from physical and regulatory requirements.
- o: Demand changes from imports or alternative tire designs belong mainly in d5.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 326200 Rubber Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326200.htm) (accessed 2026-07-22): Reports 135,300 total jobs, 85,630 production jobs representing 63.29 percent, and 20,020 tire builders representing 14.80 percent in broader rubber-product manufacturing, grounding the occupation-mix proxy.
- **S2** — [Metal and Plastic Machine Workers, Occupational Outlook Handbook](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-22): Describes computerized equipment, robots, monitoring, adjustment, inspection, and documentation tasks and continuing manufacturer adoption of labor-saving technology, used only as an adjacent implementation proxy.
- **S3** — [NHTSA Interpretation 08-00244: FMVSS No. 139](https://www.nhtsa.gov/interpretations/08-00244--139-generic-name-cord-material-3-jun-08-rsy) (accessed 2026-07-22): States that tire manufacturers self-certify conformity with applicable safety standards and describes FMVSS No. 139 requirements for new pneumatic radial tires, supporting compliance and accountable-operator constraints.
- **S4** — [2012 NAICS Definition: Tire Manufacturing](https://www2.census.gov/econ2012/Reference_materials/htm%20files/32621m.htm) (accessed 2026-07-22): Defines 326211 as establishments manufacturing tires and inner tubes from natural and synthetic rubber and separately identifies retreading under 326212, grounding the lens.
- **S5** — [2025 FHWA Forecasts of Vehicle Miles Traveled](https://www.fhwa.dot.gov/policyinformation/tables/vmt/vmt_forecast_sum.cfm) (accessed 2026-07-22): Projects total national vehicle miles traveled growing at a 0.6 percent average annual rate between 2023 and 2053 and light-duty travel at 0.6 percent through 2043, used as a replacement-demand proxy.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of employer-business owners surveyed in fall 2024 planned to sell or transfer ownership within five years, used as a cross-industry transfer proxy.
