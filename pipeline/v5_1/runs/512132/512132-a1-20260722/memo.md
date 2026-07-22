# 512132 — Drive-In Motion Picture Theaters

*v5.1 Stage 1 research memo. Run `512132-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.53 · L 0.00 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A distinctive physical venue keeps most surviving demand operator-required and supports repeat admissions and concession sales.
**Weakness:** The frozen earnings-band count is zero, while seasonal site economics and land pressure sharply constrain a transferable operating-firm pool.

## Business-model lens
- Included: U.S. lower-middle-market operators of drive-in motion-picture theaters that repeatedly sell vehicle or individual admission, concessions, rentals, and related outdoor entertainment services to external customers.
- Excluded: Indoor theaters, temporary one-off outdoor screenings without a recurring operator, film production and distribution, streaming services, dormant sites, non-operating landowners, and properties sold for redevelopment without a continuing drive-in operation.
- Customer and revenue model: Consumers generally buy admission to an outdoor, vehicle-oriented screening experience and may also buy concessions, rentals, advertising, merchandise, or special-event access. The operator controls the site experience and local pricing while paying film-rental, labor, utilities, insurance, technology, maintenance, and often land or lease costs.
- Deviation from default lens: none

## Executive view
Drive-ins retain a hard-to-software-away physical experience, but their remaining AI labor surface is modest and implementation is constrained by seasonal, owner-operated economics. The supplied dataset finds no firms in the earnings band, and no public evidence supports overriding that anchor.

## How AI changes the work
AI can support local marketing, customer messages, scheduling, bookkeeping, demand and concession forecasting, pricing analysis, inventory, and programming research. Traffic control, projection accountability, food preparation, cleaning, maintenance, safety, weather response, and live guest recovery remain physical, and small crews limit removable shifts.

## Value capture
Posted admissions and concession prices can retain initial efficiencies, but film rent, seasonal promotions, entertainment substitution, software costs, weather losses, land expense, and facility reinvestment reduce durable capture.

## Firm availability
Active drive-ins fit the recurring-service lens and some operating sites change hands, but the population is small, ownership and land are intertwined, and redevelopment or closure often destroys rather than transfers the operation. The frozen n of zero makes the supplied LMM opportunity absent despite uncertainty in the margin bridge.

## Demand durability
The format remains a distinctive family and community experience, with a current national directory footprint, but lacks a reliable admissions series and faces seasonality, weather, aging assets, streaming, film-slate volatility, and land-conversion pressure.

## Risks and uncertainty
The largest uncertainties are the absence of drive-in-specific occupation and adoption data, the zero margin-derived LMM count, sparse transfer evidence, enthusiast-directory measurement, site and land entanglement, weather, season length, and use of indoor-theater demand evidence as context.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.238 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.06 | 0.14 | 0.24 | PROXY | S2, S3 |
| rho | 0.18 | 0.38 | 0.58 | PROXY | S3 |
| e | 0.7 | 0.88 | 0.97 | ESTIMATE | S1, S8 |
| s5 | 0.04 | 0.1 | 0.2 | PROXY | S6, S7, S8 |
| q | 0.42 | 0.64 | 0.82 | PROXY | S3 |
| d5 | 0.5 | 0.8 | 1.05 | ESTIMATE | S4, S5, S8 |
| o | 0.86 | 0.95 | 0.99 | ESTIMATE | S1, S5, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.10 | 0.51 | 1.33 | PROXY |
| F | 0.00 | 0.00 | 0.00 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | PROXY |
| D | 4.30 | 7.60 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS combines drive-ins with much larger indoor-theater operations.
- a: No public source provides a drive-in-specific occupation or wage mix.
- a: Large-chain digital workflows may not reflect small seasonal operators.
- rho: The implementation evidence comes from an indoor regional chain, not drive-ins.
- rho: Digitized transactions do not establish AI-enabled labor substitution.
- rho: Very small crews may save task time without being able to remove a staffed shift.
- e: No public source measures eligibility within the supplied earnings band.
- e: The supplied n is zero under a general Information Services margin bridge even though drive-ins can combine operating cash flow with valuable land and concessions; the anchor may miss economically relevant operators but must not be replaced.
- e: Directory sites and Census establishments do not necessarily map one-to-one to firms or control positions.
- s5: The sale benchmarks are not specific to drive-ins and mostly cover smaller discretionary-earnings businesses.
- s5: Seller intentions do not measure completed control transfers.
- s5: A site sale, family handoff, or redevelopment is not qualifying unless operating control of a continuing theater transfers.
- q: Indoor public-chain price behavior is not directly representative of seasonal drive-ins.
- q: No source measures pass-through of AI-enabled savings.
- q: Retained operating savings may be consumed by weather losses, maintenance, insurance, or site reinvestment.
- d5: No public national series measures drive-in admissions or constant-quality quantity.
- d5: The directory is enthusiast-maintained and its approximately 330 locations may not match Census establishments or firms.
- d5: Broader indoor-theater demand and release data may not translate to seasonal outdoor venues.
- o: No source directly measures operator-required share for drive-ins.
- o: The physical-site requirement preserves operator need but does not preserve demand volume.
- o: A temporary outdoor exhibitor could substitute for some special-event demand without acquiring a traditional drive-in.

## Sources
- **S1** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Exact 512132 scope as establishments primarily engaged in operating drive-in motion-picture theaters.
- **S2** — [May 2023 OEWS: Motion Picture and Video Exhibition](https://www.bls.gov/oes/2023/may/naics5_512130.htm) (accessed 2026-07-22): Combined 512130 occupation employment shares and wages for guest service, food service, management, sales, administration, cleaning, security, and maintenance.
- **S3** — [The Marcus Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/62234/000006223426000011/mcs-20251231.htm) (accessed 2026-07-22): Theater ticketing and ordering technology, self-service systems, labor-productivity intent, attendance, pricing, alternate content, and operating constraints.
- **S4** — [AMC Entertainment Holdings 2025 Form 10-K/A](https://www.sec.gov/Archives/edgar/data/1411579/000110465926053024/amc-20251231x10ka.htm) (accessed 2026-07-22): Broader North American theatrical box-office recovery context, including the 2025, 2024, and 2019 levels.
- **S5** — [Strength of Theatrical Exhibition: December 2025 Update](https://cinemaunited.org/wp-content/uploads/2025/12/Strength-of-Theatrical-Exhibition-December-2025-Update.pdf) (accessed 2026-07-22): Broader moviegoing incidence and frequency, release-slate indicators, theater reinvestment, and consumer demand for experiential attributes.
- **S6** — [BizBuySell 2025 Fourth Quarter Insight Report](https://www.bizbuysell.com/news/bizbuysell-2025-fourth-quarter-insight-report/) (accessed 2026-07-22): Broad small-business sale activity and seller motives, including retirement pressure.
- **S7** — [Nightclub and Theater Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/nightclub-theater/) (accessed 2026-07-22): Observed sales and financial benchmarks for nightclub and theater businesses reported to BizBuySell from 2021 through 2025.
- **S8** — [Drive-In Theaters Located in the United States](https://www.driveinmovie.com/united-states) (accessed 2026-07-22): Maintained directory reporting about 330 operating U.S. drive-ins, along with closures and reopenings in the current footprint.
