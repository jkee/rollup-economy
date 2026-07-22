# 457210 — Fuel Dealers

*v5.1 Stage 1 research memo. Run `457210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** A sizable administrative workforce supporting repetitive customer, billing, dispatch, and route workflows creates implementable AI opportunity around a durable physical delivery core.
**Weakness:** Structural decline in heating-oil accounts and competitive commodity-price pass-through limit demand and long-run retention of savings.

## Business-model lens
- Included: Lower-middle-market U.S. dealers delivering heating oil, liquefied petroleum gas, and other fuels repeatedly to external residential, commercial, industrial, agricultural, and governmental customers, including associated account management and equipment service.
- Excluded: Merchant wholesalers, pipeline or terminal operators, gasoline stations, captive internal fleets, cash-and-carry sellers without a recurring delivery relationship, shells, and non-control financing vehicles.
- Customer and revenue model: Dealers earn per-gallon product margin through scheduled, automatic, or on-demand delivery and may also earn recurring service-contract, installation, repair, equipment-rental, budget-plan, and account fees; customers range from households to commercial and agricultural accounts.
- Deviation from default lens: none

## Executive view
Fuel dealers fit the recurring-service lens because home and business delivery is a repeated, route-based external service. Their large administrative layer offers credible AI-enabled labor avoidance, while drivers, technicians, hazardous-material handling, and physical delivery keep the implementable share bounded and the operator-required share high.

## How AI changes the work
The strongest use cases are automatic-delivery demand prediction, routing support, call and email handling, billing, collections, account setup, document extraction, service scheduling, sales assistance, technician knowledge retrieval, and exception triage. Core driving, loading, hose connection, inspection, repair, and emergency response remain physical and safety critical.

## Value capture
Commodity costs flow rapidly into customer prices and customers can compare competing dealers, but route density, automatic delivery, service contracts, installed equipment, and reliability create local switching friction. Savings should be partly retained through better density and service capacity, while competition and renewal discounts erode them over time.

## Firm availability
The industry has visible strategic-acquirer activity, and transferable customer books, routes, storage, vehicles, and technicians support consolidation. Broad owner-transition intent is only a proxy, however, and environmental diligence, customer attrition, working capital, fleet condition, and internal succession reduce the share of intentions that become qualifying control transfers.

## Demand durability
Heating oil faces gradual structural decline from conversions, efficiency, electrification, and warmer weather, while propane has broader rural, commercial, agricultural, industrial, backup-power, and transport uses. Most surviving five-year demand still needs a regulated physical delivery and service operator.

## Risks and uncertainty
The supplied LMM firm count is missing, and no public dataset links 457210 firms to recurring-account mix, normalized EBITDA, transaction outcomes, or AI labor savings. Weather volatility, commodity prices, regional policy, equipment conversions, customer churn, route density, and legacy-system readiness create wide outcome dispersion.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.15 | 0.25 | 0.36 | PROXY | S2, S3 |
| rho | 0.42 | 0.6 | 0.78 | ESTIMATE | S2, S7, S8 |
| e | 0.55 | 0.75 | 0.9 | ESTIMATE | S1, S6, S7 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S5, S6, S7 |
| q | 0.3 | 0.5 | 0.7 | ESTIMATE | S6, S7 |
| d5 | 0.83 | 0.92 | 0.99 | PROXY | S4, S6, S7 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S8, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.26 | 0.61 | 1.14 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.47 | 8.83 | 9.80 | ESTIMATE |

## Caveats
- a: OEWS data are from May 2023 and exclude self-employed workers.
- a: WEF measures expected occupational change across countries and industries, not current wage-weighted task exposure in U.S. fuel dealers.
- a: The supplied labor ratio is measured at ancestor 44-45 and may not match this delivery- and service-heavy industry.
- rho: No source reports AI implementation rates or labor avoidance for the target LMM population.
- rho: Technology modernization at a large public operator may not transfer to smaller dealers with less capital and weaker data.
- rho: PHMSA training and safety duties constrain implementation where software recommendations affect loading, transport, or delivery.
- e: NAICS is assigned at the establishment level, while the lens and LMM eligibility are firm-level constructs.
- e: Home delivery can be repeat transactional product retail without a contract, so not every dealer has a durable outsourced-service relationship.
- e: The supplied LMM firm-count input is missing, preventing translation of the share into a defensible number of eligible firms.
- s5: Owner-transition intentions are self-reported, cross-industry, and not completed sales.
- s5: Large public consolidators are not representative of the full buyer universe or target population.
- s5: The estimate excludes closures, internal reorganizations, minority investments, and asset-only transactions without transferable operations.
- q: Public operators may have greater purchasing power, density, and pricing discipline than LMM dealers.
- q: Weather and wholesale-price volatility obscure the pass-through of operating savings.
- q: Retention differs materially among variable-price fuel, fixed-price or capped plans, service contracts, and negotiated commercial accounts.
- d5: Winter-fuel consumption is weather-sensitive and does not establish a five-year structural trend on its own.
- d5: The current service basket spans heating oil, propane, other fuels, delivery, and equipment services with different trajectories.
- d5: Acquisition-driven public-company volume growth is not organic demand growth.
- o: An accountable operator can oversee more customers and locations with software, so high operator requirement does not imply stable headcount.
- o: Federal requirements vary in applicability by material, quantity, vehicle, facility, and state implementation.
- o: Customer self-monitoring and smart tanks can remove ordering tasks without eliminating delivery operations.

## Sources
- **S1** — [2022 NAICS Definition: 457210 Fuel Dealers](https://www.census.gov/naics/?details=457210&input=457210&year=2022) (accessed 2026-07-22): Defines fuel dealers as establishments primarily retailing heating oil, LP gas, and other fuels through direct selling or home delivery and distinguishes them from petroleum wholesalers and gasoline stations.
- **S2** — [Fuel Dealers - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_457200.htm) (accessed 2026-07-22): Reports 70,210 jobs: office/administrative support 23.57%, transportation/material moving 39.40%, management 7.37%, sales 4.96%, and detailed employment and wages for drivers, customer support, bookkeeping, dispatch, and repair occupations.
- **S3** — [Future of Jobs Report 2025: Jobs Outlook](https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/2-jobs-outlook/) (accessed 2026-07-22): Identifies clerical, cashier, administrative, bookkeeping, and accounting roles among expected decliners and digital access, AI/information processing, and autonomous systems as major transformation drivers.
- **S4** — [EIA Winter Fuels Outlook 2025-2026](https://www.eia.gov/outlooks/steo/report/WinterFuels.php) (accessed 2026-07-22): Reports propane as the primary heating fuel for about 5% of U.S. households, heating oil for about 3%, strong Northeast concentration, and significant weather-driven variation in consumption and expenditure.
- **S5** — [2023 National State of Owner Readiness Report](https://exit-planning-institute.org/hubfs/Member%20Center%20Resources/2023%20National%20State%20of%20Owner%20Readiness%20Report.pdf) (accessed 2026-07-22): Surveyed 1,162 U.S. owners across more than 25 industries; reports roughly 73% of privately held companies would like to transition within ten years and documents substantial preference for internal family-business exits.
- **S6** — [Star Group Reports Fiscal 2025 Full Year and Fourth Quarter Results](https://investors.stargrouplp.com/news-releases/news-release-details/star-group-lp-reports-fiscal-2025-full-year-and-fourth-quarter) (accessed 2026-07-22): Describes a full-service heating-fuel delivery and equipment-service model, acquisition-added volume, persistent net customer attrition, wholesale-cost price response, service revenue, and risks from gas conversion and heating electrification.
- **S7** — [Suburban Propane Announces Fiscal 2025 Full Year and Fourth Quarter Results](https://www.prnewswire.com/news-releases/suburban-propane-partners-lp-announces-full-year-and-fourth-quarter-results-302613801.html) (accessed 2026-07-22): Reports acquisitions, a multi-year technology-modernization initiative, 400.5 million retail propane gallons, diversified customers and uses, unit-margin management, and demand risks from competition, efficiency, conservation, and technology.
- **S8** — [PHMSA Training Requirements for Industry](https://www.phmsa.dot.gov/training/hazmat/training-requirements-industry) (accessed 2026-07-22): Requires hazmat employers to train, test, certify, and retain training records for hazmat employees, including function-specific, safety, security, and vehicle-driver training, with recurrent training at least every three years.
- **S9** — [Overview of the Spill Prevention, Control, and Countermeasure Regulation](https://www.epa.gov/oil-spills-prevention-and-preparedness-regulations/overview-spill-prevention-control-and) (accessed 2026-07-22): Explains requirements for prevention, preparedness, response plans, procedures, methods, and equipment at covered oil facilities, including provisions relevant to mobile refuelers.
