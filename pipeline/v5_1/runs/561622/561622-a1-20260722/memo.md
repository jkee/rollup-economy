# 561622 — Locksmiths

*v5.1 Stage 1 research memo. Run `561622-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.53 · L 1.41 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can remove avoidable coordination and office work while electronic access expands higher-value installation and service needs that still require a trusted local operator.
**Weakness:** Only 10 LMM firms are modeled, and the core trade is physically intensive, owner-dependent, and often break-fix rather than contractually recurring.

## Business-model lens
- Included: Lower-middle-market locksmith firms supplying repeat or recurring installation, repair, rekeying, emergency opening, master-key, safe, door-hardware, and electronic-access services to external residential, commercial, institutional, and automotive customers, with associated locking-device sales where service remains integral.
- Excluded: Pure lock or safe retail and wholesale without installation or maintenance, stand-alone key duplication, security-alarm monitoring businesses classified elsewhere, captive facilities staff, shells, and non-control financing vehicles.
- Customer and revenue model: Customers buy emergency and scheduled service calls, labor, travel, parts and hardware, project installation, and sometimes maintenance, software, monitoring, or access-control subscriptions. Pricing commonly combines a service or trip fee with hourly, per-unit, materials, or quoted-project charges; recurring contracts are emerging but are not yet the dominant model.
- Deviation from default lens: none

## Executive view
Locksmithing remains a physical, local security trade, so AI mainly changes the work around the wrench rather than the core installation or repair. Intake, dispatch, quoting, records, invoicing, follow-up, and technical retrieval can improve, while drilling, cutting, fitting, opening, site assessment, and secure handoff remain human. The modeled LMM universe is very small and unverified, and much of the industry still relies on break-fix revenue and owner expertise.

## How AI changes the work
AI can answer and qualify calls, identify urgency and location, schedule and route technicians, draft estimates, retrieve product and code information, summarize job notes, prepare invoices, follow up on quotes, maintain customer records, and assist with access-control configuration. A locksmith still must authenticate the customer, inspect the opening, select safe hardware, manipulate or drill locks, install and test devices, protect key and credential data, and accept responsibility for security-sensitive work.

## Value capture
Fixed service calls, trip fees, per-unit work, hardware margin, and quoted projects let operators retain some back-office and capacity gains. Hourly labor, competitive bids, shorter billed time, software subscriptions, electronic-access license costs, and faster competitor response share the benefit. Recurring service and access-control contracts improve capture where present, but trade evidence says they remain new or limited for many firms.

## Firm availability
The NAICS definition is naturally service-oriented, and commercial accounts, technicians, equipment, routes, and access-control relationships can transfer. A disclosed U.S. acquirer is buying lock-and-door businesses, but the frozen dataset identifies only 10 modeled LMM firms. Owner dependence, licensing, customer trust, sparse contracts, mixed product sales, and weak documentation can shrink the truly eligible set further.

## Demand durability
Traditional locksmith employment is projected to decline, but physical security, emergency access, aging door hardware, commercial retrofits, and connected access systems continue to require service. Electronic access is becoming central to many surveyed locksmiths and can create project, configuration, update, and support work. Direct-to-consumer devices, self-service, and adjacent security integrators create a meaningful downside.

## Risks and uncertainty
The main uncertainties are the unverified target count, the occupation mix, current administrative hours, owner dependence, actual AI adoption, revenue-weighted billing models, and code-specific real demand. Operational risks include bad AI quotes or dispatch, exposure of key and credential records, fraudulent lockout requests, installer licensing, technician scarcity, smart-device cybersecurity, product-vendor dependence, and acquisitions that lose the trusted owner or skilled technicians.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4078 | — | OBSERVED | — |
| n | — | 10 | — | ESTIMATE | — |
| a | 0.14 | 0.24 | 0.34 | PROXY | S2, S4 |
| rho | 0.38 | 0.58 | 0.75 | PROXY | S4 |
| e | 0.58 | 0.78 | 0.9 | ESTIMATE | S1, S9 |
| s5 | 0.09 | 0.18 | 0.29 | PROXY | S6, S7, S9 |
| q | 0.35 | 0.56 | 0.72 | PROXY | S5, S9 |
| d5 | 0.82 | 0.96 | 1.1 | PROXY | S3, S8 |
| o | 0.75 | 0.88 | 0.95 | PROXY | S1, S2, S8, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.87 | 2.27 | 4.16 | PROXY |
| F | 0.68 | 1.41 | 2.06 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | PROXY |
| D | 6.15 | 8.45 | 10.00 | PROXY |

## Caveats
- a: O*NET importance scores describe an occupation, not wage shares or time shares inside NAICS 561622.
- a: The home-services AI survey is vendor-sponsored and is concentrated in HVAC, plumbing, electrical, and general contracting rather than locksmithing.
- a: The frozen compensation ratio combines 2024 wages with 2022 receipts and an IPS harmonization factor.
- a: Electronic-access work mixes physical installation, software configuration, cybersecurity, and customer training in proportions not measured here.
- rho: The survey is an online sample of active platform customers and industry contacts and is explicitly directional.
- rho: Reported use of AI is not the share of exposed work implemented or a verified labor saving.
- rho: Small owner-operated locksmith shops may lack standardized data and workflows needed for reliable automation.
- e: The frozen count of 10 LMM-band firms is margin-bridged using a broad services margin and is not a verified target list.
- e: The NAICS code permits device and safe sales when combined with service, so product intensity can vary materially.
- e: Industry commentary indicates that many firms remain break-fix businesses with limited recurring monthly revenue.
- s5: Gallup is cross-industry and its transfer category includes outcomes that do not qualify as outside control sales.
- s5: One consolidator announcement establishes buyer activity but not an industry transaction rate.
- s5: Owner-held technical knowledge, customer trust, and licenses can make an intended sale nontransferable.
- q: The pricing survey is non-scientific and does not report revenue-weighted billing shares.
- q: Electronic-access work often uses hourly and trip fees, which can pass labor savings to customers through fewer billable hours.
- q: Recurring revenue is described as new and limited for many locksmiths rather than an established industry-wide model.
- d5: Occupational employment is not service quantity and includes locksmiths working outside NAICS 561622.
- d5: The electronic-access survey is a subscriber sample and does not measure constant-price industry demand.
- d5: Direct-to-consumer smart locks can create installation and support work but also displace traditional service calls.
- o: Operator need differs sharply between consumer smart locks, automotive work, commercial master-key systems, electronic access, and safes.
- o: Electronic access shifts work toward software and integration without necessarily keeping it inside NAICS 561622.
- o: O*NET describes today's occupation and cannot resolve five-year self-service adoption.

## Sources
- **S1** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): The official definition covers sales of mechanical or electronic locks, safes, and vaults with service, plus installation, repair, rebuilding, and adjustment of those products.
- **S2** — [O*NET OnLine: Locksmiths and Safe Repairers](https://www.onetonline.org/link/details/49-9094.00) (accessed 2026-07-22): The 2026 occupation profile documents physical key cutting, lock manipulation, drilling, door-hardware and access-system installation, safe repair, vehicle opening, and lock-and-key recordkeeping tasks.
- **S3** — [BLS Occupational Projections and Worker Characteristics, 2024-2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): BLS projects national locksmith and safe repairer employment from 18,800 in 2024 to 17,200 in 2034, a decline of 8.3 percent, while projecting 1,700 annual openings.
- **S4** — [AI in Field Service Management: How Early Adopters Win](https://www.housecallpro.com/resources/ai-in-the-trades/) (accessed 2026-07-22): A spring 2026 survey of 248 U.S. home-service professionals reports 48 percent active AI use, leading uses in customer communication, estimates, and reporting, and 84 percent of users expecting to increase use.
- **S5** — [2024 National Average Price Survey](https://www.locksmithledger.com/home/article/55137701/2024-national-average-price-survey) (accessed 2026-07-22): The trade survey describes combinations of service, trip, hourly, fixed-service, per-unit, project, and materials pricing and reports average regular-hour service-call and labor charges.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Gallup reports that 22 percent of U.S. employer-business owners planned to sell or transfer ownership within five years, versus 9 percent of nonemployers.
- **S7** — [Cobalt Acquires Acme Lock & Door](https://www.cobaltsp.com/news-insights/cobalt-acquires-acme-lock-and-door) (accessed 2026-07-22): Cobalt announced its May 2025 acquisition of a U.S. lock-and-door company as its fourteenth acquisition since December 2023 and third acquisition of 2025.
- **S8** — [Best of 2025: Electronic Access Control](https://www.locksmithledger.com/electronics-access-control/article/55326129/best-of-2025-electronic-access-control) (accessed 2026-07-22): The 2025 trade survey reports that 85 percent of locksmith respondents saw electronic access control as a major driver or complement and 40 percent expected to implement more in the following year.
- **S9** — [State of the Industry 2025](https://www.locksmithledger.com/electronics-access-control/article/55265615/state-of-the-industry-2025) (accessed 2026-07-22): Industry participants describe most locksmiths as starting with break-fix service, recurring revenue emerging through projects and access control, one operator at 14 percent recurring revenue, contract scarcity, and installation expertise as essential.
