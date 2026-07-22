# 483114 — Coastal and Great Lakes Passenger Transportation

*v5.1 Stage 1 research memo. Run `483114-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.53 · L 2.71 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High labor intensity and passenger-facing administrative work create implementable AI opportunity while safety rules preserve the operator role.
**Weakness:** Route-level demand, fare regulation, public funding, and transferability vary so widely that national proxies offer limited target-specific confidence.

## Business-model lens
- Included: US lower-middle-market firms providing recurring or repeat place-to-place passenger ferry, coastal passenger, Great Lakes passenger, and crewed passenger-vessel charter services to travelers, employers, institutions, or public agencies.
- Excluded: Foreign-port deep-sea passenger transport, inland passenger transport outside the Great Lakes System, scenic round-trip sightseeing, dinner and excursion cruises, floating casinos, public authorities that are not transferable firms, captive internal fleets, dormant vessel shells, and non-control financing vehicles.
- Customer and revenue model: Operators earn passenger and vehicle ticket revenue, charter revenue, and public or private contract payments; routes range from market-priced private services to regulated-fare or subsidized public-service concessions, with the operator supplying vessels, licensed crews, safety compliance, reservations, terminals or terminal interfaces, and accountable transport.
- Deviation from default lens: none

## Executive view
Coastal and Great Lakes passenger transport is labor-intensive and presents a meaningful AI opportunity in reservations, customer care, disruption handling, crew scheduling, finance, and compliance documentation. The licensed onboard and terminal safety core remains operator-dependent. Value retention is mixed because private ticket routes can keep savings initially, while regulated fares, subsidies, and public contract renewals invite sharing.

## How AI changes the work
AI can answer routine passenger questions, process changes and refunds, draft disruption notices, forecast contact demand, assist crew and maintenance scheduling, reconcile ticket revenue, and prepare safety records. Human review is essential for accessibility cases, irregular operations, security, loading, navigation, maintenance, and emergency decisions. Autonomous vessels are not a five-year substitute for the accountable passenger carrier.

## Value capture
Ticket-heavy private routes can retain back-office savings until competition or fare decisions reset economics. Public concessions, regulated fares, and subsidized services are more likely to share benefits through rebids, budget scrutiny, or service commitments. Operators that convert savings into reliability, frequency, and capacity should retain more than those offering a commodity crossing with transparent costs.

## Firm availability
The 36-firm LMM count is modeled rather than a verified target universe. The broader ferry sector contains private and public operators, private and public vessels, and varied terminal arrangements; public authorities are not transferable firms, and route or terminal rights can be harder to transfer than vessels. Broad owner demographics indicate succession pressure, but industry-specific completed-deal evidence is absent.

## Demand durability
Demand is durable on island lifeline and constrained water-crossing routes but uncertain on commuter and discretionary travel routes. National ferry service supply has recovered and expanded, yet survey coverage changes prevent a clean ridership trend. Telework, tourism cycles, weather, vessel reliability, public subsidies, congestion, and new routes can move outcomes in opposite directions.

## Risks and uncertainty
The occupation evidence is broader than passenger transport, transfer evidence is cross-industry, and revenue data are old and include public and inland ferries. Safety incidents, vessel age, dry-dock capital, terminal dependence, regulated fares, labor relations, cyber failures, subsidy changes, and seasonal concentration can overwhelm workflow savings. A route without durable access rights or recurring demand can be a poor acquisition despite attractive labor economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4972 | — | OBSERVED | — |
| n | — | 36 | — | ESTIMATE | — |
| a | 0.16 | 0.28 | 0.4 | ESTIMATE | S2, S7 |
| rho | 0.42 | 0.63 | 0.8 | ESTIMATE | S6, S7 |
| e | 0.48 | 0.68 | 0.84 | PROXY | S1, S4 |
| s5 | 0.08 | 0.18 | 0.3 | PROXY | S8, S9 |
| q | 0.32 | 0.5 | 0.69 | PROXY | S4 |
| d5 | 0.85 | 1.02 | 1.18 | PROXY | S3, S4, S5 |
| o | 0.91 | 0.97 | 0.995 | PROXY | S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.34 | 3.51 | 6.36 | ESTIMATE |
| F | 1.40 | 2.71 | 3.72 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | PROXY |
| D | 7.74 | 9.89 | 10.00 | PROXY |

## Caveats
- a: The BLS occupation table covers all NAICS 483 water transportation rather than 483114 and therefore mixes cargo, inland, and passenger operations.
- a: Employment shares are not wage-weighted task shares, and customer-service employment may be concentrated in larger passenger operators.
- a: The estimate excludes tasks already automated through online ticketing, kiosks, and standard dispatch software.
- rho: No source measures five-year AI implementation for LMM coastal passenger firms.
- rho: Peak-season exceptions and safety incidents may require more human staffing than ordinary-day pilots imply.
- rho: The estimate applies only to the opportunity counted in a, not to total labor.
- e: The provided LMM firm count is modeled from receipts and a margin bridge rather than observed EBITDA or a target list.
- e: The ferry census does not map exactly to NAICS 483114 and its ownership evidence is from 2015 operations.
- e: NAICS is assigned at establishment level while eligibility is a firm-level control-transfer concept.
- s5: Neither source isolates passenger transportation, maritime firms, LMM EBITDA, or completed qualifying control transfers.
- s5: The Census statistic uses 2018 data and responding employer-business owners only.
- s5: An intended exit can become a closure or internal succession and therefore not qualify.
- q: The funding and fare-regulation evidence is from 2015 and includes inland and public ferry operations outside the frozen lens.
- q: The source measures revenue structure, not contractual treatment of AI savings.
- q: Retention will vary sharply between private ticket routes, regulated utilities, and cost-reimbursed public concessions.
- d5: NCFO explicitly cautions against comparing census years because respondent populations and imputation differ.
- d5: FTA capacity-equivalent service miles measure supplied service, not passenger demand, and emphasize transit reporters.
- d5: The national range masks severe divergence between commuter, island, vehicle, and tourism-dependent routes.
- o: The evidence establishes current legal and safety requirements rather than a measured future quantity share.
- o: Some functions may migrate to remote operations centers while an accountable operator remains.
- o: Modal substitution and route closure are assigned to d5, not counted again here.

## Sources
- **S1** — [NAICS Sector 48 Definitions: 483114 Coastal and Great Lakes Passenger Transportation](https://www.census.gov/naics/resources/archives/files/sec48.pdf) (accessed 2026-07-22): Defines 483114 as passenger transportation in coastal waters, the Great Lakes System, or deep seas between US domestic ports, and distinguishes inland and scenic services.
- **S2** — [Water Transportation - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics3_483000.htm) (accessed 2026-07-22): Reports the NAICS 483 occupation mix, including 18.84% office and administrative support employment and detailed customer-service, ticket-agent, dispatcher, bookkeeping, and clerk roles.
- **S3** — [BTS Releases Ferry New Data](https://www.bts.gov/newsroom/bts-releases-ferry-new-data) (accessed 2026-07-22): Reports 2024 NCFO data from 165 of 260 known US ferry operators, including 723 vessels, 897 route segments, and 105.8 million transported passengers.
- **S4** — [2016 Highlights of Ferry Operations in the United States](https://www.bts.gov/surveys/national-census-ferry-operators-ncfo/2016-highlights-ferry-operations-united-states) (accessed 2026-07-22): Reports private/public operator and vessel structures, ticket and public funding shares, fare regulation, ferry use cases, vessel characteristics, scope limitations, and cautions against cross-census comparisons.
- **S5** — [2024 National Transit Summaries and Trends](https://www.transit.dot.gov/sites/fta.dot.gov/files/2026-04/2024%20National%20Transit%20Summaries%20and%20Trends_1.2.pdf) (accessed 2026-07-22): Reports ferryboat capacity-equivalent vehicle revenue miles of 60 million in 2019 and 64 million in 2024, with post-pandemic service recovery context.
- **S6** — [Coast Guard: Autonomous Ships and Efforts to Regulate Them](https://www.gao.gov/products/gao-24-107059) (accessed 2026-07-22): Finds current commercial autonomous-ship uses are narrow and generally retain human control, with safety, cyber, legal, and statutory minimum-crewing constraints in US waters.
- **S7** — [US Coast Guard National Maritime Center: Charter Boat Captain](https://www.dco.uscg.mil/nmc/charter_boat_captain/) (accessed 2026-07-22): Describes credentialed master endorsements and certificates of inspection for small passenger vessels, including ferries carrying more than six passengers in near-coastal and Great Lakes service.
- **S8** — [2023 National State of Owner Readiness Report](https://exit-planning-institute.org/hubfs/Member%20Center%20Resources/2023%20National%20State%20of%20Owner%20Readiness%20Report.pdf) (accessed 2026-07-22): Reports that 49% of 1,162 surveyed US business owners wanted to exit within five years, a cross-industry intent proxy rather than completed-transfer evidence.
- **S9** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 Annual Business Survey using 2018 data.
