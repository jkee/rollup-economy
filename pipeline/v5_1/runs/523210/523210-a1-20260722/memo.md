# 523210 — Securities and Commodity Exchanges

*v5.1 Stage 1 research memo. Run `523210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.35 · L 0.26 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is the persistence of a regulated accountable marketplace combined with fee models that can retain savings from improved support, surveillance, development, and administration.
**Weakness:** The principal weakness is the extremely small, unverified LMM target population in a market dominated by affiliated venue networks and powerful liquidity incumbents.

## Business-model lens
- Included: Lower-middle-market operators of recurring physical or electronic external marketplaces that facilitate buying and selling stocks, stock options, bonds, or commodity contracts, including regulated niche, specialist, and emerging exchanges with repeat transaction, access, listing, connectivity, market-data, and member-service revenue.
- Excluded: Dormant or non-operating registrations, proposed venues that have not launched, captive internal matching systems, alternative trading activities classified elsewhere, standalone clearinghouses classified elsewhere, shells, non-control financing vehicles, and exchange operators outside the lower-middle-market band.
- Customer and revenue model: Customers include broker-dealers, futures commission merchants, market makers, institutional and retail order-flow providers, issuers, data users, and connectivity customers. Revenue commonly combines transaction and clearing-related fees, access and connectivity charges, market data, memberships, and listings, with demand recurring as customers trade and maintain venue access.
- Deviation from default lens: none

## Executive view
Exchange operation is a coherent recurring marketplace service with strong operator necessity and attractive transaction, data, listing, and connectivity economics. AI can improve expensive support and regulatory workflows, but core matching and control systems are already automated, only three firms are estimated in the frozen LMM band, and active independent eligibility is not verified.

## How AI changes the work
AI can accelerate rule and filing analysis, surveillance investigation support, member service, listings review, software documentation and testing, incident knowledge retrieval, market-data operations, and corporate administration. Deterministic matching, production controls, final regulatory decisions, cyber response, and market-integrity accountability should remain tightly governed.

## Value capture
Fee schedules and recurring data, listing, access, and connectivity revenue allow an operator to retain a meaningful share of internal productivity gains. Competition for liquidity, rebates, member bargaining, regulatory fee review, vendor costs, and reinvestment in resilience and compliance reduce long-run retention.

## Firm availability
The frozen dataset estimates only three firms in the LMM band. SEC and CFTC venue lists show active small and emerging operators but also extensive affiliation, acquisitions, name changes, new designations, and non-operating histories, so stand-alone control eligibility must be verified individually.

## Demand durability
Long-run derivatives growth and recent large-exchange results support continued demand for trading, data, access, and risk-management infrastructure. Individual small venues remain exposed to liquidity network effects, product concentration, regulation, and failure to reach critical mass.

## Risks and uncertainty
The largest uncertainties are whether the three margin-bridged firms are active independent venues, how their workflows differ from large public exchanges, and whether their products can sustain liquidity. AI adds model, cyber, confidentiality, manipulation, auditability, and resilience risks; exchange ownership changes also require regulatory accommodation and preservation of self-regulatory responsibilities.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1198 | — | OBSERVED | — |
| n | — | 3 | — | ESTIMATE | — |
| a | 0.28 | 0.43 | 0.58 | PROXY | S2, S4 |
| rho | 0.35 | 0.55 | 0.72 | PROXY | S3, S4, S5, S6 |
| e | 0.3 | 0.65 | 0.9 | ESTIMATE | S5, S6 |
| s5 | 0.03 | 0.09 | 0.18 | PROXY | S6, S10, S11 |
| q | 0.45 | 0.66 | 0.8 | PROXY | S7, S8 |
| d5 | 0.93 | 1.13 | 1.34 | PROXY | S7, S8, S9, S12 |
| o | 0.82 | 0.93 | 0.98 | PROXY | S1, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.47 | 1.13 | 2.00 | PROXY |
| F | 0.04 | 0.26 | 0.64 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | PROXY |
| D | 7.63 | 10.00 | 10.00 | PROXY |

## Caveats
- a: The occupation mix is for all NAICS 523000 activities and does not isolate exchange operators.
- a: Many core exchange functions are already software-delivered, so occupation-based exposure can overstate the remaining automatable share.
- rho: Census adoption is not exchange-specific and its highest finance figures refer to very large firms.
- rho: FINRA observations concern member firms rather than exchange operators, whose market-infrastructure risk tolerance is lower.
- e: The frozen n value is margin-bridged from size classes, not a named list of three verified acquisition candidates.
- e: Regulatory venue lists contain legal entities and affiliates that do not map one-for-one to SUSB employer firms or independent control opportunities.
- s5: Gallup measures broad owner intentions and not completed regulated-exchange transactions.
- s5: Historical large-exchange combinations demonstrate feasibility but may not represent small independent venues or a five-year incidence rate.
- q: CME and ICE are diversified global incumbents far larger and more liquid than the LMM lens.
- q: Operating margin and revenue mix are evidence about economics, not a direct measurement of retained AI-enabled gross benefit.
- d5: The direct metrics come from large diversified exchange groups and may not represent small or emerging venues.
- d5: Trading volume and revenue are volatile and do not map one-for-one to constant-quality service demand after fee and product-mix changes.
- o: Regulatory status establishes operator accountability but does not quantify migration to substitute market structures.
- o: Operator requirement may vary sharply between mature securities and futures markets and newer prediction, digital-asset, or niche contract venues.

## Sources
- **S1** — [2022 NAICS Definition: 523210 Securities and Commodity Exchanges](https://www.census.gov/naics/?details=52&input=52&year=2022) (accessed 2026-07-22): Defines the industry as establishments furnishing physical or electronic marketplaces for buying and selling stocks, stock options, bonds, or commodity contracts.
- **S2** — [May 2023 Occupational Employment and Wage Estimates: NAICS 523000](https://www.bls.gov/oes/2023/may/naics3_523000.htm) (accessed 2026-07-22): Reports 1,064,060 jobs in broader NAICS 523000, including 39.70% business and financial operations, 19.18% office support, 17.33% sales, 15.29% management, and 6.45% computer and mathematical occupations.
- **S3** — [The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html) (accessed 2026-07-22): Reports nationally representative 2026 AI adoption, functional depth, worker-task use, leading text and information tasks, and higher adoption among very large firms in knowledge-intensive sectors including Finance.
- **S4** — [2026 FINRA Annual Regulatory Oversight Report: GenAI Continuing and Emerging Trends](https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai) (accessed 2026-07-22): Reports current GenAI implementation for internal efficiency and information retrieval and describes supervision, accuracy, communications, recordkeeping, fair-dealing, and human-oversight considerations.
- **S5** — [SEC National Securities Exchanges](https://www.sec.gov/about/divisions-offices/division-trading-markets/national-securities-exchanges) (accessed 2026-07-22): Lists exchanges registered under Section 6(a), identifies security-futures exchanges using Section 6(g) notices, and notes former or non-operating limited-volume venues.
- **S6** — [CFTC Designated Contract Markets](https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations?Status=Designated&col=Organization&dir=DESC) (accessed 2026-07-22): Lists active designated contract markets and documents designations, ownership changes, acquisitions, affiliate relationships, name changes, and transfers of exchange designations.
- **S7** — [CME Group Reports Full-Year and Fourth-Quarter 2025 Results](https://investor.cmegroup.com/news-releases/news-release-details/cme-group-inc-reports-fourth-consecutive-year-record-annual) (accessed 2026-07-22): Reports fourth-quarter 2025 average daily volume of 27.4 million contracts, up 7% year over year, $1.3 billion of clearing and transaction fees, and $208 million of market-data revenue.
- **S8** — [Intercontinental Exchange Reports Strong Full-Year 2025 Results](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-Reports-Strong-Full-Year-2025-Results/default.aspx) (accessed 2026-07-22): Reports full-year exchange net revenue of $5.411 billion, up 9%, including $3.885 billion of transaction revenue and $1.526 billion of recurring revenue, with a 74% operating margin.
- **S9** — [Cboe Global Markets Reports December and Full-Year 2025 Trading Volume](https://ir.cboe.com/news/news-details/2026/Cboe-Global-Markets-Reports-Trading-Volume-for-December-and-Full-Year-2025/) (accessed 2026-07-22): Reports mixed 2025 product trends, including multi-listed options average daily volume up 24.2%, index options up 20.9%, futures down 4.8%, and on-exchange U.S. equity matched shares up 26.2%.
- **S10** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of employer-business owners planned to sell or transfer ownership within five years and documents the broad survey population.
- **S11** — [SEC Approval of Rule Changes for the NYSE-Archipelago Business Combination](https://www.sec.gov/news/press/2006-29.htm) (accessed 2026-07-22): Documents SEC approval of SRO rule changes needed for an exchange business combination and preservation of exchange and regulatory responsibilities under the new holding-company structure.
- **S12** — [CFTC Chairman Testimony on the FY 2025 Budget Request](https://www.cftc.gov/PressRoom/SpeechesTestimony/opabehnam47) (accessed 2026-07-22): States that exchange-traded futures and options volumes had more than doubled over roughly the preceding 15 years amid product, participant, and technological expansion.
