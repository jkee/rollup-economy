# 488999 — All Other Support Activities for Transportation

*v5.1 Stage 1 research memo. Run `488999-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.32 · L 0.94 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A meaningful administrative and coordination layer sits above transportation work that still needs an accountable physical operator.
**Weakness:** The code is highly heterogeneous and the already-small estimated firm pool shrinks further after excluding asset-dominant and nonrecurring businesses.

## Business-model lens
- Included: US lower-middle-market firms providing recurring outsourced transportation-support operations, including transport coordination and scheduling, terminal or stockyard support, and other repeat services where an accountable operator serves external customers.
- Excluded: Independent pipeline terminal facilities and other businesses whose economics are predominantly ownership of specialized infrastructure rather than outsourced operating services; captive internal support units; one-off project work; shells; and non-control financing vehicles.
- Customer and revenue model: Business and institutional customers buy recurring, usage-based, per-transaction, or contracted support from a third-party operator. Revenue commonly follows service volume, facility use, labor, or a negotiated fixed service fee.
- Deviation from default lens: The code is narrowed to recurring outsourced operator-led services because the official examples span coordination businesses, stockyards, and asset-dominant pipeline terminals, whose operating and acquisition economics are too different for one coherent screen.

## Executive view
The opportunity is a blend of an automatable information layer and a stubbornly physical operating core. Centralizing customer communication, billing, documentation, scheduling support, and exception triage could reduce overhead and avoided hiring, but the residual NAICS code contains business models too different to underwrite as one pool, and the eligible firm universe is likely small.

## How AI changes the work
AI can draft and validate documents, classify requests, answer routine customer questions, reconcile billing inputs, produce operating reports, and recommend schedules or exception responses. Human operators remain necessary for safety, facility access, physical movement, high-consequence exceptions, and accountability to customers and regulators.

## Value capture
Savings should be most defensible inside fixed-fee contract periods and when better responsiveness or fewer errors improve the service. At renewal, sophisticated customers can demand lower prices, and commodity-like providers may compete away part of the gain; transparent labor-based and cost-plus pricing is especially leaky.

## Firm availability
National succession evidence supports meaningful five-year transfer intent among employer firms, but actual closing probability is lower. The frozen firm estimate is only nine before eligibility, and specialized facilities, permits, customer concentration, and owner relationships can make individual assets difficult to transfer.

## Demand durability
Broader-industry employment is projected to grow modestly, consistent with support demand that tracks transportation activity rather than a rapid secular expansion. Most included work remains tied to real-world movements and facilities, so software is more likely to change the labor content than eliminate the operator, although coordination-only services are vulnerable to customer self-service.

## Risks and uncertainty
The largest uncertainty is composition: 488999 mixes coordination, stockyards, pipeline terminals, and other residual activities, while occupational and demand data are available only at 488900 and include packing and crating. Contract economics are not public, and current AI adoption surveys do not show implemented labor savings in small operators. A roll-up could also encounter site-specific regulation, safety liability, union or workforce constraints, and customer concentration.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 1.1429 | — | OBSERVED | — |
| n | — | 9 | — | ESTIMATE | — |
| a | 0.16 | 0.26 | 0.38 | PROXY | S1, S2 |
| rho | 0.25 | 0.45 | 0.65 | PROXY | S3, S6 |
| e | 0.3 | 0.55 | 0.75 | ESTIMATE | S1 |
| s5 | 0.08 | 0.16 | 0.25 | PROXY | S4 |
| q | 0.35 | 0.55 | 0.75 | ESTIMATE | — |
| d5 | 0.94 | 1.02 | 1.1 | PROXY | S5 |
| o | 0.7 | 0.88 | 0.97 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.83 | 5.35 | 10.00 | PROXY |
| F | 0.31 | 0.94 | 1.59 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.58 | 8.98 | 10.00 | ESTIMATE |

## Caveats
- a: BLS publishes the occupation mix at 488900, combining 488999 with packing and crating.
- a: OEWS excludes self-employed workers and is a 2023 snapshot.
- a: The range reflects judgment about task content; the source does not measure AI exposure or whether tasks are already automated.
- rho: Survey adoption is not equivalent to labor substitution or avoided hiring.
- rho: The Deloitte respondent mix is not reported at 488999 or lower-middle-market scale.
- rho: Implementation will vary sharply between information-heavy coordinators and physical terminal or stockyard operations.
- e: No public source reports the share of 488999 firms matching the recurring outsourced operator-led lens.
- e: The provided firm count is already estimated and the code's residual nature makes activity classification unusually noisy.
- s5: Gallup is cross-industry and not limited to the EBITDA band.
- s5: Survey responses are intentions, allow multiple selections, and do not establish completed transactions.
- s5: Industry-specific ownership age and transaction incidence are unavailable.
- q: No public dataset identifies the contract mix or repricing behavior of 488999 firms.
- q: Retention will differ materially across facility-use, per-transaction, fixed-fee, and labor-based arrangements.
- d5: Employment is not constant-quality demand and may embed productivity changes.
- d5: The projection covers 2024-2034 and NAICS 488900, not exactly the 2026-2031 horizon or 488999 lens.
- d5: Different included activities can move in opposite directions.
- o: The operator requirement is inferred from activity definitions and physical occupation mix rather than directly measured.
- o: Coordination-only firms face much greater self-service and software-substitution risk than facility operators.

## Sources
- **S1** — [North American Industry Classification System, United States, 2022](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 488999 and identifies its heterogeneous illustrative activities: vanpool or carpool arrangement, independent pipeline terminal facilities, and stockyards, while distinguishing excluded adjacent transportation services.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 488900](https://www.bls.gov/oes/2023/may/naics4_488900.htm) (accessed 2026-07-22): Reports 37,070 total jobs, including 19.45% office and administrative support, 50.30% transportation and material moving, 6.85% management, 4.74% sales, and 2.95% business and financial operations, with occupation-level wages.
- **S3** — [Gen AI shows early promise in the transportation industry](https://www.deloitte.com/us/en/insights/industry/transportation/ai-in-transportation.html) (accessed 2026-07-22): Reports a July 2024 survey of more than 200 transportation executives: over half of surveyed companies had active but generally limited implementations, 71% expected transformation to take more than three years, and 40% cited data misuse as their top generative-AI risk.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 52.3% of US employer businesses are owned by people age 55 or older and that 22% of employer-business owners planned to sell, transfer, or take public within five years.
- **S5** — [Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects employment in NAICS 488900 from 42,700 in 2024 to 44,400 in 2034, a 3.9% increase.
- **S6** — [Monitoring AI Adoption in the US Economy](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html) (accessed 2026-07-22): Synthesizes US surveys showing about 18% firm-level AI adoption at year-end 2025, 41% work-related generative-AI use among workers, and substantial differences by firm size and measurement method.
