# 624230 — Emergency and Other Relief Services

*v5.1 Stage 1 research memo. Run `624230-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 4.79 · L 1.39 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Rising disaster complexity and a large planning, reporting, grant, casework, and coordination burden create recurring opportunities for human-supervised AI support.
**Weakness:** The commercially eligible firm pool and retained economics are poorly observed, while demand is unusually exposed to event timing and abrupt public-policy changes.

## Business-model lens
- Included: Lower-middle-market firms supplying recurring or repeat outsourced disaster relief, emergency food or shelter, material-aid logistics, survivor counseling, case management, or refugee and immigrant resettlement services to governments, institutions, nonprofit prime contractors, or affected populations.
- Excluded: Government emergency-management departments; captive internal response units; shells and non-control vehicles; spontaneous volunteer groups without an operating enterprise; direct medical providers, transportation carriers, restoration contractors, and logistics vendors classified outside NAICS 624230; and organizations outside the lower-middle-market EBITDA band.
- Customer and revenue model: Revenue commonly comes from government grants, cooperative agreements, cost-reimbursement programs, competitively or urgently awarded service contracts, nonprofit subcontracts, donations, and restricted program funding. Delivery spans preparedness and grant administration, emergency deployment, shelter and commodity operations, case management, resettlement, and long-tail recovery support.
- Deviation from default lens: none

## Executive view
Emergency and other relief services combine an exposed administrative and coordination layer with a highly physical, trust-sensitive delivery core. Demand need is durable but volatile, public funding and nonprofit delivery dominate, and commercially transferable operators appear to be a minority of the estimated LMM population.

## How AI changes the work
AI can support emergency-plan drafting, regulation and resource retrieval, grant applications, needs triage, multilingual document handling, case-note preparation, schedule and inventory coordination, situation-report drafting, and after-action analysis. Human command remains essential for live decisions, public warnings, safeguarding, counseling, damage assessment, shelter operations, and physical delivery.

## Value capture
Retention turns on award structure. Fixed-price or urgent response contracts may preserve some benefit through avoided surge hiring and faster throughput, while grants and reimbursable programs can rebase budgets, restrict underspend, audit costs, or redirect savings toward beneficiaries.

## Firm availability
The frozen dataset estimates 137 LMM-band firms, but it uses an 8% placeholder margin and does not establish ownership eligibility. FEMA emphasizes voluntary agencies, charitable assets cannot be distributed for private purposes, and many commercial disaster suppliers sit in other NAICS codes, so legal-form and primary-code diligence is decisive.

## Demand durability
Disaster frequency and federal recovery workload support persistent need, but annual volume is event-driven. Refugee resettlement moves independently with policy: the FY 2026 ceiling changed within the year and remained far below the prior-year target. Segment mix can therefore change much faster than aggregate social-assistance demand.

## Risks and uncertainty
Major risks are event volatility, appropriations and immigration-policy changes, grant dependence, nonprofit transfer constraints, contract novation, data privacy, multilingual or eligibility errors, misinformation during crises, degraded connectivity, volunteer availability, fraud controls, reputational harm, and classification leakage into adjacent industries.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1947 | — | OBSERVED | — |
| n | — | 137 | — | ESTIMATE | — |
| a | 0.28 | 0.46 | 0.62 | PROXY | S2, S3, S4, S6 |
| rho | 0.24 | 0.42 | 0.62 | PROXY | S2, S5, S13 |
| e | 0.02 | 0.1 | 0.25 | ESTIMATE | S1, S6, S11 |
| s5 | 0.04 | 0.1 | 0.2 | ESTIMATE | S8, S11 |
| q | 0.14 | 0.32 | 0.55 | ESTIMATE | S7, S8 |
| d5 | 0.88 | 1.04 | 1.3 | PROXY | S3, S9, S10, S12 |
| o | 0.86 | 0.95 | 0.99 | ESTIMATE | S2, S4, S6, S13 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.52 | 1.50 | 2.99 | PROXY |
| F | 0.17 | 1.39 | 3.31 | ESTIMATE |
| C | 2.80 | 6.40 | 10.00 | ESTIMATE |
| D | 7.57 | 9.88 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation sources span government and adjacent social-service settings rather than this six-digit industry.
- a: Disaster response, material relief, and refugee resettlement have materially different labor mixes.
- a: Exposure excludes already automated work and does not imply safe autonomous use during crises.
- rho: BTOS changed its AI-use wording in late 2025 to include any business function.
- rho: No six-digit industry adoption series or relief-specific implementation benchmark was found.
- rho: Disaster surges can expose tools to novel conditions that are absent from normal-period pilots.
- e: No observed legal-form or control-eligibility denominator was found for the estimated LMM band.
- e: The dataset-injected n=137 depends on an 8% placeholder margin and SUSB size-class receipts, so band membership is estimated rather than observed.
- e: For-profit vendors serving disasters may be recorded outside this industry, while tax-exempt relief organizations can appear in private-employer data.
- s5: No industry-specific control-transfer rate was found.
- s5: Emergency contract awards and nonprofit affiliations are not themselves qualifying control transfers.
- s5: The interval is conditional on eligibility and excludes dissolution without transferable operations.
- q: The federal cost-share and urgent-award sources describe public funding structures, not operator retention of AI benefits.
- q: Donation-funded, grant-funded, cost-reimbursement, and fixed-price programs have very different retention mechanics.
- q: The estimate excludes implementation and demand effects.
- d5: Billion-dollar disaster counts measure loss events, not purchased relief-service units.
- d5: Refugee ceilings are policy limits rather than realized admissions and can change within a fiscal year.
- d5: Five-year demand is unusually sensitive to disasters, wars, migration policy, appropriations, donations, and government delivery choices.
- o: This is a bounded judgment, not an observed displacement rate.
- o: Information-only navigation and routine status updates are more substitutable than shelter, logistics, counseling, or field response.
- o: Mutual aid and government insourcing could displace a lens operator without eliminating the underlying service.

## Sources
- **S1** — [2022 NAICS definition: 624230 Emergency and Other Relief Services](https://www.census.gov/naics/?details=624230&input=624230&year=2022) (accessed 2026-07-22): Defines the industry as establishments providing food, shelter, clothing, medical relief, resettlement, and counseling to victims of domestic or international disasters or conflicts.
- **S2** — [O*NET OnLine: Emergency Management Directors](https://www.onetonline.org/link/details/11-9161.00) (accessed 2026-07-22): Documents planning, liaison, response coordination, status reporting, resource maintenance, damage assessment, training, facility inspection, regulatory review, needs surveys, and grant administration tasks.
- **S3** — [BLS Occupational Outlook Handbook: Emergency Management Directors](https://www.bls.gov/ooh/management/emergency-management-directors.htm) (accessed 2026-07-22): Describes the human coordination and leadership role and projects 3% employment growth from 2024 to 2034, while noting public-sector budget constraints.
- **S4** — [O*NET OnLine: Social and Human Service Assistants](https://www.onetonline.org/link/summary/21-1093.00) (accessed 2026-07-22): Provides an adjacent task profile for resettlement and counseling support, including interviews, records, referrals, safety monitoring, home visits, transport, and direct client assistance.
- **S5** — [U.S. Census Bureau: Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports overall business AI usage of 17% to 20% from December 2025 to May 2026 and documents adoption differences by firm size.
- **S6** — [FEMA EMI: The Role of Voluntary Organizations in Emergency Management](https://training.fema.gov/is/courseoverview.aspx?code=is-288.a&lang=en) (accessed 2026-07-22): States that voluntary agencies are critical from preparedness and mitigation through immediate response and long-term recovery and that government cannot meet all disaster needs without them.
- **S7** — [FEMA: Presidential Declaration Federal Cost Share](https://emilms.fema.gov/is_1000/groups/10.html) (accessed 2026-07-22): States that FEMA Public Assistance has a minimum federal share of 75% of eligible costs, with possible increases in specified circumstances.
- **S8** — [GAO: DHS Urgent Noncompetitive Contract Awards](https://www.gao.gov/products/gao-22-105074) (accessed 2026-07-22): Explains urgent-need exceptions and oversight requirements and reports that DHS urgent noncompetitive obligations rose from $75 million in FY 2016 to $1.3 billion in FY 2020.
- **S9** — [GAO: Disaster Assistance — Improving the Federal Approach](https://www.gao.gov/products/gao-25-108216) (accessed 2026-07-22): Reports 27 U.S. billion-dollar disasters in 2024 versus 14 in 2018, at least $448 billion of disaster-assistance appropriations over ten years, and more than 600 open major declarations.
- **S10** — [NOAA NCEI: Assessing the U.S. Climate in 2024](https://www.ncei.noaa.gov/news/national-climate-202413) (accessed 2026-07-22): Reports 27 billion-dollar weather and climate disasters in 2024, the second-highest annual count, and 190 such events over 2015-2024.
- **S11** — [IRS: Organizational Test for Internal Revenue Code Section 501(c)(3)](https://www.irs.gov/charities-non-profits/charitable-organizations/organizational-test-internal-revenue-code-section-501c3) (accessed 2026-07-22): Explains that charitable assets must remain permanently dedicated to exempt or public purposes, limiting conventional private transfer economics.
- **S12** — [Emergency Presidential Determination on Refugee Admissions for Fiscal Year 2026](https://www.govinfo.gov/content/pkg/DCPD-202600360/html/DCPD-202600360.htm) (accessed 2026-07-22): Raises the FY 2026 refugee-admissions ceiling from 7,500 to 17,500 and documents continuing policy restrictions and allocation priorities.
- **S13** — [FEMA National Incident Management System: National Qualification System](https://www.usfa.fema.gov/a-z/nims/national-qualification-system.html) (accessed 2026-07-22): Describes qualification, certification, and credentialing of deployable emergency personnel and the need for interoperable resource standards.
