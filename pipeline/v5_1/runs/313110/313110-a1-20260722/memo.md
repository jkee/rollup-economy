# 313110 — Fiber, Yarn, and Thread Mills

*v5.1 Stage 1 research memo. Run `313110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.92 · L 0.99 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Machine-data, inspection, maintenance, and planning improvements applied to a labor-bearing physical process that customers still need performed.
**Weakness:** Most work is hands-on and already machine-mediated, while the eligible contract-processing population and its transfer rate are not statistically observed.

## Business-model lens
- Included: U.S. lower-middle-market mills that repeatedly provide custom, toll, or contract fiber preparation, spinning, twisting, texturing, winding, blending, yarn design, or related processing to external industrial, apparel, craft, technical-textile, or government-supply-chain customers.
- Excluded: Mills primarily selling standardized proprietary yarn as inventory, vertically integrated captive operations, hobby-only microprocessors below the economic band, distributors without processing, foreign plants, inactive facilities, and asset-only or non-control transactions.
- Customer and revenue model: Customers supply fiber or specifications and purchase recurring lots priced by processed or finished weight, setup, complexity, finishing options, design time, or negotiated industrial conversion terms.
- Deviation from default lens: Narrowed to custom, toll, and contract processing because NAICS 313110 includes both repeat outsourced processing and economically distinct standardized product manufacturing.

## Executive view
The relevant population is the minority of mills repeatedly processing customer fiber or specifications, not every yarn producer. These firms perform a durable physical conversion service with visible AI opportunities in inspection, maintenance, and planning, but the occupation mix is overwhelmingly production and maintenance, and demand is roughly flat with strong commodity-import pressure.

## How AI changes the work
AI can improve in-line defect detection, yarn measurement, predictive maintenance, scrap diagnosis, production scheduling, quoting, inventory planning, and documentation. It is much less suited to replacing physical setup, doffing, cleaning, material movement, repairs, fiber handling, and intervention when variable inputs behave unexpectedly.

## Value capture
Posted custom-mill pricing shows fixed setup and per-pound fees alongside hourly and per-pound surcharges. Fixed conversion fees offer temporary retention of throughput and overhead gains, but transparent pricing, volume breaks, and rebids share efficiency with customers; specialized recipes, domestic qualification, and scarce capacity improve bargaining power.

## Firm availability
Strategic acquisition and small-mill succession examples show that operating mills can transfer, but neither measures the target population. Customer backlog, trained labor, recipes, and equipment can be transferable assets; obsolete machinery, environmental exposure, owner-dependent know-how, and weak margins can turn a succession event into closure or an equipment sale.

## Demand durability
BLS expects real textile-mill output to be nearly flat while employment falls, consistent with ongoing productivity and competitive pressure. Protected defense sourcing and high-spec technical yarns can support domestic custom mills, while apparel cycles, imports, and standardized-yarn substitution create downside. The physical processing need remains highly operator-dependent.

## Risks and uncertainty
The largest evidentiary gap is how many LMM firms earn material recurring contract-processing revenue. Other risks include energy and fiber costs, machine obsolescence, repair skill scarcity, customer concentration, offshore price competition, quality claims, contamination, environmental liabilities, working capital, and highly variable small lots that make AI models harder to generalize.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.219 | — | OBSERVED | — |
| n | — | 62 | — | ESTIMATE | — |
| a | 0.15 | 0.24 | 0.35 | PROXY | S1, S2, S3 |
| rho | 0.31 | 0.47 | 0.64 | PROXY | S2, S3, S4 |
| e | 0.16 | 0.29 | 0.44 | ESTIMATE | S5, S6 |
| s5 | 0.14 | 0.28 | 0.43 | PROXY | S7, S8, S9 |
| q | 0.34 | 0.51 | 0.69 | PROXY | S6 |
| d5 | 0.86 | 1.01 | 1.17 | PROXY | S10, S11, S12 |
| o | 0.9 | 0.97 | 1 | ESTIMATE | S1, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.41 | 0.99 | 1.96 | PROXY |
| F | 1.40 | 2.89 | 4.09 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | PROXY |
| D | 7.74 | 9.80 | 10.00 | ESTIMATE |

## Caveats
- a: Four-digit occupation data mix contract and proprietary-product mills.
- a: The yarn-vision evidence includes a controlled laboratory prototype rather than scaled U.S. deployment.
- a: Legacy textile equipment may already automate some exposed monitoring tasks through non-AI controls.
- rho: The Census question measures any business-function use, not production implementation intensity.
- rho: Fancy-yarn and general yarn research may not generalize across natural, synthetic, industrial, and recycled inputs.
- rho: Small custom lots produce sparse, shifting training data.
- e: No statistical source reports the contract-processing share of firms or revenue.
- e: Many mills blend custom service and proprietary product business.
- e: The frozen firm count uses a food-processing margin bridge that may materially misclassify textile firms.
- s5: The strategic acquisition may exceed the target economic band.
- s5: Small custom-wool examples may fall below it.
- s5: Offered-for-sale status is not a completed qualifying transfer.
- q: One public craft-scale price list may not represent industrial tolling contracts.
- q: Customer concentration and technical differentiation can move retention in opposite directions.
- q: The estimate excludes implementation cost, demand change, and volume effects.
- d5: The BLS projection covers all textile mills at three digits, not NAICS 313110 contract work.
- d5: Import declines in one period may reflect inventory correction rather than domestic substitution.
- d5: Defense sourcing is durable but applies only to qualifying products and procurements.
- o: No direct source measures operator displacement in contract yarn processing.
- o: Operator requirement is distinct from labor intensity; automation can reduce workers while leaving an accountable mill necessary.
- o: Imported standardized yarn can eliminate the outsourced U.S. service relationship even though a foreign operator remains.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 313100 Fiber, Yarn, and Thread Mills](https://www.bls.gov/oes/2023/may/naics4_313100.htm) (accessed 2026-07-22): Detailed occupation and wage mix, including production, winding/twisting, inspection, maintenance, management, engineering, and support work.
- **S2** — [Artificial Intelligence in Manufacturing: Real World Success Stories and Lessons Learned](https://www.nist.gov/blogs/manufacturing-innovation-blog/artificial-intelligence-manufacturing-real-world-success-stories) (accessed 2026-07-22): Manufacturing AI applications in maintenance, quality, scrap, throughput, and forecasting, plus data and implementation constraints.
- **S3** — [AI-Powered Industrial Quality Assurance System for Fancy Yarn Using Computer Vision and 3D Visualization](https://www.nature.com/articles/s41598-026-49947-5) (accessed 2026-07-22): Controlled prototype evidence for AI yarn defect detection, thickness measurement, pattern analysis, and limits of existing inspection.
- **S4** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS evidence on current and expected AI use and lower adoption among very small businesses.
- **S5** — [Barnet North America](https://www.barnet.com/profile/locations/north-america/) (accessed 2026-07-22): Concrete U.S. contract-manufacturing activities for synthetic fibers and contract yarn combining, splicing, and back winding.
- **S6** — [Green Mountain Spinnery Custom Processing Fact Sheet & Price List 2025](https://www.spinnery.com/wp-content/uploads/2025/08/2025-Custom-Price-sheet-.pdf) (accessed 2026-07-22): Custom-processing model and observed setup, hourly, per-pound, volume-tier, finishing, shipping, deposit, and surcharge terms.
- **S7** — [Textiles Monterey Group Acquires Patrick Yarns, Launches FilSpec USA](https://www.textileworld.com/textile-world/textile-news/2025/06/textiles-monterey-group-acquires-patrick-yarns-launches-filspec-usa/) (accessed 2026-07-22): Completed acquisition and continued operation of a North Carolina specialty spun-yarn facility.
- **S8** — [Illinois Wool & Fiber Mill](https://ilwoolfibermill.com/) (accessed 2026-07-22): Owner-announced sale after 17 years, ongoing customer processing, and continuity intent during succession.
- **S9** — [The Wool Mill: About Us](https://thewoolmill.com/pages/about-us) (accessed 2026-07-22): Example of prior mill equipment and operating ownership passing to a new owner in 2018.
- **S10** — [Employment and Output by Industry, 2024–2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projection for textile-mill real output and employment over 2024-2034.
- **S11** — [U.S. General Imports of Cotton, Wool, Man-Made Fiber, Silk Blend and Non-Cotton Vegetable Fiber Textiles and Apparel: January 2024](https://www.trade.gov/sites/default/files/2024-03/Press%20Release%20Jan%202024%20Data%20Write-Up%20%20Tables.pdf) (accessed 2026-07-22): Observed textile, apparel, and yarn import volumes and year-over-year changes through January 2024.
- **S12** — [Berry Amendment](https://www.trade.gov/berry-amendment) (accessed 2026-07-22): Domestic-source restrictions covering Department of Defense procurement of fibers, yarns, fabrics, clothing, and other textile items.
