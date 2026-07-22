# 332323 — Ornamental and Architectural Metal Work Manufacturing

*v5.1 Stage 1 research memo. Run `332323-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.23 · L 2.22 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A high labor share and document-intensive custom fabrication workflow create meaningful implementable AI opportunity.
**Weakness:** Competitive project bidding and volatile construction demand limit durable commercial retention.

## Business-model lens
- Included: Lower-middle-market contract manufacturers that repeatedly design-assist, detail, fabricate, and sometimes install architectural metal products such as staircases, railings, open steel flooring, fire escapes, and scaffolding for external contractors, architects, developers, and owners.
- Excluded: Captive fabrication shops, field-only installers without manufacturing, commodity distributors, structural-metal activities classified elsewhere, shells, and non-control financing vehicles.
- Customer and revenue model: Project-based B2B revenue under negotiated or competitively bid fixed-price contracts and purchase orders, with repeat general-contractor and institutional customer relationships, progress billing, and change orders for scope revisions.
- Deviation from default lens: none

## Executive view
Architectural metal fabrication pairs a high labor share with repeat outsourced project work and a large modeled LMM population. AI can materially improve estimating, detailing, BIM coordination, procurement, and project administration, but shop and field craftsmanship remains physical and pricing resets through competitive bids.

## How AI changes the work
The strongest applications are drawing ingestion, quantity takeoffs, parametric detail generation, code and specification checks, bid comparison, RFIs, submittals, production scheduling, purchasing, change-order documentation, and quality records. Experienced estimators, detailers, project managers, welders, fabricators, finishers, and installers remain essential for judgment and execution.

## Value capture
Fixed-price awards let a fabricator retain savings on current work, especially when digital coordination prevents rework. Future bids, contractor negotiation, and transparent labor-hour assumptions progressively share those gains, while scope gaps and change-order disputes can erase them.

## Firm availability
The industry is fragmented and most true manufacturers fit the repeat external-customer lens. Transfer quality depends on management depth, backlog, customer concentration, bonding, safety, working capital, equipment condition, and whether estimating and relationships reside only with the owner.

## Demand durability
Demand tracks a currently uneven construction market: data centers, healthcare, recreation, and some institutional work grow while other commercial and manufacturing categories lag. Physical custom metal remains operator-required even when AI improves its design path.

## Risks and uncertainty
Cyclic project demand, tariffs and steel prices, fixed-price overruns, inaccurate takeoffs, late design changes, rework, skilled-labor constraints, safety, bonding, retainage, customer concentration, and owner dependence can outweigh indirect-labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3039 | — | OBSERVED | — |
| n | — | 424 | — | ESTIMATE | — |
| a | 0.2 | 0.31 | 0.43 | PROXY | S1, S2, S3 |
| rho | 0.41 | 0.59 | 0.74 | ESTIMATE | S2, S4 |
| e | 0.62 | 0.78 | 0.9 | ESTIMATE | S3, S5 |
| s5 | 0.14 | 0.23 | 0.35 | PROXY | S6 |
| q | 0.34 | 0.5 | 0.67 | PROXY | S2 |
| d5 | 0.9 | 1.02 | 1.15 | PROXY | S5 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.00 | 2.22 | 3.87 | ESTIMATE |
| F | 5.84 | 6.99 | 7.89 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | PROXY |
| D | 7.92 | 9.69 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source is three-digit fabricated metal manufacturing.
- a: The operating example is a much larger structural-steel fabricator and may overstate BIM sophistication.
- rho: No representative adoption study for LMM ornamental-metal firms was found.
- rho: The estimate assumes structured digital drawings and excludes autonomous shop or field work.
- e: Eligibility is not observed for the injected firm list.
- e: Some establishments may combine fabrication, erection, and adjacent structural-metal work across NAICS boundaries.
- s5: The source measures plans, not completed qualifying transfers.
- s5: Its population is broader and generally smaller than the LMM band.
- q: Structural-steel project economics are only a proxy for ornamental and architectural metal.
- q: No evidence directly measures AI savings pass-through.
- d5: Construction spending is nominal and broader than the current service basket.
- d5: Demand varies materially by geography and project type.
- o: Operator persistence is inferred from physical fabrication and project accountability rather than observed directly.
- o: Highly standardized railings or stairs may shift to catalog products more rapidly than bespoke work.

## Sources
- **S1** — [May 2022 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 332000](https://www.bls.gov/oes/2022/may/naics3_332000.htm) (accessed 2026-07-22): Broader fabricated-metal occupation mix used to bound wage-weighted task exposure.
- **S2** — [INNOVATE Corp. 2024 Annual Report: DBM Global](https://www.sec.gov/Archives/edgar/data/1006837/000100683725000021/vate-20241231.htm) (accessed 2026-07-22): Steel fabrication, design-assist, BIM, detailing, project delivery, fragmentation, backlog, customer concentration, and fixed-price contract mechanics.
- **S3** — [2022 Economic Census Questionnaire: Fabricated Structural Metal Manufacturing](https://bhs.econ.census.gov/ombpdfs2022/export/2022_MC-33232_su.pdf) (accessed 2026-07-22): Official activity definition for ornamental and architectural metal work including staircases, flooring, railings, and scaffolding, plus production and nonproduction role context.
- **S4** — [2026 Roadmap on Artificial Intelligence and Machine Learning for Smart Manufacturing](https://www.nist.gov/publications/2026-roadmap-artificial-intelligence-and-machine-learning-smart-manufacturing) (accessed 2026-07-22): Industrial AI opportunities and deployment barriers involving integration, data, reliability, explainability, and safety.
- **S5** — [July 2026 Consensus Construction Forecast](https://www.aia.org/resource-center/july-2026-consensus-construction-forecast) (accessed 2026-07-22): Current nonresidential construction conditions, 2026-2027 forecasts, sector divergence, and architecture-billings leading evidence.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): U.S. employer-business five-year sale and transfer intentions.
