# 812332 — Industrial Launderers

*v5.1 Stage 1 research memo. Run `812332-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.11 · L 1.66 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent physical service obligations combined with recurring routes and contracts.
**Weakness:** Only a limited share of total work is susceptible to incremental software-led automation, and existing plant automation narrows the remaining opportunity.

## Business-model lens
- Included: U.S. industrial laundries supplying laundered work uniforms, protective and clean-room apparel, and dust-control textiles on rental or contract service routes, including washing, finishing, inventory control, pickup, and delivery.
- Excluded: Consumer coin laundries and dry cleaners, linen-only supply services classified elsewhere, captive in-house laundries, textile manufacturing, and firms outside the lower-middle-market operating-company population.
- Customer and revenue model: Recurring business-to-business rental or service contracts combining textile inventory, scheduled laundering, replacement, and route delivery; ancillary revenue can include loss charges, special processing, and related facility-service items.
- Deviation from default lens: none

## Executive view
Industrial laundering is a recurring, route-based physical service with substantial plant and textile assets. Its defensibility comes from the need to collect, process, track, and return physical goods, while incremental technology opportunity is concentrated in the information and control layers around an already mechanized operation.

## How AI changes the work
The most credible near-term uses are route and production scheduling, inventory and RFID exception handling, demand forecasting, visual inspection, preventive maintenance, billing, and customer communication. They can improve utilization and consistency, but direct plant labor and route work remain dependent on machinery, material handling, and people; industry evidence also indicates that meaningful conventional automation is already installed in many workflows.

## Value capture
Recurring contracts and service differentiation provide a path to retain some gains through higher reliability, lower loss, better route density, and fewer production disruptions. Competitive rebids and customer procurement can pass back part of cost savings, while hardware integration and plant upgrades absorb part of the benefit.

## Firm availability
The exact code maps to a coherent operating-company model with transferable plants, routes, inventory, and customer agreements. Availability is still a minority event: owner intentions overstate completed sales, and consolidation, concentration, environmental diligence, and plant condition determine which firms are genuinely actionable.

## Demand durability
The physical service remains tied to uniforms, protective requirements, clean-room operations, and facility cleanliness. Broad-industry real-output projections imply modest growth, but the exact industrial segment may diverge with manufacturing activity, outsourcing, disposables, and customer employment.

## Risks and uncertainty
The largest uncertainties are exact-code task composition, the amount of automation already embedded in plants, implementation economics across legacy systems, environmental and energy exposure, route and customer concentration, and reliance on broader NAICS evidence for growth and occupations.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3595 | — | OBSERVED | — |
| n | — | 42 | — | ESTIMATE | — |
| a | 0.14 | 0.24 | 0.36 | PROXY | S2, S4 |
| rho | 0.3 | 0.48 | 0.65 | ESTIMATE | S4 |
| e | 0.7 | 0.84 | 0.93 | ESTIMATE | S1 |
| s5 | 0.08 | 0.14 | 0.22 | PROXY | S5 |
| q | 0.42 | 0.6 | 0.74 | ESTIMATE | S1, S4 |
| d5 | 0.95 | 1.08 | 1.18 | PROXY | S3 |
| o | 0.82 | 0.92 | 0.97 | ESTIMATE | S1, S2, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.60 | 1.66 | 3.36 | ESTIMATE |
| F | 1.95 | 2.87 | 3.64 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.79 | 9.94 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source covers NAICS 812300 rather than only 812332.
- a: Industry technology examples establish feasibility and current baseline, not a measured task share.
- rho: No representative exact-code adoption or realized-benefit study was located.
- rho: The estimate separates incremental AI realization from mechanical automation already in place.
- e: The industry definition does not measure ownership independence or transaction readiness.
- e: Mixed-service operators can be classified inconsistently across adjacent laundry codes.
- s5: The proxy is cross-industry and measures intentions rather than completed transactions.
- s5: Private add-on acquisitions and family transfers are incompletely visible in public data.
- q: No exact-code study directly measures retained economics from AI or advanced software.
- q: Capture varies with local route density, contract duration, and customer bargaining power.
- d5: The BLS projection aggregates industrial, consumer, and other laundry services.
- d5: Real output is not identical to demand faced by a representative lower-middle-market operator.
- o: Obligation differs across ordinary uniforms, protective apparel, clean-room garments, and dust-control products.
- o: A high value reflects persistence of the physical service, not immunity from price or volume pressure.

## Sources
- **S1** — [2022 NAICS definition: 812332 Industrial Launderers](https://www.census.gov/naics/?details=812332&input=812332&year=2022) (accessed 2026-07-22): Defines establishments supplying laundered industrial work uniforms, protective and clean-room apparel, and dust-control items on a rental or contract basis.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 812300](https://www.bls.gov/oes/2023/may/naics4_812300.htm) (accessed 2026-07-22): Shows the broader laundry and dry-cleaning industry's occupational mix, including large production and transportation/material-moving shares.
- **S3** — [BLS industry employment and output projections](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Reports projected 2024-2034 employment and real output for the broader NAICS 812300 industry.
- **S4** — [TRSA Trends Q&A: Industrial laundry technology and automation](https://www.trsa.org/wp-content/uploads/2026/02/RicciTrendsQAMarch26.pdf) (accessed 2026-07-22): Describes deployed wash-aisle and soil-sort automation, RFID and tracking systems, conveyors, and utility-efficiency technology in industrial laundries.
- **S5** — [Gallup: Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports national employer-business-owner intentions to sell or transfer within five years and the gap in succession preparation.
- **S6** — [BLS 2023 injury and illness rates by industry](https://www.bls.gov/iif/nonfatal-injuries-and-illnesses-tables/table-1-injury-and-illness-rates-by-industry-2023-national.htm) (accessed 2026-07-22): Reports a 2023 total recordable incidence rate of 3.4 for NAICS 812332, corroborating the industry's material physical-operating exposure.
