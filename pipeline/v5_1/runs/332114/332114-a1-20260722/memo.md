# 332114 — Custom Roll Forming

*v5.1 Stage 1 research memo. Run `332114-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.18 · L 0.16 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat engineered programs generate high-friction drawing, quote, revision, planning, and quality workflows that AI can streamline.
**Weakness:** The labor base is small relative to receipts and most of it operates physical equipment, tooling, materials, or inspection.

## Business-model lens
- Included: US lower-middle-market custom roll formers that repeatedly engineer, tool, and produce metal profiles for external construction, transportation, appliance, storage, energy, industrial, and component customers.
- Excluded: Captive in-house forming lines, firms primarily selling standard proprietary products rather than outsourced custom work, machine builders, pure distributors, non-control financing vehicles, and operations that cannot transfer independently of the owner.
- Customer and revenue model: Recurring production runs and release orders priced per part, foot, pound, run, or program, often with separate or amortized engineering and tooling charges and customer-owned specifications.
- Deviation from default lens: none

## Executive view
Custom roll forming is a durable, specification-driven outsourced manufacturing niche with a small AI-addressable office and engineering layer. AI can improve quote-to-production and quality-document workflows, but the low supplied labor share and highly physical production core limit total labor opportunity.

## How AI changes the work
AI can parse drawings and RFQs, compare revisions, assist cost estimates and routing, recommend schedules and purchases, draft certificates and corrective actions, and organize customer communication. Tool design approval, line setup, coil handling, forming, welding, cutting, inspection, maintenance, and physical release remain accountable plant work.

## Value capture
Customer-specific tooling, approvals, and integration into downstream products create switching friction that can protect workflow gains. Contractual metal pass-through, annual cost downs, rebids, and concentrated procurement organizations will share some benefits over five years.

## Firm availability
The supplied dataset estimates 115 firms in the economic band, but actual eligibility requires verifying custom external work, independence, normalized margins, customer concentration, equipment condition, and whether technical and sales relationships transfer beyond the owner.

## Demand durability
Physical profiles remain essential in construction and manufactured products, with potential support from solar, infrastructure, and modular systems. Cyclicality, imports, customer insourcing, redesign, and alternate forming processes are the main threats rather than software elimination.

## Risks and uncertainty
Key uncertainties are the six-digit occupation mix, very low supplied compensation ratio, firm-level margin and ownership, customer and end-market concentration, current ERP maturity, and real end-market volumes. The supplied inputs mix wage and receipt vintages and apply a machinery margin bridge.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0485 | — | OBSERVED | — |
| n | — | 115 | — | ESTIMATE | — |
| a | 0.09 | 0.18 | 0.29 | PROXY | S1, S2 |
| rho | 0.27 | 0.46 | 0.64 | ESTIMATE | S1, S3 |
| e | 0.62 | 0.78 | 0.89 | ESTIMATE | S3, S4 |
| s5 | 0.09 | 0.18 | 0.29 | ESTIMATE | — |
| q | 0.38 | 0.6 | 0.78 | ESTIMATE | S3 |
| d5 | 0.91 | 1.06 | 1.22 | ESTIMATE | S4, S5 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.05 | 0.16 | 0.36 | ESTIMATE |
| F | 3.22 | 4.57 | 5.51 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.64 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is for all fabricated metal manufacturing, not 332114.
- a: Occupational employment is not a direct measure of AI substitutability or current automation.
- rho: This is bounded judgment rather than an observed five-year adoption rate.
- rho: Conventional CNC and automation gains are excluded unless AI is the operative substitution mechanism.
- e: The provided n relies on receipts and a machinery-industry margin bridge rather than observed EBITDA.
- e: A single large customer program can make an otherwise transferable plant economically fragile.
- s5: No comprehensive six-digit control-transfer series was found.
- s5: Asset auctions, customer-program transfers, and internal reorganizations must be excluded.
- q: No source directly measures retention of AI-derived savings.
- q: Capture likely differs materially between engineered low-volume profiles and high-volume commodity sections.
- d5: No complete constant-price, constant-quality forecast was found for custom roll forming.
- d5: BLS operator projections mix demand, productivity, and process substitution.
- o: Domestic operators can still be displaced by imports or customer-owned lines.
- o: Process substitution belongs here only when it removes the outsourced roll-forming operator for remaining end demand.

## Sources
- **S1** — [Fabricated Metal Product Manufacturing - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics3_332000.htm) (accessed 2026-07-22): BLS reports NAICS 332 occupation shares including 28.52% metal/plastic workers, 10.84% assemblers/fabricators, 8.17% welding workers, 7.10% machinists, 4.01% cutting/press operators, and 5.17% CNC operators/programmers.
- **S2** — [Metal and Plastic Machine Workers](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-22): BLS states that metal and plastic machine workers set up and operate equipment that shapes materials, that labor-saving CNC tools and robots are expanding, and projects the occupation group to decline 7% from 2024 to 2034.
- **S3** — [2022 Economic Census Metal Forging and Stamping Classification Form](https://bhs.econ.census.gov/ombpdfs2022/export/2022_MC-33212_su.pdf) (accessed 2026-07-22): Census identifies 332114 as custom roll forming metal products by rotary motion of rolls to bend or shape products.
- **S4** — [Project Profile: Acme Express](https://www.energy.gov/eere/solar/project-profile-acme-express-fy19-sbirsttr) (accessed 2026-07-22): DOE describes roll forming as a manufacturing process used to produce gutters and metal roofing and siding, supporting the physical end-use and construction link.
- **S5** — [Occupational Projections and Worker Characteristics](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): BLS projects rolling machine setter/operator/tender employment from 22,500 in 2024 to 20,600 in 2034, an 8% decline, while extruding and drawing machine employment is projected to rise 1%; used only as broad labor and technology context.
