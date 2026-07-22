# 322120 — Paper Mills

*v5.1 Stage 1 research memo. Run `322120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Complex 24/7 mills generate high-value maintenance, quality, scheduling, and compliance knowledge work that AI can augment while customers continue to need physical paper.
**Weakness:** Absolute firm availability is unknowable from the frozen dataset, and structural decline in printing-writing plus competitive pricing limits a broad roll-up thesis.

## Business-model lens
- Included: Independent US paper mills that make paper from purchased or internally produced pulp and repeatedly supply external tissue, packaging-paper, printing-writing, technical, or specialty-paper customers, with transferable standalone operations in the target band.
- Excluded: Paperboard-only mills, converted-paper plants that do not make paper, captive internal mills, dormant or closure assets, project shells, non-control interests, and operations outside the target band.
- Customer and revenue model: Revenue is primarily tonnage, roll, sheet, or grade-based product sales under spot, formula, and recurring supply arrangements; it is repeat B2B supply rather than an outsourced service fee.
- Deviation from default lens: Paper milling is capital-intensive product manufacturing, often integrated or captive. The lens is narrowed to independent mills with recurring external supply relationships so eligibility is coherent across disparate paper grades.

## Executive view
Paper mills offer bounded AI gains in maintenance, planning, quality, compliance, and commercial workflows, but they remain capital-intensive physical manufacturers with competitive industrial pricing. The missing dataset firm count prevents any defensible absolute availability conclusion, and only independent mills with repeat external customers fit the lens.

## How AI changes the work
AI can synthesize maintenance history, assist work orders and troubleshooting, support grade changes and scheduling, draft quality and permit records, reconcile specifications, and improve procurement and customer service. It should not be assumed to replace continuous-process operators, technicians, or accountable environmental personnel.

## Value capture
Existing contracts, specialty grades, uptime, and quality can shelter some benefit. Over five years, formula pricing, bids, capacity competition, imports, and buyer negotiation should share a substantial portion, with commodity grades capturing less than technical or specialty products.

## Firm availability
Eligibility requires a standalone independent mill, repeat external sales, target-band economics, transferable permits and liabilities, and durable management. The frozen dataset has no defensible LMM firm count, and general small-business succession evidence cannot repair that gap.

## Demand durability
Tissue, packaging paper, and specialties are relatively resilient, while printing-writing continues structural contraction. Grade mix dominates the outlook; the aggregate base is moderate decline, not a single thesis that applies to every paper mill.

## Risks and uncertainty
Key risks are the missing firm-count denominator, capital and maintenance intensity, environmental liabilities, energy and fiber costs, mill closures and conversions, legacy controls, commodity pricing, grade-specific demand, and composition error from combined four-digit data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1413 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.08 | 0.15 | 0.23 | PROXY | S1, S2 |
| rho | 0.25 | 0.45 | 0.64 | ESTIMATE | S2, S3 |
| e | 0.04 | 0.12 | 0.25 | ESTIMATE | S4 |
| s5 | 0.05 | 0.14 | 0.26 | PROXY | S5 |
| q | 0.2 | 0.4 | 0.62 | ESTIMATE | S6 |
| d5 | 0.72 | 0.91 | 1.08 | PROXY | S6, S7 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.11 | 0.38 | 0.83 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 4.00 | 8.00 | 10.00 | ESTIMATE |
| D | 6.77 | 8.92 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit paper-mill occupational mix was located.
- a: Existing distributed-control, quality-control, and predictive-maintenance automation is not separated from not-yet-automated opportunity.
- rho: No industry-specific five-year AI implementation study was located.
- rho: Benefits from conventional automation and advanced process control must be separated from AI labor substitution.
- e: The frozen dataset explicitly has no defensible n value; this eligibility share must not be converted into a firm count.
- e: The code includes integrated mills and mills that also convert their own paper.
- s5: Cross-industry intentions are weak evidence for mill transactions.
- s5: Asset sales, internal reorganizations, and conversions may not qualify as transferable operating firms.
- q: No public study directly isolates pass-through of AI-derived productivity.
- q: Fiber, energy, chemicals, freight, and downtime volatility can dominate small labor savings.
- d5: Paperboard demand is included in some cited aggregates but excluded from this six-digit title.
- d5: The average is especially sensitive to the eligible firm's grade mix; printing-writing and tissue should not share one point forecast in diligence.
- o: This measures operator necessity rather than employment intensity.
- o: Quantity loss from digitization or material substitution belongs in d5.

## Sources
- **S1** — [Pulp, Paper, and Paperboard Mills - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_322100.htm) (accessed 2026-07-22): Combined-mill occupational mix: 51.68% production and 13.00% installation, maintenance, and repair, including 8.06% industrial machinery mechanics.
- **S2** — [NPDES Permit No. MA0001716 Fact Sheet](https://www3.epa.gov/region1/npdes/permits/2021/finalma0001716permit.pdf) (accessed 2026-07-22): Paper production process: fiber, water, and additives are pulped, fed to a paper machine, formed, and dewatered from about 95% water to under 5%, with wastewater treatment.
- **S3** — [Monadnock Paper Mills Draft NPDES Permit NH0000230](https://www.epa.gov/system/files/documents/2021-07/draftnh0000230permit.pdf) (accessed 2026-07-22): Concrete paper-mill operating accountability: continuous effluent-flow monitoring and recurring pH, BOD, suspended-solids, nutrient, metal, and PFAS sampling requirements.
- **S4** — [NAICS Definition: Paper Mills](https://www.census.gov/naics/?details=322&input=322&year=2012) (accessed 2026-07-22): Industry scope: establishments making paper from pulp, whether they manufacture or purchase pulp and whether they also convert the paper they make.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry succession proxy: 52.3% of employer businesses have owners age 55 or older and 22% planned a five-year sale or transfer.
- **S6** — [AF&PA Releases 66th Annual Paper Industry Capacity and Fiber Consumption Survey](https://www.afandpa.org/news/2026/afpa-releases-66th-annual-paper-industry-capacity-and-fiber-consumption-survey) (accessed 2026-07-22): 2025 grade and capacity evidence: total paper/paperboard production down 3.7%, printing-writing capacity down 13.9%, packaging paper up 1.7%, and tissue near 7.8 million tons.
- **S7** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects combined NAICS 322100 real output from 63.9 to 63.1 billion chained 2017 dollars over 2024-34 and employment down 13.1%.
