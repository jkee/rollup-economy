# 541830 — Media Buying Agencies

*v5.1 Stage 1 research memo. Run `541830-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.18 · L 3.98 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Remaining manual campaign planning, optimization, analytics, and reporting are directly exposed to AI in a large and growing digital advertising market.
**Weakness:** The same AI and platform capabilities that create labor efficiency also let clients self-serve and reprice agency work, while accounting for media pass-through obscures true firm size and labor intensity.

## Business-model lens
- Included: US lower-middle-market agencies providing repeat outsourced media planning and buying, price and placement negotiation, campaign trafficking, performance monitoring, research, verification, and post-campaign analysis for advertisers or other agencies.
- Excluded: Media sales representatives, publishers and media owners, creative-only advertising agencies, software-only adtech vendors, captive in-house buying teams, shell firms, and non-control financing vehicles.
- Customer and revenue model: Advertisers and agencies engage media buyers through recurring retainers, labor-based fees, fixed or output-based fees, commissions or percentage-of-spend arrangements, and occasional performance incentives; client media spend may flow through agency receipts.
- Deviation from default lens: none

## Executive view
Media buying is already software-mediated, but the next automation wave reaches the remaining human workflow: planning, partner selection, forecasting, optimization, and reporting. The service should retain a meaningful external role where agencies combine cross-platform judgment, negotiation, measurement, governance, and client accountability, though self-service and insourcing are unusually credible substitutes.

## How AI changes the work
AI can generate media plans, segment audiences, forecast outcomes, traffic and optimize campaigns, reconcile data, draft reports, and monitor exceptions. The practical ceiling is set by fragmented and proprietary data, privacy, brand safety, attribution ambiguity, platform conflicts, and client approval; implementation should be substantial but still supervised.

## Value capture
Labor-based compensation remains common and will transmit some efficiency gains through lower staffing or fee resets. Fixed, output-based, commission, retainer, and performance structures can retain more value initially, but transparent digital metrics, frequent pitches, client procurement, and credible insourcing limit five-year retention.

## Firm availability
Recurring client assignments make many agencies conceptually eligible, but net economic revenue can be obscured by pass-through media billings and transferability can be weakened by founder relationships, account concentration, and platform dependence. Broad owner data and active marketing-services M&A support deal availability without establishing a 541830-specific transfer rate.

## Demand durability
Digital, programmatic, video, commerce, and creator advertising continue to expand, and channel fragmentation increases planning and measurement complexity. Against that, direct platform tools and agentic buying reduce the amount of current agency work required per dollar of spend, while cyclical ad budgets make demand volatile.

## Risks and uncertainty
The largest risks are brand insourcing, autonomous platform buying, fee compression, customer concentration, opaque media rebates or pass-through accounting, privacy and governance failures, platform dependency, and inability to prove incrementality. A recession or rapid standardization of cross-platform agents could reduce both agency volumes and retained economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2759 | — | OBSERVED | — |
| n | — | 121 | — | ESTIMATE | — |
| a | 0.42 | 0.58 | 0.72 | PROXY | S2, S3, S4 |
| rho | 0.48 | 0.65 | 0.8 | PROXY | S4, S6 |
| e | 0.42 | 0.6 | 0.75 | ESTIMATE | S1, S2 |
| s5 | 0.09 | 0.15 | 0.22 | PROXY | S8, S9 |
| q | 0.3 | 0.46 | 0.62 | PROXY | S4, S7 |
| d5 | 0.92 | 1.12 | 1.3 | PROXY | S5, S6, S10 |
| o | 0.48 | 0.66 | 0.8 | PROXY | S2, S4, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.22 | 4.16 | 6.36 | PROXY |
| F | 2.76 | 3.98 | 4.89 | ESTIMATE |
| C | 6.00 | 9.20 | 10.00 | PROXY |
| D | 4.42 | 7.39 | 10.00 | PROXY |

## Caveats
- a: OEWS is available only for NAICS 541800 and includes media representatives, creative agencies, public relations, and other businesses unlike media buyers.
- a: IAB evidence describes organizations across the buy and sell sides, not wage-weighted tasks in LMM media buying agencies.
- a: The frozen labor ratio uses 2024 wages over 2022 receipts and may be materially distorted because receipts can include resold or pass-through media spend; it is also harmonized by a cross-industry median adjustment.
- rho: Full campaign-lifecycle integration is not the same as implementing a given share of labor substitution.
- rho: IAB respondents skew toward digitally engaged industry participants and may be more advanced than LMM agencies.
- rho: Ad-platform automation can shift work rather than eliminate it by increasing campaign variants and measurement demands.
- e: No source measures the share of 541830 firms satisfying every LMM lens condition.
- e: The frozen firm count uses a generic 15.65% margin bridge; media pass-through accounting and commission structures can make receipts a poor proxy for agency economic revenue and therefore distort size-band membership.
- s5: Gallup measures intentions across all employer industries, not completed media-agency transfers.
- s5: Capstone covers broad marketing services and middle-to-large transactions without an at-risk firm denominator.
- s5: Agency client relationships can be nontransferable even when the legal entity is sold.
- q: ANA's 2022 sample is small, includes large marketers, and is not media-buying-only.
- q: Compensation method incidence does not reveal revenue shares, contract duration, or realized pass-through.
- q: The five-year discounted retention rate depends on future client procurement and competitor adoption that are not observed.
- d5: Digital ad revenue is publisher/platform revenue, not agency service quantity.
- d5: One-year nominal growth and buyer plans are cyclical and do not directly measure five-year constant-price demand.
- d5: Political and sports events, recession, privacy rules, and platform changes can materially alter spending.
- o: Current AI adoption and stated buyer priorities do not directly measure eliminated agency service quantity.
- o: The operator/software boundary is fluid because agencies can embed proprietary technology and sell managed outcomes.
- o: Large platforms may both automate execution and increase demand for independent verification and cross-platform accountability.

## Sources
- **S1** — [2022 NAICS Definition: 541830 Media Buying Agencies](https://www.census.gov/naics/?details=541&input=541&year=2022) (accessed 2026-07-22): Defines the industry as establishments purchasing advertising time or space from media outlets and reselling it to agencies or individual companies.
- **S2** — [NAPCS Product List for NAICS 54183: Media Buying Agencies](https://www2.census.gov/library/reference/napcs/product-list/web-54183-final-reformatted-edited-us082208.pdf) (accessed 2026-07-22): Describes full-service planning and buying, price and placement negotiation, trafficking, monitoring, post-campaign analysis, research, competitive reporting, and verification.
- **S3** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 541800](https://www.bls.gov/oes/2023/May/naics4_541800.htm) (accessed 2026-07-22): Reports broader advertising-services employment shares, including management 16.77%, business and financial operations 16.65%, computer and mathematical 5.18%, arts/design/media 24.48%, sales 18.41%, office support 11.22%, and market research analysts 8.15%.
- **S4** — [IAB State of Data 2025: AI Is on the Brink of Transforming How Advertising Works at Its Core](https://www.iab.com/news/iab-state-of-data-report-2025/) (accessed 2026-07-22): Reports 30% full AI integration across the campaign lifecycle, near-term adoption intentions, AI-capable media functions, data and tool barriers, transparency concerns, and agency fears of client insourcing.
- **S5** — [Digital Ad Revenue Climbs to Nearly $300B as IAB Celebrates 30 Year Anniversary](https://www.iab.com/news/digital-ad-revenue-climbs-to-nearly-300b-as-iab-celebrates-30-year-anniversary/) (accessed 2026-07-22): Reports US digital ad revenue of $294.6 billion in 2025, up 13.9%, and programmatic revenue of $162.4 billion, up 20.5%, as automated buying scales.
- **S6** — [2026 Outlook: A Snapshot of U.S. Ad Spend, Opportunities, and Strategies for Growth](https://www.iab.com/insights/2026-outlook/) (accessed 2026-07-22): Reports buyers projected 9.5% ad-spend growth in 2026, or 7.1%–7.8% excluding major events, and that AI dominated buyer focus areas as campaign execution shifts toward core AI infrastructure.
- **S7** — [Labor-Based Fees Remain Dominant Form Of Agency Compensation: ANA Report](https://www.ana.net/content/show/id/76981) (accessed 2026-07-22): Reports 82% of marketers used fee-based compensation in at least one agency agreement, smaller advertisers used labor-based fees at 76%, fixed/output models were increasing, and 51% planned compensation changes for full-service agencies.
- **S8** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 22% of US employer-business owners planned to sell or transfer ownership within five years and documents the gap between employer and nonemployer transferability.
- **S9** — [Marketing Services Market Update](https://www.capstonepartners.com/insights/report-marketing-services-market-update/) (accessed 2026-07-22): Reports marketing-services M&A volume rose each year from 2023 through 2025 at an average 4.7% annual rate and was up 7.5% year to date in 2026, with buyer preference for recurring, low-concentration, technology-enabled targets.
- **S10** — [Occupational Outlook Handbook: Advertising, Promotions, and Marketing Managers](https://www.bls.gov/ooh/management/advertising-promotions-and-marketing-managers.htm) (accessed 2026-07-22): Projects 6% overall employment growth for advertising, promotions, and marketing managers from 2024 to 2034 but a 2% decline for advertising and promotions managers.
