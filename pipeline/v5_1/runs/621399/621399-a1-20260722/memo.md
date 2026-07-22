# 621399 — Offices of All Other Miscellaneous Health Practitioners

*v5.1 Stage 1 research memo. Run `621399-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 6.42 · L 4.28 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Information-heavy counseling and administration coexist with repeat patient relationships across a potentially broad pool of scaled practitioner firms.
**Weakness:** The code's extreme modality heterogeneity makes average automation, demand, retention, and transfer assumptions fragile without firm-level mix data.

## Business-model lens
- Included: Lower-middle-market independent practices providing recurring or repeat health services to external patients under NAICS 621399, including offices of acupuncturists, dental hygienists, denturists, dietitians, homeopaths, hypnotherapists, inhalation or respiratory therapists, midwives, naturopaths, and registered or licensed practical nurses.
- Excluded: Practices separately classified as physicians, dentists, chiropractors, optometrists, mental health specialists, physical or occupational therapists, speech therapists, audiologists, or podiatrists; hospital-owned or other captive departments; product-only retailers; shells; and non-control financing vehicles.
- Customer and revenue model: Practices receive patient cash, commercial insurance, Medicare or Medicaid where covered, employer or institutional contract, per-visit, per-procedure, package, membership, and care-management payments; economics vary sharply between reimbursed licensed care and cash-pay wellness-oriented services.
- Deviation from default lens: none

## Executive view
NAICS 621399 combines diverse nonphysician practices, so its opportunity is driven more by firm mix than by a single operating model. AI can materially streamline documentation, intake, education, care-plan preparation, billing, and communication, while hands-on and licensed care remains comparatively durable.

## How AI changes the work
AI can summarize histories and evidence, draft notes and personalized education, prepare care plans for review, assist coding and claims, automate scheduling and follow-up, translate communications, and support routine monitoring. Physical treatment, examinations, childbirth, emergency response, individualized diagnosis, and accountable clinical decisions still require practitioners.

## Value capture
Cash-pay and package-based firms may retain productivity longer than tightly reimbursed practices, while payer fee schedules and institutional customers limit pricing freedom. Vendor costs, competition, compliance, and conversion of saved time into added capacity rather than payroll reduction reduce realized retention.

## Firm availability
The frozen firm count suggests meaningful scale, but eligibility and transferability vary widely. Multi-practitioner firms with institutionalized referrals, records, billing, and management are more transferable than owner-branded or license-dependent solo practices.

## Demand durability
Preventive care, chronic disease, aging, and expanding nonphysician care support demand in nutrition and nursing-related segments. Discretionary wellness services are more cyclical, and generic education or monitoring faces self-service and software substitution.

## Risks and uncertainty
The largest uncertainty is the unobserved mix of modalities, payer models, and owner dependence. State scope rules, reimbursement, clinician supply, referral concentration, privacy, safety, liability, unsupported clinical claims, and inconsistent evidence standards can materially alter both automation feasibility and demand.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.54 | — | OBSERVED | — |
| n | — | 284 | — | ESTIMATE | — |
| a | 0.22 | 0.36 | 0.52 | PROXY | S2, S3, S6 |
| rho | 0.35 | 0.55 | 0.72 | PROXY | S6 |
| e | 0.48 | 0.68 | 0.84 | ESTIMATE | S1 |
| s5 | 0.04 | 0.1 | 0.18 | PROXY | S7 |
| q | 0.25 | 0.45 | 0.68 | ESTIMATE | — |
| d5 | 0.88 | 1.05 | 1.22 | PROXY | S4, S5 |
| o | 0.55 | 0.72 | 0.87 | PROXY | S2, S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.66 | 4.28 | 8.09 | PROXY |
| F | 3.00 | 4.84 | 6.09 | ESTIMATE |
| C | 5.00 | 9.00 | 10.00 | ESTIMATE |
| D | 4.84 | 7.56 | 10.00 | PROXY |

## Caveats
- a: No cited source measures the occupation or wage mix within NAICS 621399 firms.
- a: Dietitian and acupuncturist tasks do not represent every included modality.
- a: The AMA physician survey is a broad adoption proxy and may not represent nonphysician independent practices.
- rho: AMA adoption is self-reported and does not verify reliable deployment or labor release.
- rho: Physician workflows and resources differ from the nonphysician practitioner mix in this code.
- rho: Implementation will vary materially between regulated clinical care and cash-pay wellness practices.
- e: The Census definition demonstrates extreme modality heterogeneity but does not measure LMM eligibility.
- e: The frozen firm count is margin-bridged using a broad provider margin and may misclassify cash-pay, product-heavy, labor-intensive, or owner-compensated practices.
- e: Independent legal status does not ensure transferable operations or recurring revenue.
- s5: Gallup is cross-industry and not restricted to healthcare or the lower-middle market.
- s5: The survey measures intended sale or transfer rather than completed qualifying control events.
- s5: No cited source measures transaction frequency for NAICS 621399 or its component modalities.
- q: No public source measures contract mix or retained automation benefit for this heterogeneous code.
- q: Retention may be much higher in differentiated cash-pay practices than in payer-dependent nursing or clinical services.
- q: Implementation difficulty and service displacement are excluded here and represented in rho, d5, and o.
- d5: Occupation projections are not direct measures of constant-price demand for independent 621399 firms.
- d5: Dietitians and nurse midwives represent only part of the code and their shares are unknown.
- d5: Discretionary wellness demand, payer coverage, state scope rules, and substitution can differ sharply across modalities.
- o: The evidence covers selected occupations rather than the full revenue-weighted 621399 basket.
- o: Operator requirement differs substantially between childbirth, respiratory care, dental hygiene, acupuncture, nutrition counseling, and wellness services.
- o: Some demand may persist but shift to a different provider type, integrated setting, or software-enabled channel.

## Sources
- **S1** — [2022 NAICS Sector 62 Definitions: Offices of All Other Miscellaneous Health Practitioners](https://www.census.gov/naics/resources/archives/sect62.html) (accessed 2026-07-22): Defines 621399 and lists included examples such as acupuncturists, dental hygienists, denturists, dietitians, hypnotherapists, respiratory therapists, midwives, naturopaths, and registered or licensed practical nurses.
- **S2** — [O*NET OnLine: Dietitians and Nutritionists](https://www.onetonline.org/link/summary/29-1031.00) (accessed 2026-07-22): Lists nutritional assessment, laboratory-test evaluation, individualized planning, counseling, education, coordination, and patient-history record tasks.
- **S3** — [O*NET OnLine: Acupuncturists](https://www.onetonline.org/link/details/29-1291.00) (accessed 2026-07-22): Lists medical-history collection, diagnosis, patient education, care-record maintenance, outcome evaluation, and hands-on acupuncture and related treatment tasks.
- **S4** — [Occupational Outlook Handbook: Dietitians and Nutritionists](https://www.bls.gov/ooh/healthcare/dietitians-and-nutritionists.htm) (accessed 2026-07-22): Projects employment to grow 6 percent from 2024 to 2034 and attributes demand to preventive care, chronic disease, and population aging.
- **S5** — [Occupational Outlook Handbook: Nurse Anesthetists, Nurse Midwives, and Nurse Practitioners](https://www.bls.gov/ooh/healthcare/nurse-anesthetists-nurse-midwives-and-nurse-practitioners.htm) (accessed 2026-07-22): Describes advanced nursing and midwifery tasks and projects nurse-midwife employment to grow 11 percent from 2024 to 2034.
- **S6** — [AMA 2026 Physician Survey on Augmented Intelligence](https://www.ama-assn.org/system/files/physician-ai-sentiment-report.pdf/) (accessed 2026-07-22): Reports physician AI use and awareness, documentation and summarization use cases, and adoption considerations involving privacy, safety, efficacy, liability, and training.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of U.S. employer-business owners planned to sell or transfer ownership within five years and describes the survey population.
