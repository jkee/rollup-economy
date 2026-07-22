# 488119 — Other Airport Operations

*v5.1 Stage 1 research memo. Run `488119-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.16 · L 1.93 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Growing aviation volumes and acute coordination complexity create repeat demand and practical AI-assisted productivity opportunities.
**Weakness:** A heterogeneous NAICS population and strong airline/airport contracting leverage make eligible-firm counts and retained savings uncertain.

## Business-model lens
- Included: US lower-middle-market firms providing recurring outsourced airport and fixed-base operational services, including ramp and turnaround coordination, baggage handling, ground direction, aircraft service support, de-icing, runway clearing, and contract airport administration.
- Excluded: Public airport authorities, airline-captive ground operations, pure hangar or gate landlords, businesses whose economics are predominantly fuel resale or real estate, air traffic control, aircraft repair, janitorial-only firms, catering, security screening, and non-control investment vehicles.
- Customer and revenue model: Airlines, airport authorities, aircraft operators, and tenants purchase contracted services through negotiated ground-handling agreements, per-turn or activity charges, recurring FBO service relationships, and airport-management contracts. Revenue generally combines volume-linked service fees with contractual operating and quality obligations.
- Deviation from default lens: The NAICS code combines asset-heavy airport ownership and space rental with outsourced operational services. The lens is narrowed to recurring third-party operating services because airport landlord economics and labor-based handling economics cannot be screened coherently together.

## Executive view
Outsourced airport operations have a real but bounded AI opportunity. Coordination, dispatch, customer communication, inspection support, billing, and workforce administration can improve materially, while the core service basket remains physical, local, safety-sensitive, and dependent on airport and airline systems. Demand should grow with aviation activity, but the code's mixed asset and service models make firm eligibility and unit economics diligence essential.

## How AI changes the work
The clearest uses are computer-vision timestamping of aircraft turns, resource allocation, disruption prediction, dispatch, records, training, and passenger information. These tools can reduce coordinator load and avoid incremental hiring. Baggage movement, ramp driving, de-icing, runway clearing, mobility assistance, and safety response need robotics or people and should not be counted as near-term generative-AI substitution.

## Value capture
Ground handling is governed by negotiated scope, charges, service levels, and contract duration. Operators can keep some savings before repricing, but airlines and airports are concentrated, sophisticated buyers that can rebid, self-handle, or demand savings at renewal. Capture should be better in differentiated local FBO relationships than in commoditized airline handling.

## Firm availability
The frozen n=264 implies a meaningful LMM population, yet many coded firms may be public airport entities, captive units, landlords, or asset-heavy FBOs rather than transferable outsourced-service companies. After applying the lens, the opportunity remains broader than air traffic control, but every candidate requires revenue-mix, concession, parent, and change-of-control verification.

## Demand durability
FAA forecasts continued passenger and aircraft-operations growth, supporting turns, baggage, ramp, and airport administration. Physical service and accountable safety functions remain durable. Recession, traffic concentration at mega-hubs, airline self-handling, and automation of discrete equipment flows are the main offsets.

## Risks and uncertainty
Risks include customer and airport concentration, rebids, wage floors, labor turnover, safety incidents, equipment capital needs, cybersecurity, fragmented operating data, and the possibility that efficiency benefits accrue to airlines. The principal measurement problem is that available occupation and technology evidence covers broader airport populations than the six-digit LMM lens.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3355 | — | OBSERVED | — |
| n | — | 264 | — | ESTIMATE | — |
| a | 0.2 | 0.32 | 0.45 | PROXY | S3, S4, S5, S8 |
| rho | 0.25 | 0.45 | 0.65 | PROXY | S5, S6, S7, S8 |
| e | 0.4 | 0.6 | 0.75 | ESTIMATE | S1, S2 |
| s5 | 0.05 | 0.1 | 0.2 | PROXY | S11 |
| q | 0.25 | 0.45 | 0.65 | PROXY | S9, S5 |
| d5 | 0.93 | 1.09 | 1.18 | PROXY | S10 |
| o | 0.68 | 0.84 | 0.94 | PROXY | S4, S5, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.67 | 1.93 | 3.93 | PROXY |
| F | 2.96 | 4.54 | 5.96 | ESTIMATE |
| C | 5.00 | 9.00 | 10.00 | PROXY |
| D | 6.32 | 9.16 | 10.00 | PROXY |

## Caveats
- a: No published source supplies a six-digit, wage-weighted AI-exposure measure for this heterogeneous code.
- a: The broader 4881 occupation mix includes aircraft maintenance and air traffic control, which the lens excludes.
- a: The frozen compensation ratio uses 2024 wages over 2022 receipts and a cross-code harmonization adjustment.
- rho: Published adoption figures are airport-level and not specific to LMM outsourced operators.
- rho: A reported delay reduction is not the same as a labor reduction.
- rho: Cybersecurity, system interoperability, labor agreements, and airport permits may delay use.
- e: NAICS classification is unusually heterogeneous and establishment self-classification may differ by site.
- e: The frozen firm count is margin-bridged at ESTIMATE quality and may misplace asset-heavy operators around the EBITDA band.
- e: Eligibility may vary materially between commercial-airport handlers and general-aviation FBOs.
- s5: The Census acquisition statistic spans all employer industries and is not a longitudinal transfer rate.
- s5: Owner retirement, family succession, and corporate divestiture have different probabilities of producing an acquirable control stake.
- s5: Airport leases and airline contracts may require consent or rebidding after a change of control.
- q: Commercial handling, FBO, de-icing, and airport-management contracts have different billing structures.
- q: The IATA template is global and common but not mandatory.
- q: Volume growth, service penalties, and equipment capital costs are separate from retention of an implemented gross benefit.
- d5: National aviation growth may concentrate at hubs outside the target firms' footprints.
- d5: Passenger, cargo, general-aviation, and weather-service demand do not grow at the same rate.
- d5: The FAA forecast assumes adequate infrastructure and is exposed to macroeconomic, fuel-price, and geopolitical shocks.
- o: The GAO worker population includes some airport-service occupations outside the narrowed NAICS lens.
- o: Airline self-handling can remove outsourced demand while leaving the underlying service quantity intact.
- o: Operator-required does not necessarily mean the same local staffing level if remote coordination and autonomous equipment expand.

## Sources
- **S1** — [North American Industry Classification System — Sector 48-49 Archive](https://www.census.gov/naics/resources/archives/sect48-49.html) (accessed 2026-07-22): Census defines 488119 as operating airports or public flying fields and supporting airport operations through hangar rental and baggage or cargo handling, establishing the code's heterogeneous boundary.
- **S2** — [NAPCS Product List for NAICS 4881: Support Services for Air Transportation](https://www2.census.gov/library/reference/napcs/product-list/web-4881-final-reformatted-edited-us082208.pdf) (accessed 2026-07-22): Census product definitions enumerate airport/FBO services, ramp services, baggage handling, de-icing, runway clearing, ground direction, aircraft parking, administration, and facility access.
- **S3** — [A look at jobs related to air transportation for National Aviation Week](https://www.bls.gov/opub/ted/2023/a-look-at-jobs-related-to-air-transportation-for-national-aviation-week.htm) (accessed 2026-07-22): BLS reports 225,880 support-activities-for-air-transportation jobs in May 2022 and identifies large occupations including mechanics, hand material movers, aircraft service attendants, customer service, cargo agents, supervisors, and airfield operations specialists.
- **S4** — [O*NET — Baggage Porters and Bellhops](https://www.onetonline.org/link/details/39-6011.00) (accessed 2026-07-22): O*NET describes baggage marking, physical luggage transfer, traveler information, disability assistance, records, billing, security participation, equipment operation, inspection, and decision tasks.
- **S5** — [IATA — Ground Ops of the Future](https://www.iata.org/en/programs/ops-infra/ground-operations/ground-ops-of-the-future/) (accessed 2026-07-22): IATA says AI can synchronize turnaround communications, recognize objects and vehicles, capture service timing, and improve decisions; it expects timestamp-standard adoption to reduce ground-handling delays by up to 5% globally.
- **S6** — [SITA Air Transport IT Insights 2025 — Airports](https://www.sita.aero/resources/surveys-reports/air-transport-it-insights-2025/airports/) (accessed 2026-07-22): SITA reports 73% of airports investing in AI for prediction and automation, with uses in passenger flow and turnaround, while cross-system coordination remains limited.
- **S7** — [Automation in aviation and hospitality](https://www.deloitte.com/us/en/insights/industry/transportation/technology-automation-in-aviation-hospitality-workforce.html) (accessed 2026-07-22): Deloitte reports airport labor shortages, AI use in recruiting, service reductions from staffing challenges, and an expectation that alternative labor sources rise from 17% of airport payroll in 2023 to 38% in 2030.
- **S8** — [Aviation Workforce: Contributions and Characteristics of Selected Airport Workers](https://files.gao.gov/reports/GAO-25-107678/index.html) (accessed 2026-07-22): GAO documents physical baggage and cargo handling, equipment operation, hazard detection, disability assistance, safety response, and security vigilance performed by private airport service workers.
- **S9** — [IATA Standard Ground Handling Agreement and 2023 Update](https://www.iata.org/en/publications/newsletters/iata-knowledge-hub/what-is-the-iata-standard-ground-handling-agreement-sgha-and-what-has-changed-in-the-latest-edition/) (accessed 2026-07-22): IATA describes the common industry contract template covering scope, negotiated charges, service standards, duration, modification, and termination, including charge-adjustment rights for frequency, minimum wage, and process changes.
- **S10** — [FAA Aerospace Forecast Fiscal Years 2026–2046](https://www.faa.gov/data_research/aviation/aerospace_forecasts/FY_2026-2046_Full_Forecast_Document_Tables.pdf) (accessed 2026-07-22): FAA forecasts controlled-airport operations rising from 58.635 million in 2026 to 62.152 million in 2031 and system enplanements rising from 998 million to 1.131 billion over the same period.
- **S11** — [Money and Being Your Own Boss Are Top Motivators for Owning a Business](https://www.census.gov/library/stories/2025/08/business-ownership.html) (accessed 2026-07-22): Census reports that 1.3% of respondent employer businesses were acquired in 2022, a cross-industry ownership-incidence proxy.
