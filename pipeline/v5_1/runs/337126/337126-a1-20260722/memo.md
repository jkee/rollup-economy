# 337126 — Household Furniture (except Wood and Upholstered) Manufacturing

*v5.1 Stage 1 research memo. Run `337126-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → CONDITIONAL · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** High labor content plus design, planning, sourcing, content, quality, and service workflows that can benefit from AI.
**Weakness:** Missing target-count data and intense import and retailer price pressure materially weaken acquisition visibility and benefit retention.

## Business-model lens
- Included: US lower-middle-market manufacturers of nonupholstered household furniture made primarily from metal, plastics, reed, rattan, wicker, fiberglass, or other nonwood materials, supplying external retailers, wholesalers, designers, hospitality accounts, private-label customers, and direct consumers on repeat programs.
- Excluded: Wood household furniture, upholstered furniture, retail or import businesses without domestic manufacturing, captive internal plants, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat product sales through wholesale, retail, private-label, contract, e-commerce, and direct channels, generally priced by SKU or collection with promotions, freight, returns, markdowns, warranties, and periodic line reviews.
- Deviation from default lens: none

## Executive view
Nonwood household furniture manufacturing has a useful but bounded AI surface in design support, forecasting, sourcing, planning, quality, content, customer service, and administration. Physical conversion, assembly, finishing, packing, inventory, and delivery remain central, while import and retailer competition constrain capture.

## How AI changes the work
AI can assist collection development, product visualization, catalog and marketplace content, demand forecasts, purchasing, schedules, visual inspection, customer support, returns analysis, and administrative work. Cutting, forming, molding, weaving, welding, finishing, assembly, handling, and packing are less substitutable.

## Value capture
Brand, design, retailer placement, private-label relationships, responsiveness, and direct channels offer protection. Price transparency, imports, promotions, markdown allowances, line reviews, and channel bargaining transfer a large share of visible savings.

## Firm availability
The missing frozen LMM firm count is a material limitation and was not replaced. A subset of domestic manufacturers likely fits, but importer-heavy brands, captive plants, concentration, weak earnings quality, inventory exposure, and owner dependence must be excluded.

## Demand durability
Furniture remains a physical household need, but it is discretionary, durable, housing-sensitive, fashion-driven, and import-exposed. Replacement and household formation support demand while fulfilled demand continues to require accountable production and delivery.

## Risks and uncertainty
Housing and consumer cycles, imports, freight, tariffs, retailer concentration, inventory markdowns, returns, product safety, fashion misses, and material costs are material. Evidence is weakest on the firm denominator, six-digit task mix, completed transfers, contract capture, and domestic volume forecasts.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2882 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.24 | 0.34 | PROXY | S1 |
| rho | 0.43 | 0.59 | 0.72 | ESTIMATE | S1 |
| e | 0.28 | 0.43 | 0.59 | ESTIMATE | S2 |
| s5 | 0.12 | 0.21 | 0.31 | PROXY | S5 |
| q | 0.26 | 0.42 | 0.59 | ESTIMATE | — |
| d5 | 0.87 | 0.97 | 1.09 | ESTIMATE | S3, S4 |
| o | 0.94 | 0.985 | 0.998 | ESTIMATE | S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.79 | 1.63 | 2.82 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 5.20 | 8.40 | 10.00 | ESTIMATE |
| D | 8.18 | 9.55 | 10.00 | ESTIMATE |

## Caveats
- a: The workforce evidence is subsector-wide rather than six-digit.
- a: The material mix ranges from labor-intensive wicker to automated metal or plastics production.
- rho: No direct adoption survey was found.
- rho: Implementation depends on ERP and product-data quality, channel integration, SKU complexity, and production scale.
- e: The frozen LMM firm count is missing and was not estimated or replaced.
- e: NAICS activity does not reveal domestic value-add, recurring programs, or transferability.
- s5: Cross-industry intentions are not observed transactions.
- s5: The missing n prevents conversion into a defensible expected target count.
- q: No public contract sample quantifies pass-through.
- q: Branded direct-to-consumer products retain more than commodity private-label or mass-retail lines.
- d5: Retail-store sales are not product-specific domestic manufacturing demand.
- d5: New-home sales are only one furniture-demand driver and the most recent figures are cyclical.
- o: Operator requirement is inferred from physical manufacturing.
- o: Import substitution and used-furniture displacement affect d5 rather than being double-counted here.

## Sources
- **S1** — [Furniture and Related Product Manufacturing: NAICS 337](https://www.bls.gov/IAG/TGS/iag337.htm) (accessed 2026-07-22): Describes furniture production as cutting, bending, molding, laminating, and assembly across wood, metal, glass, plastics, and rattan and states that design and fashion are important, while reporting 233,800 production and nonsupervisory employees in June 2026.
- **S2** — [2022 NAICS Definition: 337126 Household Furniture (except Wood and Upholstered) Manufacturing](https://www.census.gov/naics/?details=337&input=337&year=2022) (accessed 2026-07-22): Defines the industry as nonupholstered household furniture made from materials other than wood, including metal, plastics, reed, rattan, wicker, and fiberglass, on stock or custom and assembled or knockdown bases.
- **S3** — [U.S. Census Bureau Economic Indicators](https://www.census.gov/economic-indicators/furniture-and-home-furnishings-stores-reports.html) (accessed 2026-07-22): Explains that retail sales are establishment-based and not intended to measure commodity demand, and reports May 2026 new single-family home sales of 580,000 annualized units after monthly declines, used only as a cyclical housing-demand indicator.
- **S4** — [BLS Occupational Projections and Worker Characteristics](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Projects modest decline in relevant furniture-production occupations such as cabinetmakers and bench carpenters through 2034, used only as broad directional evidence about mature manufacturing demand and productivity.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of employer-business owners surveyed in fall 2024 planned to sell or transfer ownership within five years, used as a cross-industry transfer proxy.
