# 321215 — Engineered Wood Member Manufacturing

*v5.1 Stage 1 research memo. Run `321215-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → CONDITIONAL · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Quality-critical fabrication plus engineering and project workflows provide multiple implementable AI surfaces while structural demand remains physical.
**Weakness:** The missing defensible LMM firm count prevents reliable sizing of the transferable-firm opportunity.

## Business-model lens
- Included: Independent U.S. manufacturers repeatedly supplying wood roof and floor trusses, I-joists, laminated veneer lumber, parallel strand lumber, glulam arches and beams, finger-jointed lumber, and related fabricated or laminated structural members to external customers.
- Excluded: Captive plants, prefabricated buildings and wall panels classified elsewhere, solid-sawn structural lumber, stand-alone engineering or installation services, non-operating entities, and firms without transferable operations.
- Customer and revenue model: Repeat standardized and project-specific member sales to builders, component dealers, distributors, lumberyards, developers, fabricators, and commercial construction teams, often combining product pricing with design tables, shop drawings, takeoffs, and delivery coordination.
- Deviation from default lens: none

## Executive view
Engineered wood members combine labor-intensive fabrication with quality-critical structural performance and design-support workflows, creating credible AI opportunities in inspection, optimization, maintenance, estimating, drawings, scheduling, and customer service. The major analytical weakness is the declared absence of a defensible LMM firm count, so transferable-firm opportunity cannot be sized from this packet.

## How AI changes the work
Computer vision and scanning can detect defects and process variation; optimization can improve cuts, layups, and schedules; models can assist takeoffs, quotations, design checks, and documentation. Human and organizational accountability remains necessary for structural engineering, audited quality, code compliance, production exceptions, maintenance, and product liability.

## Value capture
Custom engineering support, audited quality, reliable delivery, and material yield can protect some gains. Standardized performance and competitive builder procurement still drive repricing, particularly in high-volume trusses, I-joists, and LVL.

## Firm availability
The code includes many truss operations alongside a smaller set of capital-intensive laminated-member manufacturers, but the frozen dataset has no defensible LMM-band count. Eligibility and succession shares are estimable only as broad judgments and cannot restore that missing denominator.

## Demand durability
Residential framing, remodeling, and nonresidential long-span applications support durable physical demand and possible share gains. Cyclical construction, alternative materials, and code or fire concerns create downside, while almost all surviving volume still requires an accountable manufacturer.

## Risks and uncertainty
Key uncertainties are the missing LMM denominator, ownership concentration, different economics of truss shops and laminated-member mills, construction cyclicality, installed automation, model validation for structural quality, codes and audits, resin and lumber costs, customer concentration, and benefit pass-through.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.212 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.25 | 0.36 | PROXY | S1, S2, S3, S4 |
| rho | 0.35 | 0.54 | 0.7 | ESTIMATE | S2, S3, S4 |
| e | 0.58 | 0.75 | 0.88 | ESTIMATE | S4, S5 |
| s5 | 0.15 | 0.27 | 0.42 | PROXY | S8 |
| q | 0.4 | 0.59 | 0.76 | ESTIMATE | S4, S5 |
| d5 | 0.9 | 1.07 | 1.27 | PROXY | S5, S6, S7 |
| o | 0.97 | 0.99 | 1 | ESTIMATE | S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.47 | 1.14 | 2.14 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.73 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS combines veneer, plywood, and multiple engineered wood products.
- a: The code combines local custom truss fabrication with capital-intensive laminated-member production, so task mix varies materially.
- rho: Assistance in structural design requires professional and manufacturer accountability even when models generate work product.
- rho: Large integrated mills and local truss shops have very different implementation capacity.
- e: The frozen dataset explicitly has no defensible LMM-band firm count; this share does not replace or imply one.
- e: The 2022 code includes both former truss manufacturing and other engineered-member manufacturing, with different ownership structures.
- s5: No denominator of eligible LMM firms exists for this industry.
- s5: Retirement intent is not an observed transaction rate and the proxy is not industry-specific.
- q: Custom curved glulam and project trusses can retain more benefit than standardized I-joists or LVL.
- q: No public study measures five-year pass-through of implemented AI benefits in this industry.
- d5: NAHB covers only part of the horizon and is not a product shipment forecast.
- d5: The code includes trusses, which may track local housing starts differently from LVL, I-joists, and custom glulam.
- o: Digital design platforms could shift some service content away from manufacturers without eliminating physical production.
- o: Material substitution affects quantity in d5 and the operator type supplying remaining demand.

## Sources
- **S1** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-23): Lists leading occupations in broader veneer, plywood, and engineered-wood manufacturing, dominated by assemblers, machine operators, material movers, truck operators, supervisors, drivers, and related plant roles.
- **S2** — [VisionSmart Machine Vision for Engineered Woods](https://www.visionsmart.com/) (accessed 2026-07-23): Describes turn-key machine-vision and optimization systems for LVL, LSL, plywood, OSB, and other engineered wood products.
- **S3** — [Machine Vision Activities in the Wood Industry](https://www.automate.org/vision/industry-insights/machine-vision-activities-in-the-wood-industry) (accessed 2026-07-23): Documents scanning, grading, dimension control, predictive monitoring, defect classification, and optimization across veneer, plywood, LVL, and related wood processing.
- **S4** — [321215: Engineered Wood Member Manufacturing - Census Bureau Profile](https://data.census.gov/profile/321215_-_Engineered_Wood_Member_Manufacturing?codeset=naics~321215&g=050XX00US40151) (accessed 2026-07-23): Defines the industry to include fabricated or laminated arches, trusses, I-joists, LVL, parallel strand lumber, glulam, and related structural members.
- **S5** — [I-Joist - APA The Engineered Wood Association](https://www.apawood.org/i-joist) (accessed 2026-07-23): Describes I-joist composition, residential and light-commercial applications, performance standards, code recognition, design tools, and audited quality marks.
- **S6** — [Market Research - APA The Engineered Wood Association](https://www.apawood.org/market-research) (accessed 2026-07-23): Identifies housing starts, permits, remodeling, and nonresidential construction as demand indicators and tracks production and demand for glulam, I-joists, and LVL.
- **S7** — [2026 Housing Outlook: Ongoing Challenges, Cautious Optimism and Incremental Gains](https://www.nahb.org/news-and-economics/press-releases/2026/02/2026-housing-outlook-ongoing-challenges-cautious-optimism-and-incremental-gains) (accessed 2026-07-23): Forecasts single-family starts up 1% in 2026 and 5% in 2027 and real remodeling activity up 3% and 2%, respectively.
- **S8** — [Ward Lumber Transitions Ownership to Employees](https://www.sba.gov/success-stories/ward-lumber-transitions-ownership-employees-thanks-sba-resource-partner) (accessed 2026-07-23): A lumber-sector succession case citing regional surveys where 57% of owners sought retirement within five years and fewer than one in five had a credible succession plan.
