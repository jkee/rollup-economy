# 541420 — Industrial Design Services

*v5 Stage 1 research memo. Run `run541420-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.12 · L 3.21 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Computer-mediated drafting, rendering, research, documentation, and revision create an implementable but bounded labor opportunity.
**Weakness:** A meaningful portion of industrial-design revenue may be bespoke, project-based, and founder-dependent rather than repeat outsourced service that transfers cleanly.

## Business-model lens
- Included: US lower-middle-market studios that provide external industrial product-design services on recurring or repeat client engagements, including research, concept development, CAD and rendering, engineering coordination, and prototype support.
- Excluded: Captive manufacturer design departments, single-project studios without repeat outsourced service revenue, software-only products, contract manufacturing, financing vehicles, and firms outside the normalized EBITDA band are excluded.
- Customer and revenue model: External business customers buy bespoke product-design work, commonly scoped as projects, phases, retained design support, or time-and-materials engagements; only repeat or recurring outsourced relationships are in scope.
- Deviation from default lens: none

## Executive view
Industrial Design Services is a specialized, labor-led outsourced service, but the frozen lens captures only studios with repeat client relationships. AI can improve computer-mediated production work, while product judgment and accountable delivery remain central. The evidence supports a cautious view because a large share of the classification may be discrete project work rather than recurring service.

## How AI changes the work
O*NET identifies core work in drafting, computer use, information processing, design refinement, research, cost estimation, and documentation. Those workflows can be accelerated by AI tools. BLS and O*NET also describe client consultation, evaluation of safety and feasibility, engineering collaboration, physical models, and presentation for approval, which keep humans accountable and limit full labor substitution.

## Value capture
The service is commonly bespoke and can be sold by scope, phase, retainer, or hours. Fixed-fee phases create room to retain workflow productivity, but repeat-client renewals, competitive bids, and hourly billing can share gains with customers. Contract-level pricing evidence is needed before relying on any retention assumption.

## Firm availability
Qualifying control transfers are uncertain. Design studios can be sold, but their value may depend on principal reputation, client relationships, and key creative staff. Broad establishment dynamics are not a measure of transfers, so transaction databases and adviser interviews are the next evidence priority.

## Demand durability
BLS projects Commercial and Industrial Designer employment to increase 3 percent from 2024 to 2034, with demand supported by innovative products and offset by manufacturing declines. This is an occupational proxy, not an industry demand forecast, and indicates roughly stable current-service demand rather than a clear expansion case.

## Risks and uncertainty
The classification and occupational sources do not disclose the LMM studio staffing mix, repeat-revenue share, billing method, control-transfer rate, or realized AI labor displacement. Client confidentiality, intellectual-property restrictions, safety requirements, and physical prototyping can slow adoption. Manufacturers may also internalize work or customers may adopt design tools directly.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.9177 | — | OBSERVED | — |
| n | — | 131 | — | ESTIMATE | — |
| a | 0.15 | 0.25 | 0.4 | PROXY | S2, S3 |
| rho | 0.2 | 0.35 | 0.5 | ESTIMATE | S2, S3 |
| e | 0.18 | 0.3 | 0.45 | ESTIMATE | S1 |
| s5 | 0.1 | 0.17 | 0.25 | ESTIMATE | S4 |
| q | 0.4 | 0.55 | 0.7 | ESTIMATE | — |
| d5 | 0.93 | 1 | 1.05 | PROXY | S3 |
| o | 0.65 | 0.8 | 0.9 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.10 | 3.21 | 7.34 | ESTIMATE |
| F | 1.95 | 3.28 | 4.43 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.04 | 8.00 | 9.45 | ESTIMATE |

## Caveats
- a: No public NAICS 541420 wage-weighted occupational staffing pattern was used. The occupational proxy does not capture the share of studio work performed by principals or contractors.
- rho: This is an implementation judgment, not a forecast of software capability or pricing. Adoption will vary materially by regulated product category and client security policy.
- e: No public census tabulation separates recurring client relationships from single-project work or identifies the normalized EBITDA band. The injected LMM firm-count input may include ineligible project studios.
- s5: BLS business-dynamics data describe establishment changes and do not measure qualifying control transfers for this NAICS or LMM EBITDA cohort. This estimate excludes closures as required but cannot observe them separately.
- q: Public sources found here do not quantify NAICS 541420 billing mix or contractual savings pass-through. The value differs by whether the studio charges fixed fees, milestones, retainers, or hours.
- d5: Occupation employment is an imperfect proxy for service quantity and includes manufacturers, wholesalers, self-employed workers, and other employers. Receipts can change with price and scope even if quantity does not.
- o: The estimate assumes the current service basket and excludes software-only outputs. Regulated and complex physical products are likely more operator-dependent than consumer concept work.

## Sources
- **S1** — [2022 NAICS definition: Industrial Design Services](https://www.census.gov/naics/?input=541420&year=2022&details=541420) (accessed 2026-07-22): Defines NAICS 541420 as industrial design services concerned with the use, value, and appearance of products, supporting the industry boundary and eligibility discussion.
- **S2** — [O*NET Commercial and Industrial Designers task and activity profile](https://www.onetonline.org/link/details/27-1021.00) (accessed 2026-07-22): Reports task and work-activity content including drafting, computer work, design refinement, feasibility evaluation, client communication, documentation, cost estimation, models, and collaboration.
- **S3** — [BLS Occupational Outlook Handbook: Industrial Designers](https://www.bls.gov/ooh/arts-and-design/industrial-designers.htm) (accessed 2026-07-22): Reports 30,600 jobs in 2024, a 3 percent projected employment increase from 2024 to 2034, 7 percent of employment in specialized design services, and duties involving product concepts, CADD, prototypes, costs, and client approval.
- **S4** — [BLS Business Employment Dynamics](https://www.bls.gov/bdm/home.htm) (accessed 2026-07-22): Describes the QCEW-derived business dynamics program and its establishment creation and destruction measures, explaining why it is not a direct qualifying-control-transfer measure.
