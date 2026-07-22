# 483111 — Deep Sea Freight Transportation

*v5.1 Stage 1 research memo. Run `483111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.85 · L 0.74 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Information-heavy shore-side workflows sit beside durable physical demand that still requires an accountable operator.
**Weakness:** A 15.78% frozen labor share and competitive, volatile freight pricing limit the economic leverage and retention of AI savings.

## Business-model lens
- Included: U.S. lower-middle-market vessel operators and ship-chartering businesses with crew that provide recurring deep-sea cargo transportation to or from foreign ports for external customers.
- Excluded: Coastal, Great Lakes, and inland freight; passenger and cruise operations; freight forwarders and non-vessel-operating intermediaries; ports and terminals; ship managers without freight-transportation revenue; captive fleets; single-vessel financing or passive owning shells; and operators outside the lower-middle-market EBITDA band.
- Customer and revenue model: Voyage charters, time charters, liner service contracts, tariffs, and spot bookings paid by shippers, charterers, or logistics intermediaries for international ocean carriage; repeated trade lanes and customer shipping programs create recurring demand despite volatile rates.
- Deviation from default lens: none

## Executive view
Deep-sea freight has meaningful AI opportunity in documentation, chartering, planning, compliance, and shore-side operations, but its low frozen labor share and safety-critical shipboard work limit the direct labor prize. Demand remains physical and operator-required, while globally transparent and volatile pricing constrains long-run retention.

## How AI changes the work
AI can draft and reconcile shipping documents, review charter parties, optimize voyages and fuel, screen sanctions and compliance records, triage claims, audit invoices, summarize vessel telemetry, and assist maintenance planning. Navigation, engineering, cargo safety, maintenance, and emergencies remain physical, regulated, and accountable to qualified people.

## Value capture
Time charters and service contracts can preserve savings until amendment or renewal, but the large spot market, broker and index visibility, global capacity cycles, and competitive tenders make cost advantages contestable. Retention will vary materially by niche, customer concentration, route scarcity, and contract duration.

## Firm availability
The frozen dataset estimates 52 firms in the EBITDA band, but the classification can contain passive or single-purpose vessel entities and subsidiaries that are not independently transferable operating companies. Strategic control transfers are visible, yet the available example is far larger than the target band and does not establish a small-firm turnover rate.

## Demand durability
UNCTAD expects moderate global seaborne-trade growth through 2030, and physical cargo cannot be converted into software. Route-specific trade policy, war, sanctions, commodity shifts, and fleet oversupply still make individual-company demand and economics much more volatile than the global forecast.

## Risks and uncertainty
Key risks are rate and asset-price cycles, customer and charter concentration, fuel and emissions costs, cyber exposure, sanctions, liability, financing, and costly fleet renewal. Evidence is weakest on the eligible-firm denominator, LMM transfer frequency, task-level labor mix, and the actual sharing of productivity gains through private charters.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1578 | — | OBSERVED | — |
| n | — | 52 | — | ESTIMATE | — |
| a | 0.16 | 0.26 | 0.38 | PROXY | S1, S2 |
| rho | 0.28 | 0.45 | 0.62 | ESTIMATE | S2, S4 |
| e | 0.35 | 0.55 | 0.72 | ESTIMATE | S7 |
| s5 | 0.08 | 0.15 | 0.26 | PROXY | S6 |
| q | 0.32 | 0.5 | 0.7 | PROXY | S5 |
| d5 | 0.92 | 1.1 | 1.2 | PROXY | S3 |
| o | 0.93 | 0.97 | 0.995 | ESTIMATE | S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.74 | 1.49 | ESTIMATE |
| F | 1.45 | 2.68 | 3.82 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | PROXY |
| D | 8.56 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS does not publish a 483111-specific occupation table in the cited page.
- a: Exposure is a task mapping, not an observed substitution rate.
- a: Crewing models differ between U.S.-flag and foreign-flag vessels and between liner, tanker, and dry-bulk operations.
- rho: No source directly measures five-year AI implementation for LMM deep-sea freight operators.
- rho: A small operator may use outsourced ship management, moving exposed labor outside its payroll.
- rho: International flag-state and port-state requirements create heterogeneous adoption constraints.
- e: The official classification defines establishments, not transferable firms.
- e: Shipping commonly uses one-purpose vessel entities that can inflate apparent firm counts.
- e: The frozen n estimate is margin-bridged from receipts and may be sensitive to cyclical shipping margins.
- s5: The observed transaction is much larger than the screened band.
- s5: A vessel sale is not necessarily a qualifying operating-company control transfer.
- s5: Private transactions and ownership changes in single-purpose vessel entities are incompletely disclosed.
- q: FMC service-contract statistics primarily illuminate liner trades and not all dry-bulk, tanker, or project-cargo charters.
- q: Contract counts do not reveal rate terms, duration, or customer power.
- q: Freight-rate volatility may dominate modest operating savings.
- d5: Global seaborne volume is not U.S. operator demand and does not control for service quality.
- d5: Ton-miles can diverge from tons when routes change.
- d5: The forecast predates some possible trade, conflict, and policy changes during the horizon.
- o: The estimate concerns the continued need for an operator, not preservation of current onboard headcount.
- o: The MASS Code is new, non-mandatory, and may evolve before the end of the horizon.
- o: Consolidation could move service to a different operator without eliminating operator-required demand.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 483000 Water Transportation](https://www.bls.gov/oes/2023/may/naics3_483000.htm) (accessed 2026-07-22): Provides the all-water-transport occupation structure and confirms the published population covers employers of all sizes in NAICS 483000, including both deep-sea/coastal/Great Lakes and inland transport.
- **S2** — [Water Transportation Workers: Occupational Outlook Handbook](https://www.bls.gov/ooh/transportation-and-material-moving/water-transportation-occupations.htm) (accessed 2026-07-22): Documents vessel operation, maintenance, safety, physical skills, long tours, training, and 84,300 water-transport jobs in 2024 with 1% projected growth through 2034.
- **S3** — [Review of Maritime Transport 2025, Chapter I: International Maritime Trade](https://unctad.org/system/files/official-document/rmt2025ch1_en.pdf) (accessed 2026-07-22): Forecasts total seaborne trade to grow at an annual average of 2% from 2026-2030 and containerized trade by 2.3%.
- **S4** — [IMO adopts first global Code for autonomous ships](https://www.imo.org/en/mediacentre/pressbriefings/pages/imo-adopts-mass-code.aspx) (accessed 2026-07-22): Reports that fully crewless or remote ships remain limited; the non-mandatory MASS Code applies from July 2026, requires safety and approval controls, and retains master responsibility even off ship.
- **S5** — [Federal Maritime Commission FY 2025 Annual Report](https://www.fmc.gov/wp-content/uploads/2026/04/FY-2025-Annual-Report.pdf) (accessed 2026-07-22): Reports 384,811 original service contracts and 996,803 amendments in FY2025 and says shippers relied more on amendments while redirecting some volume to the spot market.
- **S6** — [Overseas Shipholding Group Enters Into a Definitive Agreement to Be Acquired by Saltchuk Resources](https://www.osg.com/overseas-shipholding-group-enters-into-a-definitive-agreement-to-be-acquired-by-saltchuk-resources-inc/) (accessed 2026-07-22): Documents a 2024 agreed control transaction for a U.S.-flag liquid-bulk transportation operator at $950 million total transaction value.
- **S7** — [2022 NAICS Definition: 483111 Deep Sea Freight Transportation](https://www.census.gov/naics/?details=483111&input=483111&year=2022) (accessed 2026-07-22): Defines the industry as establishments providing deep-sea cargo transportation to or from foreign ports and includes deep-sea ship chartering with crew.
