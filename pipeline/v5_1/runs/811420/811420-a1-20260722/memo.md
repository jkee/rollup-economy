# 811420 — Reupholstery and Furniture Repair

*v5.1 Stage 1 research memo. Run `811420-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.09 · L 0.00 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Nearly all of the current service quantity still requires skilled physical craft and an accountable operator.
**Weakness:** The frozen dataset estimates zero lower-middle-market firms, and bespoke owner-dependent craft work can be difficult to scale or transfer.

## Business-model lens
- Included: Independent US firms providing reupholstery, refinishing, repair, and restoration of furniture for external household and commercial customers. The screened population is limited to recurring or repeat outsourced-service firms in the lower-middle-market EBITDA band.
- Excluded: Automotive and trailer upholstery, museum-piece restoration classified as artistic work, furniture manufacturing, internal captive workshops, shells, and non-control financing vehicles.
- Customer and revenue model: Customers include households, interior designers, hospitality and commercial facilities, furniture dealers, and institutional owners. Revenue comes mainly from custom job quotes covering skilled labor, fabric and other materials, refinishing, frame repair, pickup and delivery, and sometimes repeat commercial refurbishment programs.
- Deviation from default lens: none

## Executive view
Reupholstery and furniture repair is an operator-required craft service with a narrow AI layer in quoting, visualization, materials planning, work orders, records, and customer communication. Physical craft limits substitution, while the frozen dataset indicates no estimated lower-middle-market firms, making firm availability the immediate constraint rather than service durability alone.

## How AI changes the work
AI can turn photos and customer descriptions into intake records, draft style concepts and quotes, assist fabric and material calculations, schedule jobs, and prepare communications. It does not replace inspection, stripping, sewing, padding, spring and webbing work, frame repair, refinishing, pickup, delivery, or final quality accountability.

## Value capture
Bespoke quotes, differentiated workmanship, materials margin, and restoration value can preserve benefit. Competitive commercial bids and repricing of repeat jobs may share savings with customers.

## Firm availability
The frozen dataset count is zero estimated lower-middle-market firms. That estimate may miss firms because of size-class or margin assumptions, but it cannot be overridden here. Even if firms are found, owner craft dependence and mixed manufacturing or project work can reduce eligibility and transferability.

## Demand durability
BLS projects a slight decline in upholsterer employment, used only as a proxy. Low-cost replacement and craft scarcity pressure the current basket, while premium furniture, sustainability, sentimental value, and commercial refurbishment support continued demand.

## Risks and uncertainty
The largest uncertainties are whether any firms actually sit in the lower-middle-market EBITDA band, how owner-dependent they are, the repair-specific share of upholsterer employment, constant-price order volume, and whether exposed office and design workflows are standardized enough to implement. The broad occupation and succession proxies do not resolve those issues.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4938 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.23 | PROXY | S2, S3 |
| rho | 0.25 | 0.45 | 0.63 | PROXY | S4 |
| e | 0.35 | 0.58 | 0.75 | ESTIMATE | S1 |
| s5 | 0.02 | 0.07 | 0.14 | PROXY | S5 |
| q | 0.38 | 0.62 | 0.78 | ESTIMATE | — |
| d5 | 0.76 | 0.92 | 1.08 | PROXY | S6 |
| o | 0.93 | 0.99 | 1 | PROXY | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.40 | 1.24 | 2.86 | PROXY |
| F | 0.00 | 0.00 | 0.00 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.07 | 9.11 | 10.00 | PROXY |

## Caveats
- a: O*NET covers the upholsterer occupation, which can include manufacturing and automotive tasks outside the frozen lens.
- a: The BLS occupation chart covers the broader repair industry rather than NAICS 811420 alone.
- rho: Census BTOS spans all industries and firm sizes and measures AI use in any business function.
- rho: No industry-specific AI implementation evidence was found.
- e: The injected lower-middle-market firm count is zero and is a frozen ESTIMATE from a size-distribution and margin bridge, not proof that no such firm exists.
- e: Because the injected count is zero, the eligibility share has no current counted firms to which it can be applied and is especially uncertain.
- s5: Gallup is cross-industry and measures intentions rather than completed deals.
- s5: The frozen dataset count of zero makes realized transfer opportunity absent unless the dataset bridge misses firms.
- q: No direct evidence was found on AI-enabled cost-savings retention in this industry.
- q: Pricing power likely differs sharply between bespoke residential restoration and standardized commercial refurbishment.
- d5: BLS upholsterer employment includes work outside NAICS 811420 and is not a direct demand measure.
- d5: Employment can fall because of labor supply or productivity even when service demand is stable.
- o: O*NET includes some upholsterer work outside the NAICS lens, including manufacturing and automotive tasks.
- o: The estimate applies to the current service basket and does not predict long-run product redesign.

## Sources
- **S1** — [North American Industry Classification System: Sector 81 Definitions](https://www.census.gov/naics/resources/archives/sect81.html) (accessed 2026-07-22): Defines 811420 as furniture reupholstery, refinishing, repair, and restoration and identifies automotive upholstery and museum-piece restoration exclusions.
- **S2** — [O*NET OnLine: Upholsterers](https://www.onetonline.org/link/details/51-6093.00) (accessed 2026-07-22): Describes custom upholstery, work orders, material planning, inspection, sewing, padding, frame repair, refinishing, estimates, records, and customer discussion.
- **S3** — [BLS OEWS Industry Charts: Personal and Household Goods Repair and Maintenance](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports May 2024 occupation counts in the broader repair industry, including upholsterers, managers, and office clerks.
- **S4** — [US Census Bureau: Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports overall US business AI usage and expected near-term usage from December 2025 to May 2026 BTOS data.
- **S5** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of employer-business owners planned to sell or transfer ownership within five years.
- **S6** — [BLS: Occupational Projections and Worker Characteristics](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Reports 2024 and projected 2034 upholsterer employment, decline, self-employment share, openings, and other characteristics.
