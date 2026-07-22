# 333132 — Oil and Gas Field Machinery and Equipment Manufacturing

*v5.1 Stage 1 research memo. Run `333132-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.85 · L 2.33 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large physical installed base with recurring OEM parts and support can combine operational automation with defensible customer relationships.
**Weakness:** Capital-equipment demand is volatile and can be deferred sharply when oilfield customers cut drilling and completion budgets.

## Business-model lens
- Included: U.S. lower-middle-market manufacture of oil and gas field drilling and production machinery, derricks, and water-well drilling machinery, including related aftermarket activity attributable to the manufacturer.
- Excluded: Pumps, underground-mining drills, offshore floating platforms, captive internal work, pure distribution, and firms dominated by rentals or field services rather than manufacturing.
- Customer and revenue model: Recurring or repeat revenue from external customers through equipment programs, replacement units, spare parts, repair, technical support, field service, training, or manufacturer-linked monitoring.
- Deviation from default lens: none

## Executive view
Oilfield and water-well machinery combines automatable fabrication and information work with safety-critical physical products, project variability, and persistent OEM responsibility. The central demand case is nearly flat in real terms but highly cyclical.

## How AI changes the work
CNC and robotic fabrication, machine-vision inspection, AI-assisted engineering and documentation, predictive maintenance, planning, quoting, scheduling, and supply-chain tools can reduce labor and rework; legacy integration and validation limit implementation.

## Value capture
OEM compatibility, switching risk, installed-base service relationships, know-how, delivery performance, and backlog support retention, offset by sophisticated buyer power, negotiated savings, rebids, and competitive repricing.

## Firm availability
A meaningful share of independent manufacturers should fit the external-customer repeat-revenue lens, and broad employer-business succession evidence suggests a material but uncertain five-year control-transfer pool.

## Demand durability
U.S. natural-gas growth offsets broadly stable-to-softer crude, but drilling, completions, workovers, fleet replacement, and customer capital budgets can make equipment demand swing much more than production.

## Risks and uncertainty
Oil and gas price cycles, capital discipline, cancellations, cost overruns, supply disruption, technical failures, export exposure, consolidation, imports, and neighboring-industry misclassification widen the ranges.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4317 | — | OBSERVED | — |
| n | — | 132 | — | ESTIMATE | — |
| a | 0.14 | 0.25 | 0.38 | PROXY | S2, S3 |
| rho | 0.35 | 0.54 | 0.71 | PROXY | S3, S5 |
| e | 0.56 | 0.73 | 0.86 | ESTIMATE | S1, S5 |
| s5 | 0.14 | 0.23 | 0.35 | PROXY | S4 |
| q | 0.38 | 0.56 | 0.73 | ESTIMATE | S5 |
| d5 | 0.75 | 1.03 | 1.27 | PROXY | S5, S6 |
| o | 0.94 | 0.985 | 0.999 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.85 | 2.33 | 4.66 | PROXY |
| F | 3.91 | 5.06 | 5.96 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.05 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation shares are not task shares and the BLS aggregate spans several machinery industries.
- a: Oilfield equipment can have unusually engineered, safety-critical, and project-specific work, so the interval is deliberately wide.
- rho: The NIST evidence concerns manufacturers generally, not this NAICS or LMM firms specifically.
- rho: Large public-company digital offerings indicate sector direction but likely run ahead of smaller manufacturers.
- e: No direct establishment-level dataset measures the intersection of external-customer repeat revenue, independence, correct classification, and the $1-10 million EBITDA band.
- e: NOV is much larger and broader than the target population.
- s5: Owner intentions are not completed transactions.
- s5: The survey is not specific to manufacturing, this NAICS, or the EBITDA band.
- q: This is an estimate of discounted retained gross benefit, not accounting margin.
- q: NOV's global scale, proprietary installed base, and contract mix may imply greater retention than an LMM supplier can achieve.
- d5: Long-horizon production paths do not translate one-for-one into five-year machinery orders.
- d5: NOV is global and includes offshore and broader equipment exposures; water-well machinery has a distinct demand driver.
- o: The estimate assumes persistent demand for accountable equipment manufacturers rather than any specific incumbent.
- o: Product architectures, imports, consolidation, or customer integration could displace some operators without eliminating the industry function.

## Sources
- **S1** — [2022 NAICS Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-23): Exact 333132 definition and exclusions for offshore platforms, underground-mining drills, and pumps.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Machinery Manufacturing](https://www.bls.gov/oes/2023/may/naics4_3330A1.htm) (accessed 2026-07-23): Broad machinery-manufacturing occupational mix used as the task-exposure proxy.
- **S3** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-23): Manufacturing AI adoption, use cases, expected expansion, and implementation barriers.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Employer-business owner age distribution and reported five-year sale or transfer intentions.
- **S5** — [NOV Inc. 2025 Annual Report](https://investors.nov.com/static-files/60aae165-430d-4f04-b787-b243c83612a8) (accessed 2026-07-23): Oilfield-equipment business model, aftermarket and digital services, OEM installed-base support, backlog, contract risks, customer demand drivers, rig counts, prices, and segment revenue mix.
- **S6** — [EIA Releases Annual Energy Outlook 2026](https://www.eia.gov/pressroom/releases/press587.php) (accessed 2026-07-23): U.S. crude-oil and natural-gas production outlook used to anchor the five-year real-demand proxy.
