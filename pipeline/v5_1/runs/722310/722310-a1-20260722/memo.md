# 722310 — Food Service Contractors

*v5.1 Stage 1 research memo. Run `722310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.50 · L 2.02 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A recurring contracted revenue base paired with automatable planning and administrative workflows around a still-necessary physical service.
**Weakness:** Contractual pass-through and renewal repricing can transfer a substantial share of realized savings to clients.

## Business-model lens
- Included: Independent firms providing recurring contracted food preparation, cafeteria, institutional dining, concession, workplace dining, healthcare dining, education dining, correctional food service, and related on-site food operations for external organizations.
- Excluded: Captive in-house dining units, public-company subsidiaries that are not independently transferable, non-control financing interests, single-event catering, mobile food services, vending-only operations, and firms whose economics depend on nonrecurring events rather than continuing contracts.
- Customer and revenue model: Business, education, healthcare, government, industrial, transportation, and venue customers buy multi-period outsourced food operations under cost-plus, operator-risk, or fixed-price arrangements; consumer sales and client subsidies can coexist within an account.
- Deviation from default lens: none

## Executive view
Food service contracting combines recurring customer relationships with a large labor base, but most frontline work remains physical. The implementable opportunity is concentrated in scheduling, demand forecasting, purchasing, inventory, administration, customer interaction, order capture, and checkout. Account economics differ sharply by contract, so operational savings do not translate uniformly into retained benefit.

## How AI changes the work
AI can improve unit-level labor scheduling, forecast meals, automate purchasing and inventory review, draft menus and communications, support compliance records, answer customer questions, and automate some ordering and payment. It is less able to replace cooking, sanitation, food handling, physical service, and accountable supervision. Current small-employer evidence also suggests that generic AI adoption has rarely produced headcount change, making workflow redesign and system integration more important than tool access.

## Value capture
Cost-plus accounts can return labor savings to the client, while operator-risk and fixed-price accounts initially leave more savings with the contractor. Renewal bids, benchmarking, indexation, and competitive repricing progressively share value. Durable capture therefore depends on proprietary operating routines, superior service, measurable quality, and deployments that strengthen retention rather than merely expose a lower cost base.

## Firm availability
The industry definition itself fits recurring outsourced service and requires contractor-provided management, so many firms in the provided earnings-band count should be in scope. Availability is reduced by corporate subsidiaries, customer concentration, change-of-control consent, owner-held account relationships, and concessions with volatile event economics. General employer-owner intentions imply meaningful but not automatic five-year transfer flow.

## Demand durability
Meals in hospitals, senior living, schools, workplaces, government facilities, corrections, and venues remain physically consumed services. BLS expects modest growth in food-service occupations and identifies institutional prepared meals as a source of demand. Healthcare and senior living can offset weaker workplace attendance or public-budget pressure, but the actual result depends heavily on each contractor's account mix.

## Risks and uncertainty
The main research gaps are six-digit occupation data, target-firm implementation outcomes, completed transaction rates, and contract-level gain sharing. Technology pilots may improve experience without avoiding labor. Food safety failures, labor relations, data governance, client consent, short contract duration, concentration, and aggressive renewal pricing can erase expected value. Large global operator disclosures may not represent independent target firms.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.467 | — | OBSERVED | — |
| n | — | 180 | — | ESTIMATE | — |
| a | 0.17 | 0.27 | 0.38 | PROXY | S2, S3 |
| rho | 0.22 | 0.4 | 0.58 | PROXY | S3, S4 |
| e | 0.58 | 0.76 | 0.88 | ESTIMATE | S1 |
| s5 | 0.08 | 0.15 | 0.24 | PROXY | S6 |
| q | 0.3 | 0.48 | 0.65 | PROXY | S5, S9 |
| d5 | 0.93 | 1.04 | 1.15 | PROXY | S7, S8, S5 |
| o | 0.82 | 0.91 | 0.97 | ESTIMATE | S1, S7, S8, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.70 | 2.02 | 4.12 | PROXY |
| F | 3.60 | 4.94 | 5.89 | ESTIMATE |
| C | 6.00 | 9.60 | 10.00 | PROXY |
| D | 7.63 | 9.46 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational mix is for NAICS 722300, not 722310, and is May 2023 vintage.
- a: Deloitte surveyed 375 global restaurant executives, not US lower-middle-market food service contractors.
- a: Exposure is task-level judgment; it is not the same as implementation or headcount removal.
- rho: Neither survey isolates NAICS 722310 or the specified EBITDA band.
- rho: Reported AI use includes assistive tools with no labor substitution.
- rho: Large operators may implement faster than independent target firms, while packaged vendor tools may narrow that gap.
- e: Eligibility is estimated because establishment-level NAICS coding does not reveal independence, control rights, customer concentration, or owner dependence.
- e: The provided firm count is a frozen margin-bridged estimate, not an observed count of firms with normalized earnings in the specified band.
- e: Concession operations can have recurring contracts but volatile event-driven economics.
- s5: The Gallup population spans sectors and business sizes and records intentions rather than completed transfers.
- s5: The survey permits multiple responses, so sell and transfer components cannot be added without adjustment.
- s5: No observed five-year transaction denominator was found for NAICS 722310.
- q: Compass is much larger and more diversified than firms in the lens and reports globally.
- q: Contract labels do not reveal every gain-sharing clause, subsidy, commission, or renewal response.
- q: The estimate excludes demand and volume effects and addresses only retention of implemented gross benefit.
- d5: Occupational employment is not service quantity and embeds assumed productivity.
- d5: Compass's addressable-market estimate is global, management-authored, and not adjusted to constant price or current service quality.
- d5: End-market mix varies sharply by contractor; workplace dining and healthcare can move in different directions.
- o: No source directly measures operator-required share for this industry over five years.
- o: Management accountability in the present NAICS definition does not prove that every future service format retains the same organizational boundary.
- o: Institutional food safety and labor requirements support persistence, while unattended formats create a larger downside in workplace and convenience settings.

## Sources
- **S1** — [North American Industry Classification System: Sector 72, NAICS 722310 Food Service Contractors](https://www.census.gov/naics/resources/archives/sect72.html) (accessed 2026-07-22): Defines 722310 as food service at institutional, governmental, commercial, or industrial locations under contracts for a specified period; says contract structures vary and management staff is always supplied by the contractor; separates single-event catering and vending.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 722300 Special Food Services](https://www.bls.gov/oes/2023/may/naics4_722300.htm) (accessed 2026-07-22): Reports 720600 total workers and detailed employment shares and wages, including 73.32% food preparation and serving, 4.67% management, 4.48% sales, and 3.35% office and administrative support.
- **S3** — [Deloitte: Restaurant AI Investments Heat Up, But Adoption Still Appears to Be on the Back Burner](https://www.deloitte.com/us/en/about/press-room/deloitte-how-ai-is-revolutionizing-restaurants.html) (accessed 2026-07-22): Reports a survey of 375 global restaurant executives: daily AI use in customer experience at 63% and inventory at 55%; food preparation deployment at half or less; readiness at 21% for risk and governance, 29% for technology, and 27% for talent.
- **S4** — [NFIB 2025 Small Business and Technology Survey](https://www.nfib.com/wp-content/uploads/2025/06/2025-NFIB-Technology-Survey.pdf) (accessed 2026-07-22): Reports 24% current AI use among small-business owners, 4% using or planning AI for process automation, 98% of users seeing no employment change, and 56% expecting AI to matter to their own operations within five years.
- **S5** — [Compass Group Half Year 2026 Investor Factsheet](https://www.compass-group.com/content/dam/compass-group/corporate/Investors/Results-presentations/2026/Compass-Group-Half-Year-2026-Investor-Factsheet.pdf.downloadasset.pdf) (accessed 2026-07-22): Reports contract structures of one-third cost-plus, one-third operator-risk, and one-third fixed price; describes dynamic pricing, increased fixed-price pricing cadence, food and labor indexation, and an addressable market growing around 5% annually.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 owner survey reports that among employer owners, 13% planned a sale, 11% a transfer, and 22% the combined sell-or-transfer outcome within five years; 5% planned closure and 5% had no plan.
- **S7** — [BLS Occupational Outlook Handbook: Food and Beverage Serving and Related Workers](https://www.bls.gov/ooh/food-preparation-and-serving/food-and-beverage-serving-and-related-workers.htm) (accessed 2026-07-22): Projects 5% employment growth from 2024 to 2034, describes physical and customer-service duties, and says hospital and residential-care cafeterias should serve more prepared meals and these workers remain essential.
- **S8** — [BLS Occupational Outlook Handbook: Food Service Managers](https://www.bls.gov/ooh/management/food-service-managers.htm) (accessed 2026-07-22): Projects 6% employment growth from 2024 to 2034 and describes responsibility for staffing, scheduling, purchasing, kitchen operations, food safety, complaints, budgets, payroll, and records.
- **S9** — [Compass Group Annual Report 2025](https://www.compass-group.com/content/dam/compass-group/corporate/oar-2025/oar-page/annual-report-2025.pdf) (accessed 2026-07-22): Describes competitive client retention risk, AI and cashless technology as efficiency and retention tools, labor scheduling and technology as inflation mitigations, and contractual cost indexation as a right to review client pricing.
