# 721199 — All Other Traveler Accommodation

*v5.1 Stage 1 research memo. Run `721199-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.18 · L 1.95 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High compensation intensity paired with automatable reservations, communication, pricing, scheduling, and reporting workflows is the main opportunity driver.
**Weakness:** A small supplied LMM firm pool and the absence of exact-code evidence on qualifying control transfers are the main weaknesses.

## Business-model lens
- Included: Employer-operated cabins, guest houses, villas, cottage resorts, hostels, and similar short-term traveler accommodations in the roughly $1-10M normalized EBITDA band that repeatedly sell lodging and associated operating services to external guests.
- Excluded: Pure real-estate holding companies, passive vacation-home ownership, individual hosts without a transferable operating organization, captive internal lodging, non-control financing vehicles, and accommodation classes assigned to other NAICS codes such as hotels and motels, casino hotels, bed-and-breakfast inns, RV parks, recreational camps, and rooming houses.
- Customer and revenue model: Revenue is predominantly transactional room or unit accommodation sold per stay to household travelers, with some business and government customers and ancillary food, recreation, laundry, parking, and space-rental revenue. Repeat demand is recurring at the property and destination level even when individual guests are episodic.
- Deviation from default lens: none

## Executive view
All Other Traveler Accommodation combines durable physical lodging demand with a concentrated digital-administration opportunity. Reservations, guest communications, pricing, scheduling, marketing, and reporting can absorb AI, but room turnover, maintenance, safety, and service recovery remain operator work. The supplied compensation intensity is high, although the 2024-wage/2022-receipts vintage mismatch and IPS harmonization should remain visible. Only 21 LMM firms are supplied, and both eligibility and transfer frequency are uncertain, making firm availability the practical bottleneck.

## How AI changes the work
AI is most applicable to repetitive pre-stay and post-stay communication, multilingual support, inquiry conversion, channel and rate administration, staffing schedules, review responses, purchasing prompts, and management reporting. It is less applicable to cleaning, repairs, inspection, security, and nuanced guest recovery. The broader occupation mix and hotel technology surveys imply useful task substitution, not wholesale autonomous operation.

## Value capture
Nightly and per-stay prices usually do not contractually pass labor costs through to guests, allowing initial retention. Over time, transparent online comparison, dynamic pricing, OTA competition, service reinvestment, and local supply can return part of the benefit to customers. Retention should be strongest at differentiated properties in supply-constrained destinations and weakest at commodity hostels or cabins competing mainly on price.

## Firm availability
Most employer-operated businesses in the code should meet the external-customer service lens, but passive property entities and owner-dependent micro-operations are not transferable operating platforms. Broad employer-business owners report substantial five-year sale or transfer intent, yet completed qualifying transfers will be lower. Real estate can improve collateral and salability while also increasing transaction size, financing sensitivity, and the chance that a deal is only an asset transfer.

## Demand durability
Current real travel forecasts point to moderate growth, supported mainly by domestic leisure travel. Cabins, guest houses, cottage resorts, villas, and hostels also align with regional, group, and lower-cost travel preferences. Demand remains cyclical and destination-specific, but the physical need for a ready, safe place to stay keeps most quantity attached to an accountable operator even as guest-facing processes become self-service.

## Risks and uncertainty
The largest evidence gap is exact-code data: occupation mix, technology adoption, business-model eligibility, and control-transfer history are all inferred from broader populations. The code spans properties with different service intensity and channel economics. A downturn, energy-price shock, wildfire or flood exposure, local short-term-rental restrictions, insurance costs, OTA dependence, poor connectivity, or guest resistance to reduced service could erase anticipated gains. The supplied compensation ratio may also be distorted by its wage/receipts vintage mismatch and by unusually volatile post-pandemic lodging receipts.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6882 | — | OBSERVED | — |
| n | — | 21 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.31 | PROXY | S1 |
| rho | 0.3 | 0.48 | 0.65 | PROXY | S3, S4 |
| e | 0.65 | 0.8 | 0.92 | ESTIMATE | S2 |
| s5 | 0.08 | 0.14 | 0.22 | PROXY | S5 |
| q | 0.45 | 0.66 | 0.82 | ESTIMATE | S2 |
| d5 | 0.95 | 1.12 | 1.25 | PROXY | S6 |
| o | 0.84 | 0.93 | 0.98 | ESTIMATE | S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.99 | 2.77 | 5.55 | PROXY |
| F | 1.19 | 1.95 | 2.67 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.98 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS publishes the cited occupation mix at NAICS 721 rather than 721199.
- a: The five occupations shown by BLS are not an exhaustive payroll distribution.
- a: Exposure is a task judgment and does not imply implementation or job elimination.
- rho: The surveys are global and hotel-heavy, not statistically representative of U.S. 721199 firms.
- rho: S4 is vendor-sponsored and its respondents may be unusually technology-forward.
- rho: Using AI in a task is not the same as eliminating labor or avoiding a hire.
- e: No source measures lens eligibility directly.
- e: Legal entity structures can separate property ownership from lodging operations.
- e: The supplied n estimate already has margin-bridge and size-class uncertainty; this primitive does not re-estimate it.
- s5: Gallup covers all U.S. employer-business owners, not this industry or EBITDA band.
- s5: The source measures plans rather than completed transactions.
- s5: Property sales do not necessarily transfer control of a lodging operating company.
- q: No observed study traces AI labor savings through 721199 prices over five years.
- q: Retention varies sharply by destination supply, seasonality, channel mix, and guest segment.
- q: This estimate excludes demand-volume effects, which belong in d5 and o.
- d5: The forecast covers all travel spending, not 721199 room nights.
- d5: Its published horizon ends in 2030, one year short of the run-date five-year endpoint.
- d5: Constant-dollar spending is an imperfect proxy for constant-price, constant-quality service quantity.
- o: There is no direct measure of the share of 721199 demand requiring an accountable operator in 2031.
- o: Human-led check-in is only supporting context and is not equivalent to operator necessity.
- o: Local regulation and property design can make unattended operation either easier or harder.

## Sources
- **S1** — [Accommodation: NAICS 721 — Industries at a Glance](https://www.bls.gov/iag/tgs/iag721.htm) (accessed 2026-07-22): BLS reports 2025 employment of 420,800 maids and housekeeping cleaners, 247,700 hotel/motel/resort desk clerks, 143,620 waiters, 40,380 housekeeping supervisors, and 38,100 lodging managers, with corresponding wage data, for the broader Accommodation subsector.
- **S2** — [2022 Economic Census Accommodation Location Information Questionnaire](https://bhs.econ.census.gov/ombpdfs2022/export/2022_AF-72120_mu.pdf) (accessed 2026-07-22): The Census questionnaire identifies 721199 activities as cabins, guest houses, villas, cottage resorts, and hostels; lists room or unit accommodation with or without maid service and shared hostel rooms as products; and identifies household, business, and government customer classes.
- **S3** — [Annual Survey Results: The State of Hospitality Tech 2025](https://www.hotelyearbook.com/article/122000481/annual-survey-results-the-state-of-hospitality-tech-2025) (accessed 2026-07-22): A 264-respondent global hospitality survey reports average hotel-company technology maturity of 5.35/10, PMS use of 74.41%, CRS/booking-engine use of 63.95%, RMS use of 50%, and integration, fragmentation, and legacy infrastructure as leading adoption barriers.
- **S4** — [Most hoteliers use AI daily, but guest experience still needs a human touch](https://www.hospitalitynet.org/news/4132496/most-hoteliers-use-ai-daily-but-guest-experience-still-needs-a-human-touch) (accessed 2026-07-22): The Mews Hotelier Survey 2026 covers more than 500 global properties, reports AI involvement in 11 of 19 common hotel tasks and more than half the workload in those tasks, while 59% of respondents want welcome and check-in to remain human-led.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Gallup's fall 2024 U.S. owner survey found 22% of employer-business owners planned to sell or transfer ownership within five years, compared with 9% of nonemployers; among all primarily working owners, 14% planned a sale, public offering, or transfer.
- **S6** — [U.S. Travel Forecast — Spring 2026](https://www.ustravel.org/sites/default/files/2026-05/US_Travel-Forecast_Spring26.pdf) (accessed 2026-07-22): Tourism Economics and the U.S. Travel Association forecast inflation-adjusted total travel spending rising from $1.374 trillion in 2026 to $1.534 trillion in 2030 and domestic travel spending rising from $1.195 trillion to $1.316 trillion.
