# 336110 — Automobile and Light Duty Motor Vehicle Manufacturing

*v5.1 Stage 1 research memo. Run `336110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Persistent physical demand for automobiles and light trucks, with potential episodic outsourcing around new programs or flexible capacity.
**Weakness:** No defensible LMM contract-manufacturer population or five-year transfer probability can be established from available evidence.

## Business-model lens
- Included: U.S. lower-middle-market firms, if any, providing repeat outsourced contract manufacturing of complete automobiles, light-duty motor vehicles, or chassis to external vehicle brands or program owners.
- Excluded: Large proprietary vehicle OEMs, captive assembly plants, non-control financing vehicles, motor-vehicle body builders using purchased chassis, motor-home manufacturers using purchased chassis, race-car manufacturers, component suppliers, dealers, and one-off prototype work without repeat production.
- Customer and revenue model: Multi-period B2B contract-manufacturing programs with tooling, qualification, launch, assembly, testing, and delivery obligations; revenue would derive from program units, engineering changes, and associated manufacturing support rather than retail vehicle branding.
- Deviation from default lens: Narrowed to outsourced contract vehicle or chassis manufacturing because the NAICS is dominated by proprietary OEM product manufacturing, while the fixed screen requires repeat outsourced service. Public evidence did not establish a defensible LMM target population within that subset.

## Executive view
The public evidence does not establish a viable LMM roll-up population inside 336110. Final-vehicle manufacturing is dominated by proprietary OEM and captive plants; the only coherent service lens is repeat contract manufacturing, for which both firm availability and transfer probability remain missing.

## How AI changes the work
AI can improve engineering-change review, planning, quality records, maintenance knowledge, procurement, and administrative workflows, but the production workforce is dominated by physical assembly and factory operations.

## Value capture
Any contract manufacturer could benefit from fixed-price periods and faster launches, but powerful vehicle customers and open-book cost-down expectations would likely capture a large share of sustained productivity gains.

## Firm availability
The frozen firm-count input is explicitly missing, and the research did not identify a defensible denominator or eligible LMM numerator. Large OEM plants and corporate subsidiaries should not be treated as transferable small firms.

## Demand durability
Vehicle replacement demand supports total production, but recent U.S. assembly and sectoral-output data are soft and the transition between combustion, hybrid, and electric powertrains remains policy-sensitive. None of those indicators proves demand for outsourced LMM assembly.

## Risks and uncertainty
The decisive risks are nonexistence of a scalable target pool, extreme customer concentration, capital and tooling intensity, product liability, labor relations, model-cycle volatility, policy shifts, and OEM decisions to keep final assembly captive.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0817 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.13 | 0.21 | 0.31 | PROXY | S2, S3 |
| rho | 0.25 | 0.42 | 0.6 | ESTIMATE | S2, S3 |
| e | — | — | — | MISSING | — |
| s5 | — | — | — | MISSING | — |
| q | 0.25 | 0.45 | 0.65 | ESTIMATE | S1 |
| d5 | 0.85 | 1 | 1.17 | PROXY | S4, S5, S6 |
| o | 0.94 | 0.985 | 0.999 | ESTIMATE | S1, S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.11 | 0.29 | 0.61 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 5.00 | 9.00 | 10.00 | ESTIMATE |
| D | 7.99 | 9.85 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation data cover all motor vehicle manufacturing, not a verified LMM contract subset.
- a: ILO exposure is broad and measures technical potential rather than current unautomated work.
- a: The dataset labor ratio is measured at NAICS 3361 and may not describe a hypothetical small-firm lens.
- rho: No AI implementation study for the screened contract-manufacturing population was found.
- rho: Large-OEM implementation experience may not transfer to LMM firms.
- e: The NAICS definition identifies activities, not firm revenue models or size.
- e: No replacement for the frozen missing firm count was researched or estimated.
- s5: Large OEM transactions do not proxy LMM owner succession.
- s5: The absence of a defensible population makes economy-wide owner-age evidence uninformative here.
- q: No public contract sample for a verified U.S. LMM contract-vehicle-manufacturing population was found.
- q: Commercial terms may differ materially between complete-vehicle and chassis-only programs.
- d5: Industry output and assembly volumes measure all OEM production, not outsourced LMM programs.
- d5: Monthly assembly rates are cyclical and can be distorted by shutdowns and model changeovers.
- d5: EIA scenarios depend materially on policy assumptions.
- o: The estimate addresses elimination or self-service, not conventional robotics already embedded in production.
- o: OEM insourcing could eliminate outsourced demand even while vehicle demand remains.

## Sources
- **S1** — [2022 NAICS 336110: Automobile and Light Duty Motor Vehicle Manufacturing](https://www.census.gov/naics/?details=336110&input=336110&year=2022) (accessed 2026-07-23): Industry boundary covering complete automobiles, light-duty vehicles, and chassis, plus exclusions for purchased-chassis bodies, motor homes, and race cars.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-23): Motor vehicle manufacturing occupation counts, including assemblers, machine operators, industrial engineers, supervisors, and painting operators.
- **S3** — [Generative AI and Jobs: A global analysis of potential effects on job quantity and quality](https://www.ilo.org/sites/default/files/2024-08/GenAI%20and%20Jobs_Policy%20Brief_ILO.pdf) (accessed 2026-07-23): Task-level GenAI exposure by broad occupation and evidence that most nonclerical work remains human-involved.
- **S4** — [Sectoral Output for Manufacturing: Motor Vehicle Manufacturing (NAICS 3361)](https://fred.stlouisfed.org/series/IPUEN3361T300000000) (accessed 2026-07-23): BLS industry-productivity sectoral output for 2021-2025, including the decline from 2024 to 2025.
- **S5** — [Motor Vehicle Assemblies: Monthly, Not Seasonally Adjusted](https://fred.stlouisfed.org/release/tables?eid=50089&rid=13) (accessed 2026-07-23): Federal Reserve auto and light-truck assembly annual rates for May 2025 and May 2026.
- **S6** — [Annual Energy Outlook 2026 Narrative](https://www.eia.gov/outlooks/aeo/pdf/AEO_Narrative.pdf) (accessed 2026-07-23): Alternative light-duty vehicle sales and stock pathways demonstrating substantial powertrain and policy uncertainty.
