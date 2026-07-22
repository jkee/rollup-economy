# 523940 — Portfolio Management and Investment Advice

*v5.1 Stage 1 research memo. Run `523940-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Recurring fee relationships and document- and data-intensive workflows create a broad opportunity to augment advisers and scale service capacity.
**Weakness:** No defensible LMM-band firm count exists, while client trust, founder dependence, fiduciary duties, and fee pressure limit both transferable supply and retained labor savings.

## Business-model lens
- Included: Lower-middle-market portfolio managers, registered investment advisers, wealth managers, financial planners, investment counselors, trust portfolio managers, private-fund managers, and subadvisers repeatedly managing assets or providing customized advice to external clients for fees.
- Excluded: Captive internal investment offices, shells, legal funds or trusts without a separate management operation, non-control financing vehicles, publishers of generalized investment information, broker-dealers whose primary activity is transaction intermediation, and practices whose client relationships and revenue cannot transfer independently of one individual.
- Customer and revenue model: Individuals, families, trusts, retirement plans, institutions, and pooled vehicles pay asset-based, fixed, hourly, subscription, and performance fees for discretionary portfolio management, research, reporting, financial planning, and customized investment advice. Revenue commonly recurs with assets and client relationships, while market levels, net flows, mandates, and performance influence fees.
- Deviation from default lens: none

## Executive view
Portfolio management and investment advice directly match a recurring external-service model, with asset-based and other repeat fees, persistent client needs, and active consolidation. AI can compress research, reporting, planning preparation, client service, compliance, and administration, but fiduciary accountability, personalization, trust, and portfolio authority constrain full substitution. The declared absence of a defensible LMM firm count is the central availability gap.

## How AI changes the work
AI can retrieve and summarize research, draft investment commentary and client communications, prepare meeting notes and financial-plan inputs, reconcile data, generate proposals and reports, flag portfolio or compliance exceptions, retrieve policies, and support onboarding and service. It can also assist portfolio construction and trading. Human advisers remain responsible for goals discovery, judgment under uncertainty, recommendations, conflicts, supervision, and client reassurance.

## Value capture
Asset-based and fixed fees can preserve internal efficiency between repricings, especially when advisers use saved time to serve more relationships. Retention leaks through negotiated breakpoints, fee competition, hourly billing, client sharing, performance allocations, vendor and custodian costs, adviser payouts, compliance review, and richer service. Market-driven AUM changes can obscure whether productivity actually improved margins.

## Firm availability
Most legal businesses in the code provide an externally paid service, and SEC-adviser data show a large population of small organizations. Transferability is lower where one founder owns the relationships, clients can terminate or withhold consent, employees sit in affiliates, or the entity is a captive or fund-linked manager. A missing defensible count for the economic band prevents a credible target-pool estimate.

## Demand durability
Retirement, aging, wealth and tax complexity, private-market allocations, and regulatory obligations support demand for advice and portfolio oversight. Broader real output and adviser employment are projected to grow, and the registered-adviser population reports expanding clients and employment. Standardized low-complexity portfolios and planning can migrate to software or self-service, while complex households and institutional mandates retain human accountability.

## Risks and uncertainty
Key uncertainties are the missing LMM firm count, the ancestor-code labor anchor, founder and client concentration, change-of-control consent, market-dependent revenue, fee compression, private-fund cyclicality, inconsistent transaction definitions, and realized AI savings. Model error, biased recommendations, conflicts, hallucinated communications, privacy breaches, cybersecurity, recordkeeping, vendor dependence, and regulatory enforcement can outweigh labor gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3907 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.28 | 0.43 | 0.58 | PROXY | S2, S3, S4 |
| rho | 0.3 | 0.48 | 0.66 | PROXY | S3, S4 |
| e | 0.58 | 0.74 | 0.88 | PROXY | S1, S5, S6 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S7, S8 |
| q | 0.4 | 0.62 | 0.78 | PROXY | S1, S5 |
| d5 | 1.02 | 1.12 | 1.22 | PROXY | S6, S9, S10 |
| o | 0.68 | 0.82 | 0.92 | PROXY | S1, S3, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.31 | 3.23 | 5.98 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 8.00 | 10.00 | 10.00 | PROXY |
| D | 6.94 | 9.18 | 10.00 | PROXY |

## Caveats
- a: The occupation mix is for all NAICS 523000 and excludes self-employed workers.
- a: Occupation employment shares are not payroll-weighted task exposure.
- a: Private-fund portfolio management, retail wealth advice, and one-time financial planning have materially different task mixes.
- rho: FINRA evidence is not a measured adoption rate for investment advisers.
- rho: Vendor purchase and experimentation do not establish production implementation or avoided labor.
- rho: Small practices may face larger integration costs while large firms face more complex governance.
- e: IAA data cover SEC-registered advisers and omit many smaller state-registered firms.
- e: Small employee count does not establish normalized EBITDA or transferability.
- e: The supplied n is a declared dataset gap, so the eligible share cannot produce a defensible firm count without new data.
- s5: Announced wealth-management deals do not equal closed qualifying control transfers.
- s5: Deal definitions and coverage vary, especially for small firms and recruiting transactions.
- s5: The missing frozen n prevents conversion of the probability into an expected count.
- q: No source directly measures retention of AI-derived benefit.
- q: Asset-based, performance, fixed, hourly, and subscription models pass savings through differently.
- q: Market appreciation can raise revenue without reflecting operating retention.
- d5: BLS output covers all NAICS 523000 rather than 523940.
- d5: RIA AUM growth is heavily affected by market prices and cannot be read as service quantity.
- d5: Personal-adviser employment is only one component of portfolio management and investment advice.
- o: The BLS statement concerns employment, not the operator-required share of service quantity.
- o: Retail planning and institutional or private-fund mandates have different substitution paths.
- o: A legal adviser can remain accountable even when software performs most production work.

## Sources
- **S1** — [U.S. Census Bureau: 2022 NAICS 523940 Portfolio Management and Investment Advice](https://www.census.gov/naics/?details=523940&input=523940&year=2022) (accessed 2026-07-22): Defines fee- or commission-based management of others' portfolio assets, including decision authority and size- or performance-based fees, and customized fee-based investment advice without trade authority.
- **S2** — [BLS May 2023 OEWS: Securities, Commodity Contracts, and Other Financial Investments and Related Activities](https://www.bls.gov/oes/2023/may/naics4_523000.htm) (accessed 2026-07-22): Reports the broader NAICS 523000 occupation mix, including 39.70% business and financial operations, 19.18% office and administrative support, 17.33% sales, 15.29% management, and 6.45% computer and mathematical occupations.
- **S3** — [FINRA: AI Applications in the Securities Industry](https://www.finra.org/rules-guidance/key-topics/fintech/report/artificial-intelligence-in-the-securities-industry/ai-apps-in-the-industry) (accessed 2026-07-22): Documents AI use and evaluation in customer communications, brokerage-account and portfolio management, trading, compliance, risk management, and administration, along with privacy, cybersecurity, authentication, and recordkeeping risks.
- **S4** — [FINRA 2025 Annual Regulatory Oversight Report](https://www.finra.org/sites/default/files/2025-01/2025-annual-regulatory-oversight-report.pdf) (accessed 2026-07-22): Reports cautious financial-firm use of vendor-supported generative AI for internal summarization, cross-dataset analysis, and policy retrieval and identifies supervision, accuracy, bias, privacy, cybersecurity, data-provenance, and vendor risks.
- **S5** — [Investment Adviser Association and COMPLY: Investment Adviser Industry Snapshot 2025](https://www.investmentadviser.org/wp-content/uploads/2025/05/Snapshot2025.pdf) (accessed 2026-07-22): Reports 2024 SEC-adviser firm-size and fee data, including median employment of eight, 95.5% offering asset-based fees, 45.2% fixed fees, 28.9% hourly fees, and only 17.4% compensated solely through asset-based fees.
- **S6** — [Investment Adviser Association: 2026 Investment Adviser Industry Snapshot Highlights](https://www.investmentadviser.org/industry-snapshots/) (accessed 2026-07-22): Reports 16,544 advisers in 2025, 73.7 million clients after 7.7% growth, 1.1 million non-clerical employees after 7.5% growth, and that 92.8% of advisers employed no more than 100 people.
- **S7** — [ECHELON Partners: 2025 RIA M&A Deal Report](https://www.echelon-partners.com/wp-content/uploads/2026/03/FY-Annual-2025-ECHELON-2025-RIA-MA-Deal-Report-2026.02.12VF.pdf) (accessed 2026-07-22): Reports 466 announced wealth-management transactions in 2025, 27.3% growth from 2024, exclusions for deals with no more than $100 million in assets, and limitations in tracking smaller, internal, hybrid, and breakaway transactions.
- **S8** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of U.S. employer-business owners planned to sell, transfer, or take public their business within five years, based on a fall 2024 survey.
- **S9** — [BLS Employment and Output by Industry, 2024 to 2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects broader NAICS 523000 real output from $721.7 billion in 2024 to $892.4 billion in 2034, a 2.1% annual increase, and employment growth of 6.0% over the decade.
- **S10** — [BLS Monthly Labor Review: Industry and Occupational Employment Projections, 2024 to 2034](https://www.bls.gov/opub/mlr/2026/article/industry-and-occupational-employment-projections-overview.htm) (accessed 2026-07-22): Projects personal financial-adviser employment growth of 9.6% and states that robo-advisers are expected to have only a mild employment effect because older clients with complex planning needs are unlikely to trust automated recommendations.
