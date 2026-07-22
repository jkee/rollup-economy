# 423140 — Motor Vehicle Parts (Used) Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423140-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.43 · L 0.58 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can improve valuation and matching across unique salvage vehicles and parts while an aging fleet sustains repair demand.
**Weakness:** The eligible population is small and operationally risky, and much of the labor remains physical dismantling, inspection, handling, and delivery.

## Business-model lens
- Included: Independent US wholesale automotive recyclers and salvage-yard operators that acquire end-of-life or total-loss vehicles, depollute and dismantle them, identify and inventory reusable parts, and repeatedly sell and deliver used collision, mechanical, body, electrical, and major components to repair shops, dealers, rebuilders, fleets, and other business customers.
- Excluded: Retail-only self-service junkyards, scrap-only wreckers classified outside used-parts wholesaling, auction agents, rebuilders selling complete vehicles, captive internal units, shells, internal reorganizations, and firms lacking transferable operating, compliance, inventory, and customer systems.
- Customer and revenue model: Repair and collision customers buy specific used parts as lower-cost alternatives to new OEM or aftermarket parts; the operator earns part margin plus residual scrap and core value and may provide search, interchange matching, condition grading, removal, warehousing, delivery, returns, warranty, and estimating-system integration.
- Deviation from default lens: none

## Executive view
Used-parts wholesaling offers a meaningful AI layer around a labor-intensive, environmentally regulated physical process. The most promising gains are in salvage acquisition, visual and data-assisted cataloging, interchange, pricing, quoting, inventory allocation, and routing; the operator remains essential for depollution, dismantling, condition accountability, fulfillment, and warranties.

## How AI changes the work
AI can improve bid valuation, part-demand prediction, image-assisted identification and grading, interchange recommendations, listing generation, price and inventory decisions, repair-estimator integration, service triage, and delivery planning. Hidden damage, remaining life, safe fluid removal, dismantling, storage, and exception resolution still require people and equipment.

## Value capture
Unique, condition-specific inventory and local availability allow more retention than standardized new parts or tires. E-commerce and insurer-influenced repair systems increase comparison and sharing, while salvage-auction competition can capitalize expected gains into input prices.

## Firm availability
Many wholesale recyclers have recurring repair-shop accounts and transferable yards, inventory, permits, systems, and staff. Retail self-service, scrap-first, contaminated, title-risk, real-estate-led, and owner-dependent yards are not eligible. Public transfer evidence is absent despite visible industry consolidation.

## Demand durability
A large aging vehicle fleet, recurring collision and mechanical failures, and more than 10 million annual end-of-life vehicles support both demand and supply. New vehicle technology, OEM restrictions, EV architecture, insurer policy, collision frequency, total-loss thresholds, and auction concentration can materially alter which parts are reusable and economic.

## Risks and uncertainty
The occupation proxy combines all motor-vehicle and parts wholesalers, and the best direct operating disclosure comes from a scaled public company. Environmental contamination, fluids, refrigerants, batteries, titles, theft controls, hidden damage, warranties, yard real estate, and commodity exposure create diligence risk. Scarce salvage supply and auction competition may absorb better economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | OBSERVED | — |
| n | — | 181 | — | ESTIMATE | — |
| a | 0.18 | 0.27 | 0.37 | PROXY | S1, S2, S3, S5 |
| rho | 0.34 | 0.53 | 0.71 | ESTIMATE | S3, S5 |
| e | 0.38 | 0.61 | 0.78 | ESTIMATE | S1, S3, S5 |
| s5 | 0.13 | 0.23 | 0.36 | ESTIMATE | — |
| q | 0.31 | 0.52 | 0.72 | ESTIMATE | S3 |
| d5 | 0.9 | 1.05 | 1.2 | PROXY | S3, S4, S6, S7 |
| o | 0.84 | 0.94 | 0.98 | ESTIMATE | S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.25 | 0.58 | 1.07 | ESTIMATE |
| F | 3.69 | 5.27 | 6.35 | ESTIMATE |
| C | 6.20 | 10.00 | 10.00 | ESTIMATE |
| D | 7.56 | 9.87 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS covers all NAICS 423100, not used-parts wholesalers specifically.
- a: LKQ is a very large, technologically mature public operator and is not representative of a typical LMM recycler.
- a: Occupation shares and examples of current software do not directly measure wage-weighted, not-yet-automated task exposure.
- rho: No public 423140 study measures five-year AI implementation.
- rho: Computer vision cannot reliably certify hidden damage or remaining life without inspection and testing.
- rho: Data rights and access restrictions for newer software-defined vehicles may impede matching and diagnostics.
- e: Public sources define activities but do not measure the eligible LMM firm share.
- e: NAICS boundaries between wholesale used parts, retail junkyards, and scrap wholesalers may be imperfect in business records.
- e: The dataset n is margin-bridged and may misclassify asset-heavy yards with volatile scrap and salvage economics.
- s5: No public 423140 control-transfer rate was found.
- s5: Announced strategic acquisitions overrepresent scaled and compliant operators.
- s5: Asset-only yard or real-estate sales, closures, and internal reorganizations are not qualifying transfers.
- q: No observed study isolates retention of AI-generated benefit.
- q: Salvage-auction prices, scrap commodities, collision frequency, and insurer policy can swamp workflow gains.
- q: Large networks may retain more through breadth and fulfillment than independent local yards.
- d5: EPA's national salvage-flow figure is old and includes vehicles ultimately processed mainly as scrap.
- d5: Vehicle stock, age, and miles do not directly measure used-parts purchases.
- d5: LKQ's scale and product mix extend beyond 423140 and beyond the US.
- d5: Software locks, sensor calibration, battery economics, and structural casting can reduce reuse of some newer-vehicle components.
- o: Some accountable functions may be separated among auctions, dismantlers, marketplaces, logistics firms, and warranty providers.
- o: Automation may reduce headcount materially without eliminating the operator entity.
- o: Environmental and title rules vary by state and can change operating requirements.

