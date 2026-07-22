# 332613 — Spring Manufacturing

*v5.1 Stage 1 research memo. Run `332613-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.96 · L 0.94 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat customer-specific programs and qualification create sticky demand with improvable engineering, quoting, and quality workflows.
**Weakness:** Production labor is physical and broad domestic spring and wire output has declined, limiting demand confidence.

## Business-model lens
- Included: Independent lower-middle-market spring manufacturers that repeatedly engineer and produce springs from purchased wire, strip, or rod to external-customer drawings and performance specifications.
- Excluded: Producers selling only standardized proprietary catalog products, vertically integrated primary-metal plants, captive operations, watch and clock spring makers classified elsewhere, shell entities, non-control financing vehicles, and firms outside the normalized EBITDA band.
- Customer and revenue model: OEM and industrial customers buy repeat production runs under drawings, material, heat-treatment, tolerance, fatigue-life, testing, packaging, and delivery specifications through purchase orders or supply agreements.
- Deviation from default lens: The code contains both custom OEM spring suppliers and standardized catalog producers. The lens retains recurring customer-specific manufacturing so the screened population has a coherent outsourced-service model.

## Executive view
Custom spring manufacturing fits the outsourced-service lens relatively naturally because customers repeatedly buy drawing- and performance-specific parts. AI can improve engineering and administrative flow, but most labor remains physical and broad domestic spring and wire output has contracted sharply.

## How AI changes the work
AI can assist quote preparation, design retrieval, material selection, scheduling, purchasing, test-data review, quality documentation, maintenance triage, and customer service. Coiling, setup, forming, heat treatment, grinding, inspection execution, and packaging require machinery and physical accountability.

## Value capture
Qualified programs, tooling, fatigue performance, and reliable delivery create switching cost. OEM cost-down clauses, competitive rebids, steel indices, and should-cost models can transfer visible savings, making contract structure decisive.

## Firm availability
A meaningful share of spring firms may be customer-specific suppliers, and founder succession can create transactions. Transferability still depends on customer diversification, program approvals, engineering records, equipment condition, workforce depth, and limited owner dependence.

## Demand durability
Springs remain necessary in many physical systems, but domestic volume is exposed to imports, customer build cycles, product redesign, electrification, and inventory corrections. Critical low-volume springs should be more durable than standardized high-volume products.

## Risks and uncertainty
The case weakens if the target is a catalog seller, depends on one OEM program, lacks digital production data, needs capital automation rather than AI, or competes in declining standardized products. Fatigue liability, quality escapes, and customer cost-down expectations are material.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2189 | — | OBSERVED | — |
| n | — | 122 | — | ESTIMATE | — |
| a | 0.14 | 0.22 | 0.31 | PROXY | S2, S3 |
| rho | 0.32 | 0.49 | 0.66 | ESTIMATE | S2, S6 |
| e | 0.2 | 0.38 | 0.56 | ESTIMATE | S1 |
| s5 | 0.09 | 0.18 | 0.29 | PROXY | S4 |
| q | 0.34 | 0.52 | 0.7 | ESTIMATE | — |
| d5 | 0.77 | 0.95 | 1.12 | PROXY | S5 |
| o | 0.93 | 0.98 | 0.997 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.39 | 0.94 | 1.79 | ESTIMATE |
| F | 1.87 | 3.59 | 4.88 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.16 | 9.31 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation evidence covers NAICS 332 rather than 332613 or the outsourced subset.
- a: ILO exposure is technical potential rather than observed substitution.
- a: Existing CNC coiling, feeding, and gauging are excluded from the current opportunity.
- rho: No source measures five-year AI implementation in lower-middle-market spring manufacturers.
- rho: Digital readiness differs sharply between high-volume automotive suppliers and low-volume specialty shops.
- e: The provided firm count is margin-bridged and estimated before application of the outsourced-service lens.
- e: A custom product does not necessarily imply customer-controlled outsourced manufacturing.
- s5: Owner-age data are cross-industry, based on 2018, and count responding owners rather than firms.
- s5: Age and succession pressure do not establish sale intent or transfer completion.
- q: No public contract dataset measures pass-through for eligible spring suppliers.
- q: Automotive and other high-volume OEM programs may have lower retention than low-volume critical applications.
- d5: The index combines springs with other fabricated wire products and includes firms outside the lens.
- d5: End markets differ sharply in cyclicality and qualification barriers.
- d5: Historical output is not a direct five-year forecast.
- o: Operator requirement can persist while production shifts offshore or to larger suppliers.
- o: Product elimination and import substitution are reflected mainly in d5.

## Sources
- **S1** — [NAICS Definition: Spring Manufacturing](https://www.census.gov/naics/?details=332613&input=332613&year=2017) (accessed 2026-07-22): Census defines 332613 as manufacturing springs from purchased wire, strip, or rod and excludes watch and clock springs and vertically integrated primary-metal production.
- **S2** — [Fabricated Metal Product Manufacturing: NAICS 332](https://www.bls.gov/iag/tgs/iag332.htm) (accessed 2026-07-22): BLS reports 2025 fabricated-metal employment of 56,060 press operators, 67,090 production supervisors, 101,640 machinists, 125,250 team assemblers, and 112,520 welders.
- **S3** — [Generative AI and Jobs: Policies to Manage the Transition](https://www.ilo.org/sites/default/files/2024-08/GenAI%20and%20Jobs_Policy%20Brief_ILO.pdf) (accessed 2026-07-22): ILO reports 24% of clerical tasks at high automation exposure and 58% at medium exposure, while other occupational groups have only 1% to 4% highly exposed and no more than 25% medium-exposed tasks.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Census reports that 51% of responding owners of employer businesses were age 55 or older, based on the 2019 Annual Business Survey for data year 2018.
- **S5** — [Industrial Production: Spring and Wire Product Manufacturing](https://fred.stlouisfed.org/series/IPN3326A) (accessed 2026-07-22): The Federal Reserve annual index for NAICS 3326 declined from 88.1678 in 2021 to 66.7493 in 2025, with 2017 equal to 100.
- **S6** — [Metal and Plastic Machine Workers](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-22): BLS projects overall employment of metal and plastic machine workers to decline 7% from 2024 to 2034 and reports fabricated metal product manufacturing employs 25% of the occupation.
