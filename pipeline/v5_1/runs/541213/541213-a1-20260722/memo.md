# 541213 — Tax Preparation Services

*v5.1 Stage 1 research memo. Run `541213-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.68 · L 3.52 · interval CONDITIONAL → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large labor share sits in repeat document, calculation, research, and review workflows that can be compressed while customers continue buying a completed return.
**Weakness:** The technology that improves operator productivity can also shift simple returns to self-service and weaken long-run pricing retention.

## Business-model lens
- Included: US lower-middle-market firms whose primary business is preparing and filing tax returns for external individual or small-business customers, including related return review and client explanation within the engagement.
- Excluded: CPA offices, bookkeeping, payroll, billing, captive tax departments, tax software sold without an accountable service operator, volunteer preparation, non-control financing vehicles, and firms outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: Annual or repeat outsourced tax-return engagements, generally priced per return and by form or complexity, with some add-on representation or advisory fees; revenue and staffing are highly concentrated in filing season.
- Deviation from default lens: none

## Executive view
Pure-play tax preparation is a repeat, externally purchased service with unusually document-heavy workflows and a statutory demand anchor. The opportunity is to automate intake, first-pass preparation, research, and review support while retaining a responsible preparer for exceptions and sign-off. The central tension is that the same technology can strengthen operator margins and make self-preparation or price competition easier.

## How AI changes the work
AI can classify source documents, extract fields, reconcile records, draft client questions, retrieve tax authority, populate workpapers, and flag anomalies before review. O*NET shows that calculation, record examination, verification, research, and client explanation all sit inside the core job (S3). Adoption is accelerating (S5, S6), but TaxCalcBench's sub-one-third success rate on simplified returns makes governed integration with deterministic tax software and human review more credible than autonomous filing (S4).

## Value capture
Because customers commonly buy a completed return at a form- or complexity-based price, fewer production hours do not mechanically reduce the invoice (S10). H&R Block's fiscal 2025 net average charge and assisted revenue growth show pricing can coexist with roughly flat volume (S9). Retention should still erode over time through renewal repricing, customer switching, free or low-cost software, and rivals adopting the same tools.

## Firm availability
The six-digit industry definition is narrow and most LMM firms should fit the outsourced-service lens (S1), although owner dependence, franchise restrictions, compliance quality, and weak books can make a firm ineligible. Broad employer-owner intentions suggest roughly one qualifying transfer opportunity in five over five years, and observed accounting/tax practice sales confirm a functioning market, but neither source directly measures the frozen LMM population (S7, S8).

## Demand durability
IRS forecasts imply slow growth in individual-return counts through 2031 and somewhat faster partnership-return growth (S11). Filing obligations and tax complexity support the underlying work basket, while current channel data still place professional and self-prepared e-file volumes near parity (S12). Operator-required demand is therefore durable but not protected: simple returns can migrate to software, while complex returns retain greater need for judgment and accountability.

## Risks and uncertainty
The largest evidence gaps are a six-digit wage-weighted task map, completed-transfer incidence for LMM tax firms, and longitudinal unit economics after automation. Survey adoption can be promotional, broad-industry staffing may misstate pure-play work, and preparer-channel statistics include CPA firms. Material downside would arise if integrated AI makes complex self-service reliable, price competition passes savings through quickly, or target firms prove too owner-dependent to transfer.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5877 | — | OBSERVED | — |
| n | — | 40 | — | ESTIMATE | — |
| a | 0.42 | 0.56 | 0.68 | PROXY | S2, S3, S4 |
| rho | 0.45 | 0.62 | 0.78 | PROXY | S4, S5, S6 |
| e | 0.75 | 0.86 | 0.94 | ESTIMATE | S1, S8 |
| s5 | 0.15 | 0.23 | 0.33 | PROXY | S7, S8 |
| q | 0.55 | 0.72 | 0.85 | ESTIMATE | S9, S10, S12 |
| d5 | 0.94 | 1.03 | 1.1 | PROXY | S11 |
| o | 0.41 | 0.49 | 0.57 | PROXY | S4, S12, S14 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 4.44 | 8.16 | 10.00 | PROXY |
| F | 2.74 | 3.52 | 4.18 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 3.85 | 5.05 | 6.27 | PROXY |

## Caveats
- a: BLS publishes the cited staffing pattern at NAICS 541200, which also includes CPA, bookkeeping, and payroll businesses.
- a: O*NET task importance is not time share, wage share, or AI substitutability.
- a: TaxCalcBench finds frontier models completed fewer than one-third of simplified federal returns correctly, so exposure should not be read as safe autonomous execution (S4).
- rho: The surveys cover broader tax and accounting populations, including large firms and non-US respondents in the Thomson Reuters sample.
- rho: Reported use or perceived productivity does not establish avoided hiring or sustained labor removal.
- rho: Five-year implementation depends on integration with deterministic tax engines and secure client-data systems, not general-purpose model capability alone.
- e: No source measures eligibility among the specific frozen LMM firm universe.
- e: The frozen n estimate is margin-bridged from size-class data and may misclassify firms whose normalized EBITDA differs from the assumed industry margin.
- e: An establishment can fit the NAICS definition yet fail buyer diligence or lack transferable goodwill.
- s5: Stated plans are not realized transfers and the Gallup population spans all industries and business sizes.
- s5: BizBuySell has no complete industry denominator and its reported accounting/tax practices often fall below the target EBITDA band.
- s5: Retirement can lead to closure or client-book runoff rather than a qualifying control transfer.
- q: H&R Block's brand, scale, refund products, and national marketing may overstate independent LMM pricing power.
- q: The estimate concerns retention of implemented gross benefit, not revenue growth, demand, or implementation success.
- q: Self-prepared e-file volume was growing faster than professionally prepared e-file volume at the March 2026 snapshot, increasing competitive sharing risk (S12).
- d5: IRS projections are national filing counts and do not isolate paid preparation or NAICS 541213.
- d5: The projection models extrapolate filing patterns and do not fully encode future tax-law simplification or major administrative redesign.
- d5: Return count is an imperfect measure of constant-quality service quantity because complexity varies materially across returns.
- o: The March 2026 data are an in-season snapshot and channel mix changes around deadlines and extensions.
- o: IRS professional e-file statistics include CPA and other firms outside NAICS 541213.
- o: An operator may remain legally or practically accountable while requiring far fewer labor hours; that labor effect belongs in a and rho, not o.

## Sources
- **S1** — [North American Industry Classification System: Sector 54, 541213 Tax Preparation Services](https://www.census.gov/naics/resources/archives/sect54.html) (accessed 2026-07-22): Defines 541213 as non-CPA establishments preparing tax returns without bookkeeping, billing, or payroll, and states that basic tax-law and filing knowledge is required.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 541200](https://www.bls.gov/oes/2023/May/naics4_541200.htm) (accessed 2026-07-22): Reports occupation shares and wages for the broader accounting, tax preparation, bookkeeping, and payroll industry, including accountants, tax preparers, bookkeeping clerks, and administrative occupations.
- **S3** — [O*NET OnLine: Tax Preparers 13-2082.00](https://www.onetonline.org/link/details/13-2082.00) (accessed 2026-07-22): Lists core tasks and work activities including tax computation, form completion, deduction selection, client interviews, record review, error checking, research, advice, and explanation of tax law.
- **S4** — [TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task](https://arxiv.org/abs/2507.16126) (accessed 2026-07-22): Finds state-of-the-art models correctly calculate fewer than one-third of federal returns in a simplified sample and documents tax-table, calculation, and eligibility errors.
- **S5** — [From Incubation to Integration: Generative AI Adoption Nearly Doubles as Professional Services Reach Crossroads](https://www.thomsonreuters.com/en/press-releases/2025/april/from-incubation-to-integration-generative-ai-adoption-nearly-doubles-as-professional-services-reach-crossroads) (accessed 2026-07-22): Reports tax-firm enterprise GenAI adoption rising from 8% to 21%, 79% expecting significant integration by 2027, and tax-return preparation as a use case among 63% of tax/accounting GenAI users.
- **S6** — [7 insights for firm growth, efficiency and a competitive edge](https://accountants.intuit.com/taxprocenter/practice-management/insights-for-growth-efficiency-and-a-competitive-edge/) (accessed 2026-07-22): Summarizes Intuit's April 2025 survey of 700 US accounting professionals, including 46% daily AI use, 81% reporting productivity gains, and stated automation patterns.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 52.3% of US employer businesses have owners age 55 or older and 22% of employer-business owners planned to sell or transfer ownership within five years.
- **S8** — [Accounting & Tax Practice Business Valuation Multiples & Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/accounting-cpa-tax-practice/) (accessed 2026-07-22): Documents a market for independent and franchise accounting/tax practices, reported sales during 2021-2025, a 2025 median sale price of $500,000, and transaction multiples.
- **S9** — [H&R Block, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/12659/000160529725000016/hrb-20250630.htm) (accessed 2026-07-22): Reports US assisted revenue up 6.1%, net average charge up 5.1%, company-owned return volume up 1.0%, total assisted volume down 0.9%, strong seasonality, and franchise/competitor acquisitions.
- **S10** — [Know the cost of tax preparation with H&R Block upfront pricing](https://www.hrblock.com/tax-offices/upfront-pricing/) (accessed 2026-07-22): Shows upfront per-engagement pricing based on customer circumstances, forms, states, and add-ons rather than an explicit cost-plus labor contract.
- **S11** — [IRS Publication 6292: Fiscal Year Return Projections for the United States, 2025-2032](https://www.irs.gov/pub/irs-access/p6292_accessible.pdf) (accessed 2026-07-22): Projects FY2026 and FY2031 return counts, including individual income-tax returns of 164.135 million and 168.570 million, partnerships of 5.200 million and 5.630 million, and corporations of 8.259 million and 8.463 million.
- **S12** — [Filing season statistics for week ending March 20, 2026](https://www.irs.gov/newsroom/filing-season-statistics-for-week-ending-march-20-2026) (accessed 2026-07-22): Reports 39.738 million professionally prepared e-file returns and 37.836 million self-prepared e-file returns, with year-over-year changes of negative 1.0% and positive 1.9%, respectively.
- **S13** — [Important Considerations as You Select Your Return Preparer This Filing Season](https://www.taxpayeradvocate.irs.gov/news/nta-blog/important-considerations-as-you-select-your-return-preparer-this-filing-season/2024/03/) (accessed 2026-07-22): States that over 54% of individual income-tax returns were prepared by paid preparers and describes PTIN, due-diligence, credential, representation, and preparer-responsibility distinctions.
- **S14** — [Paid Tax Return Preparers: Opportunities Remain to Improve IRS Oversight](https://www.gao.gov/products/gao-26-108723) (accessed 2026-07-22): States that more than half of individual taxpayers used paid preparers in FY2024 and explains PTIN, tax-code, credential, error, and oversight requirements.
