# 332813 — Electroplating, Plating, Polishing, Anodizing, and Coloring

*v5.1 Stage 1 research memo. Run `332813-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.48 · L 2.79 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High labor intensity and repeat qualified job-shop workflows create a meaningful AI-addressable operating surface.
**Weakness:** Environmental liabilities and a long decline in domestic real output can overwhelm workflow gains.

## Business-model lens
- Included: US lower-middle-market job shops repeatedly electroplating, plating, anodizing, coloring, buffing, polishing, cleaning, pickling, tumbling, or blasting customer-owned metal and other products for the trade.
- Excluded: Captive finishing departments, firms fabricating and finishing only their own products, metal-coating services classified in 332812, jewelry-only shops, equipment and chemistry suppliers, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring job-shop and production-program revenue billed per piece, square foot, pound, rack, barrel, batch, or quoted program, with charges for masking, pretreatment, plating metal, thickness, testing, certificates, packaging, and expedite service.
- Deviation from default lens: none

## Executive view
Electroplating and allied finishing closely fits the outsourced-service lens and has a large independent-firm base with meaningful labor intensity. AI can improve quotes, scheduling, chemistry and quality review, compliance records, and maintenance, while approved processes and failure risk support retention; environmental exposure and declining real output are substantial counterweights.

## How AI changes the work
Strong applications include drawing and specification parsing, quote and routing generation, rack and bath scheduling, chemistry trend monitoring, certificate drafting, environmental reporting, anomaly triage, maintenance knowledge, and customer updates. Masking, racking, tank operation, polishing, blasting, testing, cleaning, rework, and waste treatment remain physical.

## Value capture
Qualified chemistry, thickness consistency, audit history, freight, turnaround, and failure risk make switching costly. Standard jobs remain competitively bid, and metal surcharges plus annual productivity reviews share efficiency gains.

## Firm availability
The definition's for-the-trade orientation makes most standalone LMM firms eligible, and the estimated population is large. Succession can create deal flow, but environmental liabilities, permits, customer approvals, and owner dependence materially affect transferability.

## Demand durability
Functional and decorative finishing remains physically required, but direct real output was 89.026 in 2023 versus 100 in 2017 after an 8.2% annual decline. Stable employment in 2025 prevents assuming continued steep collapse, but a modestly declining base is prudent.

## Risks and uncertainty
Key risks are wastewater and site liabilities, PFAS and chromium regulation, worker exposure, customer concentration, offshoring, reject and rework costs, chemistry and metal prices, aging equipment, owner dependence, process substitution, and stale direct real-output data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4103 | — | OBSERVED | — |
| n | — | 650 | — | ESTIMATE | — |
| a | 0.21 | 0.34 | 0.47 | PROXY | S2, S3, S4, S5 |
| rho | 0.31 | 0.5 | 0.67 | ESTIMATE | S3, S4, S5, S6 |
| e | 0.76 | 0.9 | 0.97 | ESTIMATE | S1 |
| s5 | 0.14 | 0.28 | 0.42 | PROXY | S7 |
| q | 0.39 | 0.59 | 0.76 | ESTIMATE | S3, S5, S6 |
| d5 | 0.74 | 0.93 | 1.12 | PROXY | S8, S9, S10 |
| o | 0.88 | 0.96 | 0.99 | ESTIMATE | S1, S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.07 | 2.79 | 5.17 | ESTIMATE |
| F | 6.84 | 8.21 | 8.98 | ESTIMATE |
| C | 7.80 | 10.00 | 10.00 | ESTIMATE |
| D | 6.51 | 8.93 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation data include captive operations outside the outsourced industry.
- a: Process mix causes wide dispersion between automated lines and manual masking, polishing, or specialty-repair work.
- rho: No public study directly measures five-year AI implementation in electroplating job shops.
- rho: Regulated aerospace and medical programs should implement more slowly than low-criticality decorative work.
- e: Industry classification does not prove revenue recurrence, profitability band, or transferability.
- e: Some firms combine qualifying plating with nonqualifying fabrication, retail, or restoration activity.
- s5: The owner-age proxy is not industry- or size-specific and measures owners rather than exits.
- s5: Corporate, cooperative, and sponsor-owned firms have no individual-owner retirement trigger.
- q: No public customer-contract sample was available.
- q: Capture is stronger for qualified hard chrome, aerospace, and medical programs than for standard decorative or commodity finishes.
- d5: The latest direct real-output observation is 2023.
- d5: The aggregate mixes decorative, functional, repair, polishing, anodizing, and blasting services with different trajectories.
- o: Necessary processing can consolidate into larger or offshore providers even if an accountable operator remains required.
- o: Labor automation is captured in a and rho and not deducted again here.

## Sources
- **S1** — [NAICS definition: 332813 Electroplating, Plating, Polishing, Anodizing, and Coloring](https://www.census.gov/naics/?chart=2017&details=332813&input=332813) (accessed 2026-07-22): Defines electroplating, plating, anodizing, coloring, buffing, polishing, cleaning, sandblasting, pickling, tumbling, and related work for the trade.
- **S2** — [Metal and Plastic Machine Workers](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-22): Reports 31,700 plating-machine operators in 2024 and projects 27,400 in 2034, a 14% rounded decline.
- **S3** — [Electroplating Effluent Guidelines](https://www.epa.gov/eg/electroplating-effluent-guidelines) (accessed 2026-07-22): Defines electrodeposition purposes, identifies regulated metals and cyanide in wastewater, and describes current PFAS rulemaking for chrome finishing facilities.
- **S4** — [Controlling Hexavalent Chromium Exposures during Electroplating](https://www.osha.gov/sites/default/files/publications/OSHA_FS-3648_Electroplating.pdf) (accessed 2026-07-22): Describes electroplating through electrical current and electrolyte solution, severe chromium health effects, and the 5 micrograms per cubic meter eight-hour exposure limit.
- **S5** — [OSHA 1926.57 Ventilation](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.57) (accessed 2026-07-22): Describes ventilation and physical immersion-tank operations including electroplating, anodizing, pickling, cleaning, rinsing, and drying.
- **S6** — [Metal Finishing Effluent Guidelines regulations and support documents](https://www.epa.gov/eg/metal-finishing-effluent-guidelines-regulations-and-support-documents) (accessed 2026-07-22): Documents industry processes, generated pollutants, treatment technologies, regulatory technical basis, and compliance costs for electroplating and metal finishing.
- **S7** — [Business Owners' Ages: Over Half of U.S. Business Owners Were Age 55 and Over](https://www.census.gov/library/visualizations/2020/comm/business-owners-ages.html) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 ABS, data year 2018.
- **S8** — [Real Sectoral Output for NAICS 332813](https://fred.stlouisfed.org/data/IPUEN332813T010000000) (accessed 2026-07-22): Provides direct industry real-output index values, including 104.015 in 2019, 96.938 in 2022, and 89.026 in 2023.
- **S9** — [Real Sectoral Output Change for NAICS 332813](https://fred.stlouisfed.org/data/IPUEN332813T011000000) (accessed 2026-07-22): Reports direct industry annual real-output changes, including 7.6% in 2021, 0.3% in 2022, and negative 8.2% in 2023.
- **S10** — [Employment for NAICS 332813](https://fred.stlouisfed.org/data/IPUEN332813W200000000) (accessed 2026-07-22): Reports direct industry employment of 60,800 in 2019, 52,600 in 2023, 51,900 in 2024, and 52,600 in 2025.
