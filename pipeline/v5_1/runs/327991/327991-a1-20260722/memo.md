# 327991 — Cut Stone and Stone Product Manufacturing

*v5.1 Stage 1 research memo. Run `327991-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.67 · L 1.33 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Bundled custom-project pricing creates room to retain gains from automating fragmented quoting and coordination work.
**Weakness:** Most labor is physical and exception-heavy, while demand is cyclical and exposed to cheaper substitute surfaces.

## Business-model lens
- Included: US lower-middle-market firms that repeatedly template, cut, finish, and fabricate stone products to customer specifications, including countertop, architectural, monument, and commercial stone work sold to external customers.
- Excluded: Quarries, stone wholesalers and retailers without fabrication, captive fabrication units, installation-only contractors classified elsewhere, shells, and non-control financing vehicles.
- Customer and revenue model: Project and repeat-order revenue from builders, remodelers, designers, institutions, and end customers, commonly quoted per square foot or as a fixed project price covering material, fabrication, options, and sometimes installation.
- Deviation from default lens: none

## Executive view
Cut-stone fabrication combines a highly physical production core with a smaller but meaningful layer of quotable, schedulable, document-heavy work. AI is more likely to tighten the office and planning system around the shop than to replace cutting, finishing, handling, and final quality accountability.

## How AI changes the work
Near-term use cases are quote intake, drawing and takeoff assistance, option configuration, scheduling, purchasing, customer updates, collections, sales follow-up, and management reporting. Human checks remain essential because unique materials, site measurements, breakage, seams, and finish quality create costly exceptions.

## Value capture
Bundled fixed or per-square-foot pricing can retain early productivity gains, but transparent comparison among local fabricators and frequent project rebidding should pass a material share to customers over time.

## Firm availability
A brokered market exists for small manufacturers, but eligibility and transferability are uncertain at the target size. Equipment, property, owner relationships, and environmental and safety diligence can complicate control transfers.

## Demand durability
The current basket remains tied to construction and remodeling. Physical demand may be roughly flat over five years, with downside from housing weakness and substitute materials and upside from renewed housing turnover and renovation.

## Risks and uncertainty
The largest evidence gaps are the true occupation/time mix, the share of firms with repeat B2B revenue, and realized post-automation margins. Material substitution, silica and safety compliance, tariff exposure, cyclicality, and rework liability could overwhelm office productivity gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2755 | — | OBSERVED | — |
| n | — | 428 | — | ESTIMATE | — |
| a | 0.12 | 0.22 | 0.32 | PROXY | S1, S2 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S2, S3 |
| e | 0.35 | 0.55 | 0.75 | ESTIMATE | — |
| s5 | 0.1 | 0.18 | 0.28 | PROXY | S4, S5 |
| q | 0.42 | 0.58 | 0.72 | PROXY | S6, S7 |
| d5 | 0.88 | 1 | 1.12 | PROXY | S8, S9 |
| o | 0.84 | 0.93 | 0.98 | ESTIMATE | S1, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.46 | 1.33 | 2.54 | ESTIMATE |
| F | 4.46 | 6.06 | 7.25 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | PROXY |
| D | 7.39 | 9.30 | 10.00 | ESTIMATE |

## Caveats
- a: Stonemasons include construction workers and do not exactly represent manufacturing employees.
- a: No industry-specific time-use study separates already automated CNC work from not-yet-automated tasks.
- a: The injected compensation ratio uses 2024 wages over 2022 receipts and is harmonized to the IPS basis as stated in the assignment.
- rho: This is implementation judgment, not an observed five-year adoption rate.
- rho: Anthropic usage data overrepresent digital occupations and do not measure stone-shop deployment.
- e: The injected 428-firm count is a margin-bridged ESTIMATE and not a directly observed EBITDA-band census.
- e: NAICS establishments do not disclose repeat revenue or customer concentration in public data.
- s5: Marketplace transactions are not a census and skew toward smaller businesses.
- s5: The Census owner-age table is economy-wide, not stone-manufacturing-specific.
- s5: Internal family transfers and asset-only shutdown sales are difficult to distinguish in public data.
- q: Countertop pricing is only one segment of the NAICS code.
- q: Public quotes do not reveal negotiated contractor discounts or renewal behavior.
- q: The range excludes volume loss and implementation difficulty as required.
- d5: Dimension stone excludes engineered quartz and other fabricated materials handled by some shops.
- d5: Construction spending is nominal and broader than the service basket.
- d5: Tariffs, interest rates, and housing turnover add substantial five-year cyclicality.
- o: The estimate distinguishes operator requirement from labor intensity; automation may reduce headcount without eliminating the operator.
- o: Substitution toward laminate, porcelain, resin-agglomerated stone, and standardized modules could reduce custom operator demand faster than assumed.

## Sources
- **S1** — [O*NET OnLine: Stonemasons (47-2022.00)](https://www.onetonline.org/link/details/47-2022.00) (accessed 2026-07-23): Lists core physical tasks including setting, cutting, shaping, polishing, drilling, and moving stone; also reports lower-scored administrative and computer activities used to bound AI-exposed work.
- **S2** — [Anthropic Economic Index report: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report) (accessed 2026-07-23): Reports that physical occupation categories such as construction and material moving are underrepresented in Claude use and cautions that its user survey is not workforce-representative.
- **S3** — [Anthropic Economic Index: Uneven geographic and enterprise AI adoption](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) (accessed 2026-07-23): Reports that first-party API use is automation-dominant and especially oriented toward coding and office/administrative tasks, supporting implementability for digital workflows rather than physical fabrication.
- **S4** — [Manufacturing Business Valuation Multiples & Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/manufacturing/) (accessed 2026-07-23): Reports 2,303 sold manufacturing listings analyzed for 2021-2025, median revenue of $1,127,990, median owner earnings of $268,321, and median 2025 sale price of $650,000.
- **S5** — [Annual Business Survey: Characteristics of Business Owners, 2022 Tables](https://www.census.gov/data/tables/2022/econ/abs/2022-abs-characteristics-of-owners.html) (accessed 2026-07-23): Provides economy-wide employer-business owner characteristics including the Age of Owner table, used only as a broad succession anchor.
- **S6** — [Countertop Granite Astoria pricing page](https://www.cabinetset.com/countertop-granite-astoria) (accessed 2026-07-23): Shows a per-square-foot price including material, fabrication, installation, a template visit, basic edges, and one sink cutout, with final job-site verification.
- **S7** — [How Do Fabricators Price Countertops?](https://slabwise.com/questions/how-price-countertop) (accessed 2026-07-23): Describes prevailing per-square-foot quotes that bundle material, fabrication, standard edge work, cutouts, templating, installation, and sealing.
- **S8** — [USGS Mineral Commodity Summaries 2026: Stone (Dimension)](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-stone-dimension.pdf) (accessed 2026-07-23): States that US dimension-stone sales were estimated to have decreased each year since 2022, discusses housing and construction conditions, and lists material substitutes.
- **S9** — [US Census Bureau: Monthly Construction Spending, May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-23): Reports total May 2026 construction spending 1.5% below May 2025 and first-five-month spending 2.7% below the comparable 2025 period, with residential and nonresidential detail.
