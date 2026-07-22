# 321912 — Cut Stock, Resawing Lumber, and Planing

*v5.1 Stage 1 research memo. Run `321912-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.65 · L 0.36 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-assisted grading, recovery, line monitoring, and scheduling in recurring specification-driven processing relationships.
**Weakness:** Low compensation intensity and transparent conversion pricing constrain the economic value that can be created and retained.

## Business-model lens
- Included: US lower-middle-market firms repeatedly providing outsourced resawing, surfacing, planing, sizing, grading, cut-stock, or related lumber-processing services to external industrial, distribution, and construction customers.
- Excluded: Commodity lumber or standard cut-stock sales without a recurring processing relationship, sawmills processing logs, captive internal remanufacturing, brokers and distributors without processing, software vendors, and non-control financing vehicles.
- Customer and revenue model: Eligible firms earn repeat B2B revenue by converting purchased or customer-specified lumber into surfaced, resized, graded, or cut stock; pricing may be per board foot, per unit, per processing step, or embedded in a processed-product price.
- Deviation from default lens: none

## Executive view
Cut stock, resawing, and planing has tangible AI opportunities in grading, dimensional inspection, line-flow monitoring, recovery optimization, maintenance, and scheduling. Its low supplied labor ratio limits the gross pool, but its fit with the service lens is better than ordinary product manufacturing where processors repeatedly transform lumber to customer specifications.

## How AI changes the work
AI vision can detect defects and dimensions, assign or support grades, identify skewed or broken boards, and flag flow anomalies. Predictive models can improve maintenance and production sequences, while language systems can automate quotes, orders, certificates, and customer communication. Physical feeding, sawing, planing, stacking, packaging, and intervention still require machinery and accountable people.

## Value capture
Transparent per-board-foot processing and commodity competition make direct labor savings vulnerable to repricing. Better recovery, grade accuracy, throughput, uptime, and turnaround are less visible and more defensible, especially when the operator bears yield risk or solves variable-specification jobs. Contract structure determines who owns the improvement.

## Firm availability
The supplied LMM estimate includes 204 firms, and a meaningful subset may qualify as outsourced processors. General succession data suggest some transfer flow over five years, but named-firm work is required to distinguish toll processors from product manufacturers and to verify owner readiness, transferability, equipment condition, and environmental liabilities.

## Demand durability
Housing starts, repair and remodeling, industrial components, and distribution drive demand. Medium-term housing projections and remodeling's importance support modest growth, although rate sensitivity, tariffs, lumber cycles, reduced wood intensity, imports, and customer insourcing widen the range. Physical lumber conversion remains operator-required even with far more automation.

## Risks and uncertainty
Major risks are low labor intensity, commodity repricing, line-safety exposure, variable inputs, expensive controls integration, scarcity of field deployment data, and ambiguity between service and product revenue. The opportunity weakens if most eligible revenue is standard inventory sales, if customers own all yield benefits, or if plants already use advanced grading and optimization.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0888 | — | OBSERVED | — |
| n | — | 204 | — | ESTIMATE | — |
| a | 0.15 | 0.25 | 0.36 | PROXY | S2, S3, S4, S5 |
| rho | 0.22 | 0.4 | 0.58 | ESTIMATE | S4, S5, S6, S7 |
| e | 0.22 | 0.4 | 0.58 | ESTIMATE | S1 |
| s5 | 0.09 | 0.16 | 0.25 | PROXY | S8 |
| q | 0.22 | 0.4 | 0.58 | ESTIMATE | S9 |
| d5 | 0.9 | 1.07 | 1.22 | PROXY | S10, S11, S12 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.12 | 0.36 | 0.74 | ESTIMATE |
| F | 2.60 | 4.25 | 5.50 | ESTIMATE |
| C | 4.40 | 8.00 | 10.00 | ESTIMATE |
| D | 7.92 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupation-by-task dataset was found.
- a: The strongest grading results use a lab-collected dataset and do not establish field labor savings.
- a: The supplied compensation ratio uses 2024 wages over 2022 receipts and is harmonized to an IPS basis.
- rho: Patent and research evidence show feasibility, not broad commercial adoption.
- rho: Census AI data cover all US businesses rather than planing mills.
- rho: The 2024 recordable injury rate of 5.4 per 100 workers raises the burden of safe integration.
- e: Industry classification does not identify who owns the input lumber or whether processing is contracted as a service.
- e: Made-to-order product sales can resemble toll processing but may not meet the fixed lens.
- e: The supplied firm count is a margin-bridged estimate based on 2022 receipts and a January 2026 sector margin.
- s5: Plans may not close.
- s5: The survey population is broader than industrial LMM firms.
- s5: Its ownership-transfer category contains events excluded by the screen.
- q: The AP evidence concerns construction-material pass-through, not retention of AI savings by planing firms.
- q: No industry study directly measures five-year productivity-benefit retention.
- q: Capture differs between toll conversion and differentiated cut-stock programs.
- d5: CBO projections were published before subsequent policy and immigration changes.
- d5: Softwood-lumber demand is broader than the current service basket.
- d5: The remodeling consumption figures are from 2014 and show historical volume, not a forecast.
- o: Insourcing is difficult to separate from supplier substitution in available evidence.
- o: Operator need is higher for variable, graded stock than for standardized planing.
- o: No direct survey measures customers' future self-service plans.

## Sources
- **S1** — [NAICS Code Description: 321912 Cut Stock, Resawing Lumber, and Planing](https://www.naics.com/naics-code-description/?code=321912&v=2022) (accessed 2026-07-22): Defines the industry around cut stock, resawing purchased lumber, and planing and identifies the relevant processing activities.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Shows other-wood-product manufacturing employment is concentrated in assemblers, woodworking and sawing machine operators, material movers, truck operators, supervisors, carpenters, drivers, sales, and management.
- **S3** — [O*NET: Helpers--Production Workers](https://www.onetonline.org/link/summary/51-9198.00) (accessed 2026-07-22): Documents loading, unloading, machine operation, inspection, monitoring, packing, recording, and material movement in production support.
- **S4** — [Scalable AI-driven automation for visual lumber grading](https://www.sciencedirect.com/science/article/pii/S0959652625023431) (accessed 2026-07-22): Demonstrates AI visual grading for dimensions, knots, cracks, holes, and wane, reporting below-2.5% calibration error and 99-100% defect-detection precision on a lab dataset.
- **S5** — [Computer-implemented method and system for managing lumber production line flow using deep learning AI, vision, 3D and robotics](https://patents.justia.com/patent/20250116999) (accessed 2026-07-22): Describes AI and video monitoring of board integrity, grading, positioning, mechanical failures, and planer- or saw-line flow anomalies with human or robotic intervention.
- **S6** — [Only 3.8% of Businesses Use AI to Produce Goods and Services](https://www.census.gov/library/stories/2023/11/businesses-use-ai.html) (accessed 2026-07-22): Reports a low late-2023 starting point of 3.8% current US business AI use and 6.5% planned use within six months.
- **S7** — [BLS Table 1: Incidence rates of nonfatal occupational injuries and illnesses by industry, 2024](https://www.bls.gov/web/osh/table-1-industry-rates-national.htm) (accessed 2026-07-22): Reports 5.4 total recordable injury and illness cases per 100 full-time workers for NAICS 321912 in 2024.
- **S8** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 14% of working small-business owners planned a sale, IPO, or transfer within five years, rising to 17% among owners age 55 or older.
- **S9** — [Tariffs on lumber and appliances set stage for higher costs on new homes and remodeling projects](https://apnews.com/article/tariffs-home-improvement-housing-market-home-construction-ae55bcae89a8ad78814c3dbce69e435f) (accessed 2026-07-22): Documents construction-material cost pass-through, lumber-price volatility, and the countervailing risk that higher prices reduce housing demand.
- **S10** — [The Outlook for Housing Starts](https://www.cbo.gov/publication/60727) (accessed 2026-07-22): Projects 1.68 million average annual housing starts in 2025-2029 and 1.52 million in 2030-2033, with substantial financial and demographic uncertainty.
- **S11** — [Revisiting U.S. softwood lumber demand projections: The central role of residential construction in forest sector outlooks](https://research.fs.usda.gov/treesearch/80470) (accessed 2026-07-22): Estimates housing-start elasticity of 0.59, income elasticity of 0.14, and price elasticity of -0.21 for US softwood-lumber demand using 2000-2024 data.
- **S12** — [Wood products used in residential repair and remodeling in the United States, 2014](https://research.fs.usda.gov/treesearch/56329) (accessed 2026-07-22): Reports repair and remodeling as the first- or second-largest market for several wood products and 13.5 billion board feet of softwood lumber used in 2014.
