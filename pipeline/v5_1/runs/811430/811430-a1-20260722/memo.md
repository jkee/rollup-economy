# 811430 — Footwear and Leather Goods Repair

*v5.1 Stage 1 research memo. Run `811430-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.24 · L 0.00 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Physical, item-specific bench work keeps almost all surviving service demand operator-required.
**Weakness:** The frozen estimate of zero LMM-band firms leaves little credible acquisition population despite a defensible service.

## Business-model lens
- Included: US firms repairing footwear and leather or leather-like personal goods for external customers, including sole, heel, zipper, lining, handbag, belt, luggage, dyeing, cleaning, and related repair work, where customers use the service repeatedly or the firm has repeat referral and institutional demand.
- Excluded: Retailers primarily selling new footwear or leather goods, shoe shining without repair, repair of leather clothing classified elsewhere, captive repair units, shells, non-control financing vehicles, and firms outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: Mostly consumer-paid, per-job repair charges, with some recurring commercial or institutional accounts and mail-in work; pricing is generally fixed by job after inspection rather than cost-plus.
- Deviation from default lens: none

## Executive view
Footwear and leather-goods repair is a physically defensible service with limited but useful AI opportunity in intake and administration. Its central weakness is firm availability: the frozen dataset estimates no operators in the LMM band, and the trade remains highly fragmented and craft-dependent.

## How AI changes the work
AI can draft estimates and customer messages, classify incoming jobs from photos, retrieve repair knowledge, support scheduling and parts inventory, and automate bookkeeping or marketing. Technicians must still inspect, disassemble, cut, stitch, glue, refinish, and quality-check each item.

## Value capture
Per-job pricing lets a shop initially retain labor savings, but transparent local prices and low switching costs should share gains through price, turnaround, or service improvements. Luxury restoration may retain more than commodity repairs.

## Firm availability
The prompt's frozen n=0 is the binding issue. Repeat demand exists, but most operators appear too small and owner-dependent for the default LMM lens, and succession may transfer a craft job rather than a scalable organization.

## Demand durability
BLS projects only a modest decline for the relevant occupation, consistent with a stable-to-slightly-declining base. Repair and reuse interest helps, but inexpensive replacement products and shortages of trained craftspeople constrain demand fulfillment.

## Risks and uncertainty
There is no industry-specific task study, implementation cohort, transaction series, or constant-quality demand series. Owner labor may be understated in wage data; occupation data mix production and repair; and the economics differ between shoe repair and high-value leather restoration.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4037 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.08 | 0.17 | 0.29 | PROXY | S1, S2, S6 |
| rho | 0.34 | 0.53 | 0.7 | ESTIMATE | S2 |
| e | 0.2 | 0.4 | 0.6 | ESTIMATE | S1, S6 |
| s5 | 0.07 | 0.14 | 0.22 | PROXY | S4 |
| q | 0.36 | 0.55 | 0.73 | ESTIMATE | S1, S6 |
| d5 | 0.89 | 0.98 | 1.09 | PROXY | S3, S5 |
| o | 0.91 | 0.97 | 0.995 | PROXY | S2, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.44 | 1.45 | 3.28 | ESTIMATE |
| F | 0.00 | 0.00 | 0.00 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 8.10 | 9.51 | 10.00 | PROXY |

## Caveats
- a: O*NET is occupation-level and includes shoe and leather production work outside NAICS 811430.
- a: No industry wage-weighted task inventory was found; the range is intentionally wide.
- rho: This is a bounded implementation judgment, not a measured adoption rate.
- rho: The frozen dataset reports no estimated firms in the LMM band, so implementation evidence from sufficiently scaled operators may be scarce.
- e: The frozen n=0 estimate is not re-estimated here and makes the transferable-firm opportunity effectively unavailable in the dataset.
- e: Repeat consumer use may be episodic rather than contractually recurring.
- s5: Gallup covers all US employer businesses, not this industry or the LMM band.
- s5: Stated plans overstate completed qualifying transfers and do not distinguish every control structure.
- q: No direct evidence was found on benefit sharing or repricing after automation.
- q: Retention could differ materially between luxury restoration, commodity shoe repair, and institutional accounts.
- d5: Occupational employment is not service quantity and includes work outside the industry.
- d5: EPA material is directional policy context, not an industry demand forecast.
- d5: The range does not assume that circular-economy messaging converts into paid repair demand.
- o: The proxy does not measure future robotics adoption.
- o: Mail-in platforms may change which operator performs the work without eliminating operator requirement.

## Sources
- **S1** — [2022 NAICS Definition: 811430 Footwear and Leather Goods Repair](https://www.census.gov/naics/?details=811430&input=811430&year=2022) (accessed 2026-07-22): Industry scope, exclusions, and physical repair service model used for the lens, a, e, and q.
- **S2** — [Shoe and Leather Workers and Repairers](https://www.onetonline.org/link/summary/51-6041.00) (accessed 2026-07-22): Physical repair tasks plus estimating, payment, inventory, POS, accounting, and office-software activities used for a, rho, and o.
- **S3** — [Occupational Projections and Worker Characteristics, 2024-2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Shoe and Leather Workers and Repairers employment of 9,500 in 2024 and 9,100 in 2034, a 3.8% decline, used as a d5 proxy.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey finding that 22% of employer-business owners planned to sell or transfer ownership within five years, used as the s5 proxy.
- **S5** — [About the Model Recycling Program Toolkit](https://www.epa.gov/circulareconomy/about-model-recycling-program-toolkit) (accessed 2026-07-22): Federal circular-economy context explicitly encompassing reuse and repair, used only as a directional d5 consideration.
- **S6** — [NAPCS Product List for NAICS 8114 Personal and Household Goods Repair and Maintenance](https://www2.census.gov/library/reference/napcs/product-list/web-8114-final-reformatted-edited-us061509.pdf) (accessed 2026-07-22): Repair-product detail including sole, heel, zipper, lining, handbag, belt, dyeing, polishing, cleaning, and related services used for the lens, a, e, q, and o.
