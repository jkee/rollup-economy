# 513210 — Software Publishers

*v5.1 Stage 1 research memo. Run `513210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** A large share of high-cost digital work is addressable by AI inside a recurring-revenue product model with strong technical capacity to deploy it.
**Weakness:** The lower-middle-market firm count is missing, while AI simultaneously lowers product-development barriers and may compress seats and pricing, making aggregate availability and retained value unusually uncertain.

## Business-model lens
- Included: Commercial software publishers serving external customers through subscriptions, term or perpetual licenses, usage charges, maintenance, support, and related recurring services, viewed at lower-middle-market EBITDA scale.
- Excluded: Custom software development performed primarily for one client, captive internal software teams, pure IT consulting, infrastructure hosting without a published software product, and pre-revenue projects without a demonstrated external customer model.
- Customer and revenue model: Businesses and consumers pay recurring subscriptions, usage-based charges, license fees, maintenance, support, advertising, or transaction-linked fees for standardized software products. Revenue can be highly recurring, although consumer applications, games, perpetual licenses, and usage-sensitive products are less predictable.
- Deviation from default lens: none

## Executive view
Software publishing combines unusually AI-exposed knowledge work with recurring, scalable revenue and continuing underlying demand. The opportunity is real but not uniform: defensible workflow products can retain productivity gains, while lightly differentiated applications face faster entry, seat compression, and customer insourcing. The missing lower-middle-market firm count prevents a reliable statement about aggregate target availability.

## How AI changes the work
Generative AI can accelerate coding, testing, documentation, product analysis, support, marketing, and administration. Technical readiness is high, but production reliability, security, review, architecture, customer context, and organizational adoption keep realized savings below theoretical exposure.

## Value capture
Subscription and usage-based models, switching costs, and high gross margins support retention of savings. Competitive repricing, growing model and cloud expense, reduced seat counts, open-source alternatives, and AI-native entrants can return a substantial portion of gains to customers or suppliers.

## Firm availability
Software M&A volume indicates active seller flow, but available deal evidence lacks a U.S. lower-middle-market denominator. The dataset supplies no usable n for this industry, so firm availability remains unmeasurable rather than inferred from transaction headlines.

## Demand durability
Cybersecurity, AI, automation, connected products, and ongoing digitization support real demand growth. Durability is strongest for embedded systems of record and mission-critical workflow products and weakest where customers can rapidly recreate functionality with foundation models or bundled platforms.

## Risks and uncertainty
The largest uncertainties are the missing firm count, occupation-to-task translation, uneven adoption by firm size, AI infrastructure costs, product substitution, pricing pressure, and software's wide variation in defensibility and customer concentration.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2525 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.36 | 0.52 | 0.66 | PROXY | S2, S4 |
| rho | 0.4 | 0.6 | 0.78 | PROXY | S3, S4 |
| e | 0.48 | 0.66 | 0.8 | ESTIMATE | S1, S7 |
| s5 | 0.07 | 0.14 | 0.23 | ESTIMATE | S6 |
| q | 0.36 | 0.56 | 0.74 | ESTIMATE | S7 |
| d5 | 1.02 | 1.1 | 1.2 | PROXY | S5 |
| o | 0.62 | 0.78 | 0.9 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.45 | 3.15 | 5.20 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 6.32 | 8.58 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation table is May 2023 and reports employment categories rather than task content.
- a: Google DORA surveyed technology professionals globally, not only U.S. lower-middle-market software publishers.
- a: The injected labor-intensity value is inherited from ancestor sector 51 and is LOW quality, so it may misstate this industry's compensation-to-receipts structure.
- rho: BTOS covers the entire Information sector rather than NAICS 513210 alone.
- rho: Reported tool use and perceived productivity are not equivalent to durable labor-cost realization.
- rho: DORA's trust findings imply review work can offset some gross time savings.
- e: The NAICS definition establishes activity, not profitability, independence, size, or revenue recurrence.
- e: The pricing survey covers 100 SaaS companies and is not a representative census of all software publishers.
- e: The firm-count input n is a declared dataset gap and must remain MISSING; this estimate does not replace or infer n.
- s5: Kroll's figures are global and cover the broader software sector across transaction sizes.
- s5: Deal counts do not identify unique sellers or provide the denominator needed for a seller-incidence rate.
- s5: Financing conditions and software valuation cycles can make a single period unrepresentative of a full five-year window.
- q: Pricing architecture indicates potential value capture but does not directly measure retained labor savings.
- q: The survey is small and focused on SaaS, excluding important software-publisher business models.
- q: AI may simultaneously lower costs and increase competitive entry or infrastructure spending.
- d5: Employment growth is only a proxy for constant-price demand and spans occupations across many industries.
- d5: Product mix varies from mature maintenance software to rapidly growing AI-native applications.
- d5: Nominal subscription growth can reflect price changes rather than real service demand.
- o: Persistence differs sharply between system-of-record software and lightly differentiated point applications.
- o: The estimate concerns the need for an operating entity, not whether current staffing levels persist.
- o: AI may create new publisher categories while displacing existing products.

## Sources
- **S1** — [2022 NAICS Definition: 513210 Software Publishers](https://www.census.gov/naics/?details=513210&input=513210&year=2022) (accessed 2026-07-22): Defines the industry as establishments primarily engaged in software publishing and distinguishes the activity from custom software services.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Software Publishers](https://www.bls.gov/oes/2023/may/naics4_513200.htm) (accessed 2026-07-22): Provides employment and wage distribution across computer, management, business, sales, and administrative occupations used to bridge to AI-addressable task share.
- **S3** — [Large Firms With At Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports current and expected AI use in the Information sector and adoption differences by firm size.
- **S4** — [How Are Developers Using AI? Inside Google's 2025 DORA Report](https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/) (accessed 2026-07-22): Reports developer AI adoption, perceived productivity and quality benefits, and low trust that constrains realization.
- **S5** — [Software Developers, Quality Assurance Analysts, and Testers](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) (accessed 2026-07-22): Provides 2024-2034 employment projections and demand drivers including AI, IoT, robotics, cybersecurity, and software embedded in more products.
- **S6** — [Global Software Sector Update—Fall 2025](https://www.kroll.com/en/publications/m-and-a/global-software-sector-update-fall-2025) (accessed 2026-07-22): Documents strong recent global software transaction volume and value, used cautiously to inform seller incidence.
- **S7** — [State of Usage-Based Pricing 2025](https://metronome.com/state-of-usage-based-pricing-2025) (accessed 2026-07-22): Describes adoption of usage-based pricing among surveyed SaaS companies and its alignment of revenue with customer usage and value.
