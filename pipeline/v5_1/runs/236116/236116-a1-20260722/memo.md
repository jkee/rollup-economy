# 236116 — New Multifamily Housing Construction (except For-Sale Builders)

*v5.1 Stage 1 research memo. Run `236116-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.27 · L 0.65 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Complex, document-heavy project coordination gives AI a credible role in a high-value outsourced workflow that still requires an accountable contractor.
**Weakness:** Open-book contracting and a financing-sensitive construction cycle limit how much implemented efficiency becomes durable operator profit.

## Business-model lens
- Included: Lower-middle-market U.S. general contractors, design-build firms, and construction-management firms building new multifamily apartments and condominiums for external owners and developers, including high-rise, garden, town-house, low-income, and panelized projects.
- Excluded: For-sale or merchant builders constructing on their own account, owner-lessors constructing for their own portfolios, residential remodelers, specialty-trade subcontractors, prefabricated-building manufacturers, captive construction units, shells, and non-control financing vehicles.
- Customer and revenue model: Project-based outsourced construction for developers, investors, housing authorities, and institutional owners, commonly delivered under guaranteed-maximum-price, lump-sum, design-build, or construction-management arrangements; repeatability comes from a continuing pipeline of projects and repeat developer relationships rather than subscription revenue.
- Deviation from default lens: none

## Executive view
Multifamily GCs have a low internal compensation share but a comparatively information-dense internal workforce, making estimating, project controls, documentation, finance, and reporting plausible AI targets. The opportunity is constrained commercially by transparent GMP contracting and strategically by a cooling, capital-intensive project market.

## How AI changes the work
AI can extract and reconcile drawings, submittals, invoices, and contracts; accelerate estimates and bid packages; draft RFIs and owner reports; monitor schedules and procurement; and support document control and compliance review. It cannot independently accept construction risk, inspect unique site conditions, direct trades through disruptions, assure safety and quality, or negotiate among owners, architects, lenders, and subcontractors.

## Value capture
Open-book GMP structures dominate reported multifamily practice, so direct job-cost savings often flow to the owner or reduce use of contingency rather than increasing contractor profit. Retention is stronger in fixed fees, central overhead, risk reduction, bid capacity, and schedule performance, but sophisticated owners and competitive rebids can claim much of the visible benefit over five years.

## Firm availability
Most firms are outsourced contractors by industry definition, and professional teams, backlog, systems, and bonding relationships can transfer. Eligibility and sale probability are reduced by project joint ventures, customer concentration, founder-controlled relationships, contingent liabilities, working-capital demands, and misclassified own-account development.

## Demand durability
The market is absorbing a record completion wave while vacancies, financing costs, and construction costs pressure new starts. A near-term contraction followed by stabilization is more plausible than uninterrupted growth. Nearly all projects that proceed still require a legally and operationally accountable contractor even as software reduces coordination effort.

## Risks and uncertainty
Occupation evidence is available only for broad residential construction, contract-mix evidence is advisory rather than representative, AI surveys blend owners and contractors, and transfer evidence is cross-industry. The frozen labor ratio mixes 2024 wages with 2022 receipts, and the LMM firm count is margin-bridged. Multifamily starts are unusually volatile and differ sharply by metro and financing regime.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0771 | — | OBSERVED | — |
| n | — | 780 | — | ESTIMATE | — |
| a | 0.26 | 0.4 | 0.55 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.53 | 0.72 | PROXY | S5, S6 |
| e | 0.58 | 0.74 | 0.88 | ESTIMATE | S1 |
| s5 | 0.1 | 0.18 | 0.27 | PROXY | S7, S8 |
| q | 0.24 | 0.4 | 0.57 | PROXY | S9, S10 |
| d5 | 0.64 | 0.92 | 1.2 | PROXY | S11, S12 |
| o | 0.91 | 0.97 | 0.995 | ESTIMATE | S1, S3, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.65 | 1.22 | PROXY |
| F | 6.17 | 7.48 | 8.41 | ESTIMATE |
| C | 4.80 | 8.00 | 10.00 | PROXY |
| D | 5.82 | 8.92 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is only available for NAICS 236100 and excludes self-employed workers.
- a: The inference that multifamily firms have a more professional and less craft-heavy internal mix is not directly measured.
- a: Task applicability does not imply that entire jobs can be removed, especially where review and liability remain human.
- rho: Survey measures combine current use, pilots, scaling, and future investment rather than implemented labor savings.
- rho: Grant Thornton combines construction and real estate and discusses owners and property managers as well as contractors.
- rho: AGC respondents span construction segments and include firms larger than the target band.
- e: The frozen firm count is a margin-bridged estimate rather than an observed EBITDA-band count.
- e: NAICS codes do not identify captive contractors, temporary joint ventures, customer concentration, or transferable bonding capacity.
- e: Contractors can participate economically in development projects even when classified as third-party builders.
- s5: Gallup is cross-industry and not restricted to the LMM EBITDA band.
- s5: Construction-services transaction counts have no industry-specific denominator and skew toward other verticals.
- s5: Owner intentions and announced transactions do not guarantee qualifying completed control transfers.
- q: Contract type is an indirect proxy for discounted benefit retention.
- q: The multifamily contract-mix figures come from an advisory article rather than a published representative sample.
- q: Actual savings ownership depends on negotiated fee, contingency, allowance, shared-savings, and change-order clauses.
- d5: Housing-start units are not a direct measure of contractor service quantity or constant-quality output.
- d5: The Census monthly annualized rate is volatile and NAHB's forecast extends explicitly only through 2027.
- d5: Both sources include delivery models outside NAICS 236116 and national averages conceal large metro differences.
- o: No source directly measures the future share requiring this operator type.
- o: Large developers may internalize construction management or create captive entities outside the screened lens.
- o: Modular delivery and integrated platforms could shift more coordination away from independent GCs than assumed.

## Sources
- **S1** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines NAICS 236116 as general contractors constructing new multifamily housing and includes multifamily design-build and construction-management firms; excludes own-account for-sale builders, remodelers, specialty trades, prefabricated-building manufacturers, and owner-lessors.
- **S2** — [BLS May 2023 Occupational Employment and Wage Estimates: Residential Building Construction](https://www.bls.gov/oes/2023/may/naics4_236100.htm) (accessed 2026-07-22): Reports management occupations at 120,890 jobs, 13.05% of NAICS 236100 employment, and business/financial operations at 81,990 jobs, 8.85%, including 59,800 construction managers, 36,330 project-management specialists, and 14,600 cost estimators.
- **S3** — [O*NET OnLine: Construction Managers](https://www.onetonline.org/link/summary/11-9021.00) (accessed 2026-07-22): Lists construction-manager tasks including compliance inspection, scheduling, budgets and reports, contracts, plan interpretation, permits, trade oversight, and resolution of site problems.
- **S4** — [Working with AI: Measuring the Occupational Implications of Generative AI](https://www.microsoft.com/en-us/research/publication/working-with-ai-measuring-the-occupational-implications-of-generative-ai/) (accessed 2026-07-22): Analyzes 200,000 anonymized Copilot conversations and finds the highest AI applicability in knowledge work, including office and administrative support, with common activities in information gathering, writing, providing information, and advising.
- **S5** — [AGC 2026 Construction Hiring and Business Outlook](https://www.agc.org/sites/default/files/users/user21902/2026%20Construction%20Hiring%20and%20Business%20Outlook%20Report_Final.pdf) (accessed 2026-07-22): Reports 61% of contractor respondents use AI or plan increased investment, including 45% in office and administrative work, 23% in estimating, and 20% in design or preconstruction; the survey had 951 respondents.
- **S6** — [Grant Thornton: Multifamily AI Growth Starts with Governance](https://www.grantthornton.com/insights/articles/real-estate/2026/multifamily-ai-growth-starts-with-governance) (accessed 2026-07-22): Reports 50% of surveyed construction and real-estate leaders are piloting AI, 36% are scaling it across functions, 63% cite efficiency gains, and only 13% are confident of passing an AI-governance audit within 90 days.
- **S7** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 52.3% of U.S. employer businesses have owners age 55 or older; 14% of working owners planned a sale, public offering, or transfer within five years, rising to 17% among owners at least 55.
- **S8** — [Capstone Partners Construction Services M&A Update](https://www.capstonepartners.com/insights/article-construction-ma-update/) (accessed 2026-07-22): Reports 562 announced or closed construction-services transactions in 2025, up 18.2% from 2024; private-equity buyers represented 54.3% of sector transactions.
- **S9** — [Fident Capital: Understanding Construction Contract Types](https://fidentcapital.com/understanding-construction-contract-types-a-complete-overview/) (accessed 2026-07-22): States GMP contracts account for 60-70% of multifamily deals, lump-sum contracts 20-30%, and uncapped cost-plus less than 5%, and describes GMP as open-book with contractor exposure above the maximum.
- **S10** — [AIA A133-2019 Owner and Construction Manager Agreement, Cost Plus with GMP](https://designshop.aia.org/products/a133-2019-standard-form-of-agreement-between-owner-and-construction-manager-as-constructor-where-the-basis-of-payment-is-the-cost-of-the-work-plus-a-fee-with-a-guaranteed-maximum-price) (accessed 2026-07-22): Describes a standard large-project agreement where a construction manager provides preconstruction and construction services and becomes bound to complete labor and materials at or below an accepted guaranteed maximum price.
- **S11** — [U.S. Census Bureau Monthly New Residential Construction, June 2026](https://www.census.gov/construction/nrc/current/) (accessed 2026-07-22): Reports a June 2026 seasonally adjusted annual rate of 513,000 starts and 413,000 completions in buildings with five units or more.
- **S12** — [NAHB: Multifamily Market Expected to Cool in 2026 as Vacancies Rise](https://www.nahb.org/news-and-economics/press-releases/2026/02/multifamily-market-expected-to-cool-in-2026-as-vacancies-rise) (accessed 2026-07-22): Forecasts multifamily starts at 413,000 in 2025, 392,000 in 2026, and 367,000 in 2027 before leveling near pre-pandemic rates; reports a 7.3% vacancy rate in December and 608,000 completions in 2024.
