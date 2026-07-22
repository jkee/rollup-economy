# 313210 — Broadwoven Fabric Mills

*v5.1 Stage 1 research memo. Run `313210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.76 · L 0.89 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat physical B2B demand with opportunities to improve information-heavy workflows without displacing the accountable mill operator.
**Weakness:** Most labor is tied to physical production while domestic fabric output faces structural import and substitution pressure.

## Business-model lens
- Included: US lower-middle-market mills that repeatedly weave broadwoven fabrics or felts for external business customers, including mills that also finish or further fabricate their woven output.
- Excluded: Captive weaving operations, non-control financing vehicles, shell entities, rug and tire-fabric mills, standalone finishing mills, and firms without recurring external-customer supply relationships.
- Customer and revenue model: Repeat B2B sale of fabric by order, specification, yardage, or production run, with some contract/jobber arrangements and customer-specific finishing or fabrication.
- Deviation from default lens: none

## Executive view
Broadwoven mills sell a necessary physical intermediate through repeat B2B relationships, but the near-term AI opportunity is mainly around the plant rather than at the loom. The opportunity depends on disciplined workflow deployment in planning, quoting, quality support, maintenance, purchasing, and administration while preserving accountable physical operations.

## How AI changes the work
AI can structure specifications and orders, forecast schedules and material needs, assist root-cause and maintenance analysis, triage visual defects, draft compliance documentation, and automate routine customer and back-office work. Most operator, setup, material-handling, repair, and final quality-accountability tasks remain physical and are not counted as substitutable simply because conventional machinery can automate them.

## Value capture
Unit- or order-priced fabric lets an early operator retain some labor and throughput benefit, but powerful buyers, competitive bids, import alternatives, and renewal repricing should share much of it over five years. Savings that improve lead time, quality consistency, or small-batch economics may retain better than generic office efficiencies.

## Firm availability
The frozen dataset estimates 77 firms in the EBITDA band, but only an estimated subset has repeat external-customer revenue, independent control, defensible normalized earnings, and transferable operations. Manufacturing owner-age evidence indicates succession pressure, though age is a weak proxy for a completed qualifying sale.

## Demand durability
Fabric remains a physical input and therefore needs an accountable operator, but domestic output is exposed to imports, offshore customer production, alternative textile structures, and consolidation. Broader Fabric Mills production fell sharply after 2021 but stabilized around 2023-2025, supporting a declining rather than collapsing five-year base case.

## Risks and uncertainty
The largest uncertainties are the lack of 313210-specific occupation and AI implementation data, reliance on broader 3132 production, heterogeneous end markets, and unobserved firm-level transferability. Legacy equipment integration, mill data quality, customer concentration, environmental or safety liabilities, and false quality decisions could erase implementation gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3084 | — | OBSERVED | — |
| n | — | 77 | — | ESTIMATE | — |
| a | 0.1 | 0.16 | 0.24 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.45 | 0.6 | ESTIMATE | S4 |
| e | 0.55 | 0.68 | 0.8 | ESTIMATE | S1 |
| s5 | 0.12 | 0.2 | 0.28 | PROXY | S5 |
| q | 0.35 | 0.5 | 0.65 | ESTIMATE | S6 |
| d5 | 0.75 | 0.85 | 0.95 | PROXY | S1, S7 |
| o | 0.94 | 0.97 | 0.99 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.43 | 0.89 | 1.78 | ESTIMATE |
| F | 2.90 | 3.92 | 4.67 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.05 | 8.24 | 9.40 | ESTIMATE |

## Caveats
- a: OEWS publishes the relevant occupation evidence at 3132 rather than 313210.
- a: The estimate excludes conventional loom, sensor, and robotics automation already embodied in current operations.
- a: Census AI adoption evidence covers all US businesses, not textile mills specifically.
- rho: No source directly measures five-year AI implementation in broadwoven mills.
- rho: Small LMM mills may have less clean data and integration capacity than the average adopter.
- e: Eligibility is estimated against the frozen n=77 rather than observed firm-level screening.
- e: SUSB-derived firm counts and NAICS establishments need not map one-to-one.
- s5: The source population is women-owned manufacturing across broad demographic groups, not all broadwoven mills.
- s5: Aging-owner prevalence does not measure completion of a transferable control sale.
- q: PPI measures output prices, not the share of an AI benefit retained.
- q: Customer bargaining power and import exposure vary materially by fabric specification and end market.
- d5: The production series is 3132, not 313210.
- d5: Pandemic normalization affects the 2021 comparison.
- d5: The Federal Reserve notes that since 2022 textile detail has relied on production-worker hours, which is an imperfect output proxy.
- o: Operator requirement is estimated rather than directly surveyed.
- o: Material substitution to nonwovens, knits, composites, or imported finished goods belongs partly in demand and could also reduce the operator-required share.

## Sources
- **S1** — [2022 NAICS Definition: 313210 Broadwoven Fabric Mills](https://www.census.gov/naics/?details=31321&input=31321&year=2022) (accessed 2026-07-22): Defines 313210 as establishments weaving broadwoven fabrics and felts, including weaving-only and mills that also finish or further fabricate products.
- **S2** — [May 2024 OEWS occupation-industry chart data](https://www.bls.gov/oes/2024/may/occ_ind_emp_chart/occ_ind_emp_chart_data.htm) (accessed 2026-07-22): Reports 8,310 textile knitting and weaving machine operators and 4,280 textile winding, twisting, and drawing-out operators employed in Fabric Mills.
- **S3** — [BLS Occupational projections and worker characteristics](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Reports projected 2024-2034 declines of 11.2% for textile knitting and weaving machine operators and 10.2% for textile machine operators overall, contextualizing an already-automated physical workforce.
- **S4** — [Tracking Firm Use of AI in Real Time: A Snapshot from the Business Trends and Outlook Survey](https://www.census.gov/library/working-papers/2024/adrm/CES-WP-24-16.html) (accessed 2026-07-22): Reports economy-wide business AI use rising from 3.7% to 5.4% from September 2023 to February 2024, expected use near 6.6% by early fall 2024, and workflow and training changes among adopters.
- **S5** — [The Metamorphosis of Women Business Owners: A Focus on Age](https://www2.census.gov/ces/wp/2024/CES-WP-24-71.pdf) (accessed 2026-07-22): Census 2021 ABS analysis shows manufacturing among sectors with high shares of owners age 55 and over in multiple race and ethnicity groups, including reported values from 44.4% to 63.1%.
- **S6** — [September 2024 Producer Price Index Detailed Report](https://www.bls.gov/ppi/detailed-report/ppi-detailed-report-september-2024.pdf) (accessed 2026-07-22): Reports the 313210 broadwoven fabric mill output price index at 164.106 in May 2024 and 163.568 in September 2024, with product-level detail.
- **S7** — [Industrial Production: Fabric Mills (NAICS 3132)](https://fred.stlouisfed.org/series/IPG3132A) (accessed 2026-07-22): Federal Reserve series reports annual 3132 industrial production of 89.8390 in 2021, 81.7985 in 2022, 74.6653 in 2023, 75.6519 in 2024, and 75.8120 in 2025.
