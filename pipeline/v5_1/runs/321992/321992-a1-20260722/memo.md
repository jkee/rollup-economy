# 321992 — Prefabricated Wood Building Manufacturing

*v5.1 Stage 1 research memo. Run `321992-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.85 · L 0.50 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digitally intensive design-to-production coordination offers implementable AI gains while the underlying physical building demand still requires an accountable operator.
**Weakness:** A small, historically flat offsite share and project-based product revenue weaken both demand visibility and fit with the recurring outsourced-service lens.

## Business-model lens
- Included: Independent US manufacturers of prefabricated stationary wood buildings, volumetric modules, panelized systems, and precut building packages that serve repeat builders, developers, public agencies, or commercial customers and have transferable standalone operations.
- Excluded: Manufactured mobile homes, conventional onsite general contractors without manufacturing, captive fabrication units, project shells, one-off hobby structures, and non-control financing vehicles.
- Customer and revenue model: Revenue is principally project, module, panel, component, or complete-building sales under bids and supply contracts; repeat business can come from builders and developers, but it is not usually subscription or recurring-service revenue.
- Deviation from default lens: This is product and project manufacturing, not a recurring outsourced-service industry. The lens therefore retains only firms with repeat external B2B production relationships, a coherence-based narrowing.

## Executive view
Prefabricated wood buildings combine a physical factory core with more digital design and project coordination than basic wood products. That creates a bounded AI opportunity, but the industry fits the recurring-service lens only where manufacturers repeatedly supply builders, developers, or agencies rather than sell isolated buildings.

## How AI changes the work
The strongest uses are takeoff and estimating, BIM and design documentation, specification and code review, procurement, scheduling, production planning, change-order analysis, customer communication, and warranty triage. Assembly, machine operation, logistics, inspection, and site coordination remain substantially physical and accountable.

## Value capture
Fixed-price backlog can temporarily shelter productivity gains, while faster and more reliable delivery can support differentiation. Competitive bidding and repeat-customer negotiation should progressively share savings, especially in standardized components and panels.

## Firm availability
Succession pressure is plausible from the age profile of US employer owners, but public evidence does not identify owner age or completed transfers in prefab manufacturing. Firm eligibility is narrowed by one-off project revenue, captive factories, customer concentration, bonding, and the need for durable management and code approvals.

## Demand durability
Offsite construction addresses housing productivity and affordability problems, yet residential share was only 3% in 2024 and has not expanded recently. The base assumes modest growth rather than a step-change, with substantial downside from rates and approvals and upside from demand aggregation and regulatory modernization.

## Risks and uncertainty
Major risks are weak recurring-service fit, project cyclicality, factory underutilization, customized engineering, fragmented codes, transport limits, customer concentration, contract pass-through, and already-embedded CAD/CAM automation. Six-digit occupational and transfer data are missing.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1456 | — | OBSERVED | — |
| n | — | 160 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S1, S2 |
| rho | 0.28 | 0.48 | 0.68 | ESTIMATE | S3 |
| e | 0.1 | 0.23 | 0.4 | ESTIMATE | S3, S4 |
| s5 | 0.12 | 0.21 | 0.32 | PROXY | S5 |
| q | 0.25 | 0.47 | 0.68 | ESTIMATE | S3 |
| d5 | 0.88 | 1.08 | 1.32 | PROXY | S3, S4, S6 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.16 | 0.50 | 1.11 | ESTIMATE |
| F | 1.72 | 3.49 | 4.93 | ESTIMATE |
| C | 5.00 | 9.40 | 10.00 | ESTIMATE |
| D | 7.92 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No public six-digit occupation mix was located.
- a: Current automation penetration in CAD/CAM, CNC nesting, and estimating is not measured, so already-automated work may be overstated.
- rho: No longitudinal AI implementation study for US prefab wood manufacturers was located.
- rho: Results will differ between standardized panels and bespoke volumetric projects.
- e: The injected n is margin-bridged from size-class averages and may not correspond to standalone transferable firms.
- e: The NAICS spans components, complete panelized units, precut packages, and volumetric buildings with different recurrence patterns.
- s5: Cross-industry intentions are an imperfect proxy for completed qualifying transfers.
- s5: Strategic asset purchases, internal family transfers, and distressed plant sales may not preserve a standalone eligible firm.
- q: Public sources do not measure productivity pass-through.
- q: The mix of fixed-price, cost-plus, component-supply, and design-build contracts varies widely.
- d5: Residential completion shares do not cover all commercial and component demand.
- d5: Demand is cyclical and exposed to interest rates, construction finance, building codes, local approvals, transport radius, and conventional-building competition.
- o: Operator requirement is distinct from labor intensity.
- o: Some design and configuration services may be self-served even though physical production remains external.

## Sources
- **S1** — [Wood Product Manufacturing: NAICS 321](https://www.bls.gov/IAG/TGS/iag321.htm) (accessed 2026-07-22): 2025 occupation counts show large physical-production roles, including 75,000 team assemblers, 38,360 woodworking-machine operators, and 30,140 sawing-machine operators; also reports recent productivity and output.
- **S2** — [Other Wood Product Manufacturing - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_321900.htm) (accessed 2026-07-22): Broader-industry occupation mix, including 51.76% production employment and 20.49% assemblers and fabricators.
- **S3** — [Offsite Construction for Housing: Research Roadmap](https://www.huduser.gov/portal/publications/Offsite-Construction-for-Housing-Research-Roadmap.html) (accessed 2026-07-22): Offsite construction's potential efficiencies, quality, and cost benefits and the six research/barrier domains: regulation, standards, finance, project delivery/contracts, workforce, and business models.
- **S4** — [The Offsite Construction Market Share Flattens Nationally in 2024](https://www.nahb.org/blog/2025/08/the-offsite-construction-market-share-flattens-nationally-in-2024) (accessed 2026-07-22): 28,000 modular or panelized/precut single-family completions out of 1.019 million in 2024, a 3% share unchanged from 2023 and below 7% in 1998.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry employer-owner age and five-year transfer intentions: 52.3% age 55 or older and 22% planning a sale or transfer.
- **S6** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects broader NAICS 321900 real output from 56.8 to 67.3 billion chained 2017 dollars over 2024-34, a 1.7% annual rate.
