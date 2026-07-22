# 333120 — Construction Machinery Manufacturing

*v5.1 Stage 1 research memo. Run `333120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.52 · L 0.74 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Installed-base, parts, dealer, and technical workflows pair recurring physical demand with automatable knowledge work.
**Weakness:** Heavy physical production and cyclical capital spending limit labor substitution and demand visibility.

## Business-model lens
- Included: Independent LMM manufacturers of construction, surface-mining, and logging machinery, attachments, wear parts, portable processing equipment, and repeat engineered assemblies sold to external dealers, contractors, mines, rental fleets, or OEMs.
- Excluded: Captive plants, dealerships and rental fleets without manufacturing, repair-only firms, financing vehicles, shells, and firms outside the EBITDA band.
- Customer and revenue model: Repeat equipment, attachment, wear-part, replacement, and OEM-program sales, supported by configuration, engineering, warranty, parts, field service, and dealer or fleet relationships.
- Deviation from default lens: none

## Executive view
Construction machinery combines durable physical demand, aftermarket relationships, and complex information workflows. AI can improve engineering, quoting, planning, and support, while fabrication and assembly cap labor substitution and end-market cycles shape demand.

## How AI changes the work
Likely applications include configuration and quoting, drawing and specification review, engineering search, work instructions, parts identification, dealer and warranty support, demand planning, procurement, and quality analysis. Welding, machining, assembly, painting, testing, inspection, maintenance, and field trials remain physical.

## Value capture
Qualification, uptime, safety, installed-base compatibility, proprietary designs, and parts availability support retention. OEM cost-downs, rental-fleet purchasing, dealer discounts, bids, and cyclical competition transmit savings.

## Firm availability
The estimated LMM population is meaningful, especially in attachments, wear parts, and niche systems. Eligibility falls with captive ownership, dealership-heavy models, one-off fabrication, customer concentration, weak aftermarket revenue, and product-liability exposure.

## Demand durability
Construction, infrastructure, quarrying, surface mining, logging, and replacement needs require physical equipment. Demand should remain durable but cyclical, with fleet utilization, interest rates, public spending, commodity capex, and exports driving variance.

## Risks and uncertainty
Main risks include construction and mining cycles, customer financing, tariffs and steel costs, rental-fleet capex, dealer inventory, warranty reserves, product liability, engineering key persons, and uncertainty in the estimated independent-firm universe.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1567 | — | OBSERVED | — |
| n | — | 163 | — | ESTIMATE | — |
| a | 0.13 | 0.21 | 0.32 | PROXY | S1, S2, S3 |
| rho | 0.39 | 0.56 | 0.72 | ESTIMATE | S1, S2 |
| e | 0.55 | 0.71 | 0.84 | ESTIMATE | S1, S6 |
| s5 | 0.13 | 0.23 | 0.34 | PROXY | S5 |
| q | 0.48 | 0.64 | 0.79 | ESTIMATE | S1 |
| d5 | 0.94 | 1.06 | 1.2 | PROXY | S4, S6 |
| o | 0.92 | 0.98 | 0.995 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.32 | 0.74 | 1.44 | ESTIMATE |
| F | 4.08 | 5.34 | 6.21 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.65 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Broader machinery occupation proxy.
- a: Product scale and business model vary within the code.
- rho: No code-specific adoption measurement.
- rho: Safety-critical outputs require qualified review.
- e: Injected firm count is margin-bridged and estimated.
- e: Classification does not establish independence or recurring external economics.
- s5: Economy-wide demographic proxy.
- s5: No public code-specific five-year transfer rate.
- q: No public contract dataset quantifies pass-through.
- q: Aftermarket wear parts and proprietary attachments likely retain more than build-to-print assemblies.
- d5: Construction spending is a downstream proxy, not equipment demand.
- d5: Large earthmoving machines and niche attachments follow different cycles.
- o: Operator share can shift to large OEMs or foreign suppliers.
- o: This is separate from internal labor automation.

## Sources
- **S1** — [2022 NAICS Definition: Construction Machinery Manufacturing](https://www.census.gov/naics/?chart=2022&details=333120&input=333120) (accessed 2026-07-22): Census defines the industry as construction, surface-mining, and logging equipment and lists products including backhoes, bulldozers, rock-drill bits, graders, off-highway trucks, and portable crushing equipment.
- **S2** — [Machinery Manufacturing: NAICS 333](https://www.bls.gov/iag/tgs/iag333.htm) (accessed 2026-07-22): BLS states complex assembly is inherent in machinery production and lists 63,880 welders and 9,140 engine and other machine assemblers in the displayed broader-industry data.
- **S3** — [Machinery Manufacturing - May 2023 OEWS](https://www.bls.gov/oes/2023/may/naics3_333000.htm) (accessed 2026-07-22): BLS reports welders at 6.10% of broader machinery employment and provides machine-assembler data, supporting the production-heavy task proxy.
- **S4** — [Construction Spending, December 2025](https://www.census.gov/construction/c30/pdf/pr202512.pdf) (accessed 2026-07-22): Census reports 2025 total construction spending 1.4% below 2024 in the displayed year-to-date comparison, with divergent categories such as public highway and water, used as a downstream demand proxy.
- **S5** — [2024 Chartbook on Firms by Age of Primary Owner](https://www.fedsmallbusiness.org/-/media/project/smallbizcredittenant/fedsmallbusinesssite/fedsmallbusiness/files/2024/firms-in-focus/sbcs_chartbook2024_ownerage.pdf) (accessed 2026-07-22): Federal Reserve chartbook provides small-business owner-age evidence used only as a succession proxy.
- **S6** — [Industrial Production: Construction Machinery](https://www.federalreserve.gov/releases/G17/20250815/table1c_sup.htm) (accessed 2026-07-22): Federal Reserve publishes a direct 33312 construction-machinery production series, supporting the empirical demand route and indicating monthly 2025 index values around the high 90s in the displayed table.
