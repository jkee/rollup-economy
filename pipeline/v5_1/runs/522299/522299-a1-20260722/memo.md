# 522299 — International, Secondary Market, and All Other Nondepository Credit Intermediation

*v5.1 Stage 1 research memo. Run `522299-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** The principal driver is automating high-volume document, verification, monitoring, servicing, and compliance work around repeat credit relationships.
**Weakness:** The principal weakness is an unknown transferable-firm pool inside a heterogeneous, capital- and regulation-intensive industry where credit and funding risks can overwhelm labor savings.

## Business-model lens
- Included: U.S. lower-middle-market firms providing repeat external nondepository credit intermediation through international trade finance, factoring, secondary-market loan acquisition and repackaging, inventory or agricultural credit, industrial lending, pawn loans, and other activities included in NAICS 522299.
- Excluded: Credit card issuing, sales financing, consumer lending classified in 522291, real estate credit, depository institutions, captive financing units, government instrumentalities, shell securitization vehicles without transferable operations, non-control financing situations, and firms outside the target normalized-EBITDA band.
- Customer and revenue model: Borrowers, exporters, importers, sellers of receivables, loan sellers and buyers, and pawn customers pay interest, discounts, origination or servicing fees, pawn service charges, and transaction spreads; secondary-market firms also earn gains, fees, or spreads from acquiring, pooling, servicing, and reselling loans.
- Deviation from default lens: none

## Executive view
NAICS 522299 contains document-heavy, data-rich credit workflows with meaningful AI assistance potential, but it is unusually heterogeneous and its lower-middle-market firm count is missing. Capital, credit losses, licensing, funding, and accountable risk ownership matter at least as much as labor efficiency.

## How AI changes the work
AI can extract documents, validate files, draft credit memoranda and notices, summarize counterparties, monitor portfolios, triage servicing and collections, and assist customer communications. Humans remain responsible for relationships, exceptions, collateral, explainable adverse actions, credit authority, fraud escalation, funding, and loss decisions.

## Value capture
Savings may be retained in interest spreads, discount income, and service charges or used to accelerate decisions and support more accounts. Funding costs, regulated charges, competitive terms, credit losses, partner negotiations, and customer-acquisition costs limit capture.

## Firm availability
The frozen dataset has no defensible LMM firm count. The code includes government and institutional entities, large platforms, owner-operated pawnshops and factors, and secondary-market vehicles, so transferable operating businesses are a fraction of an unknown denominator.

## Demand durability
Specialized nonbank credit persists where banks, trade partners, sellers of receivables, and credit-constrained consumers need liquidity or risk transfer. Demand is cyclical and sensitive to bank capacity, funding markets, regulation, credit performance, trade, and platform substitution.

## Risks and uncertainty
Key risks are the missing firm-count anchor, business-model heterogeneity, funding fragility, credit losses, fraud, fair-lending and licensing failures, customer or counterparty concentration, state fee restrictions, adverse selection, and software or bank disintermediation.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1053 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.34 | 0.48 | 0.62 | PROXY | S1, S2, S3 |
| rho | 0.38 | 0.56 | 0.72 | ESTIMATE | S3, S4 |
| e | 0.25 | 0.48 | 0.7 | ESTIMATE | S1, S6, S7 |
| s5 | 0.06 | 0.13 | 0.22 | PROXY | S5 |
| q | 0.32 | 0.52 | 0.7 | ESTIMATE | S6, S7 |
| d5 | 0.87 | 1.04 | 1.23 | ESTIMATE | S6, S7 |
| o | 0.72 | 0.86 | 0.95 | ESTIMATE | S1, S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.54 | 1.13 | 1.88 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 6.26 | 8.94 | 10.00 | ESTIMATE |

## Caveats
- a: The OEWS population is broad NAICS 522290 rather than 522299 and is dominated by loan officers and loan-processing staff whose mix may not represent secondary-market, trade-finance, factoring, or pawn firms.
- a: O*NET describes an occupation across industries and does not measure wage-weighted hours or current automation.
- a: The code combines office-heavy finance businesses with store-based collateral operations and balance-sheet investment businesses.
- rho: No representative source measures AI implementation or realized labor savings in NAICS 522299.
- rho: CFPB requirements directly address consumer credit decisions and are less applicable to some commercial, trade-finance, and secondary-market workflows.
- rho: Small operators may lack clean data, integration capacity, and model-governance staff.
- e: The frozen dataset declares no defensible LMM-band firm count, so the size and composition of the candidate pool are unknown.
- e: NAICS 522299 mixes government, institutional, retail, commercial, and secondary-market models with very different capital and control-transfer characteristics.
- e: Public-company examples do not represent lower-middle-market ownership or economics.
- s5: Gallup covers all U.S. employer-business owners and measures intentions rather than completed qualifying control sales.
- s5: The proxy does not represent institutional ownership, securitization vehicles, regulated license transfers, or credit-portfolio diligence.
- s5: The missing LMM firm-count anchor prevents checking whether owner-operated firms dominate the relevant population.
- q: No representative source measures pass-through or repricing of automation benefits in 522299.
- q: Pawn charges may be regulated, whereas factoring and trade-finance terms are negotiated; one retention rate compresses unlike models.
- q: Credit and funding-cycle changes can dominate operating savings.
- d5: Federal Reserve nonbank research covers a broader NBFI population and does not measure 522299 service quantity.
- d5: A large pawn operator illustrates continuing customer use but not representative industry growth.
- d5: Credit cycles, funding availability, loan size, and nominal balances can diverge sharply from constant-price service quantity.
- o: Legal accountability does not guarantee that an independent 522299 firm remains the operator; banks, marketplaces, or software platforms may internalize the function.
- o: Secondary-market execution is more digitally substitutable than physical pawn collateral handling.
- o: No source quantifies the year-five share of this heterogeneous basket that remains with firms of the lens's kind.

## Sources
- **S1** — [2022 NAICS Definition: 522299 International, Secondary Market, and All Other Nondepository Credit Intermediation](https://www.census.gov/naics/?chart=2022&details=522299&input=522299) (accessed 2026-07-22): Official industry scope, illustrative activities, exclusions, lens heterogeneity, e, and o
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 522290](https://www.bls.gov/oes/2023/may/naics5_522290.htm) (accessed 2026-07-22): Broad nondepository-credit occupational mix and employment shares used as a proxy for a
- **S3** — [O*NET OnLine: Loan Interviewers and Clerks](https://www.onetonline.org/link/summary/43-4131.00) (accessed 2026-07-22): Loan intake, verification, documentation, records, customer contact, monitoring, compliance, and judgment tasks; a and rho
- **S4** — [CFPB Circular 2022-03: Adverse Action Notification Requirements for Complex Algorithms](https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/) (accessed 2026-07-22): Explainability and accurate-reason requirements for AI-supported credit decisions; rho and o
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year sale or transfer intentions among employer-business owners; s5
- **S6** — [Bank Regulation and the Rise of Nonbank Intermediation](https://www.federalreserve.gov/econres/feds/bank-regulation-and-the-rise-of-nonbank-intermediation.htm) (accessed 2026-07-22): Broad nonbank-intermediation capacity, bank reliance, fragility, and demand context; e, q, and d5
- **S7** — [FirstCash Holdings, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/840489/000084048926000032/fcfs-20251231.htm) (accessed 2026-07-22): Pawn operating model, collateral, short-term repeat credit, service charges, competition, regulation, and operating tasks; e, q, d5, and o
