# 512230 — Music Publishers

*v5.1 Stage 1 research memo. Run `512230-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.62 · L 1.45 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring rights data, royalty reconciliation, and licensing workflows offer substantial AI assistance while valuable catalogs still require accountable administration.
**Weakness:** Only 22 margin-bridged candidates are injected, and catalog asset trades can look like firm transfers without delivering a transferable operating platform.

## Business-model lens
- Included: US lower-middle-market music-publishing firms that repeatedly administer, register, promote, license, collect, reconcile, and distribute income from musical-composition copyrights for external songwriters and other rights owners.
- Excluded: Independent songwriters acting only as their own publishers, passive catalog-holding shells without an operating service, record-label and master-recording activities, captive publishing units, non-control royalty interests, and financing vehicles.
- Customer and revenue model: Recurring administration and exploitation of musical-work rights for songwriters and copyright owners, compensated through retained publishing shares, administration commissions, and license income from performance, mechanical, synchronization, print, and other uses.
- Deviation from default lens: none

## Executive view
Music publishers combine durable copyright administration and relationship responsibilities with a large data- and document-intensive workflow. AI can improve metadata, matching, reconciliation, search, reporting, and drafting, but rights ambiguity and contractual accountability limit unattended automation.

## How AI changes the work
AI can assist work registration, ownership matching, royalty exception triage, catalog search, contract abstraction, license intake, synchronization discovery, reports, and client communications. Humans remain responsible for disputed rights, negotiations, creative repertoire strategy, approvals, audits, and songwriter relationships.

## Value capture
Owned-catalog economics and percentage-based administration can retain internal savings, but renewal repricing, negotiated songwriter shares, platform rules, and service commitments will share some benefit.

## Firm availability
The injected estimate identifies 22 firms in the screened band. The industry definition fits recurring external service, but passive catalogs, captive affiliates, and self-publishing structures require firm-level eligibility review.

## Demand durability
Growing digital music monetization supports licensing and royalty administration, while five-year real demand remains uncertain because recorded-music revenue is an imperfect proxy for composition use and mixes prices with quantity.

## Risks and uncertainty
Major risks include catalog concentration, disputed ownership and splits, songwriter termination rights, platform bargaining power, royalty-rate changes, inaccurate matching, cybersecurity, AI-training litigation, self-administration, and overcounting asset-holding vehicles as operating firms.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1156 | — | OBSERVED | — |
| n | — | 22 | — | ESTIMATE | — |
| a | 0.34 | 0.49 | 0.64 | PROXY | S1, S2, S4 |
| rho | 0.42 | 0.64 | 0.8 | ESTIMATE | S3, S4 |
| e | 0.62 | 0.78 | 0.9 | ESTIMATE | S2 |
| s5 | 0.1 | 0.2 | 0.32 | PROXY | S5, S7 |
| q | 0.48 | 0.64 | 0.78 | ESTIMATE | S3, S4 |
| d5 | 0.93 | 1.08 | 1.22 | PROXY | S6, S8 |
| o | 0.62 | 0.8 | 0.93 | ESTIMATE | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.66 | 1.45 | 2.37 | ESTIMATE |
| F | 1.38 | 2.39 | 3.21 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 5.77 | 8.64 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS covers NAICS 512200 rather than music publishers alone and excludes self-employed workers.
- a: The mapping from occupations to current not-yet-automated tasks is judgmental.
- a: Catalog scale, genre, territory, and reliance on collective licensing materially change the work mix.
- rho: No source measures five-year AI implementation for the screened publisher population.
- rho: Standardized digital-mechanical reporting is not representative of every performance, synchronization, print, and foreign-rights workflow.
- rho: Rights errors can redirect money or create litigation, requiring controlled human review.
- e: The injected firm count is margin-bridged using a broad Information Services margin and may misclassify catalog owners with unusual royalty economics.
- e: Public classifications do not separate operating publishers from passive copyright-holding entities.
- e: Owned-catalog and third-party-administration revenue can coexist within one firm.
- s5: The SBA measures are not music-publisher transfer rates and do not share the five-year horizon.
- s5: Copyright and catalog transfers can occur without a qualifying control transfer of the service firm.
- s5: Termination rights and ownership disputes can alter catalog economics after a firm transfer.
- q: No cited source measures pass-through of AI benefits in publisher contracts.
- q: Retention differs between owned catalogs, full publishing agreements, administration-only contracts, and one-off synchronization licenses.
- q: Recovered previously unmatched royalties are not equivalent to recurring operating-cost savings.
- d5: RIAA measures recorded music, not music-publishing service quantity.
- d5: The 2024 RIAA series added direct reporting from independent labels, reducing comparability.
- d5: Nominal revenue growth mixes price, royalty rates, product mix, and quantity.
- o: Legal accountability can persist while operational work is centralized in a collective or platform.
- o: The operator-required share differs between complex legacy catalogs and clean born-digital repertoires.
- o: Self-publishing tools may displace administration firms without reducing consumption of musical works.

## Sources
- **S1** — [Sound Recording Industries - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_512200.htm) (accessed 2026-07-22): Broad NAICS 512200 occupation and wage mix, including management, business, computer, legal, creative, sales, and office-support roles.
- **S2** — [North American Industry Classification System: Sector 51](https://www.census.gov/naics/resources/archives/sect51.html) (accessed 2026-07-22): Music publishers acquire and register composition copyrights, promote and authorize uses, represent songwriters or other owners, and earn revenue through licensing agreements.
- **S3** — [Music Licensing Study](https://www.copyright.gov/policy/musiclicensingstudy/) (accessed 2026-07-22): Copyright Office findings that music licensing needs efficient processes, authoritative ownership data, and transparent payment and usage information.
- **S4** — [37 CFR 210.27 - Reports of Usage and Payment for Blanket Licensees](https://www.copyright.gov/title37/210/37cfr210-27.html) (accessed 2026-07-22): Detailed recurring, machine-readable reporting, calculation, ownership-share, publisher, usage, royalty, and adjustment requirements for digital mechanical licensing.
- **S5** — [Paths to Business Ownership](https://advocacy.sba.gov/wp-content/uploads/2021/03/Paths-to-Business-Ownership-fact-sheet.pdf) (accessed 2026-07-22): SBA summary of Census evidence that 19 percent of information-industry owners purchased a business and 64.5 percent of owners across industries planned to sell.
- **S6** — [100 Million Paid Subscriptions Milestone Drives US Recorded Music](https://www.riaa.com/2024-year-end-music-industry-revenue-report-riaa/) (accessed 2026-07-22): US recorded music reached $17.7 billion retail and $11.3 billion wholesale in 2024; streaming was 84 percent of revenue and paid subscriptions reached 100 million.
- **S7** — [Termination Rights, Royalty Distributions, Ownership Transfers, Disputes, and the Music Modernization Act](https://www.copyright.gov/rulemaking/mma-termination/) (accessed 2026-07-22): Copyright grants may be terminated in specified circumstances and the 2024 final rule directed MLC distributions consistent with termination rights.
- **S8** — [US Recorded Music Annual Revenue Achieves New High of $11.5 Billion in 2025](https://www.riaa.com/riaa-reports-us-recorded-music-annual-revenue-achieves-new-high-of-11-5-billion-in-2025/) (accessed 2026-07-22): RIAA reports record US wholesale recorded-music revenue of $11.5 billion in 2025, with streaming and paid subscriptions central to revenue.
