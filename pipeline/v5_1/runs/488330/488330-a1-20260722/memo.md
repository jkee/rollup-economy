# 488330 — Navigational Services to Shipping

*v5.1 Stage 1 research memo. Run `488330-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.71 · L 2.51 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable compulsory and physical harbor work paired with automatable dispatch, documentation, and coordination overhead.
**Weakness:** Six-digit evidence is sparse, and regulated or frequently rebid pricing may transfer a material share of productivity savings to shippers.

## Business-model lens
- Included: Recurring outsourced harbor tug and ship-assist work, docking and undocking, compulsory or contracted pilotage, and externally sold vessel-traffic reporting and navigation support performed by lower-middle-market firms.
- Excluded: One-off marine salvage, captive port or carrier navigation units, public vessel-traffic services, shells, non-control vehicles, and firms outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: Shipowners, operators, agents, terminals, and ports buy per-movement, tariff-based, hourly, or contracted navigation and harbor-assist services; repeat traffic and regulatory pilotage requirements create recurring relationships, while rates may be regulated or periodically reset.
- Deviation from default lens: The code mixes repeat harbor-assist and pilotage businesses with episodic marine salvage and public or captive traffic services. The lens is narrowed to recurring externally sold navigation services so one operating model remains coherent.

## Executive view
Recurring harbor tug, docking, and pilotage firms combine durable, safety-critical demand with a real but bounded automation opportunity. AI is more credible as an operating copilot for dispatch, documents, billing, maintenance planning, and voyage information than as a substitute for licensed pilots or tug crews within five years. The code is heterogeneous, and episodic salvage or public and captive traffic services should not be treated as the same acquisition population.

## How AI changes the work
Near-term value comes from automating port-call intake, schedule coordination, customer communications, billing reconciliation, compliance records, weather and chart briefings, incident-document drafting, and maintenance triage. Bridge teams can receive better decision support, but direct docking, tug handling, situational monitoring, inspections, and emergency decisions remain physical and accountable work. Fragmented port systems and sparse error-tolerant training data make deployment discipline important.

## Value capture
Avoided administrative hiring and better asset and crew utilization can be retained under fixed or negotiated contracts until renewal. Regulated pilotage is less attractive for retention because rate setting can explicitly true up expenses and compensation, while large shipowners and terminals can demand savings through rebids. Durable capture therefore depends on proprietary workflow integration, service quality, response time, and asset utilization rather than a generic AI tool alone.

## Firm availability
The modeled LMM population likely contains independent tug and docking operators as well as pilotage and navigation specialists, but transferability is uneven. Vessel fleets and recurring customer ties support control sales, while licenses, association governance, concessions, and owner-specific local knowledge can impede them. Succession pressure exists in small business generally, yet a verified 488330 owner and transaction census is missing.

## Demand durability
Official federal planning expects modest waterborne freight growth through 2030. Port calls, vessel size, drafts, trade lanes, commodity cycles, and local pilotage rules matter more to service jobs than tonnage alone. Physical ship-assist and compulsory pilotage should remain operator-required through the horizon; traffic reporting and routine advice face more software and carrier self-service risk.

## Risks and uncertainty
The largest evidence weakness is the absence of six-digit occupation, contract, owner-age, and transaction data. The four-digit employment proxy contains cargo handling and port operations that differ materially from this lens. Other risks include customer concentration, regulated pricing, vessel and fuel capital intensity, labor and licensing scarcity, cybersecurity, port-specific concessions, trade volatility, and the possibility that productivity gains are passed through faster than expected.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4155 | — | OBSERVED | — |
| n | — | 129 | — | ESTIMATE | — |
| a | 0.18 | 0.29 | 0.42 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S3, S4, S5, S6 |
| e | 0.5 | 0.68 | 0.82 | ESTIMATE | S1, S7 |
| s5 | 0.13 | 0.24 | 0.38 | PROXY | S8, S9 |
| q | 0.38 | 0.55 | 0.72 | PROXY | S10 |
| d5 | 0.95 | 1.04 | 1.12 | PROXY | S4, S11, S12 |
| o | 0.78 | 0.9 | 0.97 | PROXY | S5, S6, S13, S14 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.05 | 2.51 | 4.75 | ESTIMATE |
| F | 3.60 | 4.98 | 5.98 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | PROXY |
| D | 7.41 | 9.36 | 10.00 | PROXY |

## Caveats
- a: OEWS publishes the relevant occupation mix only at four-digit NAICS 488300 and excludes self-employed workers.
- a: The estimate is wage-weighted judgment from occupational groups, not a measured AI task-exposure share.
- a: Marine salvage and cargo-handling occupations in the parent industry distort the mix in opposing directions.
- rho: No industry-wide survey measures five-year AI implementation in 488330.
- rho: The IMO code concerns autonomous cargo ships rather than harbor-service firms, but it is relevant to safety and accountability constraints.
- rho: Small firms may lack standardized digital data and integration staff.
- e: The 129-firm denominator is a frozen modeled estimate rather than an observed roster.
- e: Pilot associations and public-private entities may have ownership or governance structures incompatible with control acquisition.
- e: NAICS assignment may follow an establishment's primary activity even when a firm has substantial towing or transportation revenue outside the code.
- s5: Neither source measures 488330 or the $1-10M EBITDA band.
- s5: Transactions may be asset sales without a transferable operating organization, and internal succession does not always constitute a qualifying control transfer.
- s5: Voluntary broker reporting misses private strategic deals and has a smaller-company bias.
- q: Great Lakes pilotage is a small, unusually regulated subset of national navigational services.
- q: Private harbor-tug contracts may retain more savings until rebid, while concentrated customers may capture them faster.
- q: This is the retained share of implemented gross benefit and excludes demand and implementation effects.
- d5: Waterborne tonnage is not proportional to port calls because vessel size and load factors change.
- d5: The USDOT forecast includes inland and coastal freight that may not require outsourced harbor services.
- d5: Trade policy, commodity cycles, climate-related water levels, and port disruptions create substantial forecast risk.
- o: Legal requirements could change after trials or waivers, though broad mandatory autonomous rules fall outside most of the horizon.
- o: A responsible master aboard or ashore does not necessarily imply use of a separate outsourced navigation firm.
- o: Marine vessel traffic reporting is more susceptible to software substitution than physical pilotage or tug assist.

## Sources
- **S1** — [2022 NAICS Definition: 488330 Navigational Services to Shipping](https://www.census.gov/naics/?details=4883&input=4883&year=2022) (accessed 2026-07-22): Official industry scope: navigational services, marine salvage, docking and undocking, pilotage, vessel-traffic reporting, and harbor tug services.
- **S2** — [May 2023 OEWS: NAICS 488300 Support Activities for Water Transportation](https://www.bls.gov/oes/2023/may/naics4_488300.htm) (accessed 2026-07-22): Parent-industry occupation employment and wage mix, including management, office support, dispatchers, water-transportation workers, maintenance, and material-moving occupations.
- **S3** — [O*NET: Captains, Mates, and Pilots of Water Vessels](https://www.onetonline.org/link/summary/53-5021.00?redir=53-5021.02) (accessed 2026-07-22): Task mix includes steering, docking, monitoring, inspection, safety decisions, radio communication, records, charts, crew coordination, and equipment operation.
- **S4** — [BLS Occupational Outlook Handbook: Water Transportation Workers](https://www.bls.gov/ooh/transportation-and-material-moving/water-transportation-occupations.htm) (accessed 2026-07-22): Work duties, Coast Guard training and credential requirements, physical skill requirements, occupation mix, commodity sensitivity, and 1% employment growth forecast for 2024-2034.
- **S5** — [IMO adopts first global Code for autonomous ships](https://www.imo.org/en/mediacentre/pressbriefings/pages/imo-adopts-mass-code.aspx) (accessed 2026-07-22): The 2026 MASS Code is non-mandatory, emphasizes risk, cybersecurity and human oversight, retains master responsibility, and anticipates mandatory entry into force in 2032.
- **S6** — [IMO FAQ: Autonomous shipping](https://www.imo.org/en/mediacentre/hottopics/pages/autonomous-shipping.aspx) (accessed 2026-07-22): Scope and non-mandatory status of the MASS Code, continued human oversight and master responsibility, and experience-building before mandatory rules.
- **S7** — [Census Bureau Profile: 488330 Navigational Services to Shipping](https://data.census.gov/profile/488330_-_Navigational_Services_to_Shipping?codeset=naics~488330&g=010XX00US) (accessed 2026-07-22): Six-digit industry scope and 1,065 employer establishments in 2023, contextualizing the modeled LMM subset.
- **S8** — [SBA: 5 Challenges for Family-Owned Businesses](https://www.sba.gov/blog/5-challenges-family-owned-businesses) (accessed 2026-07-22): Succession proxy: 47% of owners expecting to retire within five years reportedly lacked a successor; family-business survival statistics.
- **S9** — [BizBuySell Insight Report: Q1 2026](https://www.bizbuysell.com/insight-report/) (accessed 2026-07-22): Small-business transfer-market proxy: approximately 50,000 listed or recently sold businesses in the dataset and 2,345 reported Q1 2026 closed transactions; voluntary broker-reporting limitation.
- **S10** — [Coast Guard Great Lakes Pilotage Rates—2026 Annual Review Final Rule](https://public-inspection.federalregister.gov/2026-03054.pdf) (accessed 2026-07-22): Regulated pilotage pricing: rates are set to recover necessary and reasonable expenses, reviewed annually, and projected 2026 revenue requirement was $40.451 million.
- **S11** — [2026 National Freight Strategic Plan](https://www.transportation.gov/media/4496) (accessed 2026-07-22): Forecast waterborne freight tonnage rises from 819.772 million tons in 2025 to 853.960 million in 2030, a 4% increase, and describes growth as modest.
- **S12** — [USACE Waterborne Commerce Statistics Center](https://www.iwr.usace.army.mil/About/Technical-Centers/WCSC-Waterborne-Commerce-Statistics-Center/WCSC-Waterborne-Commerce/) (accessed 2026-07-22): Official vessel-trip and cargo data coverage, including tugboat moves, cargo, and port and waterway statistics, and the appropriate diligence dataset for service demand.
- **S13** — [46 U.S.C. Chapter 85—Pilots](https://uscode.house.gov/view.xhtml?edition=prelim&path=%2Fprelim%40title46%2Fsubtitle2%2FpartF%2Fchapter85) (accessed 2026-07-22): Federal statutory framework preserving state regulation of pilots in U.S. bays, rivers, harbors, and ports and federal pilotage requirements.
- **S14** — [46 U.S. Code § 8502—Federal pilots required](https://www.law.cornell.edu/uscode/text/46/8502) (accessed 2026-07-22): Covered coastwise seagoing vessels underway in specified waters must be under the direction and control of a licensed pilot; fees are bounded by customary or established state rates.
