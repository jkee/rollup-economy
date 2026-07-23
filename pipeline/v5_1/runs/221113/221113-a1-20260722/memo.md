# 221113 — Nuclear Electric Power Generation

*v5.1 Stage 1 research memo. Run `221113-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.19 · L 0.05 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Long-lived licensed plants provide high-reliability baseload output into growing electricity demand.
**Weakness:** The transferable LMM firm population is nearly nonexistent and safety rules constrain labor substitution.

## Business-model lens
- Included: Independent LMM operators of commercially licensed nuclear generation facilities that repeatedly provide electricity and capacity to external transmission systems, distribution utilities, markets, or contracted customers.
- Excluded: Vertically integrated captive units, government and research reactors, passive financing vehicles without operations, decommissioning-only entities, shells, and firms outside the EBITDA band.
- Customer and revenue model: Recurring regulated, merchant, capacity, or long-term contracted revenue from licensed baseload nuclear generation, with extensive operations, maintenance, security, radiation-protection, fuel, and compliance obligations.
- Deviation from default lens: none

## Executive view
Nuclear generation has durable physical demand and substantial information work, but safety regulation sharply limits implementation and the eligible LMM acquisition universe is effectively negligible.

## How AI changes the work
Appropriate uses include document and procedure retrieval, work planning, predictive maintenance, outage scheduling, configuration checks, compliance drafting, inventory, and operating-data analysis. Licensed control, field operations, maintenance, radiation protection, chemistry, security, emergency response, and safety decisions remain human-accountable.

## Value capture
Regulated rates, long-term contracts, and competitive market pricing share operating savings with customers. Capacity value, fixed prices, and better outage execution preserve only part of the benefit.

## Firm availability
Three estimated firms before screening likely overstates true LMM supply. Commercial reactors generally belong to large utilities or portfolios, and transfer requires licenses, qualified personnel, financial assurance, security, contracts, and regulator approval.

## Demand durability
Nuclear output is forecast stable to growing in the near term, supported by electricity-load growth, uprates, restarts, and long-lived assets. Outages, closure economics, fuel constraints, and licensing delay create downside.

## Risks and uncertainty
Catastrophic safety risk, cyber and physical security, nuclear liability, waste and decommissioning obligations, licensed staffing, outage overruns, regulator independence, ownership approval, and the weak firm-count bridge dominate.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1995 | — | OBSERVED | — |
| n | — | 3 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.27 | PROXY | S1, S2, S3 |
| rho | 0.2 | 0.36 | 0.53 | ESTIMATE | S1, S2, S3 |
| e | 0.05 | 0.16 | 0.33 | ESTIMATE | S3, S4, S5 |
| s5 | 0.02 | 0.06 | 0.14 | PROXY | S4, S6 |
| q | 0.16 | 0.31 | 0.49 | ESTIMATE | S5 |
| d5 | 0.97 | 1.07 | 1.18 | PROXY | S5, S7 |
| o | 0.99 | 0.999 | 1 | ESTIMATE | S1, S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.16 | 0.52 | 1.14 | ESTIMATE |
| F | 0.00 | 0.05 | 0.21 | ESTIMATE |
| C | 3.20 | 6.20 | 9.80 | ESTIMATE |
| D | 9.60 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No public nuclear-specific wage-weighted task study.
- a: The three-firm estimate makes representative sampling difficult.
- rho: Bounded judgment rather than observed adoption.
- rho: Autonomous reactor control and safety disposition are excluded.
- e: Utility margin bridge is poorly suited to nuclear plants with large fixed obligations.
- e: Establishments, licenses, owners, and transferable operating firms are not equivalent.
- s5: Economy-wide owner-age proxy is especially weak.
- s5: Asset transfers outside LMM must be excluded.
- q: Commercial structure varies materially by plant and region.
- q: No public contract sample measures AI-benefit retention.
- d5: Near-term forecast does not ensure five-year growth.
- d5: Advanced reactors may not enter the current service basket or LMM ownership.
- o: Operator consolidation may change ownership, not eliminate operator need.
- o: This is separate from labor efficiency within a plant.

## Sources
- **S1** — [NRC Operator Licensing](https://www.nrc.gov/reactors/operator-licensing) (accessed 2026-07-22): NRC licenses all individuals who operate or supervise controls at commercially owned power reactors and oversees initial and requalification examinations.
- **S2** — [NRC Licensing Process for Reactor Operators](https://www.nrc.gov/reactors/operator-licensing/licensing-process) (accessed 2026-07-22): NRC describes written examinations, plant walkthroughs, simulator performance demonstrations, and facility-certified training and experience.
- **S3** — [NRC Inspection and Safety Oversight](https://ww2.nrc.gov/about-nrc/regulatory/safety-oversight.html) (accessed 2026-07-22): NRC inspects organizational structure, operator qualifications, design, maintenance, fuel handling, environmental programs, and radiation protection at licensed plants.
- **S4** — [NRC License Transfers and Mergers](https://www.nrc.gov/reactors/operating/licensing/license-transfers-mergers) (accessed 2026-07-22): NRC maintains active license-transfer reviews and explains that plant personnel, procedures, and policies typically are not themselves part of a transfer.
- **S5** — [EIA Forecasts Strong Electricity-Demand Growth Through 2027](https://www.eia.gov/pressroom/releases/press582.php) (accessed 2026-07-22): EIA forecasts nuclear at 18% of U.S. generation in 2025, 2026, and 2027 and electricity demand rising 1% in 2026 and 3% in 2027.
- **S6** — [2024 Chartbook on Firms by Age of Primary Owner](https://www.fedsmallbusiness.org/-/media/project/smallbizcredittenant/fedsmallbusinesssite/fedsmallbusiness/files/2024/firms-in-focus/sbcs_chartbook2024_ownerage.pdf) (accessed 2026-07-22): Federal Reserve owner-age evidence used only as a broad succession proxy.
- **S7** — [The Nation's Nuclear Reactor Fleet Is on the Rise](https://www.energy.gov/ne/articles/nations-nuclear-reactor-fleet-rise) (accessed 2026-07-22): DOE describes initiatives to increase output through uprates, restart dormant facilities, and complete stalled projects amid industrial and data-center load growth.
