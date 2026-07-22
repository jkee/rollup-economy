# 332313 — Plate Work Manufacturing

*v5.1 Stage 1 research memo. Run `332313-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.21 · L 2.28 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large outsourced job-shop base repeats information-heavy quoting and planning work before every physical fabrication job.
**Weakness:** Heavy, variable physical work and customer rebidding constrain both substitution and durable retention.

## Business-model lens
- Included: US lower-middle-market plate-work job shops and contract manufacturers repeatedly cutting, punching, bending, rolling, shaping, welding, machining, finishing, inspecting, and assembling purchased metal plate for external industrial, equipment, energy, mining, and construction customers.
- Excluded: Steel mills and commodity service centers, captive OEM departments, structural erection contractors, manufacturers outside the EBITDA band, shells, and non-control financing vehicles.
- Customer and revenue model: Job, project, or production-run quotes for custom plate components and weldments, commonly under repeat OEM and industrial-customer relationships with material, programming, fabrication, inspection, and delivery bundled.
- Deviation from default lens: none

## Executive view
Plate work is a high-labor outsourced manufacturing activity with strong service-like customer relationships. AI can improve quoting, drawing review, nesting, programming, scheduling, maintenance, inspection support, and documentation, while heavy material handling, forming, welding, finishing, and accountability keep most physical work operator-led.

## How AI changes the work
AI can convert drawings and histories into draft quotes and routings, optimize plate nesting and schedules, flag specification changes, prioritize maintenance, interpret inspection data, and automate customer updates. Skilled staff still handle setup, forming, rolling, welding, grinding, inspection, and release.

## Value capture
Fixed quotes, scarce capabilities, certification, complexity, and turnaround allow initial savings retention. OEM negotiations, open-book costing, resourcing, and competitive bids pass through common gains, so operational quality and speed are more defensible than labor reduction alone.

## Firm availability
The large estimated population contains many genuine outsourced job shops, but transferability depends on customer diversity, management depth, certifications, equipment, working capital, environmental exposure, and whether technical knowledge and relationships are institutionalized.

## Demand durability
End-market diversity supports resilience but not immunity from capital cycles. Industrial, equipment, energy, mining, defense, and infrastructure programs can offset one another, while steel prices, tariffs, interest rates, and megaproject timing create a wide five-year range.

## Risks and uncertainty
Key risks are customer concentration, owner dependence, volatile steel and energy markets, cyclicality, large-job execution, weld and dimensional claims, worker scarcity, legacy machinery, integration cost, low data quality, and possible overstatement in the margin-bridged firm count.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3182 | — | OBSERVED | — |
| n | — | 575 | — | ESTIMATE | — |
| a | 0.2 | 0.32 | 0.45 | PROXY | S1, S2, S3 |
| rho | 0.36 | 0.56 | 0.72 | ESTIMATE | S3 |
| e | 0.55 | 0.72 | 0.84 | ESTIMATE | S1, S3 |
| s5 | 0.11 | 0.19 | 0.3 | PROXY | S4 |
| q | 0.36 | 0.53 | 0.69 | ESTIMATE | S3 |
| d5 | 0.84 | 0.99 | 1.15 | PROXY | S5 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.92 | 2.28 | 4.12 | ESTIMATE |
| F | 5.75 | 7.04 | 8.02 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 7.56 | 9.50 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupation-by-task dataset was located.
- a: High-mix one-off weldments and repeat production plate parts differ materially in automatable share.
- rho: Computerized cutting demonstrates workflow feasibility, not achieved AI substitution.
- rho: Small shops may lack sufficient clean historical job data for reliable models.
- e: Eligibility is not directly observed.
- e: The provided count is margin-bridged and may include low-quality, captive, or cyclically overearning operations.
- s5: Gallup is not industry- or size-specific and measures intentions, not completions.
- s5: Equipment and customer lists may sell without a transferable operating firm.
- q: No representative contract or pass-through dataset was located.
- q: Retention differs sharply between repeat OEM production and unique engineered weldments.
- d5: Construction is only one portion of plate-work demand and value is not physical tonnage.
- d5: Steel prices, tariffs, interest rates, energy cycles, defense budgets, and large-project timing can shift demand rapidly.
- o: Production may consolidate into larger operators outside the lens.
- o: Automation can reduce labor per job without eliminating accountable operator demand.

## Sources
- **S1** — [North American Industry Classification System: 332313 Plate Work Manufacturing](https://www.census.gov/naics/?details=332&input=332&year=2017) (accessed 2026-07-22): Defines the industry as establishments manufacturing fabricated metal plate work by cutting, punching, bending, shaping, and welding purchased metal plate.
- **S2** — [Fabricated Metal Product Manufacturing: NAICS 332](https://www.bls.gov/iag/tgs/iag332.htm?hmsr=afimetalparts.com) (accessed 2026-07-22): Reports 2025 broader-subsector employment including 125,250 assemblers, 112,520 welders, 101,640 machinists, and 56,060 cutting and press-machine operators.
- **S3** — [CNC Plasma and Oxyfuel Plate Cutting Machines](https://www.alltracorp.com/plate-cutting) (accessed 2026-07-22): Describes computerized automation, software integration, cutting, beveling, and marking in heavy plate processing, including plate up to 12 inches thick.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey found 22% of employer-business owners planned to sell or transfer ownership within five years, while 5% planned closure and 5% had no plan.
- **S5** — [Value of Construction Put in Place, May 2026](https://www.census.gov/construction/c30/pdf/totsa.pdf) (accessed 2026-07-22): Reports total construction at a $2.210 trillion annual rate, down 1.5% from May 2025; private manufacturing construction down 22.0% and public highway and street construction up 2.9%.
