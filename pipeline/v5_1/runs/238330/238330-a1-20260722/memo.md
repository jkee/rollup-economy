# 238330 — Flooring Contractors

*v5.1 Stage 1 research memo. Run `238330-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.17 · L 0.81 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is the ability to automate estimating and project administration around a durable, locally delivered physical service.
**Weakness:** The principal weakness is that hands-on installation dominates employment while transfer and benefit-retention evidence is indirect.

## Business-model lens
- Included: US lower-middle-market contractors installing, replacing, sanding, finishing, and refinishing resilient flooring, carpet, linoleum, and hardwood for property owners, general contractors, retailers, property managers, and other external customers, including residential and commercial new work, alterations, maintenance, and repair.
- Excluded: Retail-led sale and installation classified outside NAICS 238330; ceramic tile, stone, terrazzo, concrete, and epoxy-flooring trades classified elsewhere; captive internal crews; shell entities; non-control financing vehicles; and operations outside the stated EBITDA band.
- Customer and revenue model: Project revenue is earned through competitively quoted lump-sum or unit-price installation, replacement, repair, and refinishing work. Individual projects are episodic, but the service recurs through flooring wear, tenant turnover, remodeling, new construction, and repeat relationships with general contractors, retailers, property managers, and owners.
- Deviation from default lens: none

## Executive view
Flooring contracting remains a site-bound trade whose most plausible AI gains sit around the crew: estimating and takeoff, lead response, scheduling, purchasing, customer communication, billing, collections, and project documentation. The underlying installation service should persist, but the physical labor base limits the share of wages addressable by current AI, and project-by-project competition limits long-run retention of visible cost savings.

## How AI changes the work
AI can turn plans, photos, measurements, product specifications, and historical jobs into draft takeoffs, quotes, schedules, purchase lists, customer updates, and closeout records. It can also triage leads, draft bid responses, flag job-cost variance, and reduce clerical workload. Human review remains essential because substrate condition, moisture, pattern, waste, occupied-site constraints, material availability, and workmanship determine final cost and quality, while cutting, fitting, adhesion, sanding, and finishing remain physical.

## Value capture
Signed fixed-price work can preserve a near-term productivity gain, especially when the benefit appears as faster response, fewer errors, better crew utilization, or avoided overhead hiring. Later bids expose the gain to unit-price competition and procurement pressure, and cost-plus or open-book work shares savings more directly. Retention therefore depends on customer channel, backlog, local competition, and whether the operator converts efficiency into service quality and capacity rather than price cuts.

## Firm availability
The NAICS definition is tightly aligned with outsourced installation and repair, so most firms in the supplied LMM band should be eligible after excluding miscoded, captive, or nontransferable operations. Broad owner-aging evidence and reported construction-business sales support a real transfer pipeline, but neither source gives a flooring-specific denominator. Owner dependence, informal books, subcontractor relationships, licensing, and customer concentration may turn apparent firms into closures rather than transferable operations.

## Demand durability
Floor replacement, renovation, tenant turnover, damage repair, and new construction create repeat industry demand. BLS projects modest overall occupational growth while showing product substitution away from carpet toward resilient flooring and continued tile demand. The current outsourced basket should still require a responsible installer in five years because the work is physical, local, variable, and warranty-sensitive, though cycles and do-it-yourself products create downside.

## Risks and uncertainty
The occupation mix is available only at a parent NAICS level, AI adoption evidence is cross-industry, owner-age evidence is broad and dated, reported sales lack a denominator, and contract evidence comes from residential builders using a particular platform. Flooring firms also vary by residential versus commercial mix, employees versus subcontractors, product mix, retailer relationships, and owner involvement. A weak case would emerge if firm-level time studies show little overhead labor, if efficiency is rapidly competed into bids, or if sale-ready companies are much rarer than the supplied count implies.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2246 | — | ESTIMATE | — |
| n | — | 70 | — | ESTIMATE | — |
| a | 0.12 | 0.18 | 0.28 | PROXY | S2, S3 |
| rho | 0.3 | 0.5 | 0.7 | PROXY | S4 |
| e | 0.78 | 0.9 | 0.97 | ESTIMATE | S1 |
| s5 | 0.1 | 0.2 | 0.32 | PROXY | S6, S7 |
| q | 0.35 | 0.55 | 0.72 | PROXY | S5 |
| d5 | 0.92 | 1.03 | 1.12 | PROXY | S8 |
| o | 0.85 | 0.94 | 0.98 | PROXY | S3, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.32 | 0.81 | 1.76 | ESTIMATE |
| F | 3.00 | 4.20 | 5.02 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | PROXY |
| D | 7.82 | 9.68 | 10.00 | PROXY |

## Caveats
- a: OEWS publishes the needed mix at parent NAICS 238300 and excludes self-employed workers.
- a: Task exposure is a bounded translation from occupational duties, not a measured displacement share.
- a: Computer vision and measurement tools may expand exposure, but unstructured job sites constrain substitution of installation labor.
- rho: BTOS covers all nonfarm sectors and asks whether any business function used AI, not how much labor opportunity was implemented.
- rho: Small flooring contractors may have weaker data integration and training capacity than the national business population.
- rho: The range excludes pricing, demand, and valuation effects.
- e: No source directly measures eligibility under the frozen lens.
- e: The supplied count is an estimate created from broader datasets and margin assumptions.
- e: Project-based revenue can still meet the repeat-outsourcing lens, but repeat-customer intensity varies materially by residential, commercial, and channel mix.
- s5: The Census owner-age figure covers responding owners across employer industries and has a 2018 reference year.
- s5: BizBuySell transactions are voluntarily reported, span broad building and construction categories, and skew toward marketable firms.
- s5: Owner retirement intent does not imply a completed qualifying transfer.
- q: The source population is residential builders and remodelers using one software platform, not a representative flooring-contractor sample.
- q: Retention varies with residential versus commercial mix, subcontractor channel, backlog, local competition, and whether customers can observe the cost change.
- q: This estimate addresses benefit sharing and repricing only, not implementation difficulty or demand loss.
- d5: The BLS occupational group includes tile and stone setters, while tile and stone contracting is classified outside NAICS 238330.
- d5: Employment is affected by productivity and labor supply and is not a direct quantity-demand measure.
- d5: Construction demand is cyclical and differs sharply across carpet, resilient flooring, hardwood, residential, and commercial work.
- o: Current task content is not a forecast.
- o: Click-lock products and retailer-led installation can shift some demand away from standalone contractors.
- o: The estimate concerns continued need for an accountable operator, not the amount of human labor inside that operator.

## Sources
- **S1** — [238330: Flooring Contractors - Census Bureau Profile](https://data.census.gov/profile/238330_-_Flooring_Contractors?codeset=naics~238330&g=010XX00US) (accessed 2026-07-22): Defines NAICS 238330 as installation of resilient floor tile, carpeting, linoleum, and hardwood, including new work, alterations, maintenance, and repairs; lists adjacent and retail-led activities classified elsewhere.
- **S2** — [Building Finishing Contractors - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_238300.htm) (accessed 2026-07-22): Reports parent-industry employment and wages, including construction and extraction at 70.96% of employment, management at 5.32%, business and financial operations at 4.63%, sales at 2.94%, and office support at 8.59%.
- **S3** — [47-2042.00 - Floor Layers, Except Carpet, Wood, and Hard Tiles](https://www.onetonline.org/link/details/47-2042.00) (accessed 2026-07-22): Documents core floor-layer tasks such as surface preparation, cutting, inspecting, measuring, fitting, applying adhesive, and finishing; reports continual hand use for 89% of respondents and identifies estimating and project-management software.
- **S4** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports nationally representative BTOS evidence: 19.8% of businesses used AI as of May 3, 2026, adoption rose with firm size, and fewer than 20% of firms with at most four employees reported use.
- **S5** — [Fixed Price Projects Have 28% Higher Average Profit Margins](https://www.coconstruct.com/blog/fixed-price-projects-have-28-higher-average-profit-margins) (accessed 2026-07-22): Analyzes more than 60,000 US residential construction projects, reports builders used fixed-price contracts 80% of the time, defines fixed-price and open-book contracts, and shows different project-margin behavior.
- **S6** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were at least age 55 in the 2019 Annual Business Survey, with data year 2018 and stated population limitations.
- **S7** — [Construction Business Valuation Multiples & Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/building-construction/) (accessed 2026-07-22): Reports 3,142 building and construction businesses sold on or reported to BizBuySell, a median 207 days on market, and transaction observations that include flooring among the represented specialty services.
- **S8** — [Flooring Installers and Tile and Stone Setters](https://www.bls.gov/ooh/construction-and-extraction/tile-and-marble-setters.htm) (accessed 2026-07-22): Describes physical duties and requirements, projects 6% employment growth from 2024 to 2034, identifies new homes and renovation as primary demand sources, and reports divergent outlooks across carpet, resilient flooring, and tile occupations.
