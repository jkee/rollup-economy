# 321991 — Manufactured Home (Mobile Home) Manufacturing

*v5.1 Stage 1 research memo. Run `321991-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.65 · L 0.65 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat dealer programs can support transferable operations and AI-assisted planning, procurement, documentation, and warranty workflows.
**Weakness:** Most value creation is physical product manufacturing, leaving a small exposed labor share and a poor fit with a recurring outsourced-service lens.

## Business-model lens
- Included: Independent US manufacturers of HUD-code manufactured homes with repeat dealer, community-operator, or institutional-customer programs and sufficient standalone management to support a control transfer.
- Excluded: Captive plants, non-HUD modular construction, retailers and installers without manufacturing operations, project shells, and manufacturers whose sales are only isolated consumer transactions.
- Customer and revenue model: Homes are sold per unit, commonly through recurring dealer and distributor relationships; revenue is product and shipment based rather than a recurring service fee.
- Deviation from default lens: The code is a product-manufacturing industry rather than an outsourced-service industry, so the lens retains only firms with repeat external B2B supply relationships; this narrowing is necessary to make eligibility coherent.

## Executive view
The opportunity is constrained by the mismatch between a recurring-service acquisition lens and a concentrated product-manufacturing industry. Eligible firms can still have repeat dealer programs and transferable plants, but AI affects only a minority of wage-weighted work because assembly, material movement, inspection, and installation remain physical.

## How AI changes the work
AI is most relevant to order configuration, estimating, procurement, production scheduling, engineering documentation, compliance preparation, dealer support, warranty triage, and administrative work. It is a decision-support and workflow layer rather than a replacement for the production line.

## Value capture
Savings may be retained between price resets and through improved throughput or lower rework, but a comparable and affordability-sensitive home product exposes gains to dealer negotiation and price competition. Product-level gross-margin evidence is needed before assuming durable capture.

## Firm availability
The injected LMM firm count is uncertain for this industry because published late-2024 industry data indicate only 38 manufacturers and 152 plants. A modest five-year ownership-transfer propensity is plausible, but the independently owned, recurring-B2B subset is likely much smaller than the dataset total.

## Demand durability
Demand benefits from the need for lower-cost housing, yet shipments remain highly sensitive to financing, rates, zoning, sites, and the broader housing cycle. Recent growth reversed into early-2026 softness, supporting a wide range around modest five-year real growth.

## Risks and uncertainty
The main risks are lens ineligibility, manufacturer concentration, cyclical volumes, financing constraints, regulatory accountability, fragmented plant systems, and the possibility that apparent labor savings are offset by implementation and quality costs. The six-digit occupation mix and actual transfer history are not publicly observed.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2786 | — | OBSERVED | — |
| n | — | 63 | — | ESTIMATE | — |
| a | 0.07 | 0.13 | 0.22 | PROXY | S1, S2 |
| rho | 0.25 | 0.45 | 0.65 | ESTIMATE | S2 |
| e | 0.08 | 0.18 | 0.32 | ESTIMATE | S3 |
| s5 | 0.12 | 0.21 | 0.32 | PROXY | S4 |
| q | 0.3 | 0.5 | 0.7 | ESTIMATE | S3, S5 |
| d5 | 0.9 | 1.04 | 1.2 | PROXY | S3, S5, S6 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.20 | 0.65 | 1.59 | ESTIMATE |
| F | 0.76 | 1.96 | 3.23 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.46 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is for NAICS 321900, not the six-digit industry.
- a: The estimate excludes already-automated tasks but public occupational data do not identify current automation penetration.
- rho: No industry-wide five-year AI implementation study was located.
- rho: Implementation may be harder in smaller plants with fragmented ERP and dealer-order systems.
- e: The injected n is a margin-bridged estimate based on size-class averages and may count establishments or firms that do not fit the recurring-service lens.
- e: No public dataset measures repeat-customer revenue by manufacturer.
- s5: Cross-industry owner survey; intentions are not completed transactions.
- s5: Internal family gifts and sales to strategic consolidators may not leave a standalone transferable operation.
- q: No public evidence directly measures pass-through of manufacturing productivity savings.
- q: Material-price volatility can obscure whether margin changes come from AI or input costs.
- d5: Shipments are cyclical and sensitive to rates, chattel financing, zoning, and site availability.
- d5: The BLS projection is for NAICS 321900, much broader than manufactured homes.
- o: This measures operator requirement, not labor intensity.
- o: Manufactured Housing Survey coverage excludes modular homes, so cross-system substitution is not directly observed.

## Sources
- **S1** — [Other Wood Product Manufacturing - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_321900.htm) (accessed 2026-07-22): Broader-industry occupation mix: 51.76% production, 20.49% assemblers and fabricators, 19.91% woodworkers, with management and business occupations much smaller.
- **S2** — [Production occupations - Occupational Requirements Survey](https://www.bls.gov/ors/factsheet/productions-occupations.htm) (accessed 2026-07-22): Physical and training requirements: production workers spent 83.3% of the workday standing on average; reaching was required for 87.8%; on-the-job training for 89.9%.
- **S3** — [MHI Economic Report: Production and Shipments See Strong Year-End Finish](https://www.manufacturedhousing.org/news/mhi-economic-report-production-and-shipments-see-strong-year-end-finish/) (accessed 2026-07-22): December 2024 shipment growth, 103,571 SAAR, 152 plants, 38 manufacturers, and manufactured housing share of single-family starts.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): US employer-owner age and transfer intentions: 52.3% age 55 or older and 22% of employer-business owners planned a sale or transfer within five years.
- **S5** — [MHI March 2026 Economic Report: Production and Shipment Trends Show Slowdown](https://www.manufacturedhousing.org/news/mhi-member-exclusive-march-2026-economic-report-production-and-shipment-trends-show-slowdown/) (accessed 2026-07-22): March 2026 production down 2.3% year over year and 9.0% year to date; shipment SAAR 100,540, down 5.2% from 2025.
- **S6** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects broader NAICS 321900 real output from 56.8 in 2024 to 67.3 billion chained 2017 dollars in 2034, a 1.7% annual rate.
- **S7** — [About the Manufactured Housing Survey](https://www.census.gov/programs-surveys/mhs/about.html) (accessed 2026-07-22): Survey scope covers all new manufactured homes receiving federal inspection and reports shipments, prices, and characteristics; modular homes are outside the survey.
