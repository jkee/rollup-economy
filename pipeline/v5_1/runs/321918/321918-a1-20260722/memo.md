# 321918 — Other Millwork (including Flooring)

*v5.1 Stage 1 research memo. Run `321918-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.46 · L 1.39 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Automation of takeoff-to-CNC information flow plus yield, rework, and scheduling improvements in repeat custom millwork programs.
**Weakness:** The code mixes attractive service-like custom fabrication with excluded standardized flooring and product manufacturing, making the true eligible pool uncertain.

## Business-model lens
- Included: US lower-middle-market firms repeatedly providing outsourced, specification-driven architectural millwork production, including custom molding, trim, ornamental woodwork, stairwork, shutters, and closely related made-to-order components for external builders, dealers, architects, and contractors.
- Excluded: Standard wood flooring and stock millwork sold as products without an outsourced-service relationship, on-site construction fabrication, wood windows and doors, cut stock, captive shops, pure distributors, software vendors, and non-control financing vehicles.
- Customer and revenue model: Eligible firms earn repeat B2B revenue by engineering and fabricating customer- or project-specific millwork, commonly through quotes, purchase orders, builder programs, and project releases; commodity or branded flooring sales are excluded for coherence.
- Deviation from default lens: The code combines custom architectural millwork with standardized wood flooring and stock products. The lens is narrowed to recurring specification-driven millwork fabrication because flooring's product, retail, and consumer-demand economics are too different for a coherent single screen; the narrowing is based on business-model coherence, not attractiveness.

## Executive view
Custom architectural millwork has substantial information-heavy labor around takeoffs, drawings, submittals, quoting, programming, and project coordination, alongside physical machining and finishing. That combination creates meaningful AI opportunity. The NAICS code is heterogeneous, however, so the coherent lens excludes standardized flooring and stock products and focuses on recurring specification-driven fabrication.

## How AI changes the work
AI can interpret plans, draft takeoffs, generate quotes and submittals, assist CNC programming and nesting, schedule jobs, detect finish or dimensional defects, and support maintenance and customer communication. Existing CAD/CAM provides a foundation. Irregular geometry, material variation, sanding, finishing, assembly, handling, and project exceptions keep humans and specialized equipment central.

## Value capture
Fixed-price custom projects can retain gains from faster engineering, better yield, fewer errors, and lower rework because customers buy a finished specification and schedule rather than disclosed labor hours. Repeat builder procurement and rebidding eventually share visible savings. Complexity, service reliability, and execution quality are the main defenses against price-only competition.

## Firm availability
The supplied LMM estimate is 285 firms, but flooring and stock-product firms must be removed before assessing the acquisition pool. Custom millwork is fragmented and often founder-led, supporting succession potential, yet relationships, estimating judgment, and craftsmanship may be concentrated in the owner and reduce transferability.

## Demand durability
Demand follows residential and commercial construction, remodeling, restoration, and design preferences. Medium-term housing forecasts provide support, while current remodeling softness, rates, credit, imports, and substitution to simpler or non-wood finishes create downside. Physical custom output still requires an accountable fabricator even when design and production planning become highly automated.

## Risks and uncertainty
The chief risks are code heterogeneity, uncertain lens eligibility, project cyclicality, bespoke data, owner dependence, implementation gaps between office and shop, safety, and aggressive builder procurement. The thesis weakens if eligible firms lack repeat customers, drawings cannot be standardized, rework is already low, or project buyers extract all productivity gains through rebidding.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1924 | — | OBSERVED | — |
| n | — | 285 | — | ESTIMATE | — |
| a | 0.28 | 0.41 | 0.54 | PROXY | S2, S3, S4, S5 |
| rho | 0.25 | 0.44 | 0.62 | ESTIMATE | S3, S4, S6, S7 |
| e | 0.2 | 0.36 | 0.53 | ESTIMATE | S1, S8 |
| s5 | 0.1 | 0.17 | 0.26 | PROXY | S9 |
| q | 0.34 | 0.54 | 0.72 | ESTIMATE | S8 |
| d5 | 0.87 | 1.04 | 1.2 | PROXY | S10, S11, S12 |
| o | 0.86 | 0.94 | 0.99 | ESTIMATE | S1, S3, S4, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.54 | 1.39 | 2.58 | ESTIMATE |
| F | 3.06 | 4.69 | 5.94 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.48 | 9.78 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupation-by-task study isolates custom millwork from flooring.
- a: Automation vendors describe technical capability rather than measured labor substitution.
- a: The supplied compensation ratio uses 2024 wages over 2022 receipts and is harmonized to an IPS basis.
- rho: No representative five-year implementation cohort was found.
- rho: AI adoption evidence covers all US businesses rather than millwork firms.
- rho: A 2024 recordable injury rate of 4.0 per 100 workers increases the burden of safe shop-floor deployment.
- e: NAICS does not publish firm counts by custom versus stock revenue model.
- e: Project-specific products are not necessarily recurring outsourced services.
- e: The supplied firm count is a margin-bridged estimate based on 2022 receipts and a January 2026 sector margin.
- s5: Stated plans are not completed transactions.
- s5: The Gallup sample spans industries and smaller businesses.
- s5: Gifts and rare IPOs in the source category may not qualify.
- q: Builders FirstSource is a much larger customer and competitor than target firms.
- q: No study directly observes retention of AI-created benefit in custom millwork.
- q: Capture is lower in standardized moldings and higher in complex architectural packages.
- d5: Housing starts are an imperfect proxy for repair, remodel, and commercial custom millwork.
- d5: The Harvard indicator is nominal and only four quarters forward.
- d5: Flooring market data mainly illuminate cyclicality and substitution, not the narrowed service quantity.
- o: The excluded flooring segment has different substitution dynamics.
- o: Some digital fabrication platforms could consolidate rather than eliminate the accountable operator.
- o: No direct customer survey measures future insourcing or self-service for custom millwork.

## Sources
- **S1** — [North American Industry Classification System: Manufacturing definitions](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines NAICS 321918 and lists molding, ornamental woodwork, stairwork, flooring, and shutters while excluding windows, doors, and cut stock.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Shows the broader other-wood-product workforce is concentrated in assemblers, woodworking and sawing machine operators, material movers, supervisors, carpenters, drivers, sales, and managers.
- **S3** — [Cabinet Design Software and CNC Manufacturing Automation](https://www.microvellum.com/) (accessed 2026-07-22): Documents CAD-based design and integration with CNC machinery for custom cabinetry and commercial millwork production.
- **S4** — [Custom Woodworking Equipment and Custom Timber Processing Machines](https://www.mereen-johnson.com/industries/custom-millwork-machines/) (accessed 2026-07-22): Describes CNC contouring, machine tending, vision-guided sorting, stacking, palletizing, and conveying for custom millwork, while noting irregular geometry makes automation difficult.
- **S5** — [O*NET: Helpers--Production Workers](https://www.onetonline.org/link/summary/51-9198.00) (accessed 2026-07-22): Documents physical loading, machine operation, inspection, monitoring, packing, recordkeeping, and material-movement tasks.
- **S6** — [Only 3.8% of Businesses Use AI to Produce Goods and Services](https://www.census.gov/library/stories/2023/11/businesses-use-ai.html) (accessed 2026-07-22): Reports 3.8% current US business AI use and 6.5% planned use within six months in late 2023, indicating a low adoption base.
- **S7** — [BLS Table 1: Incidence rates of nonfatal occupational injuries and illnesses by industry, 2024](https://www.bls.gov/web/osh/table-1-industry-rates-national.htm) (accessed 2026-07-22): Reports a total recordable rate of 4.0 cases per 100 full-time workers for NAICS 321918 in 2024.
- **S8** — [Builders FirstSource 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1316835/000119312526054643/bldr-20251231.htm) (accessed 2026-07-22): Describes custom millwork such as intricate moldings, stair parts, and columns, long-term builder relationships, competitive pricing, service, multiple suppliers, and robust competition.
- **S9** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 14% of working small-business owners planned a sale, IPO, or transfer within five years, rising to 17% among owners age 55 or older.
- **S10** — [The Outlook for Housing Starts](https://www.cbo.gov/publication/60727) (accessed 2026-07-22): Projects housing starts averaging 1.68 million annually in 2025-2029 and 1.52 million in 2030-2033, with financial and demographic uncertainty.
- **S11** — [Leading Indicator of Remodeling Activity](https://www.jchs.harvard.edu/research-areas/remodeling/lira) (accessed 2026-07-22): Projects owner-occupied improvement and maintenance spending growth to slow sharply in early 2027 and states the measure is nominal with a four-quarter horizon.
- **S12** — [Mohawk Industries 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/851968/000085196826000011/mhk-20251231.htm) (accessed 2026-07-22): Reports wood flooring at 12.5% of 2024 US flooring sales but 5.2% of square feet, and documents housing, remodeling, price, import, and substitution pressures.
