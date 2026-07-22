# 236117 — New Housing For-Sale Builders

*v5.1 Stage 1 research memo. Run `236117-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.96 · L 0.14 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-addressable estimating, project administration, procurement, sales, finance, and warranty coordination inside a still operator-required physical delivery model.
**Weakness:** The industry's core own-account home-and-land sale is not an outsourced recurring service, leaving only a small and poorly measured eligible subset.

## Business-model lens
- Included: Lower-middle-market for-sale home builders with a material pattern of repeat external-customer work, principally repeated bulk or programmatic sales to institutional, investor, or community-development buyers, including the associated planning, procurement, project administration, sales coordination, handover, and warranty workflows.
- Excluded: One-off speculative sales to individual homebuyers; land-only development; rental ownership; captive construction; non-control financing vehicles; general contracting for a customer's land; remodeling; and specialty-trade subcontracting.
- Customer and revenue model: The qualifying edge case earns primarily project and home-sale revenue under repeated relationships with external bulk or programmatic buyers. Prices are generally set per home or portfolio rather than as cost-plus labor reimbursement; warranty and handover obligations accompany the sale but are not assumed to be standalone recurring revenue.
- Deviation from default lens: The NAICS core is an own-account product-and-land sale rather than an outsourced service: Census defines builders as building on land they own or control and including the land in the home sale. To keep the screen coherent with the fixed recurring-or-repeat outsourced-service population, the lens is narrowed to firms with demonstrable repeat external-customer programs; ordinary one-off speculative consumer sales are excluded.

## Executive view
The code is a difficult fit for the fixed screen because Census places ordinary for-sale builders in an own-account home-and-land sales business, not recurring outsourced services. A narrow repeat-buyer subset can still be evaluated, but eligibility is the central uncertainty. Within that subset, AI mainly improves overhead and coordination rather than physical construction, and demand is cyclical despite a persistent national housing shortage.

## How AI changes the work
The most plausible changes are faster estimating, plan and document review, scheduling, procurement comparison, subcontractor communication, sales content, buyer support, finance, and warranty triage. Field construction, inspections, exception handling, local permitting judgment, safety, and accountable site supervision remain human- and operator-intensive. Current builder use is still concentrated in marketing and market analysis, so a meaningful but incomplete implementation ramp is assumed.

## Value capture
Home and portfolio prices are not normally billed as reimbursed internal labor hours, so operating savings can improve margin initially. Repeat institutional buyers have negotiating leverage, can rebid standardized programs, and will seek volume concessions; competing builders may also price away part of the gain. Land, financing incentives, and housing-cycle effects make realized retention hard to isolate.

## Firm availability
Only a small fraction of the frozen LMM-band firm estimate is likely to satisfy the repeat outsourced-service lens. General small-business surveys indicate transfer intent but do not establish closed, qualifying sales of transferable homebuilding operations. Owner guarantees, project liabilities, inventory and land exposure, and reliance on local relationships can turn an apparent succession into a liquidation or asset sale.

## Demand durability
A modeled national housing shortage and a modest near-term start forecast support a stable-to-growing five-year unit outlook, but May 2026 starts also demonstrate volatility. Mortgage rates, buyer financing, zoning, land, materials, labor, and regional migration can overwhelm the national base case. Physical delivery still requires an accountable builder or equivalent operator even if administrative workflows become software-assisted.

## Risks and uncertainty
The largest risk is categorical: repeat home sales may still be product transactions outside the mandated service lens. Other major uncertainties are the absence of 236117-specific occupation and deal data, possible overstatement in the frozen margin-bridged firm count, sharp housing cyclicality, warranty and construction-defect liabilities, working-capital and land risk, local permitting variation, and inability to separate AI savings from price, mix, and cycle effects.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.032 | — | OBSERVED | — |
| n | — | 1714 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.34 | ESTIMATE | S2, S3, S4 |
| rho | 0.3 | 0.48 | 0.65 | ESTIMATE | S3, S4, S8 |
| e | 0.01 | 0.04 | 0.1 | ESTIMATE | S1, S8 |
| s5 | 0.07 | 0.13 | 0.22 | PROXY | S5 |
| q | 0.3 | 0.5 | 0.7 | ESTIMATE | S1 |
| d5 | 0.82 | 1.06 | 1.27 | PROXY | S6, S7, S9 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.05 | 0.14 | 0.28 | ESTIMATE |
| F | 1.27 | 3.69 | 5.88 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.22 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source is NAICS 2361 residential building construction, not 236117 alone.
- a: NAHB AI adoption percentages cover single-family builders and business functions, not wage-weighted task hours.
- a: The frozen compensation-to-receipts input uses 2024 wages over 2022 receipts and is harmonized to the IPS basis; that vintage and basis adjustment may not reflect the narrowed repeat-buyer subset.
- rho: Reported use of AI does not measure successful labor implementation.
- rho: The Census adoption benchmark spans all industries and firm sizes, while NAHB respondents are not limited to the frozen lens.
- rho: Implementation may be slower in small builders with weak data discipline and faster in standardized production platforms.
- e: No source directly counts 236117 firms with repeat external-buyer programs.
- e: Repeat product sales may not meet a strict interpretation of outsourced service even when contracts are programmatic.
- e: The frozen n=1,714 is a margin-bridged estimate from firm counts and receipts using a sector margin and is itself ESTIMATE quality.
- s5: Plans are not completed transfers, and the source combines sales, gifts, and rare offerings.
- s5: The survey is not construction-specific or restricted to $1–10M normalized EBITDA.
- s5: The eligible repeat-buyer subset may be more institutionalized and transferable than the small-business population.
- q: No direct study measures five-year pass-through of AI savings in repeat-buyer homebuilding contracts.
- q: Housing-cycle price movements, land gains, financing incentives, and mix shifts can obscure true pass-through.
- q: This primitive excludes demand loss and implementation difficulty, which are handled elsewhere.
- d5: The five-year value extrapolates beyond NAHB's explicit 2027 forecast.
- d5: Starts are broader than 236117 and broader than the narrowed repeat-buyer lens.
- d5: The Freddie Mac shortage estimate is a model-based stock gap, not realized demand or purchasing power.
- o: Operator requirement is inferred from industry structure, not directly measured.
- o: More functions may migrate to buyer-controlled construction management or vertically integrated specialty contractors.
- o: The estimate concerns accountable operators, not preservation of today's staffing or workflows.

## Sources
- **S1** — [236117: New housing for-sale builders - Census Bureau Profile](https://data.census.gov/profile/236117_-_New_housing_for-sale_builders?codeset=naics~236117) (accessed 2026-07-22): Defines the industry as builders constructing homes on land they own or control, with land included in the sale; distinguishes general contracting, remodeling, specialty trades, and leasing; reports 12,192 employer establishments in 2023.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): For residential building construction, lists carpenters at 215,170, construction laborers at 138,930, construction-trade supervisors at 79,550, construction managers at 55,510, general and operations managers at 43,560, project-management specialists at 39,980, office clerks at 37,120, bookkeepers at 24,940, services sales representatives at 24,440, and administrative assistants at 20,660.
- **S3** — [AI in Home Building: Still in Its Infancy, But Gaining Ground](https://www.nahb.org/blog/2025/08/ai-in-home-building-gaining-ground) (accessed 2026-07-22): Reports that as of July 2025 about 20% of single-family builders used AI for advertising and marketing materials and 11% used it to analyze markets and plan future projects, while most had not adopted AI in business practices.
- **S4** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports nationally representative BTOS evidence from December 2025 through May 2026: overall business AI use of 17%-20%, expected six-month use of 20%-23%, 37% use for firms with at least 250 employees, and under 20% for firms with four or fewer employees.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports a fall-2024 U.S. owner survey in which 17% of owners age 55 or older and 10% of younger owners planned a sale, gift, or rare offering within five years; cites Census evidence that 52.3% of employer businesses are owned by people age 55 or older.
- **S6** — [2026 Housing Outlook: Ongoing Challenges, Cautious Optimism and Incremental Gains](https://www.nahb.org/news-and-economics/press-releases/2026/02/2026-housing-outlook-ongoing-challenges-cautious-optimism-and-incremental-gains) (accessed 2026-07-22): Forecasts single-family starts increasing 1.0% in 2026 to 940,000 and 5% in 2027 to a 984,000 pace; also identifies material, labor, policy, financing, and mortgage-rate constraints.
- **S7** — [Monthly New Residential Construction, May 2026](https://www.census.gov/construction/nrc/current/) (accessed 2026-07-22): Reports May 2026 single-family starts at an 882,000 seasonally adjusted annual rate, down 1.9% from revised April, and single-family completions at 872,000.
- **S8** — [Average New Home Uses 24 Different Subcontractors](https://www.nahb.org/news-and-economics/housing-economics-plus/special-studies/special-studies-pages/average-new-home-uses-24-different-subcontractors) (accessed 2026-07-22): Reports an average of 24 subcontractors per new home, an average 84% share of construction costs subcontracted, and that 77% of surveyed builders subcontracted at least 75% of construction cost.
- **S9** — [U.S. Economic, Housing and Mortgage Market Outlook, November 2024](https://www.freddiemac.com/research/pdf/Freddie_Mac_Outlook_November_2024.pdf) (accessed 2026-07-22): Estimates the U.S. housing shortage at 3.7 million units as of Q3 2024, providing a modeled long-run supply-gap indicator rather than realized purchasing demand.
