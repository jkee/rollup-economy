# 531311 — Residential Property Managers

*v5.1 Stage 1 research memo. Run `531311-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 7.48 · L 5.54 · interval CONDITIONAL → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High-volume recurring communications, records, leasing administration, work-order triage, and reporting create implementable AI-assisted operating leverage.
**Weakness:** Client contracts can reprice or terminate, while local compliance, maintenance, emergencies, and resident relationships keep substantial labor and execution risk in the service.

## Business-model lens
- Included: United States lower-middle-market firms that manage residential houses, apartments, multifamily communities, and other residential rental property for external owners under recurring or repeat service agreements.
- Excluded: Owners managing only their own property, captive management departments, nonresidential property managers, associations that do not provide property management, software-only platforms, shells, and owner-dependent practices that cannot transfer without the seller.
- Customer and revenue model: Property owners purchase recurring management, leasing, rent administration, reporting, maintenance coordination, compliance, inspection, and resident-service work. Revenue commonly combines recurring management fees with leasing, maintenance coordination, application, or other service charges.
- Deviation from default lens: none

## Executive view
Residential property management is a recurring outsourced service with a large digital-administrative workload and durable physical and legal responsibilities. AI can materially improve capacity, while accountable local operations and contract relationships preserve a substantial operator role.

## How AI changes the work
The clearest uses are leasing-response automation, resident communications, document extraction, payment follow-up, work-order triage, vendor dispatch support, recordkeeping, budgeting, and owner-report drafting. Field inspection, emergencies, disputes, compliance judgment, vendor accountability, and sensitive owner and resident interactions remain human-led.

## Value capture
Recurring fee agreements allow some implemented savings to remain with the manager during contract terms, and faster response can support unit growth. Owners can recapture value at renewal, however, and software, security, verification, and higher service expectations absorb part of the gross benefit.

## Firm availability
The exact industry definition strongly matches outsourced recurring service, and unit portfolios, teams, systems, and vendor networks can transfer. Eligibility is reduced by owned-property mixtures, nonassignable agreements, owner-centric relationships, licensing, and contract attrition at change of control.

## Demand durability
Rental properties continue to require rent administration, leasing, maintenance, compliance, and resident service even when rents or occupancy soften. Software-enabled self-management and owner consolidation can reduce outsourcing, but physical and accountable operations limit full substitution.

## Risks and uncertainty
Key risks are local housing cycles, rent regulation, fair-housing and privacy liability, cyber fraud, maintenance and insurance inflation, resident-service failures, client concentration, contract termination rights, licensing, mixed owned-versus-managed portfolios, and vendor-sponsored adoption evidence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4675 | — | OBSERVED | — |
| n | — | 246 | — | ESTIMATE | — |
| a | 0.4 | 0.55 | 0.69 | PROXY | S2, S3 |
| rho | 0.42 | 0.61 | 0.75 | PROXY | S4 |
| e | 0.68 | 0.82 | 0.91 | ESTIMATE | S1 |
| s5 | 0.08 | 0.15 | 0.24 | PROXY | S6 |
| q | 0.38 | 0.55 | 0.7 | ESTIMATE | S3, S4 |
| d5 | 0.94 | 1.04 | 1.15 | PROXY | S3, S5 |
| o | 0.64 | 0.78 | 0.89 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 3.14 | 6.27 | 9.68 | PROXY |
| F | 4.29 | 5.54 | 6.44 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 6.02 | 8.11 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit wage-weighted task study was found.
- a: The broader occupational mix includes real-estate business models outside residential fee management.
- a: AI assistance in communication and records is not equivalent to eliminating field and accountable work.
- rho: Vendor-sponsored adoption data may overrepresent technology-oriented operators.
- rho: Reported use does not quantify workflow coverage or net labor savings.
- rho: The survey population is not isolated to LMM US residential fee managers.
- e: No direct audit of the margin-bridged LMM population was found.
- e: Establishments are not necessarily independent firms or transferable control targets.
- e: Contract assignability and owned-versus-managed unit mix are not visible in classification data.
- s5: Owner intentions are not completed transactions.
- s5: The succession evidence is not industry-specific.
- s5: Internal transfers or sales with severe contract attrition may not qualify.
- q: No direct evidence measures post-AI fee pass-through in residential management contracts.
- q: Ancillary fees and in-house maintenance can blur management-service retention.
- q: Owners may demand better service rather than permit equal output with fewer hours.
- d5: Occupational employment covers nonresidential and community-association managers as well as residential managers.
- d5: National vacancy and homeownership rates do not measure outsourced management penetration.
- d5: Local housing regulation and supply cycles produce wide geographic dispersion.
- o: No direct substitution study isolates the exact six-digit industry.
- o: Software may let some owners insource without eliminating the underlying management tasks.
- o: Required human presence varies sharply by portfolio scale, geography, and property condition.

## Sources
- **S1** — [2022 NAICS Definition: 531311 Residential Property Managers](https://www.census.gov/naics/?details=531311&input=531311&year=2022) (accessed 2026-07-22): Official six-digit definition of establishments primarily managing residential real estate for others.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 531000 Real Estate](https://www.bls.gov/oes/2023/May/naics4_531000.htm) (accessed 2026-07-22): Broader real-estate occupation mix, including property managers, office and administrative support, accounting, customer service, and physical occupations.
- **S3** — [Occupational Outlook Handbook: Property, Real Estate, and Community Association Managers](https://www.bls.gov/ooh/management/property-real-estate-and-community-association-managers.htm?source=post_page-----59b112572263----------------------) (accessed 2026-07-22): Management duties, recurring operational responsibilities, use of contracted managers, customer and field work, and 2024-2034 employment outlook.
- **S4** — [From Flat Rents to AI Adoption: The 2025 AppFolio Property Management Benchmark Report Reveals Key Trends](https://naahq.org/flat-rents-ai-adoption-2025-appfolio-property-management-benchmark-report-reveals-key-trends) (accessed 2026-07-22): Survey population, AI adoption and planned use, technology priorities, cybersecurity concerns, fee-manager revenue actions, and operating outlook.
- **S5** — [Quarterly Residential Vacancies and Homeownership, Second Quarter 2025](https://www.census.gov/housing/hvs/files/qtr225/Q225press.pdf) (accessed 2026-07-22): National rental vacancy and homeownership rates used as broad housing-demand context.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry five-year employer-owner sale and transfer intentions and owner-dependence context.
