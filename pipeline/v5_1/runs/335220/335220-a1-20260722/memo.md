# 335220 — Major Household Appliance Manufacturing

*v5.1 Stage 1 research memo. Run `335220-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.02 · L 0.19 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Data-rich engineering, test, warranty, and production workflows can support material AI assistance around large assembly operations.
**Weakness:** The industry is concentrated, capital-intensive product manufacturing with almost no obvious LMM outsourced-service population.

## Business-model lens
- Included: US lower-middle-market manufacturers of household cooking, laundry, refrigeration, dishwashing, water-heating, disposal, and other major appliances that repeatedly supply external private-label, OEM, distributor, builder, and retail customers.
- Excluded: Small appliances, commercial equipment, import-only brands without accountable domestic production, distributors and installers, captive plants, firms outside the EBITDA band, shells, and non-control financing vehicles.
- Customer and revenue model: Predominantly per-unit branded or private-label product sales through retailers, distributors, builders, and OEM programs; qualifying outsourced-service revenue is limited to recurring contract manufacturing, configuration, testing, and lifecycle support.
- Deviation from default lens: none

## Executive view
Major-appliance manufacturing has usable AI opportunities in design, sourcing, planning, quality, testing analytics, predictive maintenance, compliance, and warranty service. But it is scale-intensive product manufacturing, the estimated LMM population is only 17, and very few firms likely provide a recurring outsourced service.

## How AI changes the work
AI can assist product and component engineering, forecast demand, optimize supply and schedules, flag inspection and end-of-line test anomalies, predict plant maintenance, generate regulatory documentation, and triage service. Physical assembly, refrigeration work, testing, packaging, and safety release remain operator-led.

## Value capture
Brand, efficiency, reliability, distribution, and service can defend gains, while retailer and builder power, annual cost-downs, promotions, transparent pricing, and imports transfer common savings quickly. Contract manufacturers face the strongest pass-through.

## Firm availability
Only rare independent private-label or contract manufacturers clearly fit the lens. Firm-level diligence must validate true ownership, domestic production, normalized EBITDA, recurring programs, certifications, warranty and recall history, plant liabilities, and management depth.

## Demand durability
Replacement and household formation support stable demand, while housing cycles, financing costs, repair, longer product lives, imports, and retailer inventory create volatility. Regulatory efficiency changes require redesign and testing but do not eliminate physical demand.

## Risks and uncertainty
Principal risks are lens ineligibility, tiny firm count, global scale competition, retailer power, recalls and product liability, regulatory compliance, capital expenditure, refrigerants, tariffs, working capital, inventory obsolescence, and cybersecurity.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1487 | — | OBSERVED | — |
| n | — | 17 | — | ESTIMATE | — |
| a | 0.14 | 0.24 | 0.36 | PROXY | S1, S2 |
| rho | 0.34 | 0.54 | 0.7 | ESTIMATE | S3, S4 |
| e | 0.01 | 0.06 | 0.17 | ESTIMATE | S2, S3 |
| s5 | 0.05 | 0.12 | 0.22 | PROXY | S5 |
| q | 0.14 | 0.28 | 0.47 | ESTIMATE | S3, S4 |
| d5 | 0.86 | 0.99 | 1.12 | PROXY | S6 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.77 | 1.50 | ESTIMATE |
| F | 0.01 | 0.19 | 0.79 | ESTIMATE |
| C | 2.80 | 5.60 | 9.40 | ESTIMATE |
| D | 7.74 | 9.50 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupation-by-task dataset was located.
- a: Cooking, laundry, refrigeration, water-heating, and disposal products have different processes and labor mixes.
- rho: Regulatory and recall evidence establishes constraints, not an observed AI realization rate.
- rho: The small estimated LMM population may have older plants and less usable data than major brands.
- e: Eligibility depends on rare contract-manufacturing arrangements that are not observed in public data.
- e: Even small manufacturing entities may belong to large global groups and fail the control and size lens.
- s5: Gallup is not industry- or size-specific and measures plans, not completed transfers.
- s5: With very few eligible firms, one event changes the realized rate materially.
- q: No representative contract or pass-through dataset was located.
- q: Premium brands retain more than contract manufacturers, but branded product firms may fail the service lens.
- d5: BLS output combines small and major appliances and does not isolate eligible LMM operators.
- d5: Domestic manufacturer demand can decline despite stable US appliance replacement through imports.
- o: The accountable operator may be a global manufacturer outside the lens.
- o: Connected diagnostics can reduce service labor without eliminating physical manufacturing.

## Sources
- **S1** — [Electrical Equipment, Appliance, and Component Manufacturing: NAICS 335](https://www.bls.gov/iag/tgs/iag335.htm) (accessed 2026-07-22): Reports 2025 broader-subsector employment including 65,350 electrical and electronic assemblers, 57,660 team assemblers, and 14,050 inspectors.
- **S2** — [NAICS 335220 Major Household Appliance Manufacturing](https://www.census.gov/naics/?details=33&input=33&year=2022) (accessed 2026-07-22): Defines the industry as household cooking, laundry, refrigeration and freezer equipment plus dishwashers, water heaters, garbage disposals, and other major appliances.
- **S3** — [Refrigeration Products](https://www.energy.gov/cmei/buildings/refrigeration-products) (accessed 2026-07-22): States manufacturers have complied with DOE refrigeration-product standards since 1990 and documents amended 2024 standards determined technologically feasible, economically justified, and energy-conserving.
- **S4** — [Samsung Recalls Top-Load Washing Machines Due to Fire Hazard](https://www.cpsc.gov/Recalls/2023/Samsung-Recalls-Top-Load-Washing-Machines-Due-to-Fire-Hazard-Software-Repair-Available) (accessed 2026-07-22): Documents a roughly 663,500-unit washer recall for short-circuit and overheating risk, illustrating safety, software, warranty, and recall constraints.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey found 22% of employer-business owners planned to sell or transfer ownership within five years, while 5% planned closure and 5% had no plan.
- **S6** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects household-appliance manufacturing employment from 60,100 in 2024 to 55,600 in 2034, down 7.5%, while its real-output index rises from 21.9 to 24.1.
