# 925110 — Administration of Housing Programs

*v5.1 Stage 1 research memo. Run `925110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** The principal driver is a large recurring caseload governed by standardized rules, forms, payments, plans, and reporting that can benefit from AI-assisted administration.
**Weakness:** The principal weakness is structural: government housing-program administrators cannot be acquired as lower-middle-market outsourced-service firms.

## Business-model lens
- Included: No private firm population satisfies the fixed lower-middle-market outsourced-service lens. The contextual operating population is federal, state, and local government establishments primarily administering and planning housing programs, including voucher funding, eligibility, payments, compliance, reporting, oversight, and public housing agency planning.
- Excluded: Private housing-program contractors, government rental-housing operations, residential landlords, emergency-shelter operators, building-code and inspection agencies, mortgage-market intermediaries, nonprofit housing providers, shells, captive internal units, and non-control financing vehicles.
- Customer and revenue model: Housing-program administrators are funded through appropriations, intergovernmental transfers, grants, and formula-based administrative fees rather than arm's-length commercial service revenue. Housing Choice Voucher administrative fees are tied to leased unit-months and reconciled against appropriated funding and reported program data.
- Deviation from default lens: none

## Executive view
Housing-program administration is a document-, rules-, and data-intensive government activity with substantial scope for AI-assisted workflow improvement and durable public need. It nevertheless contains no transferable private-firm population under the fixed acquisition lens and lacks a commercial retention construct.

## How AI changes the work
AI can support intake, document extraction, policy search, eligibility preparation, payment and funding analysis, forecasting, participant and landlord communications, plan drafting, anomaly detection, case summarization, reporting, and audit preparation. Due process, fair housing, sensitive personal data, appeals, inspections, fraud decisions, public input, and benefit authorization require strong human review and accountable governance.

## Value capture
Efficiency can reduce administrative burden, improve accuracy, shorten processing, and redirect staff toward participants, landlords, compliance, and difficult cases. These gains accrue as public capacity or budget efficiency rather than commercial margin, and appropriations and formula-based administrative fees govern available resources.

## Firm availability
There is no transferable firm pool in NAICS 925110. The Census definition is government establishments administering and planning housing programs; private software, consulting, inspection, and outsourced administration vendors belong to other industry codes.

## Demand durability
Millions of assisted households, broad affordability pressure, recurring eligibility and payment cycles, required plans, oversight, and persistent compliance needs support durable administrative demand. Actual service volume remains constrained by appropriations, policy design, voucher utilization, and possible agency consolidation.

## Risks and uncertainty
Major risks include erroneous benefit decisions, bias and fair-housing violations, privacy and cybersecurity failures, poor data quality, opaque models, legacy-system integration, procurement and staffing limits, changing federal policy, fragmented local practices, and public distrust. Available sources describe programs and modernization but do not provide a wage-weighted task mix or constant-quality demand index.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.38 | 0.54 | 0.68 | PROXY | S3, S4, S5, S6 |
| rho | 0.23 | 0.4 | 0.58 | PROXY | S3, S4, S5, S6 |
| e | 0 | 0 | 0 | ESTIMATE | S1 |
| s5 | 0 | 0 | 0 | ESTIMATE | S1, S4 |
| q | — | — | — | MISSING | — |
| d5 | 0.99 | 1.07 | 1.17 | ESTIMATE | S2, S4, S7 |
| o | 0.93 | 0.98 | 1 | ESTIMATE | S1, S4, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | — | — | — | MISSING |
| D | 9.21 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: HUD's systems and AI inventory do not quantify avoided labor or cover every state and local housing-program administrator.
- a: The provided labor-share input is unavailable because government operations lack a comparable receipts denominator.
- rho: Electronic submission and workflow tools are not necessarily AI and may already be embedded in the current baseline.
- rho: Housing agencies differ greatly in program mix, scale, staffing, software, local rules, and data quality.
- e: The provided dataset has no defensible LMM firm-count estimate because this government activity is outside SUSB's business scope.
- e: A zero here does not imply that housing-administration vendors are unavailable; it means those firms are outside this six-digit code.
- s5: The conditional population of eligible firms is empty, so the zero records structural inapplicability rather than an observed transaction rate.
- s5: Control transactions involving private technology or administrative-service vendors do not transfer the housing agency itself.
- q: Administrative savings can expand public-service capacity, but that is not commercial benefit retention.
- q: HUD may prorate administrative-fee eligibility to available appropriations, further separating public funding from market pricing.
- d5: Caseload and appropriations measure different things, and unmet housing need does not automatically become funded administrative demand.
- d5: Program rules, voucher funding, rental markets, and federal priorities can change materially within five years.
- o: The estimate concerns continued need for an accountable public operator, not government employment levels.
- o: Local consolidation or transfer of program administration between public agencies can change who operates the service without eliminating operator need.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: 925110 Administration of Housing Programs](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Official scope as government establishments administering and planning housing programs and exclusions for rental-housing operations, shelters, code inspection, and mortgage-market activity.
- **S2** — [HUD Rental Assistance: Improved Guidance and Oversight Needed for Utility Allowances](https://www.gao.gov/products/gao-24-105532) (accessed 2026-07-22): Scale of rental assistance and PHA administration, utility-allowance workload, data and oversight gaps, tool-usability issues, and rent-burden evidence.
- **S3** — [AI@HUD](https://www.hud.gov/ai) (accessed 2026-07-22): HUD AI strategy, compliance planning, technical requirements, and 2025 agency AI use-case inventories.
- **S4** — [Public Housing Agency Plans](https://www.hud.gov/helping-americans/public-indian-housing-pha-plans) (accessed 2026-07-22): Required five-year and annual plans, program and policy content, automated portal submission, agency categories, and compliance consequences.
- **S5** — [Housing Voucher Program Support Division](https://www.hud.gov/helping-americans/public-indian-housing-program-support-division) (accessed 2026-07-22): Automated systems, funding forecasts, dashboards, reporting, data management, program assistance, training, and efforts to reduce administration burden.
- **S6** — [Enterprise Voucher Management System Resources](https://www.hud.gov/helping-americans/public-indian-housing-evms-resources) (accessed 2026-07-22): Voucher-system modernization, housing-assistance payment calculations, online funding statements, training, permissions, and reporting-error dashboards.
- **S7** — [Housing Choice Voucher Program CY 2026 Administrative Fee Rates](https://www.hud.gov/sites/default/files/PIH/documents/2026-Administrative-Fee-Rate-Descriptions.pdf) (accessed 2026-07-22): Administrative-fee payment by leased unit-month, Voucher Management System data, funding proration, quarterly reconciliation, and blended-rate procedures.
