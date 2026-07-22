# 812113 — Nail Salons

*v5.1 Stage 1 research memo. Run `812113-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.55 · L 0.85 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat consumer demand for a physical service keeps an accountable local operator necessary while centralized front-office workflows offer a modest AI opportunity.
**Weakness:** Most labor is hands-on and non-substitutable, and only four firms are estimated to occupy the target EBITDA band.

## Business-model lens
- Included: Lower-middle-market firms operating nail salons that repeatedly provide manicures, pedicures, nail extensions, nail art, and related nail-care services directly to external consumers, including multi-location operators and franchisees when the operating firm controls service delivery.
- Excluded: Independent booth renters or sole technicians outside the EBITDA band; beauty salons whose primary activity is not nail care; product-only retailers; cosmetology schools; captive units; passive franchisors without operating service delivery; shells; and non-control financing vehicles.
- Customer and revenue model: Consumers typically buy appointment-based, posted-price services and return periodically; add-on nail art, premium treatments, tips, memberships, and product sales can supplement service revenue. Revenue is predominantly transactional and local rather than governed by cost-plus contracts or negotiated enterprise pass-through clauses.
- Deviation from default lens: none

## Executive view
Nail salons fit the recurring external-service lens, but their economic core is licensed, close-contact manual work rather than information work. AI can improve a multi-site operator's front office and customer acquisition, yet the frozen labor ratio likely misses contractor and owner labor, while the estimated population contains only four firms in the EBITDA band.

## How AI changes the work
The practical use cases are scheduling support, reminders, multilingual customer messaging, marketing content, review response, demand forecasting, inventory assistance, design ideation, and routine management reporting. Cleaning, trimming, filing, polishing, extensions, massage, sanitation, client assessment, and intricate nail art remain hands-on.

## Value capture
Posted-price consumer services provide no automatic pass-through, so early savings can be retained. Over time, local competition, low switching costs, promotions, staff compensation, and reinvestment in convenience or experience should share a material portion with customers and workers.

## Firm availability
Independent salons trade regularly, but observed marketplace businesses are far smaller than the frozen EBITDA band. The four-firm estimate is unusually sensitive to the generic margin bridge, classification, multi-unit ownership, and normalization of contractor labor.

## Demand durability
BLS expects continued growth and characterizes the service as a low-cost luxury demanded across income levels. Demand is still discretionary and cyclical, but the current service basket is resistant to software substitution because it requires physical delivery.

## Risks and uncertainty
The major measurement risks are omitted contractor and owner labor, a vintage mismatch in the frozen labor ratio, a tiny estimated band population, and transaction evidence drawn from subscale salons. Operational risks include technician retention, licensing, sanitation, local competition, lease exposure, and inconsistent data systems across sites.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3687 | — | OBSERVED | — |
| n | — | 4 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.22 | PROXY | S1, S2, S3 |
| rho | 0.45 | 0.65 | 0.82 | PROXY | S3, S4 |
| e | 0.9 | 0.96 | 0.99 | PROXY | S1, S2, S5 |
| s5 | 0.1 | 0.18 | 0.28 | PROXY | S5, S6, S7 |
| q | 0.42 | 0.58 | 0.72 | PROXY | S5, S6 |
| d5 | 0.92 | 1.035 | 1.12 | PROXY | S2 |
| o | 0.95 | 0.985 | 0.998 | PROXY | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.53 | 1.34 | 2.66 | PROXY |
| F | 0.49 | 0.85 | 1.20 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | PROXY |
| D | 8.74 | 10.00 | 10.00 | PROXY |

## Caveats
- a: No source measures wage-weighted task exposure specifically for 812113.
- a: BLS reports that 28% of manicurists and pedicurists were self-employed in 2024, so QCEW wages can omit owner and contractor labor that is economically central to salons.
- a: The frozen compensation ratio combines 2024 wages with 2022 receipts and may understate effective labor intensity where technicians are paid as contractors or booth renters.
- rho: The adoption study is economy-wide and does not isolate personal-care firms.
- rho: Reported AI use is not equivalent to implemented labor-hour reduction.
- rho: Digital booking and payment already in place must not be counted again as future AI implementation.
- e: The frozen count of four is margin-bridged with a generic 15.65% margin rather than verified from named firms.
- e: BizBuySell's typical sold salon is far below the fixed EBITDA band and cannot validate the band population.
- e: SUSB firm classification may mix operating companies with multi-establishment or franchise structures.
- s5: The Gallup figure is cross-industry and intention-based.
- s5: BizBuySell does not cover every private transaction and its 2025 nail-salon median owner earnings were only $104,000.
- s5: The frozen band contains very few estimated firms, making realized transfer frequency highly discrete.
- q: Marketplace seller-discretionary-earnings data are self-reported and below the EBITDA band.
- q: Observed margin movement reflects many costs and does not identify AI benefit retention.
- q: Tips and contractor compensation can shift value outside reported firm margin.
- d5: The BLS forecast is occupation-wide and includes work outside nail salons.
- d5: Employment is not constant-price, constant-quality demand.
- d5: The five-year conversion is a judgment rather than an observed industry forecast.
- o: The estimate assumes no broad robotics breakthrough within five years.
- o: Operator-required quantity is distinct from the smaller share of administrative work exposed to AI.

## Sources
- **S1** — [2022 NAICS Definition: 812113 Nail Salons](https://www.census.gov/naics/?details=812113&input=812113&year=2022) (accessed 2026-07-22): Official classification of establishments primarily engaged in manicures, pedicures, nail extensions, and other nail-care services.
- **S2** — [Occupational Outlook Handbook: Manicurists and Pedicurists](https://www.bls.gov/ooh/personal-care-and-service/manicurists-and-pedicurists.htm) (accessed 2026-07-22): Hands-on duties, sanitation and licensure, employment setting, self-employment share, repeat-business importance, and 2024-to-2034 employment projection.
- **S3** — [O*NET OnLine: Manicurists and Pedicurists](https://www.onetonline.org/link/details/39-5092.00) (accessed 2026-07-22): Detailed physical and administrative tasks, physical proximity, repetitive motion, tool use, scheduling, records, inventory, and selling activities.
- **S4** — [The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html) (accessed 2026-07-22): National firm AI adoption, concentration in a few business functions, leading task uses, and limited observed employment reductions.
- **S5** — [Nail Salon Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/nail-salon/) (accessed 2026-07-22): Independent ownership, transaction characteristics, marketplace revenue and owner-earnings levels, and five-year financial and valuation trends.
- **S6** — [BizBuySell Insight Report Data Tables](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-22): 2025 marketplace count and financial characteristics of reported nail-salon sales.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year sale or ownership-transfer intentions among employer-business owners, used as a cross-industry transfer proxy.
