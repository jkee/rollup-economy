# 323111 — Commercial Printing (except Screen and Books)

*v5.1 Stage 1 research memo. Run `323111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.11 · L 1.49 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Specification-heavy digital files and repetitive quote-to-proof-to-production workflows expose a meaningful share of skilled prepress, estimating, planning, and service labor.
**Weakness:** Electronic substitution shrinks major print categories, while competitive bidding and online price transparency erode long-run retention of savings.

## Business-model lens
- Included: US lower-middle-market commercial printers using offset, flexographic, gravure, letterpress, engraving, and digital processes to repeatedly serve business, institutional, agency, retail, packaging-label, direct-mail, and trade customers on a job-order or program basis.
- Excluded: Screen printing, book printing, publishing, captive in-house print rooms, pure brokers without transferable operations, hobby shops, non-control financing vehicles, and owner-dependent shops without recurring external customer relationships.
- Customer and revenue model: Job-order and program revenue priced per project, run, impression, piece, or contracted schedule, often combining prepress, printing, variable data, finishing, mailing, fulfillment, and account service.
- Deviation from default lens: none

## Executive view
Commercial printing has an unusually document-rich manufacturing workflow and a large fragmented firm population, creating credible AI opportunity in quoting, prepress, job planning, and customer administration. The physical production core remains operator-dependent, while long-run digital substitution pressures much of the demand basket.

## How AI changes the work
AI can parse specifications, generate and compare estimates, check files and versions, assist preflight and imposition, summarize proof changes, schedule jobs, predict exceptions, draft production tickets, and handle routine account communication. Press setup, color management, substrates, finishing, maintenance, packing, and accountable physical quality remain human and machine work.

## Value capture
Fast-turn, short-run, variable-data, label, fulfillment, and specification-sensitive work can retain workflow gains through service and switching costs. Commodity jobs are readily rebid, and procurement teams, brokers, and online alternatives will pass a substantial share into price over five years.

## Firm availability
The supplied dataset estimates 2,058 firms in the economic band, consistent with a broad fragmented market, but actual eligibility requires verifying EBITDA, recurring accounts, equipment condition, customer concentration, and owner dependence. Retirement and consolidation support transfers, though closures and asset sales are not qualifying events.

## Demand durability
Mail and transactional print volumes show sustained decline as communication digitizes. Labels, packaging-related print, direct mail, regulated pieces, premium physical media, and fast local work soften but do not remove the pressure; remaining complex work generally still needs a commercial operator.

## Risks and uncertainty
Key uncertainties are six-digit task mix, current workflow automation, customer and product mix, the split between declining mail/forms and resilient labels or packaging, actual LMM earnings, and whether owner-held relationships transfer. The supplied compensation and firm-count inputs also mix vintages and use a margin bridge.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.247 | — | OBSERVED | — |
| n | — | 2058 | — | ESTIMATE | — |
| a | 0.17 | 0.28 | 0.41 | PROXY | S1, S2 |
| rho | 0.34 | 0.54 | 0.72 | ESTIMATE | S1, S2 |
| e | 0.65 | 0.79 | 0.89 | ESTIMATE | S3 |
| s5 | 0.12 | 0.22 | 0.34 | ESTIMATE | — |
| q | 0.32 | 0.54 | 0.73 | ESTIMATE | S3 |
| d5 | 0.69 | 0.84 | 1.01 | PROXY | S4, S5 |
| o | 0.78 | 0.89 | 0.97 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.57 | 1.49 | 2.92 | ESTIMATE |
| F | 8.18 | 9.46 | 10.00 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 5.38 | 7.48 | 9.80 | ESTIMATE |

## Caveats
- a: BLS data cover all NAICS 323, not the six-digit industry.
- a: Occupation shares do not directly measure task exposure or existing automation.
- rho: This is bounded judgment rather than an observed implementation probability.
- rho: Digital-native printers may implement faster than legacy offset-heavy plants.
- e: The supplied n uses size-class receipts and a paper-industry margin bridge rather than observed printer EBITDA.
- e: Large variation in print process, end market, and value-added services affects transferability.
- s5: No comprehensive six-digit control-transfer series was found.
- s5: Asset auctions, tuck-in customer-book purchases without operating control, and internal reorganizations must be excluded.
- q: No source directly measures retention of AI-derived benefits.
- q: Commodity offset work and differentiated data/fulfillment programs have very different pass-through.
- d5: USPS volumes omit non-mailed print and do not map one-for-one to printer output.
- d5: BLS occupational decline can reflect productivity and consolidation as well as demand.
- o: Software elimination belongs in d5; o addresses the supplier model for remaining quantity.
- o: Digital presses can lower efficient scale and enable some customer in-sourcing.

## Sources
- **S1** — [Printing and Related Support Activities - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics3_323000.htm) (accessed 2026-07-22): BLS reports 378,410 workers in NAICS 323 in May 2023; printing workers were 138,520 (36.61%), including 90,740 press operators (23.98%), 32,450 binding/finishing workers (8.58%), and 15,330 prepress workers (4.05%). Graphic designers were 16,420 (4.34%).
- **S2** — [Printing and Related Support Activities: NAICS 323](https://www.bls.gov/iag/tgs/iag323.htm) (accessed 2026-07-22): BLS describes the subsector as printing labels, business cards, stationery, business forms, and other materials and reports 341,000 total employees and 237,200 production and nonsupervisory employees in May 2026.
- **S3** — [NAICS 323111: Commercial Printing (except Screen and Books)](https://www.item.com/naics/323111) (accessed 2026-07-22): Reproduces the NAICS definition: lithographic, gravure, flexographic, letterpress, engraving, and digital printing without publishing, including job-order printing on purchased stock and quick printers.
- **S4** — [A Decade of Facts and Figures](https://facts.usps.com/table-facts/) (accessed 2026-07-22): USPS reports total mail volume declining from 154.3 billion pieces in 2016 to 108.7 billion in 2025, First-Class Mail from 61.2 billion to 42.0 billion, and Marketing Mail from 80.9 billion to 56.8 billion.
- **S5** — [Occupational Projections and Worker Characteristics](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): BLS projects printing press operator employment to decline from 150,200 in 2024 to 138,000 in 2034, an 8.1% decline, while still averaging 13,700 annual openings.
