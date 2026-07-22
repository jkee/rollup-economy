# 561422 — Telemarketing Bureaus and Other Contact Centers

*v5 Stage 1 research memo. Run `561422-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 5.66 · L 4.66 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Large portions of routine contact handling can be redesigned around AI while keeping human escalation and accountability.
**Weakness:** Automation can remove the contacts and FTEs that outsourced operators bill for, while compliance and client approval constrain implementation.

## Business-model lens
- Included: US contact-center operators that provide recurring inbound customer care, outbound sales, collections, appointment, order, or related voice/contact services to external clients, and whose normalized EBITDA is in the lower-middle-market band.
- Excluded: Captive client service departments, one-off staffing placements, software-only vendors, shell entities, and non-control financing vehicles.
- Customer and revenue model: An outsourced operator delivers recurring client programs, commonly with fees tied to minutes, hours, FTEs, transactions, or calls.
- Deviation from default lens: none

## Executive view
This is a labor-intensive outsourced-service category with clear AI applicability, but the same automation that improves delivery can reduce the billable contact volume on which operators are paid. The investment case depends on preserving complex, compliant client programs rather than relying on simple-call volume.

## How AI changes the work
AI can assist or replace routine information, order, record, billing, routing, and scripted-sales tasks described for customer-service representatives. Human oversight remains important for exceptions, complaint resolution, client-specific knowledge, quality, conversion, and regulated communications. S2, S3, and S5 support these boundaries.

## Value capture
Comparable BPO contracts are commonly priced per minute, hour, FTE, transaction, or call, so an operator may retain efficiency initially but faces direct renewal repricing and lower-volume pressure. Contract review is the decisive diligence item. S4.

## Firm availability
The code is generally aligned with third-party contact services, although its public establishment data do not reveal normalized EBITDA, captive status, customer concentration, or transferability. A verified firm and transaction census is needed before treating the injected count as an acquisition pipeline. S1 and S6.

## Demand durability
BLS projects a decline in customer-service representative employment as self-service and digital channels take simple tasks, while noting continuing demand for more complex inquiries. That is an imperfect but directionally relevant warning for the current service basket. S2.

## Risks and uncertainty
Client concentration, insecure or poor-quality automation, conversion loss, and regulation are material. The FTC requires disclosures, consent, do-not-call controls, and records for covered telemarketing, which can slow deployment and raise failure costs. The most uncertain inputs are qualifying-sale probability and the share of future work still requiring an outsourced operator. S5.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5817 | — | OBSERVED | — |
| n | — | 201 | — | ESTIMATE | — |
| a | 0.4 | 0.55 | 0.7 | ESTIMATE | S2, S3 |
| rho | 0.3 | 0.45 | 0.6 | ESTIMATE | S2, S5 |
| e | 0.55 | 0.72 | 0.85 | ESTIMATE | S1, S6 |
| s5 | 0.1 | 0.17 | 0.27 | ESTIMATE | — |
| q | 0.2 | 0.35 | 0.5 | ESTIMATE | S4 |
| d5 | 0.82 | 0.97 | 1.08 | PROXY | S2 |
| o | 0.3 | 0.48 | 0.65 | ESTIMATE | S2, S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.79 | 5.76 | 9.77 | ESTIMATE |
| F | 4.00 | 5.22 | 6.20 | ESTIMATE |
| C | 4.00 | 7.00 | 10.00 | ESTIMATE |
| D | 2.46 | 4.66 | 7.02 | ESTIMATE |

## Caveats
- a: BLS measures the customer-service occupation across employers, not the wage mix of the LMM outsourced-contact-center lens.
- a: The NAICS code includes inbound and outbound programs with materially different task complexity.
- rho: No industry-wide observed implementation rate exists for the frozen lens.
- rho: The estimate excludes revenue and pricing effects by construction.
- e: Eligibility is not a Census or BLS field.
- e: The injected firm-count estimate may include firms whose EBITDA, ownership, or client model cannot be determined from public data.
- s5: No authoritative observed control-transfer rate is published for eligible US LMM firms in this six-digit code.
- s5: Transaction databases can omit small asset deals and cannot alone distinguish qualifying control transfers from reorganizations.
- q: S4 is a global public-company comparable, not a direct sample of US LMM firms.
- q: The retained share varies sharply by client concentration, program criticality, and whether automation reduces billed volume or internal cost.
- d5: Employment is not constant-quality service quantity and spans employers outside NAICS 561422.
- d5: The BLS forecast horizon begins in 2024 rather than the packet run date.
- o: No source measures the future operator-required share for this lens.
- o: Outbound consumer telemarketing and inbound customer care face different substitution and regulatory paths.

## Sources
- **S1** — [North American Industry Classification System, 2022: NAICS 561422](https://www.census.gov/naics/?input=561422&year=2022) (accessed 2026-07-22): Industry identity and classification context for Telemarketing Bureaus and Other Contact Centers.
- **S2** — [BLS Occupational Outlook Handbook: Customer Service Representatives](https://www.bls.gov/ooh/office-and-administrative-support/customer-service-representatives.htm) (accessed 2026-07-22): Observed 2024 employment of 2,814,000 and projected 2034 employment of 2,660,300 for customer service representatives, plus task, call-center, and self-service context.
- **S3** — [O*NET Job Duties Custom List: Customer Service Representatives](https://www.onetonline.org/search/task/choose/43-4051.00) (accessed 2026-07-22): Observed occupation task list covering information provision, orders, records, billing, complaints, account actions, and additional sales.
- **S4** — [TTEC Holdings 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1013880/000155837025001823/ttec-20241231x10k.htm) (accessed 2026-07-22): Comparable BPO disclosure that inbound and outbound service fees are commonly priced per minute, hour, FTE, transaction, or call.
- **S5** — [FTC: Complying with the Telemarketing Sales Rule](https://www.ftc.gov/business-guidance/resources/complying-telemarketing-sales-rule) (accessed 2026-07-22): Telemarketing requirements concerning disclosures, consent, do-not-call procedures, recordkeeping, and potential penalties.
- **S6** — [Census 2022 Statistics of U.S. Businesses Annual Data Tables by Establishment Industry](https://www.census.gov/data/tables/2022/econ/susb/2022-susb-annual.html) (accessed 2026-07-22): Availability and coverage of firm, establishment, employment, payroll, receipts, and establishment-size data by six-digit NAICS.
