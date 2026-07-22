# 811191 — Automotive Oil Change and Lubrication Shops

*v5.1 Stage 1 research memo. Run `811191-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.29 · L 2.34 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Standardized vehicle-history, recommendation, retention, inventory, and labor workflows make AI implementation practical across repeated visits.
**Weakness:** Electrification and longer service intervals pressure underlying quantity while most on-site work remains physical and safety-accountable.

## Business-model lens
- Included: U.S. lower-middle-market quick-lube and preventive-maintenance operators whose primary work is motor-oil changes and chassis lubrication for passenger vehicles, vans, and trucks, including closely associated filter, fluid, battery, bulb, and wiper services delivered by stand-alone company-owned or franchised operating businesses.
- Excluded: General mechanical repair, tire-only service, dealer and fleet captive maintenance, gasoline stations where oil service is incidental, lubricant manufacturing and distribution, motorcycle service, do-it-yourself retail sales, pure franchisors without operating-company exposure, shells, non-control vehicles, and owner-dependent microshops.
- Customer and revenue model: Retail drivers and commercial fleets pay per completed preventive-maintenance service, often in a drive-through or stay-in-vehicle format. Revenue combines a core oil-change ticket with recommended filters, fluids, wipers, batteries, and checks; throughput depends on bay flow, technician teams, inventory availability, trust, and repeat maintenance intervals.
- Deviation from default lens: none

## Executive view
Quick lube is a coherent repeat service with highly standardized information, recommendation, and operating workflows, but the core job remains physical. AI can improve customer retention, recommendation consistency, inventory, staffing, and training while technicians continue to execute and verify the service.

## How AI changes the work
AI can recognize returning customers, interpret service history and OEM schedules, draft recommendations, personalize reminders, forecast parts and fluids, support training, schedule labor, and summarize exceptions. Technicians remain necessary for visual inspection, vehicle positioning, under-hood and pit work, fluid and filter handling, final verification, and spill or fault response.

## Value capture
High visit frequency and repeat records support conversion and planning benefits. Competitive pricing, franchise economics, software fees, customer skepticism about upselling, wage pressure, and finite bay throughput prevent full retention.

## Firm availability
The exact code fits the external-service lens, but franchise ownership and multi-site structures make firm counts and control boundaries ambiguous. Captive shops, pure franchisors, micro operators, and businesses outside the earnings band reduce the eligible population.

## Demand durability
A large installed combustion-engine fleet and modest VMT growth preserve the core need over five years. EV adoption, longer oil intervals, do-it-yourself service, and dealer competition keep the base case near flat rather than tracking VMT mechanically.

## Risks and uncertainty
The largest uncertainties are the mixed occupational proxy, pace of EV fleet penetration, oil-change interval behavior, franchise transfer structure, independent adoption of integrated tools, and conversion of broad owner intentions into qualifying control sales.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3622 | — | OBSERVED | — |
| n | — | 57 | — | ESTIMATE | — |
| a | 0.16 | 0.26 | 0.37 | PROXY | S1, S2, S3 |
| rho | 0.42 | 0.62 | 0.77 | ESTIMATE | S3 |
| e | 0.75 | 0.87 | 0.94 | ESTIMATE | S1, S3, S6 |
| s5 | 0.06 | 0.12 | 0.2 | PROXY | S7 |
| q | 0.4 | 0.58 | 0.73 | ESTIMATE | S3 |
| d5 | 0.94 | 0.99 | 1.07 | PROXY | S4, S5 |
| o | 0.93 | 0.98 | 0.995 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.97 | 2.34 | 4.13 | ESTIMATE |
| F | 2.04 | 3.12 | 3.96 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.74 | 9.70 | 10.00 | ESTIMATE |

## Caveats
- a: The five-digit occupational source mixes oil-change and car-wash labor models.
- a: AI recommendations still require technician observation and accountable customer approval.
- rho: Large-chain capabilities are not representative of all target firms.
- rho: Short service cycles leave little tolerance for slow or inaccurate recommendations.
- e: A franchise location is not necessarily a distinct transferable firm.
- e: The supplied target count is an estimate based on a broad service margin rather than observed exact-industry EBITDA.
- s5: The owner survey is broad and measures plans, not closings.
- s5: Asset sales, refranchising, and equity control transfers are not interchangeable.
- q: Recommendation lift can reflect more services sold rather than lower cost at constant quality.
- q: Aggressive automated upselling can erode trust and retention.
- d5: New-vehicle technology shares are not the in-service fleet mix.
- d5: Oil-change demand depends on mileage, interval policy, and owner compliance rather than VMT alone.
- o: Demand lost to EVs belongs primarily in d5, not in the operator-need estimate for remaining oil-service quantity.
- o: Software can reduce labor per visit while an accountable operating business remains necessary.

## Sources
- **S1** — [2022 NAICS Definition: 811191 Automotive Oil Change and Lubrication Shops](https://www.census.gov/naics/?details=8111&input=8111&year=2022) (accessed 2026-07-22): Official activity definition and cross-reference boundaries used for the lens and operator-need reasoning.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 811190](https://www.bls.gov/oes/2023/may/naics5_811190.htm) (accessed 2026-07-22): Five-digit other automotive repair and maintenance occupational mix used as a broad task-exposure proxy.
- **S3** — [Valvoline Inc. 2025 Annual Report on Form 10-K](https://www.sec.gov/Archives/edgar/data/1674910/000167491025000135/vvv-20250930.htm) (accessed 2026-07-22): Primary-company evidence on the 15-minute stay-in-vehicle format, technician inspection, service-history and OEM recommendation software, store network, and franchise structure.
- **S4** — [2025 FHWA Forecasts of Vehicle Miles Traveled](https://www.fhwa.dot.gov/policyinformation/tables/vmt/vmt_forecast_sum.cfm) (accessed 2026-07-22): Light-duty VMT forecast used as the primary maintenance-demand exposure proxy.
- **S5** — [Seventy-three Percent of All Light-Duty Vehicles Produced in 2023 Came with Gasoline Direct Injection](https://www.energy.gov/cmei/vehicles/articles/fotw-1331-february-26-2024-seventy-three-percent-all-light-duty-vehicles) (accessed 2026-07-22): DOE vehicle-technology production mix used to bound the near-term electrification headwind.
- **S6** — [2022 Economic Census: Other Services Basic Statistics](https://data.census.gov/table/ECNBASIC2022.EC2281BASIC?q=personal) (accessed 2026-07-22): Exact-industry establishment and revenue context used to qualify firm availability.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Employer-owner five-year sale and transfer intentions used as the broad starting point for the qualifying-control-transfer proxy.
