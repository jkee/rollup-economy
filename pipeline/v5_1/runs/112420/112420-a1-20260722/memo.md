# 112420 — Goat Farming

*v5.1 Stage 1 research memo. Run `112420-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Persistent physical demand plus a digitizable monitoring and administrative layer could improve the economics of the small subset of scalable contract-oriented goat operators.
**Weakness:** The NAICS category primarily contains product farms, leaving very few clearly eligible recurring outsourced-service firms and no defensible LMM firm-count estimate.

## Business-model lens
- Included: US goat-raising establishments in the lower-middle-market band that earn recurring or repeat external-customer revenue through production-style contracts, recurring commercial offtake, or comparable repeat relationships for milk, meat, breeding stock, or fiber.
- Excluded: Hobby and subsistence farms, one-off livestock sales without a repeat customer relationship, captive processor-owned farms, shells, non-control financing vehicles, and standalone vegetation-management services whose primary activity is not raising goats.
- Customer and revenue model: Eligible operators receive production fees or recurring proceeds from processors, distributors, dairies, breeders, or other commercial buyers; the typical NAICS establishment instead sells livestock or animal products and therefore may not satisfy the outsourced-service lens.
- Deviation from default lens: none

## Executive view
Goat farming is fundamentally a physical animal-production activity, while the screen requires a recurring outsourced-service model. A small contract-style subset may qualify, but missing labor-share and firm-count inputs and the absence of goat-specific contracting data make the transferable opportunity highly uncertain.

## How AI changes the work
AI can assist herd monitoring, recordkeeping, production analysis, scheduling, feed and breeding decisions, compliance, and customer administration. It has much less direct reach into feeding, herding, cleaning, repairs, treatment, transport, and births; five-year implementation depends on economical goat-specific hardware and reliable data workflows.

## Value capture
Fixed production fees or agreed prices can let an operator retain savings during a contract period, but processors and repeat buyers can demand lower pricing or better service at renewal. Differentiated genetics and specialty dairy channels may retain more than commodity meat or concentrated-processor relationships.

## Firm availability
Most goat establishments likely fail the outsourced-service and LMM tests. General employer-business transfer intentions imply some five-year deal flow among eligible firms, but many farm transitions may be family gifts, closures, or asset sales rather than intact control transfers.

## Demand durability
US goat inventories rose modestly in the latest annual observation, including faster growth in milk goats, but inventory is an imperfect one-year proxy for five-year demand. Physical goat production should remain operator-required even as monitoring and administrative work become more software-enabled.

## Risks and uncertainty
The principal uncertainties are whether any meaningful LMM population truly earns outsourced-service revenue, missing frozen l and n inputs, weak goat-specific technology and contract evidence, heterogeneous end markets, biological and animal-welfare risk, buyer concentration, commodity prices, and the chance that operations transfer only as land and livestock assets.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.2 | 0.34 | 0.5 | PROXY | S2, S3 |
| rho | 0.22 | 0.38 | 0.55 | ESTIMATE | — |
| e | 0.02 | 0.08 | 0.18 | PROXY | S1, S4 |
| s5 | 0.12 | 0.22 | 0.32 | PROXY | S5 |
| q | 0.3 | 0.46 | 0.62 | PROXY | S4 |
| d5 | 0.97 | 1.1 | 1.25 | PROXY | S6 |
| o | 0.97 | 0.995 | 1 | ESTIMATE | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 6.00 | 9.20 | 10.00 | PROXY |
| D | 9.41 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET pools multiple farm-animal industries and does not provide wage weights for goat farms.
- a: USDA precision-dairy evidence concerns cows and may not transfer economically or technically to smaller goat operations.
- a: The frozen compensation-to-receipts input is missing, limiting interpretation of the labor opportunity.
- rho: No goat-specific adoption or implementation survey was located.
- rho: Implementation economics may differ sharply between dairy, meat, fiber, and breeding operations.
- rho: The estimate excludes pricing and demand effects.
- e: The contract statistic is for all farms, and goat-specific contract incidence was not reported.
- e: Marketing contracts govern product sales and are not automatically outsourced services.
- e: No defensible LMM firm-count input is available for this record.
- s5: Gallup measures intentions, not completed qualifying control transfers.
- s5: The survey covers employer businesses across industries, not goat farms or the LMM band.
- s5: Family gifts and public offerings in the survey do not all match the screen's transaction definition.
- q: No goat-specific contract terms or customer concentration data were found.
- q: Product-price volatility may dominate realized margins but is not itself part of q.
- q: The bounds apply only to implemented gross benefits and do not include volume changes.
- d5: The source reports inventory, not constant-price demand or eligible-service revenue.
- d5: Only a one-year change is used to inform a five-year horizon.
- d5: Aggregate US data conceal divergent dairy, meat, breeding, and fiber trends.
- o: The estimate assumes demand exists; demand quantity is handled separately in d5.
- o: Vertical integration could remove independent operators even if animal production continues.
- o: Standalone software may replace portions of management work without eliminating the operator.

## Sources
- **S1** — [NAICS 2022 Version 1.0 - 11242 - Goat farming - Industry](https://www23.statcan.gc.ca/imdb/p3VD.pl?CLV=4&CPV=11242&CST=27012022&CVD=1370274&Function=getVD&MLV=5&TVD=1369825) (accessed 2026-07-23): Defines the industry as establishments primarily engaged in raising goats and identifies code 112420; supports the lens and e rationale.
- **S2** — [45-2093.00 - Farmworkers, Farm, Ranch, and Aquacultural Animals](https://www.onetonline.org/link/summary/45-2093.00) (accessed 2026-07-23): Lists goat-inclusive animal-farm duties and work activities, including physical care, monitoring, records, analysis, scheduling, equipment, treatment, cleaning, and breeding; supports a and operator-required work.
- **S3** — [Precision Dairy Farming, Robotic Milking, and Profitability in the United States](https://ers.usda.gov/publications/113704) (accessed 2026-07-23): Documents sensors, data analytics, automation, robotic milking, and growing adoption in US cow dairies; supports the technology-direction proxy for a.
- **S4** — [Marketing and Production Contracts Are Widely Used in U.S. Agriculture](https://www.ers.usda.gov/amber-waves/2019/july/marketing-and-production-contracts-are-widely-used-in-u-s-agriculture) (accessed 2026-07-23): Reports agricultural contract prevalence and distinguishes price-and-delivery marketing contracts from fee-based production contracts; supports e and q.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Reports owner age and five-year sell-or-transfer intentions for US employer businesses; supports the s5 proxy.
- **S6** — [Goat Inventory, January 31, 2025](https://data.nass.usda.gov/Statistics_by_State/Regional_Office/Southern/includes/Publications/Livestock_Releases/Goat_Inventory/Goats2025.pdf) (accessed 2026-07-23): Reports 2.51 million US goats and kids on January 1, 2025, up 1 percent year over year, and 430,000 milk goats, up 4 percent; supports the d5 proxy.
