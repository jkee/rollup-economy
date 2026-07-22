# 484210 — Used Household and Office Goods Moving

*v5.1 Stage 1 research memo. Run `484210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.34 · L 1.04 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-addressable quoting, scheduling, dispatch, customer-service, and documentation work sits alongside a service whose physical execution cannot be digitized away.
**Weakness:** The wage base is dominated by physical crews and drivers, while transfer rates and paid-move demand lack direct industry-specific longitudinal evidence.

## Business-model lens
- Included: Independent operating companies that use their own crews and vehicles to provide local or long-distance household, institutional, and office moves, including packing, loading, transport, unloading, and directly related storage or accessorial services.
- Excluded: Pure brokers and lead generators that do not transport goods, captive corporate fleets, self-storage-only businesses, freight forwarders, and financing or shell entities.
- Customer and revenue model: Consumers, employers, institutions, and offices buy project-based moves under written binding or non-binding estimates, with revenue from transportation, labor, packing, storage, and accessorial services; repeat demand is episodic rather than subscription-based.
- Deviation from default lens: none

## Executive view
Moving is a physically anchored, locally executed service with a modest but practical digital-work opportunity. The most credible gains are in estimating, lead handling, scheduling, dispatch, documentation, and claims support; the core crew work remains human and asset intensive.

## How AI changes the work
AI can turn photos or video surveys into inventory drafts, prepare estimates and customer messages, optimize schedules, summarize calls, check documents, and triage claims. Human approval remains important because access conditions, inventory errors, regulations, damage, and day-of-move exceptions can change cost and liability.

## Value capture
Project pricing creates some initial retention because a binding quote does not automatically fall when back-office effort falls. Competitive quote shopping, commercial rebids, and simple switching will transfer part of the benefit to customers over five years.

## Firm availability
The industry definition largely matches outsourced operating firms, but the frozen LMM count still needs roster-level verification. Pure brokers, local shells, owner-dependent operators, and firms centered on adjacent storage activity reduce the transferable pool; aging owners suggest succession opportunities without proving transactions.

## Demand durability
Households and organizations will continue to relocate physical goods, and most professionally served volume still needs accountable crews and carriers. Demand is cyclical and sensitive to housing turnover, migration, office footprints, and DIY alternatives, so near-flat real service quantity is more defensible than structural growth.

## Risks and uncertainty
The weakest evidence is industry-specific staffing, AI implementation, private control transfers, and job-level pass-through. Worker classification, safety, cargo claims, insurance, seasonal capacity, broker fraud, and interstate or state compliance can consume gains. A prolonged housing slowdown or a shift toward remote work and smaller offices would weaken volume.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2622 | — | OBSERVED | — |
| n | — | 127 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S1, S2, S3, S4 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S2, S4, S5 |
| e | 0.7 | 0.84 | 0.93 | ESTIMATE | S1, S6, S7 |
| s5 | 0.12 | 0.19 | 0.28 | PROXY | S8 |
| q | 0.45 | 0.62 | 0.78 | ESTIMATE | S2, S9 |
| d5 | 0.92 | 0.99 | 1.08 | PROXY | S10 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.37 | 1.04 | 2.11 | ESTIMATE |
| F | 3.95 | 4.92 | 5.68 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.10 | 9.40 | 10.00 | ESTIMATE |

## Caveats
- a: The available occupation page is for broader NAICS 484200 and is older than the run date.
- a: GenAI exposure evidence is occupational and global, not a direct wage-weighted measurement of US moving firms.
- a: Owner-managers in small firms often combine physical, sales, and administrative duties, making occupational titles an imperfect task map.
- rho: No source measures five-year AI implementation in NAICS 484210.
- rho: Interstate documentation and estimate requirements are not identical to intrastate rules.
- rho: Implementation may improve throughput rather than reduce headcount during peak season.
- e: The frozen firm count is a margin-bridged estimate, not a verified roster.
- e: FMCSA registration covers interstate activity and will miss local-only movers regulated by states.
- e: Eligibility depends on firm-level customer concentration and owner dependence not visible in industry data.
- s5: The Census statistic covers responding employer-business owners across industries and reference year 2018.
- s5: Owner age, firm age, and transferability are distinct.
- s5: Small private transactions and family transfers are poorly observed.
- q: Federal estimate rules apply to interstate household moves and are only a proxy for office and local-move contracting.
- q: Repeat customers may be infrequent, so competitive repricing can occur through new-customer quotes rather than renewals.
- q: The estimate excludes volume effects and implementation cost.
- d5: One-year ACS movement is not expenditure on professional movers.
- d5: The 2023-to-2024 change is too short a history for a structural forecast.
- d5: Office moves and storage-linked moves are not directly measured.
- o: The estimate concerns quantity requiring an accountable operator, not employment within the operator.
- o: Commercial office moves may require more accountable coordination than residential moves.
- o: Robotics adoption inside residences and offices is not directly evidenced.

## Sources
- **S1** — [North American Industry Classification System: 484210 Used Household and Office Goods Moving](https://www.census.gov/naics/?details=48421&input=48421&year=2017) (accessed 2026-07-22): Defines the industry as local or long-distance trucking of used household, institutional, or commercial furniture and equipment.
- **S2** — [Estimating Charges (Subpart D)](https://www.fmcsa.dot.gov/protect-your-move/how-to/subpartD) (accessed 2026-07-22): Documents required written estimates, binding and non-binding pricing, physical or waived surveys, tariffs, additional services, and payment constraints for interstate household moves.
- **S3** — [May 2016 National Industry-Specific Occupational Employment and Wage Estimates: Specialized Freight Trucking](https://www.bls.gov/oes/2016/may/naics4_484200.htm) (accessed 2026-07-22): Provides employer-survey occupational employment and wage estimates for the broader NAICS 484200 industry, used only as an occupation-mix proxy.
- **S4** — [Generative AI and Jobs: A Refined Global Index of Occupational Exposure](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) (accessed 2026-07-22): Reports task-level GenAI exposure methodology, highest exposure in clerical occupations, and that job transformation is more likely than full replacement.
- **S5** — [Anthropic Economic Index report: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report) (accessed 2026-07-22): Reports that transportation and material-moving occupations are underrepresented in Claude usage and survey evidence, supporting caution about implementation in physical work.
- **S6** — [What is the difference between a household goods mover and a household goods broker?](https://www.fmcsa.dot.gov/consumer-protection/what-difference-between-household-goods-hhg-mover-and-hhg-broker) (accessed 2026-07-22): Distinguishes operating movers with trucks and crews from brokers that arrange service but do not transport or assume responsibility for goods.
- **S7** — [Motor Carrier Analysis and Information Resources Online: Custom Reports](https://ai.fmcsa.dot.gov/registrationstatistics/customreports.aspx) (accessed 2026-07-22): Provides current registration and operating-authority reporting tools for household-goods carriers, relevant to a future firm-level eligibility audit.
- **S8** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older, based on the 2019 Annual Business Survey for data year 2018.
- **S9** — [What is a binding move estimate?](https://www.fmcsa.dot.gov/consumer-protection/protect-your-move/what-binding-move-estimate) (accessed 2026-07-22): Explains that binding estimates guarantee the stated amount for described services and non-binding estimates depend on actual weight, services, and tariff.
- **S10** — [United States Migration/Geographic Mobility At A Glance: ACS 1-Year Estimates](https://www.census.gov/topics/population/migration/guidance/acs-1yr.html) (accessed 2026-07-22): Reports that 11.8% of the population moved to a different residence in 2024, down from 12.1% in 2023.
