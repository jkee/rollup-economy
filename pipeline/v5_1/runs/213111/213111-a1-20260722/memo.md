# 213111 — Drilling Oil and Gas Wells

*v5.1 Stage 1 research memo. Run `213111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.33 · L 1.22 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High labor intensity and recurring outsourced rig operations create a real but bounded workflow-automation opportunity.
**Weakness:** Commodity-driven utilization and productivity gains can reduce drilling demand even while US hydrocarbon production remains high.

## Business-model lens
- Included: US lower-middle-market contractors repeatedly drilling oil and gas wells for external exploration and production customers on a contract or fee basis, including spudding, drilling, redrilling, and directional drilling performed with contractor-operated rigs and crews.
- Excluded: E&P owners drilling solely for their own account; captive drilling units; passive rig lessors without operators; completion and ancillary oilfield services classified in 213112; offshore or land contractors outside the EBITDA band; shells and non-control financing vehicles.
- Customer and revenue model: Recurring outsourced rig-and-crew service sold primarily through daywork/dayrate, well-based, or performance-based contracts, with mobilization and lower rates for some non-operating periods; activity and pricing track customer drilling budgets and rig supply.
- Deviation from default lens: none

## Executive view
Contract drilling has meaningful information-work opportunities around planning, bidding, maintenance, logistics, and reporting, but most labor and accountability remain physical and safety-critical. The service is recurring but exceptionally exposed to commodity prices, rig utilization, and customer capital budgets.

## How AI changes the work
AI can assist tenders, well-plan comparison, directional decision support, shift reporting, maintenance prediction, parts planning, crew logistics, HSE documentation, and invoice reconciliation. Rig moves, pipe handling, drilling execution, equipment repair, mud control, and emergency well control remain embodied and supervised.

## Value capture
Dayrate contracts can preserve internal cost savings during their term, while competitive rebids, lower-rate downtime, customer concentration, and performance-linked compensation share gains. The commercial result depends more on utilization and contract terms than on list pricing.

## Firm availability
The code is intrinsically outsourced, so operating firms broadly fit the service lens. Eligibility still requires active rigs, through-cycle EBITDA, transferable contracts and crews, independent ownership, and acceptable environmental and safety liabilities; the injected 241-firm estimate may be cycle-sensitive.

## Demand durability
Current US rig counts are broadly stable, and near-term oil and gas production remains high, but major land-drilling activity has declined and longer-term oil outlooks show pressure before the mid-2030s. Productivity enables output with fewer rigs, so physical production durability does not ensure drilling-service volume.

## Risks and uncertainty
Principal risks are oil and gas prices, E&P budget cuts, rapid rig productivity, customer concentration, dayrate pressure, idle-rig carrying costs, debt and working capital, equipment obsolescence, crew shortages, accidents, environmental liability, regulation, and asset-only rather than firm-level transactions.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2884 | — | OBSERVED | — |
| n | — | 241 | — | ESTIMATE | — |
| a | 0.14 | 0.24 | 0.35 | PROXY | S2 |
| rho | 0.27 | 0.44 | 0.61 | ESTIMATE | S3, S4 |
| e | 0.61 | 0.77 | 0.89 | ESTIMATE | S0 |
| s5 | 0.09 | 0.19 | 0.31 | PROXY | S8 |
| q | 0.32 | 0.48 | 0.64 | PROXY | S7 |
| d5 | 0.63 | 0.89 | 1.18 | PROXY | S5, S6, S7, S9 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.44 | 1.22 | 2.46 | ESTIMATE |
| F | 4.27 | 5.78 | 6.78 | ESTIMATE |
| C | 6.40 | 9.60 | 10.00 | PROXY |
| D | 5.92 | 8.72 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation mix includes non-drilling support services.
- a: Task exposure is inferred rather than observed labor substitution.
- rho: No direct survey measures five-year implementation in LMM drillers.
- rho: Safety and customer-control requirements may slow deployment more than technical capability suggests.
- e: The injected n is margin-bridged from size classes using a sector EBITDA margin and may be distorted by the drilling cycle.
- e: Rig ownership and operating entity can differ.
- s5: Owner age is not an observed deal probability.
- s5: Asset transactions are common and must not be counted as firm control transfers.
- q: Contract terms vary by basin, rig class, utilization, and customer.
- q: The source is a large public contractor and may not reflect LMM bargaining power.
- d5: Energy outlooks are highly price- and policy-sensitive.
- d5: Rig counts do not capture footage, lateral length, or service intensity.
- d5: The 2030 outlook covers all US production, not LMM contractors.
- o: Operator consolidation and self-performance can reduce the independent share even though physical drilling persists.

## Sources
- **S0** — [2022 NAICS definition: 213111 Drilling Oil and Gas Wells](https://www.census.gov/naics/?details=21311&input=21311&year=2022) (accessed 2026-07-23): Defines establishments drilling oil and gas wells for others on a contract or fee basis.
- **S2** — [May 2023 OEWS: Support Activities for Mining](https://www.bls.gov/oes/2023/may/naics4_213100.htm) (accessed 2026-07-23): Broader occupation mix: construction/extraction 46.43%, roustabouts 11.92%, and installation/maintenance/repair 9.16% of employment.
- **S3** — [OSHA Oil and Gas Well Drilling eTool](https://www.osha.gov/etools/oil-and-gas/drilling) (accessed 2026-07-23): Describes drilling, casing, maintenance, and well-control work and states trained personnel are essential for well control.
- **S4** — [OSHA Drilling Well Control](https://www.osha.gov/etools/oil-and-gas/drilling/well-control) (accessed 2026-07-23): Details pressure monitoring, drilling-fluid control, BOP installation/testing, and trained-personnel requirements.
- **S5** — [EIA Crude Oil and Natural Gas Drilling Activity](https://www.eia.gov/dnav/ng/ng_enr_drill_s1_m.htm) (accessed 2026-07-23): Monthly US rotary rigs averaged 553 in May 2026: 535 onshore, 18 offshore, 417 oil-directed, and 127 gas-directed.
- **S6** — [Annual Energy Outlook 2026: Oil and natural gas](https://www.eia.gov/outlooks/aeo/index.php/consumption/outlooks/aeo/) (accessed 2026-07-23): Most cases keep real Brent below $70 through 2030 and show US crude production declining through the mid-2030s; 2025 production was 13.6 million barrels per day.
- **S7** — [Patterson-UTI Energy 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/889900/000088990026000013/pten-20251231.htm) (accessed 2026-07-23): Describes daywork and performance-based contracts; reports US average operating rigs of 124 in 2023, 112 in 2024, and 100 in 2025 and wells drilled declining from 2,530 to 2,090.
- **S8** — [ABS Characteristics of Business Owners: 2024 Tables](https://www.census.gov/data/tables/2024/econ/abs/2024-abs-characteristics-of-owners.html) (accessed 2026-07-23): Official Census Age of Owner tables for employer businesses, used only as a broad succession proxy.
- **S9** — [EIA Short-Term Energy Outlook, July 2026](https://www.eia.gov/outlooks/steo/archives/jul26.pdf) (accessed 2026-07-23): Forecast US crude production of 13.8 million barrels per day in 2026 and 14.0 in 2027, with LNG exports increasing from 17 to 19 Bcf/d.
