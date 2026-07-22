# 311111 — Dog and Cat Food Manufacturing

*v5.1 Stage 1 research memo. Run `311111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.67 · L 0.64 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable recurring pet-food demand combined with practical AI-assisted planning, quality, maintenance, and administrative workflows in contract manufacturing.
**Weakness:** Only a minority of 311111 firms fit the outsourced-service lens, and no representative evidence directly measures their transfer rate or savings pass-through.

## Business-model lens
- Included: Independent dog- and cat-food contract manufacturers and co-packers that repeatedly formulate, process, package, or private-label food for external brands and retailers, at roughly $1-10M normalized EBITDA.
- Excluded: Own-brand manufacturers without material third-party production, captive plants, ingredient-only suppliers, distributors, retailers, financing vehicles, and businesses outside the LMM band.
- Customer and revenue model: Recurring B2B production for pet-food brands and retailers, generally priced per unit, batch, or production run under supply or co-manufacturing agreements, with formulation, packaging, quality, and compliance services embedded in the relationship.
- Deviation from default lens: Narrowed to contract manufacturing, co-packing, and private-label production because NAICS 311111 combines outsourced manufacturers with own-brand product companies whose economics are not recurring outsourced services.

## Executive view
The coherent opportunity is not pet-food brands broadly but recurring contract manufacturers and co-packers. They serve durable physical demand and face real workflow opportunities in planning, documentation, inspection analytics, maintenance, and customer operations. The central constraint is that eligible firms are only a minority of NAICS 311111 and regulated plant work limits the share of labor that can be removed safely.

## How AI changes the work
AI can reduce planning, purchasing, order-entry, documentation, reporting, customer-service, formulation-support, inspection-review, and predictive-maintenance labor. Vision systems and autonomous inspection can also avoid incremental quality and maintenance hiring. Physical batching, sanitation, material movement, packaging intervention, and accountable food-safety judgment remain operator-heavy, so exposure is meaningful but bounded.

## Value capture
A co-manufacturer can initially retain savings inside unit or batch pricing, particularly where qualification and scarce format capacity create switching costs. Over renewals, large brands and retailers will seek lower prices or explicit productivity sharing. Contract duration, customer concentration, open-book costing, and annual tendering will determine whether retention resembles the low or high case.

## Firm availability
Private-label sales are small relative to the total U.S. market, but contract production also serves branded clients and spans mainstream and niche formats. The landscape contains independent and family-owned operators and has active acquisition precedent. Still, the eligible denominator is unmeasured, and many NAICS firms are own-brand manufacturers outside the lens.

## Demand durability
Pet ownership is stable to growing, and food is an essential recurring purchase. Real volume should grow modestly, though premiumization, package downsizing, calorie density, and consumer value-seeking make sales growth an imperfect quantity signal. Software cannot replace the physical food basket; the meaningful displacement risk is customer insourcing, not digital self-service.

## Risks and uncertainty
The largest diligence gaps are the number of truly outsourced LMM firms, their customer concentration and contract repricing terms, and plant-level task baselines. Food-safety errors or recalls can erase labor savings, while older plants may require capital integration before AI works. Commodity volatility, retailer bargaining power, brand failures, format shifts, and vertical integration could weaken both retention and outsourced volume.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1195 | — | OBSERVED | — |
| n | — | 52 | — | ESTIMATE | — |
| a | 0.18 | 0.28 | 0.38 | PROXY | S1, S2 |
| rho | 0.3 | 0.48 | 0.65 | PROXY | S2, S3, S4 |
| e | 0.1 | 0.22 | 0.35 | PROXY | S5, S6 |
| s5 | 0.12 | 0.22 | 0.35 | PROXY | S6, S7 |
| q | 0.35 | 0.55 | 0.72 | ESTIMATE | S5, S6 |
| d5 | 0.98 | 1.08 | 1.18 | PROXY | S8 |
| o | 0.92 | 0.97 | 1 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.26 | 0.64 | 1.18 | PROXY |
| F | 0.78 | 2.02 | 3.21 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.02 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS data are NAICS 311100, not 311111 or the narrowed contract-manufacturing lens.
- a: Task exposure is inferred from occupations and documented use cases, not directly measured.
- a: The estimate excludes savings from conventional automation already in place.
- rho: Published examples skew toward larger and more advanced plants.
- rho: The poll populations are conference or trade-publication audiences rather than a probability sample.
- rho: Conventional robotics and AI-enabled software are intertwined in reported projects.
- e: Private-label dollar share omits contract manufacturing for third-party branded products.
- e: Firm count and revenue share differ substantially in a concentrated industry.
- e: The OC&C supplier list is explicitly non-exhaustive and mixes ownership situations.
- s5: The observed deal list is global and spans the wider pet-nutrition value chain.
- s5: Announced deals are not a random sample and may include non-control or out-of-band transactions.
- s5: Owner age and succession readiness are not directly observed.
- q: No representative contract dataset was found.
- q: Retention differs sharply between annual retailer tenders and longer branded co-manufacturing agreements.
- q: Customer concentration can overwhelm nominal switching friction.
- d5: APPA covers the whole pet industry rather than manufactured dog and cat food alone.
- d5: Nominal spending and household ownership do not directly measure constant-quality food quantity.
- d5: Obesity management, smaller pets, and premium calorie density could reduce tonnage despite sales growth.
- o: The operator share concerns the narrowed outsourced lens, not whether food itself remains physical.
- o: Large customers can vertically integrate even when regulatory accountability remains.
- o: The estimate does not assume that all current co-manufacturers retain their specific customers.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311100 Animal Food Manufacturing](https://www.bls.gov/oes/2023/may/naics4_311100.htm) (accessed 2026-07-23): Occupation employment and wage mix used to bridge the wage-weighted AI-exposure estimate, including production, transportation/material moving, office support, management, and business operations shares.
- **S2** — [Automation enhances precision, efficiency for pet food processors](https://www.petfoodindustry.com/petfood-forum/article/15666101/automation-enhances-precision-speed-in-quality-checks-for-pet-food-processors) (accessed 2026-07-23): Concrete pet-food use cases for vision, robots, autonomous inspection, OEE data, automated case packing and palletizing, predictive maintenance, and labor augmentation.
- **S3** — [How do I Start an Animal Food Business?](https://www.fda.gov/animal-veterinary/animal-foods-feeds/how-do-i-start-animal-food-business) (accessed 2026-07-23): FDA registration, CGMP, food-safety plan, preventive-control, monitoring, corrective-action, verification, traceability, and reportable-food obligations supporting implementation constraints and operator necessity.
- **S4** — [State of AI in pet food: Data, measurement lead to success](https://www.petfoodindustry.com/blogs-columns/adventures-in-pet-food/blog/15824627/state-of-ai-in-pet-food-data-measurement-lead-to-success) (accessed 2026-07-23): 2026 practitioner polling on AI use, trust, leadership priority, data quality, measurement, and scaling barriers in pet-food companies.
- **S5** — [U.S. private label pet food sales: Still small but soaring](https://www.petfoodindustry.com/blogs-columns/adventures-in-pet-food/blog/15665400/us-private-label-pet-food-sales-still-small-but-soaring) (accessed 2026-07-23): 2023 U.S. private-label pet-food sales, dollar share, growth, category shares, and evidence of established private-label and contract manufacturers.
- **S6** — [Consumer Perspectives: U.S. Pet and Pet Contract Manufacturing](https://www.occstrategy.com/wp-content/uploads/2024/10/OCC_Strategy-Consultants_Consumer-Perspectives_US-Pet-1.pdf) (accessed 2026-07-23): Fragmented co-manufacturer landscape, named mainstream and niche contract manufacturers, family ownership examples, M&A opportunity, outsourcing demand, and contract-duration observations.
- **S7** — [28 recent pet food, treat industry M&As](https://www.petfoodprocessing.net/articles/18342-28-recent-pet-food-treat-industry-m-and-as) (accessed 2026-07-23): Observed 2024 acquisition activity across pet nutrition, including manufacturers, contract/private-label assets, family-owned companies, and suppliers.
- **S8** — [U.S. Pet Industry Reaches $158 Billion in 2025, Poised for Continued Growth in 2026](https://americanpetproducts.org/news/u.s.-pet-industry-reaches-158-billion-in-2025-poised-for-continued-growth-in-2026) (accessed 2026-07-23): U.S. pet ownership, dog and cat household growth, nominal industry growth, inflation contribution, resilience, and value-seeking used as demand proxies.
