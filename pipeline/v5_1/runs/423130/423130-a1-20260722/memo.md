# 423130 — Tire and Tube Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423130-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.15 · L 0.23 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring safety- and wear-driven replacement creates repeat inventory, fitment, fulfillment, and account workflows that AI can assist.
**Weakness:** Low labor intensity and standardized, visible product pricing constrain the amount of implemented benefit that a distributor can retain.

## Business-model lens
- Included: Independent US merchant distributors and jobbers that repeatedly source, stock, sell, and deliver new or used tires and tubes for passenger, light-truck, commercial-truck, bus, industrial, off-road, farm, and other vehicles to dealers, installers, fleets, retailers, and business users.
- Excluded: Manufacturer-owned or captive sales branches, commission agents and electronic marketplaces, tire manufacturing and retreading, retail-only tire dealers, scrap processors, shells, internal reorganizations, and firms without transferable recurring accounts.
- Customer and revenue model: Repeat B2B customers purchase replacement or original-equipment tires and tubes; distributors earn product margin and may provide assortment availability, fitment support, warehousing, route delivery, emergency fulfillment, credit, returns, warranty, casing, and recall administration.
- Deviation from default lens: none

## Executive view
Tire wholesaling has durable replacement demand and a repeat-account distribution model, but only a moderate information-work layer and strong price transparency. AI can improve fitment, quoting, replenishment, service, and route decisions; bulky inventory, delivery, safety accountability, and competitive pass-through keep the opportunity operational rather than transformational.

## How AI changes the work
AI can assist size and application matching, substitutes, quotes, reorder forecasting, stock allocation, customer communications, claims and return triage, and dispatch prioritization. It cannot directly replace warehousing, loading, route delivery, condition inspection, credit risk, safety-sensitive fitment review, or exception ownership.

## Value capture
Distributors can retain gains through lower service cost, denser routes, fewer claims, and better availability. Standard SKUs, online comparison, fleet bids, manufacturer programs, and switching options push savings into price and service, while urgent fulfillment and specialty assortment offer stronger capture.

## Firm availability
Recurring dealer, installer, and fleet demand makes many independent distributors lens-compatible, but manufacturer branches, intermediaries, captive territories, and owner-dependent traders are excluded. Public evidence does not reveal the qualifying five-year transfer rate.

## Demand durability
Replacement is driven by tread wear, damage, aging, safety, and vehicle use. NHTSA and USTMA show a roughly 340-million-unit annual US market with 2025 shipments above 2019 and 2024. Demand is durable, though channel share, imports, tariffs, product life, and direct distribution can change wholesaler economics.

## Risks and uncertainty
Occupation evidence is only available for broad NAICS 423100, and manufacturer shipment data do not isolate independent wholesalers. The industry spans passenger, commercial, off-road, agricultural, industrial, new, and used tires. Inventory, supplier rebates, commodity and freight changes may overwhelm labor savings, and transparent prices may pass benefits to customers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0461 | — | OBSERVED | — |
| n | — | 417 | — | ESTIMATE | — |
| a | 0.15 | 0.23 | 0.32 | PROXY | S1, S2, S3 |
| rho | 0.36 | 0.55 | 0.72 | ESTIMATE | S3 |
| e | 0.4 | 0.63 | 0.79 | ESTIMATE | S1, S6 |
| s5 | 0.11 | 0.2 | 0.32 | ESTIMATE | — |
| q | 0.22 | 0.42 | 0.62 | ESTIMATE | S1, S3 |
| d5 | 0.95 | 1.05 | 1.15 | PROXY | S4, S5, S7 |
| o | 0.8 | 0.91 | 0.97 | ESTIMATE | S1, S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.10 | 0.23 | 0.42 | ESTIMATE |
| F | 4.77 | 6.40 | 7.51 | ESTIMATE |
| C | 4.40 | 8.40 | 10.00 | ESTIMATE |
| D | 7.60 | 9.55 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS aggregates all NAICS 423100 businesses, not tire wholesalers alone.
- a: Occupation shares are neither wage-weighted task exposure nor measures of current automation.
- a: Passenger replacement, commercial fleet, industrial, agricultural, and used-tire distributors have different workflows.
- rho: No public study measures five-year AI implementation for 423130.
- rho: Safety-sensitive fitment and load-rating decisions require reliable data and accountable review.
- rho: Smaller route distributors may have limited integration capacity and sparse clean histories.
- e: Public data do not measure eligibility among LMM firms.
- e: The broader 4231 manufacturer-branch share may differ materially for tires.
- e: The dataset n is margin-bridged rather than an observed EBITDA-band count.
- s5: No public 423130 control-transfer series was found.
- s5: Broker listings and announced transactions are biased toward larger or sale-ready companies.
- s5: Closures, internal reorganizations, and asset-only liquidations are not qualifying transfers.
- q: No observed study measures retention of AI-generated benefit in tire wholesaling.
- q: Commodity price and manufacturer rebate changes can obscure operating benefit.
- q: Capture should be lower for transparent passenger SKUs and higher for scarce commercial or specialty applications.
- d5: USTMA is a manufacturer association, and its forecast is not an independent wholesale-channel forecast.
- d5: Shipment figures are units, while d5 is constant-price, constant-quality demand for the current service basket.
- d5: Tariffs, imports, freight, fleet cycles, tire longevity, and direct manufacturer distribution can change wholesaler demand independently of miles driven.
- o: Accountable physical functions could migrate to manufacturers, platforms, or third-party logistics providers rather than disappear.
- o: The broad OEWS physical-job shares may not match 423130.
- o: Digital fitment standards and platform guarantees could reduce the independent operator role faster than expected.

