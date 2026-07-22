# 483211 — Inland Water Freight Transportation

*v5.1 Stage 1 research memo. Run `483211-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.22 · L 1.69 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A high labor base and repeat term-contract workflows create usable shore-side efficiency while regulation preserves the carrier's operating role.
**Weakness:** Most labor is physical or safety-critical, and demand varies materially with commodities, waterways, weather, and infrastructure reliability.

## Business-model lens
- Included: US lower-middle-market firms providing recurring or repeat outsourced cargo transportation on rivers, lakes, and intracoastal waterways outside the Great Lakes System, including crewed barge and towing operations that move bulk liquids, grain, coal, aggregates, chemicals, petroleum products, and other freight.
- Excluded: Coastal and Great Lakes freight, deep-sea freight, harbor tug services, passenger transport, captive shipper fleets, fleeting or terminal-only services classified elsewhere, dormant vessel-owning shells, non-control financing vehicles, and firms without transferable operating organizations.
- Customer and revenue model: Industrial, agricultural, energy, construction, and trading customers buy contracts of affreightment, voyage movements, or time-charter capacity under annual or multi-year term contracts and spot agreements; operators provide towboats, barges, qualified crews, dispatch, maintenance, regulatory compliance, and accountable delivery through the inland waterway network.
- Deviation from default lens: none

## Executive view
Inland water freight is labor-intensive but only a minority of work is exposed to AI because vessel operation, deck work, engineering, maintenance, and cargo safety dominate. The implementable opportunity lies in quoting, dispatch support, customer updates, documentation, billing, compliance preparation, and maintenance planning. Regulated towing operations remain operator-dependent, while term contracts offer partial but temporary insulation from benefit pass-through.

## How AI changes the work
AI can structure shipping orders, assist tow and crew schedules, summarize river and maintenance information, draft customer and compliance communications, reconcile voyage bills, and flag anomalies. Human dispatchers must handle river closures and exceptions, and credentialed crews remain responsible for navigation, watchkeeping, cargo, and emergencies. Full vessel autonomy is not a credible five-year labor case.

## Value capture
Term charters and contracts of affreightment can preserve early savings because pricing buys transport capacity and service outcomes. Yet annual renewals, competitive spot markets, and explicit labor, inflation, and fuel escalators expose costs and margins to customers. Operators that use savings to improve vessel utilization, reliability, and avoided hiring should retain more than operators competing on transparent commodity routes.

## Firm availability
The 55-firm LMM count is modeled and should not be treated as a verified target roster. The inland industry includes integrated carriers, small operators, and captive fleets; eligibility depends on finding a standalone external-service company with compliant vessels, durable customers, crews, and management. Broad succession indicators imply supply, but completed inland-marine control-transfer data are missing.

## Demand durability
Inland waterways move large volumes of grain, coal, petroleum, aggregates, chemicals, and other bulk freight at cost advantages to rail. Recent grain volume is strong, but coal decline, pipeline competition, commodity cycles, export policy, lock reliability, drought, flood, and ice create large route-specific swings. Overall five-year real quantity appears close to stable, and remaining waterborne quantity still needs an accountable operator.

## Risks and uncertainty
The main evidence gaps are a 483211-specific task study, an observed LMM target list, closed-deal data, and representative LMM contract samples. Vessel age, dry-dock capital, safety or pollution events, customer concentration, crew shortages, cyber failures, locks, and extreme river levels can overwhelm administrative savings. A weak fleet or commodity route can be unattractive even if AI workflows succeed.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3426 | — | OBSERVED | — |
| n | — | 55 | — | ESTIMATE | — |
| a | 0.12 | 0.22 | 0.34 | ESTIMATE | S2, S6, S7 |
| rho | 0.36 | 0.56 | 0.74 | ESTIMATE | S6, S7 |
| e | 0.46 | 0.65 | 0.81 | PROXY | S1, S3 |
| s5 | 0.09 | 0.19 | 0.31 | PROXY | S8, S9 |
| q | 0.36 | 0.55 | 0.72 | PROXY | S3 |
| d5 | 0.9 | 1.02 | 1.14 | PROXY | S3, S4, S5, S10 |
| o | 0.9 | 0.97 | 0.995 | PROXY | S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.59 | 1.69 | 3.45 | ESTIMATE |
| F | 1.91 | 3.30 | 4.34 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | PROXY |
| D | 8.10 | 9.89 | 10.00 | PROXY |

## Caveats
- a: BLS reports NAICS 483000 rather than 483211 and therefore mixes inland, coastal, passenger, and freight operators.
- a: Employment shares are not wage shares or task shares, and no source directly measures current AI exposure in inland barge firms.
- a: The estimate excludes already-automated work and does not assume AI removes required crew positions.
- rho: No source measures implementation of generative AI in the LMM inland-freight population.
- rho: Pilots during normal river conditions may not generalize to closures, extreme water levels, cargo incidents, or lock delays.
- rho: The estimate applies only to the opportunity counted in a, not to total labor.
- e: The supplied LMM firm count is estimated from receipts and a margin bridge rather than observed firm EBITDA.
- e: Kirby's market description covers inland tank barges and may not represent dry-cargo towing firms.
- e: NAICS is assigned at establishment level while eligibility is a firm-level control-transfer concept.
- s5: Neither source isolates transportation, maritime firms, the LMM EBITDA band, or completed control transfers.
- s5: The Census owner-age statistic uses 2018 data and responding employer businesses only.
- s5: Exit intent can produce a closure, family transfer, or asset sale that does not qualify.
- q: One large tank-barge operator may not represent smaller dry-cargo, grain, aggregate, or specialty operators.
- q: The filing describes cost escalation and market pricing, not AI-savings pass-through.
- q: Retention varies with route scarcity, fleet availability, cargo specialization, and customer concentration.
- d5: The USACE fast facts mix project tonnage and broader system statements and do not provide a five-year forecast.
- d5: USDA grain is only one commodity family and 2025 growth may reverse with crops, exports, or river conditions.
- d5: Employment is an imperfect demand proxy because productivity and minimum crewing can change independently of tonnage.
- o: The evidence establishes current legal and operational accountability rather than a measured future quantity share.
- o: Remote operations could relocate work while retaining an accountable carrier.
- o: Modal substitution and commodity-volume loss are assigned to d5 rather than counted again here.

## Sources
- **S1** — [NAICS Sector 48 Definitions: 483211 Inland Water Freight Transportation](https://www.census.gov/naics/resources/archives/files/sec48.pdf) (accessed 2026-07-22): Defines 483211 as cargo transportation on lakes, rivers, or intracoastal waterways outside the Great Lakes System and distinguishes coastal and deep-sea freight.
- **S2** — [Water Transportation - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics3_483000.htm) (accessed 2026-07-22): Reports the NAICS 483 occupation mix, including 18.84% office and administrative support employment and detailed billing, bookkeeping, customer-service, freight-agent, dispatcher, and clerk roles.
- **S3** — [Kirby Corporation 2025 Annual Report](https://www.sec.gov/Archives/edgar/data/56047/000119312526097112/kex_ars_2025.pdf) (accessed 2026-07-22): Describes inland tank-barge ownership structure, contract and spot mix, term lengths, time charters, labor and fuel escalators, utilization, commodity demand drivers, vessel regulation, and customer relationships.
- **S4** — [USACE Inland Navigation 2022 National Report: Value to the Nation Fast Facts](https://usace.contentdm.oclc.org/digital/api/collection/p16021coll2/id/15125/download) (accessed 2026-07-22): Reports inland-navigation tonnage by commodity, 397.2 million tons of estimated project tonnage, over 500 million system tons annually, and the system's cost advantage versus rail.
- **S5** — [USDA Grain Transportation Report: Review of 2025 Barged Grain Movements and Rates](https://www.ams.usda.gov/sites/default/files/media/GTR02192026.pdf) (accessed 2026-07-22): Reports 2025 Mississippi River System grain-barge volume 11% above 2024, strong corn exports, divergent soybean and wheat movements, and disruptions from water, ice, draft, and tow-size restrictions.
- **S6** — [Coast Guard: Autonomous Ships and Efforts to Regulate Them](https://www.gao.gov/products/gao-24-107059) (accessed 2026-07-22): Finds current commercial autonomous-ship uses are narrow and generally retain human control, with safety, cyber, legal, and statutory minimum-crewing constraints in US waters.
- **S7** — [US Coast Guard: Towing Vessel Credentials, Documents and Records](https://www.dco.uscg.mil/Our-Organization/Assistant-Commandant-for-Prevention-Policy-CG-5P/Traveling-Inspector-Staff-CG-5P-TI/Towing-Vessel-National-Center-of-Expertise/TugSafe/GGCredDocsRecs/) (accessed 2026-07-22): States owner, managing-operator, and master responsibilities for safe manning and watchkeeping and requires the credentialed crew complement specified by a towing vessel's certificate of inspection.
- **S8** — [2023 National State of Owner Readiness Report](https://exit-planning-institute.org/hubfs/Member%20Center%20Resources/2023%20National%20State%20of%20Owner%20Readiness%20Report.pdf) (accessed 2026-07-22): Reports that 49% of 1,162 surveyed US business owners wanted to exit within five years and that 70% preferred an internal transition, cross-industry intent evidence rather than completed transfers.
- **S9** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 Annual Business Survey using 2018 data.
- **S10** — [Water Transportation Workers: Occupational Outlook Handbook](https://www.bls.gov/ooh/transportation-and-material-moving/water-transportation-occupations.htm) (accessed 2026-07-22): Projects water-transportation-worker employment to grow 1% from 2024 to 2034 and describes vessel-operation, maintenance, credentialing, and replacement-opening needs.
