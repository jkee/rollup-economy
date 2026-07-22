# 333241 — Food Product Machinery Manufacturing

*v5.1 Stage 1 research memo. Run `333241-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.74 · L 1.69 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large installed base creates repeat parts, rebuild, maintenance, software, and replacement demand around safety-critical physical equipment.
**Weakness:** Specialized customer capital projects are lumpy, and large processors can exert strong sourcing and repricing pressure.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers of food and beverage processing machinery, including dairy, bakery, meat and poultry, and other commercial food-product processing equipment, plus manufacturer-attributable replacement, rebuild, parts, service, and monitoring revenue.
- Excluded: Food and beverage packaging machinery, commercial and industrial refrigeration, commercial cooking and food-warming equipment, captive internal units, pure distributors, and service firms that do not manufacture the relevant machinery.
- Customer and revenue model: Recurring or repeat outsourced revenue from external food and beverage processors through equipment programs, replacement units, aftermarket parts, rebuilds, maintenance, service agreements, leases, and manufacturer-linked software.
- Deviation from default lens: none

## Executive view
Food-product machinery has a defensible physical role and recurring installed-base economics, with meaningful but bounded automation inside OEM workflows. Demand is supported by defensive food production and processor automation needs, though capital spending and subsegment shocks remain material.

## How AI changes the work
AI, machine vision, digital twins, design reuse, predictive maintenance, scheduling, quoting, documentation, and robotics can reduce engineering, production, inspection, and support labor, but sanitary customization, trials, field integration, and quality accountability constrain substitution.

## Value capture
Fixed-price work and installed-base parts, rebuild, software, and service relationships support retention; processor sourcing initiatives, rebids, local competition, and negotiated renewals gradually share savings with customers.

## Firm availability
The exact industry includes many specialized OEMs with repeat external customers, but eligibility falls when firms are one-off fabricators, captive, distribution-led, or actually belong to packaging, refrigeration, or cooking-equipment codes. Broad owner evidence indicates a material but uncertain succession pool.

## Demand durability
Trade-association evidence points to continued U.S. shipment growth, reinforced by food safety, sanitation, labor scarcity, yield, and sustainability needs. Real quantity can nevertheless pause during processor capital restraint or agricultural and protein-market shocks.

## Risks and uncertainty
Key risks are processor consolidation and buyer power, fixed-price overruns, tariffs and steel costs, food recalls and animal disease, customer capital deferrals, technology obsolescence, service competition, imports, and extrapolation from large global companies.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2749 | — | OBSERVED | — |
| n | — | 146 | — | ESTIMATE | — |
| a | 0.15 | 0.27 | 0.4 | PROXY | S2, S3, S5 |
| rho | 0.37 | 0.57 | 0.73 | PROXY | S3, S5, S6 |
| e | 0.58 | 0.75 | 0.88 | ESTIMATE | S1, S5 |
| s5 | 0.14 | 0.23 | 0.35 | PROXY | S4 |
| q | 0.42 | 0.61 | 0.78 | ESTIMATE | S5 |
| d5 | 0.97 | 1.1 | 1.24 | PROXY | S5, S6 |
| o | 0.965 | 0.992 | 0.999 | ESTIMATE | S1, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.61 | 1.69 | 3.21 | PROXY |
| F | 4.11 | 5.25 | 6.16 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 9.36 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupational table combines several machinery industries and occupation shares are not task shares.
- a: JBT Marel is far larger and more digital than the target firms.
- rho: NIST reports manufacturers generally rather than food-machinery OEMs.
- rho: Trade-association trends reflect customer-side processing automation as well as automation inside equipment manufacturers.
- e: No source measures the share of LMM firms simultaneously meeting the exact NAICS, independence, external-customer, and repeat-revenue tests.
- e: A leading OEM's 50% recurring mix should not be assumed for smaller manufacturers.
- s5: Gallup covers employer-business owners across industries rather than this NAICS or company-size band.
- s5: Intentions are not completed qualifying transfers.
- q: The range concerns discounted retained gross benefit rather than accounting margin.
- q: JBT Marel's scale, intellectual property, installed base, and service network likely provide more pricing protection than many LMM firms.
- d5: The trade-association forecast reaches 2027 rather than the full five-year horizon and reports shipment value, not constant-price constant-quality quantity.
- d5: JBT Marel is global, diversified, acquisition-affected, and much larger than the U.S. LMM population.
- o: This measures persistence of the accountable operator role, not survival of any incumbent.
- o: Integrated software and third-party equipment support can shift value between machinery OEMs, software vendors, integrators, and processors without eliminating physical equipment demand.

## Sources
- **S1** — [2022 NAICS Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-23): Exact 333241 scope and exclusions for packaging machinery, refrigeration equipment, and commercial cooking equipment.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Machinery Manufacturing](https://www.bls.gov/oes/2023/may/naics4_3330A1.htm) (accessed 2026-07-23): Broad machinery-manufacturing occupational mix used as the task-exposure proxy.
- **S3** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-23): Current manufacturing AI adoption, demonstrated use cases, investment direction, and implementation barriers.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Five-year sale or transfer intentions among U.S. employer-business owners.
- **S5** — [JBT Marel Corporation 2025 Form 10-K](https://ir.jbtmarel.com/sec-filings/all-sec-filings/content/0001433660-26-000053/jbt-20251231.htm) (accessed 2026-07-23): Installed-base and recurring-revenue model, service and digital offerings, fixed-price contract structure, sourcing pressure, backlog, demand conditions, and industry risks.
- **S6** — [PMMI and FPSA Release Inaugural 2026 Processing State of the Industry Report and Infographic](https://www.pmmi.org/news/pmmi-and-fpsa-release-inaugural-2026-processing-state-of-the-industry-report-and-infographic) (accessed 2026-07-23): U.S. food and beverage processing machinery shipment value, near-term forecast, end-market mix, and automation, safety, AI, and sustainability trends.
