# 326122 — Plastics Pipe and Pipe Fitting Manufacturing

*v5.1 Stage 1 research memo. Run `326122-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.07 · L 0.48 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Large infrastructure replacement needs underpin recurring physical pipe demand while AI improves quality and uptime.
**Weakness:** Low labor intensity, existing line automation, and commodity price transparency limit the retained labor upside.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers repeatedly supplying plastic pipe, conduit, and fittings to distributors, utilities, contractors, agricultural users, and industrial customers.
- Excluded: Captive pipe-making units, installers and distributors without manufacturing, resin producers, shell entities, non-control financing vehicles, and manufacturers primarily classified in hose, profile, or other plastics codes.
- Customer and revenue model: Repeat business-to-business product sales under purchase orders, distributor programs, project bids, and supply agreements, generally priced per length, fitting, weight, or shipment with resin and freight adjustments.
- Deviation from default lens: none

## Executive view
Plastic pipe and fitting manufacturing has durable physical demand and repeat external customers, with infrastructure replacement providing a demand floor. AI opportunity is real around inspection, maintenance, planning, quoting, and administration, but continuous extrusion is already substantially controlled and core plant work remains physical.

## How AI changes the work
DOE identifies automated visual quality control, manufacturing characterization, operational optimization, and predictive maintenance as practical AI uses. In pipe plants these can reduce manual checks, downtime, scrap, planning work, and exception handling, while language models can accelerate specifications, certifications, quotes, and customer documentation. Safety, product standards, data integration, and release accountability limit full substitution.

## Value capture
Savings can accrue during contract and quote periods, particularly for differentiated fittings, fabricated specials, reliable delivery, and approved-vendor relationships. Commodity pipe prices are visible and often rebid, while resin-index clauses and powerful distributors or utilities can force sharing, producing only moderate long-run retention.

## Firm availability
The frozen LMM population is modest. Most independent manufacturers fit the recurring supply lens, but mixed distributor-fabricators and captive plants require verification. The transfer estimate reflects ordinary private-company succession and sale activity while excluding internal transfers, minority deals, closures, and failed processes.

## Demand durability
EPA reports $630.1 billion of clean-water infrastructure needs and $625.0 billion of drinking-water needs over twenty years; conveyance repair and new systems alone account for $151.1 billion in the clean-water survey. This does not equal pipe purchases, but together with BLS's modest plastics-output growth it supports stable-to-growing five-year quantity demand, subject to funding and material-share uncertainty.

## Risks and uncertainty
Public evidence is broader than 326122 and does not reveal plant automation baselines or contract terms. Commodity exposure, resin volatility, housing and construction cycles, utility funding delays, imports, customer concentration, and substitution by other materials can erode returns. A highly automated plant offers less remaining labor opportunity, while an under-digitized plant may require more capex and change management than the savings justify.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1397 | — | OBSERVED | — |
| n | — | 59 | — | ESTIMATE | — |
| a | 0.11 | 0.19 | 0.28 | PROXY | S1, S2 |
| rho | 0.28 | 0.45 | 0.62 | ESTIMATE | S2 |
| e | 0.64 | 0.78 | 0.88 | ESTIMATE | — |
| s5 | 0.12 | 0.21 | 0.33 | ESTIMATE | — |
| q | 0.33 | 0.51 | 0.68 | ESTIMATE | — |
| d5 | 0.98 | 1.08 | 1.2 | PROXY | S3, S4, S5 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.48 | 0.97 | ESTIMATE |
| F | 2.75 | 3.81 | 4.66 | ESTIMATE |
| C | 6.60 | 10.00 | 10.00 | ESTIMATE |
| D | 9.41 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is four-digit NAICS 326100 rather than 326122.
- a: Task exposure is inferred rather than measured.
- a: The estimate may miss differences between continuous pipe extrusion and more labor-intensive fitting fabrication or molding.
- rho: No five-year implementation study specific to plastic pipe was found.
- rho: Adoption may be faster at standardized, high-volume plants and slower for short-run fittings or fabricated specials.
- e: Eligibility is judged, not observed, and the frozen firm count is margin-bridged.
- e: Some fitting businesses blend distribution, fabrication, installation, and manufacturing in ways public NAICS records do not reveal.
- s5: No reliable six-digit transaction-rate or ownership-age measure was located.
- s5: Consolidation headlines can overrepresent larger strategic deals and undercount small private transfers.
- q: Commercial terms were not observed.
- q: Retention likely differs sharply between commodity straight pipe and specialized fittings or certified custom systems.
- d5: Infrastructure needs are not committed spending and include much more than pipe.
- d5: BLS output is four-digit and broad.
- d5: Material share between plastic, ductile iron, steel, concrete, and rehabilitation technologies can change.
- o: No source directly measures the operator-required share.
- o: Automation can shrink labor per unit without eliminating accountable manufacturing ownership.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 326100 Plastics Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-22): Observed broad plastics-product occupational and wage mix, including 605,750 total workers, production concentrations, management and business shares, extrusion, molding, packing, and material-handling employment.
- **S2** — [AI for Energy: Opportunities for a Modern Grid and Clean Energy Economy](https://www.energy.gov/sites/default/files/2024-04/AI%20EO%20Report%20Section%205.2g%28i%29_043024.pdf) (accessed 2026-07-22): DOE describes AI manufacturing applications including automated visual quality control, advanced characterization, operational optimization, predictive maintenance using IoT sensors, and efficient material sorting.
- **S3** — [Clean Watersheds Needs Survey](https://www.epa.gov/cwns) (accessed 2026-07-22): EPA's 2022 survey reports $630.1 billion in total clean-water infrastructure needs over twenty years, including $151.1 billion for conveyance repair and new conveyance systems, $115.3 billion for stormwater, and 17,544 reported publicly owned treatment works.
- **S4** — [Seventh Drinking Water Infrastructure Needs Survey and Assessment](https://www.epa.gov/system/files/documents/2023-09/Seventh%20DWINSA_September2023_Final.pdf) (accessed 2026-07-22): EPA reports $625.0 billion of state drinking-water infrastructure needs, with $273.1 billion for medium systems, $235.2 billion for large systems, and $100.1 billion for small systems.
- **S5** — [Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects real output for NAICS 326100 from $190.7 billion in 2024 to $212.4 billion in 2034, a 1.1% compound annual increase.
