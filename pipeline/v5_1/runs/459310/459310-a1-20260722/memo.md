# 459310 — Florists

*v5.1 Stage 1 research memo. Run `459310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** High operator-required physical fulfillment combines with a meaningful digital order, sales, administrative, purchasing, and routing layer that AI can streamline.
**Weakness:** The available labor ratio is a low-quality broad-retail ancestor measure, and no defensible LMM firm-count estimate is available.

## Business-model lens
- Included: US lower-middle-market florist firms providing repeat outsourced floral design, procurement, assembly, order management, installation, refresh, and delivery for households, weddings and events, funerals, hotels, restaurants, offices, and other external customers.
- Excluded: Growers and wholesalers, grocery or mass-merchant floral departments, pure order-gathering websites without accountable fulfillment operations, captive floral departments, owner-only designers without a transferable organization, and non-control financing vehicles.
- Customer and revenue model: Customers pay fixed order or event prices for flowers, design, assembly, logistics, installation, and service; revenue ranges from occasion orders and event contracts to formal daily, weekly, or monthly floral-refresh agreements.
- Deviation from default lens: none

## Executive view
Florists fit the repeat outsourced-service lens more naturally than most specialty retailers: they design, assemble, and deliver perishable products for recurring occasions, contracts, and events. AI can improve order, sales, marketing, purchasing, and routing workflows, but most employment is physical design and delivery. Custom service supports moderate benefit retention and operator durability, while the low and broad ancestor labor ratio and missing firm count materially weaken confidence.

## How AI changes the work
The practical AI layer covers order intake, sentiment and style translation, proposal and quote drafting, customer follow-up, marketing, bookkeeping assistance, purchase planning, spoilage forecasting, scheduling, and route optimization. Floral designers may use generated concepts, but still must choose feasible substitutions, condition stems, build arrangements, manage perishability, install events, and resolve quality failures. Implementation should be moderate because common tools are available, but small-firm data and holiday peaks complicate rollout.

## Value capture
Custom events, urgent delivery, emotion, local reputation, and perishability reduce direct price comparability and allow operators to retain more value than commodity retailers. Standard online bouquets, grocery alternatives, direct-to-consumer supply, wire fees, and rebid corporate accounts create pass-through pressure. Capture should therefore be strongest in events, funerals, and recurring commercial displays, and weakest in standardized consumer delivery.

## Firm availability
Most multi-employee florist firms provide an outsourced design-and-delivery service and should be eligible, subject to transferability and the exclusion of pure order gatherers or merchandise-heavy shops. Cross-industry owner succession and industry closures imply possible supply, but founder design reputation and undocumented relationships can turn a legal sale into an operationally weak transfer.

## Demand durability
Weddings, funerals, gifts, hospitality, and workplace displays provide durable underlying occasions. Recent current-dollar output grew and consumer purchase intentions were broadly stable, while BLS expects continued arrangement demand even as floral-designer employment and shop count decline. That pattern is consistent with stable quantity served through fewer, broader operators rather than disappearance of the service.

## Risks and uncertainty
The most important uncertainties are real rather than nominal demand, the prevalence of transferable LMM firms, and actual labor savings during peak periods. Trade-association data mix surveys, projections, and source vintages. OEWS excludes self-employed designers. The frozen compensation ratio is at ancestor 44-45 and likely understates the labor intensity of custom florists; its wage and receipt vintages differ, and the frozen firm-count primitive is missing.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.25 | 0.35 | PROXY | S1, S2 |
| rho | 0.32 | 0.48 | 0.65 | PROXY | S2, S3 |
| e | 0.55 | 0.7 | 0.84 | ESTIMATE | S2, S5 |
| s5 | 0.08 | 0.15 | 0.22 | PROXY | S3, S4, S6 |
| q | 0.39 | 0.55 | 0.7 | ESTIMATE | S6 |
| d5 | 0.93 | 1.02 | 1.12 | PROXY | S2, S5, S6, S7 |
| o | 0.78 | 0.88 | 0.95 | PROXY | S2, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.49 | 0.92 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 7.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.25 | 8.98 | 10.00 | PROXY |

## Caveats
- a: Occupation shares are employment-based, not wage-weighted task shares, and do not identify work already automated.
- a: OEWS excludes self-employed workers and may not reflect owner task bundles.
- a: The frozen labor ratio is only available at ancestor 44-45 and combines 2024 wages with 2022 receipts, so it may be materially misleading for labor-intensive custom florists.
- rho: Retail-wide adoption does not measure florist-specific use or implementation depth.
- rho: Seasonal peaks can create value from avoided temporary hiring but also amplify operational risk.
- rho: Physical production remains outside rho because it is not included in the exposed opportunity.
- e: No source measures the share of firms meeting both the repeat-service and transferability tests.
- e: Occasion orders repeat at the firm level but not necessarily under customer contracts.
- e: The frozen firm-count input is missing, so this share cannot be converted into a defensible number of eligible firms.
- s5: Gallup is cross-industry and plan-based rather than a closed-deal study.
- s5: Worker replacement openings do not directly measure owner succession.
- s5: Founder-led creative reputation may not survive a transfer even when legal control changes.
- q: No public study measures pass-through of AI-enabled florist cost savings.
- q: Trade-association quotations are selective and not a representative estimate of pricing power.
- q: Capture varies materially between custom events and standardized online bouquets.
- d5: Current-dollar output is not a real quantity index and recent growth includes price inflation.
- d5: SAF survey samples and projections may not represent all florists or the LMM lens.
- d5: Holiday and event cycles create substantial annual volatility.
- o: Task descriptions demonstrate physical work but not its share of future demand.
- o: A platform may remove sales and administration while retaining a local florist as physical fulfiller.
- o: Robotics or centralized bouquet production could reduce local operator need beyond the five-year base case.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 459300](https://www.bls.gov/oes/2023/may/naics4_459300.htm) (accessed 2026-07-22): Florist occupation mix: floral designers 45.15%, transportation/material moving 18.98%, sales-related 17.32%, office/administrative support 7.40%, management 5.23%, and business operations 1.00%.
- **S2** — [Occupational Outlook Handbook: Floral Designers](https://www.bls.gov/ooh/arts-and-design/floral-designers.htm) (accessed 2026-07-22): Task and channel evidence: designers buy inputs, consult, design, assemble, condition flowers, take orders, install events, and may provide daily, weekly, or monthly refresh contracts; local shops often fulfill online flower-service orders.
- **S3** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS retail adoption proxy: around 14% of Retail Trade businesses currently used AI and about 17% expected use within six months, below national rates.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): US employer-owner succession proxy: 52.3% of employer businesses were owned by people age 55 or older, and 22% of employer-business owners planned to sell or transfer within five years.
- **S5** — [2022 NAICS 459310: Florists](https://www.census.gov/naics/?details=459310&input=459310&year=2022) (accessed 2026-07-22): Official industry scope: establishments primarily retailing cut flowers, floral arrangements, and potted plants grown elsewhere.
- **S6** — [Society of American Florists: 2024 State of the Industry](https://safnow.org/wp-content/uploads/2024/08/2024_State_of_the_industry.pdf) (accessed 2026-07-22): Industry survey and outlook evidence: retail florist sales and shop projections, July 2024 operating outlook, service and quality differentiation, and an Ipsos poll of 1,005 US adults in which 53% expected the same flower/plant gift-purchase frequency, 26% more, and 21% less over six months.
- **S7** — [Sectoral Output for Retail Trade: Florists in the United States](https://fred.stlouisfed.org/series/IPUHN45311T300000000) (accessed 2026-07-22): BLS/FRED current-dollar sectoral output series: $6.83 billion in 2023, $7.24 billion in 2024, and $7.97 billion in 2025; source notes define the measure as current-dollar output adjusted for inventory and intra-industry shipments.
- **S8** — [Society of American Florists: 2024 Industry Snapshot](https://safnow.org/2024/12/17/2024-industry-snapshot/) (accessed 2026-07-22): Trade-association evidence of closures, consolidations, supply disruption, increased US cut-flower sales, and most surveyed floral businesses reporting sales above 2019 levels.
