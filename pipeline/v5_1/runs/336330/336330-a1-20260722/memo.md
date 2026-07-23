# 336330 — Motor Vehicle Steering and Suspension Components (except Spring) Manufacturing

*v5.1 Stage 1 research memo. Run `336330-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.07 · L 0.51 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent physical content per vehicle and an aging fleet combine with targeted AI productivity in engineering and overhead.
**Weakness:** Only a modest share of total work is plausibly AI-automatable, and powerful customers are positioned to claim much of the savings.

## Business-model lens
- Included: Independent U.S. manufacturers of steering and suspension components other than springs, including control arms, steering linkages, knuckles, shock absorbers, struts, stabilizer assemblies, and related machined or fabricated subassemblies.
- Excluded: Captive OEM operations; spring manufacturing; vehicle assembly; wholesale distribution; pure repair shops; software-only businesses; and businesses whose economics are dominated by unrelated auto-parts categories.
- Customer and revenue model: Repeat B2B sales to vehicle OEMs, tier-one integrators, distributors, and aftermarket channels, screened for firms plausibly in the $1-10 million EBITDA lower-middle-market range and serving external customers.
- Deviation from default lens: none

## Executive view
This is an embodied, safety-critical manufacturing category with durable vehicle content and a sizable aftermarket. AI offers useful operating leverage in engineering and overhead, but the directly automatable task base is limited and customer bargaining power constrains capture.

## How AI changes the work
Near-term gains are likeliest in quoting, work instructions, supplier communication, maintenance analytics, quality-document preparation, vision-inspection triage, production scheduling, and engineering search. Welding, machining, assembly, testing, material movement, and final safety accountability remain physical or tightly supervised.

## Value capture
Qualified products and switching costs support retention, but concentrated OEM and tier customers commonly exert price pressure. Capture improves with proprietary processes, difficult tolerances, aftermarket exposure, diversified programs, and evidence that AI raises quality or capacity rather than merely lowering quoted cost.

## Firm availability
The frozen firm-count estimate indicates a real but not expansive lower-middle-market universe. Independent specialists exist alongside captive and very large tier suppliers; diligence should distinguish genuine manufacturers from distributors and diversified parts groups.

## Demand durability
Steering and suspension remain necessary across internal-combustion, hybrid, and electric vehicles. The aging installed fleet supports replacement demand, while vehicle production cyclicality, platform losses, and technology-driven mix shifts create meaningful firm-level volatility.

## Risks and uncertainty
Key uncertainties are the six-digit task mix, speed of adoption in smaller plants, customer pass-through, program concentration, warranty exposure, and whether electrification changes component value per vehicle. The broad BLS occupation proxy and fleet-age bridge should be replaced with plant and segment data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1323 | — | OBSERVED | — |
| n | — | 69 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.27 | PROXY | S1 |
| rho | 0.36 | 0.54 | 0.69 | ESTIMATE | S1 |
| e | 0.54 | 0.71 | 0.84 | ESTIMATE | S1 |
| s5 | 0.11 | 0.22 | 0.34 | ESTIMATE | S1, S4 |
| q | 0.32 | 0.49 | 0.65 | ESTIMATE | S4 |
| d5 | 0.95 | 1.03 | 1.13 | PROXY | S2, S3, S4 |
| o | 0.94 | 0.99 | 1 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.19 | 0.51 | 0.99 | ESTIMATE |
| F | 2.62 | 3.97 | 4.87 | ESTIMATE |
| C | 6.40 | 9.80 | 10.00 | ESTIMATE |
| D | 8.93 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The source is four-digit NAICS 3363, not six-digit 336330.
- a: Occupation shares are not task shares and do not isolate generative-AI exposure.
- rho: Capability is distinct from adoption and is especially uncertain over five years.
- e: Savings may appear as throughput or quality improvement rather than headcount reduction.
- s5: Large tier suppliers may adopt faster than the target firm population.
- q: Aftermarket-branded products can retain more value than build-to-print OEM work.
- d5: Historic fleet age does not measure component replacement frequency.
- d5: Mix shifts can redistribute value across incumbent component designs.
- o: This excludes ordinary competitive and electrification effects already reflected in demand durability.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 336300](https://www.bls.gov/oes/2023/may/naics4_336300.htm) (accessed 2026-07-22): Broader motor-vehicle-parts employment of 557,020, including 132,430 miscellaneous assemblers (23.77%), 102,540 metal/plastic workers (18.41%), and 24,900 engine and other machine assemblers (4.47%).
- **S2** — [Table 1-26: Average Age of Automobiles and Trucks in Operation in the United States](https://www.bts.gov/archive/publications/national_transportation_statistics/table_01_26) (accessed 2026-07-22): Average age of all light vehicles increased from 8.4 years in 1995 to 11.4 years in 2014, supporting an aging installed-base demand proxy.
- **S3** — [Lightweight and Propulsion Materials](https://www.energy.gov/cmei/vehicles/lightweight-and-propulsion-materials) (accessed 2026-07-22): DOE states lightweight materials are especially important for electric and hybrid vehicles and that substitution can decrease component weight by 10-60%, evidencing continued physical-component redesign rather than disappearance.
- **S4** — [Part 573 Safety Recall Report 24V-084](https://static.nhtsa.gov/odi/rcl/2024/RCLRPT-24V084-5287.PDF) (accessed 2026-07-22): A 2024 suspension and steering component hanger defect could fatigue and fail and affect primary steering ability, illustrating safety criticality, validation needs, and ongoing physical-component demand.
