# 325991 — Custom Compounding of Purchased Resins

*v5.1 Stage 1 research memo. Run `325991-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.29 · L 0.50 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Customer-qualified formulations and repeat physical supply create durable relationships and switching costs.
**Weakness:** Production-heavy operations and transparent resin economics limit labor substitution and retained savings.

## Business-model lens
- Included: Independent LMM businesses that repeatedly blend, mix, modify, pelletize, or add additives to purchased plastic resins for external customers, including custom formulations and recycled-content compounds.
- Excluded: Base-resin polymerization, captive compounding, molding-only operations, pure distribution, shells, and firms outside the EBITDA band.
- Customer and revenue model: Repeat B2B toll or product sales of customer-qualified compounds and masterbatches, supported by formulation, testing, color or performance matching, quality documentation, and supply coordination.
- Deviation from default lens: none

## Executive view
Custom resin compounding is a repeat B2B physical process with customer qualification and useful technical-data workflows. AI can improve formulation support, quality analysis, and commercial administration, but production labor and modest compensation intensity cap total opportunity.

## How AI changes the work
AI is most applicable to formulation and prior-batch retrieval, specification and compliance drafting, quality trend detection, production planning, procurement, quoting, and complaint triage. Feeding, mixing, extrusion, pelletizing, lab testing, maintenance, material handling, and release remain physical and supervised.

## Value capture
Customer qualification, consistent properties, technical collaboration, and requalification costs provide stickiness. Resin-index pricing, tolling arrangements, transparent material costs, and large processor procurement enable benefit sharing.

## Firm availability
Most truly independent custom compounders should fit recurring external supply, but the estimated universe must be filtered for captive plants, misclassification, customer concentration, environmental condition, aging assets, and strategic ownership.

## Demand durability
Tailored compounds remain necessary physical inputs, and recycled-content and performance requirements can add formulation complexity. Overall demand is exposed to manufacturing cycles, plastic-reduction policies, import competition, and end-market substitution rather than software elimination.

## Risks and uncertainty
The largest uncertainties are current plant automation, formula differentiation and ownership, customer concentration, resin-price mechanisms, end-market mix, environmental exposure, capacity utilization, and the actual count of independent transferable firms.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.097 | — | OBSERVED | — |
| n | — | 91 | — | ESTIMATE | — |
| a | 0.15 | 0.24 | 0.35 | PROXY | S1, S2, S3 |
| rho | 0.37 | 0.54 | 0.7 | ESTIMATE | S3, S4 |
| e | 0.63 | 0.78 | 0.9 | ESTIMATE | S1, S4 |
| s5 | 0.14 | 0.24 | 0.35 | PROXY | S5 |
| q | 0.48 | 0.64 | 0.79 | ESTIMATE | S1 |
| d5 | 0.96 | 1.08 | 1.22 | ESTIMATE | S1, S6 |
| o | 0.91 | 0.97 | 0.99 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.22 | 0.50 | 0.95 | ESTIMATE |
| F | 3.54 | 4.65 | 5.45 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.74 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Adjacent four-digit occupation proxy rather than a six-digit study.
- a: Automation differs by batch size and formulation complexity.
- rho: No observed five-year industry adoption measure.
- rho: Expert validation remains necessary for material-property and compliance decisions.
- e: Injected firm count is margin-bridged and estimated.
- e: Classification does not establish independence, EBITDA, or customer diversification.
- s5: Economy-wide demographic proxy.
- s5: No public control-transfer denominator for 325991.
- q: No public contract dataset measures benefit sharing.
- q: Proprietary specialties retain more than commodity toll compounding.
- d5: Official sources establish process and regulation rather than a direct growth forecast.
- d5: Automotive, packaging, construction, and consumer end markets cycle differently.
- o: Operator share may migrate to integrated suppliers or customer plants.
- o: This estimate is separate from labor reduction within surviving operators.

## Sources
- **S1** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Census lists NAICS 325991 Custom Compounding of Purchased Resins, supporting the activity boundary.
- **S2** — [Plastics and Rubber Products Manufacturing: NAICS 326](https://www.bls.gov/iag/tgs/iag326.htm) (accessed 2026-07-22): BLS shows a production-oriented adjacent industry and lists 30,760 extruding and drawing machine operators and tenders in the displayed material, used as an occupation proxy.
- **S3** — [Plastics Product Manufacturing - May 2023 OEWS](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-22): BLS reports substantial other-production and material-moving employment and identifies chemical equipment and plant operators in adjacent plastics manufacturing, supporting the task-mix proxy.
- **S4** — [Plastics Molding and Forming Effluent Guidelines](https://www.epa.gov/eg/plastics-molding-and-forming-effluent-guidelines) (accessed 2026-07-22): EPA states extrusion and pelletizing are used to process plastic materials and describes federal effluent standards, supporting physical-process and compliance claims.
- **S5** — [2024 Firms in Focus chartbooks on small business data](https://www.fedsmallbusiness.org/reports/survey/2024/2024-small-business-data-chartbooks) (accessed 2026-07-22): Federal Reserve chartbooks provide broad owner-demographic and age-of-owner evidence used only as a succession proxy.
- **S6** — [EPA Scope Document Describing Resin Compounding and Processing](https://www.epa.gov/sites/default/files/2017-06/documents/pv29_scope_06-22-17.pdf) (accessed 2026-07-22): EPA describes resin compounding, additive-containing masterbatch, and subsequent extrusion into plastic products, supporting process and continuing material-function claims.
