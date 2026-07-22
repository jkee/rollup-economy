# 238350 — Finish Carpentry Contractors

*v5.1 Stage 1 research memo. Run `238350-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.48 · L 1.25 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable onsite installation demand paired with automatable estimating, documentation, scheduling, and back-office workflows.
**Weakness:** Most labor is physical and site-specific, while transferability and retained savings depend heavily on owner independence and repeat-customer quality that public data do not measure.

## Business-model lens
- Included: Independent lower-middle-market contractors performing onsite finish carpentry, including trim and molding, millwork, built-in cabinets, paneling, stairs, and prefabricated residential door, window, garage-door, cabinet, and countertop installation, where work is repeatedly outsourced by homebuilders, general contractors, remodelers, property operators, or recurring institutional customers.
- Excluded: Captive installation crews, shells, non-control financing vehicles, shop-based cabinet manufacturing, framing, tile or stone countertop installation, retail product sales without installation, and owner-operator or handyman work supported only by isolated one-off consumer jobs rather than a transferable repeat-customer operation.
- Customer and revenue model: Primarily project-based subcontract or direct-owner revenue, commonly bid as a fixed price for a defined scope, with some time-and-materials work for uncertain conditions. Recurrence comes from repeat builder, general-contractor, remodeler, property-manager, and institutional relationships rather than subscription contracts.
- Deviation from default lens: none

## Executive view
Finish carpentry combines a physically durable installed service with a modest but real digital labor opportunity. The practical AI case is to make estimators, project managers, owners, and office staff handle more bids and jobs with fewer clerical hours, not to replace the craft crew. Repeat GC and builder relationships can support a transferable platform, but project cyclicality, owner dependence, and competitive rebidding constrain certainty.

## How AI changes the work
AI can extract quantities and scope from plans, draft estimates and proposals, compare specifications, schedule crews, summarize site notes, maintain job records, prepare change orders, reconcile invoices, and handle routine customer communication. Human review remains necessary because field conditions, dimensions, finish quality, safety, and installation tolerances create expensive errors, and the majority of labor remains hands-on.

## Value capture
Fixed-price scopes can convert saved estimating and administrative hours into margin or added bidding capacity during the awarded job. Over time, general contractors and repeat customers will observe faster bids and market prices, while competitors can buy similar software, so part of the gain is likely shared through lower bids, better service, or unchanged prices with more included responsiveness.

## Firm availability
There is a demonstrated market for construction-business transfers and a broad construction succession pipeline, including internal and family transfers. For finish carpentry, the central diligence issue is whether customer relationships, estimating knowledge, licensing, and crew leadership reside in the company or only in the selling owner; the latter can turn an apparent contractor into a nontransferable job.

## Demand durability
Installed trim, cabinets, millwork, stairs, doors, and windows remain tied to new construction, renovation, repair, and replacement. Five-year real demand is likely near flat to modestly higher, with housing and remodeling cyclicality on the downside and population growth and nonresidential construction on the upside. Prefabrication reduces field content but generally preserves an onsite installation and accountability role.

## Risks and uncertainty
The evidence is strongest for broad building-finishing occupation mix and physical task content, and weakest for finish-carpentry-specific contract mix, eligible-firm share, succession completion, and productivity pass-through. The frozen labor ratio is LOW quality at an ancestor level with a wage/receipts vintage mismatch, and the firm count is modeled from broad margins. A bad case is a customer-concentrated, owner-sold shop whose labor savings are competed away while housing activity falls and prefabricated systems remove field hours.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2586 | — | ESTIMATE | — |
| n | — | 167 | — | ESTIMATE | — |
| a | 0.14 | 0.22 | 0.31 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.55 | 0.72 | PROXY | S4, S5, S6 |
| e | 0.45 | 0.62 | 0.78 | ESTIMATE | S1, S7 |
| s5 | 0.16 | 0.28 | 0.4 | PROXY | S7, S8, S9 |
| q | 0.38 | 0.58 | 0.75 | PROXY | S10, S11 |
| d5 | 0.9 | 1.02 | 1.12 | PROXY | S12, S13 |
| o | 0.8 | 0.9 | 0.96 | PROXY | S3, S12 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.51 | 1.25 | 2.31 | ESTIMATE |
| F | 4.13 | 5.47 | 6.39 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | PROXY |
| D | 7.20 | 9.18 | 10.00 | PROXY |

## Caveats
- a: OEWS publishes the useful occupation mix at NAICS 238300 rather than 238350, and the May 2023 vintage predates some current AI use.
- a: Task exposure assignments are judgmental and do not measure realized labor substitution.
- a: The frozen labor ratio uses 2024 wages over 2022 receipts at ancestor 23835, is rated LOW, and is harmonized to the IPS basis; those issues can materially affect the labor opportunity even if this share is sound.
- rho: RICS is global and weighted toward built-environment professionals; AGC respondents are broader and often larger than finish-carpentry targets.
- rho: Investment intentions and self-reported use are not verified operational labor savings.
- rho: Implementation applies only to the exposed share in a; it does not imply automation of onsite craft work.
- e: No source measures lens eligibility for NAICS 238350 or for the modeled EBITDA band.
- e: The Census definition includes new work, alterations, maintenance, repairs, ship joinery, and several installation niches, so customer recurrence and owner dependence vary.
- e: The frozen firm count n=167 is an ESTIMATE margin-bridged from size-class counts and receipts using a broad engineering/construction margin; eligibility does not repair that uncertainty.
- s5: The strongest timing evidence was collected in 2020 and reflects pandemic-era expectations.
- s5: Construction-wide surveys mix much larger and more transferable contractors with small owner-led shops.
- s5: BizBuySell transactions skew well below the target $1-10M EBITDA band and have no industry population denominator.
- q: No representative source reports contract-type shares or post-productivity repricing for NAICS 238350.
- q: The result is sensitive to whether savings improve scarce-capacity throughput or trigger lower bids; this range addresses price capture only, not demand volume.
- q: Federal construction and one Seattle residential contractor are imperfect endpoints for the national target population.
- d5: The BLS occupation is broader than finish carpentry and spans a ten-year rather than five-year horizon.
- d5: Census construction spending is nominal and highly aggregated, so it is used only as a cyclical boundary signal.
- d5: Interest rates, housing starts, remodeling cycles, tariffs, and factory construction can move the five-year endpoint materially.
- o: O*NET covers all carpenters rather than finish-carpentry contractors and reports current, not year-five, automation.
- o: Prefabrication can reduce field hours without eliminating accountable installation, so its effect on quantity and operator requirement is difficult to separate.
- o: Licensing and permit responsibility vary by state and project, and are not directly measured here.

## Sources
- **S1** — [2022 NAICS Definition: 238350 Finish Carpentry Contractors](https://www.census.gov/naics/?details=238350&input=238350&year=2022) (accessed 2026-07-22): Defines the industry as onsite finish carpentry covering new work, additions, alterations, maintenance, and repairs, with examples and cross-references separating framing, shop cabinet manufacturing, and other trades.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Building Finishing Contractors](https://www.bls.gov/oes/2023/may/naics4_238300.htm) (accessed 2026-07-22): Reports 839,170 total employment and major-group shares and wages, including construction 70.96%, office support 8.59%, management 5.32%, business and financial operations 4.63%, and sales 2.94%.
- **S3** — [O*NET OnLine: Carpenters 47-2031.00](https://www.onetonline.org/link/details/47-2031.00) (accessed 2026-07-22): Lists physical installation and measurement tasks plus records, scheduling, ordering, and cost-estimating tasks; reports degree-of-automation responses including 57% not at all automated, 16% slightly, and 19% moderately.
- **S4** — [2025 U.S. State of AI in Construction and Design Report](https://www.houzz.com/press/993/Houzz-Releases-Inaugural-2025-U-S-State-of-AI-in-Construction-and-Design-Report) (accessed 2026-07-22): Survey of over 700 professionals reports 32% AI use among construction businesses, 64% among large construction firms, use concentrated in admin, sales, planning, and project/client management, and 92% of contractor users without formal training.
- **S5** — [RICS Artificial Intelligence in Construction Report 2025](https://www.rics.org/news-insights/artificial-intelligence-in-construction-report) (accessed 2026-07-22): Global survey of more than 2,200 construction professionals reports 45% no AI implementation, 34% early pilots, about 15% active use, 74% limited or no preparation, and material skills, integration, data, and cost barriers.
- **S6** — [2025 Construction Hiring and Business Outlook Report](https://www.agc.org/sites/default/files/users/user21902/2025%20Construction%20Hiring%20and%20Business%20Outlook%20Report.pdf) (accessed 2026-07-22): AGC survey reports 44% planned increased AI investment, 35% increased estimating-software investment, and major IT challenges including implementation/training time, employee resistance, field-office communication, and software integration.
- **S7** — [Construction Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/building-construction/) (accessed 2026-07-22): Reports 3,142 construction businesses sold on the marketplace, with 207 median days on market, $1.51 million median revenue, and five-year transaction and valuation observations for 2021-2025.
- **S8** — [Ownership Transfer and Succession Management in Construction: Top Four Questions in 2021](https://beta.cfma.org/articles/ownership-transfer-and-succession-management-in-construction-top-four-questions-in-2-21) (accessed 2026-07-22): FMI/CFMA survey reports 29% expected to sell 100% of equity within five years after pandemic effects, 35% planned to exit in less than five years, and more than two-thirds intended internal employee or family transfers.
- **S9** — [SBA Small Business Facts: Paths to Business Ownership](https://advocacy.sba.gov/wp-content/uploads/2021/03/Paths-to-Business-Ownership-fact-sheet.pdf) (accessed 2026-07-22): Census-derived fact sheet reports 64.5% of owners planned to sell eventually and that 12% of construction owners had purchased their firms, versus 22% across employer owners.
- **S10** — [Burl: Seattle Finish Carpentry Pricing](https://www.burlseattle.com/pricing/) (accessed 2026-07-22): An industry operator states it primarily uses fixed-price contracts, builds estimates from labor, materials, and time, adds 15%-20% above estimated cost for uncertainty, and uses time-and-materials for uncertain scopes.
- **S11** — [Federal Construction Subcontracting: Insight into Subcontractor Selection Is Limited, but Agencies Use Oversight Tools to Monitor Performance](https://www.gao.gov/products/gao-15-230) (accessed 2026-07-22): GAO reports federal construction used primarily competitive fixed-price contracts, with primes responsible for agreed price and schedule and subcontractors typically performing 60%-90% of project work.
- **S12** — [Occupational Outlook Handbook: Carpenters](https://www.bls.gov/ooh/construction-and-extraction/carpenters.htm) (accessed 2026-07-22): Projects carpenter employment from 959,000 in 2024 to 1,002,100 in 2034, a 4% increase, citing homebuilding and nonresidential construction while identifying modular and prefabricated components as a labor-demand headwind.
- **S13** — [Monthly Construction Spending, May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-22): Reports $2,210.2 billion total construction SAAR in May 2026, 1.5% below May 2025, with first-five-month spending 2.7% below the comparable 2025 period and $930.2 billion residential SAAR.
