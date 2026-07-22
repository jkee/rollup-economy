# 532210 — Consumer Electronics and Appliances Rental

*v5.1 Stage 1 research memo. Run `532210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.09 · L 0.66 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring customer-account work and established digital decisioning create implementable opportunities across service, collections, merchandising, and planning.
**Weakness:** Physical asset operations, regulation, strong financing and retail substitutes, and unobserved LMM transfer rates constrain both implementation and confidence.

## Business-model lens
- Included: US lower-middle-market firms renting consumer electronics and household appliances to external customers, including recurring rental and lease-to-own operators using stores, e-commerce, or retail-partner channels.
- Excluded: Computer and office-equipment leasing classified in 532420, general rental centers classified in 532310, pure retailers and lenders, captive rental units, software-only financing platforms, and operators outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: Operators own or acquire durable merchandise and earn repeat weekly, biweekly, semimonthly, or monthly rental payments; customers may return merchandise or obtain ownership through renewal or early-purchase options. Revenue depends on approvals, collections, merchandise utilization and loss control, delivery, installation, repair, and resale or rerental.
- Deviation from default lens: none

## Executive view
Consumer electronics and appliance rental is an eligible repeat-service model with recurring payment streams and a meaningful mix of information work, but it remains asset-heavy, regulated, and operationally tied to delivery, repair, collections, and merchandise risk. Digital incumbents show that workflows can be automated, while mixed recent demand and strong retail or fintech substitutes limit confidence.

## How AI changes the work
AI can triage applications and collections, answer routine customer questions, personalize merchandising, draft communications, forecast inventory, and optimize delivery or recovery routes. It cannot remove merchandise ownership, physical handling, installation, repair, compliance accountability, or difficult customer exceptions.

## Value capture
Existing recurring agreements may preserve part of a productivity gain, but customers can terminate, return merchandise, or exercise early purchase options. Short commitments and competition from other rental operators, retailers, lenders, and BNPL platforms create repeated opportunities for savings to be competed away.

## Firm availability
Census defines the code around electronics and appliance rental, making the operating population conceptually coherent. The supplied LMM count is margin-bridged using an assumed 30% EBITDA margin, however, and transfer evidence for independent firms is absent.

## Demand durability
Demand for flexible access to durable goods should persist, but channel shift is substantial: Upbound reported e-commerce at 27% of Rent-A-Center lease-to-own revenue in 2025, while its Acima and store-based results moved in opposite directions. The service basket is durable but not insulated from digital and financing substitutes.

## Risks and uncertainty
The main uncertainties are the absence of six-digit task weights and deal-flow data, concentration of workflow evidence in one large public operator, the financing-like character of lease-to-own, consumer-protection constraints, merchandise losses, and the asset-heavy margin assumption embedded in the supplied firm count.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1065 | — | OBSERVED | — |
| n | — | 83 | — | ESTIMATE | — |
| a | 0.24 | 0.36 | 0.5 | ESTIMATE | S1, S2 |
| rho | 0.25 | 0.43 | 0.62 | ESTIMATE | S2 |
| e | 0.72 | 0.86 | 0.95 | ESTIMATE | S1 |
| s5 | 0.1 | 0.19 | 0.31 | ESTIMATE | — |
| q | 0.22 | 0.38 | 0.56 | ESTIMATE | S2 |
| d5 | 0.84 | 1 | 1.17 | PROXY | S2 |
| o | 0.62 | 0.78 | 0.9 | ESTIMATE | S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.26 | 0.66 | 1.32 | ESTIMATE |
| F | 3.12 | 4.31 | 5.21 | ESTIMATE |
| C | 4.40 | 7.60 | 10.00 | ESTIMATE |
| D | 5.21 | 7.80 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit wage-weighted task study was found; Upbound is a large operator with virtual and financial-health businesses, so its workflow mix may be more digitized than the LMM population.
- rho: The implementation range is judgment; the public-company source demonstrates technical feasibility but not LMM deployment rates.
- e: NAICS primary activity does not prove every firm is independent, recurring-service-led, or correctly placed in the supplied EBITDA band.
- s5: No industry-specific owner-age series or control-sale rate was found; franchise transfers and account or inventory purchases may not represent qualifying control transfers.
- q: The filing describes contract structure but does not measure pass-through of automation savings, and regulation can alter both price and product design.
- d5: Upbound includes businesses and geographies outside the lens; GMV and same-store sales are not constant-quality industry demand, and a one-year change is not a five-year forecast.
- o: The boundary between a rental operator, an embedded fintech platform, and a retailer is evolving; third-party fulfillment can move labor outside the classified firm without eliminating accountable operating work.

## Sources
- **S1** — [2022 NAICS Definition: 532210 Consumer Electronics and Appliances Rental](https://www.census.gov/naics/?input=532210&year=2022&details=532210) (accessed 2026-07-22): Defines the industry as establishments primarily renting consumer electronics and appliances such as televisions, stereos, and refrigerators; identifies appliance rental centers; and excludes computer leasing and general rental centers.
- **S2** — [Upbound Group, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/933036/000093303626000008/upbd-20251231.htm) (accessed 2026-07-22): Describes weekly through monthly payments, optional early purchase or ownership after 7-30 months, automated decision engines, e-commerce and store channels, delivery/setup and repair obligations, 27% Rent-A-Center e-commerce share in 2025, 8.6% Acima GMV growth, and a 2.2% Rent-A-Center same-store-sales decline.
