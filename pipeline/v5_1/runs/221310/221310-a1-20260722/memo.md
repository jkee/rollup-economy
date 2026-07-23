# 221310 — Water Supply and Irrigation Systems

*v5.1 Stage 1 research memo. Run `221310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.98 · L 1.59 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Essential recurring water service and aging distribution and treatment infrastructure sustain demand and operational need.
**Weakness:** Regulation, public or mutual ownership, capital intensity, and transaction approvals constrain both benefit retention and acquisition availability.

## Business-model lens
- Included: U.S. lower-middle-market operators of water treatment plants and water supply or irrigation systems serving external residential, commercial, industrial, agricultural, or wholesale customers through pumping, treatment, storage, aqueducts, and distribution mains.
- Excluded: Government administration of irrigation districts, water and sewer construction contractors, lawn sprinkler installers, landscaping irrigation services, bottled-water retailers, captive industrial systems, and software or equipment vendors that do not operate a water system.
- Customer and revenue model: Recurring metered, tariff, assessment, membership, capacity, or wholesale revenue for operating an essential physical water supply or irrigation system for external customers.
- Deviation from default lens: none

## Executive view
Water supply and irrigation systems provide essential recurring service with strong operator persistence and meaningful administrative, metering, planning, and asset-analytics opportunities. Physical operations, public-health accountability, legacy infrastructure, regulation, cybersecurity, and constrained conventional transferability limit implementation and capture.

## How AI changes the work
AI can improve billing and customer service, meter-data review, forecasting, leak detection, maintenance planning, compliance documentation, scheduling, and engineering analysis. Treatment control, sampling, repair, construction, emergencies, and licensed accountable operation remain human- and asset-intensive.

## Value capture
Natural-monopoly service and tariff lag protect some near-term benefit, but regulated cost-of-service reviews, public or member governance, affordability, and contract negotiations can share savings with customers over five years.

## Firm availability
Many private systems fit recurring external service, but governmental, mutual, nonprofit, captive, construction-led, and legally difficult-to-transfer entities reduce eligibility. Transactions can require extensive approvals and local acceptance.

## Demand durability
Essential service, customer growth, treatment requirements, and massive infrastructure renewal needs support durability. Conservation, leakage reduction, drought, climate variability, and flat per-capita use keep real quantity growth modest.

## Risks and uncertainty
Principal risks are water rights and source security, drought and extreme weather, contamination, aging assets, rate and affordability politics, cybersecurity, environmental compliance, capital intensity, approval-heavy transfers, and mixing drinking-water and irrigation models.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2957 | — | OBSERVED | — |
| n | — | 413 | — | ESTIMATE | — |
| a | 0.2 | 0.32 | 0.44 | PROXY | S2, S3 |
| rho | 0.23 | 0.42 | 0.6 | PROXY | S3, S6 |
| e | 0.48 | 0.68 | 0.82 | ESTIMATE | S1 |
| s5 | 0.08 | 0.18 | 0.3 | ESTIMATE | — |
| q | 0.34 | 0.52 | 0.69 | ESTIMATE | S1 |
| d5 | 0.98 | 1.03 | 1.1 | PROXY | S4, S5 |
| o | 0.985 | 0.997 | 1 | ESTIMATE | S1, S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.54 | 1.59 | 3.12 | PROXY |
| F | 4.54 | 6.34 | 7.45 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 9.65 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS data cover water, sewage, and other systems rather than 221310 alone and include public employers of all sizes.
- a: Advanced metering documents technical uses but not wage-weighted labor savings or the extent of existing automation.
- rho: EPA's advanced-metering page establishes capabilities rather than penetration or realized labor effects.
- rho: Cybersecurity evidence covers community drinking-water systems broadly and may be more stringent than some irrigation operators.
- e: The Census industry definition mixes drinking-water and irrigation systems with different ownership, regulation, seasonality, and transferability.
- e: The frozen firm estimate is derived from private-firm receipts but may still include mutual, cooperative, or special-purpose structures that do not fit a conventional acquisition.
- s5: No exact national denominator of eligible privately controlled systems and completed control transfers was found.
- s5: Strategic consolidators may make transfers more frequent in some states, while local opposition and approval processes can block or delay them.
- q: Capture differs sharply among investor-owned regulated utilities, unregulated small systems, mutual water companies, and irrigation associations.
- q: The estimate concerns discounted retained gross benefit and does not treat capital investment, rate base growth, or financing as labor benefit.
- d5: BLS projects the broader 221300 industry, including sewage, rather than six-digit water supply and irrigation quantity.
- d5: EPA's $625 billion need is a twenty-year capital requirement for public drinking-water systems, not a forecast of billed water demand or private LMM revenue.
- o: This estimates persistence of an accountable operator of the lens's kind, not survival of a particular ownership structure or firm.
- o: Severe drought or source loss can eliminate individual systems even while aggregate water service remains essential.

## Sources
- **S1** — [221310: Water Supply and Irrigation Systems](https://data.census.gov/profile/221310_-_Water_Supply_and_Irrigation_Systems?codeset=naics~221310) (accessed 2026-07-22): Exact industry scope, system components, uses, exclusions, and employer-establishment context.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Water, Sewage and Other Systems](https://www.bls.gov/oes/2023/may/naics4_221300.htm) (accessed 2026-07-22): Broad water-sector occupational structure used for the wage-weighted task-exposure bridge.
- **S3** — [Advanced Metering Infrastructure](https://www.epa.gov/watersense/advanced-metering-infrastructure) (accessed 2026-07-22): Utility digital-metering capabilities for billing, leak detection, customer usage data, and water-resource management.
- **S4** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Official ten-year employment and real-output projection for water, sewage, and other systems.
- **S5** — [EPA's 7th Drinking Water Infrastructure Needs Survey and Assessment](https://www.epa.gov/dwsrf/epas-7th-drinking-water-infrastructure-needs-survey-and-assessment) (accessed 2026-07-22): Twenty-year public drinking-water infrastructure need and its distribution, treatment, storage, and source components.
- **S6** — [Enforcement Alert: Drinking Water Systems to Address Cybersecurity Vulnerabilities](https://www.epa.gov/enforcement/enforcement-alert-drinking-water-systems-address-cybersecurity-vulnerabilities) (accessed 2026-07-22): Operational-technology dependence, public-health consequences, cyber risk, and required human risk and response controls.
