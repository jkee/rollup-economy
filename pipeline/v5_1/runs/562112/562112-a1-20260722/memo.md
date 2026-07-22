# 562112 — Hazardous Waste Collection

*v5.1 Stage 1 research memo. Run `562112-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.30 · L 2.54 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Regulated recurring pickups create automatable routing and compliance administration around a service whose physical execution remains necessary.
**Weakness:** Most labor is tied to vehicles, material movement, and safety-critical field work, while firm availability and transferability are supported only by broad proxies and estimates.

## Business-model lens
- Included: US lower-middle-market firms that repeatedly collect or haul hazardous waste for external customers, prepare or package it for transport, or operate hazardous-waste transfer stations.
- Excluded: Captive in-house waste teams, long-distance waste trucking classified outside 562112, integrated treatment-and-disposal operators, one-off emergency-only practices without repeat outsourced service, shells, and non-control financing vehicles.
- Customer and revenue model: Industrial, automotive, healthcare, institutional, commercial, and public-sector generators buy scheduled pickups, containerized-waste programs, transfer services, and occasional project or emergency work; charges commonly reflect waste volume, materials, labor, transportation, and other fees under service agreements or purchase orders.
- Deviation from default lens: none

## Executive view
Hazardous-waste collection is a route, fleet, and field-labor business with a smaller but consequential layer of documentation, dispatch, quoting, billing, and compliance work. AI can improve that layer, while regulation and physical custody preserve demand for trained accountable operators. The most attractive operating cases would have recurring pickup density, disciplined safety records, transferable permits, and standardized customer and manifest data.

## How AI changes the work
AI can assist route planning, pickup scheduling, quote preparation, customer communication, manifest checks, waste-profile review, exception detection, billing support, training content, and regulatory research. Driving, packaging, labeling, sampling, loading, equipment operation, spill response, and custody signatures remain physical or safety-critical, and generated classifications or documents require expert verification.

## Value capture
Retention is mixed. Waste-volume, labor, materials, transportation, and time-based charges can pass productivity gains to customers at renewal or rebid, while recurring service charges, route density, compliance capability, switching friction, and specialized waste knowledge support partial retention. Fuel, disposal, and mandated fees should be separated from true operating productivity.

## Firm availability
The code is naturally external service, and recurring collection programs can transfer with routes, trained crews, customer contracts, equipment, and permits. Eligibility falls for emergency-only work, poor compliance histories, concentration in one generator or facility, nonassignable approvals, aging fleets, and owner-held technical or customer relationships. Broad owner intentions and observed waste-business sales show a market, but neither measures qualifying 562112 transfers.

## Demand durability
Regulated off-site hazardous-waste movement, chain-of-custody requirements, industrial activity, and the physical need to move waste support durable service. Growth appears modest rather than exceptional: waste minimization, manufacturing cycles, insourcing, and uneven cleanup funding offset emerging contaminants, decommissioning, tighter tracking, and new waste streams.

## Risks and uncertainty
Key uncertainties are the absence of a 562112 occupational mix, unknown LMM billing shares, permit and insurance transferability, customer concentration, AI error liability, environmental indemnities, vehicle and worker safety, disposal-capacity dependence, and the margin-bridged firm count. A severe incident, regulatory violation, lost disposal outlet, or hidden remediation obligation can overwhelm administrative savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5997 | — | OBSERVED | — |
| n | — | 82 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.33 | PROXY | S2, S5 |
| rho | 0.28 | 0.46 | 0.63 | PROXY | S3, S5 |
| e | 0.5 | 0.68 | 0.82 | ESTIMATE | S1, S4 |
| s5 | 0.08 | 0.14 | 0.22 | PROXY | S6, S7 |
| q | 0.34 | 0.52 | 0.7 | PROXY | S4 |
| d5 | 0.9 | 1.02 | 1.13 | PROXY | S4, S8 |
| o | 0.8 | 0.9 | 0.96 | PROXY | S3, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.94 | 2.54 | 4.99 | PROXY |
| F | 2.34 | 3.50 | 4.44 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | PROXY |
| D | 7.20 | 9.18 | 10.00 | PROXY |

## Caveats
- a: OEWS is published for NAICS 562100 rather than 562112 and includes employers of all sizes.
- a: Employment shares are not wage-weighted task shares, and the hazardous segment likely uses more technical and compliance labor than broad waste collection.
- a: The frozen labor ratio uses 2024 wages over 2022 receipts and is harmonized by a cross-industry adjustment.
- rho: BTOS measures AI use across all employer industries rather than implementation of the exposed opportunity in hazardous-waste collection.
- rho: EPA's e-Manifest system digitizes records but does not itself establish AI use or labor substitution.
- rho: Safety, environmental liability, customer systems, and state-specific rules may make implementation slower and more review-intensive than ordinary administrative automation.
- e: No source measures the share of 562112 LMM firms satisfying every lens condition.
- e: Clean Harbors is a large integrated operator and may have more recurring service, systems, and management depth than LMM collection firms.
- e: The frozen firm count is margin-bridged and does not observe firm-level EBITDA-band membership.
- s5: Gallup covers all US employer businesses and reports intentions rather than completed transactions.
- s5: BizBuySell combines waste management and recycling businesses, is voluntary, and is concentrated below the full LMM band.
- s5: Environmental indemnities, permit continuity, and fleet condition may cause signed processes to fail before control transfer.
- q: The filing describes one large integrated operator and does not report billing-model shares for 562112 LMM firms.
- q: Contract clauses, public procurement, disposal pass-throughs, fuel surcharges, and competitive bidding may transmit gains differently.
- q: The estimate excludes demand loss and implementation friction, which are assigned to d5, o, and rho.
- d5: Occupational employment is not constant-price outsourced collection demand.
- d5: Clean Harbors revenue includes pricing, acquisitions, disposal, remediation, and other environmental services.
- d5: Industrial production, environmental policy, waste minimization, spills, disasters, and plant closures can move demand sharply within five years.
- o: Current regulatory and occupational duties do not directly measure the year-five operator-required share.
- o: The line between collection, transfer, treatment, brokerage, and software-enabled compliance may shift as providers bundle services.
- o: Federal rules coexist with state requirements, so self-service and outsourcing feasibility vary geographically and by waste type.

## Sources
- **S1** — [NAICS Sector 56 Definitions: 562112 Hazardous Waste Collection](https://www.census.gov/naics/resources/archives/sect56.html) (accessed 2026-07-22): Defines 562112 as local hazardous-waste collection or hauling and hazardous-waste transfer-station operation, potentially including identification, treatment, packaging, and labeling for transport, while excluding long-distance trucking and combined collection-disposal operations.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 562100 Waste Collection](https://www.bls.gov/oes/2023/may/naics4_562100.htm) (accessed 2026-07-22): Reports 208,430 jobs in broader waste collection, with transportation and material moving at 67.93%, heavy truck drivers 23.07%, office support 10.94%, management 4.54%, sales 2.25%, and business and financial operations 1.84%.
- **S3** — [Hazardous Waste Manifest System](https://www.epa.gov/hwgenerators/hazardous-waste-manifest-system) (accessed 2026-07-22): Explains cradle-to-grave shipment tracking, required type and quantity information, handling instructions, signatures and retained copies for each handler, receiving confirmation, and optional electronic manifest creation and submission.
- **S4** — [Clean Harbors, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/822818/000082281826000009/clh-20251231.htm) (accessed 2026-07-22): Describes recurring collection-related service, short-term projects under long-term master service agreements, customer prices based on waste volume, materials, personnel, transportation and other fees, 3.8% Environmental Services revenue growth in 2025, and higher used-oil collection pricing during the year.
- **S5** — [The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html) (accessed 2026-07-22): Reports 18% firm use of AI in a business function, 23% worker-task use, limited functional breadth among adopters, leading use in writing, document analysis and information search, 66% augmentation-only use, and employment decreases in 2% of firms.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 52.3% of US employer businesses are owned by people age 55 or older and 22% of employer-business owners planned to sell or transfer ownership within five years.
- **S7** — [Business Acquisitions Stabilize as Buyers Get Selective: AI and Cost Discipline Drive 2026 Playbook](https://www.bizbuysell.com/news/bizbuysell-2025-fourth-quarter-insight-report/) (accessed 2026-07-22): Reports flat overall 2025 small-business transaction volume, 4% service-sector growth, and 43 completed waste-management and recycling business transactions in its annual table.
- **S8** — [Occupational Outlook Handbook: Hazardous Materials Removal Workers](https://www.bls.gov/ooh/construction-and-extraction/hazardous-materials-removal-workers.htm) (accessed 2026-07-22): Documents physical and regulated duties including testing, packaging, transporting, recordkeeping, safety procedures and training, and projects 1% employment growth from 2024 to 2034 while noting persistent cleanup need and sporadic funding.
