# 325315 — Compost Manufacturing

*v5.1 Stage 1 research memo. Run `325315-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Policy-backed diversion of organics into a locally constrained, operator-required physical process.
**Weakness:** No defensible eligible-firm denominator or compost-specific control-transfer history, compounded by limited direct task data.

## Business-model lens
- Included: Independent lower-middle-market compost producers that repeatedly accept organic feedstock from external customers and sell finished compost or soil amendments.
- Excluded: Municipal or captive on-site composting, hobby operations, pure hauling, anaerobic digestion without compost production, and producers without recurring external customers.
- Customer and revenue model: Recurring tipping or processing fees from waste generators and haulers, supplemented by sales of compost to agriculture, landscaping, construction, and soil-restoration customers.
- Deviation from default lens: none

## Executive view
Compost manufacturing combines a physically durable local service with modest administrative AI opportunity. The strongest support comes from organics-diversion and landfill-methane pressure; the main unknown is how many independent LMM firms are actually transferable.

## How AI changes the work
AI is most useful around dispatch, scale-house workflows, customer communications, reporting, quality records, sales support, and compliance preparation. It is far less useful for the core embodied work of receiving, turning, screening, loading, maintenance, sampling, and site control.

## Value capture
Local permitting and capacity constraints can protect some benefit, especially during contract terms, but hauler concentration, municipal rebids, indexation, and commodity-like compost markets will return a meaningful share to customers.

## Firm availability
Commercial independents with recurring tipping relationships are eligible and their permits and sites can be valuable, yet the universe also includes municipal, captive, community, farm, and integrated waste operations. Compost-specific succession and transaction denominators are absent.

## Demand durability
A large organics stream remains landfilled, and methane and diversion policies favor more recovery capacity. Prevention and competing pathways limit growth, but material that reaches a commercial facility still requires accountable physical operation.

## Risks and uncertainty
Contamination, odors, PFAS and other persistent chemicals, permitting, neighbor opposition, feedstock loss, end-market weakness, and alternative technologies can impair facilities. The occupation bridge, contract economics, eligible-firm share, and transfer probability all require primary diligence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0994 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.12 | 0.2 | 0.3 | PROXY | S1, S2 |
| rho | 0.35 | 0.5 | 0.65 | ESTIMATE | S2, S3 |
| e | 0.35 | 0.55 | 0.7 | ESTIMATE | S3, S4 |
| s5 | 0.1 | 0.2 | 0.32 | ESTIMATE | — |
| q | 0.45 | 0.62 | 0.78 | ESTIMATE | S4 |
| d5 | 1 | 1.15 | 1.35 | PROXY | S3, S5, S6 |
| o | 0.8 | 0.9 | 0.97 | ESTIMATE | S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.40 | 0.78 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.00 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupation-by-task dataset was found for compost manufacturing.
- a: The frozen compensation ratio is for ancestor NAICS 3253 and may not resemble labor intensity at compost sites.
- rho: Implementation evidence specific to independent LMM compost producers was not available.
- rho: Facility permitting and local nuisance constraints vary widely.
- e: The assigned firm-count input is missing and must not be inferred.
- e: Facility counts and firm counts differ because operators may own multiple sites.
- s5: No observed denominator of eligible LMM compost firms or qualifying control transfers was found.
- s5: Asset purchases or permit transfers may not represent control transfers of going concerns.
- q: No representative contract dataset was available.
- q: Revenue mix between tipping fees and compost sales differs materially by facility.
- d5: EPA national waste data are not a forecast for NAICS 325315.
- d5: Constant-quality service demand is difficult to separate from changes in feedstock mix and contamination standards.
- o: The estimate is for the screened external-service basket, not all composting.
- o: Distributed and on-site technologies could reduce outsourced volumes faster than expected.

## Sources
- **S1** — [Data tables for the overview of May 2024 occupational employment and wages](https://www.bls.gov/oes/2024/may/featured_data.htm) (accessed 2026-07-22): BLS reports an annual mean wage of $65,120 for production occupations in covered chemical manufacturing and provides occupational context for the ancestor industry used as a task-mix proxy.
- **S2** — [O*NET: Industrial Production Managers](https://www.onetonline.org/link/summary/11-3051.00) (accessed 2026-07-22): Lists production-manager duties including schedules, production reports, personnel records, quality-control systems, inventory and cost control, audits, and compliance records, alongside accountable operational duties.
- **S3** — [EPA Wasted Food Scale](https://www.epa.gov/sustainable-management-food/wasted-food-scale) (accessed 2026-07-22): Defines composting as managed aerobic biological decomposition and reports that food is 24% of material in municipal solid-waste landfills and causes 58% of landfill methane emissions to the atmosphere.
- **S4** — [US Composting Council Throughput and Environmental Impact Survey](https://www.compostingcouncil.org/page/waste-360-uscc-survey) (accessed 2026-07-22): Describes an industry-wide survey of member compost producers and its focus on compost production and throughput, supporting the existence of commercial producer operations but not a complete firm census.
- **S5** — [United States 2030 Food Loss and Waste Reduction Goal](https://www.epa.gov/sustainable-management-food/united-states-2030-food-loss-and-waste-reduction-goal) (accessed 2026-07-22): EPA reports 349 pounds of food waste per person left the food supply chain in 2019 versus a 2016 baseline of 328 pounds, and a national goal to halve the baseline by 2030.
- **S6** — [California SB 1383 bill text](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201520160SB1383) (accessed 2026-07-22): Sets a target for a 75% reduction in statewide organic-waste disposal from the 2014 level by 2025, illustrating state-level policy pressure for diversion capacity.
