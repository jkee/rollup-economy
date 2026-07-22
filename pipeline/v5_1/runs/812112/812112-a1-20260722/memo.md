# 812112 — Beauty Salons

*v5.1 Stage 1 research memo. Run `812112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.01 · L 2.32 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat local demand and physically operator-required services preserve the core customer relationship while AI can streamline several surrounding workflows.
**Weakness:** Most labor remains hands-on and relationship-specific, limiting the wage-weighted exposure available for implementation.

## Business-model lens
- Included: Lower-middle-market beauty-salon firms providing repeat hair cutting, styling, coloring, shampooing, facial, makeup, and related cosmetology services directly to external customers, including multi-location and franchised operators when the screened firm operates the service locations.
- Excluded: Independent booth renters outside the screened firm's operations, booth-rental-only landlords, nail-only salons, cosmetology schools, permanent-makeup specialists classified elsewhere, product-only retailers, passive franchisors or trademark owners, shell entities, and captive internal services.
- Customer and revenue model: Customers purchase appointments or walk-in beauty services at posted or quoted per-service prices and often return on a maintenance cycle; operators may also receive product sales and booth or chair rent. Revenue is repeat-oriented but generally transactional rather than contractual.
- Deviation from default lens: none

## Executive view
Beauty salons are repeat, local, externally paid service businesses with a physical and relationship-intensive core. AI can materially improve the surrounding reception, scheduling, records, marketing, merchandising, and administrative workflow, but only a minority of wage-weighted work is exposed because customers buy skilled hands-on execution. Transfer evidence exists for the combined salon-barber market, though direct rates for scaled LMM salons are unavailable.

## How AI changes the work
Packaged tools can handle appointment requests, reminders, routine messages, marketing drafts, customer-record summaries, style-visualization support, basic analytics, inventory prompts, and portions of bookkeeping. Cutting, coloring, styling, treatment, sanitation, live assessment, exception handling, and the trusted customer relationship remain human-delivered.

## Value capture
Per-service pricing permits some administrative savings and utilization improvement to remain with the operator because there is no contractual pass-through. Competition, stylist compensation, software costs, promotions, and reinvestment in experience share the benefit over time, with contractor and booth-rental models altering where value accrues.

## Firm availability
Most scaled operating beauty salons fit the lens, and the frozen firm population is more substantial than for barber shops. BizBuySell confirms an active combined transaction market, but typical sold firms are much smaller than the target band and stylist or owner dependence can impair transferability.

## Demand durability
Repeat hair and beauty maintenance remains physically delivered, and BLS projects growth for hairdressers, hairstylists, and cosmetologists. Real volume can fluctuate with disposable income, at-home alternatives, service frequency, and style trends, while software substitution is concentrated in the surrounding workflow rather than the treatment itself.

## Risks and uncertainty
Key uncertainties are contractor and booth-rental economics, self-employment omitted from employer occupation data, stylist-dependent customer relationships, mixed service lines, and broader-industry proxies. Implementation may displace little payroll if automation merely saves unpaid owner time or if reception labor is already minimized.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.519 | — | OBSERVED | — |
| n | — | 224 | — | ESTIMATE | — |
| a | 0.11 | 0.18 | 0.26 | PROXY | S2, S3 |
| rho | 0.43 | 0.62 | 0.75 | PROXY | S4, S3 |
| e | 0.78 | 0.9 | 0.97 | ESTIMATE | S1, S7 |
| s5 | 0.12 | 0.17 | 0.24 | PROXY | S5, S6 |
| q | 0.48 | 0.6 | 0.72 | ESTIMATE | S1, S3 |
| d5 | 0.98 | 1.03 | 1.08 | PROXY | S7 |
| o | 0.95 | 0.98 | 0.995 | ESTIMATE | S3, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.98 | 2.32 | 4.05 | PROXY |
| F | 4.97 | 5.73 | 6.39 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 9.31 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation mix is for NAICS 812100 and includes barber shops, nail salons, spas, massage businesses, and other personal care services.
- a: Employer data omit self-employed and contractor stylists and may misstate the wage mix of scaled salons.
- a: Task exposure is not whole-job displacement and excludes existing booking and point-of-sale automation.
- rho: BTOS covers all nonfarm businesses and measures any AI use rather than task implementation.
- rho: No published five-year AI adoption cohort specific to beauty salons was identified.
- rho: Some apparent benefit may be conventional workflow automation already deployed and therefore outside current not-yet-automated exposure.
- e: Beauty-salon receipts can include booth rent and retail products alongside services.
- e: Some firms combine beauty, barber, facial, spa, or other activities across establishments and may have a different primary code.
- e: The supplied firm-count estimate is margin-bridged and sensitive to contractor accounting, owner compensation, and multi-establishment firm structure.
- s5: Gallup covers employer businesses across industries rather than beauty salons.
- s5: BizBuySell combines hair salons and barber shops and provides no eligible-firm denominator.
- s5: Marketplace transactions skew much smaller than the frozen EBITDA band and may have greater owner dependence.
- q: No longitudinal study of AI-driven beauty-salon gross benefit retention was identified.
- q: Employee, commission, contractor, and booth-rental models allocate benefits differently.
- q: The range applies only after implementation and does not include demand volume or implementation difficulty.
- d5: Employment is an input measure rather than service quantity.
- d5: BLS occupation projections span work outside beauty salons and include self-employment.
- d5: The horizon conversion assumes the projected decade path is approximately smooth.
- o: This is bounded judgment rather than an observed substitution rate.
- o: Operator requirement varies across haircuts, coloring, facials, makeup, consultation, ancillary retail, and other salon services.
- o: State licensing and safety rules can change over the horizon.

## Sources
- **S1** — [2022 Economic Census Form OS-81210: Personal Care Services](https://bhs.econ.census.gov/ombpdfs2022/export/2022_OS-81210_mu.pdf) (accessed 2026-07-22): Identifies beauty salons, unisex shops, day spas with hair services, facial salons, and barber shops as classified activities and lists hair, skin, retail, and booth-rental receipt categories.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 812100](https://www.bls.gov/oes/2023/may/naics4_812100.htm) (accessed 2026-07-22): Provides the broader personal-care occupation and wage mix, including hairdressers, personal appearance workers, management, reception, and administrative employment used for the exposure proxy.
- **S3** — [O*NET OnLine: Hairdressers, Hairstylists, and Cosmetologists](https://www.onetonline.org/link/details/39-5012.00) (accessed 2026-07-22): Lists hands-on cutting, coloring, styling, sanitation, assessment, appointment, records, payment, sales, supply, training, and administrative tasks and documents continual manual and close-contact work.
- **S4** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports recent U.S. business use and near-term expected use of AI by firm size, used as a broad implementation anchor.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports five-year sell-or-transfer plans among U.S. business owners, including a higher rate for employer-business owners, used as a broad transfer-intent proxy.
- **S6** — [BizBuySell Insight Report Data Tables: Full-Year 2025](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-22): Reports completed hair-salon and barber-shop marketplace transactions and transaction characteristics, confirming an active but combined and mostly small-business transfer market.
- **S7** — [Occupational Outlook Handbook: Barbers, Hairstylists, and Cosmetologists](https://www.bls.gov/ooh/personal-care-and-service/barbers-hairstylists-and-cosmetologists.htm) (accessed 2026-07-22): Describes duties, licensing, work setting, and the 2024–2034 employment outlook, including the hairdresser, hairstylist, and cosmetologist projection used for the demand proxy.
