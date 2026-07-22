# 311119 — Other Animal Food Manufacturing

*v5.1 Stage 1 research memo. Run `311119-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.21 · L 0.32 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical feed demand plus practical AI uses in planning, predictive maintenance, quality control, traceability, and mill administration.
**Weakness:** The qualifying outsourced-firm share is unmeasured, and commodity-like per-ton pricing may pass efficiency gains back to concentrated customers.

## Business-model lens
- Included: Independent custom, toll, contract, and private-label manufacturers of livestock, poultry, equine, aquaculture, and other non-dog/cat feeds, premixes, concentrates, and supplements that repeatedly produce for external customers at roughly $1-10M normalized EBITDA.
- Excluded: Proprietary feed brands without material third-party production, captive or on-farm mills, vertically integrated livestock-company mills, ingredient traders, distributors, dog/cat food manufacturers, pharmaceutical makers, and businesses outside the LMM band.
- Customer and revenue model: Recurring B2B production priced per ton, batch, formula, package, or supply program for farmers, livestock operators, dealers, and animal-nutrition brands; services may include formulation, blending, pelleting, packaging, testing, traceability, and delivery.
- Deviation from default lens: Narrowed to custom, toll, contract, and private-label production because NAICS 311119 combines outsourced manufacturing with proprietary feed products and captive or integrated mill activity that do not represent external recurring services.

## Executive view
The coherent opportunity is custom, toll, contract, and private-label feed production, not all product makers or captive mills in 311119. Demand is durable but mature, with USDA pointing to slow feed-volume growth. AI can improve planning, quality, maintenance, traceability, and administrative work, while the industry's low compensation intensity and physical plant operations bound the absolute labor opportunity.

## How AI changes the work
Smart-mill systems can connect silo demand, production schedules, formulation, sensor data, quality deviations, maintenance alerts, and traceability. Back-office order handling, procurement, documentation, and customer support are also exposed. Grinding, mixing, pelleting, sanitation, load-out, delivery, and food-safety accountability remain physical or supervised, so implementation should augment operators more often than remove the operating entity.

## Value capture
Initial savings can stay with the manufacturer inside per-ton or per-batch prices, especially in specialty formulations and constrained capacity. Bulk feed customers know input costs and can rebid frequently, so renewal repricing should share a large portion of benefits. Contract structure and customer concentration are more important than the technology in determining retained value.

## Firm availability
The population includes family and independent operators and has visible strategic and financial-buyer transactions. Yet public evidence does not quantify how many frozen-band firms derive most revenue from qualifying outsourced production. Proprietary brands, captive mills, and integrated livestock operations must be excluded before treating the dataset firm count as transferable opportunity.

## Demand durability
Livestock, dairy, poultry, equine, aquaculture, and specialty animals continue to require physical feed. USDA's baseline suggests modest growth in feed grain use and animal output over the horizon. Feed efficiency, species mix, disease, drought, and customer insourcing can offset that growth for independent mills, but software-only substitution is not credible.

## Risks and uncertainty
The main uncertainties are eligibility, contract repricing, plant age and sensor readiness, and customer make-versus-buy behavior. Commodity volatility, customer credit, local livestock cycles, contamination, recalls, dust and safety hazards, and capital-intensive modernization can overwhelm modeled labor savings. Selected trade cases likely make adoption and transfer conditions look better than the median regional mill.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0642 | — | OBSERVED | — |
| n | — | 363 | — | ESTIMATE | — |
| a | 0.16 | 0.26 | 0.36 | PROXY | S1, S2 |
| rho | 0.3 | 0.48 | 0.66 | PROXY | S2, S3 |
| e | 0.12 | 0.25 | 0.42 | ESTIMATE | S4, S5 |
| s5 | 0.12 | 0.21 | 0.33 | PROXY | S5, S6, S7 |
| q | 0.3 | 0.5 | 0.68 | ESTIMATE | S5, S6 |
| d5 | 0.97 | 1.02 | 1.08 | PROXY | S8 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S3, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.12 | 0.32 | 0.61 | PROXY |
| F | 2.94 | 4.82 | 6.33 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.54 | 9.69 | 10.00 | ESTIMATE |

## Caveats
- a: BLS is NAICS 311100, not 311119 or the narrowed outsourced population.
- a: Occupation shares are not direct measures of task exposure.
- a: Some smart-mill functions reflect conventional automation already deployed and are excluded where identifiable.
- rho: Modern-mill examples may not represent smaller legacy facilities.
- rho: Reported savings combine downtime, yield, energy, and labor effects.
- rho: Regulatory accountability limits full removal of skilled operators and quality staff.
- e: Public company descriptions prove the business model exists but do not establish its population share.
- e: Mixed pet/livestock supplement firms may classify outside 311119 depending on product and process.
- e: Firm eligibility may change if occasional custom mixing is treated as core outsourced revenue.
- s5: The examples are selected transactions rather than a frequency study.
- s5: One transaction is an asset purchase and another is a recapitalization with owner reinvestment.
- s5: Sales size does not map directly to the frozen EBITDA band.
- q: No representative contract dataset was found.
- q: Retention differs materially by bulk commodity feed, custom formula, supplement, premix, and packaging intensity.
- q: Customer concentration and local excess capacity can rapidly force pass-through.
- d5: Feed-and-residual grain use is not identical to processed feed shipments.
- d5: Higher feed conversion efficiency can reduce feed tonnage per unit of animal output.
- d5: Species mix, drought, disease, trade, and herd cycles create substantial regional volatility.
- o: The estimate addresses continued need for an outsourced operator, not merely physical feed demand.
- o: Vertical integration can displace eligible firms while total feed use grows.
- o: Highly automated mills can reduce staffing without eliminating accountable operating entities.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311100 Animal Food Manufacturing](https://www.bls.gov/oes/2023/may/naics4_311100.htm) (accessed 2026-07-23): Broader animal-food occupation and wage mix used to bridge wage-weighted task exposure, including production, material moving, office, management, and business operations.
- **S2** — [Smart Feed Mills: Automation, IoT, and AI integration](https://www.feedandadditive.com/smart-feed-mills-automation-iot-and-ai-integration/) (accessed 2026-07-23): Feed-mill AI and automation use cases, data prerequisites, operator role, predictive maintenance, quality control, demand planning, traceability, and reported operational effects.
- **S3** — [How do I Start an Animal Food Business?](https://www.fda.gov/animal-veterinary/animal-foods-feeds/how-do-i-start-animal-food-business) (accessed 2026-07-23): Facility registration, CGMP, food-safety plans, preventive controls, monitoring, corrective action, verification, recordkeeping, and reportable-food obligations.
- **S4** — [Bimini Pet Health: Contract Manufacturing and Private Label](https://biminipethealth.com/) (accessed 2026-07-23): Existence and operating model of U.S. contract/private-label animal-supplement manufacturing, including custom formulas, equine products, testing, certification, packaging, and compliance.
- **S5** — [Cargill acquires two US feed mills, strengthens production and distribution capabilities to grow with customers](https://www.cargill.com/2024/cargill-acquires-two-us-feed-mills-strengthens-production) (accessed 2026-07-23): Completed acquisition of two U.S. feed mills, customer segments, packing-line capability, planned modernization, and continuing manufacture for the seller.
- **S6** — [SC&H Capital Serves Graybill Processing, Inc. in Recapitalization by NCK Capital and Graycliff Partners](https://www.schgroup.com/representative-transactions/sch-capital-serves-graybill-processing-inc-in-recapitalization-by-nckcapital-and-graycliff-partners/) (accessed 2026-07-23): A second-generation family-owned animal-feed supplement processor, owner succession context, multiple competitive bids, and private-equity recapitalization.
- **S7** — [Anpario Acquires Bio-Vet Inc., United States](https://www.anpario.com/media/news/anpario-inc-acquires-bio-vet-inc-based-in-wisconsin-united-states/) (accessed 2026-07-23): Completed acquisition of a U.S. animal-nutrition producer with $8.2 million 2023 sales, 30-plus employees, a Wisconsin production facility, and dairy-market customers.
- **S8** — [USDA Agricultural Projections to 2035](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/113817/OCE-2026-1.pdf?v=39134) (accessed 2026-07-23): Long-term projections for corn feed and residual use, livestock inventories, soybean-meal demand, and beef, milk, egg, poultry, and export production used to anchor demand durability.
