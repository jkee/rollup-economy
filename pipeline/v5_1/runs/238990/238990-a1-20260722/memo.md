# 238990 — All Other Specialty Trade Contractors

*v5.1 Stage 1 research memo. Run `238990-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.42 · L 0.70 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeatable savings in estimating, coordination, administration, and billing around field crews that remain necessary to deliver the service.
**Weakness:** The code's heterogeneity and project-based, owner-dependent firms make both eligibility and transferability difficult to infer from aggregate data.

## Business-model lens
- Included: US lower-middle-market firms in NAICS 238990 that repeatedly provide outsourced specialty site and structure work to external customers, including private-area paving and sealing, fence and playground installation or repair, crane rental with operator, rigging, scaffolding and shoring, and similar physical specialty services.
- Excluded: One-off consumer-only operators without a repeatable customer base, firms whose economics are primarily equipment rental without an operator, captive internal crews, shells, non-control financing vehicles, and activities classified to other specialty-trade codes.
- Customer and revenue model: Project, work-order, or recurring maintenance revenue from property owners, facilities operators, general contractors, businesses, and government customers; pricing is commonly lump-sum or unit-price, with some multi-year task-order and maintenance arrangements.
- Deviation from default lens: The default recurring-or-repeat outsourced-service lens is applied, but the included population is explicitly limited to firms with repeat customers or repeat work-order potential because NAICS 238990 mixes many unrelated, often one-off construction activities.

## Executive view
This is a broad collection of physical specialty contractors with a limited but usable AI opportunity in office and coordination work. The attraction is not autonomous construction; it is reducing estimating, scheduling, dispatch, billing, compliance, and reporting effort around crews and equipment that remain essential. Heterogeneity, project cyclicality, owner dependence, and uneven transferability are the main constraints.

## How AI changes the work
AI can draft bids and submittals, extract scope from plans and correspondence, assist takeoffs, schedule crews and equipment, triage inbound requests, prepare safety and job documentation, reconcile field records, and accelerate invoicing. Field labor is much less exposed because the occupation mix is dominated by construction and equipment roles, and construction laborers perform overwhelmingly physical, site-bound work.

## Value capture
Fixed-price and unit-price contracts let contractors retain cost savings on already-awarded work, especially where faster administration increases crew utilization or shortens billing cycles. Competitive bids and periodic renewals should return part of those gains to customers, so durable capture depends on service reliability, response time, documentation quality, scarce capabilities, and customer relationships rather than software alone.

## Firm availability
Succession supply should be meaningful because 50.4% of construction employer-firm owners were over 55 in 2021, and construction businesses demonstrably transact. Yet only a portion of the provided LMM firm population combines repeat customers, transferable licenses and relationships, management below the owner, clean financials, and an acceptable equipment and bonding profile.

## Demand durability
BLS projects 5.5% ten-year employment growth for the broader Other Specialty Trade Contractors industry. Physical site work, maintenance, repair, and new construction continue to require operators, although private paving, pools, fencing, and similar activities are exposed to property cycles, interest rates, and customer capital budgets.

## Risks and uncertainty
The six-digit code mixes unrelated activities, while most occupational, owner, adoption, and outlook evidence is available only for broader construction populations. AI adoption may remain shallow at fragmented contractors; benefits may be lost to implementation friction or rebidding; and acquisitions can fail when licenses, estimator knowledge, foremen, customer relationships, or bonding capacity are tied to the seller. A severe construction downturn would also reduce utilization and obscure workflow gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3371 | — | ESTIMATE | — |
| n | — | 228 | — | ESTIMATE | — |
| a | 0.08 | 0.13 | 0.2 | PROXY | S1, S2, S3, S4, S5 |
| rho | 0.22 | 0.4 | 0.62 | PROXY | S6, S7 |
| e | 0.34 | 0.5 | 0.68 | PROXY | S1, S8 |
| s5 | 0.12 | 0.23 | 0.37 | PROXY | S8, S9 |
| q | 0.34 | 0.54 | 0.72 | PROXY | S10 |
| d5 | 0.95 | 1.027 | 1.08 | PROXY | S11 |
| o | 0.86 | 0.94 | 0.98 | PROXY | S1, S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.24 | 0.70 | 1.67 | ESTIMATE |
| F | 3.75 | 5.31 | 6.54 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | PROXY |
| D | 8.17 | 9.65 | 10.00 | PROXY |

## Caveats
- a: OEWS is available at NAICS 238900 rather than 238990 and excludes self-employed workers.
- a: The calculation maps occupations to task exposure judgmentally and is not a direct measurement of avoidable labor.
- a: The OpenAI study measures theoretical task impact, while Anthropic usage is product-specific and not representative of all workers.
- rho: BTOS construction data cover NAICS 23, not 238990 or the LMM lens.
- rho: The 2023-24 and 2025-26 surveys use different adoption vintages and question framing.
- rho: Adoption does not itself establish durable labor substitution.
- e: Customer-type percentages are construction-sector proxies and firms can report multiple customer types.
- e: Repeat customers do not guarantee contractually recurring revenue.
- e: The provided firm-count estimate is margin-bridged and may not match the operating subsegments represented by this eligibility share.
- s5: Owner age is for all construction employer firms and is not a transaction rate.
- s5: BizBuySell sales are voluntarily reported and skew far below the stated EBITDA band.
- s5: Licenses, bonding, key-person relationships, and equipment financing may impair transferability.
- q: Federal rules are a proxy for a market spanning private commercial, general-contractor, residential, and government work.
- q: The estimate does not separately observe bid competition or renewal cadence in 238990.
- q: Benefits from greater throughput may be competed away differently from direct cost savings.
- d5: Employment is an input proxy, not a direct quantity-demand measure.
- d5: The BLS category is broader than NAICS 238990 and the projection horizon is ten years.
- d5: The industry is cyclical and heterogeneous, so subsegments can diverge sharply.
- o: Current occupational intensity is not proof of future technical necessity.
- o: OEWS is for NAICS 238900, not only 238990.
- o: Some estimating, monitoring, and coordination quantities can become software-mediated even while field execution remains operator-required.

## Sources
- **S1** — [2022 Economic Census Construction Questionnaire: Specialty Trade Contractors](https://bhs.econ.census.gov/ombpdfs2022/export/2022_CC-23890_su.pdf) (accessed 2026-07-22): Defines 238990 examples as driveway paving, residential and commercial parking lots, sidewalks, patios, outdoor pools, fence and playground installation, and crane rental with operator; also distinguishes construction workers from office and supervisory staff.
- **S2** — [May 2023 OEWS: NAICS 238900 Other Specialty Trade Contractors](https://www.bls.gov/oes/2023/may/naics4_238900.htm) (accessed 2026-07-22): Reports 777,250 workers and the parent-industry occupation mix, including 62.30% construction and extraction, 9.78% transportation and material moving, 8.50% office support, 5.85% management, 4.73% installation/repair, and 3.61% business and financial operations, with occupation-level wages.
- **S3** — [BLS Occupational Requirements Survey: Construction Laborers](https://www.bls.gov/ors/factsheet/construction-laborers.htm) (accessed 2026-07-22): Documents physical site tasks, less than 0.5% routine telework, greater than 99.5% reaching and low-posture requirements, and an average 89.2% of the workday standing in 2025.
- **S4** — [GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models](https://openai.com/index/gpts-are-gpts/) (accessed 2026-07-22): Provides a task-based theoretical exposure framework and reports that roughly 80% of US workers could have at least 10% of tasks affected and 19% could have at least half affected, with higher-income work more exposed.
- **S5** — [Anthropic Economic Index Report: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report) (accessed 2026-07-22): Finds construction and extraction occupations under-represented in both the AI-user survey and Claude sessions and explains that theoretical exposure is an upper bound that systematically exceeds reported exposure.
- **S6** — [Tracking Firm Use of AI in Real Time: A Snapshot from the Business Trends and Outlook Survey](https://www.census.gov/hfp/btos/downloads/CES-WP-24-16.pdf) (accessed 2026-07-22): Reports 1.4% firm-level AI use in Construction in September 2023-February 2024, 1.9% employment-weighted use, common applications, organizational changes, and limited reported employment reductions.
- **S7** — [The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html) (accessed 2026-07-22): Reports 18% economy-wide firm adoption in November 2025-January 2026, limited functional breadth, 66% augmentation-only use among adopters, and AI-related employment decreases at only 2% of firms.
- **S8** — [The Construction Chart Book, Seventh Edition](https://stacks.cdc.gov/view/cdc/213055/cdc_213055_DS1.pdf) (accessed 2026-07-22): Census-derived construction statistics show 50.4% of employer-firm owners over 55 in 2021 and customer incidence of 69.8% individuals, 42.1% other businesses, and 15.1% government.
- **S9** — [Construction Business Valuation Multiples and Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/building-construction/) (accessed 2026-07-22): Reports 3,142 sold construction listings in its 2021-25 analysis, median days on market of 207, and observed transaction pricing and financial benchmarks, demonstrating an active but selected brokered market.
- **S10** — [FAR 36.207 Pricing Fixed-Price Construction Contracts](https://www.acquisition.gov/far/36.207) (accessed 2026-07-22): States that construction generally uses firm-fixed-price contracts and may be priced on lump-sum, unit-price, or combined bases, with unit pricing especially relevant for paving and uncertain quantities.
- **S11** — [BLS: What's Behind the Projected Construction Employment Growth from 2023 to 2033?](https://www.bls.gov/opub/btn/volume-14/whats-behind-the-projected-construction-employment-growth-from-2023-to-2033.htm) (accessed 2026-07-22): Projects Other Specialty Trade Contractors wage-and-salary employment from 780,000 in 2023 to 823,000 in 2033, a 5.5% increase, and discusses long-run construction demand drivers and cyclicality.
