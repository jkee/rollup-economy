# 327215 — Glass Product Manufacturing Made of Purchased Glass

*v5.1 Stage 1 research memo. Run `327215-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.68 · L 0.87 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A sizable independent-fabricator pool combines repeat customer relationships with digitizable quoting, planning, and quality workflows around an irreducibly physical product.
**Weakness:** Cyclical end markets and unobserved firm-level eligibility, EBITDA, transfer rates, and pass-through leave the scale of attainable opportunity uncertain.

## Business-model lens
- Included: U.S. lower-middle-market firms that repeatedly coat, laminate, temper, cut, bend, or otherwise shape purchased glass for external architectural, residential, transportation, appliance, furniture, or industrial customers.
- Excluded: Captive internal plants, non-control investment vehicles, primary glass melting, pure distribution, field installation without manufacturing, and consumer retail operations without a recurring external-customer fabrication business are excluded.
- Customer and revenue model: Repeat business-to-business fabrication orders, often job-, unit-, square-foot-, or program-priced to drawings and performance specifications, with revenue from processed glass and associated fabrication rather than a separately metered labor service.
- Deviation from default lens: none

## Executive view
Purchased-glass fabrication is a comparatively coherent, fragmented repeat B2B model with many information-heavy workflows around complex physical orders. AI can assist quoting, drawings, scheduling, nesting, inspection, customer service, and administration, while the glass transformation and accountable quality release remain physical and operator-required.

## How AI changes the work
The most implementable opportunities sit before and around the line: extracting specifications, estimating, optimizing cuts, promising dates, sequencing loads, generating paperwork, triaging defects, and analyzing downtime. Custom geometry, safety-glass requirements, remake cost, legacy equipment, and material handling keep humans in approval and execution loops.

## Value capture
Speed, reliability, low remakes, certification, specialty capabilities, and freight proximity create value beyond raw processing cost. Customers still compare bids and rebid repeat work, so some benefits are passed through, but rapid-turn and qualified fabricators should retain more than commodity job shops.

## Firm availability
The injected LMM estimate of 186 firms suggests a meaningful possible pool, but it must be filtered for independent ownership, repeat external revenue, manufacturing rather than installation or retail, and actual normalized EBITDA. No measured 327215 control-transfer cohort was available.

## Demand durability
Architectural, window, transportation, appliance, furniture, and specialty end markets preserve a broad physical demand base. High-performance and retrofit glazing provide upside, while construction and auto cycles, imports, substitution, and customer insourcing create a wide range around modest growth.

## Risks and uncertainty
The main gaps are six-digit task data, firm eligibility, realized implementation, contractual pass-through, and transfers. Construction exposure, customer concentration, breakage and remakes, product liability, certification, equipment bottlenecks, glass input and freight volatility, and working capital can outweigh software gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1936 | — | OBSERVED | — |
| n | — | 186 | — | ESTIMATE | — |
| a | 0.13 | 0.23 | 0.36 | PROXY | S2, S3 |
| rho | 0.28 | 0.49 | 0.7 | ESTIMATE | S3 |
| e | 0.52 | 0.7 | 0.84 | ESTIMATE | S1 |
| s5 | 0.15 | 0.28 | 0.41 | ESTIMATE | — |
| q | 0.38 | 0.59 | 0.77 | ESTIMATE | — |
| d5 | 0.88 | 1.03 | 1.19 | PROXY | S4, S5 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.87 | 1.95 | ESTIMATE |
| F | 4.41 | 5.83 | 6.72 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.27 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational evidence is 2016 and four-digit rather than current six-digit data.
- a: The DOE machine-learning example concerns primary flat-glass furnace control, not purchased-glass fabrication.
- rho: No representative 327215 implementation-rate study was found.
- rho: Small custom shops and scaled automated fabricators will implement at very different rates.
- e: The injected n of 186 is an ESTIMATE derived from receipts and a sector margin rather than observed 327215 EBITDA.
- e: Industry counts may mix standalone firms with establishments inside larger window, automotive, or building-products groups.
- s5: Neither qualifying transfers nor the eligible denominator are directly observed.
- s5: Automotive, architectural, residential, and specialty processors likely have different buyer pools and succession patterns.
- q: No representative contract or causal cost-to-price dataset was available.
- q: Retention should be lower in standardized commodity cutting and higher in qualified, complex, rapid-turn, or specialty fabrication.
- d5: Four-digit production is not six-digit demand and can diverge through trade and inventory.
- d5: DOE's window energy statistic establishes a use-case opportunity, not the adoption rate or five-year fabricated-glass volume.
- o: This is bounded judgment rather than a measured operator-required share.
- o: Automation can sharply reduce touches per unit without eliminating the accountable operating firm, which this primitive distinguishes.

## Sources
- **S1** — [2022 NAICS Definition: 327215 Glass Product Manufacturing Made of Purchased Glass](https://www.census.gov/naics/?details=3272&input=3272&year=2022) (accessed 2026-07-22): Defines 327215 as establishments primarily engaged in coating, laminating, tempering, or shaping purchased glass.
- **S2** — [May 2016 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 327200](https://www.bls.gov/oes/2016/may/naics4_327200.htm) (accessed 2026-07-22): Reports 85,250 jobs and occupation shares including production 55.08%, office support 8.50%, management 3.97%, engineering 2.79%, business and financial operations 2.22%, and sales 2.35%.
- **S3** — [High Performance Computing Improves Manufacturing Productivity and Competitiveness in the Glass Industry](https://www.energy.gov/cmei/ammto/articles/high-performance-computing-improves-manufacturing-productivity-and) (accessed 2026-07-22): Adjacent glass-process evidence that machine learning can convert computational modeling into real-time operating guidance; the documented surrogate moved analysis from up to two weeks to minutes.
- **S4** — [Department of Energy Windows Technologies Subprogram](https://www.energy.gov/cmei/buildings/windows) (accessed 2026-07-22): Reports that windows account for about 10% of building energy use and influence end uses comprising 40%, and identifies highly insulating windows, dynamic solar control, and daylighting as development areas.
- **S5** — [Industrial Production: Glass and Glass Product Manufacturing (NAICS 3272)](https://fred.stlouisfed.org/series/IPG3272N) (accessed 2026-07-22): Federal Reserve broad real-output proxy; May 2026 was 94.2941 on a 2017=100 index.
