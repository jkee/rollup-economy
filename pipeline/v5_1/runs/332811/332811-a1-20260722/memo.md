# 332811 — Metal Heat Treating

*v5.1 Stage 1 research memo. Run `332811-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.99 · L 1.70 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Qualification, traceability, and failure risk make repeat outsourced heat-treatment relationships durable and partially defensible.
**Weakness:** AI cannot remove the physical furnace and quality-accountability core, while recent broader industry output has been weak.

## Business-model lens
- Included: US lower-middle-market commercial heat treaters repeatedly annealing, tempering, hardening, brazing, shot peening, or cryogenically treating customer-owned metals and metal products for the trade.
- Excluded: Captive in-house heat-treat departments, firms that both fabricate and heat treat their own products under another manufacturing code, equipment sellers, laboratories without production treatment, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring job-shop and program work billed per pound, piece, batch, furnace cycle, or quoted part program, often with customer process specifications, certifications, inspection records, minimum-lot charges, and expedite fees.
- Deviation from default lens: none

## Executive view
Metal heat treating closely fits the recurring outsourced-service lens and combines a sizable independent-firm population with qualification-based switching costs. AI can improve quoting, scheduling, records, quality review, and maintenance, but physical furnace work and safety-critical release remain operator-bound.

## How AI changes the work
High-value uses include specification parsing, quote preparation, furnace-load scheduling, routing, certificate drafting, pyrometry and batch-record review, anomaly triage, maintenance knowledge, and customer status communication. Loading, fixturing, testing, repairs, and metallurgical accountability remain human and equipment work.

## Value capture
Validated recipes, approvals, audit history, turnaround, and failure risk support retention. Competitive job quoting and annual procurement reviews still share efficiency gains, especially for standard industrial cycles.

## Firm availability
The NAICS definition itself says work is performed for the trade, so most standalone LMM firms fit the service lens. Succession pressure is plausible in mature job shops, although approvals, customer relationships, and skilled personnel must survive a transfer.

## Demand durability
Recent broader coating and heat-treat output has been weak, but critical metal parts still require controlled thermal processing and aerospace fleet growth supports an important end market. The five-year base is modest growth rather than extrapolation of either the recent decline or the long-range aviation forecast.

## Risks and uncertainty
Material risks are end-market cyclicality, energy costs, furnace utilization, customer concentration, audit and certification failures, metallurgical errors, environmental and safety exposure, skilled-labor scarcity, customer insourcing, and lack of six-digit task and demand data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2585 | — | OBSERVED | — |
| n | — | 214 | — | ESTIMATE | — |
| a | 0.2 | 0.31 | 0.43 | PROXY | S2, S3, S4 |
| rho | 0.34 | 0.53 | 0.69 | ESTIMATE | S5, S6, S7 |
| e | 0.75 | 0.88 | 0.96 | ESTIMATE | S1 |
| s5 | 0.14 | 0.27 | 0.4 | PROXY | S8 |
| q | 0.42 | 0.62 | 0.78 | ESTIMATE | S5, S6 |
| d5 | 0.86 | 1.02 | 1.2 | PROXY | S9, S10, S11 |
| o | 0.91 | 0.97 | 1 | ESTIMATE | S1, S5, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.70 | 1.70 | 3.07 | ESTIMATE |
| F | 5.08 | 6.35 | 7.11 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.83 | 9.89 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation statistics cover heat treatment in captive manufacturers as well as independent trade shops.
- a: The broader 33281 occupation data also include coating and allied activities, not only 332811.
- rho: No source directly measures five-year AI implementation in commercial heat treating.
- rho: Aerospace and medical work will implement more slowly than low-criticality industrial batches.
- e: Industry classification does not prove LMM profitability, recurrence, or control transferability.
- e: Some establishments may be misclassified or combine heat treating with fabrication.
- s5: The proxy covers all employer-business owners, not heat treaters or the LMM band.
- s5: It measures age rather than sale intent or transaction completion.
- q: No public contract set was available.
- q: Capture varies sharply between tightly qualified aerospace work and commoditized industrial loads.
- d5: The production and output series are broader than NAICS 332811.
- d5: FAA fleet growth is only one end-market proxy and may not translate proportionally to domestic outsourced heat-treatment volume.
- o: The accountable operator may consolidate into larger networks even when the physical process remains necessary.
- o: Labor automation is reflected in a and rho and is not deducted again here.

## Sources
- **S1** — [2022 NAICS definition: 332811 Metal Heat Treating](https://www.census.gov/naics/?details=332811&input=332811&year=2022) (accessed 2026-07-22): Defines the industry as annealing, tempering, brazing, cryogenic treatment, hardening, and related heat treatment of metals and metal products for the trade.
- **S2** — [Metal and Plastic Machine Workers](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-22): Defines heat-treating equipment operator duties, reports 14,800 workers in 2024, and describes physical equipment and safety requirements.
- **S3** — [Heat Treating Equipment Setters, Operators, and Tenders, May 2023](https://www.bls.gov/oes/2023/May/oes514191.htm) (accessed 2026-07-22): Reports 4,010 heat-treating equipment operators in broader coating, engraving, heat treating, and allied activities and describes the occupation's industry profile.
- **S4** — [Occupational projections and worker characteristics](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Projects heat-treating equipment operators from 14,800 in 2024 to 12,900 in 2034, a 12.8% decline, with moderate-term on-the-job training.
- **S5** — [SAE AMS2750G Pyrometry](https://saemobilus.sae.org/standards/ams2750g-pyrometry) (accessed 2026-07-22): Specifies temperature sensors, instrumentation, thermal equipment, system-accuracy tests, and temperature-uniformity surveys necessary for compliant heat treatment.
- **S6** — [14 CFR 23.2260 Materials and processes](https://www.law.cornell.edu/cfr/text/14/23.2260) (accessed 2026-07-22): Requires fabrication processes to produce consistently sound aircraft structures and close-control processes to follow approved process specifications.
- **S7** — [FAA Lessons Learned: Convair 340 heat-treatment quality control](https://www.faa.gov/lessons_learned/transport_airplane/accidents/N73130) (accessed 2026-07-22): Documents catastrophic risk from omitted nitriding and concludes that quality controls must ensure completion of necessary manufacturing processes.
- **S8** — [Business Owners' Ages: Over Half of U.S. Business Owners Were Age 55 and Over](https://www.census.gov/library/visualizations/2020/comm/business-owners-ages.html) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 ABS, data year 2018.
- **S9** — [Industrial Production: Coating, Engraving, Heat Treating, and Allied Activities](https://fred.stlouisfed.org/data/IPN3328SQ) (accessed 2026-07-22): Provides quarterly real-output index values for broader NAICS 3328, including 108.4628 in 2021 Q3, 86.7257 in 2024 Q4, and subsequent recovery.
- **S10** — [Sectoral Output for NAICS 33281](https://fred.stlouisfed.org/data/IPUEN33281T301000000) (accessed 2026-07-22): Reports annual sectoral-output changes for broader NAICS 33281, including declines of 1.7% in 2023 and 3.7% in 2024.
- **S11** — [FAA Aerospace Forecast Fiscal Years 2026–2046](https://www.faa.gov/data_research/aviation/aerospace_forecasts/2026_FAA_Aerospace_Forecasts_FY2026-2046-2.pdf) (accessed 2026-07-22): Forecasts the US commercial aircraft fleet to grow from 6,949 in 2025 to 10,677 in 2046, averaging 2.1% annually.
