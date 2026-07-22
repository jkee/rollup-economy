# 621491 — HMO Medical Centers

*v5.1 Stage 1 research memo. Run `621491-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.30 · L 0.10 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The principal driver is the combination of a high labor share with integrated plan-provider data that can automate administrative work and augment repeat outpatient workflows.
**Weakness:** The principal weakness is structural eligibility: NAICS 621491 centers are HMO-owned, so very few may be standalone transferable businesses under the default roll-up lens.

## Business-model lens
- Included: HMO-owned medical centers with physicians and other medical staff providing recurring primary or specialized outpatient care to HMO subscribers, where the integrated HMO-provider enterprise or a separable licensed care-delivery platform is a transferable going concern in the lower-middle-market EBITDA band.
- Excluded: Independent physician, dental, or other practitioner groups merely contracting with prepaid plans; carrier-only underwriting and administration; hospitals; nonseparable captive locations that cannot be acquired as a control business; shells; and operations outside the lower-middle-market band.
- Customer and revenue model: Subscribers receive outpatient care through an HMO-owned delivery system funded from premiums, capitation, internal medical budgets, and sometimes service-level reimbursements. Revenue is recurring with enrollment, while care delivery is governed by network, quality, access, and medical-loss-ratio economics.
- Deviation from default lens: none

## Executive view
HMO medical centers offer meaningful administrative and clinical-support automation, but the industry definition itself creates a severe acquisition-eligibility problem: the centers are HMO-owned and may be inseparable from regulated insurance operations. The operating thesis is therefore narrower than a conventional physician-practice roll-up and depends on finding a transferable integrated or carve-out platform.

## How AI changes the work
AI can reduce work in scheduling, intake, chart preparation, coding, claims support, message routing, care-gap outreach, documentation, referral coordination, and population-health prioritization. Examination, diagnosis, prescribing, treatment, safeguarding, and consequential patient decisions remain licensed human responsibilities with audited decision support.

## Value capture
Integrated premium or capitation economics can preserve near-term cost savings, but competitive premiums, medical-loss-ratio rules, benefit commitments, provider compensation, compliance, and technology reinvestment pass much of the gain back to subscribers, purchasers, clinicians, or regulators over time.

## Firm availability
Availability is the central constraint. Census says these establishments are owned by the HMO, so many are captive assets rather than independent targets; qualifying opportunities require an entire small HMO-provider enterprise or a genuinely separable care-delivery platform with transferable contracts, licenses, staff, and subscriber access.

## Demand durability
Outpatient primary and chronic care are durable, and broad outpatient real output is projected to grow. Demand for this exact format is less certain because HMOs may use contracted physician networks or virtual channels instead of owned centers, and current Medicare Advantage enrollment evidence is stable rather than strongly growing.

## Risks and uncertainty
Major risks are misclassification of captive assets as eligible firms, insurance and provider change-of-control approvals, medical-loss-ratio pass-through, payer concentration, adverse selection, coding and risk-adjustment scrutiny, model bias or unsafe recommendations, privacy and cybersecurity, clinician resistance, and shifts from owned centers to contracted networks.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.7833 | — | OBSERVED | — |
| n | — | 4 | — | ESTIMATE | — |
| a | 0.24 | 0.36 | 0.49 | PROXY | S2, S3, S4, S5 |
| rho | 0.32 | 0.52 | 0.7 | PROXY | S3, S4, S5, S6 |
| e | 0.05 | 0.2 | 0.42 | ESTIMATE | S1, S8 |
| s5 | 0.03 | 0.08 | 0.16 | PROXY | S1, S9 |
| q | 0.22 | 0.38 | 0.55 | ESTIMATE | S8 |
| d5 | 0.9 | 1.06 | 1.2 | PROXY | S7, S10 |
| o | 0.55 | 0.72 | 0.88 | ESTIMATE | S1, S3, S4, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.41 | 5.87 | 10.00 | PROXY |
| F | 0.01 | 0.10 | 0.38 | ESTIMATE |
| C | 4.40 | 7.60 | 10.00 | ESTIMATE |
| D | 4.95 | 7.63 | 10.00 | ESTIMATE |

## Caveats
- a: BLS publishes the occupational mix at broad NAICS 621400, which also includes dialysis, surgery, emergency, and other outpatient centers.
- a: O*NET describes occupations nationally and does not measure current automation or wage-weighted task time inside HMO medical centers.
- rho: HTI-1 establishes health-IT transparency and interoperability conditions, not measured labor realization.
- rho: No 621491-specific adoption, error-rate, or staffing study was found.
- e: The frozen n estimate uses provider-margin bridging even though Census includes integrated insurer-provider establishments.
- e: No national measure of separable, control-acquirable HMO medical-center firms in the target EBITDA band was found.
- s5: Gallup intentions are not industry-specific and include transfers that may not be arm's-length control sales.
- s5: The tiny estimated firm population makes realized availability highly discrete.
- q: The 85% MLR rule directly covers Medicare Advantage and related CMS plan contracts, not every commercial or Medicaid HMO arrangement.
- q: No evidence directly measures the durable share of clinic automation benefits retained by target-band HMO owners.
- d5: NAICS 621400 includes several faster- or slower-growing outpatient models unrelated to HMO medical centers.
- d5: Medicare Advantage is only one HMO market and enrollment does not map one-for-one to visits at owned centers.
- o: No observed five-year rate of owned-center bypass or virtual substitution was found.
- o: The estimate distinguishes continued need for medical care from continued need for an HMO-owned medical-center operator.

## Sources
- **S1** — [U.S. Census Bureau NAICS Sector 62 definitions: 621491 HMO Medical Centers](https://www.census.gov/naics/resources/archives/sect62.html) (accessed 2026-07-22): Industry boundary, HMO ownership, included integrated underwriting-provider establishments, and cross-reference to independently contracting practitioners.
- **S2** — [BLS May 2023 OEWS: NAICS 621400 Outpatient Care Centers](https://www.bls.gov/oes/2023/may/naics4_621400.htm) (accessed 2026-07-22): Broad outpatient occupational mix, including 15.71% office and administrative support, 15.39% registered nurses, 6.63% medical assistants, and 4.70% medical secretaries.
- **S3** — [O*NET OnLine: Registered Nurses](https://www.onetonline.org/link/summary/29-1141.00) (accessed 2026-07-22): Clinical assessment, care planning, medical-record, medication, education, and case-management tasks used to separate digital support from embodied licensed care.
- **S4** — [O*NET OnLine: Medical Assistants](https://www.onetonline.org/link/summary/31-9092.00) (accessed 2026-07-22): Administrative and clinical task mix including scheduling, records, billing, coding, intake, vital signs, specimens, and medication support.
- **S5** — [O*NET OnLine: Medical Secretaries and Administrative Assistants](https://www.onetonline.org/link/summary/43-6013.00) (accessed 2026-07-22): Scheduling, billing, chart, report, correspondence, message-routing, and medical-record workflows used for task exposure.
- **S6** — [ASTP/ONC HTI-1 Final Rule overview](https://healthit.gov/regulations/hti-rules/hti-1-final-rule/) (accessed 2026-07-22): Certified-health-IT interoperability and algorithm-transparency requirements, including fairness, appropriateness, validity, effectiveness, and safety assessment.
- **S7** — [CMS: Medicare Advantage and Medicare Prescription Drug Programs Expected to Remain Stable in 2026](https://www.cms.gov/newsroom/press-releases/medicare-advantage-medicare-prescription-drug-programs-expected-remain-stable-2026) (accessed 2026-07-22): CMS projection of 34.0 million Medicare Advantage enrollees in 2026 versus 34.9 million in 2025 and its expectation of broadly stable enrollment.
- **S8** — [CMS Medical Loss Ratio](https://www.cms.gov/medicare/health-drug-plans/medical-loss-ratio) (accessed 2026-07-22): Medicare Advantage minimum 85% medical-loss-ratio requirement and sanctions or remittance for noncompliance, used for eligibility and retention constraints.
- **S9** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry benchmark that 22% of employer-business owners planned to sell or transfer ownership within five years.
- **S10** — [BLS Employment Projections: Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Broad NAICS 621400 real-output projection from 217.8 to 307.4 billion chained 2017 dollars, a 3.5% annual rate for 2024-2034.
