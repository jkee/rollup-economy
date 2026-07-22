# 238210 — Electrical Contractors and Other Wiring Installation Contractors

*v5.1 Stage 1 research memo. Run `238210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.29 · L 1.09 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Scarce skilled labor and a large repeat physical-service base create value for AI that removes estimating, coordination, and administrative bottlenecks without trying to replace field electricians.
**Weakness:** Only a modest wage share is directly AI-exposed, and contract repricing or time-based billing can transfer a substantial portion of implemented savings to customers.

## Business-model lens
- Included: US lower-middle-market electrical and other wiring contractors providing installation, additions, alterations, modernization, maintenance, repair, low-voltage, controls, alarm, communications, and related outsourced field services to residential, commercial, industrial, institutional, infrastructure, and public customers.
- Excluded: Captive in-house electrical departments, labor-only shells without transferable operations, non-control financing vehicles, product manufacturers or distributors without a contracting operation, electric utilities, and firms outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: External customers buy project installations and retrofits, repair calls, maintenance/service contracts, and work under master service agreements. Pricing spans fixed-price and unit-price bids, time-and-materials or time-and-equipment billing, and cost-plus arrangements.
- Deviation from default lens: none

## Executive view
Electrical contracting remains a predominantly physical, locally executed service with a meaningful but bounded digital-workflow opportunity. The strongest operational case is reducing office and coordination load around a scarce field workforce, while the main commercial constraint is that time-based and cost-plus billing plus periodic rebidding return part of those gains to customers.

## How AI changes the work
AI is most useful around estimating support, plan and specification review, proposals, change orders, scheduling, dispatch, purchasing, customer communication, accounting, and project reporting. It can also assist field diagnosis and code lookup, but the occupation mix and O*NET task set show that installation, testing, repair, supervision, and physical safety remain the core of the work.

## Value capture
Fixed-price, unit-price, and flat-rate work can retain workflow savings until competitive bids or renewals reset price. Time-and-materials and cost-plus work exposes reduced labor hours more directly, and shared-savings clauses can make pass-through explicit. Capture therefore depends on contract mix, service differentiation, local capacity constraints, and how quickly customers rebid.

## Firm availability
The 2026 contractor survey shows an aging owner and manager population, and BizBuySell records an active market in electrical and mechanical contractor businesses. Availability is nevertheless uncertain because public deal data lack a denominator, mix adjacent trades, and often cover businesses smaller than the target band; license dependence, owner relationships, and normalized owner replacement costs can also make apparent firms nontransferable.

## Demand durability
Repair, replacement, modernization, power-system additions, controls, communications, alternative-energy connections, and charging infrastructure support the service basket. BLS projects electrician employment growth, while the latest contractor survey shows near-term softness and a mix that remains exposed to construction cycles. Software should change how jobs are prepared and administered more than whether a qualified operator is required on site.

## Risks and uncertainty
The biggest evidence gaps are measured task time, realized AI deployment outcomes, LMM contract mix, and closed-transfer rates with a valid eligible-firm denominator. A poor acquisition would be a highly owner-dependent project contractor with concentrated general-contractor relationships, weak change-order discipline, little service work, a nontransferable qualifying license, dirty job-cost data, and predominantly pass-through billing. Construction cyclicality, material and labor volatility, safety liability, cyber risk, and state-by-state licensing add further uncertainty.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3902 | — | ESTIMATE | — |
| n | — | 1050 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.22 | PROXY | S1, S2, S3 |
| rho | 0.3 | 0.5 | 0.7 | ESTIMATE | S2, S3, S4 |
| e | 0.55 | 0.72 | 0.86 | PROXY | S4, S8 |
| s5 | 0.12 | 0.23 | 0.36 | PROXY | S4, S5 |
| q | 0.38 | 0.57 | 0.74 | PROXY | S4, S6 |
| d5 | 0.98 | 1.04 | 1.1 | PROXY | S4, S7, S8 |
| o | 0.86 | 0.94 | 0.98 | PROXY | S2, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.37 | 1.09 | 2.40 | ESTIMATE |
| F | 6.84 | 8.31 | 9.31 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | PROXY |
| D | 8.43 | 9.78 | 10.00 | PROXY |

## Caveats
- a: The May 2023 OEWS mix includes employers of all sizes and does not isolate the LMM band.
- a: Task exposure is assigned from occupation and task descriptions, not directly measured in electrical contractors.
- a: Anthropic usage and survey evidence under-represents construction and extraction occupations and is not a representative workforce survey.
- rho: No source measures five-year AI implementation for this industry and firm-size band.
- rho: The estimate excludes physical robotics and assumes commercially available software can integrate with contractor ERP, field-service, and document systems.
- rho: The contractor survey is subscriber-based and unweighted, so its labor-shortage rates may not represent the full NAICS population.
- e: The dataset-provided firm count is an estimate at the 23821 ancestor level and may not match six-digit 238210 exactly.
- e: The 2026 profile covers magazine subscribers across firm sizes rather than a probability sample of LMM firms.
- e: Eligibility can be state-specific because licensing and qualifying-party rules differ.
- s5: Survey respondents are not identical to owners, even though owners and top managers are the majority.
- s5: BizBuySell is voluntarily reported, includes mechanical contractors, and skews toward smaller Main Street deals below the target EBITDA band.
- s5: The range excludes closures, minority recapitalizations, and internal reorganizations unless a qualifying control transfer occurs.
- q: MYR is much larger than the screened firms and serves utility and large commercial/industrial customers.
- q: Contract label alone does not reveal competitive intensity, change-order recovery, service-call minimums, or the timing of repricing.
- q: The range concerns retention of implemented gross benefit, not implementation success, demand growth, or valuation.
- d5: The BLS projection is national, occupation-based, and ten-year rather than a five-year industry demand forecast.
- d5: Policy changes affecting solar, wind, EVs, efficiency, and public infrastructure could move demand materially.
- d5: The current service basket is heterogeneous and more cyclical in new construction than in repair and maintenance.
- o: The estimate does not assume current licensing rules are identical across states or remain unchanged.
- o: Low-voltage, home-automation, and communications work may face more self-installation and software substitution than power wiring.
- o: Operator-required demand can persist even if fewer labor hours are needed per job; that labor efficiency belongs in the labor primitives, not here.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 238210](https://www.bls.gov/oes/2023/may/naics5_238210.htm) (accessed 2026-07-22): Industry occupation and wage mix: 1,045,300 total employment; construction and extraction 65.92%, including electricians 48.69%; installation, maintenance, and repair 8.08%; office and administrative support 8.39%; management 5.45%.
- **S2** — [O*NET Online: Electricians 47-2111.00](https://www.onetonline.org/link/result/47-2111.00?c=tk) (accessed 2026-07-22): Core electrician tasks include placing conduit and pulling cable, working from ladders or scaffolds, using power and test equipment, installing and testing wiring, diagnosis, inspection, repair, code compliance, sketches, estimates, and business records.
- **S3** — [Anthropic Economic Index report: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report) (accessed 2026-07-22): Defines observed and theoretical occupational task exposure, reports that physical construction and extraction occupations are under-represented in its survey and Claude usage, and warns theoretical exposure is an upper bound while its user survey is not workforce-representative.
- **S4** — [2026 Profile of the Electrical Contractor](https://www.ecmag.com/magazine/articles/article-detail/2026-profile-of-the-electrical-contractor) (accessed 2026-07-22): Survey of 926 electrical contractors: average respondent age 59; smaller-firm respondents average 60.8; 70% are owners/top managers; 56% report difficulty finding trained workers and 27% retaining them; 2025 revenue mix was 31.7% new construction and 39.7% maintenance/service/repair, including 9.1% maintenance/service contracts.
- **S5** — [Electrical & Mechanical Contractor Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/electrical-mechanical-contractor/) (accessed 2026-07-22): Reports 266 analyzed electrical and mechanical contractor listings/sales for 2021-2025, with $1,724,323 median revenue and $385,902 median owner earnings, and identifies the population as mainly locally owned service and contracting businesses.
- **S6** — [MYR Group Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/700923/000070092326000007/myrg-20251231.htm) (accessed 2026-07-22): Describes fixed-price, unit-price, time-and-equipment, time-and-materials, cost-plus, shared-savings, and master service agreements; fixed-price contracts were 57.0% of 2025 revenue, with higher margin upside and cost-overrun risk than time-based and cost-plus contracts.
- **S7** — [Occupational Outlook Handbook: Electricians](https://www.bls.gov/ooh/construction-and-extraction/electricians.htm) (accessed 2026-07-22): Projects electrician employment to grow 9% from 2024 to 2034, from 818,700 to 896,100, and attributes need to installation and replacement of building power systems plus alternative generation connections.
- **S8** — [2022 NAICS Definition: 238210 Electrical Contractors and Other Wiring Installation Contractors](https://www.census.gov/naics/?details=238210&input=238210&year=2022) (accessed 2026-07-22): Defines the industry as establishments installing and servicing electrical wiring and equipment, including new work, additions, alterations, maintenance, and repairs across power, lighting, alarm, automation, telecom, network cable, and related wiring.
