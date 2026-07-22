# 458110 — Clothing and Clothing Accessories Retailers

*v5.1 Stage 1 research memo. Run `458110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Sales-heavy repetitive workflows offer meaningful AI assistance and labor avoidance around recommendations, clienteling, inventory, and administration.
**Weakness:** The recurring outsourced-service subset is tiny and unmeasured inside a highly competitive, promotion-sensitive product-retail industry.

## Business-model lens
- Included: Lower-middle-market clothing and accessories retailers with a material recurring external-customer service component, such as basic alterations and fitting, repeat personal wardrobe or styling service, or recurring school/work uniform programs, alongside sales of new apparel and accessories.
- Excluded: Transactional product-only apparel retail, manufacturers of custom apparel, alteration-only repair shops classified elsewhere, used clothing, shoe and precious-jewelry retailers, captive internal stores, shells, and non-control financing vehicles.
- Customer and revenue model: The eligible subset earns merchandise margin plus repeat service or program revenue from consumers, schools, employers, or other external customers through fitting, basic alterations, curated wardrobe assistance, and recurring uniform replenishment.
- Deviation from default lens: Narrowed to service-rich retailers with basic alterations, repeat fitting or styling, or recurring uniform programs because NAICS 458110 is overwhelmingly transactional product retail and the pure merchandise model does not satisfy the fixed outsourced-service lens.

## Executive view
Clothing and accessories retail is overwhelmingly transactional product commerce, so only a small subset with material alterations, fitting/styling, or uniform-program service fits the recurring outsourced-service lens. AI can improve selling and administration, but the eligible differentiation is often human, tactile, and local, while fierce channel competition limits retention.

## How AI changes the work
Useful applications include product and outfit recommendations, client follow-up, marketing content, customer-response drafting, workforce scheduling, inventory and replenishment analysis, return and fraud triage, and back-office automation. Physical fitting, sewing, garment preparation, in-person trust, and exception-rich styling remain harder to substitute.

## Value capture
Digital price transparency, promotions, low switching costs, and broad assortment competition push efficiency gains toward lower prices or higher service. Alterations, fit expertise, loyal client books, and uniform reliability offer some differentiation, but even healthy apparel gross margins can compress into modest operating margins after occupancy, labor, marketing, and markdowns.

## Firm availability
There is an active market for independent retail businesses, but service-lens-eligible apparel firms are scarce and often owner-, brand-, inventory-, and lease-dependent. Succession intent therefore converts less reliably into a qualifying operating-company control transfer than it does in route-based or contract-heavy services.

## Demand durability
Aggregate apparel quantity is likely to remain roughly flat to modestly grow over five years, with stable replacement need offset by weak budget share, resale, trade-down, and fashion volatility. Alterations and uniform replenishment persist, but digital discovery and self-service can remove part of the local operator's role.

## Risks and uncertainty
The central gap is the absence of firm-level evidence on recurring service revenue within 458110. The supplied LMM firm count is also missing, while broad occupation, spending, e-commerce, public-company, and business-sale data only indirectly describe the narrow target population.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.25 | 0.36 | PROXY | S2, S3, S7 |
| rho | 0.38 | 0.55 | 0.72 | ESTIMATE | S4, S7 |
| e | 0.005 | 0.025 | 0.07 | PROXY | S1, S2 |
| s5 | 0.09 | 0.16 | 0.25 | PROXY | S8, S9 |
| q | 0.12 | 0.24 | 0.42 | ESTIMATE | S4, S7 |
| d5 | 0.9 | 1 | 1.1 | PROXY | S5, S6, S7 |
| o | 0.48 | 0.68 | 0.85 | ESTIMATE | S1, S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.25 | 0.56 | 1.05 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 2.40 | 4.80 | 8.40 | ESTIMATE |
| D | 4.32 | 6.80 | 9.35 | ESTIMATE |

## Caveats
- a: OEWS is for NAICS 458100 rather than the six-digit code or the narrowed service subset and excludes self-employed workers.
- a: WEF is a global employer survey about occupational change rather than direct wage-weighted task substitution.
- a: The supplied labor ratio is measured at ancestor 44-45 and may not represent service-rich specialty apparel retailers.
- rho: No source directly measures AI implementation or avoided hiring in the target population.
- rho: A large public omnichannel retailer has more capital, data, and technical talent than LMM independents.
- rho: Implementation cannot convert exposed recommendation or service tasks into labor savings when customers value continuous human attention.
- e: Employment mix is not firm mix, and owner labor is absent from OEWS.
- e: Basic alterations may be incidental rather than a material recurring outsourced service.
- e: The supplied LMM firm-count input is missing, preventing conversion of this share into a defensible eligible-firm count.
- s5: Transition intention is not a completed control transfer and the EPI sample is self-selected and cross-industry.
- s5: BizBuySell retail transactions are not specific to apparel or the $1-10 million EBITDA band.
- s5: Internal family succession, minority investments, liquidations, and inventory sales are excluded.
- q: Gap is a large branded retailer, not an LMM service-rich boutique or uniform retailer.
- q: Merchandise gross margin is not retained AI benefit and excludes substantial operating expense.
- q: Retention varies sharply between transparent product sales and differentiated alteration, styling, or program fees.
- d5: Consumer Expenditure estimates include footwear and services beyond 458110 and are survey-based.
- d5: Employment decline can reflect productivity or channel shift and is not direct demand evidence.
- d5: One large retailer's nominal sales are not representative or constant-price.
- o: Total retail e-commerce share is broader than apparel, while Gap's online mix is specific to a large omnichannel company.
- o: Online purchase still requires a retailer or platform operator even when it removes a local service operator.
- o: The estimate concerns quantity needing the lens's accountable service operator, not physical store count or employment.

## Sources
- **S1** — [2022 NAICS Definition: 458110 Clothing and Clothing Accessories Retailers](https://www.census.gov/naics/?details=458110&input=458110&year=2022) (accessed 2026-07-22): Defines the industry as retailers of new clothing and accessories that may provide basic alterations, while assigning custom manufacturing and alteration/repair specialists to other industries.
- **S2** — [Clothing and Clothing Accessories Retailers - May 2023 OEWS](https://www.bls.gov/oes/2023/may/naics4_458100.htm) (accessed 2026-07-22): Reports 76.11% of employment in sales occupations, including 56.76% retail salespersons, 8.85% cashiers, and 9.70% retail supervisors; tailors, dressmakers, and custom sewers are 4,490 workers or 0.52%.
- **S3** — [Future of Jobs Report 2025: Jobs Outlook](https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/2-jobs-outlook/) (accessed 2026-07-22): Identifies cashier and clerical roles among expected decliners and digital access, AI/information processing, and autonomous systems as primary drivers of changing work.
- **S4** — [Quarterly Retail E-Commerce Sales, First Quarter 2026](https://www.census.gov/retail/eCommerce.html) (accessed 2026-07-22): Reports seasonally adjusted U.S. e-commerce sales of $326.7 billion, up 9.8% year over year, representing 16.9% of total retail sales in first-quarter 2026.
- **S5** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects employment in clothing and clothing-accessories retailers to decline from 841,300 in 2024 to 824,400 in 2034, a 2.0% decline.
- **S6** — [Consumer Expenditures 2024](https://www.bls.gov/news.release/cesan.nr0.htm) (accessed 2026-07-22): Reports average household apparel-and-services expenditure of $2,001 in 2024, down 2.0% from $2,041 in 2023 after a 4.9% increase the prior year.
- **S7** — [Gap Inc. Reports Fourth Quarter and Fiscal 2025 Results](https://investors.gapinc.com/press-releases/news-details/2026/Gap-Inc--Reports-Fourth-Quarter-and-Fiscal-2025-Results-Provides-Fiscal-2026-Outlook/default.aspx) (accessed 2026-07-22): Reports fiscal 2025 sales growth of 2%, 39% online sales mix, 40.8% gross margin, 7.3% operating margin, discounting and tariff effects, competition and inventory risks, and an AI-enabled technology agenda.
- **S8** — [2023 National State of Owner Readiness Report](https://exit-planning-institute.org/hubfs/Member%20Center%20Resources/2023%20National%20State%20of%20Owner%20Readiness%20Report.pdf) (accessed 2026-07-22): Surveyed 1,162 U.S. owners across more than 25 industries; reports roughly 73% of privately held companies would like to transition within ten years and documents substantial internal-exit preference.
- **S9** — [BizBuySell 2025 Fourth Quarter Insight Report](https://www.bizbuysell.com/news/bizbuysell-2025-fourth-quarter-insight-report/) (accessed 2026-07-22): Reports flat 2025 retail transaction volume, a 2% decline in median sale price to $250,000, and weaker median retail cash flow amid cost and sales pressure, while noting that strong niche retailers still attracted buyers.
