# 713990 — All Other Amusement and Recreation Industries

*v5.1 Stage 1 research memo. Run `713990-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.02 · L 2.64 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat booking, admission, event-sales, waiver, marketing, scheduling, and reporting workflows can be standardized across a fragmented set of physical recreation venues.
**Weakness:** The residual code's extreme business-model heterogeneity makes the frozen labor and firm-count inputs—and most public evidence—poor matches for the narrowed operating lens.

## Business-model lens
- Included: US operators of fixed-site participatory recreation venues in the roughly $1-10M normalized EBITDA band, including miniature golf and driving ranges, archery and shooting ranges, billiard parlors, escape rooms, go-kart or similar single-attraction venues, and comparable facilities selling repeat admission, reservations, memberships, parties, or events to external customers.
- Excluded: Outdoor adventure and guide operators, riding stables, recreational day camps, sports teams and leagues without facilities, boating and social clubs, mobile amusement-device and ride concession operators, fireworks services, captive amenities, non-operating property shells, and non-control financing vehicles.
- Customer and revenue model: Direct consumer and group-event revenue from admissions, timed reservations, activity fees, memberships or passes, parties, food and beverage, and ancillary merchandise; repeat use is common but most revenue is not protected by long-term contracts.
- Deviation from default lens: NAICS 713990 is unusually heterogeneous, combining fixed-site venues, outdoor guides, day camps, teams and leagues, clubs, riding stables, and mobile concession operators. The lens is narrowed to fixed-site participatory recreation venues because their on-site staffing, reservation/admission workflow, safety obligations, direct pricing, and transferable facility operations form a coherent screen; excluded models have materially different labor, seasonality, contract, asset, and transfer dynamics. The narrowing is for coherence, not attractiveness.

## Executive view
The residual NAICS code is too heterogeneous for one coherent operating thesis, so the screen focuses on fixed-site participatory recreation venues. These businesses have repeat admissions, parties, memberships, and events plus a sizable labor base, but their automatable work is primarily the transaction and management layer around a physical attraction. The opportunity is operational standardization across venue subtypes, tempered by weak subtype data and potential mismatch in the code-wide frozen inputs.

## How AI changes the work
AI and conventional automation can handle booking and ticketing, lead response, waiver processing, customer messaging, staff scheduling, promotion creation, purchasing support, forecasting, loyalty offers, and routine performance reporting. Direct attraction supervision, safety intervention, cleaning, maintenance, food preparation, and live exception handling remain human and site-bound. AI is therefore more likely to avoid incremental hiring and widen manager span than to create unattended venues at scale.

## Value capture
Venues set direct admission, reservation, membership, and event prices, so there is little contractual cost pass-through. Savings can be retained through steady pricing, higher conversion, improved throughput, and cross-sell, but local competition, discounting, and customer demand for refreshed attractions will absorb part of the benefit. Visible service degradation would quickly turn labor savings into lower repeat traffic.

## Firm availability
The frozen estimate of 288 LMM firms is code-wide, while only an uncertain share fits the fixed-site venue lens. Adjacent location-based entertainment acquisitions demonstrate strategic appetite, but there is no reliable public transaction census for these subtypes. Family transfers, closures, owner dependence, property-only sales, permits, and mixed-use venues make qualifying firm-level availability substantially lower than generic owner exit intent.

## Demand durability
Broad real recreation-services consumption and sports, fitness, and leisure participation have recently grown, supporting modest aggregate demand growth. Yet these are broad proxies: paid venue visits can lose share to free, outdoor, at-home, or new entertainment formats. Demand is discretionary and concept-specific, so maintaining novelty, safety, reviews, and local relevance is as important as the macro participation trend.

## Risks and uncertainty
The biggest weakness is classification: the residual code mixes fundamentally different businesses, and neither the frozen l nor n is measured for the narrowed venue population. Other gaps include subtype task weights, independent-center technology adoption, private control-transfer data, and inflation-adjusted same-venue demand. Execution risks include legacy system integration, cyber and payment security, waivers and permits, insurance, seasonal peaks, equipment downtime, local competition, and over-automation of hospitality.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3878 | — | OBSERVED | — |
| n | — | 288 | — | ESTIMATE | — |
| a | 0.21 | 0.31 | 0.43 | PROXY | S2, S3 |
| rho | 0.38 | 0.55 | 0.69 | PROXY | S3, S4 |
| e | 0.3 | 0.52 | 0.72 | ESTIMATE | S1 |
| s5 | 0.09 | 0.19 | 0.31 | PROXY | S4, S7 |
| q | 0.55 | 0.7 | 0.83 | ESTIMATE | S3, S4 |
| d5 | 0.88 | 1.08 | 1.25 | PROXY | S5, S6, S8 |
| o | 0.91 | 0.96 | 0.99 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.24 | 2.64 | 4.60 | PROXY |
| F | 3.49 | 5.44 | 6.72 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.01 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No occupation table specific to the narrowed fixed-site 713990 lens was found.
- a: The frozen l=0.3878 is code-wide, uses 2024 wages over 2022 receipts, and is harmonized from a QCEW/SUSB construction; it may not describe the narrowed venue mix.
- a: Owner labor and seasonal staffing may be poorly represented in employer occupation data.
- rho: Vendor claims cover hospitality and leisure broadly and do not isolate AI from conventional workflow software.
- rho: Lucky Strike's scale, brand, and centralized systems are not representative of most LMM venues.
- rho: Already automated work is outside a by definition and must not be counted as new implementation.
- e: The Census examples establish heterogeneity but provide no subtype shares for the frozen EBITDA band.
- e: The frozen n=288 is a margin-bridged code-wide estimate and may be materially misleading after lens narrowing.
- e: Mixed venues and multi-activity firms may not admit a clean primary-activity classification.
- s5: The SBA survey is old, cross-industry, and measures expected exit rather than completed control transfer.
- s5: Lucky Strike's acquisitions are not identified by seller size and include venue categories outside the narrowed lens.
- s5: Asset sales of attractions or real estate do not necessarily transfer a qualifying operating firm.
- q: The venue set spans different local competitive intensity and membership dependence.
- q: Adjacent large-operator disclosures may overstate pricing power and cross-sell capability.
- q: This estimate concerns retention after implementation, not demand growth or implementation feasibility.
- d5: BEA recreation services include many activities outside NAICS 713990 and outside the narrowed lens.
- d5: SFIA participation counts activities rather than paid venue visits or service quantity.
- d5: The Census 71399 series is nominal, ends in 2022 on the fetched page, and includes excluded business models.
- o: Safety and staffing requirements vary sharply across shooting ranges, go-karts, mini-golf, billiards, and escape rooms.
- o: Remote monitoring, smart access, digital waivers, and automated scoring may reduce on-site labor without eliminating accountable operation.
- o: The estimate applies only to the narrowed fixed-site service basket, not excluded guide, camp, team, or concession models.

## Sources
- **S1** — [2022 NAICS Definition: 713990 All Other Amusement and Recreation Industries](https://www.census.gov/naics/?details=713990&input=713990&year=2022) (accessed 2026-07-22): Defines the residual industry and lists fixed-site venues, outdoor adventure operations, day camps, clubs, teams, guides, riding stables, and mobile concession operators; supports the heterogeneity finding, lens narrowing, eligibility uncertainty, and physical operator requirement.
- **S2** — [May 2023 Occupational Employment and Wage Estimates: NAICS 713000](https://www.bls.gov/oes/2023/may/naics3_713000.htm) (accessed 2026-07-22): Reports 1,809,830 workers across amusement, gambling, and recreation, including 13.78% amusement and recreation attendants and 5.37% management occupations, with detailed food-service and supervisory roles; supports the broad occupation-mix proxy for a.
- **S3** — [Agilysys, Inc. Form 10-K for fiscal year ended March 31, 2024](https://www.sec.gov/Archives/edgar/data/78749/000095017024063222/agys-20240331.htm) (accessed 2026-07-22): Describes deployed hospitality and leisure tools for booking, activity scheduling, POS, kiosks, mobile ordering and payment, reporting, inventory, loyalty, and AI-powered checkout, and states that self-service reduces on-site labor; supports a, rho, q, and operator-workflow judgments.
- **S4** — [Lucky Strike Entertainment Corporation Form 10-K for fiscal year ended June 29, 2025](https://www.sec.gov/Archives/edgar/data/1840572/000184057225000012/bowl-20250629.htm) (accessed 2026-07-22): Discloses self-service kiosks, robotic process automation, online reservations and event sales, data-driven offerings, leaner staffing, and 75 location-based entertainment venue acquisitions since fiscal 2022; supports implementation and transfer proxies.
- **S5** — [Real personal consumption expenditures: Recreation services (chain-type quantity index)](https://fred.stlouisfed.org/series/DRCARA3A086NBEA) (accessed 2026-07-22): BEA quantity index rose from 94.638 in 2021 to 105.472 in 2022, 109.533 in 2023, 111.069 in 2024, and 112.879 in 2025; supports the broad real-demand proxy for d5.
- **S6** — [SFIA 2026 Topline Participation Report press release](https://sfia.org/resource_categories/press-release/) (accessed 2026-07-22): Reports 250 million Americans participated in at least one of 126 sport, fitness, or leisure activities in 2025, total participation grew 1.2% year over year, and core participation reached 158.8 million and grew 1.3%; supports the participation bridge for d5.
- **S7** — [5 Reasons to Hire Your Child](https://www.sba.gov/blog/5-reasons-hire-your-child) (accessed 2026-07-22): SBA-hosted article cites a survey in which 29% of business owners expected to exit within five years, 54% within ten years, and 37% wanted a family transfer; supports the cross-industry exit-intent proxy for s5.
- **S8** — [Total Revenue for All Other Amusement and Recreation Industries, Taxable Employer Firms](https://fred.stlouisfed.org/series/REVEF71399TAXABL) (accessed 2026-07-22): Census Service Annual Survey series reports nominal taxable-employer revenue of $10.5 billion in 2018, $11.417 billion in 2019, $8.852 billion in 2020, $14.156 billion in 2021, and $17.988 billion in 2022; supports broad code-level demand context with explicit inflation and scope caveats.
