# 321113 — Sawmills

*v5.1 Stage 1 research memo. Run `321113-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.08 · L 0.53 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Physical lumber demand and established machine-vision use cases support durable, implementable operating improvements.
**Weakness:** Mature automation and commodity price competition limit incremental AI labor exposure and retained benefit.

## Business-model lens
- Included: Independent U.S. sawmills producing dimension lumber, boards, beams, timbers, ties, shingles, shakes, siding, chips, and related planed output for repeat external buyers.
- Excluded: Captive mills, non-operating timber ownership, logging contractors, purchased-lumber millwork, veneer and engineered-panel production, and mills without a transferable operating business.
- Customer and revenue model: Repeat product sales to builders, distributors, dealers, industrial users, and secondary wood manufacturers, generally at market-linked prices rather than recurring service fees.
- Deviation from default lens: none

## Executive view
Sawmills are repeat-sale industrial operators rather than outsourced service firms in the everyday sense, but they fit the fixed lens because they repeatedly supply external customers. AI can improve inspection, grade recovery, maintenance, planning, and administrative work; the central constraint is that mature mechanical and vision automation has already captured much of the obvious production opportunity.

## How AI changes the work
The best remaining applications pair computer vision and optimization with mill controls, while predictive maintenance, scheduling, procurement, quoting, and documentation offer smaller software-led gains. Physical handling, maintenance, safety, and exception management remain human- and asset-intensive.

## Value capture
Recovery and grade-yield improvements can be retained better than transparent headcount savings, but commodity pricing, benchmark resets, and competition should share gains with customers over five years.

## Firm availability
A sizable employer-establishment base exists and succession pressure is plausible, yet the frozen 496-firm count is margin-bridged through a volatile cycle. Closures, family transfers, captive mills, and poor transferability make retirement intent an upper bound rather than deal flow.

## Demand durability
Housing and repair activity keep physical lumber demand durable, with modest baseline growth but material cyclical downside. Regardless of AI, converting logs into certified, delivered products continues to require an accountable industrial operator.

## Risks and uncertainty
The largest uncertainties are automation already installed by mill size, normalization of EBITDA across commodity cycles, owner succession outcomes, housing sensitivity, fiber availability, tariffs, environmental liabilities, and how much yield improvement survives competitive repricing.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1284 | — | OBSERVED | — |
| n | — | 496 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.3 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.52 | 0.7 | ESTIMATE | S3, S4 |
| e | 0.72 | 0.84 | 0.93 | ESTIMATE | S1 |
| s5 | 0.18 | 0.3 | 0.44 | PROXY | S5 |
| q | 0.32 | 0.5 | 0.68 | ESTIMATE | S6 |
| d5 | 0.9 | 1.03 | 1.18 | PROXY | S7, S8 |
| o | 0.96 | 0.985 | 1 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.22 | 0.53 | 1.08 | ESTIMATE |
| F | 6.72 | 7.78 | 8.55 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 8.64 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation data combine sawmills with wood preservation and cover employers rather than self-employed workers.
- a: No national survey reports the installed base of AI-capable scanners by mill size.
- rho: Vendor evidence demonstrates availability, not representative adoption or realized substitution.
- rho: The frozen LMM band may include mills with sharply different automation economics.
- e: Census reports 2,691 employer establishments, not firms or the frozen EBITDA-band population.
- e: The injected n estimate is margin-bridged and may be especially unstable in a cyclical commodity industry.
- s5: The retirement statistics are not national or sawmill-specific.
- s5: Intent to retire is not an observed control-transfer rate and may end in closure.
- q: Public-company commentary concerns larger North American producers, not the LMM population.
- q: Retention differs between commodity softwood, specialty hardwood, custom grades, and by-products.
- d5: Housing starts are not lumber consumption and the cited forecast covers only 2026-2027.
- d5: The current demand base may be cyclically depressed, making ratios sensitive to the starting month.
- o: Some demand can move to engineered wood, steel, concrete, imports, or vertically integrated producers.
- o: This primitive concerns operator requirement, not labor intensity inside the operator.

## Sources
- **S1** — [321113: Sawmills - Census Bureau Profile](https://data.census.gov/profile/321113_-_Sawmills?codeset=naics~321113) (accessed 2026-07-23): Defines sawmill activities and reports 2,691 employer establishments in 2023 County Business Patterns.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-23): Lists the largest occupations in Sawmills and Wood Preservation, led by sawing-machine operators, laborers/material movers, industrial-truck operators, woodworking-machine operators, supervisors, and maintenance roles.
- **S3** — [Machine Vision Activities in the Wood Industry](https://www.automate.org/vision/industry-insights/machine-vision-activities-in-the-wood-industry) (accessed 2026-07-23): Documents long-standing 3D optimization and automated inspection/grading applications throughout sawmills, including breakdown, curve sawing, edging, trimming, and sorting.
- **S4** — [Lisker sawmill measurement and optimization systems](https://www.lisker.fi/en/) (accessed 2026-07-23): Describes AI-assisted timber defect detection and over 350 measurement and optimization system deliveries across sawlines, grading, and feeding.
- **S5** — [Ward Lumber Transitions Ownership to Employees](https://www.sba.gov/success-stories/ward-lumber-transitions-ownership-employees-thanks-sba-resource-partner) (accessed 2026-07-23): Sawmill-related SBA case cites regional surveys in which 57% of owners wanted to retire within five years and fewer than one in five had a credible succession plan.
- **S6** — [West Fraser 2025 Annual Management Discussion and Analysis](https://www.sec.gov/Archives/edgar/data/1402388/000140238826000009/exhibit993-2025annualmda.htm) (accessed 2026-07-23): Reports modest expected lumber demand, mill closures, operational gains, and stumpage rates linked to lumber prices, evidencing commodity-cycle and market-price exposure.
- **S7** — [2026 Housing Outlook: Ongoing Challenges, Cautious Optimism and Incremental Gains](https://www.nahb.org/news-and-economics/press-releases/2026/02/2026-housing-outlook-ongoing-challenges-cautious-optimism-and-incremental-gains) (accessed 2026-07-23): Forecasts single-family starts rising 1% in 2026 and 5% in 2027, while multifamily starts decline in both years.
- **S8** — [May Housing Starts Fall as Multifamily Construction Slows Sharply](https://www.nahb.org/news-and-economics/press-releases/2026/06/may-housing-starts-fall-as-multifamily-construction-slows-sharply) (accessed 2026-07-23): Reports May 2026 single-family starts at an 882,000 annual rate, down 6.7% year over year, and identifies affordability and elevated rates as headwinds.
