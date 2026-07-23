# 115114 — Postharvest Crop Activities (except Cotton Ginning)

*v5.1 Stage 1 research memo. Run `115114-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.75 · L 2.50 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical crop throughput plus high-value grading, traceability, and scheduling decisions creates an implementable AI layer around an operator-required service.
**Weakness:** Crop-specific machinery, already-automated processes, seasonal utilization, and customer vertical integration can limit incremental labor savings and erode retention.

## Business-model lens
- Included: U.S. lower-middle-market independent firms repeatedly providing crop cleaning, drying, shelling, fumigating, curing, sorting, grading, packing, waxing, cooling, and associated lot-handling services after harvest for external growers, marketers, wholesalers, and processors.
- Excluded: Cotton ginning; firms that buy crops for resale; captive packing or cooling units serving only an affiliated grower, wholesaler, or processor; fruit and vegetable dehydration that creates a distinct processed product; custom feed grinding; farm management; passive property ownership; and non-control financing vehicles.
- Customer and revenue model: Operators typically earn repeat seasonal or year-round service revenue based on units handled, weight, bins, cartons, storage time, processing steps, or contracted capacity, with customers paying to prepare crops for market or further processing while preserving quality, traceability, and food safety.
- Deviation from default lens: none

## Executive view
Postharvest crop activities are a genuine recurring outsourced service with durable physical necessity and meaningful labor intensity. AI is most useful where perception and information meet machinery: grading, defect detection, lot tracking, scheduling, maintenance, and exception handling. The opportunity is moderated by already-automated lines, physical material handling, crop-specific integration, seasonal utilization, customer concentration, and the risk that customers internalize automated capacity.

## How AI changes the work
AI-enabled vision can improve size, color, grade, and defect decisions, while software can automate traceability records, production plans, inventory reconciliation, customer communication, staffing, and predictive maintenance. Manual packing, sanitation, loading, repair, product changeovers, and food-safety intervention persist, and many conveyors, coolers, sizers, and packaging machines are already conventional automation rather than new AI opportunity.

## Value capture
Operators can keep savings that lower their own labor, damage, waste, energy, rework, and downtime, especially under committed capacity or fixed unit pricing. Over five years, competitive bids and renewals can share those benefits with growers and marketers. Accurate grading, rapid recalls, documented food safety, lower claims, and scarce local throughput capacity provide the best defenses against pass-through.

## Firm availability
The industry definition aligns well with the service lens, and the dataset supplies an estimated lower-middle-market population, but margin bridging may be imprecise. Aging agricultural ownership suggests transitions, yet family succession, liquidation, facility real estate, customer contracts, seasonality, and food-safety history determine whether a firm is actually transferable.

## Demand durability
Crops still require physical preparation for market, and broader agricultural-support output projections imply modest growth. Demand varies with weather, harvest volumes, crop mix, imports, and local processor capacity. Food-safety and traceability requirements add continuing workflow complexity, while customer vertical integration and portable in-field automation are the clearest substitution risks.

## Risks and uncertainty
Key uncertainties are the absence of six-digit occupation data, representative contract terms, owner-transition evidence, and realized AI returns across crops. Operational risks include food contamination and recall, grade errors, cold-chain failure, seasonal labor shortages, crop failure, equipment downtime, customer and crop concentration, energy cost, water and fumigant regulation, and legacy-system integration. The injected compensation ratio also carries a stated wage-receipts vintage mismatch.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3779 | — | OBSERVED | — |
| n | — | 238 | — | ESTIMATE | — |
| a | 0.18 | 0.29 | 0.41 | PROXY | S1, S2, S3, S4, S5 |
| rho | 0.38 | 0.57 | 0.74 | ESTIMATE | S3, S4, S5, S6 |
| e | 0.62 | 0.76 | 0.88 | ESTIMATE | S1, S7 |
| s5 | 0.07 | 0.13 | 0.21 | PROXY | S8, S9 |
| q | 0.31 | 0.47 | 0.63 | ESTIMATE | S1, S6, S7 |
| d5 | 0.97 | 1.08 | 1.19 | PROXY | S1, S10 |
| o | 0.84 | 0.92 | 0.98 | ESTIMATE | S1, S3, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.03 | 2.50 | 4.59 | ESTIMATE |
| F | 3.90 | 5.15 | 6.12 | ESTIMATE |
| C | 6.20 | 9.40 | 10.00 | ESTIMATE |
| D | 8.15 | 9.94 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source covers all crop-support services and is dominated by field-worker occupations not representative of packinghouses.
- a: Research prototypes establish technical exposure but not commercial adoption or net labor removal.
- a: The injected labor share uses 2024 wages over 2022 receipts and a harmonization adjustment, so its vintage and basis uncertainty should be retained when interpreting labor economics.
- rho: USDA-supported systems cited include prototypes and crop-specific research, not an industry adoption census.
- rho: A model trained on one crop, grade standard, or defect may not transfer to another.
- rho: Traceability requirements create a strong digitization use case but also raise validation and integration burdens.
- e: The supplied firm estimate is margin-bridged from size-class receipts using a broad Farming/Agriculture margin and may misclassify firms with different postharvest margins.
- e: NAICS classification alone does not distinguish an independent service provider from a captive establishment in a larger enterprise.
- e: Seasonality and crop concentration can make normalized earnings materially different from reported annual results.
- s5: Farm operators and all small-business owners are not the same population as postharvest service-firm owners.
- s5: Intent to retire or sell does not measure a completed third-party control transaction.
- s5: Specialized facilities, seasonal working capital, and customer concentration can narrow the buyer pool.
- q: No representative industry dataset on contract terms or customer retention was located.
- q: Pricing and buyer power differ across grain, nuts, fresh produce, seed, and specialty crops.
- q: Benefits delivered as higher grade recovery may be shared differently from pure labor savings.
- d5: The BLS projection is for NAICS 115000 rather than 115114 and spans ten years rather than five.
- d5: Real output does not directly measure constant-quality postharvest service quantity.
- d5: Crop failures or customer vertical integration can create severe local declines despite national stability.
- o: This is a structural estimate rather than an observed displacement rate.
- o: Portable or in-field sorting can shift work away from independent postharvest facilities.
- o: An accountable operator remains necessary even when the operator is a vertically integrated customer rather than a lens firm.

## Sources
- **S1** — [U.S. Census Bureau NAICS 115114 Postharvest Crop Activities (except Cotton Ginning)](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-23): Defines the industry as services performed after harvest to prepare crops for market or processing, including cleaning, drying, shelling, fumigating, curing, sorting, grading, packing, and cooling.
- **S2** — [BLS OEWS: Support Activities for Crop Production, May 2023](https://www.bls.gov/oes/2023/may/naics4_115100.htm) (accessed 2026-07-23): Provides the nearest published occupation mix, including farming, office, production, maintenance, transportation, packing, grading, inspection, and material-moving occupations.
- **S3** — [USDA NAL: AI-Enhanced Multispectral Vision-Based In-Field Apple Sorting System](https://www.nal.usda.gov/research-tools/food-safety-research-projects/ai-enhanced-multispectral-vision-based-field-apple-sorting-system) (accessed 2026-07-23): Documents development of AI vision and conveyor integration to sort apples by size, color, surface defects, and market grade.
- **S4** — [USDA ARS: Development of Sensing Platform for Fruit Sorting](https://www.ars.usda.gov/research/publications/publication/?seqNo115=417478) (accessed 2026-07-23): Describes RGB and hyperspectral sensing and software for automated detection of external and bruise-like internal fruit defects.
- **S5** — [USDA ARS: How D'Ya Like Them Apples?](https://www.ars.usda.gov/oc/dof/how-dya-like-them-apples/) (accessed 2026-07-23): Reports a machine-vision apple sorter capable of grading 10 to 12 apples per second and illustrates the movement of sorting activity into the field.
- **S6** — [FDA: FSMA Final Rule on Requirements for Additional Traceability Records for Certain Foods](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods) (accessed 2026-07-23): Establishes lot-level records and key data elements for cooling, initial packing, shipping, receiving, and other critical tracking events relevant to postharvest operators.
- **S7** — [BLS Industries at a Glance: Support Activities for Agriculture and Forestry](https://www.bls.gov/iag/tgs/iag115.htm) (accessed 2026-07-23): Explains that independently conducted agricultural support activities are alternatives to producer self-performance and provides contextual workforce and operating-risk information.
- **S8** — [USDA ERS: America's Diverse Family Farms, 2020 Edition](https://ers.usda.gov/sites/default/files/_laserfiche/publications/100012/EIB-220.pdf?v=66964) (accessed 2026-07-23): Reports five-year farm-retirement intentions, family succession expectations, and the limited share of farmland expected to become purchasable from retiring operators.
- **S9** — [SBA Office of Advocacy: Paths to Business Ownership](https://advocacy.sba.gov/wp-content/uploads/2021/03/Paths-to-Business-Ownership-fact-sheet.pdf) (accessed 2026-07-23): Reports broad business-owner acquisition patterns and that 64.5% of owners planned eventually to sell, used only as a non-industry transition proxy.
- **S10** — [BLS Employment Projections: Industry Employment and Output](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-23): Projects broader support-activities-for-agriculture-and-forestry real output from 23.6 in 2024 to 27.6 in 2034, supporting a demand-growth proxy.
