# 459910 — Pet and Pet Supplies Retailers

*v5.1 Stage 1 research memo. Run `459910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Recurring pet-care relationships combine resilient household demand with automatable scheduling, support, marketing, and administrative workflows.
**Weakness:** The eligible service-heavy LMM population is unmeasured and likely a minority of a code defined primarily by merchandise retail.

## Business-model lens
- Included: U.S. lower-middle-market pet and pet-supply retailers that repeatedly provide external customers with operator-delivered services such as grooming, training, self-wash support, care-plan coordination, or other recurring in-store pet-care workflows alongside merchandise sales.
- Excluded: Product-only pet retailers, software-only sellers, captive units, noncommercial shelters, veterinary practices, establishments primarily engaged in grooming or boarding, and firms outside the roughly $1-10 million normalized EBITDA band.
- Customer and revenue model: The qualifying firm receives recurring fixed-fee, package, membership, or appointment revenue from pet owners for hands-on or coordinated pet services, often using food and supply retail to acquire and retain the same households.
- Deviation from default lens: The code is heterogeneous between product-only retailers and integrated retail-service operators. The lens retains only retailers with a repeat outsourced pet-service workflow; firms primarily engaged in grooming, boarding, or veterinary care are excluded because Census classifies those activities outside 459910.

## Executive view
The relevant opportunity lies in integrated pet retailers, not product-only stores. Repeat grooming, training, wash, and care-coordination relationships create a service business with automatable front- and back-office work, while essential physical handling and customer trust preserve an operator role. Eligibility and LMM availability remain poorly measured.

## How AI changes the work
AI can handle appointment intake, reminders, routine service questions, personalized outreach, product and service recommendations, employee knowledge retrieval, schedule optimization, purchasing support, demand forecasts, and bookkeeping. It cannot safely replace most grooming, animal handling, facility work, in-person behavior assessment, or accountable exception management.

## Value capture
Fixed consumer prices and repeat relationships permit meaningful initial retention, particularly when convenience and trusted staff differentiate the operator. Retention declines as chains and local competitors deploy similar tools, promotions reset expectations, and customers compare prices or shift simple advice and training online.

## Firm availability
Pet stores demonstrably transact, but public benchmarks are concentrated far below the target EBITDA band. Only a minority of firms combine retail with material recurring services, and the dataset firm-count primitive is unavailable, making the number of actionable operators the key diligence gap.

## Demand durability
Pet ownership remained broad in 2025, reported dog and cat ownership increased, and essential pet spending has been resilient. Integrated services should grow in real terms, but discretionary pressure, online product migration, at-home grooming, remote training, and establishments classified primarily as pet services limit how much demand stays inside 459910.

## Risks and uncertainty
The largest uncertainties are the unmeasured eligible share, missing LMM firm count, broad occupation proxy, and extrapolation of total pet spending to retailer-delivered services. Animal safety incidents, scarce skilled groomers, liability, fragmented systems, chain competition, and misclassification between retail and pet-care NAICS can impair the thesis.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.25 | 0.36 | PROXY | S2, S3, S6 |
| rho | 0.32 | 0.5 | 0.68 | ESTIMATE | S3, S6 |
| e | 0.05 | 0.11 | 0.23 | ESTIMATE | S1, S6 |
| s5 | 0.1 | 0.18 | 0.28 | ESTIMATE | S5 |
| q | 0.38 | 0.55 | 0.7 | ESTIMATE | S5, S6 |
| d5 | 0.98 | 1.12 | 1.25 | PROXY | S4, S6 |
| o | 0.72 | 0.85 | 0.94 | ESTIMATE | S2, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.51 | 0.99 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.06 | 9.52 | 10.00 | ESTIMATE |

## Caveats
- a: NAICS 459900 includes pet, art, manufactured-home, tobacco, and other miscellaneous retailers and excludes self-employed workers.
- a: Petco is a large public operator outside the target EBITDA band and has a broader service stack than most independents.
- a: The supplied compensation-to-receipts ratio is LOW quality, measured at ancestor 44-45, uses 2024 wages over 2022 receipts, and is harmonized to the IPS basis; it may not represent service-heavy pet retailers.
- rho: No source measures five-year implemented substitution for the qualifying LMM population.
- rho: The estimate excludes hands-on service work already treated as unexposed in a.
- e: The prevalence of ancillary services among LMM independents is not measured.
- e: The large-chain model may not generalize to independent operators.
- e: The finalizer will inject MISSING for the declared dataset gap in n, so the absolute eligible-firm count is unavailable.
- s5: BizBuySell gives sold-business benchmarks, not a transfer rate against all eligible firms.
- s5: The five-year median sold-business owner earnings of $143,381 is far below the lens EBITDA floor.
- q: Pricing and labor models differ among grooming, group training, self-wash, memberships, and care coordination.
- q: No source isolates retained AI benefit from ordinary mix, inflation, or demand changes.
- d5: APPA is a trade association and reports the whole pet industry rather than the qualifying service basket.
- d5: The explicit growth and inflation observation covers one year, while the primitive requires a five-year ratio.
- d5: Petco's resilience statements are issuer claims from a large operator.
- o: Self-wash and simple training content have lower operator need than full grooming or behavior work.
- o: Veterinary services are excluded even when an integrated retailer offers them, because they are primarily a different NAICS activity.

## Sources
- **S1** — [2022 NAICS 459910 — Pet and Pet Supplies Retailers](https://www.census.gov/naics/?details=459910&input=459910&year=2022) (accessed 2026-07-22): Official industry boundary centered on retailing pets, pet food, and pet supplies, with primarily grooming, boarding, and veterinary establishments classified elsewhere.
- **S2** — [May 2023 OEWS — Other Miscellaneous Retailers](https://www.bls.gov/oes/2023/may/naics4_459900.htm) (accessed 2026-07-22): Observed adjacent-industry occupation mix and wages, including 47.55% sales, 11.98% office and administrative support, 9.87% personal care and service, 7.87% management, and 8.65% animal caretaker employment shares.
- **S3** — [Labor market impacts of AI: A new measure and early evidence](https://www.anthropic.com/research/labor-market-impacts) (accessed 2026-07-22): Task-based theoretical and observed AI exposure methodology; customer service and data entry are among highly covered occupations; actual coverage remains below theoretical capability and physical tasks remain beyond reach.
- **S4** — [U.S. Pet Industry Reaches $158 Billion in 2025, Poised for Continued Growth in 2026](https://americanpetproducts.org/news/u.s.-pet-industry-reaches-158-billion-in-2025-poised-for-continued-growth-in-2026) (accessed 2026-07-22): Pet-industry expenditures of $158 billion in 2025 and $165 billion projected for 2026, about 4.4% projected nominal growth with roughly 2% inflation, 95 million pet-owning households, and 2025 ownership trends.
- **S5** — [Pet Store & Pet Supply Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/pet-supply-store/) (accessed 2026-07-22): Reported 2021-2025 pet-store transactions and financials, mostly independent ownership, median revenue of $937,040, median owner earnings of $143,381, and comparison with recurring-revenue pet services.
- **S6** — [Petco Health and Wellness Company, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1826470/000119312526106114/woof-20260131.htm) (accessed 2026-07-22): Observed large-chain integrated model combining merchandise with grooming, training, veterinary, booking, membership, repeat delivery, and digital workflows; issuer discussion of repeat, resilient demand and physical employee role.
