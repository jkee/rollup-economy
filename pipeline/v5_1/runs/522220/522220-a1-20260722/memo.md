# 522220 — Sales Financing

*v5.1 Stage 1 research memo. Run `522220-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.39 · L 0.88 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring origination and servicing around durable demand for financed goods creates a large base of document-, data-, decision-, and communication-intensive work.
**Weakness:** Funding costs, credit cycles, dealer economics, and captive ownership sharply limit both clean target availability and the share of technology benefits retained by operators.

## Business-model lens
- Included: U.S. lower-middle-market firms primarily originating and servicing collateralized credit for purchases of vehicles, equipment, inventory, and other goods, either directly to purchasers or through dealers and sellers, including separable externally facing captive-finance platforms.
- Excluded: Credit-card issuers, lease-only businesses, depository institutions classified by banking activity, passive loan portfolios and securitization vehicles without operations, and captive finance departments that are neither separable nor externally facing.
- Customer and revenue model: Sales-finance firms acquire borrowers through direct, dealer, merchant, manufacturer, or vendor channels and earn recurring interest, finance charges, fees, servicing income, and sometimes residual or ancillary economics while bearing funding, credit, fraud, collateral, and compliance costs.
- Deviation from default lens: none

## Executive view
Sales financing is a capital-, channel-, and compliance-intensive business spanning auto, equipment, inventory, and other collateral. AI can materially improve origination, documents, underwriting support, service, collections, and controls, but funding economics, credit risk, dealer relationships, and collateral operations constrain both implementation and benefit capture.

## How AI changes the work
AI can extract and verify documents, summarize applications, assist underwriting and fraud review, prioritize collections, draft compliant borrower and dealer communications, monitor service quality, and support reporting. Humans remain central to credit policy, exceptions, relationship management, model governance, fair lending, complex workouts, repossession, and collateral disposition.

## Value capture
Faster decisions, lower servicing cost, and improved fraud or loss control can remain with the lender because pricing is not mechanically cost-plus. Dealer incentives, competitive rates, funding cost, credit losses, customer acquisition, regulation, and technology vendors capture or consume a meaningful portion.

## Firm availability
Independent specialty lenders and separable captives can be transferable operating businesses, but many apparent firms are captive departments, depository affiliates, brokers, portfolio vehicles, or lease-dominant companies. Funding continuity, licenses, dealer contracts, servicing systems, and credit quality determine whether a platform is genuinely purchasable.

## Demand durability
Financing remains embedded in vehicle, equipment, and inventory purchases, and recent credit and equipment evidence supports modest growth. Demand is nonetheless cyclical and sensitive to interest rates, business investment, asset values, delinquencies, and substitution by banks, leasing, or alternative payment products.

## Risks and uncertainty
The principal uncertainties are the absence of exact-industry task and firm data, heterogeneity across collateral and channels, captive separability, funding and securitization access, credit losses, used-asset values, regulation, dealer power, existing automation, and whether published AI adoption produces verified labor or loss improvements.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0821 | — | OBSERVED | — |
| n | — | 372 | — | ESTIMATE | — |
| a | 0.28 | 0.43 | 0.59 | PROXY | S2, S3, S4 |
| rho | 0.42 | 0.62 | 0.78 | PROXY | S3, S4, S5 |
| e | 0.2 | 0.42 | 0.62 | ESTIMATE | S1, S3 |
| s5 | 0.08 | 0.15 | 0.25 | PROXY | S9 |
| q | 0.36 | 0.52 | 0.68 | PROXY | S3, S6 |
| d5 | 0.88 | 1.06 | 1.22 | PROXY | S3, S6, S7, S8 |
| o | 0.8 | 0.9 | 0.96 | ESTIMATE | S1, S4, S5, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.39 | 0.88 | 1.51 | PROXY |
| F | 3.12 | 5.14 | 6.55 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | PROXY |
| D | 7.04 | 9.54 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS covers broader NAICS 522200 rather than exact NAICS 522220.
- a: Occupation shares do not directly measure task hours or achievable labor removal.
- a: Automation potential varies substantially by collateral, ticket size, channel, and existing system maturity.
- rho: Published adoption evidence records use or exploration rather than realized labor substitution.
- rho: Equipment-finance evidence may not represent auto and other consumer sales-finance firms.
- rho: Regulatory and model-risk requirements can delay implementation despite technical capability.
- e: No public source measures eligibility within the supplied firm count and EBITDA band.
- e: Captive and independent firms have different separability and valuation economics.
- e: Industry classification can blur sales finance with leasing, banking, retail, brokering, and portfolio ownership.
- s5: Gallup measures cross-industry intentions rather than completed sales-finance transactions.
- s5: A portfolio sale or servicing transfer may not be a qualifying control transaction.
- s5: Captive divestitures and institutionally owned platforms are not well represented by an owner survey.
- q: No source directly measures retention of AI-enabled gross benefits.
- q: Benefit capture differs sharply by direct versus dealer channel and by funding model.
- q: Credit and interest-rate cycles can swamp operating savings.
- d5: Credit balances and originations are nominal financial measures, not constant-quality service quantities.
- d5: Auto and equipment evidence covers major but not all sales-finance segments.
- d5: The five-year outcome is highly exposed to macroeconomic and credit cycles.
- o: No source directly measures the year-five demand share requiring an in-lens operator.
- o: Partner-bank and embedded-finance structures blur where the economically relevant operator sits.
- o: Operational labor can fall substantially even when the legal and capital-bearing firm remains necessary.

## Sources
- **S1** — [NAICS Sector 52 Archive: 522220 Sales Financing](https://www.census.gov/naics/resources/archives/sect52.html) (accessed 2026-07-22): Industry scope: collateralized lending for purchases through direct or dealer arrangements and the distinction from lease-only activity.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 522200](https://www.bls.gov/oes/2023/may/naics4_522200.htm) (accessed 2026-07-22): Broader nondepository-credit occupational mix, including loan, customer-service, collections, business-financial, office-administrative, and technology work.
- **S3** — [Equipment Finance Industry Sees 3.1% Growth in New Business Volume Amid Economic Headwinds](https://www.elfaonline.org/newsroom/equipment-finance-industry-sees-3-1-c56f895d) (accessed 2026-07-22): Equipment-finance growth by lender type, profitability pressure, headcount, and AI implementation or exploration in sales, underwriting, and document processes.
- **S4** — [Artificial Intelligence and Banking](https://www.federalreserve.gov/newsevents/speech/barr20250404a.htm) (accessed 2026-07-22): Financial-sector AI use in fraud and potential in documents, underwriting, and customer service, together with accuracy, explainability, and governance constraints.
- **S5** — [CFPB Issues Guidance on Credit Denials by Lenders Using Artificial Intelligence](https://www.consumerfinance.gov/archive/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/) (accessed 2026-07-22): Use of complex underwriting algorithms and lenders' continuing duty to provide accurate, specific adverse-action reasons.
- **S6** — [Federal Reserve G.19 Consumer Credit, January 2026](https://www.federalreserve.gov/Releases/g19/current/g19.pdf) (accessed 2026-07-22): Consumer-credit balances and growth, finance-company holdings, and auto-finance rates and amounts.
- **S7** — [Repossession in Auto Finance](https://www.consumerfinance.gov/data-research/research-reports/repossession-in-auto-finance/) (accessed 2026-07-22): Scale of auto credit, active accounts and monthly originations, and participation by banks, finance companies, and captive lenders.
- **S8** — [2026 Economic Outlook: Economic Expansion Expected to Continue, but Balance of Risk Tilts Modestly Downward](https://www.leasefoundation.org/news_item/2026-economic-outlook-economic-expansion-expected-to-continue-but-balance-of-risk-tilts-modestly-downward/) (accessed 2026-07-22): Forward equipment and software investment outlook and evidence of resilient but uneven equipment demand.
- **S9** — [Most U.S. Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry five-year sale or transfer intentions among U.S. employer-business owners, used solely as a succession proxy.
