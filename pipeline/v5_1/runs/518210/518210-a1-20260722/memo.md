# 518210 — Computing Infrastructure Providers, Data Processing, Web Hosting, and Related Services

*v5.1 Stage 1 research memo. Run `518210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 8.07 · L 3.72 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring mission-critical infrastructure demand combined with automatable technical and support workflows.
**Weakness:** Hyperscaler concentration and commodity repricing can redirect growth and pass operating savings to customers or upstream vendors.

## Business-model lens
- Included: Lower-middle-market providers of recurring or repeat outsourced computing infrastructure, data processing, managed and web hosting, cloud storage, backup, platform or application hosting, and technical streaming-support services for external customers.
- Excluded: Hyperscale or other firms outside the EBITDA band; captive enterprise data centers; shells; non-control financing vehicles; software publishers without hosting; custom programmers without hosting; telecommunications carriers; and payment, payroll, or financial-transaction processors classified elsewhere.
- Customer and revenue model: Business customers pay recurring subscriptions, reserved-capacity charges, usage-based compute, storage, or bandwidth fees, and managed-service fees, commonly with service-level commitments. Revenue can combine contracted recurring fees with variable consumption.
- Deviation from default lens: none

## Executive view
The eligible core is a recurring, mission-critical outsourced-service industry with meaningful automatable technical and administrative work. Its favorable demand backdrop is tempered by hyperscaler concentration, capital and energy intensity, embedded automation, and wide variation between commodity hosting, colocation, managed infrastructure, and data processing.

## How AI changes the work
AI can reduce avoidable hiring in software maintenance, testing, documentation, monitoring triage, routine troubleshooting, customer support, reporting, and back-office work. Production conversion should be material but not complete because uptime, security, change control, incident accountability, and physical infrastructure remain human-supervised.

## Value capture
Recurring and fixed-fee managed contracts can let operators retain savings between renewals, especially when automation improves service without reducing billed capacity. Competitive repricing, usage-based billing, customer procurement, and upstream energy, hardware, licensing, or cloud costs will share or absorb part of the benefit.

## Firm availability
The NAICS activity definition fits outsourced recurring service well, but the code is heterogeneous and the provided firm count rests on an old estimated margin bridge. Founder dependence, customer concentration, supplier dependence, and asset intensity determine whether a nominal firm is truly transferable.

## Demand durability
Computing, storage, processing, and hosted workloads should expand, and core services remain operator-required despite self-service interfaces. The strongest growth may accrue to hyperscalers and new AI capacity rather than the current lower-middle-market service basket, so the demand range is deliberately far below the electricity forecast's raw growth.

## Risks and uncertainty
The largest risks are hyperscaler disintermediation, commodity price erosion, customer concentration, cybersecurity and outage liability, power availability and cost, hardware and software vendor dependence, rapid obsolescence, capital requirements, and a labor input based on a 2001 margin-bridged estimate. Direct evidence on eligible firms, realized transactions, production AI labor savings, and same-service demand cohorts is missing.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3086 | — | OBSERVED | — |
| n | — | 2001 | — | ESTIMATE | — |
| a | 0.28 | 0.45 | 0.62 | PROXY | S2, S3, S4 |
| rho | 0.45 | 0.67 | 0.82 | PROXY | S5 |
| e | 0.55 | 0.72 | 0.86 | ESTIMATE | S1 |
| s5 | 0.07 | 0.14 | 0.22 | PROXY | S7 |
| q | 0.35 | 0.58 | 0.75 | ESTIMATE | — |
| d5 | 1.05 | 1.35 | 1.75 | PROXY | S6 |
| o | 0.72 | 0.86 | 0.95 | PROXY | S1, S3, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.56 | 3.72 | 6.28 | PROXY |
| F | 7.01 | 8.54 | 9.55 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.56 | 10.00 | 10.00 | PROXY |

## Caveats
- a: Occupation employment is available at NAICS 518000 rather than as a separately labeled 518210 table.
- a: O*NET task lists describe occupations nationally, not the task frequencies or automation baselines inside lower-middle-market providers.
- a: The frozen compensation-to-receipts input is an estimated 2001 margin-bridged Information Services ratio and may not represent the current asset and labor mix.
- rho: BTOS covers the broad Information sector and asks about business AI use, not labor-hour implementation intensity.
- rho: Adoption can mean limited experimentation rather than production deployment across exposed workflows.
- e: No source directly measures the eligible share within the normalized EBITDA band.
- e: The code combines asset-heavy colocation and infrastructure with managed hosting and data processing, which can have different financial profiles.
- s5: The owner survey is not industry-specific and measures plans rather than completed transactions.
- s5: No observed denominator of eligible lower-middle-market 518210 firms was available.
- q: No source directly measures retained AI benefits in this industry.
- q: Retention differs sharply between fixed managed-service contracts and transparent usage-based resale or cost-plus arrangements.
- d5: DOE's forecast ends in 2028 and measures electricity rather than service quantity.
- d5: AI workloads, power intensity, efficiency, and hyperscaler share make the bridge unusually uncertain.
- o: NIST defines cloud characteristics but does not measure provider displacement.
- o: Operator need varies between commodity web hosting, colocation, managed infrastructure, and high-touch data processing.

## Sources
- **S1** — [2022 NAICS Manual: 518210 Computing Infrastructure Providers, Data Processing, Web Hosting, and Related Services](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Industry scope, included service examples, and exclusions used for the lens and operator-need assessment.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 518000](https://www.bls.gov/oes/2023/may/naics3_518000.htm) (accessed 2026-07-22): Employment and occupation shares for computing infrastructure providers, data processing, web hosting, and related services.
- **S3** — [O*NET OnLine: Network and Computer Systems Administrators](https://www.onetonline.org/link/summary/15-1244.00) (accessed 2026-07-22): Tasks involving monitoring, troubleshooting, backups, security, networks, servers, logs, requirements, and vendor coordination.
- **S4** — [O*NET OnLine: Software Developers](https://www.onetonline.org/link/summary/15-1252.00) (accessed 2026-07-22): Tasks involving requirements analysis, development, testing, documentation, modification, performance standards, and technical coordination.
- **S5** — [Census Bureau: Nearly 1 in 5 U.S. Businesses Use Artificial Intelligence](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): May 2026 AI-use prevalence and near-term expectations for the Information sector and employer businesses.
- **S6** — [Department of Energy Releases New Report Evaluating Increase in Electricity Demand from Data Centers](https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers) (accessed 2026-07-22): Historical and projected US data-center electricity consumption used as a directional demand proxy.
- **S7** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year owner intentions to sell or transfer employer businesses, used as a succession proxy.
- **S8** — [NIST Computer Security Resource Center Glossary: Cloud Computing](https://csrc.nist.gov/glossary/term/cloud_computing) (accessed 2026-07-22): Definition of on-demand self-service access to shared configurable computing resources with minimal provider interaction.
