# 336419 — Other Guided Missile and Space Vehicle Parts and Auxiliary Equipment Manufacturing

*v5.1 Stage 1 research memo. Run `336419-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.82 · L 0.68 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Mission-critical qualified parts participate in expanding missile and space programs with strong switching barriers.
**Weakness:** The transferable acquisition pool is extremely small and exposed to single-program outcomes.

## Business-model lens
- Included: Independent LMM manufacturers and prototype-to-production suppliers of guided-missile and space-vehicle parts, subassemblies, and auxiliary equipment other than propulsion, sold repeatedly to external primes, government programs, and commercial-space customers.
- Excluded: Complete vehicles, propulsion units, unrelated aircraft parts, captive divisions, pure distributors, government facilities, shells, and firms outside the EBITDA band.
- Customer and revenue model: Recurring development, qualified production-lot, spares, and sustainment revenue with engineering, configuration control, parts assurance, inspection, traceability, and mission-support obligations.
- Deviation from default lens: none

## Executive view
Demand and labor intensity are strong, and qualified parts suppliers have high switching barriers. The obstacle is a seven-firm estimated universe constrained by security, customer approvals, and program concentration.

## How AI changes the work
AI can assist requirements and parts-data search, configuration and quality documentation, proposal work, planning, procurement, failure-mode retrieval, and test-data review. Precision manufacture, assembly, environmental test, inspection execution, and acceptance remain physical and accountable.

## Value capture
Qualification, traceability, mission criticality, scarce processes, and unique designs preserve savings. Government cost analysis, prime cost-downs, and contract learning curves share gains.

## Firm availability
Only seven estimated candidates exist before filtering for independence, clearances, funded recurring programs, quality approvals, customer diversity, and transferable ownership.

## Demand durability
Missile replenishment, missile defense, space architectures, and commercial missions support growth. Program cancellation, appropriations, prime insourcing, redesign, and qualification failures create severe target-level volatility.

## Risks and uncertainty
Security and export controls, cyber accreditation, mission failure, counterfeit components, supply-chain quality, customer concentration, contract novation, and the weak margin bridge dominate.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4876 | — | OBSERVED | — |
| n | — | 7 | — | ESTIMATE | — |
| a | 0.2 | 0.31 | 0.42 | PROXY | S1, S2, S3, S4 |
| rho | 0.25 | 0.43 | 0.6 | ESTIMATE | S3, S4 |
| e | 0.34 | 0.54 | 0.71 | ESTIMATE | S1, S3, S5 |
| s5 | 0.07 | 0.14 | 0.25 | PROXY | S6 |
| q | 0.62 | 0.79 | 0.91 | ESTIMATE | S3, S4, S5 |
| d5 | 1.07 | 1.3 | 1.58 | PROXY | S2, S5 |
| o | 0.97 | 0.995 | 1 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.98 | 2.60 | 4.92 | ESTIMATE |
| F | 0.25 | 0.68 | 1.30 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 10.00 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No public six-digit task study.
- a: Classified and proprietary activity is underobserved.
- rho: Bounded judgment rather than observed adoption.
- rho: Final acceptance and mission assurance remain human-accountable.
- e: Auto-parts margin bridge is weak for space and missile suppliers.
- e: Establishments may not correspond to transferable firms.
- s5: Economy-wide demographic proxy.
- s5: Tiny denominator causes large uncertainty.
- q: No public contract sample measures pass-through.
- q: Commercial fixed-price components differ from government development work.
- d5: Funding is not delivered quantity.
- d5: Demand is highly program-concentrated.
- o: Operator share can migrate to primes.
- o: This is separate from internal labor automation.

## Sources
- **S1** — [Other Guided Missile and Space Vehicle Parts Manufacturing](https://www2.census.gov/library/publications/economic-census/1997/manufacturing-reports/97m3364f.pdf) (accessed 2026-07-22): Census identifies 336419 as other guided-missile and space-vehicle parts and auxiliary equipment manufacturing.
- **S2** — [DoD Background Briefing on FY 2026 Defense Budget](https://www.defense.gov/News/Transcripts/Transcript/Article/4228828/background-briefing-on-fy-2026-defense-budget/) (accessed 2026-07-22): DoD states the budget prioritizes missile defense and munitions and provides $40 billion for Space Force, more than 30% above FY2025.
- **S3** — [NASA Electrical, Electronic, and Electromechanical Parts Assurance](https://sma.nasa.gov/sma-disciplines/eee-parts) (accessed 2026-07-22): NASA describes recommendations covering part performance, failure modes, tests, reliability, and supply-chain quality for spaceflight hardware.
- **S4** — [NASA Quality and Mission Assurance](https://sma.nasa.gov/sma-disciplines/quality) (accessed 2026-07-22): NASA describes risk-based quality programs covering manufactured items, personnel, test equipment, facilities, processes, components, parts, and materials.
- **S5** — [FY2026 Defense Production Act Purchases Budget Justification](https://comptroller.defense.gov/Portals/45/Documents/defbudget/FY2026/budget_justification/pdfs/02_Procurement/PROC_DPAP_PB_2026.pdf) (accessed 2026-07-22): DoD identifies industrial shortfalls and critical supply-chain end uses including missile guidance, antimissile defense, and space-based satellites.
- **S6** — [2024 Chartbook on Firms by Age of Primary Owner](https://www.fedsmallbusiness.org/-/media/project/smallbizcredittenant/fedsmallbusinesssite/fedsmallbusiness/files/2024/firms-in-focus/sbcs_chartbook2024_ownerage.pdf) (accessed 2026-07-22): Federal Reserve owner-age evidence used only as a broad succession proxy.
