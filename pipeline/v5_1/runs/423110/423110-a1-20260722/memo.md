# 423110 — Automobile and Other Motor Vehicle Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.22 · L 0.08 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat dealer and fleet workflows create automatable pricing, documentation, matching, and customer-service work around a durable physical transaction.
**Weakness:** The dataset labor ratio is only 1.7%, and neither the eligible independent-firm share nor qualifying five-year control-transfer rate is directly observed.

## Business-model lens
- Included: Independent US merchant wholesalers that repeatedly source, take title to, market, and distribute new or used passenger vehicles, trucks, trailers, motorcycles, recreational vehicles, and similar motor vehicles to dealers, fleets, and other business buyers.
- Excluded: Manufacturer-owned or otherwise captive sales branches, retail dealerships, auction-only agents and brokers classified outside merchant wholesale, shells, internal reorganizations, and firms without transferable operating relationships.
- Customer and revenue model: Business customers buy vehicles for resale or fleet use; the wholesaler earns an inventory spread or gross margin and may bundle inspection, reconditioning coordination, title administration, financing support, and transport coordination into repeat account relationships.
- Deviation from default lens: none

## Executive view
Vehicle merchant wholesaling combines a modest AI-addressable commercial and administrative layer with a much larger physical, inventory-risk, and relationship-intensive operating core. The clearest opportunity is workflow augmentation in sourcing, pricing, documentation, customer service, and order handling, not removal of the accountable distributor.

## How AI changes the work
AI can monitor markets, draft listings and communications, match vehicle specifications to buyer needs, extract title and condition data, prioritize leads, and triage order or logistics exceptions. It is less able to replace physical inspection, movement, repair coordination, inventory financing, negotiation, and responsibility for condition or title disputes.

## Value capture
Taking title creates room to retain savings through overhead reduction, faster inventory turns, fewer errors, and improved matching. Retention is constrained by transparent market prices, auctions and digital platforms, dealer bargaining, and repeated repricing, so a material part of gross benefit is likely competed into spreads or service levels.

## Firm availability
The code includes true merchant operators, but only a subset of LMM firms are independent, recurring-account businesses with a transferable organization beyond the owner. Public evidence does not reveal control-transfer frequency; succession and consolidation may create supply, while closures, family transfers, and inventory-only liquidations do not qualify.

## Demand durability
Vehicle replacement, fleet needs, dealer inventory, and resale turnover support continuing wholesale demand, with BLS's broader 423100 outlook pointing to modest employment growth. The channel is cyclical and sensitive to financing, supply, and trade policy, but physical transfer, title, inspection, and exception accountability make full software elimination unlikely within five years.

