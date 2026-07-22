# 562920 — Materials Recovery Facilities

*v5.1 Stage 1 research memo. Run `562920-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.43 · L 1.64 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Deployable AI vision and robotic sorting can reduce residual manual picking and improve material quality within recurring contracted operations.
**Weakness:** Standalone transferable-firm availability is poorly measured, and automation savings can be absorbed by capital costs, contract repricing, and volatile commodity economics.

## Business-model lens
- Included: US lower-middle-market operators of facilities that repeatedly receive, separate, sort, bale, and market recyclable materials for external municipal, hauler, commercial, or institutional customers.
- Excluded: Captive internal facilities, government operations without transferable control, non-control financing vehicles, shells, waste collection and disposal without a materials-recovery operation, composting, recycling manufacturers, and recyclable-material merchant wholesalers classified in NAICS 423930.
- Customer and revenue model: Revenue commonly combines contracted per-ton processing or tipping fees with commodity-sale proceeds and negotiated revenue sharing. Municipal and hauler agreements may also specify contamination, residue, audit, reporting, and performance terms; some operators may receive producer-responsibility funding.
- Deviation from default lens: none

## Executive view
Materials recovery is a repeat, contract-centered physical service with a credible automation pathway, but the opportunity is inseparable from capital equipment, commodity exposure, and local processing economics. AI can improve sorting and quality control, yet the eligible standalone firm population and actual transfer frequency are uncertain because many facilities are public, captive, vertically integrated, or bundled with broader waste assets.

## How AI changes the work
Machine vision, optical characterization, and robotic picking can reduce repetitive manual sorting, improve consistency, monitor contamination, and make facilities more resilient to labor shortages. Administrative AI can also support reporting and planning. The main constraint is that implementation requires reliable hardware integrated into live lines; maintenance, exception handling, safety, mobile-equipment work, and operator accountability remain.

## Value capture
Processing-fee contracts can preserve savings until renewal, and better recovery or bale quality can create commodity value. Capture can leak through fee resets, competitive rebids, revenue-sharing formulas, performance obligations, contamination provisions, and customer demands for lower rates. Contract structure therefore matters as much as technical savings.

## Firm availability
Recent waste-and-recycling acquisitions show that recycling facilities and MRF-linked contracts are transactible. Availability is harder to infer: transaction news lacks a denominator, many plants belong to municipalities or integrated waste groups, and the frozen firm count may not map cleanly to facilities or sale perimeters.

## Demand durability
The need to receive and sort recyclable material is physically durable, and public targets, grants, and system investment can support throughput. Growth is not assured; commodity weakness, contamination, changing packaging, source reduction, deposit systems, municipal budgets, and recycling participation can reduce demand for the current basket.

## Risks and uncertainty
The largest evidence gaps are MRF-specific wage weights, automation penetration by facility size, the ownership and EBITDA distribution of plants, qualifying control-transfer rates, and representative contract economics. Capital intensity may make a lower-middle-market operator too small to deploy automation economically, while fire and safety risk, equipment downtime, commodity volatility, and residue costs can overwhelm labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2317 | — | OBSERVED | — |
| n | — | 254 | — | ESTIMATE | — |
| a | 0.18 | 0.34 | 0.5 | PROXY | S2, S3, S4, S12 |
| rho | 0.28 | 0.52 | 0.72 | PROXY | S2, S3, S4 |
| e | 0.25 | 0.45 | 0.65 | ESTIMATE | S1, S4, S5 |
| s5 | 0.08 | 0.17 | 0.3 | PROXY | S10, S11 |
| q | 0.3 | 0.5 | 0.7 | ESTIMATE | S4, S5, S6 |
| d5 | 0.88 | 1.05 | 1.22 | PROXY | S7, S8, S9, S13 |
| o | 0.78 | 0.88 | 0.96 | ESTIMATE | S1, S2, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.47 | 1.64 | 3.34 | PROXY |
| F | 2.90 | 4.85 | 6.31 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.86 | 9.24 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source is for all waste management and remediation services, not NAICS 562920.
- a: The national MRF survey is facility-based and has a limited response rate, and neither MRF study publishes a wage-weighted task decomposition.
- a: Automation already installed at larger facilities is excluded conceptually but cannot be measured consistently from the sources.
- rho: Published techno-economic results are not observed adoption rates for the screened population.
- rho: Implementation may replace hard-to-fill positions without reducing current payroll, which would lower realized substitution.
- rho: The range is sensitive to financing availability and whether retrofits require broader line redesign.
- e: No source directly measures eligibility among firms in the frozen lower-middle-market count.
- e: The frozen firm-count estimate may not align with a facility-level industry in which one operator owns multiple MRFs.
- e: Municipal ownership and vertical integration are not quantified in the cited national survey.
- s5: Transaction reporting is selective and covers the broader waste and recycling market.
- s5: Some cited transactions bundle collection, disposal, transfer, or brokerage assets with MRF operations.
- s5: The sources do not measure owner age or succession pressure for independent MRF operators.
- q: No source measures the discounted retained share of implemented gross benefit.
- q: The Phoenix agreement is one municipal contract and may not represent private hauler or commercial arrangements.
- q: Commodity prices can mask operational savings when observed only through total margins.
- d5: BLS does not publish a separate projection for NAICS 562920 and employment is not a direct measure of constant-quality service demand.
- d5: Federal funding announcements and recycling goals do not guarantee facility throughput.
- d5: The current service basket could change as packaging composition and collection rules evolve.
- o: No source directly measures the future share of MRF demand requiring an outsourced accountable operator.
- o: The estimate assumes automation changes the labor and equipment mix more than it eliminates the facility service itself.
- o: Ownership consolidation could preserve total operator-required demand while reducing the share served by lens-eligible firms.

## Sources
- **S1** — [North American Industry Classification System, United States, 2022: NAICS 562920 Materials Recovery Facilities](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines the industry as facilities separating and sorting recyclable materials from nonhazardous waste streams and distinguishes recyclable-material merchant wholesalers.
- **S2** — [Outlook on the future role of robots and artificial intelligence in Materials Recovery Facilities: Implications for the U.S. recycling system and workforce](https://www.sciencedirect.com/science/article/pii/S0959652624026830) (accessed 2026-07-22): Describes AI-enabled composition and contamination estimation, vision-based safety, robotic sorting, expected reductions in human sorting roles, new technical roles, adoption constraints, and possible industry consolidation.
- **S3** — [Techno-economic analysis of a material recovery facility employing robotic sorting technology](https://par.nsf.gov/biblio/10546347-techno-economic-analysis-material-recovery-facility-employing-robotic-sorting-technology) (accessed 2026-07-22): Evaluates AI-vision robotic sorting in a representative US MRF and discusses speed, accuracy, residual reduction, worker-shortage resilience, economics, and uncertainty.
- **S4** — [Materials Recovery Facilities in the United States: Operations, revenue, and the impact of scale](https://www.sciencedirect.com/science/article/abs/pii/S0956053X24006408) (accessed 2026-07-22): Reports a national facility survey covering input streams, process equipment, labor, commodity revenue, residue, scale economies, advanced sorting, and material-market access.
- **S5** — [MRF Contracts](https://recyclingpartnership.org/mrf-contracts/) (accessed 2026-07-22): Identifies municipal MRF contract terms including processing fees, revenue sharing, material value, audits, contamination, performance, rejected loads, residue, and reporting.
- **S6** — [City of Phoenix legislation detail: materials recovery facility processing agreement](https://phoenix.legistar.com/LegislationDetail.aspx?GUID=C7722BA0-9570-4FB0-B77E-3155393066A5&ID=7033103&Options=&Search=) (accessed 2026-07-22): Provides a concrete municipal agreement in which the processing fee is designed to recover costs and net commodity revenue is shared under specified market conditions.
- **S7** — [U.S. National Recycling Goal](https://www.epa.gov/circulareconomy/us-national-recycling-goal) (accessed 2026-07-22): Documents the national recycling goal and the stated need for changes and investment in collection and sorting systems.
- **S8** — [Solid Waste Infrastructure for Recycling Grants for States and Territories](https://www.epa.gov/circulareconomy/solid-waste-infrastructure-recycling-grants-states-and-territories) (accessed 2026-07-22): Documents grants supporting post-consumer materials management, municipal recycling and waste systems, planning, data, and implementation.
- **S9** — [Cleanup, Revitalization and Recycling Investments](https://www.epa.gov/infrastructure/cleanup-revitalization-and-recycling-investments) (accessed 2026-07-22): Documents federal investment in recycling infrastructure and education intended to improve US recycling systems.
- **S10** — [Notable waste and recycling acquisitions of 2025](https://www.wastedive.com/news/2025-notable-waste-and-recycling-acquisitions/808593/) (accessed 2026-07-22): Catalogs recent control transactions in waste and recycling, including acquisitions involving a recycling facility and MRF-related contracts.
- **S11** — [Waste and recycling M&A remains active amid evolving market](https://www.wastedive.com/news/waste-recycling-environmental-services-acquisition-private-equity-outlook/739250/) (accessed 2026-07-22): Describes sustained strategic and private-equity acquisition activity across waste, recycling, and environmental services while noting transaction-market uncertainty.
- **S12** — [Waste Management and Remediation Services - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/May/naics3_562000.htm) (accessed 2026-07-22): Provides the broader subsector occupational distribution, including material-moving, office support, installation and maintenance, and production roles used as an occupation-mix proxy.
- **S13** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects employment for the broader remediation and other waste-management category, used only as a directional demand proxy.
