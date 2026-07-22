# 327320 — Ready-Mix Concrete Manufacturing

*v5.1 Stage 1 research memo. Run `327320-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.06 · L 0.84 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is the combination of a non-digital, locally delivered product with recurring, data-rich dispatch and administrative workflows where better coordination can improve fleet and plant utilization.
**Weakness:** The principal weakness is that the majority of operating labor sits in production and transportation, making the addressable task share modest and leaving results sensitive to construction cycles and implementation quality.

## Business-model lens
- Included: Independent US establishments manufacturing and delivering ready-mix concrete, including batching, dispatch, fleet scheduling, sales, quality documentation, billing, and plant administration.
- Excluded: Cement manufacturing, aggregate mining, precast concrete, construction placement, captive activities that cannot be separated from a larger vertically integrated owner, and establishments outside the United States.
- Customer and revenue model: Primarily business-to-business sales priced per cubic yard and delivered within a local service radius to contractors and construction projects; delivery timing, mix specification, and fleet availability are integral to the sale.
- Deviation from default lens: none

## Executive view
Ready-mix combines a stubbornly physical local delivery network with a meaningful layer of dispatch, sales, administrative, quality, and fleet-coordination work. The opportunity is therefore operational augmentation around a durable physical product, not replacement of the production and driving workforce.

## How AI changes the work
The most credible applications are order intake, dispatch support, route and load planning, quote preparation, customer communication, invoice exception handling, quality-document retrieval, preventive-maintenance triage, and management reporting. The central limit is that production and transportation dominate employment and require people, equipment, and accountable real-world execution.

## Value capture
Local service radii, time-sensitive delivery, and plant and truck capacity can let reliable operators retain part of productivity gains through improved utilization, fewer errors, avoided hiring, and stronger service. Competitive bids, negotiated contracts, customer concentration, and volatile input and construction markets prevent full retention.

## Firm availability
The industry has thousands of plants and a material lower-middle-market firm universe. A mature owner base supports succession activity, but firm-level screening is required to remove captive operations, vertically integrated entities, and non-operating or non-separable companies and to distinguish age from actual willingness to sell.

## Demand durability
Concrete demand is tied to essential construction and infrastructure, and the delivered product is difficult to digitize or offshore. Durability is tempered by pronounced construction cyclicality: recent real output is above 2019 but below its 2022 level, and the near-term cement outlook anticipates contraction before recovery.

## Risks and uncertainty
The largest uncertainties are ready-mix-specific task exposure, integration and adoption rates, local price competition, regional construction cycles, owner sale intent, and substitution at particular project types. Several inputs rely on broader-industry or cross-industry proxies, so diligence should prioritize plant-level workflow and transaction evidence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2071 | — | OBSERVED | — |
| n | — | 723 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.32 | PROXY | S1, S2 |
| rho | 0.28 | 0.48 | 0.65 | PROXY | S4 |
| e | 0.65 | 0.8 | 0.9 | ESTIMATE | S3 |
| s5 | 0.15 | 0.25 | 0.36 | PROXY | S5 |
| q | 0.42 | 0.6 | 0.75 | ESTIMATE | S3, S6 |
| d5 | 0.84 | 0.98 | 1.1 | PROXY | S3, S7, S8 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.84 | 1.72 | PROXY |
| F | 6.87 | 8.01 | 8.78 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.56 | 9.41 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS table is for NAICS 327000 rather than 327320.
- a: Occupation shares do not directly measure task exposure or realizable labor-cost reduction.
- a: Driver headcount is an industry association estimate and may not align exactly with BLS employment scope.
- rho: Anthropic usage reflects users of its products and is not representative of ready-mix firms.
- rho: Automation-pattern classification does not establish realized savings.
- rho: Operational and safety-critical decisions may retain human review even when software is capable.
- e: Plant counts are not firm counts.
- e: The estimate concerns eligibility and operating reality, not willingness to sell.
- e: Vertically integrated firms can contain viable businesses but may not be separable.
- s5: The Census source covers responding employer-business owners across industries and uses 2018 data.
- s5: Owner age is not a direct measure of sale probability.
- s5: Internal succession and strategic consolidation are not separately observed.
- q: Industry profit per yard combines many non-AI factors and is not evidence of savings retention by itself.
- q: The producer-price index measures output prices, not bargaining power or pass-through mechanics.
- q: Local competitive intensity and customer mix vary substantially.
- d5: Construction cycles can dominate a five-year window.
- d5: Cement consumption is an upstream proxy and includes uses outside ready-mix.
- d5: National data mask substantial regional divergence.
- d5: The forecast is inherently uncertain and may be revised.
- o: The estimate is based on operating characteristics rather than a direct substitution study.
- o: Substitution exposure varies by end market and project type.
- o: AI-enabled entrants could alter competition without replacing the physical product.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 327000](https://www.bls.gov/oes/2023/may/naics3_327000.htm) (accessed 2026-07-23): Broader nonmetallic mineral product manufacturing employment and wage mix, including production, transportation, management, office, business, and dispatcher shares used to bridge AI task exposure.
- **S2** — [2022 Mixer Driver Recruitment and Retention Survey Executive Summary](https://www.nrmca.org/wp-content/uploads/2022/08/2022ExSummaryMixerDriverSurvey.pdf) (accessed 2026-07-23): Approximately 75,000 mixer drivers, persistent driver shortages, vacancy and turnover evidence, and the importance of the physical delivery workforce.
- **S3** — [Performance Benchmarking Survey and State of the Industry](https://www.nrmca.org/wp-content/uploads/Performance_Benchmarking_Survey_and_State_of_the_Industry.pdf) (accessed 2026-07-23): Industry scale, plant and truck counts, cubic-yard volumes, selling price, long-cycle demand history, and profit per yard.
- **S4** — [Anthropic Economic Index: September 2025 Report](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) (accessed 2026-07-23): Observed enterprise API-use automation patterns and concentration in coding and office/administrative tasks, used as a cross-industry realization proxy.
- **S5** — [The Ages of Business Owners: Why It Matters](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-23): Census owner-age distribution showing 51% of responding employer-business owners were age 55 or older.
- **S6** — [Producer Price Index by Industry: Ready-Mix Concrete Manufacturing](https://fred.stlouisfed.org/series/PCU327320327320) (accessed 2026-07-23): BLS producer-price series for ready-mix concrete manufacturing, documenting observable industry output-price movement.
- **S7** — [Real Sectoral Output for Manufacturing: Ready-Mix Concrete Manufacturing](https://fred.stlouisfed.org/series/IPUEN327320T010000000) (accessed 2026-07-23): BLS real sectoral output index for NAICS 327320, including 2019 through 2023 observations used for the five-year demand bridge.
- **S8** — [ACA Spring Forecast 2026](https://www.cement.org/2026/04/30/aca-spring-forecast-2026/) (accessed 2026-07-23): Near-term US cement-consumption forecast of a 2.5% decline in 2026 followed by positive growth in 2027.
