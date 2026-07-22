# 512131 — Motion Picture Theaters (except Drive-Ins)

*v5.1 Stage 1 research memo. Run `512131-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.75 · L 0.60 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digitized ticketing, loyalty, marketing, scheduling, and back-office systems create implementable efficiency around repeat admissions and concession revenue.
**Weakness:** Most labor is physical and demand depends on volatile film supply while the buyer-accessible LMM operator pool is small.

## Business-model lens
- Included: U.S. lower-middle-market operators of indoor motion-picture theaters that repeatedly sell admissions and related concessions, food and beverage, advertising, loyalty, rental, and event services to external customers.
- Excluded: Drive-in theaters, film production and distribution, streaming services, captive screening rooms, dormant venues, non-operating real-estate owners, and film festivals or itinerant exhibitors without a recurring operating organization.
- Customer and revenue model: Consumers pay per admission or through memberships and also buy concessions and premium experiences; operators may earn auditorium-rental, advertising, ticket-fee, loyalty, gift-card, merchandise, and alternate-content revenue. Film rental is commonly linked to admissions revenue, while venue labor, occupancy, utilities, and most technology costs remain with the exhibitor.
- Deviation from default lens: none

## Executive view
Indoor theaters combine a modest remaining digital-work surface with a business that is still dominated by physical guest service, food service, and venue operation. The experience remains operator-required, but demand is film-slate dependent and the supplied LMM count is small and margin-derived.

## How AI changes the work
AI can improve scheduling, local marketing, loyalty segmentation, demand and inventory forecasting, customer support, bookkeeping, pricing analysis, content programming support, and exception handling. It cannot replace food preparation, cleaning, safety, maintenance, physical guest recovery, projection accountability, or the venue experience, and much ticketing is already digitized.

## Value capture
Posted ticket and concession prices permit initial retention of labor savings, but film-rental economics, promotions, streaming competition, technology fees, and continuing investment in seating, sound, screens, and food service share or consume part of the benefit.

## Firm availability
The NAICS scope contains genuine recurring operators and an observed market for theater businesses, but chain ownership, leases, distressed closures, film-festival exhibitors, and asset-only property sales narrow the transferable pool. The supplied firm count depends on a sector-level margin that may not fit theater economics.

## Demand durability
Moviegoing remains widespread and the release slate is rebuilding, yet 2025 indicators mix modest nominal box-office growth with weak attendance and a continuing gap from 2019. The shared large-screen experience is difficult to replace, while streaming and title volatility keep the quantity outlook uncertain.

## Risks and uncertainty
The largest uncertainties are the combined indoor/drive-in occupation proxy, existing automation that shrinks the remaining task base, public-chain evidence applied to independents, nominal rather than quantity demand data, distributor dependence, lease and capex burdens, and sparse exact-industry transfer evidence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2013 | — | OBSERVED | — |
| n | — | 68 | — | ESTIMATE | — |
| a | 0.08 | 0.15 | 0.24 | PROXY | S2, S3 |
| rho | 0.3 | 0.5 | 0.68 | PROXY | S3 |
| e | 0.7 | 0.86 | 0.95 | ESTIMATE | S1 |
| s5 | 0.07 | 0.14 | 0.24 | PROXY | S6, S7 |
| q | 0.45 | 0.66 | 0.82 | PROXY | S3 |
| d5 | 0.75 | 0.96 | 1.15 | PROXY | S3, S4, S5 |
| o | 0.82 | 0.92 | 0.98 | PROXY | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.19 | 0.60 | 1.31 | PROXY |
| F | 2.36 | 3.57 | 4.51 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | PROXY |
| D | 6.15 | 8.83 | 10.00 | PROXY |

## Caveats
- a: OEWS combines indoor theaters, drive-ins, and other motion-picture exhibition at 512130.
- a: Occupation shares are employment-based and require an approximate wage and task mapping.
- a: Large-chain technology described by Marcus may be more advanced than lower-middle-market independent theaters.
- rho: Observed digitization is not evidence that AI has delivered equivalent labor removal.
- rho: Marcus is larger and better capitalized than the screened LMM population.
- rho: Some remaining exposed tasks occur only during peaks, limiting removable staffing.
- e: No public source measures eligibility within the supplied LMM-band firm count.
- e: The supplied n uses a general Information Services EBITDA margin that may not fit film-rental, concession, and lease economics.
- e: A financially active location can be part of a larger chain rather than a separately transferable firm.
- s5: BizBuySell's theater benchmark includes nightclubs, live-performance venues, and smaller businesses outside the supplied EBITDA band.
- s5: The seller survey has no exact-industry denominator and measures intentions, not completed transfers.
- s5: Theater closures and property dispositions do not qualify when the operating service does not survive.
- q: Price increases during inflation do not directly measure retention of AI-enabled savings.
- q: Film-rental terms vary by title and may capture part of admissions economics.
- q: Independent theaters may reinvest savings to remain competitive rather than retain them as cash flow.
- d5: Box office is nominal revenue, not constant-price quantity.
- d5: Public-chain attendance and trade-group surveys may not represent LMM independent theaters.
- d5: Demand depends unusually heavily on distributor release schedules and a small number of titles.
- o: No source directly measures the year-five operator-required share.
- o: The trade association has an advocacy interest in emphasizing experiential durability.
- o: Self-service changes labor intensity without necessarily removing the theater operator.

## Sources
- **S1** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Exact 512131 scope as operating non-drive-in motion-picture theaters and exhibiting films or videos at film festivals.
- **S2** — [May 2023 OEWS: Motion Picture and Video Exhibition](https://www.bls.gov/oes/2023/may/naics5_512130.htm) (accessed 2026-07-22): Combined 512130 occupation employment shares and wages for management, food service, ushers and ticket takers, sales, administration, cleaning, security, and maintenance.
- **S3** — [The Marcus Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/62234/000006223426000011/mcs-20251231.htm) (accessed 2026-07-22): Theater ticketing and food-ordering technology, self-service systems, labor-productivity intent, attendance, ticket and concession pricing, alternate content, and operating risks.
- **S4** — [AMC Entertainment Holdings 2025 Form 10-K/A](https://www.sec.gov/Archives/edgar/data/1411579/000110465926053024/amc-20251231x10ka.htm) (accessed 2026-07-22): North American 2025 box office of $8.9 billion compared with $8.7 billion in 2024 and $11.4 billion in 2019, plus exhibitor operating responses.
- **S5** — [Strength of Theatrical Exhibition: December 2025 Update](https://cinemaunited.org/wp-content/uploads/2025/12/Strength-of-Theatrical-Exhibition-December-2025-Update.pdf) (accessed 2026-07-22): Consumer moviegoing incidence and frequency, theater reinvestment, release-slate indicators, and experiential attributes valued by moviegoers.
- **S6** — [BizBuySell 2025 Fourth Quarter Insight Report](https://www.bizbuysell.com/news/bizbuysell-2025-fourth-quarter-insight-report/) (accessed 2026-07-22): Broad small-business sale activity, seller motives including retirement, and broker evidence on Baby Boomer listings.
- **S7** — [Nightclub and Theater Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/nightclub-theater/) (accessed 2026-07-22): Observed sales and financial benchmarks for nightclub and theater businesses reported to BizBuySell from 2021 through 2025.
