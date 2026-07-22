# 332721 — Precision Turned Product Manufacturing

*v5.1 Stage 1 research memo. Run `332721-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.08 · L 0.62 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Job-order manufacturing, repeat qualified programs, and digital CNC and inspection data create a strong base for AI-assisted operating workflows.
**Weakness:** Direct production is already automated, while broad output weakness and OEM cost-down pressure limit incremental labor and commercial upside.

## Business-model lens
- Included: Independent lower-middle-market precision turned manufacturers machining products of metal, plastic, or composite materials on a recurring job or order basis for external customers using automatic screw machines, rotary transfer machines, CNC lathes, or turning centers.
- Excluded: Captive plants, non-recurring prototype-only shops without repeat programs, manufacturers of standardized fasteners classified elsewhere, shell entities, non-control financing vehicles, and firms outside the normalized EBITDA band.
- Customer and revenue model: OEM and industrial customers buy recurring precision components under drawings, material, tolerance, inspection, traceability, packaging, and delivery requirements through purchase orders, blanket orders, or supply agreements.
- Deviation from default lens: none

## Executive view
Precision turned manufacturing closely matches the recurring outsourced-service lens because Census defines it as job- or order-based production. The large estimated firm population and digital production environment create real workflow opportunity, although CNC already automates much of the direct cycle and broad industry output has weakened.

## How AI changes the work
AI can improve RFQ parsing, estimating, manufacturability review, routing, CNC programming support, scheduling, tool-life analysis, inspection review, quality documentation, and customer communication. Setup, machine tending, maintenance, deburring, washing, and physical metrology remain operator- and equipment-dependent.

## Value capture
Qualified repeat programs, process capability, tooling knowledge, and delivery performance create switching cost. OEM cost-down clauses, competitive RFQs, metal indices, and should-cost models can transfer visible savings, so value is more durable when it improves capacity, quality, and lead time.

## Firm availability
Most independent precision turners fit the service model, and founder succession can generate seller supply. Transferability depends on repeat-program diversification, programmers and setup talent, quality systems, equipment condition, customer approvals, and reduced reliance on the owner.

## Demand durability
Turned components remain necessary across diverse physical products, with specialized qualification supporting retention. Current broad output is weak, and demand remains exposed to program cycles, imports, inventory corrections, additive manufacturing, and redesign.

## Risks and uncertainty
The case weakens if a target has mostly one-off prototypes, one dominant customer, obsolete or disconnected machines, undocumented tribal programming knowledge, heavy deferred capital needs, or contracts that force annual savings through. Quality escapes and cyber compromise of customer drawings are material risks.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1235 | — | OBSERVED | — |
| n | — | 1201 | — | ESTIMATE | — |
| a | 0.15 | 0.24 | 0.34 | PROXY | S2, S3, S6 |
| rho | 0.34 | 0.52 | 0.69 | ESTIMATE | S6 |
| e | 0.52 | 0.7 | 0.84 | ESTIMATE | S1, S7 |
| s5 | 0.09 | 0.18 | 0.3 | PROXY | S4 |
| q | 0.35 | 0.54 | 0.72 | ESTIMATE | — |
| d5 | 0.8 | 0.98 | 1.16 | PROXY | S5, S6 |
| o | 0.93 | 0.98 | 0.997 | ESTIMATE | S1, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.25 | 0.62 | 1.16 | ESTIMATE |
| F | 6.51 | 8.08 | 9.19 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.44 | 9.60 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation counts cover NAICS 332 rather than this six-digit industry.
- a: ILO exposure is technical potential rather than observed substitution.
- a: Existing CNC, bar feeding, probing, and robotic handling are not part of current unautomated opportunity.
- rho: No source measures five-year AI implementation in eligible precision-turning firms.
- rho: Modern connected turning centers and older cam-driven screw-machine fleets have very different readiness.
- e: The provided firm count is margin-bridged and may not align precisely with the stated EBITDA band.
- e: Job-order manufacturing can still be project-like if customers do not place repeat production orders.
- s5: Owner-age data are cross-industry, based on 2018, and count responding owners rather than firms.
- s5: Retirement need does not establish sale intent, business quality, or transaction completion.
- q: No public contract dataset measures AI benefit pass-through for eligible firms.
- q: Retention differs between highly qualified critical parts and readily portable commodity turned components.
- d5: The output series combines machine shops, turned products, and fasteners and includes firms outside the lens.
- d5: Historical output is not a direct five-year forecast.
- d5: Aerospace, automotive, medical, and general-industrial programs have different cycles and qualification barriers.
- o: Operator requirement can persist while production shifts to larger or offshore suppliers.
- o: Demand loss and imports are reflected mainly in d5.

## Sources
- **S1** — [Precision Turned Product Manufacturing Profile](https://data.census.gov/profile/332721_-_Precision_turned_product_manufacturing?codeset=naics~332721) (accessed 2026-07-22): Census defines 332721 as machining precision products of all materials on a job or order basis, generally in large volumes using automatic screw machines, rotary transfer machines, CNC lathes, or turning centers.
- **S2** — [Fabricated Metal Product Manufacturing: NAICS 332](https://www.bls.gov/iag/tgs/iag332.htm) (accessed 2026-07-22): BLS reports 2025 fabricated-metal employment of 56,060 press operators, 67,090 production supervisors, 101,640 machinists, 125,250 team assemblers, and 112,520 welders.
- **S3** — [Generative AI and Jobs: Policies to Manage the Transition](https://www.ilo.org/sites/default/files/2024-08/GenAI%20and%20Jobs_Policy%20Brief_ILO.pdf) (accessed 2026-07-22): ILO reports 24% of clerical tasks at high automation exposure and 58% at medium exposure, while other occupational groups have only 1% to 4% highly exposed and no more than 25% medium-exposed tasks.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Census reports that 51% of responding owners of employer businesses were age 55 or older, based on the 2019 Annual Business Survey for data year 2018.
- **S5** — [Real Sectoral Output: Machine Shops, Turned Product, and Fasteners](https://fred.stlouisfed.org/series/IPUEN3327T010000000) (accessed 2026-07-22): BLS real sectoral output for NAICS 3327 declined from an index of 102.578 in 2022 to 84.601 in 2025, with 2017 equal to 100.
- **S6** — [Machinists and Tool and Die Makers](https://www.bls.gov/ooh/production/machinists-and-tool-and-die-makers.htm) (accessed 2026-07-22): BLS projects machinist and tool-and-die employment to decline 2% from 2024 to 2034, describes use of CAD/CAM, CNC tools, and computerized measuring machines, and expects 34,200 openings annually from replacement needs.
- **S7** — [2022 Census Manufacturing Product Classification Form for 33271](https://bhs.econ.census.gov/ombpdfs2022/export/2022_MC-33271_mu.pdf) (accessed 2026-07-22): Census separately identifies automotive and other precision turned products made on CNC equipment or screw machines and contract precision turning performed with materials owned by customers.
