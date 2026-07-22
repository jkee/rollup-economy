# 326220 — Rubber and Plastics Hoses and Belting Manufacturing

*v5.1 Stage 1 research memo. Run `326220-a1-20260723`, model `claude-sonnet-5`, 2026-07-23, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.92 · L 0.80 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat demand for specification-sensitive physical components preserves the need for an accountable operator while AI improves surrounding information workflows.
**Weakness:** Production labor dominates the subsector, so the realistically AI-exposed wage pool is limited and has not been measured at the six-digit level.

## Business-model lens
- Included: Independent US manufacturers of rubber or reinforced-plastics hose and belting that repeatedly supply external industrial, automotive, distribution, or equipment-manufacturer customers and are in the lower-middle-market EBITDA band.
- Excluded: Captive plants, commodity-only producers without recurring customer relationships, garden-hose resellers, rubber or plastics tubing, molded mechanical rubber goods, and fluid-power hose assembly businesses classified elsewhere.
- Customer and revenue model: Repeat purchase orders, negotiated supply agreements, OEM programs, and distributor relationships for engineered or specification-sensitive physical products; pricing is generally per unit or lot rather than hourly service billing.
- Deviation from default lens: none

## Executive view
This is a physical manufacturing industry with recurring replacement and OEM demand, but only a modest share of wage work is plausibly exposed to AI in five years. The relevant opportunity is operational augmentation around planning, commercial work, quality, and plant knowledge rather than removal of the production core.

## How AI changes the work
AI can accelerate quote preparation, order entry, scheduling, specification retrieval, quality-document review, visual-inspection triage, maintenance troubleshooting, and purchasing analysis. Human operators remain necessary for machine setup, material handling, process intervention, testing accountability, and exception management.

## Value capture
Unit and program pricing creates room to retain savings, particularly between contract renewals and in engineered niches. Standardized products, OEM cost-down demands, rebids, and distributor purchasing power can transfer a substantial share of benefits to customers over time.

## Firm availability
The supplied dataset estimates 74 firms in the EBITDA band, but only a subset should satisfy independence, repeat external revenue, and transferability. Actual control-sale incidence is not directly observed and requires private-deal and ownership diligence.

## Demand durability
Hose and belting remain necessary physical components with replacement-driven demand, though real volume is exposed to industrial and automotive cycles, imports, redesign, and material substitution. Software is unlikely to eliminate the accountable manufacturer role.

## Risks and uncertainty
The largest evidence gaps are six-digit occupation weights, actual AI implementation outcomes, contract pass-through, and denominator-matched private control transfers. A highly automated plant or commodity-heavy customer mix could make the labor and retention opportunity materially weaker than the base case.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2365 | — | OBSERVED | — |
| n | — | 74 | — | ESTIMATE | — |
| a | 0.1 | 0.17 | 0.26 | ESTIMATE | S2 |
| rho | 0.32 | 0.5 | 0.68 | ESTIMATE | S1, S2 |
| e | 0.38 | 0.56 | 0.72 | ESTIMATE | S1 |
| s5 | 0.08 | 0.17 | 0.29 | ESTIMATE | — |
| q | 0.42 | 0.61 | 0.78 | ESTIMATE | S1 |
| d5 | 0.82 | 0.98 | 1.16 | ESTIMATE | S1, S2 |
| o | 0.91 | 0.97 | 1 | ESTIMATE | S1 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.30 | 0.80 | 1.67 | ESTIMATE |
| F | 1.90 | 3.35 | 4.50 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.46 | 9.51 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation figures are for the broader NAICS 326 plastics and rubber products subsector, not 326220.
- a: The estimate excludes already automated machine-control work and does not assume robotics substitution merely because AI can assist decisions.
- rho: No industry-specific adoption cohort was found.
- rho: Physical automation capital and ordinary process improvement are excluded unless AI is the enabling constraint.
- e: The supplied firm count is itself an ESTIMATE derived from size-class and margin assumptions.
- e: The official NAICS definition is establishment-based and does not reveal firm-level repeat revenue or transferability.
- s5: No directly observed denominator-matched control-transfer series was available.
- s5: Small private manufacturing deals are underreported in public databases.
- q: The NAICS definition establishes products but not contract structures.
- q: Customer concentration and qualification barriers vary substantially by product and end market.
- d5: BLS output data are for NAICS 326, not this six-digit industry, and recent annual changes are not a five-year forecast.
- d5: The range concerns real quantity of the current basket, not producer revenue or nominal prices.
- o: Some high-volume OEM customers may vertically integrate or redesign components.
- o: Operator requirement does not imply that current headcount or workflows remain unchanged.

## Sources
- **S1** — [2022 NAICS Definition: 326220 Rubber and Plastics Hoses and Belting Manufacturing](https://www.census.gov/naics/?input=326220&year=2022&details=326220) (accessed 2026-07-23): Defines the included manufacture of rubber and reinforced-plastics hose and belting and identifies excluded adjacent activities including tubing, molded mechanical rubber goods, and fluid-power hose assemblies.
- **S2** — [Industries at a Glance: Plastics and Rubber Products Manufacturing: NAICS 326](https://www.bls.gov/iag/tgs/iag326.htm) (accessed 2026-07-23): Shows 2025 subsector employment concentrated in machine operators, assemblers, inspectors, packers, and production supervisors, and reports annual real-output changes of -3.6%, -6.3%, -1.8%, and -3.4% for 2022-2025.
