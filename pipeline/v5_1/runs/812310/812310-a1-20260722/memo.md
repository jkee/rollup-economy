# 812310 — Coin-Operated Laundries and Drycleaners

*v5.1 Stage 1 research memo. Run `812310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.17 · L 1.20 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat necessity demand, posted cycle pricing, and industry-specific sale intent support a durable transferable operating model.
**Weakness:** The core service is already self-automated, so the remaining AI-exposed wage pool is narrower than the business's mechanized appearance suggests.

## Business-model lens
- Included: Lower-middle-market operators of coin-, card-, or similarly operated self-service laundry and drycleaning facilities for external customers, plus firms that supply and service self-service laundry equipment in apartments, dormitories, and other third-party premises. Ancillary wash-dry-fold, pickup, delivery, and vending are included when attached to an eligible self-service operation.
- Excluded: Non-self-service drycleaning and laundry businesses classified in 812320, linen and uniform supply, equipment manufacturers, passive landlords without an operating service, captive internal laundry rooms, shells, and non-control financing vehicles.
- Customer and revenue model: Walk-in customers repeatedly buy washer and dryer cycles at posted vend prices, often supplemented by vending and attended services. Route operators receive recurring cycle revenue or contractual revenue-share from equipment placed in apartments, dormitories, or other third-party properties.
- Deviation from default lens: none

## Executive view
Coin-operated and similar self-service laundries offer durable repeat demand, posted pricing, and a visibly active store-sale market. Their main limitation is that the customer-facing service is already mechanized and self-served, leaving AI to improve a relatively narrow layer of management, support, and monitoring work rather than the core wash-and-dry process.

## How AI changes the work
AI can centralize customer messages, marketing, bookkeeping, staffing, route scheduling, performance analysis, and first-line equipment troubleshooting. It cannot replace cleaning, security, cash collection, machine repair, wash-dry-fold handling, or the physical washer and dryer capacity; modern card and app systems make integration easier than at quarter-only stores.

## Value capture
Per-cycle posted prices let operators retain savings without an automatic contractual pass-through. Local price transparency, apartment revenue shares, utility and payment costs, and the need to preserve cleanliness and uptime limit capture, but observed willingness to adjust vend prices supports moderate-to-strong retention.

## Firm availability
The typical surveyed store is far below LMM scale, so the frozen firm count likely represents multi-store or route platforms produced by a margin bridge rather than directly observed eligible firms. Most true 812310 platforms fit the service lens, and industry-specific sale intentions suggest transfer activity, though individual store sales do not always convey company control.

## Demand durability
Laundry is a recurring necessity and broad-industry constant-dollar output is projected to grow modestly. Demand is local and tied to renter density and access to in-unit equipment; physical sites and machines remain operator-required even when payment, monitoring, and customer interaction become more digital.

## Risks and uncertainty
Major risks are overstated LMM firm counts from the broad margin assumption, weak cash controls and seller records, aging equipment, lease renewal, water and energy cost exposure, vandalism, local competition, and store-level demand loss when housing adds in-unit laundry. The trade survey's low response rate and heavy inclusion of ancillary wash-dry-fold services also limit generalization.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2195 | — | OBSERVED | — |
| n | — | 25 | — | ESTIMATE | — |
| a | 0.12 | 0.22 | 0.34 | PROXY | S2, S3 |
| rho | 0.42 | 0.62 | 0.78 | ESTIMATE | S3 |
| e | 0.65 | 0.82 | 0.93 | ESTIMATE | S1, S3 |
| s5 | 0.24 | 0.38 | 0.54 | PROXY | S3 |
| q | 0.48 | 0.66 | 0.8 | ESTIMATE | S3 |
| d5 | 0.98 | 1.08 | 1.18 | PROXY | S4, S5 |
| o | 0.91 | 0.97 | 0.995 | ESTIMATE | S1, S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.44 | 1.20 | 2.33 | ESTIMATE |
| F | 2.56 | 3.50 | 4.19 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.92 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is four-digit and dominated by non-self-service laundry production work.
- a: The CLA survey had 377 usable responses and a 6% response rate, and it is not restricted to the LMM band.
- a: Owner labor is omitted from the survey payroll ratio and may contain exposed management tasks.
- rho: Digital payment adoption is an enabling condition, not a measured AI implementation rate.
- rho: Legacy coin-only stores and route contracts may be slower to integrate than modern card-based stores.
- e: The frozen n=25 is an ESTIMATE based on a broad-sector margin bridge, not observed laundry-company EBITDA.
- e: The industry survey is store-oriented and may underrepresent larger route operators.
- e: Ancillary wash-dry-fold revenue can blur the boundary with 812320.
- s5: The survey had a 6% response rate and may attract more transaction-oriented owners.
- s5: Plans are not completed transactions, and selling one store may not transfer control of a multi-store company.
- s5: The survey includes firms below the LMM band.
- q: Expected general price increases do not directly measure pass-through of automation savings.
- q: Route revenue-share contracts may capture benefits differently from store-level posted pricing.
- d5: BLS publishes the projection only at four-digit 812300, not 812310.
- d5: Trade-association demand claims are directional and not a constant-quality volume series.
- d5: In-unit machines, improved apartment amenities, and household migration can reduce local laundromat demand.
- o: This primitive concerns the need for an accountable operator, not whether customers operate machines themselves.
- o: Route laundries and retail laundromats face different bypass risks.

## Sources
- **S1** — [2022 NAICS Definition: 812310 Coin-Operated Laundries and Drycleaners](https://www.census.gov/naics/?details=812&input=812&year=2022) (accessed 2026-07-22): Industry boundary covering self-service facilities and firms that supply and service self-service laundry equipment at third-party premises.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 812300 Drycleaning and Laundry Services](https://www.bls.gov/oes/2023/may/naics4_812300.htm) (accessed 2026-07-22): Broader-industry occupation mix, including production, office support, management, customer service, cleaning, and machine-maintenance work.
- **S3** — [2024 CLA Laundry Industry Survey Results](https://member.laundryassociation.org/hubfs/IndustrySurvey24.pdf?hsLang=en) (accessed 2026-07-22): Self-service store ownership, one-year sale plans, staffing and payroll, payment methods, vend-price intentions, operating concerns, revenue, and survey methodology.
- **S4** — [Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Broader 812300 real-output projection and compound annual output growth.
- **S5** — [Industry Overview - CLA, The Laundry Association](https://laundryassociation.org/for-investors/industry-overview/) (accessed 2026-07-22): Self-service and route-laundry business models, necessity character, and relationship of demand to population density and rental housing.
