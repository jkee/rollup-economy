# 561491 — Repossession Services

*v5.1 Stage 1 research memo. Run `561491-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.96 · L 1.58 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat lender demand for lawful physical collateral recovery, combined with digitizable case administration around each assignment.
**Weakness:** Most delivery remains physical and locally regulated, while the industry-specific evidence base for workflow shares, transaction frequency, and margin capture is sparse.

## Business-model lens
- Included: US lower-middle-market firms whose principal service is recovering tangible collateral for creditors after delinquency, including assignment intake, skip tracing, field recovery, transport coordination, storage, condition reporting, compliance documentation, invoicing, and lender status communication.
- Excluded: Monetary debt collection without tangible-asset recovery, creditor-owned servicing operations, software-only platforms, auction-only remarketing, ordinary towing without creditor repossession assignments, and businesses outside the $1 million to $10 million normalized EBITDA lens.
- Customer and revenue model: Creditors, auto-finance servicers, equipment lenders, and forwarding companies place repeat assignments; agencies generally earn transaction or recovery fees plus ancillary charges for field attempts, transport, storage, keys, personal-property handling, and related services.
- Deviation from default lens: none

## Executive view
Repossession is a physical, compliance-sensitive outsourced service with a real but bounded AI opportunity. The best fit is to augment skip tracing, assignment administration, exception routing, reporting, and billing around a field operation whose core act cannot be digitized away.

## How AI changes the work
AI can improve search and prioritization, extract and cross-check assignment documents, detect cancellation or lien exceptions, draft status notes and condition summaries, and automate routine communications and invoices. Human authorization and auditable controls remain essential because an incorrect recovery creates acute consumer, legal, and lender risk.

## Value capture
Transaction pricing and ancillary charges permit partial retention of desk-work efficiencies, particularly for operators with dense routes and integrated lender feeds. Sophisticated lenders and forwarders can renegotiate rates, while physical labor, trucks, fuel, storage, insurance, and compliance costs prevent administrative savings from translating fully into margin.

## Firm availability
The frozen dataset indicates a small qualifying population, and public evidence on actual agency transfers is weak. Owner-operated local coverage, client relationships, staff, trucks, lots, and compliance infrastructure are transferable, but concentration and licensing can narrow the practical buyer pool.

## Demand durability
Demand persists because secured consumer and commercial credit produces delinquent collateral across cycles. Auto-finance scale and recently above-average auto delinquency support near-term work, but volumes can reverse with cures, relief programs, underwriting changes, used-vehicle prices, regulation, and creditor recovery strategy.

## Risks and uncertainty
The largest uncertainties are the absence of six-digit labor and output data, limited public rate-card evidence, and no representative AI adoption or realized-savings study. Wrongful repossession, data security, personal-property handling, state rules, insurance, safety, and lender concentration are material operating risks.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3784 | — | OBSERVED | — |
| n | — | 13 | — | ESTIMATE | — |
| a | 0.14 | 0.25 | 0.38 | PROXY | S2, S3, S4, S5 |
| rho | 0.42 | 0.6 | 0.75 | PROXY | S4, S5, S6 |
| e | 0.82 | 0.92 | 0.97 | ESTIMATE | S1, S4, S5 |
| s5 | 0.07 | 0.14 | 0.23 | PROXY | S11 |
| q | 0.35 | 0.52 | 0.68 | PROXY | S5, S8 |
| d5 | 0.92 | 1.06 | 1.17 | PROXY | S7, S9, S10 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.89 | 2.27 | 4.31 | PROXY |
| F | 0.90 | 1.58 | 2.19 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | PROXY |
| D | 8.10 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: There is no public six-digit occupational task matrix for repossession services.
- a: Firm mix varies between desk-intensive forwarding and skip-tracing operations and field-heavy direct recovery agencies.
- a: AI exposure is task-time, not headcount reduction or EBITDA uplift.
- rho: Platform capability is not evidence of industry-wide adoption or realized savings.
- rho: Wrongful-repossession findings increase the need for human controls around cancellation, lien, and payment status.
- rho: Small independent agencies may have less-integrated systems than national forwarders.
- e: No representative public revenue-mix survey was found.
- e: Some agencies combine repossession with towing, storage, transport, or remarketing.
- e: Customer concentration can be high even when revenue is recurring.
- s5: The source measures stated plans, not completed transactions.
- s5: It covers all US employer businesses rather than repossession agencies or the target EBITDA band.
- s5: Transfers to family and external sales have different investability implications.
- q: Consumer fees reported by the CFPB do not identify the recovery agency's net price or margin.
- q: Ancillary and unsuccessful-attempt pricing varies by contract and jurisdiction.
- q: Large lenders and forwarders may capture more savings than local agencies.
- d5: The BLS projection is for broad NAICS 561400, not six-digit repossession services.
- d5: Auto finance is the best-documented collateral class but the industry also serves equipment, boats, aircraft, furniture, and appliances.
- d5: Above-average delinquency does not map one-for-one to completed repossessions.
- o: The estimate concerns required operator mediation, not the fraction of labor that remains manual.
- o: Collateral type and state law materially affect the physical process.
- o: Connected-asset technology could reduce field search without eliminating custody and transport.

## Sources
- **S1** — [North American Industry Classification System: Sector 56](https://www.census.gov/naics/resources/archives/sect56.html) (accessed 2026-07-22): Defines 561491 as repossessing tangible assets for creditors because of delinquent debts and separates it from monetary debt collection.
- **S2** — [O*NET OnLine: Private Detectives and Investigators](https://www.onetonline.org/link/summary/33-9021.00) (accessed 2026-07-22): Documents adjacent investigative tasks including database and public-record search, analysis, reporting, observation, communication, compliance evaluation, and administrative work.
- **S3** — [BLS May 2023 OEWS: NAICS 561400 Business Support Services](https://www.bls.gov/oes/2023/may/naics4_561400.htm) (accessed 2026-07-22): Provides the broad-industry occupational benchmark and demonstrates why it is a weak proxy for repossession: 750,760 total employees but only 410 private detectives and investigators in the four-digit aggregate.
- **S4** — [MBSi RecoveryConnect](https://www.mbsicorp.com/) (accessed 2026-07-22): Shows existing repossession case management, data-driven automation, mobile workflow, compliance tools, and lender-forwarder-agency integration.
- **S5** — [RecoveryIMS](https://www.autoims.com/jsp/repo/repo-home.jsp) (accessed 2026-07-22): Shows electronic assignment, tracking, communications, condition reports, charges, invoices, documentation requirements, performance measurement, and auction handoff.
- **S6** — [CFPB Takes Action Against Wrongful Auto Repossessions and Loan Servicing Breakdowns](https://www.consumerfinance.gov/archive/newsroom/cfpb-takes-action-against-wrongful-auto-repossessions-and-loan-servicing-breakdowns/) (accessed 2026-07-22): Documents wrongful repossessions after payments or loan extensions, supporting the need for reliable cancellation, payment-status, and compliance controls.
- **S7** — [CFPB: Repossession in Auto Finance](https://www.consumerfinance.gov/data-research/research-reports/repossession-in-auto-finance/) (accessed 2026-07-22): Provides public research on auto repossession and notes the limited availability of market data; accompanying CFPB materials describe more than 100 million active auto-finance accounts and over $1.64 trillion in balances through 2024.
- **S8** — [CFPB Uncovers Illegal Junk Fees on Bank Accounts, Mortgages, and Student and Auto Loans](https://www.consumerfinance.gov/archive/newsroom/cfpb-uncovers-illegal-junk-fees-on-bank-accounts-mortgages-and-student-and-auto-loans/) (accessed 2026-07-22): Shows that repossession and personal-property retrieval are separately charged services and that fee practices face contractual and regulatory scrutiny.
- **S9** — [BLS Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects broad NAICS 561400 real output from 87.4 in 2024 to 108.6 in 2034, with 2.2% annual growth, while employment declines 2.8%.
- **S10** — [Federal Reserve: Banking System Conditions](https://www.federalreserve.gov/publications/2025-december-supervision-and-regulation-report-banking-system-conditions.htm) (accessed 2026-07-22): Reports that auto-loan delinquency declined from a year earlier but remained above its ten-year quarterly average in the first half of 2025.
- **S11** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of US employer-business owners planned to sell or transfer ownership within five years, used as a broad intention-based transfer proxy.
