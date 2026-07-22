# 811111 — General Automotive Repair

*v5.1 Stage 1 research memo. Run `811111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.38 · L 2.37 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large installed vehicle fleet continues to require accountable physical repair while customer and administrative workflows can be augmented.
**Weakness:** Most labor remains hands-on, and electric drivetrains reduce portions of the current mechanical maintenance basket.

## Business-model lens
- Included: US lower-middle-market general automotive repair firms providing repeat mechanical and electrical diagnosis, maintenance, engine repair, and replacement services to external vehicle owners and fleet customers.
- Excluded: Dealership service departments, parts retailers whose primary activity is retail, oil-change-only shops, specialized repair shops classified elsewhere, captive fleet garages, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat repair orders paid by consumers, commercial fleets, warranty administrators, or insurers, with revenue from labor, parts markup, diagnostic fees, and related shop charges.
- Deviation from default lens: none

## Executive view
General automotive repair has a durable physical-service core and a meaningful administrative and diagnostic surface for AI. The opportunity is bounded by hands-on technician work, fragmented shop systems, liability, and gradual electric-vehicle substitution for parts of the mechanical service basket.

## How AI changes the work
AI can improve intake, symptom summarization, inspection-note conversion, estimate drafting, parts lookup, scheduling, follow-up, bookkeeping, marketing, and knowledge retrieval. Technicians remain responsible for physical diagnosis, disassembly, repair, calibration, testing, and safety-critical judgment.

## Value capture
Posted labor rates, flat-rate times, diagnostic fees, and parts markups support initial retention. Competitive quotes, fleet or warranty terms, and customer expectations can return part of the benefit through pricing or added service.

## Firm availability
The injected estimate identifies 461 firms in the screened band, but its margin bridge may misclassify parts-intensive operators. General repair is usually lens-eligible; realized control-transfer evidence remains weaker than broad owner-sale intentions.

## Demand durability
BLS projects real automotive-repair output growth and FHWA projects continued mileage growth. Electric vehicles need less routine mechanical maintenance, but fleet turnover is gradual and physical repair remains necessary.

## Risks and uncertainty
Key risks are electric-vehicle mix, access to vehicle and repair data, technician shortages, safety or comeback liability, cybersecurity, parts availability, customer concentration, software integration, and overestimating firm eligibility through a uniform margin assumption.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3415 | — | OBSERVED | — |
| n | — | 461 | — | ESTIMATE | — |
| a | 0.18 | 0.28 | 0.4 | PROXY | S1 |
| rho | 0.42 | 0.62 | 0.78 | ESTIMATE | S5 |
| e | 0.68 | 0.82 | 0.92 | ESTIMATE | S3 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S6 |
| q | 0.45 | 0.65 | 0.82 | ESTIMATE | S5 |
| d5 | 1.02 | 1.09 | 1.18 | PROXY | S2, S4, S7 |
| o | 0.92 | 0.97 | 0.995 | ESTIMATE | S3, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.03 | 2.37 | 4.26 | ESTIMATE |
| F | 5.88 | 7.13 | 8.01 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.38 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS source covers NAICS 8111 rather than NAICS 811111 and excludes self-employed workers.
- a: Employment shares are transformed into a wage-weighted task estimate rather than directly measuring it.
- a: Current software automation varies widely across independent shops.
- rho: No source directly measures five-year implementation of the defined exposed opportunity.
- rho: Written estimates and customer authorization create a review requirement even when drafting is automated.
- rho: Implementation capacity may be lower in owner-operated single-site firms than in the screened band.
- e: Census reports 84,859 employer establishments in 2023 but does not identify the screened firms or recurring-revenue mix.
- e: The injected firm count uses a 15.65 percent margin bridge that may misclassify parts-intensive shops.
- e: Establishments and firms are not interchangeable.
- s5: The source covers employer businesses across industries and does not give a five-year realized transfer rate.
- s5: Internal family succession, asset liquidation, and dealer affiliation changes are not automatically qualifying transfers.
- s5: Owner age was not observed for the screened population.
- q: FTC guidance describes consumer billing practices but does not measure savings pass-through.
- q: Retention differs between retail, fleet, warranty, and insurer-funded work.
- q: Benefits that merely offset technician shortages should be measured consistently as avoided hiring.
- d5: BLS output is for NAICS 8111, not NAICS 811111, and measures aggregate output rather than a fixed service basket.
- d5: FHWA vehicle miles are a demand driver rather than repair quantity.
- d5: The speed and service mix of electric-vehicle adoption are uncertain.
- o: Electrification-driven elimination of maintenance belongs primarily in demand and is not counted again here.
- o: The operator may shift from an independent shop to a dealer or manufacturer-controlled network even when physical work remains.

## Sources
- **S1** — [Automotive Repair and Maintenance - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_811100.htm) (accessed 2026-07-22): Occupation employment and wage mix for NAICS 8111, including repair, office support, sales, management, customer service, bookkeeping, vehicle service, and cleaning roles.
- **S2** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects automotive repair and maintenance employment from 1.036 million in 2024 to 1.052 million in 2034 and constant-dollar output from 153.3 billion dollars to 183.5 billion dollars.
- **S3** — [811111: General Automotive Repair - Census Bureau Profile](https://data.census.gov/profile/811111_-_General_Automotive_Repair?codeset=naics~811111) (accessed 2026-07-22): Official industry scope and 84,859 employer establishments reported in 2023 County Business Patterns.
- **S4** — [2025 FHWA Forecasts of Vehicle Miles Traveled](https://www.fhwa.dot.gov/policyinformation/tables/vmt/vmt_forecast_sum.cfm) (accessed 2026-07-22): FHWA baseline projects light-duty vehicle miles traveled growing at an average annual rate of 0.6 percent through 2043.
- **S5** — [Auto Repair Basics](https://consumer.ftc.gov/articles/0211-auto-repair-basics) (accessed 2026-07-22): Consumer repair billing practices, including flat-rate labor, diagnostic charges, written estimates, parts disclosure, and authorization for additional work.
- **S6** — [Paths to Business Ownership](https://advocacy.sba.gov/wp-content/uploads/2021/03/Paths-to-Business-Ownership-fact-sheet.pdf) (accessed 2026-07-22): SBA summary of Census evidence that 22 percent of employer-business owners purchased their businesses and 64.5 percent of owners planned to sell.
- **S7** — [Maintenance and Safety of Electric Vehicles](https://afdc.energy.gov/vehicles/electric-maintenance) (accessed 2026-07-22): Energy Department comparison showing that all-electric vehicles require less maintenance because they have fewer moving parts, fewer fluids, and reduced brake wear.
