# 522110 — Commercial Banking

*v5.1 Stage 1 research memo. Run `522110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.84 · L 3.32 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Information-heavy recurring banking workflows and spread- or fee-based revenue create multiple avenues for AI-assisted efficiency and service capacity.
**Weakness:** The frozen LMM firm count rests on non-bank EBITDA economics, while regulation, legacy technology, and competition can prevent technical productivity from becoming transferable cash flow.

## Business-model lens
- Included: US lower-middle-market commercial banks providing recurring deposit, transaction-account, payment, cash-management, commercial and consumer lending, and related relationship-banking services to external households and businesses under a bank charter.
- Excluded: Central banks, credit unions, savings institutions, nondepository lenders, securities firms, trust-only institutions, captive finance units, shells, non-control financing vehicles, money-center institutions outside the approximate $1-10M normalized EBITDA band, and operations without a transferable chartered customer franchise.
- Customer and revenue model: Banks earn net interest income from the spread between loans and other earning assets and deposits or other funding, plus account, payment, card, treasury-management, origination, servicing, and other fees; customer relationships are recurring and control transfers require regulatory approval.
- Deviation from default lens: none

## Executive view
Commercial banking combines a large administrative and analytical workforce with recurring spread- and fee-based customer relationships. AI can improve service, document, risk, fraud, compliance, and credit-support workflows, but legacy cores, regulation, model risk, and intense pricing competition constrain implementation and capture.

## How AI changes the work
AI can triage service requests, summarize policies and files, extract documents, monitor transactions, flag fraud and anomalies, support underwriting and portfolio review, draft reports, test compliance, retrieve knowledge, and assist staff. Accountable credit, fair-lending, risk, cyber, governance, and complex relationship decisions remain with the bank.

## Value capture
Efficiency is not contractually passed through in most banking products and can support lower noninterest expense, loss avoidance, or additional capacity. Loan-spread and deposit-rate competition, vendor costs, control requirements, and service reinvestment erode durable retention.

## Firm availability
Thousands of commercial and community banks remain, and regulated M&A is persistent. The decisive uncertainty is that the injected LMM count uses a non-bank EBITDA margin even though bank earnings are not well represented by EBITDA, so target-band membership needs bank-level reconstruction.

## Demand durability
Deposits, payments, credit, and cash-management services remain durable, with recent loan growth and near-term demand expectations supportive. Cycles, nonbank competition, embedded finance, and digital self-service can shift volume and economics without eliminating chartered-bank accountability.

## Risks and uncertainty
A weak outcome would combine a misleading target count, expensive core integration, vendor dependence, regulatory or model failures, limited removable headcount, aggressive deposit and loan repricing, credit losses, and customer migration to larger banks or nonbanks. Exact task exposure, implementation depth, retention, and target eligibility remain unobserved.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3071 | — | OBSERVED | — |
| n | — | 2033 | — | ESTIMATE | — |
| a | 0.3 | 0.45 | 0.6 | PROXY | S1, S2 |
| rho | 0.4 | 0.6 | 0.78 | PROXY | S2, S3 |
| e | 0.62 | 0.8 | 0.92 | ESTIMATE | S4 |
| s5 | 0.1 | 0.19 | 0.3 | PROXY | S5, S6 |
| q | 0.32 | 0.56 | 0.76 | ESTIMATE | S2, S7 |
| d5 | 0.97 | 1.1 | 1.23 | PROXY | S4, S7, S8 |
| o | 0.62 | 0.8 | 0.92 | ESTIMATE | S2, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.47 | 3.32 | 5.75 | PROXY |
| F | 7.79 | 9.23 | 10.00 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 6.01 | 8.80 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS covers all credit intermediation and related activities, all employer sizes, and jobs rather than task hours or exact commercial banks.
- a: Many teller and service transactions are already digitized, so current occupation shares can overstate not-yet-automated opportunity.
- a: Credit, compliance, fraud, cybersecurity, and customer communications require controls and human accountability even when AI assists.
- rho: The ABA findings are qualitative and do not provide a representative implementation-depth statistic by bank size.
- rho: GAO covers financial services broadly, including securities and credit unions, rather than exact NAICS 522110.
- rho: Vendor deployment does not guarantee workflow adoption, reliable output, or removable labor.
- e: The frozen n estimate applies a non-bank EBITDA margin to banks even though bank economics are balance-sheet and spread driven; the inferred $1-10M band may be materially misleading.
- e: FDIC institution counts do not identify which banks fall within the screen's normalized economic band.
- e: A chartered bank may serve external customers yet still be captive, special purpose, mutually owned, or impractical to acquire.
- s5: Federal Reserve M&A applications cover multiple regulated entity types and are not a one-for-one count of completed commercial-bank control transfers.
- s5: The FDIC structural study ends in 2019 and reports institution decline, not a current five-year hazard for the injected LMM population.
- s5: The eligible denominator is uncertain because the frozen bank n estimate uses non-bank EBITDA economics.
- q: No source directly measures the retained share of implemented AI benefit in commercial banks.
- q: Benefits may appear as faster decisions, loss avoidance, control improvement, or capacity rather than removable expense.
- q: Loan and deposit competition can pass efficiency to customers even without contractual pass-through.
- d5: The BLS output series combines monetary authorities and credit intermediation rather than isolating commercial banks.
- d5: FDIC balance-sheet growth is nominal and does not directly measure constant-price, constant-quality service demand.
- d5: SLOOS is a short-horizon survey of 60 domestic banks and cannot anchor a five-year quantity ratio by itself.
- o: The operator-required share is not the human-labor share; highly automated banks can still be accountable operators.
- o: Fintechs may own the interface while a chartered bank remains the regulated balance-sheet or deposit operator.
- o: Service mix varies materially across community, regional, retail, and commercial-focused banks.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Credit Intermediation and Related Activities](https://www.bls.gov/oes/2023/may/naics3_522000.htm) (accessed 2026-07-22): Broad credit-intermediation employment, occupational shares, and wages used to structure the task-exposure proxy.
- **S2** — [Artificial Intelligence: Use and Oversight in Financial Services](https://files.gao.gov/reports/GAO-25-107197/index.html) (accessed 2026-07-22): Financial-institution AI applications, efficiency and service benefits, and bias, privacy, cyber, data-quality, model, third-party, and accountability constraints.
- **S3** — [ABA survey: Banks view doing nothing with AI as greatest risk](https://bankingjournal.aba.com/2026/03/aba-survey-banks-view-doing-nothing-with-ai-as-greatest-risk/) (accessed 2026-07-22): Bank AI adoption posture, priority low-risk use cases, productivity observations, and governance, data, regulatory, and information-security constraints.
- **S4** — [FDIC Quarterly Banking Profile, Fourth Quarter 2025](https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-fourth-quarter-2025.pdf) (accessed 2026-07-22): Commercial-bank and community-bank institution counts, employment, assets, deposits, loans, and recent balance-sheet activity.
- **S5** — [Federal Reserve Supervision and Regulation Report: Bank Applications and M&A](https://www.federalreserve.gov/publications/2026-june-supervision-and-regulation-report-bank-applications-and-MA.htm) (accessed 2026-07-22): 2023-2025 regulated application activity and approved merger-and-acquisition applications.
- **S6** — [FDIC Releases New 2020 Community Banking Study](https://www.fdic.gov/news/press-releases/2020/pr20139.html) (accessed 2026-07-22): Community-bank consolidation, voluntary unaffiliated mergers, regulatory scale pressure, technology adoption context, and relationship-lending importance.
- **S7** — [January 2026 Senior Loan Officer Opinion Survey on Bank Lending Practices](https://www.federalreserve.gov/data/sloos/sloos-202601.htm) (accessed 2026-07-22): Recent and expected loan demand, competitive pricing pressure, and survey population used as demand and retention context.
- **S8** — [Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Broad monetary-authority and credit-intermediation chained-2017-dollar output projection used for the five-year demand proxy.
