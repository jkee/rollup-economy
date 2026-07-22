# 325211 — Plastics Material and Resin Manufacturing

*v5.1 Stage 1 research memo. Run `325211-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.17 · L 0.25 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** An explicit custom-manufacturing segment combines recurring qualified formulations with information-heavy workflows that AI can improve.
**Weakness:** Commodity exposure, feedstock economics, environmental pressure, and liability can dominate the modest labor opportunity.

## Business-model lens
- Included: Independent lower-middle-market producers that repeatedly manufacture, polymerize, mix, or blend resins and plastics materials on a custom, toll, or customer-specification basis for external customers.
- Excluded: Large integrated commodity-resin producers, businesses selling only noncustomized proprietary resins, custom compounders that only process purchased resin outside NAICS 325211, captive plants, shell entities, non-control financing vehicles, and firms outside the normalized EBITDA band.
- Customer and revenue model: Industrial customers buy recurring custom resin campaigns or volumes under formulation and performance specifications, with revenue based on conversion fees, per-pound pricing, or formulas that may adjust for monomer, feedstock, and energy costs.
- Deviation from default lens: Census explicitly includes both custom resin manufacturing or blending and noncustomized synthetic-resin production in this code. The lens retains the recurring custom and toll subset and excludes pure commodity production so eligibility and commercial retention describe a coherent outsourced service.

## Executive view
Plastics material and resin manufacturing contains an explicitly recognized custom-production segment, making the outsourced-service lens more natural than in many chemical codes. The opportunity remains narrower than the full industry because large commodity producers and purchased-resin compounders are excluded, and plant economics remain more exposed to feedstock, utilization, and product mix than labor alone.

## How AI changes the work
AI can improve formulation search, quoting, campaign scheduling, purchasing, laboratory and batch review, deviation handling, maintenance triage, regulatory documentation, and customer technical support. Physical reaction and blending, material handling, sampling, maintenance execution, and accountable release remain less substitutable.

## Value capture
Qualification costs and formulation know-how can preserve value from better yield, quality, development speed, and turnaround. Transparent savings are vulnerable to monomer-index formulas, open-book tolling, procurement benchmarks, renewal bids, and customer concentration.

## Firm availability
The explicit custom category and larger raw firm count support a plausible target population, but classification is essential because commodity resin producers and NAICS 325991 purchased-resin compounders do not qualify. Transfer diligence must cover formulations, customer approvals, environmental history, product liability, plant condition, and technical staff.

## Demand durability
Physical resin demand should persist across broad end markets, but virgin-plastics growth is contested by source reduction, recycling, regulation, and substitution. Circularity can also create new work in recycled-feedstock qualification, stabilization, blending, traceability, and customer-specific performance.

## Risks and uncertainty
The case weakens if diligence reveals commodity price-taking, little custom revenue, low addressable labor, open-book pass-through, obsolete capacity, or material environmental and product-liability exposure. Resin-family concentration, customer qualification cycles, volatile monomer spreads, and policy shifts can overwhelm AI benefits.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0627 | — | OBSERVED | — |
| n | — | 359 | — | ESTIMATE | — |
| a | 0.14 | 0.22 | 0.31 | PROXY | S2, S3 |
| rho | 0.29 | 0.45 | 0.62 | ESTIMATE | S5, S6 |
| e | 0.13 | 0.26 | 0.42 | ESTIMATE | S1 |
| s5 | 0.08 | 0.16 | 0.27 | PROXY | S4, S5 |
| q | 0.36 | 0.54 | 0.72 | ESTIMATE | — |
| d5 | 0.87 | 1.04 | 1.19 | PROXY | S6, S7, S8 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.10 | 0.25 | 0.48 | ESTIMATE |
| F | 2.50 | 4.45 | 6.00 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 7.83 | 9.98 | 10.00 | ESTIMATE |

## Caveats
- a: BLS data cover NAICS 325 rather than this six-digit code or the custom-resin subset.
- a: ILO exposure is technical potential rather than observed substitution and emphasizes generative AI.
- a: Formulation-intensive batch plants and commodity polymer trains have materially different occupation mixes.
- rho: No source measures five-year AI implementation for lower-middle-market custom resin manufacturers.
- rho: Customer approvals may require revalidation even when AI changes only internal workflow.
- e: The provided firm count is margin-bridged and may include commodity producers whose economics do not resemble the custom subset.
- e: Custom compounding of purchased resin is classified in NAICS 325991 and should not be counted even when market descriptions blur the boundary.
- s5: Census owner-age data are cross-industry, based on 2018, and count responding owners rather than firms.
- s5: Age does not establish sale intent, a transferable business, or a completed control transaction.
- q: No public contract sample measures productivity pass-through for eligible custom resin producers.
- q: Capture can be much lower for benchmarked commodity formulations and higher for qualified proprietary customer programs.
- d5: The global production projection is much broader and longer-dated than the screened U.S. service basket.
- d5: Environmental policy can reduce some virgin-resin demand while increasing custom recycled-content formulation work.
- d5: One ratio masks major differences among resin families and end markets.
- o: The estimate does not protect current product uses from source reduction or substitution, which is reflected in d5.
- o: Operator-required manufacturing can migrate to a larger integrated supplier even when material demand persists.

## Sources
- **S1** — [North American Industry Classification System: 325211 Definition](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Census defines 325211 to include manufacturing resins, plastics materials, and thermoplastic elastomers and mixing or blending resins on a custom basis, as well as noncustomized synthetic resins; it assigns custom compounding of purchased resin to 325991.
- **S2** — [Chemical Manufacturing: NAICS 325](https://www.bls.gov/iag/tgs/iag325.htm) (accessed 2026-07-22): BLS reports 2025 chemical-manufacturing employment of 124,330 chemical equipment operators, 17,600 chemical technicians, 27,530 chemists, 25,810 mixing and blending operators, and 57,400 packaging and filling operators.
- **S3** — [Generative AI and Jobs: Policies to Manage the Transition](https://www.ilo.org/sites/default/files/2024-08/GenAI%20and%20Jobs_Policy%20Brief_ILO.pdf) (accessed 2026-07-22): ILO reports 24% of clerical tasks at high automation exposure and 58% at medium exposure, while other occupational groups have 1% to 4% highly exposed and no more than 25% medium-exposed tasks.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Census reports that 51% of responding owners of employer businesses were age 55 or older, based on the 2019 Annual Business Survey for data year 2018.
- **S5** — [Chemical Manufacturing Area Sources: National Emission Standards for Hazardous Air Pollutants](https://www.epa.gov/stationary-sources-air-pollution/chemical-manufacturing-area-sources-national-emission-standards) (accessed 2026-07-22): EPA lists plastic materials and resins manufacturing among nine regulated chemical area-source categories and states that amendments were finalized on March 28, 2026.
- **S6** — [Advanced Recycling of Plastics](https://www.epa.gov/plastics/advanced-recycling-plastics) (accessed 2026-07-22): EPA states that global plastics production is projected to almost triple by 2060, describes limitations from variable recycled-plastic properties, and says resulting oils and monomers must meet qualified product specifications for new resin manufacture.
- **S7** — [Annual Energy Outlook 2026 Narrative](https://www.eia.gov/outlooks/aeo/pdf/AEO_Narrative.pdf) (accessed 2026-07-22): EIA projects industrial liquid-fuel use to grow across all cases, with HGL and naphtha feedstocks in bulk chemicals helping drive growth; industrial petroleum use rises from 5.5 million barrels per day in 2025 to 6.3 million to 7.7 million in 2050 in most cases.
- **S8** — [Plastics: Material-Specific Data](https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/plastics-material-specific-data) (accessed 2026-07-22): EPA reports that three million tons of plastics were recycled in 2018, an overall recycling rate of 8.7%, and describes resin use across containers and packaging.
