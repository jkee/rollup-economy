# 326291 — Rubber Product Manufacturing for Mechanical Use

*v5.1 Stage 1 research memo. Run `326291-a1-20260723`, model `claude-sonnet-5`, 2026-07-23, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.23 · L 0.95 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Qualification-sensitive recurring component demand supports durable outsourced production and some persistence of internally created efficiencies.
**Weakness:** Most labor is tied to physical production, while the actual AI-addressable tasks and five-year control-transfer rate lack six-digit direct evidence.

## Business-model lens
- Included: Independent US lower-middle-market manufacturers that repeatedly supply externally owned vehicle, machinery, and equipment customers with molded, extruded, or lathe-cut mechanical rubber goods.
- Excluded: Captive plants, non-control vehicles, rubber tubing, mechanical rubber goods made through other processes classified in 326299, and firms without recurring or repeat outsourced customer relationships.
- Customer and revenue model: Repeat purchase orders, approved-supplier programs, OEM contracts, and aftermarket supply for specification-sensitive molded, extruded, or lathe-cut rubber components, generally billed per part, lot, or program.
- Deviation from default lens: none

## Executive view
Mechanical rubber products are tangible, often qualified inputs with repeat OEM and aftermarket demand. AI's five-year role is mostly to compress information-heavy commercial, planning, quality, and maintenance work; the physical production core limits the exposed wage share.

## How AI changes the work
AI can assist quote preparation, drawing and specification review, scheduling, purchasing, defect classification, corrective-action drafting, maintenance troubleshooting, and retrieval of process knowledge. People remain central to tooling, machine setup, material handling, process intervention, testing sign-off, and abnormal-condition response.

## Value capture
Qualified custom components can support retention because supplier changes require testing, tooling, and engineering time. OEM cost-down pressure, program rebids, and competition for standardized parts progressively share savings with customers.

## Firm availability
The supplied dataset estimates 137 firms in the EBITDA band, but independence, repeat revenue, customer diversity, compliance, and owner dependence must be verified. Control-transfer evidence is not denominator matched and remains a major diligence need.

## Demand durability
Vehicles, machinery, and equipment continue to require physical rubber components and aftermarket replacements. Demand can still be cyclical and can shift with platform redesign, imports, material substitution, or customer insourcing.

## Risks and uncertainty
Six-digit occupation weights, AI outcomes, contract economics, and private ownership transitions are not directly measured. Product liability, environmental diligence, customer concentration, obsolete tooling, or dependence on one OEM program can impair an otherwise recurring operation.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2629 | — | OBSERVED | — |
| n | — | 137 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | ESTIMATE | S1, S2 |
| rho | 0.32 | 0.5 | 0.68 | ESTIMATE | S1, S2 |
| e | 0.42 | 0.6 | 0.76 | ESTIMATE | S1 |
| s5 | 0.08 | 0.17 | 0.29 | ESTIMATE | — |
| q | 0.45 | 0.64 | 0.8 | ESTIMATE | S1 |
| d5 | 0.82 | 0.98 | 1.17 | ESTIMATE | S1, S2 |
| o | 0.92 | 0.98 | 1 | ESTIMATE | S1 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.34 | 0.95 | 2.00 | ESTIMATE |
| F | 2.77 | 4.35 | 5.53 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.54 | 9.60 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation counts cover NAICS 326 rather than 326291.
- a: The estimate excludes already automated control tasks and does not treat generic robotics potential as AI exposure.
- rho: No 326291-specific implementation cohort was found.
- rho: Physical automation investment and ordinary lean improvement are outside this primitive unless AI is the enabling constraint.
- e: NAICS is establishment-based and does not measure recurrence or transferability.
- e: The supplied firm count is an ESTIMATE based on size classes and an assumed margin bridge.
- s5: No directly observed five-year control-transfer rate for eligible 326291 firms was available.
- s5: Small private transactions are systematically underreported.
- q: The Census definition supports the product and end-market characterization but not specific contract terms.
- q: Capture varies sharply between custom qualified components and readily substitutable standard parts.
- d5: BLS output figures are for broader NAICS 326 and are historical changes, not a five-year forecast.
- d5: The industry spans diverse mechanical parts with differing exposure to vehicle platforms and capital spending.
- o: Large OEMs may vertically integrate selected parts or eliminate them through redesign.
- o: Continued operator requirement does not imply unchanged staffing or production technology.

## Sources
- **S1** — [2022 NAICS Definition: 326291 Rubber Product Manufacturing for Mechanical Use](https://www.census.gov/naics/?input=326291&year=2022&details=326291) (accessed 2026-07-23): Defines the industry as molded, extruded, or lathe-cut mechanical rubber goods, generally parts for motor vehicles, machinery, and equipment, and distinguishes rubber tubing and other processes classified in 326299.
- **S2** — [Industries at a Glance: Plastics and Rubber Products Manufacturing: NAICS 326](https://www.bls.gov/iag/tgs/iag326.htm) (accessed 2026-07-23): Shows 2025 subsector employment concentrated in machine operators, assemblers, inspectors, packers, and production supervisors, and reports real-output changes of -3.6%, -6.3%, -1.8%, and -3.4% for 2022-2025.
