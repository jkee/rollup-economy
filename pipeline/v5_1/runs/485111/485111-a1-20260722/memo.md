# 485111 — Mixed Mode Transit Systems

*v5.1 Stage 1 research memo. Run `485111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.25 · L 0.00 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring public-service demand combined with AI-addressable dispatch, planning, customer-service, and administrative workflows.
**Weakness:** The apparent absence or near-absence of independent LMM mixed-mode operators that can actually undergo a control transfer.

## Business-model lens
- Included: US lower-middle-market private firms that operate recurring mixed-mode local or suburban transit service for external public-agency or institutional customers under operating contracts, including coordinated bus-and-rail or bus-and-other-mode systems.
- Excluded: Government transit authorities, municipal departments, captive internal fleets, stand-alone single-mode operators, support-only vendors, software-only suppliers, vehicle manufacturers, non-control financing vehicles, and firms outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: The core customer is normally a public transit authority or other public entity buying recurring operations through a competitively procured multiyear service contract; contract payments, rather than passenger fares retained directly by the operator, are the principal revenue model for the screened firm.
- Deviation from default lens: none

## Executive view
Mixed-mode transit has a narrow AI opportunity concentrated in coordination and administrative work rather than core frontline operations. Durable public-service demand and continuing accountability requirements are positives, but the screened private LMM population appears exceptionally thin and public procurement limits retained economics.

## How AI changes the work
Near-term AI can improve dispatch exception handling, rider communications, schedule and crew planning, maintenance triage, incident documentation, procurement support, and finance. Driving, mechanical work, cleaning, accessibility assistance, and safety-critical control remain human-heavy; vehicle automation is still largely in assistance and pilot stages.

## Value capture
Savings may accrue during fixed-price contract periods, but cost review, public-agency bargaining, change clauses, competitive rebids, and imitation should return a substantial share to the customer over five years. Capture depends far more on contract language and renewal timing than on passenger fare elasticity.

## Firm availability
The code describes operators of whole multi-mode metropolitan systems, which are often public authorities. Private purchased-transportation contractors exist, but an independent firm both correctly coded here and inside the target EBITDA band is likely rare; the frozen dataset estimate of zero LMM firms is directionally consistent with that structural scarcity.

## Demand durability
Transit ridership continues to recover and authorities are expected to expand or redesign bus service, supporting modest real quantity growth. Remote work, public-budget stress, and uneven rail-versus-bus recovery limit confidence, but the service's mobility and accessibility functions make wholesale disappearance unlikely.

## Risks and uncertainty
The largest uncertainties are classification and denominator risk, contract economics, union and regulatory constraints, public funding, legacy data quality, and the pace of autonomous transit. A bidder could mistake a public authority, large-company subsidiary, or contract award for an eligible transferable LMM firm.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 6.7968 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.24 | ESTIMATE | S2, S3 |
| rho | 0.3 | 0.5 | 0.7 | ESTIMATE | S3, S4, S7 |
| e | 0.02 | 0.08 | 0.2 | ESTIMATE | S1, S6, S7 |
| s5 | 0.08 | 0.18 | 0.3 | ESTIMATE | S6 |
| q | 0.3 | 0.45 | 0.6 | ESTIMATE | S5, S10 |
| d5 | 0.98 | 1.08 | 1.18 | PROXY | S8, S9 |
| o | 0.93 | 0.97 | 0.995 | PROXY | S3, S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 6.52 | 10.00 | 10.00 | ESTIMATE |
| F | 0.00 | 0.00 | 0.00 | ESTIMATE |
| C | 6.00 | 9.00 | 10.00 | ESTIMATE |
| D | 9.11 | 10.00 | 10.00 | PROXY |

## Caveats
- a: BLS publishes the cited occupation mix for Urban Transit Systems rather than specifically for 485111 private LMM contractors.
- a: The chart reports employment, not wage weights or task shares, and only the ten largest occupations.
- a: The frozen compensation-to-receipts input uses 2024 wages over 2022 receipts and is harmonized to an IPS basis; that vintage and basis mismatch can distort the economic importance of this task share.
- rho: FTA evidence emphasizes vehicle automation and demonstrations, while much of the estimated five-year opportunity is office and operations-support AI.
- rho: Large public agencies may implement more slowly than private LMM contractors, but small contractors may lack data and integration capacity.
- rho: The estimate excludes pricing, demand, and valuation effects.
- e: NTD is organized around reporting agencies and contracts, not firms or EBITDA bands.
- e: A contractor may be coded under a broader transit, staffing, or management-services NAICS rather than 485111.
- e: The provided LMM firm count is an ESTIMATE built from size-class receipts and a sector margin bridge, and equals zero; small classification errors therefore matter greatly.
- s5: No source measures five-year control-transfer probability for eligible 485111 LMM firms.
- s5: The denominator is extremely small and uncertain because the provided LMM firm count is zero.
- s5: Contract turnover, concession novation, and parent-company transactions can be mistaken for firm-level control transfers.
- q: FTA guidance governs federally assisted procurement broadly and does not measure contractor retention of AI savings.
- q: Contract terms vary materially between fixed-price, cost-reimbursement, management-fee, and concession structures.
- q: The national fare and expense totals span all transit modes and public operators, not only screened private mixed-mode contractors.
- d5: Ridership is not identical to purchased service quantity; agencies can change frequency, vehicle size, or subsidy without proportional trip changes.
- d5: The BLS occupation combines transit and intercity bus drivers and is a ten-year national employment projection.
- d5: Mixed-mode rail and bus components may follow different demand paths, and fiscal funding can interrupt otherwise durable rider need.
- o: Bus evidence does not cover every rail mode inside mixed-mode systems, some of which already use high automation.
- o: Accountable operator retention can remain high even when frontline labor hours decline sharply.
- o: Unexpected regulatory approval or a safe full-size autonomous fleet could lower operator-required quantity faster than assumed.

## Sources
- **S1** — [North American Industry Classification System, United States, 2022](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 485111 as establishments operating local and suburban transit systems using more than one mode over regular routes and schedules, and distinguishes single-mode and support-service activities.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest occupations in Urban Transit Systems, including 24,540 transit/intercity bus drivers, 2,640 bus and truck mechanics, 1,150 dispatchers, 740 customer-service representatives, and 650 general and operations managers.
- **S3** — [Transit Automation Research](https://www.transit.dot.gov/automation-research) (accessed 2026-07-22): Identifies FTA automation use cases and describes current work as research, demonstrations, business-case analysis, and resolution of policy, insurance, accessibility, and regulatory questions.
- **S4** — [When will driverless buses operate on public roads?](https://www.transit.dot.gov/when-will-driverless-buses-operate-public-roads) (accessed 2026-07-22): States most piloted systems warn or assist drivers; Level 4 shuttles are generally 6-15 passengers at 10-15 mph, current pilots retain attendants, and they may not match regular service in complex environments.
- **S5** — [FTA Circular 4220.1G: Third Party Contracting Guidance](https://www.transit.dot.gov/sites/fta.dot.gov/files/2025-01/Third-Party-Contracting-Guidance-%28Circular-4220.1G%29.pdf) (accessed 2026-07-22): Requires reasonable contract periods that do not undermine full and open competition and says federally assisted project costs must be necessary, reasonable, and allocable.
- **S6** — [2024 Annual Database Contractual Relationship](https://www.transit.dot.gov/ntd/data-product/2024-annual-database-contractual-relationship) (accessed 2026-07-22): Documents that NTD publishes contract information by agency, contractor, mode, and service type, including procurement method, contract duration, private providers, fare revenue, and net contract expenditures.
- **S7** — [49 CFR Part 37: Transportation Services for Individuals with Disabilities](https://www.transit.dot.gov/regulations-and-guidance/civil-rights-ada/part-37-transportation-services-individuals-disabilities) (accessed 2026-07-22): Requires a private entity operating fixed-route or demand-responsive service for a public entity to meet the public entity's applicable accessibility obligations.
- **S8** — [Public Transportation Ridership Update](https://www.apta.com/resource/public-transportation-ridership-update/) (accessed 2026-07-22): Reports 7.7 billion US public-transit trips in 2024, 7% growth from 2023, and recovery to 85% of pre-pandemic ridership by April 2025.
- **S9** — [Bus Drivers: Occupational Outlook Handbook](https://www.bls.gov/ooh/transportation-and-material-moving/bus-drivers.htm) (accessed 2026-07-22): Projects transit and intercity bus-driver employment to grow 4% from 2024 to 2034 and attributes growth partly to public-authority system upgrades, redesigns, service expansion, and BRT.
- **S10** — [2024 National Transit Summaries and Trends](https://www.transit.dot.gov/sites/fta.dot.gov/files/2026-04/2024%20National%20Transit%20Summaries%20and%20Trends_1.2.pdf) (accessed 2026-07-22): Reports total 2024 transit operating expenses of $62.5628 billion and fares of $11.0300 billion across modes.
