# 238130 — Framing Contractors

*v5.1 Stage 1 research memo. Run `238130-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.00 · L 0.41 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can compress scarce estimating, project-control, and back-office work while fixed-price projects preserve some near-term savings.
**Weakness:** Most compensation funds physical onsite craft work, and competitive project rebidding rapidly exposes productivity gains to customers.

## Business-model lens
- Included: Independent lower-middle-market contractors performing structural framing and sheathing, including wood, light-gauge steel, post framing, and onsite truss or wood-frame component work for builders, general contractors, developers, and property owners.
- Excluded: Structural-steel or concrete framing, offsite component manufacturing, captive framing crews, labor-only shells without transferable customer relationships or supervision, and non-control financing vehicles.
- Customer and revenue model: Project-based subcontract revenue, commonly bid as a fixed-price or lump-sum scope and billed by percentage of completion; some work uses time-and-materials or unit-price terms. Repeat business comes from recurring builder and general-contractor relationships rather than subscriptions.
- Deviation from default lens: none

## Executive view
Framing is a physical, project-based trade in which AI can improve the commercial and coordination layer but cannot replace most onsite production. The opportunity is consequently an operational augmentation thesis: better takeoffs, bidding, scheduling, documentation, billing, and crew utilization around a durable need for accountable field execution.

## How AI changes the work
Likely applications include plan and specification extraction, quantity takeoffs, estimate drafting, bid comparison, schedule updates, daily-log summarization, change-order documentation, safety paperwork, invoice matching, and customer communication. Measuring, cutting, lifting, fastening, layout, inspection, and adaptation to imperfect field conditions remain largely outside near-term AI substitution; prefabrication is a separate production shift rather than a pure software gain.

## Value capture
Fixed-price scopes allow a contractor to keep savings on already-awarded projects when labor hours or administrative cost come in below plan. Retention decays as short-cycle bids are renewed, general contractors compare competing quotes, and rivals adopt similar tools. Strong customer relationships, speed, reliability, and disciplined estimating can slow that pass-through but do not eliminate it.

## Firm availability
Most scaled independent framing subcontractors fit the external-customer lens, and broad construction transaction evidence shows that such businesses do trade. Transferability is impaired when the owner personally estimates every job, holds all builder relationships, or is the only licensed or trusted supervisor; labor-only entities and captive crews are not credible control-transfer targets.

## Demand durability
The current service basket should remain necessary over five years because buildings still require structural frames and accountable installation. The central demand case is modest growth, with major uncertainty from housing cycles and financing. Panelization, modular construction, and other prefabricated components can reduce onsite framing hours and shift value to manufacturers, but they still leave layout, assembly, coordination, and warranty accountability.

## Risks and uncertainty
The largest research weakness is that occupation data, adoption surveys, owner-age evidence, and transactions are all broader than NAICS 238130. Commercial risks include builder concentration, bid commoditization, fixed-price estimating errors, change-order disputes, worker shortages, safety liability, cyclicality, and prefab substitution. A framing-specific task census and matched post-adoption project economics could materially lower or raise the opportunity estimate.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2036 | — | ESTIMATE | — |
| n | — | 698 | — | ESTIMATE | — |
| a | 0.06 | 0.11 | 0.18 | PROXY | S2, S3 |
| rho | 0.28 | 0.46 | 0.64 | PROXY | S4 |
| e | 0.64 | 0.79 | 0.9 | ESTIMATE | S1 |
| s5 | 0.08 | 0.15 | 0.25 | PROXY | S5, S6 |
| q | 0.2 | 0.36 | 0.55 | PROXY | S7 |
| d5 | 0.89 | 1.02 | 1.13 | PROXY | S3 |
| o | 0.8 | 0.91 | 0.97 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.14 | 0.41 | 0.94 | ESTIMATE |
| F | 5.80 | 7.12 | 8.14 | ESTIMATE |
| C | 4.00 | 7.20 | 10.00 | PROXY |
| D | 7.12 | 9.28 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS excludes self-employed workers and is reported at the broader NAICS 238100 ancestor.
- a: Occupation shares are employment-weighted, while this primitive is wage- and task-weighted.
- a: The estimate concerns technically exposed current tasks, not realized adoption.
- rho: Survey expectations are not measured implementation outcomes.
- rho: The survey spans construction segments and firm sizes rather than the target lens.
- rho: Robotics and AI are combined in the source, while the primitive concerns the exposed opportunity identified here.
- e: No source directly measures eligibility among firms in the supplied EBITDA band.
- e: Licensing, subcontracting norms, and owner dependence vary substantially by state and end market.
- e: The supplied firm count is an estimate and uses ancestor-level inputs.
- s5: The Census age distribution is for responding owners across employer industries and dates to reference year 2018.
- s5: BizBuySell transactions are voluntarily reported and cover broad building and construction businesses, not framing alone.
- s5: The range excludes closures, deaths without transferable operations, minority investments, and internal reorganizations.
- q: The source is an industry software vendor rather than a representative government survey.
- q: The cited 80% figure covers construction projects across trades and vintages, not framing contractors specifically.
- q: Actual retention depends on local bid density, builder concentration, contract duration, and whether savings are observable.
- d5: Occupational employment is an imperfect demand proxy and includes self-employment and carpentry outside NAICS 238130.
- d5: The BLS projection is ten-year and the conversion to five years assumes a smooth path.
- d5: Construction demand is highly cyclical and geographically uneven.
- o: No source directly measures the future operator-required share for framing contractors.
- o: Offsite prefabrication adoption could move faster in repetitive multifamily and single-family production than in custom or alteration work.
- o: This primitive addresses who must deliver the service, not task automation already reflected in a and rho.

## Sources
- **S1** — [2022 NAICS: 238130 Framing Contractors](https://www.census.gov/naics/?chart=2022&details=23&input=23) (accessed 2026-07-22): Defines framing contractors as establishments primarily engaged in structural framing and sheathing other than structural steel or concrete, including new work, additions, alterations, maintenance, and repairs.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 238100](https://www.bls.gov/oes/2023/may/naics4_238100.htm) (accessed 2026-07-22): Reports 978,830 jobs in the broader industry, including occupation shares of 71.91% construction/extraction, 8.30% office/administrative support, 4.35% business/financial operations, and 5.85% management; also reports cost estimators, project-management specialists, construction managers, supervisors, carpenters, and laborers.
- **S3** — [Occupational Outlook Handbook: Carpenters](https://www.bls.gov/ooh/construction-and-extraction/carpenters.htm) (accessed 2026-07-22): Describes carpenter duties and physical work, reports 959,000 jobs in 2024 and projected 2034 employment of 1,002,100, and says population and factory construction support demand while modular and prefabricated components reduce the need for onsite carpentry.
- **S4** — [2025 Workforce Survey Analysis](https://www.agc.org/sites/default/files/users/user21902/2025%20Workforce%20Survey%20Analysis%20%283%29.pdf) (accessed 2026-07-22): AGC-NCCER construction survey reports 45% expect robotics and AI to automate manual or error-prone tasks over five years, 44% expect safer or more productive jobs, and smaller firms lag some modernization approaches; it also documents widespread craft and salaried hiring difficulty.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding owners of U.S. employer businesses were age 55 or older in the 2019 Annual Business Survey, using 2018 data, with stated population limitations.
- **S6** — [Construction Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/building-construction/) (accessed 2026-07-22): Reports 3,142 sold building-and-construction listings analyzed, annual transaction pricing from 2021 through 2025, and explains that the sample is based on construction businesses sold on and reported to BizBuySell.
- **S7** — [4 Main Types of Construction Contracts and How to Bill for Each](https://www.siteline.com/blog/4-main-types-of-construction-contracts-and-how-to-bill-for-each) (accessed 2026-07-22): Explains fixed-price, time-and-materials, cost-plus, and unit-price subcontract billing; says fixed price is most common between subcontractors and GCs, cites 80% fixed-price usage among 38,000 software-recorded projects, and notes contractors can retain gains from lower labor hours or material cost on fixed-price work.
