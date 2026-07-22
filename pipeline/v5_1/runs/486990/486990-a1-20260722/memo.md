# 486990 — All Other Pipeline Transportation

*v5.1 Stage 1 research memo. Run `486990-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.65 · L 0.88 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A high labor-to-receipts input and document-heavy technical compliance create a meaningful support-work automation opportunity around durable physical operations.
**Weakness:** Unknown commodity weights and captive ownership make both the eligible firm pool and five-year demand path unusually uncertain.

## Business-model lens
- Included: US lower-middle-market operators providing recurring third-party pipeline transportation of products other than crude oil, refined petroleum products, or natural gas, including carbon dioxide, hydrogen and other industrial gases, anhydrous ammonia, chemicals, coal, and slurry where classified in 486990.
- Excluded: Captive plant-transfer lines without external customers, natural-gas, crude-oil, and refined-products pipelines, construction or maintenance contractors, water and sewer utilities, shells, non-control financing vehicles, and businesses outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: Recurring throughput, capacity, take-or-pay, or dedicated-network contracts with industrial producers and users, refineries, chemical and fertilizer facilities, carbon-capture projects, storage or enhanced-recovery sites, and other commodity shippers; terms and regulatory treatment vary substantially by commodity and corridor.
- Deviation from default lens: none

## Executive view
All Other Pipeline Transportation combines a high frozen labor ratio with recurring physical infrastructure, creating meaningful administrative AI potential, but the code is small and commodity-heterogeneous. The central case depends on finding independent external-customer operators rather than captive plant links and understanding whether each line serves mature ammonia, chemical, or slurry demand or a potentially growing CO2 or hydrogen corridor.

## How AI changes the work
AI can assist scheduling, contract and invoice administration, engineering-document search, integrity-record review, regulatory drafting, work-order triage, customer communication, and finance. Field inspection, pumping or compression, control-room judgment, cybersecurity, materials compatibility, emergency response, and accountable safety management remain operator- and human-dependent.

## Value capture
Long-term fixed, indexed, take-or-pay, or minimum-volume contracts can preserve savings, but anchor-customer leverage and cost-recovery clauses can pass them through. There is no single pricing regime for the code, so contract-level diligence is indispensable.

## Firm availability
Only nine firms are estimated in band before removing captive and integrated systems. Specialized assets may be bound to an anchor facility, and transfers often occur as part of a larger industrial transaction rather than as a standalone eligible business.

## Demand durability
Existing CO2 and hydrogen networks demonstrate durable industrial use, and CCS could expand CO2 transport materially. Permitting opposition and cancellations make that upside uncertain, while ammonia, chemical, coal, and slurry corridors follow different end markets; the resulting five-year range is wider than for single-commodity pipeline codes.

## Risks and uncertainty
The largest uncertainties are the unknown commodity and contract mix, captive ownership, tiny denominator, anchor-customer concentration, project and siting risk, technical differences among gases and liquids, environmental liability, and lack of 486990-specific occupation data. New-project growth should not be assumed to accrue to existing LMM operators.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4349 | — | OBSERVED | — |
| n | — | 9 | — | ESTIMATE | — |
| a | 0.12 | 0.22 | 0.34 | PROXY | S1, S2, S3 |
| rho | 0.28 | 0.45 | 0.62 | PROXY | S2, S3, S5, S6 |
| e | 0.25 | 0.45 | 0.7 | ESTIMATE | S1, S5, S6 |
| s5 | 0.08 | 0.18 | 0.32 | ESTIMATE | S5, S6 |
| q | 0.32 | 0.52 | 0.72 | ESTIMATE | — |
| d5 | 0.86 | 1.06 | 1.35 | PROXY | S1, S5, S6, S7 |
| o | 0.92 | 0.98 | 1 | ESTIMATE | S5, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.58 | 1.72 | 3.67 | PROXY |
| F | 0.27 | 0.88 | 1.78 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.91 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS page covers all pipeline transportation and highlights common occupations rather than a complete 486990 staffing distribution.
- a: Corporate-function AI evidence comes mostly from much larger cross-industry organizations.
- a: The code's commodity heterogeneity and the frozen 2024-wage/2022-receipts vintage mismatch make wage-weighted task inference especially uncertain.
- rho: Adoption evidence is not pipeline-specific and overrepresents large enterprises.
- rho: Safety and technical constraints differ materially among CO2, hydrogen, ammonia, and slurry.
- rho: Implementation refers only to the exposed opportunity and excludes demand, pricing, and valuation effects.
- e: No public source directly enumerates the nine dataset-inferred firms or their external-customer status.
- e: Hydrogen and some chemical lines may be captured differently across regulatory and industry datasets.
- e: The frozen firm count is margin-bridged from size classes and explicitly ESTIMATE.
- s5: There is no observed transfer-rate series for eligible 486990 LMM firms.
- s5: Project cancellations, asset conversions, internal restructurings, and parent-company sales are not automatically qualifying transfers.
- s5: A base eligible pool near four firms makes realized transfer frequency highly lumpy.
- q: No source measures benefit retention or even the contract mix across this heterogeneous code.
- q: A single anchor customer's bargaining power may dominate value capture for a small dedicated line.
- q: The estimate concerns retention after implementation and does not include throughput loss or implementation difficulty.
- d5: CO2-or-other mileage is not equivalent to 486990 revenue or throughput and may omit some hydrogen infrastructure.
- d5: New CCS or hydrogen pipeline construction can expand industry demand but may not benefit the current LMM service basket or existing operators.
- d5: Commodity mix is unknown, so growth in one segment may mask contraction in another.
- o: No dataset directly measures the share of quantity that remains operator-required.
- o: Oversight differs by commodity, location, and interstate status; DOE notes that hydrogen jurisdiction varies accordingly.
- o: Loss of commodity demand belongs in d5, while o addresses whether surviving quantity still needs this kind of operator.

## Sources
- **S1** — [2022 Economic Census Transportation and Warehousing Survey Content for NAICS 486](https://bhs.econ.census.gov/ombpdfs2022/export/2022_TW-48600_su.pdf) (accessed 2026-07-22): Defines 486990 as other pipeline transportation including coal, slurry, and anhydrous ammonia, excluding petroleum-product and natural-gas pipelines; supports lens scope and heterogeneity.
- **S2** — [Pipeline Transportation: NAICS 486](https://www.bls.gov/iag/tgs/iag486.htm) (accessed 2026-07-22): Reports employment in prominent pipeline operator, mechanic, pumping, and valve occupations for the broader subsector; supports a as an occupation-mix proxy.
- **S3** — [Gen AI in corporate functions: Looking beyond efficiency gains](https://www.mckinsey.com/capabilities/operations/our-insights/gen-ai-in-corporate-functions-looking-beyond-efficiency-gains) (accessed 2026-07-22): Reports a 2024 survey of 276 corporate-function leaders, partial-role automation, use cases, barriers, and a three-to-five-year value horizon; supports a and rho by proxy.
- **S4** — [From promising to productive: Real results from gen AI in services](https://www.mckinsey.com/capabilities/operations/our-insights/from-promising-to-productive-real-results-from-gen-ai-in-services) (accessed 2026-07-22): Reports that only 3% of surveyed large-company respondents had scaled an operations-related gen-AI use case in early 2024 and describes governance and change-management constraints; supports rho by proxy.
- **S5** — [Annual Report Mileage for Hazardous Liquid or Carbon Dioxide Systems](https://www.phmsa.dot.gov/data-and-statistics/pipeline/annual-report-mileage-hazardous-liquid-or-carbon-dioxide-systems) (accessed 2026-07-22): Reports 5,321 miles in the CO2-or-other category in 2025 versus 5,345 in 2024 and provides hazardous-liquid system records; supports installed-base durability and operator diligence.
- **S6** — [Hydrogen Pipelines](https://www.energy.gov/cmei/fuels/hydrogen-pipelines) (accessed 2026-07-22): Reports about 1,600 miles of operating US hydrogen pipeline, concentrated around refineries and chemical plants, and describes technical barriers and conversion possibilities; supports d5 and operator requirements.
- **S7** — [Carbon Dioxide (CO2) Pipelines: Safety, Siting, and Eminent Domain](https://www.congress.gov/crs_external_products/IN/PDF/IN12575/IN12575.2.pdf) (accessed 2026-07-22): Reports approximately 5,300 miles of operating US CO2 pipelines, the need for a much larger network for significant CCS deployment, and recent project opposition, permit challenges, and cancellations; supports the wide d5 range.
