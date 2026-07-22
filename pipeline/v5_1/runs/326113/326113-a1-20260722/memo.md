# 326113 — Unlaminated Plastics Film and Sheet (except Packaging) Manufacturing

*v5.1 Stage 1 research memo. Run `326113-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.13 · L 0.80 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat, specification-bound physical supply and qualification requirements create recurring demand and multiple bounded workflows for AI-enabled operating improvement.
**Weakness:** Continuous-line labor limits substitution, while concentrated customers and cyclical or technically substitutable end uses can reclaim savings and destabilize demand.

## Business-model lens
- Included: US lower-middle-market manufacturers converting plastics resins into nonpackaging plastics film and unlaminated sheet for recurring or repeat external customers, including specification-bound industrial and specialty-film programs.
- Excluded: Captive internal plants, shells, non-control financing vehicles, plastics packaging film and sheet, plastics bags, laminated nonpackaging plastics sheet, rigid shapes, and activities classified outside NAICS 326113.
- Customer and revenue model: Recurring and repeat B2B sales of film or sheet by roll, sheet, weight, or production order to industrial customers under product specifications; pricing reflects resin, conversion, performance, service, and qualification, with index-based or other cost pass-through arrangements in some contracts.
- Deviation from default lens: none

## Executive view
Nonpackaging film and sheet manufacturing is a repeat B2B physical-conversion business whose practical AI opportunity lies in planning, quality, maintenance, inspection, documentation, and customer workflows. Specialty qualifications can create stickiness, but continuous extrusion limits labor substitution and customer concentration, cost pass-through, cyclicality, and process or material transitions can erode retained value.

## How AI changes the work
AI can improve demand and production planning, quoting, specification retrieval, quality-document generation, defect classification, machine-vision inspection, predictive maintenance, troubleshooting, inventory control, and customer service. Extrusion setup, continuous-line operation, maintenance, testing, handling, and accountable product release still require plant assets and skilled people.

## Value capture
Savings may be retained through better yield, uptime, quality, throughput, and service, particularly for qualified specialty products. Retention weakens where contracts pass resin costs through, buyers are concentrated, suppliers rebid frequently, or customers can demand productivity concessions; the public specialty-film example displays both operational savings and strong buyer concentration.

## Firm availability
The dataset estimates 72 firms in the LMM band, but the count is margin-bridged rather than observed. Many independent converters should fit the repeat external-customer lens, while captive capacity, classification ambiguity, technical obsolescence, customer concentration, and lack of stand-alone financials reduce the eligible and transferable pool.

## Demand durability
Industrial and specialty-film functions recur as customers manufacture and ship their products, but the basket is heterogeneous and can be cyclical. Display-related surface-protection volumes have shown severe inventory and end-market swings, and some functions can transition to alternative processes or materials; diverse applications and projected broader plastics growth provide offsets.

## Risks and uncertainty
Key uncertainties include the absence of six-digit occupational and implementation data, no direct eligibility or transaction denominator, widely varying specialty versus commodity economics, resin volatility, customer concentration, offshore competition, legacy equipment, end-market cycles, and technical substitution. A highly concentrated or obsolete product program can make otherwise capable assets unattractive.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1601 | — | OBSERVED | — |
| n | — | 72 | — | ESTIMATE | — |
| a | 0.12 | 0.22 | 0.34 | PROXY | S1, S2, S3 |
| rho | 0.38 | 0.57 | 0.73 | PROXY | S3 |
| e | 0.62 | 0.78 | 0.89 | ESTIMATE | S1, S5 |
| s5 | 0.14 | 0.23 | 0.34 | PROXY | S4 |
| q | 0.31 | 0.48 | 0.67 | ESTIMATE | S5 |
| d5 | 0.82 | 1.03 | 1.2 | PROXY | S5, S6 |
| o | 0.86 | 0.96 | 0.995 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.29 | 0.80 | 1.59 | PROXY |
| F | 3.19 | 4.24 | 5.03 | ESTIMATE |
| C | 6.20 | 9.60 | 10.00 | ESTIMATE |
| D | 7.05 | 9.89 | 10.00 | ESTIMATE |

## Caveats
- a: BLS staffing data are for four-digit plastics product manufacturing, not NAICS 326113.
- a: NIST use cases establish applicability but do not measure wage-weighted task exposure in nonpackaging film plants.
- a: The injected compensation-to-receipts ratio uses 2024 wages over 2022 receipts and is harmonized, but it is not used to set this task-share primitive.
- rho: Reported use of AI tools such as chatbots is not equivalent to implementing a share of exposed wage opportunity.
- rho: Implementation will vary materially between modern instrumented lines and older assets with limited accessible data.
- e: No source directly measures eligibility for the frozen lens.
- e: Public PE Films disclosures mix target nonpackaging surface-protection film with packaging overwrap film and do not reveal the LMM firm distribution.
- e: The injected count of 72 LMM firms is an estimate built from size distributions and a margin bridge.
- s5: Gallup covers employer businesses across industries and sizes rather than NAICS 326113 LMM firms.
- s5: Owner plans are not completed transactions and do not isolate qualifying control transfers.
- s5: Divestitures of units inside larger companies may transfer assets without representing the eligible-firm succession process.
- q: A public specialty-film segment with four customers representing 88% of segment sales is not representative of every LMM firm or application.
- q: Differentiated surface-protection film and commodity unlaminated sheet can have sharply different bargaining power.
- q: Demand loss and implementation difficulty are excluded here and represented in d5, o, and rho.
- d5: BLS output covers all plastics products over ten years, not six-digit nonpackaging film and sheet over five years.
- d5: Tredegar's PE Films segment includes packaging overwrap and is unusually concentrated in high-technology surface protection.
- d5: Nominal sales and short-term inventory restocking are not direct measures of constant-price, constant-quality industry demand.
- o: Demand eliminated by end-market contraction or material substitution is primarily captured in d5; o only addresses whether remaining demand still needs this kind of external accountable operator.
- o: Integrated customer production and alternative processes are not measured for the whole six-digit industry.

## Sources
- **S1** — [2017 NAICS Definition File — 326113 Unlaminated Plastics Film and Sheet (except Packaging) Manufacturing](https://www.census.gov/naics/2017NAICS/2017_Definition_File.pdf) (accessed 2026-07-22): Defines the industry as converting plastics resins into nonpackaging plastics film and unlaminated sheet and identifies excluded adjacent activities.
- **S2** — [May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates: Plastics Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-22): Provides the broader-industry occupation mix, including 58.94% production occupations, 4.83% extrusion and drawing machine operators, and 5.17% inspectors and testers.
- **S3** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Reports manufacturing AI adoption, expected growth, applicable use cases in quality, maintenance, forecasting and planning, and barriers including data, cost, skills, security, and legacy integration.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports employer-business owner age and broad US employer-business plans to sell or transfer ownership within five years.
- **S5** — [Tredegar Corporation 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/850429/000085042925000004/tg-20241231.htm) (accessed 2026-07-22): Describes surface-protection film applications, resin inputs and pass-through, customer concentration, demand cyclicality and inventory effects, favorable pricing, operating efficiencies, and manufacturing cost savings.
- **S6** — [BLS Employment and Output by Industry, 2024–2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects broader plastics product manufacturing real output from 190.7 to 212.4 billion chained 2017 dollars over 2024–2034.
