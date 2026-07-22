# 532112 — Passenger Car Leasing

*v5.1 Stage 1 research memo. Run `532112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.12 · L 0.56 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring multi-period contracts and data-rich fleet administration create a practical base for AI-enabled workflow compression.
**Weakness:** Asset economics, lender constraints, and large-provider concentration can dominate the labor-saving thesis and make the estimated LMM population unreliable.

## Business-model lens
- Included: Lower-middle-market firms leasing passenger cars, light-duty passenger trucks, passenger vans, and sport utility vehicles without drivers for generally long periods, including recurring fleet-leasing and related account-management services sold to external customers.
- Excluded: Short-term passenger-car rental classified in 532111; chauffeured transportation; vehicle sales; captive internal fleet units; finance-only special-purpose vehicles; and firms outside the approximate $1-10M normalized EBITDA band.
- Customer and revenue model: Operators earn recurring lease payments over multi-month or multi-year contracts and may also charge or embed fleet-management, maintenance, telematics, compliance, fuel, and vehicle-disposal services. Customers include businesses, governments, organizations, and some individual lessees.
- Deviation from default lens: none

## Executive view
Passenger-car leasing is a recurring contractual service with a meaningful administrative layer around vehicle finance, maintenance, compliance, reporting, and disposition. AI can compress that layer, but asset funding, residual values, physical service, and customer accountability remain central and limit a purely software-led model.

## How AI changes the work
AI can assist quote and document preparation, contract extraction, maintenance and claims triage, customer communications, invoice reconciliation, compliance monitoring, fleet recommendations, and remarketing analysis. Human review remains important for credit, exceptions, safety, customer negotiation, and asset decisions.

## Value capture
Long-duration contracts can protect savings before renewal, but competitive tenders and open-book fleet programs can share benefits with customers. Retention therefore depends on contract structure and disciplined separation of labor savings from fleet depreciation and residual-value volatility.

## Firm availability
The code's operating model generally fits the external recurring-service lens, although captive and finance-only entities must be screened out. Public transaction data show equipment-rental deals exist but do not support an industry-specific transfer probability.

## Demand durability
Business and government fleets continue to need vehicles and lifecycle administration. Leasing can benefit from capital intensity and fleet complexity, while reimbursement, direct ownership, remote work, and customer insourcing create downside.

## Risks and uncertainty
The main uncertainties are the asset-heavy frozen firm-count estimate, lack of six-digit task data, concentration among large fleet managers, residual-value cycles, vehicle financing access, and the possibility that savings are competed away at renewal.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0904 | — | OBSERVED | — |
| n | — | 107 | — | ESTIMATE | — |
| a | 0.22 | 0.31 | 0.4 | ESTIMATE | S2, S3 |
| rho | 0.35 | 0.5 | 0.65 | ESTIMATE | S3 |
| e | 0.55 | 0.7 | 0.85 | ESTIMATE | S1 |
| s5 | 0.08 | 0.14 | 0.22 | ESTIMATE | S5 |
| q | 0.35 | 0.5 | 0.65 | ESTIMATE | S3 |
| d5 | 0.95 | 1.15 | 1.35 | PROXY | S4 |
| o | 0.75 | 0.88 | 0.95 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.56 | 0.94 | ESTIMATE |
| F | 2.80 | 3.93 | 4.90 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.12 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is published for 532100, not 532112, and reports employment rather than task time or AI exposure.
- a: Enterprise Fleet Management is a large-provider example whose administrative technology and service mix may not represent LMM firms.
- a: The frozen labor-share input uses 2024 wages over 2022 receipts and is harmonized to the IPS basis; it was not re-estimated.
- rho: Published technology features demonstrate digital readiness, not causal labor savings from AI.
- rho: Implementation capacity is likely lower at small regional lessors than at the cited large fleet manager.
- e: Eligibility is not measured by the NAICS definition alone.
- e: The frozen LMM count is an ESTIMATE derived with a 30% margin assumption and may misclassify asset-heavy lessors.
- s5: BizBuySell reported 31 equipment-rental-and-dealer sales in 2025, but that category is broader than 532112 and its median cash flow is below the screened EBITDA band.
- s5: The estimate excludes fleet-asset sales, lease-book financings, and internal reorganizations that do not transfer an operating company.
- q: The cited provider describes service scope but does not disclose retained automation economics.
- q: Residual-value gains or losses are asset economics and are not treated as retained AI labor benefit.
- d5: The source covers one provider in the United States and Canada, not the U.S. LMM industry.
- d5: Fleet growth can reflect provider share gains and vehicle prices rather than constant-price industry service quantity.
- o: The operator-required share is not directly reported.
- o: Large customers may unbundle financing from fleet administration more readily than small customers.

## Sources
- **S1** — [2022 NAICS Definition: 532112 Passenger Car Leasing](https://www.census.gov/naics/?chart=2022&details=532112&input=532112) (accessed 2026-07-22): Defines 532112 as establishments leasing passenger cars without drivers, generally for long periods, and includes passenger cars, light-duty passenger trucks, passenger vans, and SUVs.
- **S2** — [BLS OEWS: Largest Occupations in Automotive Equipment Rental and Leasing, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest occupations for NAICS 532100, including 62,200 counter and rental clerks, 23,960 vehicle/equipment cleaners, 12,300 bus and truck mechanics, 10,840 heavy truck drivers, 7,080 general and operations managers, and 5,790 customer service representatives.
- **S3** — [Enterprise Fleet Management: Fleet Management Services, Tracking, and Vehicle Leasing](https://www.efleets.com/en.html) (accessed 2026-07-22): Describes fleet leasing and management supported by analytics, client strategy managers, telematics, mobile tools, dashboards, real-time vehicle and cost tracking, roadside assistance, compliance, alerts, and document and claims storage.
- **S4** — [Enterprise Mobility FY2024 Growth Report](https://www.enterprisemobility.com/en/news-stories/news-stories-archive/2024/10/connecting-customers-with-mobility-solutions-drives-successful-year.html) (accessed 2026-07-22): Reports approximately 900,000 vehicles under management in the United States and Canada and a leased fleet above 720,000 vehicles, up 8% year over year.
- **S5** — [BizBuySell Insight Report Data Tables: Full-Year 2025 Transactions](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-22): Reports 31 closed transactions in the broad Equipment Rental and Dealers category during 2025, with median cash flow of $273,854, demonstrating deal activity but not an industry-specific transfer rate.
