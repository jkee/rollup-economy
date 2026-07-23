# 114210 — Hunting and Trapping

*v5.1 Stage 1 research memo. Run `114210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.50 · L 0.00 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can automate a material share of wildlife-monitoring and administrative work in labor-intensive commercial preserves.
**Weakness:** The frozen lower-middle-market firm count is zero, and the narrow preserve lens excludes much of the visible hunting ecosystem assigned to other industries or to the product-harvesting portion of this code.

## Business-model lens
- Included: Commercial game preserves and hunting preserves without accommodation, including private operators selling access to managed land, seasonal memberships, repeat hunt access, or preserve-use packages to external customers.
- Excluded: Commercial hunters and trappers whose principal revenue is pelts, meat, or other harvested products; hunting guides and outfitters; wildlife and pest-control services; hunting camps with accommodation; and nature preserves.
- Customer and revenue model: Individuals, member groups, and occasional organizational customers pay fixed access fees, memberships, and hunt or preserve-use package prices; revenue depends on managed wildlife populations, land access, safety, and the quality of the preserve experience.
- Deviation from default lens: The six-digit industry combines product-harvesting hunters and trappers with commercial game and hunting preserves, which have different work and revenue models. The lens is narrowed to non-accommodation preserve operators solely to produce a coherent service-business analysis; Census cross-references keep guides, pest control, lodging, and nature preserves outside the code.

## Executive view
The coherent service business inside this heterogeneous industry is the commercial game or hunting preserve. AI can reduce monitoring and administrative work, but the frozen firm count is zero and the physical, regulated, land-based operating role remains.

## How AI changes the work
The strongest applications are automated camera-trap review and wildlife monitoring, plus booking, inquiries, marketing, scheduling, pricing support, memberships, waivers, and compliance documents. Habitat maintenance, animal handling, guest safety, and other field work remain human and physical.

## Value capture
Fixed access, membership, and package pricing permits some cost savings to remain with the preserve, although competition and customer expectations can convert savings into better service, and land and wildlife costs continue to dominate economics.

## Firm availability
The code mixes preserves with commercial hunting and trapping for products, and published data do not split the two. More decisively, the assigned frozen data report no lower-middle-market firms, so no current firm opportunity is available under those inputs.

## Demand durability
The 2022 national survey reports 14.4 million hunters and $45.2 billion of hunting expenditures, supporting a durable activity base. FWS recruitment and retention concerns and the survey-method break argue for roughly flat rather than confidently growing five-year demand, with private-access scarcity as an upside case.

## Risks and uncertainty
The largest uncertainties are the absence of firm-level preserve data, a zero frozen firm count, code heterogeneity, indirect task and adoption proxies, unknown transaction incidence, regulation and liability, wildlife health, weather, rural connectivity, and discretionary customer spending.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3448 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.22 | 0.34 | 0.47 | PROXY | S3, S4, S7 |
| rho | 0.29 | 0.48 | 0.66 | PROXY | S3, S4 |
| e | 0.18 | 0.42 | 0.68 | ESTIMATE | S1, S2 |
| s5 | 0.1 | 0.21 | 0.35 | ESTIMATE | — |
| q | 0.4 | 0.61 | 0.78 | ESTIMATE | S5 |
| d5 | 0.9 | 0.99 | 1.1 | PROXY | S5, S6 |
| o | 0.95 | 0.985 | 0.998 | ESTIMATE | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.88 | 2.25 | 4.28 | PROXY |
| F | 0.00 | 0.00 | 0.00 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.55 | 9.75 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation covers fishing and commercial hunting work rather than the narrowed preserve-operator lens.
- a: No direct preserve-level task census or AI adoption study was found.
- rho: Research-grade wildlife monitoring does not directly establish economical deployment in small commercial preserves.
- rho: Safety-critical and regulatory decisions retain human accountability.
- e: The frozen dataset reports no lower-middle-market firms in this industry, so the parameter describes a hypothetical composition rather than observed eligible firms.
- e: The Census industry definition does not publish a preserve-versus-harvesting firm split.
- s5: No preserve-specific transaction-rate evidence was found.
- s5: The frozen dataset reports no lower-middle-market firms, making the practical transaction count zero under the assigned inputs.
- q: National hunting expenditure categories do not measure preserve pricing or cost pass-through directly.
- q: Customer willingness to pay may depend more on access and wildlife quality than on administrative efficiency.
- d5: National hunting expenditure includes equipment, travel, licenses, and land-related spending beyond commercial preserves.
- d5: The 2022 national survey changed collection methodology, reducing comparability with prior surveys.
- o: The estimate concerns survival of an accountable operating role, not preservation of every current job or task.
- o: Very small properties may be managed as passive land access rather than staffed operating businesses.

## Sources
- **S1** — [2022 NAICS 11421: Hunting and Trapping](https://www.census.gov/naics/?details=11421&input=11421&year=2022) (accessed 2026-07-22): Defines the industry as commercial hunting and trapping plus commercial game and hunting preserves.
- **S2** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Provides cross-references placing hunting guides, pest control, accommodation camps, and nature preserves outside NAICS 114210.
- **S3** — [Automated methods for processing camera trap video data for distance sampling](https://www.usgs.gov/publications/automated-methods-processing-camera-trap-video-data-distance-sampling) (accessed 2026-07-22): Reports machine-learning wildlife classification performance and substantial analyst-hour savings in camera-trap processing.
- **S4** — [Artificial Intelligence in the USGS Ecosystems Mission Area: Fish and Wildlife Applications](https://www.usgs.gov/mission-areas/ecosystems/science/artificial-intelligence-usgs-ecosystems-mission-area-fish-and) (accessed 2026-07-22): Describes AI use for species presence, abundance, habitat use, disease detection, population monitoring, and behavior or movement analysis.
- **S5** — [2022 National Survey of Fishing, Hunting, and Wildlife-Associated Recreation](https://www.fws.gov/sites/default/files/documents/Final_2022-National-Survey_101223-accessible-single-page.pdf) (accessed 2026-07-22): Reports 14.4 million hunters and $45.2 billion in hunting expenditures in 2022, including trip, equipment, and other spending.
- **S6** — [Report Offers Snapshot of Hunters and Anglers in the U.S.](https://www.fws.gov/story/2024-09/report-offers-snapshot-hunters-and-anglers-us) (accessed 2026-07-22): Notes 14.4 million hunters in 2022 and indications of longer-run hunting participation decline that motivate recruitment, retention, and reactivation.
- **S7** — [Fishing and Hunting Workers: Occupational Outlook Handbook](https://www.bls.gov/ooh/farming-fishing-and-forestry/fishers-and-related-fishing-workers.htm) (accessed 2026-07-22): Describes physical hunting and trapping tasks, regulation and licensing, self-employment, and projected occupational demand.
