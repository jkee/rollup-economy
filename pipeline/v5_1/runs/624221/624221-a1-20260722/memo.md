# 624221 — Temporary Shelters

*v5.1 Stage 1 research memo. Run `624221-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Emergency lodging remains a physical, safety-critical service with persistent underlying need.
**Weakness:** No defensible population of transferable LMM temporary-shelter firms was established.

## Business-model lens
- Included: U.S. temporary-shelter operators that repeatedly provide short-term emergency or residential shelter to external clients and could plausibly meet the lower-middle-market normalized EBITDA band under the fixed lens.
- Excluded: Government-run captive units, volunteer-only programs, non-transferable entities, one-off disaster shelters, permanent supportive housing, transitional housing classified elsewhere, residential treatment facilities, and non-control financing vehicles.
- Customer and revenue model: Residents generally are not the economic customer. Funding commonly flows through government grants or subrecipient awards, philanthropy, and institutional sponsorship; a potentially investable subset would require recurring outsourced operating contracts or other reliable third-party payment.
- Deviation from default lens: none

## Executive view
Temporary shelters have a real administrative automation surface and strongly operator-dependent physical service, but the fixed acquisition lens lacks an established target population. The dataset estimates zero firms in the target EBITDA band, and public or nonprofit funding structures make transferable equity and distributable savings uncertain. Entity-level proof of an eligible operator must precede an investment thesis.

## How AI changes the work
AI can assist intake summaries, case documentation, referral search, bed and staff scheduling, HMIS data quality, incident-report drafting, grant reporting, and multilingual communications. It should not replace crisis judgment, safeguarding, counseling, supervision, security, or facility operations, and sensitive client information raises unusually important privacy and review requirements.

## Value capture
Gross labor savings may be redirected into capacity, service quality, or compliance, and cost-reimbursed or competitively renewed funding can pass benefits to funders. Retention could be stronger under fixed-price outsourced management, but the research did not establish how common such contracts are among transferable LMM firms.

## Firm availability
The frozen count identifies no LMM-band firms, while HUD programs include government and private nonprofit delivery and section 501(c)(3) rules bar private inurement. These facts do not prove the absence of commercial contractors, but they make ownership, normalized earnings, and control-transferability the decisive unresolved diligence items.

## Demand durability
The latest HUD count shows homelessness remains high despite a modest year-over-year decline, and emergency lodging cannot be delivered by software alone. Demand for the current service basket is nevertheless policy-sensitive: prevention, rental aid, hotels, permanent housing, grant levels, and local operating restrictions can all change shelter nights and the identity of the accountable provider.

## Risks and uncertainty
Core risks are the absence of a demonstrated acquisition pool, thin or non-distributable economics, funding and rebid exposure, high-consequence privacy and safeguarding failures, and occupation data that aggregate several industries. A durable social need does not guarantee paid demand or ownership economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5419 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.16 | 0.28 | 0.41 | PROXY | S1, S2 |
| rho | 0.25 | 0.45 | 0.64 | ESTIMATE | S2, S4, S6 |
| e | — | — | — | MISSING | — |
| s5 | — | — | — | MISSING | — |
| q | 0.18 | 0.38 | 0.6 | ESTIMATE | S4, S5 |
| d5 | 0.82 | 1.05 | 1.25 | PROXY | S3 |
| o | 0.8 | 0.93 | 0.99 | PROXY | S1, S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.87 | 2.73 | 5.69 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 3.60 | 7.60 | 10.00 | ESTIMATE |
| D | 6.56 | 9.77 | 10.00 | PROXY |

## Caveats
- a: OEWS covers NAICS 624200, including community food, other housing, and emergency-relief services outside 624221.
- a: Employment shares are not wage-weighted task shares, and the source does not measure AI exposure or existing automation.
- a: AI assistance in casework does not imply substitution for professional judgment or resident supervision.
- rho: No source measures five-year implementation of exposed AI tasks in 624221.
- rho: Federal ESG rules do not capture additional state licensing, local requirements, or protections for domestic-violence shelters.
- e: A zero modeled firm count does not prove that no qualifying operator exists; the dataset uses an estimated 8% social-assistance margin bridge.
- e: Grant recipients can use subrecipients or contractors, so recipient eligibility does not reveal the operator ownership mix.
- e: No defensible LMM-firm denominator was found.
- s5: The frozen dataset estimates zero firms in the target band.
- s5: IRS restrictions apply to section 501(c)(3) organizations, not every possible temporary-shelter operator.
- s5: Observed operating-control changes could occur without a transferable equity transaction.
- q: No source measures retained AI benefit for temporary-shelter operators.
- q: The estimate is conditional on an eligible operator existing despite the frozen zero firm count.
- q: Federal program terms do not represent every state, local, philanthropic, medical-crisis, youth, or domestic-violence funding arrangement.
- d5: A one-night homelessness count is not annual shelter utilization or funded demand.
- d5: The total includes unsheltered people and excludes some populations served by temporary shelters.
- d5: Policy and appropriations can cause service quantity to diverge sharply from underlying need.
- o: The sources describe current activities and compliance, not a five-year substitution rate.
- o: Physical shelter can remain necessary while provision shifts from dedicated facilities to hotels, apartments, or government operation.

## Sources
- **S1** — [2022 NAICS Definition: 624221 Temporary Shelters](https://www.census.gov/naics/?details=62&input=62&year=2022) (accessed 2026-07-22): Defines temporary shelters as establishments providing short-term emergency or temporary residential shelter and notes that operators may use their own shelters or subsidize existing housing, hotels, or motels.
- **S2** — [May 2023 OEWS: NAICS 624200 Community Food and Housing, and Emergency and Other Relief Services](https://www.bls.gov/oes/2023/may/naics4_624200.htm) (accessed 2026-07-22): Provides broader-industry employment and wage estimates by occupation, including management, business, office, community and social service, security, food-service, and facilities roles.
- **S3** — [HUD Releases 2025 Annual Homelessness Assessment Report to Congress](https://www.hud.gov/news/hud-no-26-037) (accessed 2026-07-22): Reports 745,652 people experiencing homelessness in the January 2025 point-in-time count, 3% fewer than 2024 and 27% more than 2013.
- **S4** — [Programs of HUD: Emergency Solutions Grants Program](https://www.hud.gov/hudprograms/) (accessed 2026-07-22): Describes formula grants for essential services, shelter operation, rental assistance, stabilization, and HMIS, including the administrative-cost allowance and public recipient structure.
- **S5** — [Inurement/private benefit: Charitable organizations](https://www.irs.gov/charities-non-profits/charitable-organizations/inurement-private-benefit-charitable-organizations) (accessed 2026-07-22): States that section 501(c)(3) organizations cannot operate for private interests and that net earnings cannot inure to a private shareholder or individual.
- **S6** — [24 CFR 576.403: Shelter and housing standards](https://www.ecfr.gov/current/title-24/part-576/section-576.403) (accessed 2026-07-22): Specifies ESG emergency-shelter safety, sanitation, privacy, accessibility, sleeping-space, food-preparation, and fire-safety requirements.
