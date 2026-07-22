# 621391 — Offices of Podiatrists

*v5.1 Stage 1 research memo. Run `621391-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.82 · L 1.77 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat, information-heavy clinical workflows offer administrative AI leverage while physical foot care preserves an accountable operator role.
**Weakness:** Most direct clinical labor is hands-on and licensed, while the eligible transaction pool is small and practices may depend heavily on producing owners.

## Business-model lens
- Included: Lower-middle-market independent podiatry practices providing recurring or repeat diagnosis and treatment of foot, ankle, and lower-leg conditions to external patients, including examinations, imaging review, diabetic foot care, wound care, routine procedures, surgery, orthotics-related clinical work, and follow-up care in offices or facilities of others.
- Excluded: Hospital-owned or other captive departments, physician practices classified outside 621391, product-only footwear or durable-medical-equipment sellers, nonclinical foot-care businesses, shells, and non-control financing vehicles.
- Customer and revenue model: Practices receive fee-for-service, contracted payer, Medicare or Medicaid, and patient cash payments for visits, diagnostics, procedures, surgery, supplies, and follow-up care; chronic disease and post-procedure cases create repeat utilization while reimbursement is commonly tied to coded clinical services.
- Deviation from default lens: none

## Executive view
Podiatry has a durable hands-on clinical core and repeat demand from chronic and mobility-related conditions, but only a minority of wage-bearing work appears directly substitutable. The clearest AI opportunity is in documentation, intake, billing, scheduling, patient communication, and clinical preparation rather than autonomous treatment.

## How AI changes the work
AI can summarize histories and records, draft notes and instructions, assist coding and prior authorization, route messages, support imaging or risk review, and automate administrative follow-up. Licensed clinicians and supervised teams remain necessary for physical examination, diagnosis, procedures, surgery, wound care, device fitting, and accountable treatment decisions.

## Value capture
Fee-for-service and cash-pay practices may retain administrative productivity because payment is not usually tied directly to staff hours. Payer fee schedules, software costs, compliance, competition, and the tendency to convert saved time into more capacity or better service limit cash retention.

## Firm availability
Independent group practices can be transferable when referrals, payer participation, clinician teams, systems, and management are institutionalized. Small supply in the frozen LMM band, founder production, credentialing, facility relationships, and clinician retention constrain qualifying transfers.

## Demand durability
Aging and chronic disease support continuing foot-care need, but projected podiatrist employment growth is modest and other caregivers can handle some services. Physical procedures and complex diabetic or surgical care are more durable than routine education, monitoring, and administrative contacts.

## Risks and uncertainty
Key uncertainties are clinical case mix, payer mix, owner production, referral concentration, clinician recruitment, reimbursement, AI integration, privacy, liability, and whether time savings release labor or merely expand capacity. Poor clinical outputs, documentation errors, coding mistakes, or privacy failures can create patient harm and regulatory or payer exposure.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3912 | — | OBSERVED | — |
| n | — | 25 | — | ESTIMATE | — |
| a | 0.18 | 0.28 | 0.4 | PROXY | S2, S4 |
| rho | 0.42 | 0.6 | 0.78 | PROXY | S4 |
| e | 0.62 | 0.8 | 0.92 | ESTIMATE | S1 |
| s5 | 0.05 | 0.1 | 0.17 | PROXY | S5 |
| q | 0.3 | 0.5 | 0.68 | ESTIMATE | — |
| d5 | 0.91 | 1.01 | 1.12 | PROXY | S3, S6 |
| o | 0.78 | 0.88 | 0.95 | PROXY | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.18 | 2.63 | 4.88 | PROXY |
| F | 0.92 | 1.77 | 2.56 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.10 | 8.89 | 10.00 | PROXY |

## Caveats
- a: O*NET provides task descriptions rather than time or wage weights for NAICS 621391 practices.
- a: The AMA survey covers physicians broadly and does not isolate podiatrists or independent lower-middle-market practices.
- a: Clinical case mix varies between routine office care, diabetic wound care, orthotics, and surgery.
- rho: The AMA result is self-reported physician use or awareness, not verified end-to-end implementation or realized labor savings.
- rho: Podiatry-specific adoption may differ from the physician sample because of practice size and procedural workflow.
- rho: Privacy, safety, efficacy, liability, and training constraints can delay clinical uses more than administrative uses.
- e: The Census definition establishes industry scope but does not measure eligibility among LMM firms.
- e: The frozen firm count is margin-bridged and may misclassify practices with unusually high clinician compensation, owner add-backs, or ancillary revenue.
- e: A practice can be independently classified yet remain economically inseparable from a founder or facility relationship.
- s5: Gallup is cross-industry and not restricted to healthcare or the lower-middle market.
- s5: The survey measures owner intentions rather than completed qualifying transactions.
- s5: No cited source measures podiatry practice deal frequency or transfer completion.
- q: No public source measures the share of AI-enabled gross benefit retained by independent podiatry practices.
- q: Retention differs between Medicare-heavy, commercial insurance, cash-pay, and facility-based practices.
- q: The estimate excludes demand displacement and implementation failure, which belong in d5, o, and rho.
- d5: Occupational employment is not a direct measure of constant-price service demand or independent-practice revenue.
- d5: CDC disease-burden evidence supports need but not the paid volume captured by LMM podiatry firms.
- d5: Payer policy, scope-of-practice changes, and substitution by physicians or other caregivers may change demand independently of disease prevalence.
- o: The sources describe occupations and broad outlook rather than direct buyer substitution in independent podiatry practices.
- o: Routine nail care, education, screening, wound care, surgery, and complex diabetic care have very different operator requirements.
- o: Operator-required does not necessarily mean the same practitioner type; some care can shift to another licensed provider.

## Sources
- **S1** — [2022 NAICS Sector 62 Definitions: Offices of Podiatrists](https://www.census.gov/naics/resources/archives/sect62.html) (accessed 2026-07-22): Defines 621391 as independent D.P. practices diagnosing and treating diseases and deformities of the foot in offices or facilities of others.
- **S2** — [O*NET OnLine: Podiatrists](https://www.onetonline.org/link/summary/29-1081.00) (accessed 2026-07-22): Describes podiatrist tasks including physical treatment, diagnosis from histories, examinations, imaging and tests, patient advice, surgery, device work, and medical-record maintenance.
- **S3** — [Occupational Outlook Handbook: Podiatrists](https://www.bls.gov/ooh/healthcare/podiatrists.htm) (accessed 2026-07-22): Projects podiatrist employment to grow 2 percent from 2024 to 2034; cites aging and chronic disease as demand supports and substitution by other caregivers as a limit.
- **S4** — [AMA 2026 Physician Survey on Augmented Intelligence](https://www.ama-assn.org/system/files/physician-ai-sentiment-report.pdf/) (accessed 2026-07-22): Reports AI use and awareness among U.S. physicians, leading documentation and summarization use cases, and adoption constraints involving privacy, safety, efficacy, liability, and training.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of U.S. employer-business owners planned to sell or transfer ownership within five years and describes the survey population.
- **S6** — [CDC: Promoting Foot Health](https://www.cdc.gov/diabetes/hcp/clinical-guidance/diabetes-podiatrist-health.html) (accessed 2026-07-22): Describes podiatrists' role in diabetic foot care, recommends recurring foot examinations, and reports that about 12 percent of people with diabetes develop diabetic foot ulcers during their lifetime.
