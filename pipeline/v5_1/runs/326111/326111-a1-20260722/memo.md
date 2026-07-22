# 326111 — Plastics Bag and Pouch Manufacturing

*v5.1 Stage 1 research memo. Run `326111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.43 · L 0.92 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical packaging demand and sensor-rich converting lines make targeted AI-enabled quality, uptime, and planning improvements plausible.
**Weakness:** Competitive pass-through and accelerating plastic source-reduction mandates can erode both retained savings and demand.

## Business-model lens
- Included: US LMM firms that repeatedly convert plastics resin or film into bags and pouches for external food, healthcare, personal-care, retail, institutional, industrial, and other customers, including forming, coating, plastics-to-plastics laminating, printing, and pouch converting performed within the establishment.
- Excluded: Captive packaging operations, printing-only firms using purchased packaging, paper or foil combination bags classified outside 326111, film-only producers, pure distributors, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat B2B sale of specified physical packaging, typically driven by customer production volumes, purchase orders, qualification requirements, artwork and format changes, and recurring supply agreements; resin cost changes may be passed through contractually or at renewal.
- Deviation from default lens: none

## Executive view
Plastic bag and pouch converting is a coherent, repeat-supply industry with substantial physical production labor. AI can improve inspection, maintenance, scheduling, quoting, order and artwork handling, and inventory decisions, but competitive pricing and plastic-reduction rules constrain retained value and demand.

## How AI changes the work
High-speed webs, repetitive defects, expensive scrap, unplanned downtime, frequent changeovers, and complex order specifications create practical machine-vision and predictive-analytics use cases. The largest labor effects are likely in quality review, planning, maintenance support, customer workflow, and administration rather than eliminating line operators or technicians.

## Value capture
Converters retain more where barrier performance, food or medical qualification, printing, pouch complexity, short runs, and service create switching costs. Commodity bags face strong price competition, and resin escalators or contract renewals make cost economics visible to customers, encouraging sharing of savings.

## Firm availability
The injected population is 117 estimated LMM firms, and most should have repeat external orders. Target-level diligence must still exclude captive, distribution-heavy, spot-commodity, highly concentrated, owner-dependent, and compliance-deficient operations and verify that the paper-industry margin bridge identifies the EBITDA band accurately.

## Demand durability
Food, healthcare, personal-care, industrial, and protective uses sustain packaging demand and benefit from low weight and shelf-life performance. Single-use restrictions, EPR fees, reuse and refill systems, lightweighting, paper substitution, recycled-content constraints, and customer sustainability commitments create a material downside tail.

## Risks and uncertainty
The main risks are regulatory source reduction, resin and energy volatility, customer concentration, commoditization, capital intensity, quality recalls, food-contact requirements, and the possibility that large buyers capture most productivity gains. Evidence is mostly four-digit occupations and output plus large-company disclosures rather than LMM 326111 observations.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1719 | — | OBSERVED | — |
| n | — | 117 | — | ESTIMATE | — |
| a | 0.12 | 0.23 | 0.35 | PROXY | S2, S3 |
| rho | 0.4 | 0.58 | 0.73 | PROXY | S3 |
| e | 0.66 | 0.8 | 0.9 | ESTIMATE | S1, S5 |
| s5 | 0.14 | 0.23 | 0.34 | PROXY | S4 |
| q | 0.34 | 0.51 | 0.67 | ESTIMATE | S5 |
| d5 | 0.82 | 1.02 | 1.15 | PROXY | S5, S6, S7 |
| o | 0.88 | 0.96 | 0.99 | ESTIMATE | S1, S5, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.92 | 1.76 | PROXY |
| F | 3.97 | 5.01 | 5.80 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.22 | 9.79 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation proxy includes all plastics products and may overrepresent molding and assembly relative to film converting.
- a: BLS employment shares are not wage-weighted and do not indicate tasks already automated.
- a: NIST adoption evidence spans US manufacturing rather than flexible packaging.
- rho: The reported AI adoption figures include chatbots and do not measure labor implementation.
- rho: The range assumes plants can obtain reliable line and quality data without wholesale equipment replacement.
- rho: Food, medical, and other regulated packaging require more validation than commodity retail bags.
- e: No source directly measures eligibility in the LMM 326111 population.
- e: Physical product supply is treated as repeat outsourced provision under the fixed lens.
- e: The injected firm count uses a margin bridge from paper and forest products and may misclassify the LMM band.
- s5: Gallup is cross-industry and includes firms much smaller than the LMM band.
- s5: Survey intentions include gifts and other transfers that may not qualify.
- s5: Large-company consolidation is evidence of buyer interest but not an LMM probability measure.
- q: Berry is much larger and more diversified than the LMM lens.
- q: Retention is lower for commodity bags and higher for qualified food, medical, printed, or high-barrier pouches.
- q: Demand loss and implementation failure are excluded from q.
- d5: BLS output covers all plastics products, not bags and pouches.
- d5: Company disclosures mix regions and flexible products beyond 326111.
- d5: Regulation may reduce resin weight while preserving or increasing the number and value of more engineered pouches.
- o: The value is conditional on the quantity remaining in d5; eliminated single-use demand is not counted twice.
- o: Reusable or refill systems may shift demand to operators outside 326111 rather than remove accountable supply entirely.

## Sources
- **S1** — [2017 NAICS Definition File: 326111 Plastics Bag and Pouch Manufacturing](https://www.census.gov/naics/2017NAICS/2017_Definition_File.pdf) (accessed 2026-07-22): Defines the industry as converting resin or forming, coating, or plastics-to-plastics laminating film or sheet into bags and pouches, with printing allowed in the establishment.
- **S2** — [May 2023 Occupational Employment and Wage Estimates: Plastics Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-22): Reports production occupations at 58.94% of employment, metal and plastic workers at 25.97%, inspectors and testers at 5.17%, and transportation and material-moving occupations at 10.97%.
- **S3** — [NIST MEP: The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Reports 46% of manufacturers using AI tools and more than 80% expecting increased use in two years; identifies inspection, predictive maintenance, scheduling, forecasting, document management, and material handling use cases plus data, cost, skills, cybersecurity, and legacy-system barriers.
- **S4** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 52.3% of US employer businesses are owned by people age 55 or older and 22% of employer-business owners planned a sale or transfer within five years.
- **S5** — [Berry Global Group, Inc. 2024 Annual Report on Form 10-K](https://www.sec.gov/Archives/edgar/data/1378992/000114036124047881/form10k.htm) (accessed 2026-07-22): Describes flexible films and bags, stable consumer end markets, competition on service, innovation, quality and price, resin-price pass-through, packaging's protection and shelf-life roles, and recyclable or circular-material targets.
- **S6** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects plastics-product manufacturing real output from $190.7 billion to $212.4 billion in chained 2017 dollars over 2024-2034, a 1.1% annual growth rate.
- **S7** — [CalRecycle: California Approves New Plastic and Packaging Rules](https://calrecycle.ca.gov/2026/05/01/press-release-26-05/) (accessed 2026-07-22): States that producers have until 2032 to achieve 25% less plastic, with nearly half through elimination or reuse and refill, plus recyclable or compostable and recycling targets.
