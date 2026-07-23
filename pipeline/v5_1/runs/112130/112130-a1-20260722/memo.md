# 112130 — Dual-Purpose Cattle Ranching and Farming

*v5.1 Stage 1 research memo. Run `112130-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Two recurring commodity outputs and continuous herd monitoring create multiple practical automation and decision-support use cases.
**Weakness:** The exact mixed-output population is poorly measured, often small, and vulnerable to displacement by specialized dairy and beef operators.

## Business-model lens
- Included: US lower-middle-market operators that raise cattle for both milking and meat production and repeatedly sell milk, calves, cull cows, or finished cattle to external cooperatives, processors, feeders, auctions, or packers.
- Excluded: Beef-only ranches, cattle feedlots, dairy-only farms, goat dairies, hobby farms, passive landowners, captive internal units, and non-control financing vehicles.
- Customer and revenue model: Recurring milk sales and periodic cattle sales through cooperatives, processors, livestock auctions, dealers, feeders, or packers, with the farm retaining animal-care, land, production, food-safety, and environmental accountability.
- Deviation from default lens: none

## Executive view
Dual-purpose cattle operations combine data-rich dairy and ranch workflows, so sensing, robotic milking, remote monitoring, health analytics, and administrative automation offer credible efficiencies. The exact industry is nevertheless hard to underwrite: most cattle businesses specialize, public data do not isolate qualifying mixed-output firms, and the frozen labor and LMM-firm inputs are missing. Product demand is broadly durable, but specialized dairy and beef operators may capture that demand more efficiently.

## How AI changes the work
Cow-level sensors, robotic milking, GPS, water and forage monitoring, satellite imagery, and predictive health tools can reduce routine checks and improve breeding, feeding, grazing, and intervention decisions. Physical animal care, calving, treatment, fencing, maintenance, manure, loading, and emergency response remain operator-led.

## Value capture
Mixed milk and cattle revenue diversifies outlets, but both are commodity markets with limited producer pricing power. Operators initially keep cost savings; buyer concentration, formula pricing, auction markets, competitive land use, and ongoing feed and facility needs reduce five-year retention.

## Firm availability
Aging family ownership points to succession needs, but the exact category is narrow and likely dominated by small farms. Transfers may occur as intrafamily succession, land sales, leases, herd dispersals, or specialization rather than acquisition of a transferable operating company, and no defensible LMM population count is supplied.

## Demand durability
Aggregate milk demand is projected to grow and beef demand to remain broadly stable after a near-term dip. Yet dual-purpose breeds and operating models must compete with increasingly scaled and specialized dairy and beef systems, so stable product demand does not guarantee stable demand for this exact firm type.

## Risks and uncertainty
Risks include missing exact-industry financial data, low farm scale, owner-labor dependence, land intensity, buyer concentration, milk and cattle price cycles, feed, drought, disease, animal welfare, environmental rules, and technology connectivity. Adjacent-industry evidence may not transfer cleanly to mixed milk-and-meat farms.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.12 | 0.26 | 0.4 | PROXY | S1, S2 |
| rho | 0.3 | 0.5 | 0.68 | ESTIMATE | S1, S2 |
| e | 0.08 | 0.25 | 0.5 | ESTIMATE | S3, S4 |
| s5 | 0.08 | 0.19 | 0.33 | PROXY | S4 |
| q | 0.3 | 0.5 | 0.7 | ESTIMATE | S5, S6 |
| d5 | 0.92 | 1.03 | 1.13 | PROXY | S5, S6 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.83 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Evidence comes from adjacent dairy and beef operations because exact-industry technology studies were not found.
- a: Owner and family labor are material but often absent from payroll-based occupation data.
- a: The frozen compensation-to-receipts ratio is missing and was not replaced.
- rho: USDA reports positive average returns for precision dairy technology, but economics may not transfer to smaller dual-purpose herds.
- rho: Ranching systems can identify work while still requiring travel and physical intervention.
- e: The exact-industry population is not separately characterized in the public USDA sources found.
- e: Beef-farm evidence shows 90% of specialized farms below $100,000 of sales and may not describe dual-purpose operations.
- e: The supplied LMM firm count is missing and was not estimated.
- s5: Beef-specialist demographics are an adjacent-population proxy.
- s5: Farm property sales do not necessarily transfer the operating business.
- s5: No exact-industry control-transfer series was found.
- q: The revenue mix between milk and cattle is unknown and materially affects price exposure.
- q: USDA projects lower near-term milk prices and changing cattle prices, but these are market outcomes rather than direct pass-through clauses.
- d5: Aggregate dairy and beef demand does not measure the competitiveness of dual-purpose operations.
- d5: Disease, drought, feed costs, trade, herd cycles, and slaughter decisions can dominate five-year output.
- d5: The revenue weight of milk versus meat is unknown.
- o: Operator-required demand can persist while dual-purpose firms disappear through specialization or consolidation.
- o: Veterinary, feed, breeding, hauling, and custom work may be outsourced to firms classified elsewhere.

## Sources
- **S1** — [Precision Dairy Farming, Robotic Milking, and Profitability in the United States](https://ers.usda.gov/publications/113704) (accessed 2026-07-23): USDA ERS finds increasing adoption of milking, breeding, sensor, data, and automation technologies and reports 13% higher average dairy net returns for robotic milking or use of multiple precision technologies.
- **S2** — [A scalable end-to-end IoT and remote sensing platform for precision rangeland and livestock management](https://www.ars.usda.gov/research/publications/publication/?seqNo115=427494) (accessed 2026-07-23): USDA ARS reports deployment across 12 beef ranches in four states and more than 500,000 acres, using sensors, satellite imagery, AI analytics, tracking, vegetation and environmental monitoring to reduce labor and fuel and improve decisions.
- **S3** — [North American Industry Classification System: NAICS 112130](https://www.census.gov/naics/?details=11&input=11&year=2017) (accessed 2026-07-23): Census defines NAICS 112130 as establishments primarily raising cattle for both milking and meat, distinct from beef-only, feedlot, and dairy-only establishments.
- **S4** — [2022 Census of Agriculture: Beef Producers](https://www.nass.usda.gov/Publications/Highlights/2024/Census22_HL_Cattle%20and%20Cattle%20on%20Feed_final.pdf) (accessed 2026-07-23): For specialized beef producers, average age was 58.3 and 39% were 65 or older; 97% of beef and feedlot farms were family farms, 31% had positive net income, and 90% of beef farms had under $100,000 in sales and government payments.
- **S5** — [USDA Agricultural Projections to 2035](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/113817/OCE-2026-1.pdf?v=83882) (accessed 2026-07-23): USDA projects milk output growing 1.2% annually from 2027 to 2035, dairy domestic use growth, beef per-capita disappearance declining initially then recovering, and beef exports rising through 2035.
- **S6** — [United States cattle inventory down slightly](https://www.nass.usda.gov/Newsroom/2026/01-30-2026.php) (accessed 2026-07-23): As of January 1, 2026, USDA counted 86.2 million cattle and calves, 27.6 million beef cows down 1%, 9.57 million milk cows, and a 32.9 million-head calf crop down 2%.
