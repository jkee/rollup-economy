# 333310 — Commercial and Service Industry Machinery Manufacturing

*v5.1 Stage 1 research memo. Run `333310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → CONDITIONAL · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Installed-base parts, service, and technical support can pair durable physical demand with implementable AI gains in knowledge-heavy workflows.
**Weakness:** A highly heterogeneous product code and missing firm-denominator evidence make eligible-firm supply and demand durability difficult to generalize.

## Business-model lens
- Included: US manufacturers in this code with repeat equipment programs, installed-base parts, upgrades, maintenance, diagnostics, or support sold to external commercial and service customers, where a transferable operating company can plausibly fall in the lower-middle-market band.
- Excluded: One-off project manufacturers without recurring or repeat customer revenue, captive units, shells, financing vehicles, and manufacturers whose activity is principally outside this NAICS code.
- Customer and revenue model: Customers include laundries, food-service operators, retailers, offices, automotive service businesses, entertainment venues, and other commercial users. Revenue combines equipment sales with repeat model orders and, for some firms, aftermarket parts, upgrades, field service, software, and support tied to an installed base.
- Deviation from default lens: The code combines materially different products and end markets, so the lens is narrowed to manufacturers with repeat equipment programs or installed-base aftermarket and service revenue. This is required for business-model coherence, not selected for attractiveness.

## Executive view
The coherent opportunity is not generic machinery production but repeat-program and installed-base businesses that combine physical equipment with parts, upgrades, service, diagnostics, or support. These businesses have useful AI opportunities around knowledge work and service, yet their factory labor and product breadth constrain uniform automation.

## How AI changes the work
AI can improve quoting, engineering documentation, procurement, scheduling, customer support, field diagnostics, visual quality control, and predictive maintenance. Physical fabrication, assembly, installation, testing, and repair remain operator-intensive, and advanced plant use cases require validated data and integration with legacy equipment.

## Value capture
Proprietary equipment, technical know-how, and installed-base relationships support retention through margin, faster response, and higher service quality. Benefits leak through competitive bids, distributor and customer bargaining, renewal repricing, and transparent component economics.

## Firm availability
The code likely contains eligible private manufacturers, but the assigned firm-count input is missing and the available industry definition does not identify earnings size, recurring revenue, or ownership. Availability is therefore more uncertain than the point estimate suggests and requires a firm-level market map.

## Demand durability
Broader machinery output is projected to grow modestly, while physical service end markets continue to need reliable capital equipment and aftermarket support. Durability is uneven: laundry, vending, cooking, automotive-service, optical, and amusement applications remain physical, whereas office and photographic machinery can lose volume to digital workflows.

## Risks and uncertainty
The central risk is aggregation error across very different product markets. Other risks include cyclical capital spending, customer concentration, long replacement cycles, supply-chain exposure, liability, legacy-system integration, scarce technical labor, and faster software substitution in selected product classes. Missing six-digit transfer and firm-count evidence materially weakens firm-availability confidence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2932 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.19 | 0.3 | 0.41 | PROXY | S1, S2 |
| rho | 0.24 | 0.41 | 0.59 | ESTIMATE | S2 |
| e | 0.37 | 0.55 | 0.71 | ESTIMATE | S4 |
| s5 | 0.12 | 0.22 | 0.35 | ESTIMATE | — |
| q | 0.38 | 0.58 | 0.75 | ESTIMATE | S4 |
| d5 | 0.91 | 1.06 | 1.22 | PROXY | S3, S4 |
| o | 0.93 | 0.98 | 1 | ESTIMATE | S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.53 | 1.44 | 2.84 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.46 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source is for NAICS 333300 rather than the six-digit industry.
- a: The mapping measures task potential, not observed deployment, and product-level labor mixes vary substantially within the code.
- rho: DOE examples establish technical feasibility across manufacturing rather than adoption rates in this industry.
- rho: Legacy controls, fragmented data, product liability, and small-firm implementation capacity are not measured directly.
- e: The assigned firm-count denominator is unavailable and was not replaced or re-estimated.
- e: The Census definition confirms product breadth but does not measure recurring revenue or earnings-band eligibility.
- s5: This is bounded judgment without observed six-digit transfer rates.
- s5: The assigned firm-count denominator is missing, preventing a check against the implied absolute number of transfers.
- q: No industry-wide evidence directly measures sharing of AI-enabled benefits.
- q: Retention is likely higher in proprietary aftermarket service than in competitively bid equipment sales.
- d5: The direct projection covers NAICS 333300, not this six-digit industry.
- d5: Real output is not a pure physical-unit measure and the base period differs from the packet date.
- d5: Office, photographic, laundry, vending, cooking, optical, and automotive-service equipment can follow materially different demand paths.
- o: The estimate applies after the demand change in d5 and does not count the same volume loss twice.
- o: Digital substitution risk is concentrated in only some of the many products covered by this NAICS code.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 333300 Machinery Manufacturing](https://www.bls.gov/oes/2023/may/naics4_333300.htm) (accessed 2026-07-22): Broader-subsector employment and occupation mix, including production, assembly, inspection, repair, management, business, engineering, and office roles used for the AI task-exposure bridge.
- **S2** — [Artificial Intelligence for Energy: Opportunities for a Modern Grid and Clean Energy Economy](https://www.energy.gov/sites/default/files/2024-04/AI%20EO%20Report%20Section%205.2g%28i%29_043024.pdf) (accessed 2026-07-22): Manufacturing AI applications including automated visual quality control, advanced characterization, operations optimization, and predictive maintenance using connected equipment data.
- **S3** — [Industry Employment and Output Projections, 2024 to 2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Broader NAICS 333300 real-output projection and adjacent commercial-service industry growth used as demand evidence.
- **S4** — [2022 NAICS Search: 333310 Commercial and Service Industry Machinery Manufacturing](https://www.census.gov/naics/?details=333310&input=333310&year=2022) (accessed 2026-07-22): Official industry scope spanning optical, photographic, vending, laundry, office, automotive-maintenance, and commercial-cooking machinery, establishing product and end-market heterogeneity.
