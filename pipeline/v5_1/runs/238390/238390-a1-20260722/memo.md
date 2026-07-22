# 238390 — Other Building Finishing Contractors

*v5.1 Stage 1 research memo. Run `238390-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.27 · L 1.81 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A repeat-service contractor can apply AI to a meaningful administrative and coordination layer while preserving the site-specific operator role.
**Weakness:** Industry heterogeneity and the absence of six-digit evidence on repeat revenue and transferable control events make eligible-firm availability highly uncertain.

## Business-model lens
- Included: US lower-middle-market contractors providing repeat or recurring outsourced building-finishing work to external customers, especially commercial waterproofing, concrete coating or sealing, modular furniture and exhibit installation, and recurring shade, blind, fixture, and space-reconfiguration installation.
- Excluded: One-off-only new-construction or residential installation businesses without a repeat customer base, captive internal installation units, manufacturers whose primary economics are product sales, shells, and non-control financing vehicles.
- Customer and revenue model: Project and work-order revenue from property owners, facilities managers, general contractors, dealers, exhibitors, and commercial tenants; eligible firms earn repeat demand through maintenance, renovation cycles, multi-site programs, reconfigurations, or recurring events, commonly under competitively bid fixed-price or unit-price scopes.
- Deviation from default lens: The code combines waterproofing and coating maintenance, modular-office and trade-show installation, and several one-time residential or construction installation activities. To keep one coherent screen, the lens retains only firms with demonstrable repeat commercial, maintenance, multi-site, or recurring-event demand and excludes one-off-only installers.

## Executive view
Other building finishing is a mixed collection of locally delivered physical services. The clearest AI opportunity is in the coordination layer around field work, while the clearest strategic constraint is that only part of the code has repeat commercial or maintenance demand and transferable operations independent of the owner.

## How AI changes the work
AI can draft scopes and proposals, extract requirements, assist takeoffs and estimates, schedule crews, answer routine customer questions, organize field documentation, flag job-cost variance, and accelerate invoicing. It is much less able to replace substrate assessment, site access, physical preparation and installation, safety decisions, inspection, rework, or accountable sign-off.

## Value capture
Fixed-price work can preserve early productivity gains inside the contractor, especially between bid and completion. Over repeated bids and renewals, customers and competitors are likely to capture part of the benefit through sharper pricing, faster turnaround, or higher service expectations, so retention should be meaningful but incomplete.

## Firm availability
There is an active market for construction-business transfers, but the qualifying event rate is uncertain and published marketplace data lack a population denominator. The best targets are firms with repeat accounts, delegated estimating and supervision, credible job-cost records, transferable licenses or qualifying personnel, and limited dependence on the seller's personal relationships.

## Demand durability
Real demand is likely to be broadly stable over five years but uneven by niche and end market. Renovation, repair, waterproofing, facility reconfiguration, health care, recreation, and selected growth construction can offset weakness in traditional offices or rate-sensitive residential work; most delivered quantity should still require an on-site operator.

## Risks and uncertainty
The six-digit code hides materially different business models, and no public source provides its exact occupation mix, recurring-revenue share, AI pass-through, or transfer hazard. Cyclicality, bid competition, owner dependence, customer concentration, bonding or licensing, rework, warranty claims, and weak field data can erase benefits. A portfolio tilted toward one-off new construction would be materially less coherent than the narrowed lens.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3901 | — | ESTIMATE | — |
| n | — | 116 | — | ESTIMATE | — |
| a | 0.1 | 0.2 | 0.3 | PROXY | S2, S3, S5 |
| rho | 0.35 | 0.58 | 0.75 | PROXY | S4 |
| e | 0.35 | 0.58 | 0.78 | ESTIMATE | S1 |
| s5 | 0.08 | 0.15 | 0.25 | PROXY | S7, S8 |
| q | 0.4 | 0.58 | 0.72 | ESTIMATE | S6 |
| d5 | 0.86 | 1.01 | 1.16 | PROXY | S9, S10 |
| o | 0.86 | 0.93 | 0.98 | PROXY | S1, S3, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.55 | 1.81 | 3.51 | ESTIMATE |
| F | 2.33 | 3.87 | 5.09 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.40 | 9.39 | 10.00 | PROXY |

## Caveats
- a: OEWS publishes the useful occupation mix at parent 238300 rather than the exact six-digit code.
- a: The Microsoft applicability measure is based on Copilot conversations and is not a measure of substitution or avoided hiring.
- a: The frozen compensation ratio is LOW quality, measured at ancestor 23839, uses 2024 wages over 2022 receipts, and is harmonized to the IPS basis; this primitive does not revise it.
- rho: Survey deployment percentages do not measure workflow depth, realized labor savings, or persistence.
- rho: General-contractor respondents may have more formal preconstruction and IT functions than small finishing contractors.
- e: NAICS classifies establishments by primary activity, not by recurrence, customer concentration, or revenue model.
- e: The frozen LMM firm count of 116 is an ESTIMATE margin-bridged from size-class counts and average receipts; this primitive does not revise it.
- s5: BizBuySell data are voluntarily reported and mainly represent smaller marketed businesses, not the full LMM population.
- s5: The sold-listing total spans building and construction broadly and does not provide an annual hazard rate.
- s5: ABS owner age is evidence of an observable succession indicator, not evidence that an owner will sell.
- q: No source measures AI-benefit pass-through for 238390.
- q: Contract mix varies across residential, commercial subcontract, service-call, dealer, and event work; cost-plus scopes retain less benefit than fixed-price scopes.
- d5: AIA covers nonresidential buildings and is nominal, while 238390 also serves residential and recurring event markets.
- d5: BLS occupational growth covers construction laborers and helpers across industries, not output of this industry.
- d5: The code's service mix is too broad for a single end-market forecast to represent every firm.
- o: The 91% outdoor-work statistic is for the broad construction and extraction occupational group, and some included finishing work is indoors.
- o: Operator requirement differs sharply between waterproofing, recurring exhibits, modular furniture, and simple fixture installation.

## Sources
- **S1** — [2022 NAICS Definition: 238390 Other Building Finishing Contractors](https://www.census.gov/naics/?details=238390&input=238390&year=2022) (accessed 2026-07-22): Defines the industry's included and excluded finishing activities and states that work may include new work, additions, alterations, maintenance, and repairs.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Lists the largest occupations in parent 238300 Building Finishing Contractors, led by field trades and labor and also including supervisors, general and operations managers, and office clerks.
- **S3** — [Occupational Requirements in the United States, 2024](https://www.bls.gov/news.release/archives/ors_11192024.htm) (accessed 2026-07-22): Reports physical and environmental job requirements, including outdoor exposure for 91.0% of construction and extraction workers.
- **S4** — [2026 Construction Industry Outlook](https://www.sage.com/en-us/blog/2026-construction-industry-outlook/) (accessed 2026-07-22): Reports AGC-Sage construction survey findings that 45% of firms deploy AI in office and administrative functions, 23% in estimating, and 20% in design or preconstruction.
- **S5** — [Working with AI: Measuring the Applicability of Generative AI to Occupations](https://www.microsoft.com/en-us/research/publication/working-with-ai-measuring-the-occupational-implications-of-generative-ai/) (accessed 2026-07-22): Analyzes 200,000 Copilot conversations and finds the strongest AI applicability in knowledge, office and administrative, sales, information-gathering, writing, teaching, and advising activities.
- **S6** — [Four Types of Construction Contracts You Need to Understand](https://learn.aiacontracts.com/articles/four-types-of-construction-contracts-you-need-to-understand/) (accessed 2026-07-22): States that stipulated-sum, lump-sum, or fixed-price contracting is the most common agreement form between an owner and contractor.
- **S7** — [Construction Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/building-construction/) (accessed 2026-07-22): Reports 3,142 sold building-and-construction listings in its benchmark data and a 207-day median time on market, documenting an active but selected transfer channel.
- **S8** — [2024 Annual Business Survey: Characteristics of Business Owners](https://www.census.gov/data/tables/2024/econ/abs/2024-abs-characteristics-of-owners.html) (accessed 2026-07-22): Confirms that the 2024 ABS covers reference year 2023 and provides an Age of Owner table for employer businesses.
- **S9** — [July 2026 Consensus Construction Forecast](https://www.aia.org/resource-center/july-2026-consensus-construction-forecast) (accessed 2026-07-22): Forecasts nominal nonresidential building spending down 0.3% in 2026 and up 3.0% in 2027, with substantial divergence across end markets.
- **S10** — [Construction Laborers and Helpers: Occupational Outlook Handbook](https://www.bls.gov/ooh/construction-and-extraction/construction-laborers-and-helpers.htm) (accessed 2026-07-22): Projects 7% employment growth from 2024 to 2034, links demand to construction and renovation, and notes that prefabricated components can reduce demand for some helpers.
