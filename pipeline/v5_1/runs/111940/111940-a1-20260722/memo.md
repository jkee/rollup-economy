# 111940 — Hay Farming

*v5.1 Stage 1 research memo. Run `111940-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Localized freight economics and quality-sensitive repeat demand can protect productivity gains while AI improves timing, sensing, equipment utilization, and labor efficiency.
**Weakness:** Missing labor and firm-count denominators, plus fragmented family and asset transfers, prevent a reliable estimate of actionable acquisition capacity.

## Business-model lens
- Included: US lower-middle-market independent commercial farms primarily growing hay, alfalfa, clover, or mixed hay and repeatedly selling baled, chopped, or otherwise harvested forage to external dairy, beef, equine, feed, export, or other customers.
- Excluded: Livestock farms growing forage mainly for captive use, grain-hay producers classified with grains, grass or hay seed farms, hobby farms, passive farmland landlords, custom hay contractors without crop ownership, shells, non-control financing vehicles, and farms outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: Recurring seasonal and annual forage sales by ton or bale, differentiated by species, cutting, moisture, protein, digestibility, bale form, certification, location, and delivery; transactions range from repeat direct relationships to brokered or spot sales.
- Deviation from default lens: none

## Executive view
Hay farming offers moderate AI opportunity in guidance, harvest timing, sensing, irrigation, and administration, with meaningful local value capture from freight and quality differentiation. Physical demand is durable but mature and heavily shaped by livestock cycles, drought, and captive forage. The acquisition screen is materially incomplete because both frozen l and n are missing, and farms often transfer through family, land, machinery, and leases rather than as intact operating companies.

## How AI changes the work
AI and connected equipment can improve mowing, conditioning, raking, baling, stacking, moisture and quality assessment, field scouting, irrigation, weather-window planning, maintenance, routing, recordkeeping, and sales. Broad crop farms show high guidance adoption, but hay-specific sensing commercialization has historically lagged because moisture measurement, low-input economics, and payback are difficult. Multiple cuttings and weather exposure make supervised autonomy more plausible than unattended operations within five years.

## Value capture
Hay's high freight burden, variable quality, timing sensitivity, and repeat regional relationships create more pricing texture than bulk grain. Reliable moisture, protein, bale form, delivery, and certification can protect savings. Retention is weaker in surplus regions or with concentrated dairy and feed buyers, while technology gains can be capitalized into land rent and machinery or software costs.

## Firm availability
No defensible LMM firm count is available. The industry likely contains external-sale specialists as well as captive, hobby, seasonal, and marginal operations, and the broader farm sector's 95% family ownership does not resolve them. Producer age supports succession activity, but USDA land-transfer plans show few acres offered to nonrelatives and many transitions occur through trusts, wills, gifts, or leases rather than a qualifying company sale.

## Demand durability
NASS reports 123.0 million tons of hay in 2025, up only 0.5%. Beef cow inventory was down 1% entering 2026, while dairy cows increased and longer-range USDA projections anticipate cattle recovery. Drought, pasture conditions, exports, ration costs, and regional livestock mix can create sharp local scarcity or surplus, but animal feeding keeps the physical five-year basket broadly stable.

## Risks and uncertainty
Key risks are missing l and n, drought and water rights, wildfire and weather, narrow harvest windows, quality loss and storage fires, land and machinery cost, fuel and fertilizer, livestock-cycle exposure, buyer concentration, imports or feed substitutes, and family succession complexity. Technology may not pay on small acreage and failures during cutting windows are costly. Most evidence covers all crop farms or national hay rather than six-digit LMM external sellers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.2 | 0.34 | 0.5 | PROXY | S2, S3 |
| rho | 0.28 | 0.47 | 0.65 | ESTIMATE | S2, S3 |
| e | 0.55 | 0.72 | 0.85 | ESTIMATE | S1, S6 |
| s5 | 0.08 | 0.15 | 0.25 | PROXY | S6, S7 |
| q | 0.38 | 0.58 | 0.76 | PROXY | S8 |
| d5 | 0.93 | 1.03 | 1.14 | PROXY | S4, S5, S9 |
| o | 0.96 | 0.99 | 0.999 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 7.60 | 10.00 | 10.00 | PROXY |
| D | 8.93 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The 2023 precision-adoption data are for broad crop-farm size groups, not NAICS 111940.
- a: The hay-specific sensing source is older research evidence and reports limited commercial implementation at that time.
- rho: Farm size strongly predicts technology uptake, but the LMM population's acreage and machinery age are not observed.
- rho: Weather and crop-condition variability make successful demonstrations an incomplete guide to commercial implementation.
- e: The frozen n is missing and must not be replaced with broader Census farm counts.
- e: USDA's 95% family-farm share covers all agriculture, not eligible LMM hay farms.
- s5: TOTAL measures acres and transfer methods, not closed business-control transactions.
- s5: Trusts, wills, gifts, leases, and gradual family succession may not qualify.
- q: The cited market report covers one drought-affected state and week rather than national LMM economics.
- q: No source directly observes AI-benefit sharing in hay sales.
- d5: National production includes hay grown for captive livestock use outside the lens.
- d5: Drought can simultaneously reduce supply, increase supplemental feeding, cause herd liquidation, and move prices, making tons and receipts diverge.
- o: The estimate separates operator necessity from employee labor intensity.
- o: Feed substitution affects demand quantity in d5; it should not be double counted as software displacement.

## Sources
- **S1** — [NAICS Sector 11 Definitions: 111940 Hay Farming](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-23): Official scope covering farms primarily growing hay, alfalfa, clover, or mixed hay and excluding grain hay and grass or hay seed.
- **S2** — [Precision agriculture use increases with farm size and varies widely by technology](https://www.ers.usda.gov/data-products/charts-of-note/110550) (accessed 2026-07-23): Broad crop-farm adoption proxy: in 2023 guidance autosteering was used by 52% of midsize and 70% of large-scale crop farms, with adoption motivated by yield, labor time, input cost, fatigue, and environmental benefits.
- **S3** — [Technology background and best practices: yield mapping in hay and forage](https://www.ars.usda.gov/research/publications/publication/?seqNo115=291357) (accessed 2026-07-23): Hay-specific technology proxy: yield and moisture sensing had been developed for windrowers, forage harvesters, and balers, but commercial adoption was constrained by cost, uncertain payback, and moisture-measurement difficulty.
- **S4** — [USDA NASS 2025 Annual Crop Production](https://data.nass.usda.gov/Newsroom/Executive_Briefings/2026/01-12-2026.pdf) (accessed 2026-07-23): National quantity evidence: 49.557 million hay acres yielded 123.031 million tons in 2025, with production up 0.5% from 2024.
- **S5** — [United States cattle inventory down slightly](https://www.nass.usda.gov/Newsroom/2026/01-30-2026.php) (accessed 2026-07-23): Near-term forage-demand proxy: 86.2 million cattle and calves as of January 1, 2026; beef cows were down 1% while milk cows increased to 9.57 million.
- **S6** — [USDA releases 2022 Census of Agriculture data](https://data.nass.usda.gov/Newsroom/2024/02-13-2024.php) (accessed 2026-07-23): Farm-structure proxy: 95% of US farms were family-owned and operated and the average producer age was 58.1.
- **S7** — [Most of the U.S. Rented Farmland is Owned by Non-Farmers](https://www.nass.usda.gov/Newsroom/2026/03-12-2026.php) (accessed 2026-07-23): Transfer proxy: about 43 million acres, roughly 5% of US farmland, are slated for ownership transfer by sale or gift within five years, including 23 million acres expected to sell to nonrelatives.
- **S8** — [USDA AMS Colorado Direct Hay Report for week ending April 24, 2026](https://mymarketnews.ams.usda.gov/filerepo/sites/default/files/2905/2026-04-20/1319719/ams_2905_00273.pdf) (accessed 2026-07-23): Localized commercial-structure proxy showing direct hay trade by type, bale, quality, use, and price, with demand and availability affected by drought and water constraints.
- **S9** — [Livestock Production Cycles Affect Long-Term Price Outlook for Cattle, Hogs, and Chickens](https://ers.usda.gov/amber-waves/2025/march/livestock-production-cycles-affect-long-term-price-outlook-for-cattle-hogs-and-chickens) (accessed 2026-07-23): Longer-term livestock proxy: cattle inventory is projected to recover from a multidecade low through 2033, while cattle production and prices remain cyclical.
