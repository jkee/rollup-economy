# 336414 — Guided Missile and Space Vehicle Manufacturing

*v5.1 Stage 1 research memo. Run `336414-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.96 · L 0.25 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Defense replenishment and expanding space architectures support strong physical demand and high-value engineering workflows.
**Weakness:** The eligible LMM acquisition universe is effectively tiny and heavily constrained by national-security requirements.

## Business-model lens
- Included: Independent LMM manufacturers and prototype-to-production developers of complete guided missiles or space vehicles that repeatedly supply external government, prime-contractor, or commercial-space customers.
- Excluded: Parts, propulsion units, and auxiliary equipment classified elsewhere; captive divisions, government arsenals, shells, non-control financing vehicles, and firms outside the EBITDA band.
- Customer and revenue model: Long-cycle government and prime contracts plus commercial-space programs, with recurring development, production lots, testing, configuration, compliance, and sustainment work.
- Deviation from default lens: none

## Executive view
Demand is strong and labor intensity is exceptional, but the screened acquisition population is nearly absent. AI can assist engineering and program information flows only inside tightly controlled security and mission-assurance boundaries.

## How AI changes the work
Applicable uses include requirements traceability, document search and drafting, proposal support, schedule and supply analysis, simulation assistance, test-data review, and configuration checks. Classified judgment, energetic integration, physical assembly, qualification test, inspection, and mission assurance remain accountable human work.

## Value capture
Mission criticality, security barriers, unique designs, and long programs support retention. Government cost analysis, cost-type contracts, negotiated fees, and prime cost-downs share benefits.

## Firm availability
The injected four-firm estimate is unusually fragile. Independent LMM complete-vehicle manufacturers with recurring production, clearances, facilities, funded backlog, and transferable control are likely rare.

## Demand durability
Missile replenishment, missile defense, proliferated space architectures, and commercial launch expansion support growth. Appropriation timing, program failure, cancellations, and prime concentration create extreme target-level volatility.

## Risks and uncertainty
Security, export controls, cyber accreditation, mission failure, government consent, contract novation, facility clearances, classified diligence, program concentration, and the weak margin bridge dominate.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6878 | — | OBSERVED | — |
| n | — | 4 | — | ESTIMATE | — |
| a | 0.21 | 0.32 | 0.43 | PROXY | S1, S2, S3 |
| rho | 0.23 | 0.41 | 0.58 | ESTIMATE | S3, S4 |
| e | 0.2 | 0.38 | 0.58 | ESTIMATE | S1, S4 |
| s5 | 0.05 | 0.11 | 0.21 | PROXY | S6 |
| q | 0.62 | 0.78 | 0.9 | ESTIMATE | S3, S4 |
| d5 | 1.05 | 1.25 | 1.5 | PROXY | S3, S4, S5 |
| o | 0.97 | 0.995 | 1 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.33 | 3.61 | 6.86 | ESTIMATE |
| F | 0.06 | 0.25 | 0.64 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 10.00 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No public six-digit wage-weighted task study.
- a: Classified work is largely invisible in public evidence.
- rho: Bounded judgment rather than observed adoption.
- rho: Autonomous safety-critical design or control is excluded.
- e: Injected count is margin-bridged from auto parts and especially uncertain for this project-based industry.
- e: Establishment classification may not correspond to a transferable firm.
- s5: Economy-wide demographic proxy is weak.
- s5: Tiny denominator makes probabilities unstable.
- q: No public contract sample quantifies automation pass-through.
- q: Fixed-price commercial-space programs differ from cost-type defense development.
- d5: Budget authority is not delivered quantity.
- d5: Demand is program-concentrated and politically sensitive.
- o: Operator share may migrate to large primes.
- o: This is distinct from internal labor automation.

## Sources
- **S1** — [2022 NAICS Definition: Guided Missile and Space Vehicle Manufacturing](https://www.census.gov/naics/?chart=2022&details=324&input=31) (accessed 2026-07-22): Census defines 336414 as manufacturing or prototyping complete guided missiles and space vehicles.
- **S2** — [Aerospace Product and Parts Manufacturing OEWS](https://www.bls.gov/oes/2023/may/naics4_336400.htm) (accessed 2026-07-22): BLS reports aircraft structural, surface, rigging, and systems assemblers at 5.00% of broader aerospace employment, supporting the physical-work proxy.
- **S3** — [DoD Background Briefing on FY 2026 Defense Budget](https://www.defense.gov/News/Transcripts/Transcript/Article/4228828/background-briefing-on-fy-2026-defense-budget/) (accessed 2026-07-22): DoD states FY2026 priorities include missile defense, munitions, and the defense industrial base.
- **S4** — [FY2026 Defense Budget: Funding for Selected Weapon Systems](https://www.congress.gov/crs-product/R48860) (accessed 2026-07-22): CRS reports the FY2026 request included $40.2 billion for missile defeat and defense procurement and RDT&E.
- **S5** — [FAA Aerospace Forecast FY 2026-2046](https://www.faa.gov/data_research/aviation/aerospace_forecasts/FY_2026-2046_Full_Forecast_Document_Tables.pdf) (accessed 2026-07-22): FAA describes a new era of commercial space transportation and launch-cadence expansion, used as a space-demand proxy.
- **S6** — [2024 Chartbook on Firms by Age of Primary Owner](https://www.fedsmallbusiness.org/-/media/project/smallbizcredittenant/fedsmallbusinesssite/fedsmallbusiness/files/2024/firms-in-focus/sbcs_chartbook2024_ownerage.pdf) (accessed 2026-07-22): Federal Reserve owner-age evidence used only as a broad succession proxy.
