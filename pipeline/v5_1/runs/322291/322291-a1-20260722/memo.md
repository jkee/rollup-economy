# 322291 — Sanitary Paper Product Manufacturing

*v5.1 Stage 1 research memo. Run `322291-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.51 · L 0.39 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable replenishment demand and document-heavy planning, quality, and customer workflows support recurring operational improvement.
**Weakness:** The directly AI-substitutable wage pool is small because most value creation is physical and large buyers can force productivity gains into price.

## Business-model lens
- Included: US lower-middle-market converters of facial tissue, toilet tissue, towels, napkins, disposable diapers, sanitary napkins, tampons, and related sanitary paper products that repeatedly supply distributors, institutions, retailers, hospitality, foodservice, healthcare, or private-label customers.
- Excluded: Captive plants, non-operating product brands, pure wholesalers, upstream paper mills, non-paper reusable hygiene products, non-control financing vehicles, and operations that cannot transfer independently of the owner.
- Customer and revenue model: Recurring unit sales through retail/private-label programs, distributor replenishment, and institutional supply arrangements, typically governed by purchase orders, price lists, bids, or supply contracts.
- Deviation from default lens: none

## Executive view
Sanitary paper products combine durable recurring physical demand with a limited AI-addressable labor layer. The clearest opportunity is in planning, documentation, forecasting, procurement, and commercial administration, while most plant work remains tied to machinery, materials, quality, sanitation, and fulfillment.

## How AI changes the work
AI can assist demand forecasting, purchase and production planning, customer-order ingestion, specification comparison, exception triage, deviation drafting, supplier review, and routine customer service. It cannot replace converting equipment, changeovers, maintenance, laboratory testing, physical inspection, sanitation, packaging, or final accountable product release.

## Value capture
Savings can be retained until price lists, bids, and supply agreements reset, but powerful retailers, private-label customers, distributors, and institutional buyers are likely to claim a substantial share. Reliability and compliance improvements may be more defensible than pure unit-cost savings.

## Firm availability
The supplied dataset estimates only 45 firms in the LMM band, and actual standalone eligibility is uncertain because the industry contains large strategic plants, captive facilities, and varied margin profiles. No denominator-matched control-transfer series was located.

## Demand durability
Core hygiene consumption is recurring and cannot be digitized. Reusable alternatives, material reduction, dispenser efficiency, demographic changes, and imports can affect particular categories, but the remaining physical basket should continue to require manufacturing accountability.

## Risks and uncertainty
Key uncertainties are six-digit occupational mix, actual firm ownership and earnings, customer concentration, commodity versus regulated product mix, real unit-volume trends, and the pace at which legacy plant systems can support validated AI workflows. The provided compensation and firm-count inputs also mix vintages and use a margin bridge.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1752 | — | OBSERVED | — |
| n | — | 45 | — | ESTIMATE | — |
| a | 0.07 | 0.14 | 0.23 | PROXY | S1, S2 |
| rho | 0.23 | 0.4 | 0.58 | ESTIMATE | S4, S5 |
| e | 0.5 | 0.68 | 0.82 | ESTIMATE | S3 |
| s5 | 0.08 | 0.16 | 0.27 | ESTIMATE | — |
| q | 0.24 | 0.44 | 0.64 | ESTIMATE | S4 |
| d5 | 0.96 | 1.03 | 1.11 | ESTIMATE | S3, S4 |
| o | 0.93 | 0.98 | 1 | ESTIMATE | S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.11 | 0.39 | 0.93 | ESTIMATE |
| F | 1.66 | 2.85 | 3.85 | ESTIMATE |
| C | 4.80 | 8.80 | 10.00 | ESTIMATE |
| D | 8.93 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is for all paper manufacturing, not this six-digit industry.
- a: No source measures task-level AI exposure or existing AI use in sanitary-paper plants.
- rho: This is bounded judgment, not a measured adoption forecast.
- rho: FDA evidence applies to menstrual products within the broader industry, not tissue and towel lines.
- e: Provided n relies on size-class receipts and an industry margin bridge rather than observed EBITDA.
- e: The industry spans household tissue, away-from-home products, diapers, and regulated menstrual products with different economics.
- s5: No complete six-digit control-transfer numerator and eligible-firm denominator were found.
- s5: Internal recapitalizations and asset-only plant sales must be excluded.
- q: No source directly measures sharing of AI-derived savings.
- q: Capture differs materially by branded, private-label, institutional, and commodity channels.
- d5: No complete constant-price, constant-quality five-year forecast was found.
- d5: The product mix includes mature tissue and potentially faster-growing absorbent-hygiene uses.
- o: FDA oversight evidence applies only to menstrual products, though it demonstrates operator accountability within that segment.
- o: Import displacement can remove domestic-operator demand even when US consumption persists.

## Sources
- **S1** — [Paper Manufacturing: NAICS 322](https://www.bls.gov/IAG/TGS/iag322.htm) (accessed 2026-07-22): BLS reports 356,500 total employees and 253,800 production and nonsupervisory employees in June 2026, plus 87,050 paper-goods machine operators in 2025, for the broader paper-manufacturing subsector.
- **S2** — [Paper Goods Machine Setters, Operators, and Tenders](https://www.bls.gov/oes/2023/May/oes519196.htm) (accessed 2026-07-22): BLS defines the occupation as setting up, operating, or tending machines that convert, saw, corrugate, band, wrap, box, stitch, form, or seal paper or paperboard and reports 96,460 workers nationally in May 2023.
- **S3** — [NAICS 322291 Sanitary Paper Product Manufacturing](https://www.census.gov/naics/?details=322291&input=322291&year=2007) (accessed 2026-07-22): Census defines the industry as converting purchased sanitary paper stock or wadding into facial tissues, handkerchiefs, table napkins, toilet paper, towels, disposable diapers, sanitary napkins, and tampons.
- **S4** — [Menstrual Product Options, Facts, and Safe Use](https://www.fda.gov/medical-devices/products-and-medical-procedures/menstrual-product-options-facts-and-safe-use) (accessed 2026-07-22): FDA states that all menstrual products marketed in the United States are regulated as medical devices and must meet applicable manufacturing, labeling, malfunction-reporting, and adverse-event requirements; certain products such as tampons undergo FDA review.
- **S5** — [The Facts on Tampons—and How to Use Them Safely](https://www.fda.gov/consumers/consumer-updates/facts-tampons-and-how-use-them-safely) (accessed 2026-07-22): FDA states that cleared tampons are single-use medical devices and that manufacturers submit testing on material safety, absorbency, strength, integrity, and bacterial-growth effects before legal sale.
