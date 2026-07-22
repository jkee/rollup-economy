# 327420 — Gypsum Product Manufacturing

*v5.1 Stage 1 research memo. Run `327420-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.04 · L 0.33 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent need for physical gypsum products and practical AI use cases in maintenance, quality, scheduling, and administrative workflows.
**Weakness:** Very few lower-middle-market manufacturers may satisfy the recurring outsourced-service lens, and commodity channels can force efficiency gains into price.

## Business-model lens
- Included: US lower-middle-market manufacturers of gypsum wallboard, plaster, molding, statuary, architectural plasterwork, and other gypsum products that make repeat sales to external distributors, contractors, builders, or industrial customers, including recurring specification, custom-production, inventory, and delivery work embedded in those relationships.
- Excluded: Gypsum mining without product manufacturing, captive internal units, shells, non-control financing vehicles, and firms outside the lower-middle-market band. One-time product transactions that do not amount to recurring or repeat outsourced supply are outside the screened population.
- Customer and revenue model: Revenue is principally product sales to building-material dealers, specialty distributors, lumber yards, home-center chains, contractors, and other construction customers. Wallboard is commonly priced on a delivered basis and shipped locally by truck; eligible specialty producers may also earn repeat revenue through custom fabrication, specification support, scheduled replenishment, and job-linked delivery.
- Deviation from default lens: none

## Executive view
The industry offers a real but bounded operational AI opportunity in planning, maintenance, quality, documentation, and customer coordination. The central limitation is lens eligibility: gypsum manufacturing is primarily a physical product business, and US wallboard is dominated by a small group of large producers. A credible target set is therefore likely confined to specialty or regional manufacturers with service-rich repeat relationships.

## How AI changes the work
AI can improve predictive maintenance, defect detection, production scheduling, demand forecasting, inventory visibility, technical-document retrieval, and custom-product design. It is unlikely to eliminate the core need for kiln, line, cutting, handling, maintenance, quality, and delivery work.

## Value capture
Operators can retain savings where customization, specification knowledge, service reliability, freight execution, and short runs differentiate the offer. Commodity products sold through concentrated channels face stronger customer sharing and price competition, so durable capture depends on a defensible service component rather than line efficiency alone.

## Firm availability
Commodity wallboard is unusually concentrated, while public data does not identify the count, ownership profile, or transfer history of eligible specialty firms. The practical acquisition universe may be much smaller than the dataset firm count suggests.

## Demand durability
Wallboard and plaster remain essential physical building inputs, and repair, remodel, and nonresidential demand diversify exposure. Quantity nevertheless follows construction cycles, and recent wallboard shipment weakness argues against assuming uninterrupted growth.

## Risks and uncertainty
The largest uncertainties are the eligible-firm denominator, owner succession, contract-level pass-through, and the difference between modern wallboard plants and smaller specialty shops. Commodity exposure, customer concentration, freight economics, energy costs, regulation, and construction cyclicality could erase benefits that appear attractive in a workflow-only analysis.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1248 | — | OBSERVED | — |
| n | — | 17 | — | ESTIMATE | — |
| a | 0.08 | 0.15 | 0.24 | PROXY | S2, S3 |
| rho | 0.26 | 0.44 | 0.62 | PROXY | S3, S4 |
| e | 0.04 | 0.1 | 0.22 | ESTIMATE | S1, S2 |
| s5 | 0.07 | 0.14 | 0.25 | PROXY | S2 |
| q | 0.36 | 0.53 | 0.7 | ESTIMATE | S2 |
| d5 | 0.86 | 0.98 | 1.12 | PROXY | S2, S5 |
| o | 0.91 | 0.97 | 1 | ESTIMATE | S1, S2, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.10 | 0.33 | 0.74 | PROXY |
| F | 0.07 | 0.34 | 1.06 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 7.83 | 9.51 | 10.00 | ESTIMATE |

## Caveats
- a: No source measures AI-exposed task share specifically for NAICS 327420.
- a: The estimate may differ sharply between automated wallboard lines and labor-intensive architectural-plaster shops.
- rho: The cited adoption evidence is not specific to gypsum products.
- rho: Firm size and plant modernization likely create a wide implementation gap within the lens.
- e: Public sources do not enumerate lower-middle-market firms by revenue model.
- e: The boundary between repeat product supply and an outsourced service is judgment-sensitive.
- s5: The market-concentration source concerns US wallboard, not all gypsum products or lower-middle-market firms.
- s5: No denominator-matched control-transfer cohort was located.
- q: The public source describes a large wallboard producer and may overstate customer concentration for specialty firms.
- q: No contract-level pass-through or post-automation repricing data was found.
- d5: Shipment data can reflect inventory and capacity effects as well as end demand.
- d5: The service basket for eligible specialty firms is not separately measured.
- o: The accountable-operator share is not directly observed.
- o: Specialty plaster and commodity wallboard face different substitution and channel risks.

## Sources
- **S1** — [2022 NAICS 327420: Gypsum Product Manufacturing](https://www.census.gov/naics/?details=327420&input=327420&year=2022) (accessed 2026-07-22): Official industry scope, including establishments manufacturing wallboard, plaster, plasterboard, moldings, statuary, and architectural plasterwork.
- **S2** — [Eagle Materials 2026 Annual Report and Form 10-K](https://ir.eaglematerials.com/static-files/69efccf3-9a62-483f-9042-be832a0bd75c) (accessed 2026-07-22): Wallboard manufacturing and distribution, construction-linked demand, delivered pricing, customer concentration, market concentration, capacity, recent shipment decline, input costs, and operating constraints.
- **S3** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Manufacturing AI use cases in predictive maintenance, quality, forecasting, scheduling, document management, and design, plus implementation barriers.
- **S4** — [AI Use at U.S. Businesses](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Current business AI adoption and expected-use evidence by firm size, used only as a cross-industry implementation proxy.
- **S5** — [Mineral Commodity Summaries 2026: Gypsum](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-gypsum.pdf) (accessed 2026-07-22): US gypsum production and consumption, wallboard sales, construction dependence, synthetic gypsum supply, and substitute materials.
