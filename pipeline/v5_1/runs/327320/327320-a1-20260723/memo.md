# 327320 — Ready-Mix Concrete Manufacturing

*v5.1 Stage 1 research memo. Run `327320-a1-20260723`, model `claude-sonnet-5`, 2026-07-23, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.73 · L 0.82 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digitizable dispatch and administrative workflows in a logistics-intensive industry with documented driver scarcity.
**Weakness:** Manufacture and delivery of concrete are a product transaction, leaving the eligible outsourced-service share very small.

## Business-model lens
- Included: U.S. ready-mix concrete manufacturers in the lower-middle-market EBITDA band that also earn revenue from a separately contracted recurring or repeat outsourced service supplied to external customers.
- Excluded: Ordinary manufacture, sale, and delivery of ready-mix concrete; concrete pumping or placement classified as construction; captive fleet functions; shells; and non-control financing vehicles.
- Customer and revenue model: Producers batch a perishable physical product to specification and deliver it by mixer truck to construction sites, generally against project orders, purchase agreements, or proposals; only separately contracted service revenue qualifies under the screen.
- Deviation from default lens: none

## Executive view
Ready-mix operations contain real digital opportunities in dispatch, ordering, ticketing, customer communication, and fleet coordination, amplified by persistent driver scarcity. However, the business manufactures and delivers a perishable product rather than supplying a recurring outsourced service, so only exceptional firms or revenue streams satisfy the screen.

## How AI changes the work
AI can improve load scheduling, truck routing, order capture, exception prediction, customer updates, quality documentation, billing, and maintenance planning. Driving, batching, discharge, site navigation, inspection, and safety response remain physical and accountable human-machine work, limiting total wage exposure.

## Value capture
Better dispatch can raise truck turns, on-time performance, and asset utilization, but customers rebid concrete and can capture savings through price. Time sensitivity, local plant density, reliability, and hauling constraints provide some defense against complete pass-through.

## Firm availability
Ready-mix has many employer establishments and a history of acquired manufacturing businesses, but the relevant eligible subset is not the industry at large. Firm availability depends first on finding separately contracted recurring services inside otherwise product-led operators.

## Demand durability
Concrete remains tied to physical residential, commercial, industrial, and infrastructure construction. Cyclicality can depress local volumes, yet no credible five-year software substitute exists for the delivered material or accountable producer.

## Risks and uncertainty
Key risks are categorical eligibility, construction cyclicality, local price competition, fleet and insurance costs, driver availability, fragmented software, rejected loads, environmental obligations, and the possibility that productivity gains are passed to customers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2071 | — | OBSERVED | — |
| n | — | 723 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.3 | PROXY | S2, S3, S4, S6 |
| rho | 0.35 | 0.55 | 0.75 | ESTIMATE | S2, S3 |
| e | 0 | 0.02 | 0.08 | ESTIMATE | S1, S5 |
| s5 | 0.1 | 0.2 | 0.34 | PROXY | S7 |
| q | 0.3 | 0.5 | 0.7 | ESTIMATE | S3, S5 |
| d5 | 0.9 | 1.01 | 1.13 | PROXY | S8, S9 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S2, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.29 | 0.82 | 1.86 | ESTIMATE |
| F | 0.00 | 2.19 | 4.87 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.46 | 9.90 | 10.00 | ESTIMATE |

## Caveats
- a: Neither BLS nor NRMCA directly measures wage-weighted AI task exposure.
- a: Existing automated dispatch and paperless ticketing reduce the incremental not-yet-automated opportunity.
- rho: Vendor and trade-association material establishes capability, not representative adoption or savings.
- rho: Small multi-plant operators may have weaker data and integration capacity than showcased producers.
- e: The frozen firm count may materially overstate the screenable population because it is derived from a manufacturing industry rather than a service industry.
- e: Delivery is operationally service-like but remains inseparable from a time-sensitive product sale in the industry definition.
- s5: The source covers broad business-owner populations and does not specify a sale horizon.
- s5: The estimate is conditional on a very small and uncertain eligible subset.
- q: No direct study of AI-benefit pass-through in ready-mix concrete was found.
- q: Local market concentration and construction-cycle conditions may dominate retention.
- d5: Cement tons are not ready-mix cubic yards and do not hold mix design or quality constant.
- d5: Demand is highly local and cyclical, so national averages can conceal severe regional variance.
- o: Remote dispatch can reduce staffing without eliminating the operating firm.
- o: This assesses the physical ready-mix basket even though most of it fails the outsourced-service eligibility lens.

## Sources
- **S1** — [Census Bureau Profile: Ready-mix concrete manufacturing](https://data.census.gov/profile/32732_-_Ready-mix_concrete_manufacturing?codeset=naics~32732&g=010XX00US) (accessed 2026-07-23): Defines the industry as batch or mix plants manufacturing concrete delivered to purchasers in a plastic and unhardened state and reports 6,356 employer establishments in 2023 County Business Patterns.
- **S2** — [Concrete InFocus: Changing the Game Digitally](https://www.nrmca.org/wp-content/uploads/2021/11/ConcreteInFocusWinter2021.pdf) (accessed 2026-07-23): Documents mobile ordering, dispatch chat, live truck tracking, paperless ticketing, electronic inspections, field risk assessments, smart drums, and mobile load analysis in ready-mix operations.
- **S3** — [NRMCA Quality Management System preparation guidelines](https://www.nrmca.org/wp-content/uploads/2020/06/QMS_3Parts.pdf) (accessed 2026-07-23): Describes order entry, scheduling, dispatch, truck assignment and tracking, automated dispatch, batching instructions, technical-service scheduling, and recordkeeping workflows.
- **S4** — [NRMCA 2021 Mixer Driver Recruitment and Retention Survey](https://www.nrmca.org/press-releases/september-1-2021/) (accessed 2026-07-23): Reports an approximately 75,000-person mixer-driver population, 35% turnover, and 68% of survey participants losing business due to driver shortages.
- **S5** — [NRMCA: About Concrete and delivery of ready mixed concrete](https://www.nrmca.org/draft-about-concrete/) (accessed 2026-07-23): Explains that most ready-mix is delivered in rotating-drum trucks, describes mixing and discharge, notes the product's perishability, and cites ASTM's 90-minute discharge constraint.
- **S6** — [BLS industry at a glance: Nonmetallic Mineral Product Manufacturing](https://www.bls.gov/iag/tgs/iag327.htm) (accessed 2026-07-23): Reports 74,870 heavy and tractor-trailer truck drivers in the broader NAICS 327 industry occupation table.
- **S7** — [SBA Office of Advocacy: Paths to Business Ownership](https://advocacy.sba.gov/wp-content/uploads/2021/03/Paths-to-Business-Ownership-fact-sheet.pdf) (accessed 2026-07-23): Reports that 28% of manufacturing owners acquired their firms by purchase and that 64.5% of current owners across industries planned to sell their businesses.
- **S8** — [Mineral Commodity Summaries 2026: Cement](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-cement.pdf) (accessed 2026-07-23): Reports U.S. apparent cement consumption of 110 million metric tons in both 2024 and 2025, providing an upstream volume proxy for ready-mix demand.
- **S9** — [American Cement Association Spring Forecast 2026](https://www.cement.org/2026/04/30/aca-spring-forecast-2026/) (accessed 2026-07-23): Forecasts a 2.5% decline in cement consumption in 2026 and a return to positive growth in 2027.
