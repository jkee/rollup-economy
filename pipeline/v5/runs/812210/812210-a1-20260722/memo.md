# 812210 — Funeral Homes and Funeral Services

*v5 Stage 1 research memo. Run `812210-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.33 · L 2.37 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A non-discretionary death-care need still requires trusted local coordination, documentation, and accountable physical execution.
**Weakness:** Cremation-led mix shift and transparent itemized pricing can compress the value of the current service basket and share operational gains with customers.

## Business-model lens
- Included: Independent lower-middle-market funeral homes and funeral-service operators providing arrangements, removal and preparation coordination, ceremonies, disposition coordination, pre-need planning, and related merchandise or facilities to external families.
- Excluded: Captive cemetery or hospital units, stand-alone software vendors, non-control financing vehicles, and firms outside the roughly $1–10M normalized EBITDA band.
- Customer and revenue model: Families buy a time-sensitive, episodic service at need or pre-need; revenue is generally an itemized or package charge for professional services, facilities, transportation, preparation, disposition coordination, and optional merchandise.
- Deviation from default lens: none

## Executive view
Funeral service combines a durable, death-triggered need with operator-intensive local execution. The practical AI opportunity is in administrative and coordination capacity, not substitution for the licensed and emotionally sensitive core of the service.

## How AI changes the work
Directors and managers handle documentation, scheduling, communication, marketing, records, and coordination alongside counseling, body handling, transport, ceremonies, and compliance. AI can compress the former set, but rapid service windows, accuracy requirements, and family trust make human review and local operators central.

## Value capture
Itemized GPL pricing and increasingly online comparison create pressure to share some operational gains. A retained benefit remains plausible for differentiated operators, yet standardized direct-cremation packages and transparent prices limit the case for full retention.

## Firm availability
The sector has observable independent-business transactions and a high self-employment share among funeral-home managers. There is no direct dataset for five-year control transfers among $1–10M EBITDA firms, so availability remains a wide estimate requiring broker and licensing-file diligence.

## Demand durability
Deaths are projected to increase after the post-pandemic decline, supporting the need for death-care services. However, cremation and direct cremation shift spend and labor away from the traditional casketed-funeral basket, leaving real demand for that current basket roughly flat in the central case.

## Risks and uncertainty
The main uncertainties are task-level labor allocation, ownership succession, local price competition, state regulation, and the pace at which consumer preference moves to direct cremation or nontraditional events. National projections and marketplace transactions are useful context but are not LMM-firm measurements.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.326 | — | OBSERVED | — |
| n | — | 40 | — | ESTIMATE | — |
| a | 0.22 | 0.35 | 0.48 | ESTIMATE | S1, S2 |
| rho | 0.35 | 0.52 | 0.65 | ESTIMATE | S1, S2, S3 |
| e | 0.65 | 0.8 | 0.92 | ESTIMATE | S1, S5 |
| s5 | 0.12 | 0.25 | 0.42 | ESTIMATE | S1, S5 |
| q | 0.55 | 0.68 | 0.8 | ESTIMATE | S3, S4 |
| d5 | 0.95 | 1.01 | 1.07 | ESTIMATE | S3, S6 |
| o | 0.86 | 0.93 | 0.98 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.00 | 2.37 | 4.07 | ESTIMATE |
| F | 2.28 | 3.53 | 4.51 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.17 | 9.39 | 10.00 | ESTIMATE |

## Caveats
- a: No source measures AI-exposed task hours or compensation for NAICS 812210 directly.
- a: Occupation descriptions cover funeral service workers nationally and include work outside the LMM-firm lens.
- rho: Implementation rate is a five-year judgment, not an observed adoption statistic.
- rho: State licensing, electronic-filing, and privacy requirements differ materially.
- e: The frozen LMM firm count is an estimate and is not independently recomputed here.
- e: BizBuySell describes listed and sold businesses, not the full NAICS population.
- s5: BizBuySell completed-sales data are a selected marketplace sample and its reported earnings are generally below the frozen EBITDA band.
- s5: Self-employment of managers is not equivalent to owner age or a sale probability.
- q: No source directly measures AI-savings pass-through in funeral services.
- q: Retention varies with local concentration, pre-need obligations, and the mix of merchandise versus services.
- d5: Death counts are not a one-for-one measure of demand for the current funeral-home basket.
- d5: NFDA's revenue projection is nominal and incorporates third-party IBISWorld analysis, so it is not used as a direct real-volume observation.
- o: The source documents duties and licensing but does not measure the future operator-required share.
- o: Operator necessity varies by state and by whether the firm owns a crematory.

## Sources
- **S1** — [Funeral Service Workers: Occupational Outlook Handbook](https://www.bls.gov/ooh/personal-care-and-service/funeral-service-occupations.htm) (accessed 2026-07-22): BLS reports 59,600 funeral-service-worker jobs in 2024, 4% projected employment growth from 2024 to 2034, 56% self-employment among funeral-home managers, duties including legal documents and arrangement coordination, 24–72-hour service timing, and state licensing/training requirements.
- **S2** — [O*NET OnLine: Morticians, Undertakers, and Funeral Arrangers](https://www.onetonline.org/link/summary/39-4031.00) (accessed 2026-07-22): O*NET lists administrative, scheduling, financial-record, body-handling, transport, counseling, and service-execution tasks; it also reports that 77% of respondents have constant contact with others and documents training requirements.
- **S3** — [2024 NFDA Cremation and Burial Report](https://nfda.org/Portals/0/2024_NFDA_Cremation%20and%20Burial%20Report.pdf) (accessed 2026-07-22): NFDA projects total deaths from 2,984,650 in 2025 to 3,236,200 in 2030, reports rising cremation and declining burial, forecasts 1.2% annual funeral-home revenue growth through 2029, documents online arrangements and GPL effects, and states that cremation generally generates less revenue than burial.
- **S4** — [Complying with the Funeral Rule](https://www.ftc.gov/business-guidance/resources/complying-funeral-rule) (accessed 2026-07-22): The FTC requires a General Price List when price, service type, or specific goods/services are discussed, and requires retail prices for listed items to reflect prices actually charged.
- **S5** — [Funeral Home & Mortuary Business Valuation Multiples & Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/funeral-home/) (accessed 2026-07-22): BizBuySell describes independently owned funeral and mortuary businesses and reports completed-business-sale comparables from 2021 through 2025, including a $1.5M median sale price, $750,000 median revenue, and $318,000 median owner earnings.
- **S6** — [Mortality in the United States: Provisional Data, 2025](https://www.cdc.gov/nchs/data/vsrr/vsrr044.pdf) (accessed 2026-07-22): NCHS reports 3,094,593 U.S. deaths in 2025, based on more than 99% of 2025 death records processed as of May 10, 2026, and notes that the 2025 count is provisional.
