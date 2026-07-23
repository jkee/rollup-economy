# 115113 — Crop Harvesting, Primarily by Machine

*v5.1 Stage 1 research memo. Run `115113-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.32 · L 2.70 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A high-fit outsourced service model where scarce crews and expensive mobile fleets create recurring demand for productivity and scheduling improvements.
**Weakness:** Already-mechanized work and capital-intensive, safety-critical field conditions limit both remaining AI labor exposure and rapid full-autonomy adoption.

## Business-model lens
- Included: US lower-middle-market custom harvesting firms that repeatedly supply machine-based combining, picking, threshing, mowing, baling, forage chopping, and closely related harvest and field-haul services to external farms and producers.
- Excluded: A farm harvesting only its own crops, equipment-only rental, hand-harvest labor contracting without a substantive machine-harvesting service, crop production for the operator's own account, shell entities, and non-control financing vehicles.
- Customer and revenue model: Customers are farms, ranches, dairies, landowners, and crop producers that outsource seasonal harvest operations; revenue is usually charged per acre, bale, ton, hour, crop unit, or bundled harvested-and-hauled job, with repeat seasonal relationships and the contractor supplying machinery and operators.
- Deviation from default lens: none

## Executive view
Custom machine harvesting is a coherent recurring outsourced service with high apparent lens eligibility and durable physical necessity. AI can improve fleet productivity and administration, but the work is already heavily mechanized, and full autonomy must survive difficult field conditions, safety constraints, seasonal utilization, and capital economics.

## How AI changes the work
Near-term impact is strongest in scheduling, route planning, quoting, documentation, machine settings, yield and moisture sensing, predictive maintenance, telematics, and supervised autonomy. Driverless operation and robotic specialty-crop picking add upside, but repair, transport, field recovery, setup, safety oversight, and irregular-condition judgment remain material.

## Value capture
Per-acre and per-output pricing can preserve gains during a quoted season, especially where better timeliness and lower crop loss matter. Transparent state rate surveys, repeat negotiation, commodity-like competition, and customer self-performance should pass a meaningful share of gains back to farmers over time.

## Firm availability
The NAICS boundary closely matches the outsourced-service lens, and the supplied dataset estimates a small but tangible LMM population. Businesses often have transferable fleets, crews, routes, and repeat customers, but association evidence also shows family succession, equipment liquidation, and owner dependence that may prevent qualifying outside control transfers.

## Demand durability
Every crop cycle requires harvest, while USDA projects stable-to-softening major field-crop acreage. Outsourcing can outperform acreage if high machinery costs and labor scarcity make specialist fleets more economical, but farm consolidation, larger machines, and captive autonomy can reduce external jobs.

## Risks and uncertainty
The main risks are a limited target count, extreme seasonality, weather and crop volatility, expensive fast-depreciating equipment, debt and working-capital needs, labor and visa dependence, road and field safety, customer concentration, founder-specific relationships, and autonomy that shifts value to OEMs rather than operators. The dataset labor ratio also has a material wage-receipts vintage mismatch.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.7361 | — | OBSERVED | — |
| n | — | 25 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.33 | PROXY | S2, S3, S4 |
| rho | 0.34 | 0.53 | 0.7 | PROXY | S3, S4 |
| e | 0.68 | 0.83 | 0.94 | PROXY | S1, S5 |
| s5 | 0.1 | 0.21 | 0.35 | PROXY | S5 |
| q | 0.35 | 0.52 | 0.68 | PROXY | S6 |
| d5 | 0.93 | 0.98 | 1.05 | PROXY | S7, S2, S5 |
| o | 0.87 | 0.95 | 0.99 | ESTIMATE | S1, S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.20 | 3.28 | 6.80 | PROXY |
| F | 1.60 | 2.70 | 3.57 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | PROXY |
| D | 8.09 | 9.31 | 10.00 | ESTIMATE |

## Caveats
- a: Specialty-crop robotics evidence is not representative of already mechanized grain and forage crews.
- a: The dataset labor ratio combines 2024 wages with 2022 receipts and a harmonization adjustment, so it may misstate the current labor share even though it is not re-estimated here.
- rho: Successful demonstrations may not persist through dust, darkness, lodging, mud, crop variability, and time-critical commercial workloads.
- rho: Implementation economics vary sharply by crop, terrain, fleet age, annual machine hours, and ability to redeploy equipment across regions.
- e: NAICS assignment is establishment-based and may not cleanly separate custom harvesting from diversified farming, hauling, planting, or manure services.
- e: The LMM firm count is a margin-bridged estimate from size-class receipts rather than an observed count.
- s5: Association leadership profiles are selected anecdotes and not a representative owner-age or transaction sample.
- s5: Equipment liquidation, internal family succession, and retirement without a transferable operation are not qualifying control transfers.
- q: State surveys mix farmers, custom operators, cooperatives, and other service providers and do not isolate LMM firms.
- q: Pricing power varies with harvest urgency, local crew scarcity, crop condition, field size, haul distance, and customer concentration.
- d5: The USDA baseline covers major field crops rather than the full NAICS service basket.
- d5: Acreage does not directly measure outsourced harvest intensity, crop mix, machine hours, or value of timeliness.
- o: Continued physical harvesting does not guarantee that an independent operator of today's kind remains the supplier.
- o: Autonomy could shift accountability toward manufacturers, dealers, or large farm platforms even when field work remains physical.

## Sources
- **S1** — [115113: Crop harvesting, primarily by machine - Census Bureau Profile](https://data.census.gov/profile/115113_-_Crop_harvesting%2C_primarily_by_machine?codeset=naics~115113) (accessed 2026-07-23): Official NAICS identity and machine-based crop-harvesting industry boundary.
- **S2** — [Farm Labor](https://ers.usda.gov/topics/farm-economy/farm-labor) (accessed 2026-07-23): USDA context on agricultural service-company employees, custom harvest providers, mechanization, labor constraints, and farm-labor measurement limits.
- **S3** — [Artificial Intelligence](https://www.nifa.usda.gov/grants/programs/data-science-food-agricultural-systems-dsfas/artificial-intelligence) (accessed 2026-07-23): USDA evidence on machine learning, remote sensing, precision technologies, autonomous systems, and harvesting robots in agriculture.
- **S4** — [Automation for Specialty Crops](https://www.nifa.usda.gov/about-nifa/impacts/automation-specialty-crops) (accessed 2026-07-23): USDA field evidence on machine vision, automated harvest tools, robotic picking performance, throughput gains, commercialization, and adoption constraints.
- **S5** — [U.S. Custom Harvesters, Inc. - About Us](https://uschi.com/about/) (accessed 2026-07-23): Industry-service model, repeat farmer relationships, independent and family operations, fleet growth, labor programs, succession examples, and equipment-sale evidence.
- **S6** — [Kansas Custom Rates 2026](https://agmanager.info/sites/default/files/pdf/CustomRates_2026.pdf) (accessed 2026-07-23): Current custom-work pricing structure and competitive rate context, including charges that bundle machinery, power, fuel, and operator labor.
- **S7** — [U.S. major field crop acreage projected to decline](https://www.ers.usda.gov/data-products/charts-of-note/114033) (accessed 2026-07-23): USDA long-term projection of modest contraction in major field-crop acreage through 2035, supporting the service-demand baseline.
