# 721120 — Casino Hotels

*v5.1 Stage 1 research memo. Run `721120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.72 · L 0.76 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Direct consumer economics allow an operator to retain a substantial share of carefully implemented back-office, guest-service, marketing, and monitoring efficiencies.
**Weakness:** Most employment is physical and guest-facing, and the small transferable-firm universe is both uncertain and subject to unusually demanding gaming-license approvals.

## Business-model lens
- Included: Operating US casino hotels in the lower-middle-market EBITDA band, including the integrated on-premise lodging, casino gaming, food and beverage, loyalty, guest-service, security, and back-office workflows sold repeatedly to external guests.
- Excluded: Online-only gaming and sports books, casinos without lodging, passive real-estate owners and REITs, management-only or captive internal units, shells, non-control financing vehicles, and establishments outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: Primarily direct-to-consumer, transaction-based revenue: net casino win, room charges, food and beverage, entertainment, retail, and loyalty-mediated repeat spend; some group and convention revenue may be contracted.
- Deviation from default lens: none

## Executive view
Casino hotels combine a meaningful but bounded AI labor opportunity with a mostly direct consumer revenue model that can retain savings. The opportunity is concentrated in information work and workflow orchestration rather than the large physical, guest-facing workforce. Transfer supply is plausible but thin and regulator-dependent, while the supplied LMM firm count is itself an estimate.

## How AI changes the work
AI can automate or accelerate reservations, customer messaging, marketing production, loyalty personalization, reconciliation, reporting, scheduling, demand forecasting, and first-pass surveillance or fraud review. It can also coordinate existing kiosks and robotics. Dealers, cooks, servers, housekeepers, maintenance workers, and security responders still perform physical or trust-intensive work, so occupation elimination is not the operative case.

## Value capture
Direct net-win, room, food, beverage, and entertainment revenue means savings are not mechanically returned through cost-plus contracts. Capture can nevertheless leak through comps, loyalty rewards, promotional intensity, lower room rates, service restoration, employee bargaining, and competitive reinvestment, especially where nearby casinos target the same patrons.

## Firm availability
Most true 721120 operating firms fit the repeat external-customer lens, but establishment-versus-firm classification, mixed ownership, passive real estate, and gaming-license suitability reduce actionable eligibility. A broad employer-business survey points to meaningful five-year sale or transfer intentions, and a recent small casino asset sale shows transactions occur, but a regulator-derived denominator and closed-deal series are missing.

## Demand durability
Land-based gaming remains large and grew in 2025, and BLS projects slight casino-hotel employment growth through 2034. The physical lodging, gaming, food, and entertainment bundle should largely still need a licensed accountable operator. Rapid iGaming growth, local competitive openings, and volatile visitation keep constant-price demand near flat in the downside rather than assured growth.

## Risks and uncertainty
The largest uncertainties are the unobserved LMM-specific task mix, incomplete baseline automation, fragmented property systems, union and regulator constraints, the actual eligible-firm roster, and the absence of a casino-hotel transfer-rate dataset. Cybersecurity, privacy, responsible-gaming errors, surveillance false positives, degraded hospitality, and loyalty-model failures could erase savings or delay implementation. The frozen compensation ratio also mixes 2024 wages with 2022 receipts and is harmonized by a cross-code median, while n is margin-bridged and estimated.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1811 | — | OBSERVED | — |
| n | — | 43 | — | ESTIMATE | — |
| a | 0.17 | 0.25 | 0.34 | ESTIMATE | S2, S3, S5 |
| rho | 0.25 | 0.42 | 0.58 | ESTIMATE | S4, S5, S7 |
| e | 0.55 | 0.72 | 0.88 | ESTIMATE | S1, S8 |
| s5 | 0.08 | 0.17 | 0.28 | PROXY | S6, S7, S8 |
| q | 0.42 | 0.64 | 0.82 | ESTIMATE | S8, S11 |
| d5 | 0.9 | 1.02 | 1.12 | PROXY | S9, S10, S11 |
| o | 0.78 | 0.9 | 0.97 | ESTIMATE | S7, S9, S11 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.31 | 0.76 | 1.43 | ESTIMATE |
| F | 1.71 | 2.95 | 3.94 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.02 | 9.18 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation mix is May 2023 and covers employers of all sizes rather than the LMM lens alone.
- a: Task exposure within each occupation is researcher judgment; Anthropic usage data are economy-wide and skew toward Claude users.
- a: Robotics-enabled physical automation is included only where AI plausibly avoids hiring; mature self-service already in place is excluded conceptually but cannot be measured directly.
- rho: The hotel readiness survey is vendor-sponsored, its sample is not disclosed on the fetched summary, and it is not casino-specific.
- rho: Las Vegas union constraints may overstate labor resistance for smaller nonunion regional properties.
- rho: Five-year model and integration progress could exceed the high case, while security or responsible-gaming failures could delay adoption.
- e: NAICS is assigned at the establishment level while n is a firm estimate, so multi-property operators and mixed entities can create classification mismatch.
- e: No source enumerates eligibility within the supplied LMM population.
- e: The provided n is an ESTIMATE based on a margin bridge and may include firms whose normalized EBITDA lies outside the band.
- s5: Gallup covers all US employer businesses, not casino hotels or the LMM EBITDA band.
- s5: Stated plans can exceed completed sales, and Gallup's transfer category may include family transfers that do not meet the screen's control-transfer definition.
- s5: The Stockman's transaction is one observed casino sale and may not have included a lodging operation classified specifically in NAICS 721120.
- q: Public-company revenue recognition and competitive behavior may not match smaller independent properties.
- q: No source isolates the customer-sharing response to AI-derived savings.
- q: Gaming tax rates affect cash retention but generally apply to gaming revenue rather than directly forcing labor-cost savings to customers.
- d5: BLS employment is an input proxy, not output or demand, and may fall when automation raises productivity.
- d5: AGA traditional gaming revenue excludes hotel, food, and entertainment and is nominal rather than constant-price.
- d5: National totals conceal material property-level losses from local competition and visitation shifts.
- o: The construct is not directly measured and depends on how the current integrated service basket is held constant.
- o: Online substitution varies sharply by state legality and customer segment.
- o: An accountable operator can remain necessary even if the operator employs substantially fewer people; that labor effect belongs in a and rho, not here.

## Sources
- **S1** — [721120: Casino hotels - Census Bureau Profile](https://data.census.gov/profile/721120_-_Casino_hotels?codeset=naics~721120&g=010XX00US) (accessed 2026-07-22): Defines 721120 as establishments primarily engaged in short-term lodging in hotel facilities with a casino on the premises; supports the eligibility logic and establishment-level caveat.
- **S2** — [Casino Hotels - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics5_721120.htm) (accessed 2026-07-22): Reports 322,710 total employees and detailed employment shares and wages for office, sales, protective service, food service, cleaning, gambling-services, hotel-desk, accounting, and other occupations used to bound wage-weighted task exposure.
- **S3** — [The Anthropic Economic Index](https://www.anthropic.com/news/the-anthropic-economic-index) (accessed 2026-07-22): Reports real-world Claude task use across occupations, including roughly 36% of occupations using AI for at least a quarter of tasks, 43% automation versus 57% augmentation, and low use in physical low-paid roles; supports cautious task-exposure judgments.
- **S4** — [The 2026 Hotel Operations Index: Progress, Pressure, and the Path Forward](https://www.hospitalitynet.org/report/4130590/the-2026-hotel-operations-index-progress-pressure-and-the-path-forward) (accessed 2026-07-22): Hotel-owner and operator survey summary reporting 91% still use some manual reporting, 11% have a fully integrated technology stack, 25% are AI-ready, and 40% are not ready; supports implementation constraints.
- **S5** — [Robot baristas and AI chefs caused a stir at CES 2024 as casino union workers fear for their jobs](https://apnews.com/article/ces-2024-robots-vegas-strip-casino-jobs-8bd3fd4f404a0cda90e69e539a19fb01) (accessed 2026-07-22): Documents casino-hotel use of self-check-in, automated valet tickets, and robot bartenders, emerging service robotics, and technology-related protections in five-year Las Vegas union contracts covering 40,000 workers.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey reporting that 22% of employer-business owners planned to sell or transfer ownership within five years; supplies the cross-industry succession proxy.
- **S7** — [Nevada Gaming Regulation 8 - Transfer of Ownership; Loans](https://gaming.nv.gov/uploadedFiles/gamingnvgov/content/Home/Features/Regulation8.pdf) (accessed 2026-07-22): Requires proposed transferees of licensed gaming interests to apply for and obtain required licenses, suitability findings, or registrations before transfer and governs approval, escrow, and participation; supports transfer and operating-accountability constraints.
- **S8** — [Full House Resorts, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/891482/000089148226000007/fll-20251231x10k.htm) (accessed 2026-07-22): Describes casino net-win and direct rooms, food, beverage, retail, comp, and loyalty revenue mechanics; reports the completed two-phase $9.2 million sale of Stockman's Casino to a privately owned company; also illustrates owned, leased, and third-party-hotel operating structures.
- **S9** — [State of the States 2026](https://www.americangaming.org/resources/state-of-the-states-2026/) (accessed 2026-07-22): Reports 493 commercial casino locations, 2.3% growth in traditional land-based casino revenue to $51.06 billion in 2025, and 27.6% iGaming growth to $10.73 billion; supports demand and online-substitution judgments.
- **S10** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS 2024-34 projection shows Casino Hotels employment increasing from 252,800 to 259,300, or 2.6% over ten years; used as a proxy anchor for five-year service demand.
- **S11** — [Caesars Entertainment, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1590895/000159089526000011/czr-20251231.htm) (accessed 2026-07-22): Reports competitive customer reinvestment and margin pressure in regional properties, visitation-driven Las Vegas declines, and the expectation that online gaming complements brick-and-mortar casinos; supports retention, demand dispersion, and operator-required judgments.
