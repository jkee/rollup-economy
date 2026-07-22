# 541990 — All Other Professional, Scientific, and Technical Services

*v5 Stage 1 research memo. Run `541990-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 7.48 · L 5.88 · interval CONDITIONAL → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat professional workflows contain document and data tasks that can be automated while a responsible operator still delivers the client outcome.
**Weakness:** NAICS 541990 is a catch-all category, so the available evidence does not measure the selected repeat-service practice population directly.

## Business-model lens
- Included: US lower-middle-market employer firms in this residual NAICS that provide a repeat outsourced professional service to external customers, including repeat appraisal, dispute-resolution, research, technical-review, and similar specialist engagements where the practice, rather than a named individual alone, can be transferred.
- Excluded: One-off expert engagements, owner-only practices without transferable operations, captive units, internal reorganizations, non-control financings, software-only providers, and activities classified to a specific NAICS such as translation, veterinary, legal, accounting, engineering, or management consulting.
- Customer and revenue model: Business and institutional customers buy time, reports, opinions, inspections, or case work through hourly, project, retainer, per-engagement, and occasionally recurring-service contracts.
- Deviation from default lens: Narrowed for coherence because 541990 is a residual category spanning materially different professional services; retained only repeat outsourced services delivered by transferable operating practices.

## Executive view
This is a broad residual NAICS rather than one coherent operating model. The narrowed lens contains potentially transferable repeat-service practices, but code-level evidence cannot establish the mix, operating repeatability, or transferability of the individual firms.

## How AI changes the work
AI is most relevant to research, document intake, search, first-draft reports, data preparation, scheduling, and routine client communications. Human judgment, evidence validation, field work, client trust, regulated sign-off, and responsibility remain the constraints on both substitution and implementation.

## Value capture
Labor savings can be competed away where work is hourly, project priced, or benchmarked. Retainer relationships, specialization, and accountability may preserve value, but contract review is needed before treating savings as operator retained.

## Firm availability
The residual classification contains employer firms, while Census's ABS provides an owner-age measurement framework and BizBuySell shows an active small-business service transaction market. Neither source identifies qualifying 541990 LMM control transfers, so availability remains a bounded judgment rather than an observed rate.

## Demand durability
External demand for specialized interpretation and accountable professional work should persist, and BLS projects market-research analyst employment growth from 2024 to 2034. That signal is only adjacent: the code includes service lines with different cyclicality and software substitution risk.

## Risks and uncertainty
The principal risk is category heterogeneity: a blended code-level conclusion can conceal very different recurring revenue, labor exposure, liability, regulation, and owner dependence. Diligence must identify the actual service line, customer repeat rate, owner concentration, billing model, and human-accountability requirement before any firm-level conclusion.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.8164 | — | OBSERVED | — |
| n | — | 863 | — | ESTIMATE | — |
| a | 0.22 | 0.36 | 0.5 | ESTIMATE | S1, S2, S3 |
| rho | 0.35 | 0.5 | 0.65 | ESTIMATE | S1, S3 |
| e | 0.3 | 0.45 | 0.6 | ESTIMATE | S1, S4 |
| s5 | 0.08 | 0.14 | 0.22 | ESTIMATE | S4, S5 |
| q | 0.35 | 0.5 | 0.65 | ESTIMATE | S1, S3 |
| d5 | 0.93 | 1.01 | 1.1 | ESTIMATE | S1, S3 |
| o | 0.6 | 0.75 | 0.88 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.51 | 5.88 | 10.00 | ESTIMATE |
| F | 4.95 | 6.46 | 7.63 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 5.58 | 7.58 | 9.68 | ESTIMATE |

## Caveats
- a: OEWS explains that its industry occupation estimates exclude self-employed workers, an important limitation for this code.
- a: The injected compensation-to-receipts input may be misleading because the residual NAICS mixes labor models and its QCEW wage population need not match the selected repeat-service practices.
- rho: This is an operational adoption judgment, not a measured industry implementation rate.
- rho: Regulated and high-liability specialties inside the code may implement much more slowly than routine research and report-production practices.
- e: Census owner-characteristic data cover employer firms broadly, not this exact LMM eligible subset.
- e: The injected LMM firm count uses a size-to-EBITDA bridge and does not establish whether a firm has recurring work or transferable operations.
- s5: BizBuySell's service-sector transactions are not NAICS 541990 and skew below the selected EBITDA band.
- s5: No retrieved source measures qualifying control transfers for the selected 541990 practices.
- q: Billing terms are not measured for this residual NAICS.
- q: A practice with cost-plus or tightly benchmarked fees could retain far less than the stated range, while a scarce specialist may retain more.
- d5: The BLS market-research projection is an occupation-wide measure across many industries and includes work outside this lens.
- d5: Residual-code segments can have sharply different demand cycles and no exact constant-price demand series was retrieved.
- o: The source documents analyst duties and a broad employment outlook, not the probability that future 541990 service quantity requires an operator.
- o: The answer varies substantially by specialty, regulation, client risk tolerance, and whether the service is a report or an accountable opinion.

## Sources
- **S1** — [Census Bureau NAICS-based industry definition for 541990](https://www2.census.gov/econ2007/Reference_materials/htm%20files/54199090.htm) (accessed 2026-07-22): Defines the code as other professional, scientific, or technical services not specifically provided for elsewhere and lists cross-references, establishing the residual and heterogeneous classification problem.
- **S2** — [BLS May 2024 National Industry-Specific Occupational Employment and Wage Estimates: methodology](https://www.bls.gov/oes/2024/may/oes_ind.htm) (accessed 2026-07-22): States that industry occupation and wage estimates are based on employer survey data and exclude self-employed persons; describes employment, wage, and percent-of-total fields available for industry occupation mixes.
- **S3** — [BLS Occupational Outlook Handbook: Market Research Analysts](https://www.bls.gov/ooh/business-and-financial/market-research-analysts.htm) (accessed 2026-07-22): Reports the occupation's duties, including gathering and analyzing data, converting findings into reports, and presenting results, and projects 7 percent employment growth from 2024 to 2034; used only as an adjacent workflow and demand signal.
- **S4** — [Census Annual Business Survey: Characteristics of Business Owners, 2022 Tables](https://www.census.gov/data/tables/2022/econ/abs/2022-abs-characteristics-of-owners.html) (accessed 2026-07-22): Provides owner-age and year-acquired-ownership table topics for employer businesses, showing obtainable owner succession inputs but not an industry-specific control-transfer probability.
- **S5** — [BizBuySell Insight Report, Q1 2026](https://www.bizbuysell.com/insight-report/) (accessed 2026-07-22): Reports that its quarterly market data draw on about 50,000 businesses for sale and recently sold, and that service businesses accounted for 42 percent of transactions; it is used only as evidence of a broad small-business service transaction market.
