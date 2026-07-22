# 811121 — Automotive Body, Paint, and Interior Repair and Maintenance

*v5.1 Stage 1 research memo. Run `811121-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.90 · L 1.88 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Remaining collision and customization work requires accountable physical operators, while estimating and claims administration offer AI leverage.
**Weakness:** The dominant production labor is hands-on, and insurers can recapture savings through rates, networks, and service requirements.

## Business-model lens
- Included: US lower-middle-market firms providing repeat outsourced collision, body, paint, trailer-body, interior repair, restoration, and vehicle customization services to external consumers, fleets, and insurers.
- Excluded: Automotive glass-only shops, assembly-line vehicle conversion, dealerships whose primary activity is vehicle retail, captive fleet body shops, motorcycle repair, shells, and non-control financing vehicles.
- Customer and revenue model: Repair orders funded by vehicle owners, insurers, fleets, or warranty administrators, with revenue from labor, paint and materials, parts markup, supplements, storage, and related shop charges.
- Deviation from default lens: none

## Executive view
Automotive body and paint repair has a modest AI-exposed estimating and administrative layer atop a highly physical production process. Demand is supported by vehicle travel and growing repair complexity but constrained by collision avoidance, insurer influence, and total-loss economics.

## How AI changes the work
AI can assist image and document intake, estimate drafting, parts matching, supplement preparation, scheduling, customer updates, and administration. Teardown, structural work, preparation, painting, reassembly, calibration, testing, and quality accountability remain physical and expert-led.

## Value capture
Retail restoration and customization can retain more savings than insurer-funded collision work. Direct-repair arrangements, labor-rate negotiation, supplements, and network competition are likely to share a material portion of benefits.

## Firm availability
The injected estimate identifies 175 firms in the screened band, though the uniform margin bridge may misclassify materials-intensive operators. Most collision shops fit the service lens, while project-heavy restoration and customization require closer review.

## Demand durability
Mileage growth and vehicle complexity support repair activity. Automatic emergency braking and other safety systems reduce some crashes, while cameras, sensors, calibration, expensive parts, and specialized procedures add work to remaining repairs.

## Risks and uncertainty
Major risks include insurer concentration, labor-rate pressure, technician shortages, total-loss thresholds, parts delays, calibration liability, paint and environmental compliance, safety-system adoption, software integration, and overestimating screened firms through a uniform margin assumption.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3867 | — | OBSERVED | — |
| n | — | 175 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.32 | PROXY | S1, S3 |
| rho | 0.4 | 0.58 | 0.72 | ESTIMATE | S5 |
| e | 0.7 | 0.84 | 0.93 | ESTIMATE | S3 |
| s5 | 0.12 | 0.23 | 0.35 | PROXY | S6 |
| q | 0.3 | 0.5 | 0.68 | ESTIMATE | S5 |
| d5 | 0.96 | 1.05 | 1.15 | PROXY | S2, S4, S7, S8 |
| o | 0.95 | 0.985 | 0.998 | ESTIMATE | S3, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.74 | 1.88 | 3.56 | ESTIMATE |
| F | 4.43 | 5.71 | 6.53 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.12 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation source covers NAICS 8111 rather than NAICS 811121 and excludes self-employed workers.
- a: Restoration, upholstery, fleet, and insurance collision shops have different task mixes.
- a: Employment shares are transformed into wage-weighted task exposure rather than directly measuring it.
- rho: No source directly measures five-year implementation of the defined AI-exposed opportunity.
- rho: Customer authorization and repair safety require controlled human review.
- rho: Insurer-mandated platforms can accelerate standardization but restrict shop-level tool choice.
- e: Census reports 35,029 employer establishments in 2023 but does not identify screened-band firms or revenue recurrence.
- e: The injected firm count uses a 15.65 percent margin bridge that may misclassify parts- and materials-intensive body shops.
- e: Establishments and firms are not interchangeable.
- s5: The source is all-industry and does not measure five-year realized transfers.
- s5: Internal succession, franchise changes, and asset-only liquidations are not automatically qualifying transfers.
- s5: Owner age and succession plans were not observed for the screened population.
- q: FTC guidance describes consumer estimates and authorization, not insurer bargaining or benefit pass-through.
- q: Retention differs sharply between insurer-funded collision work, fleet contracts, restoration, and customer-paid customization.
- q: Faster cycle time may create volume capacity even when per-job price does not rise.
- d5: BLS combines body, paint, interior, and glass at the five-digit level rather than isolating NAICS 811121.
- d5: Employment is not a direct measure of constant-price, constant-quality service quantity.
- d5: IIHS rear-end crash reductions do not represent all collision types or all vehicles.
- d5: Total-loss thresholds can reduce repair quantity even when crash severity and vehicle values rise.
- o: Some repairable vehicles may instead be declared total losses, which belongs primarily in demand.
- o: Physical operator need can persist while work migrates from independent firms to insurer- or manufacturer-controlled networks.
- o: Remote photo estimating changes administration, not the underlying physical repair requirement.

## Sources
- **S1** — [Automotive Repair and Maintenance - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_811100.htm) (accessed 2026-07-22): Occupation employment and wage mix for NAICS 8111, including body repair, office support, sales, management, customer service, bookkeeping, vehicle service, and cleaning roles.
- **S2** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects automotive body, paint, interior, and glass repair employment from 297,500 in 2024 to 305,100 in 2034.
- **S3** — [811121: Automotive Body, Paint, and Interior Repair and Maintenance - Census Bureau Profile](https://data.census.gov/profile/811121_-_Automotive_Body%2C_Paint%2C_and_Interior_Repair_and_Maintenance?codeset=naics~811121&g=010XX00US) (accessed 2026-07-22): Official industry definition and 35,029 employer establishments reported in 2023 County Business Patterns.
- **S4** — [Automotive Body and Glass Repairers](https://www.bls.gov/ooh/installation-maintenance-and-repair/automotive-body-and-glass-repairers.htm) (accessed 2026-07-22): BLS projects body and glass repairer employment growth and states that collision-prevention systems may limit accidents while cameras and sensors create repair work.
- **S5** — [Auto Repair Basics](https://consumer.ftc.gov/articles/0211-auto-repair-basics) (accessed 2026-07-22): Consumer repair billing practices, including flat-rate labor, diagnostic charges, written estimates, parts disclosure, and authorization for additional work.
- **S6** — [Paths to Business Ownership](https://advocacy.sba.gov/wp-content/uploads/2021/03/Paths-to-Business-Ownership-fact-sheet.pdf) (accessed 2026-07-22): SBA summary of Census evidence that 22 percent of employer-business owners purchased their businesses and 64.5 percent of owners planned to sell.
- **S7** — [2025 FHWA Forecasts of Vehicle Miles Traveled](https://www.fhwa.dot.gov/policyinformation/tables/vmt/vmt_forecast_sum.cfm) (accessed 2026-07-22): FHWA baseline projects light-duty vehicle miles traveled growing at an average annual rate of 0.6 percent through 2043.
- **S8** — [Effectiveness of Forward Collision Warning and Autonomous Emergency Braking Systems in Reducing Front-to-Rear Crash Rates](https://www.iihs.org/research-areas/bibliography/ref/2111) (accessed 2026-07-22): IIHS study reports reductions in rear-end striking crashes associated with forward-collision warning and automatic emergency braking.
