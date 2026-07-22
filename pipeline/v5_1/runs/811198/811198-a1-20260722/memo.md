# 811198 — All Other Automotive Repair and Maintenance

*v5.1 Stage 1 research memo. Run `811198-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.54 · L 2.69 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent physical service demand from an aging fleet combined with digitally improvable workflow.
**Weakness:** Residual-category heterogeneity and weak direct evidence on economics and AI realization.

## Business-model lens
- Included: Independent automotive air-conditioning service, tire repair, lubrication, safety and emissions inspection, diagnostic service without repair, rustproofing, undercoating, spray-on bed liners, and other automotive maintenance not classified elsewhere.
- Excluded: Mechanical and electrical repair; body, paint, interior, and glass work; car washes; new-parts retailing; vehicle dealers; and captive manufacturer or fleet service operations.
- Customer and revenue model: Local vehicle owners and fleets buy episodic inspections, diagnostics, tire repairs, fluid services, and protective treatments through per-job, menu-priced, or labor-plus-materials charges.
- Deviation from default lens: none

## Executive view
This is a fragmented set of local physical vehicle services with moderate AI leverage in the information layer and strong operator persistence.

## How AI changes the work
AI is most relevant to scheduling, quoting, communication, inspection documentation, knowledge retrieval, and diagnostic support; hands-on work remains physical.

## Value capture
Throughput and estimate consistency can improve margin, but local competition and fleet buyers pass some gains to customers.

## Firm availability
Succession and consolidation imply a usable acquisition pool, though many shops remain subscale and owner-dependent.

## Demand durability
An aging fleet supports recurring service while powertrain change, consumer deferral, and manufacturer-controlled diagnostics are offsets.

## Risks and uncertainty
The class mixes services with different recurrence, margins, regulation, and AI exposure; direct six-digit operating data are sparse.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4802 | — | OBSERVED | — |
| n | — | 32 | — | ESTIMATE | — |
| a | 0.17 | 0.29 | 0.41 | PROXY | S2, S3 |
| rho | 0.42 | 0.62 | 0.78 | PROXY | S3 |
| e | 0.55 | 0.75 | 0.9 | ESTIMATE | S1 |
| s5 | 0.1 | 0.18 | 0.3 | PROXY | S6, S7 |
| q | 0.5 | 0.68 | 0.82 | ESTIMATE | — |
| d5 | 0.96 | 1.08 | 1.2 | PROXY | S4, S5 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.37 | 3.45 | 6.14 | PROXY |
| F | 1.63 | 2.69 | 3.64 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.64 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The class combines materially different service models.
- a: Feature usefulness does not equal automatable labor hours.
- rho: Survey sampling does not establish national adoption.
- rho: Benefits may appear as quality or throughput rather than labor reduction.
- e: Residual-code assignment depends on primary revenue.
- e: No direct externalization measure was located.
- s5: Exit intention need not produce an outside sale.
- s5: Aftermarket deal reports cover a wider market.
- q: Value may appear as capacity or quality.
- q: Capture differs across retail and fleet work.
- d5: Vehicle age is exposure rather than direct demand.
- d5: The occupation covers neighboring automotive activities.
- o: Remote diagnosis may reduce stand-alone visits.
- o: Automated inspection lanes can reduce labor without removing the operator.

## Sources
- **S1** — [2022 NAICS Definition: 811198](https://www.census.gov/naics/?details=811198&input=811198&year=2022) (accessed 2026-07-22): Defines included residual automotive services and exclusions.
- **S2** — [BLS Occupational Employment: NAICS 811100](https://www.bls.gov/oes/2023/May/naics4_811100.htm) (accessed 2026-07-22): Shows the broader industry's repair, administrative, and sales occupational mix.
- **S3** — [2025 Ratchet+Wrench Industry Survey](https://vehiclerepair.endeavorb2b.com/wp-content/uploads/RW_Industry-Survey.pdf) (accessed 2026-07-22): Reports repair-shop AI applications in scheduling, estimates, digital inspection, and service.
- **S4** — [U.S. Vehicle Age Rises Again in 2025](https://press.spglobal.com/2025-05-21-U-S-Vehicle-Age-Rises-Again-to-12-8-Years-in-2025%2C-According-to-S-P-Global-Mobility) (accessed 2026-07-22): Supports vehicle aging, fleet growth, and out-of-warranty aftermarket demand.
- **S5** — [BLS Outlook: Automotive Service Technicians](https://www.bls.gov/ooh/installation-maintenance-and-repair/automotive-service-technicians-and-mechanics.htm) (accessed 2026-07-22): Identifies longer vehicle retention, calibration complexity, and electric vehicles as demand factors.
- **S6** — [Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Provides a cross-industry exit-intention anchor.
- **S7** — [2025 Mergers and Acquisitions Outlook Report](https://www.mema.org/research-and-insights/mema-insights/2025-mergers-acquisitions-outlook-report) (accessed 2026-07-22): Documents aftermarket deal activity and consolidation.
