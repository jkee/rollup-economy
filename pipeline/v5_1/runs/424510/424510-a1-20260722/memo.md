# 424510 — Grain and Field Bean Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `424510-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.61 · L 0.06 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Physical custody, quality accountability, and transport coordination remain indispensable even as commercial workflows become more automated.
**Weakness:** Very low labor intensity and a large cooperative or captive footprint limit both savings and conventional acquisition availability.

## Business-model lens
- Included: Independently controllable merchant wholesalers repeatedly buying and reselling corn, soybeans, wheat, other grains, and field beans to external processors, exporters, feed users, and other trade customers, including country or terminal elevators operated primarily for wholesaling.
- Excluded: Farmer-member cooperatives not available for a conventional qualifying control sale, captive or vertically integrated units of large agribusinesses, pure brokers, standalone storage businesses not primarily wholesaling, farms, shells, non-control financing vehicles, and firms outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: Recurring commodity origination and resale earning merchandising or basis margins, often combined with receiving, weighing, grading coordination, drying, storage, blending, hedging, and loading services.
- Deviation from default lens: The default lens is narrowed to independently controllable merchant wholesalers because farmer-member cooperatives and captive agribusiness locations have governance and control-transfer mechanics that are not coherent with conventional firm acquisition; the operating activities remain otherwise unchanged.

## Executive view
Grain and field bean merchandising has durable physical and accountable operating functions, but payroll is already small relative to gross commodity receipts and much handling control is automated. AI can improve commercial and administrative workflows, while transparent commodity economics, cooperative ownership, and integrated competitors constrain both the target pool and retained benefit.

## How AI changes the work
AI can summarize markets, prepare bids and contracts, extract scale and grade documents, reconcile settlements, monitor exceptions, draft producer communications, and coordinate transport. Humans remain essential for hedge and credit authority, quality disputes, official processes, equipment and safety, relationship-based origination, and physical elevator operations.

## Value capture
Cost savings can support better basis bids, faster settlements, and fewer logistics errors, but competitive local bids and benchmarked commodity markets should return much of the gain to producers or buyers. Defensible retention depends on origination density, storage position, execution, and trusted relationships rather than software alone.

## Firm availability
The apparent LMM count overstates conventionally acquirable targets because farmer-owned cooperatives are numerous and major agribusinesses operate captive locations. Independents remain, but each target requires ownership, governance, origination, environmental, safety, working-capital, hedge-control, and asset-condition diligence.

## Demand durability
The service basket remains necessary as crops move from farms to domestic processors and export markets. USDA projects a stable-to-soft acreage base, so five-year quantity is closer to flat than structurally growing, with yields, trade, crushing, feed, and biofuel policy driving the outcome.

