# 333413 — Industrial and Commercial Fan and Blower and Air Purification Equipment Manufacturing

*v5.1 Stage 1 research memo. Run `333413-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.65 · L 1.85 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Installed-base parts, filters, retrofits, and technical support combine persistent physical air-quality needs with AI-addressable engineering and service workflows.
**Weakness:** Physical production constrains labor substitution, while project cyclicality and weak firm-level transfer evidence make realizable opportunity uncertain.

## Business-model lens
- Included: US firms in NAICS 333413 that supply recurring or repeat outsourced work to external customers through engineered fan, blower, dust-collection, filtration, or stationary air-purification equipment programs and associated parts, filters, controls, upgrades, maintenance, diagnostics, or technical support, within the lower-middle-market band.
- Excluded: Pure one-off product sellers without repeat customer work, household-type fans and portable air purifiers assigned to other industries, air-conditioning equipment manufacturers, captive internal units, shells, and non-control financing vehicles.
- Customer and revenue model: Customers include industrial plants, commercial buildings, institutions, contractors, and equipment integrators. Revenue can combine engineered equipment orders with repeat replacement projects, filters and wear parts, controls, upgrades, field service, inspection, commissioning, and technical support tied to an installed base.
- Deviation from default lens: none

## Executive view
The default lens is coherent for engineered fan, blower, and stationary air-purification manufacturers with repeat projects or installed-base aftermarket work. AI has credible uses in engineering and service knowledge, but physical production and field accountability limit substitution. Demand rests on persistent ventilation, filtration, and industrial-exhaust requirements rather than on a speculative federal efficiency mandate.

## How AI changes the work
AI can improve application engineering, configuration, quoting, procurement, scheduling, technical documentation, customer support, visual inspection, diagnostics, and predictive maintenance. Fabrication, assembly, balancing, testing, installation, commissioning, and repair remain physical, while advanced use cases require reliable product data, sensors, integration, cybersecurity, and human validation.

## Value capture
Installed-base compatibility, engineered performance, technical know-how, warranty accountability, and response time support retention through margin and service quality. Benefit leakage is strongest in standard equipment bids and distributor channels where customers can compare specifications and prices.

## Firm availability
The assigned dataset indicates a meaningful potential firm population, but it is estimated and the eligible share is not observed. A firm-level map is needed to distinguish recurring parts, filters, retrofits, and service businesses from project-only manufacturers and distributor-dependent product sellers.

## Demand durability
Industrial dust and fume control, commercial ventilation, filtration, and air cleaning perform physical health, safety, and building functions. EPA identifies ventilation and filtration as indoor-air-quality practices, and OSHA standards require functional exhaust and dust-control systems in covered settings. Demand should persist, though replacement timing remains exposed to construction and industrial capital cycles.

## Risks and uncertainty
Key risks are cyclical project spending, long equipment lives, raw-material and motor supply exposure, customer concentration, distributor power, technical labor scarcity, product liability, and integration complexity. The federal fan-efficiency standards proposal was withdrawn, so regulation cannot be assumed to accelerate demand. Firm eligibility and transfer rates remain estimates without six-digit ownership or transaction evidence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3015 | — | OBSERVED | — |
| n | — | 163 | — | ESTIMATE | — |
| a | 0.21 | 0.34 | 0.46 | PROXY | S1, S2 |
| rho | 0.28 | 0.45 | 0.63 | ESTIMATE | S2 |
| e | 0.31 | 0.48 | 0.65 | ESTIMATE | S3, S6 |
| s5 | 0.13 | 0.23 | 0.35 | ESTIMATE | — |
| q | 0.43 | 0.62 | 0.78 | ESTIMATE | S6, S7 |
| d5 | 0.98 | 1.06 | 1.15 | PROXY | S4, S5, S6 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S3, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.71 | 1.85 | 3.49 | ESTIMATE |
| F | 3.26 | 4.74 | 5.85 | ESTIMATE |
| C | 8.60 | 10.00 | 10.00 | ESTIMATE |
| D | 9.41 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source covers a different four-digit machinery subsector and is therefore only a labor-mix proxy.
- a: The mapping estimates current unautomated task exposure rather than observed AI deployment, and eligible service-rich firms may differ from the industry average.
- rho: DOE establishes manufacturing use cases and technical feasibility rather than adoption rates in NAICS 333413.
- rho: Small-firm software maturity, product-liability controls, customer data access, and legacy equipment constraints are not measured directly.
- e: The assigned firm-count input is a margin-bridged estimate rather than an observed count of eligible firms.
- e: Official industry scope does not identify recurring revenue, earnings, ownership, or transferability.
- s5: This is bounded judgment without an observed industry-specific transfer rate.
- s5: The estimated firm denominator and sparse disclosure of small private transactions weaken calibration.
- q: No source directly measures commercial retention of AI-enabled benefits in this industry.
- q: Retention is likely higher for proprietary retrofits, controls, and service than for competitively specified standard equipment.
- d5: The BLS output series combines several machinery industries and is not specific to NAICS 333413.
- d5: Real output is an imperfect quantity measure and can reflect mix and quality changes.
- d5: DOE currently reports no federal energy conservation standards for fans and blowers after withdrawal of the proposal, so federal efficiency regulation is not treated as a guaranteed replacement-cycle catalyst.
- o: The estimate applies after the quantity change in d5 and avoids counting demand loss twice.
- o: Some monitoring and controls may shift to building-management platforms or larger integrated OEMs, but the physical air-handling function remains.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 333300 Commercial and Service Industry Machinery Manufacturing](https://www.bls.gov/oes/2023/may/naics4_333300.htm) (accessed 2026-07-22): Comparison machinery-manufacturing occupation mix and wages used to bridge physical production and knowledge-work exposure.
- **S2** — [Artificial Intelligence for Energy: Opportunities for a Modern Grid and Clean Energy Economy](https://www.energy.gov/sites/default/files/2024-04/AI%20EO%20Report%20Section%205.2g%28i%29_043024.pdf) (accessed 2026-07-22): Manufacturing AI applications including automated visual quality control, advanced characterization, operations optimization, and predictive maintenance using connected equipment data.
- **S3** — [Census Bureau Profile: NAICS 333413 Industrial and Commercial Fan and Blower and Air Purification Equipment Manufacturing](https://data.census.gov/profile/333413_-_Industrial_and_Commercial_Fan_and_Blower_and_Air_Purification_Equipment_Manufacturing?codeset=naics~333413) (accessed 2026-07-22): Official scope covering stationary air purification, industrial dust and fume collection, furnace filters, air washers, attic fans, and industrial and commercial fans and blowers.
- **S4** — [Industry Employment and Output Projections, 2024 to 2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Real-output projection for the combined machinery group containing NAICS 3334, used as the broad demand-growth proxy.
- **S5** — [What Is Indoor Air Quality?](https://www.epa.gov/indoor-air-quality-iaq/factsheet-what-indoor-air-quality) (accessed 2026-07-22): EPA evidence that improved ventilation and filtration or supplemental air cleaning are core practices for improving indoor air quality.
- **S6** — [29 CFR 1910.94 Ventilation](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.94) (accessed 2026-07-22): Requirements for exhaust ventilation and dust-collection systems, including construction, installation, inspection, maintenance, testing, and suitable dust collectors.
- **S7** — [Fans and Blowers](https://www.energy.gov/cmei/buildings/fans-and-blowers) (accessed 2026-07-22): Current DOE status showing required federal test procedures and efficiency representations, withdrawal of the proposed standards, and no current federal fan and blower energy conservation standards.
