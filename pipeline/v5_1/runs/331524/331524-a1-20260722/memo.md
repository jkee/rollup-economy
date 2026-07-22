# 331524 — Aluminum Foundries (except Die-Casting)

*v5.1 Stage 1 research memo. Run `331524-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.38 · L 1.03 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High labor intensity and repeat engineered programs create useful AI support opportunities around quoting, methoding, quality, maintenance, and scheduling.
**Weakness:** Most labor is physical and part-specific, while broad foundry demand is projected to contract and implementation data are scarce.

## Business-model lens
- Included: Independent US aluminum foundries outside die casting, in the approximately $1-10 million normalized EBITDA band, repeatedly producing customer-designed sand, permanent-mold, semi-permanent-mold, investment, or related castings for external customers.
- Excluded: Die casters, captive foundries, establishments further manufacturing castings into their own finished products, primary aluminum producers, shells, non-control financing vehicles, and firms outside the EBITDA band.
- Customer and revenue model: Recurring engineered business-to-business casting programs priced per part or lot with separate pattern, tooling, engineering, finishing, testing, and metal-surcharge economics under quotes, releases, purchase orders, and supply agreements.
- Deviation from default lens: none

## Executive view
Aluminum foundries have recurring engineered customer programs and very high injected labor intensity, but the labor is overwhelmingly physical. AI is credible in estimating, methoding support, documentation, quality analytics, maintenance knowledge, scheduling, and administration, with implementation constrained by low-volume data and process accountability.

## How AI changes the work
AI can retrieve analogous jobs, assist quotes and routings, summarize defect histories, prioritize maintenance, schedule work, and draft quality records. Mold and core making, melting, pouring, shakeout, finishing, inspection release, handling, and maintenance remain physical or human-supervised.

## Value capture
Complexity, patterns, qualification, and switching costs help retain yield, lead-time, and reliability gains. Metal surcharges, cost-down requests, rebids, and customer bargaining return part of recurring savings.

## Firm availability
The frozen estimate of 107 band firms is meaningful but depends on a machinery margin bridge that may conflict with the high observed labor ratio. Captive status, customer concentration, environmental liabilities, equipment, management, and qualifications determine actual eligibility.

## Demand durability
Aluminum lightweighting and diverse transportation, aerospace, industrial, and defense uses offset broad foundry contraction. BLS's declining foundry forecast and AFS's positive one-year sales outlook point to a near-flat but uncertain five-year quantity path.

## Risks and uncertainty
Key gaps are process-specific occupation data, existing simulation and automation, direct shipment forecasts, customer program exposure, import competition, contract terms, environmental liabilities, and true EBITDA. Technical defects and customer disqualification can overwhelm incremental savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3827 | — | OBSERVED | — |
| n | — | 107 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.22 | PROXY | S1, S2, S3 |
| rho | 0.3 | 0.48 | 0.65 | ESTIMATE | S3, S4 |
| e | 0.52 | 0.7 | 0.84 | ESTIMATE | S1, S4 |
| s5 | 0.14 | 0.25 | 0.38 | PROXY | S5, S4 |
| q | 0.35 | 0.57 | 0.76 | ESTIMATE | S1 |
| d5 | 0.86 | 0.98 | 1.13 | PROXY | S6, S7 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.37 | 1.03 | 2.19 | ESTIMATE |
| F | 3.50 | 4.80 | 5.73 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.26 | 9.70 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS covers all foundries rather than 331524.
- a: Sand, investment, and permanent-mold operations have materially different labor mixes.
- rho: No representative LMM implementation study was found.
- rho: Casting simulation and conventional optimization already address part of the opportunity and must not be relabeled as new AI benefit.
- e: Eligibility is not directly measured.
- e: The injected n=107 uses a machinery-sector margin bridge despite the industry's unusually high frozen compensation-to-receipts ratio.
- s5: Owner-age evidence is all-industry and data year 2018.
- s5: Age is not an observed sale or succession-completion rate.
- q: No observed retention sample was found.
- q: Retention differs between short-run engineered castings and higher-volume price-competed programs.
- d5: AFS sales growth is nominal, short-term, and covers all metalcasting.
- d5: BLS foundry output is broader than aluminum and not a physical constant-quality quantity series.
- o: Manufacturing-process substitution is captured principally in d5.
- o: Digital ordering and reporting can be self-served without removing the physical operator.

## Sources
- **S1** — [NAICS 331524: Aluminum Foundries (except Die-Casting)](https://www.census.gov/naics/?details=331524&input=331524&year=2022) (accessed 2026-07-22): Census defines the industry as aluminum foundries producing castings other than die castings and distinguishes establishments that further manufacture castings into finished products.
- **S2** — [Foundries - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_331500.htm) (accessed 2026-07-22): BLS provides employer-survey occupational employment and wage estimates for foundries, used as the broader occupation-mix evidence.
- **S3** — [Occupational projections and worker characteristics, 2024-2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): BLS reports 154,600 molding, coremaking, and casting machine setters, operators, and tenders in 2024 and projects 148,800 in 2034, a 3.8% decline.
- **S4** — [Aluminum, Copper, and Other Nonferrous Foundries: NESHAP for Area Sources](https://www.epa.gov/stationary-sources-air-pollution/aluminum-copper-and-other-nonferrous-foundries-national-emission) (accessed 2026-07-22): EPA states that smaller-emitting aluminum, copper, and other nonferrous foundries are subject to standards regulating beryllium, cadmium, chromium, lead, manganese, nickel, and other toxic emissions.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The 2019 Annual Business Survey infographic reports 51% of responding employer-business owners were age 55 or older, covering 4.1 million responding owners in data year 2018.
- **S6** — [Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects foundry employment declining 14.7% from 106,000 in 2024 to 90,400 in 2034 and real output declining from $26.9 billion to $24.8 billion, a 0.8% annual rate.
- **S7** — [AFS Projects 1.9 Percent Casting Sales Growth for 2025](https://www.afsinc.org/news/2025/07/22/afs-projects-19-percent-casting-sales-growth-2025) (accessed 2026-07-22): The American Foundry Society projected 1.9% casting sales growth for 2025 in its Metalcasting Forecast & Trends release.
