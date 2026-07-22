# 485991 — Special Needs Transportation

*v5.1 Stage 1 research memo. Run `485991-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.88 · L 2.19 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable physical transport obligations paired with automatable scheduling, dispatch, billing, and compliance workflows.
**Weakness:** Payer and broker pricing power can absorb efficiency gains while most labor remains tied to human driving and passenger assistance.

## Business-model lens
- Included: Private lower-middle-market operators repeatedly transporting elderly, disabled, infirm, or otherwise special-needs passengers, including nonemergency medical transportation and contracted paratransit, using accessible or conventional passenger vehicles.
- Excluded: Ambulance services with medical care, school or employee bus transportation, public transit agencies, captive fleets, nonprofits without transferable control economics, pure brokers or software vendors, and occasional point-to-point operators outside special-needs transportation.
- Customer and revenue model: Recurring and repeat trips paid by Medicaid agencies, managed-care plans, transportation brokers, transit authorities, care institutions, and private-pay passengers; revenue commonly follows awarded contracts or authorized fee-for-service trips, mileage, and vehicle/service categories.
- Deviation from default lens: none

## Executive view
Special-needs transportation combines durable, often mandated trip demand with a highly physical driver base. The practical AI opportunity is concentrated in scheduling, dispatch, intake, billing, documentation, and exception management rather than replacing the ride itself.

## How AI changes the work
AI-assisted intake can structure trip requests, optimize manifests, predict lateness and no-shows, surface compliance exceptions, prepare claims, and support dispatchers. Human review remains important when mobility equipment, caregiver accompaniment, same-day changes, passenger vulnerability, or payer authorization rules make a trip nonstandard.

## Value capture
Savings can be retained during fixed-rate contract periods and converted into capacity, reliability, or margin. Retention is constrained by competitive procurement, administered reimbursement, broker leverage, audits, renewal repricing, and rules that can deny payment for no-shows, unloaded miles, or documentation failures.

## Firm availability
Many scaled operators should fit a repeat outsourced-service lens, but transferability depends on licenses, insurance, vehicle quality, payer credentials, compliance history, and whether customer and dispatcher relationships survive the owner. Cross-industry employer-owner evidence suggests meaningful but not abundant five-year transfer flow.

## Demand durability
An aging population, Medicaid's statutory transportation assurance, and ADA complementary-paratransit duties support the need for transport. Telehealth, ride sharing, family reimbursement, public transit coordination, and funding pressure can temper trip growth, but most remaining rides still require a physically accountable operator.

## Risks and uncertainty
The sharpest uncertainties are the absence of six-digit occupation data, uneven state reimbursement and broker practices, unknown private-firm technology baselines, insurance and driver constraints, fraud and audit exposure, and the gap between owner transfer plans and completed control deals. The industry would be unattractive where payer rates fail to cover labor and vehicle costs or where contracts can immediately reclaim efficiency gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5523 | — | OBSERVED | — |
| n | — | 197 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S1, S2 |
| rho | 0.35 | 0.55 | 0.72 | PROXY | S2, S5 |
| e | 0.55 | 0.72 | 0.85 | ESTIMATE | S4, S5, S7 |
| s5 | 0.15 | 0.22 | 0.32 | PROXY | S3 |
| q | 0.3 | 0.5 | 0.68 | ESTIMATE | S4, S5 |
| d5 | 0.98 | 1.05 | 1.15 | PROXY | S6, S8, S4, S7 |
| o | 0.86 | 0.93 | 0.98 | ESTIMATE | S4, S5, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.77 | 2.19 | 4.45 | PROXY |
| F | 4.58 | 5.59 | 6.43 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.43 | 9.77 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is at NAICS 4859 rather than 485991 and includes materially different shuttle activities.
- a: Employment shares are used as a bridge to wage-weighted task shares; no directly measured AI-task exposure exists for this industry.
- a: The frozen compensation-to-receipts input uses 2024 wages over 2022 receipts and is harmonized to the IPS basis as stated in the assignment.
- rho: The adoption evidence concerns public ADA paratransit agencies, not private LMM NEMT firms.
- rho: Continuous dynamic optimization is narrower than the full set of AI-enabled workflows considered here.
- rho: Implementation varies with payer portals, broker interfaces, state rules, and fleet dispatch practices.
- e: No source measures lens eligibility among LMM firms in NAICS 485991.
- e: NAICS 485991 includes nonmedical special-needs and pet transportation as well as NEMT and paratransit.
- e: The frozen firm count is a margin-bridged estimate from SUSB size classes rather than observed EBITDA-band firms.
- s5: The Gallup statistic covers employer businesses across industries and business sizes.
- s5: Stated plans are not completed transfers and include gifts or rare public offerings.
- s5: Internal reorganizations and closures are excluded from the target construct.
- q: Retention differs sharply among fixed-fee contracts, state fee schedules, broker subcontracts, and private-pay trips.
- q: No source directly measures pass-through of automation savings in special-needs transportation.
- q: This primitive excludes demand loss and implementation difficulty, which are represented elsewhere.
- d5: Neither source directly measures constant-price, constant-quality quantity for private NAICS 485991 operators.
- d5: National aging does not map one-for-one to transportation eligibility or utilization.
- d5: Public ADA paratransit obligations and Medicaid transportation assurances do not guarantee private-provider volumes or adequate funding.
- o: No source directly estimates five-year operator-required share.
- o: Autonomous accessible-vehicle deployment and regulatory acceptance are uncertain.
- o: The estimate concerns retention of an accountable operator, not retention of every current driver or administrative task.

## Sources
- **S1** — [Other Transit and Ground Passenger Transportation — May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_485900.htm) (accessed 2026-07-22): Broader NAICS 4859 occupation mix: transportation occupations 74.40%, passenger-vehicle drivers 64.64%, shuttle drivers/chauffeurs 52.75%, and office/administrative support 15.10% of employment.
- **S2** — [Consider Technology Vendor Sustainability Factors When Considering Deployment of New Automated Scheduling/Dispatching Services for ADA Paratransit Operations](https://www.itskrs.its.dot.gov/2023-l01179) (accessed 2026-07-22): DOT summary of a 2022 study in which 11 of 24 surveyed transit agencies used continuous dynamic optimization daily for ADA paratransit; the technology addressed unassigned trips and same-day productivity and performance.
- **S3** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall-2024 US survey: 22% of employer-business owners reported plans to sell or transfer ownership within five years, versus 9% of nonemployers.
- **S4** — [Assurance of Transportation](https://www.medicaid.gov/medicaid/benefits/assurance-of-transportation) (accessed 2026-07-22): Federal regulations and statute require state Medicaid plans to assure necessary transportation, with NEMT payment methods consistent with efficiency, economy, and quality of care.
- **S5** — [Medicaid Non-Emergency Medical Transportation Booklet for Providers](https://www.cms.gov/medicare-medicaid-coordination/fraud-prevention/medicaid-integrity-education/downloads/nemt-booklet.pdf) (accessed 2026-07-22): Documents broker, managed-care, and direct-vendor delivery models; competitive broker selection; state preauthorization variation; qualified-driver requirements; and payment considerations including loaded mileage and no-shows.
- **S6** — [Occupational projections and worker characteristics, 2024–2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): BLS projects passenger-vehicle-driver employment from 994,000 in 2024 to 1,040,600 in 2034, a 4.7% increase; shuttle drivers and chauffeurs are projected to grow 6.7%.
- **S7** — [Part 37—Transportation Services for Individuals with Disabilities](https://www.transit.dot.gov/regulations-and-guidance/civil-rights-ada/part-37-transportation-services-individuals-disabilities) (accessed 2026-07-22): Requires public fixed-route entities to provide comparable complementary paratransit to eligible individuals and describes service, eligibility, coordination, and efficiency requirements.
- **S8** — [Older Adults Outnumber Children in 11 States and Nearly Half of U.S. Counties](https://www.census.gov/newsroom/press-releases/2025/older-adults-outnumber-children.html) (accessed 2026-07-22): The US population age 65 and older rose 3.1% to 61.2 million from 2023 to 2024, reaching 18.0% of the population.
