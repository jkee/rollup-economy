# 221115 — Wind Electric Power Generation

*v5.1 Stage 1 research memo. Run `221115-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.57 · L 0.79 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Long-lived contracted assets and sensor-rich turbine fleets create recurring electricity demand and scalable predictive operations opportunities.
**Weakness:** The independently transferable LMM pool is exceptionally small and structurally complex, while current tax and federal permitting policy can sharply reduce new-build and offshore demand.

## Business-model lens
- Included: U.S. lower-middle-market independent operating companies whose primary activity is operating onshore or offshore wind electric generation facilities and repeatedly selling generated electricity to transmission or distribution systems under power purchase agreements, tariffs, or merchant arrangements.
- Excluded: Wind turbine and component manufacturers, construction-only firms, standalone maintenance contractors outside the generation code, developers without operating generation, passive project shells, non-control tax-equity or financing vehicles, and captive utility or corporate facilities that cannot transfer independently.
- Customer and revenue model: Operators sell metered electricity and sometimes renewable attributes or capacity to utilities, public agencies, corporate offtakers, or wholesale markets, commonly under long-term fixed or escalating power purchase agreements and sometimes at merchant prices.
- Deviation from default lens: none

## Executive view
Wind generation combines durable physical output and contracted revenue with useful AI applications in monitoring, prediction, controls, and administration. The opportunity is constrained by a tiny estimated target pool that likely contains project vehicles rather than standalone operators, substantial physical maintenance, and unusually wide policy risk around credits, federal permits, and offshore leasing.

## How AI changes the work
AI can improve wake steering, forecasting, fault detection, predictive maintenance, alarm triage, siting analysis, inventory, and reporting. Technicians still must climb, inspect, troubleshoot, lubricate, repair, and replace components under strict safety procedures.

## Value capture
Long-term PPAs can preserve internal savings, while merchant exposure, cost recovery, O&M sharing, production guarantees, debt restrictions, and later contract renewal pass value to customers, vendors, lenders, or competitors.

## Firm availability
Operating wind assets trade and repower, but the frozen count is only 18 and likely mixes true firms with single-project LLCs, tax-equity structures, captive sponsor vehicles, and utility portfolios. A qualifying target needs standalone control, transferable contracts and land rights, real operating capability, and manageable project finance.

## Demand durability
Existing fleets and near-term additions support continued output, and 2025 generation grew. The accelerated credit cutoff, paused federal approvals, offshore lease cancellations, interconnection delay, curtailment, and long development cycles make year-five growth materially uncertain.

## Risks and uncertainty
Key risks are project-entity misclassification, the margin-bridged count, wind resource variability, turbine age and OEM dependence, catastrophic component failures, technician scarcity, merchant and congestion exposure, leverage and tax equity, PPA and land consents, local opposition, wildlife rules, and federal policy changes.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1303 | — | OBSERVED | — |
| n | — | 18 | — | ESTIMATE | — |
| a | 0.15 | 0.27 | 0.4 | PROXY | S2, S3, S4 |
| rho | 0.36 | 0.56 | 0.72 | PROXY | S3, S4 |
| e | 0.16 | 0.32 | 0.5 | ESTIMATE | S1, S9 |
| s5 | 0.14 | 0.26 | 0.4 | PROXY | S9, S10 |
| q | 0.52 | 0.7 | 0.84 | ESTIMATE | S9 |
| d5 | 0.82 | 1.08 | 1.32 | PROXY | S5, S6, S7, S8 |
| o | 0.975 | 0.994 | 0.999 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.79 | 1.50 | PROXY |
| F | 0.54 | 1.47 | 2.45 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.00 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: NAICS 221100 includes fossil, nuclear, hydro, solar, transmission, and distribution activities with different occupation weights.
- a: BLS wind-technician duties describe one occupation, not the industry's full wage-weighted task mix.
- a: DOE projects establish technical applications, not realized substitution shares at commercial operators.
- rho: Several cited DOE projects are early-stage research rather than scaled commercial deployments.
- rho: Realization depends on OEM access to turbine data and control interfaces.
- rho: Offshore logistics can magnify the value of prediction but also raise validation and safety requirements.
- e: The frozen count is margin-bridged using a general-utility margin that may not fit leveraged wind projects.
- e: NAICS is establishment-based, while eligibility is a firm-level and transaction-structure question.
- e: A transferable wind facility or membership interest is not necessarily a qualifying operating-company acquisition.
- s5: Gallup covers employer businesses across all industries, not wind generators.
- s5: Clearway is a large public owner and its asset transactions do not measure LMM qualifying-firm turnover.
- s5: Sponsor rotation inside a project structure may transfer economic interests without a qualifying standalone operating-company sale.
- q: Clearway's disclosed long-term PPA transactions are not representative of every LMM operator or merchant plant.
- q: Benefits that raise production may be shared or curtailed rather than fully monetized.
- q: Project debt, reserves, land royalties, and tax-equity allocations can separate project economics from cash retained by the operating owner.
- d5: Planned capacity may be delayed or cancelled and is not the same as constant-quality delivered electricity.
- d5: National output can rise while a specific region or wind regime experiences weak production or congestion.
- d5: The credit cutoff has construction and placed-in-service timing rules, so it does not affect all projects equally.
- d5: Federal restrictions weigh most heavily on federally permitted and offshore projects; much onshore development occurs on private or state land.
- o: This is a bounded judgment rather than an observed operator-requirement statistic.
- o: The accountable owner can outsource most physical and digital tasks while remaining necessary under contracts and permits.
- o: Retirement or cancellation is captured primarily in demand, not operator requirement.

## Sources
- **S1** — [2022 NAICS Manual: 221115 Wind Electric Power Generation](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Exact scope: operating wind generation facilities that use wind to drive turbines and provide electricity to transmission or distribution systems.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 221100](https://www.bls.gov/oes/2023/May/naics4_221100.htm) (accessed 2026-07-22): Broad electric-power occupational mix used to bound wage-weighted exposure across engineering, administration, operations, construction, and maintenance.
- **S3** — [Occupational Outlook Handbook: Wind Turbine Technicians](https://www.bls.gov/ooh/installation-maintenance-and-repair/wind-turbine-technicians.htm) (accessed 2026-07-22): Exact technician duties, remote monitoring and data collection, physical climbing and repairs, employment in wind generation, and projected workforce demand.
- **S4** — [DOE Announces Wind R&D Incubator Projects](https://www.energy.gov/cmei/systems/articles/doe-announces-new-165-million-incubator-program-funding-18-research-projects) (accessed 2026-07-22): Wind-specific AI work in permitting and siting analysis, sensing, wake steering, generator and converter failure modeling, offshore analysis, and resilient control.
- **S5** — [New U.S. Electric Generating Capacity Expected to Reach a Record High in 2026](https://www.eia.gov/todayinEnergy/detail.php?id=67205) (accessed 2026-07-22): Planned 2026 wind additions, comparison with 2025 and prior records, geographic concentration, and large onshore and offshore projects.
- **S6** — [Wind and Solar Generated a Record 17% of U.S. Electricity in 2025](https://www.eia.gov/TODAYINENERGY/detail.php?id=67367) (accessed 2026-07-22): Observed 2025 U.S. wind generation and year-over-year growth, plus wind's intermittent generation characteristic.
- **S7** — [Tax Provisions in P.L. 119-21, the FY2025 Reconciliation Law](https://www.congress.gov/crs-product/R48611) (accessed 2026-07-22): Accelerated eligibility cutoff for wind and solar clean-electricity production and investment credits and related restrictions.
- **S8** — [BOEM New York Offshore Wind Activities](https://www.boem.gov/renewable-energy/state-activities/new-york-activities) (accessed 2026-07-22): Current offshore lease cancellations and implementation of the federal pause on new or renewed approvals, rights-of-way, permits, leases, and loans pending review.
- **S9** — [Clearway Energy 2025 Acquisition and Disposition Disclosure](https://www.sec.gov/Archives/edgar/data/1567683/000162828025049051/R11.htm) (accessed 2026-07-22): Operating wind-facility purchase, long-term PPA, complete membership-interest sale for repowering, project financing, and asset-level transaction structure.
- **S10** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): All-industry employer-business ownership aging and five-year sell-or-transfer intentions used as the succession baseline.
