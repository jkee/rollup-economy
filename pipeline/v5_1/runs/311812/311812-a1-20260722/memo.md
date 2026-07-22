# 311812 — Commercial Bakeries

*v5.1 Stage 1 research memo. Run `311812-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.39 · L 0.83 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring replenishment relationships create durable external-customer demand and data-rich planning workflows.
**Weakness:** Physical production dominates labor, while powerful downstream buyers can recapture savings through price and commercial terms.

## Business-model lens
- Included: Lower-middle-market commercial bakeries that manufacture fresh or frozen bread, bread-type rolls, and other fresh bakery products and repeatedly supply external retail, foodservice, institutional, wholesale, vending, or contract-manufacturing customers.
- Excluded: Retail bakeries, frozen non-bread pastry manufacturers, cookie and cracker manufacturers, immediate-consumption snack bars, captive internal bakery units without external customers, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring wholesale product supply, generally priced by item, case, shipment, or negotiated customer program and delivered through direct-store-delivery or warehouse channels; some firms also manufacture under customer brands or foodservice specifications.
- Deviation from default lens: none

## Executive view
Commercial bakeries strongly fit a repeat outsourced-supply lens because they repeatedly manufacture and replenish physical products for retailers, foodservice, institutions, distributors, and brand owners. AI opportunity is concentrated in planning, administration, sales, quality documentation, and logistics; most employment remains physical production, packing, maintenance, and movement, much of it already mechanized.

## How AI changes the work
AI can improve demand forecasting, batch and shift scheduling, purchasing, inventory exceptions, route planning, pricing analysis, customer-service triage, quality-record review, and maintenance planning. It is less substitutive for mixing, shaping, baking, packing, sanitation, maintenance, and delivery, and commercial production already uses automated high-volume equipment.

## Value capture
Savings are not automatically passed through under case and negotiated product pricing, but concentrated retailers and foodservice buyers can recapture value at renewal through price, rebates, promotions, and service requirements. Differentiated branded or technically specialized products have stronger retention than commodity bread and private-label production.

## Firm availability
Most target-band commercial bakeries should meet the repeat-customer criterion, although affiliate dependence and sporadic co-packing require screening. Succession can produce opportunities among independent and family-owned firms, but plants with customer concentration, deferred capital spending, or weak food-safety systems may close or sell assets rather than transfer as going concerns.

## Demand durability
Baked foods remain physical staples and convenience products, and official broader-industry projections indicate moderate real growth. The key risk is not software elimination but share migration among large branded bakeries, regional suppliers, private label, retailer-owned facilities, imports, and in-store bake-off systems.

## Risks and uncertainty
Six-digit occupation, real-output, transaction, eligibility, and benefit-retention data are limited. Food safety, allergen control, short shelf life, waste, commodity inputs, retailer power, labor availability, route economics, customer concentration, and plant capital needs can dominate the achievable administrative savings. The provided compensation ratio mixes 2024 wages with 2022 receipts and is harmonized to the target basis, while the firm count is margin-bridged rather than directly observed.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2606 | — | OBSERVED | — |
| n | — | 143 | — | ESTIMATE | — |
| a | 0.09 | 0.15 | 0.23 | PROXY | S1, S2 |
| rho | 0.35 | 0.53 | 0.7 | ESTIMATE | S3, S4 |
| e | 0.78 | 0.9 | 0.97 | ESTIMATE | S2, S5, S6 |
| s5 | 0.09 | 0.18 | 0.3 | ESTIMATE | S7 |
| q | 0.28 | 0.48 | 0.68 | ESTIMATE | S6, S7 |
| d5 | 0.99 | 1.09 | 1.18 | PROXY | S8, S2 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.83 | 1.68 | ESTIMATE |
| F | 3.86 | 5.12 | 6.04 | ESTIMATE |
| C | 5.60 | 9.60 | 10.00 | ESTIMATE |
| D | 9.50 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source covers all NAICS 311800 establishments and excludes self-employed workers.
- a: Commercial production bakers already use high-volume equipment that may be automated, so gross task exposure is not necessarily not-yet-automated opportunity.
- a: The mapping is judgmental and wage-weighted from published occupation employment and wage data, not a directly observed AI task study.
- rho: No 311812-specific five-year AI implementation cohort was located.
- rho: FSMA scope and modified requirements vary by facility, but covered facilities must maintain documented controls and oversight.
- e: The public operator is much larger than the target band and is evidence about business model, not the eligible share of LMM firms.
- e: The provided firm count is margin-bridged using a subsector benchmark and may misclassify owner compensation or unusually capital-intensive plants.
- s5: No source directly measures five-year control-transfer probability for eligible 311812 firms.
- s5: The cited public filing describes generational change as a competitive factor but does not quantify transactions.
- q: Flowers Foods is a large branded operator and may have more brand leverage but also more concentrated national accounts than LMM firms.
- q: No observed benefit-sharing dataset was located.
- d5: The output projection is at four digits and cannot isolate commercial bakeries.
- d5: Constant-quality demand can diverge from real output if product mix, waste, distribution services, or private-label share changes.
- o: The measure concerns an accountable operator, not persistence of any particular independent supplier.
- o: A customer bringing manufacturing in-house would reduce outsourced operator demand even though physical baking continues.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311800](https://www.bls.gov/oes/2023/may/naics4_311800.htm) (accessed 2026-07-22): Reports broader-industry occupation employment and wages, including production at 49.70%, bakers at 21.90%, transportation and material moving at 13.23%, sales at 10.79%, and office support at 5.24%.
- **S2** — [Occupational Outlook Handbook: Bakers](https://www.bls.gov/ooh/production/bakers.htm) (accessed 2026-07-22): Describes physical baking tasks and commercial bakeries' use of high-volume equipment that may be automated; projects baker employment growth of 6% from 2024 to 2034 and cites demand for specialty baked goods.
- **S3** — [FSMA Final Rule for Preventive Controls for Human Food](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food) (accessed 2026-07-22): Documents covered facilities' requirements for food-safety plans, hazard analysis, preventive controls, monitoring, corrective action, verification, records, and training, subject to exemptions and modified requirements.
- **S4** — [Frequently Asked Questions on FSMA](https://www.fda.gov/food/food-safety-modernization-act-fsma/frequently-asked-questions-fsma) (accessed 2026-07-22): Explains facility-specific written food-safety plans, verification activities, and the preventive-controls qualified individual's oversight role for covered facilities.
- **S5** — [2022 NAICS Definition: 311812 Commercial Bakeries](https://www.census.gov/naics/?details=311812&input=311812&year=2022) (accessed 2026-07-22): Defines commercial bakeries as manufacturing fresh and frozen bread and bread-type rolls and other fresh bakery products except cookies and crackers, and identifies excluded adjacent industries.
- **S6** — [Flowers Foods 2025 Annual Report](https://investors.flowersfoods.com/~/media/Files/F/Flowers-Foods-V3/documents/Annual%20Report/flowers-foods-2025-annual-report.pdf) (accessed 2026-07-22): Describes recurring retail, restaurant, institutional, foodservice, wholesale, vending, in-store bakery, co-manufacturing, direct-store-delivery, and warehouse channels; reports the top ten customers were 57.7% of 2025 sales.
- **S7** — [Flowers Foods 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1128928/000095017025022243/flo-20241228.htm) (accessed 2026-07-22): Describes competition from major, regional, local, and retailer-owned bakeries and identifies price, promotions, product quality, availability, customer service, and generational changes in family-owned businesses as competitive factors.
- **S8** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects broader NAICS 311800 employment from 350.4 thousand to 369.2 thousand and real output from 62.1 to 74.4 billion chained 2017 dollars, a 1.8% annual output growth rate.
