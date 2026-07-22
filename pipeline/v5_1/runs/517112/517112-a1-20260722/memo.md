# 517112 — Wireless Telecommunications Carriers (except Satellite)

*v5.1 Stage 1 research memo. Run `517112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** The principal driver is durable growth in wireless connectivity combined with AI-ready customer, fraud, billing, and network-assurance workflows.
**Weakness:** The principal weakness is a concentrated, spectrum- and capital-intensive market with strong unit-price pressure and no defensible LMM firm-count anchor.

## Business-model lens
- Included: U.S. lower-middle-market facilities-based wireless carriers, excluding satellite, that repeatedly provide mobile voice and data, fixed wireless broadband, private or specialized mobile radio, paging, IoT connectivity, and wholesale network access to residential, business, public-sector, or reseller customers.
- Excluded: Satellite carriers, wireless agents and resellers without operated network facilities, tower-only landlords, device retailers, equipment manufacturers, construction-only contractors, captive private networks, shells, non-control financing vehicles, and firms outside the target normalized-EBITDA band.
- Customer and revenue model: Customers generally pay recurring postpaid or prepaid service charges, account or line fees, data-plan or capacity charges, and wholesale access fees, with additional device, installation, roaming, usage, financing, and support revenue. Plans are frequently bundled and customers can switch, while enterprise, public-safety, wholesale, and private-network contracts may have terms and service levels.
- Deviation from default lens: none

## Executive view
Wireless carriers have recurring service revenue, strong data and connection growth, and mature digital workflows suitable for AI in customer care, billing, fraud, sales, and network assurance. Physical radio infrastructure, licensed spectrum, security, coverage, and emergency obligations keep an accountable operator central, but industry concentration, capital intensity, price pressure, and a missing LMM firm-count anchor weaken the acquisition population case.

## How AI changes the work
AI can assist contact handling, plan and billing inquiries, churn prediction, fraud and spam detection, activation, dispatch, anomaly detection, radio optimization, energy management, capacity planning, documentation, sales, and technician diagnostics. Humans still install and repair radio assets, acquire sites, restore outages, negotiate enterprise and wholesale accounts, engineer spectrum and coverage, approve production changes, and own safety and regulatory consequences.

## Value capture
Recurring service plans can preserve part of labor productivity, especially between repricing events. Switching, promotions, falling unit prices, flat-rate traffic, service credits, device economics, spectrum, vendors, energy, and reinvestment in coverage and capacity consume or pass through much of the benefit.

## Firm availability
Facilities-based service fits the recurring external-service lens, but the national market is concentrated and the actual LMM population is unknown because n is missing. Candidates require transferable spectrum and licenses, durable sites and backhaul, diversified subscribers or contracts, adequate scale, sound maintenance capital, and limited dependence on a national host.

## Demand durability
Mobile data, 5G devices, IoT, voice, messaging, and fixed-wireless access support continued quantity growth. Connection saturation, Wi-Fi offload, wholesale and cable competition, falling real prices, satellite entry, and the gap between traffic and monetization temper that signal.

## Risks and uncertainty
Key risks are missing firm-count evidence, spectrum scarcity and transfer approval, capital intensity, national-carrier competition, wholesale dependence, price compression, churn, network outage, cyberattack, location privacy, fraud, roaming and interconnection terms, site leases, vendor concentration, energy cost, satellite substitution, and acquisition integration.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1138 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.22 | 0.35 | 0.49 | ESTIMATE | S1, S2, S3 |
| rho | 0.56 | 0.73 | 0.86 | PROXY | S3 |
| e | 0.19 | 0.43 | 0.68 | ESTIMATE | S1, S4, S5, S6 |
| s5 | 0.1 | 0.22 | 0.35 | PROXY | S4, S6 |
| q | 0.24 | 0.4 | 0.57 | ESTIMATE | S4, S5, S6 |
| d5 | 0.98 | 1.11 | 1.26 | PROXY | S4, S5, S6 |
| o | 0.89 | 0.96 | 0.99 | ESTIMATE | S1, S2, S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.56 | 1.16 | 1.92 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 4.80 | 8.00 | 10.00 | ESTIMATE |
| D | 8.72 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS technician evidence covers multiple telecommunications technologies and contractors rather than the full 517112 workforce.
- a: GSMA tracks public global operator deployments, not wage-weighted U.S. LMM task exposure.
- a: The frozen compensation ratio is an ancestor-code estimate for all 517 and may misstate wireless-carrier labor intensity.
- rho: Public deployment announcements may overrepresent large operators and successful projects.
- rho: GSMA deployment maturity does not directly measure the share of exposed labor opportunity realized within five years.
- rho: Regional carriers may adopt vendor-packaged tools but lack the data engineering and governance capacity of national operators.
- e: The FCC's nationwide-carrier count does not enumerate all regional, rural, paging, SMR, IoT, and fixed-wireless operators.
- e: The dataset has no defensible n-band value, so the actual LMM population is unknown.
- e: Network EBITDA can overstate transferable cash when spectrum, site, radio, and core reinvestment needs are excluded.
- s5: Large public transactions do not measure transfer probability among LMM regional carriers.
- s5: Customer, spectrum, license, or network asset acquisitions may not qualify as firm control transfers.
- s5: The missing LMM denominator prevents direct conversion of observed deals into a probability.
- q: T-Mobile is far larger and more integrated than a lower-middle-market regional carrier.
- q: CTIA is an industry trade association and its price measures do not isolate plan quality or operator profitability.
- q: The cited sources do not measure how AI savings are passed through or retained.
- d5: Traffic growth is not proportional to constant-quality paid service quantity under flat-rate plans.
- d5: CTIA aggregates national and regional carriers and is advocacy-oriented.
- d5: T-Mobile's growth includes acquisitions and may not represent LMM regional operators.
- o: Continued growth in wireless use does not guarantee continued demand for every regional operator.
- o: Neutral-host, wholesale, MVNO, and private-network structures can separate network ownership from the retail relationship.
- o: Satellite direct-to-device and automated networks may unbundle more of the current basket than the base assumes.

## Sources
- **S1** — [2022 NAICS Definition: 517112 Wireless Telecommunications Carriers (except Satellite)](https://www.census.gov/naics/?details=517112&input=517112&year=2022) (accessed 2026-07-22): Official industry definition and lens; a, e, and o
- **S2** — [Telecommunications Technicians](https://www.bls.gov/ooh/installation-maintenance-and-repair/telecommunications-equipment-installers-and-repairers-except-line-installers.htm) (accessed 2026-07-22): Radio, cellular, tower, outage, installation, testing, repair, and infrastructure duties and outlook; a and o
- **S3** — [Telco AI: State of the Market, Q3 2025](https://prod-cms.gsmaintelligence.com/research-file-download?assetId=67646&reportId=67642) (accessed 2026-07-22): Telco AI use cases, deployment areas, maturity, objectives, and size differences; a, rho, and o
- **S4** — [2024 Communications Marketplace Report](https://docs.fcc.gov/public/attachments/FCC-24-136A1.pdf) (accessed 2026-07-22): Mobile facilities-based concentration, competition, pricing, fixed-mobile interaction, entry conditions, and merger context; e, s5, q, d5, and o
- **S5** — [CTIA 2025 Annual Survey Highlights](https://api.ctia.org/wp-content/uploads/2025/09/2025-Annual-Survey-Highlights.pdf) (accessed 2026-07-22): 2024 U.S. wireless traffic, connections, 5G devices, investment, prices, fixed-wireless customers, sites, voice, and messaging; e, q, d5, and o
- **S6** — [T-Mobile US 2025 Full-Year Results](https://www.sec.gov/Archives/edgar/data/1283699/000128369926000007/tmus12312025ex991.htm) (accessed 2026-07-22): Wireless service revenue, customer growth, broadband growth, acquisition effects, and capital investment; e, s5, q, and d5
