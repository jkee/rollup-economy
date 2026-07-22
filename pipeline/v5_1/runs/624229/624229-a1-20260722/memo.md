# 624229 — Other Community Housing Services

*v5.1 Stage 1 research memo. Run `624229-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.28 · L 0.00 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A sizable documentation and coordination layer can be augmented while underlying housing and support needs remain persistent.
**Weakness:** Nonprofit/public dominance and grant-constrained economics leave very few clearly transferable LMM firms and weak evidence on retained savings.

## Business-model lens
- Included: Privately controllable operators providing recurring or repeat transitional-housing, low-income home-repair, housing-stabilization, or closely associated support services to governments, nonprofit prime contractors, institutional partners, or households, within the lower-middle-market EBITDA band.
- Excluded: Government agencies; charitable organizations without transferable control economics; donation-only or volunteer-only programs; passive property ownership; non-control financing vehicles; captive units; emergency shelters classified in NAICS 624221; and pure construction contractors classified elsewhere.
- Customer and revenue model: Revenue is typically a blend of competitively awarded government grants or subcontracts, reimbursable program funding, institutional service agreements, donations, and limited participant or homeowner payments. Work may combine housing operations, case management, compliance reporting, referral coordination, and field repair delivery.
- Deviation from default lens: The code combines transitional housing, volunteer-assisted low-cost housing construction or repair, and repair for elderly or disabled homeowners. The lens therefore retains only recurring or repeat service operators with transferable control economics and excludes non-transferable charitable programs and passive housing assets so that operating-workflow primitives remain coherent.

## Executive view
NAICS 624229 contains a useful administrative automation surface but is structurally awkward for a conventional control-oriented LMM screen. The code mixes transitional housing with volunteer-assisted construction and home repair, and federal programs are centered on nonprofit and public delivery. The most coherent target population is therefore a small subset of privately controllable recurring-service operators, not the industry at large.

## How AI changes the work
AI can assist intake, case-note drafting, benefits and resource research, document completeness checks, scheduling, funder reporting, and routine follow-up. It should remain human-supervised where decisions affect eligibility, safety, treatment, housing placement, or vulnerable clients; it does little to replace repairs, transport, on-site monitoring, or relationship-based support.

## Value capture
Capture depends more on contract form than technical savings. Fixed-price subcontracts and capacity-constrained programs may retain some benefit through avoided hiring or additional throughput, while cost-reimbursement grants, eligible-cost rules, competitive renewals, and mission commitments can return savings to funders or clients.

## Firm availability
Most visible delivery channels are nonprofit or governmental, and charitable asset-dedication rules limit conventional private transfer economics. The frozen n input is a placeholder-derived zero, not direct evidence that no organizations exist; a linked legal-form, ownership, award, and financial census is required before relying on firm availability.

## Demand durability
Housing instability, aging, disability, and social-service needs support durable underlying demand. HUD recorded historically high homelessness in 2024, and the FY 2026 CoC competition authorizes more than $4 billion, but funded volume can shift materially among transitional, permanent, rapid-rehousing, prevention, and repair models.

## Risks and uncertainty
The largest uncertainties are the eligible for-profit denominator, qualifying transfer incidence, and contract-specific retention. Additional risks include political and appropriations changes, privacy and security failures, biased or incorrect eligibility support, grant noncompliance, fragmented data, volunteer dependence, and misclassification across neighboring NAICS codes.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2608 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.25 | 0.42 | 0.57 | PROXY | S2, S3 |
| rho | 0.24 | 0.4 | 0.6 | PROXY | S2, S4, S5 |
| e | 0.01 | 0.06 | 0.18 | ESTIMATE | S1, S5, S8, S9 |
| s5 | 0.03 | 0.08 | 0.16 | ESTIMATE | S8 |
| q | 0.12 | 0.28 | 0.5 | ESTIMATE | S5, S6 |
| d5 | 0.9 | 1.06 | 1.25 | PROXY | S3, S6, S7, S9 |
| o | 0.82 | 0.92 | 0.98 | ESTIMATE | S2, S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.63 | 1.75 | 3.57 | PROXY |
| F | 0.00 | 0.00 | 0.00 | ESTIMATE |
| C | 2.40 | 5.60 | 10.00 | ESTIMATE |
| D | 7.38 | 9.75 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational sources cover a broader social-services population and do not isolate this NAICS code.
- a: The code's housing-repair and transitional-housing segments have materially different occupation mixes.
- a: Exposure denotes technically addressable work, not realized implementation or headcount reduction.
- rho: BTOS changed its AI-use question in late 2025 to cover any business function, complicating historical comparison.
- rho: No sector-specific adoption series was found for this six-digit industry.
- rho: Use of a drafting tool does not imply that the exposed task share is operationally implemented.
- e: No observed denominator of LMM firms by legal form or transferability was found.
- e: The dataset-injected n=0 is described as an estimate based on a placeholder margin and should not be interpreted as observed absence of operating organizations or eligible firms.
- e: NAICS establishment classification may place mixed housing-and-services organizations in another primary code.
- s5: No industry-specific transfer-rate series was found.
- s5: The range is conditional on eligibility and should not be applied to public or non-transferable charitable entities.
- s5: Asset transfers and nonprofit consolidations may look like deals but fail the qualifying-control definition.
- q: HUD program rules describe funding structure, not the share of AI benefit retained by operators.
- q: Revenue models vary sharply among grants, subcontracts, resident payments, donations, and home-repair projects.
- q: The estimate excludes demand and implementation effects, which belong in other primitives.
- d5: The 2024 point-in-time count measures need and system use on one night, not paid demand or annual service volume.
- d5: HUD reported transitional-housing beds fell 4% from 2023 to 2024 even as total homelessness rose, showing that program mix can diverge from need.
- d5: The July 2026 CoC competition was still subject to a proposed modification at the research date.
- o: The estimate is not an observed displacement rate.
- o: Digital-first navigation may substitute more operator work for low-acuity clients than the central case assumes.
- o: Physical home repair and residential supervision are more operator-dependent than referral-only services.

## Sources
- **S1** — [2022 NAICS definition: 624229 Other Community Housing Services](https://www.census.gov/naics/?input=624229&year=2022&details=624229) (accessed 2026-07-22): Defines the code as including transitional housing, volunteer-assisted low-cost housing construction or repair, repair for elderly or disabled homeowners, subsidized housing arrangements, and related household supplies.
- **S2** — [O*NET OnLine: Social and Human Service Assistants](https://www.onetonline.org/link/summary/21-1093.00) (accessed 2026-07-22): Documents adjacent frontline tasks including interviewing clients, records and reports, referrals, care plans, safety monitoring, home visits, transport, and direct public contact.
- **S3** — [BLS Occupational Outlook Handbook: Social and Human Service Assistants](https://www.bls.gov/ooh/community-and-social-service/social-and-human-service-assistants.htm) (accessed 2026-07-22): Describes client-service duties and projects 6% employment growth from 2024 to 2034, with 50,600 average annual openings.
- **S4** — [U.S. Census Bureau: Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports that overall business AI use hovered between 17% and 20% from December 2025 to May 2026 and explains the revised any-business-function measure.
- **S5** — [HUD Programs: Continuum of Care and related housing programs](https://www.hud.gov/hudprograms) (accessed 2026-07-22): Describes eligible CoC costs, project types, competitive application structure, 25% match requirement, and nonprofit/public applicant eligibility; also describes HOME and related housing delivery channels.
- **S6** — [HUD FY 2026 Continuum of Care Program Competition](https://www.hud.gov/hud-partners/coc-program-competition) (accessed 2026-07-22): States that the FY 2026 competition authorizes more than $4 billion for supportive services and housing programs and notes a pending July 2026 modification.
- **S7** — [HUD 2024 Annual Homelessness Assessment Report, Part 1](https://www.huduser.gov/portal/portal/sites/default/files/pdf/2024-AHAR-Part-1.pdf) (accessed 2026-07-22): Reports 771,480 people experiencing homelessness on a single night in 2024, an 18.1% annual increase, while transitional-housing beds declined 4% from 2023.
- **S8** — [IRS: Organizational Test for Internal Revenue Code Section 501(c)(3)](https://www.irs.gov/charities-non-profits/charitable-organizations/organizational-test-internal-revenue-code-section-501c3) (accessed 2026-07-22): Explains that a 501(c)(3) organization's assets must remain permanently dedicated to exempt or public purposes, constraining conventional private transfer economics.
- **S9** — [HUD Moving Forward on Bold Homelessness Reform](https://www.hud.gov/news/hud-no-26-031) (accessed 2026-07-22): States HUD's 2026 intention to increase investment in transitional housing and supportive services and lists nonprofit and public entities as eligible applicants.
