# 459930 — Manufactured (Mobile) Home Dealers

*v5.1 Stage 1 research memo. Run `459930-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Document-heavy financing and permitting workflows create implementable labor savings against a durable need for affordable housing and complex placement coordination.
**Weakness:** Most NAICS establishments are one-time durable-goods retailers, and manufacturers can absorb the service layer through captive retail and direct channels.

## Business-model lens
- Included: US lower-middle-market manufactured-home dealers that repeatedly serve community operators, developers, government or institutional buyers, or provide repeat outsourced coordination of home selection, permitting, financing, transport, installation, site preparation and post-sale service to external customers.
- Excluded: Pure one-time consumer product retail, manufacturer captive outlets without a transferable external service operation, parts-only stores, manufacturers, community ownership, construction contractors outside the dealer, shells and non-control financing vehicles.
- Customer and revenue model: Repeat B2B home sales and dealer-coordination services for community operators and developers, plus service-rich retail transactions where dealer margin and ancillary fees compensate selection, financing, permitting, delivery, installation and site coordination.
- Deviation from default lens: The NAICS code is primarily durable-goods retail and therefore mixes one-time consumer sellers with repeat outsourced dealer-coordinators. The lens is narrowed to repeat B2B and service-rich dealer operations so the screened population satisfies the recurring or repeat outsourced-service requirement.

## Executive view
Service-rich manufactured-home dealers have a useful AI surface in sales, finance, permitting and coordination, but the industry code is fundamentally product retail and only a minority fits the repeat outsourced-service lens. Affordable-housing need supports demand, while channel integration by manufacturers threatens independent dealer durability.

## How AI changes the work
AI can qualify leads, compare configurations, draft quotes and outreach, collect and check finance documents, prepare permit packets, track orders and schedule handoffs. Human accountability remains central for financial advice, fair-lending review, site assessment, permitting exceptions, negotiation, transport, installation and defect resolution.

## Value capture
Bundled product margins can hide and retain early workflow savings, especially when faster response improves conversion or reduces errors. Savings will leak through manufacturer bargaining, competitive discounts, higher sales compensation and customer affordability pressure as tools diffuse.

## Firm availability
The target is narrower than the NAICS population because one-time home retail is not a recurring outsourced service. Employer-owner transfer intent and recent manufacturer acquisitions indicate a live control market, but the eligible-firm count is missing and strategic buyers may favor scalable multi-location platforms.

## Demand durability
Housing undersupply and the relative affordability of factory-built homes support five-year unit demand. Finance access, interest rates, zoning, land and siting constraints can block that demand, and direct manufacturer or community channels can grow without preserving an independent dealer.

## Risks and uncertainty
The main uncertainties are the unmeasured eligible-firm population, lack of an industry occupation mix, ancestor-level labor ratio, rate and credit sensitivity, local permitting variation, fair-lending and privacy exposure, installation liability, manufacturer concentration and vertical disintermediation.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.27 | 0.39 | 0.52 | ESTIMATE | S2, S3, S4 |
| rho | 0.38 | 0.56 | 0.72 | ESTIMATE | S3, S4 |
| e | 0.08 | 0.2 | 0.34 | ESTIMATE | S1, S4, S5 |
| s5 | 0.11 | 0.18 | 0.25 | PROXY | S5, S8 |
| q | 0.48 | 0.63 | 0.78 | ESTIMATE | S4, S5, S6 |
| d5 | 0.92 | 1.15 | 1.4 | PROXY | S6, S7 |
| o | 0.66 | 0.81 | 0.92 | PROXY | S4, S5, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.42 | 0.89 | 1.52 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 6.07 | 9.31 | 10.00 | PROXY |

## Caveats
- a: O*NET profiles retail sales and lending occupations generally, not a measured occupation mix for manufactured-home dealers.
- a: The estimate excludes work already automated and does not treat regulated approval or physical field coordination as fully substitutable.
- a: The injected labor ratio is measured at ancestor 44-45 with mismatched 2024 wage and 2022 receipt vintages, so it may poorly represent service-rich dealerships.
- rho: No source measures five-year AI implementation in this dealer industry.
- rho: The service-rich firms retained by the lens may be more operationally complex than the average retail outlet.
- e: There is no observed denominator of LMM firms, and the supplied n primitive is explicitly unavailable.
- e: Large integrated manufacturers demonstrate business-model existence but may overstate service breadth relative to independent LMM dealers.
- s5: Gallup is cross-industry, includes gifts, and measures plans rather than completed transfers.
- s5: Champion's transaction is a strategic acquisition of locations and does not measure market-wide transfer frequency.
- q: No cited source observes pass-through of AI-enabled dealer savings.
- q: Retention varies with manufacturer affiliation, local competition, financing conditions and whether installation or site work is separately contracted.
- d5: Shipment counts are product quantities and include channels outside the frozen dealer lens.
- d5: The Urban Institute report is national and directional and predates the latest interest-rate and policy environment.
- o: Public-company descriptions show capabilities, not a representative industry workflow distribution.
- o: An accountable operator may remain necessary while the independent dealer is vertically displaced, which is specifically a loss under this lens.

## Sources
- **S1** — [2022 NAICS Definition: 459930 Manufactured (Mobile) Home Dealers](https://www.census.gov/naics/?details=45993&input=45993&year=2022) (accessed 2026-07-22): Defines the industry as establishments primarily retailing new and/or used manufactured homes, parts and equipment.
- **S2** — [O*NET OnLine: Retail Salespersons](https://www.onetonline.org/link/details/41-2031.00) (accessed 2026-07-22): Lists customer-needs discovery, product recommendation, payment processing, inventory, sales records, contracts, trade-in estimates and arranging delivery, insurance, financing or service contracts among retail-sales tasks.
- **S3** — [O*NET OnLine: Loan Interviewers and Clerks](https://www.onetonline.org/link/details/43-4131.00) (accessed 2026-07-22): Lists 18 tasks including verifying applications, assembling closing documents, recording and submitting applications, maintaining files, checking collateral, preparing legal and government forms, calculating costs and conducting closings.
- **S4** — [Champion Homes 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/90896/000095017025077746/sky-20250329.htm) (accessed 2026-07-22): Reports distribution through independent and company-owned retail, community operators and builder/developers; 72 active sales centers; installation and set-up construction services; trucking; and dealer floor-plan and consumer financing.
- **S5** — [Champion Homes Announces Agreement to Acquire Retail Locations from Homes Direct](https://ir.championhomes.com/press-releases/press-release-details/2026/Champion-Homes-Announces-Definitive-Agreement-to-Acquire-Retail-Locations-from-Homes-Direct/default.aspx) (accessed 2026-07-22): Reports a May 2026 agreement to acquire assets representing 11 western US retail locations and describes Homes Direct support for permitting, financing, home selection and site preparation.
- **S6** — [Manufactured Housing Institute Monthly Economic Report: May 2025](https://www.manufacturedhousing.org/wp-content/uploads/2025/07/MHI-Economic-Report-May-2025.pdf) (accessed 2026-07-22): Reports 9,270 US manufactured-home shipments in May 2025 and 44,927 year-to-date, with 42.5% single-section and 57.5% multi-section in May.
- **S7** — [Urban Institute: The Role of Manufactured Housing in Increasing the Supply of Affordable Housing](https://www.urban.org/research/publication/role-manufactured-housing-increasing-supply-affordable-housing) (accessed 2026-07-22): Finds that housing inventory deficits, unaffordable prices, growing demand for low-price housing, consumer willingness and better affordability support manufactured housing, while financing and zoning improvements are needed.
- **S8** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 survey of 1,264 US owner-operators found 14% overall and 22% of employer-business owners planned to sell or transfer ownership within five years; 8% overall planned to close.
