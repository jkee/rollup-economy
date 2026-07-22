# 624190 — Other Individual and Family Services

*v5.1 Stage 1 research memo. Run `624190-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 6.04 · L 4.20 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is a text-heavy, repeat casework and coordination workflow in which AI can expand capacity while an accountable provider preserves trust, compliance, and escalation.
**Weakness:** The principal weakness is the code's mixture of nonprofit, grant-funded, volunteer, crisis, counseling, and government-contracted models, many of which lack transferable control economics or durable benefit retention.

## Business-model lens
- Included: Lower-middle-market organizations that remain accountable for recurring or repeat case management, family or marriage counseling outside mental-health-practitioner offices, crisis and hotline coverage, personal and social-problem referral, offender rehabilitation, parenting support, or multi-program family services supplied under ongoing contracts, service plans, memberships, or repeat engagements.
- Excluded: Programs specifically classified as child and youth services, elderly or disability services, residential care, outpatient mental health practices, emergency food or housing relief, government-operated offices, captive internal programs, non-control financing vehicles, and activities consisting chiefly of one-time charitable aid, volunteer self-help, advocacy, or information publication without an accountable recurring service relationship.
- Customer and revenue model: Revenue can come from cost-reimbursement or fixed-price government contracts, grants with service obligations, institutional or employer agreements, philanthropy, and client fees. Delivery ranges from recurring case-management and counseling caseloads to continuously staffed crisis lines and multi-program service centers.
- Deviation from default lens: The code combines materially different models, including fee-paid counseling, government-contracted case management, crisis contact centers, community-action agencies, self-help organizations, and multi-purpose welfare centers. The screen is narrowed to organizations with an ongoing paid or contract-backed duty to external clients or funders; purely charitable, advocacy, volunteer, or one-time assistance models are excluded because their transferability and value-capture economics are not coherent with accountable recurring service providers.

## Executive view
The coherent recurring subset of Other Individual and Family Services is unusually information- and judgment-intensive, creating meaningful AI opportunity in casework support and administration. However, the NAICS code is structurally heterogeneous and heavily exposed to nonprofit governance, grants, government contracts, professional trust, and public budgets. The opportunity is strongest in contract-backed providers with repeat caseloads, clean data, transferable agreements, and management depth; it is weak in volunteer, advocacy, donation-led, founder-dependent, or one-time assistance programs.

## How AI changes the work
AI can accelerate intake summaries, case notes, resource and eligibility research, referral matching, form completion, translation, contract reports, quality review, scheduling, grants, and supervised digital triage. It should augment rather than autonomously replace counseling, crisis judgment, safeguarding, mandated reporting, complex case planning, and relationship building.

## Value capture
Fixed-price contracts, institutional agreements, and private client fees allow providers to retain some capacity and administrative gains. Cost-reimbursement contracts, grant budgets, funder rebasing, nonprofit mission reinvestment, and buyer price pressure share or redirect benefits, producing lower and more variable commercial retention than in ordinary professional services.

## Firm availability
The frozen dataset estimates 421 firms in the LMM band using a placeholder margin, but many classified organizations are unlikely to have transferable EBITDA economics. Broad succession evidence and service-business sales establish a possible market for the eligible commercial subset, while nonprofit control, restricted assets, founder dependence, contract novation, and professional staffing sharply narrow qualifying transfers.

## Demand durability
Underlying need for crisis support, family services, benefit navigation, substance-use and reentry support, counseling, and case coordination is durable. Realized paid demand depends on appropriations, grants, public contracting, donations, and staffing; fiscal retrenchment can reduce delivered services even when social need rises.

## Risks and uncertainty
The largest uncertainty is industry composition: no direct six-digit occupational mix, payer mix, recurring-revenue rate, eligibility denominator, or transaction incidence was found. Sensitive data, biased recommendations, hallucinated resources, crisis safety, licensure, recordkeeping, cybersecurity, and funder approval constrain AI deployment. Policy or budget changes can dominate productivity, and the frozen margin assumption may materially misclassify firm size.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5205 | — | OBSERVED | — |
| n | — | 421 | — | ESTIMATE | — |
| a | 0.29 | 0.42 | 0.56 | PROXY | S2, S3, S4, S5 |
| rho | 0.31 | 0.48 | 0.65 | PROXY | S6, S10 |
| e | 0.2 | 0.38 | 0.58 | ESTIMATE | — |
| s5 | 0.05 | 0.12 | 0.2 | PROXY | S7, S8 |
| q | 0.18 | 0.34 | 0.52 | PROXY | S9 |
| d5 | 0.94 | 1.03 | 1.13 | PROXY | S4, S5, S10 |
| o | 0.66 | 0.81 | 0.92 | PROXY | S4, S5, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.87 | 4.20 | 7.58 | PROXY |
| F | 2.66 | 4.83 | 6.29 | ESTIMATE |
| C | 3.60 | 6.80 | 10.00 | PROXY |
| D | 6.20 | 8.34 | 10.00 | PROXY |

## Caveats
- a: The occupational mix is an arithmetic residual for NAICS 624110 plus 624190, not a direct six-digit observation.
- a: Occupations and duties are translated into wage-weighted task exposure rather than directly measured as such.
- rho: The Census source covers all industries and firm sizes, not social services.
- rho: Crisis-service technology demonstrates digital workflow adoption but not autonomous AI implementation.
- e: No direct denominator of firms satisfying the narrowed recurrence, control, independence, and size criteria was found.
- e: The frozen LMM firm count is based on an estimated 8% margin in a heterogeneous, often grant-funded social-assistance industry.
- s5: Gallup measures intentions for all employer businesses, not completed transfers in this industry.
- s5: BizBuySell's broad service category is commercial and owner-operated, unlike much of NAICS 624190.
- q: The source covers the entire charitable nonprofit sector, not NAICS 624190 or the eligible subset.
- q: Indirect-cost reimbursement rules describe cost recovery, not direct measurement of AI-benefit retention.
- d5: Occupation projections span multiple industries and are not a measure of NAICS 624190 real output.
- d5: 988 is only one crisis-service segment and its volume is not representative of all included activities.
- o: Occupation duties cover social workers and assistants across industries, not only the narrowed lens.
- o: The industry spans low-risk information referral and high-risk crisis or counseling work, so operator requirement varies substantially.

## Sources
- **S1** — [NAICS Definition: 624190 Other Individual and Family Services](https://www.census.gov/naics/?details=624190&input=624190&year=2017) (accessed 2026-07-22): Defines the residual individual and family social-assistance industry and lists community action, marriage counseling, crisis intervention, multi-purpose social services, family welfare, self-help, hotline, referral, offender rehabilitation, and related activities.
- **S2** — [May 2023 Occupational Employment and Wage Estimates: NAICS 624100 Individual and Family Services](https://www.bls.gov/oes/2023/may/naics4_624100.htm) (accessed 2026-07-22): Reports total and occupation-level employment for broader Individual and Family Services, used with S3 to derive a residual occupational mix for NAICS 624110 plus 624190.
- **S3** — [May 2023 Occupational Employment and Wage Estimates: NAICS 624120 Services for the Elderly and Persons with Disabilities](https://www.bls.gov/oes/2023/may/naics5_624120.htm) (accessed 2026-07-22): Provides the same-vintage six-digit occupational counts subtracted from broader NAICS 624100 to remove the dominant elder and disability services component.
- **S4** — [Occupational Outlook Handbook: Social and Human Service Assistants](https://www.bls.gov/ooh/Community-and-Social-Service/Social-and-human-service-assistants.htm) (accessed 2026-07-22): Describes needs assessment, service research, referrals, coordination, paperwork, follow-up, and work with varied client groups and projects 6% employment growth from 2024 to 2034.
- **S5** — [Occupational Outlook Handbook: Social Workers](https://www.bls.gov/ooh/community-and-social-service/social-workers.htm) (accessed 2026-07-22): Describes assessment, referral, crisis response, monitoring, records, counseling, advocacy, licensing, and complex client work and projects 6% overall employment growth from 2024 to 2034.
- **S6** — [The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html) (accessed 2026-07-22): Reports nationally representative late-2025 firm AI adoption, employment-weighted use, limited functional and task breadth, common generative-AI tasks, augmentation, and rare employment reductions.
- **S7** — [Most U.S. Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of employer-business owners planned a sale or transfer within five years and documents survey population and employer/nonemployer differences.
- **S8** — [Service Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/service-business/) (accessed 2026-07-22): Reports 5,839 analyzed service-business sales over 2021-2025, a 170-day median time on market, and observed transaction and valuation benchmarks for a broad commercial-service proxy.
- **S9** — [Government Grants and Contracts](https://www.councilofnonprofits.org/print/pdf/node/265) (accessed 2026-07-22): Reports that the nonprofit sector earns about one-third of revenue through written government agreements and describes indirect-cost reimbursement for federally funded government service arrangements.
- **S10** — [SAMHSA Announces Funding Opportunity to Administer 988 Lifeline](https://www.samhsa.gov/newsroom/press-announcements/20260113/samhsa-announces-231-m-funding-opportunity-administer-988-lifeline) (accessed 2026-07-22): Reports more than 8 million call, text, chat, and videophone contacts in 2025 and describes a national network of more than 200 local crisis centers connecting users with skilled crisis counselors.
