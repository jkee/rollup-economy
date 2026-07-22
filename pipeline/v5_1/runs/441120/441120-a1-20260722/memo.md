# 441120 — Used Car Dealers

*v5.1 Stage 1 research memo. Run `441120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.42 · L 0.95 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Language- and data-heavy sales, merchandising, finance, and collections workflows offer implementable labor savings at dealers with genuine recurring customer relationships.
**Weakness:** Only a minority of used-car dealers clearly supply a material recurring service, while transparent pricing and scaled online competitors pressure benefit retention.

## Business-model lens
- Included: U.S. lower-middle-market used-car dealers with a material recurring or repeat external-customer service, such as dealer-held installment servicing, repair and warranty administration, or an integrated customer-pay service operation, alongside vehicle retail.
- Excluded: Purely transactional vehicle lots without a material repeat service, private-party marketplaces, franchised new-car dealers, captive or separate non-control finance vehicles, rental-fleet disposals, wholesalers, shells, and independent repair shops classified outside 441120.
- Customer and revenue model: Consumers buy used vehicles and may also purchase financing, vehicle-service contracts, warranties, or repair services; eligible dealers earn repeat revenue through loan servicing and collections or through ongoing service and warranty relationships, while vehicle gross profit remains transactional.
- Deviation from default lens: none

## Executive view
Used-car dealers have substantial AI-addressable sales, merchandising, finance, collections, and administrative work, and technology-native operators prove that many customer workflows can be digitized. The central limitation is scope: most used-car dealers are transactional retailers, so only the minority with material dealer-held loan servicing, warranty administration, repair, or another repeat service belongs in the screen. Competition is transparent and online, and the frozen revenue-to-EBITDA bridge is unusually sensitive to inventory economics.

## How AI changes the work
AI can accelerate lead response, listings, price comparisons, vehicle-history summaries, document extraction, finance application review, payment reminders, collections prioritization, call handling, and bookkeeping. Physical appraisal, reconditioning, transport, title exceptions, customer trust, and accountable credit decisions remain operator-intensive. Small dealers may implement packaged tools quickly, but fragmented systems and regulated decisions require review and governance.

## Value capture
There is no contractual obligation to pass labor savings to buyers, yet consumers compare many sites before contacting a dealer and advertised prices are visible. Vehicle-margin savings should be competed away faster than gains in dealer-held servicing, collections, warranty, or repair. Online leaders also use lower operating costs to improve price and convenience, setting a demanding benchmark for local operators.

## Firm availability
Transferability is real but poorly measured. BizBuySell reported 20 car-dealership sales in 2025, a visibly incomplete and below-band slice. Independent dealers avoid OEM franchise approval, but floorplan debt, licenses, inventory quality, real estate, dealer-held receivables, and owner-dependent sourcing can make a control transfer difficult or turn it into an asset liquidation.

## Demand durability
The used market is large and necessity-driven, with 38.6 million estimated total sales in 2025 and a near-flat 2026 forecast. Affordability supports used demand, but late-model supply, credit availability, and online channel shifts create risk for independent firms. The eligible subset's physical and regulated activities still require an accountable operator even when discovery and paperwork become self-service.

## Risks and uncertainty
Key uncertainties are the eligible-firm share, the absence of direct six-digit occupation data, and sparse control-transfer evidence. Commercial risks include wholesale inventory volatility, floorplan rates, credit losses, deceptive-pricing and disclosure enforcement, title fraud, cybersecurity, online platform scale, weak repeat loyalty, and the possibility that recurring finance or service functions sit in separate entities excluded by the lens.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0972 | — | OBSERVED | — |
| n | — | 1213 | — | ESTIMATE | — |
| a | 0.3 | 0.42 | 0.54 | PROXY | S1, S6 |
| rho | 0.4 | 0.58 | 0.72 | ESTIMATE | S5, S6 |
| e | 0.12 | 0.25 | 0.4 | ESTIMATE | S2, S4, S5 |
| s5 | 0.06 | 0.12 | 0.2 | PROXY | S7 |
| q | 0.42 | 0.57 | 0.71 | ESTIMATE | S3, S6 |
| d5 | 0.93 | 1.01 | 1.1 | PROXY | S2, S3, S8 |
| o | 0.78 | 0.88 | 0.95 | ESTIMATE | S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.47 | 0.95 | 1.51 | ESTIMATE |
| F | 3.66 | 5.83 | 7.38 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.25 | 8.89 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation table is dominated by the broader automobile-dealer population and does not isolate 441120.
- a: Commission compensation and owner labor complicate wage weighting at independent dealers.
- a: Carvana demonstrates technical feasibility at a scaled online operator, not the average LMM dealer's current task mix.
- rho: No representative study directly measures five-year implementation among LMM independent dealers.
- rho: A technology-native public company may overstate implementation capacity for smaller acquired dealerships.
- rho: The estimate excludes competitive pass-through and demand effects.
- e: Financing-channel shares are not dealer-count shares and cannot identify which LMM firms retain receivables.
- e: A sold service contract may create only a one-time commission rather than a recurring outsourced service.
- e: The frozen firm count uses a retail margin bridge that may misclassify high-revenue, inventory-intensive dealerships.
- s5: BizBuySell captures only a nonrandom slice of small-business transactions.
- s5: Reported car-dealership sales are not isolated to used-car dealers or the LMM EBITDA band.
- s5: No direct owner-age or succession survey for eligible independent dealers was found.
- q: No source directly measures AI-benefit pass-through or five-year repricing.
- q: Retention differs materially between transparent vehicle margins and recurring loan or repair economics.
- q: The estimate excludes implementation difficulty and volume loss.
- d5: Industry unit sales do not directly measure repeat service quantity at eligible dealers.
- d5: Used supply depends on prior new-vehicle production, leasing, trade-ins, and fleet disposals.
- d5: Channel share can shift rapidly toward franchised or scaled online sellers even if total used demand is stable.
- o: The operator may be centralized and online rather than a traditional local lot.
- o: Separate third-party lenders, servicers, warranty administrators, and repair shops can disaggregate the current dealer bundle.
- o: The estimate is conditional on the eligible recurring-service subset, not all used-car transactions.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 441100 Automobile Dealers](https://www.bls.gov/oes/2023/may/naics4_441100.htm) (accessed 2026-07-22): Reports the four-digit automobile-dealer occupation mix, including 33.48% sales, 14.56% office and administrative support, 6.77% management, and 25.07% installation, maintenance, and repair employment.
- **S2** — [NIADA's UCIR Shows Independent Used Sales Top 9.8 Million in 2025](https://niada.com/dashboard/niadas-ucir-shows-independent-used-sales-top-9-8-million-in-2025/) (accessed 2026-07-22): Reports 9.8 million independent-dealer used sales and 38.6 million total used sales in 2025; also reports a 32.6% BHPH/other share of independent-dealer financing and 34% of originations in deep-subprime and subprime segments.
- **S3** — [Cox Automotive Research: Independent Buyers Driven by Necessity, Not Aspiration](https://niada.com/dashboard/cox-automotive-research-independent-buyers-driven-by-necessity-not-aspiration/) (accessed 2026-07-22): A 384-buyer study reports 79% need rather than want a vehicle, 16.5 average online research hours, more than five sites visited, 77% third-party-listing use, and only 21% intent to return to the same dealership.
- **S4** — [Federal Reserve Consumer & Community Context: Vehicle Financing](https://www.federalreserve.gov/publications/2023-november-consumer-community-context.htm) (accessed 2026-07-22): Defines independent and BHPH dealers, reports that 38% of used-vehicle sales were financed in first-half 2023, and that BHPH dealers originated about 6% of 2022 auto loans.
- **S5** — [Federal Trade Commission Dealer's Guide to the Used Car Rule](https://www.ftc.gov/business-guidance/resources/dealers-guide-used-car-rule) (accessed 2026-07-22): Details mandatory Buyers Guide disclosures, dealer and warranty information, warranty cost coverage, service contracts, and compliance duties for dealers selling more than five used vehicles annually.
- **S6** — [Carvana Co. 2025 Annual Report on Form 10-K](https://www.sec.gov/Archives/edgar/data/1690820/000169082026000009/cvna-20251231.htm) (accessed 2026-07-22): Describes a vertically integrated e-commerce model, technology across inventory, merchandising, financing, logistics, and delivery, deployment of automated self-service and AI-enabled support, a 37-million-transaction 2024 market, and 596,641 retail units sold in 2025.
- **S7** — [BizBuySell Insight Report Data Tables: Full-Year 2025](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-22): Reports 20 car-dealership transactions in 2025, with $690,000 median sale price, $2.388 million median revenue, $250,000 median cash flow, and 245 median days on market.
- **S8** — [Used Vehicle Sales Expected to Dip in 2026](https://niada.com/dashboard/used-vehicle-sales-expected-to-dip-in-2026/) (accessed 2026-07-22): Reports Cox Automotive's forecast for 2026 total used sales to decline 0.9% to 38.3 million and retail used sales to decline 0.7% to 20.3 million after the market ended 2025 2.7% above 2024.
