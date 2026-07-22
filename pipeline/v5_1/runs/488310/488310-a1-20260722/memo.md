# 488310 — Port and Harbor Operations

*v5.1 Stage 1 research memo. Run `488310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.04 · L 0.92 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI can improve the document, planning, coordination, and maintenance layer around scarce port infrastructure without eliminating the accountable operator.
**Weakness:** The eligible private-firm population is obscured by public and captive facilities, while transparent or cost-plus contracts may transfer much of the productivity benefit to customers.

## Business-model lens
- Included: US lower-middle-market private firms that repeatedly operate ports, harbors, docking and pier facilities, waterfront terminals, or canals for external vessel operators, shippers, cargo owners, or public port authorities.
- Excluded: Public port authorities, captive terminals serving a vessel operator, refinery, grain exporter, or other cargo owner, pure property and infrastructure holding vehicles, marinas, stevedoring-only businesses classified in 488320, navigational services, shells, and non-control financing vehicles.
- Customer and revenue model: Eligible operators earn recurring service, access, docking, storage, facility-use, concession, and terminal-operation revenue under permits, leases, concessions, minimum commitments, per-unit charges, and service contracts.
- Deviation from default lens: none

## Executive view
Port operations combine durable control of physical infrastructure with a meaningful administrative and coordination layer. AI can improve berth and gate planning, document flow, billing, maintenance triage, customer communication, and exception management, but it does not remove the need for a facility operator. The investable population is narrower than the NAICS label suggests because public authorities and captive cargo terminals are common, and contract structures can pass savings back to powerful customers or public counterparties.

## How AI changes the work
Near-term value lies primarily in software workflows rather than autonomous cranes: extracting shipping and facility documents, predicting arrival and congestion, optimizing schedules, generating invoices and reports, prioritizing maintenance, and handling routine customer updates. GAO found process automation already widespread at large container ports, while equipment automation remained less common and produced mixed performance. LMM firms can adopt lighter software faster but face fragmented data, cyber risk, labor agreements, and zero-downtime requirements.

## Value capture
Savings are most retainable in fixed-fee, minimum-commitment, or capacity-constrained arrangements during the current term. They are less retainable under cost-plus, transparent per-unit tariffs, frequent rebids, or public-rate oversight. Faster turns, fewer errors, and better asset uptime can create service value beyond labor reduction, but concentrated shipping and cargo customers have leverage to demand lower charges at renewal.

## Firm availability
The frozen firm count includes an uncertain mix of independent operators, large-company sites, captive terminals, and potentially infrastructure-heavy entities. Federal port research distinguishes public authorities, landlord and operating ports, cargo-owner terminals, carrier terminals, and independent terminal operators. Only the last group cleanly fits. Disclosed terminal-operation acquisitions show transferability, but concession assignment and public approvals can complicate control sales.

## Demand durability
A five-year base case of modest growth is consistent with the federal water-freight forecast and the ongoing role of ports in trade. Physical infrastructure, access, maintenance, resilience, security, and stakeholder coordination create recurring needs. Results will be highly local: route shifts, tariffs, commodity declines, hurricanes, drought, bridge failures, tenant concentration, and new competing capacity can overwhelm national growth.

## Risks and uncertainty
The largest evidence problem is classification. Occupation data are only available for broad 488300 and heavily mix cargo handlers and maritime workers into the port-operator signal. Contract evidence comes from a larger integrated operator, and transfer evidence lacks a denominator. A target's concession term, renewal rights, capital obligations, customer concentration, environmental liabilities, cyber posture, and exposure to one commodity or tenant are more important than the national average.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2099 | — | OBSERVED | — |
| n | — | 65 | — | ESTIMATE | — |
| a | 0.13 | 0.21 | 0.3 | PROXY | S1, S2, S3 |
| rho | 0.34 | 0.52 | 0.68 | ESTIMATE | S3 |
| e | 0.3 | 0.48 | 0.66 | ESTIMATE | S4, S5 |
| s5 | 0.12 | 0.23 | 0.36 | PROXY | S6, S7 |
| q | 0.32 | 0.5 | 0.68 | ESTIMATE | S8, S4 |
| d5 | 0.97 | 1.04 | 1.12 | PROXY | S9, S10, S11 |
| o | 0.88 | 0.95 | 0.99 | PROXY | S1, S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.37 | 0.92 | 1.71 | ESTIMATE |
| F | 1.94 | 3.38 | 4.50 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 8.54 | 9.88 | 10.00 | PROXY |

## Caveats
- a: Four-digit NAICS 488300 includes marine cargo handling, navigational services, and other water-support activities outside 488310.
- a: Occupation shares are not task shares and the within-occupation AI mapping is judgmental.
- a: The frozen compensation-to-receipts input uses 2024 wages over 2022 receipts and is harmonized to the IPS basis, while the occupation evidence is 2023.
- rho: GAO studied the ten largest container ports and selected foreign ports, not LMM 488310 operators.
- rho: Process automation and AI are not identical; the source establishes workflow digitization and constraints rather than AI-specific results.
- rho: The range applies only to exposed work in a and excludes demand and pricing effects.
- e: NAICS is establishment-based, whereas eligibility concerns transferable firms and control of concession rights.
- e: Private terminals may be captive to vessel operators, grain exporters, petroleum refiners, or other cargo interests.
- e: The frozen n is margin-bridged from SUSB size classes using a transportation-sector EBITDA margin and is quality ESTIMATE.
- s5: Owner-age data are old, cross-industry, and represent responding owners rather than firms.
- s5: One disclosed multi-terminal acquisition cannot establish frequency and may be larger than the LMM lens.
- s5: A concession reassignment, operating-contract award, asset sale, and company control sale are economically different events.
- q: The disclosed contract accounting comes from a larger integrated maritime company and blends terminal operations with 488320-type handling.
- q: Revenue models vary sharply between landlord-style facilities, dedicated bulk terminals, public concessions, and service-contract operators.
- q: This primitive excludes implementation difficulty and demand volume.
- d5: FAF5.2 forecasts embed economic assumptions available in 2021 and precede later trade-policy and routing changes.
- d5: Water-mode tonnage does not capture vessel calls, dwell time, passenger or canal activity, pricing, or service intensity.
- d5: National averages conceal port-specific winners and losers and commodity-specific declines.
- o: Large container ports are more automated than many LMM bulk, break-bulk, inland, and specialized facilities.
- o: Operator requirements and self-service risk differ across landlord, terminal, pier, docking, and canal models.
- o: The estimate separates operator persistence from the implemented labor opportunity in rho.

## Sources
- **S1** — [2022 NAICS Definition: 488310 Port and Harbor Operations](https://www.census.gov/naics/?details=488310&input=488310&year=2022) (accessed 2026-07-22): Defines the industry as operating ports, harbors including docking and pier facilities, or canals, and distinguishes marine cargo handling, navigational services, and marinas.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 488300](https://www.bls.gov/oes/2023/may/naics4_488300.htm) (accessed 2026-07-22): Broader water-support occupation mix: 95,160 jobs; 61.16% transportation/material moving; 14.06% installation, maintenance and repair; 10.76% office/administrative support; 6.67% management; and 1.98% business/financial operations.
- **S3** — [Port Infrastructure: U.S. Ports Have Adopted Some Automation Technologies and Report Varied Effects](https://www.gao.gov/products/gao-24-106498) (accessed 2026-07-22): GAO found all ten largest US container ports used some automation, each had a terminal using process automation, four used automated handling equipment, and operators reported mixed workforce, security, performance, cost, and labor-agreement effects.
- **S4** — [Port Performance Freight Statistics Program: Annual Report to Congress 2018](https://www.bts.gov/sites/bts.dot.gov/files/docs/browse-statistical-products-and-data/port-performance/224751/ppfsp-annual-report2018.pdf) (accessed 2026-07-22): Explains landlord, operating, and jurisdictional port models; identifies lease, direct-operation, and vessel-use revenue; and distinguishes carrier-owned, cargo-interest-owned, and independent marine-terminal-operator facilities.
- **S5** — [U.S. Port Infrastructure: DOT and DHS Offer Funding and Other Assistance Ports Can Use to Improve Disaster Resilience](https://files.gao.gov/reports/GAO-25-107159/index.html) (accessed 2026-07-22): Reports more than 300 US waterside ports, describes governmental port authorities and private terminal lessees, and identifies the coordination and resilience responsibilities of port-management entities.
- **S6** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): 2019 ABS infographic for reference year 2018 reports that 51% of responding owners of employer businesses were age 55 or older, 43% were 35-54, and 6% were 34 or younger.
- **S7** — [Pangaea Logistics Solutions Announces Completion of Port and Terminal Operations Acquisition](https://www.prnewswire.com/news-releases/pangaea-logistics-solutions-announces-completion-of-port-and-terminal-operations-acquisition-301840753.html) (accessed 2026-07-22): Documents a June 2023 all-cash acquisition of marine port terminal operations in Florida and Maryland from Host Terminals.
- **S8** — [Pangaea Logistics Solutions Ltd. 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1606909/000160690925000097/panl-20241231.htm) (accessed 2026-07-22): Describes per-unit stevedoring contracts with possible minimum quantities and expected-cost-plus-margin allocation, plus terminal service contracts covering labor, storage, handling, and cargo transfer; also confirms two US port-operation acquisitions.
- **S9** — [Freight Analysis Framework Version 5](https://ops.fhwa.dot.gov/freight/freight_analysis/faf/faf5/FAF5FHWAWebinarJuly282022final.pdf) (accessed 2026-07-22): FAF5.2 baseline forecast shows domestic water-mode freight tonnage increasing from 662.453 million tons in 2017 to 855.079 million in 2050, a 0.8% compound annual growth rate, with substantial commodity variation.
- **S10** — [Port Performance Freight Statistics Program](https://www.bts.gov/ports) (accessed 2026-07-22): Describes nationally consistent port capacity and throughput measures and current datasets covering imports, vessel calls and berthing times, TEUs, tonnage, dry bulk, commodities, and port profiles.
- **S11** — [Water Transportation Workers: Occupational Outlook Handbook](https://www.bls.gov/ooh/transportation-and-material-moving/water-transportation-occupations.htm) (accessed 2026-07-22): Projects water-transportation-worker employment to grow 1% from 2024 to 2034 and identifies bulk-commodity fluctuations as a key employment driver.
