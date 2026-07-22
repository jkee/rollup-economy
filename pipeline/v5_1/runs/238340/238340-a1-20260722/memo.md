# 238340 — Tile and Terrazzo Contractors

*v5.1 Stage 1 research memo. Run `238340-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.97 · L 0.66 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeatable estimating and coordination workflows can be improved while the underlying site-installed service remains difficult to displace.
**Weakness:** Most wage dollars are tied to physical craft labor, and the pool of transferable firms with clean systems and low owner dependence may be small.

## Business-model lens
- Included: US lower-middle-market contractors installing ceramic tile, interior stone, mosaic, and job-site terrazzo for external residential and commercial customers, including new construction, renovation, maintenance, and repair work supported by repeat relationships with general contractors, builders, designers, property operators, or recurring customers.
- Excluded: Exterior stone masonry, resilient-flooring installation, retail sale-and-install operations classified outside this NAICS, precast-terrazzo manufacturing, captive internal crews, shells, non-control financing vehicles, and firms without a repeatable outsourced-service customer base.
- Customer and revenue model: Project revenue from property owners and, frequently, subcontract work for general contractors or builders; jobs are commonly bid from plans, measurements, labor, and material requirements, with repeat business driven by trade relationships rather than subscription contracts.
- Deviation from default lens: none

## Executive view
Tile and terrazzo contracting remains a site-bound skilled trade with a modest but practical AI opportunity in the information layer around each job. The operating case depends on standardizing estimating, scheduling, procurement, documentation, and customer workflows across repeat contractor relationships while protecting field quality and local reputation.

## How AI changes the work
AI can assist plan reading, quantity takeoffs, bid and change-order drafting, schedule coordination, purchasing follow-up, customer communications, invoicing, and knowledge retrieval. It is not a credible substitute for the core work of preparing uneven sites, selecting and cutting material, laying patterns, setting tile, grouting, finishing, and accepting installation liability.

## Value capture
Awarded fixed-price jobs can retain cost savings until completion, especially when faster estimating raises throughput or better coordination prevents rework. Benefits are progressively shared through competitive bids and negotiated repeat work; cost-plus and hourly arrangements expose savings sooner. Quality, schedule reliability, and responsiveness may preserve more value than a pure labor-cost reduction.

## Firm availability
The broader construction succession surveys indicate substantial owner exit intent, but planned exits are not equivalent to completed control transfers. A viable buyer pool should focus on firms with durable general-contractor or builder relationships, documented estimating and project controls, a foreman layer, clean financials, and limited dependence on the selling owner's craft or sales relationships.

## Demand durability
Tile and stone remain common in bathrooms, restaurants, and other buildings, with renovation and new construction supporting the service. The work is physically embedded in customer sites and failures create visible quality and water-intrusion consequences, preserving the need for an accountable operator even as the office layer becomes more automated.

## Risks and uncertainty
The main risks are housing and renovation cyclicality, strong local price competition, installer scarcity, rework and warranty exposure, fragmented project data, and owner dependence. Evidence is weakest at the six-digit industry level: occupation mix comes from a parent industry, succession surveys cover broad construction populations, and no source directly measures AI task savings or commercial pass-through for tile contractors.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.29 | — | ESTIMATE | — |
| n | — | 39 | — | ESTIMATE | — |
| a | 0.09 | 0.15 | 0.23 | PROXY | S2, S3 |
| rho | 0.22 | 0.38 | 0.58 | ESTIMATE | S3, S4, S5 |
| e | 0.5 | 0.72 | 0.88 | ESTIMATE | S1, S8 |
| s5 | 0.12 | 0.23 | 0.34 | PROXY | S6, S7, S8 |
| q | 0.38 | 0.6 | 0.78 | ESTIMATE | S8, S10 |
| d5 | 0.97 | 1.05 | 1.1 | PROXY | S9 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S3, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.23 | 0.66 | 1.55 | ESTIMATE |
| F | 1.94 | 3.23 | 4.08 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.73 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS publishes this occupation mix at the four-digit parent industry rather than NAICS 238340.
- a: OEWS excludes self-employed workers, material because BLS reports 25.7% self-employment for tile and stone setters.
- a: Task exposure is an analyst allocation, not a measured AI substitution rate, and does not assume robotic automation of field installation.
- rho: Construction-sector AI adoption is broader than tile contracting and the 2024 Census measure used a narrower question than the 2026 measure.
- rho: Current adoption does not directly measure the five-year share of exposed labor opportunity implemented.
- rho: Low-quality plans, site variation, fragmented software, review requirements, and workforce training may limit realized savings.
- e: No source measures lens eligibility among the injected LMM-band firms.
- e: Repeat work may come through contractor relationships even when each underlying construction project is nonrecurring.
- e: The injected firm count is an estimate from broader datasets and may include firms whose economics are not representative of transferable tile contractors.
- s5: FMI covers the broader US engineering and construction sector, and respondent selection may favor established firms.
- s5: The MNP sample is Canadian and therefore differs in financing, taxes, and ownership-transfer institutions.
- s5: Stated exit intent is not a completed qualifying transfer, and broker-reported sales are not a complete market census.
- q: No source reports the contract-type mix or savings pass-through for NAICS 238340.
- q: The federal fixed-price rule explains contract economics but is not evidence of private tile-contract prevalence.
- q: Retention depends on local competition, backlog, relationship quality, and whether savings improve speed or quality rather than only cost.
- d5: Occupational employment is not industry output and includes tile setters employed outside the target NAICS.
- d5: The BLS projection begins in 2024 and spans a full decade, while this packet uses a five-year horizon from 2026.
- d5: Housing cycles, interest rates, renovation activity, and substitution toward resilient flooring can materially alter tile demand.
- o: The estimate concerns operator necessity, not the share of tasks performed manually.
- o: Licensing and accountability rules vary by state and project type.
- o: Unexpected advances in field robotics or modular construction could reduce operator-required quantity more quickly.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: NAICS 238340 Tile and Terrazzo Contractors](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines the industry as job-site setting and installation of ceramic tile, interior stone, mosaic, and terrazzo, including new work, additions, alterations, maintenance, and repairs; identifies excluded adjacent activities.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 238300 Building Finishing Contractors](https://www.bls.gov/oes/2023/may/naics4_238300.htm) (accessed 2026-07-22): Provides parent-industry employment shares and mean wages by occupation group, including construction 70.96%, office support 8.59%, management 5.32%, business and financial operations 4.63%, and sales 2.94%.
- **S3** — [O*NET OnLine: Tile and Stone Setters, 47-2044.00](https://www.onetonline.org/link/summary/47-2044.00) (accessed 2026-07-22): Lists the occupation's physical installation tasks and information tasks, including layout, cutting, mortar application, blueprint study, estimating, ordering, scheduling-related activities, and customer assistance.
- **S4** — [Tracking Firm Use of AI in Real Time: A Snapshot from the Business Trends and Outlook Survey](https://www2.census.gov/library/working-papers/2024/adrm/ces/CES-WP-24-16R.pdf) (accessed 2026-07-22): Reports 1.4% firm-weighted current AI use in construction and 1.9% of construction workers at AI-using firms in the 2024 reference period, plus workflow, training, and applicability constraints.
- **S5** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports economy-wide business AI usage at roughly one-fifth during Census BTOS data collected from December 2025 through May 2026, while documenting a broader business-function question.
- **S6** — [FMI Releases 2024 Study on Ownership Transfer and Management Succession](https://fmicorp.com/about/news/fmi-releases-2024-study-on-ownership-transfer-and-management-succession) (accessed 2026-07-22): Reports a survey of nearly 300 US engineering and construction leaders: 38% planned to exit within five years, half of them lacked an ownership transition plan, and intended transfer modes included employee and family transactions.
- **S7** — [Preparing for the Next Chapter in Construction: 2025 MNP Report](https://www.cca-acc.com/plus/preparing-for-the-next-chapter-in-construction-2025-mnp-report/) (accessed 2026-07-22): Reports an Ipsos survey of 191 Canadian construction owners: 30% expected to transition ownership within five years, 13% were currently transitioning, and 29% had a formal transition plan.
- **S8** — [Construction Business Valuation Multiples and Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/building-construction/) (accessed 2026-07-22): Documents reported sales of small, locally owned construction businesses, including flooring and finishing specialties; the analyzed set includes 3,142 sold listings and a 207-day median time on market.
- **S9** — [Occupational Outlook Handbook: Flooring Installers and Tile and Stone Setters](https://www.bls.gov/ooh/construction-and-extraction/tile-and-marble-setters.htm) (accessed 2026-07-22): Describes duties, physical requirements, work settings, training, self-employment, and demand drivers; projects tile and stone setter employment from 52,600 in 2024 to 58,000 in 2034.
- **S10** — [Federal Acquisition Regulation Subpart 16.2: Fixed-Price Contracts](https://www.acquisition.gov/far/subpart-16.2) (accessed 2026-07-22): Defines firm-fixed-price economics: price is not adjusted for the contractor's cost experience, and the contractor bears cost responsibility and resulting profit or loss.
