# 812331 — Linen Supply

*v5.1 Stage 1 research memo. Run `812331-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 7.37 · L 4.20 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring contracts, tagged inventory, dense routes, and standardized plant workflows create multiple implementable data-driven efficiency levers.
**Weakness:** Most payroll supports physical processing and delivery, while public-company evidence blends adjacent industries and may overstate small-operator technology readiness and contract leverage.

## Business-model lens
- Included: US lower-middle-market operators that repeatedly rent, collect, launder, inspect, repair, replace, inventory, and deliver table and bed linens, towels, diapers, and nonindustrial uniforms, gowns, or coats to external business customers.
- Excluded: Industrial work-uniform and protective-apparel launders classified in 812332, customer-owned garment cleaning, captive hospital or hospitality laundries, direct textile sales without a recurring service, shells, non-control financing vehicles, and firms outside the lower-middle-market band.
- Customer and revenue model: Healthcare, hospitality, food service, personal-care, and other businesses pay recurring rental and service charges, commonly under multi-year agreements with scheduled pickup and replacement routes.
- Deviation from default lens: none

## Executive view
Linen supply combines high labor intensity with recurring contracts, route data, and standardized processing. AI can improve inventory, routing, inspection, pricing, service, and plant coordination, but the physical collection, laundering, finishing, and delivery system remains central.

## How AI changes the work
AI can forecast piece demand, reconcile tagged inventory, optimize routes and loads, detect stains or damage, recommend wash settings, automate invoices and service messages, predict churn, and assist plant staffing. Physical textile handling, sanitation, repair, packing, driving, and customer delivery remain substantial.

## Value capture
Multi-year contracts and switching friction can preserve some efficiency benefit, while renewals, competitive bids, service credits, and procurement sophistication share gains with customers. Large incumbents likely retain more than small local suppliers.

## Firm availability
The NAICS model fits recurring outsourced service, and public filings describe a fragmented market with active consolidators. Count quality remains uncertain because linen, industrial uniforms, ancillary products, plants, depots, and legal entities can be mixed.

## Demand durability
Healthcare, hospitality, food service, hygiene standards, and outsourcing support recurring volume. Demand still follows customer employment and occupancy, and disposables, insourcing, contract loss, or service failure can reduce route density.

## Risks and uncertainty
The main uncertainties are linen-specific versus industrial-uniform mix, plant age, route density, labor availability, utility cost, textile loss, sanitation requirements, customer concentration, contract transferability, public-company proxy bias, and the absence of direct AI productivity studies.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6267 | — | OBSERVED | — |
| n | — | 77 | — | ESTIMATE | — |
| a | 0.2 | 0.36 | 0.54 | PROXY | S2, S3 |
| rho | 0.38 | 0.62 | 0.8 | PROXY | S3 |
| e | 0.58 | 0.78 | 0.92 | ESTIMATE | S1, S3 |
| s5 | 0.1 | 0.21 | 0.34 | ESTIMATE | S3, S5 |
| q | 0.48 | 0.66 | 0.8 | PROXY | S3, S4 |
| d5 | 0.88 | 1.02 | 1.18 | PROXY | S3, S5 |
| o | 0.86 | 0.95 | 0.99 | ESTIMATE | S1, S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.91 | 5.60 | 10.00 | PROXY |
| F | 2.73 | 4.20 | 5.18 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | PROXY |
| D | 7.57 | 9.69 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET spans consumer, institutional, industrial, and linen-supply laundry workers without industry wage weights.
- a: Vestis mixes industrial uniforms, mats, supplies, and linen products and is much larger than the target population.
- a: Healthcare and hospitality linen workflows have different contamination, quality, and exception requirements.
- rho: Digital portals and predictive analytics are not direct measures of implemented AI labor substitution.
- rho: Public-company systems and capital resources may not transfer to independent operators.
- rho: Customer integration, RFID coverage, and plant equipment age vary materially.
- e: Public filings combine 812331 linen with activities classified in 812332 and other service categories.
- e: Plant, depot, route, and legal-entity counts can overstate distinct transferable firms.
- e: The supplied firm estimate is margin-bridged and may not reflect capital-intensive plant economics.
- s5: Public-company acquisition strategy does not quantify industry-wide completed transfers.
- s5: Deals may be classified as industrial uniform or facility services rather than linen supply.
- s5: No owner-age or succession distribution is observed for eligible firms.
- q: The retention metric covers Vestis's broader recurring rental portfolio rather than 812331 alone.
- q: Retention does not directly measure pass-through of automation benefits.
- q: Healthcare and hospitality procurement may exert more price pressure than the blended public-company customer base.
- d5: Nominal company revenue is not constant-price, constant-quality linen quantity.
- d5: Both public-company segments include activities outside 812331.
- d5: Customer employment and occupancy can diverge by served end market.
- o: Operator intensity differs between commodity hospitality linen and regulated healthcare textiles.
- o: Robotics and automated sorting could reduce plant labor without removing the linen-service operator.
- o: Customers may change the service basket toward disposables or owned goods rather than software-only supply.

## Sources
- **S1** — [North American Industry Classification System: Sector 81](https://www.census.gov/naics/resources/archives/sect81.html) (accessed 2026-07-22): Defines 812331 as contract or rental supply of laundered table and bed linens, towels, diapers, and specified nonindustrial uniforms or gowns, and distinguishes industrial launderers.
- **S2** — [O*NET OnLine: Laundry and Dry-Cleaning Workers](https://www.onetonline.org/link/summary/51-6011.00) (accessed 2026-07-22): Lists loading, machine operation, sorting, counting, marking, inspection, stain treatment, pressing, folding, packaging, equipment cleaning, and other physical laundry tasks.
- **S3** — [Vestis Corporation Fiscal 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1967649/000162828025054597/vsts-20251003.htm) (accessed 2026-07-22): Describes recurring weekly pickup and replacement routes, multi-year contracts and exit costs, fragmented competition, digital portals, predictive analytics, pricing and network tools, demand drivers, and a 4.4% adjusted fiscal-2025 revenue decline.
- **S4** — [Vestis Fourth Quarter Fiscal 2025 Earnings Presentation](https://www.sec.gov/Archives/edgar/data/1967649/000162828025054471/ex992vestis4q25earningsd.htm) (accessed 2026-07-22): Reports 91.8% fiscal-2025 rolling recurring-business retention and describes strategic pricing, standardized operations, logistics optimization, and planned cost savings.
- **S5** — [UniFirst Corporation Fiscal 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/717954/000119312525256222/unf-20250830.htm) (accessed 2026-07-22): Describes weekly textile-service routes, written service contracts, a competitive market with hundreds of smaller businesses, regular acquisition evaluation, technology investment, and 1.7% normalized organic growth in uniform and facility services.
