# 311811 — Retail Bakeries

*v5.1 Stage 1 research memo. Run `311811-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.79 · L 1.01 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat-account bakeries can pair durable physical-food demand with AI-assisted front-office and planning workflows.
**Weakness:** Most of NAICS 311811 is walk-in product retail, not a recurring outsourced service, and core baking labor is physical.

## Business-model lens
- Included: Lower-middle-market retail bakeries that make bread and other bakery products on premises and have a meaningful repeat external-customer component, including recurring wholesale, hospitality, institutional, office, event-planner, or standing custom-order accounts.
- Excluded: Pure walk-in consumer retail with no recurring account relationships, captive in-store bakery departments, immediate-consumption snack bars, resellers of products made elsewhere, commercial bakeries classified in 311812, and non-control financing vehicles.
- Customer and revenue model: Product revenue from baked goods made on premises, with eligible firms deriving a meaningful share from repeat standing orders or recurring account customers; pricing is generally per item, batch, or order rather than cost-plus labor billing.
- Deviation from default lens: The code is heterogeneous relative to the service lens because its core NAICS definition is retail product sales. The lens is narrowed to bakeries with repeat external-account relationships so that transferability and commercial retention describe a coherent recurring revenue model.

## Executive view
Retail bakeries offer practical AI-assisted improvements in order handling, scheduling, purchasing, bookkeeping, customer communication, and marketing, but the largest labor pool remains hands-on production. The principal structural issue is lens fit: most establishments sell products to walk-in consumers rather than providing a recurring outsourced service, so diligence must identify account-heavy operators rather than assume the full code is eligible.

## How AI changes the work
AI can reduce time spent translating custom requests into quotes and production tickets, forecasting demand, scheduling shifts and batches, reconciling invoices, drafting promotions, and answering routine questions. It is less able to substitute for mixing, shaping, decorating, baking, cleaning, equipment maintenance, and food-safety accountability, which dominate the occupation mix.

## Value capture
Item and order pricing provides no automatic contractual pass-through, allowing an operator to retain early savings. Retention erodes through frequent menu repricing, customer comparison, local competition, and reinvestment in quality or convenience, especially for staple products; differentiated custom and standing-account work should retain more.

## Firm availability
The provided LMM count is already an estimate, and only a minority of those firms likely have enough recurring external-account business to fit the lens. Owner succession may create transactions, but closures, family transfers, and small asset sales must not be counted as qualifying control transfers of continuing operations.

## Demand durability
Bread, cakes, pastries, and specialty baked goods remain physical consumption categories, with official projections for the broader bakery industry indicating moderate real growth. Demand can shift among independent retail bakeries, grocery in-store bakeries, foodservice, and commercial packaged products, so industry demand durability is stronger than independent-channel durability.

## Risks and uncertainty
The strongest uncertainties are the share of firms with recurring account revenue, the broader-industry occupation and demand proxies, and the lack of observed AI implementation and benefit-retention cohorts. Ingredient inflation, food-safety failures, allergen controls, short shelf life, skilled labor dependence, and channel competition could overwhelm administrative savings. The provided compensation ratio also mixes 2024 wages with 2022 receipts and is harmonized rather than directly observed on the final basis.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2858 | — | OBSERVED | — |
| n | — | 77 | — | ESTIMATE | — |
| a | 0.1 | 0.17 | 0.26 | PROXY | S1 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S4, S5 |
| e | 0.08 | 0.18 | 0.32 | ESTIMATE | S2 |
| s5 | 0.1 | 0.2 | 0.32 | ESTIMATE | S3 |
| q | 0.38 | 0.58 | 0.76 | ESTIMATE | S2 |
| d5 | 0.98 | 1.08 | 1.17 | PROXY | S6, S7 |
| o | 0.92 | 0.97 | 0.995 | ESTIMATE | S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.40 | 1.01 | 2.02 | ESTIMATE |
| F | 0.77 | 2.14 | 3.51 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 9.02 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is a four-digit 311800 proxy and mixes retail, commercial, cookie, cracker, and tortilla manufacturing.
- a: OEWS excludes self-employed workers and reports occupation employment rather than task time or current automation status.
- a: The range is a judgmental wage-weighted task mapping, not an observed AI-exposure statistic.
- rho: Retail bakeries are generally state- and locally regulated, while some facilities and interstate activities may also face FDA requirements; the compliance burden varies by business model.
- rho: No industry-specific five-year AI implementation cohort was located.
- e: The provided n is a margin-bridged estimate and may be sensitive to retail bakery margins and owner compensation.
- e: Public industry data do not separate recurring account revenue from walk-in retail sales.
- s5: Census ABS provides owner-characteristic tables but not a directly observed five-year control-transfer probability for eligible retail bakeries.
- s5: Listings and SBA-backed deals would omit private, seller-financed, family, and unannounced transactions.
- q: No observed contract pass-through dataset was located.
- q: Retention will differ sharply between differentiated custom products and price-comparable staple bread.
- d5: The BLS output series is four-digit NAICS 311800 and includes commercial bakeries, cookies, crackers, and tortillas.
- d5: Employment growth is not the same as constant-quality service quantity and may reflect labor intensity or mix shifts.
- o: Operator requirement does not guarantee that the surviving operator remains an independent retail bakery; centralized or grocery channels could take share.
- o: FDA's Food Code is a model adopted variably by state and local jurisdictions.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311800](https://www.bls.gov/oes/2023/may/naics4_311800.htm) (accessed 2026-07-22): Broader-industry occupation mix: production 49.70%, bakers 21.90%, sales 10.79%, office support 5.24%, management 3.75%, and food preparation/serving 8.53%.
- **S2** — [2022 NAICS Definition: 311811 Retail Bakeries](https://www.census.gov/naics/?details=311811&input=311811&year=2022) (accessed 2026-07-22): Defines the industry as establishments retailing bread and other bakery products not for immediate consumption made on premises from flour, and distinguishes resellers, snack bars, and commercial bakeries.
- **S3** — [2023 Annual Business Survey: Characteristics of Business Owners](https://www.census.gov/data/tables/2023/econ/abs/2023-abs-characteristics-of-owners.html) (accessed 2026-07-22): Establishes that the 2023 ABS covers reference year 2022 and includes an Age of Owner table, useful as a potential succession proxy but not a direct control-transfer measure.
- **S4** — [FDA Food Code](https://www.fda.gov/food/retail-food-protection/fda-food-code) (accessed 2026-07-22): Describes the Food Code as a model for safe handling in retail food settings and a basis used by state, local, tribal, and federal regulators.
- **S5** — [FSMA Final Rule for Preventive Controls for Human Food](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food) (accessed 2026-07-22): Documents food-safety plans, hazard analysis, process and allergen controls, monitoring, corrective action, verification, records, and employee training requirements for covered facilities, subject to exemptions.
- **S6** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects NAICS 311800 employment from 350.4 thousand in 2024 to 369.2 thousand in 2034 and real output from 62.1 to 74.4 billion chained 2017 dollars.
- **S7** — [Occupational Outlook Handbook: Bakers](https://www.bls.gov/ooh/production/bakers.htm) (accessed 2026-07-22): Projects baker employment growth of 6% from 2024 to 2034 and attributes demand partly to population and income growth and demand for commercial and retail specialty baked goods.
