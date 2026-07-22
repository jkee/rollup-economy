# 811114 — Specialized Automotive Repair

*v5.1 Stage 1 research memo. Run `811114-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Specialist technical knowledge and recurring physical repair needs support operator relevance and selective AI augmentation.
**Weakness:** The code mixes specialties with sharply different exposure to electric-drivetrain substitution, and the frozen firm count is missing.

## Business-model lens
- Included: US lower-middle-market firms providing repeat specialized mechanical or electrical repair services, including brake, suspension, exhaust, transmission, electrical, and tune-up work, to external vehicle owners and fleet customers.
- Excluded: General automotive repair, engine repair and replacement, dealership service departments, oil-change-only shops, body and glass shops, captive fleet garages, parts retailers, shells, and non-control financing vehicles.
- Customer and revenue model: Repair orders paid by consumers, fleets, warranty administrators, or insurers, with revenue from specialist labor, diagnostics, parts markup, and related shop charges.
- Deviation from default lens: none

## Executive view
Specialized automotive repair offers AI assistance in diagnosis and administration but is dominated by physical, safety-critical work. Demand is more exposed than general repair to powertrain change because exhaust, transmission, and tune-up services shrink as electric vehicles enter the fleet.

## How AI changes the work
AI can support fault triage, technical retrieval, estimate drafting, parts matching, scheduling, documentation, and customer communication. Physical inspection, repair, adjustment, testing, and accountable safety judgment remain human and equipment intensive.

## Value capture
Scarce expertise and specialist pricing can protect initial benefits, while price comparison, substitute general shops, fleets, and warranty administrators reduce long-run retention.

## Firm availability
The frozen firm count is missing and is not replaced. Census confirms a sizable all-size specialty population, but eligibility and screened-band membership require firm-level review, and realized transfer evidence is unavailable.

## Demand durability
Mileage and the existing combustion fleet support service, but electric vehicles reduce or eliminate several legacy specialties. Adaptable electrical and chassis specialists should fare better than narrowly combustion-dependent shops.

## Risks and uncertainty
The main uncertainties are specialty mix, electric-vehicle fleet transition, repair-data access, technician skills, safety liability, software integration, parts availability, customer concentration, and the unresolved screened-firm count.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4052 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.25 | 0.36 | PROXY | S1, S3 |
| rho | 0.38 | 0.56 | 0.72 | ESTIMATE | S5 |
| e | 0.7 | 0.86 | 0.95 | ESTIMATE | S3 |
| s5 | 0.1 | 0.2 | 0.32 | PROXY | S6 |
| q | 0.48 | 0.68 | 0.84 | ESTIMATE | S5 |
| d5 | 0.85 | 0.98 | 1.1 | PROXY | S2, S4, S7 |
| o | 0.86 | 0.94 | 0.98 | ESTIMATE | S3, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.99 | 2.27 | 4.20 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.31 | 9.21 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source covers NAICS 8111 and excludes self-employed workers.
- a: Brake, transmission, exhaust, suspension, and electrical shops can have materially different task mixes.
- a: The estimate transforms employment shares into wage-weighted task exposure.
- rho: No source directly measures five-year AI implementation for specialized repair firms.
- rho: Implementation varies with scan-tool access, manufacturer information, and specialty workflow standardization.
- rho: Written estimates and customer authorization require controlled review.
- e: The frozen firm count is missing and must not be inferred from Census firm or establishment totals.
- e: Census reported 7,708 firms and 8,042 establishments in 2022 across all sizes, not the screened band.
- e: Eligibility may differ materially across specialties.
- s5: The source is all-industry and does not measure five-year realized control transfers.
- s5: The missing frozen firm count prevents translating this conditional probability into a target count.
- s5: Internal succession and asset-only liquidation are not automatically qualifying transfers.
- q: FTC guidance describes consumer billing but not benefit pass-through.
- q: Pricing power differs between scarce electrical or transmission expertise and more comparable brake or exhaust work.
- q: Warranty and fleet contracts can retain more of the savings for the payer.
- d5: BLS projections are published above the six-digit specialty code.
- d5: FHWA mileage is a demand driver rather than direct repair quantity.
- d5: The range blends specialties with structurally different exposure to electric vehicles.
- o: Demand eliminated by drivetrain change is assigned to d5 and should not be counted again here.
- o: An operator may remain necessary while the work migrates to dealer or manufacturer-controlled networks.
- o: Operator necessity differs substantially across the code's specialties.

## Sources
- **S1** — [Automotive Repair and Maintenance - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_811100.htm) (accessed 2026-07-22): Occupation employment and wage mix for NAICS 8111, including repair, office support, sales, management, customer service, bookkeeping, vehicle service, and cleaning roles.
- **S2** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects automotive mechanical and electrical repair employment from 444,000 in 2024 to 450,300 in 2034 and projects broader automotive-repair output growth.
- **S3** — [Other Services Summary Statistics: 2022 Economic Census](https://data.census.gov/table/ECNBASIC2022.EC2281BASIC) (accessed 2026-07-22): Census definition and 2022 all-size counts of 7,708 firms and 8,042 establishments for specialized automotive repair.
- **S4** — [2025 FHWA Forecasts of Vehicle Miles Traveled](https://www.fhwa.dot.gov/policyinformation/tables/vmt/vmt_forecast_sum.cfm) (accessed 2026-07-22): FHWA baseline projects light-duty vehicle miles traveled growing at an average annual rate of 0.6 percent through 2043.
- **S5** — [Auto Repair Basics](https://consumer.ftc.gov/articles/0211-auto-repair-basics) (accessed 2026-07-22): Consumer repair billing practices, including flat-rate labor, diagnostic charges, written estimates, parts disclosure, and authorization for additional work.
- **S6** — [Paths to Business Ownership](https://advocacy.sba.gov/wp-content/uploads/2021/03/Paths-to-Business-Ownership-fact-sheet.pdf) (accessed 2026-07-22): SBA summary of Census evidence that 22 percent of employer-business owners purchased their businesses and 64.5 percent of owners planned to sell.
- **S7** — [Maintenance and Safety of Electric Vehicles](https://afdc.energy.gov/vehicles/electric-maintenance) (accessed 2026-07-22): Energy Department comparison showing that all-electric vehicles require less maintenance because they have fewer moving parts, fewer fluids, and reduced brake wear.
