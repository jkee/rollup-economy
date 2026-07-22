# 238220 — Plumbing, Heating, and Air-Conditioning Contractors

*v5.1 Stage 1 research memo. Run `238220-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.49 · L 1.62 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A durable installed base that needs physical service creates room to automate the high-volume coordination and administrative work surrounding scarce technicians.
**Weakness:** Most labor sits in physical, licensed field roles, while industry-specific evidence on realized AI labor avoidance and completed LMM control transfers is thin.

## Business-model lens
- Included: US lower-middle-market plumbing, HVAC, refrigeration, mechanical, piping, and related contractors that repeatedly install, maintain, repair, or replace building systems for external residential, commercial, institutional, industrial, general-contractor, or property-owner customers.
- Excluded: Shells, captive facilities teams, non-control financing vehicles, firms outside the roughly $1-10M normalized EBITDA band, and businesses whose activity is classified outside NAICS 238220 such as stand-alone duct cleaning or septic-system installation.
- Customer and revenue model: Revenue combines quoted or bid project work, time-and-material and emergency service calls, parts markups, and recurring preventive-maintenance or service agreements. Customers include property owners and managers, households, institutions, industrial and commercial operators, and general contractors.
- Deviation from default lens: none

## Executive view
This is a physically delivered, locally accountable trade with a substantial but bounded digital-work opportunity. The practical AI case is concentrated in the coordination layer around technicians—calls, dispatch, estimating, procurement, documentation, billing, and knowledge retrieval—rather than autonomous plumbing or HVAC work. Demand is supported by installed-system maintenance and replacement, but new-construction exposure, labor scarcity, fragmented systems, and owner dependence create material uncertainty.

## How AI changes the work
AI can handle call summaries and triage, draft estimates and proposals, schedule and route technicians, surface manuals and prior-job knowledge, classify invoices and parts, prepare customer updates, and turn field notes or images into compliant records. It can also assist diagnosis, but physical inspection, installation, repair, testing, and licensed sign-off remain human work. Real labor avoidance depends on workflow redesign and integration, not merely employee access to a chatbot.

## Value capture
Fixed-price repairs, installations, and service agreements preserve early productivity gains better than transparent hourly or cost-plus work. Over time, competitive bids and contract renewals will transfer part of the benefit to customers, while some savings may instead fund faster response, higher close rates, and administrative capacity. The five-year retained share is therefore meaningful but well below complete capture.

## Firm availability
The broad code contains many repeat-service and repeat-project businesses, and LMM scale usually implies a workforce and customer base beyond a sole operator. Construction succession surveys show substantial exit intent, but completed qualifying transfers will be fewer because plans are delayed, some firms close, and licensing, customer concentration, or owner-held relationships can impair transferability.

## Demand durability
Plumbing and climate-control systems require continuing maintenance, repair, retrofit, and replacement in existing buildings, and BLS projects modest industry employment growth. Efficiency and refrigerant changes can create retrofit work, while construction cycles can suppress installations. Software may avoid a minority of calls through triage and remote diagnosis, but most current service quantity still needs an accountable operator at the site.

## Risks and uncertainty
The main evidence gaps are task-level labor allocation, realized five-year implementation, the eligible share of LMM firms, and completed control-transfer rates specific to plumbing/HVAC. A downturn in construction, equipment simplification, aggressive price competition, weak field-service data, integration failure, technician resistance, rework or liability from erroneous outputs, customer concentration, and reliance on owner licenses could each erode the case.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3508 | — | ESTIMATE | — |
| n | — | 1152 | — | ESTIMATE | — |
| a | 0.17 | 0.24 | 0.33 | PROXY | S1, S2 |
| rho | 0.28 | 0.48 | 0.66 | PROXY | S3, S4 |
| e | 0.62 | 0.79 | 0.9 | ESTIMATE | S5, S6 |
| s5 | 0.14 | 0.21 | 0.3 | PROXY | S7, S8 |
| q | 0.36 | 0.57 | 0.75 | ESTIMATE | S5, S6 |
| d5 | 0.95 | 1.03 | 1.1 | PROXY | S6, S9, S10 |
| o | 0.9 | 0.96 | 0.99 | PROXY | S6, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.67 | 1.62 | 3.06 | ESTIMATE |
| F | 7.42 | 8.46 | 9.24 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 8.55 | 9.89 | 10.00 | PROXY |

## Caveats
- a: S1 is May 2023 employer-establishment data and excludes self-employed workers.
- a: The wage weighting is reconstructed from published occupational employment and mean wages, not supplied by an industry task survey.
- a: S2 reflects Claude usage and broad occupations, not plumbing/HVAC firms or all AI systems.
- rho: The adoption sources cover two-digit construction, not NAICS 238220 or the LMM band.
- rho: The Census question broadened in late 2025 from AI in production to AI in any business function, limiting trend comparability.
- rho: Using an AI tool is not the same as operational labor substitution or avoided hiring.
- e: No source quantifies the eligible share within the frozen EBITDA band.
- e: NAICS 238220 mixes plumbing, HVAC, refrigeration, sprinklers, process piping, new construction, retrofit, and repair business models.
- e: The injected firm count is an estimate and may include firms whose normalized EBITDA or transferability differs from the size-class bridge.
- s5: S7 is broader engineering and construction and reports plans rather than completed control transfers.
- s5: S8 covers all US employer businesses, not this industry or EBITDA band.
- s5: Internal family or employee transfers qualify only when control actually changes and the operation remains transferable.
- q: No source directly measures five-year pass-through of AI-enabled savings in this industry.
- q: Commercial construction bidding, residential service, emergency plumbing, and maintenance agreements have materially different pass-through dynamics.
- q: The estimate excludes demand-volume effects and implementation difficulty.
- d5: Employment is a proxy for constant-price, constant-quality service quantity and is affected by productivity and labor supply.
- d5: The occupational projections extend ten years and cover workers outside NAICS 238220.
- d5: Plumbing and HVAC demand, and new construction versus service demand, may diverge materially.
- o: The sources describe occupations, not a direct forecast of service quantity by delivery mode.
- o: Remote monitoring and equipment redesign could eliminate more low-complexity visits than the base assumes.
- o: State and locality licensing and code requirements vary.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 238220](https://www.bls.gov/oes/2023/may/naics5_238220.htm) (accessed 2026-07-22): Direct employer-establishment occupation mix and wages for NAICS 238220: 1,236,740 total jobs; 41.25% construction/extraction, 29.51% installation/maintenance/repair, 12.16% office/administrative support, 5.62% management, 4.29% business/financial operations, and 2.52% sales.
- **S2** — [Labor market impacts of AI: A new measure and early evidence](https://www.anthropic.com/research/labor-market-impacts) (accessed 2026-07-22): Task-based theoretical and observed LLM exposure methodology; 90% theoretical capability in office/administrative tasks, far lower realized coverage, and explicit limits for physical tasks.
- **S3** — [AI adoption in business grows steadily but unevenly](https://www.minneapolisfed.org/article/2026/ai-adoption-in-business-grows-steadily-but-unevenly) (accessed 2026-07-22): Census BTOS interpretation showing roughly 20% overall business use after the question broadened, less than 10% use in construction, lower adoption in small firms, predominantly supplemental task use, and limited near-term employment effects.
- **S4** — [Tracking Firm Use of AI in Real Time: A Snapshot from the Business Trends and Outlook Survey](https://www.census.gov/hfp/btos/downloads/CES-WP-24-16.pdf) (accessed 2026-07-22): Construction AI use of 1.4% current and 2.2% expected within six months in early 2024; evidence on experimentation, de-adoption, task replacement, training, workflow changes, and implementation barriers.
- **S5** — [2022 NAICS Definition: 238220 Plumbing, Heating, and Air-Conditioning Contractors](https://www.census.gov/naics/?chart=2022&details=23&input=23) (accessed 2026-07-22): Industry scope includes installing and servicing plumbing, heating, and air-conditioning equipment; parts and labor; and new work, additions, alterations, maintenance, and repairs.
- **S6** — [Heating, Air Conditioning, and Refrigeration Mechanics and Installers](https://www.bls.gov/ooh/installation-maintenance-and-repair/heating-air-conditioning-and-refrigeration-mechanics-and-installers.htm) (accessed 2026-07-22): HVAC physical duties, jobsite context, licensing/certification and refrigerant obligations, residential service contracts, 70% employment in NAICS 238220, and projected 8% employment growth from 2024 to 2034.
- **S7** — [FMI Releases 2024 Study on Ownership Transfer and Management Succession](https://fmicorp.com/about/news/fmi-releases-2024-study-on-ownership-transfer-and-management-succession) (accessed 2026-07-22): Nearly 300 engineering and construction leaders surveyed; 38% of owners plan to exit in three to five years, with reported employee and family transfer routes and widespread planning gaps.
- **S8** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 survey of 1,264 US business owners; 22% of employer-business owners planned to sell or transfer ownership within five years, versus 9% of nonemployers.
- **S9** — [Employment and output by industry, 2024-34](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Direct NAICS 238220 employment projection from 1.2983 million in 2024 to 1.3613 million in 2034, a 4.8% increase.
- **S10** — [Plumbers, Pipefitters, and Steamfitters](https://www.bls.gov/ooh/construction-and-extraction/plumbers-pipefitters-and-steamfitters.htm) (accessed 2026-07-22): Physical installation and repair duties, apprenticeship and licensing, emergency on-call work, projected 4% employment growth from 2024 to 2034, and demand from new construction and maintenance and repair of existing systems.
