# 325311 — Nitrogenous Fertilizer Manufacturing

*v5.1 Stage 1 research memo. Run `325311-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.39 · L 0.20 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Essential recurring crop nutrient demand supports physical production and repeat customer programs.
**Weakness:** Commodity economics, very low labor intensity, and a scarce outsourced-service subset constrain both AI benefit and capture.

## Business-model lens
- Included: US lower-middle-market firms repeatedly manufacturing or formulating nitrogenous fertilizer for external customers under toll, private-label, waste-conversion, or customer-specific supply programs.
- Excluded: Large integrated commodity ammonia and urea plants selling standard output, captive production, distributors and applicators, mixing-only firms classified in 325314, compost producers, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring industrial or agricultural supply programs priced per ton, batch, or contracted capacity, usually with natural-gas, ammonia, freight, or nutrient-market repricing and customer specifications for nutrient content and physical form.
- Deviation from default lens: The NAICS definition combines large commodity nitrogen production, fertilizer made from waste, and in-plant mixing. The lens is narrowed to repeat toll, private-label, waste-conversion, and customer-specific manufacturing so it represents an outsourced service rather than a commodity position.

## Executive view
The qualifying opportunity is a very small customer-specific or waste-conversion subset of a capital-intensive commodity industry. AI can streamline records, planning, maintenance, laboratory review, and commercial support, but low labor intensity and benchmark-driven pricing limit the economic surface area and retained benefit.

## How AI changes the work
Most near-term opportunity lies in production and environmental records, scheduling, maintenance knowledge, inventory, laboratory exception review, customer documentation, energy analysis, and procurement. Continuous high-pressure reaction, material handling, inspection, and process-safety accountability remain operator-controlled.

## Value capture
Local logistics, dependable capacity, customer specifications, and unusual feedstock access can preserve some gain. Global fertilizer prices, natural-gas sensitivity, per-ton bidding, input escalators, and annual farm purchasing push savings back to customers.

## Firm availability
Only toll, private-label, customer-specific, or waste-conversion firms meet the outsourced-service lens. Broad owner aging suggests succession potential among smaller firms, but upstream ammonia is concentrated, corporate, and encumbered by large assets and environmental diligence.

## Demand durability
Nitrogen is an essential plant nutrient with no substitute, and USDA shows it is consistently the largest fertilizer category by volume. Demand should be durable but roughly flat as use efficiency, crop mix, imports, and price cycles offset the underlying need.

## Risks and uncertainty
Major uncertainties are the tiny unmeasured eligible subset, natural-gas and ammonia volatility, global trade, customer concentration, environmental liabilities, process safety, cyclicality, low labor intensity, and lack of plant-task and contract evidence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0595 | — | OBSERVED | — |
| n | — | 48 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.32 | PROXY | S2, S3 |
| rho | 0.24 | 0.41 | 0.58 | ESTIMATE | S4, S5 |
| e | 0.01 | 0.06 | 0.16 | ESTIMATE | S1, S7 |
| s5 | 0.08 | 0.18 | 0.3 | PROXY | S6, S7 |
| q | 0.18 | 0.34 | 0.55 | ESTIMATE | S8 |
| d5 | 0.88 | 1 | 1.12 | PROXY | S7, S8, S9 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S4, S5, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.07 | 0.20 | 0.44 | ESTIMATE |
| F | 0.06 | 0.67 | 1.92 | ESTIMATE |
| C | 3.60 | 6.80 | 10.00 | ESTIMATE |
| D | 8.45 | 9.90 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is for a broader chemical-manufacturing group, not NAICS 325311 alone.
- a: The injected compensation ratio is unusually low and reinforces capital intensity, but it is frozen dataset input rather than evidence for task exposure.
- rho: No industry adoption study directly measures the five-year implementable share.
- rho: Implementation in back-office workflows should be faster than in process control, creating substantial plant-to-plant dispersion.
- e: Public industry data do not measure the contract-manufacturing share.
- e: USGS reports only 18 ammonia-producing companies in 2025, suggesting concentration at the upstream end, while the NAICS definition also covers smaller downstream and waste-based operations.
- s5: Owner age is neither industry-specific nor a direct observation of sales.
- s5: The qualifying lens likely has a different ownership profile from large ammonia producers documented by USGS.
- q: No public contract sample was available.
- q: Capture differs materially between commodity ammonia and differentiated waste-derived or customer-specific products.
- d5: Consumption data combine nitrogen, phosphate, and potash, though the source separately identifies nitrogen's share.
- d5: Ammonia production includes industrial uses and does not isolate qualifying LMM contract manufacturers.
- o: Operator-required demand can consolidate into larger integrated plants or imports even when the accountable production role persists.
- o: Labor automation is accounted for in a and rho, not deducted again here.

## Sources
- **S1** — [2022 NAICS definition: 325311 Nitrogenous Fertilizer Manufacturing](https://www.census.gov/naics/?details=325&input=325&year=2022) (accessed 2026-07-22): Defines the industry as nitrogenous fertilizer-material manufacture, fertilizer manufacture from sewage or animal waste, and nitrogenous materials mixed with other ingredients.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Lists chemical equipment operators, production supervisors, chemical plant operators, industrial machinery mechanics, and related plant roles among the largest occupations in chemical manufacturing groups including 3253.
- **S3** — [Producing the goods of the future: Job opportunities in manufacturing](https://www.bls.gov/careeroutlook/2026/article/manufacturing.htm) (accessed 2026-07-22): Reports that production occupations comprised about half of manufacturing jobs in 2024 and connects automated-machinery adoption to continuing mechanic demand.
- **S4** — [Fertilizer Manufacturing Effluent Guidelines](https://www.epa.gov/eg/fertilizer-manufacturing-effluent-guidelines) (accessed 2026-07-22): Describes ammonia manufacture from atmospheric nitrogen and hydrogen, downstream urea and ammonium products, and regulated wastewater streams including condensate, blowdown, spills, leaks, and runoff.
- **S5** — [Subpart G Information Sheet: Ammonia Manufacturing](https://www.epa.gov/ghgreporting/subpart-g-information-sheet) (accessed 2026-07-22): Defines covered ammonia processes and specifies reporting of process CO2 and combustion CO2, methane, and nitrous oxide, along with calculation and record duties.
- **S6** — [Business Owners' Ages: Over Half of U.S. Business Owners Were Age 55 and Over](https://www.census.gov/library/visualizations/2020/comm/business-owners-ages.html) (accessed 2026-07-22): Reports that 51% of responding owners of employer businesses were age 55 or older in the 2019 ABS, data year 2018.
- **S7** — [Mineral Commodity Summaries 2026: Nitrogen (Fixed)—Ammonia](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-nitrogen.pdf) (accessed 2026-07-22): Reports 18 companies at 38 US plants in 2025, about 80% capacity utilization, estimated production of 14.0 million metric tons versus 13.6 million in 2024, 88% of domestic ammonia production for fertilizer, and no substitute for nitrogen as a plant nutrient.
- **S8** — [Drivers of Fertilizer Markets: Supply, Demand, and Prices](https://www.ers.usda.gov/media/9156/err-354.pdf?v=84759) (accessed 2026-07-22): Reports declining US fertilizer production and consumption relative to 2006, nitrogen consumption above phosphate and potash combined, and strong roles for energy costs, crop prices, and global trade.
- **S9** — [U.S. fertilizer consumption rebounds from 2021 drop](https://www.ers.usda.gov/data-products/charts-of-note/113348) (accessed 2026-07-22): Reports 21 million metric tons total fertilizer consumption in 2013, stabilization after 2014 through 2020, a 9.4% fall to 18.3 million in 2021, and nitrogen averaging 59% of volume during 2006-23.
