# 221330 — Steam and Air-Conditioning Supply

*v5.1 Stage 1 research memo. Run `221330-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.73 · L 0.78 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Long-lived connected thermal networks preserve accountable recurring demand while data-rich administrative and operating-support workflows offer implementable productivity gains.
**Weakness:** Few systems are simultaneously private, externally serving, lower-middle-market, independently transferable, and able to retain efficiencies after regulation or contract renewal.

## Business-model lens
- Included: US lower-middle-market operators that repeatedly supply steam, hot water, heated air, or chilled water from a central plant through a thermal network to multiple external customer buildings, and that retain accountable responsibility for plant, distribution, metering, reliability, compliance, and customer service.
- Excluded: Shells, captive internal units, non-control financing vehicles, municipal or government-owned systems, campus central plants serving only affiliated buildings, in-building HVAC contractors, equipment wholesalers, firms outside the screened EBITDA band, and entities that own passive infrastructure without accountable thermal-service operations are excluded.
- Customer and revenue model: Customers are typically commercial buildings, hospitals, universities, public institutions, residential complexes, industrial sites, and mixed-use districts. Revenue commonly combines usage or demand charges with recurring customer charges under regulated tariffs or long-term service contracts, sometimes including fuel or other cost adjustments.
- Deviation from default lens: none

## Executive view
Steam and air-conditioning supply is a recurring, infrastructure-bound service with high customer switching costs and persistent physical operating duties. The credible target universe is narrower than the system universe because many plants are captive campuses, government owned, or held by large utilities. The operational opportunity lies in integrating metering, forecasting, maintenance, billing, compliance, and plant data while preserving accountable human control over safety, uptime, emissions, and field work.

## How AI changes the work
AI can improve load forecasting, meter and billing exception handling, maintenance triage, operating-log analysis, engineering knowledge retrieval, compliance drafts, work scheduling, and customer service. Advanced controls also show room for better optimization, but reductions in fuel use are not labor substitution by themselves. High-consequence control actions, emergency response, inspection, repairs, and operator sign-off will remain human-led.

## Value capture
Embedded networks and costly customer alternatives can protect value under fixed-price contracts and between rate reviews. Capture is weaker where tariffs or open-book contracts pass costs and efficiencies through, anchor customers renegotiate, or regulators reset allowed expenses. The key diligence question is whether labor productivity remains with the operator after the next rate case or contract renewal.

## Firm availability
The provided firm estimate is small and uncertain, and only a share will have external customers, standalone accountable operations, qualifying economics, and transferable control. EIA's larger physical-system universe includes many campuses and public systems that fail the lens. Infrastructure ownership can generate transactions, but corporate and fund ownership makes broad owner-age evidence a weak succession proxy.

## Demand durability
Heating and cooling remain essential, and district systems allow connected buildings to avoid individual plant space, capital, operation, and maintenance. Historical connected floorspace grew modestly, while newer geothermal and mixed-temperature networks broaden the technology path. Legacy steam can lose quantity to efficiency, redevelopment, building-level electrification, or customer bypass, so system-level connection and conversion data matter more than national averages.

## Risks and uncertainty
The main risks are an extremely narrow eligible universe, ownership and NAICS ambiguity, environmental liabilities, boiler and emissions compliance, aging buried infrastructure, outages, cybersecurity, customer and geographic concentration, weather exposure, fuel-price volatility, rate-case disallowance, decarbonization capital needs, and anchor-customer bypass. A single pipe failure, lost campus contract, unfavorable tariff reset, or mandatory plant conversion can outweigh administrative labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1294 | — | OBSERVED | — |
| n | — | 32 | — | ESTIMATE | — |
| a | 0.18 | 0.3 | 0.43 | PROXY | S2, S3 |
| rho | 0.3 | 0.5 | 0.68 | PROXY | S3, S7 |
| e | 0.38 | 0.56 | 0.72 | ESTIMATE | S1, S4, S5 |
| s5 | 0.1 | 0.2 | 0.31 | PROXY | S6 |
| q | 0.4 | 0.59 | 0.75 | PROXY | S8 |
| d5 | 0.95 | 1.03 | 1.12 | PROXY | S4, S5, S9 |
| o | 0.86 | 0.94 | 0.99 | ESTIMATE | S3, S4, S7, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.78 | 1.51 | PROXY |
| F | 1.28 | 2.45 | 3.37 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | PROXY |
| D | 8.17 | 9.68 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation table covers all of NAICS 2213 and is dominated by water and wastewater systems rather than thermal utilities.
- a: Employment shares are not wage-weighted task shares and do not reveal automation already embedded in plant controls.
- a: Staffing varies materially between steam, hot-water, chilled-water, combined heat and power, and geothermal networks.
- rho: DOE projects demonstrate technical potential rather than representative commercial adoption.
- rho: Optimization can reduce fuel rather than labor, which is outside this primitive unless it also substitutes work or avoids hiring.
- rho: Boiler requirements differ by fuel, source category, location, and equipment configuration.
- e: EIA's system universe is not a NAICS firm universe and includes captive campus and government systems.
- e: A single operator may own multiple plants or networks, while a system can involve several legal entities.
- e: The provided firm count is itself margin-bridged from size classes, and capital-intensive utility margins can vary sharply by contract and regulation.
- s5: The Census age evidence is cross-industry, represents responding employer-business owners, and uses 2018 data.
- s5: Asset or concession transfers may not constitute acquisition of a transferable operating firm.
- s5: Public, captive, and large corporate systems have transfer mechanisms unrelated to individual owner age.
- q: Con Edison is far larger than the screened band and operates in a unique dense urban market.
- q: Rate regulation and contract structures differ by state, municipality, ownership model, and customer class.
- q: A local network can have strong physical exclusivity while still facing political or anchor-customer pressure on rates.
- d5: The central growth observation covers 2012 through 2016 and may not represent the next five years.
- d5: Connected floorspace is not constant-quality thermal output and heating and cooling floorspace can overlap.
- d5: EIA commercial-building data include captive district heat and do not isolate screened private suppliers.
- o: Operator identity can change even when the physical thermal network remains in use.
- o: Networked geothermal preserves an operator role but can materially change plant, staffing, and revenue models.
- o: Remote monitoring can centralize accountability across multiple systems without eliminating it.

## Sources
- **S1** — [2022 NAICS Definition: 221330 Steam and Air-Conditioning Supply](https://www.census.gov/naics/?details=22133&input=22133&year=2022) (accessed 2026-07-22): Defines the industry as establishments primarily providing steam, heated air, or cooled air and notes that steam may be distributed through mains; distinguishes HVAC installation and equipment wholesaling.
- **S2** — [May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates: NAICS 221300](https://www.bls.gov/oes/2023/may/naics4_221300.htm) (accessed 2026-07-22): Provides the broader water, sewage, and other systems occupation mix, including 23.11 percent office and administrative support, 32.13 percent production, 12.88 percent installation and maintenance, and 9.48 percent management.
- **S3** — [Combined Heat and Power and District Energy](https://www.energy.gov/cmei/ito/combined-heat-and-power-chp-and-district-energy) (accessed 2026-07-22): Describes central plants and pipe networks, efficiency and resilience benefits, emerging control and optimization tools, and a DOE project statement that many community systems use only basic control optimization.
- **S4** — [U.S. District Energy Services Market Characterization](https://www.eia.gov/analysis/studies/buildings/districtservices/pdf/districtservices.pdf) (accessed 2026-07-22): Analyzes 660 US district-energy systems, their campus and downtown customer settings, central plants and networks, fuel mix, historical connected floorspace, reported annual additions, and trends toward modest growth, hot water, and cooling.
- **S5** — [Energy Sources Used in U.S. Commercial Buildings](https://www.eia.gov/consumption/commercial/data/2018/pdf/CBECS%20energy%20sources.pdf) (accessed 2026-07-22): Reports 86,000 commercial buildings using district heat, 305 trillion Btu consumed, 4.3 billion dollars spent, 7 percent of commercial floorspace using it, and 89 percent of district heat consumption used for space heating in 2018.
- **S6** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51 percent of responding US employer-business owners were at least age 55, based on the 2019 Annual Business Survey using 2018 data.
- **S7** — [Compliance for Industrial, Commercial, and Institutional Area Source Boilers](https://www.epa.gov/stationary-sources-air-pollution/compliance-industrial-commercial-and-institutional-area-source) (accessed 2026-07-22): Explains affected boiler fuels and exemptions, notification and electronic compliance reporting, performance testing, energy assessments, tune-ups, recordkeeping, emissions, and operator compliance obligations under the area-source boiler rule.
- **S8** — [Steam Rates and Tariffs](https://www.coned.com/en/rates-tariffs/rates/steam) (accessed 2026-07-22): Shows a regulated steam schedule with customer and usage rates, fuel adjustments, delivery revenue surcharges, and Public Service Commission tariffs, illustrating one important industry billing and pass-through model.
- **S9** — [Geothermal Heating and Cooling](https://www.energy.gov/hgeo/geothermal/geothermal-heating-cooling) (accessed 2026-07-22): Describes networked geothermal systems serving neighborhoods, blocks, campuses, and communities through connected piping, heat pumps, and heat exchangers, supporting technology substitution within an operator-required network model.
