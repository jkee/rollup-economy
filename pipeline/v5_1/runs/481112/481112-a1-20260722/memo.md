# 481112 — Scheduled Freight Air Transportation

*v5.1 Stage 1 research memo. Run `481112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.14 · L 0.97 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digitally structured cargo data and recurring network operations create a practical AI surface while physical transport still needs a certificated operator.
**Weakness:** Anchor-customer concentration and reimbursement-style contracts sharply constrain transferability and retained economics.

## Business-model lens
- Included: US lower-middle-market certificated carriers that repeatedly operate scheduled freight routes for shippers, logistics networks, integrators or public-sector customers, including independent feeder airlines under recurring service agreements.
- Excluded: Passenger-only airlines, nonscheduled charter cargo flying, freight forwarders without air-carrier operations, ground handling and MRO-only businesses, captive internal flight departments, dormant certificate shells and financing vehicles.
- Customer and revenue model: Revenue comes from scheduled air-freight charges or recurring capacity, dry-lease and feeder-service contracts; some contracts reimburse specified direct operating costs and pay aircraft- or route-linked administrative compensation.
- Deviation from default lens: none

## Executive view
Scheduled freight aviation has a meaningful information-work opportunity because shipment data, compliance records, routing and exceptions are increasingly digital. The physical operation remains regulated and labor-intensive, while feeder economics are often concentrated in powerful customers that can pass through costs and capture savings.

## How AI changes the work
AI can accelerate cargo-document validation, booking, tracking, customs and dangerous-goods checks, irregular-operations triage, maintenance planning and administrative work. Piloting, loading, inspections, repairs and final operational accountability remain largely outside substitution over five years.

## Value capture
Direct-to-shipper carriers face competing modes and other airlines; feeder carriers may operate under reimbursement and aircraft-linked fee contracts with short reduction rights. Savings can improve reliability and protect margins, but customers are positioned to reprice or reduce capacity.

## Firm availability
Some independent feeder operators clearly fit the recurring-service lens, yet the apparent 25-firm pool needs verification for active schedules, independence and standalone EBITDA. A viable acquisition must transfer both regulatory capability and an anchor contract that may itself be terminable.

## Demand durability
FAA projects moderate domestic air-cargo growth and all-cargo aircraft dominate domestic RTMs. Demand is derived from economic activity and exposed to trade, fuel, real yields, e-commerce patterns and substitution by ground or ocean modes.

## Risks and uncertainty
Principal uncertainties are the true eligible firm population, existing automation, integrator concentration and the share of savings retained under customer contracts. Cyber failures, safety incidents, pilot costs and contract termination could overwhelm incremental productivity gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1741 | — | OBSERVED | — |
| n | — | 25 | — | ESTIMATE | — |
| a | 0.16 | 0.25 | 0.36 | PROXY | S1, S2 |
| rho | 0.34 | 0.56 | 0.72 | ESTIMATE | S3, S4, S5 |
| e | 0.32 | 0.52 | 0.7 | ESTIMATE | S5, S6, S7 |
| s5 | 0.09 | 0.19 | 0.32 | ESTIMATE | S8, S9 |
| q | 0.22 | 0.38 | 0.57 | PROXY | S5, S10 |
| d5 | 0.93 | 1.11 | 1.22 | PROXY | S10, S11 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.38 | 0.97 | 1.81 | ESTIMATE |
| F | 0.87 | 2.00 | 3.04 | ESTIMATE |
| C | 4.40 | 7.60 | 10.00 | PROXY |
| D | 8.84 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS scheduled-air-transportation occupation mix is dominated by passenger carriers.
- a: IATA adoption figures are global and weighted toward air-waybill volume, not small US operators.
- a: The estimate is for not-yet-automated tasks and therefore discounts existing e-AWB and rules-based automation.
- rho: ONE Record readiness is not a direct measure of generative-AI implementation.
- rho: Small carriers may depend on an integrator's systems and permission to change workflows.
- rho: Safety-critical deployment has a higher assurance burden than administrative deployment.
- e: The injected firm count is an ESTIMATE based on size classes and an industry margin, not a verified list of 25 scheduled cargo carriers.
- e: FAA all-cargo reporting includes foreign, scheduled and nonscheduled carriers beyond the lens.
- e: A subsidiary may be operationally coherent but unavailable as a standalone control acquisition.
- s5: The direct carrier acquisition is from 2014 and market structure has since changed.
- s5: Broad small-business transaction data are not representative of regulated airlines.
- s5: Customer consent or termination rights may prevent a nominal equity sale from transferring durable cash flow.
- q: One public parent's FedEx feeder contracts may not represent direct shipper pricing.
- q: Cost reimbursement can protect downside while also preventing retention of savings on reimbursed lines.
- q: This primitive excludes volume loss and implementation failure.
- d5: Revenue ton miles combine quantity and route length and are an imperfect constant-quality service measure.
- d5: The FAA forecast is systemwide rather than LMM-carrier-specific.
- d5: Trade restrictions, recession, fuel shocks and shifts to ground transport can sharply change demand.
- o: Automation can eliminate pieces of the current service basket while leaving the carrier accountable.
- o: Small unmanned cargo aircraft may emerge first on thin routes but face certification and integration barriers.
- o: The estimate refers to operator-required transport quantity, not paperwork or booking contacts.

## Sources
- **S1** — [Data tables for OEWS occupation-industry charts, May 2024](https://www.bls.gov/oes/2024/may/occ_ind_emp_chart/occ_ind_emp_chart_data.htm) (accessed 2026-07-22): Reports 9,440 cargo and freight agents employed in scheduled air transportation.
- **S2** — [IATA ONE Record](https://www.iata.org/one-record) (accessed 2026-07-22): States that e-air-waybills are used for more than two out of three shipments and describes standardized shipment data APIs enabling automated digital cargo services.
- **S3** — [IATA Survey Shows Growing Awareness of ONE Record and Areas for Further Support](https://www.iata.org/en/pressroom/2025-releases/2025-12-10-02/) (accessed 2026-07-22): Reports over 70% awareness, nearly 50% readiness and more than 30 active ONE Record pilots among surveyed cargo participants.
- **S4** — [Technical Discipline: Artificial Intelligence – Machine Learning](https://www.faa.gov/aircraft/air_cert/step/disciplines/artificial_intelligence) (accessed 2026-07-22): FAA explains that aviation AI/ML functionality and performance must be evaluated within the certification framework to assure safety.
- **S5** — [Air T, Inc. 2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/353184/000035318426000054/airt-20260331.htm) (accessed 2026-07-22): Describes two US overnight feeder airlines, their long FedEx relationship, cost reimbursement without markup, rapid customer termination and aircraft-reduction rights, and LMM-sized carrier EBITDA.
- **S6** — [Cargo Carriers for Reporting Cargo Data to the FAA, CY 2025](https://www.faa.gov/airports/planning_capacity/passenger_allcargo_stats/reporting/all_cargo_carriers_codes) (accessed 2026-07-22): Provides the current FAA reporting roster and illustrates that the all-cargo carrier universe contains many US and foreign operator types requiring lens-level cleaning.
- **S7** — [Regularly Scheduled Air Carriers (Part 121)](https://www.faa.gov/hazmat/air_carriers/operations/part_121) (accessed 2026-07-22): States that Part 121 certificate holders include all-cargo operators and requires approved hazardous-materials programs and employee training.
- **S8** — [Ameriflight LLC Acquires Wiggins Airways](https://w3.ameriflight.com/ameriflight-acquires-wiggins-airways/) (accessed 2026-07-22): Documents the closed acquisition of a US regional overnight air-cargo carrier, direct evidence that control transfer can occur.
- **S9** — [2025 Year in Review: BizBuySell Market Recap](https://www.bizbuysell.com/blog/2025-year-in-review/) (accessed 2026-07-22): Reports 9,586 US small-business transactions in 2025; used only as broad transaction-market context, not an airline rate.
- **S10** — [FAA Aerospace Forecast Fiscal Years 2026–2046](https://www.faa.gov/data_research/aviation/aerospace_forecasts/FY_2026-2046_Full_Forecast_Document_Tables.pdf) (accessed 2026-07-22): Forecasts domestic cargo RTMs to grow 2.1% annually from 2026 to 2046, reports all-cargo carriers at 93.3% of 2025 domestic cargo RTMs and describes competition from alternative modes.
- **S11** — [UPS to become the primary air cargo provider for the United States Postal Service](https://apnews.com/article/ee49f99d9b74635831e75478036b5f93) (accessed 2026-07-22): Reports a minimum five-and-a-half-year USPS air-cargo contract with UPS and the displacement of FedEx, illustrating durable contracted demand and renewal displacement risk.
