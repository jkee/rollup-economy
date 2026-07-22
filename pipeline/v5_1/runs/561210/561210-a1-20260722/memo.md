# 561210 — Facilities Support Services

*v5.1 Stage 1 research memo. Run `561210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.03 · L 1.17 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring bundled facility contracts provide a durable operator platform where AI can improve coordination and asset-management workflows.
**Weakness:** Most labor performs physical on-site work, sharply limiting the share of wages that AI can substitute or avoid.

## Business-model lens
- Included: US lower-middle-market firms providing recurring outsourced combinations of on-site facility support services, such as janitorial, maintenance, security, mail routing, reception, laundry, grounds, utilities, and related coordination, to external business, institutional, or government customers.
- Excluded: Captive facilities departments, shell entities, non-control financing vehicles, firms outside the approximate $1-10M normalized EBITDA band, single-service contractors classified elsewhere, computer-facilities managers, property managers without operating staff, and providers responsible for a customer's core business.
- Customer and revenue model: Customers buy bundled ongoing facility operations through multi-year or annually renewable contracts, task orders, fixed monthly or unit prices, performance-based fees, labor-hour arrangements, and reimbursable pass-throughs for selected materials or services.
- Deviation from default lens: none

## Executive view
Facilities support is a recurring outsourced service with substantial physical labor and durable on-site requirements. AI is more likely to improve dispatch, maintenance planning, monitoring, documentation, procurement, and supervision than to remove cleaners, guards, technicians, or the operating platform.

## How AI changes the work
The practical use cases are work-order classification, technician routing, predictive maintenance, energy optimization, inventory planning, compliance documentation, incident summaries, staffing forecasts, and automated reporting. Physical execution, safety decisions, field diagnosis, and exception response remain human-heavy.

## Value capture
Fixed-price and performance-based contracts can preserve coordination and productivity gains within a contract term, while hourly, reimbursable, open-book, staffing-floor, and wage-adjusted arrangements pass benefits through more quickly. Recompetes and customer audits should share gains over time.

## Firm availability
The NAICS definition fits recurring outsourced operations, but eligible supply is narrowed by concentrated government or institutional accounts, contract novation and clearance rules, labor dependencies, and providers that are effectively single-service contractors. Broad service-business deal data show liquidity but not exact transfer incidence.

## Demand durability
BLS projects modest real output growth for exact-industry facilities support. Aging assets, outsourced specialization, energy management, and compliance support demand, while reduced office footprints, procurement pressure, insourcing, and customer unbundling can offset growth.

## Risks and uncertainty
The largest uncertainties are the absence of a wage-weighted task study, uneven building-data readiness, unknown contract-form mix, and no exact transfer denominator. A poor outcome would combine limited access to customer systems, small addressable management overhead, labor-hour or open-book pricing, concentrated contracts, and rapid customer unbundling or insourcing.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3109 | — | OBSERVED | — |
| n | — | 662 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.31 | PROXY | S2, S3 |
| rho | 0.27 | 0.47 | 0.66 | PROXY | S3, S4 |
| e | 0.52 | 0.68 | 0.82 | ESTIMATE | S1, S8 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S5 |
| q | 0.42 | 0.61 | 0.78 | PROXY | S7 |
| d5 | 0.95 | 1.07 | 1.16 | PROXY | S6 |
| o | 0.8 | 0.89 | 0.96 | ESTIMATE | S1, S2, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.40 | 1.17 | 2.54 | PROXY |
| F | 6.02 | 7.41 | 8.40 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | PROXY |
| D | 7.60 | 9.52 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS measures jobs rather than task hours and includes facilities and employers outside the LMM lens.
- a: Global facility-management conference evidence is not representative of US 561210 firms.
- a: Robotics, sensors, and conventional building-management software blur the boundary between AI exposure and already-automated work.
- rho: BTOS does not isolate 561210 and measures firm use rather than depth or realized labor capture.
- rho: The IFMA figures come from a global conference summary and may reflect more sophisticated organizations.
- rho: Customer-owned systems, cybersecurity rules, procurement cycles, and building-data quality can delay implementation.
- e: No source measures the eligible share of the injected LMM firm estimate.
- e: The injected firm count is margin-bridged and may not align cleanly with normalized EBITDA for pass-through-heavy contracts.
- e: A recurring contract can still be nontransferable or commercially fragile because of recompetes, novation, clearances, or customer concentration.
- s5: BizBuySell is broad, voluntary, and centered on sellers below the target EBITDA band.
- s5: The source does not distinguish asset sales, equity control transfers, or repeat activity involving the same buyer.
- s5: Government and institutional contract-transfer restrictions can reduce qualifying supply.
- q: Federal rules are a population proxy and do not quantify the industrywide mix of public and private contract forms.
- q: Fixed-price labels do not reveal staffing minimums, wage escalators, scope changes, penalties, or rebid behavior.
- q: Savings in management and dispatch may be small relative to physical labor and materials embedded in a bundled price.
- d5: BLS projections are modeled national forecasts, not observations for the LMM lens.
- d5: Chained-dollar output is not a direct constant-quality service-volume index.
- d5: Demand differs across government, healthcare, education, commercial office, industrial, and correctional facilities.
- o: No source directly measures the year-five operator-required quantity share.
- o: Operator necessity varies with facility type, service bundle, labor availability, and customer willingness to self-manage vendors.
- o: Faster robotics adoption or direct building-software procurement could reduce operator-required quantity more than assumed.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: 561210 Facilities Support Services](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Exact-industry scope, bundled outsourced facility-support model, physical service examples, and cross-references defining excluded activities.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 561200 Facilities Support Services](https://www.bls.gov/oes/2023/may/naics4_561200.htm) (accessed 2026-07-22): Exact-industry total employment, occupational shares, and wages used to structure task exposure and physical operator requirements.
- **S3** — [World Workplace Europe 2025 Summary: Shaping Sustainable Futures](https://we.ifma.org/wp-content/uploads/2025/05/WWPE-2025-Summary-web72dpi.pdf) (accessed 2026-07-22): Facility-management AI use cases and reported barriers involving data quality, combined FM-and-AI skills, workflows, governance, and integration.
- **S4** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Recent BTOS evidence on overall US business AI use, expected use, size-related adoption differences, and measured business functions.
- **S5** — [Business Acquisitions Stabilize as Buyers Get Selective: AI and Cost Discipline Drive 2026 Playbook](https://www.bizbuysell.com/news/bizbuysell-2025-fourth-quarter-insight-report/) (accessed 2026-07-22): Broad 2025 Main Street and service-business transaction activity and seller scale used as a transfer-market proxy.
- **S6** — [Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Exact-industry Facilities Support Services employment and chained-dollar output projections used for the five-year demand proxy.
- **S7** — [Federal Acquisition Regulation 8.404: Use of Federal Supply Schedules](https://www.acquisition.gov/far/8.404) (accessed 2026-07-22): Service-order pricing at hourly or task-fixed prices and the federal preference for fixed-price commercial service orders used to bridge benefit retention.
- **S8** — [GSA Facility Related Services](https://www.gsa.gov/buy-through-us/products-and-services/facilities-and-construction/facility-related-services) (accessed 2026-07-22): Concrete facility-service scope including janitorial, custodial, preventive maintenance, grounds, utility systems, HVAC, energy management, and support services.
