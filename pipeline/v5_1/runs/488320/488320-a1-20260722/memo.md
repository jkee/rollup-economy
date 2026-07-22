# 488320 — Marine Cargo Handling

*v5.1 Stage 1 research memo. Run `488320-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.54 · L 0.73 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can improve a costly planning, documentation, and equipment-utilization layer around recurring physical cargo moves, and recent consolidation demonstrates transferable operations.
**Weakness:** Most labor remains physical and labor-protected, while per-unit and cost-plus contracting gives powerful customers a clear path to recapture productivity gains.

## Business-model lens
- Included: US lower-middle-market firms repeatedly providing outsourced stevedoring, vessel loading and discharge, terminal transfer, container and break-bulk handling, bulk handling, Ro/Ro handling, and related on-terminal cargo movement to external carriers, terminal operators, shippers, and cargo owners.
- Excluded: Captive cargo-handling units serving only a parent carrier or cargo owner, port and pier operation classified in 488310, warehousing, freight packing, pure equipment leasing, shells, and non-control financing vehicles.
- Customer and revenue model: Customers buy labor- and equipment-intensive handling under per-unit, per-ton, per-container, gang-hour, time-and-materials, cost-plus, minimum-quantity, and broader terminal-service contracts, often within port concessions and coastwide labor frameworks.
- Deviation from default lens: none

## Executive view
Marine cargo handling has a high labor burden but a smaller AI-substitutable share than the headline labor intensity suggests because much of the payroll is physical, safety-sensitive work. AI can improve manifests, planning, dispatch, yard sequencing, billing, maintenance, safety reporting, and exception management. Existing port automation proves the direction, while labor agreements, capital needs, and mixed equipment performance slow implementation. The industry is transferable and consolidating, but transparent per-unit and cost-plus pricing limits retention.

## How AI changes the work
The near-term opportunity is to surround longshore and equipment work with better decisions: parse documents, forecast labor and equipment demand, assign moves, optimize sequences, predict equipment failures, reconcile counts, draft reports, and automate routine customer communication. Process automation is already common at large ports, so a must target remaining manual exceptions and fragmented back offices. Autonomous handling equipment can reduce direct labor, but its economics require scale, site redesign, integration, and negotiated work rules.

## Value capture
Handlers can keep some gains within a contract term and can sell better throughput, turnaround, visibility, safety, and reliability. However, rates often expose units, hours, or costs, and concentrated carriers, terminals, and cargo owners can demand repricing. Minimum quantities soften volume risk without necessarily protecting margin. Union wage and benefit commitments can also absorb part of the gain, making capacity expansion and avoided hiring more realistic capture mechanisms than layoffs.

## Firm availability
The six-digit definition closely matches outsourced service providers, but some operations are captive or embedded in large terminal and logistics groups. Recent acquisitions by Pangaea, AMPORTS, and Enstructure show active strategic consolidation and the transferability of handling operations. The public examples are larger than the LMM lens, and local operating rights, union obligations, equipment, and customer relationships must transfer together.

## Demand durability
Cargo flows create unavoidable physical handling demand, and the national water-freight outlook supports modest growth. The operator remains necessary even in an automated terminal. Durability is target-specific: a diversified handler at a strategic port differs radically from a single-customer, single-commodity stevedore. Trade policy, commodity cycles, route changes, strikes, weather, port capital projects, and carrier consolidation are principal demand risks.

## Risks and uncertainty
The largest evidence gap is six-digit task composition. Available BLS data cover broader water-support activities, while GAO automation research emphasizes major container ports. LMM bulk and break-bulk handlers may have different economics. Contract pass-through, local labor rules, concession transfer, customer concentration, equipment condition, safety record, and environmental liabilities require target-level diligence. The 2030 East/Gulf labor agreement materially limits five-year freedom to redesign work.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3246 | — | OBSERVED | — |
| n | — | 40 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.22 | PROXY | S1, S2, S3 |
| rho | 0.23 | 0.4 | 0.58 | ESTIMATE | S3, S4 |
| e | 0.48 | 0.68 | 0.83 | ESTIMATE | S1, S5 |
| s5 | 0.15 | 0.28 | 0.43 | PROXY | S6, S7, S8, S9 |
| q | 0.24 | 0.42 | 0.61 | ESTIMATE | S10, S4 |
| d5 | 0.96 | 1.04 | 1.13 | PROXY | S11, S12 |
| o | 0.83 | 0.92 | 0.98 | PROXY | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.24 | 0.73 | 1.66 | ESTIMATE |
| F | 2.18 | 3.46 | 4.39 | ESTIMATE |
| C | 4.80 | 8.40 | 10.00 | ESTIMATE |
| D | 7.97 | 9.57 | 10.00 | PROXY |

## Caveats
- a: Four-digit NAICS 488300 mixes marine cargo handling with port operations, pilots, tug services, and other water-support activities.
- a: OEWS occupation shares are not task shares, and currently automated tasks are not separately identified.
- a: The frozen compensation-to-receipts input uses 2024 wages over 2022 receipts and is harmonized to the IPS basis, while the occupation evidence is 2023.
- rho: The ILA-USMX agreement applies to Atlantic and Gulf Coast covered employers, not the West Coast or every inland and nonunion operation.
- rho: GAO's large-container-port sample may not transfer to smaller bulk, break-bulk, and project-cargo handlers.
- rho: The estimate applies only to the exposed opportunity in a and excludes demand and pricing.
- e: NAICS is establishment-based while eligibility concerns transferable firms.
- e: Integrated terminal operators can combine 488320 handling with 488310 port operation, warehousing, trucking, and shipping.
- e: The frozen n is margin-bridged from SUSB size classes using a transportation-sector EBITDA margin and is quality ESTIMATE.
- s5: The owner-age source is cross-industry, old, and owner-level rather than firm-level.
- s5: Public deal announcements omit failed sales, closures, and internal reorganizations and skew large.
- s5: Terminal asset acquisitions and operating-right transfers are not always equivalent to buying a standalone LMM firm.
- q: One public-company accounting policy does not establish the mix of contract types among LMM stevedores.
- q: Union wage increases and work rules may convert automation gains into negotiated labor or benefit costs.
- q: Retention differs between dedicated terminals, spot stevedoring, government work, and integrated logistics contracts and excludes demand and implementation effects.
- d5: FAF5.2 forecasts embed assumptions available in 2021 and precede later trade-policy and routing changes.
- d5: Tonnage does not map one-for-one to labor or revenue: containers, vehicles, dry bulk, liquid bulk, break-bulk, and project cargo have different handling intensity.
- d5: National growth can coexist with severe declines at a single port, terminal, commodity, or customer.
- o: Container-terminal automation is not representative of all bulk, break-bulk, vehicle, and project-cargo work.
- o: The distinction between a cargo-handling operator and an integrated port or carrier can change without eliminating physical handling.
- o: This primitive is separate from implemented labor opportunity in rho and demand quantity in d5.

## Sources
- **S1** — [2022 North American Industry Classification System Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines NAICS 488320 as establishments primarily providing stevedoring and other marine cargo handling services except warehousing and distinguishes packing, warehousing, and port-operation activities.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 488300](https://www.bls.gov/oes/2023/may/naics4_488300.htm) (accessed 2026-07-22): Broader water-support occupation mix: 95,160 jobs; 61.16% transportation/material moving; 27.71% material movers; 17.10% hand laborers; 14.06% installation, maintenance and repair; and 10.76% office/administrative support.
- **S3** — [Port Infrastructure: U.S. Ports Have Adopted Some Automation Technologies and Report Varied Effects](https://www.gao.gov/products/gao-24-106498) (accessed 2026-07-22): GAO found process automation at terminals in all ten largest US container ports, automated cargo-handling equipment at four, and mixed effects involving performance, workforce, security, cost, and labor agreements.
- **S4** — [ILA and USMX Sign Six-Year Master Contract Agreement](https://usmx.com/assets/content/public-resources/3-11-25_USMX-ILA_Sign_Historic_6-Year_Master_Contract.pdf) (accessed 2026-07-22): Documents the October 2024-September 2030 East and Gulf Coast agreement, its current-job protection and technology framework, labor peace, and the ILA president's description of automation protection and a 62% wage increase.
- **S5** — [Port Performance Freight Statistics Program: Annual Report to Congress 2018](https://www.bts.gov/sites/bts.dot.gov/files/docs/browse-statistical-products-and-data/port-performance/224751/ppfsp-annual-report2018.pdf) (accessed 2026-07-22): Distinguishes private terminals owned by vessel operators, cargo interests, and independent marine terminal operators, and explains varied ownership, revenue, control, and operating structures.
- **S6** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): 2019 ABS infographic for reference year 2018 reports 51% of responding employer-business owners were age 55 or older, 43% were 35-54, and 6% were 34 or younger.
- **S7** — [Pangaea Logistics Solutions Announces Completion of Port and Terminal Operations Acquisition](https://www.prnewswire.com/news-releases/pangaea-logistics-solutions-announces-completion-of-port-and-terminal-operations-acquisition-301840753.html) (accessed 2026-07-22): Documents Pangaea's June 2023 acquisition of marine port terminal operations in Florida and Maryland from Host Terminals and describes dry-bulk cargo-handling services.
- **S8** — [AMPORTS Acquires Red Hook ConRo Terminal at Port Freeport](https://www.amports.com/2026/01/16/amports-expands-stevedoring-operations-with-acquisition-of-red-hook-conro-terminal-at-port-freeport/) (accessed 2026-07-22): Documents a 2026 acquisition of an operating stevedoring and terminal business and AMPORTS' expansion of active US stevedoring operations.
- **S9** — [Enstructure to Acquire LOGISTEC Marine Terminal Division](https://www.globenewswire.com/news-release/2026/06/15/3311934/0/en/enstructure-to-acquire-logistec-marine-terminal-division-creating-a-leading-network-of-marine-terminals-across-north-america.html) (accessed 2026-07-22): Documents a June 2026 agreement to acquire LOGISTEC's North American marine terminal operations, including bulk, break-bulk, and container cargo-handling services across 62 ports and 84 terminals.
- **S10** — [Pangaea Logistics Solutions Ltd. 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1606909/000160690925000097/panl-20241231.htm) (accessed 2026-07-22): Describes stevedoring contracts priced per unit with possible minimum quantities and expected-cost-plus-margin allocation, terminal service contracts, and direct labor and equipment-related terminal expenses.
- **S11** — [Freight Analysis Framework Version 5](https://ops.fhwa.dot.gov/freight/freight_analysis/faf/faf5/FAF5FHWAWebinarJuly282022final.pdf) (accessed 2026-07-22): FAF5.2 baseline forecast shows domestic water-mode freight tonnage increasing from 662.453 million tons in 2017 to 855.079 million in 2050, a 0.8% compound annual growth rate, with wide commodity variation.
- **S12** — [U.S. Port Infrastructure: DOT and DHS Offer Funding and Other Assistance Ports Can Use to Improve Disaster Resilience](https://files.gao.gov/reports/GAO-25-107159/index.html) (accessed 2026-07-22): Reports that more than 300 US waterside ports handled over $2.28 trillion of international trade in 2022 and describes the physical coordination and resilience role of port and terminal operators.
