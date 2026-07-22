# 322130 — Paperboard Mills

*v5.1 Stage 1 research memo. Run `322130-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.35 · L 0.21 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat physical demand with meaningful planning, maintenance-support, quality-data, and administrative workflows that AI can augment.
**Weakness:** A tiny, capital-intensive, environmentally regulated firm universe with mostly physical labor and commodity price pass-through.

## Business-model lens
- Included: Independent US paperboard mills repeatedly supplying paperboard to external converters and packaging customers, with firms in the approximately $1-10 million normalized EBITDA band.
- Excluded: Captive mills, integrated units without meaningful external sales, shells, non-control financing vehicles, pulp-only mills, paper mills outside paperboard, and firms outside the EBITDA band.
- Customer and revenue model: Repeat business-to-business sales of specification-defined paperboard, generally priced per ton under purchase orders or supply agreements with freight, fiber, energy, and market-price adjustments.
- Deviation from default lens: none

## Executive view
Paperboard mills offer a narrow AI opportunity around information flows rather than the core continuous production process. Repeat customer demand and indispensable physical output support operator durability, but commodity pricing, large fixed assets, environmental obligations, and a very small estimated LMM universe limit the thesis.

## How AI changes the work
The practical use cases are demand and production scheduling, order entry, procurement analysis, maintenance knowledge retrieval and triage, quality-data review, compliance drafting, and sales administration. Mill tending, repair, laboratory verification, material handling, and safety accountability remain predominantly physical or human-supervised.

## Value capture
Uptime and yield improvements may be retained longer than visible administrative savings, but sophisticated converters can reclaim part of recurring cost reductions through bids, indexed pricing, and renewals. Grade differentiation, freight advantage, and constrained local capacity determine retention.

## Firm availability
The frozen dataset estimates only 14 firms in the EBITDA band before eligibility. Captive ownership, integration, environmental liabilities, capital needs, and buyer concentration shrink the transferable subset, while an aging general owner population provides only indirect succession support.

## Demand durability
Paperboard remains a required physical input for packaging and other uses, yet demand differs by grade. Broad 3221 real output is projected nearly flat and 2025 data show production declines alongside stable boxboard and high containerboard utilization, justifying a near-flat central case with a wide range.

## Risks and uncertainty
The largest uncertainties are the absence of a 322130-specific task and wage map, the tiny margin-bridged firm count, unknown captive status, environmental remediation exposure, grade-specific demand, and contract-level pricing behavior. A few mill closures or conversions could materially change the population.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0857 | — | OBSERVED | — |
| n | — | 14 | — | ESTIMATE | — |
| a | 0.07 | 0.12 | 0.19 | PROXY | S1 |
| rho | 0.32 | 0.5 | 0.68 | ESTIMATE | S2, S4 |
| e | 0.35 | 0.55 | 0.75 | ESTIMATE | S4 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S5, S4 |
| q | 0.3 | 0.5 | 0.7 | ESTIMATE | S3 |
| d5 | 0.88 | 0.98 | 1.08 | PROXY | S2, S3 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.08 | 0.21 | 0.44 | ESTIMATE |
| F | 0.74 | 1.59 | 2.44 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.27 | 9.60 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation figures are NAICS 322, not 322130.
- a: No source directly measures current AI task exposure by paperboard-mill occupation.
- rho: Implementation evidence is not specific to AI deployments in 322130.
- rho: EPA monitoring and control obligations make unchecked automation inappropriate for regulated workflows.
- e: No observed denominator of LMM paperboard-mill firms by captive status exists in the reviewed sources.
- e: The injected n=14 is an ESTIMATE based on size-class and margin bridging.
- s5: Owner-age evidence covers 2018 responding employer-business owners across all industries.
- s5: Observed owner age is not an observed sale probability.
- q: No representative contract dataset was available.
- q: Retention varies sharply by grade, customer concentration, mill utilization, and freight radius.
- d5: BLS is NAICS 3221 and reports value output, not constant-quality 322130 physical quantity.
- d5: AF&PA coverage is about 87% of capacity with estimates completing the dataset.
- o: The estimate separates operator requirement from volume decline, which is captured in d5.
- o: Some administrative customer interactions can become self-service without eliminating the mill operator.

## Sources
- **S1** — [Paper Manufacturing: NAICS 322](https://www.bls.gov/iag/tgs/iag322.htm) (accessed 2026-07-22): BLS 2025 occupation counts for paper manufacturing, including 87,050 paper-goods machine operators, 17,540 production supervisors, 14,210 industrial-truck operators, and 6,640 production managers; also reports 2025 output and productivity context.
- **S2** — [Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects pulp, paper, and paperboard mills employment falling from 84,700 in 2024 to 73,600 in 2034 and real output moving from $63.9 billion to $63.1 billion, a -0.1% output CAGR.
- **S3** — [AF&PA Releases 66th Annual Paper Industry Capacity and Fiber Consumption Survey](https://www.afandpa.org/news/2026/afpa-releases-66th-annual-paper-industry-capacity-and-fiber-consumption-survey) (accessed 2026-07-22): AF&PA reports 2025 US paper and paperboard production down 3.7% to 66.3 million tons, containerboard production down 4.4% to 36.1 million tons with a 91.9% operating rate, and boxboard production essentially flat at 12.4 million tons.
- **S4** — [Pulp and Paper Production (MACT I & III): National Emissions Standards for Hazardous Air Pollutants](https://www.epa.gov/stationary-sources-air-pollution/pulp-and-paper-production-mact-i-iii-national-emissions-standards) (accessed 2026-07-22): EPA describes paperboard mills within regulated integrated, non-integrated, and secondary-fiber mill populations and the required collection, control, treatment, monitoring, and reporting processes.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The 2019 Annual Business Survey infographic reports 51% of responding owners of employer businesses were age 55 or older, 43% were 35-54, and 6% were 34 or younger; estimates cover 4.1 million responding owners for data year 2018.
