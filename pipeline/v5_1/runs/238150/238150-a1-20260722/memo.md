# 238150 — Glass and Glazing Contractors

*v5.1 Stage 1 research memo. Run `238150-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.15 · L 1.11 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-assisted estimating and project administration can expand throughput in a labor-constrained trade without attempting to replace physical glazing crews.
**Weakness:** Most compensation supports hands-on field work, so the wage-weighted implementable AI opportunity is limited and poorly measured.

## Business-model lens
- Included: US lower-middle-market contractors installing, replacing, repairing, and maintaining architectural glass, storefronts, interior glazing, and curtain-wall or related glazing systems for external customers, including firms whose recurring activity is a sequence of bid projects and service calls.
- Excluded: Automotive glass, prefabricated-window installation classified elsewhere, glass manufacturing, captive in-house crews, shells, non-control financing vehicles, and businesses lacking a transferable operating organization.
- Customer and revenue model: Revenue is primarily project-based or service-call contracting for general contractors, building owners, property managers, retailers, institutions, and homeowners; work is commonly won through fixed-price bids, negotiated subcontracts, unit pricing, or time-and-material repair orders.
- Deviation from default lens: none

## Executive view
Glass and glazing contracting remains an operator-led physical service with modest AI opportunity concentrated in the office and coordination layer. The most plausible benefit is greater estimating, project-management, and administrative capacity rather than automation of glazier craft labor.

## How AI changes the work
AI can assist quantity takeoff, specification and drawing search, bid drafting, submittal preparation, schedule updates, procurement comparisons, service dispatch, invoice coding, and customer communication. Humans still must validate scope and dimensions, manage exceptions, coordinate trades, and perform safety-critical installation and repair.

## Value capture
Fixed-price projects allow temporary retention of labor efficiencies, especially when speed and reliable execution relieve customer bottlenecks. Rebid competition and sophisticated general contractors should progressively pass a meaningful share of savings to customers, while time-and-material work passes through faster.

## Firm availability
Most firms at the supplied LMM scale should be operating businesses with crews, systems, and relationships, but owner dependence and customer concentration reduce eligibility. Broad employer-owner survey evidence indicates a real transfer pool, though qualifying completed control sales should be materially below stated five-year transfer intentions.

## Demand durability
Architectural glass installation and repair are tied to both new construction and the existing building stock. BLS expects glazier employment to grow modestly through 2034 and explicitly links demand to both construction and window repair or replacement, supporting a near-flat to modest-growth five-year quantity range.

## Risks and uncertainty
The main uncertainties are the absence of a six-digit occupational wage mix, lack of glazing-specific AI outcome studies, construction cyclicality, office exposure, volatile material costs, bid error risk, and thin evidence on completed owner transfers. Factory preassembly and better design data may reduce field hours, while safety, warranty, and site variability constrain displacement.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3202 | — | ESTIMATE | — |
| n | — | 74 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | ESTIMATE | S2, S3 |
| rho | 0.3 | 0.48 | 0.65 | PROXY | S4, S5 |
| e | 0.68 | 0.8 | 0.9 | ESTIMATE | S1 |
| s5 | 0.08 | 0.14 | 0.2 | PROXY | S6 |
| q | 0.4 | 0.58 | 0.75 | ESTIMATE | — |
| d5 | 0.95 | 1.02 | 1.08 | PROXY | S2 |
| o | 0.93 | 0.97 | 0.99 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.38 | 1.11 | 2.33 | ESTIMATE |
| F | 2.60 | 3.59 | 4.28 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.84 | 9.89 | 10.00 | ESTIMATE |

## Caveats
- a: No current six-digit occupational wage mix was located for this industry.
- a: O*NET and BLS describe occupations, not the share of contractor payroll exposed to AI.
- a: Physical robotics at irregular jobsites is excluded unless implementable within five years.
- rho: Broad construction respondents are not representative of the 74 estimated LMM glazing firms.
- rho: Investment intention is not completed implementation or labor substitution.
- rho: Implementation must preserve bid accuracy, code compliance, safety documentation, and accountable human review.
- e: The supplied firm count is margin-bridged and estimated rather than observed at six digits.
- e: The Census establishment count includes firms far outside the LMM EBITDA band and cannot measure eligibility.
- e: Project revenue can recur at the customer level even when individual contracts are one-off.
- s5: Gallup covers all US employer businesses, not glazing contractors or the LMM EBITDA band.
- s5: Survey plans may not become completed transfers.
- s5: The estimate excludes closures, minority investments, internal reorganizations, and nontransferable owner-operator exits.
- q: No glazing-specific evidence was found measuring pass-through of technology savings.
- q: The mix of fixed-price, unit-price, and time-and-material work varies across commercial, residential, and repair contractors.
- q: Demand volume effects and implementation costs are intentionally excluded from this primitive.
- d5: Occupational employment is not constant-price, constant-quality service demand.
- d5: The BLS forecast is national and ten-year rather than five-year and includes glaziers outside NAICS 238150.
- d5: The supplied compensation ratio uses 23815 and mixes 2024 wages with 2022 receipts.
- o: The range is judgmental and does not measure future robotics adoption.
- o: Greater factory preassembly could shift value away from field contractors.
- o: Self-service is more plausible for minor residential tasks than for commercial exterior systems.

## Sources
- **S1** — [238150: Glass and glazing contractors - Census Bureau Profile](https://data.census.gov/profile/238150_-_Glass_and_glazing_contractors?codeset=naics~238150) (accessed 2026-07-22): Defines the industry as establishments installing glass panes and doing other building glass work, including new work, additions, alterations, maintenance, and repairs; reports 6,945 employer establishments for 2023.
- **S2** — [Occupational Outlook Handbook: Glaziers](https://www.bls.gov/ooh/construction-and-extraction/glaziers.htm) (accessed 2026-07-22): Documents physical glazier duties, jobsite and injury conditions, 60,500 jobs in 2024, 62% employment in foundation/structure/building-exterior contractors, projected employment of 62,500 in 2034, and demand from both new construction and repair or replacement.
- **S3** — [O*NET OnLine Job Duties: Glaziers](https://www.onetonline.org/search/task/choose/47-2121.00) (accessed 2026-07-22): Lists detailed physical and cognitive tasks including blueprint interpretation, measuring, estimating, cutting, rigging, installation, sealing, repair, material movement, and customer consultation.
- **S4** — [AGC/Sage 2025 Construction Hiring and Business Outlook](https://www.agc.org/news/2025/01/08/construction-firms-predict-strong-demand-certain-private-sector-most-types-public-sector-work-2025) (accessed 2026-07-22): Reports 44% of construction firms anticipated increased AI investment, 61% used cloud project-management tools, and 38% cited time to implement and train on technology as a top IT challenge; also documents demand dispersion and project postponements.
- **S5** — [AGC/NCCER 2025 Craft Workforce Survey](https://www.nccer.org/research/2025-workforce-survey-agc-nccer/) (accessed 2026-07-22): Reports that 92% of nearly 1,400 construction firms had difficulty hiring for open positions, supporting the incentive to avoid incremental hiring.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of employer-business owners planned to sell or transfer ownership within five years, versus 9% of nonemployers, and distinguishes transfer plans from closure or no plan.
