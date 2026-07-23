# 336213 — Motor Home Manufacturing

*v5.1 Stage 1 research memo. Run `336213-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.60 · L 0.85 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat model families and dealer relationships create reusable information workflows alongside a recovering shipment base.
**Weakness:** A tiny, concentrated eligible pool and discretionary demand make availability and durability fragile.

## Business-model lens
- Included: US lower-middle-market firms repeatedly manufacturing motor homes on purchased chassis or conversion vans on an assembly-line basis for external dealers, distributors, rental fleets, and consumers.
- Excluded: Large integrated OEMs outside the EBITDA band; captive plants; one-off van customization and repair; towable travel trailers; mobile homes; chassis-only or complete body-and-chassis manufacturing classified elsewhere.
- Customer and revenue model: Wholesale or direct product sales of Type A, B, and C motor homes and production conversion vans, with dealer orders, model-year programs, options, parts, and warranty support creating repeat revenue relationships.
- Deviation from default lens: none

## Executive view
Motor-home manufacturing has useful digital workflows around configured products, dealer networks, marketing, and warranty, but remains a highly cyclical consumer-durable business with a small eligible firm pool and physically intensive production.

## How AI changes the work
AI can improve dealer-order handling, floorplan and option retrieval, bills of material, engineering-change search, procurement, schedules, marketing content, owner-manual support, and warranty triage. Cabinetry, plumbing, electrical integration, upholstery, paint, assembly, road testing, and final inspection remain physical.

## Value capture
Brand and differentiated floorplans protect some gains, particularly in niche Class B/C products, while dealer leverage, incentives, product refreshes, and easy price comparison return gains to customers over time.

## Firm availability
Only 71 employer establishments were reported, and establishment is not independent firm. The LMM opportunity is likely concentrated in specialty converters and niche brands, making ownership and revenue-quality verification essential.

## Demand durability
The sector is recovering from a sharp post-pandemic production decline. Recent motor-home shipments and outdoor-recreation activity are supportive, but purchases remain discretionary and sensitive to financing, wealth, fuel prices, used inventory, and dealer stocking.

## Risks and uncertainty
Major risks are consumer-durable cyclicality, interest rates, dealer inventory, brand concentration, warranty and recall exposure, chassis supply, skilled trades, seasonal labor, floorplan financing, consolidation, and overestimating the count of transferable independent manufacturers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1332 | — | OBSERVED | — |
| n | — | 21 | — | ESTIMATE | — |
| a | 0.17 | 0.29 | 0.41 | PROXY | S2 |
| rho | 0.36 | 0.55 | 0.72 | ESTIMATE | S0, S8 |
| e | 0.18 | 0.37 | 0.57 | ESTIMATE | S1 |
| s5 | 0.1 | 0.21 | 0.34 | PROXY | S7 |
| q | 0.4 | 0.59 | 0.76 | ESTIMATE | S4 |
| d5 | 0.76 | 1.05 | 1.34 | PROXY | S3, S5, S6 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S0, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.85 | 1.57 | ESTIMATE |
| F | 0.52 | 1.56 | 2.61 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.30 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Four-digit occupation data include trailers and bodies.
- a: Exposure does not equal feasible automation.
- rho: No industry study directly measures five-year implementation.
- rho: Human certification and final quality accountability remain necessary.
- e: Establishment count is not firm count.
- e: The injected n of 21 is margin-bridged and may overstate independent firms in this concentrated niche.
- s5: Owner age does not observe sales.
- s5: Small private deals and closures are incompletely recorded.
- q: Industry PPI is a selling-price measure, not an AI pass-through measure.
- q: Direct-to-consumer and dealer-heavy brands have different retention.
- d5: Wholesale shipments can diverge from retail sell-through.
- d5: Outdoor-recreation value added is far broader than motor-home purchases.
- d5: Interest rates and consumer confidence drive large cycle swings.
- o: Consolidation, imports, or dealer private labels can displace particular lens firms while the operator requirement remains.

## Sources
- **S0** — [2022 NAICS definition: 336213 Motor Home Manufacturing](https://www.census.gov/naics/?details=33&input=33&year=2022) (accessed 2026-07-23): Defines motor homes on purchased chassis and assembly-line conversion vans and distinguishes excluded chassis, custom conversion, towable, and mobile-home activities.
- **S1** — [336213 Motor Home Manufacturing — Census Bureau Profile](https://data.census.gov/profile/336213_-_Motor_Home_Manufacturing?codeset=naics~336213) (accessed 2026-07-23): Reports 71 employer establishments in 2023 CBP and provides the six-digit industry definition.
- **S2** — [May 2023 OEWS: Motor Vehicle Body and Trailer Manufacturing](https://www.bls.gov/oes/2023/may/naics4_336200.htm) (accessed 2026-07-23): Broader occupation mix: production occupations 65.21% and assemblers/fabricators 31.75%.
- **S3** — [Industrial Production: Motor Home Manufacturing, annual](https://fred.stlouisfed.org/series/IPN336213A) (accessed 2026-07-23): Real-output index values of 122.5407 in 2022, 87.3771 in 2023, 65.8724 in 2024, and 73.3577 in 2025.
- **S4** — [Producer Price Index: Motor Home Manufacturing](https://fred.stlouisfed.org/series/PCU336213336213) (accessed 2026-07-23): BLS monthly industry selling-price index, including 230.211 in May 2026.
- **S5** — [RV shipments end 2025 with modest growth](https://www.rvia.org/reports-trends/rv-shipment-reports/2025-12/rv-shipments-end-2025-342220-units-modest-25-growth-over-2024) (accessed 2026-07-23): RVIA manufacturer survey reports 36,029 motor-home shipments in 2025, up 3.3%, within 342,220 total RV shipments.
- **S6** — [Outdoor Recreation Economic Statistics, 2024](https://www.bea.gov/index.php/news/2026/outdoor-recreation-economic-statistics-us-and-states-2024) (accessed 2026-07-23): BEA reports RVing was the second-largest conventional outdoor activity with $27.5 billion in current-dollar value added in 2024.
- **S7** — [ABS Characteristics of Business Owners: 2024 Tables](https://www.census.gov/data/tables/2024/econ/abs/2024-abs-characteristics-of-owners.html) (accessed 2026-07-23): Official Census Age of Owner tables for employer businesses, used only as a broad succession proxy.
- **S8** — [NHTSA interpretation: final-stage manufacturer responsibilities](https://www.nhtsa.gov/interpretations/usedchas) (accessed 2026-07-23): Final-stage manufacturers complete vehicles under federal safety standards and affix certification labels under 49 CFR Parts 567 and 568.
