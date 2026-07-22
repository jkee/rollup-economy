# 541830 — Media Buying Agencies

*v5 Stage 1 research memo. Run `541830-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 5.49 · L 2.41 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeatable analytical, operational, and administrative media-buying workflows create a bounded but material opportunity for AI-assisted labor reduction.
**Weakness:** Platform self-service and client procurement can both reduce outsourced demand and pass agency productivity gains back to customers.

## Business-model lens
- Included: Independent lower-middle-market agencies that repeatedly buy or manage advertising time or space for external advertiser or agency customers, including planning, trafficking, optimization, reporting, and negotiated media purchasing.
- Excluded: Captive advertiser buying teams, media-owner sales representatives, full-service creative agencies whose buying is incidental, shell entities, and financing vehicles are excluded.
- Customer and revenue model: External customers buy recurring campaign-management and media-buying services through fees, retainers, project scopes, commissions, or combinations; media spend itself is typically a client pass-through rather than agency revenue retained as operating value.
- Deviation from default lens: none

## Executive view
Media buying agencies provide a repeat outsourced service with meaningful AI-enabled workflow opportunity, but the opportunity is tempered by variable agency transferability, customer bargaining, and rapid platform self-service. The code specifically covers buying advertising time or space from media outlets for resale to agencies or advertisers.

## How AI changes the work
The broad advertising-services occupational mix contains substantial management, business-operations, sales, and office-support work, including 8.15% market research analysts and marketing specialists. AI can accelerate research, reporting, trafficking support, documentation, QA, and analysis, but it does not remove the need for accountable judgment in negotiation, measurement, client communication, and brand-safety decisions.

## Value capture
Agency economics use fees, retainers, labor-based fees, fixed-output fees, and sometimes commissions. ANA reports that 82% of surveyed respondents use a fee model in at least one agency agreement, while its media-agency survey found frequent contract updates and client return of many rebates; savings are therefore susceptible to repricing or scope expansion rather than being fully retained.

## Firm availability
Eligibility should be meaningful because the NAICS activity itself is outsourced media buying, but it is reduced by founder dependency, client concentration, network ownership, and weak operating controls. The Federal Reserve's employer-firm survey shows 55% of primary owners are at least 55, which supports a succession pipeline but is not evidence that a comparable share will sell. BizBuySell confirms a broad active transaction channel but not six-digit agency control-transfer rates.

## Demand durability
U.S. internet advertising revenue was $258.6 billion in 2024, 14.9% above 2023, and related marketing occupations have positive ten-year projections. Those are encouraging demand signals, yet they are not constant-dollar outsourced-buying volume. Growth can move to self-service platforms, in-house teams, or large integrated agencies.

## Risks and uncertainty
The principal evidence gap is six-digit data: BLS occupation evidence is for NAICS 541800, deal and owner evidence is cross-sector, and no source directly observes AI implementation or profit retention for LMM media buyers. Client concentration, platform terms, rebate transparency, ad-spend cyclicality, and the speed of self-service adoption can each materially weaken the operating case.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2759 | — | OBSERVED | — |
| n | — | 121 | — | ESTIMATE | — |
| a | 0.3 | 0.42 | 0.55 | PROXY | S2 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S2, S6 |
| e | 0.4 | 0.55 | 0.7 | ESTIMATE | S1, S9 |
| s5 | 0.08 | 0.15 | 0.25 | PROXY | S8, S9 |
| q | 0.28 | 0.42 | 0.58 | ESTIMATE | S5, S6 |
| d5 | 0.92 | 1.04 | 1.18 | PROXY | S3, S4, S7 |
| o | 0.55 | 0.7 | 0.82 | ESTIMATE | S1, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.16 | 2.41 | 4.13 | ESTIMATE |
| F | 2.55 | 3.85 | 4.98 | ESTIMATE |
| C | 5.60 | 8.40 | 10.00 | ESTIMATE |
| D | 5.06 | 7.28 | 9.68 | ESTIMATE |

## Caveats
- a: The only usable BLS industry occupation table is four-digit NAICS 541800, which includes creative, PR, and media-representative businesses outside this lens.
- a: Exposure is a task judgment, not an observed automation rate.
- rho: No source measures implemented AI labor savings for the frozen six-digit lens.
- rho: Implementation rates will differ sharply between programmatic specialists and relationship-led traditional-media buyers.
- e: The NAICS definition identifies activity, not EBITDA, ownership independence, customer concentration, or transferability.
- e: Marketplace data omit many privately negotiated sales and cannot establish eligibility for all firms.
- s5: S8 uses a nonrandom convenience sample that is weighted to small employer firms and is not industry-specific.
- s5: S9's transactions are voluntarily reported and do not distinguish control transfers, LMM EBITDA, or the NAICS code.
- q: ANA survey respondents are marketer members and may not represent LMM agencies.
- q: The sources describe compensation practices, not the discounted fraction of an AI-generated gross benefit retained by an operator.
- d5: Digital ad revenue is nominal spend and includes inventory purchased without an external agency.
- d5: National occupational projections are not a forecast for NAICS 541830 or a five-year constant-quality service basket.
- o: The cited programmatic figures are from a 2019 ANA report and its surveyed advertisers are not a census of LMM customers.
- o: No source directly measures the five-year operator-required share for the frozen lens.

## Sources
- **S1** — [Census NAICS 541830 Media Buying Agencies definition](https://www.census.gov/naics/resources/archives/sect54.html) (accessed 2026-07-22): Defines 541830 as establishments purchasing advertising time or space from media outlets and reselling it to advertising agencies or individual companies, and distinguishes media representatives and full-service advertising agencies.
- **S2** — [BLS May 2023 OEWS industry-specific occupational employment and wage estimates, NAICS 541800](https://www.bls.gov/oes/2023/May/naics4_541800.htm) (accessed 2026-07-22): Reports the national occupation mix and wages for Advertising, Public Relations, and Related Services, including management, business operations, market research, sales, and office-support occupations.
- **S3** — [BLS Occupational Outlook Handbook: Market Research Analysts](https://www.bls.gov/ooh/business-and-financial/market-research-analysts.htm) (accessed 2026-07-22): Reports projected 7% employment growth for market research analysts and marketing specialists from 2024 to 2034.
- **S4** — [BLS Occupational Outlook Handbook: Advertising, Promotions, and Marketing Managers](https://www.bls.gov/ooh/management/advertising-promotions-and-marketing-managers.htm) (accessed 2026-07-22): Reports 6% projected employment growth for advertising, promotions, and marketing managers from 2024 to 2034.
- **S5** — [ANA Trends in Agency Compensation report summary](https://www.ana.net/content/show/id/76981) (accessed 2026-07-22): Reports 82% use of fee-based compensation in at least one agency agreement and describes labor-based and fixed or output-based agency fees.
- **S6** — [ANA Media Agency Compensation Practices](https://www.ana.net/blogs/show/id/mm-blog-2019-09-media-agency-compensation-practices) (accessed 2026-07-22): Reports media-agency contract updates, rebate treatment, fee and commission practices, programmatic use, and some in-house or third-party programmatic buying.
- **S7** — [IAB/PwC Digital Ad Revenue Surges 15% YoY in 2024](https://www.iab.com/news/digital-ad-revenue-2024/) (accessed 2026-07-22): Reports 2024 U.S. internet advertising revenue of $258.6 billion, up 14.9% year over year, with category growth figures.
- **S8** — [Federal Reserve Small Business Credit Survey 2024 Report on Employer Firms](https://www.fedsmallbusiness.org/-/media/project/clevelandfedtenant/fsbsite/reports/2024/2024-report-on-employer-firms.pdf) (accessed 2026-07-22): Reports the weighted U.S. small employer-firm primary-owner age distribution, including 33% age 55–64 and 22% age 65 or older, and documents sampling limitations.
- **S9** — [BizBuySell Insight Report](https://www.bizbuysell.com/insight-report/) (accessed 2026-07-22): Describes the national small-business marketplace's analysis of listings and voluntarily broker-reported closed transactions across 65 industries.
