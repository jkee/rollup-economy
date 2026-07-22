# 423120 — Motor Vehicle Supplies and New Parts Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.89 · L 0.41 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Frequent, SKU-rich replenishment and repair orders create repeatable AI-assisted search, fitment, pricing, forecasting, and service workflows.
**Weakness:** Direct evidence on wage-weighted task exposure, eligible independent firms, qualifying transfers, and retained AI benefit is unavailable at six-digit level.

## Business-model lens
- Included: Independent US warehouse distributors and jobbers that repeatedly source, stock, pick, sell, and deliver new motor-vehicle parts, supplies, accessories, tools, equipment, batteries, and automotive glass to other wholesalers, retailers, repair shops, fleets, and business users.
- Excluded: Manufacturer-owned or captive sales branches, commission agents and brokers, retailers, used-parts wholesalers, tire-and-tube wholesalers, shells, internal reorganizations, and businesses lacking transferable recurring customer and supplier relationships.
- Customer and revenue model: Repeat B2B customers place replenishment and repair-driven orders from stocked assortments; distributors earn product gross margin and may provide cataloging, fitment support, availability, fulfillment, delivery, returns, warranty handling, and credit.
- Deviation from default lens: none

## Executive view
New-parts distribution has a credible recurring-customer model and a meaningful information-processing layer around a physical inventory and delivery core. AI can improve fitment search, pricing, forecasting, order handling, and service, while the industry's low but nontrivial labor intensity and competitive pass-through limit the absolute retained benefit.

## How AI changes the work
The strongest applications are catalog and fitment assistance, quote and order automation, demand and replenishment suggestions, service triage, pricing support, invoice extraction, returns classification, and exception prioritization. Physical receiving, picking, delivery, warranty accountability, credit, and difficult fitment or availability decisions remain operator work.

## Value capture
Distributors can retain savings through fewer errors and returns, lower service cost, better availability, and faster inventory turns. Online price transparency, buying power, supplier programs, and repeated customer comparison will share benefits, while fast local fulfillment, specialized assortment, credit, and reliable fitment can protect some economics.

## Firm availability
Census materials identify warehouse distributors and jobbers serving wholesalers, retailers, and repair shops, which fits repeat external service. Eligibility is reduced by captive manufacturer branches and owner-dependent or concentrated businesses. The five-year control-transfer rate remains an estimate because public industry transaction data are absent.

## Demand durability
A large and growing registered vehicle stock and vehicle miles support recurring replacement-parts need. Five-year real demand should be resilient but category-specific: electrification, vehicle durability, direct sourcing, and channel consolidation may displace legacy categories or intermediaries without removing the need to supply physical parts.

## Risks and uncertainty
Public occupation and projection evidence is only available at the four-digit 423100 level, while 423120 itself spans warehouse distributors, jobbers, automotive glass and batteries, heavy-vehicle parts, tools, accessories, and petroleum-marketing equipment. Fitment errors and dirty catalogs can limit AI deployment, and inventory and supplier economics may dominate labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0635 | — | OBSERVED | — |
| n | — | 1288 | — | ESTIMATE | — |
| a | 0.19 | 0.28 | 0.38 | PROXY | S1, S2, S3 |
| rho | 0.38 | 0.57 | 0.74 | ESTIMATE | S3 |
| e | 0.38 | 0.6 | 0.77 | ESTIMATE | S1, S4 |
| s5 | 0.11 | 0.2 | 0.32 | ESTIMATE | — |
| q | 0.28 | 0.48 | 0.68 | ESTIMATE | S1, S4 |
| d5 | 0.97 | 1.07 | 1.19 | PROXY | S5, S6, S7 |
| o | 0.76 | 0.88 | 0.95 | ESTIMATE | S1, S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.18 | 0.41 | 0.71 | ESTIMATE |
| F | 6.44 | 8.12 | 9.27 | ESTIMATE |
| C | 5.60 | 9.60 | 10.00 | ESTIMATE |
| D | 7.37 | 9.42 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS covers all of NAICS 423100 rather than 423120.
- a: Occupation employment is not wage-weighted task exposure and does not measure current automation.
- a: Warehouse distributors, local jobbers, and specialty-equipment distributors have different labor mixes.
- rho: No public 423120 study measures implemented AI opportunity over five years.
- rho: Fitment errors can impose customer downtime and warranty costs, requiring human review.
- rho: Smaller firms may lack clean product and transaction histories or integration staff.
- e: Public Census materials define establishment types but do not measure the eligible LMM firm share.
- e: The broader 4231 survey indicates that manufacturer sales branches are material, but their share may differ in 423120.
- e: The dataset n is estimated from revenue classes and an external margin bridge, not observed EBITDA.
- s5: No public source measures qualifying control transfers for 423120.
- s5: Deal databases undercount small private transactions and overrepresent sponsor-backed consolidation.
- s5: Closures and internal reorganizations must not be treated as transferable opportunities.
- q: No observed study isolates retention of AI-generated benefit in 423120.
- q: Inventory purchasing gains may be cyclical or vendor-driven rather than repeatable AI benefit.
- q: Large repair chains and retailers may capture more benefit than fragmented independent customers.
- d5: Registered vehicles and miles are demand drivers, not wholesale parts purchases.
- d5: FHWA changed from estimated 2022-2023 registration data to actual state-reported data for 2024.
- d5: The BLS projection aggregates whole vehicles, new parts, tires, and used parts and measures employment rather than output.
- d5: Powertrain transition changes category demand: EVs remove some maintenance parts while adding different electronic, thermal, and chassis content.
- o: Some physical fulfillment can shift to manufacturer or third-party logistics operators rather than the current distributor.
- o: The broad OEWS physical-labor shares may not represent 423120 precisely.
- o: Standardized catalog data and platform guarantees could accelerate disintermediation.

