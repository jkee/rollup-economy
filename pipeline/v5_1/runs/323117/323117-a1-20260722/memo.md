# 323117 — Books Printing

*v5.1 Stage 1 research memo. Run `323117-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.78 · L 0.68 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat physical-book programs create durable workflows in which AI-enabled estimating, prepress, planning, and service can compound across many jobs.
**Weakness:** Most labor is tied to accountable physical production, while powerful publisher buyers can reprice away savings and source globally.

## Business-model lens
- Included: US book printers in the lower-middle-market band producing hardcover, paperback, educational, religious, professional, and other bound books for external publishers and institutional customers, including associated prepress, binding, finishing, and fulfillment performed with the print job.
- Excluded: Publishers, authors, retailers, captive in-plant operations, pure print-on-demand software platforms without accountable production operations, and firms outside the stated EBITDA band.
- Customer and revenue model: Repeat business-to-business job and contract revenue from publishers and institutions, generally quoted per run or per unit with paper, setup, production, binding, and finishing embedded in the price.
- Deviation from default lens: none

## Executive view
Book printing combines resilient physical demand and repeat publisher relationships with a production-heavy labor model. AI is most useful around the pressroom rather than as a substitute for it: quoting, preflight, planning, proof comparison, purchasing, and service administration offer the clearest implementable savings.

## How AI changes the work
AI can turn specifications and prior job histories into draft estimates and schedules, flag file or proof anomalies, summarize job tickets, predict bottlenecks, and automate routine customer updates. Human approval remains important where a false decision can waste paper, miss color, damage a run, or delay a launch.

## Value capture
Job-level pricing and differentiated reliability permit initial retention of savings, but concentrated publishers, bid comparisons, renewal cycles, and competitive capacity should transfer a meaningful share to customers. The best defense is faster turnaround and fewer errors rather than relying solely on lower headcount.

## Firm availability
A meaningful portion of estimated LMM firms should be operationally eligible, though customer concentration, equipment condition, and owner dependence will exclude some. Generic employer-owner succession evidence supports transfer activity, but completed book-printer deal data is the largest diligence gap.

## Demand durability
Recent print unit sales have been approximately stable, supporting a near-flat five-year base. Digital formats, offshore production, and changing educational procurement pose downside; enduring preference for physical books and shorter, more frequent runs support continued operator-required demand.

## Risks and uncertainty
The central risks are that physical production labor limits AI exposure, publisher bargaining passes through gains, and stable retail unit sales mask falling domestic impressions. Firm-level economics also vary sharply with paper purchasing, press utilization, spoilage, format mix, and customer concentration.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1726 | — | OBSERVED | — |
| n | — | 81 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S1, S2, S3 |
| rho | 0.35 | 0.55 | 0.7 | ESTIMATE | S3 |
| e | 0.55 | 0.7 | 0.82 | ESTIMATE | S1 |
| s5 | 0.1 | 0.17 | 0.26 | PROXY | S4 |
| q | 0.35 | 0.52 | 0.68 | ESTIMATE | S3 |
| d5 | 0.85 | 0.96 | 1.05 | PROXY | S5, S6, S7 |
| o | 0.8 | 0.9 | 0.96 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.24 | 0.68 | 1.35 | ESTIMATE |
| F | 2.73 | 3.80 | 4.67 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.80 | 8.64 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupation-by-task dataset was located.
- a: Existing workflow automation may mean part of the apparent opportunity is already captured.
- rho: The industry source reports intended automation activity rather than realized AI labor substitution.
- rho: Small operators may lack clean historical job-cost data needed for reliable deployment.
- e: Eligibility is not directly observed at six digits.
- e: The provided firm count is an ESTIMATE based on margin-bridged size classes and may include firms lacking transferable recurring operations.
- s5: The Gallup population is not printing-specific and includes businesses far smaller and larger than the lens.
- s5: The survey records plans, not completed transfers, and includes transfers that may not convey external control.
- q: No book-printing contract sample or pass-through study was located.
- q: Customer concentration and paper-price clauses can dominate retention firm by firm.
- d5: Consumer sell-through does not translate one-for-one into US printing volume because inventories, returns, imports, and run lengths vary.
- d5: The constant-quality adjustment is judgmental and the 2024-2025 trend is a short window.
- o: The distinction between an automated platform and its underlying accountable plant can be blurred.
- o: Large publishers may internalize or vertically coordinate production without eliminating the physical work.

## Sources
- **S1** — [Printing and Related Support Activities: NAICS 323](https://www.bls.gov/iag/tgs/iag323.htm) (accessed 2026-07-22): Defines the broader subsector as printing products including books and performing data imaging, platemaking, and bookbinding; provides 2025 occupational employment context.
- **S2** — [Occupational projections and worker characteristics](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Reports national printing-worker employment and projections: 212,100 in 2024 to 190,400 in 2034, including press operators at 150,200 to 138,000 and binding/finishing workers at 35,800 to 30,000.
- **S3** — [State of the Industry Report: Executive Summary, April 2024](https://www.printing.org/docs/default-source/research-docs---public/state_of_the_industry_report_april_2024_executive_summary.pdf?sfvrsn=e3e413f8_5%2FState_of_the_Industry_Report_April_2024_EXECUTIVE_SUMMARY) (accessed 2026-07-22): Reports printers focusing on cost control, quality, productivity, automation, business intelligence, e-commerce portals, and automating production; identifies rising labor costs among major concerns.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey found 22% of employer-business owners planned to sell or transfer ownership within five years, 5% planned closure, and 5% had no plan.
- **S5** — [Print Book Sales Rose Slightly in 2025](https://www.publishersweekly.com/pw/by-topic/industry-news/financial-reporting/article/99417-print-book-sales-rose-slightly-in-2025.html) (accessed 2026-07-22): Reports Circana BookScan print unit sales reached 762.4 million in 2025, the second consecutive annual increase.
- **S6** — [Print Book Sales Saw a Small Sales Increase in 2024](https://www.publishersweekly.com/pw/print/20250113/96842-print-book-sales-saw-a-small-sales-increase-in-2024.html) (accessed 2026-07-22): Reports US print book unit sales rose by less than 1% in 2024, the first annual increase in three years at outlets reporting to Circana BookScan.
- **S7** — [AAP StatShot Annual Report: Publishing Revenues Totaled $32.5 Billion for Calendar Year 2024](https://publishers.org/news/aap-statshot-annual-report-publishing-revenues-totaled-32-5-billion-for-calendar-year-2024/) (accessed 2026-07-22): Reports estimated US publishing revenue of $32.5 billion across print and digital formats in 2024, up 4.1% from $31.3 billion in 2023.
