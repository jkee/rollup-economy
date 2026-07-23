# 336612 — Boat Building

*v5.1 Stage 1 research memo. Run `336612-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.85 · L 0.88 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat model platforms and dealer networks permit process automation and continuing replacement demand across a large recreational installed base.
**Weakness:** New boats are discretionary financed purchases with transparent alternatives, making volume and retained savings highly sensitive to consumer and dealer conditions.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers of motorboats, fishing boats, pontoons, rowboats, canoes, kayaks, sailboats, yachts outside shipyards, heavy-duty inflatable boats, rigid inflatable boats, and boat-yard-built unmanned or robotic watercraft for external dealers, distributors, fleets, and end customers.
- Excluded: Ship building and shipyard repair, floating-drydock repair, swimming-pool flotation devices, captive internal production, pure dealers or service yards, and manufacturers without recurring or repeat external-customer revenue.
- Customer and revenue model: Recurring or repeat outsourced revenue through dealer and distributor programs, repeat production orders, replacement models, fleet or club purchases, accessories attributable to the manufacturer, warranty, and manufacturer-provided support.
- Deviation from default lens: none

## Executive view
Boat building is a repeat-product manufacturing industry with moderate automation potential but low labor intensity and strong consumer cyclicality. Current units are depressed, dealer and financing conditions matter greatly, and physical production remains firmly operator-required.

## How AI changes the work
AI and automation can improve design iteration, quoting, forecasting, dealer support, documentation, scheduling, cutting, layup assistance, inspection, and inventory, while manual composite, finish, upholstery, assembly, testing, and customization remain labor-intensive.

## Value capture
Brands, design, dealer relationships, quality, and warranty support retention, but transparent retail pricing, promotions, dealer economics, competing models, used boats, and purchase deferral pass gains through over time.

## Firm availability
Repeat dealer, fleet, club, model, and warranty programs make many builders eligible, while one-off custom shops, captive plants, direct-only sporadic sellers, and pure dealers or service yards reduce the eligible share. Broad succession evidence suggests a material transfer pool.

## Demand durability
Boating participation and replacement provide a floor, but current new-unit demand is soft and exposed to financing, discretionary income, dealer inventory, used supply, and shared access. A partial recovery is plausible but not assured.

## Risks and uncertainty
Key risks are consumer recession, interest rates, dealer failures and destocking, floor-plan exposure, tariffs, product liability and recalls, seasonal production, model obsolescence, concentration, imports, used boats, and shared-access substitution.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1691 | — | OBSERVED | — |
| n | — | 78 | — | ESTIMATE | — |
| a | 0.14 | 0.25 | 0.37 | PROXY | S2, S3, S5 |
| rho | 0.35 | 0.52 | 0.68 | PROXY | S3, S5 |
| e | 0.43 | 0.62 | 0.78 | ESTIMATE | S1, S5 |
| s5 | 0.14 | 0.23 | 0.36 | PROXY | S4 |
| q | 0.29 | 0.46 | 0.64 | ESTIMATE | S5, S6 |
| d5 | 0.72 | 0.94 | 1.17 | PROXY | S5, S6 |
| o | 0.96 | 0.99 | 0.999 | ESTIMATE | S1, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.88 | 1.70 | PROXY |
| F | 2.80 | 4.01 | 5.04 | ESTIMATE |
| C | 5.80 | 9.20 | 10.00 | ESTIMATE |
| D | 6.91 | 9.31 | 10.00 | ESTIMATE |

## Caveats
- a: BLS combines boat plants with much larger shipyards and therefore misstates the exact occupational mix.
- a: Occupation shares are not task shares; leading-brand digital initiatives may run ahead of LMM builders.
- rho: NIST covers manufacturers generally rather than boat builders.
- rho: Brunswick is much larger and more technologically resourced than the target firms.
- e: No source directly measures the share of LMM builders meeting the exact repeat-revenue and independence tests.
- e: Large-company dealer networks and service models may not represent small custom builders.
- s5: Gallup covers employer businesses across industries rather than boat builders or the target size band.
- s5: Stated plans do not ensure a completed qualifying sale or transfer.
- q: This is discounted retained gross benefit rather than reported accounting margin.
- q: Premium brands and custom builders may retain more than volume builders competing through multi-brand dealers.
- d5: NMMA reports retail powerboats rather than all 336612 manufacturer shipments and does not provide a five-year forecast.
- d5: Brunswick is a diversified global leader whose brand mix, acquisitions, and dealer network differ from LMM builders.
- o: Used boats and sharing mainly reduce new-unit demand and are therefore reflected in d5, with only residual role displacement in o.
- o: This estimates persistence of the builder role rather than any brand or plant.

## Sources
- **S1** — [2022 NAICS Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-23): Exact 336612 boat-building scope, illustrative products, and exclusions.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Ship and Boat Building](https://www.bls.gov/oes/2023/may/naics4_336600.htm) (accessed 2026-07-23): Combined ship-and-boat occupational structure used as the wage-weighted task-exposure proxy.
- **S3** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-23): Manufacturing AI adoption, use cases, expected expansion, and barriers.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Employer-business owner age and five-year sale or transfer intentions.
- **S5** — [Brunswick Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/14930/000001493026000027/bcorp-20251231.htm) (accessed 2026-07-23): Boat manufacturing and dealer model, 2025 volume and sales changes, services and subscriptions, technology, dealer inventory, financing, parts, and market risks.
- **S6** — [Mixed Economic Conditions Shape a Stable Start To 2026 For U.S. Recreational Boating Industry](https://www.nmma.org/statistics/article/25352) (accessed 2026-07-23): Current U.S. new-powerboat unit decline, near-term outlook, pre-owned share, segment mix, participation, and shared-access context.
