# 332119 — Metal Crown, Closure, and Other Metal Stamping (except Automotive)

*v5.1 Stage 1 research memo. Run `332119-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.88 · L 0.76 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring customer programs create repeat quote, drawing, change-control, planning, inspection, and quality workflows with supplier switching friction.
**Weakness:** Most labor is physical, and high-volume customers can force productivity gains into price through cost downs and rebids.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly stamping metal crowns, bottle caps, canning lids and rings, other unfinished non-automotive metal stampings, and spun unfinished metal products for external packaging, appliance, electrical, industrial, consumer-product, and equipment customers.
- Excluded: Automotive stampings, metal cans and finished containers, coins, captive internal stamping lines, manufacturers classified by a further-fabricated finished product, pure distributors, non-control financing vehicles, and operations that cannot transfer independently of the owner.
- Customer and revenue model: Recurring releases and production programs priced per part, thousand units, pound, lot, or program, commonly supported by customer-specific dies, specifications, quality documentation, and metal-price adjustments.
- Deviation from default lens: none

## Executive view
Non-automotive metal stamping and closures are repeat physical manufacturing programs with a bounded but useful AI-addressable commercial, planning, engineering-document, and quality layer. Customer-specific tooling and qualifications support retention, while the production core remains press-, material-, and inspection-intensive.

## How AI changes the work
AI can parse RFQs and drawings, compare revisions, assist quotes and routings, recommend schedules and coil purchases, organize certificates and inspection data, draft corrective actions, and handle routine customer communication. Die work, press setup, coil handling, stamping or spinning, deburring, maintenance, packing, and final inspection remain physical.

## Value capture
Dies, quality history, high-speed process know-how, and approved supplier status create switching costs. Metal adjustments, annual productivity commitments, competitive resourcing, and powerful packaging or industrial procurement organizations pass some benefit to customers.

## Firm availability
The supplied dataset estimates 473 firms in the economic band, but actual eligibility requires verification of external repeat programs, standalone ownership, normalized earnings, tooling rights, customer concentration, equipment condition, and owner dependence. The combined closure and miscellaneous-stamping code adds mix uncertainty.

## Demand durability
Physical packaging closures and stamped components should persist across food, beverage, appliance, electrical, and industrial uses. Lightweighting, alternative materials, reuse, imports, insourcing, and product redesign are the main demand threats rather than software elimination.

## Risks and uncertainty
Key unknowns are six-digit occupation mix, closure-versus-other-stamping mix, current automation, program and customer concentration, contract cost-down terms, die ownership, and true LMM margins. The supplied inputs mix vintages and apply a machinery margin bridge.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2305 | — | OBSERVED | — |
| n | — | 473 | — | ESTIMATE | — |
| a | 0.09 | 0.18 | 0.29 | PROXY | S1, S2 |
| rho | 0.27 | 0.46 | 0.65 | ESTIMATE | S2, S3 |
| e | 0.57 | 0.73 | 0.85 | ESTIMATE | S2 |
| s5 | 0.1 | 0.19 | 0.31 | ESTIMATE | — |
| q | 0.34 | 0.56 | 0.75 | ESTIMATE | S2 |
| d5 | 0.89 | 1.03 | 1.18 | ESTIMATE | S2, S4 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.22 | 0.76 | 1.74 | ESTIMATE |
| F | 5.36 | 6.75 | 7.77 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 8.46 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is for the three-digit fabricated-metal sector, not 332119.
- a: No source measures current AI adoption or task exposure in stamping plants.
- rho: This is bounded judgment rather than an observed five-year adoption rate.
- rho: Conventional press automation is excluded unless AI is the operative substitution mechanism.
- e: The provided n relies on receipts and a machinery-industry margin bridge rather than observed EBITDA.
- e: The code combines packaging closures and diverse unfinished stampings with different commercial structures.
- s5: No comprehensive six-digit control-transfer series was found.
- s5: Asset auctions, customer-program transfers, and internal reorganizations must be excluded.
- q: No source directly measures retention of AI-derived benefit.
- q: Commodity crowns and high-volume stampings may face more pass-through than specialty low-volume parts.
- d5: EPA packaging data cover steel containers broadly, not metal closures or all 332119 products, and are historical rather than a forecast.
- d5: No complete constant-price industry demand forecast was found.
- o: Domestic operators can be displaced even when US end demand persists.
- o: Material or packaging elimination belongs in d5; o addresses who supplies remaining physical quantity.

## Sources
- **S1** — [Fabricated Metal Product Manufacturing - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics3_332000.htm) (accessed 2026-07-22): BLS reports 1,439,340 NAICS 332 workers in May 2023, including 57,710 cutting, punching, and press machine operators (4.01%), 46,870 inspectors/testers (3.26%), and a broad production majority.
- **S2** — [2022 NAICS Definition: 332119 Metal Crown, Closure, and Other Metal Stamping (except Automotive)](https://www.census.gov/naics/?details=332&input=332&year=2022) (accessed 2026-07-22): Census defines the industry as stamping metal crowns and closures such as bottle caps and canning lids/rings and manufacturing other unfinished non-automotive, non-can, non-coin metal stampings and spun products.
- **S3** — [DOE Module 3C: Sheet Metal Stamping](https://www.energy.gov/sites/default/files/2021-07/Module_3C.pdf) (accessed 2026-07-22): DOE describes stamping presses and dies as tools that shape and cut sheet metal into finished parts and lists punching, blanking, embossing, bending, flanging, and coining, supporting the physical-process assessment.
- **S4** — [Containers and Packaging: Product-Specific Data](https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/containers-and-packaging-product-specific) (accessed 2026-07-22): EPA reports 2.2 million tons of steel food cans, other cans, and steel packaging generated in 2018 and 1.6 million tons recycled, a 73.8% recycling rate; used as broad packaging context, not a 332119 demand measure.
