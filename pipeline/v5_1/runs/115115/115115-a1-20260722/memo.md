# 115115 — Farm Labor Contractors and Crew Leaders

*v5.1 Stage 1 research memo. Run `115115-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.35 · L 2.68 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Scarce seasonal labor and expanding H-2A use increase the value of compliant recruiting, crew assembly, payroll, transport, and worker coordination.
**Weakness:** Most cost and work sit in physical field labor, while thin pass-through economics, legal exposure, and unreliable firm-level measurement constrain automation value and acquisition confidence.

## Business-model lens
- Included: Independent U.S. operating companies primarily supplying crews or individual workers for agricultural production or manual harvesting, including recruiting, hiring, dispatch, supervision, payroll, worker transport or housing when authorized, within the specified EBITDA band.
- Excluded: Growers directly employing their own labor, agricultural associations acting only for members, temporary staffing outside agriculture, farm management, machine harvesting, postharvest packing, labor-only sole proprietors without a transferable company, captive affiliates, non-control financing vehicles, and operations without transferable control.
- Customer and revenue model: Recurring fees from farms, orchards, vineyards, nurseries, and agricultural associations for furnished workers or crews, commonly quoted per worker-hour, crew-hour, day, acre, unit harvested, or managed season; customer payments fund worker wages, payroll burden, transport, housing or other pass-through costs, compliance, supervision, and contractor margin.
- Deviation from default lens: The frozen labor-intensity ratio of 2.2759 is economically anomalous: QCEW wages plus the fixed benefit multiplier exceed SUSB receipts by more than two times. Sector-specific coverage, agricultural-production-worker scope, pass-through accounting, establishment classification, and data-vintage differences make that input unsuitable as a literal compensation share, so the automation parameter is anchored to occupational mix and task evidence instead.

## Executive view
Farm labor contractors have meaningful AI opportunity in recruiting, matching, scheduling, translation, payroll, routing, and compliance, but most wages fund physical field workers and the frozen 2.2759 labor-intensity ratio is not economically interpretable. Labor scarcity and H-2A growth support outsourcing even as mechanization limits total worker demand.

## How AI changes the work
AI can accelerate worker intake, document review, multilingual communication, demand forecasting, crew assembly, time and piece-rate reconciliation, payroll, disclosures, authorization checks, vehicle routing, and compliance exception handling. Planting, pruning, harvesting, loading, driving, housing operation, emergency response, and crew supervision remain human and physical.

## Value capture
Reliable fulfillment and fewer errors can protect contractor spread and customer retention, but wages and mandated costs dominate, growers bargain hard, savings may pass through, and competitors can adopt the same workflows.

## Firm availability
Active registration signals a real operating business but not an eligible acquisition target. Certificate holders include employees, exemptions exist, the frozen count is estimated, and independence, EBITDA, transferability, customer concentration, and normalized owner economics remain unknown.

## Demand durability
Mechanization pressures field-worker demand, while chronic scarcity, replacement openings, H-2A growth, seasonal peaks, and regulatory complexity can increase the share outsourced to contractors. A modest five-year increase is plausible but policy and crop exposure make the range wide.

## Risks and uncertainty
Risks include immigration and H-2A policy, wage mandates, joint-employment liability, worker safety, housing and transport compliance, rural connectivity, payroll and piece-rate errors, customer concentration, seasonality, crop losses, mechanization, working capital, and the frozen wage-to-receipts measurement anomaly.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 2.2759 | — | OBSERVED | — |
| n | — | 39 | — | ESTIMATE | — |
| a | 0.07 | 0.13 | 0.21 | PROXY | S2, S5, S6, S10 |
| rho | 0.33 | 0.52 | 0.69 | ESTIMATE | S3, S4, S5, S6 |
| e | 0.28 | 0.48 | 0.66 | ESTIMATE | S1, S3, S4, S10 |
| s5 | 0.11 | 0.23 | 0.38 | PROXY | S3, S9 |
| q | 0.17 | 0.33 | 0.51 | PROXY | S5, S6, S7 |
| d5 | 0.93 | 1.07 | 1.22 | PROXY | S2, S7, S8 |
| o | 0.84 | 0.93 | 0.985 | ESTIMATE | S1, S3, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.10 | 6.15 | 10.00 | ESTIMATE |
| F | 1.27 | 2.68 | 3.82 | ESTIMATE |
| C | 3.40 | 6.60 | 10.00 | PROXY |
| D | 7.81 | 9.95 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupational evidence covers NAICS 115100, not the six-digit contractor industry, and may include machine and technical services with different task mixes.
- a: The frozen wage-to-receipts mismatch likely reflects coverage, accounting, or vintage differences, so it cannot be treated as a feasible labor share.
- rho: Compliance automation can reduce errors without reducing payroll or headcount.
- rho: Capabilities and economics differ sharply between small crew leaders, multistate H-2A labor contractors, transport and housing operators, and harvesting crews.
- e: The public registry is person-and-certificate based and cannot be equated to transferable firms.
- e: The frozen 39-firm count is an estimate and should not be treated as a verified acquisition universe.
- s5: The SBA statistic is an old cross-industry secondary proxy, not a current measured exit rate.
- s5: A contractor certificate, worker network, vehicles, housing rights, and customer contracts may transfer differently or require new approvals.
- q: No public evidence directly measures five-year retention of automation savings by eligible contractors.
- q: Per-hour, piece-rate, per-acre, H-2A, transport, housing, and full-crew contracts have different pass-through behavior.
- d5: H-2A certified positions are not identical to jobs filled or contractor revenue, and employers can use the program directly.
- d5: Occupational projections measure workers across industries, not demand for NAICS 115115 firms.
- o: Direct hiring and agricultural-association exemptions can displace contractors without software becoming the supplier.
- o: A platform may capture recruiting and matching value while a licensed operating entity continues to bear employment and compliance responsibility.

## Sources
- **S1** — [NAICS Definition: 115115 Farm Labor Contractors and Crew Leaders](https://www.census.gov/naics/?details=11&input=115&year=2017) (accessed 2026-07-23): Defines the industry as establishments primarily supplying labor for agricultural production or harvesting and distinguishes machine harvesting and farm management.
- **S2** — [May 2023 Occupational Employment and Wage Estimates: NAICS 115100](https://www.bls.gov/oes/2023/may/naics4_115100.htm) (accessed 2026-07-23): Reports 337,310 workers in broader crop-support activities, including 67.2% farming occupations, 56.1% crop, nursery, and greenhouse farmworkers, and 2.67% management.
- **S3** — [MSPA Registered Farm Labor Contractor Listing](https://www.dol.gov/agencies/whd/agriculture/mspa/farm-labor-contractors) (accessed 2026-07-23): Explains federal certification, the active registry, certificate holders, expirations, and housing, transport, and driving authorizations.
- **S4** — [MSPA Certificate Registration Frequently Asked Questions](https://www.dol.gov/agencies/whd/agriculture/mspa/certificate-registration-resources/faqs) (accessed 2026-07-23): Documents registration requirements for farm labor contractors and employees and the active-certificate listing.
- **S5** — [Fact Sheet #49: Migrant and Seasonal Agricultural Worker Protection Act](https://www.dol.gov/agencies/whd/fact-sheets/49-mspa) (accessed 2026-07-23): Documents contractor registration, payroll records, wage and disclosure duties, proof of registration, and specific transport and housing authorizations.
- **S6** — [Fact Sheet #26: H-2A Temporary Agricultural Workers](https://www.dol.gov/agencies/whd/fact-sheets/26-H2A) (accessed 2026-07-23): Documents employer and H-2A labor-contractor obligations, including recruitment, wages, housing, transport, records, and FLC certificates and authorizations.
- **S7** — [U.S. H-2A Positions Certified by State, Fiscal Years 2005-24](https://ers.usda.gov/data-products/chart-gallery/86844) (accessed 2026-07-23): Reports certified positions increasing more than sevenfold from just over 48,000 in fiscal 2005 to about 385,000 in fiscal 2024 as an indicator of farm-labor scarcity.
- **S8** — [Occupational Outlook Handbook: Agricultural Workers](https://www.bls.gov/ooh/farming-fishing-and-forestry/agricultural-workers.htm) (accessed 2026-07-23): Projects employment down 3% from 2024 to 2034 but about 116,200 annual replacement openings, and describes mechanization as limiting labor demand.
- **S9** — [5 Challenges for Family-Owned Businesses](https://www.sba.gov/blog/5-challenges-family-owned-businesses) (accessed 2026-07-23): Provides a broad succession proxy: 47% of owners expecting retirement within five years reportedly lacked a successor.
- **S10** — [Food and Agricultural Industries: Opportunities for Improving Measurement and Reporting](https://www2.census.gov/ces/wp/2016/CES-WP-16-58.pdf) (accessed 2026-07-23): Explains frame and worker-coverage complications for farm labor contractors, including treatment of agricultural production workers and sole proprietors in Census and BLS data.
