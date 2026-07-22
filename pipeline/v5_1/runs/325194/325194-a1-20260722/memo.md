# 325194 — Cyclic Crude, Intermediate, and Gum and Wood Chemical Manufacturing

*v5.1 Stage 1 research memo. Run `325194-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.98 · L 0.22 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring customer specifications and difficult physical processing can create sticky outsourced relationships and useful AI-enabled quality and planning workflows.
**Weakness:** The tiny, heterogeneous eligible population and weak direct demand evidence make firm availability and five-year quantity unusually uncertain.

## Business-model lens
- Included: Independent lower-middle-market producers that repeatedly provide toll, custom, or specification-driven distillation, fractionation, synthesis, recovery, or modification of cyclic intermediates and gum or wood chemicals for external industrial customers.
- Excluded: Integrated refinery, steel, pulp, or forestry operations; plants selling only proprietary commodity output; captive facilities; shell entities; non-control financing vehicles; and firms outside the normalized EBITDA band.
- Customer and revenue model: Industrial customers purchase recurring batches, campaigns, or volumes under product specifications, with revenue based on conversion fees, unit prices, or formulas that can pass through feedstock and energy costs.
- Deviation from default lens: The code combines petroleum- or coal-derived cyclic intermediates with gum and wood chemicals and also mixes commodity and specialty operations. The lens retains only recurring outsourced toll or custom processing across those chemistries so the business model is coherent, while preserving the code's heterogeneous end-market risk.

## Executive view
This is a heterogeneous, very small firm population spanning cyclic intermediates and gum or wood chemicals. A coherent opportunity exists only among independent toll and custom processors, where recurring specifications and difficult chemistry support customer relationships, but evidence on how many such firms exist is thin.

## How AI changes the work
AI can improve quoting, campaign scheduling, feedstock planning, batch and laboratory review, maintenance triage, regulatory documentation, and retrieval of plant knowledge. Physical conversion, hazardous operations, sampling, maintenance execution, and final accountable release remain substantially outside direct substitution.

## Value capture
Niche process knowledge and customer qualification can protect benefits tied to quality, yield, and turnaround. Commodity indices, open-book conversion fees, rebids, and concentrated customers can pass through visible cost savings, with capture likely varying more by contract than by chemistry.

## Firm availability
The eligible subset may contain only a few firms because many establishments are integrated with upstream refinery, steel, pulp, or forestry operations or sell their own products. Any transfer must survive environmental, process-safety, feedstock, customer-approval, and key-person diligence.

## Demand durability
The underlying chemicals are physical industrial inputs, but current quantity signals are mixed and product-specific. Cyclic intermediates face petrochemical cycles and imports, while gum and wood chemicals face paper-market shifts, synthetic substitutes, and opportunities from bio-based feedstocks.

## Risks and uncertainty
The largest uncertainties are eligibility, the combined code's incompatible product families, customer and product concentration, environmental liabilities, opaque pass-through terms, and old plant data. The case weakens materially if diligence finds proprietary commodity sales, dependent upstream integration, or little addressable cognitive labor.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0547 | — | OBSERVED | — |
| n | — | 12 | — | ESTIMATE | — |
| a | 0.15 | 0.23 | 0.32 | PROXY | S2, S3 |
| rho | 0.29 | 0.44 | 0.61 | ESTIMATE | S5 |
| e | 0.07 | 0.16 | 0.3 | ESTIMATE | S1 |
| s5 | 0.07 | 0.14 | 0.24 | PROXY | S4, S5 |
| q | 0.36 | 0.54 | 0.72 | ESTIMATE | — |
| d5 | 0.78 | 0.97 | 1.14 | PROXY | S6, S7 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.10 | 0.22 | 0.43 | ESTIMATE |
| F | 0.09 | 0.38 | 1.00 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 7.02 | 9.31 | 10.00 | ESTIMATE |

## Caveats
- a: BLS data cover NAICS 325 and do not separate the two chemistry families or the outsourced-service subset.
- a: ILO exposure is not an observed displacement rate and focuses on generative AI.
- a: Existing distributed control and laboratory automation must be excluded from the remaining opportunity.
- rho: No source measures five-year AI implementation in eligible NAICS 325194 firms.
- rho: Implementation may differ materially between continuous cyclic-intermediate plants and smaller batch wood-chemical operations.
- e: The provided firm count is a margin-bridged estimate and is very small, so classifying one firm differently has a large effect.
- e: Public descriptions rarely distinguish proprietary product sales from true third-party toll processing.
- s5: The Census owner-age evidence is cross-industry, based on 2018, and counts responding owners rather than firms.
- s5: Aging ownership does not establish sale intent, transferability, or a completed control transaction.
- q: No public contract dataset establishes benefit sharing for eligible firms.
- q: Capture may differ sharply between bespoke modified rosin products and benchmarked cyclic intermediates.
- d5: Petrochemical feedstocks are a broader and different product population than this combined NAICS code.
- d5: Gum and wood chemical demand can diverge from cyclic intermediates, making one industry ratio structurally imprecise.
- d5: Constant-quality outsourced-service demand is not directly observed.
- o: The estimate does not protect specific chemicals from substitution or regulation, which is reflected in d5.
- o: Operator-required work can migrate to a larger integrated supplier even when the physical step persists.

## Sources
- **S1** — [2012 NAICS Definition File: 325194](https://www2.census.gov/library/reference/naics/technical-documentation/definition-files/2012_definition_file.pdf) (accessed 2026-07-22): Census defines 325194 as establishments distilling wood or gum, distilling coal tars, manufacturing wood or gum chemicals, or manufacturing cyclic crudes and intermediates from refined petroleum or natural gas.
- **S2** — [Chemical Manufacturing: NAICS 325](https://www.bls.gov/iag/tgs/iag325.htm) (accessed 2026-07-22): BLS reports 2025 chemical-manufacturing employment of 124,330 chemical equipment operators, 17,600 chemical technicians, 27,530 chemists, 25,810 mixing and blending operators, and 57,400 packaging and filling operators.
- **S3** — [Generative AI and Jobs: Policies to Manage the Transition](https://www.ilo.org/sites/default/files/2024-08/GenAI%20and%20Jobs_Policy%20Brief_ILO.pdf) (accessed 2026-07-22): ILO reports 24% of clerical tasks at high automation exposure and 58% at medium exposure, while other occupational groups have only 1% to 4% highly exposed and no more than 25% medium-exposed tasks.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Census reports that 51% of responding owners of employer businesses were age 55 or older, based on the 2019 Annual Business Survey for data year 2018.
- **S5** — [Chemical Manufacturing Area Sources: National Emission Standards for Hazardous Air Pollutants](https://www.epa.gov/stationary-sources-air-pollution/chemical-manufacturing-area-sources-national-emission-standards) (accessed 2026-07-22): EPA lists cyclic crude and intermediate production among nine regulated chemical-manufacturing area-source categories and states that amendments were finalized on March 28, 2026.
- **S6** — [U.S. Product Supplied of Petrochemical Feedstocks](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?f=a&n=pet&s=mpcup_nus_1) (accessed 2026-07-22): EIA's annual series reports U.S. petrochemical-feedstock product supplied of 115.776 million barrels in 2019 and 74.983 million barrels in 2024, with earlier annual history on the same page.
- **S7** — [Annual Energy Outlook 2026 Narrative](https://www.eia.gov/outlooks/aeo/pdf/AEO_Narrative.pdf) (accessed 2026-07-22): EIA projects industrial liquid-fuel use to grow across all cases and states that HGL and naphtha feedstocks in the bulk-chemicals sector help drive the increase; industrial petroleum use rises from 5.5 million barrels per day in 2025 to 6.3 million to 7.7 million in 2050 in most cases.
