# 332322 — Sheet Metal Work Manufacturing

*v5.1 Stage 1 research memo. Run `332322-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.63 · L 2.38 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A very large outsourced job-shop base repeats digital quoting and planning work ahead of every physical fabrication order.
**Weakness:** Competitive sourcing and a substantial physical workforce cap retained AI benefits.

## Business-model lens
- Included: US lower-middle-market sheet-metal job shops and contract manufacturers repeatedly providing outsourced detailing, cutting, punching, bending, forming, welding, assembly, finishing, and delivery for external HVAC, construction, equipment, enclosure, industrial, and OEM customers.
- Excluded: On-site sheet-metal installation contractors, stampers and custom roll formers classified elsewhere, captive OEM departments, commodity distributors, firms outside the EBITDA band, shells, and non-control financing vehicles.
- Customer and revenue model: Job, project, or repeat-production quotes for custom sheet-metal parts and assemblies, often under recurring contractor and OEM accounts with material, engineering support, programming, fabrication, finishing, inspection, and delivery bundled.
- Deviation from default lens: none

## Executive view
Sheet-metal work has a large outsourced job-shop population and high labor share. AI can improve quoting, DFM review, CAD/CAM, nesting, scheduling, maintenance, inspection support, documentation, and service, while material handling, setup, forming, welding, assembly, finishing, and accountability remain physical.

## How AI changes the work
AI can turn drawings and histories into draft quotes, routings, nests, programs, schedules, inspection flags, purchasing actions, and customer updates. Skilled operators still resolve design exceptions, run and maintain equipment, manage bends and welds, assemble products, inspect quality, and release shipments.

## Value capture
Fixed quotes and fast response allow near-term savings retention, especially for complex assemblies and urgent work. Competitive RFQs, OEM cost-downs, resourcing, material escalators, and contractor bidding transmit widely adopted gains, making quality and speed more defensible than labor savings alone.

## Firm availability
The large estimated population should contain many eligible outsourced manufacturers, but transferability depends on customer diversity, management depth, repeat programs, certifications, equipment, systems, working capital, environmental exposure, and institutionalized technical knowledge.

## Demand durability
Demand is diversified across HVAC, construction, equipment, enclosures, electronics, and industrial OEMs. Prefabrication, energy-efficiency upgrades, and reshoring support the base, while construction and OEM cycles, imports, tariffs, and metal costs create a wide range.

## Risks and uncertainty
Key risks are customer concentration, owner dependence, low-bid competition, metal-price volatility, legacy systems, short-run data sparsity, quality escapes, equipment utilization, worker scarcity, capital needs, and overstatement in the margin-bridged firm count.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2864 | — | OBSERVED | — |
| n | — | 1292 | — | ESTIMATE | — |
| a | 0.22 | 0.34 | 0.48 | PROXY | S1, S2, S3 |
| rho | 0.4 | 0.61 | 0.77 | ESTIMATE | S2 |
| e | 0.56 | 0.73 | 0.85 | ESTIMATE | S1, S2 |
| s5 | 0.11 | 0.2 | 0.31 | PROXY | S4 |
| q | 0.34 | 0.52 | 0.68 | ESTIMATE | S2 |
| d5 | 0.88 | 1.02 | 1.17 | PROXY | S2, S5 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.01 | 2.38 | 4.23 | ESTIMATE |
| F | 7.06 | 8.44 | 9.38 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.74 | 9.69 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupation-by-task dataset was located.
- a: High-mix prototype shops, HVAC duct fabricators, enclosures, and repeat OEM production have different task and automation profiles.
- rho: Observed equipment automation does not directly measure AI implementation.
- rho: Small shops may lack standardized routings and clean historical costs needed for reliable models.
- e: Eligibility is not directly observed.
- e: The provided count is margin-bridged and may include micro-shops, captive firms, or cyclically overearning businesses without transferable systems.
- s5: Gallup is not industry- or size-specific and measures plans, not completed transfers.
- s5: Equipment and customer accounts may be purchased without transfer of an operating firm.
- q: No representative contract or pass-through dataset was located.
- q: Retention varies between transactional laser cutting, repeat OEM programs, and complex finished assemblies.
- d5: Occupation and construction measures do not directly measure physical outsourced sheet-metal output.
- d5: Tariffs, metal prices, interest rates, HVAC efficiency policy, OEM cycles, and reshoring can materially shift demand.
- o: Accountable production may consolidate into larger platforms outside the lens.
- o: Routine flat-part cutting is more susceptible to platform self-service than formed, welded, and finished assemblies.

## Sources
- **S1** — [NAICS 332322 Sheet Metal Work Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines the industry as establishments primarily engaged in manufacturing sheet-metal work other than stampings and distinguishes on-site fabrication and adjacent product categories.
- **S2** — [Sheet Metal Workers](https://www.bls.gov/ooh/construction-and-extraction/sheet-metal-workers.htm) (accessed 2026-07-22): Reports 127,000 sheet-metal workers in 2024, 24% employed in manufacturing, 2% projected employment growth through 2034, continuing HVAC demand, and labor effects from prefabricated duct and automated fabrication equipment.
- **S3** — [Fabricated Metal Product Manufacturing: NAICS 332](https://www.bls.gov/iag/tgs/iag332.htm?hmsr=afimetalparts.com) (accessed 2026-07-22): Reports 2025 broader-subsector employment including 125,250 assemblers, 112,520 welders, 101,640 machinists, and 56,060 cutting and press-machine operators.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey found 22% of employer-business owners planned to sell or transfer ownership within five years, while 5% planned closure and 5% had no plan.
- **S5** — [Value of Construction Put in Place, May 2026](https://www.census.gov/construction/c30/pdf/totsa.pdf) (accessed 2026-07-22): Reports May 2026 total construction at a seasonally adjusted $2.210 trillion annual rate, down 1.5% from May 2025, with mixed private and public submarkets.
