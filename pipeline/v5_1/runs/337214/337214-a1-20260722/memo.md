# 337214 — Office Furniture (except Wood) Manufacturing

*v5.1 Stage 1 research memo. Run `337214-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.93 · L 1.20 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat workplace refresh and configuration-heavy workflows create practical AI-assisted operating opportunities.
**Weakness:** Hybrid-work uncertainty and bid-driven channels limit demand growth and retained benefits.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly supplying stock or custom nonwood office desks, systems, seating, storage, tables, workstations, and related office-type furniture to external dealers, corporate, education, healthcare, hospitality, and government customers.
- Excluded: Captive internal shops, shells, wood office furniture, architectural millwork, partitions and shelving classified separately, installation-only dealers, and used-furniture resellers.
- Customer and revenue model: Dealer and contract-channel orders, project bids, catalog sales, corporate standards programs, and repeat replacement or reconfiguration purchases, generally priced per piece, workstation, lot, or project.
- Deviation from default lens: none

## Executive view
Nonwood office furniture offers AI opportunities in specifications, quoting, configuration, planning, inspection, and customer service, but physical fabrication and assembly remain dominant. Demand appears mixed rather than collapsing: small and midsized customer orders are firmer than contract channels, while hybrid work and long replacement cycles cap growth.

## How AI changes the work
AI can interpret specifications, assist configurations and visualizations, check orders, schedule production, forecast components, identify defects, and answer dealer questions. Metal forming, welding, coating, upholstery, assembly, packing, and maintenance execution remain physical. Product-option complexity and dealer-system integration are practical constraints.

## Value capture
Ergonomics, design, brand, warranty, corporate standards, dealer relationships, and lead times create differentiation. Competitive bids, dealer economics, transparent catalogs, imports, and sophisticated contract buyers return much of the saving to customers over time.

## Firm availability
Most estimated in-band firms should be repeat external suppliers, although the count uses a machinery-sector margin that may be poorly matched to furniture. Transfer quality depends on dealer concentration, brand relevance, working capital, and retaining design and sales relationships.

## Demand durability
Refreshes, return-to-office programs, and noncorporate workplaces support physical demand. Hybrid attendance, space consolidation, reuse, imports, and long-lived modular products constrain the basket; the cited current order picture is stronger in smaller customers than large contracts.

## Risks and uncertainty
Risks include hybrid-work persistence, project cyclicality, dealer and customer concentration, steel and textile inputs, tariffs and imports, freight damage, warranty, product fashion, working capital, and mistaking design productivity for removable labor. Direct LMM contract and transfer evidence is limited.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2595 | — | OBSERVED | — |
| n | — | 58 | — | ESTIMATE | — |
| a | 0.16 | 0.24 | 0.34 | PROXY | S2, S3 |
| rho | 0.3 | 0.48 | 0.64 | PROXY | S3 |
| e | 0.67 | 0.82 | 0.93 | ESTIMATE | S1 |
| s5 | 0.15 | 0.27 | 0.4 | PROXY | S5 |
| q | 0.24 | 0.43 | 0.61 | ESTIMATE | — |
| d5 | 0.89 | 1 | 1.13 | PROXY | S4 |
| o | 0.92 | 0.97 | 0.995 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.50 | 1.20 | 2.26 | PROXY |
| F | 3.09 | 4.23 | 5.01 | ESTIMATE |
| C | 4.80 | 8.60 | 10.00 | ESTIMATE |
| D | 8.19 | 9.70 | 10.00 | ESTIMATE |

## Caveats
- a: BLS evidence combines several furniture industries and is not six-digit-specific.
- a: Already-automated CAD configuration and CNC work is excluded from the remaining opportunity.
- rho: AI-tool use does not establish labor substitution.
- rho: Rendering or design productivity may increase sales capacity rather than reduce labor.
- e: The provided count uses a machinery margin rather than a furniture-specific observed EBITDA distribution.
- e: Census defines establishments while transfer eligibility applies to firms.
- s5: No six-digit qualifying-transfer denominator was found.
- s5: Succession resilience does not equal a control-transfer probability.
- q: Capture is likely higher in differentiated ergonomic or standards-based products and lower in commodity desks and seating.
- q: No representative contract dataset was found.
- d5: The source reports directional prose rates rather than exact percentages.
- d5: HNI is a large public company and includes a broader workplace portfolio.
- d5: Projects and replacement demand can be lumpy.
- o: An operator remains necessary even if production shifts offshore or consolidates into large firms.
- o: Hybrid work reduces required quantity rather than replacing furniture with software at occupied workplaces.

## Sources
- **S1** — [Census 2022 NAICS definition: 337214 Office Furniture except Wood Manufacturing](https://www.census.gov/naics/?details=337&input=337&year=2022) (accessed 2026-07-22): Defines nonwood office-type furniture made on a stock or custom basis and assembled or unassembled.
- **S2** — [BLS May 2023 occupation estimates for Furniture and Related Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_3370A1.htm) (accessed 2026-07-22): Provides occupation-level employment and wages for the broader furniture industries, including production, upholstery, finishing, and machine-operation work.
- **S3** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Reports 46% manufacturing AI-tool use and more than 80% expecting increased use in two years, with operational use cases and adoption barriers.
- **S4** — [HNI first-quarter 2026 earnings release](https://www.sec.gov/Archives/edgar/data/48287/000004828726000098/hni-ex991q12026.htm) (accessed 2026-07-22): Reports small-to-midsized customer orders up at a low-single-digit rate, contract-customer orders down at a mid-single-digit rate, and expected low-single-digit legacy workplace sales growth in the following quarter.
- **S5** — [Deloitte Private survey: generational disparities in family-business succession planning](https://www2.deloitte.com/us/en/pages/about-deloitte/articles/press-releases/deloitte-private-survey-generational-disparatires-emerge-insuccession-planning-and-priorities-shaping-family-businesses.html) (accessed 2026-07-22): Describes a January 2024 survey of 500 US family-enterprise respondents and reports that 24% of current-generation respondents strongly agreed their succession plan would withstand departure of an important family employee.
