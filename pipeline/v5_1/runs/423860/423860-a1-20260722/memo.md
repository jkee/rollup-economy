# 423860 — Transportation Equipment and Supplies (except Motor Vehicle) Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423860-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.70 · L 0.54 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High-volume RFQ, sourcing, pricing, and document workflows can be automated while scarce physical parts and traceability preserve operator value.
**Weakness:** The code is broad, and OEM control plus compliance-heavy exceptions make both eligibility and realized automation highly target-specific.

## Business-model lens
- Included: Lower-middle-market merchant wholesalers supplying recurring aftermarket parts, components, consumables, spares, exchange units, and related sourcing, inventory, documentation, and fulfillment services for aircraft, marine vessels, rail equipment, and other non-motor-vehicle transportation assets.
- Excluded: Whole-aircraft, vessel, or rolling-stock brokers dominated by episodic asset sales; manufacturers; repair stations whose economics are primarily labor service; captive OEM or carrier units; motor-vehicle parts distributors; financing vehicles; and firms lacking transferable operations.
- Customer and revenue model: Product and exchange gross margin from repeat parts procurement by airlines, MROs, operators, government agencies, lessors, and transportation fleets, often supplemented by AOG response, pooling, consignment, inventory management, documentation, sourcing, repair coordination, and logistics fees.
- Deviation from default lens: none

## Executive view
Recurring transportation aftermarket distribution has a real AI productivity surface in RFQ intake, sourcing, pricing, inventory, and documentation, but its durable value rests on physical availability, provenance, qualification, and urgent response. Aviation evidence is strongest and suggests favorable five-year parts demand; the broad code also contains marine, rail, whole-equipment, and other niches, so a target must prove repeat aftermarket economics rather than merely carry the NAICS label.

## How AI changes the work
AI can parse large emailed RFQs, map part numbers and alternates, search internal and marketplace inventory, recommend pricing, forecast spares, draft quotes, and organize trace documents. These tools reduce repetitive sales, procurement, and administrative work. Inspection, airworthiness and export judgment, supplier qualification, AOG escalation, physical logistics, and high-stakes customer commitments remain human-accountable and create a hard ceiling on autonomous implementation.

## Value capture
Fast, accurate responses and better inventory decisions can create both cost and commercial value, especially for scarce and AOG parts. Qualification, in-stock availability, and clean documentation reduce pure price comparability. Capture is constrained by airline and MRO procurement sophistication, marketplaces, pooling, contract renewal, OEM aftermarket control, and the risk that improved data simply intensifies price competition.

## Firm availability
Owner demographics and active aerospace aftermarket transactions indicate continuing control opportunities. A firm is transferable when approved-supplier status, traceability, inventory records, vendor access, customer relationships, and AOG processes are institutionalized. It is fragile when value resides in the owner's contacts or undocumented inventory knowledge. The qualifying share of the broad NAICS population remains uncertain.

## Demand durability
Commercial aviation traffic is forecast to grow, while delayed deliveries and aging fleets sustain maintenance and spares demand through the horizon. Physical parts and accountability cannot be replaced by software. The main substitution risk is channel rather than end demand: OEM direct programs, digital marketplaces, pooling, and customer self-sourcing can move volume away from independent distributors even as total parts demand grows.

## Risks and uncertainty
The evidence base is aviation-heavy and may not represent marine or rail distributors. Inventory obsolescence, counterfeit or unapproved parts, documentation failures, export controls, supplier concentration, OEM restrictions, lease-return rules, customer concentration, working capital, cyclicality, and AOG liability can dominate labor savings. A low-quality parts master or poor trace archive can also make AI unsafe and expensive to deploy.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1078 | — | OBSERVED | — |
| n | — | 480 | — | ESTIMATE | — |
| a | 0.18 | 0.29 | 0.42 | PROXY | S1, S2, S3, S4 |
| rho | 0.25 | 0.43 | 0.6 | PROXY | S2, S3, S5, S6 |
| e | 0.28 | 0.48 | 0.66 | ESTIMATE | S7, S8 |
| s5 | 0.12 | 0.21 | 0.31 | PROXY | S9, S10, S11 |
| q | 0.42 | 0.6 | 0.76 | PROXY | S3, S4, S12, S13 |
| d5 | 1.03 | 1.14 | 1.28 | PROXY | S12, S14 |
| o | 0.78 | 0.9 | 0.97 | PROXY | S3, S4, S13 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.19 | 0.54 | 1.09 | PROXY |
| F | 4.57 | 6.27 | 7.40 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | PROXY |
| D | 8.03 | 10.00 | 10.00 | PROXY |

## Caveats
- a: Aviation-specific tools may not generalize to marine and rail distributors.
- a: Software capability does not establish current utilization or realized labor removal.
- a: Safety and export controls can require human review even where documents are machine-readable.
- rho: Adoption intent is not scaled implementation.
- rho: Sponsored tools describe best-case workflows.
- rho: Regulated customers may limit autonomous sending or approval even when extraction is accurate.
- e: The estimate spans very different aviation, marine, rail, military, golf-cart, and other niches.
- e: Some aircraft parts distributors classify outside 423860, while non-aviation firms inflate the code as an aviation proxy.
- e: The injected LMM firm count is itself estimated.
- s5: Cross-industry owner intentions do not equal closed industry deals.
- s5: Publicly disclosed aerospace transactions skew larger than the LMM band.
- s5: Inventory purchases and repair-station deals may not transfer a qualifying distributor operation.
- q: No source directly measures five-year benefit retention.
- q: AOG and hard-to-find parts have very different economics from routine consumables.
- q: OEM authorization and lease-return rules can override distributor execution quality.
- d5: Passenger traffic does not map one-for-one to parts quantities.
- d5: Current shortages inflate inventory and substitution behavior that may normalize.
- d5: Defense, rail, marine, space, and general aviation can diverge from commercial airline trends.
- o: Operator-required does not guarantee the operator remains an independent LMM distributor.
- o: The estimate is highest for regulated aircraft parts and lower for standardized marine or rail supplies.
- o: OEM vertical integration can preserve the function while eliminating the target firm type.

