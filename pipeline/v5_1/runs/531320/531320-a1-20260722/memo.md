# 531320 — Offices of Real Estate Appraisers

*v5.1 Stage 1 research memo. Run `531320-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 5.47 · L 2.57 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is the large research, comparable-analysis, data, drafting, and review workload that AI can accelerate inside a fee-per-assignment professional service.
**Weakness:** The principal weakness is that the same technology enabling productivity also supports waivers and automated alternatives that can eliminate simple assignments and shift economics away from appraisal firms.

## Business-model lens
- Included: U.S. lower-middle-market firms that repeatedly provide independent residential or commercial real-estate appraisal and valuation services to external lenders, investors, owners, insurers, attorneys, governments, and other clients, including property research, inspection, comparable analysis, valuation modeling, review, and reporting.
- Excluded: Government assessor offices, captive bank or owner valuation departments, appraisal management companies without accountable appraisal work, automated-valuation software vendors, brokerage-only opinions, personal-property appraisal, shell entities, non-control financing situations, and firms outside the target normalized-EBITDA band.
- Customer and revenue model: Clients generally pay per-assignment professional fees, often at draft and final report milestones or as services are rendered; repeat lender, legal, tax, insurance, and portfolio relationships can provide recurring demand even though each appraisal is a discrete engagement.
- Deviation from default lens: none

## Executive view
Real-estate appraisal combines highly digitizable research and reporting with licensed, property-specific judgment. AI can improve throughput and consistency, but appraisal waivers, automated valuation models, and data-collection unbundling also threaten the simplest assignments and may shift value toward platforms and clients.

## How AI changes the work
AI can accelerate public-record research, comparable screening, data normalization, narrative drafting, report consistency checks, and internal review. The appraiser must still understand the evidence, inspect when required, resolve unusual facts, select and adjust comparables, protect confidential data, and take professional responsibility for the conclusion.

## Value capture
Per-assignment fees let firms retain some productivity gains until pricing resets. Lenders, appraisal management companies, and sophisticated clients can demand faster delivery or lower fees, while software costs, rework, review obligations, and substitution of routine assignments reduce retained benefit.

## Firm availability
External professional service is inherent to the code, but individual credentials, owner production, lender panels, reputation, and concentrated relationships can make firms difficult to transfer. The frozen count is especially uncertain because it uses a broad real-estate-services margin.

## Demand durability
Appraisals remain necessary for many commercial, litigation, tax, insurance, estate, and complex lending decisions. Residential mortgage demand is cyclical and increasingly exposed to waivers, hybrid products, standardized property data, and automated valuation.

## Risks and uncertainty
Key risks are appraisal-waiver expansion, AVM substitution, mortgage and transaction cyclicality, fee pressure from lenders and appraisal management companies, data quality, bias, confidentiality, model error, state licensure, USPAP compliance, client-panel concentration, owner dependence, and nontransferable credentials or approvals.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2858 | — | OBSERVED | — |
| n | — | 49 | — | ESTIMATE | — |
| a | 0.42 | 0.58 | 0.72 | ESTIMATE | S2, S3, S5 |
| rho | 0.32 | 0.48 | 0.64 | ESTIMATE | S3, S4, S5 |
| e | 0.55 | 0.73 | 0.86 | ESTIMATE | S1, S2, S5 |
| s5 | 0.05 | 0.11 | 0.2 | PROXY | S6 |
| q | 0.28 | 0.45 | 0.63 | ESTIMATE | S2, S5 |
| d5 | 0.82 | 0.99 | 1.16 | PROXY | S2, S4, S5 |
| o | 0.52 | 0.72 | 0.88 | PROXY | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.54 | 3.18 | 5.27 | ESTIMATE |
| F | 1.37 | 2.57 | 3.61 | ESTIMATE |
| C | 5.60 | 9.00 | 10.00 | ESTIMATE |
| D | 4.26 | 7.13 | 10.00 | PROXY |

## Caveats
- a: BLS combines appraisers with government assessors, while the lens excludes government assessor offices.
- a: No public source measures wage-weighted task exposure specifically for firms classified in 531320.
- a: Commercial, residential, litigation, tax, and portfolio valuation assignments have materially different task mixes.
- rho: Professional guidance describes responsibilities and risks but does not measure realized labor savings.
- rho: Enterprise mortgage modernization primarily addresses one-to-four-unit residential work, not the full 531320 service mix.
- rho: Faster analysis may increase review depth or throughput rather than reduce labor.
- e: The frozen firm count uses a 3.96% broad real-estate-operations margin rather than observed appraisal-firm EBITDA.
- e: BLS reports that 21% of the broader appraiser-and-assessor occupation is self-employed, highlighting owner dependence but not firm-level LMM eligibility.
- e: Licenses belong to individuals, and lender or client panel approvals may not transfer with company ownership.
- s5: Gallup covers all U.S. employer-business owners and measures intentions rather than completed appraisal-firm sales.
- s5: Internal and family transfers in the survey may not qualify as control transactions for the screen.
- s5: A sale of client relationships or hired appraisers may occur without a qualifying transfer of the firm.
- q: BLS and CBRE confirm fee-per-assignment or milestone billing but do not measure how automation savings are shared.
- q: Commercial and complex appraisal pricing is less standardized than residential mortgage-panel pricing.
- q: Automation may shift value to appraisal platforms, data vendors, lenders, or appraisal management companies rather than the appraisal office.
- d5: BLS employment combines appraisers with government assessors and is not a constant-quality service-demand measure.
- d5: CBRE is a global, integrated market leader whose valuation revenue includes price, mix, geography, and enterprise-client effects.
- d5: FHFA waiver policy applies to Enterprise residential mortgages, whereas 531320 also includes commercial and nonmortgage assignments.
- o: FHFA policy demonstrates eligibility expansion but does not state the realized share of all appraisal assignments waived.
- o: USPAP obligations apply when an appraisal assignment is performed; they do not guarantee that clients will continue ordering one.
- o: Residential mortgage automation may not generalize to commercial, litigation, tax, insurance, or unusual-property valuation.

## Sources
- **S1** — [North American Industry Classification System: Sector 53](https://www.census.gov/naics/resources/archives/sect53.html) (accessed 2026-07-22): Official 531320 definition; lens and e
- **S2** — [Property Appraisers and Assessors](https://www.bls.gov/ooh/business-and-financial/appraisers-and-assessors-of-real-estate.htm?src=feed) (accessed 2026-07-22): Appraisal duties, site work, licensure, fee-per-appraisal compensation, occupational composition, and 2024-2034 employment projection; a, e, q, d5, and o
- **S3** — [Practicing Appraisers: USPAP Q&A on Artificial Intelligence](https://appraisalfoundation.org/pages/practicing-appraisers) (accessed 2026-07-22): AI use, credibility, confidentiality, bias, and continuing need for appraiser judgment; a, rho, and o
- **S4** — [FHFA Announces Updates to Enterprise Policies on Appraisals, Loan Repurchase Alternatives, and Pricing Notifications](https://www.fhfa.gov/news/news-release/fhfa-announces-updates-to-enterprise-policies-on-appraisals-loan-repurchase-alternatives-and-pricing-notifications) (accessed 2026-07-22): Expanded purchase-loan appraisal-waiver and inspection-based-waiver eligibility; rho, d5, and o
- **S5** — [CBRE Group, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1138118/000113811826000005/cbre-20251231.htm) (accessed 2026-07-22): Valuation-service scope and milestone fees, AI investment, competitive risks, and 2025 and 2024 valuation revenue; a, rho, e, q, and d5
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year sale or transfer intentions among U.S. employer-business owners; s5
