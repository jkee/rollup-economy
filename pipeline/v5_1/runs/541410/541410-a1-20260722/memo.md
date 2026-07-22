# 541410 — Interior Design Services

*v5.1 Stage 1 research memo. Run `541410-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.65 · L 2.31 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Document-, image-, research-, and coordination-heavy workflows offer substantial bounded AI leverage while regulated, site-specific delivery preserves the operator role.
**Weakness:** Founder dependence and mixed hourly or pass-through economics can limit both firm transferability and retained productivity benefit.

## Business-model lens
- Included: US lower-middle-market interior design and interior decorating firms providing repeat outsourced planning, design, documentation, specification, procurement coordination, and project-administration services for commercial, hospitality, healthcare, institutional, and residential clients.
- Excluded: Architectural and engineering firms outside NAICS 541410; furniture retailers and manufacturers; construction and installation contractors; captive corporate design teams; shells, non-control financing vehicles, solo practitioners below the LMM band, and firms limited to nonrepeat one-off engagements.
- Customer and revenue model: External property owners, developers, operators, institutions, and homeowners buy project-based services. Revenue may be fixed fee, hourly, a percentage of project cost, procurement markup, or a hybrid; repeatability is strongest with commercial, hospitality, institutional, developer, and multi-site clients.
- Deviation from default lens: none

## Executive view
Interior design combines a credible AI productivity surface with persistent physical-world and accountability requirements. The strongest fit is a repeat-client LMM practice serving commercial, hospitality, institutional, healthcare, developer, or multi-site customers; founder-led aesthetic boutiques and hourly-only residential practices are less attractive because transferability and value capture are weaker.

## How AI changes the work
AI can compress early ideation, mood boards, renderings, layout alternatives, materials research, routine documentation, estimating support, sourcing, bookkeeping, and deadline administration. It is less able to replace site inspection, code and accessibility responsibility, nuanced client discovery, multidisciplinary coordination, purchasing judgment, and construction or installation oversight.

## Value capture
Fixed-fee, project-cost, procurement-markup, and hybrid engagements can retain part of productivity gains through higher throughput or margin. Hourly billing mechanically shares gains through fewer billed hours, while competitive bids and renewals should transmit additional savings to customers, leaving moderate discounted retention.

## Firm availability
Most firms at LMM scale should already be external employer service firms, but only a subset will have repeat demand, management depth, and client relationships transferable beyond the founder. Broad employer-owner succession evidence suggests a real but limited five-year control-transfer pool; completed interior-design deal data are missing.

## Demand durability
Renovations, accessibility, safety codes, and the continuing need to coordinate real spaces support modest real demand. Construction cycles, interest rates, office-space uncertainty, hospitality capital spending, and discretionary residential renovation create meaningful downside volatility.

## Risks and uncertainty
The largest evidence gaps are six-digit occupation mix, US LMM pricing and repeat-client data, realized AI labor savings, and completed control transactions. Industry receipts may also include procurement pass-through, and founder reputation can impair transferability. A faster shift to accurate self-service design and direct procurement would erode low-complexity demand, while AI-generated errors in dimensions, specifications, or code interpretation could create costly rework or liability.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2359 | — | OBSERVED | — |
| n | — | 313 | — | ESTIMATE | — |
| a | 0.28 | 0.43 | 0.58 | PROXY | S2, S3, S4 |
| rho | 0.4 | 0.57 | 0.73 | PROXY | S4, S5 |
| e | 0.62 | 0.76 | 0.88 | ESTIMATE | S1, S9 |
| s5 | 0.09 | 0.15 | 0.22 | PROXY | S6 |
| q | 0.34 | 0.52 | 0.7 | PROXY | S7 |
| d5 | 0.96 | 1.06 | 1.12 | PROXY | S8, S9 |
| o | 0.65 | 0.8 | 0.91 | ESTIMATE | S1, S3, S4, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.06 | 2.31 | 4.00 | PROXY |
| F | 4.69 | 5.79 | 6.63 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | PROXY |
| D | 6.24 | 8.48 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS industry occupation table is four-digit NAICS 541400 and includes graphic, industrial, and other specialized design services.
- a: O*NET task importance does not measure time, wage weight, technical feasibility, or current automation.
- a: The estimate concerns current not-yet-automated work; the available adoption survey does not quantify how much work is already automated.
- rho: Regular tool use is not equivalent to production-grade implementation or realized labor avoidance.
- rho: The interior-design survey is small, global, and associated with a 3D-design platform.
- rho: Autodesk's AECO population is much broader than independent US LMM interior design firms and overrepresents Autodesk users.
- e: No source measures eligibility under the frozen recurring-or-repeat outsourced LMM lens.
- e: The injected firm-count bridge uses a 15.65% broad-sector margin and may place some procurement-heavy or owner-compensation-heavy firms in the wrong EBITDA band.
- e: NAICS 541410 includes aesthetic-only decorating consultants, increasing business-model variation within the code.
- s5: Gallup covers all US employer businesses rather than interior design or the LMM band.
- s5: Survey intentions combine sales with other transfers and do not establish completed qualifying control transactions.
- s5: Founder dependence may reduce sale completion or require long earn-outs.
- q: The pricing survey is from 2019, UK-based, and mostly residential, not US LMM commercial practices.
- q: Pricing-model shares do not directly measure five-year benefit retention.
- q: Procurement markups and pass-through purchases may make receipts an imperfect measure of service economics.
- d5: The BLS output forecast is for NAICS 541400, not 541410.
- d5: Occupation employment is not service quantity and includes interior designers working outside specialized design firms.
- d5: The estimate holds quality and the current service basket constant and therefore excludes new AI-enabled offerings.
- o: No source directly measures the future operator-required share of interior design demand.
- o: Aesthetic-only residential and decorating work is substantially more exposed to self-service than regulated commercial, healthcare, or institutional work.
- o: Rapid improvement in spatially accurate generative design, automated code checking, and direct-to-consumer procurement could push the value below the range.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: NAICS 541410 Interior Design Services](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 541410 as planning, designing, and administering interior-space projects across commercial, hospitality, healthcare, institutional, residential, and aesthetic-only decorating contexts.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Specialized Design Services](https://www.bls.gov/oes/2023/may/naics4_541400.htm) (accessed 2026-07-22): Provides the four-digit occupation mix, including 28,420 interior designers and 15,730 office and administrative support workers, used as an occupation-mix proxy for AI exposure.
- **S3** — [O*NET OnLine: Interior Designers (27-1025.00)](https://www.onetonline.org/link/details/27-1025.00) (accessed 2026-07-22): Documents interior-designer tasks including CAD construction documents, rendering, research and estimating, client advising, code compliance, professional coordination, purchasing, and on-site inspection.
- **S4** — [Concepts, 'tedious tasks' and mood boards: Here's how interior designers are using AI](https://www.homes.com/news/concepts-tedious-tasks-and-mood-boards-heres-how-interior-designers-are-using-ai/494301541/) (accessed 2026-07-22): Reports a 2025 global survey in which 82% of 328 interior-design professionals used AI regularly and describes use in ideation, visualization, sourcing, bookkeeping, and deadline management, with important quality and human-judgment limits.
- **S5** — [Autodesk 2025 State of Design & Make: Industry Insights](https://www.autodesk.com/design-make/research/state-of-design-and-make-2025/industry) (accessed 2026-07-22): Provides broader AECO evidence on AI sentiment, skilled-talent constraints, cost pressure, and planned investment relevant to five-year implementation.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Finds 22% of US employer-business owners planned a sale or ownership transfer within five years and describes transferability differences between employer and nonemployer businesses.
- **S7** — [British Institute of Interior Design: How to price a project](https://biid.org.uk/resources/how-price-project) (accessed 2026-07-22): Reports mixed, fixed-fee, hourly, and project-cost-percentage charging methods and explains their economics, used as a proxy for benefit retention under mixed pricing.
- **S8** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects NAICS 541400 output from $57.5 billion to $70.3 billion in chained 2017 dollars, a 2.0% annual increase, used as a broad demand-growth proxy.
- **S9** — [Occupational Outlook Handbook: Interior Designers](https://www.bls.gov/ooh/arts-and-design/interior-designers.htm) (accessed 2026-07-22): Projects 3% interior-designer employment growth from 2024 to 2034, cites renovation, code, and accessibility demand, and describes operator-required duties and industry settings.
