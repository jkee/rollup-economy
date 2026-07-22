# 331315 — Aluminum Sheet, Plate, and Foil Manufacturing

*v5.1 Stage 1 research memo. Run `331315-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.65 · L 0.49 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat, customer-qualified specialty work in which AI-assisted quality, yield, and uptime improvements expand scarce rolling capacity.
**Weakness:** True toll-rolling businesses appear to be a small and poorly measured fraction of an already tiny, capital-intensive LMM universe.

## Business-model lens
- Included: Independent lower-middle-market manufacturers that hot-roll or cold-roll aluminum into sheet, plate, strip, or foil, with emphasis on specialty short runs, customer-qualified products, and toll or conversion work using customer-supplied metal.
- Excluded: Primary aluminum smelting; secondary alloy smelting; extrusion; downstream stamping, coating, printing, slitting, or distribution without substantive rolling; captive rolling divisions of large integrated groups; and commodity-scale mills outside the LMM band.
- Customer and revenue model: Customers include aerospace and defense fabricators, beverage and flexible-packaging converters, automotive suppliers, industrial OEMs, and distributors. Most revenue is product sales priced as metal cost plus conversion margin; a narrower recurring-service subset earns toll rolling or finishing fees on customer-owned material and repeat specification orders.
- Deviation from default lens: none

## Executive view
Aluminum rolling offers real AI opportunities in control, quality, maintenance, and planning, but the investable recurring-service subset is narrow. The most coherent LMM target is a specialty or toll roller with customer-owned metal, repeat qualified specifications, and difficult small runs; commodity sheet or foil ownership is much less service-like and more exposed to scale and spread economics.

## How AI changes the work
Machine-learning control can adapt flow-stress and heat-flux parameters, vision can identify strip defects and coils, and predictive systems can anticipate failures. These tools should reduce scrap, downtime, setup losses, and inspection effort, while operators still thread lines, change rolls, move coils, repair equipment, and approve safety- or qualification-critical decisions.

## Value capture
Metal pass-through structures protect against some commodity volatility but also make conversion margins transparent. Capture is strongest when AI unlocks bottleneck throughput, prevents expensive quality claims, or improves delivery on a constrained qualified line; it is weakest in competitive commodity products where customers can rebid the conversion margin.

## Firm availability
The frozen estimate is only 20 LMM firms, and few are likely to combine substantive rolling with recurring toll revenue. Ownership succession may create opportunities, yet environmental diligence, aging equipment, energy intensity, working capital, customer concentration, and qualification transfer can make an apparent target unfinanceable.

## Demand durability
Packaging, aerospace, automotive lightweighting, defense, and other industrial uses create a diversified demand base, and North American sheet, plate, and foil volumes showed resilience in 2025. The LMM subset still faces powerful integrated competitors, new capacity, imports, customer destocking, and product-specific cycles.

## Risks and uncertainty
The central uncertainty is eligibility: public data do not reveal how many small establishments truly roll customer-owned aluminum rather than sell owned product or perform only downstream slitting and leveling. Other material risks are mill condition, environmental liabilities, energy cost, qualification loss, customer concentration, trade policy, and the gap between vendor capability and realized AI savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0912 | — | OBSERVED | — |
| n | — | 20 | — | ESTIMATE | — |
| a | 0.19 | 0.31 | 0.43 | PROXY | S1, S2, S3, S4 |
| rho | 0.25 | 0.43 | 0.62 | ESTIMATE | S3, S4 |
| e | 0.05 | 0.14 | 0.3 | PROXY | S5, S6, S7 |
| s5 | 0.08 | 0.14 | 0.22 | PROXY | S8 |
| q | 0.22 | 0.38 | 0.55 | PROXY | S6, S7 |
| d5 | 1 | 1.12 | 1.25 | PROXY | S6, S9 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S1, S2, S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.49 | 0.97 | ESTIMATE |
| F | 0.12 | 0.53 | 1.35 | ESTIMATE |
| C | 4.40 | 7.60 | 10.00 | PROXY |
| D | 9.50 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET covers rolling across metals and plastics, not aluminum alone.
- a: Vendor materials establish availability and functions but not representative adoption.
- a: Foil, plate, and sheet production have materially different labor mixes.
- rho: No representative adoption rate for NAICS 331315 was found.
- rho: Digital readiness varies sharply with mill age and controls architecture.
- rho: Aerospace qualification can delay or constrain process changes.
- e: Public toll examples often include slitting or leveling rather than primary gauge reduction.
- e: Company websites do not reveal revenue mix.
- e: Large-company business models may not represent specialty LMM operators.
- s5: Cross-industry intentions are not observed industrial transactions.
- s5: Stated owner plans may not become marketed businesses.
- s5: The thin population makes annual availability highly lumpy.
- q: Contract terms differ across aerospace, automotive, packaging, and distributor customers.
- q: Value capture is likely lower for commodity sheet and higher for qualified niche products.
- q: Trade protection and capacity shortages can temporarily inflate capture.
- d5: Broad aluminum demand does not translate one-for-one to LMM toll volume.
- d5: End markets have divergent cycles and substitution risks.
- d5: Capacity additions can grow industry demand while weakening incumbent utilization.
- o: The factor isolates AI-related obsolescence rather than normal competitive displacement.
- o: A specific old mill can become economically obsolete even when the process remains necessary.
- o: Product substitution differs sharply by end market.

## Sources
- **S1** — [NAICS 331315 - Aluminum Sheet, Plate, and Foil Manufacturing](https://www.naics.com/naics-code-description/?code=331315&v=2022) (accessed 2026-07-22): Industry boundary for rolling aluminum into sheet, plate, and foil products.
- **S2** — [Rolling Machine Setters, Operators, and Tenders, Metal and Plastic](https://www.onetonline.org/link/summary/51-4023.00) (accessed 2026-07-22): Core operator tasks including monitoring, setup correction, inspection, measuring, controls, roll changes, threading, and production records.
- **S3** — [Aluminum Hot Rolling Automation and Modernization](https://www.primetals.com/en/portfolio/solutions/hot-rolling/non-ferrous/aluminum/automation-for-aluminum-hot-rolling-mills/) (accessed 2026-07-22): Commercial aluminum-mill automation using real-time analytics, advanced controls, and neural networks for flow stress, heat flux, gauge, yield, and quality.
- **S4** — [Strip Cross Crack Assistant](https://www.primetals.com/en/portfolio/solutions/hot-rolling/hot-strip-mill/automation/strip-cross-crack-assistant) (accessed 2026-07-22): Commercial AI vision system for real-time strip-crack detection, operator alerts, quality improvement, and reduced waste and downtime.
- **S5** — [CAC Light Gauge Metal Toll Processing](https://cac-inc.com/toll-processing/) (accessed 2026-07-22): Direct evidence of specialty aluminum toll processing for difficult light gauges, flatness correction, cut-to-length, and customer specifications.
- **S6** — [Constellium 2025 Annual Report](https://www.sec.gov/Archives/edgar/data/1563411/000156341126000147/a2025ars.htm) (accessed 2026-07-22): Rolled-aluminum end markets, demand forecasts, margin-over-metal pricing, pass-throughs, hedging, scrap spreads, energy costs, and qualification dynamics.
- **S7** — [Real Alloy Tolling Model Description](https://www.sec.gov/Archives/edgar/data/38984/000156459016014765/rely-ex992_6.htm) (accessed 2026-07-22): Adjacent aluminum-processing evidence for customer-owned metal, per-pound or per-ton conversion fees, energy pass-throughs, proximity, and sticky customer relationships.
- **S8** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry evidence on owner age and five-year intentions to sell, transfer, close, or continue a small business.
- **S9** — [North American Aluminum Demand Steady in 2025](https://www.aluminum.org/news/north-american-aluminum-demand-steady-2025) (accessed 2026-07-22): Current association report that total 2025 aluminum demand was essentially flat while sheet and plate and foil experienced modest growth.
