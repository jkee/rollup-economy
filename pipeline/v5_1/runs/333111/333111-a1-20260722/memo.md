# 333111 — Farm Machinery and Equipment Manufacturing

*v5.1 Stage 1 research memo. Run `333111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.63 · L 0.56 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large installed base and repeat dealer, parts, engineering, and support workflows create durable relationships and automatable knowledge work.
**Weakness:** Cyclical capital spending and production-heavy operations constrain realized labor savings and demand visibility.

## Business-model lens
- Included: Independent LMM manufacturers of farm, agricultural, turf, and grounds-care machinery, implements, attachments, replacement assemblies, and repeat engineered equipment sold to external dealers, farms, landscapers, or OEMs.
- Excluded: Captive production, dealerships without manufacturing, repair-only businesses, financing vehicles, shell entities, and firms outside the EBITDA band.
- Customer and revenue model: Repeat B2B equipment and parts sales through dealers, OEM programs, direct farm accounts, and replacement cycles, with engineering, configuration, warranty, parts, and technical support.
- Deviation from default lens: none

## Executive view
Farm machinery offers repeat equipment, parts, and dealer workflows with meaningful knowledge-work automation, but physical assembly limits exposed labor and agricultural cyclicality dominates near-term demand.

## How AI changes the work
Likely uses include configuration and quoting, engineering search and change documentation, work instructions, dealer and warranty support, parts identification and forecasting, scheduling, and procurement. Welding, machining, assembly, painting, inspection, field testing, and repair remain physical.

## Value capture
Installed-base parts, product differentiation, compatibility, and dealer relationships preserve part of the benefit. Dealer margins, farmer price sensitivity, OEM cost-downs, competitive bids, and cycle-driven discounting share savings.

## Firm availability
A sizeable estimated LMM population exists, though eligibility falls with captive ownership, dealership-heavy models, low repeatability, single-product dependence, weak aftermarket revenue, and concentrated OEM accounts.

## Demand durability
Agricultural machinery is essential physical capital, but purchases can be deferred when farm income weakens. Replacement age, labor scarcity, precision technology, and eventual cycle normalization support recovery over five years.

## Risks and uncertainty
Farm-income and commodity cycles, tariffs, dealer inventory, customer financing, product liability, seasonal working capital, warranty reserves, parts availability, and actual independent-firm counts drive uncertainty.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.124 | — | OBSERVED | — |
| n | — | 233 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.3 | PROXY | S1, S2, S3 |
| rho | 0.39 | 0.56 | 0.72 | ESTIMATE | S1, S2 |
| e | 0.56 | 0.72 | 0.85 | ESTIMATE | S1, S6 |
| s5 | 0.14 | 0.24 | 0.35 | PROXY | S5 |
| q | 0.48 | 0.64 | 0.79 | ESTIMATE | S1 |
| d5 | 0.91 | 1.06 | 1.22 | PROXY | S2, S4 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.23 | 0.56 | 1.07 | ESTIMATE |
| F | 4.76 | 5.98 | 6.84 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.19 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Broad machinery occupation proxy.
- a: OEM sophistication and plant automation vary widely.
- rho: No observed code-specific implementation rate.
- rho: Safety-critical outputs need qualified review.
- e: Injected firm count is margin-bridged and estimated.
- e: Industry classification does not establish recurring outsourced economics.
- s5: Economy-wide demographic proxy.
- s5: No public code-specific transfer denominator.
- q: No public contract evidence measures pass-through.
- q: Aftermarket parts and proprietary attachments likely retain more than build-to-print components.
- d5: Farm income is a demand driver, not equipment quantity.
- d5: Large-crop, livestock, specialty-crop, and turf equipment cycles differ.
- o: Operator share can migrate to large OEMs or foreign suppliers.
- o: This is distinct from labor automation within the manufacturer.

## Sources
- **S1** — [2022 NAICS Definition: Farm Machinery and Equipment Manufacturing](https://www.census.gov/naics/?details=333&input=333&year=2022) (accessed 2026-07-22): Census defines 333111 as manufacturing agricultural and farm machinery and other turf and grounds-care equipment, including planting, harvesting, and mowing equipment.
- **S2** — [Industrial Production: Farm Machinery and Equipment (NAICS 333111)](https://fred.stlouisfed.org/series/IPG333111A) (accessed 2026-07-22): Federal Reserve/FRED provides a direct six-digit industrial-production series for farm machinery, supporting the cyclical demand evidence route.
- **S3** — [Assemblers and Fabricators](https://www.bls.gov/ooh/production/assemblers-and-fabricators.htm) (accessed 2026-07-22): BLS describes physical assembly work and reports machinery manufacturing as 10% of assembler and fabricator employment in the displayed profile.
- **S4** — [USDA Farm Sector Income Forecast](https://ers.usda.gov/topics/farm-economy/farm-sector-income-finances/farm-sector-income-forecast) (accessed 2026-07-22): USDA forecasts inflation-adjusted 2026 net farm income to decline $4.1 billion, or 2.6%, from 2025, supporting current demand-cycle pressure.
- **S5** — [2024 Chartbook on Firms by Age of Primary Owner](https://www.fedsmallbusiness.org/-/media/project/smallbizcredittenant/fedsmallbusinesssite/fedsmallbusiness/files/2024/firms-in-focus/sbcs_chartbook2024_ownerage.pdf) (accessed 2026-07-22): Federal Reserve chartbook provides small-business owner-age evidence used only as a succession proxy.
- **S6** — [2022 Economic Census Coverage for Farm Machinery](https://bhs.econ.census.gov/ombpdfs2022/export/2022_MC-33310_su.pdf) (accessed 2026-07-22): Census identifies farm machinery and equipment manufacturing, including planting, harvesting, and non-lawn-and-garden mowing equipment, supporting product scope.
