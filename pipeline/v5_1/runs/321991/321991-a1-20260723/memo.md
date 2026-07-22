# 321991 — Manufactured Home (Mobile Home) Manufacturing

*v5.1 Stage 1 research memo. Run `321991-a1-20260723`, model `claude-sonnet-5`, 2026-07-23, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.52 · L 0.72 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent need for lower-cost housing combined with improvable planning, quoting, and compliance workflows.
**Weakness:** Very few product manufacturers clearly satisfy the recurring outsourced-service lens, and core labor is physical rather than software-substitutable.

## Business-model lens
- Included: US lower-middle-market manufactured-home producers only where repeat dealer, developer, community-owner, or institutional orders create an ongoing outsourced production relationship.
- Excluded: One-off direct-to-consumer product sales, retailers, installers, transporters, captive plants, shells, and firms outside the EBITDA band.
- Customer and revenue model: Homes are sold per unit or project, generally through dealer and developer channels; recurring revenue arises only where customers repeatedly outsource production under an ongoing supplier relationship.
- Deviation from default lens: The code is product manufacturing rather than a recurring service. For coherence, the lens retains only manufacturers with repeat outsourced-production relationships and excludes one-off unit sellers.

## Executive view
The industry offers a modest, operationally useful AI opportunity in planning and administration, but the frozen recurring-service lens fits only a small minority of manufacturers. The core output remains a regulated physical home, making AI primarily an efficiency layer rather than a substitute for the operator.

## How AI changes the work
Near-term gains are most plausible in quoting, drafting assistance, procurement, scheduling, work instructions, quality-document review, warranty triage, and dealer support. Assembly, material handling, skilled trades, inspection, and final accountability remain human- and equipment-intensive.

## Value capture
Unit and project pricing permits early retention of lower overhead and fewer coordination errors, but sophisticated repeat buyers can obtain savings through bids and repricing. Product differentiation, lead-time reliability, and compliance performance determine how much benefit survives competition.

## Firm availability
Only firms with genuine repeat outsourced-production relationships qualify; most transactional home sellers do not. General small-business succession and observed manufacturing sales support some transfer probability, but niche-specific LMM deal evidence is thin.

## Demand durability
Affordable-housing need supports the category, while rates, chattel financing, land and zoning constraints, dealer inventories, and housing cycles create substantial volume risk. Nearly all surviving demand still requires a certified physical manufacturer.

## Risks and uncertainty
The largest uncertainties are lens eligibility, customer concentration, cyclical demand, financing access, regulatory error costs, and whether public transaction samples represent EBITDA-band plants. AI gains could also be smaller than expected because much labor is embodied and plant-specific.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2786 | — | OBSERVED | — |
| n | — | 63 | — | ESTIMATE | — |
| a | 0.07 | 0.13 | 0.22 | PROXY | S1, S2, S3 |
| rho | 0.3 | 0.5 | 0.7 | ESTIMATE | S2, S3 |
| e | 0.05 | 0.12 | 0.25 | ESTIMATE | S4 |
| s5 | 0.1 | 0.18 | 0.3 | PROXY | S5, S6 |
| q | 0.35 | 0.55 | 0.75 | ESTIMATE | S1, S2 |
| d5 | 0.85 | 1.03 | 1.22 | PROXY | S1, S4 |
| o | 0.9 | 0.97 | 1 | PROXY | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.23 | 0.72 | 1.72 | ESTIMATE |
| F | 0.44 | 1.38 | 2.81 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.65 | 9.99 | 10.00 | PROXY |

## Caveats
- a: Occupation evidence is broad production-work evidence rather than a direct task-exposure measure for 321991.
- a: The frozen compensation ratio uses 2024 wages over 2022 receipts and is harmonized by a cross-code median divisor.
- rho: No representative five-year adoption study was found for manufactured-home plants.
- rho: The estimate excludes standalone robotics unless AI directly enables the exposed task opportunity.
- e: The 63-firm count is a margin-bridged estimate, not an observed list of qualifying manufacturers.
- e: Repeat orders do not automatically constitute recurring outsourced service, making the eligibility boundary judgment-sensitive.
- s5: Gallup covers employer businesses across industries and sizes.
- s5: BizBuySell is a broker-marketplace sample and its manufacturing transactions are generally below the stated EBITDA band.
- q: No public contract sample was found for qualifying private firms.
- q: The lens covers only repeat relationships, which may have stronger buyer bargaining power than one-off retail sales.
- d5: Shipment counts are not adjusted for quality or configuration mix.
- d5: The current series is national and does not isolate repeat outsourced-production customers.
- o: Operator requirement is inferred from current regulation over a five-year horizon.
- o: The estimate allows limited self-supply or vertical integration but not elimination of physical production.

## Sources
- **S1** — [About the Manufactured Housing Survey](https://www.census.gov/programs-surveys/mhs/about.html) (accessed 2026-07-23): Defines MHS coverage as all new federally inspected HUD-code homes and documents monthly shipment, price, status, and characteristics data; supports demand-proxy scope and product-channel context.
- **S2** — [Manufactured Housing Homeowner Resources](https://www.hud.gov/hud-partners/manufactured-home-resources) (accessed 2026-07-23): Documents controlled-environment plant construction, certification labels, approved quality-control programs, staged inspections, and manufacturer obligations for defects.
- **S3** — [HUD Programs: Manufactured Home Construction and Safety Standards](https://www.hud.gov/hudprograms/) (accessed 2026-07-23): Describes federal design, construction, performance, installation, factory inspection, records, labeling, and corrective-action requirements.
- **S4** — [Total Shipments of New Manufactured Homes: Total Homes in the United States](https://fred.stlouisfed.org/series/SHTSAUS/) (accessed 2026-07-23): Reports the Census MHS seasonally adjusted shipment series, including 101 thousand in April 2026 and high-90s to low-100s thousand readings in preceding months, anchoring current unit demand.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Reports a fall-2024 survey of employer-business owners' five-year plans, including ownership-transfer intentions and higher transfer planning among owners age 55 or older.
- **S6** — [BizBuySell Insight Report Data Tables](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-23): Reports 2025 broker-marketplace transaction metrics by sector, including 83 reported sales for other manufacturing businesses, providing a broad realized-deal-flow proxy.
