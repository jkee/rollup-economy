# 562910 — Remediation Services

*v5.1 Stage 1 research memo. Run `562910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.81 · L 1.26 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can compress project administration and compliance work while regulated physical cleanup continues to require an accountable field operator.
**Weakness:** Most payroll is tied to physical, hazardous, site-specific execution, and public evidence does not isolate exact-industry implementation, contract economics, or transfer rates.

## Business-model lens
- Included: Lower-middle-market firms performing recurring or repeat outsourced cleanup of contaminated buildings, soil, groundwater, and mine sites; asbestos, lead, mold, and other toxic-material abatement; environmental emergency response; and integrated reclamation for external public- and private-sector customers.
- Excluded: Environmental consulting and remedial-plan design without cleanup execution, standalone excavation, ordinary janitorial or disaster-restoration work, waste collection or disposal facilities, captive internal crews, shells, non-control financing vehicles, and practices whose work is wholly episodic or inseparable from one individual.
- Customer and revenue model: Government agencies, industrial owners, property owners, developers, utilities, mines, and responsible parties purchase project-based cleanup, abatement, emergency response, monitoring, and long-term remedial operations through fixed-price, cost-reimbursement, time-and-materials, unit-price, and indefinite-delivery task-order contracts.
- Deviation from default lens: none

## Executive view
Remediation is a field-heavy, regulated service in which AI mainly improves the information and coordination layer rather than replacing cleanup crews. Durable contamination liabilities, funded public programs, and repeat industrial relationships support demand, while project concentration, safety exposure, bonding, and contract mix create wide variation in firm quality and value capture.

## How AI changes the work
AI can accelerate bid review, estimating support, scheduling, document search, daily reports, safety-plan drafting, regulatory cross-checks, change-order records, monitoring-data triage, and customer communication. It is far less able to replace containment construction, sampling, excavation, abatement, equipment operation, transport, emergency response, or accountable field supervision.

## Value capture
Operators retain more productivity benefit on well-scoped fixed-price and performance-oriented work and less on cost-reimbursement or time-and-materials contracts. Competitive task orders, rebids, transparent labor rates, validation duties, and unexpected site conditions can transfer or consume savings.

## Firm availability
The supplied LMM population is sizable and environmental-services M&A includes lower-market and remediation transactions. Only a subset will combine repeat customers, transferable licenses and supervisors, clean safety records, adequate bonding, disciplined project controls, and limited reliance on an owner or one major contract.

## Demand durability
Legacy contamination, responsible-party liability, Brownfields redevelopment, Superfund programs, industrial closures, and emerging contaminants create durable physical cleanup needs. Demand can still be lumpy because projects depend on appropriations, enforcement, property transactions, industrial investment, and site-specific technical milestones.

## Risks and uncertainty
The code spans building abatement, soil and groundwater work, emergency response, mine reclamation, and complex federal cleanup. Key risks include worker injury, environmental liability, bonding and insurance, waste-disposal dependence, fixed-price overruns, customer and project concentration, changing federal budgets, fragmented field data, and owner-dependent bidding relationships.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3746 | — | OBSERVED | — |
| n | — | 803 | — | ESTIMATE | — |
| a | 0.11 | 0.2 | 0.31 | PROXY | S2, S3 |
| rho | 0.23 | 0.42 | 0.62 | PROXY | S4, S5 |
| e | 0.4 | 0.6 | 0.76 | ESTIMATE | S1, S2, S6 |
| s5 | 0.07 | 0.16 | 0.28 | PROXY | S7 |
| q | 0.25 | 0.45 | 0.65 | ESTIMATE | S6 |
| d5 | 0.88 | 1.06 | 1.22 | PROXY | S8, S9, S10, S11 |
| o | 0.88 | 0.94 | 0.98 | ESTIMATE | S1, S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.38 | 1.26 | 2.88 | PROXY |
| F | 5.08 | 7.01 | 8.28 | ESTIMATE |
| C | 5.00 | 9.00 | 10.00 | ESTIMATE |
| D | 7.74 | 9.96 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation mix is published at NAICS 56291 and its underlying methodology is not fully exposed on the page.
- a: O*NET describes an occupation rather than measuring task time or AI substitutability inside remediation firms.
- a: The supplied compensation-to-receipts ratio combines nonmatching QCEW and SUSB vintages.
- rho: The surveys cover global construction organizations and conference-attending EHS professionals, not NAICS 562910 firms.
- rho: Stated investment plans and perceived value do not establish realized labor substitution.
- rho: Physical cleanup work cannot be implemented through generative AI alone.
- e: No public source measures the eligible share of LMM NAICS 562910 firms.
- e: Building abatement, emergency response, groundwater systems, mine reclamation, and federal cleanup have materially different recurrence and transferability.
- e: The frozen firm count is margin-bridged from size classes and may misclassify firms near the EBITDA band.
- s5: The transaction source is broad environmental services rather than six-digit remediation services.
- s5: Reported deal counts omit many undisclosed small transactions and do not provide an eligible-firm denominator.
- s5: The source's lower-middle-market deal-size definition is not the frozen EBITDA band.
- q: EPA confirms multiple contract types but does not publish a revenue-weighted mix for NAICS 562910.
- q: Private commercial and residential contract structures may differ materially from federal remediation procurement.
- q: Uncertain subsurface conditions and project liability can consume apparent productivity gains through rework or risk contingencies.
- d5: BLS publishes employment rather than constant-dollar output at broader NAICS 562900.
- d5: Federal program obligations are only part of demand and can be volatile across administrations and appropriations.
- d5: Emergency response, building abatement, mine reclamation, and long-term groundwater treatment follow different cycles.
- o: No source directly measures future operator-required quantity for remediation services.
- o: Automation potential varies between repetitive monitoring systems and irregular contaminated-site work.
- o: The estimate assumes environmental liability, certification, and on-site safety obligations remain material.

## Sources
- **S1** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Official definition and boundaries of NAICS 562910, including contaminated-building, mine-site, soil, groundwater, integrated reclamation, asbestos, lead, and toxic-material cleanup.
- **S2** — [Remediation Services Industry Profile](https://www.pellresearch.com/remediation-services) (accessed 2026-07-22): Published NAICS 56291 service categories, occupation distribution, and disclosed federal-contract activity.
- **S3** — [O*NET OnLine: Hazardous Materials Removal Workers](https://www.onetonline.org/link/details/47-4041.00) (accessed 2026-07-22): Task content covering containment, abatement, hazardous-material identification and preparation, equipment use, transport, safety compliance, recordkeeping, and information processing.
- **S4** — [RICS Artificial Intelligence in Construction Report 2025](https://www.rics.org/news-insights/artificial-intelligence-in-construction-report) (accessed 2026-07-22): Global construction survey evidence on current AI adoption, pilots, regular use, investment plans, skills shortages, and implementation barriers.
- **S5** — [Survey of AI Adoption and Investment in EHS](https://www.wolterskluwer.com/en/news/survey-from-wolters-kluwer-unveils-ai-adoption-and-investment-trends-in-ehs) (accessed 2026-07-22): 2025 survey evidence from EHS professionals on current AI use, planned investment, and the importance of data and skills.
- **S6** — [EPA Remedial Acquisition Framework](https://www.epa.gov/superfund/remedial-acquisition-framework) (accessed 2026-07-22): Remedial cleanup service scope, multi-year task-order procurement, and the use of fixed-price, cost-reimbursement, and time-and-materials contract types.
- **S7** — [Environmental Services M&A Update Q1 2025](https://rlhulett.com/app/uploads/2025/04/Environmental-Services-MA-Update-Q1-2025.pdf) (accessed 2026-07-22): PitchBook-based environmental-services deal volume, North American activity, lower-market deal mix, private-equity participation, and a disclosed thermal-remediation acquisition.
- **S8** — [EPA FY 2025 Brownfields Grant Selections](https://www.epa.gov/brownfields/applications-selected-fy-2025-brownfields-assessment-revolving-loan-fund-rlf-cleanup) (accessed 2026-07-22): More than $224 million across 214 Brownfields awards plus $42 million of supplemental revolving-loan funding for viable cleanup projects.
- **S9** — [Cleaning Up Superfund Sites: Infrastructure Investment Funding](https://www.epa.gov/infrastructure/cleaning-superfund-sites-highlights-infrastructure-investment-and-jobs-act-funding) (accessed 2026-07-22): $3.5 billion of Superfund remediation investment, roughly $3.3 billion available for extramural site work, and funding for a 49-site construction backlog.
- **S10** — [Superfund Remedial Annual Accomplishments Metrics FY 2025](https://www.epa.gov/superfund/superfund-remedial-annual-accomplishments-metrics-fiscal-year-2025) (accessed 2026-07-22): Current cleanup pipeline and FY 2025 obligations for pre-construction, construction, post-construction, and responsible-party work.
- **S11** — [BLS Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projected employment for broader NAICS 562900 rising from 185.9 thousand in 2024 to 198.7 thousand in 2034.
