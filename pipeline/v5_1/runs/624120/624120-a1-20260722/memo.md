# 624120 — Services for the Elderly and Persons with Disabilities

*v5.1 Stage 1 research memo. Run `624120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.24 · L 3.26 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is recurring, demographically supported demand combined with labor scarcity that makes better scheduling, recruiting, documentation, and claims operations economically valuable.
**Weakness:** The principal weakness is that embodied human care remains nonautomatable while administered payment and direct-care compensation requirements sharply limit retention of productivity gains.

## Business-model lens
- Included: Lower-middle-market providers of recurring or repeat nonresidential social-assistance services for elderly people and people with intellectual, developmental, or physical disabilities, including nonmedical home care, homemaker services, adult day services, companionship, social activities, and group support supplied to external clients or funding agencies.
- Excluded: Residential care facilities, skilled in-home health care, vocational rehabilitation, captive internal care units, non-control financing vehicles, and informal or unpaid family caregiving.
- Customer and revenue model: Services are commonly delivered through recurring caregiver hours, authorized service plans, day-program attendance, or ongoing support engagements. Revenue may come from Medicaid fee schedules or managed-care contracts, other public programs, grants, long-term-care insurance, or private-pay clients and families.
- Deviation from default lens: none

## Executive view
This is a very labor-intensive, recurring human-care industry with strong demographic demand and a large estimated firm population, but direct care dominates the work and payer rules constrain commercial retention. AI is more likely to improve agency coordination and avoid incremental administrative hiring than to replace caregivers. Transferability is plausible for licensed, compliant agencies with diversified payer contracts and management depth, while weak documentation, owner dependence, reimbursement concentration, and workforce instability are major liabilities.

## How AI changes the work
The practical five-year use cases are caregiver recruiting and screening support, schedule and route optimization, multilingual communication, service-plan and visit-note drafting, billing edits, authorization tracking, quality and incident triage, and family updates. Human review remains essential because clients are vulnerable and mistakes can affect safety, eligibility, payment, or abuse reporting.

## Value capture
Administrative and scheduling gains can improve margins, reduce overtime, increase filled hours, and support client retention. Medicaid fee schedules, managed-care contracting, public transparency, competition, and the phased 80% direct-care compensation requirement limit how much of an implemented gross benefit becomes durable operator economics; private-pay and mixed-payer agencies should retain more.

## Firm availability
The frozen dataset estimates 724 LMM-band firms but relies on a placeholder margin for a thin-margin sector, and not all establishments have transferable commercial economics. Broad succession intentions and observed home-care business sales show a functioning transaction market, though license, payer, compliance, and workforce diligence narrow the qualifying pool.

## Demand durability
Real demand should rise with the older population, chronic disability, preference for community living, and policy shifts away from institutions. The limiting factor is often not need but funded authorization, affordability, public budgets, and the supply and retention of caregivers, so delivered services may lag latent demand.

## Risks and uncertainty
The main evidence gaps are six-digit payer mix, normalized margins, firm eligibility, realized transfer incidence, and implemented AI outcomes. The compensation-to-receipts input above one signals meaningful vintage or measurement mismatch. Regulatory change, state-by-state reimbursement, wage inflation, client safety, fraud controls, immigration and labor supply, and Medicaid budget pressure can overwhelm administrative productivity gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 1.0073 | — | OBSERVED | — |
| n | — | 724 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S2, S3 |
| rho | 0.28 | 0.45 | 0.62 | PROXY | S4, S5 |
| e | 0.38 | 0.58 | 0.75 | ESTIMATE | — |
| s5 | 0.08 | 0.15 | 0.23 | PROXY | S7, S8 |
| q | 0.12 | 0.25 | 0.42 | PROXY | S5, S6 |
| d5 | 1.02 | 1.09 | 1.17 | PROXY | S3, S5 |
| o | 0.87 | 0.94 | 0.98 | PROXY | S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.13 | 3.26 | 6.99 | PROXY |
| F | 5.04 | 6.69 | 7.78 | ESTIMATE |
| C | 2.40 | 5.00 | 8.40 | PROXY |
| D | 8.87 | 10.00 | 10.00 | PROXY |

## Caveats
- a: OEWS reports occupations and headcount rather than wage-weighted tasks or current AI exposure.
- a: The supplied compensation-to-receipts input exceeds one after vintage and harmonization adjustments, so translating task exposure into economic opportunity warrants extra caution.
- rho: The adoption source covers all U.S. businesses, not NAICS 624120.
- rho: The five-year value is a projection and depends on state-specific privacy, labor, and Medicaid rules.
- e: No direct denominator of firms satisfying all size, independence, recurrence, and transferability criteria was found.
- e: The frozen firm count is itself margin-bridged with an estimated margin for a thin-margin, publicly funded industry.
- s5: Gallup covers all employer businesses and measures intentions rather than completed transfers.
- s5: BizBuySell's home health category mixes medical providers outside NAICS 624120 with nonmedical home-care agencies and is a voluntary marketplace sample.
- q: The Medicaid payer statistic uses a broader spending category than NAICS 624120.
- q: The federal compensation requirement has exceptions, a future applicability date, and uncertain state implementation.
- d5: BLS projects occupation employment across multiple industries, not constant-price output for NAICS 624120.
- d5: Employment growth may understate unmet demand while overstating output growth if staffing per client rises.
- o: The occupation source combines home health aides with personal care aides and spans multiple industries.
- o: The estimate distinguishes substitution for the agency model from software assistance within an agency-delivered service.

## Sources
- **S1** — [2022 NAICS Definition: 624120 Services for the Elderly and Persons with Disabilities](https://www.census.gov/naics/?details=624120&input=624120&year=2022) (accessed 2026-07-22): Defines the industry as nonresidential social assistance including day care, nonmedical home care or homemaker services, social activities, group support, and companionship, with residential, vocational, and in-home health care classified elsewhere.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 624120](https://www.bls.gov/oes/2023/may/naics5_624120.htm) (accessed 2026-07-22): Reports 2,276,120 jobs and the six-digit occupational mix, including 84.23% healthcare support, 82.28% home health and personal care aides, 3.65% community and social service, 2.75% office support, 1.77% management, and 0.96% business and financial operations.
- **S3** — [Occupational Outlook Handbook: Home Health and Personal Care Aides](https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm) (accessed 2026-07-22): Describes direct personal, household, transportation, social, observational, documentation, and physical duties and projects employment growth of 17% from 2024 to 2034, citing population aging and the shift to home- and community-based care.
- **S4** — [The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html) (accessed 2026-07-22): Reports nationally representative late-2025 firm AI use, employment-weighted use, functional breadth, worker-task adoption, leading generative-AI tasks, augmentation, and rare AI-related employment decreases.
- **S5** — [Ensuring Access to Medicaid Services Final Rule (CMS-2442-F)](https://www.cms.gov/newsroom/fact-sheets/ensuring-access-medicaid-services-final-rule-cms-2442-f) (accessed 2026-07-22): Describes HCBS oversight, reporting and payment transparency, and the phased requirement generally directing at least 80% of specified Medicaid homemaker, home health aide, and personal care payments to direct-care-worker compensation.
- **S6** — [MACPAC: Medicaid Spending](https://www.macpac.gov/medicaid-101/spending/) (accessed 2026-07-22): Reports that Medicaid financed 60.3% of the broad other health, residential, and personal care category in 2023, a category that includes a variety of home- and community-based services.
- **S7** — [Most U.S. Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of employer-business owners planned a sale or transfer within five years and documents the survey population and differences between employer and nonemployer owners.
- **S8** — [Home Health Care Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/home-health-care/) (accessed 2026-07-22): Documents completed home health care business sales and valuation, revenue, earnings, and time-on-market benchmarks from 2021 through 2025, including nonmedical home-service agencies within the adjacent category.
