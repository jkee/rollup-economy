# 333414 — Heating Equipment (except Warm Air Furnaces) Manufacturing

*v5.1 Stage 1 research memo. Run `333414-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.11 · L 1.17 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat replacement and channel demand combined with engineering, quoting, quality, and production-support workflows suited to AI assistance.
**Weakness:** Electrification can shrink parts of the product basket while safety and certification constrain factory implementation.

## Business-model lens
- Included: US lower-middle-market manufacturers of heating boilers, heating stoves, floor and wall furnaces, wall and baseboard units, and related non-warm-air heating equipment supplied repeatedly to distributors, OEMs, contractors, building owners, and institutional customers.
- Excluded: Warm-air furnaces, electric space heaters classified elsewhere, industrial and power boilers, industrial process furnaces, installation-only contractors, captive internal plants, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat B2B equipment and replacement-part sales through wholesale, contractor, OEM, specification, and project channels, generally priced per unit or configured system with distributor discounts, bids, warranties, and periodic material-price adjustments.
- Deviation from default lens: none

## Executive view
Heating-equipment manufacturing offers a bounded AI opportunity in engineering support, configuration, quoting, documentation, planning, quality, service knowledge, and administration. Physical fabrication, assembly, combustion or pressure safety, testing, certification, and warranty accountability remain central.

## How AI changes the work
AI can retrieve engineering knowledge, accelerate configurations and quotations, draft technical and compliance documents, optimize schedules and inventory, analyze defects and warranties, assist inspection, and improve service support. Welding, forming, assembly, setup, test, and safety decisions are less substitutable.

## Value capture
Specifications, approvals, installed-base compatibility, product expertise, and distributor relationships create switching costs. Competitive bids, channel discounts, material-price visibility, and powerful customers erode part of productivity gains over time.

## Firm availability
The code contains a plausible regional and family-owned target pool, but external recurring revenue, owner independence, product liability, certifications, concentration, and normalized EBITDA require verification. General succession data support availability without proving industry deal flow.

## Demand durability
Equipment replacement and a large heated building stock support demand, while electrification and heat pumps threaten parts of the current basket. Hydronic, institutional, cold-climate, specialty, and retrofit applications can remain durable, and fulfilled demand still requires a responsible equipment maker.

## Risks and uncertainty
Electrification, regulation, construction cyclicality, distributor concentration, imports, material costs, product liability, warranty, obsolete platforms, and certification costs are material. Evidence is weakest on six-digit task mix, eligible ownership, transaction incidence, and contract-level capture.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1717 | — | OBSERVED | — |
| n | — | 67 | — | ESTIMATE | — |
| a | 0.19 | 0.28 | 0.38 | PROXY | S1 |
| rho | 0.46 | 0.61 | 0.74 | ESTIMATE | S1 |
| e | 0.38 | 0.54 | 0.69 | ESTIMATE | S2 |
| s5 | 0.13 | 0.22 | 0.32 | PROXY | S5 |
| q | 0.39 | 0.56 | 0.72 | ESTIMATE | — |
| d5 | 0.9 | 0.99 | 1.1 | ESTIMATE | S3, S4 |
| o | 0.95 | 0.985 | 0.998 | ESTIMATE | S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.60 | 1.17 | 1.93 | ESTIMATE |
| F | 2.35 | 3.53 | 4.44 | ESTIMATE |
| C | 7.80 | 10.00 | 10.00 | ESTIMATE |
| D | 8.55 | 9.75 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source is broader machinery manufacturing rather than 333414.
- a: Current configurator, ERP, CAD, and factory automation adoption is not observed.
- rho: No industry survey directly measures five-year AI implementation.
- rho: Implementation varies with product complexity, certification burden, and legacy ERP or CAD systems.
- e: NAICS scope does not reveal independence, recurring revenue, or transferability.
- e: The frozen firm count is margin-bridged rather than observed.
- s5: The proxy is cross-industry intention rather than observed transactions.
- s5: Product-line acquisitions may not appear as standalone 333414 control transfers.
- q: No public contract corpus measures pass-through.
- q: Capture differs between specified proprietary equipment, private label, commodity units, and project bids.
- d5: CBECS is a 2018 building-stock snapshot, not a five-year product forecast.
- d5: The NAICS category mixes products with sharply different electrification exposure.
- o: Operator requirement is inferred from physical manufacturing activity.
- o: Heat-pump and alternative-system substitution is captured in d5 rather than double-counted here.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 333300](https://www.bls.gov/oes/2023/may/naics4_333300.htm) (accessed 2026-07-22): Reports 41.26 percent production employment in broader commercial and service industry machinery and identifies substantial engineering, office, sales, planning, inspection, assembly, machining, and welding work used for the task-mix proxy.
- **S2** — [2022 NAICS Definition: 333414 Heating Equipment (except Warm Air Furnaces) Manufacturing](https://www.census.gov/naics/?details=333414&input=333414&year=2022) (accessed 2026-07-22): Defines the industry as manufacturing heating equipment other than electric and warm-air furnaces, including heating boilers, stoves, floor and wall furnaces, and wall and baseboard units, and provides relevant exclusions.
- **S3** — [Less than one-third of U.S. commercial buildings were all-electric in 2018](https://www.eia.gov/todayinenergy/detail.php?id=60983) (accessed 2026-07-22): Reports that 83 percent of commercial buildings had space heating in 2018, 31 percent of commercial buildings were all-electric, and heat pumps were the second-most-common equipment among electricity-only heated buildings, supporting both installed demand and substitution risk.
- **S4** — [U.S. commercial buildings consumed more fuel for space heating than anything else in 2018](https://www.eia.gov/TODAYINENERGY/detail.php?id=55199) (accessed 2026-07-22): Reports that space heating accounted for 32 percent of energy consumed by US commercial buildings in 2018, evidencing the material installed heating need without constituting a product-demand forecast.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of employer-business owners surveyed in fall 2024 planned to sell or transfer ownership within five years, used as a cross-industry transfer proxy.
