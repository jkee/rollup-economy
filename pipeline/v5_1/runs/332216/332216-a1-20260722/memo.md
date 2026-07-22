# 332216 — Saw Blade and Handtool Manufacturing

*v5.1 Stage 1 research memo. Run `332216-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.50 · L 0.88 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat blade replacement and distributor programs generate structured specification, forecast, inventory, quality, and channel workflows around essential physical products.
**Weakness:** Physical production limits AI substitution, while imports, retail line reviews, and transparent commodity comparisons constrain benefit retention.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly supplying saw blades for hand and powered saws, nonpowered handtools, edge tools, and related professional or industrial tools to external distributors, retailers, OEMs, construction suppliers, industrial users, and private-label customers.
- Excluded: Power-driven handtool manufacturing, metal-cutting machine tools and dies, captive internal tool plants, pure importers or distributors, non-control financing vehicles, and owner-dependent artisan toolmakers without transferable production and customer relationships.
- Customer and revenue model: Repeat product and replenishment sales through distributors, retailers, OEM/private-label programs, and industrial accounts, priced per tool, blade, pack, lot, or program; saw blades and edge tools have more consumable replacement than durable handtools.
- Deviation from default lens: none

## Executive view
Saw blades and handtools combine durable physical end use and consumable replacement with a bounded AI-addressable product, planning, channel, quality, and administrative layer. The industry is import- and buyer-exposed, and most labor remains tied to physical production and testing.

## How AI changes the work
AI can manage product and distributor data, assist specifications and costing, forecast demand, plan inventory and sourcing, summarize tests and claims, draft catalog content, and support customers. Forming, machining, heat treatment, grinding, coating, assembly, inspection, performance testing, packing, and final release remain physical.

## Value capture
Performance, durability, specialized geometry, private-label integration, service, and distributor relationships can protect gains. Retail line reviews, bids, rebates, import comparisons, and transparent commodity SKUs share away a substantial portion over five years.

## Firm availability
The supplied dataset estimates 198 firms in the target band, but actual eligibility requires verifying domestic manufacturing, repeat external accounts, normalized earnings, brand versus OEM/private-label mix, channel concentration, and owner dependence. Consumable and durable products have different economics but similar supplier channels.

## Demand durability
Construction, maintenance, repair, fabrication, forestry, and woodworking still require physical blades and handtools; worn cutting products replenish repeatedly. Durable-tool longevity, imports, automation of end-user tasks, powered substitutes, and cyclicality temper growth.

## Risks and uncertainty
The main unknowns are six-digit labor mix, imported versus domestic content, product and channel mix, current workflow automation, distributor concentration, safety and product-liability exposure, and true LMM margins. The supplied inputs mix vintages and use a machinery margin bridge.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2381 | — | OBSERVED | — |
| n | — | 198 | — | ESTIMATE | — |
| a | 0.1 | 0.2 | 0.32 | PROXY | S1, S2 |
| rho | 0.27 | 0.46 | 0.65 | ESTIMATE | S3, S4 |
| e | 0.49 | 0.65 | 0.79 | ESTIMATE | S2 |
| s5 | 0.09 | 0.18 | 0.3 | ESTIMATE | — |
| q | 0.3 | 0.52 | 0.72 | ESTIMATE | S2, S3 |
| d5 | 0.91 | 1.05 | 1.2 | PROXY | S2, S5 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.26 | 0.88 | 1.98 | ESTIMATE |
| F | 3.66 | 5.12 | 6.22 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.55 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is for all fabricated metal manufacturing, not 332216.
- a: No source measures current AI deployment or task exposure in this industry.
- rho: This is bounded judgment rather than an observed five-year implementation rate.
- rho: Safety evidence concerns tool use and guarding, not AI adoption in manufacturing.
- e: The supplied n uses receipts and a machinery-industry margin bridge rather than observed EBITDA.
- e: The code mixes consumable saw blades with longer-lived handtools and edge tools.
- s5: No comprehensive six-digit control-transfer series was found.
- s5: Brand licensing, distributor acquisitions, asset sales, and internal reorganizations must be excluded unless operating control transfers.
- q: No source directly measures retention of AI-derived benefit.
- q: Specialized industrial blades may have more pricing power than commodity handtools.
- d5: Construction employment is an indirect downstream proxy, not tool consumption.
- d5: Domestic production can diverge from US end demand because of imports and reshoring.
- o: Domestic operators can be displaced while US tool consumption persists.
- o: Elimination of a task belongs in d5; o addresses who supplies tools for remaining work.

## Sources
- **S1** — [Fabricated Metal Product Manufacturing - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics3_332000.htm) (accessed 2026-07-22): BLS reports production occupations at 839,220 workers and 58.31% of NAICS 332 employment in May 2023, transportation/material moving at 6.51%, assemblers/fabricators at 10.84%, CNC workers at 5.17%, and inspectors at 3.26%.
- **S2** — [2022 NAICS Definition: 332216 Saw Blade and Handtool Manufacturing](https://www.census.gov/naics/?details=3322&input=3322&year=2022) (accessed 2026-07-22): Census defines the industry as manufacturing saw blades of all types, including blades for powered saws, and nonpowered handtools and edge tools.
- **S3** — [Hand and Power Tools - Overview](https://www.osha.gov/hand-power-tools) (accessed 2026-07-22): OSHA states that hand and power tools are common across nearly every industry, enable otherwise difficult or impossible tasks, and can cause severe injuries if used or maintained improperly.
- **S4** — [1926.300 - General Requirements for Tools](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.300) (accessed 2026-07-22): OSHA requires employer- or employee-furnished hand and power tools to be maintained in safe condition and requires guards for power-operated tools designed to accommodate them, supporting operator and safety accountability.
- **S5** — [Construction Laborers and Helpers](https://www.bls.gov/ooh/construction-and-extraction/construction-laborers-and-helpers.htm) (accessed 2026-07-22): BLS projects construction laborer and helper employment to grow 7% from 2024 to 2034; used only as an indirect downstream activity proxy for part of tool demand.
