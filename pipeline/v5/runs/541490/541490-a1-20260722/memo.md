# 541490 — Other Specialized Design Services

*v5 Stage 1 research memo. Run `541490-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 5.25 · L 3.26 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can reduce effort in repeatable research, visualization, specification, and coordination around operator-led product design.
**Weakness:** Observed evidence does not isolate transferable repeat-service firms or their demand, pricing, and transaction behavior within NAICS 541490.

## Business-model lens
- Included: US outsourced fashion, footwear, jewelry, textile, and related product-design studios serving external business customers on repeat seasonal, collection, or product-development engagements.
- Excluded: One-off event float and costume work, independent theatrical designers, manufacturers selling their own goods, captive design teams, nonrepeat consumer commissions, shells, and financing vehicles.
- Customer and revenue model: External manufacturers, brands, retailers, and wholesalers buy fixed-fee, retainer, or repeat project design, specification, material-selection, and development services.
- Deviation from default lens: Narrowed for coherence because NAICS 541490 combines recurring product-design studios with episodic float and costume work; the latter does not share a repeat outsourced-service revenue model.

## Executive view
The coherent repeat-service subset of NAICS 541490 is outsourced product-design work for brands and manufacturers. It offers practical workflow assistance but faces a narrow eligible population, uncertain transfers, and meaningful risk that AI tools shift work toward customers or lower-priced competitors.

## How AI changes the work
AI can shorten reference research, concept variation, rough visual development, drafting support, documentation, costing support, and administrative coordination. Designers remain responsible for client discovery, original direction, material selection, sample and production validation, and approval decisions.

## Value capture
Fixed-fee and retainer engagements create some room to retain productivity gains, particularly before renewal. Repeat buyers can nevertheless seek lower fees, more options, or shorter delivery cycles, while time-based engagements make savings visible and easier to pass through.

## Firm availability
The injected LMM population must be filtered for repeat external service revenue, independence, and transferability. Census owner-characteristic data can inform follow-up, but it does not measure qualifying sales, so the transfer assumption remains a bounded judgment.

## Demand durability
BLS projects fashion-designer employment to grow 2 percent from 2024 to 2034, supporting a near-flat proxy for the included service basket. Buyers should still need accountable partners for brand, material, prototype, and production choices even as some early-stage work becomes software-assisted.

## Risks and uncertainty
This NAICS code mixes several business models, and the data do not isolate the repeat-service subset. Six-digit occupation, pricing, retention, transaction, and constant-price demand data are absent. Customer concentration, rights ownership, seasonality, and internalization could materially weaken the assumptions.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5889 | — | OBSERVED | — |
| n | — | 82 | — | ESTIMATE | — |
| a | 0.25 | 0.38 | 0.52 | ESTIMATE | S2, S3 |
| rho | 0.25 | 0.4 | 0.55 | ESTIMATE | S2 |
| e | 0.45 | 0.62 | 0.75 | ESTIMATE | S1 |
| s5 | 0.08 | 0.13 | 0.2 | ESTIMATE | S5 |
| q | 0.25 | 0.38 | 0.52 | ESTIMATE | — |
| d5 | 0.92 | 1.01 | 1.08 | PROXY | S4 |
| o | 0.5 | 0.65 | 0.78 | ESTIMATE | S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.47 | 3.58 | 6.74 | ESTIMATE |
| F | 2.21 | 3.26 | 4.16 | ESTIMATE |
| C | 5.00 | 7.60 | 10.00 | ESTIMATE |
| D | 4.60 | 6.57 | 8.42 | ESTIMATE |

## Caveats
- a: No published occupation mix exists for six-digit NAICS 541490 or the narrowed repeat-service lens.
- a: The estimate excludes already automated work and does not assume generated output is commercially acceptable.
- rho: This is an implementation judgment, not an AI-capability forecast.
- rho: Small studios may lack integration capacity, while standardized high-volume work may implement faster.
- e: The injected firm count is not re-estimated here.
- e: NAICS classification does not identify repeat revenue, control eligibility, or whether design is sold separately from goods.
- s5: Owner age is only a potential succession indicator; it does not establish sale probability.
- s5: The estimate excludes closures without a transferable operating business and internal reorganizations.
- q: This is a commercial-retention judgment and excludes demand-volume effects and implementation constraints.
- q: Revenue-model shares are unavailable for the narrowed lens.
- d5: Employment is not constant-price service quantity and is national rather than lens-specific.
- d5: The projection covers fashion designers, not all included specialized-design activities.
- o: The boundary between software-assisted service and self-service may change quickly.
- o: This quantity judgment is separate from labor implementation and client price capture.

## Sources
- **S1** — [2022 NAICS definition: 541490 Other Specialized Design Services](https://www.census.gov/naics/?details=541490&input=541490&year=2022) (accessed 2026-07-22): Industry scope and illustrative activities, including fashion, shoe, jewelry, textile, costume, and float design, plus excluded design industries.
- **S2** — [O*NET OnLine: Fashion Designers](https://www.onetonline.org/link/summary/27-1022.00) (accessed 2026-07-22): Fashion-designer tasks including design, sketches, specifications, client discussions, material selection, sample review, market research, testing, and coordination.
- **S3** — [BLS OEWS largest occupations in Specialized Design Services, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Sector occupation mix: interior designers 29,610; graphic designers 25,220; general and operations managers 10,820; project management specialists 4,610; office clerks 4,410; and market research analysts 3,090.
- **S4** — [BLS Occupational Outlook Handbook: Fashion Designers](https://www.bls.gov/ooh/arts-and-design/fashion-designers.htm) (accessed 2026-07-22): BLS projects fashion-designer employment to grow 2 percent from 2024 to 2034 and reports 2,300 average annual openings.
- **S5** — [Census Annual Business Survey: Characteristics of Business Owners, 2022 tables](https://www.census.gov/data/tables/2022/econ/abs/2022-abs-characteristics-of-owners.html) (accessed 2026-07-22): Availability of employer-business owner-characteristic tables, including owner age, for succession diligence; the 2022 ABS covers reference year 2021.
