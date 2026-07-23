# 112519 — Other Aquaculture

*v5.1 Stage 1 research memo. Run `112519-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** The principal driver is the potential to pair recurring biological-production needs with sensing, control, and monitoring improvements in specialized operations that are difficult for customers to replicate.
**Weakness:** The principal weakness is the extremely small, heterogeneous, and poorly measured pool of firms that plausibly meet both the industry definition and the recurring outsourced-service lens.

## Business-model lens
- Included: Independent U.S. lower-middle-market establishments in NAICS 112519 that repeatedly provide contracted cultivation, growing, stocking, or related aquaculture production for external customers while raising aquatic plants or aquatic animals other than finfish and shellfish.
- Excluded: Finfish and shellfish farms, wild capture, processors without farming operations, public or nonprofit conservation-only facilities, hobby producers, passive water or land ownership, captive internal units, and farms that only sell their own biological output without a recurring outsourced-service relationship.
- Customer and revenue model: Eligible firms earn recurring contract-production or cultivation fees and may also sell algae, seaweed, alligators, frogs, turtles, or other biological output under repeat supply agreements. Contracts may be fixed-price, unit-priced, cost-plus, or tied to survival, weight, quality, or delivery specifications.
- Deviation from default lens: none

## Executive view
Other Aquaculture is a very small and heterogeneous industry spanning aquatic plants and non-finfish, non-shellfish animals. USDA reports meaningful farm-gate output, but only a small portion is likely to satisfy the fixed recurring outsourced-service lens, and direct evidence on ownership transfers, contracts, labor mix, and automation is sparse.

## How AI changes the work
AI can improve environmental monitoring, inventory and biomass estimation, anomaly detection, recordkeeping, scheduling, compliance support, and selected control systems. Physical husbandry, maintenance, harvest, biosecurity, and emergency response remain central. Existing federal demonstrations establish technical plausibility but are concentrated in finfish recirculating systems rather than this code's algae, alligator, frog, turtle, and other operations.

## Value capture
Capture depends on contract design and differentiation. Fixed-price periods, scarce permits, specialized know-how, reliable survival and quality, and difficult site replication can preserve benefits; renewal repricing, concentrated buyers, imported substitutes, and transparent unit prices can transfer savings to customers.

## Firm availability
USDA counted 238 miscellaneous-aquaculture farms with $157.7 million of sales in 2023, but most operations are small and the data do not identify outsourced-service revenue or EBITDA. The pool of independent, transferable lower-middle-market contract operators is therefore likely narrow and requires business-level confirmation.

## Demand durability
Broad U.S. aquaculture has shown modest real growth and long-run seafood consumption has increased, while aquatic plants may serve food and nonfood uses. Those indicators do not directly measure this code's service basket, and alligator, specialty-animal, algae, and seaweed markets can follow different cycles, leaving a wide five-year demand range.

## Risks and uncertainty
Major risks include biological losses, disease, storms and water conditions, energy and feed costs, permitting, environmental compliance, customer concentration, import competition, product-specific demand swings, and expensive system failures. The largest analytical uncertainty is the mismatch between public aquaculture product data and the fixed outsourced-service lens.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.14 | 0.27 | 0.41 | PROXY | S5 |
| rho | 0.23 | 0.41 | 0.59 | PROXY | S5, S6 |
| e | 0.02 | 0.08 | 0.18 | ESTIMATE | S1, S2, S3 |
| s5 | 0.13 | 0.24 | 0.37 | ESTIMATE | S2, S3 |
| q | 0.29 | 0.48 | 0.66 | ESTIMATE | S2, S4 |
| d5 | 0.91 | 1.04 | 1.2 | PROXY | S2, S3, S4 |
| o | 0.87 | 0.95 | 0.99 | ESTIMATE | S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 5.80 | 9.60 | 10.00 | ESTIMATE |
| D | 7.92 | 9.88 | 10.00 | ESTIMATE |

## Caveats
- a: The cited technology evidence is primarily from finfish recirculating systems, which are outside this six-digit industry.
- a: The code combines species and production environments with very different labor mixes, and no direct occupational distribution was found.
- rho: Research demonstrations are not evidence of economical deployment across small commercial operations.
- rho: Permitting and environmental requirements differ by organism, water source, and state.
- e: The provided dataset has no defensible LMM firm-count estimate for this industry.
- e: USDA reports farm-gate product sales, not EBITDA or outsourced-service revenue, and its miscellaneous category is not a perfect establishment-level NAICS crosswalk.
- s5: Farm-count changes do not distinguish sales, closures, family transfers, internal reorganizations, or new formations.
- s5: Permit transferability and dependence on the owner's technical relationships vary by state and production system.
- q: The code mixes highly differentiated algae and specialty-animal products with more price-sensitive farm output.
- q: USDA farm-gate sales data do not disclose contract structure, gross benefit, or post-renewal sharing.
- d5: The 2023 USDA miscellaneous category is small and concentrated, so changes at a few farms can move totals materially.
- d5: Seafood consumption and import reliance are weak proxies for algae and nonfood animal demand.
- o: Closed indoor systems may support more remote control than marine, pond, or field cultivation.
- o: A production customer's decision to internalize growing activity would reduce operator-required outsourced demand independently of technical automation.

## Sources
- **S1** — [2022 NAICS Definition: 112519 Other Aquaculture](https://www.census.gov/naics/?details=112&input=112&year=2022) (accessed 2026-07-22): Official scope covering aquatic animals other than finfish and shellfish and aquatic plants, including alligator, algae, frog, seaweed, and turtle production.
- **S2** — [2023 Census of Aquaculture, Table 8: Miscellaneous Aquaculture Production and Sales by Type](https://data.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/Aquaculture/aqua_1_008_008.pdf) (accessed 2026-07-22): Code-relevant product mix, farm counts, and 2023 sales for miscellaneous aquaculture, including algae, alligators, frogs, turtles, and other products.
- **S3** — [2023 Census of Aquaculture, Table 9: Summary by Value of Aquaculture Products Sold](https://data.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/Aquaculture/aqua_1_009_009.pdf) (accessed 2026-07-22): Aquaculture farm-size distribution and 2018-to-2023 farm and sales totals, including the miscellaneous-aquaculture category.
- **S4** — [Aquaculture](https://www.ers.usda.gov/topics/animal-products/aquaculture) (accessed 2026-07-22): Broad U.S. aquaculture systems, real sales and farm-count trends, seafood consumption, import reliance, trade, and policy context.
- **S5** — [Progress Towards the National Strategic Plan for Aquaculture Research (2022)](https://www.ars.usda.gov/sca/Task%20Forces%20and%20Working%20Groups/Science/2022%20NSTC%20Subcomittee%20on%20Aquaculture%20Research%20Plan%20Progress%20Report.pdf) (accessed 2026-07-22): Minimal current precision-technology adoption, AI-aided vision results, and federal work on controls, robots, aquaponics, and seaweed farming systems.
- **S6** — [Strategic Plan for Aquaculture Economic Development (2023-2028)](https://www.ars.usda.gov/sca/Task%20Forces%20and%20Working%20Groups/Strategic%20Plan%20for%20Aquaculture%20Economic%20Development%282023%29.pdf) (accessed 2026-07-22): Federal priorities for technology adoption, automation commercialization, operator training, infrastructure, climate resilience, and aquaculture investment.
