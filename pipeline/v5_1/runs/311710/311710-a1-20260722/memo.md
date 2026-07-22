# 311710 — Seafood Product Preparation and Packaging

*v5.1 Stage 1 research memo. Run `311710-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.11 · L 1.03 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A directly observed manual cutting, packing, inspection, and material-handling workforce with emerging vision and robotics tools.
**Weakness:** Eligible domestic service volume is obscured by principal-account processing, offshore value addition, import dependence, and species-specific seasonality.

## Business-model lens
- Included: Lower-middle-market seafood processors and packagers that repeatedly provide custom, toll, contract, co-packing, freezing, filleting, cooking, smoking, canning, or packaging services to external harvesters, aquaculture producers, brands, cooperatives, importers, or distributors.
- Excluded: Processors principally buying catch and selling seafood on their own account, vertically integrated harvest-processing operations without material third-party service revenue, retail fish markets, shared kitchens below the EBITDA band, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring or seasonal repeat processing for external product owners, generally billed per pound, per lot, per case, or under negotiated toll/co-packing agreements, with added charges for storage, packaging, labeling, certification, and specialty processes.
- Deviation from default lens: The lens is narrowed because NAICS 311710 combines external custom/toll processors with principal-account seafood manufacturers and integrated harvesters; their eligibility and benefit-retention mechanics differ materially.

## Executive view
Seafood preparation has a large manual cutting, packing, and material-handling base and credible machine-vision applications. The coherent roll-up lens is narrower: recurring custom, toll, and co-pack processors serving external product owners, not every company that buys catch and sells finished seafood.

## How AI changes the work
AI can improve species and freshness verification, inspection, traceability, HACCP documentation, production planning, inventory, and yield decisions, while vision-guided robotics can address loading and selected handling. Species variability, delicate products, wet washdown environments, sanitation, short seasons, and yield sensitivity slow physical automation.

## Value capture
Unit and batch toll fees allow initial retention through lower labor, spoilage, waste, and downtime. Over time, brand customers can re-bid work or demand better pricing, and offshore processors create alternatives; scarce permits, certifications, regional capacity, and switching risk preserve some benefit.

## Firm availability
Custom processing exists across regional fisheries and small aquaculture markets, but the share of LMM firms earning material third-party service revenue is not published. Transfer supply is also uncertain because permits, quota access, vessels, waterfront plants, and operating companies may be owned and transferred separately.

## Demand durability
Seafood consumption and aquaculture are expected to grow modestly, but U.S. import reliance means domestic processing does not move one-for-one with consumption. Catch limits, climate shifts, disease, trade policy, currency, and offshore value-added capacity can create sharp species- and region-specific swings.

## Risks and uncertainty
The biggest gaps are third-party revenue share, automation performance across species, and qualifying transfer rates. Food-safety failure, spoilage, quota loss, raw-material shortages, seasonal labor, cold-storage costs, wastewater, customer concentration, imports, and working-capital volatility can erase savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1658 | — | OBSERVED | — |
| n | — | 114 | — | ESTIMATE | — |
| a | 0.28 | 0.41 | 0.55 | PROXY | S1, S2, S3 |
| rho | 0.22 | 0.38 | 0.55 | PROXY | S2, S3, S4 |
| e | 0.18 | 0.32 | 0.5 | PROXY | S7, S8, S9 |
| s5 | 0.12 | 0.2 | 0.3 | ESTIMATE | — |
| q | 0.4 | 0.6 | 0.78 | ESTIMATE | S5, S7, S9 |
| d5 | 0.96 | 1.04 | 1.12 | PROXY | S5, S6 |
| o | 0.9 | 0.97 | 0.995 | PROXY | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.41 | 1.03 | 2.01 | PROXY |
| F | 2.00 | 3.40 | 4.66 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.64 | 10.00 | 10.00 | PROXY |

## Caveats
- a: OEWS reports employment rather than task time or wage-weighted exposure.
- a: Technology demonstrations do not establish applicability across the industry's many species, sizes, and product forms.
- rho: One USDA example focuses on blue crab loading and one NOAA device remains under commercial development.
- rho: Seasonal plants can have attractive hourly savings but weak annual payback.
- e: The NOAA custom-processing evidence is specific to Alaska crab fisheries.
- e: NOAA processor data are comprehensive for quantity, value, and employment but do not publish the revenue-model split needed here.
- s5: No industry-specific qualifying-transfer rate was found.
- s5: Permit, vessel, quota, facility, and operating-company transfers can occur separately and may not constitute a qualifying control sale.
- q: Public sources establish processing models and market structure but do not reveal commercial toll-price terms.
- q: Raw-material price, catch volume, exchange rates, and spoilage can dominate measured margin changes.
- d5: Global and Americas projections are imperfect proxies for U.S. LMM processors.
- d5: Import reliance can support domestic handling or displace domestic preparation depending on product form.
- o: Operator-required demand can persist while migrating outside the eligible U.S. independent-processor lens.
- o: HACCP obligations vary by product hazard and do not require every process to be manual.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311700](https://www.bls.gov/oes/2023/May/naics4_311700.htm) (accessed 2026-07-22): Industry-direct employment mix: production 51.76%, cutters/trimmers 29.31%, transportation/material moving 19.99%, hand packers 9.24%, and inspectors/testers 2.60%.
- **S2** — [Labor and Process Efficiency Through Autonomous Machine Vision Guided Robotic Loading on Food Manufacturing Lines](https://www.nal.usda.gov/research-tools/food-safety-research-projects/labor-and-process-efficiency-through-autonomous) (accessed 2026-07-22): USDA project uses blue crab processing to demonstrate 3D vision, deep-learning morphology recognition, robotic picking, orientation, and real-world line testing.
- **S3** — [Next-Gen AI-Driven Multimode Spectroscopy: Transforming Seafood Quality, Purity, and Traceability](https://techpartnerships.noaa.gov/next-gen-ai-driven-multimode-spectroscopy/) (accessed 2026-07-22): NOAA describes AI species identification, freshness estimation, inventory, fraud reduction, and digital traceability, including 95%+ identification accuracy and freshness within one day.
- **S4** — [Guidance on Inspection and Seafood HACCP Records](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-industry-refusal-inspection-or-access-haccp-records-pertaining-safe-and-sanitary-processing) (accessed 2026-07-22): FDA requires seafood processors to establish critical control points, monitor them, keep records, maintain written HACCP plans, and provide records during plant inspection.
- **S5** — [Fisheries of the United States](https://www.fisheries.noaa.gov/national/sustainable-fisheries/fisheries-united-states) (accessed 2026-07-22): NOAA reports 2023 U.S. seafood consumption of 19.1 pounds per capita, estimated 80% import reliance, 6.3 billion pounds imported, and $12 billion in domestic edible processed fishery products.
- **S6** — [OECD-FAO Agricultural Outlook 2026-2035: Fish and Other Aquatic Products](https://www.oecd.org/en/publications/oecd-fao-agricultural-outlook-2026-2035_47874669-en/full-report/fish-and-other-aquatic-products-for-human-consumption_be23d26b.html) (accessed 2026-07-22): Projects global aquatic-food demand up 12%, Americas imports up 9%, global production up 11%, and real traded-fish prices down 22% by 2035 versus the 2023-2025 base.
- **S7** — [Analysis of Custom Processing in Bering Sea and Aleutian Islands Crab Fisheries](https://www.fisheries.noaa.gov/resource/document/rir-and-frfa-provision-exempting-certain-custom-processing-use-caps-processor) (accessed 2026-07-22): NOAA regulatory analysis confirms a distinct custom-processing model within seafood processing and its interaction with processor shares and regional delivery requirements.
- **S8** — [Seafood Processor Survey](https://www.fisheries.noaa.gov/national/socioeconomics/seafood-processor-survey) (accessed 2026-07-22): NOAA describes its annual comprehensive survey of U.S. seafood processors covering all plant sizes, product quantities, values, product types, and monthly employment.
- **S9** — [Handbook on Processing Fish for Small-Scale Fish Farmers](https://extension.purdue.edu/extmedia/FNR/FNR-637-W.pdf) (accessed 2026-07-22): USDA-funded Sea Grant handbook documents rented shared-use processing facilities for external fish farmers, client-specific products, value-added services, and associated food-safety and traceability requirements.
