# 561790 — Other Services to Buildings and Dwellings

*v5.1 Stage 1 research memo. Run `561790-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.22 · L 1.56 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical maintenance needs and fixed monthly or quoted pricing create a modest, retainable opportunity to automate coordination around field work.
**Weakness:** Most labor is inseparable from on-site physical execution, while the broad service mix makes the estimated acquisition pool and average economics unusually uncertain.

## Business-model lens
- Included: US lower-middle-market firms repeatedly providing outsourced physical services to buildings and dwellings, including swimming-pool cleaning and maintenance, chimney cleaning and inspection, ventilation-duct cleaning, drain or gutter cleaning, pressure washing and other building-exterior cleaning, commercial kitchen exhaust cleaning, parking-lot cleaning, lighting maintenance, and stand-alone driveway or parking-lot snow removal.
- Excluded: Captive facilities staff; pest control, janitorial, landscaping, carpet cleaning, construction, licensed-trade installation, or remediation businesses properly classified elsewhere; software-only monitoring; one-person practices without a transferable operating organization; shells; and non-control financing vehicles.
- Customer and revenue model: External homeowners, property managers, associations, businesses, institutions, and public facilities buy weekly or monthly routes, seasonal programs, annual inspections, periodic maintenance, and one-time cleaning or corrective projects. Billing may be flat monthly, per visit, per asset, hourly, or fixed by quoted scope, with chemical and repair materials either bundled or separately charged.
- Deviation from default lens: none

## Executive view
Other services to buildings and dwellings is a heterogeneous collection of recurring or repeat physical property services. AI can improve intake, scheduling, routing support, estimation, documentation, marketing, and customer communication, but most payroll remains tied to travel, inspection, cleaning, testing, equipment operation, and maintenance at customer sites. Pool routes offer the clearest recurring model; chimney, duct, gutter, exterior, drain, lot, lighting, and snow services are more periodic, seasonal, or project-based.

## How AI changes the work
Practical applications include automated phone and web intake, lead qualification, route suggestions, appointment reminders, draft estimates from structured observations, work-order summaries, image-assisted documentation, supply alerts, customer education, review responses, and renewal outreach. Human technicians remain responsible for premises access, diagnosis, ladders or confined spaces, chemical handling, testing, powered equipment, repair decisions, safety, and final quality control.

## Value capture
Flat monthly pool billing and fixed quoted scopes can retain some back-office and route efficiency inside the price. Capture is weaker for hourly, per-visit, material-sensitive, or frequently rebid work, and local competitors can adopt the same tools. Operators retain value only when automation reduces paid coordination hours, avoids incremental office hiring, improves route density without hurting service, or supports more completed jobs.

## Firm availability
The supplied LMM population is larger than in some niche building services but remains only 77 estimated firms and spans dissimilar trades. Transferability is strongest where routes, contracts, customer records, technicians, equipment, and supervisors are documented; it is weaker where the owner holds the technical certification, performs key jobs, or embodies local customer trust. Classification and margin assumptions can materially alter the population.

## Demand durability
Pools need frequent testing and preventive care, chimneys and HVAC systems receive periodic inspection or cleaning guidance, older buildings require ongoing maintenance, and weather or recurring contamination renews demand for exteriors, gutters, drains, lots, and snow services. Demand is not uniformly nondiscretionary: homeowners can defer or self-perform many tasks, snow is volatile, and commercial customers may bundle work into broader facilities contracts.

## Risks and uncertainty
There is no public service-line revenue mix, six-digit occupation mix, AI deployment study, contract mix, transfer series, or constant-price demand series for this code. Major risks include technician safety, chemical and property damage, certification dependence, route density, vehicle and equipment utilization, seasonality, weather, lead-source costs, customer churn, local competition, and founder dependence. The broad classification means an average can conceal materially different economics between pool routes and project or inspection businesses.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.45 | — | OBSERVED | — |
| n | — | 77 | — | ESTIMATE | — |
| a | 0.09 | 0.18 | 0.29 | PROXY | S1, S2, S3 |
| rho | 0.28 | 0.48 | 0.67 | PROXY | S3, S4 |
| e | 0.65 | 0.81 | 0.91 | ESTIMATE | S1, S6, S7, S8, S9 |
| s5 | 0.08 | 0.16 | 0.27 | PROXY | S5 |
| q | 0.36 | 0.58 | 0.76 | PROXY | S2, S3, S6 |
| d5 | 0.93 | 1.04 | 1.16 | PROXY | S1, S2, S7, S8, S9 |
| o | 0.8 | 0.91 | 0.97 | PROXY | S1, S2, S7, S8, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.45 | 1.56 | 3.50 | PROXY |
| F | 2.59 | 3.85 | 4.81 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | PROXY |
| D | 7.44 | 9.46 | 10.00 | PROXY |

## Caveats
- a: No public six-digit occupation mix or wage-weighted task study exists for this heterogeneous industry.
- a: The broad maintenance occupation does not capture the exact mix of pool, chimney, duct, drain, gutter, exterior-cleaning, and snow services.
- a: The supplied compensation ratio combines 2024 wages with 2022 receipts.
- rho: General SME adoption does not measure labor implementation in property-service firms.
- rho: Marketing or message generation may increase activity without reducing labor requirements.
- rho: Service-line differences in route density, recordkeeping, seasonality, and safety create wide implementation variance.
- e: No source measures lens eligibility within the frozen EBITDA band.
- e: Annual or multi-year recommended maintenance is repeatable but not necessarily contractually recurring.
- e: The estimated firm count may mix materially different service lines and margin structures.
- s5: Gallup covers all employer businesses rather than this industry or EBITDA band.
- s5: Owner intentions are not completed transactions and include potentially nonqualifying transfers.
- s5: Transferability likely differs sharply between dense pool routes and owner-expert inspection or project businesses.
- q: No public source reports the national revenue-weighted pricing mix for NAICS 561790.
- q: The direct billing evidence covers pool service and may not generalize to project-oriented subsegments.
- q: Efficiency has no retained value unless paid hours fall, hiring is avoided, or released capacity can be sold.
- d5: Occupational employment is not industry service quantity and includes work outside NAICS 561790.
- d5: Maintenance recommendations do not prove customers purchase the recommended service or outsource it.
- d5: The broad code combines weekly routes, annual or multi-year inspections, discretionary cleaning, emergencies, and weather-dependent services.
- o: No source directly measures operator-required quantity for the combined industry.
- o: Residential customers can self-clean pools, gutters, drains, and exteriors despite safety or quality tradeoffs.
- o: Robotic pool cleaners, remote monitoring, and bundled facility services may erode specialist demand unevenly.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: 561790 Other Services to Buildings and Dwellings](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines the industry and lists building-exterior cleaning, swimming-pool cleaning and maintenance, chimney cleaning, ventilation-duct cleaning, and drain or gutter cleaning as illustrative examples.
- **S2** — [General Maintenance and Repair Workers](https://www.bls.gov/ooh/Installation-Maintenance-and-Repair/General-maintenance-and-repair-workers.htm) (accessed 2026-07-22): Describes physical inspection, diagnosis, preventive maintenance, estimating, recordkeeping, tool use, varied-site work, and projects 4 percent employment growth from 2024 to 2034 with continuing need at older properties.
- **S3** — [AI for Small Business](https://www.sba.gov/business-guide/manage-your-business/ai-small-business) (accessed 2026-07-22): Identifies repeat administration, data analysis, content, customer service, phone routing, and review responses as small-business AI uses while recommending small starts, human review, and data safeguards.
- **S4** — [AI Adoption by Small and Medium-Sized Enterprises](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/ai-adoption-by-small-and-medium-sized-enterprises_9c48eae6/426399c1-en.pdf) (accessed 2026-07-22): Reports lower adoption among SMEs, 11.9 percent use among 10-49 employee firms in 2024, below-10-percent core-business adoption in G7 countries, and mostly peripheral generative-AI use among SMEs.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of US employer-business owners planned to sell, transfer, or go public within five years and 5 percent planned to close.
- **S6** — [Monthly vs Per-Visit Billing for Pool Service](https://pooldial.com/resources/articles/guides/pool-service-billing-frequency) (accessed 2026-07-22): Describes flat monthly billing as standard for weekly pool service, autopay and recurring revenue, and per-visit billing for one-time repairs, cleanups, openings, and closings.
- **S7** — [Operating and Managing Public Pools, Hot Tubs and Splash Pads](https://www.cdc.gov/healthy-swimming/toolkit/operating-public-pools-hot-tubs-and-splash-pads.html) (accessed 2026-07-22): Calls for trained pool operation, at-least-twice-daily water testing, cleaning, records, filtration maintenance, shock treatment, and preventive equipment maintenance.
- **S8** — [Chimney Safety Institute of America Homeowner Resources](https://www.csia.org/homeowner-resources) (accessed 2026-07-22): Cites NFPA 211 guidance that chimneys, fireplaces, and vents be inspected at least annually and describes complete chimney sweeping and Level 1 inspection.
- **S9** — [Prepare HVAC Systems for Fall Season](https://nadca.com/blog/prepare-hvac-systems-fall-season) (accessed 2026-07-22): Recommends annual HVAC-system inspection, complete cleaning historically every four to five years subject to conditions, and defines complete system cleaning under NADCA's ACR standard.
