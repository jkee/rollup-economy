# 713940 — Fitness and Recreational Sports Centers

*v5.1 Stage 1 research memo. Run `713940-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.68 · L 2.26 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring membership billing and a sizable front-office workforce create a practical path to retain AI-enabled administrative savings.
**Weakness:** Most value still depends on a competitive, capital-intensive physical facility and in-person service that software cannot eliminate.

## Business-model lens
- Included: US lower-middle-market firms operating gyms, fitness centers, fitness studios, swimming facilities, skating rinks, and racquet or other recreational sports centers for external members and repeat users.
- Excluded: Government or captive employee facilities, passive property or financing vehicles, non-control interests, independent instructors without an operated facility, and sports instruction businesses classified outside NAICS 713940.
- Customer and revenue model: Consumers and organizations pay recurring monthly or annual memberships plus enrollment, class, training, court, pool, program, day-pass, event, and ancillary retail fees; some facilities operate through franchises or nonprofit ownership.
- Deviation from default lens: none

## Executive view
Fitness and recreational sports centers have strong recurring billing, broad consumer participation, and a meaningful administrative labor layer, but their core service remains a physical venue with trainers, attendants, cleaning, maintenance, and safety obligations. AI can improve front-office economics and member engagement without replacing most service delivery. The opportunity is vulnerable to local competition, member churn, lease and equipment commitments, franchise restrictions, and the wide variation between gyms, studios, pools, rinks, and racquet facilities.

## How AI changes the work
The clearest uses are lead response, membership sales support, scheduling, billing recovery, routine member service, marketing creation, reporting, staff administration, and workout-plan drafting. Live coaching, group instruction, lifeguarding, cleaning, maintenance, equipment supervision, and high-empathy retention conversations remain substantially human and on-site.

## Value capture
Fixed monthly and annual dues let operators retain savings more readily than cost-plus businesses, and automated billing makes revenue predictable. Competitive promotions and low switching costs constrain retention, while franchisor fees, local marketing, service reinvestment, and member expectations absorb part of the gross benefit.

## Firm availability
Most LMM operators should qualify as repeat external services, and both marketplace transactions and franchise transfers show that clubs can change control. The direct five-year transfer rate is not observed, however, and leases, franchisor approval, nonprofit ownership, owner dependence, and distressed closures reduce practical transferability.

## Demand durability
US facility memberships and visits reached records in 2025, with broad demographic participation and strong active-aging growth. Aggregate demand appears durable, but individual firms can lose share quickly to new budget chains, premium formats, studios, home fitness, or nearby facilities, especially when capital expenditure and cleanliness lag.

## Risks and uncertainty
The key gaps are establishment-level task adoption, realized AI labor savings, firm-level eligibility, and a denominator-matched LMM transfer series. Occupation data predate the current AI cycle, trade-association growth may not accrue to independents, and scaled public franchises may not represent smaller facilities. Lease liabilities, equipment replacement, safety incidents, seasonality, and local saturation can overwhelm administrative savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3964 | — | OBSERVED | — |
| n | — | 937 | — | ESTIMATE | — |
| a | 0.15 | 0.23 | 0.32 | ESTIMATE | S2, S3 |
| rho | 0.48 | 0.62 | 0.76 | ESTIMATE | S3, S6 |
| e | 0.78 | 0.88 | 0.95 | ESTIMATE | S1, S6, S7 |
| s5 | 0.14 | 0.23 | 0.33 | ESTIMATE | S6, S7, S8 |
| q | 0.55 | 0.7 | 0.83 | ESTIMATE | S3, S6 |
| d5 | 0.99 | 1.16 | 1.32 | PROXY | S4, S5, S6 |
| o | 0.84 | 0.91 | 0.97 | ESTIMATE | S1, S2, S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.14 | 2.26 | 3.86 | ESTIMATE |
| F | 7.46 | 8.45 | 9.15 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.32 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS measures occupations and wages, not task-level AI exposure or current software adoption.
- a: The NAICS mix spans low-staff gyms, instructor-led studios, pools, skating rinks, and racquet centers with very different labor models.
- a: Contract instructors and owner labor may be incompletely represented in employer payroll data.
- rho: Software feature availability does not establish adoption or realized labor avoidance.
- rho: Large franchised systems have more standardized data and rollout capacity than independent LMM operators.
- rho: Implementation excludes pricing, demand, and valuation effects.
- e: No source measures eligibility within the supplied LMM population.
- e: The code includes materially different facility types and nonprofit ownership is more common in some subsegments.
- e: The supplied n is a margin-bridged estimate rather than an observed count of normalized-EBITDA firms.
- s5: BizBuySell publishes transaction benchmarks but not a complete LMM firm-level transfer denominator on the fetched page.
- s5: Planet Fitness transfers are for one branded multi-unit system and are not representative of all facility types.
- s5: The owner-age statistic covers US small businesses generally rather than fitness-center owners.
- q: Planet Fitness is a scaled, value-priced franchise and may have different pricing power and operating leverage from independent clubs and boutique studios.
- q: The estimate discounts future sharing through renewal pricing and competition but excludes demand volume effects.
- q: Some savings may be absorbed by higher wages, equipment refresh, rent, insurance, or increased service rather than retained as profit.
- d5: HFA membership and visitation include facilities outside the LMM firm lens and do not adjust for quality or market-share shifts.
- d5: Recent growth follows pandemic disruption and may not represent a steady five-year rate.
- d5: Planet Fitness growth reflects one scaled format and includes international clubs in some reported totals.
- o: Operator-required share differs sharply between access-only gyms and pools, skating rinks, racquet clubs, and instructor-led studios.
- o: The estimate concerns accountable operators, not the number of on-site employees.
- o: Changes in liability rules, remote monitoring, and access-control technology could alter the result.

## Sources
- **S1** — [2022 NAICS Definition: 713940 Fitness and Recreational Sports Centers](https://www.census.gov/naics/?details=71394&input=71394&year=2022) (accessed 2026-07-22): Defines the industry as establishments operating fitness and recreational sports facilities for exercise, conditioning, swimming, skating, and racquet sports; supports the facility-based lens and heterogeneous service basket.
- **S2** — [Fitness and Recreational Sports Centers - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics5_713940.htm) (accessed 2026-07-22): Reports 594,740 total workers and exact six-digit occupation shares, including exercise trainers and group fitness instructors at 30.94%, office and administrative support at 17.00%, amusement and recreation attendants at 8.13%, management at 5.55%, sales at 4.19%, lifeguards and related workers at 4.51%, and janitors at 2.97%; anchors the wage-weighted task assessment.
- **S3** — [Daxko Club Automation](https://www.clubautomation.com/) (accessed 2026-07-22): Documents currently available club software for membership management, payments, scheduling, reporting, automated follow-up, AI-powered communication, and billing recovery; supports exposure and implementation feasibility, not realized savings.
- **S4** — [81 Million Americans Were Members of a Fitness Facility in 2025, New HFA Report Finds](https://www.healthandfitness.org/81-million-americans-were-members-of-a-fitness-facility-in-2025-new-hfa-report-finds/) (accessed 2026-07-22): Reports 81 million US fitness-facility members in 2025, up 5.2%, more than 100 million total users, nearly 7 billion visits, 26.1% population penetration, and broad demographic growth; supports demand durability and continued use of physical facilities.
- **S5** — [2025 Fitness Industry Foot Traffic Trends: Budget Gyms Booming, Engagement Up Across All Segments](https://www.healthandfitness.org/2025-fitness-industry-foot-traffic-trends-budget-gyms-booming-engagement-up-across-all-segments/) (accessed 2026-07-22): Reports first-half 2025 US fitness-facility visits up 3.5% year over year and monthly visits per user up 1.4%, based on a tracker covering nearly 11,000 facilities; supports the demand proxy and format competition.
- **S6** — [Planet Fitness, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1637207/000163720726000011/plnt-20251231.htm) (accessed 2026-07-22): Reports recurring monthly and annual billing, more than 90% recurring club and franchise revenue, predictable centralized billing, fixed or semi-fixed rent and labor, 20.8 million members, 2,896 clubs, franchise transfer fees, and 8 clubs refranchised in 2025; supports revenue structure, capture, operator need, and transferability.
- **S7** — [Gym & Fitness Center Business Valuation Multiples & Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/gym-fitness-center/) (accessed 2026-07-22): Provides transaction-derived benchmarks for gym and fitness-center businesses sold from 2021 through 2025, confirming an operating-business sale market and describing the size profile of reported sales; it does not provide a complete industry transfer denominator.
- **S8** — [Starting a small business is hard. Exiting can be even harder, but planning early is the key](https://apnews.com/article/small-business-succession-retirement-sale-transition-d582a18f1e440846a6ff5bb425ba6daa) (accessed 2026-07-22): Reports that 51% of US small-business owners are over age 55 and describes outsider sales, family succession, internal succession, and closure as competing exit paths; used as broad succession context.
