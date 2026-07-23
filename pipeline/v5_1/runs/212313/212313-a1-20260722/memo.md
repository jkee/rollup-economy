# 212313 — Crushed and Broken Granite Mining and Quarrying

*v5.1 Stage 1 research memo. Run `212313-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.40 · L 0.72 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Permitted reserves close to recurring infrastructure demand create a physically durable local franchise that can benefit from operational AI.
**Weakness:** The core business sells crushed stone rather than a recurring outsourced service, sharply reducing lens eligibility despite attractive operational characteristics.

## Business-model lens
- Included: Lower-middle-market granite quarry and preparation-plant operators selling crushed granite, including recurring deliveries to contractors, asphalt and concrete producers, and public works customers; genuine contract or toll crushing is included where present.
- Excluded: Dimension-stone operations, limestone and sand-and-gravel producers, captive quarries whose output is consumed only by an integrated parent, greenfield mine development, and businesses without meaningful third-party recurring revenue.
- Customer and revenue model: Revenue is primarily per-ton product sales and delivery charges to local or regional construction and infrastructure customers, with some repeat purchase orders and only a small qualifying outsourced-service component from contract processing.
- Deviation from default lens: none

## Executive view
Granite quarrying has durable physical demand and meaningful site scarcity, but it is a weak fit for a recurring outsourced-service rollup because revenue is overwhelmingly product-and-delivery based. AI is more likely to improve an existing operator than to redefine the acquisition universe.

## How AI changes the work
The practical AI wedge is in dispatch, quoting, maintenance triage, production optimization, quality records, compliance administration, and customer communication. The dominant work and risk remain embodied in extraction, materials handling, plant uptime, and field safety.

## Value capture
Benefits can accrue through fewer unplanned outages, tighter yield and energy management, faster quote-to-order cycles, lower administrative load, and better fleet routing, but commodity competition makes it difficult to retain every efficiency gain as margin.

## Firm availability
Owner succession may create opportunities, yet quarry transfers are gated by reserve quality, permits, land or mineral rights, reclamation liabilities, equipment condition, and local demand. The qualifying service-revenue subset is materially smaller than the headline establishment pool.

## Demand durability
Road maintenance, infrastructure renewal, and broader construction activity support recurring aggregate consumption. Demand remains sensitive to local construction cycles, weather, public-project timing, substitutes, and the economics of hauling a low-value heavy material.

## Risks and uncertainty
The largest uncertainties are the scarcity of granite-specific task data, unknown contract-processing revenue share, local rather than national competitive structure, transaction availability, reserve life, and environmental or zoning constraints.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.182 | — | OBSERVED | — |
| n | — | 37 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S1, S2 |
| rho | 0.35 | 0.55 | 0.7 | ESTIMATE | — |
| e | 0.03 | 0.12 | 0.27 | ESTIMATE | S1 |
| s5 | 0.08 | 0.16 | 0.27 | PROXY | S5, S2 |
| q | 0.35 | 0.55 | 0.72 | ESTIMATE | S2, S3 |
| d5 | 0.93 | 1.04 | 1.16 | PROXY | S2, S4 |
| o | 0.95 | 0.985 | 0.999 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.25 | 0.72 | 1.43 | ESTIMATE |
| F | 0.14 | 0.86 | 2.10 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.84 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The USGS crushed-stone category covers rock types beyond granite.
- a: Automation potential varies sharply with plant age, sensor coverage, and fleet standardization.
- rho: No industry-specific autonomous-task completion study was located.
- rho: Safety and environmental accountability constrain full substitution even when decision support is technically capable.
- e: Repeat product orders alone do not make aggregate sales an outsourced service.
- e: Firm-level contract processing incidence is not published in the cited industry definition.
- s5: Gallup covers employer businesses broadly, not mining.
- s5: Stated plans are not completed transactions.
- q: Defensibility is highly local.
- q: Public-project bidding and recycled aggregate can limit pricing power.
- d5: Crushed-stone totals include limestone and other rock types.
- d5: Construction spending is an imperfect volume proxy and can rise because of prices rather than tonnage.
- o: Outsourcing individual functions does not remove the need for an accountable operating company.

## Sources
- **S1** — [North American Industry Classification System: 212313 Crushed and Broken Granite Mining and Quarrying](https://www.census.gov/naics/?details=212&input=212&year=2017) (accessed 2026-07-22): Industry scope: mine-site development, granite quarrying, and preparation plants grinding or pulverizing granite and related rocks.
- **S2** — [Mineral Commodity Summaries 2026: Stone (Crushed)](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-stone-crushed.pdf) (accessed 2026-07-22): 2025 crushed-stone production, sector demand drivers, construction uses, and continuing permitting, zoning, environmental, and safety issues.
- **S3** — [USGS Statistical Compendium: Crushed Stone](https://www.usgs.gov/centers/national-minerals-information-center/statistical-compendium) (accessed 2026-07-22): Characterizes crushed stone as a high-volume, low-value, highly competitive product serving local or regional markets, with costs shaped by labor, equipment, energy, water, and compliance.
- **S4** — [U.S. Census Bureau: May 2026 Construction Spending](https://www.census.gov/construction/c30/pdf/totsa.pdf) (accessed 2026-07-22): Public highway-and-street construction annual rate and year-over-year change as an end-market demand indicator.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry employer-business owner survey: 22% planned to sell or transfer their business within five years.
