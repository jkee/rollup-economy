# 326112 — Plastics Packaging Film and Sheet (including Laminated) Manufacturing

*v5.1 Stage 1 research memo. Run `326112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.34 · L 0.56 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat, specification-bound physical packaging demand creates a durable operating role and multiple bounded AI-enabled improvement workflows.
**Weakness:** Low labor intensity and strong customer repricing, substrate competition, and plastic-reduction pressure limit the amount and durability of captured AI benefit.

## Business-model lens
- Included: US lower-middle-market manufacturers converting plastics resins into flexible packaging film and packaging sheet for recurring or repeat external customers, including repeat converter-film, food, consumer, stretch, and shrink-film programs.
- Excluded: Captive internal plants, shells, non-control financing vehicles, plastics bags and pouches, nonpackaging film and sheet, rigid packaging, and paper-foil-plastic laminating classified outside NAICS 326112.
- Customer and revenue model: Recurring and repeat B2B sales of specified film or sheet, typically by roll, weight, or production order, to converters, packagers, and consumer-product supply chains; price resets and resin-index or other contractual mechanisms can transmit input-cost changes.
- Deviation from default lens: none

## Executive view
Packaging-film manufacturing combines repeat customer programs and indispensable physical conversion with a relatively small labor base. The practical AI opportunity is operational improvement in planning, quality, maintenance, inspection, documentation, and commercial administration, while the plant, line operators, and accountable quality system remain essential.

## How AI changes the work
AI can improve demand forecasting, scheduling, raw-material planning, predictive maintenance, machine-vision inspection, defect analysis, specification and quality-document handling, quoting, and customer service. Continuous extrusion and converting still require equipment, process control, setup, maintenance, material handling, and human accountability, so substitution is partial.

## Value capture
Benefits can appear as lower scrap and downtime, improved throughput, fewer quality failures, and avoided administrative hiring. Customers can reclaim savings through renewal bids and price competition, while resin-index mechanisms already normalize a major cost component; differentiated performance, qualification, and service reliability improve retention.

## Firm availability
The dataset estimates 101 LMM-band firms, but that count is not directly observed and the sector includes scaled integrated producers as well as independent converters. Repeat external supply should make many independent firms eligible, while captive plants, adjacent-product misclassification, customer dependence, environmental diligence, and non-stand-alone operations reduce the actionable population.

## Demand durability
Food, beverage, healthcare, personal-care, and other consumer supply chains provide recurring demand, and flexible film offers protection, barrier performance, convenience, and shelf-life benefits. Demand for the current plastic basket faces meaningful downside from lightweighting, EPR, recycled-content and recyclability rules, reuse and refill systems, and competing substrates.

## Risks and uncertainty
The main uncertainties are the absence of six-digit occupational and AI-implementation data, weak evidence on LMM ownership transfers and eligibility, variable customer contracting, resin volatility, customer concentration, legacy assets, and rapidly evolving packaging regulation. Commodity products may surrender productivity gains quickly, while regulatory or substrate shifts may strand specialized capacity.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1203 | — | OBSERVED | — |
| n | — | 101 | — | ESTIMATE | — |
| a | 0.11 | 0.2 | 0.32 | PROXY | S1, S2, S3 |
| rho | 0.38 | 0.58 | 0.74 | PROXY | S3 |
| e | 0.67 | 0.81 | 0.91 | ESTIMATE | S1, S5 |
| s5 | 0.14 | 0.23 | 0.34 | PROXY | S4 |
| q | 0.34 | 0.5 | 0.67 | ESTIMATE | S5 |
| d5 | 0.84 | 1.03 | 1.16 | PROXY | S5, S6, S7 |
| o | 0.9 | 0.97 | 0.995 | ESTIMATE | S1, S5, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.20 | 0.56 | 1.14 | PROXY |
| F | 3.78 | 4.80 | 5.59 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.56 | 9.99 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupational shares are for four-digit NAICS 326100 rather than this six-digit industry.
- a: NIST use cases show technical applicability and adoption, not wage-weighted task exposure in packaging-film plants.
- a: The injected compensation-to-receipts ratio is low and based on mismatched QCEW 2024 and SUSB 2022 vintages, but it is not used to set this task-share primitive.
- rho: Manufacturing-wide survey adoption includes simple chatbots and does not measure the fraction of exposed labor opportunity actually implemented.
- rho: Implementation rates may differ sharply between modern multi-layer extrusion assets and older lines with limited sensor and data infrastructure.
- e: No source directly measures lens eligibility among estimated LMM firms.
- e: The industry includes both scaled integrated producers and independent converters, and public-company product mixes do not reveal the LMM eligibility distribution.
- e: The injected firm count is an estimate derived from broader size-distribution data.
- s5: Gallup covers employer businesses across industries and sizes, not NAICS 326112 or the LMM EBITDA band.
- s5: Owner intentions are not completed transactions, and the source does not isolate qualifying control transfers.
- s5: Corporate carve-outs and internal restructurings must be excluded even if plants change reporting ownership.
- q: A large public producer's contracting and competitive disclosures may not match LMM firms' bargaining power.
- q: Retention varies by differentiated barrier film, commodity converter film, contract duration, and customer concentration.
- q: The range excludes demand loss, which is represented in d5 and o.
- d5: BLS output covers all plastics products and a ten-year horizon, not this six-digit industry's five-year physical demand.
- d5: Public-company end-market statements span products outside NAICS 326112.
- d5: California policy is not a national forecast, but it signals a material regulatory and design pathway that may spread.
- o: Elimination of plastic packaging quantity is principally captured in d5; o only captures whether surviving demand still needs this kind of external accountable operator.
- o: The boundary between material substitution and operator substitution can be ambiguous for integrated refill and reuse systems.

## Sources
- **S1** — [2017 NAICS Definition File — 326112 Plastics Packaging Film and Sheet (including Laminated) Manufacturing](https://www.census.gov/naics/2017NAICS/2017_Definition_File.pdf) (accessed 2026-07-22): Defines the industry as converting plastics resins into flexible packaging film and packaging sheet and identifies excluded adjacent activities.
- **S2** — [May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates: Plastics Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-22): Provides the broader-industry occupation mix, including 58.94% production occupations and 4.83% extrusion and drawing machine operators.
- **S3** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Reports manufacturing AI adoption and expected growth, applicable use cases, implementation barriers, and examples of production, quality, maintenance, planning, and document workflows.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports employer-business owner age and five-year plans to sell or transfer ownership for a broad US employer-business population.
- **S5** — [Berry Global Group, Inc. 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1378992/000114036124047881/form10k.htm) (accessed 2026-07-22): Describes flexible-film product groups, stable consumer end markets, product functions, resin pass-through mechanisms, competition, customer switching, and substrate risk.
- **S6** — [BLS Employment and Output by Industry, 2024–2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects broader plastics product manufacturing real output from 190.7 to 212.4 billion chained 2017 dollars over 2024–2034.
- **S7** — [California Approves New Plastic and Packaging Rules That Put Consumers First](https://calrecycle.ca.gov/2026/05/01/press-release-26-05/) (accessed 2026-07-22): Documents enacted targets for plastic reduction, recyclable or compostable packaging, actual recycling, and shifts toward elimination, reuse, and refill by 2032.
