# 623311 — Continuing Care Retirement Communities

*v5.1 Stage 1 research memo. Run `623311-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.05 · L 1.87 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A growing older population and high occupancy support a recurring service bundle in which administrative automation can complement an operator that remains essential for care and physical delivery.
**Weakness:** Most wages are tied to in-person care and hospitality, while nonprofit ownership and complex control pathways sharply limit ordinary acquisition availability.

## Business-model lens
- Included: Operators of continuing care retirement communities and assisted-living settings with on-site nursing facilities that provide recurring residential, personal-care, dining, housekeeping, social, and nursing services to residents.
- Excluded: Independent housing without on-site nursing, assisted-living facilities without nursing facilities, standalone skilled-nursing facilities, captive employee or religious housing, passive real-estate vehicles without operations, and non-control financing interests.
- Customer and revenue model: Residents purchase a bundled continuum of housing, hospitality, personal care, and access to nursing through entrance-fee and monthly-fee contracts or rental and service-fee arrangements. Skilled-care components can also generate third-party reimbursement, while the core residential relationship is recurring and long-duration.
- Deviation from default lens: none

## Executive view
Continuing care communities sell a durable, recurring bundle of housing, hospitality, personal care, and on-site nursing into an aging population. AI can improve the administrative layer, but direct care and physical operations dominate labor. The harder issue is firm transferability: the sector is heavily nonprofit, capital intensive, frequently affiliated with multisite systems, and subject to resident, creditor, and regulatory constraints.

## How AI changes the work
The practical use cases are admissions and move-in workflow, billing, payroll, scheduling, procurement, documentation assistance, marketing, resident communication, and exception detection. Direct assistance, nursing judgment, meals, housekeeping, maintenance, transport, and human interaction remain labor intensive, while clinical uses require stronger governance and review.

## Value capture
Bundled monthly fees and long resident tenure allow an operator to keep some administrative productivity before the next fee decision. Retention is moderated by nonprofit governance, quality expectations, staffing rules, reimbursement limits, resident scrutiny, and the likelihood that part of the benefit is reinvested in service rather than removed as labor.

## Firm availability
Most operator firms perform the recurring service in the default lens, but many communities are nonprofit or already part of a multisite sponsor. Public transaction evidence confirms that assets and control can move, including through membership substitutions, yet the observed rate is low and transaction structures are more complex than ordinary owner succession.

## Demand durability
High and improving occupancy plus population aging support modest real demand growth. The bundle is operator dependent because it integrates real estate, hospitality, personal assistance, and nursing. Affordability, preference for aging at home, limited new supply, and local housing-market conditions prevent demographics from translating mechanically into volume.

## Risks and uncertainty
The firm denominator is uncertain because a facility-margin bridge may not fit entrance-fee and nonprofit economics. Other material risks are state-by-state regulation, debt and charitable-asset restrictions, clinical liability, persistent staffing shortages, weak enterprise AI capability, aging physical plants, affordability, and confusing campuses with independent transferable firms.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5322 | — | OBSERVED | — |
| n | — | 1184 | — | ESTIMATE | — |
| a | 0.15 | 0.22 | 0.3 | PROXY | S2 |
| rho | 0.26 | 0.4 | 0.58 | PROXY | S4 |
| e | 0.5 | 0.7 | 0.86 | ESTIMATE | S1, S3, S6 |
| s5 | 0.03 | 0.06 | 0.11 | PROXY | S3, S6 |
| q | 0.45 | 0.62 | 0.78 | PROXY | S3, S5 |
| d5 | 0.98 | 1.08 | 1.18 | PROXY | S5, S7 |
| o | 0.92 | 0.97 | 0.995 | ESTIMATE | S1 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.83 | 1.87 | 3.70 | PROXY |
| F | 4.72 | 6.32 | 7.60 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | PROXY |
| D | 9.02 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation table combines 623311 with 623312 and covers employers of all sizes.
- a: Task exposure is inferred within occupations and is not directly observed.
- a: Clinical documentation assistance may save time without reducing required staffing.
- rho: The survey is not-for-profit senior living and care, not a representative 623311 sample.
- rho: Automation results include conventional software rather than AI alone.
- rho: Planned deployment may not produce stable labor savings.
- e: The injected firm count uses a public healthcare-facilities margin bridge and may misclassify capital-intensive CCRC operators into the LMM band.
- e: The sector snapshot counts communities rather than firms and is from 2019.
- e: Control eligibility for nonprofit entities varies by charter, transaction form, and state law.
- s5: The transaction study is broader senior living and emphasizes not-for-profit activity.
- s5: The sector denominator and transaction numerator have different vintages.
- s5: Announced deals may not close, and a transaction can contain multiple facilities.
- q: No source directly measures commercial retention of AI benefits.
- q: Entrance-fee, rental, nonprofit, and for-profit models may retain savings differently.
- q: Payer reimbursement rules affect skilled-care revenue differently from private residential fees.
- d5: NIC's sample covers primary and secondary markets rather than every U.S. community.
- d5: Occupancy recovery after the pandemic may not repeat.
- d5: Population aging is not a direct measure of ability or willingness to enter a CCRC.
- o: No source directly measures operator displacement for the year-five CCRC service basket.
- o: Home-based care and remote monitoring can prevent some CCRC entry, but that quantity loss is conceptually separate from software replacing the operator for residents who still choose a community.
- o: The estimate assumes on-site nursing remains part of the regulated industry definition.

## Sources
- **S1** — [2022 NAICS Definition — 623311 Continuing Care Retirement Communities](https://www.census.gov/naics/?details=62&input=62&year=2022) (accessed 2026-07-22): Defines the industry as residential and personal care with on-site nursing, meals, housekeeping, social, leisure, and daily-living services, and distinguishes adjacent industries.
- **S2** — [May 2023 OEWS — Continuing Care Retirement Communities and Assisted Living Facilities for the Elderly](https://www.bls.gov/oes/2023/may/naics4_623300.htm) (accessed 2026-07-22): Provides employment shares and wages by occupation for combined NAICS 623300, including healthcare support, food service, facilities, clinical, management, sales, and office work.
- **S3** — [LeadingAge Life Plan Community Market Snapshot Report 2019](https://leadingage.org/wp-content/uploads/2022/09/LALS20-0031_eBook_MarketSnapshot_LifePlan_Community_p3b.pdf) (accessed 2026-07-22): Reports 1,954 communities, nonprofit and for-profit composition, entrance and monthly fee models, average budget, multisite affiliation, services, and historical unit growth.
- **S4** — [2025 Ziegler Link-age Funds and LeadingAge CAST CTO Hotline](https://leadingage.org/wp-content/uploads/2025/09/Ziegler-Linkage-LeadingAge-CAST-CTO-Hotline_FINAL.pdf) (accessed 2026-07-22): Measures AI competency and deployment confidence, data-governance maturity, automation plans by workflow, and implementation barriers among not-for-profit senior-living and care organizations.
- **S5** — [NIC CCRC Performance — Fourth Quarter 2025](https://www.nic.org/blog/ccrc-performance-4q-2025/) (accessed 2026-07-22): Reports occupancy, asking-rent growth, inventory changes, and multi-year occupancy gains for entrance-fee and rental CCRCs across 1,043 communities.
- **S6** — [Not-For-Profit Senior Living M&A in Review: Trends Emerge as Consolidation Continues in 2024](https://www.vizient.com/insights/articles/notforprofit-senior-living-ma-in-review-trends-emerge-as-consolidation-continues-in-2024) (accessed 2026-07-22): Counts 2024 announced senior-living transactions, identifies life-plan-community targets, distinguishes cash deals and membership substitutions, and discusses consolidation constraints.
- **S7** — [Demographic Turning Points for the United States: Population Projections for 2020 to 2060](https://www.census.gov/library/publications/2020/demo/p25-1144.html) (accessed 2026-07-22): Documents the projected expansion of the older population as all baby boomers pass age 65 and the United States ages through the screen horizon.
