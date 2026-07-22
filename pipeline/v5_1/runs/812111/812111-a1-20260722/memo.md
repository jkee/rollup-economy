# 812111 — Barber Shops

*v5.1 Stage 1 research memo. Run `812111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.85 · L 0.72 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat local demand and a physically operator-required service preserve the customer relationship while AI improves surrounding administrative workflows.
**Weakness:** Only a modest share of wage-weighted work is AI-exposed, and the estimated LMM firm population is exceptionally sparse.

## Business-model lens
- Included: Lower-middle-market barber-shop firms providing repeat haircutting, trimming, styling, shaving, beard care, and closely related grooming services directly to external customers, including multi-location and franchised operators when the screened firm operates the service locations.
- Excluded: Independent booth renters that are not part of the screened firm's operations, booth-rental-only landlords, cosmetology and barber schools, product-only retailers, passive franchise or trademark owners, shell entities, and captive internal grooming operations.
- Customer and revenue model: Customers usually purchase appointments or walk-in grooming services at posted per-service prices and return periodically; operators may also receive product sales and booth or chair rent. Revenue is transactional but highly repeat-oriented rather than contractually recurring.
- Deviation from default lens: none

## Executive view
Barber shops are repeat, local, externally paid services with a highly physical core. AI can reduce scheduling, reception, records, marketing, and administrative work, but the exposed share is modest because the customer is buying skilled manual execution and interpersonal judgment. The transfer market is observable, though evidence for scaled LMM firms is thin and owner dependence remains important.

## How AI changes the work
Packaged tools can handle appointment requests, reminders, routine customer messages, marketing drafts, record summaries, basic analytics, supply prompts, and portions of bookkeeping. The haircut, shave, sanitation, live consultation, exception handling, and customer relationship remain human-delivered.

## Value capture
Menu pricing permits some administrative savings and utilization improvement to remain with the operator because there is no contractual pass-through. Local competition, barber compensation, software expense, and promotions will share the benefit over time, with economics varying sharply between employee, commission, and booth-rental models.

## Firm availability
Most scaled operating barber shops fit the service lens, but the supplied LMM count is sparse and estimated. BizBuySell confirms category transactions, yet its typical sold business is much smaller and the combined salon-barber data do not establish a direct transfer rate for the target cohort.

## Demand durability
Repeat hair and beard care remains physically delivered and BLS projects modest barber employment growth. Real service quantity can still fluctuate with household budgets, visit frequency, home grooming, and fashion, but software substitution is much more likely in the surrounding workflow than in the core service.

## Risks and uncertainty
The largest uncertainties are the extremely small estimated firm population, contractor and booth-rental economics, self-employment omitted from employer occupation data, owner-dependent customer relationships, and the use of broader personal-care evidence. AI savings may also be confused with ordinary booking automation already in place.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.7659 | — | OBSERVED | — |
| n | — | 4 | — | ESTIMATE | — |
| a | 0.09 | 0.15 | 0.22 | PROXY | S2, S3 |
| rho | 0.4 | 0.58 | 0.72 | PROXY | S4, S3 |
| e | 0.75 | 0.88 | 0.96 | ESTIMATE | S1, S7 |
| s5 | 0.12 | 0.16 | 0.22 | PROXY | S5, S6 |
| q | 0.5 | 0.62 | 0.74 | ESTIMATE | S1, S3 |
| d5 | 0.97 | 1.02 | 1.06 | PROXY | S7 |
| o | 0.97 | 0.985 | 0.997 | ESTIMATE | S3, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.10 | 2.67 | 4.85 | PROXY |
| F | 0.49 | 0.72 | 0.99 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.41 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation mix is for NAICS 812100 and includes beauty salons, nail salons, spas, massage businesses, and other personal care services.
- a: OEWS employer data omit much self-employment; BLS reports that self-employed workers hold most barber jobs.
- a: Task exposure is not whole-job displacement and excludes work already automated by ordinary booking and point-of-sale software.
- rho: BTOS covers all nonfarm businesses and measures any AI use, not labor-task implementation.
- rho: No published five-year adoption cohort specific to barber shops was identified.
- rho: Some apparent AI benefit may be conventional workflow automation and is excluded where already deployed.
- e: The Economic Census form instructs barber and beauty shops to include booth rent, so industry receipts can mix service operation and landlord economics.
- e: The supplied firm-count estimate is very small and margin-bridged, making the eligible count highly sensitive to classification and normalized owner compensation.
- e: A firm may operate several establishments or combine barbering with beauty services.
- s5: Gallup covers employer businesses across industries rather than barber shops.
- s5: BizBuySell combines hair salons and barber shops and does not provide the eligible-firm denominator.
- s5: Marketplace transactions skew much smaller than the frozen EBITDA band and may have greater owner dependence.
- q: No longitudinal study of AI-driven barber-shop gross benefit retention was identified.
- q: Booth-rental and employee or commission models allocate benefits differently.
- q: The range applies only after implementation and does not include demand volume or implementation difficulty.
- d5: Employment is an input measure rather than service quantity.
- d5: BLS projections combine employer and self-employed work and are national.
- d5: The horizon conversion assumes the projected decade path is approximately smooth.
- o: This is bounded judgment rather than an observed substitution rate.
- o: Operator requirement may vary for ancillary retail, consultation, and simple grooming services.
- o: State licensing and safety rules can change over the horizon.

## Sources
- **S1** — [2022 Economic Census Form OS-81210: Personal Care Services](https://bhs.econ.census.gov/ombpdfs2022/export/2022_OS-81210_mu.pdf) (accessed 2026-07-22): Identifies barber shops and beauty salons as separate primary activities, lists hair-care service and booth-rental receipt categories, and instructs shops to include booth or chair rents in operating receipts.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 812100](https://www.bls.gov/oes/2023/may/naics4_812100.htm) (accessed 2026-07-22): Provides the broader personal-care occupation and wage mix, including personal appearance, management, reception, and administrative employment used for the exposure proxy.
- **S3** — [O*NET OnLine: Barbers](https://www.onetonline.org/link/summary/39-5011.00) (accessed 2026-07-22): Lists hands-on cutting, shaving, sanitation, consultation, sales, records, payment, ordering, and clerical tasks and documents the close physical and manual nature of barber work.
- **S4** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports recent U.S. business use and near-term expected use of AI by firm size, used as a broad implementation anchor.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports five-year sell-or-transfer plans among U.S. business owners, including a higher rate for employer-business owners, used as a broad transfer-intent proxy.
- **S6** — [BizBuySell Insight Report Data Tables: Full-Year 2025](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-22): Reports completed hair-salon and barber-shop marketplace transactions and transaction characteristics, confirming an active but combined and mostly small-business transfer market.
- **S7** — [Occupational Outlook Handbook: Barbers, Hairstylists, and Cosmetologists](https://www.bls.gov/ooh/personal-care-and-service/barbers-hairstylists-and-cosmetologists.htm) (accessed 2026-07-22): Describes service duties, licensing, self-employment, and the 2024–2034 employment outlook, including the barber-specific projection used for the demand proxy.
