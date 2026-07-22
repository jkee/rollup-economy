# 312111 — Soft Drink Manufacturing

*v5.1 Stage 1 research memo. Run `312111-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.37 · L 0.66 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical production cannot become software-only, while planning, records, quality triage, forecasting, and maintenance offer repeatable AI-assisted efficiency.
**Weakness:** Cost-plus and open-book beverage contracts can directly pass productivity to customers, and the eligible independent co-packer population is not observed.

## Business-model lens
- Included: Independent US beverage co-packers and contract bottlers in NAICS 312111 that repeatedly blend, carbonate, fill, label, package, or warehouse soft drinks for external beverage brands, retailers, or other beverage companies, within the lower-middle-market EBITDA band.
- Excluded: Brand owners that outsource all manufacturing, own-brand manufacturers without a recurring third-party production stream, captive plants, controlled franchise bottlers operating primarily as part of a brand system, distributors, vending operations, bottled-water plants classified in 312112, alcoholic beverage plants, non-control financings, and failed or non-operating facilities.
- Customer and revenue model: Recurring B2B production programs and purchase orders priced per case, unit, batch, or run; contracts can combine conversion margin with direct ingredient and packaging costs, volume tiers, minimum quantities, equipment support, and negotiated cost pass-throughs.
- Deviation from default lens: Narrowed to independent co-packers and contract bottlers because NAICS 312111 includes brand-led and integrated soft-drink producers that sell their own products rather than an outsourced service; recurring third-party manufacturing is the coherent service-like subset.

## Executive view
Independent soft-drink co-packers are the coherent target, not the full branded and franchise bottling industry. Their repetitive, sensor-rich production and document-heavy QA, planning, order, and maintenance workflows support targeted AI implementation, while physical production and food-safety accountability remain durable. The central commercial constraint is transparent, frequently renegotiated pricing that can pass direct-cost savings back to brand customers.

## How AI changes the work
AI can improve production and material scheduling, forecast demand, process purchase orders and invoices, extract specifications, support batch and preventive-control records, triage inspection images, diagnose downtime, and draft investigations or customer responses. It is less able to replace sanitation, line changeovers, maintenance execution, physical handling, blending, packaging, and final QA accountability. Deployment depends on clean plant data and integration with MES, ERP, CMMS, lab, and line-control systems.

## Value capture
Benefits in overhead, avoided hiring, reduced scrap, better yields, uptime, and working capital can initially accrue to the operator. Direct-cost-plus-margin agreements, documented cost-change clauses, volume discounts, open-book audits, and competitive rebids can rapidly share savings with customers. Scarce compatible capacity, customer switching cost, and fixed-price periods improve capture, but the working estimate assumes procurement eventually recovers much of the visible benefit.

## Firm availability
Brand filings confirm material reliance on co-packers, yet the number of independent LMM suppliers is obscured by integrated bottlers, captive systems, and own-brand manufacturers within 312111. Qualifying control-transfer evidence is not available with a reliable denominator. Any target must be screened for change-of-control consents, customer concentration, line ownership, formula and tooling rights, equipment condition, and a clean regulatory and recall history.

## Demand durability
Mature sparkling volume is broadly flat, with growth shifting among zero-sugar, energy, functional, and flavored formats. Outsourcing remains valuable for brands that need flexible capacity, geographic coverage, specialized packages, or launches without owning plants. Program-level demand is volatile: brands can fail, redesign packages, shift co-packers, bring volume in-house, or require unplanned capital even when aggregate beverage consumption is stable.

## Risks and uncertainty
The largest gaps are the eligible-firm denominator, private transfer rate, contract-term distribution, and actual soft-drink co-packer task mix. Additional risks include concentrated customers, formula or package complexity, aluminum and ingredient volatility, low utilization, short production runs, food-safety failures, recalls, aging lines, wastewater constraints, weak cybersecurity, and customer-funded equipment that may leave at termination.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1517 | — | OBSERVED | — |
| n | — | 63 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.33 | PROXY | S2, S4 |
| rho | 0.28 | 0.47 | 0.67 | PROXY | S3, S4, S5 |
| e | 0.18 | 0.3 | 0.45 | ESTIMATE | S1, S8, S9 |
| s5 | 0.1 | 0.16 | 0.25 | ESTIMATE | — |
| q | 0.1 | 0.24 | 0.42 | PROXY | S8, S9, S10 |
| d5 | 0.9 | 1.01 | 1.12 | PROXY | S6, S7 |
| o | 0.92 | 0.97 | 0.99 | ESTIMATE | S5, S8, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.24 | 0.66 | 1.34 | PROXY |
| F | 1.22 | 2.24 | 3.36 | ESTIMATE |
| C | 2.00 | 4.80 | 8.40 | PROXY |
| D | 8.28 | 9.80 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation proxy is four-digit beverage manufacturing and is materially contaminated by winery, brewery, hospitality, and integrated-brand employment.
- a: The source reports employment and wages, not task exposure or a wage-weighted exposure total.
- a: AI exposure does not imply that an entire job can be eliminated.
- rho: AI-use surveys are cross-sector or cross-manufacturing and do not isolate beverage co-packers.
- rho: NIST adoption figures include light uses such as chatbots and rely on cited industry surveys.
- rho: Food-safety monitoring and verification create useful data but also require validation, documentation, and accountable review.
- e: There is no observed denominator for independent co-packers within NAICS 312111.
- e: Brand filings show demand for co-packing but not the share or size distribution of eligible suppliers.
- e: Franchise bottlers and branded manufacturers can look service-like while remaining economically captive or own-account.
- s5: This is a bounded judgment rather than an observed industry transfer probability.
- s5: Private LMM transactions are underreported and frequently coded only as beverage or food manufacturing.
- s5: Customer concentration, change-of-control consent, line-specific capital, and food-safety history can impair transferability.
- q: The directly observed contract is one issuer-specific agreement and may not represent current LMM market terms.
- q: Contract economics vary sharply with capacity scarcity, run size, customer concentration, ingredient ownership, and capital support.
- q: The estimate excludes demand loss and implementation failure, which are represented elsewhere.
- d5: The Fed series combines soft drinks with ice and uses production-worker hours for the monthly series.
- d5: Coca-Cola is global and brand-specific rather than a US contract-manufacturing population.
- d5: Co-packer demand can grow even when end-market quantity is flat if brands outsource more, or decline if they insource.
- o: This is a bounded operator-necessity judgment, not an observed substitution rate.
- o: A customer may switch plants without eliminating operator-required demand; the construct concerns the service basket, not incumbent retention.
- o: High automation still requires accountable plant and food-safety management.

## Sources
- **S1** — [2022 NAICS Definition: 312111 Soft Drink Manufacturing](https://www.census.gov/naics/?details=31211&input=31211&year=2022) (accessed 2026-07-22): Official definition that 312111 comprises establishments manufacturing soft drinks and artificially carbonated waters, distinct from bottled water manufacturing.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 312100](https://www.bls.gov/oes/2023/may/naics4_312100.htm) (accessed 2026-07-22): Broader beverage occupation mix, including 21.59% production, 5.29% installation/maintenance, 5.33% management, 4.68% office/administrative, 3.48% business/financial, and 26.40% food-preparation/serving employment.
- **S3** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS evidence of 17%-20% current business AI use from December 2025 to May 2026, 20%-23% expected six-month use, and higher usage at larger firms.
- **S4** — [The Rise of Artificial Intelligence in U.S. Manufacturing: Text Only](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Manufacturing AI uses in predictive maintenance, quality, demand forecasting, document management, supply chain, and scheduling, plus adoption evidence and barriers involving data, cost, skills, cybersecurity, and legacy systems.
- **S5** — [FSMA Final Rule for Preventive Controls for Human Food](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food) (accessed 2026-07-22): Registered food facilities generally require written food-safety plans, hazard analysis, preventive controls, monitoring, corrective actions, verification, documented records, supply-chain controls where applicable, and recall plans.
- **S6** — [Industrial Production: Industry Subtotals and Individual Series, March 2026](https://www.federalreserve.gov/Releases/g17/20260316/table1a_sup.htm) (accessed 2026-07-22): Seasonally adjusted soft-drink-and-ice production index values of 94.1, 94.3, 95.2, and 94.2 in September-December 2025 and 97.3 and 99.4 in January-February 2026, with 2017=100.
- **S7** — [Coca-Cola Reports Fourth Quarter and Full Year 2025 Results](https://www.coca-colacompany.com/media-center/coca-cola-reports-fourth-quarter-and-full-year-2025-results) (accessed 2026-07-22): Global 2025 sparkling soft-drink unit volume was even; Coca-Cola Zero Sugar grew 14%, sparkling flavors declined 1%, and total price/mix grew 4%.
- **S8** — [Monster Beverage Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/865752/000110465926020831/mnst-20251231x10k.htm) (accessed 2026-07-22): A majority of nonalcohol finished goods are made by third-party bottlers and co-packers; arrangements vary and may include minimum quantities, customer-funded equipment, per-case credits, and capacity limitations.
- **S9** — [Reed's, Inc. 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1083522/000164117225001951/form10-k.htm) (accessed 2026-07-22): Brand dependence on third-party bottlers and independent co-packers, intense competition for co-packing capacity, terminable agreements, demand-planning risk, and contract-manufacturer charges that can rise with costs.
- **S10** — [Beverage Manufacturing Agreement filed with the SEC](https://www.sec.gov/Archives/edgar/data/1670869/000166357719000090/ex10_1.htm) (accessed 2026-07-22): Observed contract example with a 75% markup on direct costs, possible lower markup at higher volume, direct-cost-plus-margin invoicing, verified cost-increase pass-through, and direct pass-through of material cost decreases.
