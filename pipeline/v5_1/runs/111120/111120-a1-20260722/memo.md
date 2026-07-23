# 111120 — Oilseed (except Soybean) Farming

*v5.1 Stage 1 research memo. Run `111120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Strong canola-oil demand and precision-agriculture tools can lift yield, input efficiency, and decision quality on scaled operations.
**Weakness:** Most output remains a seasonal commodity with biological risk, limited buyer choice, and little ability to retain broadly available technology gains.

## Business-model lens
- Included: Independent lower-middle-market farms growing canola or rapeseed, sunflower, flaxseed, mustard seed, safflower, and mixed non-soy oilseeds, emphasizing scaled field-crop operations, specialty varieties, identity-preserved or certified production, seed production, and repeat processor or buyer programs.
- Excluded: Soybean, peanut, and cotton farming; oilseed crushing and refining; farm-management and custom-application services classified elsewhere; hobby and lifestyle farms; vertically integrated processor-owned acreage; and farms outside the LMM earnings band.
- Customer and revenue model: Customers include crushers, vegetable-oil and biofuel processors, seed companies, food and bird-feed businesses, exporters, and commodity merchants. Revenue is primarily seasonal crop sales; the service-like subset uses pre-harvest marketing or production contracts, verified identity preservation, specified varieties and qualities, delivery schedules, and repeat processor relationships.
- Deviation from default lens: none

## Executive view
Minor oilseed farming offers moderate precision-agriculture leverage and a favorable current canola demand signal, but ordinary commodity farms have weak service characteristics and limited pricing power. The coherent target is a scaled operator with controlled acreage, modern equipment, storage, and repeat specialty, seed, or identity-preserved processor programs.

## How AI changes the work
Planning, scouting, prescriptions, guidance, yield forecasting, maintenance, marketing, compliance, and administration are the strongest use cases. Field operations and weather-critical execution remain physical, and value depends on integrating recommendations with machinery and agronomy.

## Value capture
Verified traits, specialty quality, seed programs, segregation, reliable delivery, and scarce local processing support premiums and retention. Commodity benchmarks, concentrated buyers, crop switching, and input suppliers constrain capture.

## Firm availability
There is no defensible frozen firm count. Transferability depends on land control, leases, water, equipment, storage, operator succession, working capital, debt, crop insurance, and continuity of specialty contracts; many farm sales are asset transactions rather than acquisitions of a recurring enterprise.

## Demand durability
USDA projects record canola production and crush on strong oil demand, while food, renewable fuel, feed, and specialty uses broaden the base. The combined industry is heterogeneous, and sunflower or smaller crops can diverge sharply as acreage and processing economics change.

## Risks and uncertainty
Major uncertainties include missing labor-share and firm-count inputs, acreage and crop mix, weather, yield, input inflation, processor access, buyer concentration, policy, crop insurance, land rents, machinery capex, contract prevalence, premium durability, and adoption economics on minor crops.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.3 | 0.45 | 0.6 | PROXY | S1, S2, S3 |
| rho | 0.34 | 0.53 | 0.7 | ESTIMATE | S2, S3 |
| e | 0.12 | 0.24 | 0.38 | PROXY | S4, S5 |
| s5 | 0.08 | 0.17 | 0.26 | PROXY | S6 |
| q | 0.2 | 0.37 | 0.54 | PROXY | S4, S5 |
| d5 | 1.03 | 1.2 | 1.39 | PROXY | S7 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S1, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 4.00 | 7.40 | 10.00 | PROXY |
| D | 9.79 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Precision-agriculture studies emphasize larger corn, soybean, wheat, and cotton operations.
- a: Automated guidance is established automation rather than generative AI.
- a: Crop mix, acreage, climate, and ownership structure materially alter labor exposure.
- rho: USDA adoption evidence does not separately report these minor oilseeds.
- rho: Small farms adopt precision tools less readily than large crop farms.
- rho: Weather and biology can dominate modeled recommendations.
- e: General crop-contract evidence is not oilseed-specific.
- e: Marketing contracts manage sale terms but do not necessarily create deep service relationships.
- e: Certification raises differentiation but also segregation and recordkeeping costs.
- s5: The dataset intentionally provides no n-band estimate.
- s5: Cross-industry intentions are not observed farm transactions.
- s5: Land value and operating-business value often transact separately.
- q: Premiums can disappear when specialty supply expands.
- q: Processors may specify technology and capture the benefit through contract terms.
- q: Commodity basis and freight can outweigh small productivity improvements.
- d5: One marketing-year canola outlook is not a five-year industry forecast.
- d5: Record production can lower farm prices if demand lags.
- d5: Canola strength may not extend to all non-soy oilseeds.
- o: The factor isolates AI-specific obsolescence from ordinary crop substitution.
- o: Biofuel policy changes are captured primarily in demand.
- o: Individual specialty varieties can lose market relevance quickly.

## Sources
- **S1** — [NAICS 111120 - Oilseed (except Soybean) Farming](https://www23.statcan.gc.ca/imdb/p3VD.pl?CLV=2&CPV=111120&CST=27012022&CVD=1370970&Function=getVD&MLV=6&TVD=1383176&wbdisable=true) (accessed 2026-07-22): Industry boundary and examples covering canola or rapeseed, flaxseed, mixed oilseeds, mustard, safflower, and sunflower, with soybean excluded.
- **S2** — [Agricultural Equipment Operators](https://www.onetonline.org/link/details/45-2091.00) (accessed 2026-07-22): Direct field-crop task evidence for equipment operation, loading, input mixing, planting and spraying, harvesting, post-harvest work, and farm-management and mapping software.
- **S3** — [Precision Agriculture in the Digital Era](https://www.ers.usda.gov/publications/105893) (accessed 2026-07-22): USDA evidence on digital maps, variable-rate technology, automated guidance, adoption by crop, labor-saving benefits, productivity, pricing, soil variability, programs, and consultant access.
- **S4** — [Marketing and Production Contracts Are Widely Used in U.S. Agriculture](https://www.ers.usda.gov/amber-waves/2019/july/marketing-and-production-contracts-are-widely-used-in-u-s-agriculture) (accessed 2026-07-22): Cross-crop contract prevalence and mechanisms covering prices, qualities, quantities, delivery, higher-quality compensation, assured outlets, production guidance, and contract fees.
- **S5** — [USDA Identity Preservation Program](https://www.ams.usda.gov/services/auditing/identity-preservation) (accessed 2026-07-22): Verification framework for segregation, traceability, quality management, and testing from seed through production, processing, and distribution.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry owner-age and five-year sale, transfer, closure, and succession-intention evidence.
- **S7** — [USDA Soybeans and Oil Crops Market Outlook, July 2026](https://www.ers.usda.gov/topics/crops/soybeans-and-oil-crops/market-outlook) (accessed 2026-07-22): Current canola acreage, production, crush, imports, exports, stocks, price, and oil-demand outlook for marketing year 2026/27.
