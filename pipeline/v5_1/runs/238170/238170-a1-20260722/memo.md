# 238170 — Siding Contractors

*v5.1 Stage 1 research memo. Run `238170-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.74 · L 0.80 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Necessary on-site installation and replacement preserve operator-required demand while administrative and estimating workflows offer a focused AI efficiency opportunity.
**Weakness:** The eligible LMM pool is small and estimated, with weak siding-specific evidence on task exposure, completed transfers, and long-run real demand.

## Business-model lens
- Included: US lower-middle-market contractors installing, replacing, maintaining, and repairing wood, aluminum, vinyl, fiber-cement, and other siding, plus gutters and downspouts, for external residential and commercial customers.
- Excluded: Brick, stone, stucco, and curtain-wall installation; captive construction crews; shell firms; non-control financing vehicles; and firms without an operating siding service business.
- Customer and revenue model: Project-based installation and replacement revenue, usually bid or quoted against a defined scope and paid by homeowners, property owners, general contractors, builders, or insurers; repair and maintenance provide repeat but not typically subscription revenue.
- Deviation from default lens: none

## Executive view
Siding contracting remains a physical, local, project-delivery business. AI offers a bounded back-office and commercial workflow opportunity rather than replacement of the core trade; durable repair and replacement needs support demand, while cyclicality and project-level price competition limit certainty.

## How AI changes the work
The most credible changes are faster lead response, measurement and takeoff assistance, estimate and proposal drafting, scheduling, purchasing, customer updates, job-photo documentation, collections, and bookkeeping. Human verification remains essential because substrate damage, dimensions, code details, weather, crew capability, and installation quality are property-specific.

## Value capture
Quoted and fixed-scope projects let an operator retain savings on work already contracted. Retention decays as competitors copy the workflow, general contractors and insurers benchmark costs, and homeowners compare bids, so the durable benefit should come from both lower overhead and better conversion, cycle time, and consistency rather than price alone.

## Firm availability
The supplied LMM universe is small and estimated. Construction succession surveys indicate substantial exit intent, but many siding businesses are owner-centric and some transitions are internal, incomplete, or closures; a transferable target needs reliable crews, clean books, licenses, channel diversity, and relationships that survive the owner.

## Demand durability
Exterior cladding performs a necessary weather-protection function and eventually needs repair or replacement. Aging stock and storms support the service basket, while housing turnover, interest rates, insurance rules, new-build activity, and homeowner deferral make five-year real quantity plausibly flat rather than predictably high-growth.

## Risks and uncertainty
Key risks are a weaker or more cyclical real demand path, lead-channel dependence, storm and insurance volatility, installer scarcity, safety and warranty failures, material inflation, customer concentration, and overestimating how much fragmented small firms can implement. Evidence is mostly broader-construction or remodeling proxy data rather than siding-specific outcome measurement.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2487 | — | ESTIMATE | — |
| n | — | 30 | — | ESTIMATE | — |
| a | 0.1 | 0.16 | 0.24 | PROXY | S1, S2, S3 |
| rho | 0.35 | 0.5 | 0.65 | ESTIMATE | S3, S4 |
| e | 0.55 | 0.7 | 0.85 | ESTIMATE | S5 |
| s5 | 0.1 | 0.17 | 0.25 | PROXY | S6, S7, S8 |
| q | 0.45 | 0.6 | 0.75 | PROXY | S4, S9 |
| d5 | 0.92 | 1 | 1.09 | PROXY | S1, S10 |
| o | 0.93 | 0.97 | 0.995 | PROXY | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.35 | 0.80 | 1.55 | ESTIMATE |
| F | 1.57 | 2.44 | 3.21 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | PROXY |
| D | 8.56 | 9.70 | 10.00 | PROXY |

## Caveats
- a: OEWS publishes the cited occupation mix at the broader NAICS 2381 level, not for siding contractors alone.
- a: Anthropic usage is a measure of observed Claude use, not technical substitutability, and physical occupations are under-represented.
- a: The frozen compensation ratio is based on 2024 wages over 2022 receipts at ancestor 23817 and is quality LOW.
- rho: No siding-specific longitudinal adoption study was located.
- rho: Small contractors may lack clean historical job-cost and measurement data needed for reliable automation.
- rho: This range applies only to the exposed opportunity in a, not to total labor.
- e: The 30-firm LMM count is a margin-bridged ESTIMATE from broader datasets, not an observed siding-firm census.
- e: The Census profile reports establishments, not eligible firms or EBITDA-band businesses.
- e: Project recurrence can arise across a customer base even though an individual homeowner buys siding infrequently.
- s5: FMI surveyed nearly 300 construction leaders, not specifically LMM siding contractors.
- s5: Gallup covers all US business owners and combines sales, public offerings, and transfers.
- s5: Transaction marketplaces omit many private and internal deals and overrepresent firms intentionally marketed for sale.
- q: Residential retail, insurer-funded restoration, builder subcontracting, and commercial work have different pricing power.
- q: The sources establish contractual form, not a directly observed five-year retained-benefit share.
- q: Material costs are large and volatile, so savings in labor administration may be hard for customers to observe but also small relative to the invoice.
- d5: Neither source measures constant-price, constant-quality siding installation quantity.
- d5: The LIRA covers owner-occupied home improvement and repair, excluding important new-build and commercial channels.
- d5: Storm frequency, insurance practices, housing turnover, rates, and material substitution can move demand sharply by region.
- o: The measure concerns accountable operator requirement, not whether every task remains manual.
- o: Modular construction could reduce field installation in new-build niches faster than in replacement work.
- o: No siding-specific technology-substitution forecast was located.

## Sources
- **S1** — [Construction Laborers and Helpers](https://www.bls.gov/ooh/construction-and-extraction/construction-laborers-and-helpers.htm) (accessed 2026-07-22): BLS states that laborers and helpers use, supply, or hold materials and tools and clean work areas on construction sites; it projects 7% employment growth from 2024 to 2034 and 149,400 annual openings.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): For foundation, structure, and building exterior contractors, BLS lists roofers, construction laborers, cement masons, carpenters, field supervisors, and other physical trades among the largest occupations; general managers and office clerks are also present.
- **S3** — [Anthropic Economic Index report: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report) (accessed 2026-07-22): Anthropic reports that physical occupation categories including Construction & Extraction are under-represented in its survey and in Claude sessions, and notes that judgment and management are commonly named as capabilities AI lacks.
- **S4** — [Contractor Guide](https://sbpusa.org/public/uploads/pdfs/SBP_ContractorGuide_EN_Apr_2021.pdf) (accessed 2026-07-22): The guide recommends written construction contracts specifying scope, material and labor costs, payment schedule, warranties, change orders, and related accountability, supporting project-based contractual economics and the need for controlled workflow.
- **S5** — [238170: Siding contractors — Census Bureau Profile](https://data.census.gov/profile/238170_-_Siding_contractors?codeset=naics~238170) (accessed 2026-07-22): The Census profile defines the industry as installing exterior siding materials and gutters/downspouts, including new work, additions, alterations, maintenance, and repairs; it reports 9,142 employer establishments for 2023.
- **S6** — [FMI Releases 2024 Study on Ownership Transfer and Management Succession](https://fmicorp.com/about/news/fmi-releases-2024-study-on-ownership-transfer-and-management-succession) (accessed 2026-07-22): FMI says its nearly 300-leader construction survey found that 38% of owners planned to exit in three to five years, half without a transition plan; it also reports intended employee and family transfer routes.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Gallup's fall-2024 survey found 14% of owners who primarily work for their business planned to sell, go public, or transfer ownership in the next five years, while 8% planned to close.
- **S8** — [Construction Business Valuation Multiples & Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/building-construction/) (accessed 2026-07-22): BizBuySell reports a market of building and construction businesses sold on its platform and says median sale prices rose 19% from 2021 to 2025, establishing observable transaction activity but not a population transfer rate.
- **S9** — [Governing rules and responsibilities](https://www.sba.gov/federal-contracting/contracting-guide/governing-rules-responsibilities) (accessed 2026-07-22): SBA guidance describes fixed-price construction contracts, lump-sum payment for smaller contracts, and progress payments for larger fixed-price contracts and subcontracts.
- **S10** — [Remodeling Growth Set to Downshift in Late 2026](https://www.jchs.harvard.edu/blog/remodeling-growth-set-downshift-late-2026) (accessed 2026-07-22): Harvard's revised LIRA release projects year-over-year owner-occupied renovation and repair spending growth of 2.1% in mid-2026, easing to 1.6% by year-end, with annual spending reaching $518 billion.
