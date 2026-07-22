# 333996 — Fluid Power Pump and Motor Manufacturing

*v5.1 Stage 1 research memo. Run `333996-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.30 · L 2.38 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large installed base produces repeated matching, replacement, exchange, and rebuild workflows where proprietary history can make AI operationally valuable.
**Weakness:** Only 146 employer establishments are reported, and many are not independent transferable LMM firms, sharply constraining roll-up supply.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers and factory remanufacturers of hydraulic or pneumatic fluid-power pumps and motors that supply repeat OEM, replacement, exchange, rebuild, or repair work to external customers.
- Excluded: Pure distributors, field-service businesses without manufacturing or remanufacturing capability, general-purpose pump makers, motor-vehicle oil or water pump makers, captive internal shops, and multinational platform-scale suppliers outside the lower middle market.
- Customer and revenue model: Revenue is business-to-business and combines recurring OEM production, specification-based replacement units, remanufactured exchange programs, parts, and repair or rebuild jobs. Products are commonly quoted by model or application, with downtime and technical fit supporting aftermarket economics.
- Deviation from default lens: none

## Executive view
Fluid-power pump and motor manufacturing has a useful information layer around an irreducibly physical product and installed base. AI can improve speed and consistency in quoting, product matching, service evaluation, and operating support, but it will not remove precision production and test labor. The core challenge is less operator necessity than the very small pool of eligible independent targets.

## How AI changes the work
High-value use cases include retrieving obsolete cross-references, drafting quotes and inspection reports, matching prior repairs, assisting application engineers, forecasting parts, scheduling jobs, and answering technical questions. Adoption should augment skilled technicians and engineers while preserving measurement, machining, assembly, and test sign-off.

## Value capture
Aftermarket, exchange, obsolete-unit, and emergency work can retain meaningful benefit because availability, compatibility, warranty, and downtime matter. Contract OEM production and standard components face transparent procurement and renewal repricing, so the operator is unlikely to keep all implemented savings.

## Firm availability
Census reports 146 employer establishments, not independent companies. Even before applying the frozen LMM estimate, corporate affiliation and the mixture of original manufacturing, distribution, and remanufacture imply a narrow candidate pool; proprietary mapping of ownership is essential.

## Demand durability
A broad industrial and mobile installed base creates replacement and rebuild demand, while NFPA's 2026 forecast signals recovery. Electrification can improve hydraulic systems through controls and efficiency, yet direct electric alternatives, machinery cycles, tariffs, and customer concentration make the five-year demand range wide.

## Risks and uncertainty
Six-digit occupation, pricing, transfer, and five-year shipment data are unavailable. Other risks include OEM concentration, obsolete intellectual property, warranty claims, poor service-history data, shortages of skilled machinists and technicians, core-inventory quality, and the pace at which electric drives displace hydraulic architectures.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3424 | — | OBSERVED | — |
| n | — | 40 | — | ESTIMATE | — |
| a | 0.21 | 0.31 | 0.42 | PROXY | S1, S2, S3, S4 |
| rho | 0.36 | 0.56 | 0.73 | ESTIMATE | S3, S4, S5, S9 |
| e | 0.5 | 0.68 | 0.82 | ESTIMATE | S1, S3, S4, S5 |
| s5 | 0.09 | 0.18 | 0.28 | PROXY | S1, S6, S7 |
| q | 0.4 | 0.57 | 0.72 | PROXY | S3, S4, S5 |
| d5 | 0.88 | 1.04 | 1.2 | PROXY | S8, S9, S10 |
| o | 0.9 | 0.96 | 1 | ESTIMATE | S1, S4, S9, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.04 | 2.38 | 4.20 | ESTIMATE |
| F | 1.66 | 2.85 | 3.73 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | PROXY |
| D | 7.92 | 9.98 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source covers broad machinery manufacturing.
- a: Engineering and service-diagnostic tasks are only partially substitutable and still need accountable review.
- rho: Many targets may lack clean digital service histories and interoperable systems.
- rho: Safety-critical specifications and test results require human verification.
- e: Public websites often blur distribution, repair, remanufacture, and original manufacturing.
- e: The frozen firm count is modeled and may misclassify multi-establishment companies.
- s5: Establishments are not firms or transferable control assets.
- s5: Broad transaction data include less technical and more locally oriented manufacturers.
- q: Provider claims describe offerings, not realized margins.
- q: Core credits and exchange economics complicate comparisons of retained benefit.
- d5: The NFPA public figure is a near-term total-fluid-power forecast, not a product-specific five-year projection.
- d5: A target concentrated in construction, agriculture, mining, or energy can diverge sharply from the aggregate.
- o: Technology substitution is captured primarily in demand durability to avoid double counting.
- o: Remote diagnostics could reduce some service interaction without eliminating physical supply.

## Sources
- **S1** — [Census profile: 333996 Fluid power pump and motor manufacturing](https://data.census.gov/profile/333996_-_Fluid_power_pump_and_motor_manufacturing?codeset=naics~333996) (accessed 2026-07-23): Defines the industry as manufacturing hydraulic and pneumatic fluid-power pumps and motors, provides cross-references, and reports 146 employer establishments in 2023.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 333000 Machinery Manufacturing](https://www.bls.gov/oes/2023/may/naics3_333000.htm) (accessed 2026-07-23): Provides the broad machinery-manufacturing occupational mix used to proxy wage-weighted AI task exposure.
- **S3** — [AAH Fluid Power: Services](https://www.aahfluidpower.com/services) (accessed 2026-07-23): Documents new replacement products, remanufactured exchange units, core charges, inspections, machinist rebuilding, OEM-spec testing, warranties, and detailed repair evaluations.
- **S4** — [Precision Fluid Power: Hydraulic Sales and Repair](https://www.precisionfluidpower.com/) (accessed 2026-07-23): Shows new and remanufactured pump and motor sales, repairs, obsolete-unit support, broad end markets, rapid turnaround, and mobile quote requests.
- **S5** — [Texas Fluid Power: Hydraulic Pump, Motor and Cylinder Repair and Remanufacturing](https://txfluidpower.com/) (accessed 2026-07-23): Documents same-day quote goals, teardown and inspection reports, repair and remanufacture, OEM-spec replacement, testing, inventory, and repair warranties.
- **S6** — [BizBuySell Manufacturing Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/manufacturing/) (accessed 2026-07-23): Provides broad manufacturing closed-transaction and valuation benchmarks for 2021-2025, used only as a transferability proxy.
- **S7** — [2022 Annual Business Survey: Characteristics of Business Owners](https://www.census.gov/data/tables/2022/econ/abs/2022-abs-characteristics-of-owners.html) (accessed 2026-07-23): Provides economy-wide owner-age and ownership-characteristics tables used as a broad succession proxy.
- **S8** — [NFPA: ITR Forecast Report - 1st Quarter of 2026 Available](https://www.nfpa.com/news/itr) (accessed 2026-07-23): Reports the total fluid-power shipments index in recovery, forecast 2026 growth of 8.2%, construction-machinery recovery, and margin risks from inflation, tariffs, and price sensitivity.
- **S9** — [NFPA Technology Trends and Reports](https://www.nfpa.com/news/technology-trends-and-reports-webpage) (accessed 2026-07-23): Identifies electrification, connectivity, automation, energy efficiency, and adoption pace as technologies shaping fluid power.
- **S10** — [Parker-Hannifin Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/76334/000007633425000035/ph-20250630.htm) (accessed 2026-07-23): Documents electric and hydraulic pumps and motors, aftermarket support, OEM-specification products, and diversified industrial, transport, off-highway, energy, and other end markets.
