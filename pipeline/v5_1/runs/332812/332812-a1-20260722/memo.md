# 332812 — Metal Coating, Engraving (except Jewelry and Silverware), and Allied Services to Manufacturers

*v5.1 Stage 1 research memo. Run `332812-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.20 · L 1.51 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A broad recurring outsourced-service base benefits from AI-addressable order, schedule, quality, and compliance workflows.
**Weakness:** Physical shop labor, environmental liabilities, and competitive per-part pricing constrain implemented and retained gains.

## Business-model lens
- Included: US lower-middle-market job shops repeatedly enameling, lacquering, varnishing, painting, powder coating, hot-dip galvanizing, engraving, etching, or otherwise surfacing customer-owned metal products for manufacturers and industrial customers.
- Excluded: Captive in-house finishing lines, electroplating and anodizing classified in 332813, jewelry and printing-plate engraving, firms coating only their own fabricated products, consumer decorative shops, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring job-shop and production-program revenue billed per piece, square foot, pound, batch, line hour, or quoted program, with charges for pretreatment, masking, materials, color or finish changes, inspection, packaging, and expedite service.
- Deviation from default lens: none

## Executive view
Metal coating and engraving is a large, naturally outsourced job-shop industry with recurring manufacturer programs. AI can improve quoting, specification review, scheduling, quality records, visual inspection, and maintenance, while freight, qualification, finish consistency, and turnaround support some retention; physical processing and recent cyclical weakness limit the upside.

## How AI changes the work
Near-term uses include drawing and specification parsing, automated quotes and routings, color and material planning, line scheduling, certificate preparation, visual defect triage, maintenance knowledge, and customer updates. Racking, masking, preparation, spraying, dipping, curing, galvanizing, inspection, cleaning, and rework remain physical.

## Value capture
Approved processes, color consistency, local logistics, line fit, quality history, and fast turnaround create switching costs. Standard jobs remain competitively quoted, and material escalation plus customer productivity demands transmit part of the gain.

## Firm availability
The definition's service-to-manufacturers orientation means most standalone firms fit the lens, and the estimated firm population is large. Succession should create supply, but environmental diligence, customer concentration, and owner-dependent sales can impair transferability.

## Demand durability
Protective and decorative finishes remain physically necessary across many manufactured products. Broader industry output declined through 2024 before a partial recovery, so a flat base with cyclical downside is more defensible than strong structural growth.

## Risks and uncertainty
Key risks are manufacturing cycles, customer concentration, environmental and worker-safety liabilities, coating chemistry changes, energy and material costs, reject and rework exposure, owner dependence, customer insourcing, and unavailable six-digit task and real-demand data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2188 | — | OBSERVED | — |
| n | — | 532 | — | ESTIMATE | — |
| a | 0.2 | 0.32 | 0.45 | PROXY | S2, S3, S4 |
| rho | 0.34 | 0.54 | 0.71 | ESTIMATE | S5, S6 |
| e | 0.76 | 0.89 | 0.97 | ESTIMATE | S1 |
| s5 | 0.14 | 0.28 | 0.42 | PROXY | S7 |
| q | 0.36 | 0.56 | 0.74 | ESTIMATE | S5, S6 |
| d5 | 0.82 | 0.98 | 1.15 | PROXY | S8, S9, S10 |
| o | 0.88 | 0.96 | 0.99 | ESTIMATE | S1, S3, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.60 | 1.51 | 2.80 | ESTIMATE |
| F | 6.52 | 7.87 | 8.66 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 7.22 | 9.41 | 10.00 | ESTIMATE |

## Caveats
- a: No public six-digit occupation matrix isolates 332812.
- a: The broad process mix produces large dispersion: automated conveyor powder lines differ from manual masking and custom engraving shops.
- rho: This is bounded judgment, not an observed adoption rate.
- rho: Computer vision may improve faster than integration with legacy conveyor, oven, and pretreatment controls.
- e: Industry classification does not prove recurrence, economic band, or transferability.
- e: Some establishments may combine qualifying finishing with nonqualifying fabrication or retail activity.
- s5: The proxy is not industry- or size-specific and measures owners rather than transactions.
- s5: Cooperative, corporate, and sponsor-owned firms have no individual-owner retirement trigger.
- q: No public customer-contract sample was available.
- q: Capture is stronger for qualified technical finishes and weaker for standard powder colors on easily shipped parts.
- d5: Available real-output series are broader than 332812.
- d5: Coating demand varies with part mix, surface area, finish specification, and domestic manufacturing location, not just unit output.
- o: The accountable operator can consolidate into larger networks even if the physical service remains necessary.
- o: Labor automation is represented in a and rho rather than deducted again here.

## Sources
- **S1** — [NAICS definition: 332812 Metal Coating, Engraving, and Allied Services to Manufacturers](https://www.census.gov/naics/?details=332812&input=332812&year=2017) (accessed 2026-07-22): Defines enameling, lacquering, varnishing, hot-dip galvanizing, engraving, etching, powder coating, painting, and other surfacing services for the trade.
- **S2** — [Metal and Plastic Machine Workers](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-22): Describes machine operators as monitoring equipment and products and reports a projected 7% decline in aggregate metal and plastic machine-worker employment from 2024 to 2034.
- **S3** — [OSHA 1926.57 Ventilation](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.57) (accessed 2026-07-22): Describes immersion, spray finishing, galvanizing, surface coating, draining, drying, ventilation, and employee exposure controls for finishing operations.
- **S4** — [Occupational projections and worker characteristics](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Reports projected declines for multiple metal-processing occupations, including a 13.6% decline for plating-machine operators, as a directional automation proxy.
- **S5** — [Miscellaneous Metal Parts and Products Surface Coating NESHAP](https://19january2021snapshot.epa.gov/stationary-sources-air-pollution/surface-coating-miscellaneous-metal-parts-and-products-national_.html) (accessed 2026-07-22): Describes HAP standards for miscellaneous metal-part coating and identifies regulated organic pollutants such as xylenes, toluene, ketones, glycol ethers, styrene, and ethyl benzene.
- **S6** — [Technical Support Document for Miscellaneous Metal Parts and Products Surface Coating NESHAP](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1006FDO.TXT) (accessed 2026-07-22): Describes diverse coated products, coating application, pretreatment, curing, environmental controls, monitoring, recordkeeping, and reporting burdens.
- **S7** — [Business Owners' Ages: Over Half of U.S. Business Owners Were Age 55 and Over](https://www.census.gov/library/visualizations/2020/comm/business-owners-ages.html) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 ABS, data year 2018.
- **S8** — [Industrial Production: Coating, Engraving, Heat Treating, and Allied Activities](https://fred.stlouisfed.org/data/IPN3328SQ) (accessed 2026-07-22): Provides broader NAICS 3328 quarterly real-output values, including decline through 2024 and partial recovery through 2026 Q1.
- **S9** — [Sectoral Output for NAICS 33281](https://fred.stlouisfed.org/data/IPUEN33281T301000000) (accessed 2026-07-22): Reports annual sectoral-output changes for broader NAICS 33281, including declines of 1.7% in 2023 and 3.7% in 2024.
- **S10** — [EPA surface-coating residual risk and technology review proposal](https://www.epa.gov/sites/default/files/2019-08/documents/oar-19-000-6924coatingspkg3_signed_fr_notice16aug19.pdf) (accessed 2026-07-22): Lists the broad manufactured-product end markets using miscellaneous metal surface coating and estimates 368 facilities subject to the relevant NESHAP.
