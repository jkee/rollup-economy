# 312112 — Bottled Water Manufacturing

*v5.1 Stage 1 research memo. Run `312112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.91 · L 0.79 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Growing physical hydration demand and recurring bottling programs support durable operator need, while standardized planning, quality, record, and maintenance workflows offer targeted AI efficiency.
**Weakness:** Commodity-like buyer leverage and indexed packaging economics can pass visible productivity back to customers, while the eligible independent co-packer population is unmeasured.

## Business-model lens
- Included: Independent US bottled-water plants in NAICS 312112 that repeatedly purify, bottle, label, package, or prepare water for external brands, retailers, exchange programs, home-and-office-delivery systems, hospitality customers, or other beverage companies, within the lower-middle-market EBITDA band.
- Excluded: Own-brand manufacturers without a recurring third-party production stream, captive plants, brands that outsource all production, pure water delivery or exchange operators without manufacturing, self-service refill operators, public water utilities, wholesalers, soft-drink plants classified in 312111, non-control financings, and non-operating facilities.
- Customer and revenue model: Recurring B2B co-packing, private-label, and independent bottler programs priced per case, bottle, gallon, or production run; agreements may include minimum volumes, take-or-pay commitments, packaging and resin indexation, customer-supplied materials, quality specifications, and periodic repricing.
- Deviation from default lens: Narrowed to independent contract, private-label, and program bottlers because NAICS 312112 includes own-brand and vertically integrated water manufacturers that sell products rather than an outsourced service; recurring third-party bottling is the coherent service-like subset.

## Executive view
Independent contract and private-label water bottlers combine durable physical demand with repetitive, data-rich operations. AI opportunity is concentrated in planning, records, quality review, inventory, customer service, and maintenance rather than core filling, sanitation, testing, or accountable release. Demand history is constructive, but commoditized contracts, resin and packaging indexation, customer bargaining power, and environmental pressure limit the share of benefits retained.

## How AI changes the work
Useful applications include forecast and production scheduling, EDI and purchase-order handling, specification extraction, laboratory-result review, exception detection, lot and quality records, visual inspection triage, inventory reconciliation, invoice processing, and predictive maintenance. Mature mechanical automation already handles much line work. Physical sampling, sanitation, changeovers, material movement, repairs, validation, corrective action, and product release remain human- and asset-dependent.

## Value capture
Multi-year exclusivity, minimum commitments, take-or-pay, and scarce geographic capacity can protect economics. Capture erodes when case prices are mostly indexed, customers supply packaging, buyers can change pricing, scrap or yield improvements are contractually shared, or programs are rebid. Operational savings outside auditable direct costs and within fixed-price periods are more retainable than visible resin, packaging, or unit-labor reductions.

## Firm availability
Recurring external bottling clearly exists, but the eligible denominator is obscured by own-brand spring-water firms, integrated national producers, delivery networks, and refill operators. Private transfer probability is not observed. Target diligence must establish customer and brand ownership, change-of-control rights, source-water permissions, state and FDA compliance, packaging equipment ownership, environmental permits, recall history, and deferred maintenance.

## Demand durability
Bottled-water gallons have grown over decades and reached a new high in 2024, supported by hydration, convenience, and displacement of sugary beverages. Private-label and contract bottling can benefit brands and retailers that avoid plant capital. Offsetting risks include mature single-serve penetration, tap filtration, reusable containers, refill systems, plastic regulation, source-water controversy, local restrictions, imports, and insourcing by scaled customers.

## Risks and uncertainty
The largest evidence gaps are the eligible-firm share, qualifying transfer rate, contract-term distribution, and actual plant task mix. Additional risks include concentrated customers, freight radius, low product differentiation, PET and recycled-resin volatility, water rights, drought or source challenges, testing failures, contamination, recalls, underutilized lines, packaging mandates, cybersecurity, and older equipment that cannot generate reliable data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1878 | — | OBSERVED | — |
| n | — | 44 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.31 | PROXY | S2, S4, S5 |
| rho | 0.3 | 0.5 | 0.7 | PROXY | S3, S4, S5, S6 |
| e | 0.2 | 0.35 | 0.5 | ESTIMATE | S1, S8, S9 |
| s5 | 0.1 | 0.17 | 0.27 | ESTIMATE | — |
| q | 0.18 | 0.34 | 0.52 | PROXY | S8, S9 |
| d5 | 0.98 | 1.08 | 1.18 | PROXY | S7, S10 |
| o | 0.93 | 0.98 | 0.995 | ESTIMATE | S5, S6, S8, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.27 | 0.79 | 1.63 | PROXY |
| F | 1.02 | 2.07 | 3.12 | ESTIMATE |
| C | 3.60 | 6.80 | 10.00 | PROXY |
| D | 9.11 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation proxy is four-digit beverage manufacturing and is materially distorted by brewery, winery, hospitality, and integrated-brand activity.
- a: Employment shares are not wage-weighted task shares.
- a: Mature bottling automation means some apparently exposed machine tasks may already be automated and therefore excluded by definition.
- rho: The adoption evidence is cross-sector or cross-manufacturing rather than bottled-water-specific.
- rho: NIST figures include light uses and draw on cited industry surveys.
- rho: Automation of records and testing support cannot remove regulatory responsibility for sampling, corrective action, and release.
- e: No source measures the independent co-packer share of NAICS 312112 LMM firms.
- e: Older filed contracts prove the business model exists but may not represent current market prevalence.
- e: Manufacturing and delivery or exchange activities can coexist, complicating classification under the fixed lens.
- s5: This is a bounded hazard estimate rather than an observed transfer probability.
- s5: Small private plant transactions are underreported and frequently lack six-digit NAICS coding.
- s5: Water-source rights, customer concentration, environmental permits, and aging lines can make a nominal firm non-transferable.
- q: The observed contracts are older and issuer-specific, not a current representative sample.
- q: Terms vary by run length, package, freight geography, source-water access, capacity, and customer scale.
- q: The estimate excludes demand loss and implementation failure.
- d5: The demand source is an industry research provider and trade-publication data set rather than a government series.
- d5: The market totals include imports, vended water, and channels not wholly produced by the screened operator population.
- d5: Environmental policy and consumer reuse behavior can change faster than the historical volume trend.
- o: This is a bounded operator-necessity judgment rather than an observed substitution rate.
- o: A customer switching to another bottler does not reduce operator-required demand under the construct.
- o: Vended refill and tap filtration can eliminate some packaged production rather than merely change the supplier.

## Sources
- **S1** — [NAICS Sector 31-33 Archive: 312112 Bottled Water Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Official definition of 312112 as purifying and bottling water, including naturally carbonated water, with cross-references separating artificially carbonated water and purchased-water bottling.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 312100](https://www.bls.gov/oes/2023/may/naics4_312100.htm) (accessed 2026-07-22): Broader beverage occupation mix, including 21.59% production, 5.29% installation/maintenance, 5.33% management, 4.68% office/administrative, 3.48% business/financial, and 26.40% food-preparation/serving employment.
- **S3** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS evidence of 17%-20% current US business AI use from December 2025 to May 2026, 20%-23% expected use within six months, and higher use at larger firms.
- **S4** — [The Rise of Artificial Intelligence in U.S. Manufacturing: Text Only](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Manufacturing AI applications in predictive maintenance, quality, forecasting, document management, inventory, supply chain, and scheduling, plus adoption evidence and barriers involving data, cost, skills, cybersecurity, and legacy systems.
- **S5** — [FDA Regulates the Safety of Bottled Water Beverages](https://www.fda.gov/food/buy-store-serve-safe-food/fda-regulates-safety-bottled-water-beverages-including-flavored-water-and-nutrient-added-water) (accessed 2026-07-22): Bottled-water-specific CGMP duties covering sanitary processing, source protection, quality control, source and final-product testing, and FDA plant inspection.
- **S6** — [Small Entity Compliance Guide: Bottled Water and Total Coliform and E. coli](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/small-entity-compliance-guide-bottled-water-and-total-coliform-and-e-coli) (accessed 2026-07-22): Binding bottled-water requirements for weekly source testing when the source is not a public system, follow-up E. coli testing, corrective measures, finished-product testing, and corrective-action records.
- **S7** — [Bottled Water Volume Growth Quickens in 2024](https://www.beveragemarketing.com/news-detail.asp?id=825) (accessed 2026-07-22): US bottled-water volume grew 2.9% in 2024 after 0.4% in 2023 and 1.1% in 2022; per-capita consumption reached 47.3 gallons, with an expectation of 50 gallons around decade-end.
- **S8** — [True Drinks and Niagara Bottling Agreement filed with the SEC](https://www.sec.gov/Archives/edgar/data/1134765/000141588915003511/ex10-1.htm) (accessed 2026-07-22): Observed bottled-water contract with five-year exclusivity, a 3.2 million-case annual minimum, $2-per-case take-or-pay shortfall, pricing indexed 60% to soft-drink PPI and 20% to PET resin, and a 3% material-loss allowance.
- **S9** — [Primo Water Corporation Registration Statement](https://www.sec.gov/Archives/edgar/data/1365101/000095012310101733/g22358b4e424b4.htm) (accessed 2026-07-22): Evidence of recurring independent bottler arrangements requiring customer specifications and quality compliance, brand-supplied packaging inputs, generally three-year terms, and customer pricing modification on 30 days' notice.
- **S10** — [Bottled Water Reporter: 2024 U.S. Bottled Water Market Statistics](https://bottledwater.org/wp-content/uploads/2025/07/BWR_BWstats_June2025_FinalwithBMCad.pdf) (accessed 2026-07-22): BMC market table showing total gallons of 15.70 billion in 2021, 15.88 billion in 2022, 15.95 billion in 2023, and 16.40 billion in 2024; single-serve PET was 70.7% of 2024 volume.
- **S11** — [Plastic Minimum Content Standards and Reporting for Beverage Manufacturers](https://calrecycle.ca.gov/bevcontainer/bevdistman/plasticcontent/) (accessed 2026-07-22): California requires covered plastic beverage containers to average 25% postconsumer recycled content from 2025 and 50% from 2030, with annual manufacturer reporting and penalties for noncompliance.
