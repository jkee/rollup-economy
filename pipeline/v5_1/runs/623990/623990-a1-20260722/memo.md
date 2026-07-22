# 623990 — Other Residential Care Facilities

*v5.1 Stage 1 research memo. Run `623990-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 6.79 · L 4.16 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring publicly funded occupancy, persistent resident need, and heavy documentation and coordination burden create a focused opportunity for workflow assistance across multi-home operators.
**Weakness:** Direct human care and safeguarding dominate the service, while administered reimbursement, nonprofit ownership, and regulatory transfer constraints limit both benefit capture and the conventional acquisition pool.

## Business-model lens
- Included: US lower-middle-market operators of staffed residential group homes that provide recurring supervision, personal care, habilitation, case support, and daily living assistance to children, disabled people without nursing care, or justice-involved residents under government, Medicaid, managed-care, or agency placement arrangements.
- Excluded: Donation-dependent orphanages, boot or disciplinary camps, private-pay atypical residences, temporary shelters, nursing facilities, assisted living, residential mental health or substance-abuse facilities, intellectual and developmental disability facilities classified elsewhere, correctional institutions, captive government operations, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring occupancy- or service-linked payments, commonly per-diem reimbursement, public-agency placement contracts, Medicaid or managed-care reimbursement, and block or capacity contracts, with residents receiving continuous supervision and personal care.
- Deviation from default lens: Narrowed for coherence to staffed group-home operators supported mainly by public or managed-care reimbursement. The full code also contains donor-funded orphanages, disciplinary camps, and atypical private-pay homes whose payer, ownership, transferability, and demand economics are too different for one screen; the narrowing is based on business-model comparability, not attractiveness.

## Executive view
Staffed group homes provide recurring, essential care to vulnerable residents, but the NAICS code is heterogeneous and much of the economics are shaped by public reimbursement, licensing, nonprofit ownership, and direct-care labor. AI can reduce documentation and coordination burden; it cannot replace continuous supervision, personal care, safeguarding, or relationship-based case work.

## How AI changes the work
Useful applications include case-note and shift-summary drafting, incident-report support, schedule and authorization checks, billing review, policy retrieval, recruiting administration, care-plan synthesis, and management reporting. Human review remains necessary because outputs can affect resident safety, placements, legal proceedings, benefits, and regulatory compliance.

## Value capture
Fixed or administered reimbursement can preserve some back-office savings between rate reviews. Capture is weaker where cost reports, contract renewals, direct-care spending requirements, understaffing, or payer pressure redirect savings toward wages and service quality rather than margin.

## Firm availability
The code includes scaled group-home operators, but the transferable pool is diluted by nonprofits, government-controlled programs, single-site homes, mixed-code providers, and entities without conventional equity. Licensure, Medicaid enrollment, incident history, property structure, and resident continuity make diligence and closing more complex than ordinary service acquisitions.

## Demand durability
Need for safe residential support remains durable for children and adults who cannot live independently, and direct human accountability is difficult to substitute. Growth is restrained by public budgets and deliberate movement toward family placements, self-directed supports, and less institutional settings; qualifying small community homes may benefit or lose share depending on state implementation.

## Risks and uncertainty
The largest uncertainties are the code's mixed populations and ownership forms, the absence of wage-weighted task data for the narrowed lens, and state-level variation in rates, licensing, placement policy, and transfer approval. Material operating risks include abuse or neglect allegations, critical incidents, workforce shortages, wage mandates, reimbursement delays, occupancy volatility, property separation, payer concentration, and compliance failures. The injected compensation ratio is directionally plausible for labor-intensive care but uses a vintage-mismatched denominator, while the injected firm count relies on a public healthcare-facility margin proxy that may misstate this provider model.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.8153 | — | OBSERVED | — |
| n | — | 511 | — | ESTIMATE | — |
| a | 0.18 | 0.29 | 0.37 | PROXY | S2, S3, S4, S5 |
| rho | 0.3 | 0.44 | 0.6 | PROXY | S3, S4, S5, S6, S8 |
| e | 0.35 | 0.52 | 0.7 | ESTIMATE | S1, S2, S7 |
| s5 | 0.06 | 0.12 | 0.2 | PROXY | S1, S9 |
| q | 0.22 | 0.38 | 0.56 | ESTIMATE | S8 |
| d5 | 0.9 | 1.01 | 1.12 | PROXY | S2, S7 |
| o | 0.92 | 0.97 | 0.99 | ESTIMATE | S1, S3, S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.76 | 4.16 | 7.24 | PROXY |
| F | 3.96 | 5.62 | 6.89 | ESTIMATE |
| C | 4.40 | 7.60 | 10.00 | ESTIMATE |
| D | 8.28 | 9.80 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS matrix covers the full heterogeneous industry rather than the narrowed payer model.
- a: O*NET tasks are occupation-wide and do not measure current AI substitution.
- a: The wage adjustment is judgmental because the matrix reports employment rather than payroll by occupation.
- rho: Economy-wide adoption does not establish care-provider implementation or labor avoidance.
- rho: State privacy, licensing, documentation, and incident-reporting requirements vary.
- rho: Savings from documentation assistance may be redeployed to resident care rather than reduce hiring.
- e: No source measures eligibility under the narrowed ownership and earnings lens.
- e: Legal entities may operate facilities across several neighboring residential-care codes.
- e: The injected firm-count estimate uses a broad healthcare-facility margin bridge that may not represent publicly reimbursed group homes.
- s5: Gallup measures intentions across industries rather than completed care-provider deals.
- s5: Nonprofit affiliations and asset transfers may not qualify as conventional control transfers.
- s5: Public transaction databases undercount small private and nonprofit combinations.
- q: The CMS direct-care spending rule applies to specified Medicaid services and has flexibilities, not every activity or payer in the narrowed lens.
- q: State reimbursement and contract structures vary materially.
- q: No source directly measures retention of AI-enabled benefits.
- d5: Employment is a proxy for real service demand and can move with staffing rules or labor availability.
- d5: The BLS line covers excluded orphanage, camp, and atypical residential models.
- d5: National Medicaid HCBS trends do not identify this six-digit industry or distinguish qualifying group-home settings.
- o: No source directly measures the operator-required share of future service quantity.
- o: Remote monitoring can change staffing models without eliminating accountable-provider demand.
- o: Policy-driven reclassification or movement to home-based services can displace lens operators while resident need persists.

## Sources
- **S1** — [2022 NAICS Definition: 623990 Other Residential Care Facilities](https://www.census.gov/naics/?chart=2022&details=623990&input=623990) (accessed 2026-07-22): Defines the industry as residential care with supervision and personal care, gives group-home and youth-care examples, and identifies neighboring excluded care industries.
- **S2** — [BLS National Employment Matrix: Other Residential Care Facilities](https://data.bls.gov/projections/nationalMatrix?ioType=i&queryParams=623900) (accessed 2026-07-22): Provides the detailed industry occupation mix and projects total employment from 165.8 thousand to 170.0 thousand, including large healthcare-support, community-social-service, and personal-care groups.
- **S3** — [O*NET OnLine: Personal Care Aides](https://www.onetonline.org/link/details/31-1122.00) (accessed 2026-07-22): Describes direct personal care, health monitoring, companionship, household help, transport, case review, and client-record tasks.
- **S4** — [O*NET OnLine: Residential Advisors](https://www.onetonline.org/link/details/39-9041.00) (accessed 2026-07-22): Describes observation, safety rounds, first aid, mediation, rule enforcement, resident plans, counseling, reports, and administrative work.
- **S5** — [O*NET OnLine: Child, Family, and School Social Workers](https://www.onetonline.org/link/details/21-1021.00) (accessed 2026-07-22): Describes case records, reports, interviews, service plans, legal matters, counseling, referrals, coordination, and placement-related judgment.
- **S6** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports nationally representative recent business AI use near one-fifth overall, higher adoption among larger firms, and measurement across multiple administrative functions.
- **S7** — [Medicaid Home and Community-Based Services](https://www.medicaid.gov/medicaid/home-community-based-services) (accessed 2026-07-22): Explains policy support for care in homes and communities and reports that 86.2 percent of Medicaid long-term-support users received HCBS in 2021.
- **S8** — [HCBS Payment Adequacy Provisions in the Ensuring Access to Medicaid Services Final Rule](https://www.medicaid.gov/medicaid/access-care/downloads/access-final-rule-slides-july-2024.pdf) (accessed 2026-07-22): Documents reporting, oversight, and the generally applicable 80 percent direct-care compensation minimum for specified Medicaid personal-care services beginning in 2030, with stated flexibilities and exceptions.
- **S9** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of employer-business owners intended to sell or transfer ownership within five years, providing a broad succession-intention proxy.
