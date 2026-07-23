# 115310 — Support Activities for Forestry

*v5.1 Stage 1 research memo. Run `115310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.85 · L 2.62 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Large, persistent forest-restoration and wildfire-treatment needs paired with practical remote-sensing and workflow-automation opportunities.
**Weakness:** A small, estimated LMM firm pool exposed to public procurement, heterogeneous business models, and weak observed succession evidence.

## Business-model lens
- Included: US lower-middle-market firms providing recurring or repeat outsourced forestry support to external customers, including timber cruising and estimation, forest management and consulting, reforestation and stand improvement, pest and vegetation control, wildfire prevention and suppression support, and related field implementation.
- Excluded: Logging and timber ownership, government agencies performing work internally, captive forestry departments, one-person practices without transferable operations, equipment-only rental outside the industry, non-control investments, and shells.
- Customer and revenue model: Customers include federal, state, Tribal, and local land managers, industrial and family forest owners, timber businesses, utilities, conservation organizations, and developers. Revenue commonly comes from competitively bid fixed-price or unit-price projects, time-and-materials consulting, multi-year or preseason blanket agreements, and repeat seasonal field programs.
- Deviation from default lens: none

## Executive view
Forestry support is a genuine outsourced-service industry with repeat public and private customers, meaningful labor intensity, and clear AI use cases in inventory, mapping, risk analysis, estimating, scheduling, and documentation. Its field-heavy and safety-critical core remains operator-dependent. The main commercial uncertainties are heterogeneous subsegments, public-budget exposure, contract repricing, and the small, margin-bridged LMM firm population.

## How AI changes the work
AI can fuse satellite, drone, GIS, weather, inventory, and treatment data; automate timber-cruise interpretation, proposal drafts, compliance reports, routing, crew scheduling, and invoicing; and improve treatment prioritization. The Forest Service's remote-sensing and risk frameworks show the direction of travel. Planting, thinning, spraying, equipment operation, field validation, and fire response remain substantially physical.

## Value capture
Fixed-price and per-acre contractors can retain productivity gains during a contract term, and faster planning can increase capacity. Retention erodes at rebid or renewal where public procurement and industrial buyers compare unit prices; hourly work can pass savings through immediately. Differentiated safety records, qualifications, mobilization capacity, and local knowledge support retention.

## Firm availability
The frozen dataset suggests a small LMM-band population, but the eligible share is unobserved. Many NAICS firms should fit the external-service lens, while key-person consultancies, episodic vendors, captive operators, and firms with nontransferable credentials reduce availability. Broad owner-age evidence indicates succession pressure but not completed control transfers.

## Demand durability
Wildfire risk, reforestation backlog, insect and disease threats, timber management, and long-horizon treatment mandates support durable work. Demand will be lumpy by geography and funding cycle; unmet ecological need only becomes contractor revenue after appropriation, planning, environmental review, award, and mobilization.

## Risks and uncertainty
Material risks include federal and state budget changes, delayed projects, wildfire season volatility, customer concentration, low-bid procurement, labor and migrant-workforce constraints, safety liabilities, seasonal utilization, equipment intensity, professional key-person dependence, and uncertain credential transfer. The broad code also mixes high-exposure consulting with low-exposure physical crews, so acquisition-level task and contract diligence is essential.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6078 | — | OBSERVED | — |
| n | — | 30 | — | ESTIMATE | — |
| a | 0.22 | 0.34 | 0.47 | PROXY | S2, S6 |
| rho | 0.38 | 0.58 | 0.75 | ESTIMATE | S2, S6 |
| e | 0.4 | 0.62 | 0.78 | ESTIMATE | S1, S8 |
| s5 | 0.1 | 0.22 | 0.34 | PROXY | S7 |
| q | 0.35 | 0.56 | 0.74 | ESTIMATE | S8 |
| d5 | 0.94 | 1.09 | 1.28 | PROXY | S2, S4, S5, S9 |
| o | 0.84 | 0.93 | 0.98 | ESTIMATE | S2, S6, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.03 | 4.79 | 8.57 | ESTIMATE |
| F | 1.27 | 2.62 | 3.53 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.90 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation spans government, forestry, agriculture-support, and self-employment populations rather than NAICS 115310 alone.
- a: No source measures wage-weighted AI exposure for this six-digit industry.
- a: The injected labor-share input uses 2024 wages over 2022 receipts and a harmonization adjustment; that vintage mismatch affects the downstream labor opportunity even though it does not change this task share.
- rho: The available evidence demonstrates technical feasibility and public-agency use, not five-year private-contractor implementation rates.
- rho: Implementation potential differs sharply between consulting and inventory work and manual reforestation or suppression crews.
- e: No observed study measures the eligible share of the frozen LMM firm population.
- e: The frozen firm count is itself margin-bridged from receipts-size classes using a broad agriculture margin, which may misclassify forestry contractors.
- e: Eligibility likely varies by subsegment because consulting, reforestation, pest control, and fire support have different recurrence and transferability.
- s5: The proxy is national, all-industry, and based on 2018 responding employer-business owners.
- s5: It measures owners rather than firms and does not observe sales, control changes, or transferability.
- s5: Preseason agreements, licenses, safety records, and key customer relationships may not transfer cleanly.
- q: No observed study of AI-benefit pass-through in forestry-support contracts was found.
- q: Retention varies materially between fixed-price consulting, per-acre field services, emergency fire call-outs, and hourly work.
- q: Federal and state customers can impose wage, reporting, and competition requirements that limit retention.
- d5: Need, policy targets, and appropriations are not completed service quantity.
- d5: Federal budget changes, litigation, permitting, fire-season variability, and workforce capacity can delay or cancel work.
- d5: The BLS projection is an employment proxy and automation can lower employment even if service quantity rises.
- o: The operator-required share is not directly observed.
- o: Consulting and timber-inventory subsegments face more software substitution than reforestation, pest-control, and fire-support operations.
- o: Public agencies can internalize work if staffing or procurement policy changes.

## Sources
- **S1** — [115310: Support Activities for Forestry](https://data.census.gov/profile/115310_-_Support_activities_for_forestry?codeset=naics~115310&g=010XX00US) (accessed 2026-07-23): Defines the industry as support related to timber production, wood technology, forestry economics and marketing, and forest protection, including timber estimating, firefighting, pest control, and reforestation consulting.
- **S2** — [Forest and Conservation Workers](https://www.bls.gov/ooh/farming-fishing-and-forestry/forest-and-conservation-workers.htm) (accessed 2026-07-23): Describes physical forestry duties, reports that support activities for agriculture and forestry employ 23% of the occupation, projects a 5% employment decline from 2024 to 2034, and states that remote sensing allows fewer workers to count and identify trees while wildfire raises some demand.
- **S3** — [Support Activities for Agriculture and Forestry: May 2023 OEWS](https://www.bls.gov/oes/2023/may/naics3_115000.htm) (accessed 2026-07-23): Documents that the available national occupation table is for the broader NAICS 115000 population and excludes self-employed workers, supporting the proxy limitation on occupational evidence.
- **S4** — [Reforestation](https://www.fs.usda.gov/managing-land/forest-management/vegetation-management/reforestation) (accessed 2026-07-23): Reports more than 4 million acres of potential National Forest reforestation need, identifies wildfire as about 80% of need, and describes the REPLANT Act and escalating disturbance drivers.
- **S5** — [Mind the Gap: Reforestation Needs vs. Reforestation Capacity in the Western United States](https://research.fs.usda.gov/treesearch/68214) (accessed 2026-07-23): Estimates that planting capacity fell about 3.8 million acres short of fire-driven need from 2000 through 2021 and anticipates the gap increasing by 2050.
- **S6** — [RiskMonitor](https://research.fs.usda.gov/firelab/products/dataandtools/riskmonitor) (accessed 2026-07-23): Describes a Forest Service framework using simulations, maps, charts, and tabular summaries to prioritize fuel treatments, compare strategies, and monitor risk-reduction progress.
- **S7** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-23): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 Annual Business Survey covering 2018.
- **S8** — [Pacific Northwest Region Fire Procurement](https://www.fs.usda.gov/r06/fire/resources/fire-procurement) (accessed 2026-07-23): Documents preseason Incident Blanket Purchase Agreements, competitive vendor solicitations, and multiple five-year agreement periods for fire-support resources.
- **S9** — [Science Supporting the Wildfire Crisis Strategy and Bipartisan Infrastructure Law](https://research.fs.usda.gov/rmrs/understory/science-supporting-wildfire-crisis-strategy-bipartisan-infrastructure-law-fact) (accessed 2026-07-23): States that the strategy calls for treating up to 20 million additional National Forest acres and up to 30 million additional acres on other federal, state, Tribal, and private lands.
