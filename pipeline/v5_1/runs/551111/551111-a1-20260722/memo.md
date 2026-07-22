# 551111 — Offices of Bank Holding Companies

*v5.1 Stage 1 research memo. Run `551111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → CONDITIONAL · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Document-heavy financial oversight and reporting work creates plausible AI task exposure wherever a staffed holding office exists.
**Weakness:** The industry definition supplies no observable recurring external-customer service model, leaving the eligible firm base and all commercial-demand primitives unsupported.

## Business-model lens
- Included: A correctly classified bank holding-company office only if it independently supplies a recurring or repeat outsourced service to unaffiliated external customers while remaining primarily a non-managing holding office. The available classification evidence suggests that this is an exceptional edge case rather than the ordinary establishment model.
- Excluded: Entities whose primary activity is holding bank equity or exercising ownership control; banks and other operating financial institutions; offices that administer or manage affiliated establishments; captive shared-service units; shells; non-control financing vehicles; and internal reorganizations.
- Customer and revenue model: The default lens requires revenue from repeat services sold to external customers. No defensible recurring external-customer billing model was identified for correctly classified bank holding-company offices; ordinary economics arise from ownership and control of affiliates rather than outsourced-service fees.
- Deviation from default lens: none

## Executive view
The official classification is structurally at odds with the frozen outsourced-service lens. A bank holding-company office principally owns or controls financial institutions; the Census form separately identifies direct management and centralized support. The packet therefore treats eligible external-service firms as rare classification-edge cases and does not fabricate commercial quantities for a market that was not observed.

## How AI changes the work
Where staff exist, AI can assist financial-statement review, accounting analysis, report drafting, policy research, monitoring, and document preparation. Human accountability remains central for governance, regulatory interpretation, control decisions, exception handling, and approvals, so task exposure is materially larger than near-term autonomous execution.

## Value capture
No external-customer billing structure was found for correctly classified bank holding-company offices. Savings inside a parent group may accrue to owners, but intercompany cost allocation is outside the external recurring-service lens and cannot establish commercial retention.

## Firm availability
The Census activity choices distinguish bank holding companies from managing offices and operating banks. That makes most establishments counted in this code ineligible by construction; the evidence does not identify a transferable population of qualifying outsourced-service firms.

## Demand durability
Bank ownership, governance, and regulatory reporting can persist, but persistence of those internal functions is not evidence of durable external-customer demand for the frozen service basket. Both the current quantity and the year-five operator-required share remain undefined.

## Risks and uncertainty
The main risk is category error: treating legal ownership vehicles, internal control functions, or bank transactions as independent service businesses. Broader sector occupation and AI-adoption proxies also mix populations and may poorly represent the small staff of a pure holding office.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2624 | — | OBSERVED | — |
| n | — | 113 | — | ESTIMATE | — |
| a | 0.28 | 0.43 | 0.56 | PROXY | S2, S3, S4 |
| rho | 0.22 | 0.42 | 0.6 | PROXY | S5, S6 |
| e | 0.001 | 0.005 | 0.02 | ESTIMATE | S1, S6 |
| s5 | — | — | — | MISSING | — |
| q | — | — | — | MISSING | — |
| d5 | — | — | — | MISSING | — |
| o | — | — | — | MISSING | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.65 | 1.90 | 3.53 | PROXY |
| F | — | — | — | MISSING |
| C | — | — | — | MISSING |
| D | — | — | — | MISSING |

## Caveats
- a: The occupation evidence is for sector 55 rather than this six-digit code.
- a: The sector includes managing offices that the Census classification distinguishes from non-managing holding offices.
- a: The range is task exposure, not job displacement, and excludes work already automated.
- rho: BTOS asks about any AI use and does not measure task coverage or labor substitution.
- rho: The cited sector comparison is Finance and Insurance, not NAICS 551111.
- rho: The five-year conversion from adoption to implemented exposed work is judgmental.
- e: No observed count of external-service sellers within this code was found.
- e: Mixed-activity legal entities may be classified by establishment-level primary activity in ways that public company descriptions do not reveal.
- e: The supplied firm-count input may be materially misleading for this lens because it counts holding-company establishments rather than verified outsourced-service firms.
- s5: Holding-company formations, bank acquisitions, and internal reorganizations are not interchangeable with transfers of eligible service firms.
- s5: A transaction rate for all bank holding companies would answer a different question.
- q: Ownership returns and intercompany allocations are not external service revenue.
- q: No fixed-fee, hourly, or cost-plus mix was observable for the frozen lens.
- d5: Growth in bank assets, subsidiaries, or regulatory filings would not directly measure demand for the lens's external service basket.
- d5: Sector-level employment or establishment growth mixes holding and managing offices.
- o: Regulatory accountability inside a holding company does not by itself establish external customer demand for a holding-company operator.
- o: Any estimate would depend on first defining a qualifying service.

## Sources
- **S1** — [2022 Economic Census Form MN-55111: Management of Companies and Enterprises](https://bhs.econ.census.gov/ombpdfs2022/export/2022_MN-55111_mu.pdf) (accessed 2026-07-22): The primary-activity choices distinguish bank holding companies, non-managing other holding companies, financial holding companies, and offices engaged in direct management or centralized administrative support.
- **S2** — [Management of Companies and Enterprises: NAICS 55](https://www.bls.gov/iag/tgs/iag55.htm) (accessed 2026-07-22): Defines the broader sector, explains its mix of holding and managing establishments, and reports common accounting, financial-management, office-supervision, and general-management occupations.
- **S3** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 551000](https://www.bls.gov/oes/2023/may/naics3_551000.htm) (accessed 2026-07-22): Provides the detailed occupational distribution for the broader Management of Companies and Enterprises sector used as the occupation-mix proxy.
- **S4** — [O*NET OnLine: Accountants and Auditors](https://www.onetonline.org/link/summary/13-2011.00) (accessed 2026-07-22): Describes accounting work including examining records, preparing statements and reports, analyzing controls, and advising management, which informs the task-exposure proxy.
- **S5** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports recent U.S. business AI adoption by firm size and sector, including the broad Finance and Insurance comparison used to anchor implementation bounds.
- **S6** — [Bank Holding Company Act of 1956](https://www.federalreserve.gov/frrs/regulations/bank-holding-company-act-of-1956.htm) (accessed 2026-07-22): Documents the ownership, control, approval, activity, capital, and management constraints surrounding bank and financial holding companies, supporting the governance and population caveats.
