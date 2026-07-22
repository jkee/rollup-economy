# 238290 — Other Building Equipment Contractors

*v5.1 Stage 1 research memo. Run `238290-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.71 · L 1.87 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A safety-critical installed equipment base creates repeat workflows where AI can increase office and technician throughput without eliminating the accountable field operator.
**Weakness:** The broad NAICS code obscures how much of the LMM firm population actually has transferable recurring service revenue rather than cyclical project work.

## Business-model lens
- Included: U.S. lower-middle-market contractors in NAICS 238290 that repeatedly install, inspect, maintain, repair, modernize, or rig building and industrial equipment for external customers, including elevators and escalators, commercial doors, conveyors, millwright work, and related equipment services.
- Excluded: Shells, captive internal maintenance units, non-control financing vehicles, equipment manufacturers without a contracted service operation, and contractors whose work is only a one-off project with no repeat outsourced customer relationship.
- Customer and revenue model: Commercial, institutional, industrial, government, and multifamily customers buy project installation or modernization, recurring preventive-maintenance agreements, inspections, emergency callouts, and time-and-materials repairs. Fixed monthly service fees and contract escalators coexist with competitively bid projects and separately billed extra work.
- Deviation from default lens: none

## Executive view
The opportunity is concentrated in workflow-heavy support around a physical service operation, not in replacing field trades. Repeat maintenance, repair, inspection, modernization, and emergency obligations support durable customer need, while NAICS heterogeneity and uneven recurring-revenue quality require firm-level screening. The frozen labor ratio is low quality and the frozen LMM firm count is estimated, so both should be validated before underwriting.

## How AI changes the work
AI can compress bid intake, estimating support, scope comparison, scheduling, dispatch, parts lookup, service-record drafting, customer messaging, invoicing, collections, safety-document preparation, and technician knowledge retrieval. Physical installation, inspection, troubleshooting, rigging, component replacement, and final safety accountability remain bottlenecks, so gains are more likely to appear as avoided office hiring and higher technician utilization than wholesale technician substitution.

## Value capture
Fixed monthly maintenance fees, annual escalators, project pricing, and separately billed extra work allow some benefit to remain with the operator before renewal. Capture erodes as contracts reprice, customers negotiate, and competitors bid from similar tools; transparent hourly and cost-plus work is especially susceptible to sharing. Contract duration, proprietary-equipment access, response performance, and customer retention are therefore central diligence items.

## Firm availability
Employer-owner succession evidence points to meaningful five-year transfer intent, and construction businesses are visibly bought and sold. However, a qualifying transfer depends on a transferable technician bench, licenses, bonding, documented customer contracts, vendor and OEM access, and low owner dependence. Project-only insulation and rigging shops should not be treated like maintenance-route businesses merely because they share the NAICS code.

## Demand durability
Regular maintenance, code compliance, emergency response, equipment wear, accessibility needs, and modernization of aging controls sustain the core service basket. New-installation and industrial-project work remain cyclical, but the installed base and physical safety obligations make full software displacement unlikely within five years.

## Risks and uncertainty
The largest uncertainty is mix: NAICS 238290 combines attractive contracted service with one-off installation, insulation, dismantling, and rigging. Other risks include OEM proprietary systems, union or licensed-labor constraints, technician scarcity, customer concentration, public bidding, weak field data, cybersecurity of connected equipment, safety liability, and savings being competed away. Firm-level contract and workflow evidence could move the primitives materially in either direction.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3774 | — | ESTIMATE | — |
| n | — | 191 | — | ESTIMATE | — |
| a | 0.13 | 0.2 | 0.29 | PROXY | S2, S3, S4 |
| rho | 0.42 | 0.62 | 0.78 | PROXY | S5, S6 |
| e | 0.4 | 0.58 | 0.72 | PROXY | S1, S2, S8 |
| s5 | 0.15 | 0.22 | 0.3 | PROXY | S7, S11 |
| q | 0.48 | 0.64 | 0.78 | PROXY | S8, S9, S10 |
| d5 | 0.98 | 1.05 | 1.14 | PROXY | S3, S8 |
| o | 0.86 | 0.93 | 0.98 | PROXY | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.82 | 1.87 | 3.41 | ESTIMATE |
| F | 4.06 | 5.20 | 6.02 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | PROXY |
| D | 8.43 | 9.77 | 10.00 | PROXY |

## Caveats
- a: The latest directly reachable six-digit BLS occupation table is May 2023 and excludes self-employed workers.
- a: The OpenAI exposure study covers the U.S. workforce broadly and measures technical task exposure, not realized labor removal in this industry.
- a: The frozen compensation-to-receipts input is low quality, uses ancestor 23829 data, and mixes 2024 wages with 2022 receipts; it does not alter this task-share estimate but weakens later translation into economics.
- rho: BTOS is sector-wide, not NAICS 238290, and its 2023-2024 question captured use to produce goods and services rather than every internal workflow.
- rho: The AGC evidence is investment intent from substantially larger contractors, not implemented benefit among the target firms.
- rho: Implementation is likely faster in office workflows than in technician diagnosis or safety-relevant decisions.
- e: NAICS 238290 is unusually heterogeneous and establishment classifications do not disclose each firm's recurring-revenue mix.
- e: Otis is far larger and more elevator-focused than the target population and includes international revenue.
- e: The frozen firm count is itself an estimate margin-bridged from size-class receipts and a broad Engineering/Construction EBITDA margin; the estimate here does not re-estimate that count.
- s5: Gallup measures stated plans rather than completed transactions and is not specific to construction, NAICS 238290, or the EBITDA band.
- s5: Gallup respondents could select more than one plan, so component percentages are not additive; the reported 22% summary is used directly.
- s5: BizBuySell's construction sample is self-reported and mostly smaller than the $1 million-$10 million EBITDA lens.
- q: The airport agreement is one large public contract from 2017 and may not represent private or smaller-customer terms.
- q: KONE and Otis are global OEMs with brand, installed-base, and proprietary-equipment advantages that independents may not share.
- q: No source directly observes retention of AI-created gross benefit, so the discount path is judgmental.
- d5: The BLS projection covers one important occupation, not the entire heterogeneous NAICS service basket.
- d5: Otis is global, elevator-specific, and reports sales and portfolio growth rather than constant-quality U.S. service quantity.
- d5: New construction and industrial capital spending can make project portions of demand substantially more cyclical than maintenance.
- o: Elevator duties and licensing are not representative of every commercial-door, conveyor, insulation, and rigging activity in NAICS 238290.
- o: Rapid remote-diagnostics adoption could reduce routine site quantity faster than current occupational descriptions imply.
- o: The estimate concerns accountable operator requirement, not whether each task remains manually performed.

## Sources
- **S1** — [NAICS 238290 Other Building Equipment Contractors definition](https://www.census.gov/naics/?details=238290&input=238290&year=2012) (accessed 2026-07-22): Defines the industry as establishments installing or servicing building equipment and expressly includes maintenance and repairs, while listing heterogeneous activities such as elevators, commercial doors, conveyors, insulation, machine rigging, and millwright work.
- **S2** — [May 2023 OEWS Industry-Specific Estimates: NAICS 238290](https://www.bls.gov/oes/2023/may/naics5_238290.htm) (accessed 2026-07-22): Reports 153,170 jobs and the exact industry occupation mix and wages, including 46.22% construction and extraction, 21.05% installation/maintenance/repair, 9.48% office support, 6.55% management, and 5.09% business and financial operations.
- **S3** — [Occupational Outlook Handbook: Elevator and Escalator Installers and Repairers](https://www.bls.gov/ooh/construction-and-extraction/elevator-installers-and-repairers.htm) (accessed 2026-07-22): Describes physical, technical, recordkeeping, preventive-maintenance, inspection, and emergency-repair duties; states most states require licensing; and projects 5% employment growth from 2024 to 2034, supported by maintenance, updating old equipment, accessibility, and sophisticated controls.
- **S4** — [GPTs are GPTs: An early look at the labor market impact potential of large language models](https://openai.com/index/gpts-are-gpts/) (accessed 2026-07-22): Provides broad U.S. task-exposure evidence: about 80% of workers could have at least 10% of tasks affected and about 19% could have at least 50% affected, used only as a cross-occupation technical-exposure proxy.
- **S5** — [Tracking Firm Use of AI in Real Time: A Snapshot from the Business Trends and Outlook Survey](https://www.census.gov/hfp/btos/downloads/CES-WP-24-16.pdf) (accessed 2026-07-22): Reports nationally representative business AI use rising from 3.7% to 5.4% from September 2023 to February 2024 and construction at 1.4%, with only 1.9% of construction workers at firms using AI.
- **S6** — [AGC 2025 Construction Outlook: Firms with $50 Million to $500 Million in Revenue](https://www.agc.org/sites/default/files/users/user21902/2025_Outlook_50M%20to%20500M_FINAL.pdf) (accessed 2026-07-22): Among 325 respondents, 54% expected increased AI investment in 2025, alongside planned increases in document management, project management, accounting, estimating, CRM, scheduling, and service-management software.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 52.3% of U.S. employer businesses are owned by people age 55 or older and 22% of employer-business owners planned to sell, transfer ownership, or go public within five years.
- **S8** — [Otis Worldwide Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1781335/000178133526000011/otis-20251231.htm) (accessed 2026-07-22): Reports Service at 65% of 2025 sales and 91% of segment profit; approximately 2.5 million units in the global maintenance portfolio; 5% Service organic sales growth; maintenance pricing and productivity benefits; and 2025 revenue split among new equipment, maintenance and repair, and modernization.
- **S9** — [Hillsborough County Aviation Authority Elevator, Escalator, Moving Walkway and Dumbwaiter Maintenance Contract](https://www.tampaairport.com/sites/default/files/Maintenance%20Contract%20for%20Schindler%20Electric%20Corp%2C%20Escalators%20and%20Moving%20Sidewalks.pdf) (accessed 2026-07-22): Shows a U.S. public maintenance contract paid in equal monthly installments, adjusted by a 3.5% annual price increase, with extra work and emergency callbacks billed under separate labor rates and response obligations.
- **S10** — [KONE as an investment](https://www.kone.com/global/en/investors/kone-as-an-investment.html) (accessed 2026-07-22): States that Service provides a stable recurring revenue base driven by safety, reliability, and long customer relationships, with approximately 90% annual retention; also distinguishes more cyclical new-building and modernization work.
- **S11** — [Construction Business Valuation Multiples and Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/building-construction/) (accessed 2026-07-22): Reports 3,142 sold construction listings analyzed for 2021-2025, median 207 days on market, median $750,000 sale price, $1.51 million revenue, $323,174 owner earnings, and stable transaction multiples, demonstrating an observable but smaller-company construction transfer market.
