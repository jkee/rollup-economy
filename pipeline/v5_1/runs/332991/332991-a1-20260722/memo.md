# 332991 — Ball and Roller Bearing Manufacturing

*v5.1 Stage 1 research memo. Run `332991-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.22 · L 1.15 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large, diverse installed base of rotating equipment requiring precision physical bearings and replacement support.
**Weakness:** The wage base is dominated by embodied precision production, while powerful OEM buyers constrain retained productivity value.

## Business-model lens
- Included: Independent lower-middle-market manufacturers of ball, roller, mounted, precision, and specialty bearings supplied repeatedly to external OEM, distributor, maintenance, aerospace, energy, transportation, and industrial customers.
- Excluded: Captive internal plants, distributors without manufacturing, bearing repair services classified elsewhere, shell import brands, and non-control financing vehicles.
- Customer and revenue model: Repeat component and replacement sales through OEM programs, qualified supply agreements, distributor replenishment, maintenance demand, and standing purchase orders, generally priced per bearing or lot.
- Deviation from default lens: none

## Executive view
Ball and roller bearing manufacturing offers durable physical demand across many rotating-equipment markets, but most labor is precision production and inspection rather than readily substitutable information work. Repeat OEM and aftermarket relationships fit the lens; transfer and contract evidence are thin.

## How AI changes the work
AI can improve RFQ and standard search, quoting, planning, procurement, customer support, failure analysis drafts, and quality analytics. Forming, heat treatment, grinding, assembly, lubrication, metrology, testing, and maintenance remain embodied.

## Value capture
Qualification and failure risk can protect specialty products, while large OEMs, global brands, annual cost-downs, imports, and distributors reclaim savings in commodity lines.

## Firm availability
Most true independent producers serve repeat external customers, but the 60-firm target population is margin-derived. Import brands, captive plants, and asset-only transactions require careful exclusion.

## Demand durability
Aerospace, wind, industrial motors, automation, transport, and replacement support demand, offset by cycles and longer product life. Remaining demand is inherently physical and requires precision manufacturing.

## Risks and uncertainty
Product failure, recalls, steel and energy costs, tariffs, imports, OEM concentration, qualification losses, automotive redesign, aerospace cycles, and skilled grinding or metrology shortages can overwhelm administrative gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2623 | — | OBSERVED | — |
| n | — | 60 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.31 | PROXY | S1, S2 |
| rho | 0.34 | 0.52 | 0.67 | ESTIMATE | S2, S3 |
| e | 0.53 | 0.7 | 0.83 | ESTIMATE | — |
| s5 | 0.11 | 0.22 | 0.34 | ESTIMATE | — |
| q | 0.4 | 0.58 | 0.74 | ESTIMATE | — |
| d5 | 0.98 | 1.09 | 1.23 | PROXY | S4, S5, S6 |
| o | 0.94 | 0.99 | 1 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.43 | 1.15 | 2.18 | ESTIMATE |
| F | 2.42 | 3.74 | 4.64 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.21 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupational distribution or direct AI task study was found.
- a: The frozen compensation ratio combines 2024 wages with 2022 receipts and may vary materially by commodity versus aerospace-grade mix.
- rho: Representative LMM implementation data were not found.
- rho: Aerospace and ultra-precision bearings face stricter controls than catalog industrial products.
- e: The assigned 60-firm count is margin-bridged rather than an observed EBITDA-band census.
- e: An operator may own multiple plants, and brands may outsource production.
- s5: No owner-age or succession panel specific to bearing manufacturers was found.
- s5: Product-line, plant, inventory, and distributor acquisitions must be separated from going-concern control transfers.
- q: No representative contract dataset was available.
- q: Retention differs sharply between commodity catalog bearings and proprietary precision or aerospace products.
- d5: Aircraft fleets, wind capacity, and motor energy share are drivers rather than direct bearing shipment forecasts.
- d5: Longer-life bearings can reduce replacement units even as installed equipment grows.
- o: This measures operator requirement for remaining bearing demand, not domestic share or retention by the same supplier.
- o: Condition monitoring can extend replacement intervals without eliminating physical operators.

## Sources
- **S1** — [BLS May 2023 OEWS: Fabricated Metal Product Manufacturing](https://www.bls.gov/oes/2023/may/naics3_332000.htm) (accessed 2026-07-22): Reports production occupations at 58.31% of fabricated-metal employment, machinists at 7.10%, and substantial grinding, pressing, rolling, and other production roles.
- **S2** — [NIST Highly Accurate Measurements for Manufacturing at the Smallest Scale](https://www.nist.gov/nist-work/highly-accurate-measurements-manufacturing-smallest-scale) (accessed 2026-07-22): Explains that high-end mechanical parts can require accuracy of a few micrometers and that calibrated standards support billions of dimensional measurements needed for parts to fit and operate.
- **S3** — [OSHA 1926.307 Mechanical power-transmission apparatus](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.307) (accessed 2026-07-22): Requires power-transmission equipment inspection at intervals not exceeding 60 days and bearings to remain aligned and properly adjusted, supporting maintenance and physical accountability.
- **S4** — [FAA Aerospace Forecast Fiscal Years 2025-2045](https://www.faa.gov/data_research/aviation/aerospace_forecasts/FY-2025-2045-Full-Forecast-Document-and-Tables.pdf) (accessed 2026-07-22): Forecasts the U.S. commercial aircraft fleet increasing from 7,387 in 2024 to 10,607 in 2045, an average annual growth rate of 1.7%.
- **S5** — [EIA: Solar and battery storage to lead new U.S. generating capacity additions in 2025](https://www.eia.gov/TODAYINENERGY/detail.php?id=64586) (accessed 2026-07-22): Reports expected U.S. wind capacity additions of 7.7 GW in 2025, versus 5.1 GW added in 2024.
- **S6** — [U.S. Department of Energy Better Plants: Motors](https://betterbuildingssolutioncenter.energy.gov/better-plants/motors) (accessed 2026-07-22): Reports that electric motors for industrial drives account for about 54% of U.S. manufacturing electricity consumption and emphasizes maintenance and motor-management programs.