## Risks and uncertainty
The largest uncertainties are the independent share of the firm universe, whether the distributor EBITDA-margin bridge fits grain economics, task-level payroll exposure, and benefit pass-through through local basis competition. A target with weak hedge controls, obsolete assets, environmental liabilities, one processor outlet, poor origination density, or cooperative/captive governance could be unsuitable.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0119 | — | OBSERVED | — |
| n | — | 655 | — | ESTIMATE | — |
| a | 0.16 | 0.25 | 0.34 | PROXY | S1, S2, S3 |
| rho | 0.3 | 0.5 | 0.68 | ESTIMATE | S2, S3, S4 |
| e | 0.38 | 0.56 | 0.72 | ESTIMATE | S1, S5, S6 |
| s5 | 0.1 | 0.18 | 0.28 | PROXY | S7 |
| q | 0.18 | 0.32 | 0.5 | ESTIMATE | S6, S8 |
| d5 | 0.92 | 0.99 | 1.07 | PROXY | S4, S6 |
| o | 0.84 | 0.93 | 0.98 | ESTIMATE | S2, S3, S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.02 | 0.06 | 0.11 | ESTIMATE |
| F | 5.23 | 6.76 | 7.87 | ESTIMATE |
| C | 3.60 | 6.40 | 10.00 | ESTIMATE |
| D | 7.73 | 9.21 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source is secondary and covers all firm sizes.
- a: Occupation shares are headcount, not payroll, and do not isolate independent targets.
- a: The supplied compensation-to-receipts ratio uses gross commodity receipts, so even genuine labor savings are structurally small relative to sales.
- rho: No grain-merchant-specific five-year AI implementation study was found.
- rho: One harvest season is insufficient to assess reliability across commodity cycles.
- e: USDA counted 312 grain-and-oilseed cooperatives in 2024 but does not state their share of 424510 LMM firms.
- e: Some cooperatives can merge or sell assets even though ordinary third-party control acquisition is unavailable.
- e: The supplied firm count is an estimate based on a broad distributor margin bridge that may poorly represent thin-margin grain merchants.
- s5: The Gallup survey is not specific to grain merchants, rural firms, or the LMM band.
- s5: Survey intentions include transfers that may not qualify or close.
- q: No source directly measures AI-benefit pass-through in grain merchandising.
- q: Local storage scarcity and crop conditions can dominate pricing power.
- q: The estimate excludes volume effects and implementation difficulty.
- d5: Acreage is an imperfect proxy for handled volume.
- d5: Five-year outcomes are highly sensitive to weather, yields, trade policy, and biofuel demand.
- d5: The source includes cotton and rice in addition to the main 424510 crops.
- o: The necessary operator may be integrated, cooperative, or public rather than an independent LMM merchant.
- o: Official inspection is not required for every domestic movement, though measurement and quality control remain necessary.

## Sources
- **S1** — [Grain and Field Bean Merchant Wholesalers - Market Size, Financial Statistics, Industry Trends](https://www.pellresearch.com/grain-and-field-bean-merchant-wholesalers) (accessed 2026-07-22): Industry occupation mix: 16% office/administrative support, 9% sales, 6% management, 16% farming, 6% production, and 35% transportation/material moving; also identifies main product lines.
- **S2** — [Official Grain Inspection & Weighing System](https://www.ams.usda.gov/services/fgis/official-grain-inspection-weighing-system) (accessed 2026-07-22): Describes uniform official grain inspection and weighing, authorized service providers, official certificates, quality attributes, equipment verification, and appeal processes.
- **S3** — [Operation of a Bulk Weighing Scale](https://www.ams.usda.gov/resources/operation-bulk-weighing-scale) (accessed 2026-07-22): Shows that modern official loose-grain weighing uses load cells and a scale-control computer to automate gates, readings, tare, gross, and net weights.
- **S4** — [U.S. major field crop acreage projected to decline](https://www.ers.usda.gov/data-products/charts-of-note/114033) (accessed 2026-07-22): USDA projects eight-crop acreage down 2.4% from 2026/27 to 2035/36, with corn declining, soybeans easing after an initial rise, and wheat flat.
- **S5** — [USDA Ag Co-op Statistics](https://content.govdelivery.com/accounts/USDARD/bulletins/4033d4c) (accessed 2026-07-22): USDA counted 1,620 agricultural cooperatives in 2024, including 312 whose major commodity was grain and oilseeds; it describes member ownership, mergers, locations, and services.
- **S6** — [Transportation of U.S. Grains: A Modal Share Analysis](https://www.ams.usda.gov/services/transportation-analysis/modal) (accessed 2026-07-22): States that U.S. grain moves to domestic and foreign markets through truck, rail, and barge in a highly competitive transportation market.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 survey found 22% of employer-business owners planned to sell or transfer ownership within five years and separately measured closure and uncertainty.
- **S8** — [Wholesale and retail Producer Price Indexes: margin prices](https://www.bls.gov/opub/btn/volume-1/wholesale-and-retail-producer-price-indexes-margin-prices.htm) (accessed 2026-07-22): Explains that trade-industry output prices are margins received by wholesalers and retailers and illustrates their sensitivity to small selling-price changes.
- **S9** — [United States Warehouse Act](https://www.ams.usda.gov/rules-regulations/uswa) (accessed 2026-07-22): Explains federal licensing and standards for agricultural warehouse operators.
