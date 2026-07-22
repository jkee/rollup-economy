# 312120 — Breweries

*v5.1 Stage 1 research memo. Run `312120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.85 · L 1.17 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can improve complex forecasting, sales, inventory, compliance, and production-planning workflows without replacing licensed physical production.
**Weakness:** A contracting beer category and distributor-retailer bargaining can absorb operational gains.

## Business-model lens
- Included: Lower-middle-market U.S. production breweries with recurring external wholesale, self-distribution, private-label, contract-brewing, or alternating-proprietor relationships, including microbreweries and regional breweries with material off-site sales.
- Excluded: Hospitality-dominant brewpubs and taproom breweries whose economics are principally restaurant or bar operations; brand-only contract-brewing marketers that do not operate a brewery; captive pilot facilities; shell entities; and firms outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: Repeat beer production and supply to distributors, retailers, hospitality accounts, or brand owners through wholesale, self-distribution, contract-production, and shared-brewery arrangements, with some ancillary direct-to-consumer sales.
- Deviation from default lens: NAICS 312120 combines distribution-focused production breweries with hospitality-focused brewpubs and taprooms. The latter depend on restaurant, bar, and venue labor and customer economics that would make one labor, retention, and demand screen incoherent, so the lens is narrowed to production breweries with material recurring external supply relationships.

## Executive view
Distribution-focused breweries offer AI-addressable commercial and planning work around an irreducibly physical, regulated production process. The main concern is demand: 2025 craft volume fell 4% and overall beer volume 5.7%, with microbreweries especially weak. The industry also mixes production suppliers with hospitality businesses, so a coherent screen must exclude hospitality-dominant brewpubs and taprooms.

## How AI changes the work
AI can improve SKU and account forecasting, production scheduling, raw-material and packaging purchasing, inventory control, distributor depletion analysis, sales prioritization, marketing production, customer support, bookkeeping, and compliance preparation. Human brewers, cellar and packaging crews, quality staff, maintenance workers, and drivers remain necessary for physical and accountable execution.

## Value capture
Wholesale price lists do not automatically pass through savings, but breweries compete for scarce distributor attention, retail placement, and consumer demand. Three-tier and franchise structures can weaken control over route to market. Savings are likely to be divided among retained margin, promotions, service, and price support rather than fully captured.

## Firm availability
A mature market with closings above openings creates more ownership events and distress, while broad owner aging adds succession pressure. Yet many closures are liquidations and many brewery transactions involve brands rather than transferable operating firms, so observed craft churn cannot be treated as an acquisition rate.

## Demand durability
Beer production remains operator-required, but category quantity is declining. A narrowed LMM production-brewery basket faces retailer rationalization, changing alcohol preferences, and underused capacity; differentiated brands, nonalcoholic offerings, contract production, and local strength can offset but not erase the base contraction case.

## Risks and uncertainty
Major risks are sustained volume decline, distributor dependence, state franchise constraints, brand concentration, excess capacity, input and packaging costs, product recalls, alcohol regulation, and a mismatch between the frozen food-processing margin bridge and brewery economics. The six-digit task mix and transfer denominator are not observed.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1905 | — | OBSERVED | — |
| n | — | 95 | — | ESTIMATE | — |
| a | 0.16 | 0.28 | 0.4 | PROXY | S4, S5 |
| rho | 0.32 | 0.55 | 0.72 | ESTIMATE | S5, S8 |
| e | 0.35 | 0.52 | 0.7 | PROXY | S2, S3 |
| s5 | 0.14 | 0.25 | 0.38 | ESTIMATE | S3, S7, S8 |
| q | 0.3 | 0.5 | 0.7 | ESTIMATE | S3, S6 |
| d5 | 0.68 | 0.84 | 1 | PROXY | S3, S9 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S2, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.39 | 1.17 | 2.19 | ESTIMATE |
| F | 2.79 | 4.17 | 5.26 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.12 | 8.06 | 9.90 | ESTIMATE |

## Caveats
- a: The occupation mix is a three-digit beverage-and-tobacco proxy.
- a: General GenAI exposure does not measure current brewery automation or labor substitution.
- a: Owner labor and cross-trained small-brewery jobs blur wage-weighted task allocation.
- rho: No representative brewery AI-adoption or realized-savings study was found.
- rho: Implementation capacity may be weaker at owner-operated firms than at scaled beverage manufacturers.
- rho: The estimate excludes autonomous delivery and speculative general-purpose robotics.
- e: Craft segment counts are establishments or brewing companies, not necessarily firms in the dataset band.
- e: Onsite sales thresholds do not reveal whether hospitality is economically dominant.
- e: The frozen firm count uses a food-processing margin bridge that may be unsuitable for taproom and brewpub models.
- s5: Closures are not control transfers and may destroy rather than transfer operations.
- s5: The owner-age statistic is cross-industry and based on 2018 data.
- s5: Brand acquisitions without operating assets may not qualify under the lens.
- q: Distribution and franchise rules vary materially by state.
- q: Self-distributed and direct-to-consumer volume may retain more benefit than wholesaler-served volume.
- q: Category contraction can turn cost savings into defensive trade spending rather than price cuts.
- d5: Brewers Association craft definitions do not exactly match NAICS or the LMM lens.
- d5: A single recent year can be cyclical, and survivor cohorts may outperform category totals.
- d5: Product mix shifts toward nonalcoholic beer or adjacent beverages may not remain inside the current service basket.
- o: The estimate addresses required operator involvement, not survival of each independent brand.
- o: Contract brewing can preserve operator-required production while shifting it to a different firm.
- o: State and federal license structures and direct-sales permissions vary.

## Sources
- **S1** — [Fancy Another Pint?](https://www.census.gov/newsroom/blogs/global-reach/2020/11/fancy_another_pint.html) (accessed 2026-07-23): States that NAICS 312120 comprises establishments primarily engaged in brewing beer, ale, malt liquors, and nonalcoholic beer.
- **S2** — [Craft Beer Industry Market Segments](https://www.brewersassociation.org/statistics-and-data/craft-beer-industry-market-segments/) (accessed 2026-07-23): Defines microbreweries, brewpubs, taproom breweries, regional breweries, contract brewing companies, and alternating proprietors, including onsite and offsite sales thresholds and production responsibility.
- **S3** — [A Year of Correction for Craft Beer, With Early Signals of Recovery](https://www.brewersassociation.org/association-news/a-year-of-correction-for-craft-beer-with-early-signals-of-recovery/) (accessed 2026-07-23): Reports 2025 craft production down 4%, overall beer down 5.7%, 9,578 operating craft breweries, 300 openings, 481 closures, segment counts, and segment production changes.
- **S4** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 312000](https://www.bls.gov/oes/2023/may/naics3_312000.htm) (accessed 2026-07-23): Reports the broader beverage-and-tobacco occupation mix, including production at 22.11%, transportation/material moving at 12.33%, office support at 4.87%, and sales at 12.15% of employment.
- **S5** — [Generative AI and Jobs: A Refined Global Index of Occupational Exposure](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) (accessed 2026-07-23): Finds clerical work has the highest GenAI exposure and that job transformation is generally more likely than full automation.
- **S6** — [FTC and DOJ Staff Comment on California Beer Distribution](https://www.ftc.gov/system/files/documents/advocacy_documents/joint-comment-ftc-staff-doj-antitrust-division-staff-california-state-assembly-concerning-california/v200008_california_beer_distribution_advocacy_2020.pdf) (accessed 2026-07-23): Describes the three-tier chain in which brewers sell to licensed wholesalers that sell onward to retailers and discusses competition and distribution constraints.
- **S7** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-23): Reports that 51% of responding employer-business owners were age 55 or older in the 2019 Annual Business Survey, data year 2018.
- **S8** — [Getting Started in the Beer Industry](https://www.ttb.gov/business-central/industry-startup-tutorial/IS-B-0010) (accessed 2026-07-23): Explains regulated brewery, brewpub, pilot brewery, and alternating-proprietorship operating types and federal application requirements.
- **S9** — [Green Shoots: Where Craft Beer Goes From Here](https://www.brewersassociation.org/insights/green-shoots-where-craft-beer-goes-from-here/) (accessed 2026-07-23): Reports 2025 craft volume down 4%, operating breweries down 2.9%, microbrewery production down 8.9%, and estimated craft brewing capacity utilization of only 55%.
