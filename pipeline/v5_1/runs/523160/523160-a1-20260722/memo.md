# 523160 — Commodity Contracts Intermediation

*v5.1 Stage 1 research memo. Run `523160-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** The principal driver is a high-value recurring workflow in which AI can compress research, documentation, compliance, and service effort around transactions that still require accountable market access.
**Weakness:** The principal weakness is that the code mixes outsourced brokerage with proprietary trading and provides no defensible frozen count of eligible LMM firms.

## Business-model lens
- Included: Lower-middle-market commodity futures, options, spot-commodity, foreign-exchange, and virtual-currency intermediaries that repeatedly act as agents for external customers and earn commissions or transaction fees, including transferable introducing-broker and specialist brokerage operations with ongoing customer, execution, compliance, and reporting responsibilities.
- Excluded: Principal trading companies whose economics are proprietary risk-taking rather than outsourced customer service; commodity pools and investment advisers when classified elsewhere; physical commodity wholesalers and retailers; exchange and clearinghouse operators; captive desks; shells; non-control financing vehicles; and firms outside the lower-middle-market band.
- Customer and revenue model: Customers include commercial hedgers, producers, institutions, professional traders, and retail accounts. Eligible intermediaries earn commissions, transaction charges, account and platform fees, or disclosed execution economics, while regulated customer onboarding, order handling, supervision, recordkeeping, and support recur with account activity.
- Deviation from default lens: NAICS 523160 combines agents that broker customer transactions for commissions or fees with principals that trade commodity contracts for their own account on a spread basis. The screen retains recurring external-customer brokerage and intermediation and excludes proprietary principal trading because the latter is a risk-capital strategy rather than an outsourced service and would make labor, retention, and transfer constructs incoherent.

## Executive view
The coherent outsourced-service subset is regulated commodity brokerage rather than proprietary trading. It combines highly paid information, sales, compliance, and operations work with recurring customer activity, creating meaningful workflow opportunity, but the six-digit code does not disclose how many firms belong to that subset and the frozen LMM firm count is missing.

## How AI changes the work
AI can assist market and rule research, KYC and document review, communications, call notes, surveillance triage, reconciliation, compliance drafting, reporting, and customer service. It should not autonomously own client recommendations, supervisory conclusions, exception resolution, trading authority, or other regulated accountable decisions.

## Value capture
Commission and transaction-fee models allow some productivity and capacity gains to remain with the operator. Electronic price transparency, negotiated institutional pricing, platform and FCM revenue shares, vendor costs, and competitive commission compression distribute part of the gain to customers and counterparties.

## Firm availability
NFA data show a substantial population of introducing brokers and a smaller population of FCMs, but registration categories do not reveal NAICS assignment, independence, recurring economics, EBITDA, or transferability. Principal-trading firms inside the code are excluded, leaving eligibility and the effective target count unusually uncertain.

## Demand durability
Hedging, price discovery, new derivatives products, global participation, and volatility sustain commodity-market activity. Demand for human intermediation grows more slowly than contract volume because direct access and automated execution continue to absorb routine orders.

## Risks and uncertainty
The main uncertainties are the agent-versus-principal composition of the code, the missing LMM firm count, the amount of work already automated, and the lack of industry-specific transaction and AI telemetry. Regulatory model risk, market-data confidentiality, cyber risk, hallucinations, recordkeeping, supervision, client concentration, and dependence on FCM or venue relationships can all limit implementation or transferability.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4837 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.37 | 0.53 | 0.68 | PROXY | S2, S3, S5 |
| rho | 0.4 | 0.61 | 0.77 | PROXY | S4, S5 |
| e | 0.18 | 0.42 | 0.65 | ESTIMATE | S1, S6 |
| s5 | 0.05 | 0.12 | 0.2 | PROXY | S6, S7 |
| q | 0.35 | 0.56 | 0.72 | ESTIMATE | S1, S3 |
| d5 | 0.88 | 1.08 | 1.27 | PROXY | S3, S8 |
| o | 0.5 | 0.71 | 0.86 | PROXY | S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.86 | 6.26 | 10.00 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 4.40 | 7.67 | 10.00 | PROXY |

## Caveats
- a: The occupation mix covers all NAICS 523000 activities and is not observed for commodity-contract intermediaries.
- a: Task exposure is a judgmental wage-weighted mapping; existing electronic execution means occupation titles overstate the still-unautomated opportunity.
- rho: The Census figures are cross-industry and the highest finance adoption figures refer to very large firms, not the LMM lens.
- rho: FINRA observations concern securities member firms and do not measure commodity-intermediary implementation depth or realized labor savings.
- e: No denominator separates principal trading companies from recurring customer intermediaries within the six-digit employer-firm population.
- e: The frozen dataset provides no defensible LMM firm count for this industry, and NFA categories overlap and span multiple NAICS codes.
- s5: Gallup measures stated plans across all employer businesses, not completed commodity-brokerage control transfers.
- s5: NFA membership counts establish a regulated population but do not identify ownership changes or the eligible LMM cohort.
- q: No source directly measures retention of AI-enabled gross benefits in commodity intermediation.
- q: Pricing and revenue-sharing terms differ materially among independent IBs, guaranteed IBs, FCMs, retail platforms, and institutional execution specialists.
- d5: The occupational projection includes securities and other financial services and is not a six-digit output forecast.
- d5: Exchange-traded contract volume is not equivalent to outsourced brokerage demand, revenue, or constant-quality service quantity.
- o: The BLS automation discussion is broad and emphasizes securities as well as commodities.
- o: Registration establishes accountable firms but does not measure how much transaction quantity requires human or broker-operated service.

## Sources
- **S1** — [2022 NAICS Definition: 523160 Commodity Contracts Intermediation](https://www.census.gov/naics/?details=523160&input=523160&year=2022) (accessed 2026-07-22): Defines the industry as own-account principals trading on a spread basis or agents brokering spot or futures commodity contracts and options for commissions or transaction fees, and lists relevant cross-references.
- **S2** — [May 2023 Occupational Employment and Wage Estimates: NAICS 523000](https://www.bls.gov/oes/2023/may/naics3_523000.htm) (accessed 2026-07-22): Reports 1,064,060 jobs in broader NAICS 523000, including 39.70% business and financial operations, 19.18% office support, 17.33% sales, 15.29% management, and 6.45% computer and mathematical occupations.
- **S3** — [Occupational Outlook Handbook: Securities, Commodities, and Financial Services Sales Agents](https://www.bls.gov/ooh/sales/securities-commodities-and-financial-services-sales-agents.htm) (accessed 2026-07-22): Describes client, advice, market-monitoring, trading, and agreement-analysis duties; projects 3% employment growth from 2024 to 2034; and states that automated trading has reduced trader demand while specialized expertise remains relevant.
- **S4** — [The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html) (accessed 2026-07-22): Reports nationally representative 2026 AI adoption, functional depth, worker-task use, leading text and information tasks, and higher adoption among very large firms in knowledge-intensive sectors including Finance.
- **S5** — [2026 FINRA Annual Regulatory Oversight Report: GenAI Continuing and Emerging Trends](https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai) (accessed 2026-07-22): Reports that member firms have started implementing GenAI for internal-process and information-retrieval efficiency, identifies summarization and extraction as the leading use case, and describes supervision, accuracy, communications, recordkeeping, and fair-dealing constraints.
- **S6** — [NFA Membership and Directories](https://www.nfa.futures.org/registration-membership/membership-and-directories.html) (accessed 2026-07-22): Reports 2,742 total NFA members as of June 30, 2026, including 890 introducing brokers, 72 futures commission merchants, 108 swap dealers, 4 retail foreign-exchange dealers, and 6 exchanges, with overlapping categories disclosed.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of employer-business owners planned to sell or transfer ownership within five years and documents the broad survey population.
- **S8** — [CFTC Chairman Testimony on the FY 2025 Budget Request](https://www.cftc.gov/PressRoom/SpeechesTestimony/opabehnam47) (accessed 2026-07-22): States that exchange-traded futures and options volumes had more than doubled over roughly the preceding 15 years amid product, participant, and technological expansion.
