# 314110 — Carpet and Rug Mills

*v5.1 Stage 1 research memo. Run `314110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.68 · L 0.43 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat, specification-heavy production and inspection workflows create focused AI opportunities without eliminating the need for a physical operator.
**Weakness:** Only a small, unobserved share of carpet mills likely fits the outsourced-service lens, against a backdrop of declining real output.

## Business-model lens
- Included: Lower-middle-market carpet and rug mills providing repeat commission coating, finishing, printing, or contract/custom production to external manufacturers, dealers, hospitality groups, institutions, and other commercial customers.
- Excluded: Stock or branded product manufacturing without a recurring outsourced-service relationship; pure distribution, retail, installation, carpet cutting and binding classified elsewhere, captive internal finishing, shells, and non-control financing vehicles.
- Customer and revenue model: Business customers place repeat purchase orders or production runs priced per yard, unit, lot, or specification; the qualifying subset earns manufacturing-service revenue through commission finishing/printing or recurring contract production rather than a subscription.
- Deviation from default lens: The code is narrowed to commission finishing/printing and repeat contract production because NAICS 314110 primarily describes goods manufacturing, while the qualifying outsourced production-service model has different eligibility and retention economics from branded or stock carpet sales.

## Executive view
The coherent opportunity is not the whole carpet-mill industry but a small subset of commission finishers, printers, and repeat contract producers. That subset has real order, planning, inspection, and customer-service workflows for AI, but most labor remains embodied production work and demand has been declining.

## How AI changes the work
AI can reduce clerical touch time, translate specifications into work instructions, improve scheduling and demand planning, draft customer communications, and support camera-based defect detection. Physical machine operation, maintenance, material movement, tactile inspection, and accountability remain human- and equipment-intensive.

## Value capture
Savings can initially accrue to the operator because work is quoted per run, yard, or specification. Competitive bids, powerful dealers, imports, and hard-surface alternatives should pass a meaningful portion back to customers over renewal cycles; retention is better where quality, customization, and turnaround are hard to benchmark.

## Firm availability
The frozen dataset estimates 52 LMM-band firms, but the official code primarily covers product manufacturers. Actual eligibility is likely confined to a minority with repeat external commission or contract-service revenue, and a broad employer-business transfer survey is only a proxy for control availability.

## Demand durability
Replacement demand supplies a recurring base, and commercial or specialty carpet still serves applications where acoustics, comfort, design, or performance matter. Even so, the Federal Reserve output index fell materially through 2025, and hard surfaces, imports, housing turnover, construction, and consumer confidence remain major demand risks.

## Risks and uncertainty
The greatest uncertainty is denominator quality: a product-manufacturing NAICS code and a margin-bridged firm count may leave very few true outsourced-service targets. Other risks are continued volume contraction, customer concentration, capital spending needed for machine vision, legacy data, false defect calls, and rapid competitive pass-through of savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1697 | — | OBSERVED | — |
| n | — | 52 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.24 | PROXY | S2, S3, S4 |
| rho | 0.25 | 0.45 | 0.65 | ESTIMATE | S3, S4, S6 |
| e | 0.05 | 0.12 | 0.25 | ESTIMATE | S1, S6 |
| s5 | 0.08 | 0.16 | 0.25 | PROXY | S5, S6 |
| q | 0.25 | 0.45 | 0.65 | ESTIMATE | S6 |
| d5 | 0.65 | 0.85 | 1.05 | PROXY | S6, S7 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S3, S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.14 | 0.43 | 1.06 | ESTIMATE |
| F | 0.30 | 1.11 | 2.33 | ESTIMATE |
| C | 5.00 | 9.00 | 10.00 | ESTIMATE |
| D | 5.85 | 8.16 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS evidence is for 3141 Textile Furnishings Mills, not six-digit 314110.
- a: Occupation employment counts are not wage weights and do not reveal task shares within occupations.
- a: AI exposure evidence spans economies and occupations rather than U.S. carpet mills specifically.
- rho: No carpet-mill adoption survey separates pilots from production deployments.
- rho: The estimate assumes adequate machine data and digital order records, which may be absent in smaller mills.
- rho: It excludes labor savings from conventional capital equipment unless AI is essential to the workflow.
- e: The dataset firm count is an estimate derived from size classes and a margin bridge, not an observed roster.
- e: Public disclosures from one integrated operator establish existence but not population share.
- e: Some contract manufacturing relationships may be repeat purchases without constituting an outsourced service under the lens.
- s5: Gallup covers all U.S. employer businesses, not manufacturing or LMM carpet mills.
- s5: Plans to sell, gift, or go public are intentions and include transfers outside the qualifying-control definition.
- s5: The eligible population is small, so a few transactions can move the realized rate sharply.
- q: No observed pass-through study exists for commission carpet finishing.
- q: Retention varies sharply by customer concentration, differentiation, capacity utilization, and whether work is cost-plus or competitively bid.
- q: The estimate excludes volume effects, which belong in demand primitives.
- d5: The Federal Reserve series is five-digit 31411 and measures all carpet/rug output, not the narrowed service subset.
- d5: The 2021 comparison point was affected by pandemic-era housing and remodeling conditions.
- d5: A public company filing may reflect its own market framing and cites trade-association information not independently reproduced here.
- o: This estimate conditions on demand already surviving in d5 and avoids counting hard-surface substitution twice.
- o: Operator requirement could fall faster for standardized printing than for small-batch custom finishing.
- o: No direct survey measures self-service or software-only displacement for this physical production service.

## Sources
- **S1** — [2022 NAICS Definition: 314110 Carpet and Rug Mills](https://www.census.gov/naics/?details=31411&input=31411&year=2022) (accessed 2026-07-22): Defines the industry as establishments manufacturing woven, tufted, and other carpets and rugs and/or finishing carpets and rugs; supports the lens mismatch and eligibility judgment.
- **S2** — [BLS OEWS Data Tables for Industry Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest occupations in Textile Furnishings Mills, including 5,870 sewing machine operators, 4,260 winding/twisting operators, 2,970 knitting/weaving operators, 1,820 production supervisors, 1,720 industrial truck operators, and other physical production roles.
- **S3** — [Artificial Intelligence and the Changing Demand for Skills in the Labour Market](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/04/artificial-intelligence-and-the-changing-demand-for-skills-in-the-labour-market_861a23ea/88684e36-en.pdf) (accessed 2026-07-22): Finds high-skill cognitive occupations most exposed and non-routine physical occupations least exposed; lists textile pressers among the five least AI-exposed occupations and cautions that exposure measures have not been shown to equal adoption.
- **S4** — [BLS Occupational Outlook Handbook: Quality Control Inspectors](https://www.bls.gov/ooh/production/quality-control-inspectors.htm) (accessed 2026-07-22): Describes inspection tasks, automated vision systems, and 3D scanners; projects little or no employment change through 2034 because technology automates some but not all inspection and validation tasks.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Gallup's fall-2024 U.S. survey of 1,264 working business owners reports that 22% of employer-business owners planned to sell or transfer ownership within five years and that 52.3% of employer businesses were owned by people age 55 or older.
- **S6** — [Live Ventures Incorporated 2024 Form 10-K](https://ir.liveventures.com/annual-reports/content/0001628280-24-052099/0001628280-24-052099.pdf) (accessed 2026-07-22): Identifies commission carpet coating/finishing and contract commission printing business lines; reports about $11.4 billion of 2023 carpet/rug shipments, about 52% tied to residential replacement, fewer than 100 domestic manufacturers, and competition based on service, quality, price, innovation, and technology.
- **S7** — [Industrial Production: Carpet and Rug Mills (NAICS 31411)](https://fred.stlouisfed.org/series/IPG31411A) (accessed 2026-07-22): Federal Reserve annual real-output index reported 86.4779 for 2021, 86.8040 for 2022, 77.2588 for 2023, 73.7997 for 2024, and 70.4170 for 2025.
