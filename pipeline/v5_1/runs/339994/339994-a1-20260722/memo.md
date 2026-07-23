# 339994 — Broom, Brush, and Mop Manufacturing

*v5.1 Stage 1 research memo. Run `339994-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.90 · L 1.39 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring replenishment and repeat custom designs create reusable product, quote, and customer-history data across a long tail of professional applications.
**Weakness:** Commodity products and a low labor-cost share limit retained AI economics unless the target has defensible custom or specification-driven revenue.

## Business-model lens
- Included: U.S. lower-middle-market manufacturers of industrial, commercial, laboratory, medical, food-service, sanitation, and other professional brushes, brooms, mops, and related custom brushing or cleaning tools supplied repeatedly to external customers.
- Excluded: Consumer-only household brands, artist and cosmetic brush specialists, direct-to-consumer craft sellers, distributors without manufacturing, captive plants, and platform-scale manufacturers outside the lower middle market.
- Customer and revenue model: Revenue is recurring business-to-business supply through standard catalog replenishment, wholesale and private-label programs, specification-driven custom brushes, replacement tools, prototypes, and repeat production runs for industrial, institutional, healthcare, laboratory, and food-service customers.
- Deviation from default lens: The code combines commodity household cleaning products, artist and cosmetic tools, and highly engineered industrial or medical brushes with materially different pricing and demand. The lens is narrowed to professional B2B industrial and institutional products with repeat supply economics so one operating screen is coherent; the narrowing is based on business-model consistency, not attractiveness.

## Executive view
The professional B2B portion of this heterogeneous code has recurring consumables and custom application work around an irreducibly physical product. AI can improve quotation, product selection, order handling, and planning, but the low compensation intensity and production-heavy workflow bound the labor opportunity. Commercial quality depends on avoiding commodity-heavy household and janitorial exposure.

## How AI changes the work
AI can translate application requirements into candidate materials and geometries, retrieve prior designs, draft quotes and proofs, streamline order entry, forecast replenishment, and support scheduling and purchasing. Prototyping, tufting, winding, molding, trimming, assembly, inspection, and sanitation validation remain physical.

## Value capture
Custom industrial, laboratory, medical, and fast-turn products can retain benefit through application knowledge and specification fit. Standard brooms, mops, and brushes sold through wholesale or private-label procurement are more price transparent and should pass through more savings.

## Firm availability
The frozen estimate identifies 31 LMM firms, but the code spans consumer and professional product models and likely includes corporate plants. ABMA evidence of mature closely held manufacturers supports succession potential, yet a product and ownership map is still required.

## Demand durability
Professional cleaning and sanitation remain recurring needs, and BLS projects modest janitorial employment growth while CDC guidance reinforces healthcare cleaning practices. Industrial brushes also serve diverse processes, but imports, robotics, reusable tools, and manufacturing cycles temper the outlook.

## Risks and uncertainty
Key uncertainties are code heterogeneity, six-digit occupation and shipment data gaps, commodity exposure, retailer or distributor concentration, private-label rebids, imported bristles and finished goods, tariffs, resin and wire costs, product liability, sanitation standards, and customer-specific tooling.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1777 | — | OBSERVED | — |
| n | — | 31 | — | ESTIMATE | — |
| a | 0.21 | 0.32 | 0.43 | PROXY | S1, S2, S3, S4, S5 |
| rho | 0.4 | 0.61 | 0.78 | ESTIMATE | S3, S4, S5 |
| e | 0.34 | 0.51 | 0.68 | ESTIMATE | S1, S3, S4, S5, S6 |
| s5 | 0.1 | 0.19 | 0.3 | PROXY | S6, S7, S8 |
| q | 0.36 | 0.55 | 0.72 | PROXY | S3, S4, S5, S6 |
| d5 | 0.91 | 1.04 | 1.18 | PROXY | S3, S4, S5, S9, S10 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1, S3, S4, S5, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.60 | 1.39 | 2.38 | ESTIMATE |
| F | 1.16 | 2.23 | 3.20 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | PROXY |
| D | 8.55 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation mix is much broader than the six-digit industry.
- a: Custom industrial producers and commodity mop producers have different task mixes.
- rho: Benefits depend on digitized specifications, historical quotes, and material-performance data.
- rho: Food, laboratory, medical, and safety applications require accountable validation.
- e: The code does not publicly separate professional industrial products from consumer categories.
- e: The supplied firm count is an estimate and may include ineligible corporate establishments.
- s5: The ABMA membership extends beyond the exact U.S. six-digit lens and includes suppliers.
- s5: Broad sale data do not establish qualifying control transfers.
- q: Public manufacturer claims do not disclose realized pricing or contracts.
- q: Raw-material inflation can obscure productivity retention.
- d5: Cleaning-service employment is an indirect product-demand proxy.
- d5: Custom industrial brush demand can follow manufacturing cycles rather than cleaning demand.
- o: Robotic cleaning still consumes brushes, pads, and replacement tools but may change formats and volumes.
- o: Some application support and ordering can become self-service.

## Sources
- **S1** — [2022 NAICS definition: 339994 Broom, Brush, and Mop Manufacturing](https://www.census.gov/naics/?details=33&input=33&year=2022) (accessed 2026-07-23): Defines the industry as establishments primarily manufacturing brooms, mops, and brushes.
- **S2** — [May 2023 Occupational Employment and Wage Estimates: NAICS 339000 Miscellaneous Manufacturing](https://www.bls.gov/oes/2023/may/naics3_339000.htm) (accessed 2026-07-23): Provides the broad occupation mix used to proxy wage-weighted AI task exposure.
- **S3** — [Cocker-Weber Brush Company: Custom Industrial Brushes](https://www.cocker-weber.com/) (accessed 2026-07-23): Documents engineered and repaired brushes, exact specifications, diverse industrial applications, and customer productivity use cases.
- **S4** — [Gordon Brush: U.S. Wholesale Industrial Brush Manufacturer](https://www.gordonbrush.com/) (accessed 2026-07-23): Documents more than 17,000 specialty and industrial brushes, custom design, private labeling, rapid turnaround, and industry-specific technical resources.
- **S5** — [Justman Brush Company](https://www.justmanbrush.com/) (accessed 2026-07-23): Shows more than 2,500 standard and specialty brushes, custom design, U.S. production, and laboratory, medical, scientific, industrial, and food-service markets.
- **S6** — [American Brush Manufacturers Association](https://abma.org/) (accessed 2026-07-23): Documents a long-standing North American broom, brush, and mop manufacturing community, industry data programs, innovation, global competition, and a base of small and family-run companies.
- **S7** — [BizBuySell Manufacturing Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/manufacturing/) (accessed 2026-07-23): Provides broad manufacturing transaction benchmarks for 2021-2025, used only as a control-transfer proxy.
- **S8** — [2022 Annual Business Survey: Characteristics of Business Owners](https://www.census.gov/data/tables/2022/econ/abs/2022-abs-characteristics-of-owners.html) (accessed 2026-07-23): Provides economy-wide owner-age and ownership-characteristics tables used only as a succession proxy.
- **S9** — [BLS Occupational Outlook Handbook: Janitors and Building Cleaners](https://www.bls.gov/OOH/building-and-grounds-cleaning/janitors-and-building-cleaners.htm) (accessed 2026-07-23): Projects 2% employment growth from 2024 to 2034, 351,300 annual openings, and continuing need for clean and healthy spaces while noting high-tech methods may limit growth.
- **S10** — [CDC Recommendations for Environmental Infection Control in Health-Care Facilities](https://www.cdc.gov/infection-control/hcp/environmental-control/recommendations.html) (accessed 2026-07-23): Documents recurring environmental cleaning and disinfection practices, including explicit procedures for mops, cloths, surfaces, and medical equipment.
