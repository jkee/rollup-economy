# 115112 — Soil Preparation, Planting, and Cultivating

*v5.1 Stage 1 research memo. Run `115112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.71 · L 3.29 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Contractors can spread expensive precision equipment and supervisory technology across many customer acres during labor-constrained seasonal windows.
**Weakness:** Large farms can use the same automation to self-perform, while transparent per-acre pricing and local competition constrain durable retention.

## Business-model lens
- Included: US lower-middle-market contractors that repeatedly provide soil preparation, plowing, seedbed preparation, fertilizing, seeding, planting, transplanting, thinning, pollinating, cultivating, crop spraying, and weed or pest-control field services to external farms while retaining accountable responsibility for equipment, operators, scheduling, application accuracy, safety, compliance, and job completion.
- Excluded: Shells, captive internal farm units, non-control financing vehicles, passive equipment lessors without accountable operations, crop harvesting, postharvest services, farm-labor contractors, full farm-management services, input retail without field application, farms self-performing work, firms outside the screened EBITDA band, and operations that lack recurring external customers are excluded.
- Customer and revenue model: Customers are crop farms, landowners, farm managers, cooperatives, and agribusinesses that outsource equipment-intensive field passes. Revenue is commonly charged per acre, per hour, per job, or by application volume, with materials sometimes billed separately; repeat demand follows planting, tillage, fertilizer, spraying, and cultivation calendars.
- Deviation from default lens: none

## Executive view
This is a recurring outsourced-service industry with a clear customer problem: farms need timely, equipment-intensive field work during narrow agronomic and weather windows. Precision guidance already automates part of steering, and the next productivity layer is multi-machine supervision, routing, prescription execution, documentation, and administrative coordination. The main strategic tension is that the same technology can make a scaled contractor more efficient or enable a large farm to self-perform.

## How AI changes the work
AI and autonomy can reduce continuous in-cab attention, optimize paths and input rates, coordinate machines, detect skips and overlaps, schedule around weather, generate records, quote jobs, dispatch crews, and manage customer communication. Operators remain needed for transport, setup, refilling, calibration, obstacles, repairs, chemical handling, exceptions, and accountable completion. Existing auto-steer is a baseline capability, not a new labor opportunity.

## Value capture
Per-acre and per-job pricing permits near-term retention when an operator lowers labor, overlap, fuel, or rework. Timeliness, scarce capacity, precision, and trustworthy records support differentiation. Transparent extension rate surveys, annual price resets, neighboring contractors, customer equipment economics, and bidding limit durable capture, so contract and renewal evidence matters.

## Firm availability
Most active firms in the EBITDA band should fit the external-service lens, though farm-affiliated side businesses, mixed NAICS activity, passive rental, and material sales require screening. The estimated firm count suggests a meaningful but not directly observed population. Succession may occur through family transfer or equipment auctions rather than acquisition of a customer-bearing operating company.

## Demand durability
Planted land requires recurring field operations, and broad agricultural-service reliance has grown over time. Farm and harvested-acre counts have declined, but larger farm scale, expensive specialized machinery, labor scarcity, cover crops, precision requirements, and additional service content can sustain outsourcing. Reduced tillage, drought, consolidation, bundled input application, and customer insourcing are the principal offsets.

## Risks and uncertainty
Key risks are weather-compressed seasons, customer and regional concentration, equipment debt, utilization, fuel and repair costs, operator scarcity, chemical liability, drift, crop damage, autonomous-equipment safety, cyber and positioning failures, insurance, subscription dependence, and customer insourcing. Broad occupation and demand proxies also mix harvesting, labor contracting, and postharvest work outside this code.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3627 | — | OBSERVED | — |
| n | — | 126 | — | ESTIMATE | — |
| a | 0.26 | 0.42 | 0.58 | PROXY | S1, S2, S4, S5 |
| rho | 0.32 | 0.54 | 0.72 | PROXY | S4, S5 |
| e | 0.78 | 0.9 | 0.96 | ESTIMATE | S1, S3 |
| s5 | 0.17 | 0.28 | 0.4 | PROXY | S8 |
| q | 0.41 | 0.58 | 0.73 | PROXY | S6 |
| d5 | 0.93 | 0.99 | 1.08 | PROXY | S3, S7, S9 |
| o | 0.67 | 0.8 | 0.9 | ESTIMATE | S3, S4, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.21 | 3.29 | 6.06 | PROXY |
| F | 4.62 | 5.61 | 6.27 | ESTIMATE |
| C | 8.20 | 10.00 | 10.00 | PROXY |
| D | 6.23 | 7.92 | 9.72 | ESTIMATE |

## Caveats
- a: The occupation mix is for a broader four-digit industry dominated by crop laborers who may work outside this code.
- a: Guidance systems already automate steering on much row-crop acreage, so their existing benefit is excluded from remaining exposure.
- a: Exposure differs between row-crop ground work, specialty crops, aerial application, pollination, and labor-intensive transplanting or thinning.
- rho: Farm adoption statistics are not implementation rates among external contractors.
- rho: Near-total steering automation does not eliminate operators responsible for implements, roads, refills, obstacles, and failures.
- rho: Adoption is concentrated in larger row-crop operations and transfers less directly to small fields and specialty crops.
- e: Multi-service agricultural contractors can change NAICS classification as harvesting, labor, postharvest, or farm-management revenue changes.
- e: Some custom operations are side businesses of farms and may be captive in substance or lack separable financials.
- e: The provided firm count is margin-bridged and sensitive to the low assumed industry margin.
- s5: The Census age evidence is cross-industry, represents responding employer-business owners, and uses 2018 data.
- s5: Equipment and customer lists can transfer without acquisition of the legal operating company.
- s5: Owner age is not a direct measure of sale intent, timing, or control-transfer type.
- q: One regional survey cannot represent all crops, geographies, field sizes, equipment, or application risks.
- q: Published rates are self-reported and often exclude materials, while actual contracts may bundle them.
- q: Retention differs between commodity row-crop work, specialty crops, aerial spraying, and precision prescription services.
- d5: Long-run broad-sector receipt growth does not isolate soil preparation, planting, and cultivating.
- d5: National cropland can be stable while regional weather and crop shifts cause severe local demand volatility.
- d5: Constant-quality adjustment is difficult because precision documentation and variable-rate application add service content per acre.
- o: Technology can strengthen contractors through utilization scale or disintermediate them by making self-performance easier.
- o: The accountable operator may shift to an equipment dealer, input retailer, cooperative, or farm employee rather than disappear.
- o: Operator-required share varies by field size, local labor, customer capital, crop, and equipment specialization.

## Sources
- **S1** — [2022 Economic Census Classification Form: Agricultural Services](https://bhs.econ.census.gov/ombpdfs2022/export/2022_AG-11500_mu.pdf) (accessed 2026-07-22): Defines 115112 services as crop-production support including crop dusting and spraying, plowing, fertilizer application, seeding, planting, thinning, transplanting, pollinating, cultivating, and weed or pest control, while distinguishing adjacent support industries.
- **S2** — [May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates: NAICS 115100](https://www.bls.gov/oes/2023/may/naics4_115100.htm) (accessed 2026-07-22): Provides the broader support-activities occupation mix, including 67.20 percent farming occupations, 13.78 percent transportation and material moving, and detailed agricultural equipment operator, management, and office employment.
- **S3** — [The Growing Contribution of Support Services to U.S. Agricultural Production](https://www.ers.usda.gov/data-products/charts-of-note/109259) (accessed 2026-07-22): Reports increasing farm reliance on outside agricultural services and long-run inflation-adjusted receipt growth alongside fewer service establishments and fewer farms.
- **S4** — [Precision Agriculture Use Increases With Farm Size and Varies Widely by Technology](https://www.ers.usda.gov/data-products/charts-of-note/110550) (accessed 2026-07-22): Reports 2023 use of guidance auto-steering by 52 percent of midsize and 70 percent of large-scale crop farms, substantial mapping use, size-linked adoption, and labor-time savings as an adoption motive.
- **S5** — [Most Row Crop Acreage Managed Using Auto-Steer and Guidance Systems](https://www.ers.usda.gov/amber-waves/2023/april/most-row-crop-acreage-managed-using-auto-steer-and-guidance-systems) (accessed 2026-07-22): Documents guidance coverage of major row-crop acreage, automated steering for planting, tilling, fertilizing, and harvesting, reduced operator attention, input efficiency, adoption barriers, and connectivity needs.
- **S6** — [2025 Custom Work Charges in Maryland and Delaware](https://www.extension.umd.edu/resource/custom-work-charges-maryland-and-delaware-fs-683) (accessed 2026-07-22): Reports surveyed per-acre minimum, maximum, median, and average rates for plowing, disking, cultivating, field preparation, strip tillage, and planting, illustrating fixed job pricing and dispersion.
- **S7** — [2022 Census of Agriculture: Number of U.S. Farms Falls Below 2 Million](https://ers.usda.gov/data-products/charts-of-note/108629) (accessed 2026-07-22): Reports a 7 percent decline in farm count and a 2.2 percent decline in land in farms from 2017 to 2022, with average farm size increasing.
- **S8** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51 percent of responding US employer-business owners were at least age 55, based on the 2019 Annual Business Survey using 2018 data.
- **S9** — [2022 Census of Agriculture: Cover Crop Use Continues To Be Most Common in Eastern United States](https://ers.usda.gov/data-products/charts-of-note/108950) (accessed 2026-07-22): Reports that cover-crop acreage increased 17 percent from 2017 to 2022, evidence that service passes can change even when total cropland does not grow.
