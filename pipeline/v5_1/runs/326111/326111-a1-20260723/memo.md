# 326111 — Plastics Bag and Pouch Manufacturing

*v5.1 Stage 1 research memo. Run `326111-a1-20260723`, model `claude-sonnet-5`, 2026-07-23, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.40 · L 0.89 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring demand for lightweight physical packaging supports repeat customer programs and targeted AI improvements around production and commercial workflows.
**Weakness:** Commodity pricing and accelerating single-use-plastic reduction or material substitution can erode both demand and retained savings.

## Business-model lens
- Included: US lower-middle-market converters and integrated manufacturers that repeatedly supply plastic film bags or pouches to external food, consumer-products, healthcare, industrial, retail, waste, or e-commerce customers.
- Excluded: Captive packaging operations, pure distributors, manufacturers only of film or sheet without bag or pouch conversion, paper-combination bags classified elsewhere, purchased-material printers, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring per-unit orders and supply programs for stock or custom bags and pouches, often involving print, dimensions, barrier, seal, gauge, and qualification specifications; revenue can range from spot commodity orders to negotiated multi-year programs.
- Deviation from default lens: none

## Executive view
Plastic bag and pouch manufacturing combines recurring physical packaging demand with a machine-intensive workforce. AI is most credible in scheduling, quality triage, maintenance, artwork and order workflow, quoting, and service rather than direct replacement of converting labor. Custom and validated formats can retain value, while commodity bags face bid pressure and policy-driven substitution.

## How AI changes the work
Extrusion, converting, sealing, printing, material handling, setup, and maintenance remain physical. Machine vision, anomaly detection, schedule and resin optimization, predictive-maintenance support, artwork review, document extraction, quoting, and customer-service automation can reduce indirect and exception-handling work.

## Value capture
Custom graphics, barrier performance, food or medical qualification, and reliable short-run service provide switching friction. Commodity grocery, merchandise, trash, or simple industrial bags are more transparent and frequently bid, while resin-index clauses can quickly expose lower costs to customers.

## Firm availability
The industry likely contains transferable independent converters, but the nominal pool must be filtered for captive operations, obsolete assets, customer concentration, regulatory exposure, thin margins, and founder-dependent selling. General owner-age evidence suggests succession, not a measured deal probability.

## Demand durability
Food, healthcare, waste handling, industrial shipping, and e-commerce sustain packaging functions, and flexible formats can displace heavier rigid packaging. Offsetting forces include lightweighting, reuse, paper substitution, bag restrictions, extended producer responsibility, and pressure to reduce single-use plastics.

## Risks and uncertainty
The largest risks are resin and energy volatility, customer concentration, commodity bids, food-contact or medical qualification, print and seal quality, equipment reliability, recyclability requirements, and fast-changing plastic policy. Broad flexible-packaging and e-commerce indicators are imperfect quantity proxies.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1719 | — | OBSERVED | — |
| n | — | 117 | — | ESTIMATE | — |
| a | 0.13 | 0.23 | 0.35 | PROXY | S2, S3 |
| rho | 0.36 | 0.56 | 0.72 | ESTIMATE | S3 |
| e | 0.45 | 0.65 | 0.8 | ESTIMATE | S1, S7 |
| s5 | 0.14 | 0.25 | 0.37 | PROXY | S4, S5 |
| q | 0.3 | 0.52 | 0.72 | ESTIMATE | S1, S7 |
| d5 | 0.82 | 1.04 | 1.22 | PROXY | S6, S7, S8 |
| o | 0.86 | 0.95 | 0.99 | ESTIMATE | S1, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.32 | 0.89 | 1.73 | ESTIMATE |
| F | 3.42 | 4.82 | 5.75 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.05 | 9.88 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source is four-digit plastics manufacturing, not this six-digit industry.
- a: Employment shares are not task shares and require judgmental wage weighting.
- rho: BLS documents automation in machine operation generally, not AI implementation outcomes.
- rho: Implementation may improve throughput or scrap without reducing labor.
- e: The injected count is model-derived.
- e: Flexible packaging sources include activities outside plastic bags and pouches.
- s5: ABS includes other industries and sizes.
- s5: Plant sales and internal restructurings are not necessarily qualifying firm transfers.
- q: No source directly measures retention of AI-generated savings.
- q: Value capture varies materially between commodity sacks and differentiated printed or barrier pouches.
- d5: E-commerce sales are not packaging units and include digital services and goods with varied packaging.
- d5: The trade association covers flexible packaging beyond this NAICS code.
- d5: EPA strategy statements do not establish enacted nationwide quantity limits.
- o: This is conditional on year-five demand remaining after reduction and substitution.
- o: An external operator may lose volume to vertical integration even when physical demand persists.

## Sources
- **S1** — [2022 NAICS Definition: Plastics Bag and Pouch Manufacturing](https://www.census.gov/naics/?details=326111&input=326111&year=2022) (accessed 2026-07-23): Defines converting resins or film into single- or multiweb plastic bags and pouches and identifies relevant exclusions.
- **S2** — [May 2023 OEWS: Plastics Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-23): Provides the broader plastics-manufacturing occupation mix, including extruding, forming, inspection, packaging, and other production roles used as the task-mix proxy.
- **S3** — [Metal and Plastic Machine Workers](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-23): Describes setup, test runs, minor repairs, inspection, monitoring, and how automation can let operators control multiple machines.
- **S4** — [ABS Characteristics of Business Owners: 2022 Tables](https://www.census.gov/data/tables/2022/econ/abs/2022-abs-characteristics-of-owners.html) (accessed 2026-07-23): Provides age-of-owner tables used as a broad succession proxy.
- **S5** — [Annual Business Survey Methodology: 2022](https://www.census.gov/programs-surveys/abs/technical-documentation/methodology.2022.html) (accessed 2026-07-23): Explains ABS coverage, sampling, and business and owner characteristic limitations.
- **S6** — [Quarterly Retail E-Commerce Sales: First Quarter 2026](https://www.census.gov/retail/eCommerce.html) (accessed 2026-07-23): Reports $326.7 billion of seasonally adjusted first-quarter 2026 e-commerce sales, 9.8% above first-quarter 2025 and 16.9% of total retail sales, as a packaging-demand proxy.
- **S7** — [U.S. Flexible Packaging Industry Economic Impact](https://www.flexpack.org/economic-impact) (accessed 2026-07-23): Describes flexible packaging's role across food, healthcare, agriculture, and e-commerce and reports its broad 2025 US economic footprint.
- **S8** — [National Strategy to Prevent Plastic Pollution](https://www.epa.gov/newsreleases/biden-harris-administration-announces-national-strategy-prevent-plastic-pollution) (accessed 2026-07-23): Documents policy directions including reducing single-use plastic consumption, expanding reuse and refill, and considering producer-responsibility approaches.
