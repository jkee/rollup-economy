# 561440 — Collection Agencies

*v5.1 Stage 1 research memo. Run `561440-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 7.31 · L 4.49 · interval CONDITIONAL → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is the unusually direct fit between repetitive, software-mediated collection work and productivity technology, reinforced by BLS's explicit expectation that enhanced software and automated calling will let collectors handle more accounts.
**Weakness:** The principal weakness is that the same digital tools available to an acquirer are available to creditors and scaled platforms, while regulation makes mistakes expensive; operator bypass and compliance costs can absorb a large portion of the apparent labor upside.

## Business-model lens
- Included: Independent third-party agencies collecting consumer or commercial claims for clients and remitting recoveries, using letters, telephone, email, text, portals, payment processing, skip tracing, dispute handling, and account servicing. Recurring or repeat creditor placements must be supported by transferable client relationships, systems, procedures, licenses, and compliance controls.
- Excluded: In-house or captive first-party collection departments; debt buyers whose economics primarily come from owning purchased receivables rather than collecting and remitting client claims; law firms primarily providing legal services; repossession services; credit bureaus; payment processors; and businesses outside the $1 million to $10 million normalized EBITDA range or without transferable going-concern operations.
- Customer and revenue model: Creditors and debt owners outsource account placements to agencies, commonly paying a contingent percentage of amounts recovered; some arrangements may use fixed, placement, or servicing fees. Revenue is recurring or repeat through portfolios and creditor relationships but varies with placements and recoveries.
- Deviation from default lens: none

## Executive view
Collection agencies combine a highly exposed digital workflow with real demand durability and meaningful transferability. The investable case depends less on replacing collectors wholesale than on using automation to raise accounts handled per employee while preserving compliant, auditable human control over disputes and consequential exceptions.

## How AI changes the work
The most accessible gains are account prioritization, data cleansing, contact sequencing, notice drafting, call summarization, quality review, payment-plan administration, recordkeeping, and agent assistance. Consumer negotiation, hardship, disputed identity, legal status, complaints, and unusual facts should remain controlled human escalations.

## Value capture
Contingent pricing allows cost savings to accrue initially to the agency and improved recoveries to benefit both agency and client. Capture decays through rebids, commission-rate pressure, client demands for technology benefits, integration costs, compliance staffing, model monitoring, and vendor fees.

## Firm availability
The sector's outsourced model supports acquisition transfer, but five-year seller availability is unmeasured directly. Practical supply will favor owners with diversified creditor relationships, clean licensing and complaint records, defensible data controls, durable placements, credible management depth, and systems that can survive client diligence.

## Demand durability
Household debt remains very large and 4.8% of balances were in some stage of delinquency in 2026Q1. Need persists across credit products, but revenue is cyclical and sensitive to placement volumes, charge-offs, cure rates, creditor policy, regulatory enforcement, and direct digital servicing.

## Risks and uncertainty
The central risks are FDCPA and Regulation F violations, state-law fragmentation, consent and third-party disclosure errors, inaccurate or poorly documented account data, algorithmic bias or hallucination, cybersecurity, client concentration, contingent-revenue volatility, litigation, reputational harm, and technology-enabled insourcing.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4147 | — | OBSERVED | — |
| n | — | 120 | — | ESTIMATE | — |
| a | 0.58 | 0.72 | 0.84 | PROXY | S2, S3 |
| rho | 0.46 | 0.63 | 0.77 | PROXY | S3, S5, S6, S7, S8 |
| e | 0.58 | 0.75 | 0.87 | ESTIMATE | S1, S5, S8 |
| s5 | 0.09 | 0.17 | 0.27 | PROXY | S11 |
| q | 0.42 | 0.6 | 0.76 | ESTIMATE | S10 |
| d5 | 0.94 | 1.08 | 1.22 | PROXY | S3, S4, S9 |
| o | 0.49 | 0.67 | 0.81 | PROXY | S3, S5, S6, S7, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 4.43 | 7.52 | 10.00 | PROXY |
| F | 3.19 | 4.49 | 5.43 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 4.61 | 7.24 | 9.88 | PROXY |

## Caveats
- a: Occupation evidence includes first-party collectors outside the target business population.
- a: Task exposure is not equivalent to safe end-to-end autonomy.
- rho: Federal rules do not measure adoption or realized margin gains.
- rho: State law, client requirements, and data quality can impose tighter constraints.
- e: No direct national estimate of transferable EBITDA in the target size band was found.
- e: Client consent, licensing, and compliance diligence vary materially by transaction.
- s5: Intentions include family transfers and do not equal completed arm's-length sales.
- s5: The survey is not specific to collection agencies or the target EBITDA range.
- q: A large public debt buyer's vendor arrangements are only an adjacent view of target-company pricing.
- q: Contract terms and rebid cadence vary by creditor and debt type.
- d5: NAICS 561400 includes answering, telemarketing, and other support services.
- d5: Household debt is nominal and excludes commercial collections.
- d5: Delinquency and placements are cyclical.
- o: Labor automation can improve agency margins without displacing the agency.
- o: Observed creditor insourcing rates for the target market were not found.

## Sources
- **S1** — [2017 NAICS Sector 56 detail: 561440 Collection Agencies](https://www.census.gov/naics/?details=561&input=561&year=2017) (accessed 2026-07-22): Lens boundary and the client-claim collection and remittance business model used for e.
- **S2** — [O*NET OnLine: Bill and Account Collectors (43-3011.00)](https://www.onetonline.org/link/summary/43-3011.00) (accessed 2026-07-22): Collector tasks, work activities, work context, software use, and judgment requirements used for a.
- **S3** — [BLS Occupational Outlook Handbook: Bill and Account Collectors](https://www.bls.gov/ooh/office-and-administrative-support/bill-and-account-collectors.htm) (accessed 2026-07-22): Projected collector employment decline, software and automated-calling productivity, and continuing debt demand used for a, rho, d5, and o.
- **S4** — [BLS Employment Projections: Industry employment and output](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Broad NAICS 561400 employment and real-output projections used as a d5 proxy.
- **S5** — [CFPB Regulation F compilation](https://www.consumerfinance.gov/rules-policy/debt-collection-practices/regulation-f-compilation/) (accessed 2026-07-22): Federal communication, validation, credit-reporting, and time-barred-debt requirements used for rho, e, and o.
- **S6** — [CFPB Regulation F section 1006.6: Communications in connection with debt collection](https://www.consumerfinance.gov/rules-policy/regulations/1006/6/) (accessed 2026-07-22): Communication limits, cease-contact duties, and reasonable email/text procedures used for rho and o.
- **S7** — [CFPB Regulation F section 1006.42: Sending required disclosures](https://www.consumerfinance.gov/rules-policy/regulations/1006/42/) (accessed 2026-07-22): Electronic disclosure, notice, and E-SIGN requirements used for rho and o.
- **S8** — [FTC: Fair Debt Collection Practices Act text](https://www.ftc.gov/legal-library/browse/rules/fair-debt-collection-practices-act-text) (accessed 2026-07-22): Federal prohibitions and consumer validation and dispute rights used for rho, e, and o.
- **S9** — [New York Fed: Household Debt Balances Rise Slightly as Delinquency Transition Rates Hold Steady](https://www.newyorkfed.org/newsevents/news/research/2026/20260512) (accessed 2026-07-22): 2026Q1 household debt and delinquency levels used for d5.
- **S10** — [Encore Capital Group 2024 Annual Report](https://www.sec.gov/Archives/edgar/data/1084961/000108496125000045/encore2024annualreport-f.htm) (accessed 2026-07-22): Statement that collection agencies receive contingent fees based on amounts collected, used for q.
- **S11** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): National five-year employer-owner sale-or-transfer intention benchmark used for s5.
