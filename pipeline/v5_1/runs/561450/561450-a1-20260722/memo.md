# 561450 — Credit Bureaus

*v5.1 Stage 1 research memo. Run `561450-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.16 · L 2.59 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring, workflow-embedded data products can retain AI-enabled savings from dispute, data-quality, support, and analytics work without billing by labor hour.
**Weakness:** The industry is already heavily automated, and the small LMM specialist population faces severe data, regulatory, cyber, and incumbent-dependence risks.

## Business-model lens
- Included: US lower-middle-market credit bureaus and specialty consumer or commercial reporting agencies that repeatedly compile credit, employment, payment, identity, or related histories and sell reports, scores, monitoring, batch data, decision support, or credit-investigation services to external customers.
- Excluded: Debt collection, credit repair and counseling, lending, captive bank credit departments, general background investigation without a credit-reporting function, generic data-broker or software products not operated as a bureau, the nationwide bureaus themselves when outside the LMM band, shells, non-control financing vehicles, and one-off investigations without a recurring or repeat reporting service.
- Customer and revenue model: Financial institutions, landlords, employers, insurers, utilities, retailers, governments, and other permissible users purchase bureau data through per-report or other transaction fees, fixed-term data contracts, recurring licenses and subscriptions, batch services, monitoring, implementation, support, and occasional analytics or governance consulting. Bureau products are commonly delivered in real time or embedded in customer decision workflows.
- Deviation from default lens: none

## Executive view
Credit bureaus sell repeat access to regulated data and decision infrastructure, often through recurring or transaction-based contracts that are not tied to labor hours. AI can still compress remaining dispute, data-quality, support, analytics, and engineering work, but the sector is already highly automated and the LMM target population is small. Attractive targets would own differentiated lawful data, recurring embedded customer workflows, strong accuracy and security controls, and limited dependence on any nationwide bureau or single data supplier.

## How AI changes the work
AI can triage disputes and documents, match identities and records, detect anomalies, draft correspondence, assist data-quality investigations, accelerate model and software development, summarize regulatory material, and automate routine support. It is less able to replace accountable reinvestigation, model-risk governance, cybersecurity decisions, ambiguous identity resolution, data-rights management, complex client implementation, and final responsibility for accurate consumer files.

## Value capture
Per-report, volume, fixed-term, subscription, and recurring-license pricing allows productivity to remain as margin or added capacity because customers buy information and reliable decisions rather than hours. Multi-year workflow embedding supports near-term retention, while renewal negotiation, concentrated buyers, volume tiers, regulatory service obligations, direct licensing, and alternative data should pass through or absorb part of the benefit over five years.

## Firm availability
Most firms in the LMM band should be eligible external repeat-service providers, but the dataset's margin bridge is unusually consequential for data-rich businesses and the nationwide bureaus themselves sit outside the target band. Strategic acquisitions show that data and decisioning assets transfer, yet no source supplies a US LMM deal denominator; regulatory liabilities, cyber history, data-license consent, and incumbent dependence can make a nominal bureau difficult to buy.

## Demand durability
Credit, rental, employment, insurance, utility, fraud, identity, and verification decisions sustain repeat demand, and digital channels create more real-time checks and monitoring. Lending and hiring cycles, regulation, customer consolidation, free or inexpensive information, open banking, direct score licensing, and first-party data constrain growth and can shift value away from report resellers.

## Risks and uncertainty
The largest gaps are a six-digit occupation mix, current automation by workflow, LMM implementation outcomes, specialty-bureau contract economics, the true EBITDA-band firm count, and completed control deals by denominator. Accuracy failures, biased or opaque models, cyber breaches, improper data use, weak reinvestigations, or dependence on a nationwide-bureau feed can destroy customer trust and create liability. Public-company evidence may materially overstate LMM technology maturity, data defensibility, growth, and buyer access.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2657 | — | OBSERVED | — |
| n | — | 41 | — | ESTIMATE | — |
| a | 0.28 | 0.42 | 0.56 | PROXY | S2, S3, S4, S7, S8 |
| rho | 0.4 | 0.58 | 0.75 | PROXY | S4, S5, S7, S8 |
| e | 0.78 | 0.9 | 0.97 | ESTIMATE | S1, S6 |
| s5 | 0.07 | 0.14 | 0.23 | PROXY | S4, S10 |
| q | 0.42 | 0.62 | 0.79 | PROXY | S9, S12 |
| d5 | 0.98 | 1.1 | 1.2 | PROXY | S5, S11, S12 |
| o | 0.69 | 0.83 | 0.93 | ESTIMATE | S1, S4, S6, S8, S12 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.19 | 2.59 | 4.46 | PROXY |
| F | 1.89 | 2.93 | 3.73 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | PROXY |
| D | 6.76 | 9.13 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation table is for NAICS 561400 and is heavily shaped by call centers and collection agencies rather than credit bureaus.
- a: O*NET credit-authorizer tasks include lending and collection work and do not measure time, wages, feasibility, or current automation inside bureaus.
- a: TransUnion's technology disclosures describe a large incumbent whose automation and technical occupation mix may exceed those of LMM specialists.
- a: The sharp growth in complaints includes automated, duplicate, and abusive submissions and is not a clean measure of legitimate bureau labor demand.
- a: The injected labor ratio uses 2024 wages over 2022 receipts and may understate controllable labor where bureau receipts monetize proprietary data or include large nonlabor technology and data costs.
- rho: Public-company platform migration demonstrates capability, not audited labor avoidance or representative LMM adoption.
- rho: Current high automation means the marginal workflows left to implement may be unusually exception-heavy and difficult.
- rho: Accuracy, privacy, discrimination, cybersecurity, and FCRA reinvestigation requirements can slow deployment or require human review.
- rho: Complaint-volume growth can create an implementation incentive while also overwhelming quality-control systems.
- e: No source measures eligibility under the frozen LMM recurring-or-repeat outsourced-service lens.
- e: NAICS 561450 includes consumer and commercial bureaus, credit rating, and investigation services with different degrees of recurring revenue.
- e: The injected firm count uses a broad 15.65% Business & Consumer Services margin; data-rich bureaus can have materially different margins and therefore different implied EBITDA-band membership.
- e: The three nationwide bureaus dominate general-purpose consumer credit reporting but are outside the LMM target band; the relevant population is the smaller specialist tail.
- s5: Gallup covers all US employer businesses and includes transfers or gifts rather than only completed control sales.
- s5: TransUnion's disclosed acquisitions are not a representative count of US LMM 561450 deals and include international or adjacent businesses.
- s5: No source supplies an eligible-firm denominator, failed-process rate, owner-age distribution, or LMM transaction completion rate.
- s5: Consumer data rights, cybersecurity history, regulatory exposure, and portability of data-supply contracts can impair transferability.
- q: The cited contract disclosures come from global public incumbents, not LMM specialty bureaus.
- q: Neither source measures the share of AI benefit retained after renewal or competition.
- q: High implementation and compliance spending may consume productivity without appearing as customer pass-through.
- q: Retention can differ sharply between proprietary recurring datasets, commodity report resellers, consulting, and one-off investigations.
- d5: The BLS forecast is for NAICS 561400, which includes call centers, collection agencies, document preparation, and other support services.
- d5: Experian's growth is nominal, global-company evidence and includes adjacent fraud, analytics, health, automotive, marketing, and consumer services.
- d5: Demand is cyclical with mortgage, consumer credit, hiring, rental, and insurance activity.
- d5: The estimate holds the current service basket and quality constant; new analytics products are not treated as guaranteed demand.
- o: No source directly measures the future share of credit-reporting quantity requiring a bureau operator.
- o: FCRA obligations support accountable operation but do not guarantee that today's specialist firm, delivery channel, or data product remains necessary.
- o: Direct score licensing, consumer-permissioned data, open banking, lender consortiums, and inexpensive public data can bypass parts of the bureau value chain.
- o: Large incumbents' scale, proprietary files, and workflow embedding may overstate the operator-required share for small report resellers or narrow specialists.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: NAICS 561450 Credit Bureaus](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines the industry as compiling credit and employment histories and providing them to financial institutions, retailers, and others evaluating individual or business creditworthiness; examples include credit rating, investigation, and reporting services.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Business Support Services](https://www.bls.gov/oes/2023/may/naics4_561400.htm) (accessed 2026-07-22): Provides the four-digit NAICS 561400 occupation mix, including a 59.44% office-support share, 35.85% customer-service representatives, and smaller computer, data-entry, compliance, and credit-clerk groups.
- **S3** — [O*NET OnLine: Credit Authorizers, Checkers, and Clerks](https://www.onetonline.org/link/summary/43-4041.00?redir=43-4041.01) (accessed 2026-07-22): Documents compiling and analyzing credit information, computerized-record review, public-record checks, interviewing, subscriber reporting, complaint resolution, transaction verification, and report preparation.
- **S4** — [TransUnion 2025 Annual Report on Form 10-K](https://www.sec.gov/Archives/edgar/data/1552033/000155203326000012/tru-20251231.htm) (accessed 2026-07-22): Describes real-time and batch credit products, SaaS automated decisions, subscription and transaction products, internal and product AI use, the OneTru AI-enabled platform and US credit migration, embedded client workflows, and strategic acquisitions.
- **S5** — [Experian Full-Year Results FY2026](https://www.experianplc.com/newsroom/press-releases/2026/full-year-results-fy26) (accessed 2026-07-22): Reports 10% North American organic growth, 8% B2B organic growth, largely completed North American cloud migration, and $792 million invested in acquisitions during FY2026.
- **S6** — [CFPB 2025 List of Consumer Reporting Companies](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/consumer-reporting-companies/) (accessed 2026-07-22): Documents the three nationwide bureaus plus specialty consumer reporting companies serving credit, employment, rental, insurance, utilities, check screening, and other decisions, along with FCRA access and dispute obligations.
- **S7** — [CFPB: Correcting Flaws in the Consumer Complaint System](https://www.consumerfinance.gov/about-us/newsroom/the-cfpb-is-correcting-flaws-to-restore-integrity-and-utility-to-the-consumer-complaint-system/) (accessed 2026-07-22): Reports credit and consumer reporting complaints rising from more than 150,000 in 2019 to more than five million in 2025, 2.1 million 2025 closures with non-monetary relief, AI-assisted and abusive submissions, manual-review needs, and API and validation automation.
- **S8** — [CFPB Enforcement Action: Experian Information Solutions, Inc.](https://www.consumerfinance.gov/enforcement/actions/experian-information-solutions-inc/) (accessed 2026-07-22): Describes FCRA duties to forward and reinvestigate disputes, correct or remove inaccurate or unverifiable information, provide notices, and maintain reasonable accuracy procedures, along with pending allegations of deficient execution.
- **S9** — [Equifax 2024 Annual Report on Form 10-K](https://investor.equifax.com/sec-filings/annual-reports/content/0000033185-25-000025/0000033185-25-000025.pdf) (accessed 2026-07-22): Describes transactional and tier-priced information services, generally annual subscriptions with preset or unlimited transactions, multi-year subscription contracts, and bundled data, decisioning, training, model, and service obligations.
- **S10** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Finds that 22% of US employer-business owners planned to sell or transfer ownership within five years, providing a broad succession anchor.
- **S11** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects four-digit NAICS 561400 real output from $87.4 billion in 2024 to $108.6 billion in 2034, a 2.2% annual increase, while employment declines 2.8%.
- **S12** — [Experian Business Model](https://www.experianplc.com/what-we-do/our-business-model) (accessed 2026-07-22): Describes credit-bureau data, analytics, models, fraud and identity services delivered through transactional and fixed-term data contracts, batch services, recurring licenses and support, and consultancy for analytics and regulatory governance.
