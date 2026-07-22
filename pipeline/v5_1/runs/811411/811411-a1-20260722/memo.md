# 811411 — Home and Garden Equipment Repair and Maintenance

*v5.1 Stage 1 research memo. Run `811411-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.36 · L 0.34 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Physical, repeat repair demand remains operator-required while a limited administrative and diagnostic-support layer is amenable to AI.
**Weakness:** Only four lower-middle-market firms are estimated, and replacement, seasonality, mixed retail models, and owner dependence can sharply narrow the actionable pool.

## Business-model lens
- Included: Independent US firms repairing and maintaining home and garden equipment for external household and commercial customers, including lawnmowers, handheld power tools, edgers, snow and leaf blowers, and trimmers. The screened population is limited to recurring or repeat outsourced-service firms in the lower-middle-market EBITDA band.
- Excluded: Retailers whose principal business is selling new outdoor power equipment, manufacturer- or dealer-captive service units, commercial or industrial machinery repair, internal maintenance departments, shells, and non-control financing vehicles.
- Customer and revenue model: Customers include households, landscapers, property managers, and other equipment users. Revenue comes from diagnostic and service charges, hourly or flat-rate labor, parts markups, seasonal tune-ups and maintenance, and sometimes pickup or delivery fees.
- Deviation from default lens: none

## Executive view
This is a physical repair business with a bounded AI opportunity in intake, estimating, scheduling, records, parts research, and customer communication. The underlying outsourced service remains operator-required, but the dataset indicates only a few lower-middle-market firms and demand is exposed to equipment replacement, seasonality, and product-technology shifts.

## How AI changes the work
AI can turn customer descriptions, work orders, manuals, parts histories, and technician notes into triage suggestions, draft estimates, parts recommendations, scheduling actions, and completed records. It is unlikely to replace the inspection, disassembly, adjustment, parts replacement, testing, and handling that dominate mechanic work.

## Value capture
Flat diagnostic fees, flat-rate labor, parts margins, and faster turnaround can preserve savings. Hourly billing, warranty reimbursement, and local price competition can instead return part of the benefit to customers.

## Firm availability
The frozen dataset count is four estimated lower-middle-market firms. Eligibility is likely meaningful but not universal because mixed retail economics, captive arrangements, seasonal concentration, and owner dependence can make some nominally classified firms unsuitable.

## Demand durability
BLS projects modest growth for small-engine mechanics, used here only as a demand proxy. The installed equipment base and recurring maintenance support durability, while cheaper replacement, electrification, and more disposable products could reduce repair demand.

## Risks and uncertainty
The principal evidence gaps are a true wage-weighted task mix for 811411, workflow-level AI adoption, firm-level eligibility within the tiny dataset pool, closed transaction data, and constant-price repair volumes. Results are particularly sensitive to whether mixed dealer-retail businesses are classified consistently and whether equipment remains economical to repair.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3399 | — | OBSERVED | — |
| n | — | 4 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S2, S3 |
| rho | 0.3 | 0.5 | 0.68 | PROXY | S4 |
| e | 0.45 | 0.65 | 0.8 | ESTIMATE | S1 |
| s5 | 0.03 | 0.09 | 0.17 | PROXY | S5 |
| q | 0.35 | 0.58 | 0.75 | ESTIMATE | — |
| d5 | 0.83 | 1.02 | 1.18 | PROXY | S6 |
| o | 0.88 | 0.97 | 1 | PROXY | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.41 | 1.22 | 2.59 | PROXY |
| F | 0.08 | 0.34 | 0.70 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.30 | 9.89 | 10.00 | PROXY |

## Caveats
- a: O*NET is occupation-level rather than NAICS-specific and does not provide wage-weighted task shares.
- a: The BLS occupation chart covers the broader Personal and Household Goods Repair and Maintenance industry rather than NAICS 811411 alone.
- rho: Census BTOS spans all industries and firm sizes and measures AI use in any business function, not durable labor substitution.
- rho: Implementation depends on service-management software, parts catalogs, and usable historical repair data.
- e: The injected firm count is only four and is an estimate derived through a size-distribution and margin bridge.
- e: The NAICS definition excludes new-equipment retailers, but real-world company classification and mixed revenue models may not follow that boundary cleanly.
- s5: Gallup covers employer businesses across industries and measures intentions rather than completed transactions.
- s5: No industry-specific deal-flow or owner-age series was found.
- q: No industry-specific evidence directly measures how AI-enabled cost savings flow into price or margin.
- q: Revenue mix between flat-rate, hourly, warranty, and parts-driven work may vary materially by operator.
- d5: The BLS series covers small-engine mechanics across industries, not NAICS 811411 service demand.
- d5: The projection is employment rather than constant-quality service quantity.
- o: The estimate applies to the current service basket and does not assume all future equipment preserves today's repairability.
- o: O*NET describes worker tasks, not the fraction of customer demand that can migrate to self-service.

## Sources
- **S1** — [North American Industry Classification System: Sector 81 Definitions](https://www.census.gov/naics/resources/archives/sect81.html) (accessed 2026-07-22): Defines 811411 as repair and servicing of home and garden equipment without retailing new equipment and identifies the retail cross-reference.
- **S2** — [O*NET OnLine: Outdoor Power Equipment and Other Small Engine Mechanics](https://www.onetonline.org/link/summary/49-3053.00) (accessed 2026-07-22): Describes mechanic tasks including records, diagnosis, physical repair, maintenance, customer intake, estimates, and equipment handling.
- **S3** — [BLS OEWS Industry Charts: Personal and Household Goods Repair and Maintenance](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports May 2024 occupation counts in the broader repair industry, including mechanics, managers, office clerks, and upholsterers.
- **S4** — [US Census Bureau: Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports overall US business AI usage and expected near-term usage from December 2025 to May 2026 BTOS data.
- **S5** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of employer-business owners planned to sell or transfer ownership within five years.
- **S6** — [BLS Occupational Outlook Handbook: Small Engine Mechanics](https://www.bls.gov/ooh/installation-maintenance-and-repair/small-engine-mechanics.htm) (accessed 2026-07-22): Projects overall small-engine-mechanic employment growth from 2024 to 2034 and describes the occupation outlook.
