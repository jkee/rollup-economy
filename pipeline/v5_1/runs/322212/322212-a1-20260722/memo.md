# 322212 — Folding Paperboard Box Manufacturing

*v5.1 Stage 1 research memo. Run `322212-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.51 · L 0.42 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring, version-heavy carton programs create automatable estimating, artwork, scheduling, quality-documentation, and service work.
**Weakness:** Low labor intensity and strict brand, food-contact, and quality accountability limit the share of enterprise economics AI can change.

## Business-model lens
- Included: Independent US folding-paperboard-box manufacturers in the approximately $1-10 million normalized EBITDA band that repeatedly design, print, cut, fold, glue, and supply cartons to external customers.
- Excluded: Captive packaging operations, paperboard mills, setup-box producers, brokers without accountable production, shells, financing vehicles, and firms outside the EBITDA band.
- Customer and revenue model: Recurring business-to-business carton programs for food, beverage, pharmaceutical, personal-care, and other consumer goods, sold through quotes, purchase orders, releases, and supply agreements with charges influenced by board, printing complexity, tooling, run length, and freight.
- Deviation from default lens: none

## Executive view
Folding-carton manufacturers combine recurring external programs and a sizable estimated LMM population with information-rich prepress, artwork, estimating, scheduling, and quality workflows. The core operation remains physical, and the low injected labor-to-receipts ratio caps the economic importance of labor automation.

## How AI changes the work
AI can extract specifications, prepare estimates, compare artwork revisions, flag copy inconsistencies, assist dieline and schedule choices, draft quality records, retrieve maintenance knowledge, and triage customer requests. Printing, die cutting, folding, gluing, setup, material handling, maintenance, inspection, and accountable approval remain human- or equipment-led.

## Value capture
Speed-to-quote, launch reliability, fewer errors, spoilage reduction, and service differentiation are more retainable than transparent labor cuts. Large brands and contract packagers still use rebids, board escalators, and cost-down negotiations to reclaim a portion.

## Firm availability
Census reports 462 employer establishments, while the frozen margin bridge estimates 181 firms in the EBITDA band. Parent-company integration, captive status, customer concentration, equipment condition, and certifications must be resolved before treating that estimate as a transferable pool.

## Demand durability
Cartons serve recurring food, beverage, medicine, personal-care, and consumer-goods demand. Prior PPC forecasts and current BLS converted-paper output projections indicate modest growth, with paper-for-plastic substitution as an upside and packaging reduction, flexible formats, and weak goods volumes as offsets.

## Risks and uncertainty
The largest gaps are the six-digit task mix, current workflow automation, true firm rather than establishment count, margin-band classification, customer concentration, pricing terms, current carton shipment forecasts, and regulatory review burdens. Brand or compliance errors can erase labor savings quickly.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0789 | — | OBSERVED | — |
| n | — | 181 | — | ESTIMATE | — |
| a | 0.14 | 0.22 | 0.32 | PROXY | S1, S4 |
| rho | 0.4 | 0.6 | 0.76 | ESTIMATE | S4, S5 |
| e | 0.56 | 0.73 | 0.86 | ESTIMATE | S3 |
| s5 | 0.14 | 0.24 | 0.36 | PROXY | S6 |
| q | 0.36 | 0.56 | 0.74 | ESTIMATE | S4, S5 |
| d5 | 0.98 | 1.06 | 1.15 | PROXY | S2, S5, S7 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.18 | 0.42 | 0.77 | ESTIMATE |
| F | 4.38 | 5.61 | 6.50 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 9.21 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is broader NAICS 322.
- a: Food-contact, pharmaceutical, and brand-critical work requires review even when AI prepares drafts or checks.
- rho: No representative five-year implementation study was found.
- rho: AI assistance may increase review throughput without reducing payroll proportionally.
- e: Census reports establishments, not eligible firms or EBITDA.
- e: The injected n=181 is an ESTIMATE based on size classes and a margin bridge.
- s5: Owner-age evidence is all-industry and data year 2018.
- s5: Owner age does not measure willingness, sale readiness, or transferability.
- q: No representative contract dataset was available.
- q: Retention is likely higher for complex short runs and regulated cartons than for long-run commodity cartons.
- d5: The direct PPC forecast is stale for the requested horizon.
- d5: BLS covers all converted paper products and AF&PA boxboard is an upstream input, not carton demand.
- o: Some prototyping and very short runs may move to in-house digital equipment.
- o: Material substitution and package elimination are quantity effects captured in d5.

## Sources
- **S1** — [Paper Manufacturing: NAICS 322](https://www.bls.gov/iag/tgs/iag322.htm) (accessed 2026-07-22): BLS reports 2025 employment of 87,050 paper-goods machine operators, 17,540 production supervisors, 14,210 industrial-truck operators, and 6,640 production managers in paper manufacturing, supporting a production-heavy occupation mix.
- **S2** — [Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects converted paper product manufacturing real output from $99.0 billion in 2024 to $116.9 billion in 2034, a 1.7% annual rate, while employment falls 5.4%.
- **S3** — [322212: Folding Paperboard Box Manufacturing - Census Bureau Profile](https://data.census.gov/profile/322212_-_Folding_Paperboard_Box_Manufacturing?codeset=naics~322212&g=010XX00US) (accessed 2026-07-22): Census defines 322212 as establishments converting non-corrugated paperboard into folding paperboard boxes and reports 462 employer establishments in 2023.
- **S4** — [Determining the Regulatory Status of Components of a Food Contact Material](https://www.fda.gov/food/packaging-food-contact-substances-fcs/determining-regulatory-status-components-food-contact-material) (accessed 2026-07-22): FDA states that the overall regulatory status of food-contact material depends on each substance and identifies 21 CFR 176 for paper and paperboard components, supporting compliance and review constraints.
- **S5** — [AF&PA Releases 66th Annual Paper Industry Capacity and Fiber Consumption Survey](https://www.afandpa.org/news/2026/afpa-releases-66th-annual-paper-industry-capacity-and-fiber-consumption-survey) (accessed 2026-07-22): AF&PA reports 2025 boxboard production was essentially flat at 12.4 million tons and overall US paper and paperboard production declined 3.7%; survey data represent about 87% of US capacity with estimates completing the dataset.
- **S6** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The 2019 Annual Business Survey infographic reports 51% of responding employer-business owners were age 55 or older; estimates cover 4.1 million responding owners in data year 2018.
- **S7** — [Folding Carton Market to Enjoy Measured Growth Through 2026](https://paperbox.org/folding-carton-market-to-enjoy-measured-growth-through-2026/) (accessed 2026-07-22): Paperboard Packaging Council reported a forecast for US folding-carton demand to grow 1.3% annually and reach 5.4 million tons by 2026, with nondurable-goods output forecast to rise 0.8% over that five-year forecast.
