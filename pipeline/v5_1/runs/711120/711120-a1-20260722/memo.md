# 711120 — Dance Companies

*v5.1 Stage 1 research memo. Run `711120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.96 · L 1.21 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digitally exposed administrative and commercial workflows sit beside a live service that still requires an accountable human operator.
**Weakness:** Nonprofit governance and scarce observed control transfers may leave very few genuinely acquirable LMM firms.

## Business-model lens
- Included: US dance companies producing recurring or repeat live dance performances and related contracted programs for ticket buyers, presenters, schools, sponsors, and community or institutional customers, within the roughly $1-10M normalized EBITDA band.
- Excluded: Independent dancers and choreographers, dance schools without a producing company, captive university or municipal ensembles, shells, non-control financing vehicles, and organizations whose charitable governance cannot support a qualifying control transaction.
- Customer and revenue model: A mixed model of fixed-price tickets and subscriptions, presenter or institutional performance fees, education and outreach contracts, sponsorship, and contributed or grant revenue; the recurring-service screen is met through repeated seasons, tours, residencies, and programs rather than continuous service contracts.
- Deviation from default lens: none

## Executive view
Dance companies contain a real but bounded AI labor opportunity in fundraising, marketing, ticketing, scheduling, finance, and documentation. The artistic and physical delivery core remains human, while the more consequential constraint is that a large portion of the sector is nonprofit, mission-governed, and not conventionally transferable.

## How AI changes the work
AI can draft campaigns and grant materials, segment patrons, answer routine customer questions, reconcile and classify records, prepare schedules and production documents, and generate first-pass creative collateral. It is more likely to reduce administrative hiring and increase staff throughput than to replace dancers, choreographers, rehearsal directors, technicians, or accountable artistic leadership.

## Value capture
Fixed ticket and program pricing provides some initial insulation from direct labor-cost pass-through. Over time, however, presenters, funders, workers, and competing arts organizations can claim part of the benefit, and nonprofits may reinvest savings into mission delivery rather than convert them into owner cash flow.

## Firm availability
A modeled LMM population exists, but legal form and governance sharply narrow the truly acquirable set. Conventional equity control is most plausible among for-profit operators; nonprofit mergers or board-control changes can qualify only when governance, mission, assets, and operating continuity support a genuine control transaction.

## Demand durability
Live dance remains differentiated by embodied performance and communal attendance, and BLS expects modest growth in the broader performing-arts industry and dancer occupations. The downside is that measured ballet and other-dance attendance was materially lower in 2022 than 2017, while funding constraints and local concentration make recovery uneven.

## Risks and uncertainty
The nearest staffing and output data combine dance with theater and music; nonprofit counts do not map neatly to NAICS or EBITDA; pandemic-era revenue and attendance distort trend inference; contractors are poorly captured; and no reliable industry transfer series exists. A roll-up could fail through insufficient transferable targets, founder or artistic-director dependence, donor flight, mission conflict, weak attendance, or quality damage from over-automation.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5794 | — | OBSERVED | — |
| n | — | 26 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.34 | PROXY | S1, S2 |
| rho | 0.38 | 0.58 | 0.74 | PROXY | S2, S3 |
| e | 0.1 | 0.24 | 0.42 | ESTIMATE | S4, S5 |
| s5 | 0.08 | 0.18 | 0.32 | ESTIMATE | S4, S5 |
| q | 0.38 | 0.58 | 0.76 | ESTIMATE | S4 |
| d5 | 0.91 | 1.06 | 1.17 | PROXY | S6, S7, S8 |
| o | 0.78 | 0.9 | 0.97 | ESTIMATE | S7, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.23 | 3.09 | 5.83 | PROXY |
| F | 0.30 | 1.21 | 2.42 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.10 | 9.54 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source is NAICS 711100, not 711120, and excludes self-employed workers.
- a: Observed AI usage is not the same as feasible substitution and is concentrated among users of one model provider.
- a: Seasonal artists and contractors may not be represented consistently in employer payroll data.
- rho: Neither source measures dance-company implementation.
- rho: The customer-support study concerns conversational service work in a Fortune 500 software setting.
- rho: Implementation depends on integration with ticketing, donor CRM, payroll, and rights-management systems.
- e: The 4,762 count covers dance-related nonprofits, not only NAICS 711120 or the LMM band.
- e: Dataset n is margin-bridged from firm counts and average receipts and may not identify nonprofit economics cleanly.
- e: Eligibility of nonprofit combinations is jurisdiction- and charter-specific.
- s5: There is no observed denominator of eligible dance companies and no industry-specific transfer series.
- s5: Nonprofit leadership succession is not automatically a qualifying control transfer.
- s5: Distress may produce closures or asset transfers that fail the transferable-operation test.
- q: Revenue mix is from nonprofit dance companies during a pandemic-distorted period.
- q: Retained gross benefit is not the same as distributable profit in a charitable organization.
- q: Grant restrictions and collective-bargaining or artist-contract terms vary widely.
- d5: BLS output is for NAICS 711100 and includes theater, music, and other performing arts companies.
- d5: The NEA's 2017-2022 comparison captures pandemic disruption and is not a normalized trend.
- d5: Employment growth is only an indirect indicator of constant-quality service demand.
- o: The estimate concerns the current service basket, not all future entertainment spending.
- o: High-quality generated video and self-service instruction could displace peripheral products faster than live performances.
- o: Operator requirement does not guarantee profitable demand.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 711100 Performing Arts Companies](https://www.bls.gov/oes/2023/May/naics4_711100.htm) (accessed 2026-07-22): Occupation mix and wages for the nearest published industry: 135,030 total employment; management 8.62%; arts/design/entertainment/sports/media 41.79%; office and administrative support 7.48%; dancers and choreographers 3.39%; and source limitations including exclusion of self-employed workers.
- **S2** — [Anthropic Economic Index report: Economic primitives](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) (accessed 2026-07-22): Observed November 2025 AI-use patterns: office and administrative support reached 13% of enterprise API transcripts after a 3 percentage-point rise; the report identifies email, document processing, CRM, and scheduling, and reports creative writing and editing use in arts-related tasks.
- **S3** — [Measuring the Productivity Impact of Generative AI](https://www.nber.org/digest/20236/measuring-productivity-impact-generative-ai) (accessed 2026-07-22): Field evidence from 5,179 customer-support agents: AI assistance increased issues resolved per hour by nearly 14% on average, with larger gains among less-experienced workers.
- **S4** — [Conjuring Arts Data from Tax Forms and Taxonomies—How a Dance Researcher Does It](https://www.arts.gov/stories/blog/2024/conjuring-arts-data-from-tax-forms-and-taxonomies-how-dance-researcher-does-it) (accessed 2026-07-22): Dance/USA's 708-company nonprofit panel, estimate of 4,762 actively registered nonprofit dance-related organizations, 2018-2022 revenue and employment changes, project-based contracting, and the shift from 54/46 earned/contributed revenue to 40/60.
- **S5** — [Inurement/private benefit: Charitable organizations](https://www.irs.gov/charities-non-profits/charitable-organizations/inurement-private-benefit-charitable-organizations) (accessed 2026-07-22): IRS rule that a 501(c)(3) may not be organized or operated for private interests and that no part of net earnings may inure to a private shareholder or individual, constraining conventional owner economics and transferability.
- **S6** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS 2024-2034 chained-2017-dollar projection for NAICS 711100: output rises from $29.8 billion to $36.9 billion, a 2.1% compound annual rate, while employment rises 3.6%.
- **S7** — [Arts Participation Patterns in 2022: Highlights from the Survey of Public Participation in the Arts](https://www.arts.gov/sites/default/files/2022-SPPA-final.pdf) (accessed 2026-07-22): US adult attendance evidence: ballet fell from 3.1% in 2017 to 2.0% in 2022, and other dance from 6.3% to 3.3%, with the period materially affected by the pandemic.
- **S8** — [Dancers and Choreographers: Occupational Outlook Handbook](https://www.bls.gov/ooh/entertainment-and-sports/dancers-and-choreographers.htm) (accessed 2026-07-22): Core duties requiring embodied human work and coordination, plus a 5% employment-growth projection from 17,000 jobs in 2024 to 17,800 in 2034 and BLS's note that funding constraints may offset demand.