## Sources
- **S1** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): For the selected durable-goods wholesale grouping, leading occupations include 229,190 nontechnical wholesale/manufacturing sales representatives, 146,830 hand material movers, 77,370 general and operations managers, 62,040 stockers/order fillers, 42,160 customer service representatives, and 38,620 shipping/receiving/inventory clerks.
- **S2** — [AIquote aviation parts quotation platform](https://www.aiquote.ai/) (accessed 2026-07-22): Describes automatic extraction of aviation RFQs from emails, pricing and inventory rules, automatic sending of qualifying quotes, and human dashboard review of exceptions, demonstrating exposure in a core industry workflow.
- **S3** — [FAA Advisory Circular 21-29D: Detecting and Reporting Suspected Unapproved Parts](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_21-29D.pdf) (accessed 2026-07-22): Calls for traceability to FAA-approved sources and receiving inspection that verifies packaging, part and serial numbers, tampering, shelf or life limits, and supporting documents; identifies FAA Form 8130-3 and other approved records.
- **S4** — [IATA Aviation Supply Chain](https://www.iata.org/en/programs/ops-infra/techops/aviation-supply-chain/) (accessed 2026-07-22): Documents airline use of spares inventory, AOG desks, exchanges, loans, pooling, accredited suppliers, forecasting, and maintenance data; reports $1.4 billion in extra 2025 spares-inventory cost and describes OEM aftermarket dominance.
- **S5** — [Practical AI for Industrial Distribution](https://www.inddist.com/home/article/22950770/practical-ai-for-industrial-distribution) (accessed 2026-07-22): A 2025 distributor survey reported 29% AI use, about 10% positive business impact, more than 43% expected adoption within two years, and 50% ERP use; the article identifies fragmented data and integration as barriers.
- **S6** — [AI in distribution: driving digital transformation today](https://www.mckinsey.com/industries/industrials/our-insights/where-value-is-won-and-lost-in-distribution) (accessed 2026-07-22): Reports that 90% of distributors had AI initiatives but only 11% had fully adopted, while 25% of adopters realized expected cost savings; logistics and inventory ranked as the leading AI-impact areas.
- **S7** — [How Big is the U.S. Aircraft Parts Distribution Industry?](https://www.aviationsuppliers.org/asa-member-bulletin---feb-2020---how-big-is-the-us-aircraft-parts-distribution-industry) (accessed 2026-07-22): Explains that 423860 includes commercial vessels, golf carts, railroad cars, and military vehicles as well as aircraft parts, and argues the code is an imperfect but useful proxy for aircraft parts distribution.
- **S8** — [Census Bureau profile: NAICS 423860](https://data.census.gov/profile/423860_-_Transportation_equipment_and_supplies_%28except_motor_vehicle%29_merchant_wholesalers?codeset=naics~423860&g=010XX00US) (accessed 2026-07-22): Identifies the national industry and reports 2,375 employer establishments, establishing the broad population to which the narrower recurring-aftermarket lens is applied.
- **S9** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 52.3% of U.S. employer businesses are owned by people age 55 or older and 22% of employer-business owners planned to sell, transfer, or go public within five years.
- **S10** — [MRO Memo: Where Is Aftermarket M&A Headed Next?](https://aviationweek.com/mro/aircraft-propulsion/mro-memo-where-aftermarket-ma-headed-next) (accessed 2026-07-22): Reports that private-equity-led deals represented almost one-fifth of MRO-sector M&A activity in the first half of 2025 and notes buyer preference for predictable recurring repair volumes and scalable component businesses.
- **S11** — [Alliance Air Parts merger with RIM Enterprises](https://www.infinitycappartners.com/news/infinity-capital-partners-advises-alliance-air-parts-on-its-merger-with-rim-enterprises) (accessed 2026-07-22): Documents a June 12, 2025 merger involving an Oklahoma City aircraft de-manufacturer and supplier to the business-aviation aftermarket, providing direct evidence of control activity in the parts ecosystem.
- **S12** — [Aerospace Supply Chain Bottlenecks Continue to Constrain Airlines](https://www.iata.org/en/pressroom/2025-releases/2025-12-09-02/) (accessed 2026-07-22): Reports a delivery shortfall of at least 5,300 aircraft, backlog above 17,000, average fleet age of 15.1 years, and supply-demand normalization unlikely before 2031-2034; also reports $3.1 billion in added maintenance cost and $1.4 billion in surplus inventory holding cost.
- **S13** — [Acquisition of FAA certified parts for consumable items](https://www.acquisition.gov/dlad/11.9201-acquisition-faa-certified-parts-consumable-items.) (accessed 2026-07-22): Requires specified dealer/distributor accreditation or traceability documentation for government acquisition of FAA-certified consumable parts, illustrating continuing qualification and documentation accountability.
- **S14** — [FAA Aerospace Forecast Fiscal Years 2026-2046: Forecast Overview](https://www.faa.gov/data_research/aviation/aerospace_forecasts/2026_Forecast_Overview.pdf) (accessed 2026-07-22): Forecasts U.S. carrier domestic passenger growth of 2.4% annually, system revenue passenger miles growth of 2.6% annually from 2025-2046, and turbine general-aviation fleet growth of 2.1% annually.