## Risks and uncertainty
The largest evidence weakness is that public occupation and outlook data aggregate all motor-vehicle and parts wholesalers, while the target code mixes passenger vehicles, trucks, trailers, motorcycles, RVs, and other vehicles. The estimated eligible and transferable populations are unobserved, and inventory economics can dominate labor savings. A platform-led shift in title, inspection, and guarantees could reduce the operator-required share.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.017 | — | OBSERVED | — |
| n | — | 1569 | — | ESTIMATE | — |
| a | 0.16 | 0.24 | 0.33 | PROXY | S2, S3 |
| rho | 0.32 | 0.5 | 0.68 | ESTIMATE | S3 |
| e | 0.12 | 0.32 | 0.5 | ESTIMATE | S1, S6 |
| s5 | 0.1 | 0.19 | 0.31 | ESTIMATE | — |
| q | 0.25 | 0.45 | 0.65 | ESTIMATE | S6 |
| d5 | 0.88 | 1.03 | 1.16 | PROXY | S1, S4, S5 |
| o | 0.68 | 0.82 | 0.92 | ESTIMATE | S2, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.03 | 0.08 | 0.15 | ESTIMATE |
| F | 4.81 | 7.35 | 8.84 | ESTIMATE |
| C | 5.00 | 9.00 | 10.00 | ESTIMATE |
| D | 5.98 | 8.45 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is for NAICS 423100, combining vehicle wholesalers with new-parts, tire, and used-parts wholesalers.
- a: OEWS occupation shares do not directly measure tasks, task time, current automation, or wage-weighted exposure.
- a: The vehicle-wholesale mix ranges from relationship-led fleet sales to highly transactional used-vehicle trading.
- rho: No industry study measures five-year implementation of AI in 423110.
- rho: Vendor demonstrations may omit integration, data-rights, and exception-handling costs.
- rho: Implementation will differ sharply between digitally mature auction-linked firms and small relationship-led wholesalers.
- e: No public source measures the eligible share of LMM 423110 firms.
- e: NAICS establishment definitions do not identify captive status, transferability, recurring customers, or normalized EBITDA.
- e: The dataset n is margin-bridged and may be particularly noisy in a high-revenue, inventory-intensive vehicle trade.
- s5: No public 423110 control-transfer rate was found.
- s5: Observed broker listings would be selection-biased toward sale-ready firms.
- s5: Owner age alone would not distinguish a qualifying control sale from closure or family succession.
- q: There is no observed benefit-sharing study for this industry.
- q: Inventory gains and losses can swamp operating savings and obscure retention.
- q: Capture may be lower in transparent commodity-like channels and higher in specialized vehicles or constrained supply.
- d5: The forward BLS figure is employment, not constant-price demand, and covers all of 423100.
- d5: The historical output series spans multiple cycles and does not isolate 423110.
- d5: Interest rates, tariffs, vehicle supply, fleet cycles, and changes in dealer inventory practices create substantial five-year volatility.
- o: The physical occupation shares are for 423100 and may reflect parts and tire distribution more than vehicle wholesaling.
- o: Some accountable functions can be supplied by auctions, logistics firms, or platforms rather than the merchant wholesaler itself.
- o: Legal and market conventions around digital title, remote inspection, and platform guarantees could change faster than assumed.

## Sources
- **S1** — [2022 NAICS Definition: 423110 Automobile and Other Motor Vehicle Merchant Wholesalers](https://www.census.gov/naics/?details=423110&input=423110&year=2022) (accessed 2026-07-22): Defines 423110 as merchant wholesale distribution of new and used passenger automobiles, trucks, trailers, motorcycles, motor homes, snowmobiles, and other motor vehicles.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 423100](https://www.bls.gov/oes/2023/may/naics4_423100.htm) (accessed 2026-07-22): Reports 367,580 total jobs; 19.66% sales, 13.83% office/administrative support, 16.10% installation/maintenance/repair, and 29.96% transportation/material-moving employment, with detailed occupations and wages.
- **S3** — [Occupational Outlook Handbook: Wholesale and Manufacturing Sales Representatives](https://www.bls.gov/ooh/sales/wholesale-and-manufacturing-sales-representatives.htm) (accessed 2026-07-22): Describes prospecting, needs analysis, price and term negotiation, contracts, orders, follow-up, reporting, and web-enabled selling; states that online sales mostly complement face-to-face selling and that AI and chatbots may limit employment growth.
- **S4** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects employment in NAICS 423100 from 381,100 in 2024 to 398,400 in 2034, an increase of 17,300 or 4.5%.
- **S5** — [BLS Long-term Percent Change in Hours, Output, and Employment](https://www.bls.gov/charts/productivity-wholesale-retail/long-term-percent-change-hours-and-output-and-employment.htm) (accessed 2026-07-22): Reports 2.9% average annual output growth for motor vehicles and parts wholesale over 1987-2025 and current employment of 379,100.
- **S6** — [Annual Wholesale Trade Survey: Purpose, Coverage, and Content](https://www.census.gov/econ/overview/wh0200.html) (accessed 2026-07-22): States that covered merchant wholesalers take title to goods they sell and reports sales, inventories, purchases, operating expenses, and e-commerce; excludes agents, brokers, commission merchants, and non-wholesale businesses.
