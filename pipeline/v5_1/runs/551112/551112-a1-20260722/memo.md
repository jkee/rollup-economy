# 551112 — Offices of Other Holding Companies

*v5.1 Stage 1 research memo. Run `551112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Financial, accounting, reporting, and monitoring workflows in staffed holding offices contain meaningful document and analytical task exposure.
**Weakness:** The industry definition supplies no observable recurring external-customer service model, leaving the eligible firm base and all commercial-demand primitives unsupported.

## Business-model lens
- Included: A correctly classified non-bank holding-company office only if it independently supplies a recurring or repeat outsourced service to unaffiliated external customers while remaining primarily a non-managing holding office. The classification evidence suggests this is an exceptional mixed-activity case rather than the ordinary establishment model.
- Excluded: Entities whose primary activity is holding securities or other equity interests to own a controlling interest or influence management; offices that directly manage affiliated establishments; captive shared-service units; operating subsidiaries; shells; passive or non-control investment vehicles; and internal reorganizations.
- Customer and revenue model: The default lens requires repeat service revenue from external customers. No defensible recurring external-customer billing model was identified for correctly classified other holding-company offices; ordinary economics arise from ownership interests and control rather than outsourced-service contracts.
- Deviation from default lens: none

## Executive view
The official classification is structurally at odds with the frozen outsourced-service lens. An other holding-company office principally owns equity interests to control or influence affiliated enterprises; the Census form separately identifies direct management and centralized support. Eligible external-service firms are therefore treated as rare mixed-activity or classification-edge cases, and unsupported commercial quantities remain missing.

## How AI changes the work
Where a staffed office exists, AI can assist accounting review, performance reporting, document preparation, research, monitoring, and portions of planning. Human responsibility remains material for capital allocation, governance, negotiation, exceptions, and consequential approvals, so exposed work does not translate one-for-one into implemented substitution.

## Value capture
No external-customer billing structure was found for correctly classified other holding-company offices. Internal efficiency may benefit owners of a corporate group, but ownership returns and captive allocations do not establish retention from outsourced-service customers under this lens.

## Firm availability
The Census form explicitly distinguishes a holding company not engaged in direct management from an office that manages or provides centralized support to affiliated establishments. Most establishments in this code are therefore ineligible by business model, and the evidence does not reveal a transferable cohort of qualifying external-service firms.

## Demand durability
Ownership administration and governance may persist as corporate functions, but their persistence is not evidence of external-customer demand for a recurring service basket. Current service quantity and the year-five need for an operator remain undefined until qualifying services are observed.

## Risks and uncertainty
The principal risk is category error: treating ownership vehicles, captive functions, or portfolio-company transactions as independent service businesses. The occupation and adoption evidence also comes from broader populations and may substantially misstate the small, varied staff of a pure holding office.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.365 | — | OBSERVED | — |
| n | — | 1639 | — | ESTIMATE | — |
| a | 0.27 | 0.42 | 0.55 | PROXY | S2, S3, S4, S5 |
| rho | 0.25 | 0.45 | 0.63 | PROXY | S6 |
| e | 0.002 | 0.01 | 0.04 | ESTIMATE | S1 |
| s5 | — | — | — | MISSING | — |
| q | — | — | — | MISSING | — |
| d5 | — | — | — | MISSING | — |
| o | — | — | — | MISSING | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.99 | 2.76 | 5.06 | PROXY |
| F | — | — | — | MISSING |
| C | — | — | — | MISSING |
| D | — | — | — | MISSING |

## Caveats
- a: The occupation evidence is for sector 55 rather than this six-digit code.
- a: The broader sector includes managing offices that the Census form places in a different six-digit code.
- a: The range is wage-weighted task exposure in concept, but public data do not provide a six-digit task-by-wage crosswalk.
- rho: BTOS measures any business-function use, not task coverage or substitution.
- rho: No published NAICS 551112 adoption rate was identified.
- rho: The five-year implementation conversion is judgmental and sensitive to holding-company staffing intensity.
- e: No observed count of external-service sellers within this code was found.
- e: Public company descriptions often consolidate holding entities and operating subsidiaries, obscuring establishment-level classification.
- e: The supplied firm-count input may be materially misleading for this lens because it counts holding-company establishments rather than verified outsourced-service firms.
- s5: Holding-company transaction volume is not a proxy for transfers of eligible service firms without deal-level classification.
- s5: Internal reorganizations and subsidiary sales must be excluded.
- q: Dividends, capital gains, and intercompany charges are not evidence of external service billing.
- q: No fixed-fee, hourly, subscription, or cost-plus mix was observable for the frozen lens.
- d5: Growth in portfolio companies, assets, or holding-company establishments does not directly measure demand for an external service basket.
- d5: Broader sector data combine holding and managing offices.
- o: Governance obligations within a corporate group do not themselves establish external customer demand.
- o: Any estimate would depend on first defining and observing a qualifying service.

## Sources
- **S1** — [2022 Economic Census Form MN-55111: Management of Companies and Enterprises](https://bhs.econ.census.gov/ombpdfs2022/export/2022_MN-55111_mu.pdf) (accessed 2026-07-22): The primary-activity choices distinguish non-managing other holding companies from bank and financial holding companies and from offices engaged in direct management or centralized administrative support.
- **S2** — [Management of Companies and Enterprises: NAICS 55](https://www.bls.gov/iag/tgs/iag55.htm) (accessed 2026-07-22): Defines the broader sector, explains its mix of holding and managing establishments, and reports common accounting, financial-management, office-supervision, and general-management occupations.
- **S3** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 551000](https://www.bls.gov/oes/2023/may/naics3_551000.htm) (accessed 2026-07-22): Provides the detailed occupational distribution for the broader Management of Companies and Enterprises sector used as the occupation-mix proxy.
- **S4** — [O*NET OnLine: Accountants and Auditors](https://www.onetonline.org/link/summary/13-2011.00) (accessed 2026-07-22): Describes accounting work including examining records, preparing statements and reports, analyzing controls, and advising management, which informs the task-exposure proxy.
- **S5** — [O*NET OnLine: General and Operations Managers](https://www.onetonline.org/link/details/11-1021.00) (accessed 2026-07-22): Describes performance-data review, financial and operational coordination, policy work, planning, and high-frequency consequential decision making, informing the exposure and human-accountability bounds.
- **S6** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports recent U.S. business AI adoption by firm size and sector, used as a broad anchor for the implementation range.
