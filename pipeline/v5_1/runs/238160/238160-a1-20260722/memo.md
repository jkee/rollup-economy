# 238160 — Roofing Contractors

*v5.1 Stage 1 research memo. Run `238160-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.54 · L 0.94 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A measurable office, estimating, business, and sales layer can use AI to increase quote and job throughput amid persistent construction hiring difficulty.
**Weakness:** Most industry employment is hands-on construction, limiting wage-weighted substitution and leaving realized savings dependent on disciplined workflow integration.

## Business-model lens
- Included: US lower-middle-market contractors installing, replacing, repairing, coating, inspecting, and maintaining residential, commercial, and institutional roof systems for external customers, including firms whose recurring activity is a sequence of projects, storm-restoration jobs, maintenance calls, and reroofing work.
- Excluded: Roofing-material manufacturing or distribution without contracting, captive owner or general-contractor crews, solar installation without roofing responsibility, shells, non-control financing vehicles, and businesses lacking a transferable operating organization.
- Customer and revenue model: Revenue comes from fixed-price bids, negotiated commercial contracts, unit-priced work, insurance-funded residential restoration, service and maintenance agreements, and time-and-material repairs for homeowners, property managers, general contractors, institutions, and commercial building owners.
- Deviation from default lens: none

## Executive view
Roofing is a large, repeat outsourced service where AI can improve the information and coordination layer but not replace most field production. Six-digit occupation data show that the majority of employment remains construction work, while a meaningful office, estimating, management, and sales layer creates a bounded opportunity to avoid hiring and increase throughput.

## How AI changes the work
AI can support aerial-image and plan takeoff, estimating, lead qualification, proposal and insurance-document drafting, contract review, procurement comparison, crew scheduling, daily logs, invoicing, collections, and customer updates. Roof inspection, scope validation, safe setup, material handling, installation, waterproofing, repair, and final accountability remain human-led.

## Value capture
Fixed-price jobs let operators retain improvements during the contract, and response speed can matter in storm or leak events. Competitive bidding, insurer price visibility, customer procurement, and adoption by peers should transfer a significant share of benefits to customers over five years.

## Firm availability
The supplied LMM population is sizable, and most scaled roofing contractors should have transferable organizations. Eligibility is reduced by owner-centric sales, transient subcontracting models, storm-normalized earnings risk, safety history, customer concentration, and weak operating controls; broad employer-owner data imply a real but smaller completed-transfer pool than stated intentions.

## Demand durability
Repair and replacement of the installed roof stock underpin demand even when new construction slows. BLS expects roofer employment to grow through 2034, while the reroofing survey shows meaningful short-term dispersion and cyclicality rather than uniformly rising volume.

## Risks and uncertainty
Major uncertainties include uneven AI adoption, task exposure within mixed field-office roles, output errors in scopes or claims, integration and training cost, insurance and storm volatility, subcontractor dependence, safety liability, material-price swings, and the lack of roofing-specific closed-deal probabilities. A bad case combines low field adoption, rapid competitive pass-through, weak storm-normalized earnings, and owner dependence.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2772 | — | ESTIMATE | — |
| n | — | 216 | — | ESTIMATE | — |
| a | 0.1 | 0.17 | 0.25 | PROXY | S1, S2 |
| rho | 0.32 | 0.5 | 0.68 | PROXY | S3, S4, S5 |
| e | 0.62 | 0.76 | 0.88 | ESTIMATE | S1, S7 |
| s5 | 0.09 | 0.15 | 0.21 | PROXY | S6 |
| q | 0.38 | 0.55 | 0.72 | ESTIMATE | — |
| d5 | 0.96 | 1.03 | 1.11 | PROXY | S7, S8 |
| o | 0.94 | 0.98 | 0.995 | ESTIMATE | S2, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.35 | 0.94 | 1.88 | ESTIMATE |
| F | 4.13 | 5.22 | 5.97 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 9.02 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The OEWS table is from May 2023 and covers employers of all sizes, not only the LMM lens.
- a: Occupation categories do not reveal what portion of each job is already automated or newly AI-exposed.
- a: Sales representatives often perform physical inspections, and managers may perform field supervision, reducing exposure relative to their occupational titles.
- rho: Survey belief, research, evaluation, or budget allocation is not operational implementation.
- rho: The underlying respondent frames differ and are not limited to US LMM roofing contractors.
- rho: Accuracy failures in measurements, scopes, contracts, and claims can erase labor savings or create liability.
- e: The supplied LMM firm count is margin-bridged and estimated rather than directly observed.
- e: Residential, storm-restoration, and commercial roofing have different transferability and revenue quality.
- e: The broad lens includes repeat project revenue even when formal recurring contracts are absent.
- s5: Gallup covers all US employer businesses rather than roofing contractors or the LMM EBITDA band.
- s5: Survey plans may not become completed transactions.
- s5: Closures, minority investments, internal reorganizations, and nontransferable owner exits are excluded.
- q: No roofing-specific study was found measuring pass-through of AI-enabled labor savings.
- q: Insurance restoration, retail replacement, commercial bids, and maintenance contracts have materially different price transparency.
- q: Demand effects and implementation costs are intentionally excluded from this primitive.
- d5: Occupational employment is not constant-price, constant-quality roofing service demand.
- d5: The BLS projection is national and ten-year rather than five-year.
- d5: The reroofing survey is US and Canada, self-selected, and reports one year-over-year quarter rather than a structural forecast.
- d5: The supplied compensation ratio mixes 2024 wages with 2022 receipts.
- o: The range is judgmental and future robotics adoption is uncertain.
- o: Simple inspections and measurements can shift away from contractors without eliminating installation accountability.
- o: Residential and commercial roof systems differ in amenability to standardization and automation.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Roofing Contractors](https://www.bls.gov/oes/2023/may/naics5_238160.htm) (accessed 2026-07-22): Measures 238,300 employees in NAICS 238160 and its occupation mix and wages, including 69.04% construction/extraction, 11.20% office/administrative, 6.94% management, 5.52% business/financial, 4.01% sales, 50.33% roofers, and 2.69% cost estimators.
- **S2** — [O*NET OnLine: Roofers](https://www.onetonline.org/link/details/47-2181.00) (accessed 2026-07-22): Documents roofer tasks including inspection, estimating labor and materials, scaffolding, cutting, installation, repair, coating, insulation, ventilation, and waterproofing, showing the mix of cognitive and physical work.
- **S3** — [Contractors show optimism regarding AI, but concerns remain](https://www.nrca.net/RoofingNews/contractors-show-optimism-regarding-ai-but-concerns-remain.12-16-2025.13079/Details/Story) (accessed 2026-07-22): Reports Dodge survey results from 235 US general and trade contractors: 51% evaluating AI changes, 40% allocating AI budget, 57% concerned about reliability or accuracy, 54% about security and privacy, and 49% of smaller firms about cost.
- **S4** — [Only 8% of U.S. construction professionals use AI on the job](https://www.nrca.net/RoofingNews/only-8-of-u-s--construction-professionals-use-ai-on-the-job-.5-12-2026.13305/Details/Story) (accessed 2026-07-22): Reports DEWALT survey results that 8% of US construction professionals currently use AI on the job, 90% expect it to be indispensable within five years, 37% are piloting or researching it, and job-relevant training is the primary barrier.
- **S5** — [AGC/NCCER 2025 Craft Workforce Survey](https://www.nccer.org/research/2025-workforce-survey-agc-nccer/) (accessed 2026-07-22): Reports that 92% of nearly 1,400 construction firms had difficulty hiring for open positions, supporting the incentive to avoid incremental hiring.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of US employer-business owners planned to sell or transfer ownership within five years, versus 9% of nonemployers, and distinguishes transfer plans from closure or no plan.
- **S7** — [Occupational Outlook Handbook: Roofers](https://www.bls.gov/ooh/construction-and-extraction/roofers.htm) (accessed 2026-07-22): Reports 166,700 roofer jobs in 2024, projected 176,500 in 2034, 6% growth, and demand from replacement, repair, new roofs, and some rooftop solar installation.
- **S8** — [Trade Association Coalition Announces Q2 Findings from Market Index Survey for Reroofing](https://www.nrca.net/RoofingNews/trade-association-coalition-announces-q2-findings--from-market-index-survey-for-reroofing.8-1-2025.12865/details/story) (accessed 2026-07-22): Reports Q2 2025 reroofing results: 34% of roofing contractors saw installed volume increase year over year, 28% no change, and 38% a decrease; also reports inquiry, contract, and backlog dispersion.
