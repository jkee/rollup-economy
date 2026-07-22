# 311615 — Poultry Processing

*v5.1 Stage 1 research memo. Run `311615-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.80 · L 1.06 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repetitive labor-intensive processing with strong vision, sensing, workflow, and selective robotics applicability against growing broiler volume.
**Weakness:** The qualifying independent service subset is likely small because vertically integrated processors dominate poultry throughput.

## Business-model lens
- Included: Lower-middle-market poultry slaughter and processing firms that repeatedly provide inspected, custom, toll, co-processing, cutting, packaging, or value-added processing services to external farms, brands, cooperatives, or food companies.
- Excluded: Vertically integrated poultry companies processing birds they own, captive plants, businesses principally selling their own poultry products, contract grow-out farms, on-farm self-processing, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring or repeat processing for external poultry owners and brands, billed per bird, per pound, per batch, or under negotiated toll/co-processing agreements, sometimes with packaging and specialty-process add-ons.
- Deviation from default lens: The lens is narrowed because NAICS 311615 is dominated by vertically integrated product companies while a smaller custom and toll-processing subset supplies a recurring outsourced service; combining them would make eligibility and retention incoherent.

## Executive view
Poultry processing has credible AI exposure because work is repetitive, high-throughput, and increasingly sensor-friendly. The investable lens is much narrower than the code: only custom, toll, and co-processors serving external owners qualify, while the dominant vertically integrated processors do not.

## How AI changes the work
Near-term gains are strongest in scheduling, records, quality imaging, contamination detection, yield optimization, predictive maintenance, and guided inspection. Direct robotic deboning is promising but still must meet human line speed and yield while surviving washdown and controlling new food-safety risks.

## Value capture
Unit processing fees and scarce inspected capacity support initial retention, particularly where customers need certifications or consistent slots. Renewal bargaining, transparent per-bird economics, customer scale, and replication by competing processors will share benefits over time.

## Firm availability
Most industry capacity is tied to integrators that own birds and control processing and marketing. The qualifying subset consists of independent plants serving farms, brands, and aggregators; some are too small for the EBITDA band and others rely heavily on self-owned throughput, making eligibility and transfer supply uncertain.

## Demand durability
Broiler production is projected to grow steadily, and turkey output is expected to recover, supporting physical throughput. Disease outbreaks, feed and export shocks, weakening turkey consumption, and growth captured by integrated plants remain material risks for eligible processors.

## Risks and uncertainty
The main diligence gaps are third-party revenue share, commercial automation performance at LMM scale, and control-transfer frequency. Food-safety events, avian influenza, wastewater, labor, line downtime, yield loss, customer concentration, and integrator competition can overwhelm savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1666 | — | OBSERVED | — |
| n | — | 87 | — | ESTIMATE | — |
| a | 0.24 | 0.38 | 0.52 | PROXY | S1, S2 |
| rho | 0.25 | 0.42 | 0.6 | PROXY | S2 |
| e | 0.08 | 0.18 | 0.32 | PROXY | S3, S4, S5 |
| s5 | 0.1 | 0.18 | 0.28 | ESTIMATE | — |
| q | 0.45 | 0.65 | 0.82 | PROXY | S4, S5 |
| d5 | 0.99 | 1.07 | 1.15 | PROXY | S6 |
| o | 0.92 | 0.98 | 1 | PROXY | S2, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.40 | 1.06 | 2.08 | PROXY |
| F | 0.85 | 2.16 | 3.50 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | PROXY |
| D | 9.11 | 10.00 | 10.00 | PROXY |

## Caveats
- a: The occupation source includes non-poultry slaughter and processing and is employment-weighted rather than wage-weighted.
- a: Research targets demonstrate exposure, not proven commercial labor substitution.
- rho: The cited program is forward-looking research rather than representative adoption evidence.
- rho: Implementation will differ materially between software workflows and food-contact robotics.
- e: Broiler organization evidence concerns production systems, not a firm-level processor revenue census.
- e: Small custom plants may not reach the $1-10M EBITDA band; larger co-packers may not advertise customers.
- s5: No industry-specific transfer-rate series was found.
- s5: Facility sales, label-owner changes, and family succession may not be qualifying control transfers.
- q: Published small-plant charges do not represent confidential LMM co-processing agreements.
- q: Commodity product sales and processor-owned throughput can obscure true service margins.
- d5: The USDA baseline assumes no further animal-disease outbreaks and continuation of existing policies and trade agreements.
- d5: Industry production growth need not accrue to independent service processors.
- o: Operator-required demand can shift from outsourced processors to self-processing or integrated plants.
- o: Different federal and state exemptions create heterogeneous compliance burdens and market access.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311600](https://www.bls.gov/oes/2023/may/naics4_311600.htm) (accessed 2026-07-22): Broader-industry occupation mix: production 59.77%, cutters and trimmers 18.64%, slaughterers and meat packers 12.20%, and maintenance and repair 6.47%.
- **S2** — [Center for Scalable and Intelligent Automation in Poultry Processing](https://www.nal.usda.gov/research-tools/food-safety-research-projects/center-scalable-and-intelligent-automation-poultry-processing-csiapp) (accessed 2026-07-22): USDA program identifies AI, robotics, sensing, robotic deboning, human-in-the-loop work, contamination detection, and the speed, yield, validation, sanitation, and food-safety challenges of automation.
- **S3** — [Financial Risks and Incomes in Contract Broiler Production](https://www.ers.usda.gov/amber-waves/2014/august/financial-risks-and-incomes-in-contract-broiler-production) (accessed 2026-07-22): USDA describes the integrator model: almost all broilers are raised under contract, while poultry companies supply birds and feed and handle processing and marketing.
- **S4** — [Solving Processing Issues a Key to Successful Local Meat Marketing](https://www.ers.usda.gov/amber-waves/2013/december/solving-processing-issues-a-key-to-successful-local-meat-marketing) (accessed 2026-07-22): USDA documents external poultry-processing services, anchor customers, bottleneck capacity, farmer commitments, variable pricing, scheduling tools, and small-processor throughput challenges.
- **S5** — [Plant in a Box: A Solution for USDA-Inspected Poultry Processing?](https://extension.oregonstate.edu/es/catalog/pub/plant-box-solution-usda-inspected-poultry-processing) (accessed 2026-07-22): Extension case study reports external processing customers, per-bird and per-pound fees, labor intensity, throughput, seasonal staffing, and the economics of a small inspected poultry plant.
- **S6** — [Long-Term Growth Projected as U.S. Poultry and Egg Sector Recovers](https://www.ers.usda.gov/amber-waves/2024/august/long-term-growth-projected-as-u-s-poultry-and-egg-sector-recovers) (accessed 2026-07-22): USDA projects chicken production from 45.7 billion pounds in 2022 to 52.5 billion in 2033 and turkey production up 14% from 2022 by 2033, with explicit disease and policy assumptions.
- **S7** — [9 CFR 381.145: Poultry Products Entering or at Official Establishments](https://www.law.cornell.edu/cfr/text/9/381.145) (accessed 2026-07-22): Federal rules require inspected and identified product, examination, operator identification at receipt, quality-control records, corrective action, and accountable establishment personnel.
