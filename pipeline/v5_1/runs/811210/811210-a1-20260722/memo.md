# 811210 — Electronic and Precision Equipment Repair and Maintenance

*v5.1 Stage 1 research memo. Run `811210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Growing need to maintain and document complex installed precision equipment, especially medical equipment.
**Weakness:** Extreme segment heterogeneity, proprietary restrictions, and the declared firm-count gap.

## Business-model lens
- Included: Independent repair and maintenance of consumer electronics, computers, office machines, communications equipment, and scientific, medical, and other electronic or precision instruments without primarily retailing new equipment.
- Excluded: New-equipment retailers, captive manufacturer service, appliance and automotive repair, software-only support, manufacturing, and remanufacturing that changes intended use or performance.
- Customer and revenue model: Consumer depot work, business service calls, maintenance contracts, warranty subcontracting, field service, calibration, and regulated equipment service generate incident, hourly, fixed-price, and contract revenue.
- Deviation from default lens: none

## Executive view
A valuable precision-service core is combined with challenged consumer and office repair; heterogeneity, proprietary access, and the absent firm count weaken the aggregate thesis.

## How AI changes the work
AI can improve triage, visual inspection, document retrieval, fault recognition, dispatch, and reporting, while physical repair and validation remain constrained.

## Value capture
First-time-fix and technician leverage support value, but OEM schedules, procurement, warranties, and replacement cost constrain capture.

## Firm availability
Transferability depends on credentials, authorization, customers, and specialists; the absent frozen firm count prevents a grounded quantity estimate.

## Demand durability
Medical service is favorable while several office and communications repair occupations contract, producing modest aggregate growth with wide uncertainty.

## Risks and uncertainty
Consumer electronics, computers, communications, medical devices, and scientific instruments have materially different regulation, product life, and economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3986 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.23 | 0.38 | 0.53 | PROXY | S2, S7 |
| rho | 0.35 | 0.55 | 0.72 | PROXY | S5, S7 |
| e | 0.5 | 0.72 | 0.88 | ESTIMATE | S1, S5, S6 |
| s5 | 0.08 | 0.16 | 0.28 | PROXY | S8 |
| q | 0.44 | 0.62 | 0.78 | ESTIMATE | — |
| d5 | 0.92 | 1.04 | 1.17 | PROXY | S3, S4, S6 |
| o | 0.76 | 0.88 | 0.96 | ESTIMATE | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.28 | 3.33 | 6.08 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 8.80 | 10.00 | 10.00 | ESTIMATE |
| D | 6.99 | 9.15 | 10.00 | ESTIMATE |

## Caveats
- a: Segment task mixes differ greatly.
- a: Manufacturing inspection is adjacent rather than direct repair evidence.
- rho: Medical controls are not representative of consumer repair.
- rho: Feasibility does not establish safe autonomy.
- e: The frozen firm count is absent, so downstream opportunity counts cannot be grounded.
- e: Externalization differs sharply by equipment type.
- s5: Exit intent is not a marketable business.
- s5: No direct six-digit transaction series was located.
- q: Capture may appear as uptime or compliance.
- q: Warranty work may constrain price.
- d5: Employment is an imperfect demand proxy.
- d5: Segment mix can dominate the aggregate.
- o: Persistence is lower for disposable consumer devices.
- o: It is higher for medical and installed scientific equipment.

## Sources
- **S1** — [2022 NAICS Definition: 811210](https://www.census.gov/naics/?details=811210&input=811210&year=2022) (accessed 2026-07-22): Defines included equipment repair and the new-retail exclusion.
- **S2** — [BLS Occupational Employment: NAICS 811200](https://www.bls.gov/oes/2023/may/naics4_811200.htm) (accessed 2026-07-22): Shows the repair, administrative, engineering, sales, and production mix.
- **S3** — [BLS Occupational Projections and Characteristics](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Reports mixed projections across electronic repair occupations.
- **S4** — [BLS Outlook: Medical Equipment Repairers](https://www.bls.gov/ooh/Installation-Maintenance-and-Repair/Medical-equipment-repairers.htm) (accessed 2026-07-22): Supports strong medical-equipment repair demand.
- **S5** — [FDA Guidance on Remanufacturing and Servicing](https://www.fda.gov/news-events/press-announcements/fda-issues-final-guidance-clarify-remanufacturing-devices-need-maintenance-or-repair) (accessed 2026-07-22): Establishes servicing controls and the remanufacturing boundary.
- **S6** — [Nixing the Fix](https://www.ftc.gov/reports/nixing-fix-ftc-report-congress-repair-restrictions) (accessed 2026-07-22): Documents repair restrictions affecting independent markets.
- **S7** — [IPC Paper on AI in Automated Optical Inspection](https://www.electronics.org/news-release/new-ipc-white-paper-focuses-use-artificial-intelligence-automated-optical-inspection) (accessed 2026-07-22): Supports AI inspection capability and implementation barriers.
- **S8** — [Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Provides a cross-industry exit-intention anchor.
