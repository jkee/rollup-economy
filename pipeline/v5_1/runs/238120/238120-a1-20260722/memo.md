# 238120 — Structural Steel and Precast Concrete Contractors

*v5.1 Stage 1 research memo. Run `238120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.16 · L 1.43 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digitally modeled but physically executed work creates useful AI-assisted coordination while preserving the need for a safety-accountable field operator.
**Weakness:** Most labor remains hazardous hands-on erection, and hard-bid project turnover exposes savings to customer and competitor repricing.

## Business-model lens
- Included: US lower-middle-market contractors that erect and assemble structural steel or precast concrete and install reinforcing steel for external owners, general contractors, fabricators, and precast producers, including new work, additions, maintenance, and repairs.
- Excluded: Shells, captive erection crews, non-control financing vehicles, pure steel fabrication or precast manufacturing without field contracting operations, poured-in-place concrete contractors, and engineering-only firms.
- Customer and revenue model: Project-based specialty subcontracting, generally awarded as fixed-price, lump-sum, or unit-price scopes with progress billing and change orders; repeat revenue comes through relationships with general contractors, fabricators, precast suppliers, industrial owners, and public agencies rather than subscriptions.
- Deviation from default lens: none

## Executive view
Structural-steel and precast contractors offer a bounded AI labor opportunity in estimating, VDC/model review, project controls, documentation, and administration, while the dominant erection workforce remains physical and safety-critical. The operator role is durable and demand is plausibly stable to modestly growing, but cyclical end markets and repeated competitive bidding limit retention.

## How AI changes the work
AI can assist model and drawing comparison, specification search, takeoffs, bid and scope drafting, lift-plan inputs, logistics scenarios, RFIs and submittals, schedule-risk review, daily-report synthesis, safety-document preparation, invoice coding, and collections. Human estimators, detailers, project managers, superintendents, riggers, and ironworkers remain responsible for completeness, temporary stability, constructability, safe picks, connections, welding, field tolerances, and exceptions.

## Value capture
Better coordination and estimating can protect margin on awarded work and let scarce overhead staff support more projects. Generic efficiency is likely to leak into future bid prices, while durable value depends on proprietary production data, fewer field errors, stronger safety and schedule reliability, and integration with the contractor's BIM and project systems.

## Firm availability
Most firms are externally facing specialty contractors, but transferability depends heavily on management depth, surety and customer relationships, certifications, labor access, and safety performance. Broad construction surveys indicate substantial owner-exit intent, yet internal transitions are common and weak preparation reduces the completed third-party control-transfer pool.

## Demand durability
Commercial and industrial buildings, infrastructure, and bridge rehabilitation continue to require steel, reinforcing steel, and precast erection. BLS projects modest growth for ironworkers and the broader contractor group, while the PCI outlook shows growth pockets alongside slower aggregate expansion; present construction spending softness and end-market cycles remain meaningful downside risks.

## Risks and uncertainty
The largest uncertainties are the lack of a current six-digit wage-weighted occupation table, no direct AI implementation or pass-through study for erectors, the mixed steel/rebar/precast population, owner and credential dependence, serious safety and model-quality risks, tariffs and material volatility, and cyclicality. A bad outcome combines limited office savings, costly integration, fast price pass-through, and a contraction in nonresidential starts.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3614 | — | ESTIMATE | — |
| n | — | 152 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.27 | PROXY | S2, S3, S4, S6 |
| rho | 0.32 | 0.55 | 0.73 | ESTIMATE | S5, S6, S7 |
| e | 0.8 | 0.9 | 0.96 | ESTIMATE | S1 |
| s5 | 0.13 | 0.23 | 0.33 | PROXY | S8, S9 |
| q | 0.21 | 0.38 | 0.58 | ESTIMATE | S1, S7 |
| d5 | 0.9 | 1.02 | 1.16 | PROXY | S4, S10, S11, S12 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1, S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.46 | 1.43 | 2.85 | ESTIMATE |
| F | 4.54 | 5.60 | 6.27 | ESTIMATE |
| C | 4.20 | 7.60 | 10.00 | ESTIMATE |
| D | 8.46 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: CES uses the five-digit 23812 series and does not provide a full wage-weighted occupation matrix for this packet.
- a: Production-and-nonsupervisory status is not identical to physical task content.
- a: The frozen compensation ratio is ancestor-level 23812 and mixes 2024 wages with 2022 receipts before harmonization.
- rho: RICS respondents were global construction professionals, not a US NAICS 238120 LMM sample.
- rho: No controlled concrete-or-steel-erector implementation study was found.
- e: Eligibility is not observed, and the NAICS combines structural-steel erection, reinforcing-steel placement, and precast installation.
- e: The supplied firm count is a margin bridge from size-class data rather than an observed list of firms in the EBITDA band.
- s5: FMI/CFMA is a broad voluntary E&C survey and not a probability sample of steel and precast erection contractors.
- s5: Internal equity transitions do not necessarily constitute a qualifying control transfer.
- q: No direct study of AI-benefit pass-through in steel erection, reinforcing-steel placement, or precast installation was found.
- q: Retention differs across hard-bid public work, negotiated industrial projects, and subcontractor relationships with affiliated fabricators.
- d5: Employment is an indirect demand proxy and the available projection is broad-industry or occupation level rather than NAICS 238120 output.
- d5: Census construction spending is nominal and short-term, not the required constant-price quantity measure.
- d5: Demand varies materially between structural steel, rebar placement, and precast erection and across local end markets.
- o: Operator requirement is a five-year judgment rather than a directly measured outcome.
- o: Integrated fabricator-erector models and modular construction may advance faster in selected segments than nationally.

## Sources
- **S1** — [238120: Structural Steel and Precast Concrete Contractors — Census Bureau Profile](https://data.census.gov/profile/238120_-_Structural_Steel_and_Precast_Concrete_Contractors?codeset=naics~238120) (accessed 2026-07-22): Defines erection and assembly of structural steel or precast parts and installation of reinforcing steel, including new work, alterations, maintenance, and repairs; reports 4,005 employer establishments in 2023.
- **S2** — [Employees on nonfarm payrolls by industry, May 2026](https://www.bls.gov/ces/data/employment-and-earnings/2026/table1b_202605.htm) (accessed 2026-07-22): Reports 85,000 employees for structural steel and precast concrete contractors in the current May 2026 column.
- **S3** — [Production and nonsupervisory employment by industry, May 2026](https://www.bls.gov/ces/data/employment-and-earnings/2026/table6b_202605.htm) (accessed 2026-07-22): Reports 72,300 production and nonsupervisory employees for structural steel and precast concrete contractors in the current May 2026 column.
- **S4** — [Ironworkers — Occupational Outlook Handbook](https://www.bls.gov/ooh/construction-and-extraction/structural-iron-and-steel-workers.htm) (accessed 2026-07-22): Describes physically demanding outdoor and height work, safety hazards, 65,700 structural iron and steel workers in 2024, and 4% projected ironworker growth through 2034 tied to buildings and aging highways and bridges.
- **S5** — [Optimism high for AI in construction but skills shortages and integration challenges adoption](https://www.rics.org/news-insights/optimism-high-for-ai-in-construction-but-skills-shortages-and-integration-challenges-adoption) (accessed 2026-07-22): More than 2,200 global construction-professional responses: 45% reported no AI use, 1% had scaled across projects, and barriers included skilled personnel, system integration, and data quality.
- **S6** — [AISC BIM & VDC Resources](https://www.aisc.org/aisc/solutions-center/bim-vdc-resources/) (accessed 2026-07-22): States BIM is now an everyday occurrence and provides structural-steel-specific BIM and model-review guidance addressing design and fabrication issues.
- **S7** — [AGC/NCCER 2025 Craft Workforce Survey](https://www.nccer.org/research/2025-workforce-survey-agc-nccer/) (accessed 2026-07-22): Nearly 1,400 construction firms responded and 92% reported difficulty hiring for open positions.
- **S8** — [FMI Releases 2024 Study on Ownership Transfer and Management Succession](https://fmicorp.com/about/news/fmi-releases-2024-study-on-ownership-transfer-and-management-succession) (accessed 2026-07-22): Nearly 300 E&C leaders surveyed; 38% planned to exit in three to five years, half of that group lacked an ownership transition plan, and 58% overall lacked a plan.
- **S9** — [The Ownership Clock Is Running Out](https://fmicorp.com/insights/quick-reads/the-ownership-clock-is-running-out) (accessed 2026-07-22): Reports 58% lack a formal transfer plan, 51% of owners planning to exit within five years lack a defined strategy, and about 64% plan internal ownership transitions.
- **S10** — [Employment and output by industry, 2024–2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects foundation, structure, and building exterior contractor employment from 992,500 in 2024 to 1,032,100 in 2034, a 4.0% increase.
- **S11** — [Monthly Construction Spending, May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-22): Reports total construction spending 1.5% below May 2025, first-five-month spending 2.7% below 2025, private nonresidential at a $738.7 billion annual rate, and public construction at $541.2 billion.
- **S12** — [PCI 2026 Market and Construction Forecast](https://oasis.pci.org/AssetListing/PCI-2026-Market-and-Construction-Forecast-13438/Handout-PCI-2026-Market-Forecast-Webinar-24041) (accessed 2026-07-22): Forecasts total construction growth through 2029 at slower rates, with precast opportunities in K-12, bridges, parking, apartments, and data centers, while noting regional contraction and segment divergence.
