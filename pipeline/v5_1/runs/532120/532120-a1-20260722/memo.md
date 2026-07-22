# 532120 — Truck, Utility Trailer, and RV (Recreational Vehicle) Rental and Leasing

*v5.1 Stage 1 research memo. Run `532120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.56 · L 1.09 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Physical asset accountability makes demand hard to replace entirely while data-rich fleet workflows offer targeted automation potential.
**Weakness:** Capital intensity and physical maintenance limit labor leverage, and the code's mixed customer and contract models widen every commercial estimate.

## Business-model lens
- Included: Lower-middle-market firms renting or leasing trucks, truck tractors, buses, semi-trailers, utility trailers, or recreational vehicles without drivers to external commercial or consumer customers, including repeat short-term rental and recurring full-service lease relationships.
- Excluded: Light-duty passenger-truck and SUV rental or leasing classified in 53211; rentals with drivers; dealer sales; captive internal fleets; passive financing vehicles; and firms outside the approximate $1-10M normalized EBITDA band.
- Customer and revenue model: The code mixes short-duration transaction revenue from consumer and commercial rentals with multi-year commercial leases and bundled maintenance, fuel, compliance, and digital fleet services. Customers pay time- and usage-based rental charges or recurring lease and service fees.
- Deviation from default lens: none; the full default population is retained despite the code's short-term consumer and long-term commercial submodels, with uncertainty represented in the primitive ranges

## Executive view
Truck, trailer, and RV rental and leasing combines a durable physical-asset service with automatable reservation, contract, maintenance, billing, and fleet workflows. The opportunity is constrained by substantial physical labor, capital intensity, cyclical utilization, and a heterogeneous mix of multi-year B2B leases and short-term consumer transactions.

## How AI changes the work
AI can improve quoting, reservation support, contract extraction, dispatch, maintenance prediction and authorization, damage triage, invoice reconciliation, customer communication, compliance monitoring, and fleet utilization. It has limited reach into cleaning, repairs, inspections, vehicle movement, roadside work, and physical handoffs.

## Value capture
Existing long-term contracts and flexible short-term prices can retain some workflow benefit, but tendered fleet accounts, transparent consumer pricing, renewal competition, credits, and technology costs create pass-through. Retention should be tested separately by submodel.

## Firm availability
Most operating lessors and rental firms fit the external-service lens, but passive fleet owners and finance structures require screening. Broad equipment-rental deal data establish a market without supporting a reliable five-year industry transfer probability.

## Demand durability
Businesses need flexible capacity and outsourced fleet support, while consumers continue to rent moving equipment and RVs. Freight cycles, housing moves, travel demand, fleet ownership economics, and branch utilization make quantity more volatile than the recurring lease base suggests.

## Risks and uncertainty
Key risks are the 30% margin assumption behind the frozen firm count, fleet financing and residual values, maintenance and safety liabilities, cyclicality, large-operator evidence bias, and mixing commercial leases with consumer rentals in one code.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2268 | — | OBSERVED | — |
| n | — | 250 | — | ESTIMATE | — |
| a | 0.16 | 0.24 | 0.32 | ESTIMATE | S2, S3, S4 |
| rho | 0.35 | 0.5 | 0.65 | ESTIMATE | S3, S4 |
| e | 0.6 | 0.75 | 0.9 | ESTIMATE | S1 |
| s5 | 0.08 | 0.13 | 0.2 | ESTIMATE | S5 |
| q | 0.35 | 0.5 | 0.65 | ESTIMATE | S3, S4 |
| d5 | 0.9 | 1.08 | 1.25 | PROXY | S3, S4 |
| o | 0.82 | 0.92 | 0.97 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.51 | 1.09 | 1.89 | ESTIMATE |
| F | 4.13 | 5.20 | 6.16 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.38 | 9.94 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is for 532100 and does not isolate 532120 or measure task exposure.
- a: Ryder and U-Haul are large-company examples and may have more automation than LMM operators.
- rho: Digital platforms and structured contracts show readiness but do not establish realized AI labor substitution.
- rho: Results may differ sharply between multi-year truck fleets and branch-based consumer RV or trailer rentals.
- e: Eligibility within the estimated LMM population is not observed.
- e: The frozen n value depends on a round 30% EBITDA-margin assumption that may misclassify capital-intensive firms.
- s5: BizBuySell's 31 reported Equipment Rental and Dealers sales in 2025 combine industries and are mostly below the target EBITDA band.
- s5: Fleet disposals, lease-book transfers, franchise changes, and internal reorganizations are excluded from qualifying control transfers.
- q: The cited filings describe contract structures but not the retained share of automation benefits.
- q: Pricing power differs materially between bespoke commercial leases and price-transparent consumer rentals.
- d5: U-Haul mixes truck and trailer rentals with other businesses, and revenue changes include price and mix.
- d5: Ryder is a large commercial fleet company and its conditions may not represent consumer RV or trailer operators or LMM firms.
- o: No source directly measures operator substitution for the full 532120 basket.
- o: Peer-to-peer RV and trailer platforms could reduce traditional operator share faster than commercial truck leasing.

## Sources
- **S1** — [2022 NAICS Definition: 532120 Truck, Utility Trailer, and RV Rental and Leasing](https://www.census.gov/naics/?chart=2022&details=532120&input=532120) (accessed 2026-07-22): Defines 532120 as establishments renting or leasing without drivers trucks, truck tractors, buses, semi-trailers, utility trailers, or recreational vehicles and excludes light-duty passenger trucks and SUVs.
- **S2** — [BLS OEWS: Largest Occupations in Automotive Equipment Rental and Leasing, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest occupations for NAICS 532100, including 62,200 counter and rental clerks, 23,960 vehicle/equipment cleaners, 12,300 bus and truck mechanics, 10,840 heavy truck drivers, 7,080 general and operations managers, and 5,790 customer service representatives.
- **S3** — [Ryder System 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/85961/000008596126000007/r-20251231.htm) (accessed 2026-07-22): Describes full-service leasing, flexible maintenance, commercial rental, digital support, fuel services, and lease periods generally of three to seven years for trucks and tractors and ten years for trailers; estimates one million U.S. commercial fleet vehicles are leased or rented from third parties such as Ryder.
- **S4** — [U-Haul Holding Company 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/4457/000095017025078451/uhal-20250331.htm) (accessed 2026-07-22): Reports a fleet of about 192,100 trucks, 137,500 trailers, and 39,700 towing devices and self-moving equipment rental revenue of $3.726 billion in fiscal 2025 versus $3.625 billion in fiscal 2024, with transaction and revenue-per-transaction commentary.
- **S5** — [BizBuySell Insight Report Data Tables: Full-Year 2025 Transactions](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-22): Reports 31 closed transactions in the broad Equipment Rental and Dealers category during 2025, with median cash flow of $273,854, demonstrating deal activity but not an industry-specific transfer rate.
