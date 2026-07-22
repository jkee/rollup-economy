# 812320 — Drycleaning and Laundry Services (except Coin-Operated)

*v5.1 Stage 1 research memo. Run `812320-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.10 · L 1.56 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A meaningful labor bill and repetitive intake, inspection, scheduling, and customer workflows create a bounded automation opportunity around the physical plant.
**Weakness:** Most production work handles irregular textiles physically, while traditional dry-cleaning demand and regulatory equipment costs can erode the benefit.

## Business-model lens
- Included: US lower-middle-market operators that repeatedly clean, press, finish, receive, collect, or deliver customer-owned garments and household textiles through staffed plants, stores, routes, or drop sites.
- Excluded: Coin- or card-operated self-service laundries, linen and uniform rental, carpet and upholstery cleaning, captive institutional laundries, passive drop-site property entities, shells, non-control financing vehicles, and firms outside the lower-middle-market band.
- Customer and revenue model: Households and small commercial accounts usually pay per item, per bag, by weight, or through recurring pickup and delivery plans for garment and textile cleaning.
- Deviation from default lens: none

## Executive view
Garment care has a high labor share, but most plant labor is physical handling, finishing, and exception work rather than purely cognitive administration. AI can improve intake, visual inspection, routing, customer service, and process control while regulatory equipment transition and uneven demand limit implementation.

## How AI changes the work
AI can classify garments and stains, suggest treatment, detect finishing defects, forecast workload, automate order messages, optimize routes, and assist pricing and scheduling. Loading, sorting, pressing, spotting, folding, maintenance, and accountable custody remain equipment- and labor-intensive.

## Value capture
Per-item and subscription pricing permits some savings retention, but low switching costs and local competition encourage faster service, promotions, pickup convenience, and lower effective prices. Capital and compliance costs may consume much of the gain.

## Firm availability
The code broadly fits the repeat-service lens, yet plant, route, storefront, and specialty-cleaning models differ materially. Environmental liabilities, owner dependence, and affiliated drop sites reduce the share of countable firms that are transferable platforms.

## Demand durability
Household laundry outsourcing and pickup delivery can support volume, while traditional dry cleaning faces washable clothing, casual dress, and home laundering. The physical service survives for selected garments and convenience users, but mix shift is central.

## Risks and uncertainty
Key risks are physical-task dominance, unproven robotics economics, PCE replacement costs, contaminated-site liabilities, water and energy expense, garment damage, route density, lease transfer, owner dependence, and the absence of segment-level volume or transaction data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3902 | — | OBSERVED | — |
| n | — | 94 | — | ESTIMATE | — |
| a | 0.12 | 0.25 | 0.4 | PROXY | S2, S4 |
| rho | 0.2 | 0.4 | 0.65 | ESTIMATE | S4 |
| e | 0.68 | 0.84 | 0.95 | ESTIMATE | S1 |
| s5 | 0.09 | 0.19 | 0.32 | ESTIMATE | — |
| q | 0.35 | 0.55 | 0.72 | ESTIMATE | — |
| d5 | 0.78 | 0.95 | 1.12 | PROXY | S3 |
| o | 0.72 | 0.88 | 0.97 | ESTIMATE | S1, S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.37 | 1.56 | 4.06 | ESTIMATE |
| F | 3.07 | 4.46 | 5.45 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 5.62 | 8.36 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET covers laundry workers across household, industrial, and institutional settings rather than this NAICS lens alone.
- a: The task source provides no wage or time weights and underrepresents sales, route, and office work.
- a: EPA's description applies only to facilities using PCE and not to wet-cleaning or other solvent systems.
- rho: No source measures five-year AI implementation in independent dry cleaners.
- rho: Plant age and information-system quality vary materially.
- rho: Regulatory equipment replacement can either accelerate modernization or crowd out automation investment.
- e: The code combines cleaning plants, drop stores, pickup sites, specialty cleaners, and laundries with different transferability.
- e: Environmental liabilities and below-market real-estate leases can make an otherwise operating firm ineligible.
- e: The supplied firm estimate is margin-bridged and may count establishments or affiliated entities differently from acquisition targets.
- s5: No observed deal-flow or owner-succession rate is available for the lens.
- s5: Store sales may exclude the processing plant or customer routes and may not transfer a durable operation.
- s5: PCE conversion and environmental diligence can turn intended sales into closures.
- q: No public evidence measures automation benefit retention in retail garment care.
- q: Premium specialty cleaning and commodity wash-and-fold have different pricing power.
- q: Savings may be absorbed by solvent transition, utilities, rent, insurance, and delivery costs.
- d5: Occupational employment is not constant-price, constant-quality service demand.
- d5: The occupation includes industries and customer segments outside 812320.
- d5: The split between traditional dry cleaning and pickup laundry is not observed.
- o: Operator requirement is lower for standardized wash-and-fold than for specialty garments.
- o: Robotic sorting and finishing could advance faster than assumed.
- o: PCE restrictions change cleaning technology but do not directly indicate future customer quantity.

## Sources
- **S1** — [2022 NAICS Definition: 812320 Drycleaning and Laundry Services (except Coin-Operated)](https://www.census.gov/naics/?details=812320&input=812320&year=2022) (accessed 2026-07-22): Defines staffed dry-cleaning, laundry, pickup and drop-off, and specialty garment-cleaning activities and distinguishes self-service laundry, linen supply, and carpet cleaning.
- **S2** — [O*NET OnLine: Laundry and Dry-Cleaning Workers](https://www.onetonline.org/link/summary/51-6011.00) (accessed 2026-07-22): Lists machine loading and operation, sorting and counting, marking, stain and fabric inspection, spotting, pressing, folding, packaging, maintenance, and material-handling tasks.
- **S3** — [BLS Occupational Projections and Worker Characteristics, 2024-2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Projects laundry and dry-cleaning worker employment from 202.6 thousand in 2024 to 213.5 thousand in 2034, a 5.4% increase, across the broad occupation.
- **S4** — [EPA Guide to Complying with the 2024 PCE Dry Cleaning Regulation](https://www.epa.gov/system/files/documents/2025-01/pce-dry-cleaner-compliance-guide.pdf) (accessed 2026-07-22): Describes manual loading, unloading, stain removal, solvent handling, maintenance, recordkeeping, alternative cleaning systems, and the staged prohibition of PCE in dry cleaning.
