# 315250 — Cut and Sew Apparel Manufacturing (except Contractors)

*v5.1 Stage 1 research memo. Run `315250-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → CONDITIONAL · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** AI-addressable design-to-production coordination around repeat private-label orders.
**Weakness:** A heterogeneous code, shrinking domestic output, and no defensible frozen LMM firm count.

## Business-model lens
- Included: US lower-middle-market full-package, OEM, and private-label cut-and-sew manufacturers that buy fabric and repeatedly supply custom or customer-branded apparel to external brands, uniform programs, distributors, institutions, or other business customers.
- Excluded: Own-brand and direct-to-consumer apparel companies whose economics depend primarily on brand ownership, merchandising, or retail; jobbers that only market their own finished apparel; captive production; one-off bespoke tailoring; contractors working only on customer-owned materials; shells; and non-control financing vehicles.
- Customer and revenue model: Repeat business-to-business private-label or OEM supply, commonly quoted per style and unit as an all-in price covering purchased materials, construction, decoration, labels, packaging, and delivery, with sampling and repeat production runs.
- Deviation from default lens: NAICS 315250 combines own-account branded manufacturers and jobbers with full-package private-label/OEM suppliers. The lens is narrowed to the latter because recurring outsourced manufacturing for external customers is economically distinct from selling a manufacturer's own apparel product or brand.

## Executive view
The coherent target is not the entire code but the private-label and OEM subset that repeatedly supplies external brands and institutions. That subset has a meaningful digital coordination layer around design, specifications, sourcing, quoting, production control, and quality records, while its physical sewing core limits total AI exposure. The major weaknesses are a declining US apparel-output baseline, competitive all-in unit pricing, and the frozen absence of a defensible LMM firm count.

## How AI changes the work
AI can turn sketches and tech packs into structured production inputs, help draft bills of materials and quotes, suggest design variants, forecast capacity, coordinate sourcing, prepare customer updates, and organize inspection evidence. Computer vision can assist quality checks. Physical fabric positioning, sewing, finishing, rework, and rapid changeovers remain difficult, so implementation is concentrated in pre-production and control rather than end-to-end autonomous manufacture.

## Value capture
Full-package manufacturers quote a finished unit whose price depends on materials, construction, decoration, quantity, freight, and timing. Repeat customers can rebid those packages, and higher volume already earns lower unit prices, making direct productivity gains contestable. Operators retain more value when AI shortens sampling and launch cycles, enables economic small runs, improves on-time delivery, or prevents costly defects.

## Firm availability
Official classification includes own-account manufacturers and jobbers that market finished apparel, so only a minority is expected to fit the repeat outsourced-service lens. Broader manufacturing ownership is old and clothing/fabric business sales are observable, but public transactions are mostly far smaller than the target band. A missing frozen LMM firm count prevents defensible opportunity-volume estimation.

## Demand durability
Software cannot deliver a physical garment, and the private-label buyer continues to need a party responsible for material sourcing, fit, quality, labels, packaging, and delivery. Nevertheless, BLS projects real US apparel output to decline 1.9% annually through 2034. The narrowed subset must win through speed, low minimums, repeat restocks, traceability, specialized construction, or institutional demand to resist offshore substitution.

## Risks and uncertainty
Evidence rarely isolates the new 2022 six-digit code, much less its private-label/OEM and LMM subset. Broad apparel occupation and output data may overstate either exposure or decline for a specific target. Vendor claims demonstrate operating models but are not representative. Inventory, working capital, duties, customer concentration, labor compliance, fashion volatility, and owner-dependent technical knowledge can overwhelm modest AI savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3449 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.1 | 0.19 | 0.3 | PROXY | S2, S3, S4, S6 |
| rho | 0.28 | 0.5 | 0.7 | ESTIMATE | S6, S9 |
| e | 0.12 | 0.3 | 0.5 | ESTIMATE | S1, S6 |
| s5 | 0.09 | 0.2 | 0.33 | PROXY | S7, S8 |
| q | 0.2 | 0.43 | 0.67 | ESTIMATE | S6 |
| d5 | 0.74 | 0.91 | 1.07 | PROXY | S5, S6 |
| o | 0.87 | 0.96 | 0.99 | ESTIMATE | S3, S6, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.39 | 1.31 | 2.90 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 4.00 | 8.60 | 10.00 | ESTIMATE |
| D | 6.44 | 8.74 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation data cover all apparel manufacturing, not 315250 or the narrowed private-label subset.
- a: Task exposure does not establish technically reliable substitution or payroll reduction.
- a: Conventional mechanization is excluded unless AI is integral to perception, planning, or control.
- rho: No representative 315250 AI-adoption survey was found.
- rho: Adoption may relieve bottlenecks or increase service levels rather than reduce headcount.
- rho: The frozen labor ratio is measured at ancestor NAICS 3152 rather than this six-digit industry.
- e: A vendor's repeat-order claim establishes that the model exists, not its prevalence across the industry.
- e: Some firms mix own-brand, blanks, and private-label revenue and may only be partly eligible.
- e: The frozen n input is missing and must not be inferred from this eligibility estimate.
- s5: Neither source isolates 315250, the narrowed lens, or the target EBITDA band.
- s5: BizBuySell's clothing-and-fabric median cash flow was $100,000 in 2025, well below the lens.
- s5: Because frozen n is missing, transferable-firm volume cannot be quantified even with this probability.
- q: The public pricing example is a single provider and may involve offshore production despite US-based project support.
- q: Commodity products and sophisticated customers likely capture more savings than differentiated, fast-turn, low-volume work.
- q: The estimate excludes implementation costs and volume effects.
- d5: The BLS projection is NAICS 315, not 315250 or the narrowed lens.
- d5: The 2024-2034 output path includes trade, productivity, and product-mix effects, not just final demand.
- d5: The high case depends on the narrowed subset gaining share in a contracting domestic industry.
- o: Operator requirement is separate from domestic location or employment intensity.
- o: Standardized garments are more automatable than delicate, high-mix, or fit-sensitive products.
- o: Some customers could vertically integrate, but that is self-supply rather than software-only fulfillment.

## Sources
- **S1** — [Census Bureau profile: 315250 Cut and Sew Apparel Manufacturing (except Contractors)](https://data.census.gov/profile/315250_-_Cut_and_Sew_Apparel_Manufacturing_%28except_Contractors%29?codeset=naics~315250) (accessed 2026-07-22): Defines the industry as making cut-and-sew apparel from purchased fabric and includes jobbers that buy raw materials, design and prepare samples, arrange production, and market finished apparel; distinguishes work on materials owned by others.
- **S2** — [BLS Industry at a Glance: Apparel Manufacturing, NAICS 315](https://www.bls.gov/iag/tgs/iag315.htm) (accessed 2026-07-22): Reports roughly 73,000-74,000 apparel-manufacturing jobs in spring 2026 and 25,280 sewing-machine operators in 2025, with cutting, inspection, and production-supervision occupations also listed.
- **S3** — [O*NET: Sewing Machine Operators 51-6031.00](https://www.onetonline.org/link/details/51-6031.00) (accessed 2026-07-22): Describes physical core tasks including positioning items under needles, guiding garment parts, threading machines, monitoring stitches, and detecting malfunctions.
- **S4** — [ILO: Generative AI and Jobs — A Refined Global Index of Occupational Exposure](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) (accessed 2026-07-22): Finds clerical occupations retain the highest GenAI exposure and frames exposure as task-transformation potential, not immediate whole-job automation.
- **S5** — [BLS Table 2.11: Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects apparel-manufacturing real output from $12.3 billion in 2024 to $10.1 billion in 2034, a -1.9% compound annual rate, and employment from 84,500 to 58,800.
- **S6** — [DesignTo Clothing: Custom Apparel Development and Manufacturing](https://www.designtoclothing.com/) (accessed 2026-07-22): Illustrates a full-package model with fabric guidance, sampling, labels, packaging, MOQ 30+, repeat restocks, all-in unit quotes, quantity discounts, quality checkpoints, and a self-reported 94% repeat-order rate.
- **S7** — [BizBuySell Insight Report Data Tables: Full-Year 2025](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-22): Reports 21 completed clothing-and-fabric manufacturer sales in 2025, with median price $150,000, median revenue $414,000, median cash flow $100,000, and 287 median days on market.
- **S8** — [US Census Bureau CES Working Paper 24-71: The Metamorphosis of Women Business Owners — A Focus on Age](https://www2.census.gov/ces/wp/2024/CES-WP-24-71.pdf) (accessed 2026-07-22): Using Annual Business Survey data, reports manufacturing employer businesses with a 62.4% share in its older-owner analysis.
- **S9** — [A Deployment Case Study in Robotic Apparel Automation](https://arxiv.org/abs/2606.16078) (accessed 2026-07-22): States apparel automation remains challenging because fabrics are deformable and describes staged deployments requiring digital validation, interoperability, runtime verification, and workforce enablement.
