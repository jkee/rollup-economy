# 561312 — Executive Search Services

*v5.1 Stage 1 research memo. Run `561312-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** HIGHEST_PRIORITY · A 8.23 · L 6.38 · interval PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High-value retained mandates combine information-intensive delivery work with fees that are linked more to role value than to recorded labor hours.
**Weakness:** The most defensible service value and the most transferable enterprise value both depend heavily on individual consultants' relationships and judgment.

## Business-model lens
- Included: U.S. lower-middle-market executive-search firms providing recurring or repeat retained, exclusive, or contingency recruitment and placement services for executive and senior-management roles to external business, nonprofit, and public-sector clients.
- Excluded: Internal corporate recruiting teams, general employment placement, temporary staffing, professional employer organizations, stand-alone human-resources consulting, coaching without a client-sponsored search, shells, and nontransferable solo practices.
- Customer and revenue model: Customers engage firms for senior-leadership searches. Revenue is commonly a fixed retainer linked to estimated first-year candidate compensation, sometimes supplemented by completion-related adjustments, reimbursed expenses, or contingency fees; repeat work depends on client relationships, sector specialization, and successful placements.
- Deviation from default lens: none

## Executive view
Executive search is unusually rich in AI-addressable research, synthesis, outreach, and coordination work, while retained, compensation-linked fees can preserve part of the benefit. The durable core is narrower: confidential judgment, client trust, candidate persuasion, and senior-hire accountability remain human and relationship dependent.

## How AI changes the work
AI can generate position specifications and outreach, map markets, search and rank candidate pools, summarize biographies and interviews, surface comparable experience, schedule interactions, draft client reports, and maintain knowledge bases. Consultants remain responsible for winning mandates, interpreting context, assessing leadership and culture, managing conflicts, persuading passive candidates, checking references, and negotiating sensitive offers.

## Value capture
A retained fee linked to expected candidate compensation rather than hours creates room to retain savings through lower research cost and more concurrent searches. Over time, clients can demand faster delivery, negotiate fees, build internal sourcing capability, or expect technology-enabled service as standard, reducing retained benefit.

## Firm availability
The code is primarily an external-service industry and includes many specialist boutiques, but a searchable firm is not necessarily a transferable firm. Client ownership by individual consultants, team mobility, restrictive covenants, proprietary-data rights, and post-sale retention are central diligence issues.

## Demand durability
Senior leadership succession and specialized hiring support recurring demand, but mandates are discretionary and react quickly to business confidence, transaction activity, and labor-market conditions. Broader employment-services output is projected to expand, while recent public-company search volume was roughly flat even as revenue rose through pricing.

## Risks and uncertainty
The occupation and demand series are broader than executive search, and exact lower-middle-market data on workflow hours, contract mix, transfer outcomes, and AI benefit sharing are unavailable. Candidate-data privacy, algorithmic bias, hallucinated credentials, client insourcing, consultant departures, cyclicality, and weak post-acquisition retention can overwhelm modeled productivity.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4355 | — | OBSERVED | — |
| n | — | 360 | — | ESTIMATE | — |
| a | 0.58 | 0.72 | 0.84 | PROXY | S1, S2, S3, S5 |
| rho | 0.48 | 0.66 | 0.8 | PROXY | S3, S4, S5 |
| e | 0.78 | 0.9 | 0.97 | ESTIMATE | S1, S5 |
| s5 | 0.07 | 0.16 | 0.27 | PROXY | S6, S7 |
| q | 0.46 | 0.64 | 0.8 | PROXY | S5 |
| d5 | 0.88 | 1.06 | 1.2 | PROXY | S5, S8 |
| o | 0.6 | 0.78 | 0.9 | ESTIMATE | S1, S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 4.85 | 8.28 | 10.00 | PROXY |
| F | 4.87 | 6.38 | 7.33 | ESTIMATE |
| C | 9.20 | 10.00 | 10.00 | PROXY |
| D | 5.28 | 8.27 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation data cover broader employment services and are heavily affected by temporary-help workers on agency payrolls.
- a: The public-company workflow may not represent boutique lower-middle-market firms.
- a: Task exposure is not the same as end-to-end job replacement, especially for confidential executive assessment and persuasion.
- rho: SHRM respondents are employer HR professionals, not executive-search firms.
- rho: Reported time savings do not quantify the share of exposed labor actually removed or redeployed.
- rho: Client confidentiality, algorithmic-bias controls, and fragmented legacy databases may slow smaller firms.
- e: No source measures eligibility within the injected lower-middle-market firm count.
- e: A nominally qualifying firm may still be economically nontransferable if client relationships belong personally to one rainmaker.
- e: The injected count is margin-bridged and may misclassify firms with unusually variable consultant compensation or owner distributions.
- s5: The Gallup statistic is an all-industry intention measure, not completed control transfers.
- s5: Heidrick & Struggles is far larger than the screened firms.
- s5: Team lift-outs and earn-in arrangements may not qualify as control transfers of durable operating firms.
- q: The observed billing structure comes from one large global retained-search firm.
- q: No source measures sharing of AI productivity gains or the revenue mix of lower-middle-market firms.
- q: Contingency-heavy firms may experience different retention and volume effects from retained firms.
- d5: BLS publishes output for broader NAICS 561300, not executive search separately.
- d5: The recent public-company revenue increase was primarily price-driven and is not a constant-quality volume measure.
- d5: Executive-search demand is highly cyclical and concentrated in discretionary senior hiring.
- o: No direct source measures year-five operator necessity for executive search.
- o: Internal talent teams may adopt the same sourcing tools as search firms and remove routine mandates.
- o: Legal, privacy, and bias rules could preserve accountable intermediaries but also increase their compliance cost.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: 561312 Executive Search Services](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Exact-industry scope, executive-search workflow, nonemployment of placed candidates, and cross-references excluding general placement, temporary help, PEOs, and HR consulting.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 561300](https://www.bls.gov/oes/2023/may/naics4_561300.htm) (accessed 2026-07-22): Broader employment-services occupation and wage shares, including management, human-resources, computer, sales, and administrative occupations, used with a disclosed contamination bridge.
- **S3** — [2025 Talent Trends: The Role of AI in HR Continues to Expand](https://www.shrm.org/topics-tools/research/2025-talent-trends/ai-in-hr) (accessed 2026-07-22): U.S. employer use of AI in recruiting, recruiting use cases, reported efficiency and cost benefits, and continuing need for human judgment.
- **S4** — [2026 SHRM Government Affairs Policy Talking Points: Artificial Intelligence](https://www.shrm.org/content/dam/en/shrm/advocacy/shrm_policy_talking_points_artificial_intelligence%20%284%29%20%282%29.pdf) (accessed 2026-07-22): Current HR AI adoption and the reported five-year planned expansion of recruiting AI use.
- **S5** — [Heidrick & Struggles International, Inc. 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1066605/000106660525000017/hsii-20241231.htm) (accessed 2026-07-22): Executive-search workflow, retained and compensation-linked billing, repeat engagements, consultant economics, recent search revenue and confirmation trends, and macroeconomic and AI-related risks.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry five-year sale or transfer intentions among U.S. employer-business owners.
- **S7** — [Heidrick & Struggles International, Inc. December 2025 Form 8-K](https://www.sec.gov/Archives/edgar/data/1066605/000119312525313582/d832427d8k.htm) (accessed 2026-07-22): Observed completion of an exact-industry control merger, used only as a directional transferability signal.
- **S8** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Broader NAICS 561300 real-output and employment projections used as a demand proxy.
