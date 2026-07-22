# 811310 — Commercial and Industrial Machinery and Equipment (except Automotive and Electronic) Repair and Maintenance

*v5.1 Stage 1 research memo. Run `811310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.77 · L 2.50 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The need to keep increasingly automated high-cost equipment operating safely.
**Weakness:** Uneven value capture across contracts, compounded by cyclical end markets and service-line heterogeneity.

## Business-model lens
- Included: Independent repair and maintenance of agricultural, heavy, construction, mining, material-handling, machine-tool, commercial refrigeration, and other commercial or industrial machinery, including welding repair and machinery-related blade or saw sharpening.
- Excluded: Automotive, electronic, and precision repair; manufacturing and substantial remanufacturing; captive customer maintenance; facilities services not primarily machinery repair; and internal equipment-rental repair.
- Customer and revenue model: Businesses buy emergency field service, shop rebuilds, preventive maintenance, inspection, welding, sharpening, parts and labor, and uptime contracts through time-and-materials, call-out, fixed-scope, markup, and recurring charges.
- Deviation from default lens: none

## Executive view
Industrial machinery repair combines durable physical necessity with AI-enabled planning and diagnosis, though cyclicality, OEM control, and heterogeneity require discipline.

## How AI changes the work
AI is credible in predictive maintenance, fault isolation, retrieval, triage, quoting, dispatch, and parts planning; execution remains physical and safety-sensitive.

## Value capture
Faster resolution and technician leverage create value, but time-based billing can transfer productivity gains directly to customers.

## Firm availability
The estimated firm base and succession support search capacity, though many targets are small, concentrated, and owner-dependent.

## Demand durability
Automation increases complexity and maintenance need; downtime costs and installed capital support demand, while industrial cycles create volatility.

## Risks and uncertainty
Service lines differ in maturity, cyclicality, skills, OEM access, and contract economics, and the frozen firm count is estimated.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4035 | — | OBSERVED | — |
| n | — | 1513 | — | ESTIMATE | — |
| a | 0.18 | 0.31 | 0.44 | PROXY | S2, S4, S5, S6 |
| rho | 0.3 | 0.5 | 0.68 | PROXY | S4, S5, S6 |
| e | 0.58 | 0.75 | 0.89 | ESTIMATE | S1, S8 |
| s5 | 0.09 | 0.18 | 0.3 | PROXY | S7, S9 |
| q | 0.4 | 0.59 | 0.74 | ESTIMATE | — |
| d5 | 0.99 | 1.1 | 1.24 | PROXY | S3, S5 |
| o | 0.92 | 0.97 | 0.995 | ESTIMATE | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.87 | 2.50 | 4.83 | PROXY |
| F | 7.05 | 8.56 | 9.66 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.11 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Large-enterprise evidence may not transfer to small contractors.
- a: Predictive maintenance can shift timing without reducing labor.
- rho: Surveys emphasize manufacturers rather than external providers.
- rho: Vendor sponsorship may overstate momentum.
- e: Externalization varies by service line.
- e: The frozen firm count is itself estimated.
- s5: Exit intent does not guarantee a sale.
- s5: Deal commentary favors larger transactions.
- q: Efficiency may reduce billed hours.
- q: Contract form determines capture.
- d5: Occupational growth is not real revenue growth.
- d5: Industrial cycles can dominate short periods.
- o: Monitoring may prevent failures.
- o: Modularity can shift repair to centralized rebuilds.

## Sources
- **S1** — [2022 NAICS Definition: 811310](https://www.census.gov/naics/?details=811310&input=811310&year=2022) (accessed 2026-07-22): Defines included commercial and industrial machinery repair.
- **S2** — [BLS Occupational Employment: NAICS 811300](https://www.bls.gov/oes/2023/may/naics4_811300.htm) (accessed 2026-07-22): Shows the exact industry's repair-heavy occupational mix.
- **S3** — [BLS Outlook: Industrial Machinery Mechanics](https://www.bls.gov/ooh/installation-maintenance-and-repair/industrial-machinery-mechanics-and-maintenance-workers-and-millwrights.htm) (accessed 2026-07-22): Supports strong demand and automation-related maintenance need.
- **S4** — [AI in Predictive Maintenance](https://www.deloitte.com/global/en/Industries/consumer/analysis/using-ai-in-predictive-maintenance-to-forecast-the-future.html?icid=mosaic-grid_using-ai_in_predictive_maintenance_to_forecast_the_future) (accessed 2026-07-22): Describes predictive-maintenance opportunity and implementation requirements.
- **S5** — [2025 Smart Manufacturing Survey](https://www.deloitte.com/us/en/insights/industry/manufacturing-industrial-products/2025-smart-manufacturing-survey.html) (accessed 2026-07-22): Documents operational priorities, maintenance maturity, and implementation barriers.
- **S6** — [Fluke Predictive Maintenance Survey](https://pressroom.fluke.com/fluke-survey-finds-predictive-maintenance-adoption-doubles-as-manufacturers-boost-digital-investment/) (accessed 2026-07-22): Supports rising digital investment and continuing skill obstacles.
- **S7** — [Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Provides a cross-industry exit-intention anchor.
- **S8** — [FTC and States Sue Deere over Repair Restrictions](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-states-sue-deere-company-protect-farmers-unfair-corporate-tactics-high-repair-costs) (accessed 2026-07-22): Supports proprietary-access risk in agricultural and industrial equipment repair.
- **S9** — [2025 Industrials and Services M&A Outlook](https://www.pwc.com/gx/en/services/deals/trends/2025/industrials-services.html) (accessed 2026-07-22): Supports buyer interest in industrial services and efficiency capabilities.
