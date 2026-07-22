# 541840 — Media Representatives

*v5 Stage 1 research memo. Run `541840-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 5.45 · L 2.93 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can reduce the proposal, research, documentation, and account-administration burden while preserving customer-facing sales coverage.
**Weakness:** Self-service digital placement and owner-dependent relationships can erode both service demand and transferability.

## Business-model lens
- Included: Independent representatives that sell media time or space for media owners and provide repeat account management, prospecting, proposal, contract, and campaign-support work to external media-owner customers.
- Excluded: Media-owner captive sales teams, media buying agencies, advertising agencies, software-only ad-placement products, non-control investments, and representatives whose work is solely a one-off transaction without a repeat outsourced-service relationship.
- Customer and revenue model: The customer is a media owner; the representative is commonly compensated through commissions or other performance-linked revenue tied to selling the owner's inventory, with recurring account relationships and campaign renewals where present.
- Deviation from default lens: none

## Executive view
Media Representatives consists of independent firms selling media time or space for media owners. The work has real administrative and proposal-generation exposure, but its transferability and demand are constrained by relationship dependence and automated digital placement.

## How AI changes the work
Advertising sales work includes prospect research, account paperwork, proposal and media-kit preparation, cost estimates, reporting, and contract drafting. Those workflows can be accelerated with controlled AI, whereas persuasion, customer discovery, negotiation, and relationship maintenance remain operator-intensive.

## Value capture
Sales compensation often includes commissions and bonuses, and sales quotas create competitive pressure. An operator may retain some productivity benefit through better account coverage and lower back-office load, but commission terms, customer pricing, and competitive service levels can pass a substantial portion through.

## Firm availability
The classification specifically covers independent representatives, which fits external outsourced service. Whether a particular lower-middle-market firm is transferable depends on assignable media-owner agreements, recurring accounts, management depth, and how much revenue remains tied to the seller-owner.

## Demand durability
BLS expects advertising-sales employment to decline as print weakens and digital placement automates, even while digital advertising grows and still uses agents. The durable portion is therefore likely concentrated in managed relationships and complex inventory rather than routine placement.

## Risks and uncertainty
No direct public measure was found for NAICS-specific transfer probability, benefit retention, operator-required quantity, or wage-weighted task exposure. The occupation evidence covers a broader workforce, and firm outcomes can vary sharply with channel mix, customer concentration, contract assignability, and self-service substitution.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4372 | — | OBSERVED | — |
| n | — | 50 | — | ESTIMATE | — |
| a | 0.3 | 0.45 | 0.6 | PROXY | S1, S2 |
| rho | 0.4 | 0.58 | 0.72 | ESTIMATE | S1, S2 |
| e | 0.65 | 0.8 | 0.9 | ESTIMATE | S3 |
| s5 | 0.05 | 0.13 | 0.25 | ESTIMATE | — |
| q | 0.25 | 0.4 | 0.55 | PROXY | S2 |
| d5 | 0.85 | 0.97 | 1.05 | PROXY | S2 |
| o | 0.45 | 0.65 | 0.8 | PROXY | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.10 | 4.56 | 7.55 | ESTIMATE |
| F | 1.55 | 2.93 | 4.03 | ESTIMATE |
| C | 5.00 | 8.00 | 10.00 | PROXY |
| D | 3.83 | 6.30 | 8.40 | PROXY |

## Caveats
- a: The occupation includes employees outside the target NAICS and omits proprietor labor.
- a: No observed wage-weighted task allocation is available for the frozen lens.
- rho: This is a judgment about realized operational adoption rather than a measured adoption rate.
- rho: AI policy, client approval requirements, and the inventory systems of media owners can vary materially by firm.
- e: The classification definition identifies activity, not recurring revenue, size-adjusted profitability, or control eligibility.
- e: The supplied firm-count input is not re-estimated here.
- s5: This is not an observed sale probability.
- s5: Owner dependence, agreement assignability, and customer concentration can create wider variation than the aggregate range conveys.
- q: BLS evidence concerns workers across the occupation rather than independent firms under the lens.
- q: Contracts may be fixed-fee, commission, salary-plus-commission, or negotiated individually.
- d5: Employment is not equivalent to constant-price service quantity.
- d5: The BLS projection spans a longer interval than the frozen horizon and covers a broader occupation.
- o: The result depends heavily on media channel, inventory complexity, and whether the media owner preserves third-party representation.
- o: No source directly measures operator-required quantity for the exact lens.

## Sources
- **S1** — [O*NET OnLine: Advertising Sales Agents](https://www.onetonline.org/link/summary/41-3011.00) (accessed 2026-07-22): Advertising-sales-agent tasks, work activities, and client-contact requirements used as an occupation proxy.
- **S2** — [BLS Occupational Outlook Handbook: Advertising Sales Agents](https://www.bls.gov/ooh/sales/advertising-sales-agents.htm) (accessed 2026-07-22): Documented duties, performance-linked compensation, employment outlook, and digital-placement automation context.
- **S3** — [U.S. Census Bureau NAICS 2022: Media Representatives](https://www.census.gov/naics/?details=541&input=541&year=2022) (accessed 2026-07-22): Official industry definition of independent representatives selling media time or space for media owners.
