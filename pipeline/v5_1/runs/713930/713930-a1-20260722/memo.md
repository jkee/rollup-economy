# 713930 — Marinas

*v5.1 Stage 1 research memo. Run `713930-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.41 · L 2.15 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring, capacity-constrained storage and dockage revenue gives an operator room to retain administrative efficiency gains.
**Weakness:** The automation opportunity is bounded because most essential marina work is physical, safety-sensitive, and site-specific.

## Business-model lens
- Included: US marina firms in the lower-middle-market band that earn recurring or repeat revenue from wet-slip dockage, dry storage, launching, utilities, fuel, boatyard service, and related services for pleasure-craft owners.
- Excluded: Municipal or member-owned facilities without transferable control, captive resort facilities, passive real-estate or financing vehicles, and businesses primarily classified as boat dealers, rental operators, or standalone repair shops.
- Customer and revenue model: Boat owners pay annual, seasonal, monthly, or transient berth and storage charges, often supplemented by launch, utility, fuel, repair, maintenance, and retail revenue.
- Deviation from default lens: none

## Executive view
Marinas combine recurring berth and storage revenue with scarce physical locations and a service layer that remains operator-intensive. The practical AI opportunity is concentrated in administrative and coordination work rather than dock labor, while transaction evidence shows an active market for control transfers. The case weakens materially in locations with poor occupancy, deferred maintenance, adverse water conditions, or economics dominated by nonoperating real estate.

## How AI changes the work
AI-enabled marina systems can streamline reservation intake, billing, customer responses, service estimates, work-order scheduling, inventory records, payments, document handling, and routine marketing. Human staff remain necessary for docking, launching, fueling, repairs, inspections, safety, vendor supervision, and exceptions, limiting substitution to a minority of wage-weighted work.

## Value capture
Recurring annual and seasonal fees do not automatically reprice downward when back-office costs fall, and capacity-constrained facilities have demonstrated pricing power. Retention will be lower where savings are spent on service upgrades, where nearby slips are available, or where customers demand concessions at renewal.

## Firm availability
Most LMM marina firms should fit the recurring external-service lens, though public, member-owned, captive, and real-estate-shell structures are exclusions. Broker data indicate meaningful property sale activity and consolidation, but the available denominator does not cleanly isolate qualifying LMM firm control transfers.

## Demand durability
Installed boats require ongoing storage and access even when new-boat sales soften, and high occupancy and waitlists indicate durable demand in constrained markets. Demand is nevertheless discretionary and highly local, with affordability, insurance, fuel, drought, storms, and access restrictions capable of reducing service volume.

## Risks and uncertainty
The largest evidence gaps are the absence of a six-digit wage-weighted task census, direct automation outcome studies, a firm-level eligibility census, and a deduplicated LMM control-transfer series. Broker market statistics may be selective, and national averages conceal extreme site-level exposure to permitting, lease tenure, environmental liabilities, capital expenditure, and weather.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3316 | — | OBSERVED | — |
| n | — | 67 | — | ESTIMATE | — |
| a | 0.18 | 0.27 | 0.38 | ESTIMATE | S2, S3 |
| rho | 0.45 | 0.6 | 0.72 | ESTIMATE | S3 |
| e | 0.72 | 0.84 | 0.93 | ESTIMATE | S1 |
| s5 | 0.1 | 0.16 | 0.25 | PROXY | S4, S5, S6 |
| q | 0.62 | 0.75 | 0.87 | ESTIMATE | S1, S4 |
| d5 | 0.96 | 1.04 | 1.14 | PROXY | S4, S7, S8 |
| o | 0.88 | 0.94 | 0.98 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.07 | 2.15 | 3.63 | ESTIMATE |
| F | 2.83 | 3.70 | 4.52 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.45 | 9.78 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation evidence is for broad NAICS 713 rather than six-digit marinas.
- a: The range concerns current not-yet-automated tasks and may overstate opportunity at marinas already using integrated management systems.
- a: The frozen compensation ratio has a 2024-wage/2022-receipts vintage mismatch and is harmonized to the IPS basis as provided.
- rho: Vendor feature availability is not evidence of adoption or realized labor savings.
- rho: Small seasonal marinas may lack clean data, management capacity, and reliable connectivity.
- rho: Implementation excludes pricing, demand, and valuation effects.
- e: No source measures eligibility within the supplied LMM population.
- e: NAICS permits related fuel, retail, rental, and repair activities, creating firm-level revenue-mix variation.
- e: The supplied n of 67 is itself a margin-bridged estimate from size-class data.
- s5: The transaction denominator is operations rather than firms and is not limited to the EBITDA band.
- s5: Broker reports may miss private transfers and may include real-estate transactions without operating-company control.
- s5: The 51% owner-age statistic is for US small businesses generally, not marinas.
- q: The 2026 investment report is broker-authored and does not measure AI benefit retention.
- q: Pricing power is location-specific; marinas with deferred maintenance or weak amenities can have vacancies despite broader capacity constraints.
- q: The estimate excludes volume effects, which are represented in demand primitives.
- d5: Revenue and expenditure growth are nominal and not direct quantity measures.
- d5: NMMA manufacturer sentiment is North American and adjacent to, not representative of, marina operators.
- d5: Climate events, drought, insurance withdrawal, and permitting constraints can produce severe local divergence.
- o: Some transient booking, payment, access control, and customer communication can become self-service.
- o: This is a bounded judgment, not a measured industry share.
- o: Physical operator requirements vary by facility design, fuel sales, repair activity, and local regulation.

## Sources
- **S1** — [NAPCS Product List for NAICS 7139: Other Amusement and Recreation Industries](https://www2.census.gov/library/reference/napcs/product-list/web-7139-final-reformatted-edited-us061509.pdf) (accessed 2026-07-22): Defines marina products as pleasure-craft dockage, launching, utilities, and storage and states that dockage revenue includes annual membership, initiation, and transient fees; supports the recurring-service lens, eligibility, billing structure, and physical operator role.
- **S2** — [Amusement, Gambling, and Recreation Industries: NAICS 713](https://www.bls.gov/iag/tgs/iag713.htm) (accessed 2026-07-22): Reports broader-subsector occupational employment concentrated in frontline recreation roles, including 276,700 amusement and recreation attendants in 2025; used only as an occupation-mix boundary for the automation estimate.
- **S3** — [DockMaster Marina Management Software](https://www.dockmaster.com/) (accessed 2026-07-22): Documents currently available marina workflows for AI-assisted scheduling and estimates, reservations, billing, accounting, inventory, payments, e-signatures, customer records, and mobile field work; supports task exposure and technical implementability, not realized savings.
- **S4** — [2026 Marina Investment Report](https://www.leisurepropertiesgroup.com/wp-content/uploads/2026/03/2026-Marina-Investment-Report-Final-2.pdf) (accessed 2026-07-22): Reports 3,408 active marina operations, 102 marina sales in 2025, 2025 revenue up 4.3%, occupancy around 92%, more than half of surveyed US marinas above 95% occupancy, 26% at capacity, and 68% raising rates by 4%-6%; supports transfer, capture, and demand proxies.
- **S5** — [State of the Marina Market](https://www.marinadockage.com/state-of-the-marina-market/) (accessed 2026-07-22): A marina broker with more than 250 reported transactions describes retirement among common sale motives and active corporate, individual, and regional acquisition demand; supports the existence and composition of the transfer market.
- **S6** — [Starting a small business is hard. Exiting can be even harder, but planning early is the key](https://apnews.com/article/small-business-succession-retirement-sale-transition-d582a18f1e440846a6ff5bb425ba6daa) (accessed 2026-07-22): Reports that 51% of US small-business owners are over age 55 and describes sale, family succession, internal succession, and closure as alternative exit paths; used as a broad-population succession proxy.
- **S7** — [Innovation Driving U.S. Boat Sales Demand As Key Winter Boat Show Buying Season Gets Underway](https://www.nmma.org/press/article/24937) (accessed 2026-07-22): Reports 2024 US new-powerboat unit sales down an estimated 9%-12%, expected 2025 boating expenditures 3%-5% above 2024, and an estimated 85 million annual US boating participants; supports demand range and cyclicality.
- **S8** — [Marine Leadership Barometer: Q1 Survey Signals Steadier Industry Outlook in 2026](https://www.nmma.org/press/article/25503) (accessed 2026-07-22): Reports that 43% of surveyed NMMA manufacturer executives expected modest industry improvement and 60% expected company revenue growth over the following year, while infrastructure constraints remained a concern; used as adjacent demand sentiment.
