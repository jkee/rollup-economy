# 326299 — All Other Rubber Product Manufacturing

*v5.1 Stage 1 research memo. Run `326299-a1-20260723`, model `claude-sonnet-5`, 2026-07-23, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.09 · L 0.50 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring demand for physical industrial rubber inputs preserves the need for an accountable supplier across the five-year horizon.
**Weakness:** The residual NAICS category is highly heterogeneous, making eligibility and commercial-retention assumptions unusually uncertain.

## Business-model lens
- Included: Independent US lower-middle-market manufacturers that repeatedly supply external business customers with rubber tubing, industrial roll coverings, sheeting, roofing membrane, reclaimed rubber, or other specification-based rubber products included in 326299.
- Excluded: Captive plants, non-control vehicles, one-off or commodity-only operations without repeat customer relationships, and consumer or medical-product businesses such as balloons, floor mats, hair products, pacifiers, and contraceptive devices whose regulation, channels, and demand economics differ materially.
- Customer and revenue model: Repeat purchase orders, distributor supply, approved-supplier relationships, and recurring industrial programs for physical rubber products, priced per unit, length, area, weight, lot, or customer specification.
- Deviation from default lens: The code combines industrial inputs, building products, reclaimed material, consumer goods, and regulated personal or medical products. It is narrowed to recurring B2B outsourced industrial-product manufacturers so customer economics and operator requirements are coherent rather than blended across incompatible models.

## Executive view
This residual code is too heterogeneous for one coherent commercial screen, so the lens is limited to repeat B2B industrial-product manufacturers. Within that lens, physical-product demand supports operator durability, but AI addresses mainly information workflows around a production-heavy labor base.

## How AI changes the work
AI can assist quotes, specifications, scheduling, procurement, defect review, corrective actions, maintenance troubleshooting, order processing, and plant knowledge. Human work remains essential in compounding, setup, forming, cutting, handling, testing, and production exceptions.

## Value capture
Custom and qualification-sensitive products can retain savings between negotiations. Commodity tubing, sheeting, reclaimed rubber, and distributor channels face stronger input-indexing, rebid, and price-competition pressure.

## Firm availability
The supplied dataset estimates 203 firms in the EBITDA band, but the diverse NAICS basket means only a minority-to-majority subset fits recurring B2B outsourced industrial supply. Ownership and deal evidence are not denominator matched.

## Demand durability
Industrial, construction, and replacement uses sustain physical demand, while cycles, imports, redesign, and substitute materials can reduce particular segments. Software is not a substitute for the finished rubber object or accountable producer.

## Risks and uncertainty
The main risk is aggregation across unlike products and channels. Six-digit occupation mix, eligible-firm count, AI results, contract pass-through, environmental liabilities, and control transfers all need direct diligence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1388 | — | OBSERVED | — |
| n | — | 203 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | ESTIMATE | S1, S2 |
| rho | 0.31 | 0.5 | 0.68 | ESTIMATE | S1, S2 |
| e | 0.24 | 0.4 | 0.57 | ESTIMATE | S1 |
| s5 | 0.08 | 0.17 | 0.3 | ESTIMATE | — |
| q | 0.4 | 0.6 | 0.78 | ESTIMATE | S1 |
| d5 | 0.8 | 0.98 | 1.18 | ESTIMATE | S1, S2 |
| o | 0.9 | 0.97 | 1 | ESTIMATE | S1 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.50 | 1.06 | ESTIMATE |
| F | 2.56 | 4.33 | 5.75 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.20 | 9.51 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupational evidence is for NAICS 326, not 326299 or the narrowed lens.
- a: The highly varied production processes could produce materially different exposure by product segment.
- rho: No eligible-lens implementation cohort was found.
- rho: Capital-intensive physical automation is excluded unless AI is the enabling constraint.
- e: The supplied firm count is an ESTIMATE and the establishment-based NAICS definition does not reveal firm revenue mix.
- e: Product heterogeneity makes classification error especially likely.
- s5: No directly observed transfer rate for eligible 326299 firms was found.
- s5: Small private deals and failed sale processes are underreported.
- q: The official definition establishes product scope, not actual contract terms.
- q: Capture likely varies more across this residual code than within more homogeneous manufacturing industries.
- d5: Historical BLS output changes cover all NAICS 326 and are not a five-year forecast.
- d5: The narrowed product basket still spans industrial, construction, and recycled-material cycles.
- o: The residual code contains products with different substitution threats.
- o: Continued operator need does not imply unchanged labor intensity or production methods.

## Sources
- **S1** — [2022 NAICS Definition: 326299 All Other Rubber Product Manufacturing](https://www.census.gov/naics/?input=326299&year=2022&details=326299) (accessed 2026-07-23): Shows the code's heterogeneous scope, including rubber tubing, latex foam, reclaimed rubber, consumer goods, contraceptive devices, sheeting, roofing membrane, industrial roll coverings, and other rubber products, plus the exclusions to adjacent industries.
- **S2** — [Industries at a Glance: Plastics and Rubber Products Manufacturing: NAICS 326](https://www.bls.gov/iag/tgs/iag326.htm) (accessed 2026-07-23): Shows 2025 subsector employment concentrated in machine operators, assemblers, inspectors, packers, and production supervisors, and reports real-output changes of -3.6%, -6.3%, -1.8%, and -3.4% for 2022-2025.
