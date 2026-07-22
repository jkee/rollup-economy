# 324191 — Petroleum Lubricating Oil and Grease Manufacturing

*v5.1 Stage 1 research memo. Run `324191-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.85 · L 0.26 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical consumable demand plus formulation and qualification complexity sustains operator-required customer relationships.
**Weakness:** AI-addressable labor is a minority of a production-heavy cost base, and the independent eligible population is not directly measured.

## Business-model lens
- Included: Independent lower-middle-market formulators and blenders that repeatedly supply specialty lubricating oils, greases, and related technical support to external industrial, commercial-vehicle, and equipment customers.
- Excluded: Captive refinery units, vertically integrated oil-major operations, commodity-only consumer motor-oil brands, distributors without manufacturing, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat B2B product sales under customer specifications, purchase orders, distributor relationships, and some supply agreements; revenue is primarily per unit shipped, supported by formulation, testing, reliability, and technical service.
- Deviation from default lens: The code spans commodity automotive lubricants and technically differentiated industrial formulations. The lens is narrowed to independent specialty B2B formulators because their repeat supply and technical-service model is coherent and distinct from captive or mass-market production.

## Executive view
Independent specialty lubricant formulators combine repeat consumable demand with formulation know-how and switching friction, but they remain physical manufacturers rather than software-like service businesses. The implementable AI opportunity is concentrated in indirect labor and decision support, not blending-line labor.

## How AI changes the work
AI can accelerate formulation search, technical-document drafting, certificates and specifications, demand planning, purchasing, quoting, customer support, maintenance triage, and quality-exception analysis. Human operators, chemists, and accountable quality personnel remain necessary for hazardous-material handling, physical testing, process interventions, and release decisions.

## Value capture
Differentiated formulas, qualification work, dependable supply, and technical support can protect some productivity gains. Commodity-equivalent products, negotiated distributor economics, transparent input costs, and competitive rebids create meaningful pass-through over time.

## Firm availability
A meaningful independent segment exists within a fragmented global industry, but the six-digit population also includes captive and scaled operations outside the lens. Cross-industry survey evidence suggests employer firms are transferable, though completed lubricant-manufacturer deal data are missing.

## Demand durability
Industrial equipment and the installed internal-combustion fleet require recurrent lubrication, while synthetic and specialty products add performance value. Electrification, longer drain intervals, and manufacturer consolidation limit volume upside but are unlikely to remove the operator-required product basket within five years.

## Risks and uncertainty
The largest uncertainties are the eligible share of the injected firm count, six-digit occupational mix, and customer-level price-retention mechanics. Product-liability, environmental, raw-material, OEM-approval, and quality failures can overwhelm modest labor savings; small regional firms may also lose share as customers demand breadth and scale.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.057 | — | OBSERVED | — |
| n | — | 82 | — | ESTIMATE | — |
| a | 0.13 | 0.22 | 0.33 | PROXY | S1, S2, S3 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S3 |
| e | 0.24 | 0.4 | 0.58 | ESTIMATE | S4 |
| s5 | 0.12 | 0.2 | 0.31 | PROXY | S5 |
| q | 0.43 | 0.6 | 0.76 | ESTIMATE | S4 |
| d5 | 0.97 | 1.04 | 1.11 | PROXY | S4 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.10 | 0.26 | 0.51 | ESTIMATE |
| F | 1.95 | 3.25 | 4.43 | ESTIMATE |
| C | 8.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.54 | 9.88 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation data are for NAICS 324, dominated by refining, and are not six-digit-specific.
- a: Task exposure is judgmentally mapped and excludes already-automated process control.
- rho: No adoption study specific to small U.S. lubricant formulators was found.
- rho: The range assumes adequate digital records and excludes autonomous safety-critical control.
- e: The fragmentation evidence is global and includes distributors as well as manufacturers.
- e: Eligibility is not observed among the injected U.S. firm population.
- s5: Cross-industry owner intentions are not completed transactions.
- s5: The survey's typical firms are smaller than the $1-10M EBITDA lens.
- q: No representative contract sample was available.
- q: Retention will differ sharply between proprietary specialty fluids and specification-equivalent commodity lubricants.
- d5: The cited forecast is global and vendor-derived within an issuer filing.
- d5: Constant-quality quantity must be inferred from market-value and profit-pool forecasts.
- o: Operator requirement is inferred from the physical product and compliance workflow, not directly measured.
- o: The estimate may overstate persistence where OEM-filled-for-life components eliminate aftermarket demand.

## Sources
- **S1** — [May 2021 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 324000](https://www.bls.gov/oes/2021/may/naics3_324000.htm) (accessed 2026-07-22): Broader-subsector occupation mix and employment shares used to bound wage-weighted AI task exposure.
- **S2** — [Petroleum and Coal Products Manufacturing: NAICS 324](https://www.bls.gov/iag/tgs/iag324.htm) (accessed 2026-07-22): Current broader-subsector occupation counts, wages, industry definition, and safety context.
- **S3** — [2026 Roadmap on Artificial Intelligence and Machine Learning for Smart Manufacturing](https://www.nist.gov/publications/2026-roadmap-artificial-intelligence-and-machine-learning-smart-manufacturing) (accessed 2026-07-22): AI opportunities in process control and quality assurance plus data, integration, explainability, and reliability barriers.
- **S4** — [Moove Lubricants Holdings F-1/A](https://www.sec.gov/Archives/edgar/data/2026793/000119312524229454/d824889df1a.htm) (accessed 2026-07-22): Lubricants value chain, formulation and service complexity, fragmentation, supply reliability, and real market and profit-pool growth forecasts.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): U.S. employer-business owner five-year sale or transfer intentions and long-term transferability evidence.
- **S6** — [Managing Used Oil: Answers to Frequent Questions for Businesses](https://www.epa.gov/hw/managing-used-oil-answers-frequent-questions-businesses) (accessed 2026-07-22): Physical handling, analysis, recordkeeping, recycling, and compliance requirements surrounding used lubricant oil.
