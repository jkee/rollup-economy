# 236118 — Residential Remodelers

*v5.1 Stage 1 research memo. Run `236118-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.54 · L 0.82 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A durable installed base of aging homes creates repeat project demand while AI can compress the coordination and administrative layer around field work.
**Weakness:** Physical trades dominate delivery, and fragmented custom projects with concealed conditions constrain both AI implementation and operational standardization.

## Business-model lens
- Included: Lower-middle-market residential remodeling general contractors, design-build firms, and project construction managers providing additions, alterations, reconstruction, maintenance, and repairs to external homeowners, landlords, multifamily owners, property managers, insurers, and housing organizations under recurring or repeat project relationships.
- Excluded: For-sale remodeling performed on the firm's own account; captive internal construction units; non-control financing vehicles; nonresidential remodeling; new-home construction; and firms whose primary activity is a specialized trade classified in NAICS 238.
- Customer and revenue model: Customers outsource responsibility for a residential project or maintenance program. Revenue is commonly earned through fixed-price, time-and-materials, cost-plus, design-build, construction-management, insurance-restoration, or recurring maintenance arrangements; repeatability is strongest with property managers, multifamily owners, insurers, and prior homeowners.
- Deviation from default lens: The NAICS definition includes for-sale remodelers alongside contractors and construction managers. The lens is narrowed to coherent for-others service businesses because own-account resale activity does not have an external service customer; this is a business-model distinction, not an attractiveness choice.

## Executive view
Residential remodeling is fundamentally an outsourced project service, although the NAICS also includes an own-account for-sale edge that is excluded. The opportunity is concentrated in estimating, design support, scheduling, procurement, customer communication, and administration, not physical trade work. Aging homes and households support demand, while fragmentation, cyclicality, labor scarcity, and custom-site uncertainty limit implementation and transferability.

## How AI changes the work
AI can accelerate lead qualification, scope and proposal drafting, visual options, estimating support, schedule updates, document control, product comparison, customer communications, change-order paperwork, bookkeeping, and warranty triage. It does not remove demolition, installation, field measurement, inspection, safety, or judgment about concealed conditions. The practical gain depends on clean historical job-cost data and disciplined workflows that many local remodelers lack.

## Value capture
Fixed-price and design-build work can retain savings initially, while time-and-materials and transparent cost-plus work exposes more benefit to the customer. Quote competition and repeat commercial buyers should capture part of the gain over five years. Reputation, trust inside occupied homes, design quality, warranty, and scarce local capacity reduce but do not eliminate pass-through.

## Firm availability
Most correctly classified firms in the modeled LMM band should fit the for-others service lens, but the frozen count is an estimate based on a broad homebuilding margin. General small-business succession evidence suggests meaningful intent, not closed deal probability. Owner dependence, licensing, local reputation, project liabilities, and weak management depth can make a remodeling firm difficult to transfer despite attractive reported earnings.

## Demand durability
The housing stock is old, homeowners face replacement cycles, and aging-in-place, energy efficiency, resilience, and mortgage lock-in support professional remodeling. Near-term nominal growth is expected to slow, and real volume can fall when affordability, financing, insurance, or home sales weaken. Complex projects still require an accountable operator even as software increases homeowner self-service and direct trade coordination.

## Risks and uncertainty
The largest uncertainties are the 2361 rather than 236118 occupation proxy, absence of remodeler-specific realized AI productivity data, short-horizon nominal demand forecasts, unknown contract mix and pass-through, estimated LMM firm count, labor and subcontractor constraints, permitting and regional variation, construction-defect and warranty liabilities, change-order disputes, and the possibility that owner relationships vanish after a transfer.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2119 | — | OBSERVED | — |
| n | — | 2921 | — | ESTIMATE | — |
| a | 0.13 | 0.22 | 0.32 | ESTIMATE | S2, S3, S4 |
| rho | 0.28 | 0.44 | 0.62 | ESTIMATE | S3, S4, S7 |
| e | 0.68 | 0.83 | 0.93 | ESTIMATE | S1 |
| s5 | 0.08 | 0.14 | 0.23 | PROXY | S5 |
| q | 0.32 | 0.52 | 0.7 | ESTIMATE | S1 |
| d5 | 0.88 | 1.05 | 1.22 | PROXY | S6, S7, S8, S9 |
| o | 0.89 | 0.95 | 0.99 | ESTIMATE | S1, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.31 | 0.82 | 1.68 | ESTIMATE |
| F | 8.16 | 9.38 | 10.00 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.83 | 9.97 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation mix is for NAICS 2361 residential building construction, not remodelers alone.
- a: The NAHB AI figures cover single-family home builders rather than a remodeling-only sample.
- a: The frozen compensation-to-receipts ratio uses 2024 wages over 2022 receipts and a median harmonization factor, which may not represent the narrowed for-others subset.
- rho: AI use is not equivalent to successful labor implementation.
- rho: Custom projects and undocumented site conditions make remodeling less standardized than production homebuilding.
- rho: Implementation could be higher for scaled design-build platforms and lower for owner-led local contractors.
- e: No source quantifies the share of 236118 LMM firms that are for-others, repeat-service operators.
- e: Some firms may be project businesses dependent on one owner even at modeled LMM EBITDA.
- e: The frozen n is a margin-bridged ESTIMATE using a homebuilding sector margin rather than observed remodeler EBITDA.
- s5: The survey measures plans, not completed control transfers, and combines sales with gifts and rare offerings.
- s5: It is not construction-specific or restricted to $1–10M normalized EBITDA.
- s5: Deaths without transferable operations and internal reorganizations are excluded from the target construct.
- q: No direct source measures five-year retention of AI-generated gross benefits in residential remodeling.
- q: Materials inflation, project mix, homeowner selections, and change orders can mask true pass-through.
- q: Implementation difficulty and demand changes are excluded here and handled in rho and d5/o.
- d5: The explicit LIRA forecast extends only four quarters and is nominal, requiring extrapolation and inflation adjustment judgment.
- d5: NAHB sentiment is a member survey and is not a quantity index.
- d5: National housing-age evidence masks large regional differences in incomes, insurance, disasters, regulation, and home values.
- o: The 39% DIY statistic covers all projects, not the current professional LMM service basket.
- o: Accountable-operator persistence is inferred from workflow and liability structure rather than directly measured.
- o: The estimate preserves the operator role, not today's staffing levels or administrative tasks.

## Sources
- **S1** — [2022 NAICS Definition: Residential Remodelers (236118)](https://www.census.gov/naics/?details=23&input=23&year=2022) (accessed 2026-07-22): Defines 236118 as establishments responsible for additions, alterations, reconstruction, maintenance, and repairs to single- and multifamily residential buildings, including remodeling general contractors, for-sale remodelers, design-build firms, and project construction management firms.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): For residential building construction, lists carpenters at 215,170, construction laborers at 138,930, trade supervisors at 79,550, construction managers at 55,510, general and operations managers at 43,560, project-management specialists at 39,980, office clerks at 37,120, bookkeepers at 24,940, services sales representatives at 24,440, and administrative assistants at 20,660.
- **S3** — [AI in Home Building: Still in Its Infancy, But Gaining Ground](https://www.nahb.org/blog/2025/08/ai-in-home-building-gaining-ground) (accessed 2026-07-22): Reports that as of July 2025 about 20% of single-family builders used AI for advertising and marketing and 11% used it to analyze markets and plan future projects, while most had not adopted AI in their business practices.
- **S4** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports nationally representative BTOS data from December 2025 through May 2026: overall business AI use of 17%-20%, expected six-month use of 20%-23%, 37% use among firms with at least 250 employees, and under 20% among firms with four or fewer employees.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports a fall-2024 U.S. owner survey in which 17% of owners age 55 or older and 10% of younger owners planned a sale, gift, or rare offering within five years; cites Census evidence that 52.3% of employer businesses are owned by people age 55 or older.
- **S6** — [Remodeling Growth Set to Downshift in Late 2026](https://www.jchs.harvard.edu/blog/remodeling-growth-set-downshift-late-2026) (accessed 2026-07-22): Projects nominal year-over-year owner-occupied renovation and repair spending growth of 2.1% in mid-2026, slowing to 1.6% by year-end, with annual spending reaching $518 billion.
- **S7** — [Improving America's Housing 2025](https://www.jchs.harvard.edu/sites/default/files/reports/files/Harvard_JCHS_Improving_Americas_Housing_2025.pdf) (accessed 2026-07-22): Finds remodeling innovation has been limited and industry fragmentation constrains investment, while aging homes and households, work-from-home patterns, energy efficiency, accessibility, resilience, and maintenance needs support continued investment; says improvements and repairs have been the majority of private residential construction spending for 16 years except 2021.
- **S8** — [NAHB Expects Remodeling Growth in 2026 and Beyond](https://www.nahb.org/news-and-economics/press-releases/2026/02/nahb-expects-remodeling-growth-in-2026-and-beyond) (accessed 2026-07-22): Reports 24 consecutive quarters of Remodeling Market Index readings above the break-even level of 50 and identifies aging housing stock, mortgage lock-in, and aging in place as persistent tailwinds.
- **S9** — [From Size of Homes to Rental Costs, Census Data Provide Economic and Lifestyle Profile of U.S. Housing](https://www.census.gov/library/stories/2023/06/owning-or-renting-the-american-dream.html) (accessed 2026-07-22): Reports from the 2021 American Housing Survey that 49.0 million homeowners, or 59%, made home improvements; 53.0 million of 135.0 million projects, or 39%, were do-it-yourself; and homeowners spent a median $5,000 on improvements.
- **S10** — [Remodeling Market Poised for Growth as the Age of Owner-Occupied Homes Increases](https://www.nahb.org/news-and-economics/press-releases/2025/05/remodeling-market-poised-for-growth-as-the-age-of-owner-occupied-homes-increases) (accessed 2026-07-22): Reports NAHB analysis of ACS data showing almost half of U.S. owner-occupied homes were built before 1980, the median age was 41 years, and around 48% dated to the 1980s or earlier.
