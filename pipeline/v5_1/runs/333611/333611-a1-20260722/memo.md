# 333611 — Turbine and Turbine Generator Set Units Manufacturing

*v5.1 Stage 1 research memo. Run `333611-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.14 · L 1.51 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Growing power demand and proprietary installed-base service create durable, operator-required work.
**Weakness:** The true transferable LMM population is uncertain in a capital-intensive industry dominated by large OEMs.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly supplying complete nonaircraft steam, hydraulic, gas, and wind turbines or turbine-generator set units, together with manufacturer-provided parts, upgrades, technical support, and service, to external power, industrial, and infrastructure customers.
- Excluded: Captive internal units, shells, aircraft turbines, stand-alone generators, wind-blade or tower manufacturers, turbine-component job shops, and independent repair providers classified outside NAICS 333611.
- Customer and revenue model: Long-cycle engineered equipment and generator-set projects supplemented by installed-base replacement parts, planned outages, controls upgrades, long-term service agreements, and technical support; sales are negotiated directly or through major project channels.
- Deviation from default lens: none

## Executive view
Turbine manufacturing is engineering- and service-rich, with unusually strong physical, certification, and installed-base requirements. AI can assist proposals, engineering, quality, diagnostics, and service knowledge, but accountable fabrication, testing, commissioning, and safety sign-off remain. Demand is strong, yet the true independent LMM population is uncertain and likely smaller than the provided estimate.

## How AI changes the work
AI can help configure proposals, search engineering history, draft documentation and code, schedule complex projects, interpret inspection data, predict failures, and triage service. Machining, welding, winding, assembly, balancing, testing, installation, and outage work remain physical. Certification, deterministic controls, cyber review, and product liability limit autonomous action.

## Value capture
Certified designs, installed-base parts, proprietary controls, availability history, outage response, and failure cost create substantial switching friction. Sophisticated utilities and industrial customers still negotiate guarantees, penalties, and long-term pricing, sharing savings and transferring risk to suppliers.

## Firm availability
The count of 38 estimated in-band firms needs unusually careful resolution to ultimate ownership and complete-unit activity. Large-company establishments, component suppliers, and service firms can look like small turbine businesses in statistical data. Eligible niche OEMs may be valuable but technically and financially demanding transfers.

## Demand durability
Electricity demand is growing after a long plateau, gas-turbine backlogs are strong, and installed equipment requires service and repowering. Wind orders have weakened at the cited large OEM, and each technology depends on policy, permitting, interconnection, fuel economics, and long project cycles.

## Risks and uncertainty
Risks include a possibly overstated LMM firm count, OEM and customer concentration, qualification, export and cybersecurity controls, warranty tails, performance penalties, working capital, long lead components, policy shifts, field safety, and key engineers. Large-OEM evidence may not transfer to niche firms.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2173 | — | OBSERVED | — |
| n | — | 38 | — | ESTIMATE | — |
| a | 0.23 | 0.34 | 0.46 | PROXY | S2, S3 |
| rho | 0.32 | 0.51 | 0.68 | PROXY | S3, S4 |
| e | 0.42 | 0.64 | 0.82 | ESTIMATE | S1, S4 |
| s5 | 0.13 | 0.23 | 0.36 | PROXY | S6 |
| q | 0.43 | 0.63 | 0.79 | ESTIMATE | S4 |
| d5 | 1.03 | 1.2 | 1.4 | PROXY | S4, S5 |
| o | 0.96 | 0.99 | 0.999 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.64 | 1.51 | 2.72 | PROXY |
| F | 1.81 | 3.03 | 4.03 | ESTIMATE |
| C | 8.60 | 10.00 | 10.00 | ESTIMATE |
| D | 9.89 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS data cover NAICS 333600 rather than six-digit 333611.
- a: Large-OEM engineering and service mixes may not represent niche LMM builders.
- a: Equipment-efficiency gains are not labor substitution unless they remove manufacturer hours or avoid hiring.
- rho: GE Vernova is a very large OEM and not representative of LMM implementation resources.
- rho: AI can assist safety-critical engineering but cannot replace required accountable sign-off.
- e: The provided firm count is margin-bridged and especially vulnerable to establishment-versus-firm and product-classification error in an industry dominated by large OEM groups.
- e: Component and service companies are outside this exact industry lens even if economically adjacent.
- s5: No six-digit qualifying-transfer denominator was found.
- s5: Family-business succession evidence may be less representative here than in ordinary industrial manufacturing.
- q: GE Vernova's large service backlog demonstrates the model but not LMM retention rates.
- q: Capture should be higher in proprietary installed-base parts and urgent support than in competitively tendered equipment.
- d5: EIA electricity and capacity growth do not translate one-for-one to domestic turbine manufacturing.
- d5: GE Vernova is a dominant large OEM whose backlog may not be addressable by LMM firms.
- d5: Wind and gas order trends diverge, while steam and hydro are project-specific.
- o: The operator may be a large global OEM rather than an LMM supplier.
- o: Technology substitution can remove turbine units even as total electricity demand rises.

## Sources
- **S1** — [Census 2022 NAICS definition: 333611 Turbine and Turbine Generator Set Units Manufacturing](https://www.census.gov/naics/?details=33361&input=33361&year=2022) (accessed 2026-07-22): Defines nonaircraft turbine manufacturing and complete steam, hydraulic, gas, and wind turbine-generator set units.
- **S2** — [BLS May 2023 occupation estimates for Engine, Turbine, and Power Transmission Equipment Manufacturing](https://www.bls.gov/oes/2023/may/naics4_333600.htm) (accessed 2026-07-22): Reports 44,230 production workers at 47.86% of broader NAICS 333600 employment and 17,510 assemblers and fabricators at 18.94%.
- **S3** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Reports 46% manufacturing AI-tool use and more than 80% expecting increased use in two years, with operational use cases and implementation barriers.
- **S4** — [GE Vernova 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1996810/000199681026000015/gev-20251231.htm) (accessed 2026-07-22): Reports $94.387 billion of Power equipment and service RPO, up 29% from 2024, largely from gas-turbine equipment and contractual service, and reports wind-turbine orders of 854 units in 2025 versus 1,212 in 2024.
- **S5** — [EIA Annual Energy Outlook 2026 release](https://www.eia.gov/pressroom/releases/press587.php) (accessed 2026-07-22): Reports projected US electricity-demand growth averaging 0.9%-1.6% annually through 2050 across cases and installed generating-capacity increases of 50%-90%, with natural gas, solar, and wind supplying most growth.
- **S6** — [Deloitte Private survey: generational disparities in family-business succession planning](https://www2.deloitte.com/us/en/pages/about-deloitte/articles/press-releases/deloitte-private-survey-generational-disparatires-emerge-insuccession-planning-and-priorities-shaping-family-businesses.html) (accessed 2026-07-22): Describes a January 2024 survey of 500 US family-enterprise respondents and reports that 24% of current-generation respondents strongly agreed their succession plan would withstand departure of an important family employee.
