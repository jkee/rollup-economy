# 336214 — Travel Trailer and Camper Manufacturing

*v5.1 Stage 1 research memo. Run `336214-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.52 · L 0.54 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A broad independent specialty base and repeat dealer/configuration workflows create implementable information-work opportunities.
**Weakness:** The code mixes discretionary RVs with functional trailers, while most labor remains physical and the injected firm count is uncertain.

## Business-model lens
- Included: US lower-middle-market firms repeatedly manufacturing standardized or configured travel trailers, campers, pickup coaches and caps, automobile trailers, utility trailers, light-truck trailers, and single-car transporters for external dealers, distributors, fleets, and consumers.
- Excluded: One-off custom fabricators without repeat models or customers; truck semitrailers classified in 336212; mobile homes; repair and retail-only businesses; captive plants; and firms outside the EBITDA band.
- Customer and revenue model: Repeat-model product sales through dealers and distributors or direct fleet/customer orders, with model options, parts, warranty, and periodic product refreshes; end demand spans discretionary recreation and functional utility/light-trailer uses.
- Deviation from default lens: The code combines recreational travel trailers/campers with functional utility, horse, automobile, and light-truck trailers and pickup caps. To keep the screen coherent, the lens retains repeat-model manufacturers with established dealer, distributor, or fleet channels across these products and excludes one-off custom fabrication; this narrowing is based on revenue-model coherence, not attractiveness.

## Executive view
Travel-trailer and camper manufacturing has reusable model, dealer, configuration, and warranty workflows, plus a sizable independent specialty base. Its low labor share, physical production, heterogeneous segments, and discretionary RV exposure limit a uniform opportunity case.

## How AI changes the work
AI can improve dealer and fleet quoting, option compatibility, prior-design retrieval, bills of material, purchasing, scheduling, marketing content, manuals, quality records, and warranty triage. Frames, walls, cabinetry, wiring, plumbing, upholstery, paint, assembly, and final inspection remain physical.

## Value capture
Specialty features, brand, and lead time support retention, while commodity utility trailers and mainstream RV models face rapid price comparison, dealer leverage, promotions, and model-year discounting.

## Firm availability
Regional utility and specialty manufacturers create plausible LMM availability, but the code also contains consolidated RV plants and very small custom shops. Segment, ownership, and normalized economics must be verified before treating the injected 206-firm estimate as transferable supply.

## Demand durability
The market is normalizing after a pandemic boom and correction. Towable shipments grew modestly in 2025 and outdoor recreation remains economically substantial, but financing costs, dealer inventory, used units, fuel prices, and consumer confidence can drive large swings; functional utility products provide some diversification.

## Risks and uncertainty
Risks include consumer-durable cyclicality, dealer inventory and financing, segment heterogeneity, brand and customer concentration, warranty/recall exposure, seasonal labor, raw-material and component volatility, imports, consolidation, and an imprecise eligible-firm denominator.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0943 | — | OBSERVED | — |
| n | — | 206 | — | ESTIMATE | — |
| a | 0.16 | 0.27 | 0.39 | PROXY | S2 |
| rho | 0.34 | 0.53 | 0.7 | ESTIMATE | S0 |
| e | 0.41 | 0.61 | 0.78 | ESTIMATE | S0 |
| s5 | 0.12 | 0.24 | 0.38 | PROXY | S7 |
| q | 0.35 | 0.53 | 0.71 | ESTIMATE | S4 |
| d5 | 0.75 | 1.04 | 1.32 | PROXY | S3, S5, S6 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S0 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.54 | 1.03 | ESTIMATE |
| F | 3.88 | 5.53 | 6.64 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.20 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is four-digit and includes other body/trailer industries.
- a: The heterogeneous product mix widens the exposure range.
- rho: No direct industry implementation survey exists.
- rho: Recreational and utility manufacturers may have materially different digital maturity.
- e: The provided n is margin-bridged and not observed.
- e: Different segments have different margins, making a single Auto Parts margin bridge fragile.
- s5: Owner age does not directly measure transfers.
- s5: Small private deals are incompletely reported.
- q: PPI observes product selling prices rather than AI-benefit retention.
- q: Retention varies materially between branded RVs and commodity utility trailers.
- d5: Wholesale shipments can reflect inventory rather than retail demand.
- d5: The production series aggregates disparate products.
- d5: Discretionary RV demand is highly sensitive to rates and consumer confidence.
- o: Imports and consolidation can displace individual lens firms while physical operator demand persists.

## Sources
- **S0** — [2022 NAICS definition: 336214 Travel Trailer and Camper Manufacturing](https://www.census.gov/naics/?details=33&input=33&year=2022) (accessed 2026-07-23): Defines travel trailers, campers, pickup coaches and caps, automobile/utility/light-truck trailers, and relevant exclusions.
- **S1** — [336214 Travel Trailer and Camper Manufacturing — Census Bureau Profile](https://data.census.gov/profile/336214_-_Travel_Trailer_and_Camper_Manufacturing?codeset=naics~336214) (accessed 2026-07-23): Industry scope and examples including single-car transporters, campers, horse trailers, pickup caps, recreational travel trailers, and utility trailers.
- **S2** — [May 2023 OEWS: Motor Vehicle Body and Trailer Manufacturing](https://www.bls.gov/oes/2023/may/naics4_336200.htm) (accessed 2026-07-23): Broader occupation mix: production occupations 65.21% and assemblers/fabricators 31.75%.
- **S3** — [Industrial Production: Travel Trailer and Camper Manufacturing](https://fred.stlouisfed.org/series/IPG336214A) (accessed 2026-07-23): Federal Reserve real-output index reports 2025 at 81.2049 on a 2017=100 basis.
- **S4** — [Producer Price Index: Travel Trailer and Camper Manufacturing](https://fred.stlouisfed.org/data/PCU336214336214) (accessed 2026-07-23): BLS monthly industry selling-price index through June 2026.
- **S5** — [RV shipments end 2025 with modest growth](https://www.rvia.org/reports-trends/rv-shipment-reports/2025-12/rv-shipments-end-2025-342220-units-modest-25-growth-over-2024) (accessed 2026-07-23): RVIA reports about 306,191 towable shipments in 2025, up about 2.5%, within 342,220 total RV shipments.
- **S6** — [Outdoor Recreation Economic Statistics, 2024](https://www.bea.gov/index.php/news/2026/outdoor-recreation-economic-statistics-us-and-states-2024) (accessed 2026-07-23): BEA reports RVing generated $27.5 billion in current-dollar value added in 2024 and was the second-largest conventional outdoor activity.
- **S7** — [ABS Characteristics of Business Owners: 2024 Tables](https://www.census.gov/data/tables/2024/econ/abs/2024-abs-characteristics-of-owners.html) (accessed 2026-07-23): Official Census Age of Owner tables for employer businesses, used only as a broad succession proxy.
- **S8** — [2026 RV Wholesale Shipments To Rise Modestly](https://www.rvia.org/news-insights/2026-rv-wholesale-shipments-rise-modestly) (accessed 2026-07-23): Spring 2026 forecast range of 328,800–367,000 total RV shipments, median 349,000, following 342,200 in 2025.
