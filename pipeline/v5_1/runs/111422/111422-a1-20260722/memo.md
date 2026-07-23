# 111422 — Floriculture Production

*v5.1 Stage 1 research memo. Run `111422-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** High labor intensity and controlled-environment data create practical opportunities for sensing, decision support, planning, and selective automation.
**Weakness:** The transferable LMM population is unobserved, and buyer power plus seasonal, perishable demand can erode the share of efficiency gains retained by growers.

## Business-model lens
- Included: Independently managed US commercial growers primarily producing cut flowers and roses, florist greens, potted flowering and foliage plants, bedding and garden plants, and floriculture propagative material under cover or in open fields, with repeat sales to external wholesalers, retailers, landscapers, florists, institutions, or consumers.
- Excluded: Retail florists and garden centers primarily reselling plants purchased from others; nursery and tree production; captive internal growing units; hobby growers; passive greenhouse or landholding interests; shells; and operations without a transferable production business.
- Customer and revenue model: Revenue comes from seasonal and recurring wholesale or retail sales of live plants, flowers, greens, and unfinished propagation material. Pricing reflects species and cultivar, format, quality, timing, availability, customer channel, and contract or spot terms; biological inventory is perishable and demand peaks around planting and gift occasions.
- Deviation from default lens: The NAICS activity produces physical crops rather than supplying an outsourced service. The closest coherent population retained is independently managed commercial floriculture growers with repeat external sales; resale-only retailers and noncommercial growers are excluded because they do not represent the classified production operation.

## Executive view
Floriculture is a labor-intensive physical-production industry with repeat external sales, not an outsourced service. AI-enabled sensing, disease detection, planning, inventory, and office automation can reduce avoidable labor and shrink, particularly in larger greenhouse operations, but many propagation and handling tasks remain physical. Differentiation offers more value retention than bulk row crops, while buyer power, imports, perishability, and seasonality constrain it. Missing compensation and LMM-firm-count inputs are central gaps in sizing the opportunity.

## How AI changes the work
The strongest applications are machine-vision crop and disease inspection, sensor-informed climate and irrigation control, production scheduling, demand forecasting, inventory and shrink management, quality documentation, purchasing, and order administration. USDA-supported specialty-crop work demonstrates relevant sensing and deep-learning systems, but broad deployment must handle many cultivars, biological variation, equipment integration, and seasonal production cycles. Existing conventional controls are excluded from the new opportunity.

## Value capture
A grower can retain benefits through differentiated products, precise timing, higher sell-through, lower shrink, quality consistency, and direct channels. Large retailers and wholesalers can demand lower prices at renewal, competing growers and imports discipline pricing, and automation vendors can capture savings through equipment and software charges. Retention should therefore vary sharply by channel and product distinctiveness.

## Firm availability
USDA counted 11,728 floriculture producers in 2025, including 8,478 with hired workers, but the survey threshold is far below the target earnings band and the assigned LMM firm count is missing. Broader horticulture is fragmented by operation count but corporate-owned operations account for most sales. Family ownership, real-estate dependence, mixed retail or nursery activity, and owner-specific expertise can prevent an apparent operation from becoming a transferable company.

## Demand durability
Recent USDA data show expansion in floriculture sales, producer count, and covered production area, while broader crop-production real output is projected to rise modestly. Floriculture demand is nevertheless discretionary, seasonal, and exposed to housing and garden spending, events, imports, weather, and changing consumer preferences. Physical production continues to require an accountable operator even where sensing and handling automate.

## Risks and uncertainty
The largest uncertainties are the missing compensation and LMM-count inputs, the lack of floriculture-specific occupation and AI adoption data, nominal rather than real demand observations, wide differences between small owner-operated and large corporate greenhouses, import competition, customer concentration, energy and labor cost volatility, pest and disease losses, perishability, and facility or land value embedded in transactions.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.12 | 0.22 | 0.34 | PROXY | S2, S3, S4, S5 |
| rho | 0.25 | 0.43 | 0.62 | ESTIMATE | S5 |
| e | 0.18 | 0.38 | 0.58 | ESTIMATE | S1, S3, S4 |
| s5 | 0.13 | 0.24 | 0.37 | PROXY | S4, S7 |
| q | 0.12 | 0.27 | 0.45 | ESTIMATE | S3, S5 |
| d5 | 0.88 | 1.06 | 1.24 | PROXY | S3, S6 |
| o | 0.95 | 0.98 | 1 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 2.40 | 5.40 | 9.00 | ESTIMATE |
| D | 8.36 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation mix is for all NAICS 11 industries rather than floriculture production.
- a: The broad horticulture labor-cost share includes nursery and other specialty crops.
- a: BLS occupational estimates exclude self-employed proprietors, while many operations are family or individually owned.
- a: Research prototypes and specialty-crop examples do not establish commercial labor displacement in floriculture.
- rho: The estimate applies only to the exposed task share in a.
- rho: USDA examples span specialty crops and include research-stage systems, not a representative floriculture adoption sample.
- rho: Implementation will vary sharply between large automated greenhouses and small diversified growers.
- e: The assigned LMM establishment-count input is missing, so this share cannot imply a firm count.
- e: USDA thresholds begin far below the target earnings band and operations are not necessarily equivalent to transferable firms.
- e: The broader horticulture ownership statistics include nursery and specialty-crop operations outside NAICS 111422.
- s5: The succession-intention source is cross-industry and measures plans rather than completed deals.
- s5: The family-ownership statistic covers broader horticulture, not floriculture alone.
- s5: Intrafamily succession and asset sales without an operating-company transfer are not qualifying events.
- q: No source directly measures the retained share of AI-enabled gross benefit.
- q: Pricing power varies materially by product differentiation, season, spoilage risk, and customer channel.
- q: Observed sales growth does not identify whether cost savings were retained or passed through.
- d5: The BLS projection covers all crop production rather than NAICS 111422.
- d5: USDA floriculture sales are nominal and include both wholesale and retail sales.
- d5: Recent year-over-year growth may reflect prices, mix, survey revision, or temporary conditions rather than durable quantity growth.
- o: A high operator-required share does not imply that the current workforce or grower identity remains unchanged.
- o: Imports and retailer vertical integration affect domestic operator demand and are only indirectly reflected in d5.

## Sources
- **S1** — [NAICS Sector 11 Definitions: 111422 Floriculture Production](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-22): Industry boundary: growing or producing cut flowers, florist greens, potted flowering and foliage plants, flower seeds, and related floriculture products under cover or in open fields; resale-only retailers are classified elsewhere.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Sector 11](https://www.bls.gov/oes/2023/may/naics2_11.htm) (accessed 2026-07-22): Broad agriculture-sector occupation mix used as a labor-exposure proxy; the page also states that self-employed workers are excluded.
- **S3** — [2025 Floriculture Crops Highlights](https://www.nass.usda.gov/Publications/Highlights/2026/2025FloricultureCrops.pdf) (accessed 2026-07-22): Floriculture producer count, hired-worker operations, peak workers per operation, covered production area, product categories, and nominal sales for 2025 and comparison with 2024.
- **S4** — [U.S. Horticulture Operations Report $18.3 Billion in Sales](https://www.nass.usda.gov/Newsroom/2026/02-26-2026.php) (accessed 2026-07-22): Broader horticulture ownership concentration and cost structure: family or individual operations were 56 percent of operations, corporate operations were 63 percent of sales, and labor was 36 percent of 2024 expenses.
- **S5** — [Automation for Specialty Crops](https://www.nifa.usda.gov/about-nifa/impacts/automation-specialty-crops) (accessed 2026-07-22): Relevant automation applications and constraints, including sensors, imaging, labor-reducing systems, and deep-learning models integrated into nursery and greenhouse devices for disease scanning.
- **S6** — [Industry employment and output projections to 2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Real output for the broader crop-production industry is projected to grow from 175.8 billion chained 2017 dollars in 2024 to 201.8 billion in 2034, a 1.4 percent annual rate.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry US employer-business owner age and five-year sale-or-transfer intentions used only as a succession proxy.
