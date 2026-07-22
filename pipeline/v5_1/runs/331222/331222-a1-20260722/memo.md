# 331222 — Steel Wire Drawing

*v5.1 Stage 1 research memo. Run `331222-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.87 · L 0.39 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repetitive, sensor-friendly production supports implementable AI in inspection, process stability, maintenance, and scheduling.
**Weakness:** Very low labor intensity and commodity pass-through sharply limit the retained economic value of task automation.

## Business-model lens
- Included: Independent U.S. manufacturers repeatedly drawing, annealing, coating, cleaning, spooling, inspecting, and selling steel wire made from purchased steel rod to external customers.
- Excluded: Captive drawing lines, integrated steelmakers drawing their own wire, downstream wire-product fabrication such as nails or springs, distributors, passive entities, and firms without transferable operations.
- Customer and revenue model: Repeat product sales to reinforcing, prestressing, spring, fastener, cable, automotive, appliance, bedding, construction, industrial, and agricultural customers, priced by weight, diameter, grade, tensile properties, coating, packaging, processing, freight, and wire-rod market conditions.
- Deviation from default lens: none

## Executive view
Steel wire drawing is already a low-labor, continuous process, so AI's best opportunities are defect inspection, tension and diameter control, die and bearing maintenance, break prevention, scheduling, and paperwork. Low compensation intensity and transparent wire-rod economics constrain aggregate labor savings and benefit retention.

## How AI changes the work
Vision and gauges can detect surface and dimensional defects, models can predict breaks and die wear, and software can optimize scheduling, quality records, purchasing, and quotations. Physical handling, setup, die changes, maintenance, testing, and responsible release remain.

## Value capture
Specialty chemistry, dimensions, coatings, qualification, delivery, and fewer breaks protect some gains. Commodity products, wire-rod surcharges, bids, imports, and low labor content make visible savings difficult to retain fully.

## Firm availability
Independent specialty drawers plausibly fit the lens, but captive integration and the machinery-margin bridge make the 46-firm estimate uncertain. Customer concentration, equipment condition, trade exposure, and working capital matter for transferability.

## Demand durability
Construction reinforcement, cable, fasteners, springs, vehicles, appliances, and industrial uses sustain physical demand, with construction and durable-goods cyclicality. Nearly all remaining volume still requires an accountable producer.

## Risks and uncertainty
Key risks are line-speed model errors, false rejects, wire breaks, legacy integration, cyber-physical security, wire-rod prices and availability, imports and tariffs, construction cycles, customer concentration, low labor intensity, and LMM misclassification.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0847 | — | OBSERVED | — |
| n | — | 46 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.31 | PROXY | S1, S2, S3, S4 |
| rho | 0.36 | 0.55 | 0.71 | ESTIMATE | S2, S3, S4 |
| e | 0.54 | 0.72 | 0.86 | ESTIMATE | S5, S6 |
| s5 | 0.15 | 0.27 | 0.42 | PROXY | S9 |
| q | 0.28 | 0.47 | 0.66 | PROXY | S6, S7, S8 |
| d5 | 0.88 | 1.07 | 1.27 | PROXY | S6, S10 |
| o | 0.98 | 0.995 | 1 | ESTIMATE | S3, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.15 | 0.39 | 0.75 | ESTIMATE |
| F | 2.50 | 3.69 | 4.61 | ESTIMATE |
| C | 5.60 | 9.40 | 10.00 | PROXY |
| D | 8.62 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS combines rolled shapes, pipe, tube, and wire drawing.
- a: Equipment and inspection sources establish capability but not adoption across U.S. LMM firms.
- rho: Process and quality improvements do not all substitute labor.
- rho: High-volume reinforcing wire and specialty fine or alloy wire have different data and integration economics.
- e: The Census profile defines the industry but does not expose a firm-level target population in the fetched content.
- e: The frozen n uses a Machinery margin, which may misclassify low-labor commodity wire businesses.
- s5: The evidence is not industry-specific and is not a completed-transfer rate.
- s5: Acquisition of a plant or assets may not qualify as control transfer of an eligible firm.
- q: Reinforcing, prestressing, spring, fastener, cable, bedding, and specialty alloy wire have different pricing power.
- q: Insteel manufactures downstream reinforcement products as well as drawing wire; Gerdau is integrated and global.
- d5: BLS output covers all 331200 products, not 331222 alone.
- d5: Insteel is concentrated in construction reinforcement and does not represent all drawn-wire end markets.
- o: Imports can displace domestic operators without making software the supplier.
- o: Operator requirement does not imply unchanged headcount.

## Sources
- **S1** — [Steel Product Manufacturing from Purchased Steel - May 2023 OEWS](https://www.bls.gov/oes/2023/may/naics4_331200.htm) (accessed 2026-07-23): Provides the broader purchased-steel occupational mix across production, maintenance, material-moving, technical, management, commercial, and office roles.
- **S2** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-23): Documents AI use and barriers in predictive maintenance, quality, process control, resource management, and scheduling.
- **S3** — [Cable and Wire Surface Defect Inspection](https://www.taymer.com/wire-cable/inspection/) (accessed 2026-07-23): Describes machine-learning vision systems for surface-defect inspection of wire and cable.
- **S4** — [Steel Wire Drawing Quality and Uniformity Controls](https://www.listrongwiremachinery.com/news/how-does-the-steel-wire-drawing-machine-ensure-the-quality-and-uniformity-of-the-wire-produced.html) (accessed 2026-07-23): Describes automatic tension control, laser micrometers, and surface cameras providing real-time wire quality data.
- **S5** — [331222: Steel Wire Drawing - Census Bureau Profile](https://data.census.gov/profile/331222_-_Steel_wire_drawing?codeset=naics~331222) (accessed 2026-07-23): Defines the industry as drawing wire from purchased steel and distinguishes integrated steelmaking and downstream wire products.
- **S6** — [Insteel Industries 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/764401/000143774925031597/iiin20250927_10k.htm) (accessed 2026-07-23): Documents wire-rod input exposure, competitive pricing, construction demand, imports, outages, and an 85% nonresidential and 15% residential sales mix.
- **S7** — [Insteel Industries March 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/764401/000143774926012525/iiin20260328_10q.htm) (accessed 2026-07-23): Reports successful raw-material cost recovery through price increases, supportive nonresidential demand, and continued wire-rod pricing and trade risks.
- **S8** — [Gerdau 2025 Form 20-F](https://www.sec.gov/Archives/edgar/data/1073404/000110465926027678/ggb-20251231x20f.htm) (accessed 2026-07-23): Distinguishes commodity wire rod from differentiated drawn and specialty wire products and documents steel-price volatility and import pressure.
- **S9** — [5 Challenges for Family-Owned Businesses](https://www.sba.gov/blog/5-challenges-family-owned-businesses) (accessed 2026-07-23): Reports that 47% of owners expecting to retire within five years do not have a successor.
- **S10** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-23): Projects broader 331200 real output from $25.6 billion in 2024 to $30.9 billion in 2034, a 1.9% annual rate.
