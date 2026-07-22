# 333618 — Other Engine Equipment Manufacturing

*v5.1 Stage 1 research memo. Run `333618-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.08 · L 1.10 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Complex engineering, testing, calibration, and compliance workflows offer meaningful AI exposure around a durable installed base and backup-power applications.
**Weakness:** Electrification and integrated-OEM ownership may shrink both the addressable demand basket and the truly transferable LMM firm pool.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers of internal-combustion engines other than automotive gasoline and aircraft engines, including diesel, semidiesel, stationary, marine, nonroad, and other application engines supplied repeatedly to external OEM, distributor, fleet, power, and industrial customers.
- Excluded: Captive plants, non-control investment vehicles, automotive gasoline engines, aircraft engines, pure distributors, engine rebuilders without manufacturing, and equipment assemblers that purchase rather than manufacture the engine are excluded.
- Customer and revenue model: Repeat business-to-business engine and parts sales under OEM programs, dealer or distributor channels, fleet specifications, generator and equipment platforms, and replacement or service-parts relationships, generally priced by unit, configuration, or supply agreement.
- Deviation from default lens: none

## Executive view
Other engine manufacturing has a rich engineering, test, compliance, and production information layer, but much capacity belongs to large integrated OEMs and the current product basket faces electrification risk. AI can assist design, calibration, diagnostics, planning, quality, and documentation, while physical build, test, certification, warranty, and field support remain operator-required.

## How AI changes the work
The clearest uses are engineering search, simulation assistance, calibration analysis, requirements and compliance drafting, quote and supply planning, machine monitoring, inspection triage, predictive maintenance, and test-data analysis. Safety, durability, emissions certification, model traceability, and physical test requirements limit autonomous substitution.

## Value capture
Platform qualification, control integration, certification, installed base, dealer support, service parts, and durability history create switching costs. Powerful OEM and fleet customers demand productivity concessions, and a shift toward electric platforms can weaken an engine supplier's pricing leverage.

## Firm availability
The injected estimate of 73 LMM firms requires a strict bottom-up check because large-group plants, captive production, rebuilders, and equipment assemblers may contaminate the count. Specialty targets exist, but six-digit transfer frequency is unobserved and strategic buyer capacity may be narrow.

## Demand durability
Backup and remote power, construction, agricultural, marine, recreational, and industrial uses support continuing physical engine demand. Electrification, batteries, fuel cells, emissions compliance, and platform redesign create much more structural downside than in passive power-transmission components.

## Risks and uncertainty
Major gaps are firm eligibility, six-digit tasks, implementation, contract pass-through, and transactions. Certification, emissions regulation, product liability, warranty reserves, electronics and software investment, dealer obligations, customer concentration, tariffs, and technology substitution can dominate AI benefits.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1813 | — | OBSERVED | — |
| n | — | 73 | — | ESTIMATE | — |
| a | 0.2 | 0.33 | 0.46 | PROXY | S2, S3, S5 |
| rho | 0.25 | 0.46 | 0.65 | PROXY | S3, S5 |
| e | 0.3 | 0.5 | 0.69 | ESTIMATE | S1, S5 |
| s5 | 0.09 | 0.2 | 0.33 | ESTIMATE | — |
| q | 0.39 | 0.59 | 0.77 | ESTIMATE | — |
| d5 | 0.78 | 1 | 1.18 | PROXY | S4, S5, S6 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.36 | 1.10 | 2.17 | PROXY |
| F | 1.75 | 3.40 | 4.62 | ESTIMATE |
| C | 7.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.33 | 9.80 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source is four-digit and not specific to engine equipment.
- a: Regulatory complexity increases documentation exposure but also requires expert accountability that limits substitution.
- rho: No representative 333618 adoption or realized-savings dataset was found.
- rho: Large global engine OEMs may be more digitized than the LMM population, while small specialty firms may have cleaner but smaller datasets.
- e: The injected n of 73 is an ESTIMATE based on receipts and a machinery-sector margin rather than observed 333618 EBITDA.
- e: Firm and establishment boundaries are particularly problematic for diversified engine and equipment OEMs.
- s5: Neither the qualifying transfer numerator nor eligible denominator is observed.
- s5: A small number of specialty-engine transactions could materially alter the measured rate.
- q: No representative contract-level pass-through data were available.
- q: Retention likely differs between proprietary specialty engines and customer-controlled platform designs.
- d5: The BLS projection combines engines with turbines and power-transmission equipment.
- d5: EIA and EPA establish applications and constraints but do not measure the LMM industry's forward demand.
- o: This is bounded judgment rather than an observed share.
- o: Automation can reduce labor intensity without eliminating the accountable operating and certifying firm.

## Sources
- **S1** — [2022 NAICS Definition: 333618 Other Engine Equipment Manufacturing](https://www.census.gov/naics/?details=333&input=333&year=2022) (accessed 2026-07-22): Defines 333618 as manufacturing internal-combustion engines other than automotive gasoline and aircraft engines.
- **S2** — [May 2023 OEWS: Engine, Turbine, and Power Transmission Equipment Manufacturing](https://www.bls.gov/oes/2023/may/naics4_333600.htm) (accessed 2026-07-22): Reports 92,420 jobs and occupation shares including production 47.86%, engineering 17.03%, management 7.84%, business and financial operations 6.23%, and computer and mathematical 2.38%.
- **S3** — [NIST Augmented Intelligence for Manufacturing Systems](https://www.nist.gov/programs-projects/augmented-intelligence-manufacturing-systems-aims) (accessed 2026-07-22): Describes integrated metrology, physics models, and AI for machine monitoring, diagnostics, prognostics, quality, and yield, targeting roughly 500,000 U.S. machine tools.
- **S4** — [BLS Employment and Output by Industry Projections](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects four-digit 333600 output from 38.0 to 43.1 over the projection decade, a 1.3% annual increase, while employment declines from 92.8 thousand to 88.4 thousand.
- **S5** — [EPA Regulations for Emissions from Nonroad Vehicles and Engines](https://www.epa.gov/regulations-emissions-vehicles-and-engines/regulations-emissions-nonroad-vehicles-and-engines) (accessed 2026-07-22): Documents diverse engine applications and separate standards for heavy-equipment compression- and spark-ignition engines, marine engines, recreational vehicles, and small equipment.
- **S6** — [EIA: How Electricity Is Generated](https://www.eia.gov/energyexplained/electricity/how-electricity-is-generated.php) (accessed 2026-07-22): Documents internal-combustion engines in mobile construction-site power and emergency or backup generation, with diesel generators capable of using several fuels.
