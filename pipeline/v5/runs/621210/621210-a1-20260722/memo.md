# 621210 — Offices of Dentists

*v5 Stage 1 research memo. Run `621210-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.72 · L 1.80 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat patient care with automateable front-office and revenue-cycle workflows around a still-human clinical core.
**Weakness:** The strongest transfer and automation inputs are proxies or bounded estimates rather than NAICS-specific realized data.

## Business-model lens
- Included: Independent and group dental offices that provide recurring preventive, diagnostic, restorative, surgical, orthodontic, or specialty dental care directly to external patients, and their practice-management activities.
- Excluded: Captive dental units, internal corporate clinics, shell entities, non-control financing vehicles, and businesses that only sell software, laboratories, equipment, or staffing to dental offices.
- Customer and revenue model: Patient-care practices paid per visit or procedure by patients and third-party dental benefit plans, with repeat preventive and continuing-care appointments.
- Deviation from default lens: none

## Executive view
Dental offices combine recurring patient care with a substantial administrative layer, but the economically central clinical work remains hands-on and clinician-accountable. The case depends on operational improvement around access, scheduling, documentation, and revenue-cycle workflow rather than substitution of dentists or hygienists.

## How AI changes the work
Likely uses include patient communication, appointment recovery, eligibility and claim workflow, note preparation, coding support, call handling, and image-review assistance. The estimated labor opportunity is deliberately limited because examination, diagnosis, consent, treatment, and patient trust require human clinical responsibility.

## Value capture
Per-visit and per-procedure billing can let an operator retain part of a productivity gain, but insurer fee schedules and local price competition limit retention. The observed gap in 2022 dental visits among covered and uncovered older adults, 69.6% versus 56.4%, illustrates that payment coverage shapes care use (S4).

## Firm availability
Potential transfer supply is supported only indirectly. ADA reports 15.5% of professionally active dentists were at least 65 in 2024 and an average retirement age of 68.7 (S2), but that does not identify LMM owners, sale timing, or whether an operation transfers rather than closes. DSO affiliation reached 16% of dentists in 2024 (S3), so ownership and buyer pathways are evolving.

## Demand durability
BLS projects dentist employment to grow 4% between 2024 and 2034, citing older people retaining teeth and needs for restorative and other care (S1). That is an imperfect proxy for office service volume, but it supports modest rather than disappearing demand. Software may shift the administrative boundary while leaving a high share of service delivery operator-required.

## Risks and uncertainty
None of the retrieved sources measures NAICS-specific task exposure, implementation realization, retained automation value, or LMM control-transfer frequency. Payer mix, state ownership rules, specialty mix, staff shortages, and practice-management-system interoperability can move outcomes substantially. Direct diligence should prioritize payroll-task mapping, payer contracts, workflow logs, and broker or lender transaction data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4536 | — | OBSERVED | — |
| n | — | 369 | — | ESTIMATE | — |
| a | 0.12 | 0.18 | 0.28 | ESTIMATE | — |
| rho | 0.4 | 0.55 | 0.7 | ESTIMATE | — |
| e | 0.72 | 0.82 | 0.9 | ESTIMATE | S3 |
| s5 | 0.07 | 0.11 | 0.17 | PROXY | S2 |
| q | 0.5 | 0.62 | 0.74 | ESTIMATE | S4 |
| d5 | 1 | 1.02 | 1.04 | PROXY | S1 |
| o | 0.85 | 0.92 | 0.97 | ESTIMATE | S1 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.87 | 1.80 | 3.56 | ESTIMATE |
| F | 4.79 | 5.69 | 6.52 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.50 | 9.38 | 10.00 | ESTIMATE |

## Caveats
- a: No retrieved source measures wage-weighted, not-yet-automated task exposure for dental offices.
- a: The frozen compensation ratio includes owner-clinician and nonclinical labor differently from a task-based payroll sample.
- rho: No retrieved survey measures five-year implementation of the defined exposure opportunity.
- rho: Adoption and realization can differ materially between small single-site offices and multi-site groups.
- e: The 16% figure is a dentist affiliation measure, not a share of LMM firms or eligible control transfers.
- e: State dental-practice ownership rules can affect transfer structure without making patient demand ineligible.
- s5: Age is for dentists, not firm owners, and does not observe transactions.
- s5: The source is national and is not restricted to the supplied EBITDA band.
- q: The cited coverage statistics measure utilization, not pass-through or the retained share of automation benefits.
- q: Fee-for-service, PPO, Medicaid, and specialty practices can retain value differently.
- d5: The projection covers the dentist occupation across all employing industries, not NAICS 621210 output.
- d5: Employment is not a direct measure of constant-quality service quantity.
- o: The BLS forecast does not directly measure the operator-required share of dental-office output.
- o: The estimate assumes the current service basket and excludes a redesign toward software-only oral-health products.

## Sources
- **S1** — [Dentists: Occupational Outlook Handbook](https://www.bls.gov/ooh/healthcare/dentists.htm) (accessed 2026-07-22): BLS reports dentist employment of 149,300 in 2024 and 155,200 projected in 2034, a 4% increase, and attributes expected demand to older people retaining teeth and other dental-care needs.
- **S2** — [Dentist Workforce](https://www.ada.org/resources/research/health-policy-institute/dentist-workforce) (accessed 2026-07-22): ADA reports 202,485 professionally active dentists in 2024; 18.7% were ages 55-64, 15.5% were age 65 or older, and the average retirement age was 68.7.
- **S3** — [Dental Practice Research](https://www.ada.org/resources/research/health-policy-institute/dental-practice-research) (accessed 2026-07-22): ADA reports that 16% of U.S. dentists were affiliated with a dental support organization in 2024 and that there were 135,665 dental practice establishments in the United States in the latest cited data.
- **S4** — [Dental Care Among Adults Age 65 and Older: United States, 2022](https://www.cdc.gov/nchs/products/databriefs/db500.htm) (accessed 2026-07-22): CDC reports that 63.7% of adults age 65 and older had a dental visit in 2022; the rate was 69.6% with dental coverage and 56.4% without coverage.
