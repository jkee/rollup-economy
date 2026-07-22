# 325212 — Synthetic Rubber Manufacturing

*v5.1 Stage 1 research memo. Run `325212-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.03 · L 0.47 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent physical demand plus AI-assisted quality, planning, maintenance, and compliance workflows in repeat qualified production.
**Weakness:** Most of NAICS 325212 is product manufacturing rather than an outsourced service, leaving a poorly measured eligible-firm subset.

## Business-model lens
- Included: US lower-middle-market synthetic-rubber manufacturers that repeatedly produce customer-specified elastomers or latex under contract or toll-manufacturing relationships for external customers.
- Excluded: Captive plants, commodity producers selling only their own standard product, internal production units, pure distributors, natural-rubber processors, rubber-product fabricators, and non-control financing vehicles.
- Customer and revenue model: Recurring batch or continuous production for industrial customers, generally priced per pound or shipment under specifications and purchase agreements, with feedstock and energy clauses negotiated contractually.
- Deviation from default lens: The NAICS definition covers product manufacturing generally, while the fixed screen requires an outsourced-service model; the lens is narrowed to contract and toll producers to avoid mixing commodity product sellers with transferable recurring-service businesses.

## Executive view
The qualifying opportunity is a narrow contract-manufacturing subset of a capital-intensive product industry. AI can improve planning, quality records, maintenance knowledge, and compliance workflows, but it does not displace the physical or accountable plant operator, and commodity-style pricing limits how much benefit remains with the supplier.

## How AI changes the work
Useful applications are production scheduling, batch and laboratory record review, root-cause assistance, maintenance work-order drafting, procurement analysis, customer documentation, and regulatory reporting. Human review and deterministic process controls remain necessary around recipes, emissions, quality release, and process safety.

## Value capture
Customer qualification and plant-specific know-how create switching friction, supporting partial capture. Against that, per-unit bids, renewal negotiation, index-linked inputs, and cost-down expectations can transfer much of an efficiency gain to customers over five years.

## Firm availability
Only toll or contract producers meet the recurring outsourced-service lens; most establishments in the NAICS definition simply manufacture synthetic rubber as a product. Broad owner-age evidence suggests succession pressure, but specialized-asset and environmental diligence can lead to internal transfers, strategic sales, or closures rather than clean LMM control transactions.

## Demand durability
Synthetic rubber remains physically required in tires and a range of industrial products, so software does not eliminate the service basket. Federal Reserve output data nevertheless show a long volatile decline followed by partial recovery, making flat rather than robust demand the prudent base case.

## Risks and uncertainty
The largest uncertainties are the very small eligible contract-production share, absent plant-level task data, unknown contract pass-through terms, environmental liabilities, customer concentration, feedstock volatility, import competition, and whether the injected LMM firm estimate captures truly independent transferable plants.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1206 | — | OBSERVED | — |
| n | — | 25 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.34 | PROXY | S2, S3 |
| rho | 0.25 | 0.42 | 0.6 | ESTIMATE | S4, S5 |
| e | 0.02 | 0.08 | 0.18 | ESTIMATE | S1, S6 |
| s5 | 0.1 | 0.2 | 0.32 | PROXY | S7 |
| q | 0.3 | 0.48 | 0.68 | ESTIMATE | S8 |
| d5 | 0.8 | 0.97 | 1.12 | PROXY | S8, S9 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.47 | 0.98 | ESTIMATE |
| F | 0.08 | 0.54 | 1.43 | ESTIMATE |
| C | 6.00 | 9.60 | 10.00 | ESTIMATE |
| D | 7.52 | 9.51 | 10.00 | ESTIMATE |

## Caveats
- a: BLS evidence is for manufacturing or occupations nationally, not NAICS 325212 contract producers.
- a: The primitive concerns current not-yet-automated tasks; plant-level installed-control-system data were unavailable.
- rho: This is bounded judgment rather than observed adoption.
- rho: EPA-described monitoring, recordkeeping, leak-control, and operating requirements make fully autonomous implementation less plausible than back-office assistance.
- e: No public source measures contract-manufacturing incidence at six digits.
- e: The injected firm count may include integrated or commodity producers that do not fit the recurring outsourced-service lens.
- s5: The owner-age statistic covers all employer businesses and responding owners, not NAICS 325212 or LMM firms.
- s5: It does not observe control transfers or distinguish sales from family succession and closure.
- q: No contract sample was publicly available, so the range is judgmental.
- q: Product mix and customer concentration can create much stronger or weaker pricing power than the base case.
- d5: Industrial production is supply-side output, not lens-specific demand.
- d5: The index mixes commodity and customer-specific production and does not hold product quality constant.
- o: Operator requirement does not guarantee that an independent LMM operator retains the work; large integrated suppliers can consolidate it.
- o: The estimate separates physical operator necessity from labor automation, which is captured in a and rho.

## Sources
- **S1** — [2022 NAICS definition: 325212 Synthetic Rubber Manufacturing](https://www.census.gov/naics/?details=325&input=325&year=2022) (accessed 2026-07-22): Defines the industry as establishments primarily engaged in manufacturing synthetic rubber and distinguishes it from rubber-product manufacturing.
- **S2** — [Producing the goods of the future: Job opportunities in manufacturing](https://www.bls.gov/careeroutlook/2026/article/manufacturing.htm) (accessed 2026-07-22): Reports that production occupations represented about half of manufacturing employment in 2024 and describes projected manufacturing openings.
- **S3** — [Industrial Production Managers](https://www.bls.gov/ooh/management/industrial-production-managers.htm) (accessed 2026-07-22): Lists production-manager duties including scheduling, customer and supplier communication, hiring, production-data analysis, reports, safety monitoring, process streamlining, and quality-control oversight.
- **S4** — [Regulatory Impact Analysis for Synthetic Organic Chemical Manufacturing and Polymers and Resins Rules](https://www.epa.gov/system/files/documents/2023-04/Proposed_HON_RIA_final_2023-03.pdf) (accessed 2026-07-22): Describes synthetic-rubber production as monomer synthesis followed by polymerization and identifies equipment leaks, process vents, wastewater, and storage tanks as emission sources.
- **S5** — [Synthetic Organic Chemical Manufacturing Industry NESHAP](https://www.epa.gov/stationary-sources-air-pollution/synthetic-organic-chemical-manufacturing-industry-national) (accessed 2026-07-22): States that applicable owners and operators face control, monitoring, reporting, and recordkeeping requirements for process vents, storage vessels, transfer racks, wastewater streams, and equipment leaks.
- **S6** — [2022 Economic Census basic statistics: NAICS 325212](https://data.census.gov/table/ECNBASIC2022.EC2200BASIC?codeset=naics~325212&g=010XX00US) (accessed 2026-07-22): Shows a national six-digit industry table for Synthetic Rubber Manufacturing and identifies its universe as operating establishments with paid employees.
- **S7** — [Business Owners' Ages: Over Half of U.S. Business Owners Were Age 55 and Over](https://www.census.gov/library/visualizations/2020/comm/business-owners-ages.html) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 ABS, data year 2018.
- **S8** — [Industrial Production: Synthetic Rubber (NAICS 325212), table data](https://fred.stlouisfed.org/data/IPG325212S) (accessed 2026-07-22): Provides monthly Federal Reserve industrial-production index observations for NAICS 325212, including the decline through 2024 and partial recovery in 2025-26.
- **S9** — [EPA air toxic rule for elastomer production](https://www.epa.gov/archive/epapages/newsroom_archive/newsreleases/0704044acbf9c5cf8525646b007ce57c.html) (accessed 2026-07-22): Identifies synthetic-rubber end uses including tires, hoses, belts, footwear, adhesives, caulks, wire insulation, and floor tiles.
