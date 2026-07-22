# 541410 — Interior Design Services

*v5 Stage 1 research memo. Run `541410-a2-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 2.*

**Base tier:** CONDITIONAL · A 6.72 · L 2.15 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Workflow acceleration in documentation, visualization, research, estimating, and coordination while retaining accountable professional delivery.
**Weakness:** Limited public evidence on qualifying transfers and a project-based, founder-dependent revenue model with mixed fee pass-through.

## Business-model lens
- Included: Independent interior-design firms that provide repeat or recurring outsourced planning, design development, specifications, procurement coordination, construction-administration, or project-management services to external residential, commercial, hospitality, healthcare, and retail customers.
- Excluded: Captive in-house design departments, furniture-store services supplied free with merchandise, one-off decorative retail sales without an outsourced service relationship, shells, and non-control financing vehicles.
- Customer and revenue model: Project-based professional services, commonly billed through hourly, fixed, cost-plus, percentage-of-project-cost, or combined fee arrangements; repeat revenue arises from renovation cycles, multi-site customers, referrals, and ongoing customer relationships rather than a pure subscription.
- Deviation from default lens: none

## Executive view
Interior design services combine digitally assistable documentation and coordination work with site-specific, client-facing, and accountable professional delivery. The opportunity depends on converting workflow acceleration into capacity while preserving design quality and customer trust.

## How AI changes the work
AI can assist drafting, rendering, research, specifications, estimates, product search, and internal communication. It is less suited to independently owning client discovery, code and accessibility judgment, contractor coordination, site verification, or final design accountability.

## Value capture
Fee structures span hourly, fixed, cost-plus, percentage, and hybrid arrangements. Fixed engagements may retain efficiency during a project, while hourly rates, cost-plus margins, competitive bidding, and later repricing can share gains with customers.

## Firm availability
The eligible population is limited to transferable LMM firms with external-service revenue and a durable operation beyond the founder. Public evidence does not identify the five-year rate of qualifying control transfers, making target-level deal and succession diligence necessary.

## Demand durability
BLS projects modest occupational growth and identifies renovation, building-code, and accessibility needs as demand supports. Demand is project-driven and exposed to construction and discretionary-spending cycles rather than contractually recurring revenue alone.

## Risks and uncertainty
Occupation data are an imperfect proxy for the industry wage mix and service demand. Founder dependence, varied state rules, heterogeneous residential and commercial work, private transaction opacity, and incomplete evidence on AI adoption and contract pass-through widen the ranges.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2359 | — | OBSERVED | — |
| n | — | 313 | — | ESTIMATE | — |
| a | 0.28 | 0.38 | 0.5 | ESTIMATE | S1, S2 |
| rho | 0.45 | 0.6 | 0.73 | ESTIMATE | S1, S2 |
| e | 0.65 | 0.78 | 0.88 | ESTIMATE | S3 |
| s5 | 0.07 | 0.13 | 0.21 | ESTIMATE | — |
| q | 0.42 | 0.56 | 0.7 | ESTIMATE | S4 |
| d5 | 0.98 | 1.015 | 1.04 | PROXY | S1 |
| o | 0.8 | 0.9 | 0.96 | ESTIMATE | S1, S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.19 | 2.15 | 3.44 | ESTIMATE |
| F | 4.38 | 5.61 | 6.55 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.84 | 9.13 | 9.98 | ESTIMATE |

## Caveats
- a: The sources describe the Interior Designers occupation, not the entire wage mix of NAICS 541410 firms.
- a: The frozen compensation-to-receipts input has a QCEW-versus-SUSB vintage and coverage mismatch; this task-share estimate does not correct it.
- a: Source task descriptions do not measure AI task performance or adoption.
- rho: No source measures five-year implemented AI savings for this NAICS industry.
- rho: State-specific title, licensure, and code requirements can materially change implementation speed.
- e: Census product definitions establish the service scope but do not measure eligibility or transferability.
- e: The injected LMM firm count is an estimate derived from size-class bridging and is not re-estimated here.
- s5: No reachable public source was found that reports five-year qualifying-control-transfer incidence for the defined NAICS 541410 LMM population.
- s5: Observed announcement counts would understate private small-business sales and would not identify qualifying control transfers reliably.
- q: The ASID chapter guidance describes fee methods, not their national revenue shares or pass-through behavior.
- q: Residential and commercial work can have materially different fee mixes and buyer power.
- d5: Employment is not output or constant-quality demand and covers designers working outside specialized design services.
- d5: The BLS projection spans 2024 to 2034 and may not capture near-term construction cycles or changes in service mix.
- o: Sources establish task and service characteristics, not the future share of demand served without an accountable operator.
- o: The estimate may be too high in low-complexity residential decorating and too low for regulated or complex commercial projects.

## Sources
- **S1** — [Interior Designers: Occupational Outlook Handbook](https://www.bls.gov/ooh/arts-and-design/interior-designers.htm) (accessed 2026-07-22): BLS describes duties including plans, specifications, cost estimates, installation oversight, contractor coordination, site visits, codes, CAD/BIM use, 2024 employment, and projected 3 percent employment growth from 2024 to 2034; it also identifies renovation, codes, and accessibility as demand factors.
- **S2** — [O*NET OnLine: Interior Designers, 27-1025.00](https://www.onetonline.org/link/details/27-1025.00) (accessed 2026-07-22): O*NET lists core work including ADA-compliant planning, CAD construction documents, code research, client consultation, contractor coordination, shop-drawing review, inspection, materials selection, cost estimation, and presentation.
- **S3** — [Census NAPCS Product List for NAICS 54141: Interior Design Services](https://www2.census.gov/library/reference/napcs/product-list/web-54141-final-reformatted-edited-us082208.pdf) (accessed 2026-07-22): Census product definitions identify full-service and other interior-design services for residential, nonresidential, hospitality, and retail customers, including programming, design development, specifications, construction documents, and construction contract administration.
- **S4** — [American Society of Interior Designers Minnesota: Costs and Fees](https://mn.asid.org/costs) (accessed 2026-07-22): ASID Minnesota describes fixed, hourly, and cost-plus fee methods, says most residential and many commercial designers use or combine them, and explains that cost-plus compensates the designer through an agreed percentage.
