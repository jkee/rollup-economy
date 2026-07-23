# 221117 — Biomass Electric Power Generation

*v5.1 Stage 1 research memo. Run `221117-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.29 · L 1.42 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Contracted recurring power sales and operator-heavy, instrumented thermal plants create a plausible path to retain AI-enabled operating efficiencies.
**Weakness:** A sustained decline in wood-derived generation and uncertain eligibility of the estimated LMM firms undermine five-year demand and target availability.

## Business-model lens
- Included: US lower-middle-market firms that control and operate stand-alone wood-, wood-waste-, or agricultural-residue-fueled electric power plants and repeatedly sell electricity and associated renewable attributes to external offtakers.
- Excluded: Captive industrial cogeneration; regulated-utility units; passive project or tax-equity vehicles; development-stage projects without operating generation; municipal-solid-waste incinerators whose primary economics include disposal fees; landfill-gas projects; and renewable natural gas production.
- Customer and revenue model: Recurring electricity sales, typically through a power purchase agreement or wholesale market, potentially supplemented by renewable energy credits; the screened firm procures feedstock and remains accountable for plant operation, environmental compliance, and delivery.
- Deviation from default lens: NAICS 221117 combines stand-alone wood or residue power, captive industrial generation, landfill gas, and waste-to-energy facilities. The lens retains stand-alone solid-biomass generators selling externally because the excluded models have materially different feedstock, tipping-fee, captive-use, and control economics that would make one screen incoherent.

## Executive view
Stand-alone biomass generators have a data-rich operating environment and a labor mix led by plant operators, creating credible opportunities in monitoring, diagnostics, maintenance planning, combustion optimization, and compliance workflow. Long-term PPAs can preserve savings and a recent 100% project-company sale confirms transferability. The counterweight is structural demand erosion: national wood-derived generation fell roughly 18% from 2019 to 2024, and the target population is obscured by captive, municipal, regulated, landfill-gas, and waste-disposal models.

## How AI changes the work
AI can forecast feedstock quality and inventory, improve boiler and combustion settings, detect equipment anomalies, prioritize maintenance, triage alarms, and draft environmental or operating reports. These tools augment a workforce concentrated in plant operation and maintenance, but they do not remove fuel handling, ash, repair, testing, emergency response, or licensed accountability.

## Value capture
Existing fixed or long-term PPAs can delay customer capture of internal cost reductions, supporting moderate retention. Savings may still be absorbed by aging-plant maintenance, emissions controls, feedstock inflation, debt restrictions, performance penalties, or lower renewal pricing when biomass competes against cheaper resources.

## Firm availability
The code is economically heterogeneous, so eligibility requires direct verification of external sales, operational control, EBITDA, feedstock contracts, and PPA durability. A 2024 acquisition of all equity in a 55 MW project company shows that a contracted wood-waste plant can transfer, but does not prove frequent LMM deal flow or owner succession.

## Demand durability
Every surviving plant's output remains operator-required, yet the quantity of wood-derived generation has contracted. Waste diversion, renewable attributes, firm generation needs, and contracts can support individual assets, but retirements, fuel competition, aging boilers, environmental regulation, and unfavorable power economics can continue to reduce the service basket.

## Risks and uncertainty
Major risks are plant and PPA concentration, fuel availability and delivered cost, emissions compliance, fire and boiler outages, ash disposal, community opposition, capital needs, project debt, and a declining national generation base. The frozen firm count and compensation ratio span heterogeneous business models, and published AI evidence does not measure actual labor savings at LMM biomass plants.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2995 | — | OBSERVED | — |
| n | — | 28 | — | ESTIMATE | — |
| a | 0.14 | 0.27 | 0.4 | PROXY | S1, S2 |
| rho | 0.28 | 0.47 | 0.65 | ESTIMATE | S2, S3 |
| e | 0.2 | 0.42 | 0.65 | ESTIMATE | S4, S5 |
| s5 | 0.05 | 0.12 | 0.22 | PROXY | S5 |
| q | 0.5 | 0.69 | 0.85 | ESTIMATE | S5, S6 |
| d5 | 0.68 | 0.84 | 1.02 | PROXY | S4, S7 |
| o | 0.95 | 0.98 | 1 | ESTIMATE | S2, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.47 | 1.52 | 3.11 | ESTIMATE |
| F | 0.40 | 1.42 | 2.59 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.46 | 8.23 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS provides headcount shares rather than wage-weighted task shares.
- a: The 2,300-worker exact-industry estimate includes landfill gas, waste biomass, and other models outside the narrowed lens.
- a: DOE's AI use cases cover the wider power system and are not observed biomass labor savings.
- rho: Published evidence demonstrates cross-power-sector use cases and biomass-combustion research, not broad production deployment in US LMM biomass plants.
- rho: Financially stressed or closure-risk plants may defer even positive-payback systems.
- e: The frozen firm count is margin-bridged rather than observed and may include inactive or non-operating entities.
- e: A 55 MW plant transaction demonstrates an eligible structure but not the population share in the target EBITDA band.
- s5: One disclosed acquisition cannot establish an industry transfer rate.
- s5: The seller and buyer were institutional owners, not owner-operators with known succession needs.
- s5: No owner-age data were found for eligible private firms.
- q: Public announcements confirm long-term PPAs but do not disclose price, escalators, reopeners, or remaining term.
- q: Feedstock cost and power revenue may be separately indexed, making benefit retention plant-specific.
- d5: Historical generation is affected by outages, fuel prices, weather, and plant mix as well as demand.
- d5: The retained lens is narrower than EIA's fuel categories.
- d5: BLS projects only 1.9% employment growth from 2024 to 2034, but employment is not a demand measure and no exact-industry output projection is published.
- o: Operator-required demand does not imply preservation of the current independent firm count after consolidation.
- o: The estimate concerns accountable operation, not staffing levels.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 221117](https://www.bls.gov/oes/2023/may/naics5_221117.htm) (accessed 2026-07-23): Exact-industry employment of 2,300; power plant operators 38.31%; production 48.01%; maintenance 14.85%; management 14.05%; business and financial operations 6.66%; and administrative support 4.60%.
- **S2** — [AI for Energy](https://www.energy.gov/sites/default/files/2024-04/AI%20EO%20Report%20Section%205.2g%28i%29_043024.pdf) (accessed 2026-07-23): DOE identifies power-sector AI functions including predictive asset maintenance, anomaly detection, state estimation from sparse measurements, outage analysis, and operational decision support.
- **S3** — [A review on the application of machine learning for combustion in power generation applications](https://www.osti.gov/biblio/1981002) (accessed 2026-07-23): The DOE-hosted research review covers biomass combustion and identifies modeling, prediction, forecasting, optimization, fault detection, and control as machine-learning applications in combustion power generation.
- **S4** — [Electric Power Annual Table 3.1.B: Net Generation from Renewable Sources](https://www.eia.gov/electricity/annual/table.php?t=epa_03_01_b.html) (accessed 2026-07-23): Wood-derived generation fell from 38.543 million MWh in 2019 to 31.564 million MWh in 2024; landfill gas fell from 10.468 million to 7.341 million MWh, while biogenic MSW fell from 6.093 million to 5.402 million MWh.
- **S5** — [Pacolet Milliken Acquires Piedmont Green Power](https://pacoletmilliken.com/pacolet-milliken-acquires-piedmont-green-power-to-grow-its-sustainable-power-and-infrastructure-portfolio/) (accessed 2026-07-23): In January 2024 Pacolet announced acquiring 100% of a project company owning a 55 MW biomass plant that uses about 600,000 tons of wood waste annually and sells to Georgia Power under a long-term PPA.
- **S6** — [Small Municipal Waste Combustors: New Source Performance Standards and Emission Guidelines](https://www.epa.gov/stationary-sources-air-pollution/small-municipal-waste-combustors-smwc-new-source-performance) (accessed 2026-07-23): EPA identifies Clean Air Act limits for particulate matter, carbon monoxide, dioxins and furans, sulfur dioxide, nitrogen oxides, hydrogen chloride, lead, mercury, and cadmium, illustrating operator-intensive compliance obligations in combustion-based waste power.
- **S7** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-23): BLS projects biomass electric power generation employment from 2,400 in 2024 to 2,500 in 2034, a 1.9% increase, while publishing no separate exact-industry output forecast.
