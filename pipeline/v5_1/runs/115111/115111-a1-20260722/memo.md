# 115111 — Cotton Ginning

*v5.1 Stage 1 research memo. Run `115111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.06 · L 1.57 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Indispensable local processing combined with measurable machine-vision and process-control use cases creates a credible path to operational improvement at surviving high-throughput gins.
**Weakness:** A tiny, consolidating firm universe and volatile cotton volumes make firm availability and durable utilization materially less certain than the technical automation opportunity.

## Business-model lens
- Included: Independent, cooperative, and custom cotton-ginning establishments that repeatedly separate lint from seed and perform associated drying, cleaning, contamination control, baling, and shipment preparation for external growers or cotton owners.
- Excluded: Captive ginning embedded in a vertically integrated farming operation, inactive plants, cotton farming, cottonseed processing, warehousing without ginning, and machinery or software vendors.
- Customer and revenue model: Seasonal business-to-business processing fees paid by growers, cooperatives, or cotton owners, generally linked to bales or volume handled, with possible ancillary revenue from seed handling, storage, and related services.
- Deviation from default lens: none

## Executive view
Cotton ginning is a narrow, essential, machinery-intensive agricultural service with tangible AI opportunities in sensing, contamination control, process settings, maintenance, and administration. Its appeal is tempered by seasonality, a small and consolidating establishment base, volatile crop volumes, and cooperative or customer bargaining that can pass savings through.

## How AI changes the work
AI is most likely to augment an already automated physical process: camera systems can inspect lint and contaminants, models can tune drying and cleaning, and predictive tools can improve maintenance, scheduling, dispatch, and paperwork. Material handling, repair, safety oversight, and exception response remain physical and site-specific.

## Value capture
A high-throughput gin with local density and reliable quality can retain some labor, downtime, and quality gains. Capture weakens when utilization is low, retrofit costs are high, competitors have spare capacity, or cooperative governance returns savings to growers.

## Firm availability
The market is small: USDA counted 419 active gins in 2025, and the injected target-band firm count is only 32. Eligibility is further narrowed by inactive or captive plants, cooperative structures, and ownership or revenue ambiguity, while declining gin counts suggest both consolidation and a thin acquisition pool.

## Demand durability
Every commercially harvested cotton crop requires ginning, supporting the service's functional necessity. Five-year volume remains uncertain because acreage, yield, weather, water, exports, mill use, and regional shifts can dominate; consolidation may nevertheless increase throughput at surviving plants.

## Risks and uncertainty
The largest uncertainties are the absence of cotton-gin-specific occupational task shares, current adoption and payback data, ownership-resolved establishment data, and transaction evidence. Crop volatility, seasonal utilization, legacy integration, contamination-model accuracy, local capacity, and cooperative pass-through widen the outcomes.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2956 | — | OBSERVED | — |
| n | — | 32 | — | ESTIMATE | — |
| a | 0.14 | 0.25 | 0.37 | PROXY | S2, S3, S4 |
| rho | 0.3 | 0.53 | 0.72 | PROXY | S3, S4 |
| e | 0.55 | 0.73 | 0.86 | ESTIMATE | S1, S5, S6 |
| s5 | 0.1 | 0.22 | 0.35 | ESTIMATE | S6 |
| q | 0.35 | 0.55 | 0.72 | ESTIMATE | S2, S3, S5 |
| d5 | 0.82 | 0.98 | 1.18 | PROXY | S5, S6 |
| o | 0.97 | 0.995 | 1 | ESTIMATE | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.50 | 1.57 | 3.15 | PROXY |
| F | 1.63 | 2.92 | 3.80 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.95 | 9.75 | 10.00 | ESTIMATE |

## Caveats
- a: No cotton-ginning-specific task-time survey was located.
- a: The direct commercial machine-vision evidence is older and does not establish current fleet-wide deployment.
- rho: Technical capability is not equivalent to economical realization.
- rho: Seasonal plants may have fewer annual hours over which to amortize automation.
- e: The active-gin census does not identify ownership or whether revenue falls in the target band.
- e: Cooperative and vertically integrated structures blur the external-customer boundary.
- s5: Closures are not necessarily acquisitions or succession events.
- s5: No comprehensive transaction series for private cotton gins was located.
- q: Cooperative economics can intentionally return savings to members rather than retain them as firm profit.
- q: Local competitive structure varies sharply across cotton regions.
- d5: One year of national change is not a five-year forecast.
- d5: National bale volume can diverge materially from the serviceable volume of a particular local gin.
- o: The construct concerns persistence of an accountable operator, not preservation of every current job.
- o: Remote supervision could change the organizational form without eliminating accountability.

## Sources
- **S1** — [North American Industry Classification System: Sector 11, NAICS 115111 Cotton Ginning](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-22): Exact industry definition: establishments primarily engaged in ginning cotton.
- **S2** — [What Is a Cotton Gin?](https://www.ars.usda.gov/southeast-area/stoneville-ms/cotton-ginning-research/docs/what-is-a-cotton-gin/) (accessed 2026-07-22): Core process, including lint-seed separation, drying, cleaning, foreign-matter removal, equipment adjustment, maintenance, and throughput considerations.
- **S3** — [Machine Vision Automating Cotton Gins](https://www.ars.usda.gov/news-events/news/research-news/2004/machine-vision-automating-cotton-gins/) (accessed 2026-07-22): Commercial machine-vision use for trash monitoring and automatic cleaner control, demonstrating direct automation feasibility and quality benefits.
- **S4** — [Machine-vision detection and removal of plastic contamination in cotton gins](https://www.ars.usda.gov/research/publications/publication/?seqNo115=384988) (accessed 2026-07-22): Low-cost color-camera and air-jet system for automated contamination detection and removal.
- **S5** — [Cotton Ginnings Survey](https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Cotton_Ginnings/index.php) (accessed 2026-07-22): The survey is a census of active gins across 17 cotton states and records bales, lint weight, average bale weight, and plants throughout the season.
- **S6** — [Cotton Ginnings 2025 Summary](https://esmis.nal.usda.gov/sites/default/release-files/795901/ctgnan26.pdf) (accessed 2026-07-22): Reports 13.5 million running bales ginned in 2025, down 4 percent from 2024; 419 active gins versus 446 in 2024; and 60 percent of active gins processing more than 20,000 bales.
