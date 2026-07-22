# 483113 — Coastal and Great Lakes Freight Transportation

*v5.1 Stage 1 research memo. Run `483113-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.04 · L 0.44 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Regulated operator accountability and term-charter revenue make shore-side productivity improvements implementable without threatening the core service.
**Weakness:** The addressable AI task share is modest and the evidence for eligible, transferable LMM firms is indirect.

## Business-model lens
- Included: US lower-middle-market operators providing recurring or repeat outsourced cargo transportation in coastal waters, on the Great Lakes System, or between US domestic ports, including crewed coastal and Great Lakes barge and vessel charter services.
- Excluded: Deep-sea foreign freight, inland freight outside the Great Lakes System, harbor tug services, passenger operations, captive shipper fleets, dormant vessel-owning shells, non-control financing vehicles, and firms without transferable operating organizations.
- Customer and revenue model: Business and government shippers buy voyages, contracts of affreightment, or time charters, with a mix of annual or multi-year term contracts and market-priced spot movements; the carrier supplies vessels, qualified crews, compliance, and accountable transport execution.
- Deviation from default lens: none

## Executive view
Coastal and Great Lakes freight combines a modest shore-side AI opportunity with unusually durable need for regulated, accountable vessel operators. The opportunity is concentrated in customer service, voyage administration, dispatch support, billing, documentation, compliance preparation, and maintenance planning rather than crew elimination. Contracting can preserve some early savings, but annual renewals and sophisticated shippers should reclaim a meaningful share over five years.

## How AI changes the work
AI can structure shipping instructions, draft quotations and voyage documents, reconcile bills, answer routine status questions, summarize weather and maintenance records, flag compliance exceptions, and assist schedulers. Human approval remains important, and licensed masters, engineers, deck crews, and managing operators retain responsibility for navigation, cargo, emergency response, and safe manning. Autonomous-vessel adoption is unlikely to remove that operating core within five years.

## Value capture
Time charters and term contracts sell vessel availability and service outcomes, so administrative productivity need not be passed through immediately. However, many contracts renew annually, spot moves reprice at market, and established fuel and labor escalators show customers already negotiate cost sharing. Retention depends on translating savings into reliability, capacity, and avoided hires before procurement cycles reset rates.

## Firm availability
The industry definition fits outsourced recurring transport, but the 85-firm LMM count is modeled and not a verified target list. Captive fleets, holding shells, weakly compliant operators, single-customer assets, and firms with citizenship or endorsement transfer issues reduce eligibility. Broad US owner-age and exit-intent data suggest succession supply, but closed maritime control-transfer evidence is missing.

## Demand durability
Five-year real quantity is likely roughly stable, with upside from general freight growth and constrained vessel supply but downside from commodity cycles, pipeline substitution, decarbonization, and modal shifts. Demand varies sharply across petrochemicals, refined products, coal, fertilizer, grain, and Great Lakes bulk trades. For freight that remains on the water, regulatory crewing and safety accountability make full software substitution unlikely.

## Risks and uncertainty
The largest uncertainties are the absence of a 483113-specific task study, an unverified LMM target roster, cross-industry succession proxies, and reliance on one large operator for contract evidence. Safety incidents, cyber failures, customer concentration, vessel age, dry-dock needs, environmental rules, commodity exposure, and Jones Act constraints can dominate administrative savings. A weak route or an undercapitalized fleet can make the opportunity unattractive even when AI workflows perform well.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0913 | — | OBSERVED | — |
| n | — | 85 | — | ESTIMATE | — |
| a | 0.12 | 0.22 | 0.34 | ESTIMATE | S2, S3 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S3, S9 |
| e | 0.45 | 0.65 | 0.82 | ESTIMATE | S1, S4, S10 |
| s5 | 0.1 | 0.2 | 0.32 | PROXY | S5, S6 |
| q | 0.36 | 0.55 | 0.72 | PROXY | S4 |
| d5 | 0.92 | 1.01 | 1.12 | PROXY | S4, S7, S8 |
| o | 0.88 | 0.96 | 0.99 | PROXY | S3, S9, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.15 | 0.44 | 0.89 | ESTIMATE |
| F | 2.53 | 4.00 | 5.06 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | PROXY |
| D | 8.10 | 9.70 | 10.00 | PROXY |

## Caveats
- a: The BLS occupation mix covers NAICS 483000 rather than 483113 and includes passenger and inland operators.
- a: Employment shares are not wage shares or task shares, and no source directly measures current generative-AI exposure in coastal freight firms.
- a: The estimate excludes already-automated work and does not assume autonomous vessels replace licensed crews within five years.
- rho: Implementation evidence is not specific to generative-AI deployments at LMM coastal freight operators.
- rho: Cybersecurity and safety-management controls may slow adoption even for shore-side workflows.
- rho: The estimate applies only to the opportunity counted in a, not to total industry labor.
- e: The provided firm count is an estimate derived from receipts and margins, not an observed roster.
- e: NAICS is assigned at establishment level while eligibility is a firm-level control-transfer concept.
- e: Jones Act citizenship and vessel requirements can restrict buyer structures and post-close operating flexibility.
- s5: Neither source isolates transportation, maritime firms, the LMM EBITDA band, or completed control transfers.
- s5: The Census age statistic uses 2018 data and covers responding owners rather than all owners.
- s5: Exit intent is not a transaction, and an exit can be a closure or internal succession that does not qualify.
- q: One public operator may not represent LMM coastal, Great Lakes, dry-bulk, or general-cargo contracting.
- q: The filing reports fuel and other price mechanisms, not AI-related savings pass-through.
- q: Customer concentration and competitive tendering can make retention vary widely by route and vessel class.
- d5: Employment is an imperfect quantity proxy because productivity, utilization, and crew rules can change independently of freight demand.
- d5: The BTS forecast is all-mode US freight and its horizon is much longer than five years.
- d5: Commodity and route mix can overwhelm aggregate trends, especially for coal and petroleum movements.
- o: The proxy addresses legal and operational accountability more directly than customer self-service or modal substitution.
- o: Some operator functions could migrate to remote operations centers without eliminating an accountable operator.
- o: The estimate conditions on year-five service quantity; demand loss and mode substitution belong in d5.

## Sources
- **S1** — [2022 NAICS Definition: 483113 Coastal and Great Lakes Freight Transportation](https://www.census.gov/naics/?details=483113&input=483113&year=2022) (accessed 2026-07-22): Defines the industry as cargo transportation in coastal waters, the Great Lakes System, or deep seas between US domestic ports, and includes coastal and Great Lakes barge transport and crewed chartering.
- **S2** — [Water Transportation - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics3_483000.htm) (accessed 2026-07-22): Reports the NAICS 483 occupation mix, including 18.84% office and administrative support employment, 5.72% business and financial operations, and detailed customer-service, freight-agent, dispatcher, bookkeeping, and clerk employment.
- **S3** — [Coast Guard: Autonomous Ships and Efforts to Regulate Them](https://www.gao.gov/products/gao-24-107059) (accessed 2026-07-22): Finds current commercial autonomous-ship uses are narrow and generally retain human control; describes safety, cyber, legal, and statutory minimum-crewing constraints in US waters.
- **S4** — [Kirby Corporation 2025 Annual Report](https://www.sec.gov/Archives/edgar/data/56047/000119312526097112/kex_ars_2025.pdf) (accessed 2026-07-22): Reports coastal contract mix, time charters, renewal terms, fuel escalators, utilization, commodity demand drivers, industry ownership mix, regulation, competition, and coastal operating conditions.
- **S5** — [2023 National State of Owner Readiness Report](https://exit-planning-institute.org/hubfs/Member%20Center%20Resources/2023%20National%20State%20of%20Owner%20Readiness%20Report.pdf) (accessed 2026-07-22): Reports that 49% of 1,162 surveyed US business owners wanted to exit within five years, a cross-industry intent proxy rather than completed-transfer evidence.
- **S6** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 Annual Business Survey using 2018 data.
- **S7** — [Water Transportation Workers: Occupational Outlook Handbook](https://www.bls.gov/ooh/transportation-and-material-moving/water-transportation-occupations.htm) (accessed 2026-07-22): Projects water-transportation-worker employment to grow 1% from 2024 to 2034 and identifies bulk-commodity demand as a key employment driver.
- **S8** — [Freight Activity in the U.S. Expected to Grow Fifty Percent by 2050](https://www.bts.gov/newsroom/freight-activity-us-expected-grow-fifty-percent-2050) (accessed 2026-07-22): Reports FAF5 projections for 50% growth in total US freight tonnage from 2020 to 2050 and notes forecasts vary by mode and economic scenario.
- **S9** — [US Coast Guard: Credentials, Documents and Records](https://www.dco.uscg.mil/Our-Organization/Assistant-Commandant-for-Prevention-Policy-CG-5P/Traveling-Inspector-Staff-CG-5P-TI/Towing-Vessel-National-Center-of-Expertise/TugSafe/GGCredDocsRecs/) (accessed 2026-07-22): States that owners, managing operators, and masters are responsible for safe manning and watchkeeping, and that vessels must carry the credentialed crew complement required by the certificate of inspection.
- **S10** — [MARAD Domestic Shipping: The Jones Act](https://www.maritime.dot.gov/ports/domestic-shipping/domestic-shipping) (accessed 2026-07-22): States that domestic waterborne merchandise transportation requires a US-built, US-owned, Coast Guard coastwise-endorsed vessel, subject to limited statutory waivers.
