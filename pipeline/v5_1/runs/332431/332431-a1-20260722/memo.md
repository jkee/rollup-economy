# 332431 — Metal Can Manufacturing

*v5.1 Stage 1 research memo. Run `332431-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.07 · L 0.36 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring high-volume customer demand and local supply relationships make the operating basket highly durable.
**Weakness:** A tiny, concentrated target universe and already-automated production leave limited addressable labor and strong customer bargaining power.

## Business-model lens
- Included: US lower-middle-market independent manufacturers supplying metal cans, lids, and ends on recurring or repeat contracts to external food, beverage, pet-food, aerosol, and general-line customers.
- Excluded: Captive can plants, shells, non-control financing vehicles, firms outside the EBITDA band, pure distributors, and producers whose qualifying can manufacturing operation is not independently transferable.
- Customer and revenue model: High-volume cans and ends are supplied repeatedly under annual or multi-year agreements, frequently from plants near customer filling operations; specialty and general-line cans may use shorter quoted runs, but revenue still depends on recurring packaging demand and customer qualification.
- Deviation from default lens: none

## Executive view
Metal cans provide unusually repeatable physical demand but limited current labor exposure because high-speed production is already automated and the frozen compensation ratio is low. AI is most credible in inspection, maintenance, planning, yield, specification, and indirect workflows rather than direct line substitution.

## How AI changes the work
AI can improve defect detection, predict equipment failures, optimize schedules and changeovers, analyze scrap and yield, manage specifications, forecast demand, and automate office work. Continuous production, mature controls, food-contact quality, uptime requirements, and customer validation limit rapid replacement of remaining operating labor.

## Value capture
Multi-year arrangements provide volume visibility, but pricing formulas, renewal negotiations, productivity expectations, and concentrated buyers share gains. Specialty designs, decoration, tooling, or scarce local capacity can preserve more benefit than commodity food or beverage cans.

## Firm availability
The frozen count is only 19 and the market is dominated by large strategic producers, so the investable independent population is likely small. Specialty and general-line firms may qualify, but captive plants, dedicated assets, and strategic ownership reduce eligibility and transaction frequency.

## Demand durability
Cans remain essential for recurring packaged-food, beverage, pet-food, aerosol, and general-line applications. Recent large-company unit trends are positive, but material substitution, overcapacity, customer concentration, crop cycles, consumer preferences, and packaging regulation keep growth modest and uneven.

## Risks and uncertainty
The largest uncertainties are the true number of independent LMM firms, current automation baselines, and contract-specific sharing of productivity. Customer loss, dedicated-plant economics, metal and energy costs, coating rules, quality failures, transport radius, and alternative packaging can dominate AI benefits.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0912 | — | OBSERVED | — |
| n | — | 19 | — | ESTIMATE | — |
| a | 0.09 | 0.17 | 0.27 | PROXY | S1, S2, S3, S4 |
| rho | 0.36 | 0.58 | 0.75 | ESTIMATE | S3, S4 |
| e | 0.35 | 0.55 | 0.72 | ESTIMATE | S1, S5 |
| s5 | 0.1 | 0.18 | 0.28 | PROXY | S6 |
| q | 0.24 | 0.41 | 0.59 | PROXY | S5 |
| d5 | 0.94 | 1.06 | 1.18 | PROXY | S5, S7 |
| o | 0.93 | 0.98 | 0.998 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.12 | 0.36 | 0.74 | ESTIMATE |
| F | 0.82 | 1.70 | 2.53 | ESTIMATE |
| C | 4.80 | 8.20 | 10.00 | PROXY |
| D | 8.74 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation data are for the broader fabricated-metal subsector.
- a: Current automation intensity varies between high-speed beverage and food-can plants and smaller specialty-can producers.
- rho: Manufacturing-wide AI surveys overrepresent larger organizations relative to the target lens.
- rho: Some apparent AI gains are conventional controls, machine vision, or robotics rather than AI substitution.
- e: The frozen firm count is margin-bridged and may misclassify firms in a concentrated industry.
- e: Silgan's greater-than-half US food-can share is a large-company market signal, not a direct count of eligible LMM firms.
- s5: Gallup is cross-industry and measures plans, not completed qualifying transfers.
- s5: Plant acquisitions by strategic buyers may not represent acquisition of an independent lens firm.
- q: Silgan is the dominant US metal-food-can producer and may face different bargaining dynamics than specialty LMM suppliers.
- q: Contract terms vary by can type, customer, decoration, tooling, and plant dedication.
- d5: Public-company figures are global or multi-region and can include market-share changes.
- d5: Unit volume is not a constant-quality measure because can sizes, gauges, decoration, and end types change.
- o: Alternative packaging can eliminate metal-can units even when packaged-product demand persists.
- o: Consolidation can move production to a different operator without eliminating the need for an operator.

## Sources
- **S1** — [2022 NAICS Definition: Metal Can Manufacturing](https://www.census.gov/naics/?details=332431&input=332431&year=2022) (accessed 2026-07-22): Defines NAICS 332431 as establishments manufacturing metal cans, lids, and ends.
- **S2** — [Fabricated Metal Product Manufacturing: NAICS 332](https://www.bls.gov/iag/tgs/iag332.htm) (accessed 2026-07-22): Provides broader-subsector occupation evidence, including large employment in assemblers, welders, machinists, press operators, and production supervisors.
- **S3** — [2026 Roadmap on Artificial Intelligence and Machine Learning for Smart Manufacturing](https://www.nist.gov/publications/2026-roadmap-artificial-intelligence-and-machine-learning-smart-manufacturing) (accessed 2026-07-22): Identifies AI manufacturing applications and the data, integration, explainability, reliability, and safety barriers to industrial deployment.
- **S4** — [Shaping the AI-Powered Factory of the Future](https://documents.nam.org/tech/Shaping-the-AI-Powered-Factory-of-the-Future-Report.pdf) (accessed 2026-07-22): Reports only 18% of surveyed manufacturers have a formal operational AI strategy, with data availability, format, skills, culture, and legacy systems cited as barriers.
- **S5** — [Silgan Holdings Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/849869/000162828026012202/slgn-20251231.htm) (accessed 2026-07-22): Reports greater-than-half US metal-food-can share, about 90% of projected 2026 metal-container sales under multi-year arrangements, metal-cost pass-through, a 300-mile general sales radius, 3% 2025 unit growth, and competition from other packaging materials.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Gallup reports that 22% of US employer-business owners planned a sale, transfer, or public offering within five years and 52.3% of employer businesses are owned by people age 55 or older.
- **S7** — [Crown Holdings, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1219601/000162828026012904/cck-20251231.htm) (accessed 2026-07-22): Reports recent global beverage-can demand growth, demand drivers including new products and sustainability, and risks from overcapacity, customer loss, packaging preferences, regulation, and metal supply.
