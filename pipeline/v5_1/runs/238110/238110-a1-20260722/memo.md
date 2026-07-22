# 238110 — Poured Concrete Foundation and Structure Contractors

*v5.1 Stage 1 research memo. Run `238110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.19 · L 0.87 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Essential, locally executed physical work preserves the need for an accountable operator while AI can relieve scarce estimating and project-administration capacity.
**Weakness:** Most payroll is hands-on craft labor, and project-by-project competitive bidding can erode retained AI savings quickly.

## Business-model lens
- Included: US lower-middle-market contractors pouring and finishing concrete foundations and structural elements for external residential, commercial, industrial, and public-project customers.
- Excluded: Shells, captive construction units, non-control financing vehicles, concrete manufacturers without field contracting operations, and firms whose economics are principally paving rather than foundations or structural concrete.
- Customer and revenue model: Project-based subcontracting for owners and general contractors, commonly bid as fixed-price, lump-sum, or unit-price scopes with progress billing and change orders; repeat business comes from contractor and developer relationships rather than subscription revenue.
- Deviation from default lens: none

## Executive view
Poured-concrete contractors have a real but bounded AI opportunity concentrated in estimating, project controls, administration, and compliance rather than the dominant physical craft workforce. The service remains operator-intensive and modest demand growth is plausible, but frequent rebidding should pass a meaningful share of cost savings to customers.

## How AI changes the work
AI can accelerate drawing and specification review, preliminary takeoffs, bid narratives, RFIs, submittals, schedule and daily-log synthesis, invoice coding, collections follow-up, safety-document drafting, and knowledge retrieval. Human estimators and project leaders remain accountable for scope gaps, quantities, constructability, sequencing, safety, and jobsite exceptions, while craft labor continues to perform the concrete work.

## Value capture
Savings on an awarded fixed-price scope can initially accrue to the contractor, and scarce-labor capacity can support more throughput. Over repeated bid cycles, however, general contractors and owners can compare bids and force part of the productivity gain into price; durable capture depends on proprietary operating data, lower rework, faster response, and customer reliability rather than access to a generic model.

## Firm availability
Most establishments in the industry are externally facing specialty contractors and therefore fit the service lens. Broad construction succession evidence indicates many planned exits, but internal transfers dominate and weak transition planning means stated intent will not translate one-for-one into purchasable control transactions.

## Demand durability
Concrete foundations and structural elements remain essential physical inputs, and BLS projects modest employment growth for the industry. Demand is nevertheless cyclical and end-market-specific; high rates, development pauses, or a shift to precast can hurt, while public infrastructure, manufacturing, power, and data-center projects can support volume.

## Risks and uncertainty
The key uncertainties are the absence of concrete-specific AI implementation and pass-through studies, construction-cycle volatility, misclassification and owner dependence in the estimated LMM population, safety and estimating liability, fragmented data, and the gap between succession intent and completed transferable deals. A poor outcome would combine low office-task savings with rapid bid-price pass-through and a downturn in cast-in-place project volume.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.25 | — | ESTIMATE | — |
| n | — | 288 | — | ESTIMATE | — |
| a | 0.09 | 0.15 | 0.23 | PROXY | S1, S3, S4 |
| rho | 0.35 | 0.58 | 0.75 | ESTIMATE | S4, S5 |
| e | 0.84 | 0.92 | 0.97 | ESTIMATE | S2 |
| s5 | 0.14 | 0.24 | 0.34 | PROXY | S6, S7 |
| q | 0.2 | 0.36 | 0.56 | ESTIMATE | S5 |
| d5 | 0.91 | 1.03 | 1.15 | PROXY | S8, S9, S10 |
| o | 0.95 | 0.98 | 1 | ESTIMATE | S2, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.32 | 0.87 | 1.73 | ESTIMATE |
| F | 5.71 | 6.70 | 7.34 | ESTIMATE |
| C | 4.00 | 7.20 | 10.00 | ESTIMATE |
| D | 8.64 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation mix is May 2023 and covers employers of all sizes, not only $1-10M EBITDA firms.
- a: Task exposure is researcher-assigned rather than observed for concrete contractors.
- a: The frozen compensation ratio is ancestor-level 23811 and mixes 2024 wages with 2022 receipts before harmonization.
- rho: The 92% hiring-difficulty figure covers construction firms broadly, not this six-digit industry or LMM firms specifically.
- rho: No longitudinal implementation study specific to concrete subcontractors was found.
- e: Eligibility is not directly observed and legal licensing and bonding requirements vary by state and project type.
- e: The supplied firm count is a margin bridge from size-class data, not an observed roster of LMM firms.
- s5: FMI/CFMA is a voluntary broad E&C survey, not a probability sample of NAICS 238110 LMM firms.
- s5: Stated exit intent can exceed completed transfers, and internal transitions may or may not meet the screen's control-transfer definition.
- q: No representative source directly measures AI-benefit pass-through for concrete subcontractors.
- q: Mix varies between negotiated repeat work, hard-bid public projects, and residential subcontracting, producing wide retention differences.
- d5: Employment projections are an indirect demand proxy and extend ten years rather than five.
- d5: The current Census spending release shows near-term construction softness but nominal spending is not the required constant-price, constant-quality quantity.
- d5: Concrete demand differs substantially across residential, data-center, manufacturing, commercial, and public infrastructure markets.
- o: Operator requirement is a five-year judgment, not directly measured.
- o: Prefabrication and vertical integration could matter more in selected end markets than the national average.

## Sources
- **S1** — [Poured Concrete Foundation and Structure Contractors — May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics5_238110.htm) (accessed 2026-07-22): NAICS 238110 occupation mix and wages: 255,210 total employment; construction and extraction 78.04%; cement masons and concrete finishers 34.09%; management 5.91%; business and financial operations 3.18%; detailed office occupations.
- **S2** — [2022 NAICS 238110 — Poured Concrete Foundation and Structure Contractors](https://www.census.gov/naics/?details=238110&input=238110&year=2022) (accessed 2026-07-22): Defines the industry as establishments primarily engaged in pouring and finishing concrete foundations and structural elements.
- **S3** — [Anthropic Economic Index report: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report) (accessed 2026-07-22): Reports that physical occupational categories including Construction & Extraction are underrepresented both in its AI-user survey and in Claude sessions.
- **S4** — [Generative AI and Jobs: A Refined Global Index of Occupational Exposure](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) (accessed 2026-07-22): Documents a task-level GenAI exposure framework based on 29,753 tasks, 52,558 worker data points, and expert review; supports treating occupational exposure as task-specific rather than job-wide.
- **S5** — [AGC/NCCER 2025 Craft Workforce Survey](https://www.nccer.org/research/2025-workforce-survey-agc-nccer/) (accessed 2026-07-22): Reports that 92% of surveyed construction companies had difficulty hiring for open positions, supporting the incentive to use technology for avoidable hiring and capacity.
- **S6** — [FMI Releases 2024 Study on Ownership Transfer and Management Succession](https://fmicorp.com/about/news/fmi-releases-2024-study-on-ownership-transfer-and-management-succession) (accessed 2026-07-22): Nearly 300 E&C leaders surveyed; 38% of owners planned to exit in three to five years, half of that group lacked an ownership transition plan, and 58% of all respondents lacked a plan.
- **S7** — [The Ownership Clock Is Running Out](https://fmicorp.com/insights/quick-reads/the-ownership-clock-is-running-out) (accessed 2026-07-22): FMI summarizes that 58% lack a formal transfer plan, 51% of owners planning to exit within five years lack a defined strategy, and about 64% plan internal transitions.
- **S8** — [Employment and output by industry, 2024–2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects NAICS 238110 employment from 258,200 in 2024 to 273,500 in 2034, a 5.9% increase.
- **S9** — [Masonry Workers — Occupational Outlook Handbook](https://www.bls.gov/ooh/construction-and-extraction/brickmasons-blockmasons-and-stonemasons.htm) (accessed 2026-07-22): Reports 206,700 cement masons and concrete finishers in 2024, 30% employed by poured-concrete contractors, physical work conditions, and 2% projected occupation growth through 2034.
- **S10** — [Value of Construction Put in Place — May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-22): Reports first-five-month 2026 construction spending of $858.4 billion, 2.7% below the same period of 2025, and May private nonresidential spending at a $738.7 billion annual rate.
