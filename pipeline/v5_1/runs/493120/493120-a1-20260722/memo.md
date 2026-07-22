# 493120 — Refrigerated Warehousing and Storage

*v5.1 Stage 1 research memo. Run `493120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 7.34 · L 4.63 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Standardized pallet workflows and harsh cold environments create strong labor-avoidance incentives while physical custody and temperature control remain indispensable.
**Weakness:** Capital-intensive implementation and a small, consolidating firm pool are compounded by uncertainty over whether future capacity growth stays outsourced or shifts to captive networks.

## Business-model lens
- Included: US lower-middle-market operators that repeatedly provide outsourced refrigerated and frozen storage, handling, inventory control, blast freezing, case picking, inspection, and related cold-chain warehouse services to external customers.
- Excluded: Captive food-producer or retailer warehouses, passive real-estate shells, refrigerated transportation without warehousing, general dry storage, household cold lockers, non-control financing vehicles, and firms without recurring or repeat external-customer service revenue.
- Customer and revenue model: Food producers, processors, distributors, retailers, and selected life-sciences customers buy recurring temperature-controlled space plus transactional handling and value-added services under warehouse agreements, rate letters, tariffs, and occasionally dedicated leases, often with minimum storage commitments and price-adjustment clauses.
- Deviation from default lens: none

## Executive view
Refrigerated warehouses have structured, labor-intensive movement and information flows, strong incentives to remove people from harsh environments, and service demand anchored in physical product integrity. The opportunity is constrained by high capital needs, food-safety requirements, facility specificity, and evidence that recent capacity growth has favored private as well as public warehouses.

## How AI changes the work
AI can forecast per-load labor, schedule appointments and shifts, optimize slotting and energy use, reconcile inventory, triage exceptions, and automate documentation and billing. Paired with pallet shuttles, AS/RS, AMRs, conveyors, and WES controls, it can reduce movement and picking labor, while humans remain essential for loading variability, sanitation, maintenance, compliance, and recovery from faults.

## Value capture
Minimum storage guarantees and fixed transactional service rates can preserve productivity savings during contract terms. Short rate letters, annual tariffs, cost-to-serve reviews, renewal bargaining, and sophisticated food-company customers make retention incomplete over five years.

## Firm availability
Properly classified independent cold stores generally provide recurring outsourced service, but the LMM pool is small and transferability depends on real estate, refrigeration assets, environmental condition, certifications, and customer concentration. Multiple completed acquisitions show strategic demand, but no denominator supports treating deal examples as an observed transfer rate.

## Demand durability
Refrigerated product must remain within a controlled physical chain, and customer survey evidence points to rising frozen and refrigerated food demand. USDA capacity grew overall from 2023 to 2025, but public capacity declined as private capacity rose, so outsourced service growth should be underwritten below total cold-chain capacity growth.

## Risks and uncertainty
A bad outcome combines expensive automation with an unsuitable legacy building, poor WMS data, commissioning downtime, food-safety failures, and a customer contract that reprices the benefit away. Demand can also disappoint through inventory destocking, speculative overbuilding, customer insourcing, consolidation, or loss of a concentrated account.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6886 | — | OBSERVED | — |
| n | — | 128 | — | ESTIMATE | — |
| a | 0.33 | 0.45 | 0.58 | PROXY | S1, S2, S5 |
| rho | 0.22 | 0.38 | 0.56 | PROXY | S3, S4, S5 |
| e | 0.7 | 0.82 | 0.92 | ESTIMATE | S8 |
| s5 | 0.1 | 0.16 | 0.23 | PROXY | S6, S9 |
| q | 0.3 | 0.52 | 0.7 | PROXY | S5 |
| d5 | 0.93 | 1.08 | 1.22 | PROXY | S7, S8, S10 |
| o | 0.86 | 0.94 | 0.99 | ESTIMATE | S5, S7, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.00 | 4.71 | 8.95 | PROXY |
| F | 3.70 | 4.63 | 5.37 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | PROXY |
| D | 8.00 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source combines all warehousing and storage industries and employer sizes.
- a: Lineage is a global scale leader whose automation footprint and workflow standardization differ from LMM firms.
- a: The frozen compensation-to-output input is sector-specific but does not reveal the wage share of each task.
- rho: The CSW case study is vendor-authored and reports capabilities rather than a quantified labor reduction.
- rho: MHI is an industry association for material-handling suppliers and users, not a representative adoption survey.
- rho: Automation can be economically attractive in new high-throughput buildings but infeasible in smaller brownfield sites.
- e: USDA counts facilities rather than firms and includes private and semiprivate warehouses outside the default lens.
- e: The frozen n input is margin-bridged and may misclassify capital-intensive firms whose normalized EBITDA differs from the assumed transportation margin.
- e: Dedicated facilities may have recurring revenue but depend on a single customer and specific real estate.
- s5: Gallup includes employer firms of all industries and sizes and measures plans rather than completions.
- s5: Lineage acquisitions are examples from one dominant buyer and do not establish an annual transfer rate.
- s5: The estimate excludes real-estate-only purchases, captive asset transfers without an external-service business, minority recapitalizations, and closures.
- q: The source is a global public operator substantially larger than the target firms.
- q: Dedicated build-to-suit, shared public warehouse, rate-letter, tariff, and lease economics differ materially.
- q: Energy and refrigeration costs can obscure labor savings in customer pricing and operator margins.
- d5: Capacity is supply, not utilization or constant-quality demand.
- d5: USDA's public/private classification is facility-based and the survey vintages are only two years apart.
- d5: The customer-demand survey covers the United States, Canada, and Mexico and was sponsored by the largest provider.
- d5: Public capacity contraction signals that total cold-chain expansion may not accrue proportionally to outsourced operators.
- o: No source directly measures the future share of outsourced cold-storage quantity requiring a lens operator.
- o: Public capacity fell while private and semiprivate capacity expanded between USDA surveys, but capacity does not reveal occupied volume.
- o: Automation changes staffing intensity more readily than it removes operator accountability.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 493100 Warehousing and Storage](https://www.bls.gov/oes/2023/may/naics4_493100.htm) (accessed 2026-07-22): Broader warehousing occupation mix and wages: transportation/material-moving 75.38% of employment, office support 10.13%, and management 2.93%, with detailed core warehouse roles.
- **S2** — [Factors affecting occupational utilization, 2024-34](https://www.bls.gov/emp/tables/factors-affecting-occupational-utilization.htm) (accessed 2026-07-22): BLS identifies AGVs, robotics, collaborative automation, and automated storage/retrieval as reducing staffing shares in core NAICS 493000 material-moving, packing, and stocking occupations.
- **S3** — [Automation for the Cold Chain](https://www.mhi.org/blog/66367/automation-for-the-cold-chain) (accessed 2026-07-22): Cold-specific labor difficulty and applicable automation including AS/RS, pallet shuttles, AMRs, conveyors, WCS, WES, and WMS integration, alongside temperature-zone equipment constraints.
- **S4** — [An Effective, AI-driven Approach to Predictive Labor Resourcing: CSW Success Story](https://datexcorp.com/casestudy/csw-datex-endeavor-labs-case-study-2/) (accessed 2026-07-22): A five-location third-party cold-storage provider used two years of WMS shipment and activity data to deploy ML-based hourly labor and throughput predictions.
- **S5** — [Lineage, Inc. 2025 Form 10-K](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001868159/68d35d88-89d6-4e9f-985d-c891eb0967bb.html) (accessed 2026-07-22): Cold-storage contract types, one-to-five-year typical warehouse agreements, transactional pricing, minimum guarantees, repricing mechanisms, labor as largest operating-cost component, 83 fully/semi-automated warehouses among 501, and long customer relationships.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 owner survey finding that 22% of employer-business owners planned to sell or transfer ownership within five years.
- **S7** — [USDA NASS Capacity of Refrigerated Warehouses 2023 Summary](https://esmis.nal.usda.gov/sites/default/release-files/x059c7329/cc08k3098/vq281845s/rfwh0125.pdf) (accessed 2026-07-22): In 2023, US gross refrigerated capacity was 3.70 billion cubic feet; public warehouses held 2.51 billion cubic feet or 68% of total capacity; 492 of 900 facilities were public.
- **S8** — [USDA NASS Capacity of Refrigerated Warehouses 2025 Summary](https://esmis.nal.usda.gov/sites/default/release-files/795764/rfwh0126.pdf) (accessed 2026-07-22): In 2025, US gross refrigerated capacity was 3.99 billion cubic feet; public warehouses held 2.46 billion cubic feet or 62% of total capacity; 476 of 931 facilities were public.
- **S9** — [Lineage 2025 business combinations and asset acquisitions disclosure](https://www.sec.gov/Archives/edgar/data/1868159/000186815926000012/R12.htm) (accessed 2026-07-22): Completed acquisitions of Bellingham Cold Storage in 2025, ColdPoint Logistics in 2024, and Burris and NOVA cold-storage operations in 2023, plus the 2025 Tyson warehouse asset acquisition.
- **S10** — [Lineage 2026 Cold Chain Insights Survey](https://www.onelineage.com/news-stories/lineage-cold-chain-insights-survey-2026) (accessed 2026-07-22): Survey of 1,000 food-and-beverage supply-chain decision-makers across the US, Canada, and Mexico: 72% reported rising refrigerated/frozen-food demand and respondents prioritized AI, data, automation, and flexible 3PL capacity.
