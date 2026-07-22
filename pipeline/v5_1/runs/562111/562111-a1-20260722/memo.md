# 562111 — Solid Waste Collection

*v5.1 Stage 1 research memo. Run `562111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.31 · L 1.08 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Dense recurring routes, durable external demand, contract or subscription revenue, and demonstrated tuck-in acquisition activity support a coherent consolidation thesis with targeted administrative AI gains.
**Weakness:** Most work and customer value remain tied to physical route execution, fleet assets, safety, and disposal access, sharply limiting the share of economics that AI labor substitution can reach.

## Business-model lens
- Included: US lower-middle-market firms providing recurring or repeat local collection and hauling of nonhazardous solid waste or mixed recyclables, plus nonhazardous transfer-station operations sold to external residential, commercial, industrial, institutional, or municipal customers.
- Excluded: Hazardous waste collection, brush and rubble removal, long-distance waste trucking, materials recovery facilities, waste consulting, captive municipal departments, combined collection-and-disposal businesses classified outside NAICS 562111, shells, non-control financing vehicles, and firms outside the target EBITDA band.
- Customer and revenue model: Residential subscriptions, commercial and industrial service agreements, municipal contracts, scheduled route charges, container and frequency-based fees, and repeat transfer-station tipping fees paid by external customers.
- Deviation from default lens: none

## Executive view
Solid waste collection combines highly recurring, essential local service with active consolidation, but its operating core is trucks, routes, equipment, and field labor rather than information work. AI can improve the administrative and coordination layer; it is unlikely to transform most direct collection work within five years.

## How AI changes the work
The clearest uses are customer intake, billing and complaint workflows, dispatch assistance, dynamic route changes, work-order preparation, driver-document processing, maintenance triage, safety-event review, and management reporting. The dominant collector and driver roles remain physical, exposed to weather and safety constraints, and only partly addressable through information assistance.

## Value capture
Residential subscriptions and multi-period commercial or municipal agreements create time to retain productivity gains, especially in dense routes with reliable service. Capture erodes at renewal, during municipal rebids, and where customers can compare several capable haulers or demand sharing of observable efficiencies.

## Firm availability
The code contains many externally facing route businesses that fit recurring-service economics, and public-company filings show continuing tuck-in acquisitions. Availability is tempered by strong strategic-buyer competition, route-density logic that makes adjacency valuable to incumbents, and the possibility that attractive independents sell at prices reflecting synergies unavailable to a new platform.

## Demand durability
Households and businesses continue to generate waste that must be collected and hauled, supporting stable operator-required demand. Real growth should be modest; diversion, recycling rules, onsite compaction, packaging changes, and local economic conditions can alter volume, route frequency, and service mix without eliminating the need for collection.

## Risks and uncertainty
The main uncertainties are the absence of six-digit occupation and real-output measures, the share of database firms that are genuinely independent recurring-service LMM operations, and the gap between succession intentions and closed control deals. Operational risks include vehicle capital intensity, fuel and disposal costs, insurance, worker safety, driver availability, municipal rebids, environmental rules, and integration failures. The injected compensation-to-receipts ratio may also understate the strategic importance of labor that controls route reliability and safety even when direct payroll is not the largest cost pool.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2156 | — | OBSERVED | — |
| n | — | 1140 | — | ESTIMATE | — |
| a | 0.14 | 0.24 | 0.35 | PROXY | S2, S3, S4, S5 |
| rho | 0.34 | 0.52 | 0.7 | PROXY | S4, S5, S6 |
| e | 0.76 | 0.87 | 0.95 | ESTIMATE | S1, S8 |
| s5 | 0.09 | 0.16 | 0.24 | PROXY | S7, S8 |
| q | 0.43 | 0.59 | 0.74 | ESTIMATE | S8 |
| d5 | 0.99 | 1.08 | 1.15 | PROXY | S1, S9 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S3, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.41 | 1.08 | 2.11 | PROXY |
| F | 7.03 | 8.16 | 8.95 | ESTIMATE |
| C | 8.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.91 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation mix is for four-digit Waste Collection and includes adjacent waste-collection activities.
- a: O*NET describes occupations across industries and does not measure AI substitution or avoidable hiring.
- a: The range is task judgment rather than an observed wage-weighted exposure statistic.
- rho: The Census measure is economy-wide and counts use that may not avoid labor.
- rho: Vendor adoption claims may conflate conventional optimization or automation with AI.
- rho: Implementation varies sharply with route-software maturity, fleet telemetry, and local management quality.
- e: No source measures the eligible share within the target EBITDA band.
- e: Business databases can assign NAICS from self-reports or primary-revenue judgments that obscure integrated operations.
- e: The dataset firm-count estimate may include entities without transferable standalone operations.
- s5: Gallup covers employer businesses across industries and measures plans, not completed qualifying deals.
- s5: A public consolidator's acquisitions are evidence of buyer demand, not a denominator-based transfer rate.
- s5: Strategic buyers may outbid financial or independent operators for route-dense assets.
- q: No source directly measures retention of AI-enabled gross benefit.
- q: Customer and contract mix varies materially across local markets.
- q: Municipal rebids and aggressive strategic competitors can transfer savings to customers.
- d5: The BLS output projection is available only for the broader parent industry.
- d5: Constant-quality demand is not the same as tonnage because route frequency, container size, and service mix can change.
- d5: Local population, regulation, and commercial activity create wide geographic dispersion.
- o: There is no direct measurement of operator-required quantity for the lens.
- o: Automation may reduce crew size without reducing the operator-required service quantity measured here.
- o: Municipal insourcing and integrated disposal providers can displace lens firms even when physical collection demand persists.

## Sources
- **S1** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines NAICS 562111 as local nonhazardous solid-waste or mixed-recyclable collection and hauling plus nonhazardous transfer stations, and identifies adjacent excluded activities.
- **S2** — [Waste Collection: May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_562100.htm) (accessed 2026-07-22): Provides the four-digit occupation and wage mix: transportation and material-moving roles are 67.93 percent of employment, office support is 10.94 percent, and management is 4.54 percent.
- **S3** — [O*NET OnLine: Refuse and Recyclable Material Collectors](https://www.onetonline.org/link/details/53-7081.00) (accessed 2026-07-22): Describes core collection work including truck inspection, route driving, dumping, hoist and compactor operation, mounting and dismounting vehicles, exception communication, and weather checks.
- **S4** — [O*NET OnLine: Dispatchers, Except Police, Fire, and Ambulance](https://www.onetonline.org/link/details/43-5032.00) (accessed 2026-07-22): Describes dispatch scheduling, daily run preparation, customer problem handling, work-order relay and preparation, and reporting tasks that are candidates for AI assistance.
- **S5** — [O*NET OnLine: Customer Service Representatives](https://www.onetonline.org/link/details/43-4051.00) (accessed 2026-07-22): Describes customer inquiries, orders, complaints, interaction records, billing, account changes, and grievance routing that inform exposed administrative tasks.
- **S6** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports nationally representative recent business AI adoption near one-fifth overall, higher adoption among larger firms, and measurement across functions including customer service, finance, human resources, and information technology.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of employer-business owners planned to sell or transfer ownership within five years, providing a broad succession-intention proxy.
- **S8** — [Casella Waste Systems, Inc. 2025 Annual Report on Form 10-K](https://www.sec.gov/Archives/edgar/data/911177/000091117726000008/cwst-20251231.htm) (accessed 2026-07-22): Documents residential subscriptions, commercial and industrial service agreements, municipal contracts and rebids, competition, pricing drivers, and nine completed acquisitions including multiple collection tuck-ins.
- **S9** — [BLS Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects 1.6 percent annual constant-price output growth for Waste Management and Remediation Services and positive employment growth for four-digit Waste Collection.
