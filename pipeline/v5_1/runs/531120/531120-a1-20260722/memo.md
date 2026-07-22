# 531120 — Lessors of Nonresidential Buildings (except Miniwarehouses)

*v5.1 Stage 1 research memo. Run `531120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.97 · L 1.16 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Long-duration lease revenue can retain workflow savings while complex occupied buildings continue to require accountable physical and contractual stewardship.
**Weakness:** The broad code mixes sharply different property-demand trajectories and contains many asset-holding entities that are not transferable operating-service platforms.

## Business-model lens
- Included: US lower-middle-market owner-lessors and master lessors of office, retail, industrial, medical, lodging, and other nonresidential buildings, excluding self-storage, that repeatedly lease space to external tenants and retain accountable leasing, building-operation, maintenance, compliance, or vendor-oversight functions.
- Excluded: Third-party property managers, self-storage lessors, passive single-asset shells without a transferable operating organization, captive internal real-estate units, non-control financing vehicles, venue operators classified elsewhere, and firms outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: External business and institutional tenants pay recurring base rent and, depending on lease structure, reimburse some taxes, insurance, utilities, maintenance, or common-area costs; the lessor provides usable space and remains responsible directly or through vendors for lease administration and building stewardship.
- Deviation from default lens: none

## Executive view
Nonresidential lessors combine recurring lease revenue with document-, accounting-, tenant-, and building-data workflows that are increasingly AI-enabled. The opportunity is constrained by a heterogeneous property mix and by the prevalence of passive asset entities whose economics and transfer path differ from an operating platform.

## How AI changes the work
AI can abstract leases, reconcile receivables and expense recoveries, classify tenant requests, draft communications and reports, forecast maintenance, analyze energy and building-system data, and coordinate vendors. Human operators remain central to negotiations, inspections, life safety, physical repairs, emergencies, capital decisions, and accountable tenant relations.

## Value capture
Multi-year rents and expense-recovery clauses can preserve administrative savings, especially between renewals. Capture is reduced by concessions, competitive renewal terms, manager/vendor bargaining, software integration costs, tenant service expectations, and the need to invest in building systems.

## Firm availability
Eligible multi-property operating lessors exist, but many establishments are single-asset or passive legal entities. Commercial property and portfolio transactions cannot be treated as qualifying control transfers of the operating company without beneficial-owner and platform-level matching.

## Demand durability
Demand diverges sharply: remote work pressures office space and e-commerce pressures some retail, while logistics, medical, lodging, and specialized buildings can be steadier or grow. Physical buildings that remain occupied continue to need accountable stewardship even as administrative and control workflows become more automated.

## Risks and uncertainty
Key risks are property-type and local-cycle concentration, secular office and retail weakness, interest-rate and refinancing stress, passive-entity prevalence, the service-margin bridge used for the frozen firm count, old building-stock evidence, legacy-system integration, cybersecurity, and confusing asset sales with platform transfers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1236 | — | OBSERVED | — |
| n | — | 583 | — | ESTIMATE | — |
| a | 0.22 | 0.38 | 0.54 | PROXY | S2, S3 |
| rho | 0.38 | 0.62 | 0.82 | PROXY | S3 |
| e | 0.12 | 0.32 | 0.58 | ESTIMATE | S1 |
| s5 | 0.04 | 0.11 | 0.23 | ESTIMATE | — |
| q | 0.6 | 0.78 | 0.92 | ESTIMATE | S1, S2 |
| d5 | 0.78 | 0.95 | 1.1 | PROXY | S2, S4, S5, S6 |
| o | 0.66 | 0.82 | 0.94 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.41 | 1.16 | 2.19 | PROXY |
| F | 2.15 | 4.94 | 7.02 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 5.15 | 7.79 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation and IREM evidence span owner and third-party managers, residential and nonresidential properties, and firms larger than the frozen lens.
- a: Task lists and technology use do not provide wage-weighted time shares.
- a: Office, retail, industrial, medical, lodging, and other buildings have different labor mixes and automation potential.
- rho: Use of AI in any workflow is not the share of exposed work operationally implemented.
- rho: The IREM sample is not specific to LMM 531120 owner-lessors and likely overrepresents professional managers.
- rho: Building-system interoperability and data quality vary substantially by asset vintage.
- e: No source directly measures eligibility within the supplied LMM band.
- e: The frozen firm count uses a 3.96% Real Estate Operations and Services margin associated with agency, brokerage, and property-management economics; normalized owner-lessor earnings and depreciation treatment can differ sharply, so band membership may be materially misstated.
- e: One beneficial owner may hold separate buildings in many legal entities.
- s5: No eligible-firm denominator or owner-succession cohort was observed.
- s5: Asset and portfolio sales are not necessarily operating-company control transfers.
- s5: Partnership interest transfers and beneficial-owner changes are often private.
- q: No source directly measures five-year retention of AI-derived gross benefit.
- q: Gross, modified-gross, and net lease structures allocate expenses differently.
- q: Savings produced by outsourced managers may accrue to the manager rather than the owner-lessor.
- d5: Property-manager employment is not constant-price demand for 531120 space or operating services.
- d5: Work-at-home and e-commerce shares are national behavior indicators, not direct five-year space-demand forecasts.
- d5: The CBECS growth comparison ends in 2018 and predates pandemic-era office changes.
- d5: The frozen lens's property-type and geographic mix is unknown.
- o: Triple-net tenants assume more operating responsibility than tenants under gross leases.
- o: Industrial, office, retail, medical, lodging, and mixed-use buildings require different operator involvement.
- o: Third-party property managers can substitute for direct owner-lessor staffing without eliminating building demand.

## Sources
- **S1** — [U.S. Census Bureau NAICS Sector 53: 531120 Lessors of Nonresidential Buildings](https://www.census.gov/naics/resources/archives/sect53.html) (accessed 2026-07-22): Defines 531120 as owner-lessors and sublessors of nonresidential buildings other than self-storage and states that establishments may self-manage or use another establishment to manage property.
- **S2** — [BLS Occupational Outlook Handbook: Property, Real Estate, and Community Association Managers](https://www.bls.gov/ooh/management/property-real-estate-and-community-association-managers.htm) (accessed 2026-07-22): Lists leasing, collections, budgeting, records, inspections, repairs, contracting, complaint, and compliance duties; notes some task automation; and projects 4% occupation employment growth from 2024 to 2034.
- **S3** — [IREM Proptech Insights 2025](https://www.irem.org/file%20library/globalnavigation/learning/tech%20hub/irem-proptech-insights-25-fnl.pdf) (accessed 2026-07-22): Reports 46.3% of respondents using AI in workflows including accounts payable, collections, lease abstraction, and BMS operations, and identifies cost, integration, and cost-benefit hurdles.
- **S4** — [U.S. Census Bureau Quarterly Retail E-Commerce Sales, First Quarter 2026](https://www.census.gov/retail/eCommerce.html) (accessed 2026-07-22): Reports e-commerce at 16.9% of seasonally adjusted retail sales in first-quarter 2026, with year-over-year e-commerce growth of 9.8% versus 3.9% for total retail sales.
- **S5** — [BLS American Time Use Survey: 2025 Results](https://www.bls.gov/news.release/pdf/atus.pdf) (accessed 2026-07-22): Reports that 35% of employed people did some or all work at home on days they worked in 2025, including 51% of workers with a bachelor's degree or higher.
- **S6** — [U.S. EIA: Commercial Buildings Have Gotten Larger in the United States](https://www.eia.gov/todayinEnergy/detail.php?id=46118) (accessed 2026-07-22): Reports 5.9 million commercial buildings and 97 billion square feet in 2018, with building count up 6% and floorspace up 11% from 2012, while identifying variation by building activity.
