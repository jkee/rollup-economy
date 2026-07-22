# 316210 — Footwear Manufacturing

*v5.1 Stage 1 research memo. Run `316210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.23 · L 1.22 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat per-pair production relationships in specialty niches where domestic speed, compliance, or origin matters.
**Weakness:** A physical production-heavy labor mix sits inside a domestic market with severe import pressure and a poorly measured eligible-firm share.

## Business-model lens
- Included: Independent US footwear factories that repeatedly manufacture footwear for external brands, retailers, distributors, or government customers under contract, OEM, private-label, or white-label arrangements.
- Excluded: Brand-owned factories producing only proprietary footwear, footwear brands that outsource all production, wholesalers and retailers, repair shops, orthopedic extension footwear, captive internal units, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat B2B production runs priced per pair, style, batch, or contract, often with development, sampling, material procurement, quality control, and packaging bundled into the manufacturing relationship.
- Deviation from default lens: The NAICS code groups factories by product and does not distinguish own-brand production from outsourced manufacturing. The lens is narrowed to contract, OEM, and private-label factories because only those firms provide the recurring external service required by the fixed screen.

## Executive view
The qualifying opportunity is not the whole footwear industry but domestic contract, OEM, and private-label factories. Those plants serve repeat brand and institutional customers and remain physically necessary, yet their production-heavy labor mix limits near-term AI substitution and their demand is constrained by overwhelming import competition.

## How AI changes the work
AI can translate tech packs, check specifications, support pattern and material decisions, schedule jobs, draft quotes and compliance records, predict material needs, assist visual inspection, and manage customer communication. Cutting, stitching, lasting, molding, cementing, finishing, handling, and maintenance remain physical tasks requiring machinery and operators.

## Value capture
A fixed per-pair or per-run price permits initial retention of labor and error savings. Repeat bidding, brand purchasing leverage, transparent landed-cost comparisons, and the portability of many styles push savings back to customers, while short runs, regulated sourcing, speed, and specialty construction improve retention.

## Firm availability
Contract manufacturing clearly exists in the US, but NAICS data do not reveal which firms primarily serve external brands. The 52-firm frozen-band count therefore overstates the eligible population, and broad five-year employer-owner transfer intentions are only a proxy for factory availability.

## Demand durability
Real US footwear output declined materially from 2019 to 2024 and imports dominate the market. Specialty domestic procurement, rapid replenishment, small batches, and reshoring could stabilize eligible factories, but the base case still assumes lower real quantity in year five. Surviving outsourced demand almost always needs an accountable physical manufacturer.

## Risks and uncertainty
Key risks are misidentifying brand companies as contract factories, customer concentration, offshore price competition, style volatility, legacy equipment, scarce skilled labor, capital needs, warranty and fit failures, and uncertain machine-vision economics. Policy-driven demand can reverse quickly with procurement or tariff changes.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3273 | — | OBSERVED | — |
| n | — | 52 | — | ESTIMATE | — |
| a | 0.09 | 0.17 | 0.27 | PROXY | S2, S3 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S3 |
| e | 0.18 | 0.34 | 0.52 | ESTIMATE | S1, S7 |
| s5 | 0.14 | 0.22 | 0.31 | PROXY | S6 |
| q | 0.25 | 0.45 | 0.65 | ESTIMATE | S5, S7 |
| d5 | 0.65 | 0.84 | 1.08 | PROXY | S4, S5 |
| o | 0.9 | 0.97 | 1 | ESTIMATE | S3, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.41 | 1.22 | 2.55 | ESTIMATE |
| F | 1.35 | 2.55 | 3.60 | ESTIMATE |
| C | 5.00 | 9.00 | 10.00 | ESTIMATE |
| D | 5.85 | 8.15 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS industry chart covers own-brand and contract factories together.
- a: O*NET task descriptions are national occupation profiles, not observations of eligible plants.
- a: Robotics may automate physical tasks but is outside pure AI substitution unless coupled to implementable capital projects.
- rho: No current adoption survey isolates US contract footwear factories.
- rho: Implementation economics vary between molded, cemented, stitched, and handcrafted footwear.
- rho: High style turnover can erode training-data reuse.
- e: Public marketing may advertise contract capability even when most revenue is proprietary product.
- e: Some firms combine brands, retail, and contract production.
- e: The frozen firm-count estimate is itself margin-bridged and may misclassify band membership.
- s5: Intentions differ from completed control transfers.
- s5: Gallup spans all employer industries and sizes.
- s5: A strategic buyer may acquire a brand but close or offshore its factory, failing the transferable-operation test.
- q: No public dataset measures contract repricing or savings sharing.
- q: Government cost or pricing clauses may differ from commercial private-label agreements.
- q: Retention can be higher for scarce specialty capacity and lower for portable commodity styles.
- d5: The 2019-2024 interval includes pandemic disruption.
- d5: Import customs values and domestic sectoral output are not directly comparable measures.
- d5: Tariffs, Berry Amendment procurement, and supply-chain policy can materially alter domestic demand.
- o: Demand may migrate to larger foreign operators even if an operator remains necessary globally.
- o: This primitive concerns operator necessity, not employment intensity.
- o: Highly automated molded footwear may require fewer people but still requires a responsible plant operator.

## Sources
- **S1** — [2022 NAICS Definition: Footwear Manufacturing](https://www.census.gov/naics/?details=316210&input=316210&year=2022) (accessed 2026-07-22): Defines NAICS 316210 as establishments primarily engaged in manufacturing footwear except orthopedic extension footwear and lists major footwear examples; the definition does not separate contract from own-brand factories.
- **S2** — [BLS OEWS Data Tables for Industry Employment Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest footwear-manufacturing occupations, including 3,180 shoe-machine operators, 2,580 shoe and leather workers, 470 sewing-machine operators, 380 production supervisors, 240 maintenance workers, and 230 inspectors.
- **S3** — [O*NET: Shoe Machine Operators and Tenders](https://www.onetonline.org/link/details/51-6042.00) (accessed 2026-07-22): Describes core tasks including inspecting finished shoes, aligning parts, operating machines, loading thread, reading work orders, conducting maintenance, and handling materials, grounding the physical-versus-informational task bridge.
- **S4** — [BLS via FRED: Real Sectoral Output for Footwear Manufacturing](https://fred.stlouisfed.org/data/IPUEN316210T010000000) (accessed 2026-07-22): Provides the NAICS 316210 real sectoral-output index (2017=100), including 99.028 in 2019, 78.738 in 2020, 84.105 in 2021, 77.568 in 2022, 76.733 in 2023, and 75.404 in 2024.
- **S5** — [USITC Trade Shifts 2024: Footwear Figures](https://www.usitc.gov/system/files/research_and_analysis/tradeshifts/2024/files/footwear_figures.html) (accessed 2026-07-22): Reports $27.319 billion of US footwear imports in 2024, with China at 35.8% and Vietnam at 32.4%, grounding the scale and concentration of offshore competition.
- **S6** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports from a fall 2024 US survey that 22% of employer-business owners planned to sell or transfer ownership within five years, rising to 30% among employer owners age 55 or older.
- **S7** — [Okabashi Wholesale and Contract Manufacturing](https://www.okabashi.com/pages/wholesale) (accessed 2026-07-22): A current US footwear manufacturer explicitly offers private-label and contract manufacturing, says it has contract manufacturing with major brands, and describes a repeat external-customer production model; it also states that over 99% of American-worn footwear is made abroad.
