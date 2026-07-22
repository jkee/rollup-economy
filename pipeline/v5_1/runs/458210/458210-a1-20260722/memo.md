# 458210 — Shoe Retailers

*v5.1 Stage 1 research memo. Run `458210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** A sales-heavy occupation mix contains repeatable product-advice, transaction, inventory, and administrative tasks that packaged AI can augment.
**Weakness:** Almost no shoe retailers clearly satisfy the recurring outsourced-service lens, and the surviving product-linked benefit is exposed to price and channel competition.

## Business-model lens
- Included: Lower-middle-market shoe retailers whose customer proposition includes a repeat, externally supplied service component, such as institutional footwear programs, recurring fitting and measurement, or managed replenishment tied to footwear sales.
- Excluded: Ordinary one-off merchandise retail, manufacturer-owned brand stores, captive procurement, pure e-commerce product sellers, shoe repair classified in NAICS 811430, and firms outside the normalized EBITDA band.
- Customer and revenue model: Households or institutional accounts pay mainly per footwear purchase; the eligible subset embeds fitting, selection, account administration, and replenishment in the merchandise margin rather than charging a standalone recurring fee.
- Deviation from default lens: The code is heterogeneous relative to the screen because almost all activity is product retail, not outsourced service. The lens is narrowed to retailers with a genuine repeat service component so product-only transactions are not mislabeled as outsourced services.

## Executive view
Shoe retail is fundamentally a merchandise business, so only a thin specialty subset fits the recurring outsourced-service lens. In that subset AI can remove routine selling and administrative work, but the available population is uncertain and value capture is weakened by transparent product pricing and channel competition.

## How AI changes the work
AI can improve product search and matching, answer routine questions, support purchasing and replenishment, automate customer communications, and reduce bookkeeping or scheduling work. Physical fitting, merchandising, customer trust, exception handling, loss prevention, and minimum store coverage keep much of the sales-heavy labor base human.

## Value capture
Savings are embedded in merchandise economics rather than protected by recurring fixed fees. Competitors, promotions, and online price comparison are likely to pass much of the benefit to customers, although specialist reputation and institutional relationships can preserve some margin.

## Firm availability
Broad owner-aging evidence indicates meaningful transfer intent, but there is no defensible dataset count for firms in the EBITDA band and the eligible service-model share appears extremely small. Product-only shoe stores, brand-owned chains, and incidental fitting do not qualify.

## Demand durability
Consumers will continue buying footwear, but that does not guarantee demand for the current store-based service basket. E-commerce growth and a long decline in shoe-store establishments pressure physical demand; complex fitting, orthopedic needs, and managed institutional programs are more durable than ordinary transactions.

## Risks and uncertainty
The largest risk is category error: treating product retail as outsourced service. Other uncertainties are the ancestor-level labor ratio, the missing firm-count input, absence of shoe-specific AI deployment evidence, intentions rather than completed transfer data, and unknown real unit demand for the specialty subset.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.14 | 0.23 | 0.34 | PROXY | S2, S3 |
| rho | 0.3 | 0.48 | 0.66 | ESTIMATE | S3, S4 |
| e | 0.002 | 0.008 | 0.02 | ESTIMATE | S1, S8 |
| s5 | 0.13 | 0.21 | 0.3 | PROXY | S7 |
| q | 0.18 | 0.3 | 0.46 | ESTIMATE | S1, S5 |
| d5 | 0.84 | 0.94 | 1.04 | PROXY | S4, S5, S6 |
| o | 0.72 | 0.86 | 0.95 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.45 | 0.91 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 3.60 | 6.00 | 9.20 | ESTIMATE |
| D | 6.05 | 8.08 | 9.88 | ESTIMATE |

## Caveats
- a: OEWS covers employers of all sizes and excludes self-employed workers; the eligible lower-middle-market subset may have a different occupation mix.
- a: The occupation table is May 2023 and the O*NET retail-salesperson task data are cross-retail rather than shoe-specific.
- a: The dataset labor ratio is only available at ancestor 44-45, uses 2024 wages over 2022 receipts, and is harmonized to the IPS basis; it may not represent specialty shoe retailers.
- rho: No source measures five-year implementation for independent shoe retailers.
- rho: Implementation may avoid incremental hiring rather than remove scheduled store coverage.
- rho: This excludes demand migration and price competition, which are addressed in d5, o, and q.
- e: No public dataset measures the service-model share or the normalized EBITDA band for this code.
- e: Incidental fitting during a product sale is not treated as an outsourced service.
- e: The provided n input is a declared dataset gap and will be injected as MISSING; it was not replaced or estimated here.
- s5: The Gallup survey is cross-industry and includes firms outside the lens and EBITDA band.
- s5: Planned sales and gifts are not observed completed transfers.
- s5: Deaths without transferable operations and internal reorganizations are excluded from the estimate.
- q: There is no direct estimate of benefit pass-through for specialty shoe retailers.
- q: The eligible subset may have more differentiated service and retain more value than ordinary shoe stores.
- q: Volume loss is excluded here and addressed in d5 and o.
- d5: The 2017-2022 Census comparison is on the former 44821 basis and spans pandemic disruption.
- d5: Published sales are nominal, whereas d5 requires constant-price and constant-quality quantity.
- d5: Aggregate e-commerce data cover all retail and do not isolate footwear or the eligible service subset.
- o: No source directly measures operator displacement in specialty shoe retail.
- o: The range is conditional on year-five demand and does not count channel-driven quantity loss already reflected in d5.
- o: Rapid improvements in remote sizing and automated returns could reduce operator-required share.

## Sources
- **S1** — [2022 NAICS Definition: 458210 Shoe Retailers](https://www.census.gov/naics/?details=45&input=45&year=2022) (accessed 2026-07-22): Defines the industry as establishments primarily retailing new footwear, establishing the product-retail nature of the code.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 458200 Shoe Retailers](https://www.bls.gov/oes/2023/may/naics4_458200.htm) (accessed 2026-07-22): Reports 173,350 total employees; 87.39% in sales occupations, including 70.19% retail salespersons, 13.19% retail-sales supervisors, and 3.33% cashiers; also reports office, management, and material-moving shares and wages.
- **S3** — [O*NET OnLine: 41-2031.00 Retail Salespersons](https://www.onetonline.org/link/details/41-2031.00) (accessed 2026-07-22): Lists retail-sales tasks including customer-needs gathering, recommendations, transactions, records, inventory, returns, fitting assistance, and delivery arrangements; reports near-universal external-customer importance and daily face-to-face interaction.
- **S4** — [BLS Occupational Outlook Handbook: Retail Sales Workers](https://www.bls.gov/ooh/sales/retail-sales-workers.htm) (accessed 2026-07-22): Projects little or no employment change from 2024 to 2034 and states that online sales will limit physical-store growth while in-store customer service keeps retail salespersons needed.
- **S5** — [U.S. Census Bureau Quarterly Retail E-Commerce Sales, First Quarter 2026](https://www.census.gov/retail/eCommerce.html) (accessed 2026-07-22): Reports adjusted e-commerce sales up 9.8% year over year versus 3.9% for total retail and e-commerce at 16.9% of retail sales.
- **S6** — [2022 Economic Census Comparative Statistics: 44821 Shoe Stores, 2017 and 2022](https://data.census.gov/table/ECNCOMP2022.EC2200COMP?codeset=naics~44821&g=010XX00US) (accessed 2026-07-22): Reports 24,844 establishments and $36.036 billion sales in 2017 versus 19,083 establishments and $36.901 billion sales in 2022 on the 2017 NAICS basis.
- **S7** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 52.3% of employer businesses owned by people age 55 or older and 22% of employer-business owners planning to sell or transfer ownership within five years.
- **S8** — [U.S. Census Bureau 2022 Retail Trade Questionnaire: Shoe Stores](https://bhs.econ.census.gov/ombpdfs2022/export/2022_RT-44821_mu.pdf) (accessed 2026-07-22): Lists shoe-store activities under 448210 and classifies footwear, luggage, handbag, briefcase, and leather-goods repair separately under 811430.
