# 441340 — Tire Dealers

*v5.1 Stage 1 research memo. Run `441340-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → CONDITIONAL · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Durable replacement demand paired with repeatable customer-intake, scheduling, quoting, inventory, and administrative workflows across multi-location operators.
**Weakness:** No defensible LMM firm-count estimate, compounded by a physical labor core that limits the share of wages AI can substitute.

## Business-model lens
- Included: Independent and regional tire dealers in the lower-middle-market band that repeatedly sell, fit, balance, rotate, inspect, and repair tires for external retail or fleet customers, including locations that also provide adjacent automotive repair.
- Excluded: Pure product wholesalers, tire manufacturers and retreaders, captive dealership service departments, national-chain corporate stores, non-operating finance vehicles, and shops without transferable customer, workforce, or operating systems.
- Customer and revenue model: Repeat consumer and fleet visits produce transaction revenue from tires plus installation, balancing, rotation, repair, alignment, and related service labor; some fleet relationships are account-based, but most consumer work is episodic rather than contracted.
- Deviation from default lens: none

## Executive view
Tire dealers combine durable, physically delivered replacement demand with a meaningful but bounded opportunity to automate the customer and administrative layer. The operating opportunity is strongest in multi-location firms where call handling, scheduling, quoting, purchasing, reminders, and management reporting repeat at scale; it is weaker in owner-run shops and in the technician work itself.

## How AI changes the work
AI can answer and triage calls, prepare fitment-aware quotes, schedule bays, draft inspection explanations, trigger maintenance reminders, assist inventory ordering, summarize store performance, and reduce routine bookkeeping effort. It can support diagnostics and technician documentation, but mounting, balancing, inspection, driving, material handling, and most repairs remain physical and safety-sensitive.

## Value capture
Savings can appear as avoided service-writer and administrative hiring, improved quote conversion, fewer missed calls, better bay use, and tighter stock. Installed-tire pricing is easy to compare and fleet accounts can be rebid, so some benefit will migrate to customers; convenience, speed, and constrained local service capacity preserve a meaningful retained share.

## Firm availability
Employer tire and auto-service businesses do transact, and aging owners create a transfer pipeline. Still, many establishments are chain-controlled, too small, franchise-constrained, owner-dependent, or predominantly product retail, and the supplied dataset has no defensible LMM firm-count band, making absolute availability the central unresolved issue.

## Demand durability
Replacement tire shipments remain broadly stable, and every mainstream vehicle powertrain continues to require tires, inspection, and installation. Online tire shopping may shift customer acquisition and product margin, but the physical last mile of fitment and roadworthiness remains local; channel loss rather than disappearance of tire need is the main demand risk.

## Risks and uncertainty
The largest evidence gaps are 441340-specific occupation weights, a true LMM firm denominator, transfer completion rates, and measured post-deployment labor outcomes. Competitive price transparency, franchise rules, technician shortages, product liability, inconsistent point-of-sale data, customer resistance to automated advice, and consolidation by large chains could each weaken the thesis.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2114 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.17 | 0.27 | 0.38 | PROXY | S2, S3, S4 |
| rho | 0.34 | 0.53 | 0.71 | PROXY | S5, S3, S4 |
| e | 0.24 | 0.44 | 0.64 | ESTIMATE | S1, S8 |
| s5 | 0.12 | 0.21 | 0.31 | PROXY | S7, S8 |
| q | 0.38 | 0.57 | 0.74 | ESTIMATE | S1, S8 |
| d5 | 0.92 | 1.03 | 1.14 | PROXY | S6 |
| o | 0.84 | 0.92 | 0.97 | PROXY | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.49 | 1.21 | 2.28 | PROXY |
| F | — | — | — | MISSING |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.73 | 9.48 | 10.00 | PROXY |

## Caveats
- a: The occupation mix is for NAICS 441300 and includes automotive parts retailers.
- a: ORS requirements describe occupations economy-wide, not tire-dealer establishments.
- a: Task exposure is inferred rather than directly measured, and current point-of-sale automation varies widely.
- rho: BTOS measures use of any AI function, not implementation depth or labor savings.
- rho: Retail Trade is broader and may differ from service-intensive tire dealerships.
- rho: Five-year technology performance and vendor integration are uncertain.
- e: The supplied firm-count input is missing, so this share cannot establish an absolute eligible-firm count.
- e: NAICS includes both tire-only retail and tire retail combined with automotive repair.
- e: Public transaction listings skew toward smaller and voluntarily marketed businesses.
- s5: Gallup covers all industries and reports intentions, not completed transfers.
- s5: BizBuySell combines tire-relevant shops with broader auto repair and represents only reported marketplace transactions.
- s5: Transfers may be more common among employer firms but less common in the specific EBITDA band.
- q: No source directly measures contractual or competitive pass-through of AI savings in tire retail.
- q: Retention differs between product margin, service labor, national accounts, and local retail work.
- q: The estimate excludes demand-volume effects and implementation failure.
- d5: A one-year industry forecast is not a five-year demand projection.
- d5: Shipments include channels and original-equipment tires outside the operating lens.
- d5: Units do not directly capture real service intensity or dealer channel share.
- o: ORS is occupation-wide and current, not tire-specific or forward-looking.
- o: Operator requirement is distinct from the number of workers needed per transaction.
- o: The upper bound assumes no rapid breakthrough in economical small-shop robotics.

## Sources
- **S1** — [2022 NAICS Definition: 441340 Tire Dealers](https://www.census.gov/naics/?details=441340&input=441340&year=2022) (accessed 2026-07-22): Defines the industry as retailers of new or used tires and tubes, including new-tire retail combined with automotive repair, and identifies excluded retreading and wholesale activities.
- **S2** — [BLS Data Tables for OEWS Industry Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest occupations and employment counts in NAICS 441300, including parts salespersons, tire repairers/changers, drivers, retail salespersons, technicians, supervisors, and managers.
- **S3** — [BLS Occupational Requirements Survey: Retail Salespersons](https://www.bls.gov/ors/factsheet/retail-salespersons.htm) (accessed 2026-07-22): Documents in-person and physical requirements: speaking for more than 99.5% of workers, low-posture work for 85.1%, and routine telework for less than 5%.
- **S4** — [BLS Occupational Requirements Survey: Installation, Maintenance, and Repair Workers](https://www.bls.gov/ors/factsheet/pdf/installation-maintenance-and-repair-occupations.pdf) (accessed 2026-07-22): Reports that work was controlled by people for 88.9% of these workers in 2025 and routine telework was allowed for less than 0.5%.
- **S5** — [Census Bureau: Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports December 2025-May 2026 BTOS adoption evidence, including approximately 14% current and 17% expected AI use in Retail Trade and lower adoption among the smallest firms.
- **S6** — [USTMA February 2026 Forecast Predicts Slightly Higher 2026 Tire Shipments](https://www.ustires.org/newsroom/ustma-february-2026-forecast) (accessed 2026-07-22): Projects 338.9 million total U.S. tire shipments in 2026 versus 336.3 million in 2025 and 332.7 million in 2019, with modest growth in replacement categories.
- **S7** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 2024 survey evidence on five-year plans: 14% of all primary owners, 17% of owners age 55 or older, and 22% of employer-business owners planned to sell or transfer ownership.
- **S8** — [BizBuySell 2025 Fourth Quarter Insight Report](https://www.bizbuysell.com/news/bizbuysell-2025-fourth-quarter-insight-report/) (accessed 2026-07-22): Reports 247 completed Auto Repair and Service Shop sales in 2025 and broader seller and broker evidence on retirement-driven transaction supply; the category is adjacent rather than tire-dealer-specific.
