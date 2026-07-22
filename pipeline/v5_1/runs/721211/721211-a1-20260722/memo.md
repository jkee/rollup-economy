# 721211 — RV (Recreational Vehicle) Parks and Campgrounds

*v5.1 Stage 1 research memo. Run `721211-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.82 · L 1.12 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A concentrated office, reservation, customer-service, pricing, and management workflow layer can be standardized across otherwise fragmented physical park operations.
**Weakness:** Most labor and nearly all service continuity remain tied to site-specific physical operations, while land-heavy family ownership makes eligible control transfers uncertain.

## Business-model lens
- Included: Private operating companies that run RV parks and campgrounds for external guests, including short-stay and seasonal campsite accommodation, reservations, guest service, site utilities, washrooms, laundry, grounds, recreation amenities, camp stores, and related add-ons.
- Excluded: Public or nonprofit campgrounds, bare-land and residential mobile-home-site lessors, passive property-holding entities, non-control financing vehicles, captive internal facilities, recreational facilities without accommodation, and recreational or vacation camps classified outside NAICS 721211.
- Customer and revenue model: Direct-to-consumer accommodation sold by night, week, month, or season, with repeat visits and ancillary fees for site selection, amenities, rentals, retail, and activities; some parks also have longer-duration annual or membership-like arrangements.
- Deviation from default lens: none

## Executive view
RV parks and campgrounds combine a meaningful administrative automation pocket with an operation that remains anchored in physical property care. The clearest opportunities are reservations, guest communications, bookkeeping, marketing, scheduling, occupancy optimization, and pricing; the larger bodies of maintenance, grounds, housekeeping, safety, and recreation work are much less substitutable. Private operating firms generally fit the external-customer lens, but land-heavy structures and family ownership complicate transferability. Demand looks durable in the mixed camping basket, yet the 2025 decline in RV participation argues against assuming growth.

## How AI changes the work
AI and established campground systems can answer routine questions, take and modify bookings, process payments, send pre-arrival and in-stay messages, draft marketing, support bookkeeping, forecast occupancy, recommend prices, and optimize the site grid. Human work remains important for exceptions, complaints, sales judgment, safety, maintenance triage, guest recovery, and supervision. Physical execution across utilities, grounds, washrooms, housekeeping, repairs, food, and activities remains the limiting boundary.

## Value capture
Because accommodation and add-ons are sold at market prices rather than billed as reimbursed labor, savings can initially accrue to the operator. Scarce, well-located parks with constrained new supply may retain more through margin and reinvestment. Frequent repricing, online comparison, public alternatives, and guest expectations for visible service and amenities will share part of the benefit through price competition or service investment over five years.

## Firm availability
The industry definition largely describes active guest-facing operators, but the underlying asset often combines land, infrastructure, owner residence, and a family business. Sector brokers report active mid-market and value-add buying, while campground succession guidance emphasizes family transfers and emotional and estate complexity. A qualifying sale is plausible but far from automatic, and the key diligence need is a denominator-based record of operating-company control transfers rather than property listings.

## Demand durability
Camping participation remains above pre-pandemic benchmarks and vehicle-accessible camping grew in 2025, supporting continued need for sites and facilities. However, KOA reported a slight year-over-year reset in 2024 and OIA reported a 6.4% RV-camping decline in 2025. Fuel and RV costs, weather, public-site competition, and discretionary travel budgets create downside; affordability, domestic travel, constrained zoning, and broad tent and vehicle participation support the base case.

## Risks and uncertainty
The central evidence gaps are exact-721211 occupation and automation data, representative independent-park software adoption and realized labor savings, a firm-level eligibility census, and a completed control-transfer denominator. Vendor revenue claims may overstate typical results, and participation surveys do not isolate paid private site-nights. Seasonality, local regulation, catastrophe exposure, utility infrastructure, and the inseparability of operations from real estate can dominate the economics even when administrative automation works.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2816 | — | OBSERVED | — |
| n | — | 34 | — | ESTIMATE | — |
| a | 0.14 | 0.22 | 0.31 | PROXY | S1, S4, S5 |
| rho | 0.25 | 0.45 | 0.65 | PROXY | S3, S4, S5 |
| e | 0.55 | 0.78 | 0.9 | ESTIMATE | S6, S8 |
| s5 | 0.1 | 0.2 | 0.32 | ESTIMATE | S7, S8 |
| q | 0.35 | 0.55 | 0.75 | ESTIMATE | S4, S9 |
| d5 | 0.85 | 0.98 | 1.15 | PROXY | S9, S10 |
| o | 0.87 | 0.94 | 0.98 | ESTIMATE | S1, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.39 | 1.12 | 2.27 | PROXY |
| F | 1.70 | 2.96 | 3.83 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.39 | 9.21 | 10.00 | ESTIMATE |

## Caveats
- a: The latest accessible BLS industry occupation table is May 2023 and is four-digit NAICS 721200, which also includes recreational camps.
- a: BLS excludes self-employed workers, material in small owner-operated parks.
- a: Task exposure is judgmentally mapped from occupation groups and is not a direct measurement of hours saved in campgrounds.
- a: Vendor descriptions establish technical availability, not representative adoption or realized labor displacement.
- rho: Census evidence is not specific to NAICS 721211 and survey wording changed in late 2025.
- rho: Installed software does not prove sustained workflow use or headcount avoidance.
- rho: Small, seasonal, owner-operated parks may have limited process standardization and capital for integration.
- e: No source enumerates lens eligibility among firms in the injected EBITDA band.
- e: NAICS is assigned at establishment level while eligibility and the injected count are firm-level constructs.
- e: Campground value is often concentrated in land, complicating separation of transferable operations from property ownership.
- s5: Broker reports are marketing-oriented and do not provide a population denominator or completed-sale frequency.
- s5: Property transfers do not always transfer the operating company or constitute a qualifying control event.
- s5: Succession evidence is from a Wisconsin association and may not represent the national owner-age distribution.
- q: Campspot's reported revenue effects are vendor claims and may reflect selection into advanced pricing tools.
- q: Retention varies sharply by local scarcity, zoning, seasonality, public-campground competition, and guest segment.
- q: Annual and seasonal arrangements may retain gains differently from transient nightly bookings.
- d5: KOA includes Canada and is commissioned by a major campground franchisor.
- d5: Participation and trip spending are not equivalent to paid private campground site-nights.
- d5: The five-year horizon is exposed to fuel and RV ownership costs, weather and wildfire, household travel budgets, and local supply constraints.
- o: The estimate concerns the need for an accountable operator, not the amount of on-site labor.
- o: Local health, fire, pool, lodging, and utility rules vary and may raise the irreducible operator requirement.
- o: The occupation mix includes recreational camps as well as RV parks and campgrounds.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 721200](https://www.bls.gov/oes/2023/may/naics4_721200.htm) (accessed 2026-07-22): Direct BLS occupation mix for the broader RV parks and recreational camps industry: 64,480 workers; management 12.00%, building and grounds 16.08%, personal care and service 13.78%, office and administrative support 19.34%, and installation, maintenance and repair 16.14%, with detailed desk clerk, customer service, reservation, bookkeeping, grounds, housekeeping, recreation, and repair occupations.
- **S2** — [GPTs are GPTs: An early look at the labor market impact potential of large language models](https://openai.com/index/gpts-are-gpts/) (accessed 2026-07-22): Broad occupational task-exposure context: about 80% of the U.S. workforce could have at least 10% of tasks affected and about 19% could have at least 50% affected; used only as context, not as a direct campground estimate.
- **S3** — [Large Firms With At Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Census BTOS evidence that U.S. business AI use was 17% to 20% from December 2025 to May 2026, expected use was 20% to 23%, and fewer than 20% of firms with four or fewer employees reported use.
- **S4** — [Increase Campground Revenue](https://software.campspot.com/features/growth-and-revenue/) (accessed 2026-07-22): Direct evidence that campground software automates dynamic pricing, site-grid optimization, reservation add-ons, and marketplace booking; Campspot states more than 3,500 U.S. and Canadian campgrounds use it and reports specific 2025 network revenue effects, subject to vendor-selection caveats.
- **S5** — [Anthropic Economic Index report: Learning curves](https://www.anthropic.com/research/economic-index-march-2026-report) (accessed 2026-07-22): Observed Claude usage across occupations and workflows: 49% of jobs had at least one-quarter of tasks represented in Claude use, and customer-service tasks such as payment and billing support showed high exposure in automated API workflows.
- **S6** — [North American Industry Classification System, United States, 2022](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Official definition of NAICS 721211 as operating sites for campers and equipment with facilities including washrooms, laundry, recreation halls, playgrounds, stores, and snack bars; excludes facilities without accommodations and residential mobile-home-site lessors.
- **S7** — [RV & MHP Investment Report 2025](https://www.leisurepropertiesgroup.com/wp-content/uploads/2025/03/RV-MHP-Investment-Report-2025-Final.pdf) (accessed 2026-07-22): Broker evidence of fragmented private ownership, a 2024 shift toward $1 million to $10 million mid-market deals, active private-equity and mid-market buyers, value-add acquisitions, seller financing, and zoning and capital barriers to new supply.
- **S8** — [WACO News July 2025: Preparing Your Campground to Carry On](https://www.wisconsincampgrounds.com/wp-content/uploads/2025/08/7.-July-Newsletter.pdf) (accessed 2026-07-22): Industry succession guidance describing owner residence, generational family ownership, emotional ties, blurred personal and business property, and campground value concentrated in land rather than ready cash.
- **S9** — [2025 Camping & Outdoor Hospitality Report press release](https://www.koapressroom.com/press/2025-camping-outdoor-hospitality-report/) (accessed 2026-07-22): KOA survey evidence: over 11 million more households camped in 2024 than in 2019, camping was slightly down year over year, 65% planned the same or more travel spending, and the study used 2,912 U.S. plus 1,207 Canadian household responses.
- **S10** — [2026 Camping Report: Executive Summary](https://oia.outdoorindustry.org/l/51282/2026-02-23/f4j3xz) (accessed 2026-07-22): Outdoor Industry Association evidence that 42.3 million Americans camped near vehicles in 2025, up more than 5% in one year and 6.2 million since 2020, while RV camping fell 6.4% year over year and returned to pre-pandemic levels.
