# 322211 — Corrugated and Solid Fiber Box Manufacturing

*v5.1 Stage 1 research memo. Run `322211-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.65 · L 0.78 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring, specification-rich customer orders create implementable AI workflows across quoting, scheduling, quality, maintenance support, and service.
**Weakness:** Physical production dominates labor and competitive board-linked pricing can pass efficiency gains to powerful customers.

## Business-model lens
- Included: Independent US corrugated and solid-fiber box manufacturers in the approximately $1-10 million normalized EBITDA band that repeatedly design, convert, print, and supply boxes to external customers.
- Excluded: Captive packaging plants, containerboard mills without box converting, brokers without accountable production, shells, non-control financing vehicles, and firms outside the EBITDA band.
- Customer and revenue model: Recurring business-to-business sales of custom or standard corrugated boxes under quotes, purchase orders, supply agreements, and recurring replenishment programs, commonly priced per thousand square feet or per unit with board and freight adjustments.
- Deviation from default lens: none

## Executive view
Corrugated box manufacturing combines a substantial estimated LMM population and recurring local customer relationships with a production-heavy labor base. AI is most credible in quoting, design support, order management, scheduling, procurement, maintenance assistance, and service rather than physical converting.

## How AI changes the work
AI can structure customer specifications, accelerate quotes, check artwork and orders, assist CAD choices, forecast demand, sequence jobs, surface maintenance knowledge, and automate routine service. Machine setup, feeding, printing, die cutting, gluing, bundling, maintenance, quality release, and material movement remain substantially physical.

## Value capture
Benefits that improve speed, accuracy, scrap, uptime, and customer retention are less visible and more retainable than simple administrative cost cuts. Board-price formulas and competitive rebids nevertheless return a meaningful portion to customers over five years.

## Firm availability
Most independent converters fit repeat external supply, but captive plants and integrated divisions do not. The frozen estimate of 212 band firms is materially uncertain because profitability varies by mix, equipment, and board costs; owner aging provides only broad transfer support.

## Demand durability
E-commerce and physical-goods distribution support box usage, and BLS expects converted-paper output growth. Lightweighting, right-sizing, reusable alternatives, industrial cyclicality, and the 2025 upstream containerboard decline prevent treating online-sales growth as one-for-one box growth.

## Risks and uncertainty
Key uncertainties are the six-digit occupational mix, baseline automation, independent-versus-captive ownership, margin-bridged firm count, customer concentration, equipment condition, board-price pass-through, and actual square-foot shipment growth. A downturn in goods production can quickly lower plant utilization.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.186 | — | OBSERVED | — |
| n | — | 212 | — | ESTIMATE | — |
| a | 0.11 | 0.18 | 0.27 | PROXY | S1 |
| rho | 0.4 | 0.58 | 0.74 | ESTIMATE | S1 |
| e | 0.55 | 0.72 | 0.85 | ESTIMATE | S5 |
| s5 | 0.14 | 0.24 | 0.36 | PROXY | S4 |
| q | 0.34 | 0.54 | 0.72 | ESTIMATE | S5 |
| d5 | 0.97 | 1.06 | 1.17 | PROXY | S2, S3, S5 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.78 | 1.49 | ESTIMATE |
| F | 4.59 | 5.84 | 6.74 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 9.12 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is NAICS 322 and not specific to corrugated plants.
- a: Current ERP, CAD, and plant-automation penetration is unknown, creating risk of counting already automated work.
- rho: No representative AI implementation study for 322211 was found.
- rho: Implementation can shift work to exception handling rather than eliminate it.
- e: Eligibility is not directly observed.
- e: The injected n=212 uses an estimated EBITDA margin bridge and can misclassify low- or high-margin converters.
- s5: The Census age distribution is all-industry and data year 2018.
- s5: Age is a succession-pressure proxy, not an observed transfer rate.
- q: No contract-level retention sample was available.
- q: Retention varies between commodity brown-box volume and high-service custom displays or short runs.
- d5: E-commerce sales are nominal and not a direct measure of corrugated use.
- d5: BLS output is NAICS 3222, while upstream AF&PA containerboard data include uses beyond 322211.
- o: On-demand box-making systems may internalize a small portion of standard demand at large customers.
- o: Volume effects from packaging reduction belong in d5 rather than this operator-share estimate.

## Sources
- **S1** — [Paper Manufacturing: NAICS 322](https://www.bls.gov/iag/tgs/iag322.htm) (accessed 2026-07-22): BLS reports 2025 paper-manufacturing employment of 87,050 paper-goods machine operators, 17,540 production supervisors, 14,210 industrial-truck operators, and 6,640 production managers, evidencing a production-heavy labor mix.
- **S2** — [Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects converted paper product manufacturing output from $99.0 billion in 2024 to $116.9 billion in 2034 in chained 2017 dollars, a 1.7% compound annual growth rate, while employment falls 5.4%.
- **S3** — [Quarterly Retail E-Commerce Sales, First Quarter 2026](https://www.census.gov/retail/mrts/www/data/pdf/ec_current.pdf) (accessed 2026-07-22): Census reports seasonally adjusted US retail e-commerce sales of $326.7 billion in 2026 Q1, up 9.8% from 2025 Q1 and equal to 16.9% of total retail sales.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The 2019 Annual Business Survey infographic reports 51% of responding owners of employer businesses were age 55 or older, based on 4.1 million responding owners in data year 2018.
- **S5** — [AF&PA Releases 66th Annual Paper Industry Capacity and Fiber Consumption Survey](https://www.afandpa.org/news/2026/afpa-releases-66th-annual-paper-industry-capacity-and-fiber-consumption-survey) (accessed 2026-07-22): AF&PA reports 2025 containerboard production fell 4.4% to 36.1 million tons, capacity declined 5.1%, and operating rate held at 91.9%; its data represent about 87% of US paper and paperboard capacity with estimates completing the dataset.
