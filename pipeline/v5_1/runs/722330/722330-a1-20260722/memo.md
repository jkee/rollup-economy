# 722330 — Mobile Food Services

*v5.1 Stage 1 research memo. Run `722330-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.47 · L 1.00 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat consumer demand plus standardized digital ordering and back-office workflows can support measurable administrative and coordination efficiency across a multi-unit mobile fleet.
**Weakness:** Most work is physical and the estimated LMM universe contains only seven firms, with no direct evidence on which are eligible or likely to transfer.

## Business-model lens
- Included: Independent mobile food-service firms in the roughly $1-10M normalized-EBITDA band that operate transferable trucks, carts, mobile canteens, or mobile concession fleets and repeatedly serve consumers, workplaces, venues, or other external customers through recurring routes, regular locations, or repeat bookings.
- Excluded: Founder-only or otherwise nontransferable operations, one-off pop-ups without repeat demand, captive units, shells, non-control financing vehicles, nonmobile restaurants, single-event caterers classified in 722320, and long-term fixed-site food-service contractors classified in 722310.
- Customer and revenue model: Primarily menu-priced sales of prepared food and nonalcoholic beverages for immediate consumption, paid by consumers at or before service; eligible firms may also receive contracted or scheduled revenue from workplaces, venues, institutions, and repeat event customers.
- Deviation from default lens: none

## Executive view
Mobile food services remain a hands-on operating business. AI can improve ordering, scheduling, purchasing, inventory, marketing, bookkeeping, and management decisions, but most payroll supports cooking, serving, cleaning, supervision, and mobility. The opportunity therefore depends on disciplined fleet operations and avoidable administrative hiring more than replacement of frontline crews. Demand has supportive food-away-from-home tailwinds, while the transferable LMM universe is exceptionally small and poorly observed.

## How AI changes the work
The near-term workflow is a connected operating stack: POS and digital ordering feed demand forecasts, purchasing suggestions, prep plans, route and event scheduling, labor rosters, customer messaging, bookkeeping, and exception alerts. Generative systems can draft promotions, answer booking inquiries, reconcile documents, and summarize unit performance. Human staff remain central to safe preparation, quality judgment, service recovery, driving, setup, cleaning, and supervision; restaurant operators themselves predominantly expect technology to augment rather than replace labor.

## Value capture
Menu-priced consumer transactions provide no automatic contractual pass-through, so an operator can retain early efficiency gains or redeploy them into service, availability, and margin resilience. Retention erodes as competitors adopt similar tools, customers respond to promotions and prices, and venues or repeat corporate customers negotiate renewals. The best evidence would be unit-level margin and pricing cohorts after deployment, which public sources do not provide.

## Firm availability
The frozen dataset estimates only seven firms in the EBITDA band, and no public list identifies them. Larger multi-truck fleets should be more transferable and more likely to have recurring routes, venues, and repeat bookings than typical owner-operated trucks, but founder identity, recipes, local permits, commissary access, or venue relationships may still be inseparable from ownership. Restaurant sale marketplaces demonstrate transaction activity only in a much smaller earnings population and cannot establish the qualifying five-year rate.

## Demand durability
Prepared food away from home has a long real-growth history, and BLS expects continued demand associated with dining out, takeout, and delivery. Mobile operators also offer convenience and flexible placement. Against that, demand is discretionary, locally competitive, weather- and event-sensitive, and exposed to permitting or site restrictions. Most surviving quantity should still require an accountable operator because the core basket entails physical food preparation, service, sanitation, equipment, and mobile assets.

## Risks and uncertainty
The principal evidence gap is granularity: occupation data cover parent NAICS 722300, technology surveys cover restaurants broadly, transfer data cover self-selected small restaurant sales, and demand data cover all food away from home. Self-employment is missing from OEWS. The seven-firm LMM estimate is margin-bridged and highly sensitive to classification. A poor outcome would combine founder-dependent targets, nontransferable permits or venue rights, weak recurring demand, low workflow standardization, and savings competed away through local menu pricing.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.312 | — | OBSERVED | — |
| n | — | 7 | — | ESTIMATE | — |
| a | 0.1 | 0.16 | 0.24 | PROXY | S2, S3 |
| rho | 0.3 | 0.5 | 0.68 | PROXY | S3, S7 |
| e | 0.6 | 0.72 | 0.85 | ESTIMATE | S1 |
| s5 | 0.1 | 0.22 | 0.36 | ESTIMATE | S6 |
| q | 0.38 | 0.58 | 0.74 | ESTIMATE | S1, S3 |
| d5 | 0.94 | 1.04 | 1.13 | PROXY | S4, S5 |
| o | 0.84 | 0.93 | 0.98 | PROXY | S1, S2, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.37 | 1.00 | 2.04 | PROXY |
| F | 0.56 | 1.20 | 1.84 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.90 | 9.67 | 10.00 | PROXY |

## Caveats
- a: OEWS does not publish a six-digit 722330 occupation table and excludes self-employed workers, important in mobile food.
- a: Task exposure fractions are analyst judgment rather than a measured AI-exposure index.
- a: The frozen compensation-to-receipts input uses 2024 wages over 2022 receipts and is harmonized to the IPS basis, creating a stated vintage and basis mismatch.
- rho: Survey respondents are restaurants generally, not NAICS 722330 or the LMM EBITDA band.
- rho: Planned spending is not successful implementation or verified labor avoidance.
- rho: FDA Food Code requirements are a model adopted and modified by jurisdictions, not a single uniform federal operating rule.
- e: No public source measures the share of 722330 LMM firms meeting the recurring-service and transferability lens.
- e: The frozen LMM firm count is itself a margin-bridged estimate from size-class receipts and a restaurant EBITDA margin, so classification near the band is uncertain.
- e: Local permits, commissary arrangements, and venue rights may attach to an owner or location rather than transfer with the company.
- s5: BizBuySell is a self-selected marketplace and does not provide a transfer probability or NAICS 722330 breakout.
- s5: Its sold restaurants had median owner earnings of $120,355 over 2021-2025, far below the screen's EBITDA band.
- s5: The tiny dataset-estimated LMM population means one actual transfer would move the realized share sharply.
- q: No source directly observes pass-through of AI-enabled savings in mobile food services.
- q: Consumer retail sales and negotiated venue or workplace agreements have different pass-through dynamics.
- q: The estimate excludes demand volume effects, which belong in d5 and o, and implementation friction, which belongs in rho.
- d5: Food-away-from-home spending includes restaurants, institutions, vending, and other outlets beyond mobile food.
- d5: Employment growth mixes demand and labor-productivity effects and covers occupations across industries.
- d5: The USDA long history does not isolate the current five-year cycle or constant-quality meals.
- o: The accountable-operator construct is inferred from physical workflow and model regulation, not directly surveyed.
- o: FDA's Food Code is guidance for jurisdictional adoption and includes exceptions for establishments deemed minimal risk.
- o: The BLS occupation mix is for NAICS 722300 and excludes self-employed workers.

## Sources
- **S1** — [North American Industry Classification System: Sector 72, including 722330 Mobile Food Services](https://www.census.gov/naics/resources/archives/sect72.html) (accessed 2026-07-22): Defines 722330 as establishments preparing and serving meals and snacks for immediate consumption from motorized vehicles or nonmotorized carts, with examples including mobile canteens, food carts, and concession stands; supports the lens, revenue-model inference, eligibility estimate, and physical-service nature.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 722300 Special Food Services](https://www.bls.gov/oes/2023/may/naics4_722300.htm) (accessed 2026-07-22): Reports 720,600 total parent-industry jobs and detailed employment and wages, including food preparation and serving at 73.32% of employment, management at 4.67%, sales at 4.48%, office support at 3.35%, and transportation and material moving at 3.70%; supports occupation-based AI exposure and operator-required workflow proxies.
- **S3** — [Restaurant Technology Landscape Report 2024](https://go.restaurant.org/rs/078-ZLA-461/images/NatRestAssoc_TechLandscapeReport_2024.pdf) (accessed 2026-07-22): Restaurant operator and consumer survey reporting 2024 investment plans including 52% back office, 52% inventory, 37% automated labor management, 25% self-ordering, 16% AI, and 3% limited-service robotics; also reports 69% expect augmentation rather than labor replacement and 61% of adults are favorable toward variable pricing.
- **S4** — [Total U.S. food spending reached $2.51 trillion in 2025](https://www.ers.usda.gov/data-products/charts-of-note/114212) (accessed 2026-07-22): Reports inflation-adjusted food-away-from-home spending of $1.41 trillion in 2025 versus $818 billion in 1997 and a 56.3% share of total food expenditures in 2025; supports the broad real-demand proxy.
- **S5** — [Occupational Outlook Handbook: Food and Beverage Serving and Related Workers](https://www.bls.gov/ooh/food-preparation-and-serving/food-and-beverage-serving-and-related-workers.htm) (accessed 2026-07-22): Projects 5% employment growth from 2024 to 2034 and attributes continued need to dining out, takeout, delivery, and essential food-serving operations; supports the five-year demand proxy.
- **S6** — [Restaurant Business Valuation Multiples and Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/restaurants/) (accessed 2026-07-22): Reports 8,692 sold restaurant listings analyzed over 2021-2025 and median sold-business owner earnings of $120,355; demonstrates active but much smaller restaurant transactions and anchors the transfer estimate's caveat.
- **S7** — [FDA Food Code 2022, Print Version](https://www.fda.gov/media/184685/download) (accessed 2026-07-22): The model code generally requires the permit holder or designated person in charge to be present during all operating hours, with a minimal-risk exception, and assigns food-safety duties; supports implementation constraints and continued accountable-operator need.
