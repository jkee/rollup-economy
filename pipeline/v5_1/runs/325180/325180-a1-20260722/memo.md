# 325180 — Other Basic Inorganic Chemical Manufacturing

*v5.1 Stage 1 research memo. Run `325180-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.50 · L 0.50 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring specification-bound production creates defensible demand and valuable administrative, quality, and planning workflows for AI assistance.
**Weakness:** The eligible contract-production subset may be very small and carries capital, compliance, and environmental liabilities that AI does not remove.

## Business-model lens
- Included: Independent lower-middle-market toll, contract, and custom producers that repeatedly synthesize, purify, blend, or regenerate basic inorganic chemicals for external customers under recurring specifications.
- Excluded: Integrated or captive plants, businesses selling only proprietary commodity output, shell entities, non-control financing vehicles, and firms outside the normalized EBITDA band.
- Customer and revenue model: Industrial customers pay per batch, unit, or contracted production campaign, often with specification, testing, documentation, and hazardous-material handling embedded in the price.
- Deviation from default lens: The code combines large continuous commodity plants with contract and specialty-batch operations. The lens retains only recurring outsourced contract or toll production so that firm eligibility and value capture describe one coherent business model.

## Executive view
The coherent opportunity is a narrow set of independent toll and custom inorganic producers, not the code's large commodity plants. These businesses have recurring industrial specifications and document-intensive workflows, but most labor and enterprise value remain tied to hazardous physical production and regulated assets.

## How AI changes the work
AI is most useful in quoting, production planning, purchasing, maintenance triage, batch and certificate review, regulatory documentation, and retrieval of plant knowledge. It is much less substitutive in material handling, equipment operation, maintenance execution, sampling, and final accountable release.

## Value capture
Savings can persist when they improve turnaround, right-first-time quality, or compliance as well as cost. Direct labor savings are more exposed to renewal repricing, open-book tolling, and procurement pressure, so commercial retention depends heavily on contract structure and customer concentration.

## Firm availability
Only a minority of the dataset firms are likely to meet the recurring outsourced-service lens. Aging ownership provides a succession signal, but permits, environmental liabilities, customer approvals, and plant capital requirements make transferability materially harder than owner demographics imply.

## Demand durability
The physical service basket should remain operator-required because customers need controlled chemical conversion and safe delivery. Real demand is likely durable but cyclical, with product-level exposure to imports, reformulation, regulation, and downstream plant utilization.

## Risks and uncertainty
The largest uncertainties are the scarcity of truly eligible firms, environmental and process-safety liabilities, opaque contract pass-through, concentration in a few customers or products, and whether old plant data can support validated AI. A superficially attractive labor case can fail if diligence reveals mostly physical production roles or commodity price-taking.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1272 | — | OBSERVED | — |
| n | — | 119 | — | ESTIMATE | — |
| a | 0.14 | 0.22 | 0.31 | PROXY | S1, S2 |
| rho | 0.3 | 0.45 | 0.62 | ESTIMATE | S4 |
| e | 0.04 | 0.1 | 0.2 | ESTIMATE | S6 |
| s5 | 0.08 | 0.16 | 0.27 | PROXY | S3, S4 |
| q | 0.38 | 0.55 | 0.72 | ESTIMATE | — |
| d5 | 0.88 | 1.02 | 1.13 | PROXY | S5 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.50 | 0.98 | ESTIMATE |
| F | 0.52 | 1.71 | 3.23 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.92 | 9.79 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation counts cover all NAICS 325 chemical manufacturing rather than this six-digit code or the eligible contract-production subset.
- a: ILO exposure is global and focused on generative AI; it is not an observed displacement measure.
- a: The estimate excludes already automated distributed-control and conventional process-control tasks.
- rho: No source measures five-year implementation for small inorganic contract manufacturers.
- rho: Implementation will vary sharply with electronic batch records, historian quality, and customer validation requirements.
- e: The provided firm count is margin-bridged and estimated before applying the service-business lens.
- e: Public descriptions often do not reveal whether production is toll, captive, or proprietary.
- s5: The Census figure covers responding owners of employer businesses across industries and is based on 2018 data.
- s5: Age, intent to exit, completed sale, and transferable operating condition are different quantities.
- q: No public contract sample establishes pass-through behavior for eligible firms.
- q: Commodity-linked pricing and customer concentration can make capture much lower than gross operational benefit.
- d5: EIA's bulk-chemical outlook is broader than inorganic chemicals and reports energy and feedstock consumption rather than service quantity.
- d5: Constant-quality demand is not directly observed, and the five-year result can be dominated by the industrial cycle.
- o: The estimate assumes the current service basket and does not protect individual chemicals from regulatory phaseout or technological substitution.
- o: Accountable operation may consolidate into larger plants even when physical demand persists.

## Sources
- **S1** — [Chemical Manufacturing: NAICS 325](https://www.bls.gov/iag/tgs/iag325.htm) (accessed 2026-07-22): BLS reports 2025 chemical-manufacturing employment of 124,330 chemical equipment operators, 17,600 chemical technicians, 27,530 chemists, 25,810 mixing and blending operators, and 57,400 packaging and filling operators; it also reports current employment and hours.
- **S2** — [Generative AI and Jobs: Policies to Manage the Transition](https://www.ilo.org/sites/default/files/2024-08/GenAI%20and%20Jobs_Policy%20Brief_ILO.pdf) (accessed 2026-07-22): ILO reports that clerical support work has 24% of tasks at high automation exposure and 58% at medium exposure, while other occupational groups have only 1% to 4% highly exposed and no more than 25% medium-exposed tasks.
- **S3** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The Census infographic reports that 51% of responding owners of employer businesses were age 55 or older, based on the 2019 Annual Business Survey for data year 2018.
- **S4** — [Chemical Manufacturing Area Sources: National Emission Standards for Hazardous Air Pollutants](https://www.epa.gov/stationary-sources-air-pollution/chemical-manufacturing-area-sources-national-emission-standards) (accessed 2026-07-22): EPA identifies industrial inorganic chemical manufacturing among nine regulated chemical area-source categories and states that amendments to the standards were finalized on March 28, 2026; the page defines area sources using hazardous-air-pollutant thresholds.
- **S5** — [Annual Energy Outlook 2026 Narrative](https://www.eia.gov/outlooks/aeo/pdf/AEO_Narrative.pdf) (accessed 2026-07-22): EIA projects industrial liquid-fuel use to grow across all cases, with bulk-chemical HGL and naphtha feedstocks helping drive the increase, and projects industrial petroleum use rising from 5.5 million barrels per day in 2025 to 6.3 million to 7.7 million in 2050 in most cases.
- **S6** — [Chemical Manufacturing Sector Profile](https://archive.epa.gov/sectors/web/html/chemical.html) (accessed 2026-07-22): EPA's archived sector profile distinguishes commodity producers operating large dedicated continuous plants from specialty-batch producers making smaller quantities as needed with changing materials, conditions, and equipment.
