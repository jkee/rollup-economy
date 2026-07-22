# 624110 — Child and Youth Services

*v5.1 Stage 1 research memo. Run `624110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.23 · L 3.74 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is the combination of documentation-heavy case workflows and recurring public demand: assisted drafting, retrieval, reporting, and coordination can release scarce professional time without replacing the accountable service provider.
**Weakness:** The principal weakness is that many apparent providers are nonprofit, publicly controlled, affiliated, grant-dependent, or contract-constrained, sharply reducing both the transferable target pool and the share of productivity gains that an owner can retain.

## Business-model lens
- Included: Government-contracted or managed-care-funded child welfare and youth service providers delivering recurring foster and adoption support, family preservation, child guidance, case management, life-skills training, and structured youth development services.
- Excluded: Donation-only youth centers, recreational-only programs, scouting, child day care, residential group homes, one-time adoption facilitators, and grant projects without recurring service contracts are excluded.
- Customer and revenue model: State and local agencies, public child-welfare systems, and managed-care or prime-contractor partners purchase recurring case-management, placement-support, prevention, counseling, and youth-program services through contracts, grants, or reimbursed service arrangements.
- Deviation from default lens: The NAICS definition spans operating models with materially different payers and delivery economics. The lens is narrowed solely to recurring contracted providers so a common customer, revenue model, and service workflow can be evaluated coherently.

## Executive view
The coherent opportunity is a recurring-contract provider whose staff spend meaningful time on case documentation, service plans, referrals, reporting, and cross-agency coordination. AI can reduce administrative load, but high-stakes human service delivery, public-payer economics, nonprofit governance, and a thin transferable target pool constrain the thesis.

## How AI changes the work
The practical near-term use case is augmentation: draft and summarize case records, retrieve policy, prepare routine reports, check documentation completeness, and support scheduling and referrals. Interviews, counseling, home assessment, child-safety decisions, court-facing work, and final case accountability remain human-led, with privacy controls and review embedded in the workflow.

## Value capture
Fixed-price contracts and grants can preserve part of a productivity gain during an award period, especially when saved caseworker time expands capacity. Capture weakens under cost reimbursement, utilization payment, restricted budgets, staffing commitments, competitive rebids, and funder expectations that savings improve service rather than margin.

## Firm availability
The nominal category overstates the actionable pool because it includes donation-led programs, public bodies, affiliates, one-time facilitators, and nonprofits that cannot transfer like ordinary owner-operated firms. Even within the narrowed lens, board approvals, restricted assets, contract assignment, licensure, and payer consent make succession slower and less certain.

## Demand durability
Child protection, foster and adoption support, family preservation, and youth-risk interventions are recurring public needs. The outlook is resilient rather than unbounded: appropriations, demographics, policy shifts toward prevention, reimbursement rates, and the balance between outsourced and public delivery can move volumes and provider economics.

## Risks and uncertainty
Principal risks are confidentiality breaches, incorrect case summaries, missed safeguarding signals, automation bias, audit or court consequences, weak integration with fragmented case systems, staff resistance, payer concentration, contract loss, labor shortages, restricted nonprofit economics, and reputational harm involving vulnerable children. Evidence is weakest on exact task time, firm transferability, contract-level capture, and the target industry's own long-run demand series.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4846 | — | OBSERVED | — |
| n | — | 238 | — | ESTIMATE | — |
| a | 0.28 | 0.42 | 0.55 | PROXY | S2, S3, S4 |
| rho | 0.3 | 0.46 | 0.62 | PROXY | S3, S4, S5 |
| e | 0.28 | 0.45 | 0.62 | ESTIMATE | S1, S9 |
| s5 | 0.04 | 0.1 | 0.18 | PROXY | S6 |
| q | 0.2 | 0.36 | 0.53 | ESTIMATE | S9 |
| d5 | 0.92 | 1.08 | 1.2 | PROXY | S7, S8, S9 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.63 | 3.74 | 6.61 | PROXY |
| F | 2.09 | 3.96 | 5.33 | ESTIMATE |
| C | 4.00 | 7.20 | 10.00 | ESTIMATE |
| D | 8.10 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational employment table covers the broader Individual and Family Services industry rather than this six-digit industry.
- a: O*NET describes occupations across employers and does not measure time shares inside the target lens.
- a: Adoption, foster-care, prevention, counseling, and youth-program workflows differ materially.
- rho: The Census adoption measure is economy-wide rather than specific to social assistance.
- rho: Reported adoption is not equivalent to realized labor savings.
- rho: Local data-access and contracting rules may dominate technical feasibility.
- e: No observed ownership or size distribution was available for the narrowed provider lens.
- e: Nonprofit control, restricted assets, and public-agency operation can make economically attractive organizations unavailable.
- e: The injected firm-count estimate uses an arbitrary placeholder uncertainty margin because social-assistance economics are thin.
- s5: The benchmark covers employer businesses across industries.
- s5: Sale intentions are not completed transactions.
- s5: Nonprofit succession may occur through affiliation or asset transfer rather than a conventional sale.
- q: Payment rules vary by jurisdiction, program, and prime contractor.
- q: Mission-led providers may redeploy savings into service quality rather than distributable earnings.
- q: Implementation costs and supervisory review may consume early productivity gains.
- d5: The output projection is for the parent industry and is materially influenced by elderly and disability services.
- d5: Recent payroll direction is a short window and not a full-cycle demand measure.
- d5: Public funding can remain durable while individual providers lose contracts or face reimbursement pressure.
- o: Some prevention, life-skills, and referral functions are more digitally substitutable than placement or case-management work.
- o: Payer policy may change faster than provider practice.
- o: Substitution risk differs sharply across the activities grouped in the NAICS code.

## Sources
- **S1** — [2022 NAICS 624110 — Child and Youth Services](https://www.census.gov/naics/?chart=2022&details=624110&input=624110) (accessed 2026-07-22): Defines the industry as nonresidential child and youth social assistance, including adoption, foster-care placement, drug prevention, life-skills training, positive social development, child guidance, and youth self-help; distinguishes excluded recreation, child care, and residential group homes.
- **S2** — [Occupational Employment and Wages, May 2023: NAICS 624100 Individual and Family Services](https://www.bls.gov/oes/2023/may/naics4_624100.htm) (accessed 2026-07-22): Provides the parent-industry occupational employment mix, including management, community and social service, child and family social worker, social and human service assistant, and personal-care occupations.
- **S3** — [O*NET OnLine: Child, Family, and School Social Workers](https://www.onetonline.org/link/details/21-1021.00) (accessed 2026-07-22): Describes roles relevant to foster care, adoption, case management, and youth services and documents tasks spanning case records, interviews, service plans, referrals, home evaluation, counseling, placement, legal issues, and interagency coordination.
- **S4** — [O*NET OnLine: Social and Human Service Assistants](https://www.onetonline.org/link/details/21-1093.00) (accessed 2026-07-22): Shows that core work includes client assessment, care plans, records, reports, interviews, referrals, home visits, public service, interpersonal relationships, computer use, administration, compliance, and judgment.
- **S5** — [Artificial Intelligence Use by Businesses Was Rising, Then Began to Plateau](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports nationally representative Business Trends and Outlook Survey evidence that AI use was near one-fifth of businesses overall and materially higher at larger firms, providing a broad adoption benchmark.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of employer-business owners planned to sell or transfer their business within five years, furnishing a broad succession-intention proxy.
- **S7** — [BLS Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Provides projected employment and output growth for Social Assistance and the broader Individual and Family Services industry, while the component detail shows that elderly and disability services account for much of the parent industry's employment.
- **S8** — [BLS Table B-1a: Employees on Nonfarm Payrolls by Industry Sector and Selected Industry Detail](https://www.bls.gov/ces/data/employment-and-earnings/2026/table1a_202604.htm) (accessed 2026-07-22): Provides recent payroll employment observations for Child and Youth Services, showing a broadly stable to modestly higher level over the latest available year.
- **S9** — [Social Services Block Grant Fact Sheet, Fiscal Year 2023](https://ocsannualreport.acf.hhs.gov/annual-report-fy23/ssbg-fact-sheet) (accessed 2026-07-22): Documents federal block-grant funding to states and territories and substantial service delivery in adoption, foster care, protective services, youth-at-risk programs, case management, and counseling.
