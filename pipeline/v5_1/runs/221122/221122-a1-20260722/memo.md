# 221122 — Electric Power Distribution

*v5.1 Stage 1 research memo. Run `221122-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.92 · L 0.46 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Essential physical-network accountability and durable electricity demand support recurring operator-required service.
**Weakness:** Only a small, poorly measured share of the apparent firm population is likely to be a private, independent, transferable physical distribution operator.

## Business-model lens
- Included: Privately controlled lower-middle-market operators of physical electric distribution systems that repeatedly deliver electricity and related distribution service to external customers.
- Excluded: Publicly managed utilities, member-owned cooperatives without a transferable controlling owner, captive distribution units, generation-only and transmission-only businesses, electricity brokers and agents, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring regulated or contract-based charges to residential, commercial, and industrial customers for electricity delivery and associated distribution service, commonly recovered through approved tariffs and usage-linked charges.
- Deviation from default lens: NAICS 221122 combines physical distribution-system operators with brokers and agents that arrange electricity sales over others' systems. The lens is narrowed to private physical-system operators because the two models have materially different assets, regulation, labor workflows, and transfer mechanics; the narrowing is for coherence rather than attractiveness.

## Executive view
Electric distribution is an essential, recurring infrastructure service with meaningful AI-addressable administrative and analytical work, but the investable population is much narrower than the NAICS firm count suggests. Public ownership, cooperative structures, large-utility subsidiaries, regulation, and broker inclusion make firm-level eligibility and transferability the central diligence problem.

## How AI changes the work
AI is most plausible in customer communications, billing exceptions, meter-data review, outage intake, inspection-image triage, forecasting, work-order preparation, procurement, and regulatory documentation. Field restoration, switching, physical maintenance, and safety-critical control remain human-accountable, and legacy operational technology slows implementation.

## Value capture
Savings are not automatically retained. Regulatory lag and incentive structures may preserve part of the benefit, but rate cases, earnings-sharing rules, contract repricing, and customer scrutiny can pass a substantial share through over the five-year horizon.

## Firm availability
The frozen firm count is a weak guide to actionable targets because the code includes brokers and the utility population includes public entities, cooperatives, captive operations, and subsidiaries. A firm-by-firm match to EIA ownership and state regulatory records is necessary before treating the apparent population as controllable acquisition targets.

## Demand durability
Electricity delivery demand is supported by electrification, data centers, and the persistent need for safe, reliable local networks. Efficiency, distributed generation, storage, and territory-specific demographic changes can constrain delivered volume, but they rarely remove the need for an accountable network operator.

## Risks and uncertainty
The largest uncertainties are eligibility, transaction frequency, state approval, tariff treatment of savings, cybersecurity, operational-technology integration, and the gap between broad-industry occupation data and staffing at small physical distributors. The opportunity would be unattractive if the candidate list resolves mainly to non-transferable entities or if rate mechanisms promptly pass operating savings to customers.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0837 | — | OBSERVED | — |
| n | — | 442 | — | ESTIMATE | — |
| a | 0.2 | 0.3 | 0.41 | PROXY | S2 |
| rho | 0.28 | 0.46 | 0.63 | PROXY | S3 |
| e | 0.04 | 0.12 | 0.25 | ESTIMATE | S1, S4 |
| s5 | 0.08 | 0.16 | 0.28 | ESTIMATE | S4, S6 |
| q | 0.12 | 0.28 | 0.45 | ESTIMATE | S6 |
| d5 | 0.99 | 1.07 | 1.17 | PROXY | S5 |
| o | 0.96 | 0.99 | 0.999 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.19 | 0.46 | 0.86 | PROXY |
| F | 1.42 | 3.62 | 5.57 | ESTIMATE |
| C | 2.40 | 5.60 | 9.00 | ESTIMATE |
| D | 9.50 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation table is for broader NAICS 221100 and May 2023 employment, not the narrowed operator lens.
- a: Employment shares are not wage-weighted task shares and do not reveal what is already automated.
- a: The frozen compensation-to-receipts input has a vintage mismatch and may understate or overstate the relevant labor base for small operators.
- rho: DOE describes opportunities and priorities rather than realized labor implementation.
- rho: Adoption can differ sharply by utility scale, grid condition, data architecture, and state regulatory regime.
- rho: Critical-infrastructure cybersecurity and human-in-the-loop requirements may limit labor removal even when tools are deployed.
- e: No source directly measures the share of frozen LMM firms meeting all lens conditions.
- e: The frozen count is margin-bridged from establishment and receipts data and can misclassify regulated utilities with atypical capital structures or accounting.
- e: EIA's ownership counts describe utilities rather than the Census firm universe used for the frozen count.
- s5: No industry-specific denominator of eligible independent firms and qualifying transfers was found.
- s5: State approval rules and buyer concentration create substantial geographic variation.
- s5: Observed utility M&A can overrepresent large systems and parent-company deals that do not fit the lens.
- q: Retention is jurisdiction-specific and depends on rate-case timing and tariff design.
- q: The cited regulatory structure is directional and not a measurement of retained AI savings.
- q: Competitive retail or contract arrangements can reprice differently from regulated delivery service.
- d5: EIA projections are national scenarios rather than forecasts for small private distribution systems.
- d5: Electricity consumption is not identical to constant-quality distribution-service demand.
- d5: Weather, large-load interconnections, and distributed resources can dominate five-year outcomes in a small territory.
- o: The range is a bounded judgment rather than an observed operator-required share.
- o: The narrowed physical-operator lens mechanically produces higher operator requirement than the broker segment that was excluded.
- o: Rapid adoption of durable behind-the-meter self-supply could lower the share in selected territories.

## Sources
- **S1** — [2022 NAICS 221122: Electric Power Distribution](https://www.census.gov/naics/?details=221122&input=221122&year=2022) (accessed 2026-07-22): Defines the industry as establishments operating electric distribution systems or acting as brokers and agents arranging electricity sales over systems operated by others.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 221100](https://www.bls.gov/oes/2023/may/naics4_221100.htm) (accessed 2026-07-22): Reports 393,880 employees in the broader electric power generation, transmission, and distribution industry, including 34,620 in management, 20,170 in construction and extraction, 44,310 in production, and 32,100 power plant operators, distributors, and dispatchers.
- **S3** — [Last Mile Digitization for Resilience](https://www.energy.gov/sites/default/files/2025-06/Last%20Mile%20Digitization%20for%20Resilience_20250605_Final_Amended.pdf) (accessed 2026-07-22): DOE describes distribution-grid digitization needs and recommends expanded use of artificial intelligence and machine learning for predictive diagnostics and automation; it also identifies the distribution grid as the location of most outages.
- **S4** — [Investor-owned utilities served 72% of U.S. electricity customers in 2017](https://www.eia.gov/todayinenergy/detail.php?id=40913) (accessed 2026-07-22): Reports almost 3,000 U.S. electric distribution companies in 2017 and distinguishes investor-owned, publicly managed, and cooperative ownership; investor-owned utilities served 72% of customers.
- **S5** — [EIA projects growing U.S. electricity demand and capacity through 2050](https://www.eia.gov/pressroom/releases/press587.php) (accessed 2026-07-22): EIA's Annual Energy Outlook 2026 projects average annual U.S. electricity demand growth of 0.9% to 1.6% through 2050 across modeled cases and substantial installed-capacity growth.
- **S6** — [The Changing Structure of the Electric Power Industry: An Update](https://www.eia.gov/electricity/policies/legislation/california/pdf/chg_str_issu.pdf) (accessed 2026-07-22): Describes investor-owned utilities' geographic service monopolies, obligation to serve, state and federal regulation, and approval of rates intended to permit a fair return, supporting the structural discussion of control transfers and benefit pass-through.
