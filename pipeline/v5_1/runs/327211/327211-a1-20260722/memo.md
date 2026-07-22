# 327211 — Flat Glass Manufacturing

*v5.1 Stage 1 research memo. Run `327211-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.71 · L 0.66 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat physical demand plus measurable process-control, yield, and planning workflows create a credible but bounded AI opportunity.
**Weakness:** The genuinely independent, transferable LMM universe may be much smaller than the receipts-based estimate, while most labor remains tied to physical production and maintenance.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers that melt silica sand or cullet to make flat glass, including plants that both make flat glass and laminate it, and repeatedly supply external building, transportation, or fabrication customers.
- Excluded: Captive plants, non-control investment vehicles, pure distributors, installers, and processors that buy all flat glass rather than melting it are excluded.
- Customer and revenue model: Repeat business-to-business product orders, commonly quoted or contracted by specification, volume, and delivery schedule; revenue is product sales rather than a separately billed labor service.
- Deviation from default lens: none

## Executive view
Flat-glass manufacturing is a physical, capital- and energy-intensive business with repeat B2B demand. AI has credible uses in process control, quality triage, planning, quoting, and administration, but only a minority of the wage base is plausibly substitutable within five years, and an LMM buyer must distinguish independent plants from captive or integrated assets.

## How AI changes the work
The clearest pathway is decision support around furnace control, predictive maintenance, inspection, scheduling, yield, and documentation. DOE has shown that machine learning can compress furnace diagnostics dramatically, but the continuous process and quality consequences make supervised deployment more plausible than unattended replacement.

## Value capture
Benefits can appear as avoided downtime, scrap, energy, overtime, and administrative hiring. Retention is incomplete because sophisticated industrial customers rebid and renegotiate, while commodity competition transmits cost improvements into price; reliability and differentiated specifications give the operator some defense.

## Firm availability
The injected LMM count is an estimated 28 firms, but actual eligibility is uncertain in this capital-intensive code. Integrated ownership, captive supply, environmental exposure, and EBITDA misclassification can shrink the transferable pool, while observed control-transfer data specific to 327211 are absent.

## Demand durability
Physical flat glass remains necessary for buildings, transport, and downstream fabrication, so software does not eliminate the basket. Broad glass output has been subdued and cyclical, making a roughly flat real-demand base case more defensible than aggressive growth, with efficiency retrofits and advanced glazing providing upside.

## Risks and uncertainty
The largest evidence gaps are current six-digit occupational tasks, realized implementation among LMM plants, actual private-firm ownership and EBITDA, transaction frequency, and contract-level pass-through. Furnace outages, energy exposure, trade, environmental liabilities, concentration, and construction cycles can dominate AI benefits.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1831 | — | OBSERVED | — |
| n | — | 28 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.32 | PROXY | S2, S3 |
| rho | 0.25 | 0.45 | 0.65 | PROXY | S3 |
| e | 0.35 | 0.55 | 0.75 | ESTIMATE | S1 |
| s5 | 0.12 | 0.22 | 0.35 | ESTIMATE | — |
| q | 0.35 | 0.55 | 0.75 | ESTIMATE | — |
| d5 | 0.9 | 1 | 1.12 | PROXY | S4 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.22 | 0.66 | 1.52 | PROXY |
| F | 1.25 | 2.38 | 3.41 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.46 | 9.80 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational mix is 2016 and four-digit 327200 rather than current six-digit 327211.
- a: The DOE example demonstrates technical exposure at one large producer, not a representative labor-saving rate.
- rho: One DOE-supported project may be unusually well resourced and technically mature.
- rho: The estimate covers operational implementation of exposed opportunity, not gross productivity improvement.
- e: The injected n is itself an ESTIMATE derived from receipts and a sector margin rather than observed 327211 EBITDA.
- e: Multi-establishment groups and captive operations are difficult to distinguish from public industry counts.
- s5: There is no observed denominator of eligible 327211 firms or verified control-transfer numerator.
- s5: Asset sales, closures, and intra-group reorganizations must be excluded from a future measurement.
- q: No representative contract sample or causal cost-to-price evidence was available.
- q: The estimate may vary substantially between commodity float glass and differentiated laminated or specialty products.
- d5: The source is four-digit production, not six-digit demand, and production can diverge from demand through trade and inventory.
- d5: A 2017-based index level does not itself identify the forward five-year growth rate.
- o: This is bounded judgment, not a measured operator-required share.
- o: Plant automation could reduce staffing intensity without eliminating the accountable operating firm, which this primitive intentionally distinguishes.

## Sources
- **S1** — [2022 NAICS Definition: 327211 Flat Glass Manufacturing](https://www.census.gov/naics/?details=3272&input=3272&year=2022) (accessed 2026-07-22): Defines 327211 as establishments melting silica sand or cullet to make flat glass, or both flat and laminated glass.
- **S2** — [May 2016 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 327200](https://www.bls.gov/oes/2016/may/naics4_327200.htm) (accessed 2026-07-22): Reports 85,250 total jobs and the occupation mix, including production at 55.08%, management at 3.97%, business and financial operations at 2.22%, and sales at 2.35%.
- **S3** — [High Performance Computing Improves Manufacturing Productivity and Competitiveness in the Glass Industry](https://www.energy.gov/cmei/ammto/articles/high-performance-computing-improves-manufacturing-productivity-and) (accessed 2026-07-22): Documents Vitro and LLNL's machine-learning furnace-control surrogate, reducing analysis from up to two weeks to minutes and estimating 2% productivity improvement.
- **S4** — [Industrial Production: Glass and Glass Product Manufacturing (NAICS 3272)](https://fred.stlouisfed.org/series/IPG3272N) (accessed 2026-07-22): Federal Reserve industrial-production proxy for real output; May 2026 was 94.2941 on a 2017=100 index.
