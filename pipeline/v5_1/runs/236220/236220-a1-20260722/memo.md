# 236220 — Commercial and Institutional Building Construction

*v5.1 Stage 1 research memo. Run `236220-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.48 · L 0.52 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-assisted preconstruction and project administration can stretch scarce managerial capacity across a large base of repeat, externally served building owners.
**Weakness:** Competitive and transparent contracting can pass savings to customers, while demand is fragmented across sharply diverging building categories and regions.

## Business-model lens
- Included: US lower-middle-market commercial and institutional general contractors, design-build firms, and project construction-management firms that repeatedly deliver new construction, additions, alterations, maintenance, or repairs for external private, nonprofit, and public customers.
- Excluded: Specialty trades classified outside 236220; owner-captive construction units; shells; non-control financing vehicles; and for-sale/speculative builders whose activity is not an outsourced service to an external customer.
- Customer and revenue model: Project-based revenue from commercial, institutional, and public owners under competitively bid or negotiated fixed-price, guaranteed-maximum-price, cost-plus, design-build, and construction-management arrangements; repeat owners, frameworks, renovations, and follow-on projects provide repeat-service economics despite finite individual projects.
- Deviation from default lens: none

## Executive view
Commercial and institutional builders have a bounded AI opportunity concentrated in estimating, project controls, procurement, reporting, and administration rather than physical construction. The addressable firm population is large and repeat relationships are common, but competition, public procurement, owner transparency, bonding, and project cyclicality limit how automatically operational efficiency becomes retained value.

## How AI changes the work
The most practical applications are takeoffs, bid leveling, schedule and cost-risk review, contract search, RFIs and submittals, progress documentation, compliance drafting, accounting, and business development. Field execution, supervision, safety judgment, owner negotiation, and exception handling remain human-intensive; fragmented data and changing project teams make scaling harder than isolated tool demos suggest.

## Value capture
Fixed-price and guaranteed-price work can retain savings during a project, but cost-plus and fee arrangements reveal them to owners. Public bidding and private competitive tendering should reprice part of any recurring cost advantage, while prequalification, speed, reliability, and scarce project-management capacity can preserve a share through better throughput and selective bidding.

## Firm availability
Most general contracting, design-build, and construction-management firms serve external owners and can earn repeat work, although the code also includes speculative builders and owner-dependent project businesses. Succession evidence suggests meaningful transfer activity, but many owners lack plans, favor internal transitions, or operate firms whose bonding and customer relationships do not survive a control change cleanly.

## Demand durability
The service remains strongly operator-required because buildings must be physically delivered under accountable safety, contract, code, and schedule management. Quantity demand is diversified but uneven: data centers and healthcare are strong, while traditional offices, warehouses, and some discretionary commercial segments remain soft; institutional and renovation work add stability.

## Risks and uncertainty
The screen can fail if it treats AI assistance as headcount elimination, assumes all contractors have usable project data, or overlooks local cyclicality and public-bid pricing. Customer concentration, fixed-price overruns, claims, bonding limits, subcontractor failures, loss of key estimators or superintendents, and the highly varied building-category mix can dominate any modeled savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1374 | — | OBSERVED | — |
| n | — | 10875 | — | ESTIMATE | — |
| a | 0.12 | 0.19 | 0.28 | PROXY | S1, S2 |
| rho | 0.32 | 0.5 | 0.68 | PROXY | S2, S3 |
| e | 0.62 | 0.75 | 0.87 | PROXY | S4, S5 |
| s5 | 0.16 | 0.25 | 0.35 | PROXY | S6, S7 |
| q | 0.38 | 0.57 | 0.73 | ESTIMATE | S5, S8 |
| d5 | 0.79 | 0.98 | 1.18 | PROXY | S9, S10 |
| o | 0.89 | 0.96 | 0.99 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.52 | 1.05 | PROXY |
| F | 10.00 | 10.00 | 10.00 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.03 | 9.41 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is four-digit NAICS 236200 and 2023 vintage, though 236220 is a major component of that group.
- a: The task-exposure weights are bounded judgment rather than an observed automation measure.
- a: The frozen compensation-to-receipts input mixes 2024 wages with 2022 receipts and was harmonized across industries, potentially obscuring current project and subcontracting mix.
- rho: Only 10% of the RICS respondent base came from the Americas.
- rho: AGC combines current use with plans to increase investment and does not measure labor substitution.
- rho: Public procurement, owner technology mandates, safety rules, and project-specific data structures can slow implementation.
- e: Repeat-customer revenue is not a direct firm-eligibility measure.
- e: The survey is Ontario-based and its sample is 80% trade contractors, although it reports a general-contractor split.
- e: The exact six-digit share of for-sale builders and owner-dependent firms is unavailable.
- s5: Exit plans do not equal closed qualifying transfers.
- s5: FMI/CFMA covers broad E&C and firms above the target band; 44% of respondents were below $20 million in revenue.
- s5: Licensing, bonding, customer relationships, and key-person dependence can make a nominally available firm nontransferable.
- q: No observed source measures discounted five-year AI-benefit retention for 236220.
- q: The code spans public institutions, negotiated private work, and highly competitive bid markets with different pass-through dynamics.
- q: The estimate excludes demand, implementation cost, and implementation feasibility by design.
- d5: The public forecasts extend only 12-18 months; years three through five are judgmental.
- d5: Construction spending is nominal and the real-quantity conversion is sensitive to labor and materials inflation.
- d5: Data-center growth is unusually concentrated, while office, warehouse, retail, lodging, education, and regional markets can diverge sharply.
- o: No source directly measures the operator-required share five years ahead.
- o: The code includes modular on-site assembly, and further prefabrication could reduce on-site scope without removing overall accountability.
- o: Large public agencies, institutions, retailers, and data-center owners may internalize more construction management than assumed.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 236200](https://www.bls.gov/oes/2023/may/naics4_236200.htm) (accessed 2026-07-22): Nonresidential-building occupation mix: 52.35% construction/extraction, 15.16% management, 12.70% business/financial, and 7.65% office support, with detailed employment and wages for construction managers, project-management specialists, and estimators.
- **S2** — [RICS artificial intelligence in construction report 2025](https://www.rics.org/news-insights/artificial-intelligence-in-construction-report) (accessed 2026-07-22): Global survey of more than 2,200 construction professionals: 45% no implementation, 34% pilots, about 15% active use, 74% limited/no preparation, plus adoption barriers and five-year workflow expectations.
- **S3** — [The 2026 Construction Hiring and Business Outlook](https://www.agc.org/sites/default/files/users/user21902/2026%20Construction%20Hiring%20and%20Business%20Outlook%20Report_Final.pdf) (accessed 2026-07-22): US commercial-contractor survey reports 61% use AI or plan increased investment, with 45% using it for office/admin, 23% for estimating, and 20% for design/preconstruction; also documents labor and project constraints.
- **S4** — [North American Industry Classification System, United States, 2022: 236220 definition](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 236220 as new work, additions, alterations, maintenance, and repairs for commercial and institutional buildings, including general contractors, for-sale builders, design-build firms, construction managers, modular assembly, data centers, hospitals, schools, offices, hotels, and warehouses.
- **S5** — [2026 Ontario Construction Secretariat Contractor Survey](https://iciconstruction.com/wp-content/uploads/2026/03/OCS-2026-Contractor-Outlook-Survey-Feb-26-FINAL.pdf) (accessed 2026-07-22): Survey of 400 ICI contractors reports 73% of work from repeat customers overall and 67% for general contractors, along with bid/sole-source mix, maintenance work, and prequalification evidence.
- **S6** — [2024 Ownership Transfer & Management Succession: FMI and CFMA Industry Study](https://fmicorp.com/uploads/media/2024_OTMS_Study_FINAL.pdf) (accessed 2026-07-22): Survey of almost 300 E&C executives: 38% planned exit in fewer than five years, 51% of that group lacked a defined transfer plan, 64% intended internal transition, and 44% represented firms below $20 million revenue.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey shows 22% of employer-business owners planned to sell, transfer, or take public within five years, while 5% planned closure and 5% were unsure or had no plan.
- **S8** — [Federal Acquisition Regulation Part 16: Types of Contracts](https://www.acquisition.gov/far/part-16) (accessed 2026-07-22): Explains firm-fixed-price contractor responsibility for performance costs and profit/loss versus minimal cost responsibility under cost-plus-fixed-fee, and notes sealed bids use fixed-price forms; supports value-retention mechanisms.
- **S9** — [Monthly Construction Spending, May 2026](https://www.census.gov/construction/c30/pdf/release.pdf) (accessed 2026-07-22): Census table reports total nonresidential construction spending down 3.8% year over year and private nonresidential down 6.6%, with current levels and changes across office, commercial, healthcare, education, lodging, and other relevant categories.
- **S10** — [July 2026 Consensus Construction Forecast](https://www.aia.org/resource-center/july-2026-consensus-construction-forecast) (accessed 2026-07-22): AIA panel forecasts commercial spending up 4.8% in 2026 and 5.8% in 2027, institutional up 2.8% and 2.7%, and data centers up 33% and 25%; without data centers, commercial is forecast down 1% then up 1%.
