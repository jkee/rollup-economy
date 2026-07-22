# 313240 — Knit Fabric Mills

*v5.1 Stage 1 research memo. Run `313240-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.85 · L 1.09 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Machine vision and production-data workflows can reduce inspection, scrap, reporting, and coordination work in repeat B2B programs.
**Weakness:** A small acquisition population and structurally pressured domestic textile output make both transferable supply and five-year demand uncertain.

## Business-model lens
- Included: US lower-middle-market mills that repeatedly knit weft or warp fabric, make lace, or combine knitting with finishing or further nonapparel fabrication for external B2B customers under recurring programs or repeat purchase orders.
- Excluded: Apparel knitting mills, captive internal production units, one-off asset-only operations, non-control financing vehicles, and mills without a transferable operating business or repeat external-customer revenue.
- Customer and revenue model: Primarily per-pound, per-yard, per-roll, or per-program B2B sales and contract-manufacturing charges to apparel, industrial, medical, furnishings, and other downstream textile customers; specifications and repeat orders create recurring relationships but generally not long-duration subscriptions.
- Deviation from default lens: The code includes both own-account product mills and contract/program production. The lens is narrowed to mills with repeat external-customer programs so that outsourced and own-account operations are not treated as one revenue model.

## Executive view
Knit fabric mills combine a physically intensive core with a narrower but credible digital opportunity in visual inspection, production monitoring, scheduling, quality records, quoting, and administration. Repeat B2B programs can support transferable customer relationships, but the industry remains exposed to import competition, weak domestic output trends, capital intensity, and customer concentration.

## How AI changes the work
AI is most concrete at the machine-vision and information layer. Cameras can identify defects during knitting, stop machines, and generate traceability and productivity records; language and forecasting tools can assist specifications, purchasing, quoting, scheduling, customer communication, and maintenance triage. Operators, mechanics, material handlers, and setup personnel still perform most of the physical work, limiting substitution.

## Value capture
Benefits from lower scrap, earlier defect detection, better uptime, and avoided administrative hiring may remain with the operator during fixed-price cycles. Per-unit quoting, competitive rebids, open-book or cost-plus arrangements, and customer procurement pressure will share savings over time. Specialty, fast-turn, or high-compliance programs should retain more than commodity fabrics.

## Firm availability
The estimated LMM population is small, and only a subset will combine repeat external-customer revenue, stand-alone management, transferable equipment and know-how, acceptable customer concentration, and manageable environmental or deferred-maintenance liabilities. Broad owner-exit intent supports turnover, but completed qualifying control transfers should be much less frequent than stated plans.

## Demand durability
Physical fabric remains necessary across apparel and nonapparel applications, so software is unlikely to eliminate the operator. The more serious risk is that domestic demand migrates to imports or larger integrated suppliers. Recent real output for textile mills is depressed, although reshoring, short lead times, niche technical fabrics, and customer resilience requirements provide an upside case.

## Risks and uncertainty
Public evidence is mostly broader than NAICS 313240. Key uncertainties are actual contract-versus-own-account mix, customer concentration, equipment age, existing automation, environmental exposure from integrated finishing, specialty versus commodity end markets, and whether owner transition intent becomes a sale rather than a family transfer or closure.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1768 | — | OBSERVED | — |
| n | — | 47 | — | ESTIMATE | — |
| a | 0.18 | 0.28 | 0.4 | PROXY | S2, S3 |
| rho | 0.35 | 0.55 | 0.72 | PROXY | S3, S4 |
| e | 0.55 | 0.72 | 0.88 | ESTIMATE | S1 |
| s5 | 0.12 | 0.26 | 0.4 | PROXY | S5, S6 |
| q | 0.3 | 0.5 | 0.68 | ESTIMATE | S3, S7 |
| d5 | 0.75 | 0.9 | 1.05 | PROXY | S7, S8 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.45 | 1.09 | 2.04 | PROXY |
| F | 2.27 | 3.67 | 4.61 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.75 | 8.64 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source is NAICS 3132, broader than 313240, and includes broadwoven, narrow, nonwoven, and knit fabric mills.
- a: The Smartex source is a vendor announcement and describes product capability, not independently measured labor displacement.
- a: Exposure is to task substitution or avoided hiring, not whole-job elimination.
- rho: The adoption survey spans all manufacturing industries and firm sizes.
- rho: Installed AI does not imply full use, reliable performance, or realized labor savings.
- rho: Quality-critical customer specifications may require continued human review even after automated detection.
- e: No source measures the eligible share of NAICS 313240 firms in the specified EBITDA band.
- e: The provided firm count is an estimate and may include firms whose EBITDA is cyclically or temporarily within the band.
- e: Repeat purchase orders can be economically recurring without being contractually recurring.
- s5: The owner survey covers private businesses across industries and includes partial financial exits.
- s5: BizBuySell covers voluntarily reported small-business transactions and is not a complete LMM M&A census.
- s5: A planned succession may preserve operations without producing an acquirable third-party opportunity.
- q: No public source isolates five-year benefit retention for knit mills.
- q: Commodity versus specialty fabric mix can move retention sharply.
- q: The estimate excludes volume loss and implementation failure, which belong in other primitives.
- d5: The output history is for NAICS 313 rather than 313240.
- d5: Industrial production is realized domestic output, not a direct measure of demand for the screened firms' current service basket.
- d5: The range does not assume a specific future tariff regime.
- o: Operator requirement is high conditional on domestic demand surviving; demand loss itself is represented in d5.
- o: Some design, inspection, and documentation roles may become self-served even though physical production does not.
- o: A customer can replace the lens operator through vertical integration without eliminating the physical process.

## Sources
- **S1** — [North American Industry Classification System: Knit Fabric Mills definition](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-23): Defines knit fabric mills as knitting weft or warp fabric, knitting and finishing fabric, manufacturing lace, and related nonapparel further fabrication; distinguishes apparel knitting.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Fabric Mills](https://www.bls.gov/oes/2023/may/naics4_313200.htm) (accessed 2026-07-23): Reports the broader fabric-mill occupation mix, including production occupations at 61.73%, knitting and weaving machine operators at 19.98%, installation and maintenance at 10.28%, and inspectors at 5.96%.
- **S3** — [Smartex Announced the Launch of Smartex-V1, an Advanced Camera Vision System for Circular Knitting Machines](https://www.textileworld.com/textile-world/knitting-apparel/2020/11/smartex-announced-the-launch-of-smartex-v1-an-advanced-camera-vision-system-for-circular-knitting-machines%E2%80%A8/) (accessed 2026-07-23): Describes AI computer vision incorporated into circular knitting machines to detect defects, stop machines, monitor production, and automate quality and productivity reporting.
- **S4** — [NAM to White House: Here's How to Boost AI Adoption in Manufacturing](https://nam.org/nam-to-white-house-heres-how-to-boost-ai-adoption-in-manufacturing/) (accessed 2026-07-23): Reports a 2025 Manufacturing Leadership Council survey in which 51% of manufacturers already used AI and 60% expected to use it by 2027.
- **S5** — [2025 Business Owner Report: How business owners are planning their futures](https://www.shorebridgewm.com/resources/2025/11/06/2025-business-owner-report-how-business-owners-are-planning-their-futures) (accessed 2026-07-23): Reports a national survey of 540 private-company owners: 56% planned to exit some or all of their stake within five years; external sales represented 23% of transition responses, with family and internal paths also common.
- **S6** — [BizBuySell Insight Report, Q2 2026](https://www.bizbuysell.com/insight-report/) (accessed 2026-07-23): Reports manufacturing transaction activity, longer close times, and buyer emphasis on earnings quality, clean financials, owner independence, and SBA eligibility; explains coverage of voluntarily reported small-business transactions.
- **S7** — [Industrial Production: Textile Mills (NAICS 313)](https://fred.stlouisfed.org/series/IPG313A) (accessed 2026-07-23): Federal Reserve real-output index for US textile mills: 74.4140 in 2022, 67.8961 in 2024, and 67.0305 in 2025.
- **S8** — [SelectUSA Textiles Industry](https://www.trade.gov/selectusa-textiles-industry) (accessed 2026-07-23): Reports textile-mill shipments of $25.3 billion in 2023 and notes industry focus on niche markets, advanced technologies, process efficiency, and reshoring or nearshoring.