## Sources
- **S1** — [2022 Economic Census Form: Motor Vehicle Supplies and New Parts Merchant Wholesalers](https://bhs.econ.census.gov/ombpdfs2022/export/2022_WH-42312_mu.pdf) (accessed 2026-07-22): Identifies 423120 warehouse distributors selling mainly to jobbers or wholesalers and jobbers selling mainly to retailers and repair shops; distinguishes own-account merchant wholesalers, manufacturer branches, agents, brokers, and electronic markets; asks about inventories, e-commerce, customer classes, selling methods, and technologies.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 423100](https://www.bls.gov/oes/2023/may/naics4_423100.htm) (accessed 2026-07-22): Reports 367,580 total jobs; 19.66% sales, 13.83% office/administrative support, 16.10% installation/maintenance/repair, and 29.96% transportation/material-moving employment, with detailed occupations and wages.
- **S3** — [Occupational Outlook Handbook: Wholesale and Manufacturing Sales Representatives](https://www.bls.gov/ooh/sales/wholesale-and-manufacturing-sales-representatives.htm) (accessed 2026-07-22): Describes prospecting, customer needs, pricing, negotiation, contracts, orders, follow-up, reports, and online selling; says online wholesale mostly complements face-to-face sales and AI/chatbots may limit employment growth.
- **S4** — [Motor Vehicle and Motor Vehicle Parts and Supplies Merchant Wholesalers: 2022](https://www.census.gov/content/dam/Census/library/publications/2022/econ/e22-awts.pdf) (accessed 2026-07-22): Defines the 4231 merchant model, reports that manufacturer sales branches represented 49.9% of 2022 group sales and independent merchant wholesalers 50.1%, and reports substantial sales, inventories, operating expenses, and payroll expense for the group.
- **S5** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects employment in NAICS 423100 from 381,100 in 2024 to 398,400 in 2034, an increase of 17,300 or 4.5%.
- **S6** — [FHWA Highway Statistics 2024: Motor Vehicle Traffic Fatalities, 1900-2024](https://www.fhwa.dot.gov/policyinformation/statistics/2024/fi200.cfm) (accessed 2026-07-22): Reports 297,525,836 registered vehicles and 3.294 trillion vehicle-miles in 2024, compared with 276,491,174 registered vehicles and 3.262 trillion miles in 2019.
- **S7** — [FHWA Highway Statistics 2024: Annual Vehicle-Miles of Travel, 1980-2024](https://www.fhwa.dot.gov/policyinformation/statistics/2024/vm202.cfm) (accessed 2026-07-22): Reports national annual vehicle-miles rising from 3.262 trillion in 2019 to 3.294 trillion in 2024, after the 2020 disruption.
