# 541213 — Tax Preparation Services

*v5 Stage 1 research memo. Run `541213-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.02 · L 0.83 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat filing cycles paired with automatable information-processing and review-support work.
**Weakness:** Uncertain depth and transferability of the lower-middle-market standalone-firm population, alongside software substitution for simple returns.

## Business-model lens
- Included: US lower-middle-market firms whose primary external service is preparing federal or state tax returns for repeat individual or small-business clients, including document intake, return preparation, review, filing, and client communication.
- Excluded: CPA offices, accounting, bookkeeping, billing, payroll, software-only products, captive tax departments, shell entities, non-control financing vehicles, and firms outside the normalized EBITDA band.
- Customer and revenue model: Recurring or repeat annual outsourced tax-return service sold directly to individuals or small businesses, generally for a per-return or complexity-based fee.
- Deviation from default lens: none

## Executive view
Standalone tax preparation offers repeat annual service relationships and a labor-heavy workflow with meaningful AI assistance potential. The central uncertainty is whether the transferable lower-middle-market subset is sufficiently deep after excluding very small practices and non-control units.

## How AI changes the work
The work contains structured intake, document handling, calculations, form completion, verification, scheduling, and client follow-up [S1]. AI can compress those steps and help reviewers surface exceptions, while accountable judgment, changing law, client interviews, and exactness requirements keep humans in the loop.

## Value capture
Firms often charge per return or by complexity, so faster internal processing need not automatically reduce fees. However, software alternatives and local price competition are likely to share part of the benefit with clients, particularly for simple returns.

## Firm availability
The NAICS definition is relatively coherent because it separates standalone tax preparation from CPA offices and combined accounting, bookkeeping, billing, and payroll services [S4]. Public evidence reviewed does not identify how many firms meet the normalized EBITDA and control-transfer conditions, so eligibility and transfer likelihood remain bounded judgments.

## Demand durability
IRS reported a recent increase in e-filed individual returns submitted by tax professionals [S2], consistent with recurring filing activity. That evidence does not settle long-run demand for outsourced preparation because self-preparation, free filing options, and integrated software can displace simpler work.

## Risks and uncertainty
Quality failures during a compressed filing season can damage client trust and create liability. The work is sensitive to tax-law and program changes; GAO describes both expanded Direct File capabilities and changing direction from Congress [S3]. Public data also do not cleanly observe EBITDA, ownership, franchise status, or qualifying control transfers for the target population.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5877 | — | OBSERVED | — |
| n | — | 40 | — | ESTIMATE | — |
| a | 0.38 | 0.53 | 0.68 | ESTIMATE | S1 |
| rho | 0.25 | 0.42 | 0.57 | ESTIMATE | S1 |
| e | 0.07 | 0.14 | 0.25 | ESTIMATE | S4 |
| s5 | 0.07 | 0.12 | 0.18 | ESTIMATE | — |
| q | 0.35 | 0.5 | 0.65 | ESTIMATE | — |
| d5 | 0.96 | 1.03 | 1.1 | PROXY | S2 |
| o | 0.65 | 0.78 | 0.88 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.23 | 5.23 | 9.11 | ESTIMATE |
| F | 0.29 | 0.83 | 1.66 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.24 | 8.03 | 9.68 | ESTIMATE |

## Caveats
- a: O*NET describes the Tax Preparer occupation rather than the full NAICS payroll mix, which also includes management and administrative staff.
- a: The estimate concerns technically exposed current tasks, not realized savings or customer demand.
- rho: This is a five-year operating judgment, not a measured adoption forecast.
- rho: Tax-law changes, vendor integrations, data-access permissions, and state-specific filing requirements could move implementation materially.
- e: No public source reviewed measures the denominator at the specified EBITDA band or identifies franchise and control restrictions consistently.
- e: The supplied firm-count input is not re-estimated here.
- s5: This is not a market-wide business exit rate.
- s5: Seasonality, preparer licensing, customer concentration, and dependence on a selling preparer can make nominally available firms nontransferable.
- q: No public, lens-specific evidence was verified for contractual pass-through or realized post-automation price changes.
- q: This excludes demand changes and implementation difficulty, which belong in other primitives.
- d5: Filing-season e-file counts are not NAICS revenue, constant-quality service quantity, or a five-year forecast.
- d5: The measure is dominated by individual returns and does not distinguish the lower-middle-market lens.
- o: This is a judgment about the present service basket, not a forecast of all tax filing.
- o: Future federal and state policy, software reliability, and tax-law complexity can change the operator-required share in either direction.

## Sources
- **S1** — [O*NET OnLine: Tax Preparers (13-2082.00)](https://www.onetonline.org/link/summary/13-2082.00) (accessed 2026-07-22): Tax-preparer tasks, work activities, work context, software use, accuracy requirement, and occupation scope.
- **S2** — [IRS: Filing season statistics for week ending Dec. 26, 2025](https://www.irs.gov/newsroom/filing-season-statistics-for-week-ending-dec-26-2025) (accessed 2026-07-22): Comparable nationwide individual-return, e-file, tax-professional, and self-prepared filing-season totals.
- **S3** — [GAO: Direct File: IRS Successfully Piloted Online Tax Filing but Opportunities Exist to Expand Access](https://www.gao.gov/products/gao-25-106933) (accessed 2026-07-22): Direct File capability expansion, uptake of prepopulation, limitations, and policy-continuation uncertainty.
- **S4** — [U.S. Census Bureau profile: 541213 Tax Preparation Services](https://data.census.gov/profile/541213_-_Tax_Preparation_Services?codeset=naics~541213) (accessed 2026-07-22): NAICS scope and exclusions for standalone tax preparation services.
