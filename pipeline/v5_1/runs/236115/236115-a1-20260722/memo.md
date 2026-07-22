# 236115 — New Single-Family Housing Construction (except For-Sale Builders)

*v5.1 Stage 1 research memo. Run `236115-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.73 · L 1.23 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can compress the document-heavy coordination layer around a large and persistent physical construction workflow.
**Weakness:** Cyclical project demand and founder-dependent local relationships can undermine both predictable cash flow and transferable enterprise value.

## Business-model lens
- Included: Lower-middle-market U.S. general contractors, design-build firms, and construction-management firms building new single-family homes for external owners, including detached, attached, modular, and prefabricated homes assembled on site.
- Excluded: For-sale or merchant builders constructing on their own account, residential remodelers, specialty-trade subcontractors, manufactured-home setup contractors, captive construction units, shells, and non-control financing vehicles.
- Customer and revenue model: Project-based outsourced construction for homeowners, investors, or other owners, commonly under fixed-price or cost-plus contracts; repeatability comes from a continuing sequence of customer projects rather than subscription revenue.
- Deviation from default lens: none

## Executive view
Custom single-family general contractors combine a modest labor-cost base with a real but bounded AI opportunity concentrated in estimating, documentation, scheduling, procurement, and office administration. The physical, local, and accountable parts of delivery remain resistant to full substitution, while project cyclicality and founder dependence complicate transferability.

## How AI changes the work
AI can draft and summarize RFIs, contracts, bids, budgets, progress reports, permits, and customer communications; extract plan and invoice data; assist takeoffs and estimating; and flag schedule or procurement risks. It is less able to inspect unique sites, sequence trades under changing conditions, negotiate with local subcontractors, assure code compliance, or accept project liability.

## Value capture
Fixed-price contracts allow a contractor to retain labor savings during an awarded project, but cost-plus transparency and competitive rebidding return part of visible savings to customers. Benefits expressed as faster response, fewer errors, increased bidding capacity, and more reliable completion may persist longer than simple clerical cost reductions.

## Firm availability
Most establishments are external-customer contractors by definition, but LMM eligibility is reduced by own-account development, episodic project flow, customer concentration, and businesses built around the founder's license and local reputation. Aging owners and active construction M&A support transfer flow, yet many exits may be closures or internal transitions rather than qualifying control sales.

## Demand durability
Five-year real demand is likely near today's level but has a wide cyclical range. Household formation and constrained housing supply support construction, while mortgage rates, land availability, permitting, materials costs, and regional migration can sharply change starts. For demand that remains, an accountable operator is still needed to coordinate physical construction and compliance.

## Risks and uncertainty
The best occupation data cover all residential building construction, not this six-digit industry, and exclude self-employed workers. AI adoption surveys skew broad and possibly large-firm. Contract evidence comes from software users. The frozen labor and firm-count inputs have vintage and model bridges, and custom builders' project economics can blur into for-sale development.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2334 | — | OBSERVED | — |
| n | — | 4486 | — | ESTIMATE | — |
| a | 0.18 | 0.28 | 0.38 | PROXY | S2, S3, S4 |
| rho | 0.3 | 0.47 | 0.68 | PROXY | S5 |
| e | 0.5 | 0.64 | 0.8 | ESTIMATE | S1 |
| s5 | 0.1 | 0.18 | 0.27 | PROXY | S6, S7 |
| q | 0.38 | 0.55 | 0.72 | PROXY | S8 |
| d5 | 0.78 | 1.02 | 1.2 | PROXY | S9, S10 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.50 | 1.23 | 2.41 | PROXY |
| F | 8.71 | 10.00 | 10.00 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | PROXY |
| D | 6.86 | 9.69 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is available only for broader NAICS 236100 and excludes self-employed workers.
- a: The task-to-exposure classification is judgmental and does not measure tasks already automated.
- a: Generative-AI applicability is not the same as full labor substitution, especially for safety- and liability-sensitive work.
- rho: The AGC measure combines current use with intended investment and does not quantify labor savings.
- rho: The survey spans construction segments and firm sizes rather than NAICS 236115 LMM firms.
- rho: Five-year implementation depends on software integration and data standardization not measured by the source.
- e: The frozen firm-count estimate is margin-bridged and may include firms outside a normalized $1-10M EBITDA band.
- e: NAICS classification does not reveal customer concentration, owner dependence, or recurring project cadence.
- e: Custom-home builders can shift between contract building and own-account development.
- s5: Gallup is cross-industry and includes businesses outside the LMM band.
- s5: Construction-services deal counts are not a denominator-based transfer rate and are not specific to custom-home GCs.
- s5: Stated owner plans may not become completed qualifying transfers.
- q: Contract form is an indirect proxy for discounted benefit retention.
- q: The source is a construction-software vendor's customer-project sample from 2018-2020.
- q: The estimate does not assume demand growth or implementation success, which belong in other primitives.
- d5: The Census starts series includes homes built for sale and therefore does not isolate NAICS 236115.
- d5: BLS employment is a labor-input projection, not a direct demand-volume forecast.
- d5: Five-year residential construction outcomes are unusually sensitive to financing conditions and local supply constraints.
- o: No source directly measures the year-five operator-required share.
- o: Modular construction and platform-based procurement could shift more coordination away from local GCs than assumed.
- o: State licensing, permitting, and liability rules vary materially.

## Sources
- **S1** — [2022 NAICS Definition: 236115 New Single-Family Housing Construction (except For-Sale Builders)](https://www.census.gov/naics/?details=236115&input=236115&year=2022) (accessed 2026-07-22): Defines the industry as general contractors responsible for entire new single-family construction and includes design-build, construction-management, modular, and prefabricated on-site assembly; excludes own-account for-sale builders and remodelers.
- **S2** — [BLS OEWS Data Tables for Industry Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Residential Building Construction's largest occupations include 215,170 carpenters, 138,930 construction laborers, 79,550 trade supervisors, 55,510 construction managers, 43,560 general managers, 39,980 project-management specialists, 37,120 office clerks, 24,940 bookkeeping clerks, 24,440 service sales representatives, and 20,660 administrative assistants.
- **S3** — [O*NET OnLine: Construction Managers](https://www.onetonline.org/link/summary/11-9021.00) (accessed 2026-07-22): Lists construction-manager tasks including compliance inspection, scheduling, budget and progress reporting, contracts, permits, plan interpretation, field supervision, and resolution of site problems.
- **S4** — [Working with AI: Measuring the Occupational Implications of Generative AI](https://www.microsoft.com/en-us/research/publication/working-with-ai-measuring-the-occupational-implications-of-generative-ai/) (accessed 2026-07-22): Analyzes 200,000 anonymized Copilot conversations and finds common successful AI work activities in information gathering, writing, providing information, teaching, and advising.
- **S5** — [AGC 2026 Construction Hiring and Business Outlook](https://www.agc.org/sites/default/files/users/user21902/2026%20Construction%20Hiring%20and%20Business%20Outlook%20Report_Final.pdf) (accessed 2026-07-22): Reports that 61% of respondents use AI or plan to increase investment, including 45% for office and administrative work, 23% for estimating, and 20% for design or preconstruction.
- **S6** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 52.3% of U.S. employer businesses are owned by people age 55 or older and 14% of working owners expected to sell, go public, or transfer ownership within five years.
- **S7** — [Capstone Partners Construction Services M&A Update](https://www.capstonepartners.com/insights/article-construction-ma-update/) (accessed 2026-07-22): Reports 562 announced or closed construction-services transactions in 2025, up 18.2% from 2024, with private-equity buyers representing 54.3% of sector transactions.
- **S8** — [CoConstruct: Builders Use Fixed Price Construction Contracts 80% of the Time](https://www.coconstruct.com/blog/builders-use-fixed-price-construction-contracts-80-of-the-time) (accessed 2026-07-22): Analyzes over 38,000 residential projects from 2018-2020 and reports fixed-price use of 71.5% for builders doing one or two homes annually, 77.2% for three or four, and 84.8% for ten or more.
- **S9** — [U.S. Census Bureau Monthly New Residential Construction, June 2026](https://www.census.gov/construction/nrc/current/) (accessed 2026-07-22): Reports June 2026 single-family housing starts at a seasonally adjusted annual rate of 895,000, 0.2% below the revised May rate.
- **S10** — [BLS Employment and Output by Industry Projections](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects Residential Building Construction employment from 943,100 to 982,400 over the published decade, a 4.2% increase or 0.4% annually.
