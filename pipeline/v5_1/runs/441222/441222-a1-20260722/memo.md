# 441222 — Boat Dealers

*v5.1 Stage 1 research memo. Run `441222-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.42 · L 0.71 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Existing marine-specific automation can remove substantial lead, listing, quote, marketing, and paperwork effort while physical boat service keeps the customer relationship operator-led.
**Weakness:** The code is dominated by cyclical merchandise sales, and neither full-service eligibility nor five-year transfer probability is directly measured for LMM firms.

## Business-model lens
- Included: US full-service boat dealerships in the lower-middle-market band that sell new or pre-owned boats and also provide repeat customer services such as maintenance and repair, parts support, brokerage or consignment, storage, marina services, financing, insurance, or extended-service administration.
- Excluded: Pure inventory retailers with no material repeat service relationship, boat manufacturers, stand-alone marinas, stand-alone repair shops classified elsewhere, distributors, captive manufacturer outlets, and non-control financing vehicles.
- Customer and revenue model: Predominantly consumer-facing boat and accessory sales, with recurring or repeat revenue from service labor, parts, storage, brokerage, finance and insurance commissions, warranties, and other ancillary services. Boat sales are transactional and cyclical; service and ownership-lifecycle revenue is the recurring component relevant to the lens.
- Deviation from default lens: The code combines transactional merchandise sellers with full-service dealerships. The lens is narrowed to dealers with a material repeat service or ownership-lifecycle relationship because pure boat retail alone does not supply a recurring outsourced service.

## Executive view
The relevant opportunity is not pure boat retail but the full-service dealership that owns the recurring customer relationship across maintenance, parts, storage, brokerage, financing, insurance, and future trade-ins. AI can reduce the administrative load around that relationship, while the physical asset and regulated transaction preserve a strong need for an operator. Demand and margins remain highly cyclical.

## How AI changes the work
Dealer-specific software can already generate listings, qualify leads, answer inventory questions, produce quotes, syndicate inventory, prepare closing packets, and automate follow-up. Those tools target sales support, marketing, office, and service-adviser tasks; they do much less to substitute for diagnosis, repair, inspection, trade appraisal, delivery, and high-trust selling.

## Value capture
Capture should be better in fixed-price service, fee, and administrative workflows than in heavily negotiated boat sales. Online price transparency and intense competition can pass savings to buyers, while higher-margin service and ownership-lifecycle revenue offers more room to retain productivity gains.

## Firm availability
The market is fragmented and mostly owner-operated, and consolidation is demonstrably active. Eligibility is less certain than raw fragmentation because many independents remain predominantly new-boat sellers with limited ancillary capability; deal volume also lacks an industry-specific denominator.

## Demand durability
Boat purchases are discretionary and rate-sensitive, but the installed fleet creates repeat maintenance, parts, storage, repair, and resale needs. Recent new-unit contraction warrants a broad range, while used-boat activity and ownership-lifecycle services reduce the risk that the whole current basket disappears.

## Risks and uncertainty
The biggest risks are a prolonged affordability downturn, inventory and floorplan pressure, tariff exposure, severe weather, low digital maturity, poor data integration, and overestimating how many dealers have a material service relationship. The key evidence gaps are an occupation-weighted task map, eligible-dealer census, and denominator-based control-transfer history.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1119 | — | OBSERVED | — |
| n | — | 397 | — | ESTIMATE | — |
| a | 0.18 | 0.29 | 0.4 | PROXY | S1, S2 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S1, S2 |
| e | 0.35 | 0.55 | 0.72 | ESTIMATE | S3 |
| s5 | 0.08 | 0.16 | 0.27 | ESTIMATE | S3, S4 |
| q | 0.35 | 0.57 | 0.76 | ESTIMATE | S3 |
| d5 | 0.84 | 1 | 1.16 | PROXY | S3, S5 |
| o | 0.82 | 0.92 | 0.98 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.71 | 1.29 | ESTIMATE |
| F | 4.01 | 5.76 | 7.01 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.89 | 9.20 | 10.00 | ESTIMATE |

## Caveats
- a: No source measures wage-weighted AI task exposure specifically for NAICS 441222.
- a: The MRAA survey concerns digital marketing rather than the whole dealership labor pool.
- a: Vendor capability claims show technical availability, not realized labor substitution.
- rho: Existing product features do not establish sustained adoption or headcount avoidance.
- rho: Small dealerships may lack clean inventory and customer data or integration staff.
- rho: Physical technician work and accountable deal approval remain outside the implementation case.
- e: OneWater is a large consolidator and is not representative of independent LMM dealers.
- e: The provided firm count is margin-bridged and may include firms whose EBITDA arises mainly from inventory sales.
- e: Ancillary activities can be present but too small to make the repeat-service lens economically meaningful.
- s5: The reported 94 and 91 transactions cover automotive, RV, marine, powersports, trucking, and equipment dealerships across North America, not only US boat dealers.
- s5: Broker-reported activity may be selected toward marketable firms and does not reveal failed sale processes.
- s5: Owner age and succession readiness are not directly observed.
- q: A public consolidator's segment economics may not match LMM independents.
- q: Service, parts and other is a mixed category that includes distribution activity.
- q: The estimate separates price retention from implementation and demand effects, but real dealer decisions can couple them.
- d5: New-boat unit sales are more cyclical than the full ownership-lifecycle service basket.
- d5: The sources do not hold quality and price constant exactly.
- d5: Interest rates, tariffs, weather, fuel costs, and consumer confidence can dominate a five-year period.
- o: OEM direct sales and mobile service could grow faster than assumed.
- o: The operator requirement is stronger for repair and delivery than for search, marketing, and simple brokerage administration.
- o: State franchise, title, and registration rules vary and may change.

## Sources
- **S1** — [2025 Marine Industry Digital Marketing Report](https://mraa.com/wp-content/uploads/2025/04/2025DigitalMarketingSurveyReport.pdf) (accessed 2026-07-22): Dealer survey reports time/staffing as the most-cited digital-marketing pain point at 13.4%; 57% use an API/feed for external inventory, while 35% do not; it documents ongoing integration and automation gaps.
- **S2** — [Boatyard Sales: Marine Dealership Management Software](https://info.boatyard.com/sales) (accessed 2026-07-22): Documents currently offered marine-dealer workflows including AI-powered listings and sales agents, digital quoting, inventory and lead management, marketplace syndication, and automatic mapping of customer and boat data into closing documents.
- **S3** — [OneWater Marine Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1772921/000177292125000085/onew-20250930.htm) (accessed 2026-07-22): Reports roughly 4,000 US dealerships, mostly owner-operated with three stores or fewer; describes full-service activities and independent retailers' limited non-boat capability; provides revenue, gross-margin, cyclicality, and used-boat evidence.
- **S4** — [The current state of the marine buy-sell market](https://boatingindustry.com/news/2026/01/30/the-current-state-of-the-marine-buy-sell-market/) (accessed 2026-07-22): A dealership broker reports 94 transactions in 2024 and 91 in 2025 across several North American dealership verticals and describes weaker recent activity, buyer caution, financing costs, and valuation pressure.
- **S5** — [NMMA Confirms 9% Decline in 2024 New Boat Retail Sales](https://www.nmma.org/statistics/article/25001) (accessed 2026-07-22): NMMA reports a 9% decline in 2024 new powerboat retail unit sales and highlights uncertainty around participation and consumer behavior.
