# 316990 — Other Leather and Allied Product Manufacturing

*v5.1 Stage 1 research memo. Run `316990-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → CONDITIONAL · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Repeat specialized OEM programs where domestic speed, compliance, engineering support, or origin requirements matter.
**Weakness:** No defensible LMM-band firm count exists, and the NAICS code is too heterogeneous to infer eligible target availability from aggregate data.

## Business-model lens
- Included: Independent US contract cut-and-sew and assembly manufacturers that repeatedly produce customer-designed bags, carrying cases, pouches, straps, harnesses, and related soft goods from leather, textiles, plastics, or substitutes for external brands, OEMs, distributors, medical, industrial, outdoor, defense, or government customers.
- Excluded: Own-brand-only manufacturers, wholesalers and retailers, captive factories, consumer bespoke artisans without repeat outsourced programs, leather shoe parts and soles, industrial leather belting, pet furnishings, unrelated hard goods, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat B2B contract, OEM, or private-label programs priced per unit, batch, or purchase order, often bundling design-for-manufacture, prototyping, sourcing, cutting, sewing, assembly, quality control, branding, packaging, and fulfillment.
- Deviation from default lens: NAICS 316990 combines consumer luggage and purses, wallets, shoe findings, pet furnishings, industrial belting, protective leather goods, and products made from substitute materials. These have materially different processes and end markets, so the lens is narrowed for coherence to contract-manufactured bags, cases, straps, harnesses, and related sewn soft goods; the narrowing is based on operating-model comparability, not attractiveness.

## Executive view
A coherent opportunity exists inside the broad code among domestic contract manufacturers of bags, cases, straps, harnesses, and related soft goods. Repeat OEM programs and physical accountability support operator durability, while production-heavy labor limits AI substitution and the missing LMM firm-count input prevents a grounded estimate of how many targets exist.

## How AI changes the work
AI can accelerate tech-pack intake, quoting, materials planning, pattern and nesting support, work instructions, scheduling, production reporting, compliance documentation, customer service, and visual quality triage. Material handling, cutting, sewing, joining, hardware installation, assembly, maintenance, and final tactile judgment remain physical and often high-mix.

## Value capture
Fixed per-unit or per-run pricing supports initial margin retention. Custom engineering, prototypes, regulated materials, domestic-origin rules, short lead times, and product-specific quality systems create switching costs, but repeat tenders and customer cost visibility share gains over time.

## Firm availability
Current US contract manufacturers visibly serve external brands and OEMs, but NAICS 316990 also contains own-brand consumer firms and very different industrial products. Eligibility is therefore a minority estimate, and the frozen dataset's missing LMM firm count is the most consequential availability gap.

## Demand durability
Ancestor-industry real output in 2024 remained above 2017 and 2019 levels but fell from its 2022 peak. The narrowed niche can benefit from medical, defense, outdoor, and industrial programs as well as domestic sourcing, yet product and customer diversity justify a flat central five-year quantity outlook rather than a strong directional claim.

## Risks and uncertainty
Major risks include an unknown target count, lens misclassification, customer concentration, offshore re-sourcing, fashion and procurement volatility, legacy equipment, skilled sewing labor scarcity, high-mix integration costs, warranty failures, and the possibility that advertised contract capability is immaterial to revenue.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3247 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.1 | 0.19 | 0.3 | PROXY | S2, S3 |
| rho | 0.38 | 0.58 | 0.75 | ESTIMATE | S3, S6 |
| e | 0.1 | 0.24 | 0.42 | ESTIMATE | S1, S6 |
| s5 | 0.14 | 0.22 | 0.31 | PROXY | S5 |
| q | 0.3 | 0.5 | 0.7 | ESTIMATE | S6 |
| d5 | 0.76 | 0.98 | 1.2 | PROXY | S4, S6 |
| o | 0.9 | 0.97 | 1 | ESTIMATE | S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.49 | 1.43 | 2.92 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.84 | 9.51 | 10.00 | ESTIMATE |

## Caveats
- a: BLS covers the full heterogeneous NAICS industry rather than the narrowed lens.
- a: The occupation chart provides counts but not a complete wage-weighted task distribution.
- a: AI-enabled robotics could expand physical automation but requires capital and integration beyond software deployment.
- rho: No current adoption survey isolates eligible US contract soft-goods plants.
- rho: Frequent custom designs reduce the value of historical training data.
- rho: Quality failures in medical, defense, or equipment cases can outweigh labor savings.
- e: The provided dataset has no defensible LMM-band firm count, so this share cannot currently be converted into an eligible-firm count.
- e: Firms often mix proprietary brands, wholesale, custom work, and contract production.
- e: Publicly advertised capability may not represent a material share of revenue.
- s5: Survey plans are not completed transactions.
- s5: Gallup spans all employer industries and sizes.
- s5: The missing frozen LMM firm count makes observed transaction-rate calibration especially difficult.
- q: No public dataset measures savings pass-through in this contract niche.
- q: Retention differs between commodity promotional bags and regulated medical, defense, or device-specific cases.
- q: Demand effects and implementation costs are excluded from this primitive.
- d5: The BLS series is at ancestor NAICS 31699 and combines products excluded from the lens.
- d5: Pandemic and reopening effects distort recent comparisons.
- d5: Consumer fashion, medical devices, defense procurement, and industrial cases can move independently.
- o: The operator can migrate offshore even when operator-required demand remains globally.
- o: This estimate concerns accountable operator necessity, not workforce size.
- o: Simpler products may become more automated than complex, high-mix sewn assemblies.

## Sources
- **S1** — [2022 NAICS Definition: Other Leather and Allied Product Manufacturing](https://www.census.gov/naics/?details=316&input=316&year=2022) (accessed 2026-07-22): Defines NAICS 316990 and its heterogeneous examples, including billfolds, luggage, purses, dog furnishings, shoe findings and soles, watch bands, protective leather goods, and products made from leather substitutes.
- **S2** — [BLS OEWS Data Tables for Industry Employment Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest occupations in other leather and allied product manufacturing, including 2,430 shoe/leather workers, 1,620 assemblers, 1,400 sewing-machine operators, 500 production supervisors, 410 managers, and 400 shipping/inventory clerks.
- **S3** — [O*NET: Sewing Machine Operators](https://www.onetonline.org/link/details/51-6031.00) (accessed 2026-07-22): Describes core physical tasks such as monitoring machines, positioning and guiding material, threading equipment, measuring output, attaching components, inspecting defects, and maintenance; reports 84% continually use their hands and 71% continually make repetitive motions.
- **S4** — [BLS via FRED: Real Sectoral Output for Other Leather and Allied Product Manufacturing](https://fred.stlouisfed.org/data/IPUEN31699T010000000) (accessed 2026-07-22): Provides the real sectoral-output index for NAICS 31699 (2017=100), including 97.171 in 2019, 96.486 in 2020, 117.471 in 2021, 120.624 in 2022, 112.705 in 2023, and 110.281 in 2024.
- **S5** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports from a fall 2024 US survey that 22% of employer-business owners planned to sell or transfer ownership within five years, rising to 30% among employer owners age 55 or older.
- **S6** — [United Manufacturers: Private Label and Custom Contract Sewing](https://www.unitedmfg.com/custom-contract) (accessed 2026-07-22): Documents a current US contract model offering OEM/private-label production, prototyping, patterns, samples, small-to-large runs, assembly, packaging and fulfillment for bags, cases, straps, harnesses, protective gear, and industrial and specialty applications.
