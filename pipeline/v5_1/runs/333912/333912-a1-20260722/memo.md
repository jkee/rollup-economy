# 333912 — Air and Gas Compressor Manufacturing

*v5.1 Stage 1 research memo. Run `333912-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.37 · L 1.54 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A durable installed base and expensive customer energy use support repeat equipment, parts, and upgrade demand plus rich AI-assisted application and service workflows.
**Weakness:** Segment-specific evidence on firm eligibility, implementation, transfers, and price retention is thin, while standard equipment remains competitively procured.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers of general-purpose reciprocating and centrifugal air or gas compressors, non-laboratory vacuum pumps, and nonagricultural spraying and dusting compressor or spray-gun units that repeatedly supply external industrial, commercial, distributor, OEM, and aftermarket customers.
- Excluded: Captive plants, non-control investment vehicles, refrigeration and air-conditioning compressors, motor-vehicle compressors, fluid-power pumps and motors, agricultural spraying equipment, laboratory vacuum pumps, pure distributors, and service-only businesses without manufacturing are excluded.
- Customer and revenue model: Repeat business-to-business equipment, configured-system, replacement, spare-parts, and aftermarket sales through direct, OEM, distributor, and service channels, commonly priced by unit, configuration, project, or supply agreement.
- Deviation from default lens: none

## Executive view
Air and gas compressor manufacturing combines a broad industrial installed base and aftermarket economics with information-heavy application, configuration, controls, and service workflows. AI can assist quoting, engineering, scheduling, test analysis, quality, maintenance, parts, and customer support, while pressure equipment remains physically manufactured, tested, warranted, and operator-required.

## How AI changes the work
The clearest uses are application sizing, configuration, drawing and specification review, quote generation, production planning, machine monitoring, inspection triage, test-data analysis, connected-fleet diagnostics, parts identification, and technical support. Safety, performance guarantees, varied field conditions, legacy equipment, and long product lives require expert validation.

## Value capture
Installed-base compatibility, reliability, energy performance, controls, distribution, spare parts, and response time support retention. Standard equipment and OEM or project procurement remain price competitive, so customers recapture part of savings through bids and negotiations.

## Firm availability
The injected LMM estimate of 57 firms suggests a plausible target pool, but diversified ownership, distributor or service miscoding, recurring revenue, and actual EBITDA require a bottom-up audit. Six-digit transfer evidence is absent.

## Demand durability
Compressed air and vacuum serve broad industrial processes, and high electricity cost creates replacement, efficiency, controls, and monitoring demand. Broader machinery output projections are modestly positive, while industrial capex, oil and gas, imports, and customer consolidation produce cyclicality.

## Risks and uncertainty
Major gaps are six-digit occupations, firm eligibility, actual implementation, contractual pass-through, and deal flow. Pressure and product liability, warranty, distributor dependence, customer concentration, castings and motors, electronics, cyclicality, tariffs, and working capital can dominate AI savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2521 | — | OBSERVED | — |
| n | — | 57 | — | ESTIMATE | — |
| a | 0.18 | 0.3 | 0.43 | PROXY | S2, S3, S5 |
| rho | 0.3 | 0.51 | 0.7 | PROXY | S3 |
| e | 0.48 | 0.68 | 0.82 | ESTIMATE | S1 |
| s5 | 0.14 | 0.27 | 0.4 | ESTIMATE | — |
| q | 0.41 | 0.62 | 0.8 | ESTIMATE | — |
| d5 | 0.92 | 1.06 | 1.21 | PROXY | S4, S5 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.54 | 1.54 | 3.04 | PROXY |
| F | 2.53 | 3.92 | 4.79 | ESTIMATE |
| C | 8.20 | 10.00 | 10.00 | ESTIMATE |
| D | 8.65 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational evidence combines several machinery industries and is not six-digit-specific.
- a: DOE's energy evidence concerns compressor use at customer plants, not manufacturer labor exposure.
- rho: No representative 333912 adoption or realized-savings dataset was found.
- rho: Firms with connected installed fleets may implement faster than build-to-print or basic equipment manufacturers.
- e: The injected n of 57 is an ESTIMATE based on receipts and a machinery-sector margin rather than observed 333912 EBITDA.
- e: Firm and establishment boundaries can hide compressor plants inside diversified machinery groups.
- s5: Neither qualifying transfers nor the eligible firm denominator is directly observed.
- s5: Installed-base aftermarket businesses and project-oriented compressor OEMs likely have different buyer pools.
- q: No representative contract-level pass-through evidence was available.
- q: Retention should be higher in proprietary configured systems and aftermarket parts than in standardized compressors sold through competitive bids.
- d5: The BLS projection combines several machinery industries and does not isolate compressors.
- d5: DOE's compressed-air figures are old and indicate customer energy importance rather than current equipment volume growth.
- o: This is bounded judgment rather than a measured operator-required share.
- o: Remote monitoring and controls may reduce service labor while leaving the accountable equipment manufacturer required.

## Sources
- **S1** — [NAICS Definition: 333912 Air and Gas Compressor Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines 333912 as general-purpose reciprocating and centrifugal compressors, non-laboratory vacuum pumps, and nonagricultural spraying and dusting compressors or spray-gun units.
- **S2** — [May 2023 OEWS: Machinery Manufacturing Including NAICS 3339](https://www.bls.gov/oes/2023/may/naics4_3330A1.htm) (accessed 2026-07-22): Reports 777,330 jobs and shares including production 48.45%, engineering 10.14%, office support 8.48%, management 7.51%, business and financial operations 5.96%, sales 3.67%, and computer and mathematical 2.10%.
- **S3** — [NIST Augmented Intelligence for Manufacturing Systems](https://www.nist.gov/programs-projects/augmented-intelligence-manufacturing-systems-aims) (accessed 2026-07-22): Describes integrated metrology, physics models, and AI for real-time machine health and process prediction, with deployment to industrial partners and a goal covering roughly 500,000 U.S. machine tools.
- **S4** — [BLS Employment and Output by Industry Projections](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects the 3330A1 machinery composite's real output from 241.2 to 266.8 over the projection decade, a 1.0% annual increase.
- **S5** — [DOE Determine the Cost of Compressed Air for Your Plant](https://www.energy.gov/sites/default/files/2014/05/f16/compressed_air1.pdf) (accessed 2026-07-22): Reports that most industrial facilities need compressed air, with generation using about 10% of electricity at a typical facility and 30% or more at some facilities.
