# 531110 — Lessors of Residential Buildings and Dwellings

*v5.1 Stage 1 research memo. Run `531110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.42 · L 1.30 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring rent supports retention of administrative productivity while occupied homes continue to require accountable maintenance and resident operations.
**Weakness:** Many apparent firms are property-holding entities whose eligibility, earnings band, and qualifying control-transfer path do not resemble a transferable service platform.

## Business-model lens
- Included: US lower-middle-market residential owner-lessors and master lessors that repeatedly lease homes, apartments, townhomes, or similar dwellings to external residents and retain an accountable operating role in leasing, tenant service, compliance, maintenance, or vendor oversight.
- Excluded: Residential property managers acting solely for third-party owners, passive single-asset shells with no transferable operating organization, captive internal real-estate units, non-control financing vehicles, and firms outside the approximately $1-10M normalized EBITDA band.
- Customer and revenue model: External residents pay recurring rent under leases for occupancy; the lessor retains rental revenue and bears or coordinates property operating, maintenance, compliance, and tenant-service obligations, sometimes through third-party managers.
- Deviation from default lens: none

## Executive view
Residential owner-lessors have recurring lease revenue and repeat tenant operations, with clear AI opportunities in communications, leasing administration, collections, reporting, and work-order triage. The main screening problem is that the NAICS population also contains passive or single-asset property entities whose value and transfer mechanics are primarily real-estate rather than operating-platform driven.

## How AI changes the work
AI can draft and classify resident communications, answer routine questions, extract lease data, support applicant workflows, reconcile payments, forecast delinquencies, triage maintenance requests, prepare reports, and coordinate vendors. Human operators remain necessary for fair-housing judgment, exceptions, inspections, repairs, emergencies, disputes, and accountable decisions.

## Value capture
Lease rents are not tied directly to administrative labor hours, so savings can persist within lease terms. Capture is reduced by software and implementation costs, regulated rents, renewal competition, resident concessions, outsourced-manager economics, and the need to reinvest in service quality.

## Firm availability
Some multi-property residential owner-operators are transferable businesses, but many nominal firms are asset-holding entities or outsource the operating layer. Visible property sales and recapitalizations do not establish a high probability of qualifying control transfer of an operating platform.

## Demand durability
Rental housing and occupancy services should remain durable, but national vacancy has risen from recent lows and local supply-demand conditions vary widely. Software changes how leasing and service are delivered more readily than it eliminates the need for housing or accountable property operations.

## Risks and uncertainty
Major uncertainties are the frozen firm's margin-based band assignment, passive-entity prevalence, local rent and vacancy cycles, rent regulation, fair-housing and privacy exposure, outsourced management, fragmented property systems, and confusing asset transactions with operating-company transfers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1652 | — | OBSERVED | — |
| n | — | 902 | — | ESTIMATE | — |
| a | 0.2 | 0.34 | 0.48 | PROXY | S2 |
| rho | 0.35 | 0.58 | 0.78 | PROXY | S2, S3 |
| e | 0.15 | 0.35 | 0.6 | ESTIMATE | S1 |
| s5 | 0.04 | 0.1 | 0.2 | ESTIMATE | — |
| q | 0.55 | 0.72 | 0.88 | ESTIMATE | S1 |
| d5 | 0.94 | 1.02 | 1.1 | PROXY | S2, S4 |
| o | 0.72 | 0.86 | 0.95 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.46 | 1.30 | 2.47 | PROXY |
| F | 2.99 | 5.60 | 7.55 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.77 | 8.77 | 10.00 | ESTIMATE |

## Caveats
- a: BLS describes an occupation across residential, commercial, and community-association settings rather than the 531110 workforce.
- a: Task lists and importance do not measure time shares or identify work already automated.
- a: The supplied compensation ratio is low and may reflect outsourced management and maintenance, so exposed direct payroll is not the whole operating-cost opportunity.
- rho: Use of any AI tool is not the implemented share of exposed work.
- rho: The AppFolio sample covers property-management professionals, not specifically LMM residential owner-lessors.
- rho: Vendor-sponsored respondents may overrepresent digitally mature firms.
- e: No source measures lens eligibility among firms in the supplied EBITDA band.
- e: The frozen firm count is margin-bridged using a 3.96% Real Estate Operations and Services margin associated with agency, brokerage, and property-management economics; owner-lessor normalized earnings can differ materially, so band membership may be misstated.
- e: Legal-entity and establishment counts may split one portfolio across many property-owning entities or combine related properties.
- s5: No matched denominator of eligible LMM residential owner-lessors was observed.
- s5: Asset-level sales are not qualifying firm-control transfers.
- s5: Private partnership and beneficial-ownership changes are incompletely disclosed.
- q: No source directly measures retention of AI-derived gross benefit by residential owner-lessors.
- q: Expense responsibility, rent regulation, and lease duration vary across markets and property types.
- q: Savings achieved by a third-party manager may be retained in management fees rather than passed to the owner-lessor.
- d5: Property-manager employment is not constant-price demand for 531110 services.
- d5: The national rental vacancy rate masks large local and property-class differences.
- d5: Rent levels and nominal revenue are not constant-quality quantities.
- o: The mix of single-family rentals, multifamily buildings, residential hotels, and regulated housing is unknown.
- o: Third-party managers can substitute for direct owner-lessor operations without eliminating rental demand.
- o: Rapid improvement in remote access, inspection, and maintenance orchestration could reduce direct operator requirements further.

## Sources
- **S1** — [U.S. Census Bureau NAICS Sector 53: 531110 Lessors of Residential Buildings and Dwellings](https://www.census.gov/naics/resources/archives/sect53.html) (accessed 2026-07-22): Defines 531110 as owner-lessors and sublessors of residential buildings and states that establishments may self-manage or use another establishment to manage the property.
- **S2** — [BLS Occupational Outlook Handbook: Property, Real Estate, and Community Association Managers](https://www.bls.gov/ooh/management/property-real-estate-and-community-association-managers.htm) (accessed 2026-07-22): Lists leasing, rent collection, records, budgeting, inspections, repairs, contracting, complaint, and compliance duties; notes automation of vacancy posting and maintenance-request assignment; and projects 4% employment growth from 2024 to 2034.
- **S3** — [AppFolio 2025 Property Management Benchmark Report Highlights](https://www.appfolio.com/blog/post-2025-benchmark-report) (accessed 2026-07-22): Reports a survey of more than 2,000 property-management professionals and an increase in AI usage from 21% to 34%, alongside heightened fraud and data-security concerns.
- **S4** — [U.S. Census Bureau: Residential Vacancies and Homeownership, First Quarter 2026](https://www.census.gov/housing/hvs/files/currenthvspress.pdf) (accessed 2026-07-22): Reports a 7.3% national rental vacancy rate in first-quarter 2026, statistically unchanged from 7.1% in first-quarter 2025, and a 65.3% homeownership rate.
