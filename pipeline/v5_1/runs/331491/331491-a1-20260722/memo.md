# 331491 — Nonferrous Metal (except Copper and Aluminum) Rolling, Drawing, and Extruding

*v5.1 Stage 1 research memo. Run `331491-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.89 · L 0.69 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Qualification-heavy repeat processing relationships can retain workflow gains while critical-material end markets expand.
**Weakness:** More than half of employment is physical production, and public data cannot isolate toll-processing firms or six-digit task exposure.

## Business-model lens
- Included: Independent US toll, contract, and custom processors that repeatedly roll, draw, or extrude purchased nickel, titanium, zinc, lead, precious, refractory, or other nonferrous metals into customer-specified shapes and have transferable operations in the target band.
- Excluded: Copper and aluminum processors, captive mills, integrated primary smelters, businesses focused on speculative metal ownership rather than processing, project shells, and non-control investments.
- Customer and revenue model: Revenue is earned through conversion charges and per-pound or per-lot sales, commonly with metal-price pass-through, specifications, certifications, minimum lots, and repeat industrial purchase orders.
- Deviation from default lens: The code mixes commodity mill-product manufacturing with outsourced toll and custom conversion. The lens retains repeat external processing relationships because treating captive and commodity-integrated mills as recurring service firms would be incoherent.

## Executive view
Specialty nonferrous processors offer repeat, qualification-heavy customer relationships and meaningful digital workflows, but most labor remains tied to physical machines, quality, maintenance, and material handling. The coherent acquisition population is toll and custom conversion, not captive or commodity-integrated mills.

## How AI changes the work
The strongest uses are quoting, specification review, production planning, inventory and purchasing, certificate and traceability preparation, maintenance knowledge, quality analysis, and customer communication. Machine setup, furnace work, inspection, material movement, and final product release remain operator-intensive.

## Value capture
Conversion-charge economics and qualification barriers can preserve savings, especially for scarce alloys and difficult tolerances. Multi-year buyer negotiations and requalification of competitors still create pass-through pressure.

## Firm availability
The injected pool is only an estimate and may be distorted by metal-price revenue. Eligible firms must be independent, repeatedly serve external customers, have durable certifications and management, and avoid captive or speculative metal economics.

## Demand durability
Aerospace, defense, energy, electronics, batteries, and high-performance industrial uses support real growth, while imports, commodity cycles, and alloy substitution widen the range. The outlook is favorable but not uniform across metals.

## Risks and uncertainty
Major risks include four-digit proxy data, metal-price volatility, customer concentration, qualification loss, scrap and yield variation, working capital, environmental obligations, legacy systems, and already-automated process controls.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2059 | — | OBSERVED | — |
| n | — | 80 | — | ESTIMATE | — |
| a | 0.09 | 0.17 | 0.26 | PROXY | S1 |
| rho | 0.28 | 0.49 | 0.68 | ESTIMATE | S1, S2 |
| e | 0.18 | 0.36 | 0.56 | ESTIMATE | S2 |
| s5 | 0.11 | 0.2 | 0.31 | PROXY | S3 |
| q | 0.28 | 0.49 | 0.7 | ESTIMATE | S2, S4 |
| d5 | 0.93 | 1.1 | 1.29 | PROXY | S4, S5 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S2, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.69 | 1.46 | ESTIMATE |
| F | 1.53 | 3.07 | 4.34 | ESTIMATE |
| C | 5.60 | 9.80 | 10.00 | ESTIMATE |
| D | 8.74 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Four-digit occupation data include different nonferrous processes and product mixes.
- a: Existing machine controls, optimization software, and automated inspection are not separated from not-yet-automated tasks.
- rho: No six-digit longitudinal AI implementation study was located.
- rho: Higher-specification plants may gain more from documentation but implement more slowly because validation burdens are greater.
- e: Public data do not separate toll processing from metal-product sales.
- e: The injected n uses a machinery margin proxy that may not reflect volatile metal pass-through revenue.
- s5: Cross-industry intentions are not completed transactions.
- s5: Strategic asset purchases and family transfers may not preserve an eligible standalone firm.
- q: No public evidence directly measures productivity pass-through.
- q: Reported revenue and margin can be distorted by large changes in metal prices.
- d5: Four-digit output includes processes outside 331491.
- d5: Demand and qualification cycles vary sharply across nickel, titanium, zinc, lead, precious, and refractory metal shapes.
- o: This measures operator requirement, not employment intensity.
- o: Material or geography substitution belongs primarily in d5.

## Sources
- **S1** — [Nonferrous Metal (except Aluminum) Production and Processing - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_331400.htm) (accessed 2026-07-22): Broader-industry occupation mix: 53.18% production, 7.66% installation/maintenance/repair, 7.76% office support, and 10.47% extruding/drawing operators.
- **S2** — [NAICS 331491 Definition](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Industry scope: rolling, drawing, or extruding shapes from purchased nonferrous metals other than copper and aluminum, including integrated scrap recovery and shape production.
- **S3** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry succession proxy: 52.3% of employer businesses have owners age 55 or older and 22% planned a five-year sale or transfer.
- **S4** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects broader NAICS 331400 real output from 50.3 to 64.1 billion chained 2017 dollars over 2024-34, a 2.4% annual rate.
- **S5** — [What Are Critical Minerals and Materials?](https://www.energy.gov/cmm/what-are-critical-minerals-and-materials) (accessed 2026-07-22): DOE maps nickel, titanium, cobalt, zinc, precious, refractory, and other nonferrous materials to batteries, aerospace, defense, high-performance alloys, electronics, catalysts, and energy technologies.
