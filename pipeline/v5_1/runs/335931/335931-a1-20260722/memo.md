# 335931 — Current-Carrying Wiring Device Manufacturing

*v5.1 Stage 1 research memo. Run `335931-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.96 · L 1.34 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Electrification and recurring qualified customer programs support durable demand and improvable engineering, planning, and quality workflows.
**Weakness:** Safety-critical physical production and a small eligible service subset limit implementable AI opportunity.

## Business-model lens
- Included: Independent lower-middle-market manufacturers that repeatedly produce customer-specific, private-label, or qualified plugs, terminals, bus bars, receptacles, GFCIs, switches, lamp holders, and related current-carrying wiring devices for external OEM, distribution, and infrastructure customers.
- Excluded: Manufacturers selling only proprietary standardized catalog products, captive plants, electronic connectors classified elsewhere, noncurrent-carrying devices, pure distributors, shell entities, non-control financing vehicles, and firms outside the normalized EBITDA band.
- Customer and revenue model: Customers buy recurring production programs under electrical, dimensional, material, safety, testing, certification, packaging, and delivery specifications through purchase orders or supply agreements.
- Deviation from default lens: The code includes branded standard products and customer-specific contract programs. The lens retains recurring outsourced and private-label production so eligibility and commercial retention describe a coherent model.

## Executive view
The coherent opportunity is the subset of wiring-device manufacturers serving recurring customer-specific and private-label programs. Electrical demand is structurally supportive and labor intensity is meaningful, but assembly and testing are physical and product safety sharply constrains autonomous AI use.

## How AI changes the work
AI can improve RFQ and specification review, quoting, scheduling, purchasing, test-data analysis, quality and certification documentation, maintenance triage, and customer service. Stamping, molding, plating, winding, assembly, and electrical testing execution remain equipment- and labor-dependent.

## Value capture
Qualification, certification, tooling, reliability, and delivery create switching cost. Standardized alternatives, bids, commodity indices, distributor leverage, and should-cost analysis can pass through visible labor savings.

## Firm availability
Only a minority of product manufacturers likely fit the outsourced-service lens. Transferability depends on customer-program portability, safety certifications, quality history, tooling, product liability, workforce depth, and reduced owner dependence.

## Demand durability
Current-carrying devices remain essential as electricity use, data centers, building electrification, and infrastructure expand. Domestic opportunity is tempered by construction cycles, imports, supplier consolidation, and product integration.

## Risks and uncertainty
The case weakens if a target is primarily a branded catalog company, depends on one distributor, lacks digital test records, faces certification changes, or needs capital automation rather than AI. Electrical failures, recalls, counterfeit risk, and commodity price volatility can overwhelm savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3262 | — | OBSERVED | — |
| n | — | 138 | — | ESTIMATE | — |
| a | 0.13 | 0.21 | 0.3 | PROXY | S2, S3 |
| rho | 0.31 | 0.49 | 0.66 | ESTIMATE | S2 |
| e | 0.07 | 0.16 | 0.3 | ESTIMATE | S1 |
| s5 | 0.08 | 0.17 | 0.28 | PROXY | S4 |
| q | 0.32 | 0.51 | 0.7 | ESTIMATE | — |
| d5 | 0.91 | 1.07 | 1.22 | PROXY | S5, S6 |
| o | 0.93 | 0.98 | 0.997 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.53 | 1.34 | 2.58 | ESTIMATE |
| F | 0.92 | 2.51 | 4.07 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 8.46 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS data cover NAICS 335 rather than 335931 or the outsourced subset.
- a: ILO exposure is technical potential rather than observed substitution.
- a: Existing automated stamping, molding, assembly, and electrical testing are excluded from the remaining opportunity.
- rho: No source measures five-year AI implementation among eligible wiring-device manufacturers.
- rho: Certification and safety-critical applications may require conservative human review even when models perform well.
- e: The provided firm count is margin-bridged and estimated before applying the outsourced-service lens.
- e: A customized configuration of a branded standard device may not constitute outsourced manufacturing.
- s5: Owner-age data are cross-industry, based on 2018, and count responding owners rather than firms.
- s5: Age does not establish sale intent, transferability, or transaction completion.
- q: No public contract dataset establishes benefit sharing for eligible firms.
- q: Retention can be lower in standardized outlets and switches than in qualified custom bus bars or terminals.
- d5: Electricity demand is an indirect driver and not a direct measure of wiring-device quantity.
- d5: BLS projections cover a broader electrical-equipment group.
- d5: Residential receptacles, industrial bus bars, and protective devices have different cycles.
- o: Operator requirement can persist while production moves offshore or to larger suppliers.
- o: Demand elimination and imports are reflected primarily in d5.

## Sources
- **S1** — [NAICS Definition: Current-Carrying Wiring Device Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Census defines 335931 and lists bus bars, GFCIs, lamp holders, lightning arrestors and coils, receptacles, and electrical wiring switches as examples.
- **S2** — [Electrical Equipment, Appliance, and Component Manufacturing: NAICS 335](https://www.bls.gov/iag/tgs/iag335.htm) (accessed 2026-07-22): BLS reports 2025 employment of 65,350 electrical and electronic equipment assemblers, 57,660 team assemblers, 14,050 inspectors and testers, and 14,650 production supervisors in the broader subsector.
- **S3** — [Generative AI and Jobs: Policies to Manage the Transition](https://www.ilo.org/sites/default/files/2024-08/GenAI%20and%20Jobs_Policy%20Brief_ILO.pdf) (accessed 2026-07-22): ILO reports 24% of clerical tasks at high automation exposure and 58% at medium exposure, while other occupational groups have only 1% to 4% highly exposed and no more than 25% medium-exposed tasks.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Census reports that 51% of responding owners of employer businesses were age 55 or older, based on the 2019 Annual Business Survey for data year 2018.
- **S5** — [Faster-Than-Expected Growth in Data Center Power Demand](https://www.eia.gov/todayinenergy/detail.php/detail.php?id=67344) (accessed 2026-07-22): EIA reports U.S. electricity demand grew about 1.7% annually from 2020 through 2025, compared with 0.1% annually from 2005 through 2019, and identifies data centers as a growth driver.
- **S6** — [Producing the Goods of the Future: Job Opportunities in Manufacturing](https://www.bls.gov/careeroutlook/2026/article/manufacturing.htm) (accessed 2026-07-22): BLS states that other electrical equipment and component manufacturing is projected to add about 48,400 jobs from 2024 to 2034, the most among manufacturing industries.
