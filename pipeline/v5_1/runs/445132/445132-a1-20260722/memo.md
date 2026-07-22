# 445132 — Vending Machine Operators

*v5.1 Stage 1 research memo. Run `445132-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Recurring external-location relationships combine scalable route data with physical replenishment that preserves accountable operator demand.
**Weakness:** Most remaining labor is physical, while high existing adoption of cashless and vending-management technology reduces the genuinely incremental automation pool.

## Business-model lens
- Included: Lower-middle-market U.S. vending-machine operators that repeatedly place, stock, merchandise, collect from, monitor, and service machines at external customer locations under route or location relationships.
- Excluded: Captive in-house vending operations; machine manufacturers or one-time equipment sellers; amusement, gambling, personal-service, and DVD machines classified elsewhere; passive machine financiers; shells; and firms outside the normalized EBITDA band.
- Customer and revenue model: Operators earn merchandise gross margin from repeated end-user purchases and commonly secure continuing access to workplaces, factories, schools, healthcare, hospitality, residential, or public locations through service agreements or location commissions; route density and replenishment quality drive economics.
- Deviation from default lens: none

## Executive view
Vending is a coherent recurring outsourced-service model: operators repeatedly stock and service unattended retail at customer locations. AI opportunity is meaningful in planning and information work but bounded because point-of-sale is already automated and the remaining route is heavily physical.

## How AI changes the work
AI can improve demand forecasting, assortment, dynamic routing, pre-kitting, warehouse picks, fault triage, settlement, pricing, sales proposals, and customer communications. Filling, loading, driving, cleaning, installation, food handling, and many repairs still require people and equipment.

## Value capture
Operators can retain savings through controlled machine pricing and denser routes, but competitive location bids and commissions share benefits with hosts and users. Capture is strongest where service reliability, data, exclusive access, and route density matter more than the highest commission.

## Firm availability
The route model is transferable and survey evidence shows substantial route buying and selling, while broad owner aging supports succession. Whole-company control transfers are less common than route-part trades, and the missing LMM firm count prevents a defensible opportunity count.

## Demand durability
Industry evidence shows post-pandemic recovery, more machines on location, and expansion beyond offices. Moderate real growth is plausible, but hybrid work, machine-to-micro-market conversion, product inflation, nutrition shifts, and host self-service widen the range.

## Risks and uncertainty
Major risks are already-automated baseline work, legacy connectivity, thin margins, fuel and card fees, theft, spoilage, route concentration, client rebids, office attendance, equipment capital, and survey evidence that blends adjacent formats. Direct operator task and transaction data are the most important next diligence inputs.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1295 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.12 | 0.22 | 0.34 | PROXY | S2, S3, S4 |
| rho | 0.48 | 0.65 | 0.8 | ESTIMATE | S3, S4 |
| e | 0.65 | 0.82 | 0.94 | ESTIMATE | S1, S3 |
| s5 | 0.14 | 0.24 | 0.36 | PROXY | S3, S6 |
| q | 0.38 | 0.58 | 0.75 | ESTIMATE | S1, S4 |
| d5 | 0.95 | 1.1 | 1.28 | PROXY | S4, S5 |
| o | 0.78 | 0.9 | 0.97 | ESTIMATE | S1, S2, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.30 | 0.74 | 1.41 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.41 | 9.90 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET combines vending with coin and amusement-machine service roles and supplies task presence, not wage-weighted time shares.
- a: The occupation profile omits some warehouse, sales, and central-office roles.
- a: The frozen compensation ratio is from ancestor NAICS 4451 grocery and convenience retail and may not reflect route driving, technical service, and warehouse labor in vending.
- rho: This is implementation judgment rather than an observed five-year realization rate.
- rho: High VMS and cashless adoption means some readily captured benefits are already in the baseline.
- rho: New AI functionality may be limited by legacy machine connectivity and data ownership.
- e: No source directly measures eligibility under the normalized-EBITDA and transferability lens.
- e: Many survey respondents combine vending with micro markets, office coffee, pantry, or bottling.
- e: The frozen LMM firm-count input is missing, so the eligible-firm count cannot be calculated.
- s5: The operator survey is not a probability sample and combines vending with adjacent convenience services.
- s5: The owner-age evidence is all-industry, owner-level, and from data year 2018.
- s5: The evidence does not provide a unique eligible-firm denominator or isolate external control changes.
- q: No source directly measures AI-benefit pass-through in vending contracts.
- q: Retention varies with location exclusivity, route density, client subsidy, and whether end users or hosts bear price changes.
- q: The estimate excludes demand changes and implementation friction.
- d5: The sources mix vending with adjacent formats and report nominal revenue.
- d5: The NAMA forecast comes from an industry body and participating companies represent about 27 percent of industry activity.
- d5: Office attendance, product inflation, client subsidies, and conversion to micro markets can separate revenue from current-basket quantity.
- o: This is a bounded judgment rather than an observed operator-retention share.
- o: Technology can change the format from traditional vending to smart cooler or micro market without eliminating the convenience-services operator.
- o: The estimate concerns accountable operation, not preservation of route headcount or visit frequency.

## Sources
- **S1** — [2022 NAICS Definition: 445132 Vending Machine Operators](https://www.census.gov/naics/?details=445132&input=445132&year=2022) (accessed 2026-07-22): Defines the industry as establishments retailing merchandise through vending machines that they service and identifies excluded machine categories.
- **S2** — [O*NET OnLine: Coin, Vending, and Amusement Machine Servicers and Repairers](https://www.onetonline.org/link/summary/49-9091.00) (accessed 2026-07-22): Lists tasks including filling, inspection, testing, repair, maintenance records, transaction records, cash collection, settlement, service calls, transport, and installation.
- **S3** — [State of the Industry for Vending and Micro Market Report: 2022 Was a Year of Continued Recovery](https://www.vendingmarketwatch.com/reports/article/53063695/state-of-the-industry-for-vending-and-micro-market-report-2022-was-a-year-of-continued-recovery) (accessed 2026-07-22): Reports that 74 percent of respondents ran one to ten routes, almost half were acquiring or divesting routes or route parts, VMS use reached 77 percent, and remote data collection reached 47 percent in 2022.
- **S4** — [Technology and Convenience Fuel Growth: 2024 State of the Vending and Micro Market Industry](https://www.vendingmarketwatch.com/home/article/55295667/technology-and-convenience-fuel-growth-2024-state-of-the-vending-and-micro-market-industry) (accessed 2026-07-22): Reports 2.3 million vending machines on location in 2024, up 7 percent; 60 percent of operators increased locations; more than 70 percent of machines accepted cashless payments; and operator size and consolidation evidence.
- **S5** — [NAMA State of Convenience Services Report Release](https://www.globenewswire.com/news-release/2026/03/20/3259860/0/en/Report-Convenience-Services-Outpacing-Much-of-Foodservice-and-Shifting-Toward-Tech-Enabled-Health-Forward-Offerings.html) (accessed 2026-07-22): Reports $31.1 billion of broader convenience-services revenue in 2025, 8.1 percent average annual growth since 2023, vending as the largest business line, and a 6.5 percent annual growth forecast; participants represented about 27 percent of activity.
- **S6** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51 percent of responding owners of employer businesses were 55 or older, 43 percent were 35 to 54, and 6 percent were 34 or younger, based on the 2019 ABS with data year 2018.