## Sources
- **S1** — [2022 Economic Census Form: Used Motor Vehicle Parts and Supplies](https://bhs.econ.census.gov/ombpdfs2022/export/2022_WH-42314_mu.pdf) (accessed 2026-07-22): Identifies used-parts dealers including wholesale junkyards; distinguishes own-account merchant wholesalers from retail yards and other operating types; asks about inventory, e-commerce, customers, employee functions, and automation technologies.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 423100](https://www.bls.gov/oes/2023/may/naics4_423100.htm) (accessed 2026-07-22): Reports 367,580 total jobs; 19.66% sales, 13.83% office/administrative support, 16.10% installation/maintenance/repair, and 29.96% transportation/material-moving employment, with detailed occupations and wages.
- **S3** — [LKQ Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1065696/000106569626000012/lkq-20251231.htm) (accessed 2026-07-22): Describes acquiring and dismantling total-loss vehicles, software-supported salvage bidding, parts inventory and repair-estimator integration, e-commerce search/price/order tools, repair-shop customers, insurer influence, routing, warranties, limited salvage supply, technology restrictions, and physical distribution.
- **S4** — [US EPA Vehicles Product Stewardship](https://archive.epa.gov/wastes/conserve/tools/stewardship/web/html/vehicles.html) (accessed 2026-07-22): States that more than 10 million vehicles are sent to salvage yards and scrap facilities each year and approximately 75% of a vehicle by weight is metal that is recycled.
- **S5** — [Processing End-of-Life Vehicles: A Guide for Environmental Protection, Safety and Profit](https://www.epa.gov/sites/production/files/2020-10/documents/eol_vehicle_guide_final_english.pdf) (accessed 2026-07-22): Details vehicle acceptance and storage, hazardous-material removal, dismantling for usable parts, hulk storage and crushing; states that usable engine and body components can be salvaged, reconditioned, and sold to repair shops or restorers.
- **S6** — [DOE Fact of the Week 1362: Average Vehicle Age by Type, 2023](https://www.energy.gov/cmei/vehicles/articles/fotw-1362-sept-30-2024-pickup-trucks-had-highest-average-age-all-vehicle) (accessed 2026-07-22): Reports 2023 average ages of 13.1 years for pickup trucks, 12.1 for heavy trucks, 11.9 for cars, 11.8 for vans, and 8.1 for SUVs/CUVs, based on Argonne analysis of vehicles-in-operation data.
- **S7** — [FHWA Highway Statistics 2024: Motor Vehicle Traffic Fatalities, 1900-2024](https://www.fhwa.dot.gov/policyinformation/statistics/2024/fi200.cfm) (accessed 2026-07-22): Reports 297,525,836 registered vehicles and 3.294 trillion vehicle-miles in 2024, compared with 276,491,174 registered vehicles and 3.262 trillion miles in 2019.
