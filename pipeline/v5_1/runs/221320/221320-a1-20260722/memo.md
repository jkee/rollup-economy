# 221320 — Sewage Treatment Facilities

*v5.1 Stage 1 research memo. Run `221320-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.12 · L 1.31 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Mandatory wastewater collection, treatment, and discharge compliance create durable recurring operator-required service.
**Weakness:** Public ownership, environmental liability, capital needs, permit and contract approvals, and limited private transferability constrain firm availability and value capture.

## Business-model lens
- Included: U.S. lower-middle-market operators of sewer systems and sewage treatment facilities that collect, convey, treat, and dispose of wastewater for external residential, commercial, industrial, municipal, institutional, or wholesale customers.
- Excluded: Municipal departments without a transferable operating business, captive industrial treatment systems, septic-tank and portable-toilet services, sewer cleaning and rodding contractors, non-sewer waste treatment facilities, water supply utilities, construction contractors, and software or equipment vendors that do not operate an in-scope system.
- Customer and revenue model: Recurring tariff, assessment, contracted, availability, capacity, volumetric, or wholesale revenue for accountable operation of sewer collection and wastewater treatment infrastructure serving external customers.
- Deviation from default lens: none

## Executive view
Sewage treatment provides essential recurring service and unusually direct evidence of deployed monitoring, analytics, and AI/ML. Physical collection and treatment, permit accountability, aging infrastructure, public ownership, capital intensity, and approval-heavy transfers keep the opportunity operationally constrained.

## How AI changes the work
AI can improve monitoring, overflow prediction, process decision support, capacity optimization, maintenance planning, billing, reporting, scheduling, and compliance preparation. Sampling, field work, repair, emergencies, and accountable effluent control remain operator-intensive.

## Value capture
Monopoly territories, tariff lag, fixed charges, and long contracts protect some benefit, but rate cases, municipal rebids, open-book terms, affordability, performance sharing, and compliance reinvestment can pass savings through.

## Firm availability
Private wastewater utilities and contract operators can fit the lens, but public facilities, special-purpose entities, captive systems, short contracts, and legal or permit-transfer constraints reduce an already small estimated firm pool.

## Demand durability
Population, connections, treatment standards, wet-weather management, reuse, and major infrastructure needs support durable service. Conservation, industrial shifts, drought, insourcing, and reduced infiltration constrain volume growth.

## Risks and uncertainty
Principal risks are permit violations, environmental liability, overflows, aging assets, extreme weather, cybersecurity, energy and chemical costs, public ownership, municipal procurement, contract concentration, rate pressure, capital intensity, and proxy mismatch.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2356 | — | OBSERVED | — |
| n | — | 89 | — | ESTIMATE | — |
| a | 0.19 | 0.31 | 0.43 | PROXY | S2, S3 |
| rho | 0.25 | 0.45 | 0.64 | PROXY | S3, S6 |
| e | 0.35 | 0.57 | 0.75 | ESTIMATE | S1, S6 |
| s5 | 0.07 | 0.16 | 0.28 | ESTIMATE | — |
| q | 0.3 | 0.48 | 0.66 | ESTIMATE | S4, S6 |
| d5 | 0.99 | 1.04 | 1.12 | PROXY | S4, S5 |
| o | 0.985 | 0.997 | 1 | ESTIMATE | S1, S3, S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.45 | 1.31 | 2.59 | PROXY |
| F | 1.86 | 3.56 | 4.79 | ESTIMATE |
| C | 6.00 | 9.60 | 10.00 | ESTIMATE |
| D | 9.75 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS data cover water, sewage, and other systems rather than 221320 alone and include public employers of all sizes.
- a: EPA smart-sewer cases show technical and capital benefits, not wage-weighted labor substitution across an entire treatment operator.
- rho: EPA case studies may select larger or more successful utilities than the private LMM population.
- rho: Compliance requirements establish implementation friction but do not measure AI adoption or realized savings.
- e: Most U.S. wastewater infrastructure is publicly owned, while the frozen firm count is derived from private-firm data; the exact surviving private business models are not observed.
- e: Facility ownership, contract operator, asset owner, and permittee can be different legal entities, complicating lens classification.
- s5: No national denominator of eligible privately controlled wastewater operators and completed control transfers was found.
- s5: Strategic environmental-service buyers may increase transaction frequency for contract operators even when treatment assets themselves do not transfer.
- q: Capture varies sharply among investor-owned asset utilities, municipal contract operators, public-private partnerships, industrial treatment contracts, and special districts.
- q: Avoided fines and deferred capital are economically valuable but are not necessarily retained labor benefit or distributable margin.
- d5: BLS projects broad NAICS 221300 including water systems, not wastewater treatment alone.
- d5: EPA's $630.1 billion need includes stormwater, nonpoint sources, and decentralized systems outside 221320 and measures capital requirements rather than service quantity.
- o: This estimates persistence of an accountable operator of the lens's kind, not survival of a particular owner, contract, or facility.
- o: Decentralized treatment and reuse can relocate responsibility without eliminating the need for accountable operation.

## Sources
- **S1** — [2022 NAICS Definition: 221320 Sewage Treatment Facilities](https://www.census.gov/naics/?details=221320&input=221320&year=2022) (accessed 2026-07-22): Exact industry scope and exclusions for waste disposal, water supply, septic, and sewer-cleaning activities.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Water, Sewage and Other Systems](https://www.bls.gov/oes/2023/may/naics4_221300.htm) (accessed 2026-07-22): Broad water-sector occupational structure used for the wage-weighted task-exposure bridge.
- **S3** — [Smart Sewers](https://www.epa.gov/npdes/smart-sewers) (accessed 2026-07-22): Deployed wastewater monitoring, modeling, analytics, AI/ML use cases, implementation constraints, and operating and capital outcomes.
- **S4** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Official ten-year employment and real-output projection for water, sewage, and other systems.
- **S5** — [Clean Watersheds Needs Survey](https://www.epa.gov/cwns) (accessed 2026-07-22): National twenty-year clean-water infrastructure need, category breakdown, treatment-facility count, and population served.
- **S6** — [Compliance Tips for Small, Mechanical Wastewater Treatment Plants](https://www.epa.gov/compliance/compliance-tips-small-mechanical-wastewater-treatment-plants) (accessed 2026-07-22): NPDES effluent-limit accountability for small public and private wastewater treatment plant owners and operators.
