# 445131 — Convenience Retailers

*v5.1 Stage 1 research memo. Run `445131-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Routine ordering and account coordination sit beside physical fulfillment that preserves a role for an accountable local operator.
**Weakness:** Only an uncommon subset of convenience retailers appears eligible under the outsourced-service lens, and the LMM firm count is missing.

## Business-model lens
- Included: Lower-middle-market convenience retailers without fuel pumps that provide recurring external customers with a genuine outsourced food-provision function, such as contracted workplace, institutional, or multi-site pantry stocking, standing-order preparation, or scheduled delivery tied to ongoing account responsibility.
- Excluded: Ordinary walk-in retail transactions; fuel-pump convenience stores; supermarkets; vending-machine operators; one-off delivery; captive outlets; shells; non-control financing vehicles; and firms outside the normalized EBITDA band.
- Customer and revenue model: Recurring commercial or institutional accounts pay merchandise margins and, where applicable, delivery or account fees for repeated stocking or standing-order fulfillment; consumer foot traffic may coexist but does not itself qualify.
- Deviation from default lens: The official code is product retail, not outsourced services. The lens is narrowed to the small subset assuming recurring external-customer responsibility for food provisioning because mixing those accounts with ordinary walk-in convenience retail would be incoherent.

## Executive view
The code is overwhelmingly walk-in product retail, leaving only a very small subset that provides a qualifying recurring outsourced provisioning service. Within that subset, routine transaction and coordination labor is automatable, but physical food handling, local availability, safety, and shrink control remain operator responsibilities.

## How AI changes the work
AI can support standing-order capture, customer messaging, promotion, forecasting, replenishment, scheduling, invoice matching, and basic service recovery. Checkout self-service is already reducing cashier demand. Stocking, food preparation, cleaning, security, age verification, delivery, and exception handling constrain substitution.

## Value capture
Operators can initially keep savings under fixed shelf or account prices, but packaged-goods transparency and low switching costs invite repricing. Capture is more durable where reliability, prepared food, emergency availability, or bundled delivery differentiates the account.

## Firm availability
Broad owner-aging evidence suggests succession opportunities, but no industry-specific transfer denominator exists. More importantly, most convenience retailers fail the outsourced-service lens, and the frozen LMM firm count is unavailable.

## Demand durability
Food is essential and broad real food spending stabilized in 2024, supporting near-flat real quantity. Convenience-service demand can still lose share to supermarkets, direct distributors, vending, delivery platforms, and customer self-service.

## Risks and uncertainty
The largest risk is mistaking frequent consumer purchases for contracted outsourced service. Other risks include thin margins, theft, cash controls, food safety, labor turnover, lease and location dependence, channel competition, and data fragmentation. Firm-level recurring-account evidence is the decisive next diligence step.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1295 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.22 | 0.36 | 0.5 | PROXY | S2, S3 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S3 |
| e | 0.01 | 0.03 | 0.08 | ESTIMATE | S1 |
| s5 | 0.1 | 0.17 | 0.27 | PROXY | S4 |
| q | 0.25 | 0.45 | 0.65 | ESTIMATE | S1, S5 |
| d5 | 0.92 | 1.01 | 1.1 | PROXY | S5, S6 |
| o | 0.65 | 0.82 | 0.93 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.40 | 1.03 | 1.86 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 5.00 | 9.00 | 10.00 | ESTIMATE |
| D | 5.98 | 8.28 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation evidence combines grocery, convenience, and specialty food retailers.
- a: Employment counts are not task-time or wage weights.
- a: The estimate excludes checkout and ordering automation already in operation.
- rho: This is implementation judgment rather than a measured adoption rate.
- rho: BLS self-checkout evidence establishes technical substitution in one task but not full workflow realization.
- rho: Eligible independent firms may have less capital and weaker data than major chains.
- e: No source measures service-lens eligibility within the code.
- e: Ancillary service revenue may not affect an establishment's primary NAICS classification.
- e: The frozen LMM firm-count input is missing, so the eligible-firm count remains unknown.
- s5: The age evidence is all-industry, owner-level, and from data year 2018.
- s5: Owner shares do not equal firm shares in businesses with multiple owners.
- s5: No observed industry-specific eligible-firm or transfer denominator is available.
- q: No source directly observes pass-through of AI-related savings.
- q: Retention could be higher for differentiated prepared food and emergency availability than for standard packaged goods.
- q: The range excludes volume changes and implementation cost.
- d5: Neither source isolates six-digit convenience retailers or the recurring-account lens.
- d5: The FRED series is nominal and includes all food and beverage stores.
- d5: Local traffic, remote work, food inflation, regulation, and competition can produce wide geographic dispersion.
- o: This is a bounded judgment, not an observed operator-retention measure.
- o: The physical-operator requirement is higher for prepared or age-restricted products than for packaged pantry items.
- o: Continued operator need does not imply preservation of cashier jobs.

## Sources
- **S1** — [2022 NAICS Definition: Grocery and Convenience Retailers](https://www.census.gov/naics/?details=4451&input=4451&year=2022) (accessed 2026-07-22): Defines 445131 as establishments retailing a limited grocery line such as milk, bread, soda, and snacks, excluding fuel-pump stores, supermarkets, and vending-machine operators.
- **S2** — [May 2024 OEWS Data Tables for Industry Charts](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports leading occupations in food and beverage retailers, including 838,060 cashiers, 637,090 stockers and order fillers, 185,500 food preparation workers, 168,200 retail supervisors, and 132,220 fast-food and counter workers.
- **S3** — [Occupational Outlook Handbook: Cashiers](https://www.bls.gov/ooh/sales/cashiers.htm) (accessed 2026-07-22): Describes checkout and customer-assistance duties and projects cashier employment to decline 10 percent from 2024 to 2034 because of self-service checkout and increasing online sales.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51 percent of responding owners of employer businesses were 55 or older, 43 percent were 35 to 54, and 6 percent were 34 or younger, based on the 2019 ABS with data year 2018.
- **S5** — [Retail Sales: Food and Beverage Stores](https://fred.stlouisfed.org/data/MRTSSM445USN) (accessed 2026-07-22): Provides Census-sourced monthly nominal sales for food and beverage stores, including $89.736 billion in December 2024 and $91.318 billion in December 2025.
- **S6** — [As Food Price Inflation Slowed in 2024, Inflation-Adjusted Food Spending Rebounded](https://www.ers.usda.gov/data-products/charts-of-note/111011) (accessed 2026-07-22): Reports 2024 real food-at-home spending growth of 1.8 percent after a 2.6 percent decline in 2023, and real food-away-from-home spending growth of 0.4 percent in 2024.
