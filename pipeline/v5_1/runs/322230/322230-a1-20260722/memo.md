# 322230 — Stationery Product Manufacturing

*v5.1 Stage 1 research memo. Run `322230-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.44 · L 0.41 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat order workflows create a practical, if limited, opportunity to automate estimating, order entry, scheduling, procurement, and customer administration.
**Weakness:** Most wages support physical production while the underlying paper-stationery basket faces persistent digital substitution and competitive pass-through.

## Business-model lens
- Included: US lower-middle-market manufacturers of envelopes, notebooks, pads, filing products, computer paper, and related stationery that repeatedly supply distributors, institutions, printers, retailers, or business customers.
- Excluded: Captive converting operations, hobby-scale makers, firms primarily engaged in printing or wholesale distribution, non-control financing vehicles, and businesses whose operations cannot transfer independently of the owner.
- Customer and revenue model: Repeat product orders under purchase orders, distributor programs, private-label arrangements, and institutional supply contracts; revenue is generally per unit or per production run rather than time-and-materials billing.
- Deviation from default lens: none

## Executive view
Stationery converting is a physical manufacturing business with a modest AI-addressable office layer. The opportunity is chiefly better order-to-production coordination and leaner administration, while demand faces continuing digital substitution and commodity price pressure.

## How AI changes the work
AI can extract specifications from emails and PDFs, assist quotes, flag artwork or order anomalies, predict schedule and inventory exceptions, draft customer responses, and organize quality records. Machine setup, material handling, maintenance, packing, and accountable physical inspection remain human- and equipment-dependent.

## Value capture
Fixed unit prices permit some savings retention between repricing events, especially in customized short runs. Distributors, large accounts, competitive bidding, and transparent commodity alternatives are likely to share away a substantial portion over five years.

## Firm availability
The supplied dataset estimates 99 firms in the economic band, but actual eligibility depends on independence, recurring external customers, transferable operations, and normalized earnings. Succession and deal evidence are not denominator-matched, so control-transfer probability remains uncertain.

## Demand durability
Paper-based communication and filing continue to lose occasions to digital workflows. Remaining education, creative, premium, compliance, mail, and tactile uses should still require physical conversion and fulfillment, leaving a durable but smaller basket.

## Risks and uncertainty
The main uncertainties are the absence of six-digit task-time data, incomplete firm-level eligibility and ownership information, divergent commodity versus premium product economics, import competition, and lack of matched real shipment volumes. The supplied compensation and firm-count inputs also mix vintages and rely on a margin bridge.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1387 | — | OBSERVED | — |
| n | — | 99 | — | ESTIMATE | — |
| a | 0.09 | 0.17 | 0.28 | PROXY | S1, S2 |
| rho | 0.25 | 0.43 | 0.62 | ESTIMATE | S1, S2 |
| e | 0.55 | 0.72 | 0.85 | ESTIMATE | S3 |
| s5 | 0.09 | 0.17 | 0.28 | ESTIMATE | S4 |
| q | 0.28 | 0.48 | 0.68 | ESTIMATE | S5 |
| d5 | 0.68 | 0.82 | 0.98 | PROXY | S3, S6 |
| o | 0.84 | 0.93 | 0.98 | ESTIMATE | S2, S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.12 | 0.41 | 0.96 | ESTIMATE |
| F | 2.86 | 4.14 | 5.15 | ESTIMATE |
| C | 5.60 | 9.60 | 10.00 | ESTIMATE |
| D | 5.71 | 7.63 | 9.60 | ESTIMATE |

## Caveats
- a: Occupation evidence is for NAICS 322, not 322230.
- a: No source measures current AI deployment or task time in stationery plants.
- rho: This is bounded judgment rather than measured five-year implementation evidence.
- rho: Physical automation is excluded unless AI is the operative substitution mechanism.
- e: The provided n is an estimate produced from size-class and margin assumptions, not a verified target list.
- e: Manufacturing revenue is repeat product supply rather than a pure service contract.
- s5: Census provides an owner-age data product but the fetched page does not provide a 322230-specific age distribution.
- s5: No complete denominator-matched control-transfer series was found.
- q: The industry PPI shows realized output prices, not contractual sharing of AI benefits.
- q: Capture likely varies sharply between commodity and customized products.
- d5: The source is directional and centered on graphic paper for mail, not a complete 322230 volume index.
- d5: The BLS PPI cannot separate real volume from price without matched shipment-value data.
- o: Operator requirement is estimated after demand attrition; eliminated paper use belongs in d5.
- o: Imports can displace domestic operators even when physical-product demand remains.

## Sources
- **S1** — [Paper Manufacturing: NAICS 322](https://www.bls.gov/iag/tgs/iag322.htm) (accessed 2026-07-22): BLS page reports 356,500 total employees and 253,800 production and nonsupervisory employees in June 2026, and 87,050 paper-goods machine operators in 2025 for the broader paper-manufacturing subsector.
- **S2** — [Paper Goods Machine Setters, Operators, and Tenders](https://www.bls.gov/oes/2023/May/oes519196.htm) (accessed 2026-07-22): Defines the occupation as setting up, operating, or tending machines that convert, saw, corrugate, band, wrap, box, stitch, form, or seal paper and paperboard, and reports 96,460 workers nationally in May 2023.
- **S3** — [322230: Stationery Product Manufacturing](https://data.census.gov/profile/322230_-_Stationery_Product_Manufacturing?codeset=naics~322230) (accessed 2026-07-22): Census defines the industry as converting paper or paperboard into writing, filing, artwork, and similar products, including computer paper, office die-cuts, envelopes, stationery, and tablets.
- **S4** — [ABS - Characteristics of Business Owners: 2022 Tables (Employer Businesses)](https://www.census.gov/data/tables/2022/econ/abs/2022-abs-characteristics-of-owners.html) (accessed 2026-07-22): Census identifies Age of Owner as an available owner-characteristics topic and states that the 2022 ABS covers reference year 2021; used only to identify obtainable diligence evidence, not a numeric transfer rate.
- **S5** — [Producer Price Index by Industry: Stationery Product Manufacturing](https://fred.stlouisfed.org/data/PCU322230322230) (accessed 2026-07-22): BLS-derived monthly output-price index for NAICS 322230, including 166.437 in December 2024, 173.416 in December 2025, and 176.311 in April 2026; establishes observable product pricing but not benefit pass-through.
- **S6** — [The Paper Shortage and Its Effects on Mail](https://www.uspsoig.gov/reports/white-papers/paper-shortage-and-its-effects-on-mail) (accessed 2026-07-22): USPS OIG states that demand for graphic paper, the paper type most frequently used in mail, had been steadily declining before the pandemic and describes the pandemic decline in production and demand.
