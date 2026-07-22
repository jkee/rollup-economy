# 813211 — Grantmaking Foundations

*v5.1 Stage 1 research memo. Run `813211-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.02 · L 0.42 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can compress proposal review, research, monitoring, reporting, knowledge, and administrative work across recurring grant cycles.
**Weakness:** Foundations are restricted capital allocators without conventional saleable ownership, so eligible firms and qualifying control transfers are nearly absent.

## Business-model lens
- Included: United States lower-middle-market grantmaking foundations and charitable trusts that repeatedly solicit, evaluate, award, administer, and monitor grants for external charitable beneficiaries and have institutional operations separable from a single donor or manager.
- Excluded: Contract fundraising firms, donor-advised-fund sponsors classified elsewhere, operating charities primarily delivering their own programs, family offices and investment vehicles, pass-through shells, captive corporate giving units, and foundations whose restricted assets or donor-dependent governance cannot support a qualifying control transfer.
- Customer and revenue model: Foundations deploy endowed, donated, or trust assets through grants rather than selling services to grantees. Operating resources come from investment income, contributions, and endowment draw, while grants and administration are governed by charitable purpose, payout requirements, boards, donors, and tax rules.
- Deviation from default lens: none

## Executive view
Grantmaking foundations have a research-, document-, finance-, and administration-heavy workflow that is technically suited to AI assistance. The roll-up lens fit is nevertheless exceptionally weak because foundations allocate restricted charitable capital rather than sell outsourced services, and their assets and governance do not provide conventional transferable owner control.

## How AI changes the work
AI can support proposal intake, eligibility checks, summarization, document review, portfolio research, meeting preparation, knowledge management, monitoring, reporting, and communications. Mission strategy, contextual diligence, relationships, conflict resolution, final grant judgment, investment oversight, and board accountability remain human-led.

## Value capture
Administrative savings can remain within the institution because grantees do not reprice the service. They are likely to become lower expense, added operating capacity, or more grantmaking rather than distributable acquisition cash flow, and governance and compliance costs reduce realization.

## Firm availability
The supplied firm count may identify organizations with large receipts, but investment returns, contributions, and grant flows are not conventional sales or EBITDA. Most foundations are donor-, trust-, or board-controlled charitable vehicles and fall outside the default outsourced-service and qualifying-control lens.

## Demand durability
Foundation giving was roughly flat in real terms in 2024 and most surveyed foundations expected stable or higher 2025 giving. Endowment markets, required distributions, policy shifts, community needs, spend-downs, and donor preferences create a wide five-year range.

## Risks and uncertainty
Principal risks are legal and tax restrictions, donor dependence, non-saleable control, misleading receipts-based sizing, sensitive applicant data, bias and explainability, hallucinated diligence, grantee trust, fragmented systems, market-driven payout volatility, and benefits that accrue to mission rather than owners.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0662 | — | OBSERVED | — |
| n | — | 1483 | — | ESTIMATE | — |
| a | 0.31 | 0.47 | 0.62 | PROXY | S2, S4 |
| rho | 0.29 | 0.49 | 0.68 | PROXY | S3, S4 |
| e | 0.005 | 0.02 | 0.06 | ESTIMATE | S1, S5 |
| s5 | 0.002 | 0.01 | 0.04 | ESTIMATE | S5 |
| q | 0.5 | 0.69 | 0.85 | ESTIMATE | S5, S6 |
| d5 | 0.9 | 1.03 | 1.16 | PROXY | S6, S7 |
| o | 0.76 | 0.88 | 0.96 | ESTIMATE | S1, S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.24 | 0.61 | 1.12 | PROXY |
| F | 0.02 | 0.42 | 2.44 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.84 | 9.06 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is for NAICS 813200, not six-digit 813211, and includes fundraising-heavy organizations.
- a: Occupation shares do not reveal task exposure or already automated work.
- a: Application summarization is more automatable than mission judgment, relationship diligence, or fiduciary approval.
- rho: TAG's membership and technology orientation may overrepresent digitally mature foundations.
- rho: Experimentation does not equal scaled workflow implementation or labor savings.
- rho: Candid's application survey primarily measures applicant-use policy, not internal automation.
- e: Grantmaking is capital allocation rather than an outsourced service purchased by grantees.
- e: The margin-bridged n input treats foundation receipts and investment flows as conventional sales and EBITDA.
- e: Donor, trust, tax, and charitable-purpose restrictions sharply limit private acquisition economics.
- s5: Trustee or board turnover is not a qualifying control sale.
- s5: No representative denominator of closed foundation control transactions was found.
- s5: Foundation mergers and asset transfers remain constrained by governing instruments, tax law, and state oversight.
- q: Operational retention inside a foundation is not acquirer cash flow.
- q: Mandatory and policy-driven payouts can redirect savings to charitable distributions.
- q: No direct study measures realized AI benefit retention in grantmaking foundations.
- d5: Grant dollars are not constant-quality grantmaking service quantity.
- d5: Candid's survey had an 8.3 percent response rate and captures expectations rather than a five-year forecast.
- d5: Market performance can move payout dollars without equivalent changes in operating workload.
- o: An accountable legal entity can remain necessary even when most processing is automated.
- o: Application self-service does not remove mission, fiduciary, and award accountability.
- o: No source directly measures the future operator-required share of grantmaking quantity.

## Sources
- **S1** — [2022 NAICS Definition: 813211 Grantmaking Foundations](https://www.census.gov/naics/?details=81321&input=81321&year=2022) (accessed 2026-07-22): Official scope covering grantmaking foundations and charitable trusts that award grants from trust funds or fund selected entities.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 813200 Grantmaking and Giving Services](https://www.bls.gov/oes/2023/may/naics4_813200.htm) (accessed 2026-07-22): Broader-industry employee occupation and wage mix, including management, business, fundraising, administrative, community-service, and media occupations.
- **S3** — [Grantmaking in the Age of AI: A Design Studio Report](https://www.tagtech.org/2025/09/grantmaking-in-the-age-of-ai/) (accessed 2026-07-22): Reported experimentation with AI among staff at grantmaking organizations and the prevalence of missing funder AI policies and governance frameworks.
- **S4** — [Where Do Foundations Stand on AI-Generated Grant Proposals?](https://candid.org/blogs/funders-insights-on-ai-generated-grant-application-proposals/) (accessed 2026-07-22): Foundation survey evidence on AI-generated applications, policy uncertainty, direct-knowledge diligence, and potential use of AI for summarization, categorization, and pre-screening.
- **S5** — [Self-Dealing by Private Foundations: Use of Foundation Income or Assets](https://www.irs.gov/charities-non-profits/private-foundations/self-dealing-by-private-foundations-use-of-foundations-income-or-assets) (accessed 2026-07-22): Prohibition on transferring or using private-foundation income or assets for the benefit of disqualified persons and related governance constraints.
- **S6** — [Taxes on Failure to Distribute Income: Private Foundations](https://www.irs.gov/charities-non-profits/private-foundations/taxes-on-failure-to-distribute-income-private-foundations) (accessed 2026-07-22): Annual charitable distribution requirement, qualifying distributions, carryforward and set-aside rules, and penalties for undistributed income.
- **S7** — [More Than a Third of Foundations Expect to Boost Giving in 2025 but Outlook Remains Unpredictable](https://candid.org/blogs/data-forecasts-more-foundation-giving-in-2025-charitable-giving-trends/) (accessed 2026-07-22): 2025 Foundation Giving Forecast Survey expectations, response rate, drivers of grantmaking, and inflation-adjusted 2024 giving change.
