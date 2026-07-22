# 322219 — Other Paperboard Container Manufacturing

*v5.1 Stage 1 research memo. Run `322219-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.15 · L 0.99 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Custom, repeat specifications and higher labor intensity create useful AI opportunities in estimating, design support, scheduling, quality, and customer workflows.
**Weakness:** The NAICS code mixes fundamentally different container businesses, leaving eligibility and demand highly uncertain after narrowing.

## Business-model lens
- Included: Independent US manufacturers in the approximately $1-10 million normalized EBITDA band repeatedly supplying custom setup paperboard boxes and specialty fiber tubes, cores, cans, drums, mailing cases, reels, and similar containers to external industrial and consumer customers.
- Excluded: High-volume sanitary food containers, paper cups and plates, and milk cartons; captive plants; paperboard mills; folding or corrugated boxes; brokers without accountable production; shells; financing vehicles; and firms outside the EBITDA band.
- Customer and revenue model: Repeat business-to-business programs for specification-defined rigid boxes and specialty fiber containers, sold through quotes, purchase orders, releases, and supply agreements with pricing based on materials, dimensions, printing or finishing, tooling, run length, and freight.
- Deviation from default lens: NAICS 322219 combines setup boxes and industrial fiber tubes, cans, and drums with sanitary food containers, cups, plates, and milk cartons. The lens retains specialty setup-box and industrial fiber-container manufacturing because those share custom, repeat, specification-led production; high-volume sanitary and milk-container operations are excluded because their food-contact compliance, production scale, and commodity customer model make a single screen incoherent.

## Executive view
The narrowed specialty-container lens has recurring custom work, higher injected labor intensity, and useful information workflows around specifications, quotes, artwork, scheduling, and service. Its weakness is a small, poorly observed and highly varied firm population embedded in a heterogeneous NAICS code.

## How AI changes the work
AI can parse specifications, draft estimates, compare artwork, recommend past designs, assist schedules and procurement, retrieve maintenance knowledge, draft quality records, and answer routine customer questions. Forming, winding, cutting, wrapping, printing, assembly, inspection, handling, and maintenance remain physical.

## Value capture
Custom decoration, geometry, tooling, short runs, and service make some efficiency gains hard for customers to benchmark. Standard industrial cores and tubes face more transparent bids and material pass-through, so retention varies substantially across the retained basket.

## Firm availability
The frozen estimate of 67 firms covers product groups excluded by the coherence narrowing and uses a broad margin bridge. A product-by-firm ownership map is therefore essential; general owner aging suggests succession pressure but does not establish transfer flow.

## Demand durability
The retained products serve consumer presentation, shipping, and industrial winding or containment uses. Broader converted-paper output growth supports modest demand, but end-market diversity, material substitution, industrial cycles, and scarce direct shipment data justify a wide range.

## Risks and uncertainty
Major uncertainties are subgroup weights, six-digit occupations, existing automation, true EBITDA-band membership, customer concentration, equipment condition, pricing terms, and direct demand series. Results would be misleading if sanitary-container firms dominate the frozen n population.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2168 | — | OBSERVED | — |
| n | — | 67 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.3 | PROXY | S1, S2 |
| rho | 0.38 | 0.57 | 0.73 | ESTIMATE | S1 |
| e | 0.3 | 0.5 | 0.68 | ESTIMATE | S2 |
| s5 | 0.14 | 0.25 | 0.38 | PROXY | S5 |
| q | 0.38 | 0.59 | 0.77 | ESTIMATE | S2 |
| d5 | 0.94 | 1.04 | 1.15 | PROXY | S3, S4 |
| o | 0.93 | 0.98 | 1 | ESTIMATE | S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.40 | 0.99 | 1.90 | ESTIMATE |
| F | 2.15 | 3.60 | 4.68 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.74 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS data are NAICS 322 rather than 322219 or the narrowed lens.
- a: The retained product groups may have different task mixes despite greater coherence than the full code.
- rho: No representative implementation evidence for the narrowed population was found.
- rho: Integration cost may be disproportionately high for small custom manufacturers.
- e: No source gives the revenue or firm share of each 322219 product group.
- e: The injected n=67 is an ESTIMATE using a broad industry margin and may not fit each subgroup.
- s5: Owner-age evidence is all-industry and from data year 2018.
- s5: The narrowed population may be more family-owned than the employer-business average.
- q: No representative contract sample was found.
- q: Retention is likely higher in decorated setup boxes and lower in standardized industrial cores.
- d5: No direct demand series for the narrowed basket was found.
- d5: The retained end markets are diverse and can move in opposite directions.
- o: Standard mailing tubes or cores may face more self-service and distributor substitution than bespoke products.
- o: Material substitution and end-market contraction are captured in d5.

## Sources
- **S1** — [Paper Manufacturing: NAICS 322](https://www.bls.gov/iag/tgs/iag322.htm) (accessed 2026-07-22): BLS reports 2025 paper-manufacturing employment of 87,050 paper-goods machine operators, 17,540 production supervisors, 14,210 industrial-truck operators, and 6,640 production managers, supporting a production-heavy occupation mix.
- **S2** — [322219: Other Paperboard Container Manufacturing - Census Bureau Profile](https://data.census.gov/profile/322219_-_Other_Paperboard_Container_Manufacturing?codeset=naics~322219) (accessed 2026-07-22): Census defines the industry as converting purchased paperboard into containers other than corrugated, solid-fiber, and folding boxes, with illustrative examples including fiber cans and drums, milk cartons, sanitary food containers, and setup boxes.
- **S3** — [Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects converted paper product manufacturing output increasing from $99.0 billion in 2024 to $116.9 billion in 2034 in chained 2017 dollars, a 1.7% compound annual rate.
- **S4** — [AF&PA Releases 66th Annual Paper Industry Capacity and Fiber Consumption Survey](https://www.afandpa.org/news/2026/afpa-releases-66th-annual-paper-industry-capacity-and-fiber-consumption-survey) (accessed 2026-07-22): AF&PA reports 2025 boxboard production essentially flat at 12.4 million tons while overall US paper and paperboard production declined 3.7%; survey data represent about 87% of industry capacity with estimates completing the dataset.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The 2019 Annual Business Survey infographic reports 51% of responding owners of employer businesses were age 55 or older; estimates represent 4.1 million responding owners in data year 2018.
