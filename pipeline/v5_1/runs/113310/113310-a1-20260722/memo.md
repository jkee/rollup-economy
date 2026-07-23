# 113310 — Logging

*v5.1 Stage 1 research memo. Run `113310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.71 · L 0.57 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Machine and truck coordination, telematics, and administrative workflows can improve utilization in an already mechanized service.
**Weakness:** A small transferable pool serves volatile local wood markets while retaining irreducible safety, equipment, terrain, and customer-concentration risk.

## Business-model lens
- Included: Independent LMM contract logging operators that repeatedly cut, process, yard, load, and where contracted transport timber or produce field chips for external timberland owners, mills, forest managers, or public agencies.
- Excluded: Timber-tract owners selling standing timber, firms primarily taking timber-price ownership risk rather than charging for harvesting, vertically integrated mill crews, captive forestry units, one-person lifestyle operators, landholding shells, and firms outside the EBITDA band.
- Customer and revenue model: Repeat tract- or volume-based harvesting work under timber-sale, mill-supply, stewardship, or service contracts, with revenue commonly tied to harvested tons, board feet, loads, acres, machine time, or fixed project scope.
- Deviation from default lens: NAICS 113310 mixes outsourced contract harvesting with timber buyers and vertically integrated crews that earn a commodity spread or serve a captive owner. The lens keeps independent repeat-service contractors so the revenue and pass-through analysis is coherent.

## Executive view
Contract logging has a modest AI opportunity in dispatch, telematics, planning, bidding, and administration, but the core work is dangerous, physical, capital-intensive, and terrain-specific. The dataset suggests only 28 LMM-band firms before eligibility screening, so individual-business diligence matters greatly.

## How AI changes the work
Likely uses include tract and route planning, truck-machine coordination, production simulation, maintenance alerts, geospatial boundary checks, bid preparation, safety and environmental records, invoicing, and customer reporting. Felling, machine operation, rigging, loading, repair, and site hazard response remain operator work.

## Value capture
Fixed and unit-rate contracts can preserve near-term productivity gains, but competitive bids, mill and landowner bargaining, transparent rates, fuel clauses, and renewals share value. Gains tied to fewer delays or better uptime may be harder for customers to observe and reprice immediately.

## Firm availability
Independent repeat contractors fit, but the code also contains timber buyers and captive crews. A small estimated LMM pool, owner dependence, customer concentration, equipment debt, and the possibility of asset-only exits constrain transferable availability.

## Demand durability
Physical timber harvesting persists across sawlogs, pulpwood, chips, salvage, thinning, and biomass. Housing and paper cycles, mill closures, imports, weather access, wildfire policy, mass timber, and regional resource conditions create a wide volume range.

## Risks and uncertainty
The largest risks are a small estimated firm pool, business-model mixing, customer and mill concentration, timber cycles, equipment leverage and downtime, diesel, trucking, labor, severe safety exposure, weather, fire, soil and water rules, and inconsistent rural connectivity.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1926 | — | OBSERVED | — |
| n | — | 28 | — | ESTIMATE | — |
| a | 0.07 | 0.14 | 0.23 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.53 | 0.69 | ESTIMATE | S3, S4, S7 |
| e | 0.46 | 0.65 | 0.8 | ESTIMATE | S1, S8 |
| s5 | 0.14 | 0.26 | 0.39 | PROXY | S2, S9 |
| q | 0.31 | 0.49 | 0.66 | ESTIMATE | S3, S8 |
| d5 | 0.87 | 0.98 | 1.11 | PROXY | S2, S5, S6, S7 |
| o | 0.94 | 0.985 | 1 | ESTIMATE | S1, S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.19 | 0.57 | 1.22 | ESTIMATE |
| F | 1.66 | 2.81 | 3.66 | ESTIMATE |
| C | 6.20 | 9.80 | 10.00 | ESTIMATE |
| D | 8.18 | 9.65 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation data include workers employed outside logging firms.
- a: Regional harvesting systems and terrain create materially different task mixes.
- rho: Bounded judgment rather than an observed adoption rate.
- rho: The Forest Service coordination project demonstrates a workflow but not broad commercial AI adoption.
- e: No current public source measures the eligible service share.
- e: Contractor, timber buyer, dealer, and mill-affiliated models can coexist within one firm.
- e: The supplied firm count is an estimate bridged from receipts and a sector margin.
- s5: Economy-wide owner-age proxy.
- s5: Worker replacement demand is not evidence of company control transfers.
- s5: No denominator-based transfer series for contract loggers.
- q: No public contract panel quantifies pass-through.
- q: Timber buyers and fee contractors allocate commodity and productivity risk differently.
- d5: Employment combines demand and productivity effects.
- d5: The pulpwood observation is regional, product-specific, and dated.
- d5: Forest treatment appropriations do not guarantee merchantable contract volume.
- o: The accountable operator may become a larger integrated mill or fleet platform rather than an independent contractor.
- o: This primitive excludes task automation already captured in a and rho.

## Sources
- **S1** — [NAICS Definition: 113310 Logging](https://www.census.gov/naics/?details=11&input=11&year=2017) (accessed 2026-07-22): Census defines logging as cutting timber, cutting and transporting timber, or producing wood chips in the field, and separates timber-tract operations.
- **S2** — [Logging Workers](https://www.bls.gov/ooh/farming-fishing-and-forestry/logging-workers.htm) (accessed 2026-07-22): BLS reports 44,300 logging workers in 2024, including 30,900 equipment operators, describes physical harvesting and grading duties, and projects employment to decline 2 percent through 2034.
- **S3** — [Improving Mechanical Thinning and Biomass Transportation Efficiency](https://research.fs.usda.gov/srs/projects/harvest-efficiency) (accessed 2026-07-22): The Forest Service describes real-time machine and truck coordination, harvesting simulations, geospatial boundary control, and a project outcome of improving logging-operation production by 15 percent.
- **S4** — [29 CFR 1910.266 Logging Operations](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.266) (accessed 2026-07-22): OSHA specifies safety practices for logging and requires site-specific hazard evaluation, supervisor consultation, machine control, and safe felling, yarding, loading, and transport.
- **S5** — [Southern Pulpwood Production, 2022](https://research.fs.usda.gov/treesearch/67437) (accessed 2026-07-22): The Forest Service reports Southern pulpwood production declined from 59.0 million cords in 2021 to 56.0 million in 2022, with roundwood production at 41.6 million cords.
- **S6** — [Forest Resources of the United States, 2022](https://research.fs.usda.gov/treesearch/80035) (accessed 2026-07-22): The 2026 Forest Service report provides national resource statistics on forest area, growth, removals, and timber products output and identifies the breadth of the physical resource base.
- **S7** — [What Loggers Are Noticing and Doing about Changing Winter Weather](https://research.fs.usda.gov/nrs/projects/loggers-changing-winter-weather) (accessed 2026-07-22): Forest Service research reports fewer operable winter logging days, heavier equipment, workforce constraints, changing tract access, and adaptation by logging businesses in northern Minnesota.
- **S8** — [Selling Timber](https://extension.umn.edu/managing-woodlands/selling-timber) (accessed 2026-07-22): University of Minnesota Extension describes timber-sale contracts, competitive bid solicitation, logger selection, harvest monitoring, and contract administration, supporting the customer and repricing model.
- **S9** — [2024 Chartbook on Firms by Age of Primary Owner](https://www.fedsmallbusiness.org/-/media/project/smallbizcredittenant/fedsmallbusinesssite/fedsmallbusiness/files/2024/firms-in-focus/sbcs_chartbook2024_ownerage.pdf) (accessed 2026-07-22): Federal Reserve owner-age evidence used only as a broad succession proxy for qualifying control transfers.
