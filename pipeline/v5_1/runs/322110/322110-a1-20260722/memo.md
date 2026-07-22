# 322110 — Pulp Mills

*v5.1 Stage 1 research memo. Run `322110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.13 · L 0.08 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A 24/7 process plant generates valuable maintenance, planning, quality, and compliance workflows that AI can augment without eliminating the operator.
**Weakness:** Very few independent target-band firms fit the lens, and commodity pricing plus a low labor share limits retained upside.

## Business-model lens
- Included: Independent US market-pulp mills that repeatedly supply external paper, paperboard, tissue, specialty-cellulose, or other fiber customers and could transfer as an operating control investment in the target EBITDA band.
- Excluded: Integrated pulp operations captive to an affiliated paper or paperboard mill, dormant or closure assets, project shells, non-control interests, and mills outside the target band.
- Customer and revenue model: Revenue is tonnage-based commodity or specification-grade pulp sales under spot, formula, and recurring supply arrangements; it is repeat B2B product supply rather than an outsourced service fee.
- Deviation from default lens: Pulp milling is capital-intensive product manufacturing and often vertically integrated. The lens is narrowed to independent market-pulp suppliers with repeat external customer relationships so the transferable population is coherent.

## Executive view
Pulp mills are a poor fit for a recurring outsourced-service roll-up: the industry is capital intensive, frequently integrated, commodity priced, environmentally regulated, and represented by an injected pool of only five estimated LMM firms. AI can improve information and maintenance workflows, but the low compensation-to-receipts ratio and physical process core constrain economic scope.

## How AI changes the work
Useful applications include maintenance knowledge retrieval, work-order preparation, process-event synthesis, procurement, fiber and chemical planning, laboratory and quality records, environmental reporting, sales documentation, and management analysis. Continuous process operation and hands-on maintenance remain human-accountable and equipment-bound.

## Value capture
Market-linked tonnage pricing and sophisticated industrial buyers expose savings to competition. Specialty grades, uptime, yield, and service reliability may preserve some benefit, but commodity cycles and volatile inputs make attribution and durable retention difficult.

## Firm availability
Only independent market-pulp mills with external recurring supply relationships are eligible; integrated captive operations are excluded. The dataset's five-firm estimate is fragile, and corporate portfolio transactions or mill asset sales often do not create an eligible standalone LMM transfer.

## Demand durability
Packaging, tissue, specialty cellulose, and exports provide durable outlets, while graphic-paper contraction, recovered fiber, capacity rationalization, and recent lower pulp consumption create downside. The five-year center is modest real decline rather than collapse.

## Risks and uncertainty
The central risks are near-zero eligible population, capital intensity, environmental liabilities, commodity pricing, fiber and energy costs, legacy controls, cyber and process safety, mill closures, and composition error from four-digit evidence. One firm can materially change every availability conclusion.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0549 | — | OBSERVED | — |
| n | — | 5 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.22 | PROXY | S1, S2 |
| rho | 0.25 | 0.44 | 0.62 | ESTIMATE | S2, S3 |
| e | 0.02 | 0.08 | 0.2 | ESTIMATE | S2 |
| s5 | 0.05 | 0.13 | 0.25 | PROXY | S4 |
| q | 0.18 | 0.35 | 0.55 | ESTIMATE | S5 |
| d5 | 0.78 | 0.94 | 1.1 | PROXY | S5, S6 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.04 | 0.14 | 0.30 | ESTIMATE |
| F | 0.01 | 0.08 | 0.36 | ESTIMATE |
| C | 3.60 | 7.00 | 10.00 | ESTIMATE |
| D | 7.49 | 9.31 | 10.00 | ESTIMATE |

## Caveats
- a: Four-digit occupational mix may not represent stand-alone pulp mills.
- a: Existing distributed-control, predictive-maintenance, and process-optimization systems are not separated from not-yet-automated work.
- rho: No US pulp-mill study directly measures five-year AI implementation.
- rho: Apparent optimization gains may come from conventional advanced process control rather than AI substitution.
- e: The injected n is margin-bridged and may be implausible for a capital-intensive mill industry.
- e: A mill may be legally separate but commercially captive to an affiliated paper operation.
- s5: Cross-industry owner intentions are a weak proxy for corporate mill transactions.
- s5: Asset sales, closures, and integrated-company reorganizations may not qualify.
- q: No public evidence directly isolates pass-through of AI-derived savings.
- q: Commodity price cycles can overwhelm modest productivity effects.
- d5: Combined pulp/paper output masks stand-alone market-pulp flows.
- d5: Demand varies sharply by hardwood/softwood, fluff, dissolving, bleached/unbleached, and geography.
- o: This measures need for an operator, not headcount.
- o: Demand loss from grade substitution belongs in d5, not here.

## Sources
- **S1** — [Pulp, Paper, and Paperboard Mills - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_322100.htm) (accessed 2026-07-22): Broader-mill occupation mix: 51.68% production employment and 13.00% installation, maintenance, and repair, including 8.06% industrial machinery mechanics.
- **S2** — [Universal Industrial Sectors Integrated Solutions Model for Pulp and Paper Manufacturing Industry](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P100RB13.TXT) (accessed 2026-07-22): Integrated pulp production stages: wood preparation, cooking/pulping, washing, screening, optional bleaching, and paper making, supporting the continuous physical-process characterization.
- **S3** — [Pulp and Paper NESHAP Plain English Description](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=2000F35D.TXT) (accessed 2026-07-22): Continuous operating-parameter monitoring, recordkeeping, and reporting requirements used to demonstrate ongoing environmental compliance.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry succession proxy: 52.3% of employer businesses have owners age 55 or older and 22% planned a five-year sale or transfer.
- **S5** — [AF&PA Releases 66th Annual Paper Industry Capacity and Fiber Consumption Survey](https://www.afandpa.org/news/2026/afpa-releases-66th-annual-paper-industry-capacity-and-fiber-consumption-survey) (accessed 2026-07-22): 2025 paper and paperboard production fell 3.7%; wood-pulp consumption fell 3.2%; packaging and tissue were more resilient than printing-writing grades.
- **S6** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects NAICS 322100 output from 63.9 to 63.1 billion chained 2017 dollars over 2024-34 and employment down 13.1%.
