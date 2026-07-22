# 562212 — Solid Waste Landfill

*v5.1 Stage 1 research memo. Run `562212-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.26 · L 1.13 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Tipping-fee economics and scarce permitted airspace can retain workflow savings while monitoring, transaction, fleet, and equipment data support targeted automation.
**Weakness:** The addressable work is a minority layer around a capital-intensive, physically executed, environmentally liable operation with long closure obligations.

## Business-model lens
- Included: US lower-middle-market firms operating landfills for nonhazardous solid waste, including firms that combine local collection or hauling with their own landfill operations and repeatedly serve external municipal, commercial, industrial, and construction customers.
- Excluded: Captive internal disposal sites, shell entities, non-control financing vehicles, hazardous-waste treatment or disposal, standalone collection or transfer stations without landfill operations, solid-waste combustors and incinerators, sewage treatment, composting, and other nonhazardous treatment facilities that are not landfills.
- Customer and revenue model: Municipalities, haulers, businesses, institutions, and contractors pay tipping or disposal fees commonly based on tons, loads, waste type, and contract terms; integrated operators may also earn recurring collection fees, environmental surcharges, and revenue from landfill-gas electricity or renewable natural gas.
- Deviation from default lens: none

## Executive view
Solid-waste landfills offer a bounded AI opportunity around scale-house transactions, billing, customer service, dispatch, environmental reporting, monitoring analytics, and maintenance, but the core business remains a capital-intensive physical utility. Permitted airspace, location, heavy equipment, groundwater and methane systems, closure funding, and decades of post-closure responsibility dominate the operating proposition.

## How AI changes the work
AI can extract and validate load data, automate routine customer and billing work, forecast inbound tonnage, optimize integrated routes, flag monitoring anomalies, draft regulatory materials, and prioritize equipment, leachate, and gas-system maintenance. It cannot create airspace, move and compact waste, install cover and liners, sample wells, repair equipment, or assume legal and environmental accountability.

## Value capture
Per-ton and per-load gate pricing and multi-period disposal contracts can preserve early administrative and analytical savings. Local capacity, haul distance, waste acceptance, and permit scarcity support pricing, while municipal bids, escalators, renewals, competing sites, and customer concentration share gains over time.

## Firm availability
The frozen dataset estimates 91 firms in the EBITDA band. In-code firms usually have recurring external disposal revenue, but public or captive sites, larger-parent ownership, depleted airspace, concentrated municipal contracts, weak permits, financial assurance, closure accruals, and environmental liabilities reduce eligible and transferable supply.

## Demand durability
Population, commerce, construction, and cleanup activity continue to generate residual waste, but recycling, composting, organics rules, waste prevention, incineration, and other diversion constrain landfill growth. Real demand is likely durable but slow-growing and highly local. Remaining landfill volume still requires an accountable physical operator through active life, closure, and post-closure care.

## Risks and uncertainty
The largest evidence gaps are the six-digit task mix, realized AI savings, current commercial landfill tonnage, remaining airspace, contract terms, and completed LMM transfers. Major risks include groundwater or methane releases, fires, injury, odor and community opposition, permit restrictions, airspace depletion, leachate costs, closure underfunding, diversion mandates, customer concentration, cyber failures, and inherited contamination.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2963 | — | OBSERVED | — |
| n | — | 91 | — | ESTIMATE | — |
| a | 0.1 | 0.19 | 0.31 | PROXY | S2, S3, S5 |
| rho | 0.28 | 0.5 | 0.68 | ESTIMATE | S3, S7 |
| e | 0.72 | 0.87 | 0.95 | ESTIMATE | S1, S3 |
| s5 | 0.06 | 0.14 | 0.23 | PROXY | S3, S6 |
| q | 0.5 | 0.68 | 0.82 | ESTIMATE | — |
| d5 | 0.9 | 1.03 | 1.16 | PROXY | S4, S5 |
| o | 0.9 | 0.96 | 0.99 | PROXY | S3, S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 1.13 | 2.50 | ESTIMATE |
| F | 2.57 | 4.01 | 4.89 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.10 | 9.89 | 10.00 | PROXY |

## Caveats
- a: OEWS covers broader NAICS 562200 and mixes landfills with other treatment and disposal facilities.
- a: Employment shares do not measure wage-weighted task time, current automation, or six-digit operating differences.
- a: Integrated collection-and-landfill firms may have more routing and customer-service exposure than standalone disposal sites.
- rho: No source directly measures AI implementation or avoided labor in LMM landfill firms.
- rho: Monitoring and transaction data availability varies substantially by facility and does not guarantee interoperable systems.
- rho: Environmental compliance and safety decisions require accountable human review even when analysis is automated.
- e: NAICS establishment classification does not reveal external-customer share, public ownership, or captive status.
- e: Remaining airspace and permit quality can determine eligibility even when current EBITDA fits the lens.
- e: The frozen n of 91 is a margin-bridged estimate and is not re-estimated here.
- s5: Gallup covers all employer businesses and reports intentions rather than completed sales.
- s5: The source does not isolate waste firms, landfills, LMM EBITDA, or qualifying control transactions.
- s5: A landfill sale may transfer long-tail closure and remediation liabilities that materially alter deal structure.
- q: No representative source reports revenue-weighted contract structures or AI-benefit pass-through for LMM NAICS 562212 firms.
- q: Unit pricing supports initial retention but does not prevent competitive or contractual repricing over five years.
- q: Airspace depletion, fuel, leachate, closure accruals, host fees, and capital spending can overwhelm labor-related savings.
- d5: EPA's latest national materials-flow figures on the cited page are for 2018 and only municipal solid waste.
- d5: Refuse-collector employment is not landfill output and includes collection and recycling activity.
- d5: Demand can rise nationally while individual facilities lose volume because of diversion rules, route changes, closures, or exhausted airspace.
- o: Federal criteria are implemented primarily through states, which may impose different or stricter requirements.
- o: The LMOP database is not exhaustive and includes closed as well as accepting municipal landfills, not all NAICS 562212 firms.
- o: Operator need remains high for residual tonnage, but diversion can remove demand before it reaches a landfill.

## Sources
- **S1** — [NAICS 562212 Solid Waste Landfill definition](https://www.census.gov/naics/resources/archives/sect56.html) (accessed 2026-07-22): Defines the industry as nonhazardous solid-waste landfill operation, including combined local collection or hauling with landfill disposal, and distinguishes adjacent waste activities.
- **S2** — [May 2023 OEWS: Waste Treatment and Disposal](https://www.bls.gov/oes/2023/may/naics4_562200.htm) (accessed 2026-07-22): Reports the broader NAICS 562200 occupation mix, including transportation and material moving at 44.51%, construction and extraction at 15.40%, office support at 9.47%, maintenance at 8.48%, production at 5.61%, and management at 6.63%.
- **S3** — [EPA Requirements for Municipal Solid Waste Landfills](https://www.epa.gov/landfills/requirements-municipal-solid-waste-landfills-mswlfs) (accessed 2026-07-22): Details groundwater monitoring, corrective action, closure plans, final cover, financial assurance, and a standard 30-year post-closure period maintaining cover, leachate, groundwater, and methane systems.
- **S4** — [EPA National Overview: Facts and Figures on Materials, Wastes and Recycling](https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/national-overview-facts-and-figures-materials) (accessed 2026-07-22): Reports 292.4 million tons of municipal solid waste generated and about 146.1 million tons landfilled in 2018, alongside recycling, composting, combustion, and other management pathways.
- **S5** — [Occupational Outlook Handbook: Hand Laborers and Material Movers](https://www.bls.gov/ooh/transportation-and-material-moving/hand-laborers-and-material-movers.htm) (accessed 2026-07-22): Describes refuse-collector physical and driving duties and projects refuse and recyclable material collector employment to increase from 147,900 in 2024 to 149,200 in 2034, while noting population support and routing automation.
- **S6** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of US employer-business owners planned to sell, transfer, or take public within five years, including 13% planning a sale and 11% a transfer.
- **S7** — [EPA LMOP Landfill and Project Database](https://www.epa.gov/lmop/lmop-landfill-and-project-database) (accessed 2026-07-22): Reports a database of more than 2,600 municipal landfills and, as of September 2024, 488 landfills supplying gas to 542 operational energy projects, with explicit non-exhaustiveness caveats.
