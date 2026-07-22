# 484121 — General Freight Trucking, Long-Distance, Truckload

*v5.1 Stage 1 research memo. Run `484121-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.11 · L 0.83 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Limited-domain driverless freight makes a large driver wage pool technically exposed, while a deep carrier population supplies many potential transferable firms.
**Weakness:** Most exposed driver work will not be implemented quickly across smaller fleets, and competitive freight pricing plus technology-vendor economics can pass away much of the realized benefit.

## Business-model lens
- Included: U.S. lower-middle-market for-hire carriers providing recurring or repeat long-distance full-truckload movement of general freight from shipper origin to consignee destination.
- Excluded: Private shipper fleets, captive transportation units, freight brokers without carrier operations, independent driving services classified elsewhere, local trucking, LTL networks, specialized freight, shells, and non-control financing vehicles.
- Customer and revenue model: Shippers and logistics intermediaries purchase full-load capacity under lane or customer contracts and spot quotes, generally priced per mile, shipment, or committed capacity with fuel and accessorial adjustments.
- Deviation from default lens: none

## Executive view
Long-distance truckload has a large addressable firm population and unusually meaningful technical exposure because highway driving itself has entered limited commercial driverless operation. The central constraint is adoption: the biggest wage pool converts only on supported lanes with compatible equipment, terminals, insurance, remote support, and customer processes. Back-office AI is easier but smaller, while fierce rate competition and vendor pricing limit retained economics.

## How AI changes the work
AI can automate document intake, billing, customer status responses, appointment work, bid preparation, route and load suggestions, driver communication, safety review, and maintenance triage. Driverless systems can substitute highway-driving hours within validated operating domains. Drivers or field staff remain necessary for many surface-street, loading, inspection, cargo-securement, fueling, maintenance, weather, and emergency exceptions until end-to-end operating domains broaden.

## Value capture
Truckload pricing resets through bids, contracts, and spot markets in a fragmented industry where carriers compete heavily on price, service, and capacity. Savings that become common will migrate toward shippers, and autonomous-system suppliers can charge for part of the benefit. Temporary scarcity, dense lanes, high utilization, and superior reliability can preserve more value for an early operator, but sustained retention requires operating differentiation rather than technology access alone.

## Firm availability
The frozen estimate of 2,819 firms provides a broad theoretical pool, and most are structurally eligible for the external-service lens. Actual transferability depends on normalized cycle earnings, fleet debt and age, insurance, claims, safety ratings, customer concentration, and how much commercial goodwill resides with the owner. General exit surveys imply substantial intent, but only a discounted portion should become qualifying closed control transfers.

## Demand durability
The economy continues to require movement of full loads, and federal output, tonnage, and combination-truck-mile forecasts all point to long-run growth. Demand remains volatile over a five-year deal horizon because inventory cycles, manufacturing, trade, fuel, and intermodal competition move load volumes and rates. AI changes how freight is operated more readily than it eliminates the need for an accountable carrier.

## Risks and uncertainty
The largest uncertainty is the pace and lane coverage of driverless implementation at LMM fleets. Provider scale plans can slip, state rules and insurance can fragment rollout, and off-domain tasks can preserve labor even after highway automation. A business is unattractive if its lanes do not match scalable operating domains, customers rapidly reprice savings, fleet capex is heavy, safety or claims impair transfer, or normalized profit reflects a temporary freight cycle peak.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2105 | — | OBSERVED | — |
| n | — | 2819 | — | ESTIMATE | — |
| a | 0.32 | 0.45 | 0.58 | PROXY | S1, S2, S3, S4 |
| rho | 0.1 | 0.22 | 0.38 | ESTIMATE | S4, S5, S6 |
| e | 0.9 | 0.96 | 0.99 | ESTIMATE | S7, S8 |
| s5 | 0.16 | 0.27 | 0.4 | PROXY | S9, S10 |
| q | 0.2 | 0.38 | 0.58 | ESTIMATE | S11 |
| d5 | 0.98 | 1.07 | 1.16 | PROXY | S12, S13, S14 |
| o | 0.95 | 0.985 | 1 | ESTIMATE | S5, S11 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.27 | 0.83 | 1.86 | ESTIMATE |
| F | 9.67 | 10.00 | 10.00 | ESTIMATE |
| C | 4.00 | 7.60 | 10.00 | ESTIMATE |
| D | 9.31 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation mix covers all truck transportation and excludes self-employed workers.
- a: O*NET task frequencies are occupation-wide rather than specific to long-distance truckload fleets.
- a: Driverless feasibility is highly operating-domain-specific and should not be interpreted as exposure of every lane or duty.
- a: The frozen compensation-to-receipts input uses 2024 wages over 2022 receipts and is harmonized to an IPS basis as stated in the assignment.
- rho: Autonomy-provider scale targets and readiness statements are forward-looking and may slip.
- rho: Implementation varies sharply by weather, road class, terminal access, cargo, state law, and customer process.
- rho: Back-office deployment is easier but represents a smaller wage pool than driving.
- e: Eligibility is not observed for the 2,819 modeled firms.
- e: The frozen firm count is margin-bridged using a sector margin and may misclassify firms near the earnings-band boundaries.
- e: A carrier may fit the service definition yet fail practical transferability because of safety history, customer concentration, or owner dependence.
- s5: Neither source measures truckload-carrier control transfers in the target EBITDA band.
- s5: Marketplace transactions skew smaller than the target band and are voluntarily reported.
- s5: Industry downturns can increase seller intent while reducing the share of businesses that close as going concerns.
- q: Large public-carrier disclosures are a proxy for LMM pricing behavior.
- q: Dedicated, differentiated, or capacity-constrained lanes can retain more than commodity one-way truckload.
- q: The estimate excludes implementation probability and freight-volume response to lower rates.
- d5: All cited forecasts cover broader truck or freight populations than the target code.
- d5: Real industry output is not identical to constant-quality physical service quantity.
- d5: Truckload demand is cyclical and can deviate sharply from long-run forecasts over one five-year window.
- o: Operator-required does not mean a human must remain in the cab.
- o: Private-fleet insourcing would reduce the lens share even though physical trucking persists.
- o: Intermodal substitution is primarily reflected in d5 to avoid double counting.

## Sources
- **S1** — [May 2023 OEWS: NAICS 484000 Truck Transportation](https://www.bls.gov/oes/2023/may/naics3_484000.htm) (accessed 2026-07-22): Broader-industry occupation mix, including heavy tractor-trailer drivers at 58.12%, office/administrative support at 11.32%, and dispatchers at 2.42% of employment.
- **S2** — [O*NET OnLine: Heavy and Tractor-Trailer Truck Drivers](https://www.onetonline.org/link/summary/53-3032.00) (accessed 2026-07-22): Driver tasks include driving, route adjustment, logs and document review as well as vehicle and cargo inspection, coupling, loading support, maintenance, and emergency work.
- **S3** — [O*NET OnLine: Dispatchers, Except Police, Fire, and Ambulance](https://www.onetonline.org/link/summary/43-5032.00) (accessed 2026-07-22): Dispatch work includes scheduling operations and employees, coordinating resources, relaying information, responding to problems, and maintaining records.
- **S4** — [Aurora Innovation First Quarter 2026 Shareholder Letter](https://ir.aurora.tech/sec-filings/all-sec-filings/content/0001828108-26-000050/aurora26q1shareholderlet.htm) (accessed 2026-07-22): Reports $1 million of Q1 2026 revenue across driverless and supervised commercial loads, continued testing of weigh-station and on-route fueling, and planned second-generation driverless hardware rollout.
- **S5** — [FMCSA: Safe Integration of Automated Driving Systems-Equipped Commercial Motor Vehicles](https://www.fmcsa.dot.gov/newsroom/safe-integration-automated-driving-systems-equipped-commercial-motor-vehicles) (accessed 2026-07-22): Explains Level 4 operation within an operating domain, continued human roles outside it, regulatory adaptation needs, and continuing motor-carrier safety oversight even without an onboard human.
- **S6** — [FMCSA: Human Factor in ADS-Equipped Commercial Motor Vehicles](https://www.fmcsa.dot.gov/research-and-analysis/human-factor-ads-equipped-commercial-motor-vehicles) (accessed 2026-07-22): States that little research had focused specifically on ADS-equipped commercial vehicles and describes ongoing Level 3 and Level 4 transfer-of-control research.
- **S7** — [2022 NAICS Definition: 484121 General Freight Trucking, Long-Distance, Truckload](https://www.census.gov/naics/?details=484121&input=484121&year=2022) (accessed 2026-07-22): Defines the industry as long-distance full-truck movement of general freight from origin to destination, with a single full load not combined with other shipments.
- **S8** — [2022 Annual Business Survey: Employer Firms in NAICS 484121](https://data.census.gov/table/ABSCS2022.AB00MYCSA01B?codeset=naics~484121&y=2022) (accessed 2026-07-22): Reports 50,747 employer firms, $170.831 billion of sales or revenue, 590,026 employees, and $34.507 billion of annual payroll for the six-digit industry.
- **S9** — [2023 National State of Owner Readiness Report](https://exit-planning-institute.org/hubfs/Member%20Center%20Resources/2023%20National%20State%20of%20Owner%20Readiness%20Report.pdf) (accessed 2026-07-22): Reports that 49% of surveyed U.S. business owners wanted to exit within five years.
- **S10** — [BizBuySell Insight Report: Q2 2026](https://www.bizbuysell.com/insight-report/) (accessed 2026-07-22): Reports 2,117 completed small-business transactions in Q2 2026, retirement as the leading stated sale motivation at 45%, and financing and preparation constraints on completion.
- **S11** — [J.B. Hunt Transport Services 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/728535/000143774926005294/jbht20251231_10k.htm) (accessed 2026-07-22): Describes full-load freight as highly fragmented and competitive, with thousands of often-small carriers, competition primarily on price, service and capacity, and use of both contractual and spot rate quotes.
- **S12** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects truck-transportation real output from $391.5 billion in 2024 to $487.1 billion in 2034, a 2.2% compound annual increase.
- **S13** — [FHWA 2024 Forecasts of Vehicle Miles Traveled](https://www.fhwa.dot.gov/policyinformation/tables/vmt/2024_vmt_forecast_sum.cfm) (accessed 2026-07-22): Forecasts combination-truck vehicle miles to increase 1.1% annually through 2050.
- **S14** — [FHWA Freight Analysis Framework Version 5 Overview](https://ops.fhwa.dot.gov/freight/freight_analysis/faf/faf5/FAF5FHWAWebinarJuly282022final.pdf) (accessed 2026-07-22): Projects truck freight tonnage from 11.848 billion tons in 2017 to 17.545 billion tons in 2050, a 1.2% compound annual increase.
