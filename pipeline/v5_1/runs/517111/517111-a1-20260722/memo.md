# 517111 — Wired Telecommunications Carriers

*v5.1 Stage 1 research memo. Run `517111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** The principal driver is recurring connectivity demand combined with AI-exposed customer, billing, provisioning, and network-assurance workflows.
**Weakness:** The principal weakness is capital-heavy technology migration under strong price and substitution pressure, compounded by no defensible LMM firm-count anchor.

## Business-model lens
- Included: U.S. lower-middle-market facilities-based wired carriers that repeatedly provide fiber, cable, copper, or mixed-network broadband, voice, video distribution, dedicated internet access, private network, optical transport, wavelength, and wholesale connectivity services to residential, business, carrier, or public-sector customers.
- Excluded: Telecommunications resellers without operated wired facilities, wireless carriers, satellite carriers other than the direct-to-home distribution exception included by NAICS, tower-only landlords, construction-only contractors, equipment manufacturers, captive networks, shells, non-control financing vehicles, and firms outside the target normalized-EBITDA band.
- Customer and revenue model: Customers generally pay recurring monthly subscription, per-connection, per-location, capacity, or metered bandwidth charges, with additional installation, equipment, usage, support, and wholesale fees. Residential contracts are often cancelable, while enterprise and carrier arrangements may have terms, minimums, service levels, and renewal repricing.
- Deviation from default lens: none

## Executive view
Wired carriers have recurring connectivity revenue and a meaningful AI-exposed layer in customer care, billing, provisioning, assurance, and network analysis, while physical fiber, cable, repairs, and accountability remain operator-intensive. Fiber and enterprise data demand are durable, but legacy decline, fixed-wireless competition, capital intensity, pricing pressure, and a missing LMM firm-count anchor limit confidence in firm availability.

## How AI changes the work
AI can automate or assist contact handling, ticket triage, billing review, fraud detection, outage communications, network anomaly detection, capacity planning, configuration support, documentation, sales proposals, and technician diagnostics. People still build and splice networks, enter premises, replace equipment, restore outages, negotiate access and accounts, approve production changes, and own safety, security, and service consequences.

## Value capture
Monthly and per-connection pricing can preserve some labor benefit, especially between renewals. Competitive promotions, falling bandwidth unit prices, speed upgrades, service credits, wholesale repricing, vendor costs, and reinvestment in capacity and reliability share or consume the remainder.

## Firm availability
The activity definition fits recurring outsourced service, but the actual lower-middle-market population is unknown because n is missing. Candidates require transferable facilities and franchises, sustainable maintenance capital, diversified customers, modern technology, limited subsidy restrictions, and economics that remain inside the target band after normalizing network reinvestment.

## Demand durability
Broadband, fiber, enterprise transport, cloud connectivity, and data-center interconnection remain durable. Copper voice, DSL, and legacy video contract, while fiber overbuilds, fixed wireless, satellite, and wholesale alternatives redistribute demand among operators and technologies.

## Risks and uncertainty
Key risks are missing firm-count evidence, capital intensity, overbuild, fixed-wireless and satellite substitution, copper and video decline, pricing compression, concentration, pole and right-of-way access, subsidy and franchise obligations, cyberattack, prolonged outage, vendor lock-in, service credits, obsolete plant, union and workforce constraints, and acquisition integration.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1138 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.24 | 0.38 | 0.52 | ESTIMATE | S1, S2, S3, S6 |
| rho | 0.52 | 0.7 | 0.84 | PROXY | S3 |
| e | 0.43 | 0.66 | 0.84 | ESTIMATE | S1, S4, S6 |
| s5 | 0.08 | 0.18 | 0.3 | PROXY | S4, S5, S6 |
| q | 0.27 | 0.44 | 0.61 | ESTIMATE | S4, S6, S7 |
| d5 | 0.91 | 1.03 | 1.16 | PROXY | S4, S5, S6, S7 |
| o | 0.77 | 0.9 | 0.97 | ESTIMATE | S1, S2, S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.57 | 1.21 | 1.99 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 5.40 | 8.80 | 10.00 | ESTIMATE |
| D | 7.01 | 9.27 | 10.00 | ESTIMATE |

## Caveats
- a: BLS covers technicians across wired and wireless telecommunications and contractors, not the full 517111 occupation mix.
- a: GSMA tracks global operators and publicly announced deployments rather than wage-weighted U.S. lower-middle-market tasks.
- a: The frozen compensation ratio is an ancestor-code estimate for all 517 and may misstate 517111 labor intensity.
- rho: Publicly announced deployments may overrepresent successful projects and large operators.
- rho: GSMA reports deployment counts and maturity, not the share of exposed labor opportunity realized within five years.
- rho: Small carriers may buy proven vendor features faster than large carriers but have less integration staff and weaker data.
- e: The official activity definition does not identify normalized EBITDA or transferable ownership.
- e: The dataset has no defensible n-band value, so the size and composition of the actual LMM population are unknown.
- e: Reported EBITDA can overstate transferable cash generation when network replacement, spectrum, pole, or expansion capital is treated separately.
- s5: Fiber-industry expectations and one acquisitive public company do not measure an eligible-firm transfer probability.
- s5: Network asset purchases and subscriber transfers may not qualify as company control transfers.
- s5: The missing LMM denominator prevents direct conversion of observed deals into a probability.
- q: Cogent's enterprise and carrier-focused mix is not representative of every residential or regional wired carrier.
- q: A lower unit price can coexist with revenue growth as traffic, speed, and connection counts expand.
- q: The cited sources do not measure savings-sharing after AI implementation.
- d5: Fixed connection counts and fiber passings are not constant-quality service quantity for the entire wired-carrier basket.
- d5: Trade-association deployment projections may be optimistic and may count multiple fiber passings of the same home.
- d5: Fiber growth can accrue to large incumbents while LMM cable, copper, and video operators lose customers.
- o: Continued demand for connectivity does not guarantee continued demand for the current wired operator or technology.
- o: Wholesale and open-access models can separate physical network ownership from retail operator functions.
- o: Fixed wireless and satellite may substitute more quickly in some geographies than the base assumes.

## Sources
- **S1** — [2022 NAICS Definition: 517111 Wired Telecommunications Carriers](https://www.census.gov/naics/?details=517111&input=517111&year=2022) (accessed 2026-07-22): Official industry definition and lens; a, e, and o
- **S2** — [Telecommunications Technicians](https://www.bls.gov/ooh/installation-maintenance-and-repair/telecommunications-equipment-installers-and-repairers-except-line-installers.htm) (accessed 2026-07-22): Physical installation, repair, testing, records, customer, outage, and infrastructure duties and occupational outlook; a and o
- **S3** — [Telco AI: State of the Market, Q3 2025](https://prod-cms.gsmaintelligence.com/research-file-download?assetId=67646&reportId=67642) (accessed 2026-07-22): Telco AI use cases, deployment areas, maturity, objectives, and size differences; a and rho
- **S4** — [2024 Communications Marketplace Report](https://docs.fcc.gov/public/attachments/FCC-24-136A1.pdf) (accessed 2026-07-22): Fixed-market technologies, connections, competition, pricing, entry conditions, and merger context; e, s5, q, d5, and o
- **S5** — [Fiber Broadband Association Reports Historic Fiber Deployment Highs](https://fiberbroadband.org/2025/12/16/fiber-broadband-association-reports-historic-fiber-deployment-highs/) (accessed 2026-07-22): 2025 U.S. fiber passings, market reach, competitive expansion, and deployment direction; s5 and d5
- **S6** — [Cogent Communications Holdings, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1158324/000110465926017968/ccoi-20251231x10k.htm) (accessed 2026-07-22): Wired service scope, recurring billing, acquisitions, competitive pricing, network dependence, and demand; a, e, s5, q, and d5
- **S7** — [CTIA 2025 Annual Survey Highlights](https://api.ctia.org/wp-content/uploads/2025/09/2025-Annual-Survey-Highlights.pdf) (accessed 2026-07-22): Fixed-wireless subscriber growth, cable losses, wireless pricing, and substitution pressure; q, d5, and o
