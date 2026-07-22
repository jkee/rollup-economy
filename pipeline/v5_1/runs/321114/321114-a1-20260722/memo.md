# 321114 — Wood Preservation

*v5.1 Stage 1 research memo. Run `321114-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.11 · L 0.28 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Regulated, specification-heavy treatment for long-lived infrastructure supports repeat, operator-required demand.
**Weakness:** A small firm universe and environmental-transfer risk constrain feasible acquisitions, while low labor intensity limits AI savings.

## Business-model lens
- Included: Independent U.S. facilities that repeatedly pressure- or thermally treat lumber, railroad ties, utility poles, posts, pilings, crossarms, and similar wood for external customers.
- Excluded: Captive treating operations, untreated sawmilling, chemical manufacturing, in-field remedial pole treatment classified outside the industry, non-operating property entities, and facilities lacking transferable permits or operations.
- Customer and revenue model: Repeat batch product and toll-treatment sales to lumber distributors, railroads, utilities, infrastructure contractors, agricultural suppliers, and builders, generally priced per unit or volume with wood and preservative inputs reflected in quotes or contracts.
- Deviation from default lens: none

## Executive view
Wood preservation is a small, regulated process-manufacturing industry with durable repeat demand from construction and infrastructure. AI opportunity exists in quality, process advice, maintenance, compliance, logistics, and administration, but compensation is a small share of receipts and the physical hazardous-chemical process remains asset- and operator-dependent.

## How AI changes the work
AI can detect treatment anomalies, recommend recipes, anticipate equipment failure, inspect material, sequence charges, and automate traceability and reports. Human accountability remains essential for loading, sampling, maintenance, certified pesticide application, safety, and environmental response.

## Value capture
Approved-supplier status and quality consistency can protect some gains in utility, rail, and marine products. Commodity residential lumber is more exposed to competitive repricing, and input-linked contracts may reveal cost reductions.

## Firm availability
The frozen population is only 57 estimated firms, and environmental liabilities, permit transferability, captive ownership, and normalized earnings can shrink it substantially. Succession pressure is plausible but not directly measured for treaters.

## Demand durability
Preservation extends the usefulness of wood in exposed settings, with repeat demand across remodeling, construction, rail, utility, agricultural, and marine uses. Alternative materials and chemical restrictions are the principal threats, while an accountable treatment operator remains necessary for nearly all surviving volume.

## Risks and uncertainty
Critical risks are contaminated sites, worker exposure, preservative registration changes, product liability, customer concentration, housing cyclicality, wood and chemical input volatility, and a lack of direct adoption and transaction evidence for the small-firm population.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0819 | — | OBSERVED | — |
| n | — | 57 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.27 | PROXY | S1, S2 |
| rho | 0.3 | 0.48 | 0.65 | ESTIMATE | S2, S3 |
| e | 0.58 | 0.76 | 0.9 | ESTIMATE | S2, S3, S4 |
| s5 | 0.16 | 0.28 | 0.42 | PROXY | S6 |
| q | 0.4 | 0.58 | 0.75 | ESTIMATE | S3, S4 |
| d5 | 0.91 | 1.04 | 1.18 | ESTIMATE | S3, S4, S5 |
| o | 0.97 | 0.99 | 1 | ESTIMATE | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.10 | 0.28 | 0.57 | ESTIMATE |
| F | 2.96 | 4.14 | 5.01 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.83 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The available occupational source combines sawmills and wood preservation.
- a: No national evidence quantifies current control-system, sensor, or vision adoption by independent treating-plant size.
- rho: Regulation makes workflow automation valuable but raises the cost of errors.
- rho: This is bounded judgment rather than a measured adoption rate.
- e: The injected n is margin-bridged from industry-average economics and may misclassify plants with volatile wood and chemical costs.
- e: Eligibility can be lost through site-specific environmental liabilities that industry-level data cannot reveal.
- s5: The source is a New York lumber case, not a national wood-preservation cohort.
- s5: No observed denominator of eligible plants or qualifying transfers is available.
- q: Retention varies sharply between commodity decking lumber and specification-heavy rail, pole, piling, or marine products.
- q: No public evidence directly measures automation-benefit pass-through in LMM treaters.
- d5: Housing forecasts cover only part of the service basket and only the first two forecast years.
- d5: Rail and utility demand is inferred from durable end uses rather than an observed five-year volume forecast.
- o: Material substitution can eliminate some treated-wood quantity even though remaining treatment still requires an operator.
- o: Permitting and certification are jurisdiction- and chemistry-specific.

## Sources
- **S1** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-23): Shows the broader Sawmills and Wood Preservation occupation mix led by physical production, material-moving, driving, supervision, and maintenance roles.
- **S2** — [Wood Preserving Area Sources: National Emission Standards for Hazardous Air Pollutants](https://www.epa.gov/stationary-sources-air-pollution/wood-preserving-area-sources-national-emission-standards-hazardous) (accessed 2026-07-23): Defines pressure and thermal wood preservation and details regulated pollutants, enclosed-vessel equipment, and management-practice requirements.
- **S3** — [Overview of Wood Preservative Chemicals](https://www.epa.gov/ingredients-used-pesticide-products/overview-wood-preservative-chemicals) (accessed 2026-07-23): Documents restricted-use heavy-duty preservatives, commercial rail and pole uses, residential preservative systems, and ongoing registration review.
- **S4** — [Creosote](https://www.epa.gov/ingredients-used-pesticide-products/creosote) (accessed 2026-07-23): States that creosote protects railroad ties and utility poles, is applied using high-pressure equipment by certified applicators, and carries worker and ecological risks.
- **S5** — [2026 Housing Outlook: Ongoing Challenges, Cautious Optimism and Incremental Gains](https://www.nahb.org/news-and-economics/press-releases/2026/02/2026-housing-outlook-ongoing-challenges-cautious-optimism-and-incremental-gains) (accessed 2026-07-23): Forecasts single-family starts up 1% in 2026 and 5% in 2027 and real remodeling activity up 3% and 2%, respectively.
- **S6** — [Ward Lumber Transitions Ownership to Employees](https://www.sba.gov/success-stories/ward-lumber-transitions-ownership-employees-thanks-sba-resource-partner) (accessed 2026-07-23): A lumber-sector succession case citing regional surveys where 57% of owners sought retirement within five years and fewer than one in five had a credible succession plan.
