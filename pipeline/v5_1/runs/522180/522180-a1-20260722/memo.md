# 522180 — Savings Institutions and Other Depository Credit Intermediation

*v5.1 Stage 1 research memo. Run `522180-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Recurring spread-and-fee financial services contain large rule-bound document, servicing, compliance, and customer-support workflows.
**Weakness:** The population anchor is missing and mutual charters, regulatory approvals, capital constraints, and legacy cores narrow both transferability and implementation.

## Business-model lens
- Included: U.S. lower-middle-market savings and loan associations, savings banks, private banks, industrial banks, and similar depository institutions providing recurring deposit, mortgage, consumer, commercial-lending, payment, and account services to external customers.
- Excluded: Commercial banks, credit unions, nondepository lenders, trust-only entities without ordinary deposit and lending operations, captive finance units, shells, and non-control financing vehicles.
- Customer and revenue model: Households and businesses place insured deposits and use loans, payments, and account services; institutions earn net interest spread between loans or securities and funding, plus account and transaction fees, subject to capital, liquidity, consumer-protection, and charter supervision.
- Deviation from default lens: none

## Executive view
Savings and other depository institutions have substantial automatable clerical, lending-support, fraud, compliance, and customer-service work, and their spread-and-fee economics can retain part of implemented savings. The opportunity remains constrained by missing population evidence, mutual ownership, charter approvals, capital needs, legacy cores, and competition from larger banks and fintech channels.

## How AI changes the work
AI can extract and verify documents, assist underwriting and servicing, draft communications, detect anomalies, summarize cases, search policy, prepare reports, support compliance, and prioritize exceptions. Humans remain accountable for final credit and pricing decisions, fair lending, suspicious activity, model governance, cybersecurity, complaints, liquidity, capital, and board oversight.

## Value capture
Because customers pay through interest spreads and fees rather than reimbursing labor cost, operating savings can initially accrue to earnings and capital. Deposit competition, loan repricing, fee pressure, vendor expense, regulation, and mutual ownership reduce durable retention.

## Firm availability
Bank-merger activity is observable and formal approval pathways are active. Stock-form institutions can undergo conventional control transactions, whereas mutual savings banks may require mutual merger or conversion and all transactions face regulatory, capital, community, and safety-and-soundness review.

## Demand durability
Household use of bank accounts remains pervasive and insured deposit, payment, mortgage, and credit functions are durable. Digital channels change delivery and reduce branch work, while charter consolidation and migration to commercial banks or fintech-fronted products can shrink the exact industry's share.

## Risks and uncertainty
The largest uncertainties are the missing firm-count anchor, ownership-form mix, exact-industry occupation and volume data, core-provider dependence, cybersecurity and model risk, rate-cycle effects, credit losses, regulatory approval, mutual conversions, deposit competition, and the difference between charter absorption and a qualifying control transfer.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2906 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.32 | 0.46 | 0.59 | PROXY | S2, S3 |
| rho | 0.3 | 0.49 | 0.66 | PROXY | S3, S4 |
| e | 0.38 | 0.6 | 0.78 | ESTIMATE | S1, S5, S6 |
| s5 | 0.09 | 0.15 | 0.22 | PROXY | S5, S7 |
| q | 0.35 | 0.55 | 0.7 | PROXY | S5 |
| d5 | 0.95 | 1.04 | 1.13 | ESTIMATE | S5, S8 |
| o | 0.84 | 0.93 | 0.98 | ESTIMATE | S4, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.12 | 2.62 | 4.53 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 7.00 | 10.00 | 10.00 | PROXY |
| D | 7.98 | 9.67 | 10.00 | ESTIMATE |

## Caveats
- a: The OEWS table is broad NAICS 522 rather than exact 522180 and reports occupations rather than task time.
- a: Current automation through core platforms, rules engines, digital servicing, and workflow software is not directly measured.
- a: Privacy, fair-lending, model-risk, cybersecurity, and safety-and-soundness obligations preserve review and accountability work.
- rho: Treasury evidence spans the financial sector and may be weighted toward much larger institutions.
- rho: OCC's request for information establishes relevance and barriers but does not measure adoption or realized savings.
- rho: Vendor-distributed AI can accelerate implementation while creating concentration and operational dependency.
- e: The frozen dataset provides no defensible lower-middle-market firm count, so no source anchors the population denominator.
- e: Savings institutions include both stock and mutual ownership forms with materially different control pathways.
- e: Regulatory approval and capital requirements can make a legally transferable institution economically ineligible.
- s5: The FDIC merger rate covers all insured banks and savings institutions rather than exact 522180.
- s5: Institution absorption can reflect an affiliate reorganization rather than a qualifying outside control transfer.
- s5: One year's merger activity may not represent a five-year credit, rate, and regulatory cycle.
- q: Aggregate margin data do not identify the sharing of technology benefits.
- q: Interest-rate movements can dominate measured spreads and obscure operating savings.
- q: Mutual institutions may direct more savings toward depositor or community benefit than stock institutions.
- d5: Deposit and loan balances are financial stocks affected by prices and interest rates, not direct service quantities.
- d5: Broad bank-account ownership does not isolate savings institutions from commercial banks or credit unions.
- d5: The exact industry's customer and volume trend is not separately observed.
- o: Digital self-service can remove labor and branding without removing the regulated institution behind the product.
- o: Operator-required demand for depository institutions collectively is higher than for exact 522180 because customers can switch charter types.
- o: No source directly measures year-five software-only substitution for this service basket.

## Sources
- **S1** — [2022 NAICS Definition: 522180 Savings Institutions and Other Depository Credit Intermediation](https://www.census.gov/naics/?details=5221&input=5221&year=2022) (accessed 2026-07-22): Exact-industry scope, including savings and loan associations, savings banks, private banks, industrial banks, and Morris Plans engaged in deposits and lending.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 522000](https://www.bls.gov/oes/2023/may/naics3_522000.htm) (accessed 2026-07-22): Broad credit-intermediation occupation mix, including office and administrative support, financial operations, tellers, customer service, and loan clerks.
- **S3** — [Treasury Releases Report on the Uses, Opportunities, and Risks of Artificial Intelligence in Financial Services](https://home.treasury.gov/news/press-releases/jy2760) (accessed 2026-07-22): Increasing financial-sector AI use and material privacy, bias, consumer-harm, cybersecurity, compliance, and third-party risks.
- **S4** — [OCC Issues Request for Information on Community Bank Digitalization](https://www.occ.gov/news-issuances/news-releases/2025/nr-occ-2025-41.html) (accessed 2026-07-22): Digital technology's relevance to community-bank demand, revenue, efficiency, and competitiveness, and the existence of implementation and technology-provider barriers.
- **S5** — [FDIC Quarterly Banking Profile: Fourth Quarter 2025](https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-fourth-quarter-2025.pdf) (accessed 2026-07-22): Savings-institution counts, assets, deposits, income, margins, funding costs, noninterest income, and broader insured-institution merger activity.
- **S6** — [Mutual to Stock Conversions](https://www.fdic.gov/bank-examinations/mutual-stock-conversions) (accessed 2026-07-22): Existence and recent regulator actions for insured state-chartered mutual savings banks converting to stock form.
- **S7** — [OCC Issues Interim Final Rule on Bank Mergers](https://www.occ.gov/news-issuances/news-releases/2025/nr-occ-2025-44.html) (accessed 2026-07-22): Regulated merger procedures for national banks and federal savings associations and the 2025 restoration of streamlined and expedited review pathways.
- **S8** — [Report on the Economic Well-Being of U.S. Households in 2024: Banking and Credit](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-banking-and-credit.htm) (accessed 2026-07-22): Persistence of bank and credit-union account ownership, credit access, overdraft use, and nonbank financial-service substitution.