## Sources
- **S1** — [2022 Economic Census Form: Tire and Tube Merchant Wholesalers](https://bhs.econ.census.gov/ombpdfs2022/export/2022_WH-42313_mu.pdf) (accessed 2026-07-22): Identifies new and used tire-and-tube wholesaling for passenger and commercial vehicles; distinguishes own-account distributors, manufacturer branches, and agents; asks about inventories, e-commerce, customer classes, selling methods, employee functions, and automation technologies.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 423100](https://www.bls.gov/oes/2023/may/naics4_423100.htm) (accessed 2026-07-22): Reports 367,580 total jobs; 19.66% sales, 13.83% office/administrative support, 16.10% installation/maintenance/repair, and 29.96% transportation/material-moving employment, with detailed occupations and wages.
- **S3** — [Occupational Outlook Handbook: Wholesale and Manufacturing Sales Representatives](https://www.bls.gov/ooh/sales/wholesale-and-manufacturing-sales-representatives.htm) (accessed 2026-07-22): Describes prospecting, needs analysis, pricing, negotiation, contracts, orders, follow-up, reports, and online selling; says online wholesale mostly complements face-to-face sales and AI/chatbots may limit employment growth.
- **S4** — [NHTSA TireWise: Tire Safety Ratings and Awareness](https://www.nhtsa.gov/vehicle-safety/tires) (accessed 2026-07-22): States that worn, damaged, irregularly worn, and aging tires require replacement; reports more than 300 million US vehicles in 2024 and approximately 340 million replacement tires purchased annually.
- **S5** — [USTMA July 2025 Forecast Predicts Higher 2025 Tire Shipments](https://www.ustires.org/newsroom/ustma-july-2025-forecast) (accessed 2026-07-22): Projects 340.2 million US tire shipments in 2025 versus 337.3 million in 2024 and 332.7 million in 2019; forecasts 2025 replacement passenger, light-truck, and truck shipments up 1.2%, 2.5%, and 3.7%.
- **S6** — [Motor Vehicle and Motor Vehicle Parts and Supplies Merchant Wholesalers: 2022](https://www.census.gov/content/dam/Census/library/publications/2022/econ/e22-awts.pdf) (accessed 2026-07-22): Defines the broader 4231 merchant model and reports manufacturer sales branches represented 49.9% of group sales while merchant wholesalers excluding those branches represented 50.1%, confirming a material captive component.
- **S7** — [FHWA Highway Statistics 2024: Annual Vehicle-Miles of Travel, 1980-2024](https://www.fhwa.dot.gov/policyinformation/statistics/2024/vm202.cfm) (accessed 2026-07-22): Reports national annual vehicle-miles of 3.294 trillion in 2024, above 3.262 trillion in 2019 and the 2020 trough.
