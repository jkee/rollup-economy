# 441210 — Recreational Vehicle Dealers

*v5.1 Stage 1 research memo. Run `441210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.72 · L 0.64 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A sizable recurring repair, warranty, parts, and customer-support operation provides repeat demand and AI-addressable coordination work beyond the initial RV sale.
**Weakness:** Hands-on service limits labor substitution, while highly cyclical, financing-sensitive unit sales make five-year demand and normalized dealership earnings unusually uncertain.

## Business-model lens
- Included: U.S. lower-middle-market recreational-vehicle dealers that sell new or used RVs and provide repeat external-customer service through repair, warranty work, parts and accessories, inspections, storage, consignment support, or related ownership services.
- Excluded: RV manufacturers, campgrounds, rental-only operators, independent mobile technicians and repair shops classified elsewhere, pure transactional lots without material repeat service, captive finance units, non-control financing vehicles, shells, and internal fleet-maintenance operations.
- Customer and revenue model: Households purchase or consign RVs and may return for customer-pay repairs, warranty work, parts, accessories, inspections, winterization, storage, and ownership support; revenue mixes high-ticket transactional unit sales and F&I with recurring labor, parts, and service work.
- Deviation from default lens: none

## Executive view
RV dealers have a clearer recurring-service component than many vehicle retailers: repair, warranty, parts, accessories, and ownership support sit beside high-ticket unit sales. The occupation mix still caps substitution because almost 30% of the broader dealer workforce is in hands-on installation, maintenance, and repair. Dealer AI adoption is already measurable, but near-term RV shipments have weakened sharply and normalized earnings remain difficult to assess after pandemic volatility.

## How AI changes the work
AI can improve lead and CRM follow-up, inventory content, specification and recall retrieval, estimate drafting, work-order triage, appointment intake, status updates, parts communication, bookkeeping, and management reporting. IDS finds 36% of surveyed dealers already use AI and 40% plan to. Physical inspection, diagnosis, repair, unit preparation, demonstrations, transport, and safety accountability remain labor-intensive, and poor chatbot experiences can damage trust.

## Value capture
Customer-pay service and constrained technician capacity offer better retention than competitively shopped unit sales. Warranty and insurance work are reimbursed under outside rules, and national consolidators can use technology savings to compete on price and responsiveness. A dealer should retain a majority, but not all, of implemented gross benefit over five years.

## Firm availability
The dealership buy-sell ecosystem is active, with specialist brokers, consolidators, and standardized valuation practices. Available transaction counts span multiple dealer verticals, so RV-only control-transfer incidence remains a proxy. Aged inventory, floorplan debt, real estate, manufacturer ties, and volatile EBITDA can turn an intended sale into a delayed process or asset liquidation.

## Demand durability
The latest 2026 shipment forecast is down 8.2% from 2025, reflecting financing and household-budget pressure. Against that, 8.1 million households own RVs, usage has increased, and service and repair demand follows the installed base rather than only current shipments. Physical ownership support and repair keep most surviving demand operator-required, but the five-year quantity range must remain wide.

## Risks and uncertainty
Primary risks are discretionary unit demand, interest rates, aged inventory, floorplan financing, manufacturer quality and warranty reimbursement, long repair-event cycle times, technician scarcity, geographic seasonality, and consolidation by national chains. Evidence weaknesses include the four-digit occupation proxy, vendor survey coverage, stated rather than realized purchase intent, broad dealership transaction counts, and the frozen labor ratio's vintage mismatch.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0883 | — | OBSERVED | — |
| n | — | 502 | — | ESTIMATE | — |
| a | 0.22 | 0.32 | 0.43 | PROXY | S1, S2 |
| rho | 0.4 | 0.57 | 0.71 | ESTIMATE | S2, S6 |
| e | 0.52 | 0.68 | 0.82 | ESTIMATE | S2, S6 |
| s5 | 0.11 | 0.2 | 0.3 | PROXY | S7 |
| q | 0.49 | 0.63 | 0.76 | ESTIMATE | S2, S5 |
| d5 | 0.83 | 1 | 1.16 | PROXY | S3, S4, S5 |
| o | 0.87 | 0.94 | 0.98 | ESTIMATE | S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.31 | 0.64 | 1.08 | ESTIMATE |
| F | 5.46 | 6.82 | 7.76 | ESTIMATE |
| C | 9.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.22 | 9.40 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational evidence is four-digit and includes boat, motorcycle, and other dealers.
- a: Owner and family labor at independent dealerships may be underrepresented in wage weights.
- a: AI exposure does not imply that physical repair, safety judgments, or customer accountability can be removed.
- rho: The IDS survey is North American, vendor-sponsored, and does not disclose a population-weighted U.S. LMM sample in the fetched material.
- rho: Planning to use AI is not equivalent to operational implementation or realized labor avoidance.
- rho: The estimate excludes pricing, demand, and valuation effects.
- e: The certified-technician count lacks a complete dealership denominator and includes locations rather than firms.
- e: Dealer survey priorities do not prove that every respondent already has material recurring-service revenue.
- e: The frozen firm count uses a retail margin bridge and the compensation ratio has mismatched wage and receipt vintages.
- s5: The 94 transactions span several dealership verticals and are not an RV-specific numerator.
- s5: Transactions, rooftops, and firms are different units.
- s5: Pandemic-era earnings volatility and aged inventory can delay or prevent otherwise intended transfers.
- q: No source directly measures five-year pass-through of AI savings at RV dealers.
- q: Capture differs between customer-pay service, manufacturer warranty, insurance work, F&I, and unit sales.
- q: This estimate excludes implementation difficulty and demand changes.
- d5: Wholesale shipments are not retail sales and can diverge during inventory corrections.
- d5: Strong purchase interest is not a purchase probability and is sensitive to financing and household budgets.
- d5: The dealer basket mixes cyclical vehicle sales with more durable installed-base service.
- o: The accountable operator may shift from a local dealer to a consolidated regional platform or mobile-service network.
- o: Some status communication and owner education can move entirely to software without eliminating the dealer relationship.
- o: The estimate applies to eligible service-oriented firms, not pure RV research or private-party transactions.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 441200 Other Motor Vehicle Dealers](https://www.bls.gov/oes/2023/may/naics4_441200.htm) (accessed 2026-07-22): Reports 175,690 workers and the occupation mix, including 33.15% sales, 14.22% office and administrative support, 8.00% management, 29.80% installation/maintenance/repair, and 6.88% recreational-vehicle service technicians.
- **S2** — [IDS 2026 RV Industry Trends Report](https://publications.ids-astra.com/view/569147507) (accessed 2026-07-22): Reports 2025 dealer survey AI use at 36%, planned use at 40%, and no use at 24%; documents uses in ads, estimates, and CRM, service communication workflows, service-cycle metrics, and dealer focus on customer-pay, insurance, and warranty work.
- **S3** — [RV RoadSigns Quarterly Forecast: Summer 2026](https://www.rvia.org/rv-roadsigns-quarterly-forecast) (accessed 2026-07-22): Projects 2026 wholesale shipments between 300,000 and 328,100 units with a 314,000 median, 8.2% below the 342,200 units shipped in 2025, citing household-budget and financing pressure.
- **S4** — [Go RVing 2025 RV Owner Demographic Profile and Industry Insights](https://www.rvia.org/2025-go-rving-rv-owner-demographic-profile) (accessed 2026-07-22): Reports 8.1 million RV-owning households, 16.9 million households with strong five-year purchase interest, 30 median annual use days, and 94% of transactions occurring in person.
- **S5** — [New Study Details the RV Industry's $159 Billion Economic Impact on the United States Economy](https://www.rvia.org/news-insights/new-study-details-rv-industrys-159-billion-economic-impact-united-states-economy) (accessed 2026-07-22): Reports $38 billion of RV sales and service economic output and describes downstream strength supported by 8.1 million RV-owning households despite plateauing post-pandemic shipments.
- **S6** — [RV Industry Association Publishes 2025 Annual Report](https://www.rvia.org/news-insights/rv-industry-association-publishes-2025-annual-report) (accessed 2026-07-22): Reports more than 7,500 certified RV technicians and nearly 1,000 dealerships employing at least one certified technician as of 2025.
- **S7** — [Experts Share Dealership Acquisitions Tips and Tricks](https://www.rvnews.com/experts-share-dealership-acquisitions-tips-and-tricks/) (accessed 2026-07-22): Reports 94 dealership transactions facilitated by Performance Brokerage Services in 2024 across multiple dealer verticals and details RV-dealer valuation, inventory, and transaction considerations.
