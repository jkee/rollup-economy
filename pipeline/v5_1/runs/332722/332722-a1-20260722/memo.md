# 332722 — Bolt, Nut, Screw, Rivet, and Washer Manufacturing

*v5.1 Stage 1 research memo. Run `332722-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.50 · L 0.83 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring qualified fastener programs create sticky physical demand and improvable commercial, planning, and quality workflows.
**Weakness:** Commodity competition, pass-through pressure, and already automated production limit incremental AI value.

## Business-model lens
- Included: Independent lower-middle-market manufacturers that repeatedly produce customer-specific, private-label, or qualified metal bolts, nuts, screws, rivets, washers, and other industrial fasteners for external OEM and industrial customers.
- Excluded: Manufacturers selling only standardized proprietary or commodity catalog fasteners, captive plants, precision turned product firms classified elsewhere, plastics fastener producers, pure distributors, shell entities, non-control financing vehicles, and firms outside the normalized EBITDA band.
- Customer and revenue model: OEM and industrial customers buy repeat fastener runs under drawings or standards covering material, dimensions, strength, heat treatment, coating, traceability, testing, packaging, and delivery through purchase orders or supply agreements.
- Deviation from default lens: The code includes both commodity catalog fasteners and customer-specific or qualified contract programs. The lens retains recurring outsourced production so eligibility and commercial retention describe one coherent model.

## Executive view
The coherent opportunity is the subset of fastener manufacturers serving recurring custom, private-label, or qualified OEM programs. Labor intensity is meaningful, but production is physical and often already highly automated, while standardized products face severe price and import competition.

## How AI changes the work
AI can improve RFQ and specification review, quoting, scheduling, purchasing, tool-life analysis, inspection review, traceability documentation, maintenance triage, and customer service. Heading, threading, forming, heat treatment, coating, sorting, and packaging remain equipment-dependent.

## Value capture
Qualification, traceability, tooling, and reliable delivery can protect savings in critical programs. Standardized alternatives, annual bids, cost-down clauses, should-cost models, distributor power, and metal indices make visible productivity gains vulnerable to pass-through.

## Firm availability
Only a subset of producers meets the outsourced-service lens because many sell standardized catalog fasteners. Founder succession can create transactions, but transferability requires diversified qualified programs, maintained machines, quality certifications, workforce depth, and limited owner dependence.

## Demand durability
Fasteners remain indispensable across most physical industries, but domestic volume is cyclical and exposed to imports, customer inventory, product redesign, and build rates. Qualified critical fasteners should be more durable than commodity bolts and washers.

## Risks and uncertainty
The case weakens if a target competes primarily on standardized price, relies on one OEM, has obsolete equipment or weak traceability, needs capital automation rather than AI, or accepts mandatory annual cost-downs. Quality escapes and product liability can overwhelm modest labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2377 | — | OBSERVED | — |
| n | — | 155 | — | ESTIMATE | — |
| a | 0.11 | 0.19 | 0.28 | PROXY | S2, S3, S6 |
| rho | 0.29 | 0.46 | 0.63 | ESTIMATE | S2, S6 |
| e | 0.09 | 0.21 | 0.36 | ESTIMATE | S1 |
| s5 | 0.08 | 0.17 | 0.28 | PROXY | S4 |
| q | 0.24 | 0.43 | 0.63 | ESTIMATE | — |
| d5 | 0.78 | 0.97 | 1.14 | PROXY | S5 |
| o | 0.94 | 0.985 | 0.998 | ESTIMATE | S1, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.30 | 0.83 | 1.68 | ESTIMATE |
| F | 1.21 | 3.02 | 4.52 | ESTIMATE |
| C | 4.80 | 8.60 | 10.00 | ESTIMATE |
| D | 7.33 | 9.55 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation evidence covers NAICS 332 rather than 332722 or the retained contract subset.
- a: ILO exposure is technical potential rather than observed substitution.
- a: Existing heading, threading, feeding, and sorting automation is outside the remaining opportunity.
- rho: No source measures five-year AI implementation in eligible fastener manufacturers.
- rho: Digital readiness differs between modern high-volume cold-heading lines and older specialty plants.
- e: The provided firm count is margin-bridged and estimated before applying the outsourced-service lens.
- e: Producing to an industry fastener standard does not itself establish outsourced customer-specific manufacturing.
- s5: Owner-age data are cross-industry, based on 2018, and count responding owners rather than firms.
- s5: Age and succession pressure do not establish sale intent or transaction completion.
- q: No public contract dataset measures benefit sharing for eligible fastener producers.
- q: Retention can be much higher for qualified aerospace or medical fasteners than for standardized industrial products.
- d5: The output series combines machine shops, turned products, and fasteners and includes firms outside the lens.
- d5: Historical output is not a direct five-year forecast.
- d5: Commodity construction fasteners and qualified aerospace fasteners have very different demand patterns.
- o: Operator requirement can persist while production shifts offshore or to larger suppliers.
- o: Demand elimination and import substitution are reflected primarily in d5.

## Sources
- **S1** — [NAICS Definition: Turned Product and Fastener Manufacturing](https://www.census.gov/naics/?details=33272&input=33272&year=2022) (accessed 2026-07-22): Census defines 332722 as manufacturing metal bolts, nuts, screws, rivets, washers, and other industrial fasteners using headers, threaders, and nut-forming machines; the broader 33272 definition includes customized machinery and equipment parts.
- **S2** — [Fabricated Metal Product Manufacturing: NAICS 332](https://www.bls.gov/iag/tgs/iag332.htm) (accessed 2026-07-22): BLS reports 2025 fabricated-metal employment of 56,060 press operators, 67,090 production supervisors, 101,640 machinists, 125,250 team assemblers, and 112,520 welders.
- **S3** — [Generative AI and Jobs: Policies to Manage the Transition](https://www.ilo.org/sites/default/files/2024-08/GenAI%20and%20Jobs_Policy%20Brief_ILO.pdf) (accessed 2026-07-22): ILO reports 24% of clerical tasks at high automation exposure and 58% at medium exposure, while other occupational groups have only 1% to 4% highly exposed and no more than 25% medium-exposed tasks.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Census reports that 51% of responding owners of employer businesses were age 55 or older, based on the 2019 Annual Business Survey for data year 2018.
- **S5** — [Real Sectoral Output: Machine Shops, Turned Product, and Fasteners](https://fred.stlouisfed.org/series/IPUEN3327T010000000) (accessed 2026-07-22): BLS real sectoral output for NAICS 3327 declined from an index of 102.578 in 2022 to 84.601 in 2025, with 2017 equal to 100.
- **S6** — [Metal and Plastic Machine Workers](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-22): BLS projects metal and plastic machine-worker employment to decline 7% from 2024 to 2034 and states that firms continue expanding CNC tools and robots to improve quality and lower costs.
