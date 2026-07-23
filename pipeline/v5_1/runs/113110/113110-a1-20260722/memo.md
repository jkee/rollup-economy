# 113110 — Timber Tract Operations

*v5.1 Stage 1 research memo. Run `113110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.96 · L 0.70 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Geospatial AI and inventory analytics can improve management of a renewable resource with recurring stewardship needs.
**Weakness:** Only a handful of eligible operators may exist, and value is often dominated by land and timber prices rather than transferable service operations.

## Business-model lens
- Included: Independent U.S. operators managing timber tracts to grow and sell standing timber, including inventory, silvicultural planning, road and access coordination, reforestation, fire and pest management, harvest-sale administration, and landowner reporting.
- Excluded: Passive land lessors; logging contractors that cut or haul timber; forest nurseries; short-rotation woody crop farms; captive internal forestry departments; pure timberland investment vehicles without operating control; and firms outside the target EBITDA band.
- Customer and revenue model: Repeated timber-sale and tract-management activity serving external mills, loggers, landowners, or timber buyers, screened for transferable operating firms plausibly generating $1-10 million normalized EBITDA.
- Deviation from default lens: none

## Executive view
Timber-tract operations combine renewable biological assets and recurring stewardship with commodity and housing cycles. AI can improve inventory, mapping, and administration, but the addressable firm universe is very small and much of the sector is land- or investment-vehicle economics rather than an outsourced operating platform.

## How AI changes the work
AI can assist satellite and LiDAR interpretation, stand inventory, growth and yield modeling, harvest scheduling, road planning, document preparation, certification records, sale marketing, and pest or fire detection. Field verification, boundary work, silviculture, access coordination, and accountable stewardship remain operator tasks.

## Value capture
Commodity stumpage pricing and mill buyer power limit retention. Operators with superior inventory, certification, regional scale, long landowner relationships, flexible harvest timing, and high-quality management contracts can keep more benefit.

## Firm availability
The frozen estimate is only ten firms and requires careful validation. Passive landholders, REIT-like vehicles, captive forestry operations, and land-only entities must be excluded; a land-rich business can also have economics unlike a service roll-up.

## Demand durability
Standing timber is renewable and serves construction, repair, panels, packaging, pulp, exports, and energy. Housing is currently soft and regional mill capacity matters, but diversified end uses and long rotations support a broad stable-demand case.

## Risks and uncertainty
Key risks are tiny firm availability, stumpage and housing cycles, mill closures, fire, storm, pests, climate, long biological duration, land concentration, environmental regulation, and confusing asset appreciation with operating performance.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1376 | — | OBSERVED | — |
| n | — | 10 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.34 | PROXY | S1, S2 |
| rho | 0.38 | 0.55 | 0.7 | ESTIMATE | S2 |
| e | 0.34 | 0.52 | 0.7 | ESTIMATE | S1 |
| s5 | 0.08 | 0.18 | 0.31 | ESTIMATE | — |
| q | 0.25 | 0.43 | 0.61 | ESTIMATE | S1, S3 |
| d5 | 0.84 | 1 | 1.17 | PROXY | S3, S4 |
| o | 0.87 | 0.95 | 0.99 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.29 | 0.70 | 1.31 | ESTIMATE |
| F | 0.39 | 1.06 | 1.86 | ESTIMATE |
| C | 5.00 | 8.60 | 10.00 | ESTIMATE |
| D | 7.31 | 9.50 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation proxy is broader than 113110 and dated 2018.
- a: Employment shares are not wage-weighted not-yet-automated task shares.
- rho: Operators with standardized plantations and high-quality LiDAR data should implement faster than mixed small tracts.
- e: The frozen count is margin-bridged from a farming margin and may not reflect land-heavy timber economics.
- s5: No observed control-transfer rate specific to eligible timber-tract operators was found.
- q: Fee-management operations retain differently from operators bearing biological and stumpage-price risk.
- d5: The long-run Forest Service projection is old and model-dependent.
- d5: National housing starts do not directly measure standing-timber demand.
- o: Automation within the operator changes labor needs but should not be counted as operator displacement.

## Sources
- **S1** — [NAICS Definition: Timber Tract Operations](https://www.census.gov/naics/?details=11&input=11&year=2017) (accessed 2026-07-22): Census defines 113110 as operating timber tracts to sell standing timber and distinguishes it from passive land lessors, short-rotation crops, and logging contractors.
- **S2** — [May 2018 National Industry-Specific Occupational Employment and Wage Estimates: Forestry and Logging](https://www.bls.gov/oes/2018/May/naics3_113000.htm) (accessed 2026-07-22): In the broader forestry-and-logging industry, forest, conservation, and logging workers represented 55.39% of employment, grounding the physical-task proxy.
- **S3** — [Monthly New Residential Construction, May 2026](https://www.census.gov/construction/nrc/current/) (accessed 2026-07-22): Census reports May 2026 housing starts at a 1.177 million seasonally adjusted annual rate, 8.7% below May 2025, illustrating current construction-cycle weakness.
- **S4** — [Global Context for the United States Forest Sector in 2030](https://research.fs.usda.gov/treesearch/download/21081.pdf) (accessed 2026-07-22): Forest Service modeling projected U.S. industrial roundwood harvests exceeding domestic consumption and industrial roundwood exports increasing through 2030.
