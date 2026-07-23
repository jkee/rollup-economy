# 336211 — Motor Vehicle Body Manufacturing

*v5.1 Stage 1 research memo. Run `336211-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.85 · L 1.52 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat configured builds create both recurring demand and reusable information workflows suitable for AI assistance.
**Weakness:** Physical production dominates labor and the industry's many niches make general evidence a weak predictor of any specific target.

## Business-model lens
- Included: US lower-middle-market firms repeatedly manufacturing truck, bus, and automobile bodies or cabs, including final-stage assembly of vocational and special-purpose vehicles on purchased chassis, for external commercial, fleet, dealer, and public customers.
- Excluded: Captive body operations; one-off personal customization; repair-only shops; trailer and motor-home manufacturers classified elsewhere; complete chassis manufacturing; firms outside the EBITDA band.
- Customer and revenue model: Configured product sales and repeat fleet, dealer, OEM, or municipal orders, with revenue earned per body or completed vehicle and often supplemented by options, parts, and warranty support.
- Deviation from default lens: none

## Executive view
Motor vehicle body manufacturing combines a substantial physical shop-floor base with unusually document-intensive configuration, quotation, and compliance work. Independent specialty manufacturers can fit the lens, but demand and value capture vary sharply by vocational niche.

## How AI changes the work
Near-term opportunity sits in quote-to-order configuration, CAD and prior-design retrieval, bills of material, supplier communication, production planning, inspection records, certification support, and warranty triage. Fabrication, fitting, painting, wiring, integration, and final inspection remain embodied.

## Value capture
Differentiated designs, lead times, certification capability, and aftermarket support can preserve gains. Standardized bodies sold through recurring tenders face quicker repricing and stronger pass-through.

## Firm availability
Regional specialists and final-stage manufacturers create a plausible LMM pool, though captive units, very small custom shops, and subsidiaries reduce eligibility. Transferability depends heavily on customer concentration, certifications, engineering files, and management depth.

## Demand durability
Fleet replacement and vocational needs are durable, and public programs support selected zero-emission bodies and completed vehicles. Recent broader-industry real output has contracted, so the five-year range must reflect cyclicality, chassis supply, rates, and public budgets.

## Risks and uncertainty
Risks include niche concentration, municipal budget timing, chassis shortages, recalls and certification liability, warranty reserves, raw-material volatility, skilled-trade scarcity, technology transition, and dependence on founders or a few fleets.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.239 | — | OBSERVED | — |
| n | — | 247 | — | ESTIMATE | — |
| a | 0.18 | 0.3 | 0.42 | PROXY | S2 |
| rho | 0.34 | 0.53 | 0.7 | ESTIMATE | S0, S3 |
| e | 0.43 | 0.64 | 0.81 | ESTIMATE | S0 |
| s5 | 0.12 | 0.24 | 0.38 | PROXY | S7 |
| q | 0.41 | 0.6 | 0.77 | ESTIMATE | — |
| d5 | 0.83 | 1.02 | 1.2 | PROXY | S4, S5, S6 |
| o | 0.95 | 0.985 | 1 | ESTIMATE | S3, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.59 | 1.52 | 2.81 | ESTIMATE |
| F | 4.22 | 5.89 | 6.99 | ESTIMATE |
| C | 8.20 | 10.00 | 10.00 | ESTIMATE |
| D | 7.88 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation data combine all NAICS 336200 industries.
- a: Task exposure is inferred rather than measured.
- rho: No directly observed five-year implementation rate exists.
- rho: Product-safety accountability keeps human review in the loop.
- e: The injected n is an estimate derived from size classes and an industry margin proxy.
- e: NAICS examples span materially different vocational niches.
- s5: Owner age is not a transaction probability.
- s5: Public deal databases undercount small private transfers.
- q: Retention differs between proprietary emergency vehicles and standardized dry-freight bodies.
- q: No source isolates AI-derived benefit retention.
- d5: 33621 includes truck trailers and other adjacent products.
- d5: Grant-supported replacements are not a steady-state national forecast.
- d5: Older 336211 real-output history ends in 2021.
- o: OEM insourcing and consolidation could reduce independent operators without eliminating manufacturing demand.

## Sources
- **S0** — [NAICS 336211 Motor Vehicle Body Manufacturing definition](https://www.census.gov/naics/?details=336211&input=336211&year=2017) (accessed 2026-07-23): Industry definition and examples including truck bodies, school buses, firefighting vehicles, tanker bodies, tow trucks, and final assembly on purchased chassis.
- **S2** — [May 2023 OEWS: Motor Vehicle Body and Trailer Manufacturing](https://www.bls.gov/oes/2023/may/naics4_336200.htm) (accessed 2026-07-23): Broader occupation mix, including 49,330 miscellaneous assemblers/fabricators (29.23%) and 31,640 metal/plastic workers (18.75%).
- **S3** — [NHTSA interpretation: final-stage manufacturer responsibilities](https://www.nhtsa.gov/interpretations/usedchas) (accessed 2026-07-23): Defines final-stage manufacturer and states conformity and certification-label duties under 49 CFR Parts 567 and 568.
- **S4** — [Real Sectoral Output: Motor Vehicle Body and Trailer Manufacturing](https://fred.stlouisfed.org/series/IPUEN33621T010000000) (accessed 2026-07-23): BLS/FRED broader-industry real-output index: 107.624 in 2022, 94.212 in 2023, 87.007 in 2024, and 84.461 in 2025.
- **S5** — [Table Data: Real Sectoral Output for Motor Vehicle Body Manufacturing](https://fred.stlouisfed.org/data/IPUEN336211T010000000) (accessed 2026-07-23): Six-digit historical real-output index and annual changes through 2021, including a 10.3% decline in 2020 and 4.2% growth in 2021.
- **S6** — [Clean Heavy-Duty Vehicles Grant Program Awards](https://www.epa.gov/clean-heavy-duty-vehicles-program/clean-heavy-duty-vehicles-grant-program-awards) (accessed 2026-07-23): EPA reports more than three million Class 6/7 vehicles in use and 51 grants of about $595 million replacing more than 1,900 school buses and vocational vehicles.
- **S7** — [ABS Characteristics of Business Owners: 2024 Tables](https://www.census.gov/data/tables/2024/econ/abs/2024-abs-characteristics-of-owners.html) (accessed 2026-07-23): Official employer-business owner-characteristics program includes Age of Owner tables used only as a broad succession proxy.
- **S8** — [NHTSA interpretation: certification by final-stage manufacturers](https://www.nhtsa.gov/interpretations/2872o) (accessed 2026-07-23): A final-stage manufacturer completing a vehicle must conform to applicable safety standards and affix the required certification label.
