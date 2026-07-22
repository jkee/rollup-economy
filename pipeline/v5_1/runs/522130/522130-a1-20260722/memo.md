# 522130 — Credit Unions

*v5.1 Stage 1 research memo. Run `522130-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 4.75 · L 2.30 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Rule-bound financial processing and recurring member service create a sizable workflow-automation opportunity.
**Weakness:** Member-owned non-stock governance prevents ordinary outside ownership and directs economic value back to members rather than financial sponsors.

## Business-model lens
- Included: U.S. lower-middle-market credit unions providing recurring deposit, payment, consumer-lending, mortgage, member-service, and related financial services to eligible external members.
- Excluded: Commercial banks, savings institutions, nondepository lenders, corporate credit unions serving other credit unions, credit-union service organizations classified elsewhere, captive finance units, and shells without operating member relationships.
- Customer and revenue model: Members place insured share deposits and use loans, payments, and account services; the credit union earns interest spread and fees to cover operating costs, losses, and required net worth, while residual economic value belongs to members through retained capital, dividends, rates, fees, and services.
- Deviation from default lens: none

## Executive view
Credit unions contain substantial document, servicing, fraud, compliance, and member-support work that AI can assist, but their member-owned cooperative form is a fundamental barrier to conventional outside control and private capture. Persistent consolidation does not erase the distinction between a member-approved credit-union merger and an equity acquisition.

## How AI changes the work
AI can classify and extract documents, draft member communications, support fraud and anomaly detection, summarize cases, assist servicing, search policy, prepare compliance work, and prioritize exceptions. Humans and boards remain accountable for lending, fair treatment, model governance, cybersecurity, complaints, suspicious activity, exceptions, and member governance.

## Value capture
Operational savings can fund capital, resilience, technology, and service expansion, but credit-union economic value belongs to members and is ultimately expressed through rates, fees, dividends, services, or retained net worth. Durable private capture by an outside owner is therefore structurally limited.

## Firm availability
Federally insured credit-union counts continue to decline through consolidation, yet most credit unions issue no stock and are controlled democratically by members. Ordinary mergers can transfer operations to another cooperative; only unusual conversions or legally permissible structures resemble an outside control opportunity.

## Demand durability
Insured accounts, payments, and credit remain durable household needs, and aggregate credit-union membership and loans are growing. Smaller institutions face weaker member growth and channel substitution, so industry demand does not guarantee survival of a particular charter.

## Risks and uncertainty
Key risks are the unsuitable EBITDA-based firm-count anchor, non-stock ownership, member and regulator approvals, core-vendor dependence, model bias and explainability, privacy, cyber fraud, capital requirements, interest-rate exposure, and the gap between aggregate system growth and smaller-credit-union performance.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2605 | — | OBSERVED | — |
| n | — | 1194 | — | ESTIMATE | — |
| a | 0.34 | 0.48 | 0.61 | PROXY | S2, S3, S4 |
| rho | 0.28 | 0.46 | 0.62 | PROXY | S3, S4 |
| e | 0.01 | 0.04 | 0.1 | ESTIMATE | S1, S6 |
| s5 | 0.08 | 0.15 | 0.22 | PROXY | S5, S6 |
| q | 0.08 | 0.18 | 0.32 | PROXY | S7 |
| d5 | 0.96 | 1.07 | 1.16 | PROXY | S5, S8 |
| o | 0.8 | 0.91 | 0.97 | ESTIMATE | S3, S5, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.99 | 2.30 | 3.94 | PROXY |
| F | 1.08 | 3.38 | 5.32 | ESTIMATE |
| C | 1.60 | 3.60 | 6.40 | PROXY |
| D | 7.68 | 9.74 | 10.00 | ESTIMATE |

## Caveats
- a: The OEWS source covers broad NAICS 522 rather than exact-industry credit unions and measures occupations rather than tasks.
- a: The estimate excludes tasks already automated by core banking, rules engines, online account servicing, and robotic process automation.
- a: Fair-lending, privacy, model-risk, cybersecurity, and explainability obligations preserve accountable human work around high-impact decisions.
- rho: NCUA describes exploration, use cases, and expectations but does not report a representative production-adoption rate.
- rho: Treasury evidence spans the financial sector and may reflect institutions with much greater resources than lower-middle-market credit unions.
- rho: Third-party adoption can accelerate access while concentrating operational, privacy, and model risk.
- e: The supplied firm count applies an EBITDA margin to a cooperative depository model for which EBITDA is not a natural size measure and may materially misstate the screened population.
- e: A merger into another credit union transfers operations but does not create ordinary seller equity value for an outside sponsor.
- e: State-chartered credit-union conversion rules can differ from federal rules.
- s5: The source reports net count decline, not a cohort-level probability of qualifying control transfer.
- s5: A credit-union merger is governed by member ownership and regulatory approval rather than conventional seller succession.
- s5: Recent consolidation may be concentrated among institutions smaller than the supplied economic band.
- q: The source explains surplus disposition but does not measure the retention of technology savings.
- q: Capital needs and supervisory expectations vary materially with growth, asset risk, and institution condition.
- q: Benefits may appear as better member pricing or services rather than operator cash flow.
- d5: Asset and loan balances are nominal financial stocks, not constant-quality service quantities.
- d5: Aggregate membership growth is concentrated and may not represent institutions in the supplied economic band.
- d5: Commercial banks, fintechs, and nonbank payment providers can take activity even when household use of financial services remains durable.
- o: Digital delivery can eliminate interactions without eliminating the regulated institution behind the service.
- o: The operator-required share for credit unions specifically is lower than for depository institutions collectively because customers can switch charter types.
- o: No source directly measures year-five software-only substitution for the exact current service basket.

## Sources
- **S1** — [2022 NAICS Definition: 522130 Credit Unions](https://www.census.gov/naics/?details=5221&input=5221&year=2022) (accessed 2026-07-22): Exact-industry scope: cooperatives accepting members' share deposits and offering consumer loans to members.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 522000](https://www.bls.gov/oes/2023/may/naics3_522000.htm) (accessed 2026-07-22): Broad credit-intermediation occupation mix, including office and administrative support, financial operations, tellers, customer service, and loan clerks.
- **S3** — [Artificial Intelligence (AI)](https://ncua.gov/regulation-supervision/regulatory-compliance-resources/artificial-intelligence-ai) (accessed 2026-07-22): Credit-union AI use cases, operational opportunities, board oversight, risk controls, data security, monitoring, and third-party due diligence.
- **S4** — [Treasury Releases Report on the Uses, Opportunities, and Risks of Artificial Intelligence in Financial Services](https://home.treasury.gov/news/press-releases/jy2760) (accessed 2026-07-22): Increasing financial-sector AI use and material privacy, bias, consumer-harm, cybersecurity, compliance, and third-party risks.
- **S5** — [NCUA Releases Fourth Quarter 2025 Credit Union System Performance Data](https://ncua.gov/newsroom/press-release/2026/ncua-releases-fourth-quarter-2025-credit-union-system-performance-data) (accessed 2026-07-22): Federally insured credit-union membership, asset and loan growth, institution counts, charter mix, and long-running consolidation.
- **S6** — [Bank to Credit Union Conversions](https://ncua.gov/support-services/credit-union-resources-expansion/field-membership-expansion/bank-credit-union-conversions) (accessed 2026-07-22): Member-owned, member-controlled, not-for-profit cooperative structure, lack of stock, elected boards, field-of-membership limits, and conversion and merger requirements.
- **S7** — [Evaluating Earnings](https://ncua.gov/regulation-supervision/letters-credit-unions-other-guidance/evaluating-earnings) (accessed 2026-07-22): Credit-union surplus belongs to members and must balance retained net worth with dividends, lower rates, services, growth, and future member benefits.
- **S8** — [Report on the Economic Well-Being of U.S. Households in 2024: Banking and Credit](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-banking-and-credit.htm) (accessed 2026-07-22): Persistence of bank and credit-union account ownership, credit access, overdraft use, and nonbank financial-service substitution.
