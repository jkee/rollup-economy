# 326160 — Plastics Bottle Manufacturing

*v5.1 Stage 1 research memo. Run `326160-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.20 · L 0.93 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat physical demand combined with improvable planning, quality, uptime, and administrative workflows.
**Weakness:** Capital intensity and buyer bargaining power constrain implementation and long-run retention of savings.

## Business-model lens
- Included: US lower-middle-market manufacturers producing plastic bottles for external food, beverage, household, personal-care, pharmaceutical, and industrial customers through recurring or repeat supply relationships.
- Excluded: Captive in-house bottle plants, plastic containers other than bottles, resin production, distributors without manufacturing operations, shells, and non-control financing vehicles.
- Customer and revenue model: Predominantly repeat B2B sales under customer specifications, purchase orders, supply agreements, and negotiated unit pricing; revenue is volume multiplied by per-unit bottle prices, often with resin-cost adjustment mechanisms.
- Deviation from default lens: none

## Executive view
Plastic bottle manufacturing offers a bounded operational AI opportunity inside a capital-intensive, repeat-order B2B business. The best uses improve planning, inspection, documentation, uptime, and commercial administration; the physical process and customer qualification remain central.

## How AI changes the work
AI can assist quoting, production scheduling, resin and inventory planning, quality-document review, predictive maintenance, vision inspection, and customer-service workflows. Production labor and line interventions remain constrained by machinery, safety, uptime, and validation.

## Value capture
Near-term savings may be retained between negotiations and when they improve scrap, uptime, or responsiveness in ways customers cannot easily benchmark. Over renewals, concentrated buyers and competitive bidding are likely to share or extract a meaningful portion.

## Firm availability
The code is coherent, but not every counted firm is an independent, transferable platform: captive plants, weak assets, concentration, and environmental or capex liabilities matter. General small-business succession evidence supports deal flow but is not industry-specific.

## Demand durability
Recurring needs for rigid bottles support stable quantities, yet packaging policy, lightweighting, reuse, alternative materials, and large customers' insourcing create real downside. Remaining outsourced demand still requires a responsible physical operator.

## Risks and uncertainty
The largest uncertainties are six-digit task mix, the installed automation baseline, customer contract economics, eligible-firm ownership, and actual transaction incidence. Resin volatility, customer concentration, obsolete blow-molding assets, food or pharmaceutical compliance, and environmental liabilities can overwhelm workflow gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1699 | — | OBSERVED | — |
| n | — | 102 | — | ESTIMATE | — |
| a | 0.16 | 0.24 | 0.33 | PROXY | S1 |
| rho | 0.42 | 0.57 | 0.7 | PROXY | S2 |
| e | 0.38 | 0.53 | 0.68 | ESTIMATE | S3 |
| s5 | 0.12 | 0.2 | 0.3 | PROXY | S4 |
| q | 0.34 | 0.5 | 0.66 | ESTIMATE | — |
| d5 | 0.94 | 1.01 | 1.09 | ESTIMATE | S2, S3 |
| o | 0.94 | 0.98 | 0.995 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.46 | 0.93 | 1.57 | PROXY |
| F | 2.79 | 3.97 | 4.96 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 8.84 | 9.90 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source is four-digit NAICS 326100 rather than six-digit 326160.
- a: AI task exposure is inferred rather than measured.
- a: Existing machine and vision automation is excluded conceptually but not observable in the source table.
- rho: The cited occupation group includes metalworking and processes unlike bottle manufacturing.
- rho: Implementation depends heavily on plant age, SKU changeover frequency, and customer validation requirements.
- e: The frozen firm-count estimate is margin-bridged rather than observed.
- e: NAICS establishment classification does not disclose independent ownership or recurring-customer status.
- s5: Cross-industry survey intentions are not completed transactions.
- s5: No six-digit owner-age or deal-flow series was found.
- q: No public contract sample quantifies pass-through for independent bottle manufacturers.
- q: Retention varies sharply with custom tooling, qualification costs, and customer concentration.
- d5: The range is judgment rather than a constant-price six-digit forecast.
- d5: End-market and resin mix differ materially across bottle plants.
- o: Operator requirement is inferred from the physical manufacturing activity.
- o: Packaging substitution is also reflected in d5, so o is limited to insourcing, self-service, and software-only displacement.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 326100 Plastics Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-22): Confirms that the source covers employers of all sizes in NAICS 326100 and provides its occupation employment and wage mix, including a large production-occupation presence used to bound AI task exposure.
- **S2** — [Metal and Plastic Machine Workers, Occupational Outlook Handbook](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-22): Reports a projected 7 percent employment decline from 2024 to 2034 and explains that firms continue expanding CNC tools, robots, and other labor-saving machinery while computerized equipment still requires skilled operation and maintenance.
- **S3** — [2007 NAICS Definition: 326160 Plastics Bottle Manufacturing](https://www2.census.gov/econ2007/Reference_materials/htm%20files/326160.htm) (accessed 2026-07-22): Defines the industry as establishments primarily engaged in manufacturing plastics bottles and distinguishes other plastic containers, grounding the lens and physical-operator requirement.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports a fall 2024 survey of employer-business owners about plans over the next five years and that 74 percent of owners planning for retirement intend to sell or transfer ownership, used only as a cross-industry transfer proxy.
