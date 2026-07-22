# 331512 — Steel Investment Foundries

*v5.1 Stage 1 research memo. Run `331512-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.97 · L 0.73 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Long-lived, qualification-heavy aerospace and industrial part programs create durable outsourced relationships and pricing differentiation.
**Weakness:** The physical one-use mold process dominates labor, while customer concentration and program approvals can make otherwise attractive firms fragile.

## Business-model lens
- Included: Independent US steel investment foundries that repeatedly produce detailed lost-wax steel castings to external aerospace, defense, turbine, industrial, medical, automotive, fluid-handling, or other customer specifications and have transferable operations in the target band.
- Excluded: Captive OEM foundries, non-steel investment casters, conventional steel or iron foundries, finished-product manufacturers classified by their final product, project shells, and non-control interests.
- Customer and revenue model: Revenue is earned through tooling, qualification, casting, heat-treatment, finishing, inspection, and sometimes machining charges under repeat part programs and purchase orders, commonly with alloy and energy surcharges.
- Deviation from default lens: The code includes externally contracted and captive casting operations. The lens retains independent repeat casting programs because captive production is not an outsourced service.

## Executive view
Steel investment foundries fit repeat outsourced manufacturing better than many primary-metal industries because customer-specific tooling and qualifications sustain long programs. AI opportunity is concentrated in engineering, quality, planning, maintenance, and administration, while a laborious one-use wax-and-shell process remains physical.

## How AI changes the work
AI can accelerate drawing and RFQ review, manufacturability analysis, process plans, tooling knowledge, schedules, defect investigations, maintenance retrieval, certificates, and customer communication. Wax patterns, tree assembly, shell dipping, dewaxing, firing, pouring, finishing, and inspection remain operator-intensive.

## Value capture
Qualification and switching costs support retention, particularly for complex, sole-source, or capacity-constrained parts. Annual productivity clauses and dual-sourcing share savings with sophisticated aerospace and industrial buyers.

## Firm availability
Independent program foundries often fit the lens, but captive assets, customer concentration, export controls, certification, permits, capital backlog, and key-person technical knowledge narrow transferability.

## Demand durability
Aerospace and turbine growth support a favorable base relative to aggregate foundries, with defense, medical, fluid-handling, and industrial uses diversifying demand. Program delays and alternate manufacturing technologies widen the range.

## Risks and uncertainty
Risks include platform concentration, qualification loss, export-control and cybersecurity obligations, shell and casting yield, energy and alloy costs, air emissions, capital needs, additive-manufacturing substitution, and four-digit occupation proxies.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2163 | — | OBSERVED | — |
| n | — | 55 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S1, S2, S3 |
| rho | 0.26 | 0.47 | 0.66 | ESTIMATE | S2, S3 |
| e | 0.33 | 0.55 | 0.74 | ESTIMATE | S2, S4 |
| s5 | 0.1 | 0.2 | 0.31 | PROXY | S5 |
| q | 0.34 | 0.57 | 0.77 | ESTIMATE | S2, S4 |
| d5 | 0.9 | 1.08 | 1.29 | PROXY | S4, S6, S7 |
| o | 0.93 | 0.98 | 1 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.22 | 0.73 | 1.60 | ESTIMATE |
| F | 1.66 | 3.14 | 4.20 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 8.37 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Four-digit occupation data include much less engineering-intensive casting methods.
- a: Existing simulation, robotic dipping, automated inspection, and digital quality systems are not separately observed.
- rho: No six-digit longitudinal AI adoption study was located.
- rho: High-specification plants may have larger document opportunity but slower validation and change control.
- e: Public data do not quantify captive versus independent foundries.
- e: Aerospace-program revenue can be recurring yet highly concentrated and vulnerable to platform changes.
- s5: Cross-industry intentions are not completed deal probabilities.
- s5: Strategic asset acquisitions and internal reorganizations may not qualify as standalone LMM transfers.
- q: No source directly measures AI-productivity pass-through.
- q: Certification, alloy, energy, and yield costs can mask retained labor benefit.
- d5: Aerospace evidence includes many parts and materials outside steel investment castings.
- d5: Long qualification cycles can delay demand and make individual programs lumpy.
- o: This measures need for an accountable operator, not the number of workers.
- o: Physical-process substitution affects d5 and o at the margin, not pure software self-service.

## Sources
- **S1** — [Foundries - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_331500.htm) (accessed 2026-07-22): Aggregate foundry occupation mix: 66.92% production and 7.33% installation, maintenance, and repair.
- **S2** — [NAICS Definition: Steel Investment Foundries](https://www2.census.gov/library/reference/naics/technical-documentation/definition-files/2012_definition_file.pdf) (accessed 2026-07-22): Official scope and method: steel investment castings use wax shapes coated in refractory slurry, creating seamless molds and highly detailed, consistent castings.
- **S3** — [Economic Impact Analysis of Final Iron and Steel Foundries NESHAP](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1006JPE.TXT) (accessed 2026-07-22): Investment-casting process detail: repeated ceramic coating, pattern burnout, and mold heating to about 1,800°F before casting.
- **S4** — [Advanced Manufacturing Office Update: Investment Casting Projects](https://www.energy.gov/cmei/amo/articles/advanced-manufacturing-office-update-july-2014) (accessed 2026-07-22): Examples of complete-to-print complex investment castings and finished subassemblies supplied to automotive and aerospace customers.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry succession proxy: 52.3% of employer businesses have owners age 55 or older and 22% planned a five-year sale or transfer.
- **S6** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects aerospace products and parts real output up 2.0% annually over 2024-34, while aggregate foundry output declines 0.8% annually.
- **S7** — [FAA Aerospace Forecast Fiscal Years 2026-2046](https://www.faa.gov/data_research/aviation/aerospace_forecasts/2026_FAA_Aerospace_Forecasts_FY2026-2046-2.pdf) (accessed 2026-07-22): FAA forecasts the US commercial aircraft fleet increasing from 6,949 aircraft in 2025 to 10,677 in 2046.
