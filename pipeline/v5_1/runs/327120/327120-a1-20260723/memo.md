# 327120 — Clay Building Material and Refractories Manufacturing

*v5.1 Stage 1 research memo. Run `327120-a1-20260723`, model `claude-sonnet-5`, 2026-07-23, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.93 · L 0.70 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring need for heavy structural products and high-temperature linings preserves accountable physical production.
**Weakness:** Cyclical end markets and a predominantly physical workforce constrain both demand visibility and the realizable AI labor opportunity.

## Business-model lens
- Included: Independent US lower-middle-market manufacturers that repeatedly supply external contractors, distributors, industrial plants, utilities, or building-products customers with brick, structural clay products, ceramic tile, clay pipe, or clay and nonclay refractories.
- Excluded: Captive plants, non-control vehicles, boutique or one-off decorative ceramic studios, commodity-only operations without repeat customer relationships, and concrete or glass brick manufacturers classified elsewhere.
- Customer and revenue model: Repeat orders, distributor and contractor programs, project releases, and qualified industrial supply for heavy physical building products and heat-resistant refractories, generally billed per unit, pallet, weight, area, lot, or project.
- Deviation from default lens: The code combines construction-facing clay building materials with qualification-intensive industrial refractories. It is narrowed to repeat external-customer manufacturers and excludes one-off decorative production, while retaining both official product families to avoid selecting a preferred niche.

## Executive view
Clay building materials and refractories are durable physical products with repeat construction, maintenance, and industrial demand, but they are energy- and production-intensive. AI can improve surrounding information and control workflows, while only a modest share of labor is realistically substitutable within five years.

## How AI changes the work
AI can assist estimates, specifications, kiln and production planning, defect review, maintenance troubleshooting, logistics, purchasing, and order administration. People remain essential for material preparation, forming, firing, handling, packing, quality accountability, and abnormal plant conditions.

## Value capture
Qualified refractories and locally differentiated heavy products can retain savings, while contractor bids, distributor pressure, energy and freight surcharge mechanics, and imports progressively share gains with customers.

## Firm availability
The supplied dataset estimates 129 firms in the EBITDA band. Recurring B2B supply is common, but captive plants, decorative or project-only producers, geographic concentration, permits, and environmental liabilities reduce transferable eligibility; actual control-sale incidence is unmeasured.

## Demand durability
Repair and replacement support both construction products and refractories, yet construction and heavy-industry cycles create meaningful downside. Physical heat resistance and structural function make software substitution unlikely.

## Risks and uncertainty
The code blends construction materials with industrial refractories. Recent broader-subsector output weakness, energy costs, imports, environmental obligations, plant location, customer concentration, and missing direct task or deal evidence are material uncertainties.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.243 | — | OBSERVED | — |
| n | — | 129 | — | ESTIMATE | — |
| a | 0.08 | 0.16 | 0.25 | ESTIMATE | S1, S2 |
| rho | 0.27 | 0.45 | 0.63 | ESTIMATE | S1, S2 |
| e | 0.36 | 0.54 | 0.7 | ESTIMATE | S1 |
| s5 | 0.07 | 0.16 | 0.28 | ESTIMATE | — |
| q | 0.34 | 0.54 | 0.72 | ESTIMATE | S1 |
| d5 | 0.7 | 0.92 | 1.14 | ESTIMATE | S1, S2 |
| o | 0.92 | 0.98 | 1 | ESTIMATE | S1 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.70 | 1.53 | ESTIMATE |
| F | 2.33 | 4.02 | 5.26 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 6.44 | 9.02 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation data are for all NAICS 327, not 327120.
- a: Exposure likely differs between automated high-volume brick or tile lines and lower-volume engineered refractories.
- rho: No 327120-specific AI implementation cohort was found.
- rho: Ordinary plant automation and capital replacement are excluded unless AI is the enabling constraint.
- e: The supplied size-band count is an ESTIMATE based on size classes and an assumed margin.
- e: NAICS is establishment-based and does not identify firm revenue recurrence or transferability.
- s5: No directly observed control-transfer rate for eligible firms was found.
- s5: Small private transactions and unsuccessful sale processes are underreported.
- q: The Census definition establishes product scope but not billing or pass-through terms.
- q: Capture differs materially between commodity building products and qualification-sensitive refractory systems.
- d5: BLS output evidence is for broader NAICS 327 and is historical, not a five-year forecast.
- d5: Construction products and refractories follow different end-market cycles, widening the range.
- o: Direct imports can remove a domestic lens operator even though production remains necessary elsewhere.
- o: Durable operator need does not imply unchanged employment, energy intensity, or plant footprint.

## Sources
- **S1** — [2022 NAICS Definition: 327120 Clay Building Material and Refractories Manufacturing](https://www.census.gov/naics/?input=327120&year=2022&details=327120) (accessed 2026-07-23): Defines shaped, molded, baked, burned, or hardened clay and nonclay refractories, ceramic and structural tile, brick, clay pipe, and other structural clay products; explains that refractories retain shape and chemical identity under high heat and are used in furnace linings.
- **S2** — [Industries at a Glance: Nonmetallic Mineral Product Manufacturing: NAICS 327](https://www.bls.gov/iag/tgs/iag327.htm) (accessed 2026-07-23): Lists major 2025 occupations including molders and shapers, forming-machine operators, material movers, production supervisors, and truck drivers; reports real-output changes of 2.3%, -4.5%, -9.1%, and -0.7% for 2022-2025.
