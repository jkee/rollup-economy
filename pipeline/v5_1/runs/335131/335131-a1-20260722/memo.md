# 335131 — Residential Electric Lighting Fixture Manufacturing

*v5.1 Stage 1 research memo. Run `335131-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** A large residential installed base combined with renovation, housing formation, and premiumization toward integrated and connected fixtures.
**Weakness:** Cyclical housing exposure and low switching costs in a highly import- and style-competitive product market.

## Business-model lens
- Included: Independent lower-middle-market manufacturers of fixed and portable residential electric lighting fixtures and metal, paper, or textile lamp shades, including indoor and outdoor ceiling, wall, pendant, recessed, track, table, floor, low-voltage, solar, decorative, and residential grow-light fixtures.
- Excluded: Commercial, industrial, institutional, roadway, and traffic lighting; LED semiconductor and bulb manufacturing; glass and plastic shade manufacturing; ceiling fans and bath fans with integrated lighting; current-carrying wiring devices; importers, distributors, retailers, installers, and design firms without principal domestic fixture-manufacturing activity; and captive divisions that are not independently marketable businesses.
- Customer and revenue model: Product revenue from homebuilders, electrical and lighting distributors, retailers, e-commerce channels, designers, remodelers, and homeowners. Repeat demand comes from new construction, renovation, style refreshes, replacement, and product-line introductions; branded and specified products can earn better margins than private-label or commodity fixtures.
- Deviation from default lens: none

## Executive view
Residential lighting fixtures combine a style- and channel-intensive product-development model with tangible manufacturing and compliance requirements. AI can accelerate design, visualization, merchandising, forecasting, and support, but housing cyclicality, imports, and physical production bound the upside.

## How AI changes the work
The most practical applications are concept exploration, renderings, CAD assistance, component and supplier analysis, demand planning, pricing, catalog and e-commerce content, customer-service triage, and back-office automation. Prototypes, optical and thermal performance, electrical safety, tooling, finishing, assembly, and inspection still require physical execution and expert judgment.

## Value capture
Branded firms with differentiated collections, disciplined inventory, and stable channels can convert faster product development and lower indirect labor into more launches and better margins. Builder-grade and private-label manufacturers face stronger pass-through pressure from retailers, distributors, and imported alternatives.

## Firm availability
The market contains independent decorative, architectural-residential, outdoor, portable-lamp, shade, low-voltage, and builder-focused manufacturers. Attractive targets are more likely to pair design and channel relationships with controlled working capital than to rely on commodity domestic fabrication alone.

## Demand durability
Homes require physical lighting, and the enormous installed base supports renovation and replacement. New construction adds cyclical demand, while LED longevity slows replacement and integrated controls shift product mix toward electronics and software-enabled features.

## Risks and uncertainty
Major uncertainties include housing and remodeling cycles, tariffs and import sourcing, retailer or builder concentration, style obsolescence, inventory markdowns, electrical and connected-product compliance, channel migration to e-commerce, and whether AI-generated designs increase differentiation or accelerate imitation.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3176 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.22 | 0.34 | 0.47 | PROXY | S1 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S1, S2 |
| e | 0.58 | 0.72 | 0.84 | ESTIMATE | S1, S2 |
| s5 | 0.08 | 0.17 | 0.3 | ESTIMATE | S3 |
| q | 0.35 | 0.52 | 0.7 | ESTIMATE | S2, S3 |
| d5 | 0.93 | 1.03 | 1.15 | ESTIMATE | S3, S4 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.98 | 2.25 | 4.06 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.74 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS table covers NAICS 335100, including commercial and other lighting products, rather than residential fixtures alone.
- a: Occupation shares are not task shares.
- a: Domestic manufacturers range from design-led assemblers to vertically integrated metalworking and finishing plants.
- rho: No direct task-level AI adoption evidence was available for residential fixture manufacturers.
- rho: Design-led firms may realize more substitution than plants with a high share of direct labor.
- e: Capture depends on brand strength, channel mix, inventory discipline, outsourced versus in-house production, and whether saved time translates to fewer costs or simply more product variants.
- s5: LED adoption evidence covers residential and commercial markets and predates the run date.
- s5: Substitution differs between portable decorative lamps, builder-grade fixtures, and integrated smart luminaires.
- q: No direct customer-retention data were available.
- q: Quality is likely higher for branded specification relationships and lower for private-label and promotional retail programs.
- d5: Monthly housing data are volatile and include multifamily units.
- d5: Installed lighting units are not annual fixture sales.
- d5: Domestic manufacturer revenue can diverge from end-market demand because of import share and channel inventory changes.
- o: Asset-light import-and-assemble models may consolidate more roles than vertically integrated plants.
- o: Small firms may already have highly combined management functions.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 335100](https://www.bls.gov/oes/2023/may/naics4_335100.htm) (accessed 2026-07-22): Broader lighting-industry occupation mix used as the task-exposure proxy.
- **S2** — [2022 NAICS Definition: Residential Electric Lighting Fixture Manufacturing](https://www.census.gov/naics/?details=335131&input=335131&year=2022) (accessed 2026-07-22): Official scope, illustrative products, and cross-reference exclusions for NAICS 335131.
- **S3** — [2020 U.S. Lighting Market Characterization](https://www.energy.gov/sites/default/files/2024-08/ssl-lmc2020_apr24.pdf) (accessed 2026-07-22): Residential installed-base size, LED penetration, technology transition, and lighting-market context.
- **S4** — [Monthly New Residential Construction, June 2026](https://www.census.gov/construction/nrc/current/) (accessed 2026-07-22): Current total and single-family housing-start evidence for demand conditions.
