# 335132 — Commercial, Industrial, and Institutional Electric Lighting Fixture Manufacturing

*v5.1 Stage 1 research memo. Run `335132-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Efficiency retrofits and integration of lighting with sensors and connected building controls.
**Weakness:** Long product lives and intense specification-based competition in standardized fixture categories.

## Business-model lens
- Included: Independent lower-middle-market manufacturers of electric luminaires and fixtures principally designed for commercial, industrial, and institutional buildings, including troffers, linear ambient fixtures, high- and low-bay luminaires, architectural fixtures, task and specialty building fixtures, and integrated LED and control-ready products.
- Excluded: Residential, roadway, vehicular, traffic-signal, and nonelectric lighting; LED semiconductor and standalone bulb manufacturing; current-carrying wiring devices; controls-only software or hardware vendors; distributors, lighting designers, contractors, and installers without principal fixture manufacturing; and captive divisions not independently marketable.
- Customer and revenue model: Project, specification, distributor, OEM, retrofit, and replacement revenue from electrical distributors, contractors, architects and engineers, facility owners, industrial operators, institutions, energy-service companies, and public agencies. Repeat demand reflects specifications, product families, renovation cycles, warranties, controls compatibility, and installed-base replacement.
- Deviation from default lens: none

## Executive view
Commercial, industrial, and institutional lighting is a technical specification and project-channel business wrapped around physical manufacturing. AI can accelerate engineering support, quotations, submittals, and service, while fixture performance, certification, controls interoperability, production, and project execution remain defensible human and physical work.

## How AI changes the work
High-value uses include code and specification search, fixture selection support, photometric analysis, CAD assistance, bill-of-material review, quotation, submittal generation, project tracking, field-support triage, and administration. Testing, certification, thermal and optical validation, factory operations, quality assurance, and accountable application decisions limit replacement.

## Value capture
Firms with specified products, usable technical data, controls expertise, and disciplined channels can convert productivity into faster response, more project coverage, and lower indirect cost. Standardized products sold through tenders or powerful distributors face greater price pass-through.

## Firm availability
Potential targets include architectural, industrial high-bay, institutional, retrofit, linear, specialty, and controls-ready luminaire makers. Attractive independents tend to own application know-how, certifications, product data, and channel relationships rather than competing solely on sheet metal and assembly.

## Demand durability
Buildings require physical light, and a large legacy stock still offers retrofit and controls opportunities. Public, institutional, warehouse, data-center, and industrial investment can support demand even when offices soften, but long-lived LEDs reduce routine replacement frequency.

## Risks and uncertainty
Uncertainties include nonresidential construction cycles, office utilization, public budgets, code adoption, energy prices and incentives, distributor concentration, imports, component availability, cybersecurity and interoperability of connected products, warranty exposure, and the pace at which value shifts to controls platforms.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3176 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.24 | 0.36 | 0.49 | PROXY | S1, S4 |
| rho | 0.36 | 0.54 | 0.7 | ESTIMATE | S3, S4 |
| e | 0.6 | 0.74 | 0.85 | ESTIMATE | S3, S4 |
| s5 | 0.1 | 0.21 | 0.34 | ESTIMATE | S3, S4 |
| q | 0.44 | 0.64 | 0.8 | ESTIMATE | S4 |
| d5 | 0.97 | 1.08 | 1.22 | ESTIMATE | S3, S4, S5 |
| o | 0.95 | 0.98 | 1 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.10 | 2.47 | 4.36 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 8.80 | 10.00 | 10.00 | ESTIMATE |
| D | 9.21 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS table covers all NAICS 335100 lighting manufacturing, not only commercial, industrial, and institutional fixtures.
- a: Occupation shares are not task shares.
- a: The balance of engineering, specification support, and direct production differs across standard and custom manufacturers.
- rho: Direct task-level AI adoption data were unavailable for the six-digit industry.
- rho: Custom engineered and controls-rich products may see high augmentation but slower autonomous substitution because errors affect projects and compliance.
- e: Value capture varies with custom content, brand and specification strength, channel concentration, controls software ownership, and the ability to translate faster work into lower cost or additional project wins.
- s5: DOE adoption figures are older than the run date.
- s5: Integrated controls may expand fixture value for capable manufacturers while displacing undifferentiated products.
- s5: Service-life extension lowers replacement frequency but does not remove renovation or performance-upgrade demand.
- q: No direct retention data were available.
- q: Quality is strongest in proprietary, custom, or tightly specified applications and weaker in commodity troffers and linear fixtures.
- d5: Construction spending includes many categories unrelated to lighting and reflects price as well as volume.
- d5: Efficiency and control retrofits depend on energy prices, incentives, capital budgets, and code adoption.
- d5: Long LED lives can defer ordinary replacement after retrofit waves mature.
- o: Highly standardized manufacturers may centralize more support work than custom architectural or controls-rich firms.
- o: Small firms may already operate with combined roles and thin management layers.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 335100](https://www.bls.gov/oes/2023/may/naics4_335100.htm) (accessed 2026-07-22): Broader lighting-industry occupation mix used as the task-exposure proxy.
- **S2** — [2022 NAICS Definition: Commercial, Industrial, and Institutional Electric Lighting Fixture Manufacturing](https://www.census.gov/naics/?details=335132&input=335132&year=2022) (accessed 2026-07-22): Official six-digit industry definition and boundary.
- **S3** — [LED Adoption Report](https://www.energy.gov/cmei/ssl/led-adoption-report) (accessed 2026-07-22): LED penetration, connected-controls adoption, and remaining commercial and industrial energy-savings opportunity.
- **S4** — [Purchasing Energy-Efficient Commercial and Industrial LED Luminaires](https://www.energy.gov/cmei/femp/purchasing-energy-efficient-commercial-and-industrial-led-luminaires) (accessed 2026-07-22): Current efficiency, controls, qualification, warranty, product-availability, and service-life evidence for commercial luminaires.
- **S5** — [Monthly Construction Spending, May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-22): Current private nonresidential, public, and educational construction-spending conditions.
