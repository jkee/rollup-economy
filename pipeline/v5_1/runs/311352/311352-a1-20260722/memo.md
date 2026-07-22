# 311352 — Confectionery Manufacturing from Purchased Chocolate

*v5.1 Stage 1 research memo. Run `311352-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.59 · L 0.54 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring chocolate demand and outsourced private-label or wholesale production preserve the need for accountable physical manufacturers.
**Weakness:** Most labor remains physical, while competitive rebids and retailer leverage limit retention of implemented savings.

## Business-model lens
- Included: US lower-middle-market manufacturers that convert purchased chocolate into finished confectionery for recurring wholesale, private-label, corporate-gifting, foodservice, distributor, or retailer customers.
- Excluded: Storefront-led on-premises retail confectioners, immediate-consumption foodservice, cacao-bean processors, nonchocolate candy makers, pure retailers, captive plants, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat finished-product sales priced per unit, case, shipment, or production run, often through private-label programs, wholesale catalogs, distributor relationships, seasonal orders, and recurring branded accounts.
- Deviation from default lens: The NAICS definition mixes industrial manufacturers with establishments retailing chocolate confectionery made on premises. The lens retains recurring external-customer manufacturing and excludes storefront-led retail because their labor mix, customer acquisition, pricing, and transferability are materially different.

## Executive view
Purchased-chocolate confectionery manufacturing combines repeat physical demand with a meaningful population of estimated LMM firms, but it is still a plant-and-product business rather than a labor-light service. AI can improve surrounding workflows, while private-label competition and retailer bargaining constrain retained value.

## How AI changes the work
The most credible uses are order intake, scheduling, demand forecasting, formulation and traceability records, visual-inspection triage, maintenance prioritization, customer support, and administration. Molding, enrobing, decorating, sanitation, packaging interventions, and final quality accountability remain physical and limit wage-weighted substitution.

## Value capture
Per-unit and per-run pricing permits some initial retention of savings. Over five years, private-label rebids, wholesale renewal discussions, competing converters, and retailer leverage share benefits; proprietary products, responsiveness, and seasonal reliability can preserve more.

## Firm availability
The code contains both industrial manufacturers and retail-led confectioners, so only a portion of the frozen 43-firm estimate fits the narrowed recurring-manufacturing lens. Aging manufacturing ownership supports potential supply, but completed transferable control deals should be expected well below stated exit intent.

## Demand durability
Household confectionery participation and seasonal occasions are durable, yet category dollar growth is currently inflation-heavy and real volume is pressured. Constant-price five-year demand is therefore approximately flat, with downside from elasticity and substitution and upside from population, gifting, and product innovation.

## Risks and uncertainty
Key uncertainties are the industrial-versus-retail firm split, six-digit labor tasks, private-company contract terms, customer concentration, and actual closed transactions. Input-price shocks, food-safety events, seasonal working capital, retailer power, and dependence on a few accounts could overwhelm modest AI gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1406 | — | OBSERVED | — |
| n | — | 43 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.34 | PROXY | S2, S3, S4 |
| rho | 0.25 | 0.42 | 0.6 | PROXY | S5, S6 |
| e | 0.4 | 0.58 | 0.75 | ESTIMATE | S1 |
| s5 | 0.07 | 0.13 | 0.21 | PROXY | S7, S8 |
| q | 0.35 | 0.56 | 0.76 | PROXY | S9 |
| d5 | 0.89 | 1 | 1.1 | PROXY | S3, S10 |
| o | 0.89 | 0.95 | 0.99 | ESTIMATE | S1, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.20 | 0.54 | 1.15 | PROXY |
| F | 1.27 | 2.32 | 3.30 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | PROXY |
| D | 7.92 | 9.50 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is for NAICS 311 and mixes very different food processes.
- a: Advanced-technology exposure includes robotics, specialized software, and equipment rather than isolating AI.
- rho: The BTOS question now covers AI in any business function, broadening measured use.
- rho: Survey adoption does not measure the fraction of exposed opportunity actually captured.
- e: No source measures eligibility within the frozen 43-firm estimate.
- e: The margin bridge used to estimate the band may misclassify branded, retail-heavy, or volatile-margin firms.
- s5: The evidence does not isolate this NAICS or EBITDA band.
- s5: Stated plans are not completed transactions and include transfer forms outside the qualifying definition.
- q: Large-brand economics do not represent smaller converters.
- q: Observed price realization responds mainly to cocoa and other cost inflation, not AI productivity.
- d5: The category mixes multiple NAICS codes and retail margins.
- d5: The constant-price conversion is judgmental because the cited forecast is nominal.
- o: The estimate excludes storefront-led manufacturers through the lens narrowing.
- o: Consolidation into larger suppliers preserves operator-required demand but may remove it from the LMM population.

## Sources
- **S1** — [North American Industry Classification System: 311352 Confectionery Manufacturing from Purchased Chocolate](https://www.census.gov/naics/?details=311&input=311&year=2022) (accessed 2026-07-22): Official definition covering confectionery made from chocolate produced elsewhere and on-premises retail confectionery manufacturing.
- **S2** — [Food Manufacturing: NAICS 311](https://www.bls.gov/iag/tgs/iag311.htm) (accessed 2026-07-22): Broader food-manufacturing employment and occupation mix, including production/nonsupervisory employment and common batchmaking and packaging roles.
- **S3** — [Food Processing Equipment Workers](https://www.bls.gov/ooh/production/food-and-tobacco-processing-workers.htm) (accessed 2026-07-22): Physical production duties, 78% employment in food manufacturing, automatic weighing and mixing, and 5% projected 2024-2034 employment growth.
- **S4** — [Three Results From Recent Research on Advanced Technology Use and Automation](https://www.census.gov/newsroom/blogs/research-matters/2023/09/advanced-technology-use-and-automation-results.html) (accessed 2026-07-22): Manufacturing worker exposure to advanced automating technologies was 52% versus 28% elsewhere and is described as an upper-bound measure.
- **S5** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS AI usage of 17-20% overall in late 2025 through May 2026, expected use of 20-23%, and materially higher use at larger businesses.
- **S6** — [Census Bureau's 2023 Annual Business Survey Provides Insight into Technology Adoption by Businesses](https://www.census.gov/library/stories/2025/09/technology-impact.html) (accessed 2026-07-22): Most technology adopters reported no overall worker-number change and often experienced workflow or skill effects rather than simple substitution.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 five-year owner plans: 17% of owners age 55 or older and 10% of younger owners planned sale or another ownership transfer.
- **S8** — [Employee Ownership for Manufacturers](https://project-equity.org/publication/employee-ownership-for-manufacturing/) (accessed 2026-07-22): Reports that 60% of small and midsize manufacturers have owners at or near retirement age.
- **S9** — [The Hershey Company 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/47111/000162828026008586/hsy-20251231.htm) (accessed 2026-07-22): Large branded confectioner evidence on favorable price realization, volume elasticity, and lags between list-price changes and net sales.
- **S10** — [Confectionery Sales Climb to $55 Billion in 2025](https://candyusa.com/news/confectionery-sales-climb-to-55-billion-in-2025/) (accessed 2026-07-22): 2025 category sales, 99.8% household penetration, chocolate share, seasonal concentration, and nominal forecast through 2030.
