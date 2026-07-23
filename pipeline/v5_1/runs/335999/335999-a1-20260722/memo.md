# 335999 — All Other Miscellaneous Electrical Equipment and Component Manufacturing

*v5.1 Stage 1 research memo. Run `335999-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.05 · L 1.18 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Growing power-density, reliability, electrification, and grid-modernization needs for specialized physical electrical apparatus.
**Weakness:** The residual NAICS combines unrelated product and revenue models, so the true outsourced-service target pool is much smaller than the modeled firm count.

## Business-model lens
- Included: Independent U.S. firms providing repeat outsourced engineering and production of specialized power-conversion, power-supply, power-quality, UPS, high-voltage, ultrasonic, and related industrial electrical apparatus for external customers.
- Excluded: Captive plants, commodity extension-cord and appliance-cord production, electric bells and door-opening devices, branded consumer products, one-off development without repeat production, and equipment classified to other electrical or electronic NAICS industries.
- Customer and revenue model: Recurring B2B programs based on customer specifications, qualification, configurable designs, repairable installed products, and repeat purchase orders; revenue comes from engineered units, production runs, spares, upgrades, and associated testing or support.
- Deviation from default lens: Narrowed to repeat outsourced specialized industrial apparatus because this residual NAICS combines materially different products, from cords and bells to UPS systems, converters, accelerators, and ultrasonic equipment, making one service screen incoherent.

## Executive view
335999 offers a sizable but messy target universe. The coherent opportunity is specialized repeat outsourced apparatus production, where engineering and qualification create stickiness; most commodity and proprietary catalog businesses do not fit the lens.

## How AI changes the work
AI can materially improve configuration, quoting, application engineering, technical documentation, purchasing, planning, and support, while certified physical assembly and test remain human- and equipment-dependent.

## Value capture
Fixed-price configured products allow temporary retention of productivity gains, reinforced by faster response and better engineering reuse; rebids, customer bargaining, and transparent commodity content reduce retention.

## Firm availability
The frozen dataset estimates 143 LMM-band firms, but only a minority likely operate repeat outsourced programs. Economy-wide owner aging suggests some succession flow, although the category's diversity makes screening expensive.

## Demand durability
Data-center load, electrification, renewable interconnection, and grid modernization support power-conversion and power-quality equipment. Volatile broader electrical-equipment output and mature residual products temper that demand case.

## Risks and uncertainty
Major risks are poor NAICS coherence, overestimating eligible firms, certification and product-liability exposure, rapid semiconductor integration, customer concentration, imported competition, and acquisitions with incompatible engineering stacks.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2554 | — | OBSERVED | — |
| n | — | 143 | — | ESTIMATE | — |
| a | 0.15 | 0.24 | 0.35 | PROXY | S2, S3 |
| rho | 0.3 | 0.48 | 0.66 | ESTIMATE | S2, S3 |
| e | 0.1 | 0.23 | 0.39 | ESTIMATE | S1 |
| s5 | 0.08 | 0.17 | 0.29 | PROXY | S4 |
| q | 0.38 | 0.57 | 0.74 | ESTIMATE | S1 |
| d5 | 0.95 | 1.12 | 1.3 | PROXY | S2, S5, S6 |
| o | 0.92 | 0.975 | 0.998 | ESTIMATE | S1, S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.46 | 1.18 | 2.36 | ESTIMATE |
| F | 1.23 | 3.03 | 4.57 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.74 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS evidence covers all NAICS 335 rather than the narrowed lens.
- a: ILO exposure is technical potential, not observed current substitution.
- rho: No 335999-specific AI adoption series was found.
- rho: Implementation varies by product criticality and digital maturity.
- e: The frozen 143-firm count is modeled and not a verified target roster.
- e: NAICS classification alone cannot distinguish outsourced programs from proprietary catalog products.
- s5: The Census statistic represents responding owners of employer businesses economy-wide.
- s5: Owner observations are not firm-level transfer events.
- q: No public contract-term distribution exists for the narrowed lens.
- q: Product and material savings may be passed through differently from labor savings.
- d5: Electricity and grid indicators are end-market proxies, not 335999 shipments.
- d5: Demand growth may accrue to transformers, controls, batteries, or semiconductors classified elsewhere.
- d5: The residual industry's product mix is unusually diverse.
- o: Hardware integration could reduce unit counts without eliminating the operator.
- o: Conventional automation and semiconductor integration are distinct from generative-AI substitution.

## Sources
- **S1** — [2022 NAICS 335999: All Other Miscellaneous Electrical Equipment and Component Manufacturing](https://www.census.gov/naics/?details=335999&input=335999&year=2022) (accessed 2026-07-23): Industry boundary and diverse illustrative products including converters, power supplies, UPS systems, surge suppressors, cords, bells, and ultrasonic equipment.
- **S2** — [Electrical Equipment, Appliance, and Component Manufacturing: NAICS 335](https://www.bls.gov/iag/tgs/iag335.htm) (accessed 2026-07-23): Broader-sector occupation mix and recent output volatility for electrical-equipment manufacturing.
- **S3** — [Generative AI and Jobs: A global analysis of potential effects on job quantity and quality](https://www.ilo.org/sites/default/files/2024-08/GenAI%20and%20Jobs_Policy%20Brief_ILO.pdf) (accessed 2026-07-23): Task-level GenAI exposure by broad occupation, with clerical tasks substantially more exposed than other groups.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-23): Economy-wide evidence that 51% of responding employer-business owners were age 55 or older.
- **S5** — [Fossil generation could rise with faster-than-expected growth in data center power demand](https://www.eia.gov/TODAYINENERGY/detail.php?id=67344) (accessed 2026-07-23): Observed 2020-2025 electricity-load growth and 2026-2027 forecasts, including data centers as a key driver.
- **S6** — [Clean Energy Resources to Meet Data Center Electricity Demand](https://www.energy.gov/oe/clean-energy-resources-meet-data-center-electricity-demand) (accessed 2026-07-23): DOE evidence on rapidly growing data-center load, continuous firm-power requirements, and grid-modernization needs.
