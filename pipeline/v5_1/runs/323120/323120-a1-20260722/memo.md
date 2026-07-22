# 323120 — Support Activities for Printing

*v5.1 Stage 1 research memo. Run `323120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 5.60 · L 2.97 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digital job intake and exception-heavy prepress workflows create a substantial AI-addressable labor surface in a high-labor-share industry.
**Weakness:** Routine support tasks can be automated or insourced entirely, reducing demand for the independent operator rather than merely lowering its labor cost.

## Business-model lens
- Included: Independent US lower-middle-market providers of recurring outsourced prepress and postpress services to printers, publishers, packaging converters, agencies, and other external customers, including data imaging, platemaking, typesetting, print preparation, trade binding, finishing, and related production support.
- Excluded: Captive in-plant departments, full-service printers whose support work is incidental to printing, software-only design platforms, equipment vendors, non-control financing vehicles, and firms outside the EBITDA band.
- Customer and revenue model: Repeat business-to-business job revenue, usually quoted per file, plate, project, run, unit, or finishing operation, with some standing account relationships and volume schedules.
- Deviation from default lens: none

## Executive view
Printing support has a larger digital workflow surface than printing plants, but its mixed structure matters: prepress can be heavily AI-assisted while binding and finishing remain physical. The opportunity is therefore strongest in firms that combine repeat digital intake with enough technical and physical accountability to resist complete self-service.

## How AI changes the work
AI can parse specifications, normalize job tickets, prepare and compare files, flag preflight exceptions, assist imposition and version control, draft estimates, schedule work, and automate status messages. It is less able to replace setup, material movement, binding, finishing, maintenance, and release decisions where a mistake can spoil an entire run.

## Value capture
Providers can initially retain savings within job quotes and use faster turnaround or fewer remakes as differentiation. Over time, transparent vendor comparisons, insourcing, integrated printer workflows, and standing-account negotiations should transfer much of commodity-task savings to customers.

## Firm availability
The code likely contains a meaningful transferable set, but buyer diligence must screen customer concentration, owner-held technical knowledge, equipment age, and captive relationships. Generic succession evidence suggests turnover, while industry-specific completed-transfer evidence remains absent.

## Demand durability
The need for support work persists, but independent demand faces pressure from software automation, printer integration, and consolidation. Specialty finishing, overflow capacity, complex files, variable data, and rush work are more durable than routine preflight or typesetting.

## Risks and uncertainty
The largest uncertainty is the service-mix split hidden inside the six-digit code. A prepress-heavy firm may have high AI exposure but weak operator-required demand, while a bindery-heavy firm may have durable operator demand but less AI-substitutable labor.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3259 | — | OBSERVED | — |
| n | — | 57 | — | ESTIMATE | — |
| a | 0.24 | 0.38 | 0.54 | PROXY | S1, S2, S3 |
| rho | 0.4 | 0.6 | 0.76 | ESTIMATE | S3 |
| e | 0.45 | 0.62 | 0.78 | ESTIMATE | S1 |
| s5 | 0.1 | 0.17 | 0.27 | PROXY | S4 |
| q | 0.3 | 0.48 | 0.65 | ESTIMATE | S3 |
| d5 | 0.7 | 0.86 | 1 | PROXY | S1, S2, S3 |
| o | 0.62 | 0.78 | 0.9 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.25 | 2.97 | 5.35 | ESTIMATE |
| F | 2.04 | 3.13 | 4.13 | ESTIMATE |
| C | 6.00 | 9.60 | 10.00 | ESTIMATE |
| D | 4.34 | 6.71 | 9.00 | ESTIMATE |

## Caveats
- a: No six-digit occupational or task distribution was located.
- a: The code combines digital prepress with physically intensive postpress operations, so firm-level exposure will be bimodal.
- rho: Industry evidence describes automation priorities, not achieved AI substitution.
- rho: Implementation economics differ sharply between file-based prepress and machine-based postpress.
- e: Eligibility has not been observed directly at six digits.
- e: The provided firm count is an ESTIMATE based on a margin bridge and may include nontransferable or captive-like operations.
- s5: Gallup is not industry- or size-band-specific and measures plans rather than completed transfers.
- s5: Family and employee transfers may not qualify as external control changes.
- q: No representative contract or repricing dataset was located.
- q: Urgent and technically complex work may retain much more value than commodity file preparation or finishing.
- d5: Employment is not a direct measure of constant-quality service demand.
- d5: The code's prepress and postpress segments may follow materially different demand paths.
- o: Operator displacement is likely much higher in routine prepress than in physical trade binding.
- o: Software may automate the interface while an unseen production operator remains accountable downstream.

## Sources
- **S1** — [Printing and Related Support Activities: NAICS 323](https://www.bls.gov/iag/tgs/iag323.htm) (accessed 2026-07-22): Defines the broader subsector as printing products and performing support activities such as data imaging, platemaking, and bookbinding, and provides current occupational context.
- **S2** — [Occupational projections and worker characteristics](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Reports national 2024-2034 projections of 26,200 to 22,300 for prepress technicians, a 14.6% decline, and 35,800 to 30,000 for print binding and finishing workers, a 16.1% decline.
- **S3** — [State of the Industry Report: Executive Summary, April 2024](https://www.printing.org/docs/default-source/research-docs---public/state_of_the_industry_report_april_2024_executive_summary.pdf?sfvrsn=e3e413f8_5%2FState_of_the_Industry_Report_April_2024_EXECUTIVE_SUMMARY) (accessed 2026-07-22): Reports printers focusing on cost and quality control, productivity, automation, business intelligence, e-commerce portals, and production automation, with rising labor costs among major concerns.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey found 22% of employer-business owners planned to sell or transfer ownership within five years, while 5% planned closure and 5% had no plan.
