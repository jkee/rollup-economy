# 311351 — Chocolate and Confectionery Manufacturing from Cacao Beans

*v5.1 Stage 1 research memo. Run `311351-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.04 · L 0.00 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent repeat consumer demand for physical chocolate products keeps the accountable manufacturing operator necessary.
**Weakness:** The frozen LMM count is zero and the labor base is dominated by physical plant work with limited AI-only substitution.

## Business-model lens
- Included: US lower-middle-market manufacturers that shell, roast, or grind cacao beans and make chocolate, cacao products, or chocolate confectionery for repeat wholesale, private-label, foodservice, or retail-channel customers.
- Excluded: Purchased-chocolate confectioners, nonchocolate candy makers, immediate-consumption shops, pure retailers, captive internal plants, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat product sales under wholesale, distributor, private-label, foodservice, and retailer relationships; revenue is primarily per unit or shipment rather than a cost-plus service fee.
- Deviation from default lens: none

## Executive view
Cacao-bean chocolate manufacturing has durable repeat demand and real pricing discretion, but it is fundamentally a physical, regulated production business. The largest AI opportunities sit around the line rather than replacing it, and the frozen firm-count estimate identifies no firms in the target EBITDA band.

## How AI changes the work
AI can improve visual-inspection triage, production scheduling, demand forecasting, maintenance prioritization, traceability records, customer service, and administrative work. Sanitation, material handling, process control, maintenance, and final food-quality accountability remain human-and-equipment intensive, so exposed labor and five-year implementation are bounded.

## Value capture
Unit-based product pricing lets operators retain some productivity benefit, especially where products or customer service are differentiated. Retailer leverage, private-label rebids, competitive pricing, and volume elasticity gradually share the gains; large branded-company pricing power is an optimistic proxy for independent firms.

## Firm availability
Manufacturing owners skew older and cross-industry survey evidence shows meaningful five-year transfer intent. Yet intent does not equal a completed qualifying control sale, and specialized plants can be hard to finance or transfer. More importantly, the injected size-band estimate is zero, so candidate existence is the immediate diligence question.

## Demand durability
Confectionery reaches nearly every household and seasonal occasions support recurring consumption. Reported dollar growth is heavily price-driven while volume has struggled, so constant-price five-year demand is best treated as roughly flat rather than extrapolating nominal forecasts.

## Risks and uncertainty
The principal evidence gaps are six-digit occupation data, LMM AI deployment outcomes, private-company pricing and renewal behavior, and completed transfer rates. Cocoa volatility, retailer concentration, food-safety failures, customer concentration, branded versus private-label mix, and migration to purchased chocolate can dominate small productivity gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1138 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.12 | 0.2 | 0.3 | PROXY | S2, S3, S4 |
| rho | 0.22 | 0.38 | 0.55 | PROXY | S5, S6 |
| e | 0.55 | 0.75 | 0.9 | ESTIMATE | S1 |
| s5 | 0.07 | 0.13 | 0.2 | PROXY | S7, S8 |
| q | 0.4 | 0.62 | 0.8 | PROXY | S9 |
| d5 | 0.9 | 1.01 | 1.1 | PROXY | S3, S10 |
| o | 0.92 | 0.97 | 1 | ESTIMATE | S1, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.12 | 0.35 | 0.75 | PROXY |
| F | 0.00 | 0.00 | 0.00 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | PROXY |
| D | 8.28 | 9.80 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is for NAICS 311, not 311351.
- a: Advanced-technology exposure includes robotics and dedicated equipment, not just AI, and is explicitly an upper bound.
- rho: Survey definitions of AI changed over time and include any business function.
- rho: Large-company deployment experience may not transfer to LMM plants.
- e: The frozen dataset estimates zero firms in the EBITDA band, so this eligibility share has no effect unless that estimate is revised.
- e: Census reports establishments, not eligible control-transfer firms.
- s5: Neither source isolates NAICS 311351 or the stated EBITDA band.
- s5: Intentions are not completed transactions, and gifts may not qualify as an external control transfer.
- q: Hershey has brand strength and scale unlike most LMM firms.
- q: Observed pricing responses reflect cocoa inflation and broader productivity, not AI savings alone.
- d5: Category evidence mixes manufacturing codes and channels.
- d5: The NCA forecast is nominal and partly reflects inflation; conversion to constant-price quantity is judgmental.
- o: The estimate does not separately model consolidation into large manufacturers.
- o: A shift from bean processing to purchased chocolate would move activity to NAICS 311352 even if confectionery demand persists.

## Sources
- **S1** — [311351: Chocolate and Confectionery Manufacturing from Cacao Beans - Census Bureau Profile](https://data.census.gov/profile/311351_-_Chocolate_and_Confectionery_Manufacturing_from_Cacao_Beans?codeset=naics~311351) (accessed 2026-07-22): Industry definition, cross-references, and 280 employer establishments in 2023.
- **S2** — [Food Manufacturing: NAICS 311](https://www.bls.gov/iag/tgs/iag311.htm) (accessed 2026-07-22): Broader food-manufacturing employment and occupation mix, including production/nonsupervisory employment and common batchmaking and packaging roles.
- **S3** — [Food Processing Equipment Workers](https://www.bls.gov/ooh/production/food-and-tobacco-processing-workers.htm) (accessed 2026-07-22): Physical duties, 78% employment in food manufacturing, automatic weighing and mixing, and 5% projected employment growth from 2024 to 2034.
- **S4** — [Three Results From Recent Research on Advanced Technology Use and Automation](https://www.census.gov/newsroom/blogs/research-matters/2023/09/advanced-technology-use-and-automation-results.html) (accessed 2026-07-22): Manufacturing worker exposure to advanced automating technologies was 52% versus 28% outside manufacturing, explicitly described as an upper bound.
- **S5** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS AI usage of 17-20% overall in late 2025 through May 2026, expected use of 20-23%, and higher use at larger firms.
- **S6** — [Census Bureau's 2023 Annual Business Survey Provides Insight into Technology Adoption by Businesses](https://www.census.gov/library/stories/2025/09/technology-impact.html) (accessed 2026-07-22): Most adopting businesses reported no overall worker-number change; AI and other technologies often required workflow and skill changes.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 survey of five-year owner plans: 17% of owners age 55 or older versus 10% of younger owners planned sale or other ownership transfer.
- **S8** — [Employee Ownership for Manufacturers](https://project-equity.org/publication/employee-ownership-for-manufacturing/) (accessed 2026-07-22): Reported that 60% of small and midsize manufacturers have owners at or near retirement age.
- **S9** — [The Hershey Company 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/47111/000162828026008586/hsy-20251231.htm) (accessed 2026-07-22): Large branded confectioner evidence on price realization, volume elasticity, raw-material pricing, and lag from list-price increases to net sales.
- **S10** — [Confectionery Sales Climb to $55 Billion in 2025](https://candyusa.com/news/confectionery-sales-climb-to-55-billion-in-2025/) (accessed 2026-07-22): 2025 US confectionery retail sales, 99.8% household purchase penetration, chocolate share, seasonal concentration, and nominal forecast to 2030.
