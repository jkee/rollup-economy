# 458310 — Jewelry Retailers

*v5.1 Stage 1 research memo. Run `458310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Trust-based repair, appraisal, and custom work creates a repeat service relationship while AI can streamline the surrounding sales and administrative load.
**Weakness:** Service revenue is unmeasured and may be too incidental at many jewelry retailers, while skilled owner and bench-worker dependence limits both automation and transferability.

## Business-model lens
- Included: Lower-middle-market jewelry retailers with a material repeat service offering to external customers, including jewelry and watch repair, resizing and alteration, cleaning and maintenance, appraisal, gem identification, custom design, and related customer-account work combined with new-jewelry retail.
- Excluded: Product-only jewelry sellers, manufacturer-owned or captive brand stores, pure e-commerce sellers without an accountable service operation, repair-only establishments classified in NAICS 811490, used-jewelry specialists classified elsewhere, and firms outside the normalized EBITDA band.
- Customer and revenue model: Households pay per repair, appraisal, custom project, or merchandise purchase; service-led retailers may generate repeated visits over an item's life and use repairs and maintenance to support long-term trust and merchandise sales.
- Deviation from default lens: The code mixes product-only retail with retailers that combine merchandise sales and skilled repair, appraisal, or custom work. The lens is narrowed to firms where those repeat services are a material external offering so the screen does not treat all jewelry sales as outsourced service.

## Executive view
A meaningful but minority subset of jewelry retailers combines merchandise with repeat repair, appraisal, maintenance, and custom work. AI can improve sales and administrative workflows, yet the skilled physical service core is hard to substitute and owner or bench-jeweler dependence complicates implementation and transfer.

## How AI changes the work
The practical opportunities are product and customer search, marketing, CRM, repair intake, quote preparation, bookkeeping, appraisal-document drafts, inventory support, and CAD ideation. Inspection, gem grading, soldering, stone setting, polishing, secure custody, and trusted customer judgment remain predominantly human; 3D printing and robotic polishing augment only parts of the workflow.

## Value capture
Quoted repair, appraisal, and custom-work fees are less transparent than branded merchandise prices, and reputation supports retention. Savings in selling and merchandising face greater pass-through, while some automation benefit will be reinvested in faster turnaround, customer acquisition, and quality control.

## Firm availability
The NAICS definition permits retail combined with repair, and the occupation mix confirms a substantial skilled workforce, but public data do not reveal how many LMM firms have material repeat service revenue. Broad owner-aging evidence suggests transfers, while reputation and bench-skill concentration can reduce transferability.

## Demand durability
The installed base of jewelry and watches supports ongoing resizing, maintenance, repair, appraisal, and modification. Discretionary spending, imports, channel shifts, and automation pressure employment, but most surviving physical service demand should still need an accountable operator.

## Risks and uncertainty
The main uncertainties are the eligible firm share, the missing firm-count input, use of a 458300 occupation proxy that includes luggage, the ancestor-level labor ratio, limited evidence on completed transfers, and no public real-volume series for jewelry services. Product-led stores with only incidental service would fail the lens.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.15 | 0.24 | 0.35 | PROXY | S2, S3, S4 |
| rho | 0.28 | 0.46 | 0.64 | ESTIMATE | S4, S5 |
| e | 0.16 | 0.31 | 0.48 | ESTIMATE | S1, S2, S6 |
| s5 | 0.14 | 0.23 | 0.33 | PROXY | S5, S7 |
| q | 0.37 | 0.55 | 0.71 | ESTIMATE | S1, S6 |
| d5 | 0.88 | 0.99 | 1.1 | PROXY | S5, S6 |
| o | 0.8 | 0.91 | 0.97 | ESTIMATE | S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.45 | 0.91 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 7.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.04 | 9.01 | 10.00 | ESTIMATE |

## Caveats
- a: The OEWS mix combines jewelry, luggage, and leather-goods retailers and excludes self-employed workers.
- a: O*NET tasks do not supply shoe-specific time shares or distinguish already-automated work.
- a: The dataset labor ratio is only available at ancestor 44-45, uses 2024 wages over 2022 receipts, and is harmonized to the IPS basis; it may not represent service-led jewelry retailers.
- rho: No source measures five-year AI implementation in the eligible population.
- rho: Automation may increase throughput and reduce queues rather than remove a full position.
- rho: Demand and pricing effects are excluded and addressed separately.
- e: Public data identify allowed activities and occupations but not the share of firms with material repeat service revenue.
- e: The 458300 occupation mix includes luggage and leather-goods retailers.
- e: The provided n input is a declared dataset gap and will be injected as MISSING; it was not replaced or estimated here.
- s5: The Gallup evidence is cross-industry and reports plans rather than completed transfers.
- s5: BLS replacement openings are occupational, not firm-control transfers.
- s5: Deaths without transferable operations and internal reorganizations are excluded.
- q: No direct study measures AI-benefit pass-through in jewelry services.
- q: Retention should be lower for merchandise-facing sales workflows than for skilled repair and appraisal.
- q: Volume loss and operator displacement are excluded here.
- d5: Employment projections conflate demand, productivity, imports, and occupational mix.
- d5: No public series isolates real service transactions at service-led jewelry retailers.
- d5: Metal-price volatility can raise nominal tickets without increasing constant-quality quantity.
- o: No source directly measures software-only substitution for the eligible service basket.
- o: The estimate is conditional on year-five demand and does not double-count demand decline in d5.
- o: Simple cleaning, design visualization, and document drafting are more substitutable than physical repair or certified appraisal.

## Sources
- **S1** — [2022 NAICS Definition: 458310 Jewelry Retailers](https://www.census.gov/naics/?details=458310&input=458310&year=2022) (accessed 2026-07-22): Defines jewelry retailers and expressly includes establishments retailing new jewelry, watches, or clocks in combination with lapidary work or repair services; distinguishes repair-only establishments in 811490.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 458300](https://www.bls.gov/oes/2023/may/naics4_458300.htm) (accessed 2026-07-22): Reports 124,200 total employees; 63.96% sales, 9.89% management, 9.58% office support, 9.07% jewelers and precious-stone or metal workers, and 0.73% watch and clock repairers.
- **S3** — [O*NET OnLine: 41-2031.00 Retail Salespersons](https://www.onetonline.org/link/details/41-2031.00) (accessed 2026-07-22): Lists retail-sales tasks including needs discovery, recommendations, transactions, records, inventory, returns, and product explanation, and documents intensive external-customer interaction.
- **S4** — [O*NET OnLine: 51-9071.00 Jewelers and Precious Stone and Metal Workers](https://www.onetonline.org/link/details/51-9071.00) (accessed 2026-07-22): Lists core skilled tasks including creation, inspection, repair, costing, stone grading, setting, shaping, and computer-assisted design.
- **S5** — [BLS Occupational Outlook Handbook: Jewelers and Precious Stone and Metal Workers](https://www.bls.gov/ooh/production/jewelers-and-precious-stone-and-metal-workers.htm) (accessed 2026-07-22): Describes design, repair, appraisal, CAD/CAM and 3D-printing tasks; reports 35,100 jobs in 2024, a 5% projected decline to 2034, 4,000 annual replacement openings, and productivity pressure from 3D printing and robotic polishing.
- **S6** — [U.S. Census Bureau 2022 Retail Trade Questionnaire: Jewelry Stores](https://bhs.econ.census.gov/ombpdfs2022/export/2022_RT-44831_su.pdf) (accessed 2026-07-22): Separately identifies repair-only businesses as 811490 while asking jewelry stores to report maintenance, repair, and alteration service revenue and listing additive manufacturing and other technologies.
- **S7** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 52.3% of employer businesses owned by people age 55 or older and 22% of employer-business owners planning to sell or transfer ownership within five years.
