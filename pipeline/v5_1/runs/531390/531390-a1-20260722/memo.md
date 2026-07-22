# 531390 — Other Activities Related to Real Estate

*v5.1 Stage 1 research memo. Run `531390-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 6.88 · L 4.18 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Document, record, coordination, and reporting work is pervasive across repeat real estate service workflows and is amenable to controlled AI assistance.
**Weakness:** Heterogeneous service lines, adjacent-code boundaries, cyclical transaction exposure, fiduciary risk, and a margin-sensitive estimated firm stock limit confidence.

## Business-model lens
- Included: US lower-middle-market real estate escrow agencies, listing-service operators, real estate fiduciaries, landman and right-of-way service firms, real estate consultants other than agents or appraisers, and real estate asset-management service firms other than property managers, when they repeatedly serve unaffiliated customers for transaction, project, retainer, data-access, or administration fees.
- Excluded: Lessors, real estate agents and brokers, property managers, appraisers, title abstract and settlement offices classified in 541191, title insurers, captive owner or developer departments, shells, and firms without a repeat external-customer service model.
- Customer and revenue model: Customers include lenders, buyers and sellers, investors, developers, energy and infrastructure companies, and property owners. Revenue is typically earned through per-transaction escrow or administration charges, project fees, recurring listing or data access, retainers, or asset-management fees rather than ownership of the underlying property.
- Deviation from default lens: none

## Executive view
Other real estate services combine document-heavy transaction administration, data and listing workflows, land and rights research, fiduciary work, and bespoke advice. AI can assist a large share of information processing, but the code is heterogeneous and the operator often remains responsible for funds, exceptions, client judgment, and legally consequential outputs.

## How AI changes the work
Useful applications include document intake and extraction, parcel and public-record retrieval, closing-file and contract checks, listing normalization, market and comparable research, report drafts, scheduling, customer updates, fee calculations, and internal policy retrieval. Humans remain central to negotiation, funds authorization, fiduciary decisions, field investigation, exception resolution, advice, and final approval.

## Value capture
Transaction, project, subscription, retainer, and asset-management fees can preserve savings within current contracts, but institutional procurement, digital competition, renewals, and customer expectations can pass benefits through. Data, integration, cyber, insurance, compliance, and quality-control costs reduce retained value.

## Firm availability
The estimated LMM stock includes plausible independent escrow, listing, landman, fiduciary, consulting, and asset-management service firms, but eligibility and margins vary by service line. Adjacent-code classification, captive operations, key-person relationships, licenses, and nontransferable referral books reduce the conventional acquisition population.

## Demand durability
Real estate finance, transfers, development, and rights administration remain recurring economic needs, while the service mix is exposed to property and credit cycles. Digital self-service can remove basic listings and document handling, but accountable escrow, fiduciary, exception, and advisory functions should persist.

## Risks and uncertainty
Key risks are code heterogeneity, boundary misclassification, the margin-bridged firm count, cyclical transaction volume, wire fraud, mishandled client funds, document and record errors, state-law variation, cyber incidents, data quality, professional liability, customer concentration, key-person dependence, and software shifting work to lenders, title firms, or customers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3851 | — | OBSERVED | — |
| n | — | 162 | — | ESTIMATE | — |
| a | 0.3 | 0.5 | 0.68 | PROXY | S1, S2, S3, S4, S5 |
| rho | 0.34 | 0.56 | 0.74 | ESTIMATE | S3, S4, S5 |
| e | 0.42 | 0.64 | 0.82 | ESTIMATE | S1 |
| s5 | 0.06 | 0.12 | 0.2 | PROXY | S6 |
| q | 0.34 | 0.54 | 0.72 | ESTIMATE | — |
| d5 | 0.9 | 1.1 | 1.25 | PROXY | S7 |
| o | 0.64 | 0.82 | 0.94 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.57 | 4.31 | 7.75 | ESTIMATE |
| F | 2.62 | 4.18 | 5.34 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 5.76 | 9.02 | 10.00 | ESTIMATE |

## Caveats
- a: The available occupation mix is for all real estate at NAICS 531000, not 531390.
- a: O*NET title-examiner and broker roles are adjacent workflow proxies; Census classifies title abstract offices and real estate brokers outside 531390.
- a: The six-digit code mixes escrow, listing, fiduciary, landman, consulting, and asset-management services with different task structures.
- a: The injected compensation ratio uses a 2024 wage numerator and 2022 receipts denominator, although it is six-digit and MED quality.
- rho: No source measures five-year implementation of exposed work in 531390.
- rho: Implementation should vary sharply between standardized escrow or listing workflows and bespoke landman, fiduciary, or consulting engagements.
- rho: Digital closing and document tools may shift work between lenders, title firms, and escrow providers rather than remove it from the chain.
- e: The public code definition establishes activities but not the share of LMM firms meeting the recurring-service and transferability lens.
- e: Primary-activity classification is difficult near the boundaries with title settlement, brokerage, property management, appraisal, and title insurance.
- e: The injected n of 162 is margin-bridged using a 3.96% real-estate-operations-and-services margin and carries ESTIMATE quality; service-line margins may differ materially.
- s5: Gallup covers employer businesses across industries and reports intentions rather than completed external control transfers.
- s5: Internal succession, employee ownership, dissolution, and client-book migration do not necessarily constitute qualifying transfers.
- s5: Private deal databases may omit small transactions and asset sales.
- q: No cited source measures retention of implemented AI benefits in this industry.
- q: Escrow transaction fees, listing subscriptions, landman project rates, and fiduciary or asset-management fees have different pass-through dynamics.
- q: Efficiency may be used to reduce closing time or strengthen controls rather than lower cost or expand margin.
- d5: The BLS projection covers all real estate, including lessors and activities outside 531390.
- d5: Property output is not the same quantity as transaction-support and advisory services.
- d5: A five-year endpoint may land at a different point in the property and credit cycle.
- o: No source directly measures the future operator-required share across this heterogeneous code.
- o: Settlement-agent requirements and permitted escrow arrangements vary by transaction and state.
- o: Listing and basic information services face more direct software substitution than fiduciary, funds-control, landman, or bespoke consulting work.

## Sources
- **S1** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 531390 as other real estate-related services and lists real estate escrow agencies, listing services, fiduciaries' offices, and landman services, while identifying excluded adjacent activities.
- **S2** — [BLS May 2023 Occupational Employment and Wage Estimates: NAICS 531000 Real Estate](https://www.bls.gov/oes/2023/may/naics3_531000.htm) (accessed 2026-07-22): Reports the broad real estate occupation mix, including 20.11% management, 18.16% sales, 18.18% office support, 8.34% business and financial operations, and 1.00% computer and mathematical occupations.
- **S3** — [O*NET OnLine: Title Examiners, Abstractors, and Searchers](https://www.onetonline.org/link/details/23-2093.00) (accessed 2026-07-22): Describes adjacent record-intensive tasks including examining legal documents, preparing reports and instrument lists, verifying completeness, entering records, checking closing files, and resolving title-related problems.
- **S4** — [O*NET OnLine: Real Estate Brokers](https://www.onetonline.org/link/summary/41-9021.00) (accessed 2026-07-22): Describes adjacent real estate information and advisory tasks including computerized listings, contract monitoring, market analysis, transaction review, negotiation, compliance, and database entry.
- **S5** — [CFPB Assessment of the TILA-RESPA Integrated Disclosure Rule](https://files.consumerfinance.gov/f/documents/cfpb_trid-rule-assessment_report.pdf) (accessed 2026-07-22): Explains that settlement companies include escrow companies and that settlement agents ensure closing requirements are met, documents are complete, fees are collected, signatures obtained, and deeds recorded.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of employer-business owners planned to sell or transfer ownership within five years, used as a broad succession-intention proxy.
- **S7** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects broad NAICS 531000 real estate output to rise from $2,258.7 billion in 2024 to $2,721.0 billion in 2034, a 1.9% compound annual rate in chained 2017 dollars.
