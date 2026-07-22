# 326199 — All Other Plastics Product Manufacturing

*v5.1 Stage 1 research memo. Run `326199-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.23 · L 0.94 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A broad pool of repeat B2B manufacturers with engineering, planning, quality, and production-support workflows amenable to improvement.
**Weakness:** Residual-code heterogeneity makes eligibility, demand, and transfer estimates unusually uncertain.

## Business-model lens
- Included: US lower-middle-market custom and contract manufacturers within 326199 that mold, thermoform, fabricate, or assemble plastic components and products for external OEM, industrial, institutional, or private-label customers under recurring or repeat programs.
- Excluded: Captive internal plants; one-off consumer novelty, disposable houseware, seasonal recreational, resilient-flooring, and commodity retail-product models lacking recurring outsourced customer programs; pure distributors; shells; and non-control financing vehicles.
- Customer and revenue model: Repeat B2B program revenue based on part or product volumes, tooling and engineering charges, purchase orders, blanket orders, or supply agreements, with unit pricing periodically reset for resin, labor, freight, and competitive bids.
- Deviation from default lens: The residual code spans unrelated products including cups, dinnerware, gloves, siding, floor coverings, inflatables, hardware, and trash containers. To keep one coherent screen, the lens retains repeat custom or contract B2B plastic-product supply and excludes consumer, seasonal, and project business models that have different acquisition, retention, and demand mechanics.

## Executive view
The residual code is too diverse for one meaningful screen, so the analysis keeps repeat custom and contract B2B plastics manufacturing. That subset has useful AI opportunities in quoting, engineering coordination, scheduling, quality, inspection, maintenance, and administration, while physical conversion remains central.

## How AI changes the work
AI can compress RFQ review, cost estimation, scheduling, work instructions, engineering-change handling, quality documentation, vision inspection, maintenance diagnosis, and customer support. High-mix molds, inserts, finishing, secondary operations, and line intervention constrain physical substitution.

## Value capture
Tooling, qualification history, process know-how, and delivery performance create switching costs. OEM purchasing sophistication, annual productivity asks, resin transparency, and rebids nevertheless transfer a substantial share of visible gains to customers.

## Firm availability
A large nominal firm universe is offset by the narrow eligible share and uncertain classification. Broad succession data support potential control flow, but product mix, ownership, recurring program quality, customer concentration, asset condition, and closed transactions need verification.

## Demand durability
Diversified end markets stabilize the narrowed portfolio, while imports, substitution, insourcing, sustainability rules, and cycles can reduce specific programs. Physical products continue to require accountable manufacturing operators.

## Risks and uncertainty
Heterogeneity is the dominant risk: firms sharing this code can have entirely different process, channel, demand, and margin structures. Other material risks are customer concentration, resin and freight volatility, obsolete presses and molds, environmental exposure, quality claims, and workforce scarcity.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1714 | — | OBSERVED | — |
| n | — | 1811 | — | ESTIMATE | — |
| a | 0.16 | 0.25 | 0.35 | PROXY | S1 |
| rho | 0.39 | 0.55 | 0.7 | PROXY | S2 |
| e | 0.24 | 0.39 | 0.55 | ESTIMATE | S3 |
| s5 | 0.12 | 0.2 | 0.29 | PROXY | S4 |
| q | 0.36 | 0.53 | 0.7 | ESTIMATE | — |
| d5 | 0.94 | 1.03 | 1.14 | ESTIMATE | S2, S3 |
| o | 0.93 | 0.98 | 0.995 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.43 | 0.94 | 1.68 | PROXY |
| F | 6.39 | 7.97 | 9.12 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 8.74 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Four-digit occupation data do not isolate the residual code or narrowed lens.
- a: The installed automation baseline and wage weighting by process are unknown.
- rho: The occupation source mixes metal and plastics processes.
- rho: Implementation will vary sharply between high-volume molding and high-mix fabrication or assembly.
- e: Census examples demonstrate heterogeneity but do not quantify each submodel's firm share.
- e: The frozen firm count is estimated from size classes and a margin bridge.
- s5: Cross-industry intentions are not completed transactions.
- s5: Transactions may be classified under customer end markets rather than 326199.
- q: No public contract corpus measures retention.
- q: Commodity products retain less than tightly qualified, low-volume, engineered parts.
- d5: No single forecast fits the code's many products.
- d5: The base is a portfolio judgment for the narrowed lens, not the full residual code.
- o: The physical-operator requirement is inferred rather than surveyed.
- o: Product elimination and material substitution are primarily included in d5 to avoid double counting.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 326100 Plastics Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-22): Confirms coverage of NAICS 326100 employers and reports the industry occupation and wage mix used as the exposure proxy, including management, engineering, office, sales, production, maintenance, and material-moving work.
- **S2** — [Metal and Plastic Machine Workers, Occupational Outlook Handbook](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-22): Describes machine setup, monitoring, adjustment, inspection, and documentation; reports continuing adoption of CNC, robotics, and digital prototyping; and notes foreign competition and potential reshoring.
- **S3** — [2012 NAICS Definitions](https://www2.census.gov/library/reference/naics/technical-documentation/definition-files/2012_definition_file.pdf) (accessed 2026-07-22): Defines 326199 as plastics products outside the specifically named plastics categories and lists disparate examples including inflatables, air mattresses, bowls, hangers, cups, dinnerware, gloves, hardware, siding, trash containers, and resilient floor coverings, supporting the heterogeneous-lens narrowing.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of employer-business owners surveyed in fall 2024 planned to sell or transfer ownership within five years, used as a cross-industry proxy rather than an observed plastics transaction rate.
