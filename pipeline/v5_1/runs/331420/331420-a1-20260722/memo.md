# 331420 — Copper Rolling, Drawing, Extruding, and Alloying

*v5.1 Stage 1 research memo. Run `331420-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.94 · L 0.43 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Structural electrification demand combined with qualification and custom-profile switching costs can make yield, quality, and uptime gains valuable.
**Weakness:** Only 14 estimated LMM firms, many product- and commodity-oriented, leave a very narrow and poorly observed recurring-service acquisition set.

## Business-model lens
- Included: Independent lower-middle-market firms that alloy, roll, draw, or extrude copper and copper alloys into tube, rod, bar, sheet, strip, foil, wire, or custom shapes, emphasizing toll conversion, specialty alloys, custom profiles, difficult short runs, and repeat specification programs.
- Excluded: Primary copper smelting and refining; aluminum or other non-copper metal mills; wire-product fabrication without drawing; distributors and machine shops without substantive copper conversion; captive or large integrated commodity mills outside the LMM band; and businesses lacking recurring customer programs.
- Customer and revenue model: Customers include plumbing and HVAC suppliers, electrical-equipment and data-center infrastructure manufacturers, utilities, transportation and aerospace suppliers, industrial OEMs, distributors, and other mills. Revenue generally combines benchmark-linked copper cost with a conversion or fabrication margin; repeat custom drawings, alloy specifications, tooling, qualification, stocking, and just-in-time releases create recurring economics, with a smaller toll-processing subset handling customer material.
- Deviation from default lens: none

## Executive view
The investable case is a specialty copper or copper-alloy converter with repeat custom profiles, qualifications, small difficult runs, and possibly customer-owned-metal tolling—not a commodity tube or rod mill. AI can improve inspection, process stability, maintenance, scheduling, and documentation, but the opportunity is constrained by only 14 estimated LMM firms and heavy copper working capital.

## How AI changes the work
The clearest uses are full-line surface inspection, automated copper-alloy microstructure evaluation, anomaly detection, gauge and setup recommendations, predictive maintenance, scrap and alloy classification, production scheduling, traceability, quoting, and quality records. Material handling, roll and die changes, annealing, drawing, testing, repairs, and exception recovery remain physical.

## Value capture
Copper price changes are generally passed through, exposing the conversion margin to customer scrutiny. Sustainable capture depends on specialty qualification, custom geometry, short-run responsiveness, difficult alloy expertise, on-time delivery, yield, and avoided quality claims; simple material or administrative savings are likely to be shared.

## Firm availability
The target pool is exceptionally small and heterogeneous. Succession may surface a niche operator, but diligence must examine metal-price working capital, customer concentration, owned versus customer tooling, end-market exposure, environmental history, equipment and furnace condition, energy, labor, imports, and transfer of customer approvals.

## Demand durability
Electrification, grid investment, data centers, thermal management, HVAC, and industrial equipment support copper demand. However, plastics increasingly substitute in plumbing, aluminum threatens some refrigeration and electrical applications, brass-intensive manufacturing has moved offshore, and construction cycles can weaken the demand seen by a specific LMM mill.

## Risks and uncertainty
Key uncertainties are the true incidence of toll or repeat custom programs, the classification of intermediaries versus actual mills, capture under copper pass-through pricing, substitution, customer concentration, imports, capital condition, environmental exposure, and whether small plants can operationalize AI despite limited engineering resources.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0737 | — | OBSERVED | — |
| n | — | 14 | — | ESTIMATE | — |
| a | 0.2 | 0.32 | 0.45 | PROXY | S1, S2, S3, S4, S5 |
| rho | 0.28 | 0.46 | 0.63 | ESTIMATE | S4, S5 |
| e | 0.15 | 0.3 | 0.48 | PROXY | S6, S7, S8 |
| s5 | 0.08 | 0.14 | 0.22 | PROXY | S9 |
| q | 0.26 | 0.43 | 0.6 | PROXY | S6, S7, S10 |
| d5 | 0.97 | 1.15 | 1.32 | PROXY | S6, S10, S11 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1, S2, S3, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.43 | 0.84 | ESTIMATE |
| F | 0.25 | 0.74 | 1.46 | ESTIMATE |
| C | 5.20 | 8.60 | 10.00 | PROXY |
| D | 9.12 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET occupations include other metals and plastics.
- a: AI examples cover inspection rather than the full production system.
- a: Tube, wire, strip, foil, rod, and alloy operations have materially different labor mixes.
- rho: No representative NAICS-level adoption study was found.
- rho: Inspection is easier to retrofit than closed-loop process control.
- rho: Aerospace, electrical, and pressure-product qualifications constrain rapid changes.
- e: Public examples do not disclose revenue or margin mix.
- e: Some custom copper suppliers outsource extrusion and may not belong in this NAICS.
- e: Recurring product sales are less service-like than customer-owned tolling.
- s5: Cross-industry intentions are not observed copper-mill transactions.
- s5: Stated plans may not become marketed businesses.
- s5: A one-firm event materially changes availability in this small universe.
- q: Capture differs materially across standard tube, electrical products, and specialty alloys.
- q: Metal-price movements and FIFO accounting can obscure process economics.
- q: Shortages and tariffs can temporarily inflate pricing power.
- d5: Broad copper demand does not translate one-for-one into domestic LMM processing.
- d5: Plumbing and construction exposure can offset electrification growth.
- d5: Imported finished goods can bypass domestic semi-finished copper products.
- o: This factor addresses AI-related obsolescence, not ordinary share loss.
- o: Individual legacy mills can become uneconomic even if the process persists.
- o: Material substitution risk is real and product-specific.

## Sources
- **S1** — [NAICS 331420 - Copper Rolling, Drawing, Extruding, and Alloying](https://www.naics.com/naics-code-description/?code=331420&v=2022) (accessed 2026-07-22): Industry boundary covering copper scrap recovery, alloying, and rolling, drawing, or extruding bar, plate, sheet, strip, tube, wire, and other shapes.
- **S2** — [Rolling Machine Setters, Operators, and Tenders, Metal and Plastic](https://www.onetonline.org/link/summary/51-4023.00) (accessed 2026-07-22): Core rolling tasks: monitoring, setup correction, inspection, measurement, controls, roll changes, threading, trimming, and records.
- **S3** — [Extruding and Drawing Machine Setters, Operators, and Tenders, Metal and Plastic](https://www.onetonline.org/link/summary/51-4021.00) (accessed 2026-07-22): Core extrusion and drawing tasks: die selection and change, controls, inspection, testing, troubleshooting, handling, and cutting.
- **S4** — [Glintect Managed AI Roll-to-Roll Inspection](https://glintect.com/) (accessed 2026-07-22): Commercial availability of managed AI inline inspection with existing-camera integration and reported effects on inspection coverage, waste, labor, and deployment time.
- **S5** — [Automated Copper Alloy Grain Size Evaluation Using a Deep-Learning CNN](https://arxiv.org/abs/2005.09634) (accessed 2026-07-22): Copper-alloy-specific proof of concept for automated microstructure evaluation with potential labor, accuracy, and approval-turnaround improvements.
- **S6** — [Custom Copper Extrusions for OEM and Electrical Applications](https://www.deecometals.com/copper-extrusions) (accessed 2026-07-22): Custom profiles, repeat production geometry, small and large programs, design review, tight tolerances, value-added finishing, and electrical/data-center applications.
- **S7** — [Custom Toll Processing](https://www.cralloys.com/products-services/toll-processing/) (accessed 2026-07-22): Adjacent specialty-alloy toll model serving mills and distributors with just-in-time turnaround and nonstandard quantities, sizes, tolerances, and specifications.
- **S8** — [Custom Brass Extrusion Services](https://www.gambometals.com/article/en/list/faq-1.html) (accessed 2026-07-22): Customer drawing and tooling support for custom copper-alloy shapes and raw-material-market pricing at order date.
- **S9** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry evidence on owner age and five-year intentions to sell, transfer, close, or continue small businesses.
- **S10** — [Mueller Industries 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/89439/000008943926000008/mli-20251227.htm) (accessed 2026-07-22): Copper and brass products and markets, raw-material pass-through, spread economics, lower core volumes, imports, plastic and aluminum substitution, utilities, and pricing discipline.
- **S11** — [IEA Copper Outlook](https://www.iea.org/reports/copper-2) (accessed 2026-07-22): Copper demand, clean-technology use, secondary supply and reuse, primary supply requirements, and refining concentration through 2030 and 2040.
