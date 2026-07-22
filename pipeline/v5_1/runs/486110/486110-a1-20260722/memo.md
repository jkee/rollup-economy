# 486110 — Pipeline Transportation of Crude Oil

*v5.1 Stage 1 research memo. Run `486110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.29 · L 0.74 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Data-rich regulated operations support AI-assisted monitoring, integrity analysis, maintenance planning, and compliance while indexed rate ceilings can preserve savings.
**Weakness:** Only a handful of estimated LMM firms exist, many may be captive or nontransferable, and physical safety obligations sharply limit labor substitution.

## Business-model lens
- Included: Private lower-middle-market owners and operators of crude-oil pipeline systems or segments that repeatedly transport crude oil for external shippers under tariffs or transportation contracts.
- Excluded: Captive producer or refiner pipelines without meaningful external customers, passive non-control infrastructure interests, construction contractors, terminal-only businesses outside pipeline transportation, natural-gas and refined-products pipelines, and entities whose operations or permits cannot transfer with control.
- Customer and revenue model: Recurring transportation charges paid by crude producers, marketers, refiners, and other shippers under indexed or otherwise regulated tariffs, negotiated contracts, throughput commitments, and related capacity arrangements.
- Deviation from default lens: none

## Executive view
Crude-oil pipelines are highly automated physical infrastructure with meaningful data, compliance, engineering, and control-room workflows still performed by people. AI can improve analysis and administration, but low labor intensity, strict safety accountability, and a tiny pool of potentially independent LMM operators constrain the opportunity.

## How AI changes the work
AI can prioritize alarms and integrity findings, summarize inspections, identify anomalous trends, improve maintenance planning, draft regulatory documentation, support scheduling and nominations, and accelerate contract or invoice review. Controllers, engineers, integrity managers, and field technicians remain responsible for validation, abnormal conditions, repairs, emergency response, and regulated decisions.

## Value capture
Indexed rate ceilings can allow a pipeline to retain firm-specific operating savings because ceilings move with industry costs rather than immediately resetting to each operator's cost. Negotiated shipper contracts, rate challenges, competitive alternatives, and renewal leverage reduce retention, especially on underutilized systems.

## Firm availability
The frozen universe contains only seven estimated LMM-band firms, and a substantial share may be captive, affiliated, jointly owned, or economically inseparable from one producer or refiner. A viable control transfer requires operating responsibility, external customers, permits, contracts, and integrity obligations to move together.

## Demand durability
Pipeline assets remain essential for transported barrels, but EIA's current outlook points to near-term US crude-production decline in most cases and PHMSA reports recent crude-pipeline mileage contraction. Refinery throughput and exports remain substantial, so aggregate quantity is more likely to decline modestly than disappear, with large basin-level variation.

## Risks and uncertainty
Safety incidents, leaks, cybersecurity events, integrity remediation, environmental liability, shipper concentration, basin decline, regulatory changes, tariff disputes, and stranded capacity can overwhelm administrative savings. Evidence on LMM ownership and transferability is particularly weak. The industry would be unattractive where the pipeline is captive, underutilized, exposed to a single declining shipper, or carries unbounded integrity liabilities.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1889 | — | OBSERVED | — |
| n | — | 7 | — | ESTIMATE | — |
| a | 0.14 | 0.24 | 0.35 | PROXY | S1, S2, S3 |
| rho | 0.28 | 0.48 | 0.65 | PROXY | S2, S3, S8 |
| e | 0.15 | 0.38 | 0.65 | ESTIMATE | S6, S5 |
| s5 | 0.13 | 0.22 | 0.36 | PROXY | S7 |
| q | 0.45 | 0.68 | 0.82 | ESTIMATE | S5 |
| d5 | 0.78 | 0.96 | 1.08 | PROXY | S4, S9 |
| o | 0.985 | 0.995 | 0.999 | ESTIMATE | S2, S8, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.30 | 0.87 | 1.72 | PROXY |
| F | 0.21 | 0.74 | 1.56 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.68 | 9.55 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS occupation categories do not measure AI exposure or current automation.
- a: Some analytical work is already automated by SCADA and computational monitoring and is therefore excluded from not-yet-automated opportunity.
- a: The frozen compensation-to-receipts ratio uses 2024 wages over 2022 receipts and is harmonized to the IPS basis as stated in the assignment.
- rho: Existing computational monitoring is not necessarily AI and may leave less incremental opportunity than greenfield comparisons suggest.
- rho: The source evidence establishes feasibility and constraints, not a measured five-year implementation share.
- rho: A safety incident or cyber event could materially slow deployment.
- e: No source measures lens eligibility among LMM crude-pipeline firms.
- e: NAICS establishments may sit inside larger integrated energy groups and need not correspond to transferable firms.
- e: The frozen count of seven firms is a margin-bridged estimate, not an observed EBITDA-band census.
- s5: Gallup covers employer businesses across industries and sizes rather than pipeline operators.
- s5: Stated owner plans are not completed transfers and include gifts or rare public offerings.
- s5: The tiny eligible population makes the realized five-year proportion highly discrete.
- q: FERC reports that approximately 86% of interstate crude and petroleum-product pipeline rates use indexing, but the target includes intrastate and negotiated arrangements.
- q: Rate ceilings are not necessarily realized rates, particularly where pipelines compete or have spare capacity.
- q: The estimate excludes implementation and demand effects.
- d5: Pipeline mileage is not constant-quality service quantity.
- d5: EIA projections span wide supply cases and are national rather than specific to LMM systems.
- d5: Energy policy, oil prices, drilling productivity, refinery closures, exports, and basin bottlenecks can shift rapidly.
- o: No source directly estimates a five-year operator-required share.
- o: The accountable operator could be consolidated into a larger platform even though the physical service remains operator-required.
- o: Demand destruction is represented in d5 and is not counted again here.

## Sources
- **S1** — [Pipeline Transportation of Crude Oil — May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_486100.htm) (accessed 2026-07-22): Direct industry occupation mix, including production occupations at 28.27%, petroleum pump-system operators/refinery operators/gaugers at 19.20%, transportation/material-moving at 22.53%, maintenance/repair at 7.74%, and business/financial operations at 5.51% of employment.
- **S2** — [Control Room Management](https://www.phmsa.dot.gov/pipeline/control-room-management/control-room-management) (accessed 2026-07-22): PHMSA states that pipeline safety regulations prescribe requirements for controllers, control rooms, and SCADA systems used to remotely monitor and control hazardous-liquid pipelines, including human-factor reliability and abnormal-condition response.
- **S3** — [Fact Sheet: Leak Detection Systems](https://primis-uat.phmsa.dot.gov/stakeholder-comms/factsheets/fsleakdetectionsystems/) (accessed 2026-07-22): Describes electronic leak detection from volume and mass balances to rate-of-change and computational pipeline monitoring, while noting that trained controllers or dispatchers use the systems to locate and isolate leaks.
- **S4** — [Annual Report Mileage for Hazardous Liquid or Carbon Dioxide Systems](https://www.phmsa.dot.gov/data-and-statistics/pipeline/annual-report-mileage-hazardous-liquid-or-carbon-dioxide-systems) (accessed 2026-07-22): Reports US crude-oil pipeline mileage of 81,829 in 2025, down from 83,209 in 2024 and 84,149 in 2023.
- **S5** — [Five-Year Review of the Oil Pipeline Index, Docket RM26-6-000](https://www.ferc.gov/sites/default/files/2026-05/20260424-4000.PDF) (accessed 2026-07-22): Explains indexed price-cap regulation and states that roughly 350 interstate oil pipelines file tariffs and approximately 86% of crude-oil and petroleum-product transportation rates are set under indexing, with negotiated contracts also referencing the index.
- **S6** — [North American Industry Classification System — Sector 48-49](https://www.census.gov/naics/resources/archives/sect48-49.html) (accessed 2026-07-22): Defines NAICS 486110 as establishments primarily engaged in pipeline transportation of crude oil and distinguishes natural-gas and refined-product pipelines.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall-2024 US survey found that 22% of employer-business owners planned to sell or transfer ownership within five years.
- **S8** — [Hazardous Liquid Integrity Management](https://www.phmsa.dot.gov/pipeline/liquified-natural-gas/hazardous-liquid-integrity-management) (accessed 2026-07-22): PHMSA describes operator duties to identify, prioritize, assess, evaluate, repair, and validate integrity for hazardous-liquid pipelines that could affect high-consequence areas.
- **S9** — [Annual Energy Outlook 2026 Narrative](https://www.eia.gov/outlooks/aeo/narrative/index.php) (accessed 2026-07-22): Projects US crude production decreasing through the mid-2030s in nearly all cases; refinery throughput remains above 14.7 million barrels per day in all cases; crude exports remain material, with wide supply-case uncertainty.
