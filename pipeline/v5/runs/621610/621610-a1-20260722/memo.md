# 621610 — Home Health Care Services

*v5 Stage 1 research memo. Run `621610-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.98 · L 3.43 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable, growing need for accountable in-home care paired with administrative workflow burden.
**Weakness:** AI addresses a limited portion of a predominantly hands-on workforce and value capture is constrained by payer and regulatory dynamics.

## Business-model lens
- Included: US lower-middle-market home health agencies that provide recurring skilled nursing, therapy, aide, care-coordination, and related in-home services to external patients or payer-funded customers.
- Excluded: Captive health-system units, shell entities, internal staffing departments, entities without control-transferable operations, and financing vehicles.
- Customer and revenue model: Recurring episodes, visits, and care plans paid principally by government and commercial health plans, patients, or their representatives; Medicare-certified services are commonly reimbursed through a case-mix and wage-adjusted 30-day bundle.
- Deviation from default lens: none

## Executive view
Home health combines a large, labor-intensive direct-care workforce with recurring regulated service delivery. AI is more likely to improve agency administration and coordination than to replace in-home care.

## How AI changes the work
Aides dominate industry employment and perform hands-on, interpersonal work. The practical opportunity is concentrated in documentation preparation, scheduling, intake, authorizations, coding support, communications, and coordination, with clinical review retained.

## Value capture
Medicare generally pays a standardized, case-mix and wage-adjusted 30-day bundle, which can preserve some agency productivity gains. Annual rate changes, payer negotiation, regulated documentation, and labor competition make that retention uncertain.

## Firm availability
The supplied LMM count is an estimate. A general small-business transaction market exists, but clean financials, payer credentials, compliance history, management depth, and low owner dependence are central to whether an agency can transfer.

## Demand durability
BLS projects 17% growth in the broad aide occupation from 2024 to 2034, citing aging and a shift toward home- and community-based care. Regulated HHAs must retain an accountable governing body, administrator, and clinical manager.

## Risks and uncertainty
The biggest unknowns are payer mix, state-level Medicaid rules, staffing scarcity, certification and quality exposure, EHR fragmentation, and the absence of direct evidence on AI adoption, realized savings, and LMM agency transfer rates. Occupational growth is only a proxy for industry service demand.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6718 | — | OBSERVED | — |
| n | — | 1983 | — | ESTIMATE | — |
| a | 0.18 | 0.29 | 0.42 | ESTIMATE | S1, S2 |
| rho | 0.28 | 0.44 | 0.6 | ESTIMATE | S3, S5 |
| e | 0.7 | 0.82 | 0.9 | ESTIMATE | S5 |
| s5 | 0.07 | 0.12 | 0.19 | ESTIMATE | S6, S7 |
| q | 0.35 | 0.54 | 0.7 | ESTIMATE | S3, S4 |
| d5 | 1 | 1.08 | 1.16 | PROXY | S2 |
| o | 0.88 | 0.94 | 0.98 | PROXY | S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.35 | 3.43 | 6.77 | ESTIMATE |
| F | 7.38 | 8.49 | 9.38 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.80 | 10.00 | 10.00 | PROXY |

## Caveats
- a: The published 58.14% is employment share, not wage share, and is from 2023.
- a: The occupation table does not measure AI-susceptible task time or distinguish agency-specific workflow maturity.
- rho: No source measures realized five-year AI implementation for 621610 firms.
- rho: Medicare-certified HHA regulations do not cover every non-Medicare service in the NAICS code.
- e: The supplied firm-band count is an estimate and does not identify captive status, transferability, or certification.
- e: No published source was found that measures lens eligibility for 621610 LMM firms.
- s5: BizBuySell reports marketplace transactions, listings, and broker sentiment rather than an industry-specific transfer rate.
- s5: The cited SBA owner-retirement research uses older 1992-2010 panel data and small-business owners generally.
- q: Medicare PPS is not the revenue model for all 621610 services or payers.
- q: No source provides the discounted five-year operator-retention share of AI benefit.
- d5: This is an occupational, national ten-year projection, not an industry-specific five-year real-demand forecast.
- d5: Employment growth can differ from service quantity because staffing intensity and productivity change.
- o: The regulation applies to Medicare-certified HHAs and does not prove future operator need for every service or payer in NAICS 621610.
- o: The estimate does not model changes in benefit design or family-provided care.

## Sources
- **S1** — [BLS Occupational Employment and Wage Statistics: Home Health and Personal Care Aides, May 2023](https://www.bls.gov/oes/2023/May/oes311120.htm) (accessed 2026-07-22): Reports 931,330 home health and personal care aides in Home Health Care Services, equal to 58.14% of industry employment, with a 15.44 dollar mean hourly wage and 32,120 dollar annual mean wage.
- **S2** — [BLS Occupational Outlook Handbook: Home Health and Personal Care Aides](https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm) (accessed 2026-07-22): Describes hands-on aide duties, reports a 17% projected employment increase from 2024 to 2034, and attributes demand to older people and a shift toward home- and community-based settings.
- **S3** — [CMS Medicare Payment Systems: Home Health Prospective Payment System](https://www.cms.gov/outreach-and-education/medicare-learning-network-mln/mlnproducts/html/medicare-payment-systems.html) (accessed 2026-07-22): States that Medicare pays HHAs a national standardized 30-day bundled rate, adjusted for case mix and geographic wage differences, and that the HHA bills covered services.
- **S4** — [CMS CY 2025 Home Health Prospective Payment System Final Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2025-home-health-prospective-payment-system-final-rule-fact-sheet-cms-1803-f) (accessed 2026-07-22): Reports a permanent negative 1.975% adjustment to the CY 2025 home health payment rate related to implementation of the Patient-Driven Groupings Model.
- **S5** — [42 CFR 484.105: Organization and Administration of Home Health Services](https://ecfr.io/Title-42/Section-484.105) (accessed 2026-07-22): Requires an HHA governing body, an administrator responsible for daily operations, clinical-manager oversight of patient care and personnel, and HHA responsibility for services furnished under arrangement.
- **S6** — [BizBuySell Insight Report: Q2 2026 Business-for-Sale Market](https://www.bizbuysell.com/insight-report/) (accessed 2026-07-22): Reports 2,117 businesses changed hands in Q2 2026; service businesses accounted for 40% of transactions, and the report describes buyer interest in recurring-revenue healthcare-related services while emphasizing selectivity.
- **S7** — [SBA Office of Advocacy: Retirement, Recessions, and Older Small Business Owners](https://advocacy.sba.gov/wp-content/uploads/2019/05/Retirement-Recessions-and-Older-Small-Business-Owners-Summary.pdf) (accessed 2026-07-22): The older small-business-owner study reports that owners in 2010 expected to retire at age 72.6 on average, versus 68.4 for employees, supporting uncertainty around retirement-driven exits.
