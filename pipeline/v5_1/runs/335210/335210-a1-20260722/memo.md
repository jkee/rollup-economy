# 335210 — Small Electrical Appliance Manufacturing

*v5.1 Stage 1 research memo. Run `335210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.28 · L 0.46 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High-volume digital product, sourcing, forecast, test, and service data can support repeatable AI workflows.
**Weakness:** The eligible domestic contract-manufacturer population is likely very small and exposed to global retail price competition.

## Business-model lens
- Included: US lower-middle-market manufacturers of small electric appliances, electric housewares, household fans, vacuums, floor-care machines, air cleaners, portable heaters, food-preparation devices, and similar products that repeatedly supply external private-label, OEM, distributor, and retail customers.
- Excluded: Major appliances, commercial equipment, import-only brand owners without accountable domestic operations, distributors, captive plants, firms outside the EBITDA band, shells, and non-control financing vehicles.
- Customer and revenue model: Predominantly per-unit branded or private-label product sales to retailers, distributors, and OEMs; qualifying outsourced-service revenue is concentrated in recurring contract manufacturing, product configuration, testing, and lifecycle support.
- Deviation from default lens: none

## Executive view
Small-appliance manufacturing offers AI opportunities in design support, sourcing, forecasting, planning, quality, testing analytics, and service, while assembly and safety accountability remain physical. Most firms are product sellers rather than outsourced-service providers, and the estimated LMM population is only 22 before eligibility screening.

## How AI changes the work
AI can assist product and component design, forecast retailer demand, optimize sourcing and schedules, flag defects and abnormal test results, predict maintenance, generate compliance records, and automate customer support. Humans and equipment still assemble, wire, test, package, inspect, and release products.

## Value capture
Global supplier comparisons, retailer concentration, promotions, private-label tenders, and online price transparency transmit common savings rapidly. Brand, intellectual property, reliability, product-launch speed, and fewer returns offer better retention.

## Firm availability
Only recurring domestic private-label or contract manufacturers clearly fit the lens. Every candidate requires confirmation of domestic operations, normalized EBITDA, customer recurrence, certification, recall and warranty exposure, retailer concentration, and transferable management.

## Demand durability
Household appliance output is projected to grow modestly even as employment falls, but small appliances are discretionary, import-exposed, and prone to product fads and channel inventory swings. Replacement and household formation support a roughly stable base.

## Risks and uncertainty
Key risks are service-lens ineligibility, tiny estimated firm count, imports, retailer bargaining, recalls and product liability, component shortages, tariffs, short product cycles, inventory obsolescence, cybersecurity, and margin-bridge error.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.218 | — | OBSERVED | — |
| n | — | 22 | — | ESTIMATE | — |
| a | 0.16 | 0.27 | 0.4 | PROXY | S1, S2 |
| rho | 0.38 | 0.58 | 0.74 | ESTIMATE | S3 |
| e | 0.03 | 0.1 | 0.24 | ESTIMATE | S2 |
| s5 | 0.07 | 0.15 | 0.26 | PROXY | S4 |
| q | 0.15 | 0.3 | 0.49 | ESTIMATE | S3 |
| d5 | 0.86 | 0.99 | 1.12 | PROXY | S5 |
| o | 0.86 | 0.94 | 0.98 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.53 | 1.37 | 2.58 | ESTIMATE |
| F | 0.07 | 0.46 | 1.39 | ESTIMATE |
| C | 3.00 | 6.00 | 9.80 | ESTIMATE |
| D | 7.40 | 9.31 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupation-by-task dataset was located.
- a: Vacuums, cooking appliances, fans, floor care, and air cleaners have different electronics, motor, and assembly mixes.
- rho: Recall evidence illustrates consequences of quality failures, not an implementation rate.
- rho: Import-heavy brands may have data but little domestic labor to automate.
- e: Eligibility depends on whether repeat private-label manufacturing is treated as outsourced service.
- e: The provided n is an ESTIMATE and may include import-led product businesses or firms outside the true band.
- s5: Gallup is not industry- or size-specific and measures plans, not completed transfers.
- s5: With few eligible firms, one transaction changes the realized rate sharply.
- q: No representative contract or pass-through dataset was located.
- q: A differentiated premium brand can retain much more than a private-label contract assembler.
- d5: BLS output is an aggregate index for small and major appliances and does not isolate eligible operators.
- d5: Domestic manufacturing demand can fall even if US consumer unit demand rises through imports.
- o: The accountable operator may be an overseas contract manufacturer outside the lens.
- o: Connected features can shift value toward software without eliminating physical appliance demand.

## Sources
- **S1** — [Electrical Equipment, Appliance, and Component Manufacturing: NAICS 335](https://www.bls.gov/iag/tgs/iag335.htm) (accessed 2026-07-22): Reports 2025 broader-subsector employment including 65,350 electrical and electronic assemblers, 57,660 team assemblers, and 14,050 inspectors.
- **S2** — [NAICS 33521 Small Electrical Appliance Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines the industry as small electric appliances and housewares, household fans, vacuum cleaners, and floor-care machines and distinguishes adjacent major and commercial appliances.
- **S3** — [Sensio Recalls Steam Espresso Machines Due to Burn and Laceration Hazards](https://www.cpsc.gov/Recalls/2025/Sensio-Recalls-Steam-Espresso-Machines-Due-to-Burn-and-Laceration-Hazards) (accessed 2026-07-22): Documents a 12,300-unit small-appliance recall after 18 handle-ejection reports and eight reported injuries, illustrating safety, quality, and product-liability constraints.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey found 22% of employer-business owners planned to sell or transfer ownership within five years, while 5% planned closure and 5% had no plan.
- **S5** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects household-appliance manufacturing employment from 60,100 in 2024 to 55,600 in 2034, down 7.5%, while its real-output index rises from 21.9 to 24.1.
