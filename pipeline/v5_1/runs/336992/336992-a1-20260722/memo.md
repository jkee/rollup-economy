# 336992 — Military Armored Vehicle, Tank, and Tank Component Manufacturing

*v5.1 Stage 1 research memo. Run `336992-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.57 · L 0.66 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Multi-year vehicle franchises, fleet modernization, spares, and allied recapitalization can sustain repeat demand for qualified specialized suppliers.
**Weakness:** The independently transferable LMM target set is probably thin and each candidate may carry acute program, prime-customer, clearance, and contract-transfer concentration.

## Business-model lens
- Included: U.S. lower-middle-market independent manufacturers whose primary activity is producing complete military armored vehicles, combat tanks, self-propelled weapons, or specialized tank components for repeat government, prime-contractor, or allied-customer programs.
- Excluded: Nonarmored military universal carriers, government arsenals and depots, captive business units that cannot transfer independently, firms whose primary activity is generic fabricated-metal or electronics production outside this NAICS code, and financing or shell entities.
- Customer and revenue model: Revenue comes from competitively awarded or negotiated prime contracts, subcontracts, task or delivery orders, options, modifications, and multi-year production programs; pricing can be firm-fixed-price, cost-reimbursement, or time-and-materials, with repeat work tied to platform production, upgrades, spares, and allied orders.
- Deviation from default lens: none

## Executive view
Demand is strategically durable and recent prime backlog is strong, but the exact LMM acquisition pool is likely much smaller than the frozen estimate implies. The best targets are independent, qualified component suppliers with repeat positions across several funded platforms, transferable clearances and contracts, and limited dependence on a single prime or option year.

## How AI changes the work
AI can improve digital engineering, requirements analysis, estimating, procurement, scheduling, configuration documentation, quality analytics, inspection, and maintenance. Physical armor fabrication and integration, classified-data controls, validation, and accountable engineering sign-off keep the opportunity assistive rather than autonomous.

## Value capture
Fixed-price production can retain savings until repricing, while cost-reimbursement work and transparent government or prime negotiations pass benefits back quickly. Scarce qualification and reliable delivery support retention, but compliance costs and rebids limit it.

## Firm availability
Full vehicle franchises are concentrated in primes far above the LMM band, while independently purchasable exact-code component firms are difficult to distinguish from captive sites and suppliers classified by production process. Succession may produce deals, but clearance, FOCI, customer, and novation diligence narrow the executable set.

## Demand durability
Long-lived fleets, modernization, spares, allied orders, and a large cited Combat Systems backlog support the five-year outlook. The Army's lower FY2026 tracked-vehicle request and ordinary program volatility argue against extrapolating the recent backlog increase.

## Risks and uncertainty
Principal risks are the estimated firm count, establishment-versus-firm classification, single-program and single-prime concentration, fixed-price overruns, budget or option changes, export and security constraints, clearance continuity, customer-controlled data, and long qualification cycles.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1245 | — | OBSERVED | — |
| n | — | 23 | — | ESTIMATE | — |
| a | 0.16 | 0.28 | 0.41 | PROXY | S2, S3 |
| rho | 0.28 | 0.47 | 0.65 | PROXY | S3, S9 |
| e | 0.22 | 0.42 | 0.62 | ESTIMATE | S1, S5, S8, S9 |
| s5 | 0.1 | 0.18 | 0.29 | PROXY | S4, S8, S9 |
| q | 0.38 | 0.57 | 0.75 | ESTIMATE | S5 |
| d5 | 0.9 | 1.08 | 1.29 | PROXY | S5, S6, S7 |
| o | 0.97 | 0.992 | 0.999 | ESTIMATE | S1, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.22 | 0.66 | 1.33 | PROXY |
| F | 0.66 | 1.62 | 2.63 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.73 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: NAICS 336900 also includes motorcycles, bicycles, and miscellaneous transportation equipment with a different occupational mix.
- a: NIST documents manufacturing-wide applications and adoption, not measured labor displacement in classified defense production.
- rho: NIST's reported adoption is not specific to cleared facilities or military programs.
- rho: Security requirements differ by contract and component; not every exact-industry firm handles classified information.
- e: The frozen firm count is margin-bridged and estimated; the Auto Parts margin may not represent defense-vehicle suppliers.
- e: NAICS is establishment-based, while acquisition eligibility is a firm-level and often contract-specific question.
- e: Stock purchases and asset purchases face different government-contract transfer mechanics.
- s5: Gallup covers employer businesses across all industries, not defense manufacturing.
- s5: A stock transaction may avoid novation but can still trigger ownership, clearance, customer, and FOCI review.
- s5: Survey intentions may be delayed or never become arm's-length sales.
- q: General Dynamics' company-wide U.S. government contract mix is not the contract mix of an LMM tank-component supplier.
- q: Retention varies materially between firm-fixed-price subcontracts, cost-plus development, and competitively rebid production.
- q: Savings may be consumed by compliance, cybersecurity, validation, and higher output requirements.
- d5: General Dynamics Combat Systems includes munitions and weapon systems outside NAICS 336992 and reflects one large prime.
- d5: The FY2026 Army figure is a budget request, not final outlays, and covers weapons and tracked combat vehicles more broadly than the exact code.
- d5: Modernization investment does not translate one-for-one into armored-vehicle manufacturing revenue.
- o: This is a bounded judgment rather than an observed operator-requirement statistic.
- o: The estimate concerns continued need for an accountable manufacturer, not whether the same private firm or platform wins future work.
- o: Unmanned or differently configured ground systems can change the product basket while still requiring manufacturing.

## Sources
- **S1** — [2022 NAICS Manual: 336992 Military Armored Vehicle, Tank, and Tank Component Manufacturing](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Exact scope: complete military armored vehicles, combat tanks, specialized tank components, and self-propelled weapons; excludes nonarmored military universal carriers.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 336900 Other Transportation Equipment Manufacturing](https://www.bls.gov/oes/2023/may/naics4_336900.htm) (accessed 2026-07-22): Broad occupational mix used for task exposure, including production, engineering, office and administrative support, maintenance, welding, assembly, and inspection employment.
- **S3** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Manufacturing AI adoption and use cases in maintenance, quality, forecasting, assembly, vision, documents, supply chain, scheduling and digital twins, plus data, cost, skill, cyber and legacy-integration barriers.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): All-industry employer-business ownership aging and five-year sell-or-transfer intentions used as the succession-flow proxy.
- **S5** — [General Dynamics Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm) (accessed 2026-07-22): Combat Systems program and backlog evidence, international wheeled and tracked vehicle awards, next-generation Abrams awards, long-term vehicle franchises, and company-wide U.S. government contract-type mix.
- **S6** — [Army FY 2026 President's Budget Highlights](https://www.asafm.army.mil/Portals/72/Documents/BudgetMaterial/2026/pbr/FY26%20Presidents%20Budget%20Highlights.pdf) (accessed 2026-07-22): FY2026 Armored Multi-Purpose Vehicle procurement and requested Weapons and Tracked Combat Vehicles funding compared with the FY2025 continuing-resolution level.
- **S7** — [Army Modernization: Actions Needed to Support Fielding New Equipment](https://www.gao.gov/products/gao-24-107566) (accessed 2026-07-22): Army modernization investment, fielding cadence, Stryker-mounted modernization, and implementation risks around facilities, personnel, training, and transferred vehicles.
- **S8** — [FAR 42.1204 Applicability of Novation Agreements](https://www.acquisition.gov/far/42.1204) (accessed 2026-07-22): Government-contract successor and novation requirements, distinction between asset and stock transactions, evidence of performance capability, and security-clearance documentation.
- **S9** — [DCSA Entity Vetting, Facility Clearances and Foreign Ownership, Control or Influence](https://www.dcsa.mil/Industrial-Security/Entity-Vetting-Facility-Clearances-FOCI/) (accessed 2026-07-22): Facility-clearance eligibility and FOCI oversight for entities handling classified government information.
