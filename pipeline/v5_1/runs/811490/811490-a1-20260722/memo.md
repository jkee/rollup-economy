# 811490 — Other Personal and Household Goods Repair and Maintenance

*v5.1 Stage 1 research memo. Run `811490-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.92 · L 1.89 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Physical intervention on valuable or specialized goods keeps most surviving demand tied to accountable operators.
**Weakness:** The code's extreme subsector heterogeneity can make aggregate estimates poor guides to any actual acquisition candidate.

## Business-model lens
- Included: US LMM firms repairing or servicing personal and household goods not assigned to the excluded repair industries, including garments, watches, jewelry, musical instruments, bicycles, motorcycles, and recreational boats, when supplied as repeat outsourced services to external customers.
- Excluded: Retail of new goods, home and garden equipment repair, appliance repair, furniture repair or reupholstery, footwear and leather-goods repair, captive internal units, shells, non-control financing vehicles, and firms outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: A heterogeneous mix of consumer and small-business repair revenue, usually per job or service event after inspection, with some maintenance plans, fleet or dealer relationships, storage-linked boat work, and repeat institutional accounts.
- Deviation from default lens: none; the full NAICS scope is retained, but heterogeneity is flagged and reflected in wide ranges rather than selecting an attractive subsector.

## Executive view
This is a broad collection of physically defensible repair services with moderate AI opportunity in administration and technician support. A small LMM acquisition population exists in the frozen data, but subsector heterogeneity and owner-dependent craft skill make a code-level thesis unreliable without firm-by-firm classification.

## How AI changes the work
AI can improve intake from text or images, quote and work-order drafting, troubleshooting support, parts research, customer updates, scheduling, records, inventory, marketing, and bookkeeping. Garment fitting and sewing, instrument tuning, precision calibration, mechanical disassembly, fabrication, and final quality control remain physical operator work.

## Value capture
Most per-job pricing permits initial retention, while competitive repair markets share some savings through price and turnaround. Scarce-skill and high-value-asset niches may retain more; dealer, insurer, fleet, or contract channels may retain less.

## Firm availability
The frozen dataset estimates 48 LMM-band firms, but only a bounded share is likely independent, repeat-service-oriented, and transferable without the owner. Boat, motorcycle, and multi-location repair operations are more likely to reach scale than tailoring, watch, or instrument crafts.

## Demand durability
Representative BLS outlooks range from material decline in camera repair to slight growth in musical-instrument and other precision repair. The aggregate base is near stable, but the result is highly sensitive to subsector mix and repair-versus-replace economics.

## Risks and uncertainty
The NAICS definition combines radically different labor, safety, seasonality, ticket size, and customer models. Occupation proxies omit several major categories; there is no direct task-share, benefit-retention, transaction, or constant-quality demand series; and the 48-firm count is margin-bridged rather than observed.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3589 | — | OBSERVED | — |
| n | — | 48 | — | ESTIMATE | — |
| a | 0.11 | 0.24 | 0.39 | PROXY | S1, S2, S3, S4 |
| rho | 0.36 | 0.55 | 0.72 | ESTIMATE | S2, S3, S4 |
| e | 0.32 | 0.54 | 0.73 | ESTIMATE | S1 |
| s5 | 0.07 | 0.14 | 0.22 | PROXY | S6 |
| q | 0.39 | 0.58 | 0.76 | ESTIMATE | S1 |
| d5 | 0.85 | 0.98 | 1.11 | PROXY | S5, S7 |
| o | 0.86 | 0.95 | 0.99 | PROXY | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.57 | 1.89 | 4.03 | ESTIMATE |
| F | 1.17 | 2.46 | 3.48 | ESTIMATE |
| C | 7.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.31 | 9.31 | 10.00 | PROXY |

## Caveats
- a: No single occupation represents the NAICS code, and the cited occupations omit important bicycle, motorcycle, jewelry, watch, and boat-repair labor.
- a: O*NET task importance is not an industry wage-weighted time share.
- rho: The estimate is not a measured industry adoption rate.
- rho: Implementation will differ sharply between a tailor, a motorcycle shop, and a boat-service operator.
- e: The frozen n=48 is a margin-bridged estimate and is not re-estimated here.
- e: The eligibility share may vary more by subsector than the range captures.
- s5: Gallup is cross-industry and not limited to LMM firms.
- s5: Stated plans do not measure completed transfers or distinguish all qualifying control outcomes.
- q: No observed benefit-retention study was found.
- q: Commercial retention for marine or motorcycle service may differ materially from tailoring or watch repair.
- d5: BLS occupation employment is not constant-quality demand and only partially maps to NAICS 811490.
- d5: The NAICS code's subsector mix is unknown, so equal qualitative weighting can misstate the aggregate.
- d5: EPA repair context is directional and does not quantify consumer spending.
- o: Representative occupations do not cover every service in the code.
- o: The estimate separates operator elimination from demand loss, but real repair-versus-replace behavior can blur that boundary.

## Sources
- **S1** — [2022 NAICS Definition: 811490 Other Personal and Household Goods Repair and Maintenance](https://www.census.gov/naics/?details=811490&input=811490&year=2022) (accessed 2026-07-22): Official industry scope and examples, including garments, watches, jewelry, musical instruments, bicycles, motorcycles, and recreational boats, used for the lens, a, e, and q.
- **S2** — [Tailors, Dressmakers, and Custom Sewers](https://www.onetonline.org/link/details/51-6052.00) (accessed 2026-07-22): Garment measuring, fitting, stitch removal, sewing, and alteration tasks plus bookkeeping, CAD, CRM, inventory, and office software used for a, rho, and o.
- **S3** — [Musical Instrument Repairers and Tuners](https://www.onetonline.org/link/details/49-9063.00) (accessed 2026-07-22): Physical tuning, testing, disassembly, soldering, part repair, fabrication, finishing, and reassembly tasks used for a, rho, and o.
- **S4** — [Camera and Photographic Equipment Repairers](https://www.onetonline.org/link/summary/49-9061.00) (accessed 2026-07-22): Physical adjustment, disassembly, testing, calibration, diagnosis, fabrication, documentation, computer use, and estimation activities used for a, rho, and o.
- **S5** — [Occupational Projections and Worker Characteristics, 2024-2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Ten-year employment projections of -15.1% for camera repairers, -4.5% for tailors and custom sewers, -1.1% for watch repairers, +1.4% for musical-instrument repairers, and +2.0% for other precision-equipment repairers, used as d5 proxies.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey finding that 22% of employer-business owners planned to sell or transfer ownership within five years, used as the s5 proxy.
- **S7** — [About the Model Recycling Program Toolkit](https://www.epa.gov/circulareconomy/about-model-recycling-program-toolkit) (accessed 2026-07-22): Federal circular-economy context explicitly encompassing reuse and repair, used only as a directional d5 consideration.
