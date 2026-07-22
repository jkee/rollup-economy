# 327212 — Other Pressed and Blown Glass and Glassware Manufacturing

*v5.1 Stage 1 research memo. Run `327212-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.85 · L 0.76 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat qualified production offers practical AI-assisted quality, scheduling, engineering, and administrative workflows while preserving the need for a physical operator.
**Weakness:** NAICS heterogeneity and the absence of firm-level eligibility and transaction evidence make the transferable target population highly uncertain.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers that repeatedly make pressed, blown, or otherwise shaped non-container glassware and glass components to industrial or commercial customer specifications, including laboratory, technical, lighting, appliance, and specialty applications.
- Excluded: Branded consumer tableware sold principally through retail, one-off studio or art glass, captive internal plants, glass packaging containers, pure distributors, and firms whose only activity is installation are excluded.
- Customer and revenue model: Repeat business-to-business orders for specified glassware or components, commonly priced by unit, batch, tooling program, or supply agreement, with revenue primarily from manufactured products.
- Deviation from default lens: The code combines contract-like industrial and technical glass production with consumer tableware and one-off art glass. The lens retains repeat specification-driven B2B manufacturing and excludes retail-brand and one-off artistic models so customer economics and transferability are coherent; the narrowing is based on business-model incompatibility, not attractiveness.

## Executive view
The coherent target is repeat, specification-driven industrial and commercial glass production, not the code's consumer-brand or one-off art businesses. AI can improve inspection, planning, process decisions, quoting, and administration, but physical forming and handling dominate, and actual firm eligibility is uncertain.

## How AI changes the work
Machine vision and analytical models are most useful in defect detection, recipe support, yield analysis, predictive maintenance, scheduling, and technical paperwork. Continuous or repetitive lines can implement more than high-mix craft processes; skilled operators remain responsible for heat, tooling, changeovers, and quality release.

## Value capture
Technical qualification, tooling, and delivery reliability create some switching friction, allowing part of benefits to remain with the operator. Rebid cycles, industrial procurement, import competition, and cost transparency erode retention, especially for standardized products.

## Firm availability
The injected estimate of 51 LMM firms precedes the necessary filter for channel, recurrence, ownership, and actual EBITDA. The mixed code makes a bottom-up company map essential; transaction frequency and succession conditions are not observed at six digits.

## Demand durability
The product remains physical and operator-required, but demand varies by laboratory, lighting, appliance, and other technical end markets. Broad glass production is subdued rather than structurally expanding, with resilient qualified applications offset by imports, substitution, and customer offshoring.

## Risks and uncertainty
Major unknowns include the narrowed population's size, current occupation mix, plant digitization, realized AI labor savings, customer pass-through, and control transfers. Energy and furnace risk, specialized labor, product liability, environmental issues, customer concentration, imports, and obsolete product designs may outweigh AI benefits.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2369 | — | OBSERVED | — |
| n | — | 51 | — | ESTIMATE | — |
| a | 0.1 | 0.19 | 0.31 | PROXY | S2, S3 |
| rho | 0.22 | 0.42 | 0.63 | PROXY | S3 |
| e | 0.28 | 0.48 | 0.68 | ESTIMATE | S1 |
| s5 | 0.13 | 0.25 | 0.38 | ESTIMATE | — |
| q | 0.4 | 0.6 | 0.78 | ESTIMATE | — |
| d5 | 0.85 | 0.98 | 1.12 | PROXY | S4 |
| o | 0.91 | 0.97 | 1 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.76 | 1.85 | PROXY |
| F | 1.69 | 3.16 | 4.27 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.74 | 9.51 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source is 2016 and four-digit rather than current six-digit data.
- a: The process-control example concerns flat glass and is only an adjacent technology proxy.
- rho: No representative 327212 adoption study was found.
- rho: The estimate applies only to the exposed opportunity in a, not total labor or general productivity.
- e: The injected n of 51 is an ESTIMATE based on receipts and a sector margin rather than observed firm EBITDA.
- e: Product and channel heterogeneity makes establishment-level industry coding a weak proxy for firm eligibility.
- s5: The numerator and denominator for qualifying transfers are both unobserved.
- s5: Consumer glass and industrial specialty glass likely have materially different buyer universes.
- q: No contract-level pass-through study was available.
- q: Retention is likely higher in qualified technical components than in undifferentiated tableware or lighting glass.
- d5: Four-digit production can diverge from six-digit domestic demand because of trade, inventory, and product mix.
- d5: The historical index level does not directly measure a five-year forward demand ratio.
- o: This is judgment rather than a measured quantity.
- o: Automation can lower labor intensity substantially without eliminating the accountable operating firm, which remains required under this construct.

## Sources
- **S1** — [2022 NAICS Definition: 327212 Other Pressed and Blown Glass and Glassware Manufacturing](https://www.census.gov/naics/?details=327212&input=327212&year=2022) (accessed 2026-07-22): Official industry scope for pressed, blown, and shaped non-container glass and glassware, which spans materially different product and customer models.
- **S2** — [May 2016 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 327200](https://www.bls.gov/oes/2016/may/naics4_327200.htm) (accessed 2026-07-22): Reports 85,250 total jobs and broad occupation shares including production 55.08%, office support 8.50%, management 3.97%, business and financial operations 2.22%, and sales 2.35%.
- **S3** — [High Performance Computing Improves Manufacturing Productivity and Competitiveness in the Glass Industry](https://www.energy.gov/cmei/ammto/articles/high-performance-computing-improves-manufacturing-productivity-and) (accessed 2026-07-22): Adjacent glass-process evidence: a Vitro/LLNL machine-learning surrogate moved furnace analysis from up to two weeks to minutes and was designed for real-time control.
- **S4** — [Industrial Production: Glass and Glass Product Manufacturing (NAICS 3272)](https://fred.stlouisfed.org/series/IPG3272N) (accessed 2026-07-22): Broad real-output proxy from the Federal Reserve; the index was 94.2941 in May 2026 with 2017=100.
