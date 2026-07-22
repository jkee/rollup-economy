# 493110 — General Warehousing and Storage

*v5.1 Stage 1 research memo. Run `493110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** HIGHEST_PRIORITY · A 9.18 · L 7.71 · interval PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A very large wage-weighted physical and administrative workflow base with identifiable software, robotics, and decision-support applications.
**Weakness:** LMM implementation is constrained by brownfield layouts, capital intensity, integration complexity, and customer contracts that can pass productivity gains through.

## Business-model lens
- Included: US lower-middle-market operators of general merchandise warehouses and distribution facilities that repeatedly provide storage, handling, inventory control, pick-pack, and related fulfillment services to external customers.
- Excluded: Captive in-house warehouses, real-estate-only shells, refrigerated and farm-product storage classified elsewhere, non-control financing vehicles, and firms without recurring or repeat external-customer service revenue.
- Customer and revenue model: Business customers buy recurring storage capacity and transaction-based receiving, handling, picking, packing, shipping, clerical, and accessorial services; contracts commonly combine monthly minimums with per-unit and hourly charges.
- Deviation from default lens: none

## Executive view
General warehouses combine a large physical labor base with clerical and planning workflows that are increasingly software-enabled. The opportunity depends on converting selective automation into durable unit-cost advantage without assuming that highly variable brownfield handling becomes fully autonomous.

## How AI changes the work
AI can improve demand and labor planning, slotting, exception triage, inventory reconciliation, documentation, billing, and customer communication; coupled automation can reduce travel, picking, packing, and vehicle-operator hours. Irregular items, mixed layouts, safety, maintenance, and customer-specific processes keep substantial work human-led.

## Value capture
Monthly minimums and transaction rates can preserve some savings before renewal, while hourly, cost-plus, productivity-sharing, and competitively rebid contracts pass benefits through. Retention should therefore be meaningful but incomplete and highly contract-specific.

## Firm availability
Most properly classified independent general warehouses fit recurring external-service economics, but dedicated single-customer sites, captive units, passive property shells, and fragile customer concentrations reduce true eligibility. Broad employer-owner surveys indicate transfer intent, while completed control-transfer evidence for this industry remains thin.

## Demand durability
BLS projects 2.3% annual real-output growth for warehousing and storage through 2034. E-commerce and physical supply chains support quantity, and automation is more likely to change staffing per unit than eliminate custody and accountable operation of facilities.

## Risks and uncertainty
The main risks are overestimating automation of irregular physical work, underbudgeting integration and facility redesign, customer capture of savings, concentration-driven contract loss, and confusing broad four-digit data with general warehousing. A bad outcome is expensive technology layered onto low-quality data and inflexible customer contracts with little retained benefit.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 2.5931 | — | OBSERVED | — |
| n | — | 1098 | — | ESTIMATE | — |
| a | 0.28 | 0.4 | 0.52 | PROXY | S1, S2 |
| rho | 0.25 | 0.42 | 0.6 | PROXY | S3, S4 |
| e | 0.72 | 0.84 | 0.93 | ESTIMATE | — |
| s5 | 0.08 | 0.13 | 0.2 | PROXY | S5 |
| q | 0.25 | 0.45 | 0.65 | PROXY | S6 |
| d5 | 0.98 | 1.12 | 1.25 | PROXY | S7 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S2, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 7.26 | 10.00 | 10.00 | PROXY |
| F | 6.70 | 7.71 | 8.56 | ESTIMATE |
| C | 5.00 | 9.00 | 10.00 | PROXY |
| D | 8.82 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is NAICS 493100 rather than six-digit 493110 and includes employers of all sizes.
- a: Task exposure is inferred from occupations and stated automation mechanisms rather than directly measured.
- a: The unusually high frozen compensation-to-output input may make occupational wage shares an imperfect guide to controllable operating labor.
- rho: The logistics adoption survey overrepresents enterprises with revenue above $500 million.
- rho: The warehouse literature review draws heavily on non-US case studies and Industry 4.0 tools broader than AI.
- rho: Implementation success depends strongly on SKU profile, building geometry, throughput, and customer IT interfaces.
- e: No source directly measures eligibility under the frozen lens.
- e: The frozen n estimate is margin-bridged and may include firms whose EBITDA quality or classification differs from the lens.
- e: Single-customer dedicated facilities can be operating businesses yet have weak standalone transferability.
- s5: Gallup is not industry-specific and includes employer businesses outside the LMM band.
- s5: Intent is not an observed completion rate.
- s5: The estimate excludes closures, minority recapitalizations, and internal reorganizations without a qualifying control change.
- q: The pricing study is a market guide, not a representative contract census.
- q: Retention varies sharply between dedicated cost-plus sites and shared multi-client warehouses.
- q: Customer concentration and service-level penalties can transfer value even when headline unit prices are fixed.
- d5: The projection is four-digit NAICS 493000, not 493110.
- d5: A ten-year national projection is converted to the required five-year horizon using its stated compound rate.
- d5: Real output is the closest public quantity proxy but is not a direct constant-quality service-basket volume index.
- o: No source directly measures the share of future quantity requiring an accountable LMM operator.
- o: Large customers may insource highly standardized fulfillment or shift volume to vertically integrated platforms.
- o: The estimate concerns operator requirement, not the number of workers inside each facility.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 493100 Warehousing and Storage](https://www.bls.gov/oes/2023/may/naics4_493100.htm) (accessed 2026-07-22): Industry occupation mix and wages: 1,912,650 total jobs; transportation/material-moving 75.38%, office support 10.13%, management 2.93%; detailed warehouse occupations and wages.
- **S2** — [Factors affecting occupational utilization, 2024-34](https://www.bls.gov/emp/tables/factors-affecting-occupational-utilization.htm) (accessed 2026-07-22): BLS identifies AGVs, robotics, collaborative automation, and automated storage/retrieval as reducing shares of industrial-truck operators, hand material movers, packers, and stockers in NAICS 493000.
- **S3** — [Digital logistics: Into the express lane?](https://www.mckinsey.com/capabilities/operations/our-insights/digital-logistics-into-the-express-lane) (accessed 2026-07-22): Logistics digital and gen-AI adoption expectations, smaller-company adoption lag, implementation delays, and data, integration, skills, and change-management barriers.
- **S4** — [Applications of Industry 4.0 Technologies in Warehouse Management: A Systematic Literature Review](https://www.mdpi.com/2305-6290/7/2/24) (accessed 2026-07-22): Warehouse technology benefits and implementation barriers including lifecycle cost, legacy integration, physical layout, poor data, skills, maintenance, cybersecurity, and safety.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 owner survey: 22% of employer-business owners reported plans to sell or transfer ownership within five years, versus 9% of nonemployers.
- **S6** — [Armstrong & Associates Contract Warehouse Pricing Guidelines and North American Warehousing Market Report 2023](https://www.3plogistics.com/wp-content/uploads/2025/06/Warehousing-Report-2023.pdf) (accessed 2026-07-22): Observed 3PL pricing units including monthly minimums, per-order and per-pick fees, storage, hourly forklift and clerical labor, IT/EDI charges, and fully burdened rates including margin.
- **S7** — [BLS Table 2.11 Employment and output by industry, 2024-34](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): NAICS 493000 real output in chained 2017 dollars rises from $134.7 billion in 2024 to $169.7 billion in 2034, a 2.3% compound annual rate; employment rises only 1.4%.
