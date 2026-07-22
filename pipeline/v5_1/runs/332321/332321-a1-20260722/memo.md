# 332321 — Metal Window and Door Manufacturing

*v5.1 Stage 1 research memo. Run `332321-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.24 · L 1.54 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Configured-to-order products create recurring digital work from specification and quote through production and certification.
**Weakness:** Much of the industry is product manufacturing, and physical assembly plus competitive channels constrain substitution and retention.

## Business-model lens
- Included: US lower-middle-market metal window, door, frame, screen, trim, and curtain-wall manufacturers that repeatedly configure, engineer, fabricate, glaze, assemble, finish, and supply custom products to external dealers, contractors, architects, and building owners.
- Excluded: Installation contractors, distributors, wood-window manufacturers, automotive trim producers, captive internal plants, firms outside the EBITDA band, shells, and non-control financing vehicles.
- Customer and revenue model: Quoted per-unit, package, or project revenue through dealer, contractor, and specification channels, with configuration, engineering, fabrication, testing documentation, warranties, and delivery often bundled.
- Deviation from default lens: none

## Executive view
Metal window and door manufacturing offers AI opportunities in configuration, estimating, engineering, scheduling, quality inspection, forecasting, and service, while physical assembly and certification remain operator-required. The recurring-service lens fits custom and contract suppliers better than standard branded-product manufacturers.

## How AI changes the work
AI can translate opening schedules and specifications into configurations, quotes, drawings, cut lists, production plans, inspection flags, certification records, and customer responses. Humans still manage exceptions, materials, machining, welding, glazing, sealing, finishing, testing, maintenance, and release.

## Value capture
Customization, certification, reliable lead times, dealer service, and warranties support retention, while comparable products, contractor bidding, channel rebates, price-book updates, and private-label tenders transmit gains to customers.

## Firm availability
Only a portion of the estimated population clearly supplies an outsourced recurring service. Custom engineering, private-label work, repeat external accounts, management depth, certification, warranty history, and normalized earnings require firm-level confirmation.

## Demand durability
Replacement and energy upgrades temper weakness in new construction, but metal products compete with vinyl, wood, fiberglass, and imports. Commercial and residential cycles, codes, incentives, and regional material preferences create a wide five-year range.

## Risks and uncertainty
Major risks are service-lens ambiguity, construction cyclicality, channel concentration, raw-material volatility, warranty and water-infiltration claims, certification failures, custom-product complexity, imported competition, and overstatement in the margin-bridged firm count.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2453 | — | OBSERVED | — |
| n | — | 279 | — | ESTIMATE | — |
| a | 0.16 | 0.27 | 0.4 | PROXY | S1, S2 |
| rho | 0.38 | 0.58 | 0.74 | ESTIMATE | S3 |
| e | 0.18 | 0.35 | 0.55 | ESTIMATE | S1, S3 |
| s5 | 0.1 | 0.18 | 0.29 | PROXY | S4 |
| q | 0.28 | 0.46 | 0.63 | ESTIMATE | S3 |
| d5 | 0.84 | 0.99 | 1.14 | PROXY | S3, S5 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.60 | 1.54 | 2.90 | ESTIMATE |
| F | 2.89 | 4.70 | 6.14 | ESTIMATE |
| C | 5.60 | 9.20 | 10.00 | ESTIMATE |
| D | 7.56 | 9.50 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupation-by-task dataset was located.
- a: Highly configured architectural systems and standard residential lines have materially different information and production labor mixes.
- rho: Certification and energy-performance evidence establishes constraints and product complexity, not observed AI implementation.
- rho: Smaller manufacturers may lack clean configuration and warranty data.
- e: Eligibility depends on the boundary between repeat configured manufacturing and outsourced service.
- e: The provided firm count is a margin-bridged ESTIMATE and may include product-only or nontransferable operations.
- s5: Gallup is not industry- or size-specific and measures plans rather than completed transfers.
- s5: A strategic plant purchase may not preserve the standalone firm or its recurring service relationships.
- q: No representative contract or pass-through dataset was located.
- q: Retention differs markedly between specified custom curtain wall and standard residential products.
- d5: Housing starts are only one demand component and do not measure metal product share.
- d5: Interest rates, commercial vacancies, tariffs, glass availability, codes, and incentive policy can materially move demand.
- o: Production can consolidate into larger manufacturers outside the lens.
- o: Self-service configuration may reduce office labor without eliminating accountable manufacturing.

## Sources
- **S1** — [NAICS 332321 Metal Window and Door Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines the industry as manufacturing metal-framed windows, metal doors, frames, screens, molding and trim, and curtain walls, typically using purchased glass.
- **S2** — [Fabricated Metal Product Manufacturing: NAICS 332](https://www.bls.gov/iag/tgs/iag332.htm?hmsr=afimetalparts.com) (accessed 2026-07-22): Reports 2025 broader-subsector employment including 125,250 assemblers, 112,520 welders, 101,640 machinists, and 56,060 cutting and press-machine operators.
- **S3** — [Residential Windows, Doors, and Skylights](https://www.energystar.gov/products/res_windows_doors_skylights) (accessed 2026-07-22): Reports average household energy-bill savings up to 13% from replacing single-pane windows and describes climate-zone performance requirements, independent certification, NFRC labels, installation, and warranties.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey found 22% of employer-business owners planned to sell or transfer ownership within five years, while 5% planned closure and 5% had no plan.
- **S5** — [Monthly New Residential Construction, May 2026](https://www.census.gov/construction/nrc/current/) (accessed 2026-07-22): Reports May 2026 privately owned housing starts at a seasonally adjusted annual rate of 1.177 million, 8.7% below May 2025, and building permits at 1.413 million.
