# 311813 — Frozen Cakes, Pies, and Other Pastries Manufacturing

*v5.1 Stage 1 research memo. Run `311813-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.73 · L 0.35 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat foodservice, retail, and private-label supply combines long-lived physical demand with data-rich planning workflows.
**Weakness:** Low labor intensity and buyer power limit the economic importance and retained share of AI-enabled labor savings.

## Business-model lens
- Included: Lower-middle-market manufacturers of frozen bakery products other than bread, including frozen cakes, pies, doughnuts, pastries, desserts, and sweet yeast goods, supplying repeat external foodservice, distributor, retail, private-label, or contract-packing customers.
- Excluded: Frozen bread manufacturing, retail bakeries, fresh commercial bakeries, cookie and cracker manufacturing, snack bars, captive production without external customers, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat wholesale product supply priced per unit, case, shipment, negotiated program, or contract-manufacturing arrangement; revenue commonly flows through foodservice distributors, chains, institutions, supermarkets, and private-label customers.
- Deviation from default lens: none

## Executive view
Frozen pastry manufacturing has strong repeat outsourced-supply fit and durable physical-product demand, but its labor ratio is relatively low and factory work is dominated by production, packing, maintenance, warehousing, and cold-chain activity. AI's most credible contribution is in planning, quality documentation, procurement, customer coordination, and logistics rather than direct substitution for plant labor.

## How AI changes the work
AI can improve demand and promotion forecasting, batch and labor scheduling, purchasing, formulation and specification search, quality-record review, inventory and cold-chain exception management, customer-service triage, bid preparation, and maintenance planning. Human accountability remains necessary for hazard controls, allergens, sanitation, line intervention, and product release.

## Value capture
Per-case pricing permits initial retention, but private-label, contract-pack, distributor, and large chain customers can recover value through bids, rebates, pricing true-ups, renewal pressure, or volume shifts. Public evidence of contractual ingredient-cost true-ups and lost low-margin seasonal business supports a conservative retention range.

## Firm availability
Most target firms should serve repeat external customers, though captive plants and seasonal one-off programs require screening. The plant, freezer, food-safety, customer-approval, and working-capital requirements may favor strategic buyers and make some distressed situations asset sales rather than transferable going concerns.

## Demand durability
Frozen shelf life and centralized manufacturing support retail and foodservice convenience, while broader bakery output is projected to grow moderately. Risks include discretionary dessert demand, health preferences, private-label pressure, customer program turnover, alternative desserts, and share shifts to larger suppliers or in-house production.

## Risks and uncertainty
Key gaps are six-digit occupation and real-output data, target-firm transaction evidence, and observed AI savings and retention cohorts. Food safety, allergens, cold-chain failure, energy and ingredient costs, customer concentration, seasonal programs, recalls, capacity utilization, and capital spending can outweigh administrative savings. The provided compensation ratio mixes 2024 wages and 2022 receipts and is harmonized, while the firm count is margin-bridged rather than directly observed.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1187 | — | OBSERVED | — |
| n | — | 81 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.22 | PROXY | S1, S2 |
| rho | 0.34 | 0.52 | 0.69 | ESTIMATE | S3, S4 |
| e | 0.78 | 0.9 | 0.97 | ESTIMATE | S5, S6 |
| s5 | 0.08 | 0.17 | 0.29 | ESTIMATE | — |
| q | 0.22 | 0.42 | 0.63 | ESTIMATE | S6 |
| d5 | 0.96 | 1.07 | 1.18 | PROXY | S7, S6 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.13 | 0.35 | 0.72 | ESTIMATE |
| F | 2.90 | 4.17 | 5.10 | ESTIMATE |
| C | 4.40 | 8.40 | 10.00 | ESTIMATE |
| D | 9.22 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS combines all NAICS 311800 segments and excludes self-employed workers.
- a: Published occupation counts do not reveal task time, current software use, or the wage share already automated.
- a: The frozen subsector's lower provided compensation-to-receipts ratio suggests capital and materials matter more than labor, but that dataset input is not a task-exposure measure.
- rho: No 311813-specific AI implementation cohort was located.
- rho: Products vary between ready-to-eat and ready-to-bake formats, changing food-safety workflows and acceptable automation.
- e: The public-company evidence spans products outside 311813 and a much larger scale than the target firms.
- e: The provided target-band firm count is margin-bridged and may be sensitive to this subsector's capital intensity and margins.
- s5: No source directly measures five-year qualifying control transfers for target-band 311813 firms.
- s5: Private transactions and plant asset sales are difficult to classify consistently.
- q: J&J Snack Foods spans multiple snack and bakery categories and is larger than the target band.
- q: Contractual ingredient-cost true-ups do not prove contractual pass-through of labor savings, so the value remains an estimate.
- d5: BLS output is four-digit and includes fresh bread, retail bakeries, cookies, crackers, and tortillas.
- d5: The J&J result is one company's nominal sales and volume commentary, not an industry quantity index.
- o: Operator-required demand can move from independent target firms to integrated customers or larger manufacturers.
- o: Ready-to-bake and ready-to-eat products have different handling and downstream labor requirements.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311800](https://www.bls.gov/oes/2023/may/naics4_311800.htm) (accessed 2026-07-22): Reports broader-industry occupation employment and wages, including production at 49.70%, bakers at 21.90%, packaging-machine operators at 6.71%, transportation and material moving at 13.23%, and office support at 5.24%.
- **S2** — [Occupational Outlook Handbook: Bakers](https://www.bls.gov/ooh/production/bakers.htm) (accessed 2026-07-22): Describes physical baking tasks and commercial production using high-volume machines and ovens that may be automated, alongside quality checks, cleaning, and equipment work.
- **S3** — [FSMA Final Rule for Preventive Controls for Human Food](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food) (accessed 2026-07-22): Documents requirements for process, allergen, sanitation, monitoring, corrective-action, verification, supply-chain, and recall controls for covered food facilities, subject to exemptions.
- **S4** — [FDA Draft Guidance: Hazard Analysis and Risk-Based Preventive Controls for Human Food, Appendix 1](https://www.fda.gov/media/99581/download) (accessed 2026-07-22): Identifies potential biological hazards for refrigerated or frozen ready-to-bake and fully baked bakery items, including distinctions involving fillings, frostings, and toppings.
- **S5** — [2022 NAICS Definition: 311813 Frozen Cakes, Pies, and Other Pastries Manufacturing](https://www.census.gov/naics/?details=311813&input=311813&year=2022) (accessed 2026-07-22): Defines the industry as manufacturing frozen bakery products other than bread, including cakes, pies, doughnuts, pastries, desserts, and sweet yeast goods, and identifies excluded adjacent industries.
- **S6** — [J&J Snack Foods 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/785956/000143774925036456/jjsf20250927_10k.htm) (accessed 2026-07-22): Documents foodservice, supermarket, private-label and contract-packing channels; customer concentration and limited long-term contracting; competition on price, quality and service; contractual ingredient-cost pricing true-ups; bakery sales of $405.9 million; and pie volume and seasonal-bid losses.
- **S7** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects broader NAICS 311800 real output from 62.1 to 74.4 billion chained 2017 dollars between 2024 and 2034, a 1.8% compound annual rate.
