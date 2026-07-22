# 325220 — Artificial and Synthetic Fibers and Filaments Manufacturing

*v5.1 Stage 1 research memo. Run `325220-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.13 · L 1.04 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat customer specifications create valuable AI-assisted quality, planning, maintenance, and documentation workflows around unavoidable physical production.
**Weakness:** Domestic fiber output is structurally weak and the true contract-manufacturing subset is not publicly measured.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly producing or texturizing artificial and synthetic fibers or filaments to external-customer specifications under contract, tolling, or dedicated-program arrangements.
- Excluded: Captive integrated fiber plants, standard-product commodity sellers without an outsourced production relationship, texturizers of purchased fiber classified in NAICS 313110, glass-fiber manufacturers, distributors, shells, and non-control vehicles.
- Customer and revenue model: Recurring industrial programs priced per pound, lot, or contracted capacity, with customer specifications for polymer, denier, color, finish, tow, staple, yarn, or filament performance and periodic raw-material or energy repricing.
- Deviation from default lens: The NAICS definition mixes broad product manufacturing with customer-specific production. The lens is narrowed to repeat contract, toll, and dedicated-program manufacturing so the screened firms share a coherent outsourced-service revenue model.

## Executive view
The relevant target is a narrow contract or dedicated-program subset inside a structurally pressured domestic fiber industry. AI can improve quality, specification, scheduling, maintenance, and compliance work, but physical production remains operator-required and much of the savings may be competed away in per-pound pricing.

## How AI changes the work
Near-term uses center on laboratory and batch-record review, defect triage, production scheduling, maintenance knowledge, specification comparison, procurement analysis, and regulatory documentation. Safety-critical line control and physical spinning, winding, texturizing, handling, and repairs remain human-and-equipment work.

## Value capture
Qualified specialty programs and repeatability requirements create switching friction. Retention is weakened by indexed inputs, contract renewals, customer cost-down demands, commodity benchmarks, and offshore alternatives.

## Firm availability
Public industry classification does not identify which firms actually perform recurring outsourced production. Broad owner aging creates possible succession supply, but corporate ownership, strategic consolidation, environmental diligence, and facility obsolescence reduce the share that becomes a clean qualifying transfer.

## Demand durability
Fiber is a physical input across consumer and industrial end uses, so software cannot self-serve it. Domestic real output at 71.8055 in June 2026 relative to 2017 equals 100 nevertheless signals substantial structural pressure, justifying a declining base case with a wide range.

## Risks and uncertainty
Key risks are low and unmeasured eligibility, declining domestic output, import competition, product-mix heterogeneity, energy and polymer volatility, environmental liabilities, customer concentration, old equipment, and a lack of plant-level task or contract evidence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3604 | — | OBSERVED | — |
| n | — | 29 | — | ESTIMATE | — |
| a | 0.16 | 0.27 | 0.39 | PROXY | S2, S3 |
| rho | 0.28 | 0.47 | 0.65 | ESTIMATE | S4, S5 |
| e | 0.05 | 0.15 | 0.3 | ESTIMATE | S1 |
| s5 | 0.1 | 0.21 | 0.34 | PROXY | S6 |
| q | 0.28 | 0.46 | 0.65 | ESTIMATE | S1, S7 |
| d5 | 0.68 | 0.86 | 1.08 | PROXY | S5, S7 |
| o | 0.92 | 0.98 | 1 | ESTIMATE | S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.65 | 1.83 | 3.65 | ESTIMATE |
| F | 0.22 | 1.04 | 2.21 | ESTIMATE |
| C | 5.60 | 9.20 | 10.00 | ESTIMATE |
| D | 6.26 | 8.43 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation evidence covers a broader chemical-manufacturing group rather than NAICS 325220 alone.
- a: Installed automation and task allocation vary strongly between melt spinning, solvent spinning, and texturizing operations.
- rho: This is bounded judgment, not an observed fiber-industry adoption rate.
- rho: EPA monitoring, testing, and recordkeeping obligations limit unattended automation in regulated acrylic and modacrylic processes.
- e: No public dataset reports toll or contract share at six digits.
- e: Dedicated customer specifications alone do not necessarily make a product sale an outsourced service.
- s5: The age statistic is not industry- or size-specific and measures owners, not firms or exits.
- s5: Plants owned by diversified groups have no individual-owner succession trigger.
- q: No public contract set separates specialty from commodity programs.
- q: Retention can differ sharply between high-specification technical fiber and standard polyester or nylon output.
- d5: The production index is supply-side and not specific to contract producers.
- d5: The 2017 comparison does not by itself determine the next five years and mixes fast-growing technical fibers with pressured commodity fibers.
- o: Required operator quantity can migrate to larger or offshore plants even if the physical operator role persists.
- o: This primitive does not duplicate labor automation, which is reflected in a and rho.

## Sources
- **S1** — [2022 NAICS definition: 325220 Artificial and Synthetic Fibers and Filaments Manufacturing](https://www.census.gov/naics/?details=32522&input=32522&year=2022) (accessed 2026-07-22): Defines the industry as cellulosic and noncellulosic fiber and filament manufacturing, including manufacturing and texturizing, and distinguishes texturizing fibers made elsewhere.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Lists chemical equipment operators, production supervisors, chemical plant operators, industrial machinery mechanics, and related plant roles among the largest occupations in chemical manufacturing groups including 3252.
- **S3** — [Producing the goods of the future: Job opportunities in manufacturing](https://www.bls.gov/careeroutlook/2026/article/manufacturing.htm) (accessed 2026-07-22): Reports that production occupations were about half of manufacturing jobs in 2024 and that continued automated-machinery adoption increases need for mechanics.
- **S4** — [AP-42 Section 6.9 Synthetic Fibers](https://gaftp.epa.gov/ap42/ch06/s09/final/c06s09_1995.pdf) (accessed 2026-07-22): Describes finished fiber forms and melt, dry-solvent, wet-solvent, and reaction spinning methods across polyester, nylon, polyolefin, acrylic, modacrylic, spandex, and rayon.
- **S5** — [Acrylic and Modacrylic Fibers Production NESHAP for Area Sources](https://www.epa.gov/stationary-sources-air-pollution/acrylic-and-modacrylic-fibers-production-national-emission) (accessed 2026-07-22): States fiber composition thresholds, end uses, and standards for process vents, spinning lines, storage, wastewater, and equipment leaks, including testing, monitoring, and recordkeeping.
- **S6** — [Business Owners' Ages: Over Half of U.S. Business Owners Were Age 55 and Over](https://www.census.gov/library/visualizations/2020/comm/business-owners-ages.html) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 ABS, data year 2018.
- **S7** — [Industrial Production: Artificial and Synthetic Fibers and Filaments (NAICS 32522)](https://fred.stlouisfed.org/series/IPG32522N) (accessed 2026-07-22): Reports the Federal Reserve real-output index at 71.8055 in June 2026, with 2017 equal to 100, and identifies the series as monthly US industrial production.
