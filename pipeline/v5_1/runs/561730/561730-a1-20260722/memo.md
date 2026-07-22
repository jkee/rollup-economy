# 561730 — Landscaping Services

*v5.1 Stage 1 research memo. Run `561730-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.21 · L 2.45 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring route-based work creates repeated opportunities to compound gains from dispatch, estimating, scheduling, documentation, and selective equipment autonomy.
**Weakness:** Most production is physical, variable, outdoors, and exception-heavy, which caps substitution and makes implementation depend on property mix and operational discipline.

## Business-model lens
- Included: LMM firms providing recurring or repeat outsourced landscape maintenance, mowing, edging, pruning, planting, fertilization, irrigation care, seasonal cleanup, tree care, snow service, and customer-requested enhancement or installation work to external customers.
- Excluded: Captive grounds crews, shell entities, non-control financing vehicles, pure landscape architecture without installation, retail garden centers, construction-only contractors, and operators whose work is solely one-off rather than recurring or repeat outsourced service.
- Customer and revenue model: Commercial, institutional, government, multifamily, homeowners-association, and residential customers buy recurring maintenance through fixed-fee or per-occurrence arrangements and commission repeat enhancement or installation projects. Route density, renewal retention, labor scheduling, and equipment utilization drive economics.
- Deviation from default lens: none

## Executive view
Landscaping combines a large physical field workforce with recurring route-based maintenance and fragmented ownership. AI can improve the coordination layer and autonomous equipment can address selected repetitive work, but horticultural variety, property exceptions, weather, safety, and customer accountability limit full labor substitution. The opportunity is therefore operationally meaningful only when workflow discipline and site selection are strong.

## How AI changes the work
The near-term changes are quoting from imagery, scheduling, route design, dispatch, customer communication, invoicing, documentation, procurement, and supervisor decision support. Computer vision and autonomous mowing can extend into standardized properties. Crews remain necessary for edging, trimming, planting, treatments, irrigation diagnosis, tree work, debris, complex terrain, and exception handling.

## Value capture
Fixed-fee recurring maintenance can preserve productivity gains during the contract period, while better routing and avoided hiring can improve service reliability without an explicit customer price concession. Renewal bids, easy cancellation, fragmented competition, per-occurrence billing, and customer procurement eventually share part of the gain, so durable capture depends on retention, density, service quality, and differentiated execution.

## Firm availability
The industry is highly fragmented and has active tuck-in logic around route density, customer relationships, and multi-service coverage. Broad owner-succession evidence and exterior-services deal activity support a recurring supply of sellers, but the qualifying share is reduced by owner dependence, weak systems, project-heavy mixes, internal transfers, and firms too small or informal to support a control transaction.

## Demand durability
Commercial and institutional grounds require recurring upkeep, and outsourcing provides a stable base. Positive employment and broader real-output projections support modest growth rather than contraction. Demand remains exposed to weather, drought and water rules, construction and property cycles, budget pressure, and customers substituting simpler grounds or self-service equipment.

## Risks and uncertainty
The largest uncertainties are the wage-weighted task split within field occupations, actual autonomous-equipment performance on mixed properties, adoption by LMM firms, maintenance-versus-project revenue mix, and firm-level transaction incidence. A roll-up can fail if route density is poor, acquisitions lack transferable customer relationships, equipment creates new supervision burdens, or renewal competition gives savings back to customers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4087 | — | OBSERVED | — |
| n | — | 593 | — | ESTIMATE | — |
| a | 0.18 | 0.3 | 0.43 | PROXY | S2, S3, S4, S5 |
| rho | 0.3 | 0.5 | 0.68 | PROXY | S4, S5, S3 |
| e | 0.55 | 0.72 | 0.85 | ESTIMATE | S1, S6 |
| s5 | 0.1 | 0.17 | 0.25 | PROXY | S6, S7, S8 |
| q | 0.48 | 0.64 | 0.78 | PROXY | S6, S4 |
| d5 | 0.98 | 1.1 | 1.2 | PROXY | S3, S6, S9 |
| o | 0.72 | 0.86 | 0.94 | ESTIMATE | S2, S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.88 | 2.45 | 4.78 | PROXY |
| F | 5.65 | 6.91 | 7.79 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | PROXY |
| D | 7.06 | 9.46 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation shares are employment-weighted rather than wage-weighted task shares.
- a: The technology survey emphasizes commercial contractors and may overrepresent software-engaged firms.
- a: Autonomous-mower interest is not equivalent to deployable substitution across irregular or safety-sensitive properties.
- rho: Stated technology expectations are not realized implementation outcomes.
- rho: Commercial landscaping respondents may not represent residential route operators or installation-heavy firms.
- rho: Implementation depends on data quality, standard operating procedures, fleet replacement cycles, and local labor economics.
- e: No source measures eligibility within the supplied LMM count.
- e: The injected firm-count estimate may include many small operators whose normalized EBITDA or transferability is uncertain.
- e: Business-model mix varies sharply between maintenance, tree care, treatment, irrigation, snow, and design-build operators.
- s5: The owner survey is cross-industry and measures plans rather than completed transactions.
- s5: The M&A report combines landscaping with several other exterior building services.
- s5: Private tuck-ins and failed transactions are incompletely observed.
- q: BrightView is much larger than the screened firms.
- q: Residential, per-visit, and project billing may pass savings through faster than commercial fixed-fee maintenance.
- q: The estimate excludes implementation difficulty and volume effects, which belong in other primitives.
- d5: Exact-industry employment is not quantity demand and embeds productivity assumptions.
- d5: The real-output projection is for a broader industry group.
- d5: BrightView's cited commercial-market outlook relies on third-party research and is not representative of all customer segments.
- o: This is bounded judgment rather than an observed displacement rate.
- o: Large simple turf areas are more substitutable than complex residential, institutional, or ornamental properties.
- o: The estimate may be high if customers accept narrower service baskets or equipment vendors assume outcome accountability.

## Sources
- **S1** — [NAICS Sector 56: Administrative and Support and Waste Management and Remediation Services](https://www.census.gov/naics/resources/archives/sect56.html) (accessed 2026-07-22): Official Census scope for Landscaping Services, including landscape care, maintenance, installation, and listed exclusions for construction-only, architecture-only, and retail activities.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 561730](https://www.bls.gov/oes/2023/may/naics5_561730.htm) (accessed 2026-07-22): Exact-industry occupational mix and wages; grounds-maintenance occupations dominate employment, with smaller management, sales, and office-support shares.
- **S3** — [Grounds Maintenance Workers](https://www.bls.gov/ooh/building-and-grounds-cleaning/grounds-maintenance-workers.htm) (accessed 2026-07-22): Physical task content, outdoor conditions, hazards, employment concentration, occupational openings, and positive demand outlook for grounds-maintenance work.
- **S4** — [Where Technology Meets Opportunities: Inside Aspire's 2025 Industry Report](https://blog.landscapeprofessionals.org/where-technology-meets-opportunities-inside-aspires-2025-industry-report/) (accessed 2026-07-22): Survey of more than one thousand commercial landscaping professionals on staffing difficulty, repeat customers, software use, AI adoption, property intelligence, autonomous mowers, routing, scheduling, and field operations.
- **S5** — [AI Trailblazers: How Landscape Pros Are Increasing Their Efficiency](https://blog.landscapeprofessionals.org/ai-trailblazers-how-landscape-pros-are-increasing-their-efficiency/) (accessed 2026-07-22): Industry examples of AI in administration, design, marketing, estimating from satellite imagery, and staged deployment, together with reported low current AI adoption.
- **S6** — [BrightView Holdings, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1734713/000119312525288109/bv-20250930.htm) (accessed 2026-07-22): Recurring annual landscape-maintenance contracts, fixed-fee and per-occurrence structures, short customer cancellation rights, essential-service characterization, market fragmentation, and maintenance-versus-development business models.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry U.S. employer-business owner plans to sell or transfer ownership within five years and broader succession-plan limitations.
- **S8** — [Facility Services M&A Update: Q4 2025](https://www.sequeirapartners.com/wp-content/uploads/2026/02/Sequeira-Partners-Facility-Services-Q4-2025_F.pdf) (accessed 2026-07-22): North American facility-services transaction activity and buyer interest in exterior building services, a broad category explicitly including landscaping and grounds maintenance.
- **S9** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projections show positive exact-industry employment growth for Landscaping Services and stronger real-output growth for the broader Services to Buildings and Dwellings group.
