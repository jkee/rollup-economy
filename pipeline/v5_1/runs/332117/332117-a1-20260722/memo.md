# 332117 — Powder Metallurgy Part Manufacturing

*v5.1 Stage 1 research memo. Run `332117-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.10 · L 0.97 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Qualified recurring programs create dense RFQ, process, traceability, inspection, and quality-document workflows with meaningful switching friction.
**Weakness:** Most labor remains tied to physical process control and quality, while a small firm universe and concentrated programs limit transfer opportunities.

## Business-model lens
- Included: US lower-middle-market manufacturers producing pressed-and-sintered, metal-injection-molded, and related powder-metallurgy parts on repeat job or order programs for external automotive, industrial, appliance, medical, aerospace, defense, and consumer-product customers.
- Excluded: Captive internal plants, primary metal-powder producers, businesses focused solely on additive-manufacturing machines or services outside the NAICS definition, proprietary-product companies without outsourced customer programs, non-control financing vehicles, and non-transferable owner-dependent operations.
- Customer and revenue model: Recurring program and release-order revenue priced per part or lot, commonly supported by customer-specific tooling, material and process specifications, qualification, inspection, and quality documentation.
- Deviation from default lens: none

## Executive view
Powder-metallurgy parts are a qualified, repeat job-order manufacturing niche with strong operator-required demand and meaningful document, engineering, planning, and quality workflows. AI opportunity is real but bounded by physical production, validation, and accountable materials decisions.

## How AI changes the work
AI can parse RFQs and drawings, compare revisions, assist estimates and process plans, organize inspection and furnace data, recommend schedules and maintenance, draft control plans and corrective actions, and manage routine customer documentation. Powder handling, tooling, compaction or molding, sintering, secondary operations, laboratory testing, maintenance, and final release remain physical and accountable.

## Value capture
Tooling, qualifications, traceability, and embedded component designs create switching costs that protect some gains. Annual cost-down requirements, open-book programs, metal clauses, and concentrated automotive or industrial purchasing can transfer substantial recurring benefit to customers.

## Firm availability
The supplied dataset estimates 58 firms in the target economic band. Census's job-order description fits the lens, but firm-level independence, earnings, customer concentration, certifications, equipment, and dependence on owners or key metallurgists require verification.

## Demand durability
Physical parts remain necessary across industrial and consumer systems. Electrification, additive manufacturing, machining, casting, imports, and redesign can change the part mix, while specialized geometry, material efficiency, medical, aerospace, defense, and industrial applications support demand.

## Risks and uncertainty
Major uncertainties are six-digit occupation mix, actual program and end-market concentration, present workflow automation, customer cost-down terms, technical staff transferability, additive substitution, and true LMM margins. The supplied inputs mix vintages and use a machinery margin bridge.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2877 | — | OBSERVED | — |
| n | — | 58 | — | ESTIMATE | — |
| a | 0.1 | 0.2 | 0.31 | PROXY | S1, S2 |
| rho | 0.23 | 0.42 | 0.61 | ESTIMATE | S3, S4 |
| e | 0.66 | 0.81 | 0.9 | ESTIMATE | S2 |
| s5 | 0.08 | 0.16 | 0.27 | ESTIMATE | — |
| q | 0.4 | 0.63 | 0.81 | ESTIMATE | S2, S3 |
| d5 | 0.91 | 1.07 | 1.24 | ESTIMATE | S2, S3, S4 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.26 | 0.97 | 2.18 | ESTIMATE |
| F | 2.25 | 3.45 | 4.37 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.74 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is for all fabricated metal manufacturing, not 332117.
- a: No source measures current AI deployment or task exposure in powder-metallurgy plants.
- rho: This is bounded judgment, not an observed five-year implementation rate.
- rho: NIST additive-manufacturing evidence is adjacent to, not representative of, conventional pressing and sintering.
- e: The supplied n relies on size-class receipts and a machinery-industry margin bridge, not observed EBITDA.
- e: A single automotive or industrial program can dominate plant economics.
- s5: No comprehensive six-digit control-transfer series was found.
- s5: Asset sales, facility closures, and internal reorganizations must be excluded.
- q: No source directly measures retention of AI-derived benefit.
- q: Capture differs between qualified safety-critical programs and price-sensitive commodity parts.
- d5: No complete constant-price five-year forecast was found for the industry.
- d5: Additive powder-bed fusion is a potential complement or substitute but is not the same industry process.
- o: Domestic firms can be displaced even while US end demand persists.
- o: Process substitution is counted only when it removes the outsourced powder-metallurgy operator for remaining quantity.

## Sources
- **S1** — [Fabricated Metal Product Manufacturing - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics3_332000.htm) (accessed 2026-07-22): BLS reports production occupations at 839,220 workers and 58.31% of NAICS 332 employment in May 2023, with large groups including metal/plastic workers, assemblers/fabricators, welders, and inspectors.
- **S2** — [332117: Powder Metallurgy Part Manufacturing](https://test.data.census.gov/profile/332117_-_Powder_metallurgy_part_manufacturing?codeset=naics~332117) (accessed 2026-07-22): Census defines the industry as manufacturing powder-metallurgy products using techniques such as pressing and sintering or metal injection molding and states that establishments generally make a wide range of parts on a job or order basis.
- **S3** — [Powder Bed Fusion](https://www.nist.gov/additive-manufacturing/research-areas/technologies/powder-bed-fusion) (accessed 2026-07-22): NIST describes an adjacent powder-based process and emphasizes material characterization, in-process sensing, monitoring, model-based control, performance qualification, and end-to-end digital implementation, supporting the importance of data and qualification while not representing conventional pressing/sintering.
- **S4** — [Measurement Science for Additive Manufacturing Program](https://www.nist.gov/programs-projects/measurement-science-additive-manufacturing-program) (accessed 2026-07-22): NIST states that metal additive processes form parts by melting or sintering powder, wire, or other feed forms and highlights powder characterization and registration of manufacturing and inspection data sets, illustrating adjacent process substitution and quality requirements.
