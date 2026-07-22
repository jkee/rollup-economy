# 531190 — Lessors of Other Real Estate Property

*v5.1 Stage 1 research memo. Run `531190-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.37 · L 2.21 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring site rent and resident-service workflows create retainable administrative efficiencies while the physical community remains necessary.
**Weakness:** The NAICS code mixes active communities with passive land leasing, making eligible-firm availability and dataset fit unusually uncertain.

## Business-model lens
- Included: US lower-middle-market owner-operators that lease manufactured-home sites to residents who own their homes and receive recurring community access, grounds, utility, compliance, and resident-service operations.
- Excluded: Manufactured homes rented with the site, passive vacant-lot and grazing-land lessors, one-off ground leases without an operating organization, building lessors, self-storage, shells, captive units, non-control financing vehicles, and firms outside the lower-middle-market band.
- Customer and revenue model: Residents typically pay recurring site rent under monthly or annual arrangements, sometimes with separately billed utilities, amenities, storage, home-sale, or other community services.
- Deviation from default lens: Narrowed to manufactured-home-site lessors because the code also contains passive vacant-lot and grazing-land leasing, whose near-absent service workflow, tenant relationship, and operating obligations make one screen incoherent. The narrowing follows an explicit Census example and is not based on attractiveness.

## Executive view
Manufactured-home-site leasing offers recurring fixed rent and durable physical demand, while AI can streamline resident service, collections, leasing, reporting, and vendor coordination. The code-level opportunity is uncertain because 531190 also contains passive land-lessor models and the eligible community share is unknown.

## How AI changes the work
AI can handle routine inquiries, summarize resident cases, draft notices, triage work orders, extract lease and invoice data, support delinquency workflows, forecast occupancy, and compare vendor bids. Field inspection, utilities, maintenance, disputes, compliance, and capital work still require accountable operators.

## Value capture
Site rent is not tied directly to labor hours, creating room to retain efficiencies. Capture is constrained by resident affordability, legal protections, local rent regulation, reputational scrutiny, and the need to reinvest in aging infrastructure.

## Firm availability
Manufactured-home sites are explicitly inside the industry, but the supplied count also covers vacant-lot and grazing-land lessors and may contain property entities rather than operating firms. Public acquisitions show liquidity without resolving the eligible denominator.

## Demand durability
Affordable housing need, resident moving costs, and scarce developed sites support continuity. Local employment, community condition, utility failures, regulation, natural hazards, and closures can nevertheless impair individual properties.

## Risks and uncertainty
The principal uncertainties are the community share of the NAICS population, entity-level count inflation, an unsuitable broad margin anchor, infrastructure liabilities, rent regulation, resident relations, fair-housing compliance, local demand, and limited evidence on AI adoption by independent operators.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2265 | — | OBSERVED | — |
| n | — | 97 | — | ESTIMATE | — |
| a | 0.25 | 0.42 | 0.6 | PROXY | S2, S3 |
| rho | 0.35 | 0.58 | 0.78 | ESTIMATE | — |
| e | 0.2 | 0.45 | 0.7 | ESTIMATE | S1 |
| s5 | 0.08 | 0.17 | 0.28 | ESTIMATE | S3 |
| q | 0.58 | 0.75 | 0.88 | ESTIMATE | S3 |
| d5 | 0.96 | 1.06 | 1.2 | PROXY | S3 |
| o | 0.82 | 0.93 | 0.99 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.79 | 2.21 | 4.24 | ESTIMATE |
| F | 1.51 | 3.43 | 4.82 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.87 | 9.86 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET spans many property types and does not provide manufactured-home-community task shares.
- a: UMH combines site leasing with rental homes, home sales, finance, and other services.
- a: Small community owners may perform maintenance directly rather than employ the occupational mix implied by O*NET.
- rho: No source measures AI implementation in lower-middle-market manufactured-home communities.
- rho: Technology readiness likely varies sharply between professional portfolios and owner-managed communities.
- rho: Resident-facing automation can create accessibility, discrimination, and escalation risks.
- e: No public source measures the manufactured-home-site share of firms in the supplied band.
- e: Property-level special-purpose entities can inflate firm counts relative to transferable operating platforms.
- e: The dataset uses a broad real-estate-services margin that may poorly represent site-rental economics.
- s5: One public REIT's acquisitions are not representative of all qualifying transfers.
- s5: A community sale can be an asset transfer without transfer of the operating company.
- s5: No owner-age or succession distribution is available for the narrowed lens.
- q: UMH's pricing experience may not represent independent operators or regulated jurisdictions.
- q: Resident immobility can support retention but also raises legal, political, and reputational constraints.
- q: No source directly measures pass-through of implemented technology savings.
- d5: Occupancy and nominal income are not direct constant-price, constant-quality quantity measures.
- d5: UMH's portfolio includes rental homes and services outside land-only site leasing.
- d5: National housing need can conceal weak local markets and community closures.
- o: The accountable entity may outsource most daily property management while retaining ownership responsibility.
- o: Operator intensity varies with community age, utility ownership, amenities, and resident-service scope.
- o: Future remote sensing and contractor platforms could reduce the human share more than assumed.

## Sources
- **S1** — [North American Industry Classification System: Sector 53](https://www.census.gov/naics/resources/archives/sect53.html) (accessed 2026-07-22): Defines 531190 as lessors of real estate other than buildings, including manufactured-home sites, vacant lots, and grazing land, and distinguishes buildings and self-storage.
- **S2** — [O*NET OnLine: Property, Real Estate, and Community Association Managers](https://www.onetonline.org/link/summary/11-9141.00) (accessed 2026-07-22): Lists budgeting, rent collection, leasing, records, resident communication, complaint resolution, contractor coordination, inspection, maintenance, and compliance tasks for managers of rented land and property.
- **S3** — [UMH Properties 2025 Annual Report](https://www.sec.gov/Archives/edgar/data/752642/000149315226010595/formars.pdf) (accessed 2026-07-22): Describes manufactured-home-site leasing and community operations; reports 145 communities, occupancy rising from 87.3% to 88.1%, healthy affordable-housing demand, broad annual rent increases, and five communities with 587 sites acquired in 2025.
