# 713290 — Other Gambling Industries

*v5.1 Stage 1 research memo. Run `713290-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.37 · L 0.96 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring host contracts and a legally required licensed operator preserve the service relationship while AI improves monitoring, dispatch, compliance, and support.
**Weakness:** Physical field work and prior machine automation limit labor substitution, while regulation and mature-market demand create wide downside uncertainty.

## Business-model lens
- Included: Lower-middle-market licensed distributed-gaming concession operators that own or control coin-, card-, video-, or slot-gambling devices and repeatedly place, monitor, maintain, repair, and support them in external bars, restaurants, convenience stores, truck stops, fraternal or veterans organizations, and similar host locations.
- Excluded: Bingo halls, card rooms, slot parlors, bookmakers, online gambling sites, lottery control boards and ticket agents, direct-to-consumer gambling operators, captive device operations, manufacturers or distributors without recurring field operations, shells, passive license interests, and firms outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: External licensed host locations receive recurring equipment placement, uptime, compliance, cash-control, reporting, and field-service support. The operator commonly earns a regulated or contracted share of net terminal income under a multi-year location or use agreement rather than billing technicians by the hour.
- Deviation from default lens: NAICS 713290 mixes materially different models: direct gambling facilities, bookmakers and online sites, lottery entities, and third-party gambling-device concession operators. The lens is narrowed to distributed-device concession operators because they are the code's explicit recurring outsourced-service model; combining them with direct wagering businesses would make the primitive estimates incoherent.

## Executive view
Distributed-gaming terminal operators are a genuine recurring outsourced-service business embedded inside a highly heterogeneous gambling code. They place and support regulated machines across networks of external host locations under recurring agreements and revenue shares. AI can improve monitoring, dispatch, records, compliance, account support, and route planning, but the core still requires licensed accountability and physical field service. Eligibility, regulatory transfer friction, and mature-market demand are more uncertain than the operator requirement itself.

## How AI changes the work
The strongest use cases are remote fault triage, predictive maintenance, technician-assist search, work-order generation, parts planning, route optimization, compliance drafting, anomaly detection, location support, and performance analytics. The weak use cases are installing and moving terminals, opening regulated equipment, replacing parts, collecting cash, testing machines, and resolving urgent on-site failures. Central monitoring and ticket-in/ticket-out systems also mean some obvious automation has already occurred.

## Value capture
Because operators commonly earn a share of net terminal income rather than technician-hour fees, internal labor savings can remain with the operator. Illinois's mandatory after-tax profit split makes that especially clear. Capture erodes through location-contract renewal, competitor conversions, service expectations, equipment reinvestment, route-acquisition spending, taxes, and regulatory changes rather than through automatic hourly pass-through.

## Firm availability
The code contains many ineligible direct gambling businesses, but state license lists confirm a substantial population of third-party terminal operators. Public filings show acquisitions of routes and operating companies, supporting transferability. Suitability reviews, board approval, licensed personnel, host contracts, and asset-by-asset route structures complicate control transfers and can separate an economic route purchase from a clean firm acquisition.

## Demand durability
Mature distributed-gaming markets appear stable rather than fast growing. Illinois still has a very large installed base, while Pennsylvania's recent VGT revenue was nearly flat and Accel's mature Illinois location growth was small. New jurisdictions and locations can add demand, but saturation, host closures, tax changes, discretionary-spending pressure, and online gambling can offset it. Service quantity that remains should almost always need a licensed operator.

## Risks and uncertainty
The principal evidence gaps are the eligible share of the 332 dataset-implied firms, a wage-weighted occupation mix for concession operators, national deal-flow and owner-age data, state-by-state contract economics, and same-location real demand. Regulation is both protection and risk: it preserves the operator role but can alter taxes, revenue shares, license eligibility, machine caps, or legal availability. A bad outcome would combine mature-market decline with adverse tax changes and intense competition for host renewals.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1991 | — | OBSERVED | — |
| n | — | 332 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.3 | ESTIMATE | S2, S3, S4, S5, S6 |
| rho | 0.4 | 0.6 | 0.75 | ESTIMATE | S3, S4, S5, S6 |
| e | 0.18 | 0.32 | 0.48 | ESTIMATE | S1, S4, S8 |
| s5 | 0.08 | 0.17 | 0.28 | ESTIMATE | S4, S6, S7 |
| q | 0.55 | 0.72 | 0.85 | ESTIMATE | S5, S6 |
| d5 | 0.85 | 1.02 | 1.2 | PROXY | S4, S6, S8 |
| o | 0.9 | 0.96 | 1 | ESTIMATE | S4, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.38 | 0.96 | 1.79 | ESTIMATE |
| F | 2.82 | 4.74 | 6.15 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.65 | 9.79 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS mix is four-digit NAICS 713200 and is dominated by casino and other gambling roles, not the narrow concession-operator segment.
- a: O*NET combines slot-machine work with vending and amusement-machine service and does not measure wage-weighted AI exposure.
- a: The estimate may overstate opportunity if central monitoring, ticketing, route optimization, and cash controls are already highly automated.
- rho: No source directly measures implementation of AI in LMM distributed-gaming operators.
- rho: Rules and central-system architectures differ by state.
- rho: High implementation in administrative tasks does not eliminate licensed field response or physical repair.
- e: No national source provides establishment or firm counts by the business-model examples inside NAICS 713290.
- e: State license counts are not firm counts and can include operators outside the LMM band or common ownership across jurisdictions.
- e: The dataset n estimate may be distorted by online betting and government-adjacent lottery entities with very different economics.
- s5: Public-company acquisitions are selected examples and may overstate deal activity among all LMM operators.
- s5: Acquisitions of routes, location contracts, or equipment may not transfer control of an entire firm.
- s5: Illinois rules are not nationally representative, and no owner-demographic evidence was found.
- q: Illinois's statutory split is unusually explicit and may not generalize to other states.
- q: The estimate assumes the operator, not the host, employs the affected labor and bears the cost.
- q: Competition may dissipate savings through better equipment, faster service, or location acquisition spending rather than explicit price cuts.
- d5: Net terminal income combines wagering volume, hold, game mix, and nominal prices and is not a direct service-quantity measure.
- d5: Accel is one large operator and its 2024 growth includes acquisitions and entry into Louisiana.
- d5: Pennsylvania is a small truck-stop-only VGT market, while Illinois is unusually large and mature.
- o: Illinois's mandated separation and licensing regime may be stricter than other states.
- o: The estimate concerns continued need for an accountable operator, not the number of employees the operator needs.
- o: Migration of wagering to online products is captured as lost physical demand in d5 rather than again in o.

## Sources
- **S1** — [2022 NAICS Definition: 713290 Other Gambling Industries](https://www.census.gov/naics/?details=713290&input=713290&year=2022) (accessed 2026-07-22): Defines the heterogeneous industry and explicitly includes coin- or card-operated gambling-device concession operators that supply and service equipment in others' facilities, alongside bingo, betting, lottery, card-room, and online gambling activities.
- **S2** — [May 2022 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 713200 Gambling Industries](https://www.bls.gov/oes/2022/may/naics4_713200.htm) (accessed 2026-07-22): Provides the broad gambling-industry occupation mix, including 10,630 installation, maintenance, and repair workers, or 5.27% of employment, plus management, office, sales, protective, and service roles.
- **S3** — [O*NET OnLine: Coin, Vending, and Amusement Machine Servicers and Repairers](https://www.onetonline.org/link/details/49-9091.00) (accessed 2026-07-22): Describes slot-machine installation, diagnosis, testing, repair, parts replacement, cleaning, transport, recordkeeping, invoicing, collections, parts ordering, and on-site service calls.
- **S4** — [Illinois Gaming Board Open Meeting Minutes, April 23, 2026](https://igb.illinois.gov/content/dam/soi/en/web/igb/documents/board-meetings/minutes/2026/20260423-open-meeting-minutes.pdf) (accessed 2026-07-22): Reports 52 active terminal operators, 8,722 establishments, 49,591 VGTs, 47,202 terminals with ticket-in/ticket-out technology, and March 2026 net terminal income and taxes.
- **S5** — [Illinois Video Gaming Act](https://www.ilga.gov/legislation/ILCS/details?ActID=3095&ActName=Video%2BGaming%2BAct.&ChapAct=230%2BILCS%2B40%2F&Chapter=GAMING&ChapterID=25&MajorTopic=REGULATION&Print=True&SeqEnd=1950000&SeqStart=100000) (accessed 2026-07-22): Requires licensed terminal operators and written host use agreements, mandates a 50/50 split of after-tax terminal profit between operator and host, restricts service and machine access to licensed people, separates operator and host ownership, and assigns operator reporting and tax duties.
- **S6** — [Accel Entertainment 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1698991/000169899125000011/acel-20241231.htm) (accessed 2026-07-22): Describes recurring installation, maintenance, operation, and service for location partners; multi-year location contracts and competitor conversions; 4,117 locations and 26,346 terminals in 2024; and physical, support, regulatory, renewal, and demand risks.
- **S7** — [Accel Entertainment 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1698991/000169899126000018/acel-20251231.htm) (accessed 2026-07-22): Reports the 2024 acquisition of Illinois Gaming Entertainment assets, including 16 operating locations and equipment for $13.5 million, and the acquisition and subsequent results of Louisiana distributed-gaming operator Toucan Gaming.
- **S8** — [Pennsylvania Gaming Control Board Reports Fiscal Year 2025/26 Gaming Revenue](https://gamingcontrolboard.pa.gov/news-and-transparency/press-release/pennsylvania-gaming-control-board-reports-fiscal-year-gaming) (accessed 2026-07-22): Reports $41.62 million of VGT revenue in fiscal 2025/26, up 0.55%, 75 operating VGT facilities versus 73 a year earlier, and revenue by five named terminal operators.
