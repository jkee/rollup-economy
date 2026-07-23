# 339115 — Ophthalmic Goods Manufacturing

*v5.1 Stage 1 research memo. Run `339115-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.29 · L 1.61 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring prescription changes, age-related presbyopia, contact-lens replacement, and eye-protection needs sustain physical product demand.
**Weakness:** Vertical integration, imports, online sellers, and concentrated retail and vision-plan channels exert persistent price and volume pressure on small manufacturers.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers of prescription eyeglasses outside retail settings, ophthalmic lenses, contact lenses, frames, sunglasses, standard-power reading glasses, and protective eyewear, including manufacturer-attributable finishing, coating, parts, warranty, and service revenue.
- Excluded: Retail optical stores that grind lenses, intraocular lenses, molded glass or plastic lens blanks, pure distributors, captive internal units, fashion brands without manufacturing activity, and service businesses that do not manufacture in-scope ophthalmic goods.
- Customer and revenue model: Repeat outsourced revenue from optical retailers, optometrists, ophthalmologists, laboratories, distributors, employers, safety programs, government buyers, and branded-product customers through prescription replenishment, lens and frame programs, coatings, contact-lens replacement, protective eyewear, and warranties.
- Deviation from default lens: none

## Executive view
Ophthalmic goods serve a very large, recurring corrective-vision and eye-protection need, but the eligible LMM manufacturing pool is small and exposed to vertically integrated groups, imports, retail concentration, and online price pressure. AI can improve digital ordering, design, planning, inspection, and service while physical production remains necessary.

## How AI changes the work
The strongest applications are prescription-order handling, lens and frame design, demand planning, scheduling, customer service, documentation, machine vision, and quality analytics. Grinding, coating, molding, assembly, testing, verification, and release limit substitution.

## Value capture
Turnaround, accuracy, coatings, fit, safety certification, brand, design, and retailer relationships support retention. Large optical groups, insurers and vision plans, retail chains, imports, private label, and online channels constrain it.

## Firm availability
True independent manufacturers often have repeat demand, but retailers, distributors, fashion brands, captive units, adjacent lens businesses, and out-of-band firms reduce a small estimated pool. Exact transfer data are sparse.

## Demand durability
Refractive error affects a vast population and presbyopia accompanies aging, supporting replacement lenses, contacts, readers, and frames. Imports, surgery, retail consolidation, price competition, and durable products limit domestic growth.

## Risks and uncertainty
Principal risks are channel concentration, imports, insurer and retailer pricing, fashion and inventory cycles, regulatory or prescription error, remakes, product liability, corrective surgery, consolidation, and the broad demand proxy.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3156 | — | OBSERVED | — |
| n | — | 47 | — | ESTIMATE | — |
| a | 0.17 | 0.29 | 0.42 | PROXY | S2, S3, S5 |
| rho | 0.23 | 0.44 | 0.63 | PROXY | S3, S5 |
| e | 0.46 | 0.68 | 0.82 | ESTIMATE | S1 |
| s5 | 0.12 | 0.25 | 0.38 | ESTIMATE | — |
| q | 0.36 | 0.57 | 0.75 | ESTIMATE | S1, S5, S6 |
| d5 | 0.97 | 1.09 | 1.23 | PROXY | S4, S6 |
| o | 0.94 | 0.985 | 0.998 | ESTIMATE | S1, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.49 | 1.61 | 3.34 | PROXY |
| F | 2.06 | 3.53 | 4.42 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 9.12 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS data cover all medical equipment and supplies rather than the small ophthalmic-goods industry.
- a: General manufacturing AI use cases do not establish realized task savings in prescription and regulated product workflows.
- rho: NIST adoption evidence spans all manufacturing and includes chatbots as well as operational applications.
- rho: FDA quality-system applicability varies across ophthalmic product types and specific exemptions.
- e: No public source measures the exact intersection of industry classification, independence, recurring external revenue, and the target EBITDA band.
- e: Only about 47 firms are estimated in the size band, so classification errors materially change the eligible share.
- s5: This is a structured estimate without an exact-industry transaction denominator.
- s5: The small eligible firm pool and presence of large vertically integrated optical groups make annual transfer rates volatile.
- q: Capture differs materially between custom prescription lenses, contact lenses, premium frames, commodity readers and sunglasses, and protective eyewear.
- q: The estimate concerns retained gross benefit rather than reported accounting margin.
- d5: BLS projects the broad NAICS 339100 industry rather than ophthalmic goods and may embed higher-value product mix.
- d5: NEI establishes the size and persistence of corrective-vision need but does not forecast domestic manufacturer shipments.
- o: This estimates persistence of an accountable operator of the lens's kind, not survival of each incumbent brand, laboratory, or product line.
- o: Digital surfacing and automated finishing can consolidate production into fewer operators even while physical demand persists.

## Sources
- **S1** — [339115: Ophthalmic Goods Manufacturing](https://data.census.gov/profile/339115_-_Ophthalmic_Goods_Manufacturing?codeset=naics~339115) (accessed 2026-07-22): Exact industry scope, examples, adjacent-industry exclusions, and employer-establishment context.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Medical Equipment and Supplies Manufacturing](https://www.bls.gov/oes/2023/may/naics4_339100.htm) (accessed 2026-07-22): Broad medical-equipment occupational structure used to bridge task exposure.
- **S3** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing: Text Only](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Manufacturing AI adoption, use cases, expected expansion, and barriers involving data, cost, skills, cybersecurity, and legacy systems.
- **S4** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Official broad medical-equipment and supplies manufacturing output projection used for the five-year demand bridge.
- **S5** — [Quality Management System Regulation (QMSR)](https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr) (accessed 2026-07-22): Finished-device quality-system applicability, ISO 13485 incorporation, risk management, and manufacturer accountability.
- **S6** — [Refractive Errors](https://www.nei.nih.gov/eye-health-information/eye-conditions-and-diseases/refractive-errors) (accessed 2026-07-22): Scale and types of refractive error, aging-related presbyopia, and eyeglasses or contact lenses as corrective treatments.
