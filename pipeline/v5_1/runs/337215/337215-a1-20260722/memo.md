# 337215 — Showcase, Partition, Shelving, and Locker Manufacturing

*v5.1 Stage 1 research memo. Run `337215-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.59 · L 1.33 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Diversified recurring storage, security, and fixture needs create durable physical demand.
**Weakness:** Project bidding and divergent construction end markets weaken pricing and forecast confidence.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly supplying stock or custom wood and nonwood showcases, store and office fixtures, partitions, shelving, lockers, frames, laminated fixture tops, and furniture parts to external retail, warehouse, office, education, healthcare, industrial, and government customers.
- Excluded: Captive internal shops, shells, refrigerated display cases, safes and vaults, kitchen and bathroom countertops, on-site shelving construction, and installation-only contractors classified outside NAICS 337215.
- Customer and revenue model: Project bids, dealer and distributor orders, roll-out programs, catalog replenishment, architect or contractor specifications, and repeat replacement or expansion purchases, generally priced per unit, bay, fixture package, lot, or project.
- Deviation from default lens: none

## Executive view
This is a diversified physical-fixture industry with practical AI opportunities in takeoffs, specifications, estimating, planning, order checking, and inspection. Manufacturing remains material- and project-intensive. Warehouse, education, and institutional demand can offset weaker offices or stores, but end-market divergence makes a single forecast uncertain.

## How AI changes the work
AI can parse drawings and specifications, produce takeoffs, assist quotes and layouts, check configurations, schedule production, forecast materials, and identify defects. Cutting, forming, welding, laminating, finishing, assembly, packing, and field coordination remain physical. Custom work and late design changes constrain reuse.

## Value capture
Fit, coordination, standards, rollout consistency, lead time, and freight can defend value. General contractors, retail procurement, distributors, public bids, value engineering, imports, and alternative fabricators return a large portion of savings to customers.

## Firm availability
The estimated population is sizeable and fragmented, but the EBITDA band uses a machinery margin that may overstate eligible furniture businesses. Buyers must separate true manufacturing from installation-heavy operations and assess backlog, project concentration, and owner-held estimating or sales relationships.

## Demand durability
Physical storage, security, division of space, and product display persist across many settings. Current construction spending is soft overall but public education remains active; warehouses and industrial facilities may behave differently from offices and retail. Reuse and imports constrain replacement.

## Risks and uncertainty
Risks include construction cycles, project concentration, contractor disputes, change orders, tariffs and materials, freight, field-measurement errors, load-rating liability, retail closures, office consolidation, and confusing faster estimates with removable labor. Direct contract and transaction evidence is limited.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2764 | — | OBSERVED | — |
| n | — | 164 | — | ESTIMATE | — |
| a | 0.17 | 0.25 | 0.35 | PROXY | S2, S3 |
| rho | 0.3 | 0.48 | 0.64 | PROXY | S3 |
| e | 0.66 | 0.82 | 0.93 | ESTIMATE | S1 |
| s5 | 0.15 | 0.27 | 0.41 | PROXY | S5 |
| q | 0.27 | 0.46 | 0.64 | ESTIMATE | — |
| d5 | 0.93 | 1.04 | 1.17 | PROXY | S1, S4 |
| o | 0.93 | 0.98 | 0.997 | ESTIMATE | S1 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.56 | 1.33 | 2.48 | PROXY |
| F | 4.58 | 5.82 | 6.68 | ESTIMATE |
| C | 5.40 | 9.20 | 10.00 | ESTIMATE |
| D | 8.65 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS evidence is broader than six-digit 337215.
- a: Already-automated CAD/CAM and CNC tasks are excluded from the remaining opportunity.
- rho: General AI-tool adoption does not measure implemented substitution.
- rho: Project throughput gains can increase capacity without reducing labor.
- e: The provided count uses a machinery margin that may not match custom fixture manufacturing economics.
- e: Census classifies establishments while eligibility applies to firms.
- s5: No six-digit qualifying-transfer denominator was found.
- s5: Succession-plan resilience is not a transaction probability.
- q: Capture should be higher for repeat branded rollouts and proprietary systems than for commodity shelving or public locker bids.
- q: No representative contract dataset was found.
- d5: Construction spending is nominal, broad, and a short-term indicator.
- d5: The industry's end markets can diverge sharply: warehouse shelving may grow while office partitions or store fixtures decline.
- o: An operator may remain necessary while production shifts offshore or consolidates.
- o: Automated warehouses may reduce conventional static shelving but add specialized rack and guard systems.

## Sources
- **S1** — [Census profile: 337215 Showcase, Partition, Shelving, and Locker Manufacturing](https://data.census.gov/profile/337215_-_Showcase%2C_Partition%2C_Shelving%2C_and_Locker_Manufacturing?codeset=naics~337215&g=010XX00US) (accessed 2026-07-22): Defines wood and nonwood fixtures, shelving, lockers, frames, partitions, laminated tops, and furniture parts made on stock or custom and assembled or knockdown bases.
- **S2** — [BLS May 2023 occupation estimates for Furniture and Related Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_3370A1.htm) (accessed 2026-07-22): Provides occupation-level employment and wages for the broader furniture industries, including production, woodworking, finishing, upholstery, and machine-operation work.
- **S3** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Reports 46% manufacturing AI-tool use and more than 80% expecting increased use in two years, with operational use cases and adoption barriers.
- **S4** — [Census Monthly Construction Spending, May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-22): Reports total construction 1.5% below May 2025, first-five-month spending 2.7% below 2025, and May public educational construction at a $113.4 billion annual rate, 0.6% above April.
- **S5** — [Deloitte Private survey: generational disparities in family-business succession planning](https://www2.deloitte.com/us/en/pages/about-deloitte/articles/press-releases/deloitte-private-survey-generational-disparatires-emerge-insuccession-planning-and-priorities-shaping-family-businesses.html) (accessed 2026-07-22): Describes a January 2024 survey of 500 US family-enterprise respondents and reports that 24% of current-generation respondents strongly agreed their succession plan would withstand departure of an important family employee.
